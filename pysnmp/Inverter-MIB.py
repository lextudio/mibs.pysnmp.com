# SNMP MIB module (Inverter-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Inverter-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:34 2024
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

argus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PwrSysInv_ObjectIdentity = ObjectIdentity
pwrSysInv = _PwrSysInv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 10)
)


class _PwrInvCount_Type(Integer32):
    """Custom type pwrInvCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PwrInvCount_Type.__name__ = "Integer32"
_PwrInvCount_Object = MibScalar
pwrInvCount = _PwrInvCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 1),
    _PwrInvCount_Type()
)
pwrInvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrInvCount.setStatus("current")
_TsiModules_ObjectIdentity = ObjectIdentity
tsiModules = _TsiModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5)
)


class _TsiModulesCount_Type(Integer32):
    """Custom type tsiModulesCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiModulesCount_Type.__name__ = "Integer32"
_TsiModulesCount_Object = MibScalar
tsiModulesCount = _TsiModulesCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 1),
    _TsiModulesCount_Type()
)
tsiModulesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModulesCount.setStatus("current")
_TsiModulesTable_Object = MibTable
tsiModulesTable = _TsiModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5)
)
if mibBuilder.loadTexts:
    tsiModulesTable.setStatus("current")
_TsiModulesEntry_Object = MibTableRow
tsiModulesEntry = _TsiModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1)
)
tsiModulesEntry.setIndexNames(
    (0, "Inverter-MIB", "tsiModulesIndex"),
)
if mibBuilder.loadTexts:
    tsiModulesEntry.setStatus("current")


class _TsiModulesIndex_Type(Integer32):
    """Custom type tsiModulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiModulesIndex_Type.__name__ = "Integer32"
_TsiModulesIndex_Object = MibTableColumn
tsiModulesIndex = _TsiModulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 1),
    _TsiModulesIndex_Type()
)
tsiModulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModulesIndex.setStatus("current")


class _TsiStatusACOut_Type(Integer32):
    """Custom type tsiStatusACOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiStatusACOut_Type.__name__ = "Integer32"
_TsiStatusACOut_Object = MibTableColumn
tsiStatusACOut = _TsiStatusACOut_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 2),
    _TsiStatusACOut_Type()
)
tsiStatusACOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiStatusACOut.setStatus("current")


class _TsiStatusACIn_Type(Integer32):
    """Custom type tsiStatusACIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiStatusACIn_Type.__name__ = "Integer32"
_TsiStatusACIn_Object = MibTableColumn
tsiStatusACIn = _TsiStatusACIn_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 3),
    _TsiStatusACIn_Type()
)
tsiStatusACIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiStatusACIn.setStatus("current")


class _TsiStatusDCIn_Type(Integer32):
    """Custom type tsiStatusDCIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiStatusDCIn_Type.__name__ = "Integer32"
_TsiStatusDCIn_Object = MibTableColumn
tsiStatusDCIn = _TsiStatusDCIn_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 4),
    _TsiStatusDCIn_Type()
)
tsiStatusDCIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiStatusDCIn.setStatus("current")


class _TsiAddress_Type(Integer32):
    """Custom type tsiAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiAddress_Type.__name__ = "Integer32"
_TsiAddress_Object = MibTableColumn
tsiAddress = _TsiAddress_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 5),
    _TsiAddress_Type()
)
tsiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiAddress.setStatus("current")


class _TsiLoadPosition_Type(Integer32):
    """Custom type tsiLoadPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiLoadPosition_Type.__name__ = "Integer32"
_TsiLoadPosition_Object = MibTableColumn
tsiLoadPosition = _TsiLoadPosition_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 6),
    _TsiLoadPosition_Type()
)
tsiLoadPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiLoadPosition.setStatus("current")


class _TsiLoadRatioW_Type(Integer32):
    """Custom type tsiLoadRatioW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiLoadRatioW_Type.__name__ = "Integer32"
_TsiLoadRatioW_Object = MibTableColumn
tsiLoadRatioW = _TsiLoadRatioW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 7),
    _TsiLoadRatioW_Type()
)
tsiLoadRatioW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiLoadRatioW.setStatus("current")


class _TsiLoadRatioVA_Type(Integer32):
    """Custom type tsiLoadRatioVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiLoadRatioVA_Type.__name__ = "Integer32"
_TsiLoadRatioVA_Object = MibTableColumn
tsiLoadRatioVA = _TsiLoadRatioVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 8),
    _TsiLoadRatioVA_Type()
)
tsiLoadRatioVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiLoadRatioVA.setStatus("current")


class _TsiSerialNumber_Type(Integer32):
    """Custom type tsiSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TsiSerialNumber_Type.__name__ = "Integer32"
_TsiSerialNumber_Object = MibTableColumn
tsiSerialNumber = _TsiSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 9),
    _TsiSerialNumber_Type()
)
tsiSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiSerialNumber.setStatus("current")


class _TsiVout_Type(Integer32):
    """Custom type tsiVout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiVout_Type.__name__ = "Integer32"
_TsiVout_Object = MibTableColumn
tsiVout = _TsiVout_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 10),
    _TsiVout_Type()
)
tsiVout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiVout.setStatus("current")


class _TsiIout_Type(Integer32):
    """Custom type tsiIout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiIout_Type.__name__ = "Integer32"
_TsiIout_Object = MibTableColumn
tsiIout = _TsiIout_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 11),
    _TsiIout_Type()
)
tsiIout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiIout.setStatus("current")


class _TsiPoutW_Type(Integer32):
    """Custom type tsiPoutW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiPoutW_Type.__name__ = "Integer32"
_TsiPoutW_Object = MibTableColumn
tsiPoutW = _TsiPoutW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 12),
    _TsiPoutW_Type()
)
tsiPoutW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPoutW.setStatus("current")


class _TsiPoutVA_Type(Integer32):
    """Custom type tsiPoutVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiPoutVA_Type.__name__ = "Integer32"
_TsiPoutVA_Object = MibTableColumn
tsiPoutVA = _TsiPoutVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 13),
    _TsiPoutVA_Type()
)
tsiPoutVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPoutVA.setStatus("current")


class _TsiVinAC_Type(Integer32):
    """Custom type tsiVinAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiVinAC_Type.__name__ = "Integer32"
_TsiVinAC_Object = MibTableColumn
tsiVinAC = _TsiVinAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 14),
    _TsiVinAC_Type()
)
tsiVinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiVinAC.setStatus("current")


class _TsiIinAC_Type(Integer32):
    """Custom type tsiIinAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiIinAC_Type.__name__ = "Integer32"
_TsiIinAC_Object = MibTableColumn
tsiIinAC = _TsiIinAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 15),
    _TsiIinAC_Type()
)
tsiIinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiIinAC.setStatus("current")


class _TsiPinACW_Type(Integer32):
    """Custom type tsiPinACW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiPinACW_Type.__name__ = "Integer32"
_TsiPinACW_Object = MibTableColumn
tsiPinACW = _TsiPinACW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 16),
    _TsiPinACW_Type()
)
tsiPinACW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPinACW.setStatus("current")


class _TsiPinACVA_Type(Integer32):
    """Custom type tsiPinACVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiPinACVA_Type.__name__ = "Integer32"
_TsiPinACVA_Object = MibTableColumn
tsiPinACVA = _TsiPinACVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 17),
    _TsiPinACVA_Type()
)
tsiPinACVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPinACVA.setStatus("current")


class _TsiACInFreq_Type(Integer32):
    """Custom type tsiACInFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiACInFreq_Type.__name__ = "Integer32"
_TsiACInFreq_Object = MibTableColumn
tsiACInFreq = _TsiACInFreq_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 18),
    _TsiACInFreq_Type()
)
tsiACInFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACInFreq.setStatus("current")


class _TsiVinDC_Type(Integer32):
    """Custom type tsiVinDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiVinDC_Type.__name__ = "Integer32"
_TsiVinDC_Object = MibTableColumn
tsiVinDC = _TsiVinDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 19),
    _TsiVinDC_Type()
)
tsiVinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiVinDC.setStatus("current")


class _TsiIinDC_Type(Integer32):
    """Custom type tsiIinDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiIinDC_Type.__name__ = "Integer32"
_TsiIinDC_Object = MibTableColumn
tsiIinDC = _TsiIinDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 20),
    _TsiIinDC_Type()
)
tsiIinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiIinDC.setStatus("current")


class _TsiPinDC_Type(Integer32):
    """Custom type tsiPinDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiPinDC_Type.__name__ = "Integer32"
_TsiPinDC_Object = MibTableColumn
tsiPinDC = _TsiPinDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 21),
    _TsiPinDC_Type()
)
tsiPinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPinDC.setStatus("current")


class _TsiTemperature_Type(Integer32):
    """Custom type tsiTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiTemperature_Type.__name__ = "Integer32"
_TsiTemperature_Object = MibTableColumn
tsiTemperature = _TsiTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 22),
    _TsiTemperature_Type()
)
tsiTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiTemperature.setStatus("current")


class _TsiSoftVersion_Type(Integer32):
    """Custom type tsiSoftVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiSoftVersion_Type.__name__ = "Integer32"
_TsiSoftVersion_Object = MibTableColumn
tsiSoftVersion = _TsiSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 23),
    _TsiSoftVersion_Type()
)
tsiSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiSoftVersion.setStatus("current")


class _TsiBusErrorCnt_Type(Integer32):
    """Custom type tsiBusErrorCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TsiBusErrorCnt_Type.__name__ = "Integer32"
_TsiBusErrorCnt_Object = MibTableColumn
tsiBusErrorCnt = _TsiBusErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 24),
    _TsiBusErrorCnt_Type()
)
tsiBusErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiBusErrorCnt.setStatus("current")


class _TsiPhaseNumber_Type(Integer32):
    """Custom type tsiPhaseNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiPhaseNumber_Type.__name__ = "Integer32"
_TsiPhaseNumber_Object = MibTableColumn
tsiPhaseNumber = _TsiPhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 25),
    _TsiPhaseNumber_Type()
)
tsiPhaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseNumber.setStatus("current")


class _TsiStatusMod_Type(Integer32):
    """Custom type tsiStatusMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiStatusMod_Type.__name__ = "Integer32"
_TsiStatusMod_Object = MibTableColumn
tsiStatusMod = _TsiStatusMod_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 26),
    _TsiStatusMod_Type()
)
tsiStatusMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiStatusMod.setStatus("current")


class _TsiStatusAC_Type(Integer32):
    """Custom type tsiStatusAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiStatusAC_Type.__name__ = "Integer32"
_TsiStatusAC_Object = MibTableColumn
tsiStatusAC = _TsiStatusAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 27),
    _TsiStatusAC_Type()
)
tsiStatusAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiStatusAC.setStatus("current")


class _TsiStatusDC_Type(Integer32):
    """Custom type tsiStatusDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiStatusDC_Type.__name__ = "Integer32"
_TsiStatusDC_Object = MibTableColumn
tsiStatusDC = _TsiStatusDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 28),
    _TsiStatusDC_Type()
)
tsiStatusDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiStatusDC.setStatus("current")


class _TsiPresent_Type(Integer32):
    """Custom type tsiPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiPresent_Type.__name__ = "Integer32"
_TsiPresent_Object = MibTableColumn
tsiPresent = _TsiPresent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 29),
    _TsiPresent_Type()
)
tsiPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPresent.setStatus("current")


class _TsiGroupAC_Type(Integer32):
    """Custom type tsiGroupAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiGroupAC_Type.__name__ = "Integer32"
_TsiGroupAC_Object = MibTableColumn
tsiGroupAC = _TsiGroupAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 30),
    _TsiGroupAC_Type()
)
tsiGroupAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiGroupAC.setStatus("current")


class _TsiGroupDC_Type(Integer32):
    """Custom type tsiGroupDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiGroupDC_Type.__name__ = "Integer32"
_TsiGroupDC_Object = MibTableColumn
tsiGroupDC = _TsiGroupDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 31),
    _TsiGroupDC_Type()
)
tsiGroupDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiGroupDC.setStatus("current")


class _TsiRestrained_Type(Integer32):
    """Custom type tsiRestrained based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiRestrained_Type.__name__ = "Integer32"
_TsiRestrained_Object = MibTableColumn
tsiRestrained = _TsiRestrained_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 32),
    _TsiRestrained_Type()
)
tsiRestrained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiRestrained.setStatus("current")


class _TsiNoEPC_Type(Integer32):
    """Custom type tsiNoEPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TsiNoEPC_Type.__name__ = "Integer32"
_TsiNoEPC_Object = MibTableColumn
tsiNoEPC = _TsiNoEPC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 33),
    _TsiNoEPC_Type()
)
tsiNoEPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiNoEPC.setStatus("current")


class _TsiPoutNominalW_Type(Integer32):
    """Custom type tsiPoutNominalW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiPoutNominalW_Type.__name__ = "Integer32"
_TsiPoutNominalW_Object = MibTableColumn
tsiPoutNominalW = _TsiPoutNominalW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 34),
    _TsiPoutNominalW_Type()
)
tsiPoutNominalW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPoutNominalW.setStatus("current")


class _TsiPoutNominalVA_Type(Integer32):
    """Custom type tsiPoutNominalVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiPoutNominalVA_Type.__name__ = "Integer32"
_TsiPoutNominalVA_Object = MibTableColumn
tsiPoutNominalVA = _TsiPoutNominalVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 35),
    _TsiPoutNominalVA_Type()
)
tsiPoutNominalVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPoutNominalVA.setStatus("current")


class _TsiVinNominalAC_Type(Integer32):
    """Custom type tsiVinNominalAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiVinNominalAC_Type.__name__ = "Integer32"
_TsiVinNominalAC_Object = MibTableColumn
tsiVinNominalAC = _TsiVinNominalAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 36),
    _TsiVinNominalAC_Type()
)
tsiVinNominalAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiVinNominalAC.setStatus("current")


class _TsiVinNominalDC_Type(Integer32):
    """Custom type tsiVinNominalDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiVinNominalDC_Type.__name__ = "Integer32"
_TsiVinNominalDC_Object = MibTableColumn
tsiVinNominalDC = _TsiVinNominalDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 37),
    _TsiVinNominalDC_Type()
)
tsiVinNominalDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiVinNominalDC.setStatus("current")


class _TsiVinNominalFreqAC_Type(Integer32):
    """Custom type tsiVinNominalFreqAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TsiVinNominalFreqAC_Type.__name__ = "Integer32"
_TsiVinNominalFreqAC_Object = MibTableColumn
tsiVinNominalFreqAC = _TsiVinNominalFreqAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 5, 5, 1, 38),
    _TsiVinNominalFreqAC_Type()
)
tsiVinNominalFreqAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiVinNominalFreqAC.setStatus("current")
_PhaseGroup_ObjectIdentity = ObjectIdentity
phaseGroup = _PhaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6)
)


class _PhaseCount_Type(Integer32):
    """Custom type phaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseCount_Type.__name__ = "Integer32"
_PhaseCount_Object = MibScalar
phaseCount = _PhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 1),
    _PhaseCount_Type()
)
phaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseCount.setStatus("current")
_PhaseGroupTable_Object = MibTable
phaseGroupTable = _PhaseGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5)
)
if mibBuilder.loadTexts:
    phaseGroupTable.setStatus("current")
_PhaseGroupEntry_Object = MibTableRow
phaseGroupEntry = _PhaseGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1)
)
phaseGroupEntry.setIndexNames(
    (0, "Inverter-MIB", "phaseGroupIndex"),
)
if mibBuilder.loadTexts:
    phaseGroupEntry.setStatus("current")


class _PhaseGroupIndex_Type(Integer32):
    """Custom type phaseGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseGroupIndex_Type.__name__ = "Integer32"
_PhaseGroupIndex_Object = MibTableColumn
phaseGroupIndex = _PhaseGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 1),
    _PhaseGroupIndex_Type()
)
phaseGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseGroupIndex.setStatus("current")


class _BRatioAvailableW_Type(Integer32):
    """Custom type bRatioAvailableW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BRatioAvailableW_Type.__name__ = "Integer32"
_BRatioAvailableW_Object = MibTableColumn
bRatioAvailableW = _BRatioAvailableW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 2),
    _BRatioAvailableW_Type()
)
bRatioAvailableW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRatioAvailableW.setStatus("current")


class _BRatioAvailableVA_Type(Integer32):
    """Custom type bRatioAvailableVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BRatioAvailableVA_Type.__name__ = "Integer32"
_BRatioAvailableVA_Object = MibTableColumn
bRatioAvailableVA = _BRatioAvailableVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 3),
    _BRatioAvailableVA_Type()
)
bRatioAvailableVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRatioAvailableVA.setStatus("current")


class _BRatioInstalledW_Type(Integer32):
    """Custom type bRatioInstalledW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BRatioInstalledW_Type.__name__ = "Integer32"
_BRatioInstalledW_Object = MibTableColumn
bRatioInstalledW = _BRatioInstalledW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 4),
    _BRatioInstalledW_Type()
)
bRatioInstalledW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRatioInstalledW.setStatus("current")


class _BRatioInstalledWA_Type(Integer32):
    """Custom type bRatioInstalledWA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BRatioInstalledWA_Type.__name__ = "Integer32"
_BRatioInstalledWA_Object = MibTableColumn
bRatioInstalledWA = _BRatioInstalledWA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 5),
    _BRatioInstalledWA_Type()
)
bRatioInstalledWA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRatioInstalledWA.setStatus("current")


class _WVout_Type(Integer32):
    """Custom type wVout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WVout_Type.__name__ = "Integer32"
_WVout_Object = MibTableColumn
wVout = _WVout_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 6),
    _WVout_Type()
)
wVout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wVout.setStatus("current")


class _WIout_Type(Integer32):
    """Custom type wIout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WIout_Type.__name__ = "Integer32"
_WIout_Object = MibTableColumn
wIout = _WIout_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 7),
    _WIout_Type()
)
wIout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wIout.setStatus("current")


class _BNbOndCfg_Type(Integer32):
    """Custom type bNbOndCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbOndCfg_Type.__name__ = "Integer32"
_BNbOndCfg_Object = MibTableColumn
bNbOndCfg = _BNbOndCfg_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 8),
    _BNbOndCfg_Type()
)
bNbOndCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbOndCfg.setStatus("current")


class _BRedundancy_Type(Integer32):
    """Custom type bRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BRedundancy_Type.__name__ = "Integer32"
_BRedundancy_Object = MibTableColumn
bRedundancy = _BRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 9),
    _BRedundancy_Type()
)
bRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRedundancy.setStatus("current")


class _WACOutFreq_Type(Integer32):
    """Custom type wACOutFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WACOutFreq_Type.__name__ = "Integer32"
_WACOutFreq_Object = MibTableColumn
wACOutFreq = _WACOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 10),
    _WACOutFreq_Type()
)
wACOutFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wACOutFreq.setStatus("current")


class _LPinDC_Type(Integer32):
    """Custom type lPinDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LPinDC_Type.__name__ = "Integer32"
_LPinDC_Object = MibTableColumn
lPinDC = _LPinDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 11),
    _LPinDC_Type()
)
lPinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPinDC.setStatus("current")


class _LPinACW_Type(Integer32):
    """Custom type lPinACW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LPinACW_Type.__name__ = "Integer32"
_LPinACW_Object = MibTableColumn
lPinACW = _LPinACW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 12),
    _LPinACW_Type()
)
lPinACW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPinACW.setStatus("current")


class _LPinACVA_Type(Integer32):
    """Custom type lPinACVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LPinACVA_Type.__name__ = "Integer32"
_LPinACVA_Object = MibTableColumn
lPinACVA = _LPinACVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 13),
    _LPinACVA_Type()
)
lPinACVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPinACVA.setStatus("current")


class _LCurrentPowerInW_Type(Integer32):
    """Custom type lCurrentPowerInW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LCurrentPowerInW_Type.__name__ = "Integer32"
_LCurrentPowerInW_Object = MibTableColumn
lCurrentPowerInW = _LCurrentPowerInW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 14),
    _LCurrentPowerInW_Type()
)
lCurrentPowerInW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lCurrentPowerInW.setStatus("current")


class _LCurrentPowerInVA_Type(Integer32):
    """Custom type lCurrentPowerInVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LCurrentPowerInVA_Type.__name__ = "Integer32"
_LCurrentPowerInVA_Object = MibTableColumn
lCurrentPowerInVA = _LCurrentPowerInVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 15),
    _LCurrentPowerInVA_Type()
)
lCurrentPowerInVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lCurrentPowerInVA.setStatus("current")


class _LInstalledPowerInW_Type(Integer32):
    """Custom type lInstalledPowerInW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LInstalledPowerInW_Type.__name__ = "Integer32"
_LInstalledPowerInW_Object = MibTableColumn
lInstalledPowerInW = _LInstalledPowerInW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 16),
    _LInstalledPowerInW_Type()
)
lInstalledPowerInW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lInstalledPowerInW.setStatus("current")


class _LInstalledPowerInVA_Type(Integer32):
    """Custom type lInstalledPowerInVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LInstalledPowerInVA_Type.__name__ = "Integer32"
_LInstalledPowerInVA_Object = MibTableColumn
lInstalledPowerInVA = _LInstalledPowerInVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 17),
    _LInstalledPowerInVA_Type()
)
lInstalledPowerInVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lInstalledPowerInVA.setStatus("current")


class _LAvailablePowerInW_Type(Integer32):
    """Custom type lAvailablePowerInW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LAvailablePowerInW_Type.__name__ = "Integer32"
_LAvailablePowerInW_Object = MibTableColumn
lAvailablePowerInW = _LAvailablePowerInW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 18),
    _LAvailablePowerInW_Type()
)
lAvailablePowerInW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lAvailablePowerInW.setStatus("current")


class _LAvailablePowerInVA_Type(Integer32):
    """Custom type lAvailablePowerInVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LAvailablePowerInVA_Type.__name__ = "Integer32"
_LAvailablePowerInVA_Object = MibTableColumn
lAvailablePowerInVA = _LAvailablePowerInVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 19),
    _LAvailablePowerInVA_Type()
)
lAvailablePowerInVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lAvailablePowerInVA.setStatus("current")


class _BNbInvSeen_Type(Integer32):
    """Custom type bNbInvSeen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbInvSeen_Type.__name__ = "Integer32"
_BNbInvSeen_Object = MibTableColumn
bNbInvSeen = _BNbInvSeen_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 20),
    _BNbInvSeen_Type()
)
bNbInvSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbInvSeen.setStatus("current")


class _BNbInvOK_Type(Integer32):
    """Custom type bNbInvOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbInvOK_Type.__name__ = "Integer32"
_BNbInvOK_Object = MibTableColumn
bNbInvOK = _BNbInvOK_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 21),
    _BNbInvOK_Type()
)
bNbInvOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbInvOK.setStatus("current")


class _BNbInvMO_Type(Integer32):
    """Custom type bNbInvMO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbInvMO_Type.__name__ = "Integer32"
_BNbInvMO_Object = MibTableColumn
bNbInvMO = _BNbInvMO_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 22),
    _BNbInvMO_Type()
)
bNbInvMO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbInvMO.setStatus("current")


class _BNbInvKO_Type(Integer32):
    """Custom type bNbInvKO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbInvKO_Type.__name__ = "Integer32"
_BNbInvKO_Object = MibTableColumn
bNbInvKO = _BNbInvKO_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 23),
    _BNbInvKO_Type()
)
bNbInvKO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbInvKO.setStatus("current")


class _BNbInvNT_Type(Integer32):
    """Custom type bNbInvNT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbInvNT_Type.__name__ = "Integer32"
_BNbInvNT_Object = MibTableColumn
bNbInvNT = _BNbInvNT_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 6, 5, 1, 24),
    _BNbInvNT_Type()
)
bNbInvNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbInvNT.setStatus("current")
_AcGroup_ObjectIdentity = ObjectIdentity
acGroup = _AcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7)
)


class _AcGroupCount_Type(Integer32):
    """Custom type acGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcGroupCount_Type.__name__ = "Integer32"
_AcGroupCount_Object = MibScalar
acGroupCount = _AcGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 1),
    _AcGroupCount_Type()
)
acGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGroupCount.setStatus("current")
_AcGroupTable_Object = MibTable
acGroupTable = _AcGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5)
)
if mibBuilder.loadTexts:
    acGroupTable.setStatus("current")
_AcGroupEntry_Object = MibTableRow
acGroupEntry = _AcGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1)
)
acGroupEntry.setIndexNames(
    (0, "Inverter-MIB", "acGroupIndex"),
)
if mibBuilder.loadTexts:
    acGroupEntry.setStatus("current")


class _AcGroupIndex_Type(Integer32):
    """Custom type acGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcGroupIndex_Type.__name__ = "Integer32"
_AcGroupIndex_Object = MibTableColumn
acGroupIndex = _AcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 1),
    _AcGroupIndex_Type()
)
acGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGroupIndex.setStatus("current")


class _AcNbInvOK_Type(Integer32):
    """Custom type acNbInvOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcNbInvOK_Type.__name__ = "Integer32"
_AcNbInvOK_Object = MibTableColumn
acNbInvOK = _AcNbInvOK_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 2),
    _AcNbInvOK_Type()
)
acNbInvOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acNbInvOK.setStatus("current")


class _AcNbInvMO_Type(Integer32):
    """Custom type acNbInvMO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcNbInvMO_Type.__name__ = "Integer32"
_AcNbInvMO_Object = MibTableColumn
acNbInvMO = _AcNbInvMO_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 3),
    _AcNbInvMO_Type()
)
acNbInvMO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acNbInvMO.setStatus("current")


class _AcNbInvKO_Type(Integer32):
    """Custom type acNbInvKO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcNbInvKO_Type.__name__ = "Integer32"
_AcNbInvKO_Object = MibTableColumn
acNbInvKO = _AcNbInvKO_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 4),
    _AcNbInvKO_Type()
)
acNbInvKO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acNbInvKO.setStatus("current")


class _AcNbInvSeen_Type(Integer32):
    """Custom type acNbInvSeen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcNbInvSeen_Type.__name__ = "Integer32"
_AcNbInvSeen_Object = MibTableColumn
acNbInvSeen = _AcNbInvSeen_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 5),
    _AcNbInvSeen_Type()
)
acNbInvSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acNbInvSeen.setStatus("current")


class _AcPinACW_Type(Integer32):
    """Custom type acPinACW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AcPinACW_Type.__name__ = "Integer32"
_AcPinACW_Object = MibTableColumn
acPinACW = _AcPinACW_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 6),
    _AcPinACW_Type()
)
acPinACW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPinACW.setStatus("current")


class _AcPinACVA_Type(Integer32):
    """Custom type acPinACVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AcPinACVA_Type.__name__ = "Integer32"
_AcPinACVA_Object = MibTableColumn
acPinACVA = _AcPinACVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 7),
    _AcPinACVA_Type()
)
acPinACVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPinACVA.setStatus("current")


class _AcVinAC_Type(Integer32):
    """Custom type acVinAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcVinAC_Type.__name__ = "Integer32"
_AcVinAC_Object = MibTableColumn
acVinAC = _AcVinAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 8),
    _AcVinAC_Type()
)
acVinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVinAC.setStatus("current")


class _AcIinAC_Type(Integer32):
    """Custom type acIinAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcIinAC_Type.__name__ = "Integer32"
_AcIinAC_Object = MibTableColumn
acIinAC = _AcIinAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 9),
    _AcIinAC_Type()
)
acIinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIinAC.setStatus("current")


class _AcACinFreq_Type(Integer32):
    """Custom type acACinFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcACinFreq_Type.__name__ = "Integer32"
_AcACinFreq_Object = MibTableColumn
acACinFreq = _AcACinFreq_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 10),
    _AcACinFreq_Type()
)
acACinFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acACinFreq.setStatus("current")


class _AcACinOK_Type(Integer32):
    """Custom type acACinOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcACinOK_Type.__name__ = "Integer32"
_AcACinOK_Object = MibTableColumn
acACinOK = _AcACinOK_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 7, 5, 1, 11),
    _AcACinOK_Type()
)
acACinOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acACinOK.setStatus("current")
_DcGroup_ObjectIdentity = ObjectIdentity
dcGroup = _DcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8)
)


class _DcGroupCount_Type(Integer32):
    """Custom type dcGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcGroupCount_Type.__name__ = "Integer32"
_DcGroupCount_Object = MibScalar
dcGroupCount = _DcGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 1),
    _DcGroupCount_Type()
)
dcGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcGroupCount.setStatus("current")
_DcGroupTable_Object = MibTable
dcGroupTable = _DcGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5)
)
if mibBuilder.loadTexts:
    dcGroupTable.setStatus("current")
_DcGroupEntry_Object = MibTableRow
dcGroupEntry = _DcGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1)
)
dcGroupEntry.setIndexNames(
    (0, "Inverter-MIB", "dcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcGroupEntry.setStatus("current")


class _DcGroupIndex_Type(Integer32):
    """Custom type dcGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcGroupIndex_Type.__name__ = "Integer32"
_DcGroupIndex_Object = MibTableColumn
dcGroupIndex = _DcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 1),
    _DcGroupIndex_Type()
)
dcGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcGroupIndex.setStatus("current")


class _DcNbInvOK_Type(Integer32):
    """Custom type dcNbInvOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcNbInvOK_Type.__name__ = "Integer32"
_DcNbInvOK_Object = MibTableColumn
dcNbInvOK = _DcNbInvOK_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 2),
    _DcNbInvOK_Type()
)
dcNbInvOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNbInvOK.setStatus("current")


class _DcNbInvMO_Type(Integer32):
    """Custom type dcNbInvMO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcNbInvMO_Type.__name__ = "Integer32"
_DcNbInvMO_Object = MibTableColumn
dcNbInvMO = _DcNbInvMO_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 3),
    _DcNbInvMO_Type()
)
dcNbInvMO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNbInvMO.setStatus("current")


class _DcNbInvKO_Type(Integer32):
    """Custom type dcNbInvKO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcNbInvKO_Type.__name__ = "Integer32"
_DcNbInvKO_Object = MibTableColumn
dcNbInvKO = _DcNbInvKO_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 4),
    _DcNbInvKO_Type()
)
dcNbInvKO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNbInvKO.setStatus("current")


class _DcNbInvSeen_Type(Integer32):
    """Custom type dcNbInvSeen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcNbInvSeen_Type.__name__ = "Integer32"
_DcNbInvSeen_Object = MibTableColumn
dcNbInvSeen = _DcNbInvSeen_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 5),
    _DcNbInvSeen_Type()
)
dcNbInvSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNbInvSeen.setStatus("current")


class _DcPinDC_Type(Integer32):
    """Custom type dcPinDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DcPinDC_Type.__name__ = "Integer32"
_DcPinDC_Object = MibTableColumn
dcPinDC = _DcPinDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 6),
    _DcPinDC_Type()
)
dcPinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPinDC.setStatus("current")


class _DcVinDC_Type(Integer32):
    """Custom type dcVinDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcVinDC_Type.__name__ = "Integer32"
_DcVinDC_Object = MibTableColumn
dcVinDC = _DcVinDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 7),
    _DcVinDC_Type()
)
dcVinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcVinDC.setStatus("current")


class _DcIinDC_Type(Integer32):
    """Custom type dcIinDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcIinDC_Type.__name__ = "Integer32"
_DcIinDC_Object = MibTableColumn
dcIinDC = _DcIinDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 8),
    _DcIinDC_Type()
)
dcIinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIinDC.setStatus("current")


class _DcDCInOK_Type(Integer32):
    """Custom type dcDCInOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcDCInOK_Type.__name__ = "Integer32"
_DcDCInOK_Object = MibTableColumn
dcDCInOK = _DcDCInOK_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 8, 5, 1, 9),
    _DcDCInOK_Type()
)
dcDCInOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcDCInOK.setStatus("current")
_MiscInfoGroup_ObjectIdentity = ObjectIdentity
miscInfoGroup = _MiscInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9)
)


class _MiscInfoGroupCount_Type(Integer32):
    """Custom type miscInfoGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MiscInfoGroupCount_Type.__name__ = "Integer32"
_MiscInfoGroupCount_Object = MibScalar
miscInfoGroupCount = _MiscInfoGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 1),
    _MiscInfoGroupCount_Type()
)
miscInfoGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscInfoGroupCount.setStatus("current")
_MiscInfoGroupTable_Object = MibTable
miscInfoGroupTable = _MiscInfoGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5)
)
if mibBuilder.loadTexts:
    miscInfoGroupTable.setStatus("current")
_MiscInfoGroupEntry_Object = MibTableRow
miscInfoGroupEntry = _MiscInfoGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1)
)
miscInfoGroupEntry.setIndexNames(
    (0, "Inverter-MIB", "miscInfoGroupIndex"),
)
if mibBuilder.loadTexts:
    miscInfoGroupEntry.setStatus("current")


class _MiscInfoGroupIndex_Type(Integer32):
    """Custom type miscInfoGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MiscInfoGroupIndex_Type.__name__ = "Integer32"
_MiscInfoGroupIndex_Object = MibTableColumn
miscInfoGroupIndex = _MiscInfoGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 1),
    _MiscInfoGroupIndex_Type()
)
miscInfoGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscInfoGroupIndex.setStatus("current")


class _BOldVersionNumber_Type(Integer32):
    """Custom type bOldVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BOldVersionNumber_Type.__name__ = "Integer32"
_BOldVersionNumber_Object = MibTableColumn
bOldVersionNumber = _BOldVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 2),
    _BOldVersionNumber_Type()
)
bOldVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bOldVersionNumber.setStatus("current")


class _EPhaseNumber_Type(Integer32):
    """Custom type ePhaseNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EPhaseNumber_Type.__name__ = "Integer32"
_EPhaseNumber_Object = MibTableColumn
ePhaseNumber = _EPhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 3),
    _EPhaseNumber_Type()
)
ePhaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePhaseNumber.setStatus("current")


class _BNbMajor_Type(Integer32):
    """Custom type bNbMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbMajor_Type.__name__ = "Integer32"
_BNbMajor_Object = MibTableColumn
bNbMajor = _BNbMajor_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 4),
    _BNbMajor_Type()
)
bNbMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbMajor.setStatus("current")


class _WTempoMajorAl_Type(Integer32):
    """Custom type wTempoMajorAl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WTempoMajorAl_Type.__name__ = "Integer32"
_WTempoMajorAl_Object = MibTableColumn
wTempoMajorAl = _WTempoMajorAl_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 5),
    _WTempoMajorAl_Type()
)
wTempoMajorAl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wTempoMajorAl.setStatus("current")


class _WtempoMinorAl_Type(Integer32):
    """Custom type wtempoMinorAl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtempoMinorAl_Type.__name__ = "Integer32"
_WtempoMinorAl_Object = MibTableColumn
wtempoMinorAl = _WtempoMinorAl_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 6),
    _WtempoMinorAl_Type()
)
wtempoMinorAl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtempoMinorAl.setStatus("current")


class _LSerialNumber_Type(Integer32):
    """Custom type lSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LSerialNumber_Type.__name__ = "Integer32"
_LSerialNumber_Object = MibTableColumn
lSerialNumber = _LSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 7),
    _LSerialNumber_Type()
)
lSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSerialNumber.setStatus("current")


class _BNbMinor_Type(Integer32):
    """Custom type bNbMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbMinor_Type.__name__ = "Integer32"
_BNbMinor_Object = MibTableColumn
bNbMinor = _BNbMinor_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 8),
    _BNbMinor_Type()
)
bNbMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbMinor.setStatus("current")


class _BNbTotalAlarmNumber_Type(Integer32):
    """Custom type bNbTotalAlarmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbTotalAlarmNumber_Type.__name__ = "Integer32"
_BNbTotalAlarmNumber_Object = MibTableColumn
bNbTotalAlarmNumber = _BNbTotalAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 9),
    _BNbTotalAlarmNumber_Type()
)
bNbTotalAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbTotalAlarmNumber.setStatus("current")


class _BACInputPresent_Type(Integer32):
    """Custom type bACInputPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BACInputPresent_Type.__name__ = "Integer32"
_BACInputPresent_Object = MibTableColumn
bACInputPresent = _BACInputPresent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 10),
    _BACInputPresent_Type()
)
bACInputPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bACInputPresent.setStatus("current")


class _BSaturationThresh_Type(Integer32):
    """Custom type bSaturationThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BSaturationThresh_Type.__name__ = "Integer32"
_BSaturationThresh_Object = MibTableColumn
bSaturationThresh = _BSaturationThresh_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 11),
    _BSaturationThresh_Type()
)
bSaturationThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSaturationThresh.setStatus("current")


class _BNbGroupsDC_Type(Integer32):
    """Custom type bNbGroupsDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbGroupsDC_Type.__name__ = "Integer32"
_BNbGroupsDC_Object = MibTableColumn
bNbGroupsDC = _BNbGroupsDC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 12),
    _BNbGroupsDC_Type()
)
bNbGroupsDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbGroupsDC.setStatus("current")


class _BNbGroupsAC_Type(Integer32):
    """Custom type bNbGroupsAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BNbGroupsAC_Type.__name__ = "Integer32"
_BNbGroupsAC_Object = MibTableColumn
bNbGroupsAC = _BNbGroupsAC_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 13),
    _BNbGroupsAC_Type()
)
bNbGroupsAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bNbGroupsAC.setStatus("current")


class _BProgRelay_Type(Integer32):
    """Custom type bProgRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BProgRelay_Type.__name__ = "Integer32"
_BProgRelay_Object = MibTableColumn
bProgRelay = _BProgRelay_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 14),
    _BProgRelay_Type()
)
bProgRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bProgRelay.setStatus("current")


class _BSystemLoadPosition_Type(Integer32):
    """Custom type bSystemLoadPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BSystemLoadPosition_Type.__name__ = "Integer32"
_BSystemLoadPosition_Object = MibTableColumn
bSystemLoadPosition = _BSystemLoadPosition_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 15),
    _BSystemLoadPosition_Type()
)
bSystemLoadPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSystemLoadPosition.setStatus("current")


class _WSoftSubRevision_Type(Integer32):
    """Custom type wSoftSubRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WSoftSubRevision_Type.__name__ = "Integer32"
_WSoftSubRevision_Object = MibTableColumn
wSoftSubRevision = _WSoftSubRevision_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 16),
    _WSoftSubRevision_Type()
)
wSoftSubRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wSoftSubRevision.setStatus("current")


class _WSoftMainRevision_Type(Integer32):
    """Custom type wSoftMainRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WSoftMainRevision_Type.__name__ = "Integer32"
_WSoftMainRevision_Object = MibTableColumn
wSoftMainRevision = _WSoftMainRevision_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 17),
    _WSoftMainRevision_Type()
)
wSoftMainRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wSoftMainRevision.setStatus("current")


class _WInvVersionTextError_Type(Integer32):
    """Custom type wInvVersionTextError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WInvVersionTextError_Type.__name__ = "Integer32"
_WInvVersionTextError_Object = MibTableColumn
wInvVersionTextError = _WInvVersionTextError_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 18),
    _WInvVersionTextError_Type()
)
wInvVersionTextError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wInvVersionTextError.setStatus("current")


class _BInvMaxKnowParameters_Type(Integer32):
    """Custom type bInvMaxKnowParameters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BInvMaxKnowParameters_Type.__name__ = "Integer32"
_BInvMaxKnowParameters_Object = MibTableColumn
bInvMaxKnowParameters = _BInvMaxKnowParameters_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 9, 5, 1, 19),
    _BInvMaxKnowParameters_Type()
)
bInvMaxKnowParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bInvMaxKnowParameters.setStatus("current")
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10)
)


class _AlarmGroupCount_Type(Integer32):
    """Custom type alarmGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmGroupCount_Type.__name__ = "Integer32"
_AlarmGroupCount_Object = MibScalar
alarmGroupCount = _AlarmGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10, 1),
    _AlarmGroupCount_Type()
)
alarmGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGroupCount.setStatus("current")
_AlarmGroupTable_Object = MibTable
alarmGroupTable = _AlarmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10, 5)
)
if mibBuilder.loadTexts:
    alarmGroupTable.setStatus("current")
_AlarmGroupEntry_Object = MibTableRow
alarmGroupEntry = _AlarmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10, 5, 1)
)
alarmGroupEntry.setIndexNames(
    (0, "Inverter-MIB", "alarmGroupIndex"),
)
if mibBuilder.loadTexts:
    alarmGroupEntry.setStatus("current")


class _AlarmGroupIndex_Type(Integer32):
    """Custom type alarmGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmGroupIndex_Type.__name__ = "Integer32"
_AlarmGroupIndex_Object = MibTableColumn
alarmGroupIndex = _AlarmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10, 5, 1, 1),
    _AlarmGroupIndex_Type()
)
alarmGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGroupIndex.setStatus("current")


class _BDeviceNumber_Type(Integer32):
    """Custom type bDeviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BDeviceNumber_Type.__name__ = "Integer32"
_BDeviceNumber_Object = MibTableColumn
bDeviceNumber = _BDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10, 5, 1, 2),
    _BDeviceNumber_Type()
)
bDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDeviceNumber.setStatus("current")


class _BEventType_Type(Integer32):
    """Custom type bEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BEventType_Type.__name__ = "Integer32"
_BEventType_Object = MibTableColumn
bEventType = _BEventType_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10, 5, 1, 3),
    _BEventType_Type()
)
bEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bEventType.setStatus("current")


class _WEventNumber_Type(Integer32):
    """Custom type wEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WEventNumber_Type.__name__ = "Integer32"
_WEventNumber_Object = MibTableColumn
wEventNumber = _WEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10, 5, 1, 4),
    _WEventNumber_Type()
)
wEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEventNumber.setStatus("current")


class _SEventString_Type(DisplayString):
    """Custom type sEventString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SEventString_Type.__name__ = "DisplayString"
_SEventString_Object = MibTableColumn
sEventString = _SEventString_Object(
    (1, 3, 6, 1, 4, 1, 7309, 10, 10, 5, 1, 5),
    _SEventString_Type()
)
sEventString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sEventString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Inverter-MIB",
    **{"argus": argus,
       "pwrSysInv": pwrSysInv,
       "pwrInvCount": pwrInvCount,
       "tsiModules": tsiModules,
       "tsiModulesCount": tsiModulesCount,
       "tsiModulesTable": tsiModulesTable,
       "tsiModulesEntry": tsiModulesEntry,
       "tsiModulesIndex": tsiModulesIndex,
       "tsiStatusACOut": tsiStatusACOut,
       "tsiStatusACIn": tsiStatusACIn,
       "tsiStatusDCIn": tsiStatusDCIn,
       "tsiAddress": tsiAddress,
       "tsiLoadPosition": tsiLoadPosition,
       "tsiLoadRatioW": tsiLoadRatioW,
       "tsiLoadRatioVA": tsiLoadRatioVA,
       "tsiSerialNumber": tsiSerialNumber,
       "tsiVout": tsiVout,
       "tsiIout": tsiIout,
       "tsiPoutW": tsiPoutW,
       "tsiPoutVA": tsiPoutVA,
       "tsiVinAC": tsiVinAC,
       "tsiIinAC": tsiIinAC,
       "tsiPinACW": tsiPinACW,
       "tsiPinACVA": tsiPinACVA,
       "tsiACInFreq": tsiACInFreq,
       "tsiVinDC": tsiVinDC,
       "tsiIinDC": tsiIinDC,
       "tsiPinDC": tsiPinDC,
       "tsiTemperature": tsiTemperature,
       "tsiSoftVersion": tsiSoftVersion,
       "tsiBusErrorCnt": tsiBusErrorCnt,
       "tsiPhaseNumber": tsiPhaseNumber,
       "tsiStatusMod": tsiStatusMod,
       "tsiStatusAC": tsiStatusAC,
       "tsiStatusDC": tsiStatusDC,
       "tsiPresent": tsiPresent,
       "tsiGroupAC": tsiGroupAC,
       "tsiGroupDC": tsiGroupDC,
       "tsiRestrained": tsiRestrained,
       "tsiNoEPC": tsiNoEPC,
       "tsiPoutNominalW": tsiPoutNominalW,
       "tsiPoutNominalVA": tsiPoutNominalVA,
       "tsiVinNominalAC": tsiVinNominalAC,
       "tsiVinNominalDC": tsiVinNominalDC,
       "tsiVinNominalFreqAC": tsiVinNominalFreqAC,
       "phaseGroup": phaseGroup,
       "phaseCount": phaseCount,
       "phaseGroupTable": phaseGroupTable,
       "phaseGroupEntry": phaseGroupEntry,
       "phaseGroupIndex": phaseGroupIndex,
       "bRatioAvailableW": bRatioAvailableW,
       "bRatioAvailableVA": bRatioAvailableVA,
       "bRatioInstalledW": bRatioInstalledW,
       "bRatioInstalledWA": bRatioInstalledWA,
       "wVout": wVout,
       "wIout": wIout,
       "bNbOndCfg": bNbOndCfg,
       "bRedundancy": bRedundancy,
       "wACOutFreq": wACOutFreq,
       "lPinDC": lPinDC,
       "lPinACW": lPinACW,
       "lPinACVA": lPinACVA,
       "lCurrentPowerInW": lCurrentPowerInW,
       "lCurrentPowerInVA": lCurrentPowerInVA,
       "lInstalledPowerInW": lInstalledPowerInW,
       "lInstalledPowerInVA": lInstalledPowerInVA,
       "lAvailablePowerInW": lAvailablePowerInW,
       "lAvailablePowerInVA": lAvailablePowerInVA,
       "bNbInvSeen": bNbInvSeen,
       "bNbInvOK": bNbInvOK,
       "bNbInvMO": bNbInvMO,
       "bNbInvKO": bNbInvKO,
       "bNbInvNT": bNbInvNT,
       "acGroup": acGroup,
       "acGroupCount": acGroupCount,
       "acGroupTable": acGroupTable,
       "acGroupEntry": acGroupEntry,
       "acGroupIndex": acGroupIndex,
       "acNbInvOK": acNbInvOK,
       "acNbInvMO": acNbInvMO,
       "acNbInvKO": acNbInvKO,
       "acNbInvSeen": acNbInvSeen,
       "acPinACW": acPinACW,
       "acPinACVA": acPinACVA,
       "acVinAC": acVinAC,
       "acIinAC": acIinAC,
       "acACinFreq": acACinFreq,
       "acACinOK": acACinOK,
       "dcGroup": dcGroup,
       "dcGroupCount": dcGroupCount,
       "dcGroupTable": dcGroupTable,
       "dcGroupEntry": dcGroupEntry,
       "dcGroupIndex": dcGroupIndex,
       "dcNbInvOK": dcNbInvOK,
       "dcNbInvMO": dcNbInvMO,
       "dcNbInvKO": dcNbInvKO,
       "dcNbInvSeen": dcNbInvSeen,
       "dcPinDC": dcPinDC,
       "dcVinDC": dcVinDC,
       "dcIinDC": dcIinDC,
       "dcDCInOK": dcDCInOK,
       "miscInfoGroup": miscInfoGroup,
       "miscInfoGroupCount": miscInfoGroupCount,
       "miscInfoGroupTable": miscInfoGroupTable,
       "miscInfoGroupEntry": miscInfoGroupEntry,
       "miscInfoGroupIndex": miscInfoGroupIndex,
       "bOldVersionNumber": bOldVersionNumber,
       "ePhaseNumber": ePhaseNumber,
       "bNbMajor": bNbMajor,
       "wTempoMajorAl": wTempoMajorAl,
       "wtempoMinorAl": wtempoMinorAl,
       "lSerialNumber": lSerialNumber,
       "bNbMinor": bNbMinor,
       "bNbTotalAlarmNumber": bNbTotalAlarmNumber,
       "bACInputPresent": bACInputPresent,
       "bSaturationThresh": bSaturationThresh,
       "bNbGroupsDC": bNbGroupsDC,
       "bNbGroupsAC": bNbGroupsAC,
       "bProgRelay": bProgRelay,
       "bSystemLoadPosition": bSystemLoadPosition,
       "wSoftSubRevision": wSoftSubRevision,
       "wSoftMainRevision": wSoftMainRevision,
       "wInvVersionTextError": wInvVersionTextError,
       "bInvMaxKnowParameters": bInvMaxKnowParameters,
       "alarmGroup": alarmGroup,
       "alarmGroupCount": alarmGroupCount,
       "alarmGroupTable": alarmGroupTable,
       "alarmGroupEntry": alarmGroupEntry,
       "alarmGroupIndex": alarmGroupIndex,
       "bDeviceNumber": bDeviceNumber,
       "bEventType": bEventType,
       "wEventNumber": wEventNumber,
       "sEventString": sEventString}
)
