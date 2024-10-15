# SNMP MIB module (Wellfleet-OSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-OSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:50 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfOsiGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfOsiGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfOsi_ObjectIdentity = ObjectIdentity
wfOsi = _WfOsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1)
)


class _WfOsiDelete_Type(Integer32):
    """Custom type wfOsiDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiDelete_Type.__name__ = "Integer32"
_WfOsiDelete_Object = MibScalar
wfOsiDelete = _WfOsiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 1),
    _WfOsiDelete_Type()
)
wfOsiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiDelete.setStatus("mandatory")


class _WfOsiDisable_Type(Integer32):
    """Custom type wfOsiDisable based on Integer32"""
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


_WfOsiDisable_Type.__name__ = "Integer32"
_WfOsiDisable_Object = MibScalar
wfOsiDisable = _WfOsiDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 2),
    _WfOsiDisable_Type()
)
wfOsiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiDisable.setStatus("mandatory")


class _WfOsiState_Type(Integer32):
    """Custom type wfOsiState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfOsiState_Type.__name__ = "Integer32"
_WfOsiState_Object = MibScalar
wfOsiState = _WfOsiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 3),
    _WfOsiState_Type()
)
wfOsiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiState.setStatus("mandatory")
_WfOsiIsisVersion_Type = DisplayString
_WfOsiIsisVersion_Object = MibScalar
wfOsiIsisVersion = _WfOsiIsisVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 4),
    _WfOsiIsisVersion_Type()
)
wfOsiIsisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiIsisVersion.setStatus("mandatory")


class _WfOsiRouterType_Type(Integer32):
    """Custom type wfOsiRouterType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l1l2", 3),
          ("l1only", 1))
    )


_WfOsiRouterType_Type.__name__ = "Integer32"
_WfOsiRouterType_Object = MibScalar
wfOsiRouterType = _WfOsiRouterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 5),
    _WfOsiRouterType_Type()
)
wfOsiRouterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiRouterType.setStatus("mandatory")
_WfOsiRouterId_Type = OctetString
_WfOsiRouterId_Object = MibScalar
wfOsiRouterId = _WfOsiRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 6),
    _WfOsiRouterId_Type()
)
wfOsiRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiRouterId.setStatus("mandatory")


class _WfOsiLoadBal_Type(Integer32):
    """Custom type wfOsiLoadBal based on Integer32"""
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


_WfOsiLoadBal_Type.__name__ = "Integer32"
_WfOsiLoadBal_Object = MibScalar
wfOsiLoadBal = _WfOsiLoadBal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 7),
    _WfOsiLoadBal_Type()
)
wfOsiLoadBal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiLoadBal.setStatus("mandatory")


class _WfOsiMaxAreas_Type(Integer32):
    """Custom type wfOsiMaxAreas based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WfOsiMaxAreas_Type.__name__ = "Integer32"
_WfOsiMaxAreas_Object = MibScalar
wfOsiMaxAreas = _WfOsiMaxAreas_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 8),
    _WfOsiMaxAreas_Type()
)
wfOsiMaxAreas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiMaxAreas.setStatus("mandatory")


class _WfOsiMaxEs_Type(Integer32):
    """Custom type wfOsiMaxEs based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_WfOsiMaxEs_Type.__name__ = "Integer32"
_WfOsiMaxEs_Object = MibScalar
wfOsiMaxEs = _WfOsiMaxEs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 9),
    _WfOsiMaxEs_Type()
)
wfOsiMaxEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiMaxEs.setStatus("mandatory")


class _WfOsiMaxL1Is_Type(Integer32):
    """Custom type wfOsiMaxL1Is based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WfOsiMaxL1Is_Type.__name__ = "Integer32"
_WfOsiMaxL1Is_Object = MibScalar
wfOsiMaxL1Is = _WfOsiMaxL1Is_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 10),
    _WfOsiMaxL1Is_Type()
)
wfOsiMaxL1Is.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiMaxL1Is.setStatus("mandatory")


class _WfOsiMaxL2Is_Type(Integer32):
    """Custom type wfOsiMaxL2Is based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WfOsiMaxL2Is_Type.__name__ = "Integer32"
_WfOsiMaxL2Is_Object = MibScalar
wfOsiMaxL2Is = _WfOsiMaxL2Is_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 11),
    _WfOsiMaxL2Is_Type()
)
wfOsiMaxL2Is.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiMaxL2Is.setStatus("mandatory")


class _WfOsiMaxExtAddr_Type(Integer32):
    """Custom type wfOsiMaxExtAddr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_WfOsiMaxExtAddr_Type.__name__ = "Integer32"
_WfOsiMaxExtAddr_Object = MibScalar
wfOsiMaxExtAddr = _WfOsiMaxExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 12),
    _WfOsiMaxExtAddr_Type()
)
wfOsiMaxExtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiMaxExtAddr.setStatus("mandatory")


class _WfOsiCksumIsPdus_Type(Integer32):
    """Custom type wfOsiCksumIsPdus based on Integer32"""
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


_WfOsiCksumIsPdus_Type.__name__ = "Integer32"
_WfOsiCksumIsPdus_Object = MibScalar
wfOsiCksumIsPdus = _WfOsiCksumIsPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 13),
    _WfOsiCksumIsPdus_Type()
)
wfOsiCksumIsPdus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCksumIsPdus.setStatus("mandatory")
_WfOsiL1LspPassword_Type = DisplayString
_WfOsiL1LspPassword_Object = MibScalar
wfOsiL1LspPassword = _WfOsiL1LspPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 14),
    _WfOsiL1LspPassword_Type()
)
wfOsiL1LspPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiL1LspPassword.setStatus("mandatory")
_WfOsiL2LspPassword_Type = DisplayString
_WfOsiL2LspPassword_Object = MibScalar
wfOsiL2LspPassword = _WfOsiL2LspPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 15),
    _WfOsiL2LspPassword_Type()
)
wfOsiL2LspPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiL2LspPassword.setStatus("mandatory")
_WfOsiAreaAddr_Type = OctetString
_WfOsiAreaAddr_Object = MibScalar
wfOsiAreaAddr = _WfOsiAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 16),
    _WfOsiAreaAddr_Type()
)
wfOsiAreaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiAreaAddr.setStatus("mandatory")
_WfOsiAreaAddrAlias1_Type = OctetString
_WfOsiAreaAddrAlias1_Object = MibScalar
wfOsiAreaAddrAlias1 = _WfOsiAreaAddrAlias1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 17),
    _WfOsiAreaAddrAlias1_Type()
)
wfOsiAreaAddrAlias1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiAreaAddrAlias1.setStatus("mandatory")
_WfOsiAreaAddrAlias2_Type = OctetString
_WfOsiAreaAddrAlias2_Object = MibScalar
wfOsiAreaAddrAlias2 = _WfOsiAreaAddrAlias2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 18),
    _WfOsiAreaAddrAlias2_Type()
)
wfOsiAreaAddrAlias2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiAreaAddrAlias2.setStatus("obsolete")
_WfOsiCorruptedLsps_Type = Counter32
_WfOsiCorruptedLsps_Object = MibScalar
wfOsiCorruptedLsps = _WfOsiCorruptedLsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 19),
    _WfOsiCorruptedLsps_Type()
)
wfOsiCorruptedLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCorruptedLsps.setStatus("mandatory")
_WfOsiL1LspDbOverloads_Type = Counter32
_WfOsiL1LspDbOverloads_Object = MibScalar
wfOsiL1LspDbOverloads = _WfOsiL1LspDbOverloads_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 20),
    _WfOsiL1LspDbOverloads_Type()
)
wfOsiL1LspDbOverloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1LspDbOverloads.setStatus("mandatory")
_WfOsiL2LspDbOverloads_Type = Counter32
_WfOsiL2LspDbOverloads_Object = MibScalar
wfOsiL2LspDbOverloads = _WfOsiL2LspDbOverloads_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 21),
    _WfOsiL2LspDbOverloads_Type()
)
wfOsiL2LspDbOverloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2LspDbOverloads.setStatus("mandatory")
_WfOsiManAddrDroppedAreas_Type = Counter32
_WfOsiManAddrDroppedAreas_Object = MibScalar
wfOsiManAddrDroppedAreas = _WfOsiManAddrDroppedAreas_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 22),
    _WfOsiManAddrDroppedAreas_Type()
)
wfOsiManAddrDroppedAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiManAddrDroppedAreas.setStatus("mandatory")
_WfOsiSeqNumberSkips_Type = Counter32
_WfOsiSeqNumberSkips_Object = MibScalar
wfOsiSeqNumberSkips = _WfOsiSeqNumberSkips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 23),
    _WfOsiSeqNumberSkips_Type()
)
wfOsiSeqNumberSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiSeqNumberSkips.setStatus("mandatory")
_WfOsiOwnLspPurges_Type = Counter32
_WfOsiOwnLspPurges_Object = MibScalar
wfOsiOwnLspPurges = _WfOsiOwnLspPurges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 24),
    _WfOsiOwnLspPurges_Type()
)
wfOsiOwnLspPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiOwnLspPurges.setStatus("mandatory")
_WfOsiOthLspPurges_Type = Counter32
_WfOsiOthLspPurges_Object = MibScalar
wfOsiOthLspPurges = _WfOsiOthLspPurges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 25),
    _WfOsiOthLspPurges_Type()
)
wfOsiOthLspPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiOthLspPurges.setStatus("mandatory")
_WfOsiExceedMaxSeqNums_Type = Counter32
_WfOsiExceedMaxSeqNums_Object = MibScalar
wfOsiExceedMaxSeqNums = _WfOsiExceedMaxSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 26),
    _WfOsiExceedMaxSeqNums_Type()
)
wfOsiExceedMaxSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiExceedMaxSeqNums.setStatus("mandatory")
_WfOsiNearestL2Is_Type = OctetString
_WfOsiNearestL2Is_Object = MibScalar
wfOsiNearestL2Is = _WfOsiNearestL2Is_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 27),
    _WfOsiNearestL2Is_Type()
)
wfOsiNearestL2Is.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNearestL2Is.setStatus("mandatory")


class _WfOsiMaxDynEs_Type(Integer32):
    """Custom type wfOsiMaxDynEs based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_WfOsiMaxDynEs_Type.__name__ = "Integer32"
_WfOsiMaxDynEs_Object = MibScalar
wfOsiMaxDynEs = _WfOsiMaxDynEs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 28),
    _WfOsiMaxDynEs_Type()
)
wfOsiMaxDynEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiMaxDynEs.setStatus("mandatory")


class _WfOsiMaxDynL1Is_Type(Integer32):
    """Custom type wfOsiMaxDynL1Is based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WfOsiMaxDynL1Is_Type.__name__ = "Integer32"
_WfOsiMaxDynL1Is_Object = MibScalar
wfOsiMaxDynL1Is = _WfOsiMaxDynL1Is_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 29),
    _WfOsiMaxDynL1Is_Type()
)
wfOsiMaxDynL1Is.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiMaxDynL1Is.setStatus("mandatory")


class _WfOsiMaxDynL2Is_Type(Integer32):
    """Custom type wfOsiMaxDynL2Is based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WfOsiMaxDynL2Is_Type.__name__ = "Integer32"
_WfOsiMaxDynL2Is_Object = MibScalar
wfOsiMaxDynL2Is = _WfOsiMaxDynL2Is_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 30),
    _WfOsiMaxDynL2Is_Type()
)
wfOsiMaxDynL2Is.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiMaxDynL2Is.setStatus("mandatory")
_WfOsiNumDynEsAdjs_Type = Counter32
_WfOsiNumDynEsAdjs_Object = MibScalar
wfOsiNumDynEsAdjs = _WfOsiNumDynEsAdjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 31),
    _WfOsiNumDynEsAdjs_Type()
)
wfOsiNumDynEsAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumDynEsAdjs.setStatus("mandatory")
_WfOsiNumDynL1Adjs_Type = Counter32
_WfOsiNumDynL1Adjs_Object = MibScalar
wfOsiNumDynL1Adjs = _WfOsiNumDynL1Adjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 32),
    _WfOsiNumDynL1Adjs_Type()
)
wfOsiNumDynL1Adjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumDynL1Adjs.setStatus("mandatory")
_WfOsiNumDynL2Adjs_Type = Counter32
_WfOsiNumDynL2Adjs_Object = MibScalar
wfOsiNumDynL2Adjs = _WfOsiNumDynL2Adjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 33),
    _WfOsiNumDynL2Adjs_Type()
)
wfOsiNumDynL2Adjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumDynL2Adjs.setStatus("mandatory")
_WfOsiNumL1Routes_Type = Counter32
_WfOsiNumL1Routes_Object = MibScalar
wfOsiNumL1Routes = _WfOsiNumL1Routes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 34),
    _WfOsiNumL1Routes_Type()
)
wfOsiNumL1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumL1Routes.setStatus("mandatory")
_WfOsiNumL2Routes_Type = Counter32
_WfOsiNumL2Routes_Object = MibScalar
wfOsiNumL2Routes = _WfOsiNumL2Routes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 35),
    _WfOsiNumL2Routes_Type()
)
wfOsiNumL2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumL2Routes.setStatus("mandatory")
_WfOsiNumDynPtpEsAdjs_Type = Counter32
_WfOsiNumDynPtpEsAdjs_Object = MibScalar
wfOsiNumDynPtpEsAdjs = _WfOsiNumDynPtpEsAdjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 36),
    _WfOsiNumDynPtpEsAdjs_Type()
)
wfOsiNumDynPtpEsAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumDynPtpEsAdjs.setStatus("mandatory")
_WfOsiNumDynPtpIsAdjs_Type = Counter32
_WfOsiNumDynPtpIsAdjs_Object = MibScalar
wfOsiNumDynPtpIsAdjs = _WfOsiNumDynPtpIsAdjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 37),
    _WfOsiNumDynPtpIsAdjs_Type()
)
wfOsiNumDynPtpIsAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumDynPtpIsAdjs.setStatus("mandatory")


class _WfOsiClnpSrcRtOptionDisable_Type(Integer32):
    """Custom type wfOsiClnpSrcRtOptionDisable based on Integer32"""
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


_WfOsiClnpSrcRtOptionDisable_Type.__name__ = "Integer32"
_WfOsiClnpSrcRtOptionDisable_Object = MibScalar
wfOsiClnpSrcRtOptionDisable = _WfOsiClnpSrcRtOptionDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 38),
    _WfOsiClnpSrcRtOptionDisable_Type()
)
wfOsiClnpSrcRtOptionDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiClnpSrcRtOptionDisable.setStatus("mandatory")
_WfOsiNumL1Lsps_Type = Counter32
_WfOsiNumL1Lsps_Object = MibScalar
wfOsiNumL1Lsps = _WfOsiNumL1Lsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 39),
    _WfOsiNumL1Lsps_Type()
)
wfOsiNumL1Lsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumL1Lsps.setStatus("mandatory")
_WfOsiNumL2Lsps_Type = Counter32
_WfOsiNumL2Lsps_Object = MibScalar
wfOsiNumL2Lsps = _WfOsiNumL2Lsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 40),
    _WfOsiNumL2Lsps_Type()
)
wfOsiNumL2Lsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiNumL2Lsps.setStatus("mandatory")


class _WfOsiFletchRelaxedEnable_Type(Integer32):
    """Custom type wfOsiFletchRelaxedEnable based on Integer32"""
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


_WfOsiFletchRelaxedEnable_Type.__name__ = "Integer32"
_WfOsiFletchRelaxedEnable_Object = MibScalar
wfOsiFletchRelaxedEnable = _WfOsiFletchRelaxedEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 1, 41),
    _WfOsiFletchRelaxedEnable_Type()
)
wfOsiFletchRelaxedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiFletchRelaxedEnable.setStatus("mandatory")
_WfOsiStaticRouteTable_Object = MibTable
wfOsiStaticRouteTable = _WfOsiStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2)
)
if mibBuilder.loadTexts:
    wfOsiStaticRouteTable.setStatus("mandatory")
_WfOsiStaticRouteEntry_Object = MibTableRow
wfOsiStaticRouteEntry = _WfOsiStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2, 1)
)
wfOsiStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiStaticRouteAddr"),
)
if mibBuilder.loadTexts:
    wfOsiStaticRouteEntry.setStatus("mandatory")


class _WfOsiStaticRouteDelete_Type(Integer32):
    """Custom type wfOsiStaticRouteDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiStaticRouteDelete_Type.__name__ = "Integer32"
_WfOsiStaticRouteDelete_Object = MibTableColumn
wfOsiStaticRouteDelete = _WfOsiStaticRouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2, 1, 1),
    _WfOsiStaticRouteDelete_Type()
)
wfOsiStaticRouteDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticRouteDelete.setStatus("mandatory")


class _WfOsiStaticRouteDisable_Type(Integer32):
    """Custom type wfOsiStaticRouteDisable based on Integer32"""
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


_WfOsiStaticRouteDisable_Type.__name__ = "Integer32"
_WfOsiStaticRouteDisable_Object = MibTableColumn
wfOsiStaticRouteDisable = _WfOsiStaticRouteDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2, 1, 2),
    _WfOsiStaticRouteDisable_Type()
)
wfOsiStaticRouteDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticRouteDisable.setStatus("mandatory")


class _WfOsiStaticRouteAddr_Type(OctetString):
    """Custom type wfOsiStaticRouteAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WfOsiStaticRouteAddr_Type.__name__ = "OctetString"
_WfOsiStaticRouteAddr_Object = MibTableColumn
wfOsiStaticRouteAddr = _WfOsiStaticRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2, 1, 3),
    _WfOsiStaticRouteAddr_Type()
)
wfOsiStaticRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiStaticRouteAddr.setStatus("mandatory")
_WfOsiStaticRouteNibbleLength_Type = Integer32
_WfOsiStaticRouteNibbleLength_Object = MibTableColumn
wfOsiStaticRouteNibbleLength = _WfOsiStaticRouteNibbleLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2, 1, 4),
    _WfOsiStaticRouteNibbleLength_Type()
)
wfOsiStaticRouteNibbleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticRouteNibbleLength.setStatus("mandatory")
_WfOsiStaticRouteNextHopIs_Type = OctetString
_WfOsiStaticRouteNextHopIs_Object = MibTableColumn
wfOsiStaticRouteNextHopIs = _WfOsiStaticRouteNextHopIs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2, 1, 5),
    _WfOsiStaticRouteNextHopIs_Type()
)
wfOsiStaticRouteNextHopIs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticRouteNextHopIs.setStatus("mandatory")


class _WfOsiStaticRouteType_Type(Integer32):
    """Custom type wfOsiStaticRouteType based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("areaaddr", 11),
          ("es", 9),
          ("extaddr", 13))
    )


_WfOsiStaticRouteType_Type.__name__ = "Integer32"
_WfOsiStaticRouteType_Object = MibTableColumn
wfOsiStaticRouteType = _WfOsiStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2, 1, 6),
    _WfOsiStaticRouteType_Type()
)
wfOsiStaticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticRouteType.setStatus("mandatory")


class _WfOsiStaticRouteCost_Type(Integer32):
    """Custom type wfOsiStaticRouteCost based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfOsiStaticRouteCost_Type.__name__ = "Integer32"
_WfOsiStaticRouteCost_Object = MibTableColumn
wfOsiStaticRouteCost = _WfOsiStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 2, 1, 7),
    _WfOsiStaticRouteCost_Type()
)
wfOsiStaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticRouteCost.setStatus("mandatory")
_WfOsiCircuitTable_Object = MibTable
wfOsiCircuitTable = _WfOsiCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3)
)
if mibBuilder.loadTexts:
    wfOsiCircuitTable.setStatus("mandatory")
_WfOsiCircuitEntry_Object = MibTableRow
wfOsiCircuitEntry = _WfOsiCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1)
)
wfOsiCircuitEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiCircuitId"),
)
if mibBuilder.loadTexts:
    wfOsiCircuitEntry.setStatus("mandatory")


class _WfOsiCircuitDelete_Type(Integer32):
    """Custom type wfOsiCircuitDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiCircuitDelete_Type.__name__ = "Integer32"
_WfOsiCircuitDelete_Object = MibTableColumn
wfOsiCircuitDelete = _WfOsiCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 1),
    _WfOsiCircuitDelete_Type()
)
wfOsiCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitDelete.setStatus("mandatory")


class _WfOsiCircuitDisable_Type(Integer32):
    """Custom type wfOsiCircuitDisable based on Integer32"""
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


_WfOsiCircuitDisable_Type.__name__ = "Integer32"
_WfOsiCircuitDisable_Object = MibTableColumn
wfOsiCircuitDisable = _WfOsiCircuitDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 2),
    _WfOsiCircuitDisable_Type()
)
wfOsiCircuitDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitDisable.setStatus("mandatory")


class _WfOsiCircuitState_Type(Integer32):
    """Custom type wfOsiCircuitState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfOsiCircuitState_Type.__name__ = "Integer32"
_WfOsiCircuitState_Object = MibTableColumn
wfOsiCircuitState = _WfOsiCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 3),
    _WfOsiCircuitState_Type()
)
wfOsiCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitState.setStatus("mandatory")
_WfOsiCircuitId_Type = Integer32
_WfOsiCircuitId_Object = MibTableColumn
wfOsiCircuitId = _WfOsiCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 4),
    _WfOsiCircuitId_Type()
)
wfOsiCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitId.setStatus("mandatory")


class _WfOsiCircuitRouterLevel_Type(Integer32):
    """Custom type wfOsiCircuitRouterLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("esisonly", 8),
          ("ext", 4),
          ("l1", 1),
          ("l1l2", 3),
          ("l1l2ext", 7),
          ("l2", 2),
          ("l2ext", 6))
    )


_WfOsiCircuitRouterLevel_Type.__name__ = "Integer32"
_WfOsiCircuitRouterLevel_Object = MibTableColumn
wfOsiCircuitRouterLevel = _WfOsiCircuitRouterLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 5),
    _WfOsiCircuitRouterLevel_Type()
)
wfOsiCircuitRouterLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitRouterLevel.setStatus("mandatory")


class _WfOsiCircuitL1DefaultMetric_Type(Integer32):
    """Custom type wfOsiCircuitL1DefaultMetric based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfOsiCircuitL1DefaultMetric_Type.__name__ = "Integer32"
_WfOsiCircuitL1DefaultMetric_Object = MibTableColumn
wfOsiCircuitL1DefaultMetric = _WfOsiCircuitL1DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 6),
    _WfOsiCircuitL1DefaultMetric_Type()
)
wfOsiCircuitL1DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitL1DefaultMetric.setStatus("mandatory")


class _WfOsiCircuitL2DefaultMetric_Type(Integer32):
    """Custom type wfOsiCircuitL2DefaultMetric based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfOsiCircuitL2DefaultMetric_Type.__name__ = "Integer32"
_WfOsiCircuitL2DefaultMetric_Object = MibTableColumn
wfOsiCircuitL2DefaultMetric = _WfOsiCircuitL2DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 7),
    _WfOsiCircuitL2DefaultMetric_Type()
)
wfOsiCircuitL2DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitL2DefaultMetric.setStatus("mandatory")


class _WfOsiCircuitL1DrPriority_Type(Integer32):
    """Custom type wfOsiCircuitL1DrPriority based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfOsiCircuitL1DrPriority_Type.__name__ = "Integer32"
_WfOsiCircuitL1DrPriority_Object = MibTableColumn
wfOsiCircuitL1DrPriority = _WfOsiCircuitL1DrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 8),
    _WfOsiCircuitL1DrPriority_Type()
)
wfOsiCircuitL1DrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitL1DrPriority.setStatus("mandatory")


class _WfOsiCircuitL2DrPriority_Type(Integer32):
    """Custom type wfOsiCircuitL2DrPriority based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfOsiCircuitL2DrPriority_Type.__name__ = "Integer32"
_WfOsiCircuitL2DrPriority_Object = MibTableColumn
wfOsiCircuitL2DrPriority = _WfOsiCircuitL2DrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 9),
    _WfOsiCircuitL2DrPriority_Type()
)
wfOsiCircuitL2DrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitL2DrPriority.setStatus("mandatory")


class _WfOsiCircuitIsisHelloTimer_Type(Integer32):
    """Custom type wfOsiCircuitIsisHelloTimer based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_WfOsiCircuitIsisHelloTimer_Type.__name__ = "Integer32"
_WfOsiCircuitIsisHelloTimer_Object = MibTableColumn
wfOsiCircuitIsisHelloTimer = _WfOsiCircuitIsisHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 10),
    _WfOsiCircuitIsisHelloTimer_Type()
)
wfOsiCircuitIsisHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitIsisHelloTimer.setStatus("mandatory")


class _WfOsiCircuitEsisHelloTimer_Type(Integer32):
    """Custom type wfOsiCircuitEsisHelloTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_WfOsiCircuitEsisHelloTimer_Type.__name__ = "Integer32"
_WfOsiCircuitEsisHelloTimer_Object = MibTableColumn
wfOsiCircuitEsisHelloTimer = _WfOsiCircuitEsisHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 11),
    _WfOsiCircuitEsisHelloTimer_Type()
)
wfOsiCircuitEsisHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitEsisHelloTimer.setStatus("mandatory")


class _WfOsiCircuitEshConfigTime_Type(Integer32):
    """Custom type wfOsiCircuitEshConfigTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_WfOsiCircuitEshConfigTime_Type.__name__ = "Integer32"
_WfOsiCircuitEshConfigTime_Object = MibTableColumn
wfOsiCircuitEshConfigTime = _WfOsiCircuitEshConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 12),
    _WfOsiCircuitEshConfigTime_Type()
)
wfOsiCircuitEshConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitEshConfigTime.setStatus("mandatory")
_WfOsiCircuitPassword_Type = DisplayString
_WfOsiCircuitPassword_Object = MibTableColumn
wfOsiCircuitPassword = _WfOsiCircuitPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 13),
    _WfOsiCircuitPassword_Type()
)
wfOsiCircuitPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitPassword.setStatus("mandatory")
_WfOsiCircuitReceivedPkts_Type = Counter32
_WfOsiCircuitReceivedPkts_Object = MibTableColumn
wfOsiCircuitReceivedPkts = _WfOsiCircuitReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 14),
    _WfOsiCircuitReceivedPkts_Type()
)
wfOsiCircuitReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitReceivedPkts.setStatus("mandatory")
_WfOsiCircuitSentPkts_Type = Counter32
_WfOsiCircuitSentPkts_Object = MibTableColumn
wfOsiCircuitSentPkts = _WfOsiCircuitSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 15),
    _WfOsiCircuitSentPkts_Type()
)
wfOsiCircuitSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitSentPkts.setStatus("mandatory")
_WfOsiCircuitDroppedPkts_Type = Counter32
_WfOsiCircuitDroppedPkts_Object = MibTableColumn
wfOsiCircuitDroppedPkts = _WfOsiCircuitDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 16),
    _WfOsiCircuitDroppedPkts_Type()
)
wfOsiCircuitDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitDroppedPkts.setStatus("mandatory")
_WfOsiCircuitFragmentedPdus_Type = Counter32
_WfOsiCircuitFragmentedPdus_Object = MibTableColumn
wfOsiCircuitFragmentedPdus = _WfOsiCircuitFragmentedPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 17),
    _WfOsiCircuitFragmentedPdus_Type()
)
wfOsiCircuitFragmentedPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitFragmentedPdus.setStatus("mandatory")
_WfOsiCircuitCongestionDiscards_Type = Counter32
_WfOsiCircuitCongestionDiscards_Object = MibTableColumn
wfOsiCircuitCongestionDiscards = _WfOsiCircuitCongestionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 18),
    _WfOsiCircuitCongestionDiscards_Type()
)
wfOsiCircuitCongestionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitCongestionDiscards.setStatus("mandatory")
_WfOsiCircuitAddrUnreachDiscards_Type = Counter32
_WfOsiCircuitAddrUnreachDiscards_Object = MibTableColumn
wfOsiCircuitAddrUnreachDiscards = _WfOsiCircuitAddrUnreachDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 19),
    _WfOsiCircuitAddrUnreachDiscards_Type()
)
wfOsiCircuitAddrUnreachDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitAddrUnreachDiscards.setStatus("mandatory")
_WfOsiCircuitAgedPduDiscards_Type = Counter32
_WfOsiCircuitAgedPduDiscards_Object = MibTableColumn
wfOsiCircuitAgedPduDiscards = _WfOsiCircuitAgedPduDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 20),
    _WfOsiCircuitAgedPduDiscards_Type()
)
wfOsiCircuitAgedPduDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitAgedPduDiscards.setStatus("mandatory")
_WfOsiCircuitPduFormatErrDiscards_Type = Counter32
_WfOsiCircuitPduFormatErrDiscards_Object = MibTableColumn
wfOsiCircuitPduFormatErrDiscards = _WfOsiCircuitPduFormatErrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 21),
    _WfOsiCircuitPduFormatErrDiscards_Type()
)
wfOsiCircuitPduFormatErrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitPduFormatErrDiscards.setStatus("mandatory")
_WfOsiCircuitUnsuppOptsDiscards_Type = Counter32
_WfOsiCircuitUnsuppOptsDiscards_Object = MibTableColumn
wfOsiCircuitUnsuppOptsDiscards = _WfOsiCircuitUnsuppOptsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 22),
    _WfOsiCircuitUnsuppOptsDiscards_Type()
)
wfOsiCircuitUnsuppOptsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitUnsuppOptsDiscards.setStatus("mandatory")
_WfOsiCircuitSentErrorReports_Type = Counter32
_WfOsiCircuitSentErrorReports_Object = MibTableColumn
wfOsiCircuitSentErrorReports = _WfOsiCircuitSentErrorReports_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 23),
    _WfOsiCircuitSentErrorReports_Type()
)
wfOsiCircuitSentErrorReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitSentErrorReports.setStatus("mandatory")
_WfOsiCircuitReceivedControlPdus_Type = Counter32
_WfOsiCircuitReceivedControlPdus_Object = MibTableColumn
wfOsiCircuitReceivedControlPdus = _WfOsiCircuitReceivedControlPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 24),
    _WfOsiCircuitReceivedControlPdus_Type()
)
wfOsiCircuitReceivedControlPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitReceivedControlPdus.setStatus("mandatory")
_WfOsiCircuitSentControlPdus_Type = Counter32
_WfOsiCircuitSentControlPdus_Object = MibTableColumn
wfOsiCircuitSentControlPdus = _WfOsiCircuitSentControlPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 25),
    _WfOsiCircuitSentControlPdus_Type()
)
wfOsiCircuitSentControlPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitSentControlPdus.setStatus("mandatory")
_WfOsiCircuitStateChanges_Type = Counter32
_WfOsiCircuitStateChanges_Object = MibTableColumn
wfOsiCircuitStateChanges = _WfOsiCircuitStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 26),
    _WfOsiCircuitStateChanges_Type()
)
wfOsiCircuitStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitStateChanges.setStatus("mandatory")
_WfOsiCircuitAdjStateChanges_Type = Counter32
_WfOsiCircuitAdjStateChanges_Object = MibTableColumn
wfOsiCircuitAdjStateChanges = _WfOsiCircuitAdjStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 27),
    _WfOsiCircuitAdjStateChanges_Type()
)
wfOsiCircuitAdjStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitAdjStateChanges.setStatus("mandatory")
_WfOsiCircuitInitFailures_Type = Counter32
_WfOsiCircuitInitFailures_Object = MibTableColumn
wfOsiCircuitInitFailures = _WfOsiCircuitInitFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 28),
    _WfOsiCircuitInitFailures_Type()
)
wfOsiCircuitInitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitInitFailures.setStatus("mandatory")
_WfOsiCircuitRejectedAdjs_Type = Counter32
_WfOsiCircuitRejectedAdjs_Object = MibTableColumn
wfOsiCircuitRejectedAdjs = _WfOsiCircuitRejectedAdjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 29),
    _WfOsiCircuitRejectedAdjs_Type()
)
wfOsiCircuitRejectedAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitRejectedAdjs.setStatus("mandatory")
_WfOsiCircuitReceivedBadLsps_Type = Counter32
_WfOsiCircuitReceivedBadLsps_Object = MibTableColumn
wfOsiCircuitReceivedBadLsps = _WfOsiCircuitReceivedBadLsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 30),
    _WfOsiCircuitReceivedBadLsps_Type()
)
wfOsiCircuitReceivedBadLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitReceivedBadLsps.setStatus("mandatory")
_WfOsiCircuitReceivedBadSnps_Type = Counter32
_WfOsiCircuitReceivedBadSnps_Object = MibTableColumn
wfOsiCircuitReceivedBadSnps = _WfOsiCircuitReceivedBadSnps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 31),
    _WfOsiCircuitReceivedBadSnps_Type()
)
wfOsiCircuitReceivedBadSnps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitReceivedBadSnps.setStatus("mandatory")
_WfOsiCircuitReceivedBadEshs_Type = Counter32
_WfOsiCircuitReceivedBadEshs_Object = MibTableColumn
wfOsiCircuitReceivedBadEshs = _WfOsiCircuitReceivedBadEshs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 32),
    _WfOsiCircuitReceivedBadEshs_Type()
)
wfOsiCircuitReceivedBadEshs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitReceivedBadEshs.setStatus("mandatory")
_WfOsiCircuitReceivedBadL1Iihs_Type = Counter32
_WfOsiCircuitReceivedBadL1Iihs_Object = MibTableColumn
wfOsiCircuitReceivedBadL1Iihs = _WfOsiCircuitReceivedBadL1Iihs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 33),
    _WfOsiCircuitReceivedBadL1Iihs_Type()
)
wfOsiCircuitReceivedBadL1Iihs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitReceivedBadL1Iihs.setStatus("mandatory")
_WfOsiCircuitReceivedBadL2Iihs_Type = Counter32
_WfOsiCircuitReceivedBadL2Iihs_Object = MibTableColumn
wfOsiCircuitReceivedBadL2Iihs = _WfOsiCircuitReceivedBadL2Iihs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 34),
    _WfOsiCircuitReceivedBadL2Iihs_Type()
)
wfOsiCircuitReceivedBadL2Iihs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitReceivedBadL2Iihs.setStatus("mandatory")
_WfOsiCircuitL1DrChanges_Type = Counter32
_WfOsiCircuitL1DrChanges_Object = MibTableColumn
wfOsiCircuitL1DrChanges = _WfOsiCircuitL1DrChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 35),
    _WfOsiCircuitL1DrChanges_Type()
)
wfOsiCircuitL1DrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitL1DrChanges.setStatus("mandatory")
_WfOsiCircuitL2DrChanges_Type = Counter32
_WfOsiCircuitL2DrChanges_Object = MibTableColumn
wfOsiCircuitL2DrChanges = _WfOsiCircuitL2DrChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 36),
    _WfOsiCircuitL2DrChanges_Type()
)
wfOsiCircuitL2DrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitL2DrChanges.setStatus("mandatory")
_WfOsiCircuitClnpForwarding_Type = Counter32
_WfOsiCircuitClnpForwarding_Object = MibTableColumn
wfOsiCircuitClnpForwarding = _WfOsiCircuitClnpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 37),
    _WfOsiCircuitClnpForwarding_Type()
)
wfOsiCircuitClnpForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpForwarding.setStatus("mandatory")
_WfOsiCircuitClnpDefaultLifeTime_Type = Counter32
_WfOsiCircuitClnpDefaultLifeTime_Object = MibTableColumn
wfOsiCircuitClnpDefaultLifeTime = _WfOsiCircuitClnpDefaultLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 38),
    _WfOsiCircuitClnpDefaultLifeTime_Type()
)
wfOsiCircuitClnpDefaultLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpDefaultLifeTime.setStatus("mandatory")
_WfOsiCircuitClnpInReceives_Type = Counter32
_WfOsiCircuitClnpInReceives_Object = MibTableColumn
wfOsiCircuitClnpInReceives = _WfOsiCircuitClnpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 39),
    _WfOsiCircuitClnpInReceives_Type()
)
wfOsiCircuitClnpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpInReceives.setStatus("mandatory")
_WfOsiCircuitClnpInAddrErrors_Type = Counter32
_WfOsiCircuitClnpInAddrErrors_Object = MibTableColumn
wfOsiCircuitClnpInAddrErrors = _WfOsiCircuitClnpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 40),
    _WfOsiCircuitClnpInAddrErrors_Type()
)
wfOsiCircuitClnpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpInAddrErrors.setStatus("mandatory")
_WfOsiCircuitClnpForwPdus_Type = Counter32
_WfOsiCircuitClnpForwPdus_Object = MibTableColumn
wfOsiCircuitClnpForwPdus = _WfOsiCircuitClnpForwPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 41),
    _WfOsiCircuitClnpForwPdus_Type()
)
wfOsiCircuitClnpForwPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpForwPdus.setStatus("mandatory")
_WfOsiCircuitClnpInUnknownNlps_Type = Counter32
_WfOsiCircuitClnpInUnknownNlps_Object = MibTableColumn
wfOsiCircuitClnpInUnknownNlps = _WfOsiCircuitClnpInUnknownNlps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 42),
    _WfOsiCircuitClnpInUnknownNlps_Type()
)
wfOsiCircuitClnpInUnknownNlps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpInUnknownNlps.setStatus("mandatory")
_WfOsiCircuitClnpInDelivers_Type = Counter32
_WfOsiCircuitClnpInDelivers_Object = MibTableColumn
wfOsiCircuitClnpInDelivers = _WfOsiCircuitClnpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 43),
    _WfOsiCircuitClnpInDelivers_Type()
)
wfOsiCircuitClnpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpInDelivers.setStatus("mandatory")
_WfOsiCircuitClnpInUnknownUlps_Type = Counter32
_WfOsiCircuitClnpInUnknownUlps_Object = MibTableColumn
wfOsiCircuitClnpInUnknownUlps = _WfOsiCircuitClnpInUnknownUlps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 44),
    _WfOsiCircuitClnpInUnknownUlps_Type()
)
wfOsiCircuitClnpInUnknownUlps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpInUnknownUlps.setStatus("mandatory")
_WfOsiCircuitClnpSegCreates_Type = Counter32
_WfOsiCircuitClnpSegCreates_Object = MibTableColumn
wfOsiCircuitClnpSegCreates = _WfOsiCircuitClnpSegCreates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 45),
    _WfOsiCircuitClnpSegCreates_Type()
)
wfOsiCircuitClnpSegCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpSegCreates.setStatus("mandatory")
_WfOsiCircuitClnpInOpts_Type = Counter32
_WfOsiCircuitClnpInOpts_Object = MibTableColumn
wfOsiCircuitClnpInOpts = _WfOsiCircuitClnpInOpts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 46),
    _WfOsiCircuitClnpInOpts_Type()
)
wfOsiCircuitClnpInOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpInOpts.setStatus("mandatory")
_WfOsiCircuitClnpOutOpts_Type = Counter32
_WfOsiCircuitClnpOutOpts_Object = MibTableColumn
wfOsiCircuitClnpOutOpts = _WfOsiCircuitClnpOutOpts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 47),
    _WfOsiCircuitClnpOutOpts_Type()
)
wfOsiCircuitClnpOutOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpOutOpts.setStatus("mandatory")
_WfOsiCircuitEsisEshIns_Type = Counter32
_WfOsiCircuitEsisEshIns_Object = MibTableColumn
wfOsiCircuitEsisEshIns = _WfOsiCircuitEsisEshIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 48),
    _WfOsiCircuitEsisEshIns_Type()
)
wfOsiCircuitEsisEshIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitEsisEshIns.setStatus("mandatory")
_WfOsiCircuitEsisIshOuts_Type = Counter32
_WfOsiCircuitEsisIshOuts_Object = MibTableColumn
wfOsiCircuitEsisIshOuts = _WfOsiCircuitEsisIshOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 49),
    _WfOsiCircuitEsisIshOuts_Type()
)
wfOsiCircuitEsisIshOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitEsisIshOuts.setStatus("mandatory")
_WfOsiCircuitEsisRduOuts_Type = Counter32
_WfOsiCircuitEsisRduOuts_Object = MibTableColumn
wfOsiCircuitEsisRduOuts = _WfOsiCircuitEsisRduOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 50),
    _WfOsiCircuitEsisRduOuts_Type()
)
wfOsiCircuitEsisRduOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitEsisRduOuts.setStatus("mandatory")
_WfOsiCircuitL1DesignatedRouter_Type = OctetString
_WfOsiCircuitL1DesignatedRouter_Object = MibTableColumn
wfOsiCircuitL1DesignatedRouter = _WfOsiCircuitL1DesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 51),
    _WfOsiCircuitL1DesignatedRouter_Type()
)
wfOsiCircuitL1DesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitL1DesignatedRouter.setStatus("mandatory")
_WfOsiCircuitL2DesignatedRouter_Type = OctetString
_WfOsiCircuitL2DesignatedRouter_Object = MibTableColumn
wfOsiCircuitL2DesignatedRouter = _WfOsiCircuitL2DesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 52),
    _WfOsiCircuitL2DesignatedRouter_Type()
)
wfOsiCircuitL2DesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitL2DesignatedRouter.setStatus("mandatory")
_WfOsiCircuitClnpOutEchoReplies_Type = Counter32
_WfOsiCircuitClnpOutEchoReplies_Object = MibTableColumn
wfOsiCircuitClnpOutEchoReplies = _WfOsiCircuitClnpOutEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 53),
    _WfOsiCircuitClnpOutEchoReplies_Type()
)
wfOsiCircuitClnpOutEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpOutEchoReplies.setStatus("mandatory")
_WfOsiCircuitClnpOutEchoRequests_Type = Counter32
_WfOsiCircuitClnpOutEchoRequests_Object = MibTableColumn
wfOsiCircuitClnpOutEchoRequests = _WfOsiCircuitClnpOutEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 54),
    _WfOsiCircuitClnpOutEchoRequests_Type()
)
wfOsiCircuitClnpOutEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpOutEchoRequests.setStatus("mandatory")
_WfOsiCircuitClnpInEchoReplies_Type = Counter32
_WfOsiCircuitClnpInEchoReplies_Object = MibTableColumn
wfOsiCircuitClnpInEchoReplies = _WfOsiCircuitClnpInEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 55),
    _WfOsiCircuitClnpInEchoReplies_Type()
)
wfOsiCircuitClnpInEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpInEchoReplies.setStatus("mandatory")
_WfOsiCircuitClnpInEchoRequests_Type = Counter32
_WfOsiCircuitClnpInEchoRequests_Object = MibTableColumn
wfOsiCircuitClnpInEchoRequests = _WfOsiCircuitClnpInEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 56),
    _WfOsiCircuitClnpInEchoRequests_Type()
)
wfOsiCircuitClnpInEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitClnpInEchoRequests.setStatus("mandatory")
_WfOsiCircuitNumDynEsAdjs_Type = Counter32
_WfOsiCircuitNumDynEsAdjs_Object = MibTableColumn
wfOsiCircuitNumDynEsAdjs = _WfOsiCircuitNumDynEsAdjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 57),
    _WfOsiCircuitNumDynEsAdjs_Type()
)
wfOsiCircuitNumDynEsAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitNumDynEsAdjs.setStatus("mandatory")
_WfOsiCircuitNumDynL1Adjs_Type = Counter32
_WfOsiCircuitNumDynL1Adjs_Object = MibTableColumn
wfOsiCircuitNumDynL1Adjs = _WfOsiCircuitNumDynL1Adjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 58),
    _WfOsiCircuitNumDynL1Adjs_Type()
)
wfOsiCircuitNumDynL1Adjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitNumDynL1Adjs.setStatus("mandatory")
_WfOsiCircuitNumDynL2Adjs_Type = Counter32
_WfOsiCircuitNumDynL2Adjs_Object = MibTableColumn
wfOsiCircuitNumDynL2Adjs = _WfOsiCircuitNumDynL2Adjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 59),
    _WfOsiCircuitNumDynL2Adjs_Type()
)
wfOsiCircuitNumDynL2Adjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitNumDynL2Adjs.setStatus("mandatory")
_WfOsiCircuitNumDynPtpIsAdjs_Type = Counter32
_WfOsiCircuitNumDynPtpIsAdjs_Object = MibTableColumn
wfOsiCircuitNumDynPtpIsAdjs = _WfOsiCircuitNumDynPtpIsAdjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 60),
    _WfOsiCircuitNumDynPtpIsAdjs_Type()
)
wfOsiCircuitNumDynPtpIsAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitNumDynPtpIsAdjs.setStatus("mandatory")
_WfOsiCircuitNumDynPtpEsAdjs_Type = Counter32
_WfOsiCircuitNumDynPtpEsAdjs_Object = MibTableColumn
wfOsiCircuitNumDynPtpEsAdjs = _WfOsiCircuitNumDynPtpEsAdjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 61),
    _WfOsiCircuitNumDynPtpEsAdjs_Type()
)
wfOsiCircuitNumDynPtpEsAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitNumDynPtpEsAdjs.setStatus("mandatory")
_WfOsiCircuitBadIshReceived_Type = Counter32
_WfOsiCircuitBadIshReceived_Object = MibTableColumn
wfOsiCircuitBadIshReceived = _WfOsiCircuitBadIshReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 62),
    _WfOsiCircuitBadIshReceived_Type()
)
wfOsiCircuitBadIshReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitBadIshReceived.setStatus("mandatory")
_WfOsiCircuitEsisIshIns_Type = Counter32
_WfOsiCircuitEsisIshIns_Object = MibTableColumn
wfOsiCircuitEsisIshIns = _WfOsiCircuitEsisIshIns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 63),
    _WfOsiCircuitEsisIshIns_Type()
)
wfOsiCircuitEsisIshIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiCircuitEsisIshIns.setStatus("mandatory")


class _WfOsiCircuitIihHoldMultiplier_Type(Integer32):
    """Custom type wfOsiCircuitIihHoldMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WfOsiCircuitIihHoldMultiplier_Type.__name__ = "Integer32"
_WfOsiCircuitIihHoldMultiplier_Object = MibTableColumn
wfOsiCircuitIihHoldMultiplier = _WfOsiCircuitIihHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 64),
    _WfOsiCircuitIihHoldMultiplier_Type()
)
wfOsiCircuitIihHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitIihHoldMultiplier.setStatus("mandatory")


class _WfOsiCircuitIshHoldMultiplier_Type(Integer32):
    """Custom type wfOsiCircuitIshHoldMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WfOsiCircuitIshHoldMultiplier_Type.__name__ = "Integer32"
_WfOsiCircuitIshHoldMultiplier_Object = MibTableColumn
wfOsiCircuitIshHoldMultiplier = _WfOsiCircuitIshHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 65),
    _WfOsiCircuitIshHoldMultiplier_Type()
)
wfOsiCircuitIshHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitIshHoldMultiplier.setStatus("mandatory")


class _WfOsiCircuitDisableRedirect_Type(Integer32):
    """Custom type wfOsiCircuitDisableRedirect based on Integer32"""
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


_WfOsiCircuitDisableRedirect_Type.__name__ = "Integer32"
_WfOsiCircuitDisableRedirect_Object = MibTableColumn
wfOsiCircuitDisableRedirect = _WfOsiCircuitDisableRedirect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 3, 1, 66),
    _WfOsiCircuitDisableRedirect_Type()
)
wfOsiCircuitDisableRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiCircuitDisableRedirect.setStatus("mandatory")
_WfOsiExternalAddressTable_Object = MibTable
wfOsiExternalAddressTable = _WfOsiExternalAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4)
)
if mibBuilder.loadTexts:
    wfOsiExternalAddressTable.setStatus("mandatory")
_WfOsiExternalAddressEntry_Object = MibTableRow
wfOsiExternalAddressEntry = _WfOsiExternalAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4, 1)
)
wfOsiExternalAddressEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiExtAddrCircuit"),
    (0, "Wellfleet-OSI-MIB", "wfOsiExtAddr"),
)
if mibBuilder.loadTexts:
    wfOsiExternalAddressEntry.setStatus("mandatory")


class _WfOsiExtAddrDelete_Type(Integer32):
    """Custom type wfOsiExtAddrDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiExtAddrDelete_Type.__name__ = "Integer32"
_WfOsiExtAddrDelete_Object = MibTableColumn
wfOsiExtAddrDelete = _WfOsiExtAddrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4, 1, 1),
    _WfOsiExtAddrDelete_Type()
)
wfOsiExtAddrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiExtAddrDelete.setStatus("mandatory")


class _WfOsiExtAddrDisable_Type(Integer32):
    """Custom type wfOsiExtAddrDisable based on Integer32"""
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


_WfOsiExtAddrDisable_Type.__name__ = "Integer32"
_WfOsiExtAddrDisable_Object = MibTableColumn
wfOsiExtAddrDisable = _WfOsiExtAddrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4, 1, 2),
    _WfOsiExtAddrDisable_Type()
)
wfOsiExtAddrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiExtAddrDisable.setStatus("mandatory")


class _WfOsiExtAddr_Type(OctetString):
    """Custom type wfOsiExtAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WfOsiExtAddr_Type.__name__ = "OctetString"
_WfOsiExtAddr_Object = MibTableColumn
wfOsiExtAddr = _WfOsiExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4, 1, 3),
    _WfOsiExtAddr_Type()
)
wfOsiExtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiExtAddr.setStatus("mandatory")
_WfOsiExtAddrCircuit_Type = Integer32
_WfOsiExtAddrCircuit_Object = MibTableColumn
wfOsiExtAddrCircuit = _WfOsiExtAddrCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4, 1, 4),
    _WfOsiExtAddrCircuit_Type()
)
wfOsiExtAddrCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiExtAddrCircuit.setStatus("mandatory")
_WfOsiExtAddrNibbleLength_Type = Integer32
_WfOsiExtAddrNibbleLength_Object = MibTableColumn
wfOsiExtAddrNibbleLength = _WfOsiExtAddrNibbleLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4, 1, 5),
    _WfOsiExtAddrNibbleLength_Type()
)
wfOsiExtAddrNibbleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiExtAddrNibbleLength.setStatus("mandatory")
_WfOsiExtAddrSnpa_Type = OctetString
_WfOsiExtAddrSnpa_Object = MibTableColumn
wfOsiExtAddrSnpa = _WfOsiExtAddrSnpa_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4, 1, 6),
    _WfOsiExtAddrSnpa_Type()
)
wfOsiExtAddrSnpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiExtAddrSnpa.setStatus("mandatory")


class _WfOsiExtAddrCost_Type(Integer32):
    """Custom type wfOsiExtAddrCost based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfOsiExtAddrCost_Type.__name__ = "Integer32"
_WfOsiExtAddrCost_Object = MibTableColumn
wfOsiExtAddrCost = _WfOsiExtAddrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 4, 1, 7),
    _WfOsiExtAddrCost_Type()
)
wfOsiExtAddrCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiExtAddrCost.setStatus("mandatory")
_WfOsiStaticEsTable_Object = MibTable
wfOsiStaticEsTable = _WfOsiStaticEsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 5)
)
if mibBuilder.loadTexts:
    wfOsiStaticEsTable.setStatus("mandatory")
_WfOsiStaticEsEntry_Object = MibTableRow
wfOsiStaticEsEntry = _WfOsiStaticEsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 5, 1)
)
wfOsiStaticEsEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiStaticEsCircuit"),
    (0, "Wellfleet-OSI-MIB", "wfOsiStaticEsId"),
)
if mibBuilder.loadTexts:
    wfOsiStaticEsEntry.setStatus("mandatory")


class _WfOsiStaticEsDelete_Type(Integer32):
    """Custom type wfOsiStaticEsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiStaticEsDelete_Type.__name__ = "Integer32"
_WfOsiStaticEsDelete_Object = MibTableColumn
wfOsiStaticEsDelete = _WfOsiStaticEsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 5, 1, 1),
    _WfOsiStaticEsDelete_Type()
)
wfOsiStaticEsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticEsDelete.setStatus("mandatory")


class _WfOsiStaticEsDisable_Type(Integer32):
    """Custom type wfOsiStaticEsDisable based on Integer32"""
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


_WfOsiStaticEsDisable_Type.__name__ = "Integer32"
_WfOsiStaticEsDisable_Object = MibTableColumn
wfOsiStaticEsDisable = _WfOsiStaticEsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 5, 1, 2),
    _WfOsiStaticEsDisable_Type()
)
wfOsiStaticEsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticEsDisable.setStatus("mandatory")


class _WfOsiStaticEsId_Type(OctetString):
    """Custom type wfOsiStaticEsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfOsiStaticEsId_Type.__name__ = "OctetString"
_WfOsiStaticEsId_Object = MibTableColumn
wfOsiStaticEsId = _WfOsiStaticEsId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 5, 1, 3),
    _WfOsiStaticEsId_Type()
)
wfOsiStaticEsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiStaticEsId.setStatus("mandatory")
_WfOsiStaticEsCircuit_Type = Integer32
_WfOsiStaticEsCircuit_Object = MibTableColumn
wfOsiStaticEsCircuit = _WfOsiStaticEsCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 5, 1, 4),
    _WfOsiStaticEsCircuit_Type()
)
wfOsiStaticEsCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiStaticEsCircuit.setStatus("mandatory")
_WfOsiStaticEsSnpa_Type = OctetString
_WfOsiStaticEsSnpa_Object = MibTableColumn
wfOsiStaticEsSnpa = _WfOsiStaticEsSnpa_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 5, 1, 5),
    _WfOsiStaticEsSnpa_Type()
)
wfOsiStaticEsSnpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiStaticEsSnpa.setStatus("mandatory")
_WfOsiTrafficFilterTable_Object = MibTable
wfOsiTrafficFilterTable = _WfOsiTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6)
)
if mibBuilder.loadTexts:
    wfOsiTrafficFilterTable.setStatus("mandatory")
_WfOsiTrafficFilterEntry_Object = MibTableRow
wfOsiTrafficFilterEntry = _WfOsiTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1)
)
wfOsiTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiTrafficFilterCircuit"),
    (0, "Wellfleet-OSI-MIB", "wfOsiTrafficFilterRuleNumber"),
    (0, "Wellfleet-OSI-MIB", "wfOsiTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfOsiTrafficFilterEntry.setStatus("mandatory")


class _WfOsiTrafficFilterDelete_Type(Integer32):
    """Custom type wfOsiTrafficFilterDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiTrafficFilterDelete_Type.__name__ = "Integer32"
_WfOsiTrafficFilterDelete_Object = MibTableColumn
wfOsiTrafficFilterDelete = _WfOsiTrafficFilterDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 1),
    _WfOsiTrafficFilterDelete_Type()
)
wfOsiTrafficFilterDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterDelete.setStatus("mandatory")


class _WfOsiTrafficFilterDisable_Type(Integer32):
    """Custom type wfOsiTrafficFilterDisable based on Integer32"""
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


_WfOsiTrafficFilterDisable_Type.__name__ = "Integer32"
_WfOsiTrafficFilterDisable_Object = MibTableColumn
wfOsiTrafficFilterDisable = _WfOsiTrafficFilterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 2),
    _WfOsiTrafficFilterDisable_Type()
)
wfOsiTrafficFilterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterDisable.setStatus("mandatory")


class _WfOsiTrafficFilterStatus_Type(Integer32):
    """Custom type wfOsiTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfOsiTrafficFilterStatus_Type.__name__ = "Integer32"
_WfOsiTrafficFilterStatus_Object = MibTableColumn
wfOsiTrafficFilterStatus = _WfOsiTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 3),
    _WfOsiTrafficFilterStatus_Type()
)
wfOsiTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterStatus.setStatus("mandatory")
_WfOsiTrafficFilterCounter_Type = Counter32
_WfOsiTrafficFilterCounter_Object = MibTableColumn
wfOsiTrafficFilterCounter = _WfOsiTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 4),
    _WfOsiTrafficFilterCounter_Type()
)
wfOsiTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterCounter.setStatus("mandatory")
_WfOsiTrafficFilterDefinition_Type = Opaque
_WfOsiTrafficFilterDefinition_Object = MibTableColumn
wfOsiTrafficFilterDefinition = _WfOsiTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 5),
    _WfOsiTrafficFilterDefinition_Type()
)
wfOsiTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterDefinition.setStatus("mandatory")
_WfOsiTrafficFilterReserved_Type = Integer32
_WfOsiTrafficFilterReserved_Object = MibTableColumn
wfOsiTrafficFilterReserved = _WfOsiTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 6),
    _WfOsiTrafficFilterReserved_Type()
)
wfOsiTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterReserved.setStatus("mandatory")
_WfOsiTrafficFilterCircuit_Type = Integer32
_WfOsiTrafficFilterCircuit_Object = MibTableColumn
wfOsiTrafficFilterCircuit = _WfOsiTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 7),
    _WfOsiTrafficFilterCircuit_Type()
)
wfOsiTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterCircuit.setStatus("mandatory")
_WfOsiTrafficFilterRuleNumber_Type = Integer32
_WfOsiTrafficFilterRuleNumber_Object = MibTableColumn
wfOsiTrafficFilterRuleNumber = _WfOsiTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 8),
    _WfOsiTrafficFilterRuleNumber_Type()
)
wfOsiTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterRuleNumber.setStatus("mandatory")
_WfOsiTrafficFilterFragment_Type = Integer32
_WfOsiTrafficFilterFragment_Object = MibTableColumn
wfOsiTrafficFilterFragment = _WfOsiTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 9),
    _WfOsiTrafficFilterFragment_Type()
)
wfOsiTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterFragment.setStatus("mandatory")
_WfOsiTrafficFilterName_Type = DisplayString
_WfOsiTrafficFilterName_Object = MibTableColumn
wfOsiTrafficFilterName = _WfOsiTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 6, 1, 10),
    _WfOsiTrafficFilterName_Type()
)
wfOsiTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTrafficFilterName.setStatus("mandatory")
_WfOsiL1LspHdrTable_Object = MibTable
wfOsiL1LspHdrTable = _WfOsiL1LspHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 7)
)
if mibBuilder.loadTexts:
    wfOsiL1LspHdrTable.setStatus("mandatory")
_WfOsiL1LspHdrEntry_Object = MibTableRow
wfOsiL1LspHdrEntry = _WfOsiL1LspHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 7, 1)
)
wfOsiL1LspHdrEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiL1LspHdrLspId"),
)
if mibBuilder.loadTexts:
    wfOsiL1LspHdrEntry.setStatus("mandatory")


class _WfOsiL1LspHdrLspId_Type(OctetString):
    """Custom type wfOsiL1LspHdrLspId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfOsiL1LspHdrLspId_Type.__name__ = "OctetString"
_WfOsiL1LspHdrLspId_Object = MibTableColumn
wfOsiL1LspHdrLspId = _WfOsiL1LspHdrLspId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 7, 1, 1),
    _WfOsiL1LspHdrLspId_Type()
)
wfOsiL1LspHdrLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1LspHdrLspId.setStatus("mandatory")
_WfOsiL1LspHdrLifetime_Type = Integer32
_WfOsiL1LspHdrLifetime_Object = MibTableColumn
wfOsiL1LspHdrLifetime = _WfOsiL1LspHdrLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 7, 1, 2),
    _WfOsiL1LspHdrLifetime_Type()
)
wfOsiL1LspHdrLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1LspHdrLifetime.setStatus("mandatory")
_WfOsiL1LspHdrSeqnum_Type = Integer32
_WfOsiL1LspHdrSeqnum_Object = MibTableColumn
wfOsiL1LspHdrSeqnum = _WfOsiL1LspHdrSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 7, 1, 3),
    _WfOsiL1LspHdrSeqnum_Type()
)
wfOsiL1LspHdrSeqnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1LspHdrSeqnum.setStatus("mandatory")
_WfOsiL1LspHdrFlags_Type = OctetString
_WfOsiL1LspHdrFlags_Object = MibTableColumn
wfOsiL1LspHdrFlags = _WfOsiL1LspHdrFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 7, 1, 4),
    _WfOsiL1LspHdrFlags_Type()
)
wfOsiL1LspHdrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1LspHdrFlags.setStatus("mandatory")
_WfOsiL1LspHdrCksum_Type = OctetString
_WfOsiL1LspHdrCksum_Object = MibTableColumn
wfOsiL1LspHdrCksum = _WfOsiL1LspHdrCksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 7, 1, 5),
    _WfOsiL1LspHdrCksum_Type()
)
wfOsiL1LspHdrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1LspHdrCksum.setStatus("mandatory")
_WfOsiL2LspHdrTable_Object = MibTable
wfOsiL2LspHdrTable = _WfOsiL2LspHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 8)
)
if mibBuilder.loadTexts:
    wfOsiL2LspHdrTable.setStatus("mandatory")
_WfOsiL2LspHdrEntry_Object = MibTableRow
wfOsiL2LspHdrEntry = _WfOsiL2LspHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 8, 1)
)
wfOsiL2LspHdrEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiL2LspHdrLspId"),
)
if mibBuilder.loadTexts:
    wfOsiL2LspHdrEntry.setStatus("mandatory")


class _WfOsiL2LspHdrLspId_Type(OctetString):
    """Custom type wfOsiL2LspHdrLspId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfOsiL2LspHdrLspId_Type.__name__ = "OctetString"
_WfOsiL2LspHdrLspId_Object = MibTableColumn
wfOsiL2LspHdrLspId = _WfOsiL2LspHdrLspId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 8, 1, 1),
    _WfOsiL2LspHdrLspId_Type()
)
wfOsiL2LspHdrLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2LspHdrLspId.setStatus("mandatory")
_WfOsiL2LspHdrLifetime_Type = Integer32
_WfOsiL2LspHdrLifetime_Object = MibTableColumn
wfOsiL2LspHdrLifetime = _WfOsiL2LspHdrLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 8, 1, 2),
    _WfOsiL2LspHdrLifetime_Type()
)
wfOsiL2LspHdrLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2LspHdrLifetime.setStatus("mandatory")
_WfOsiL2LspHdrSeqnum_Type = Integer32
_WfOsiL2LspHdrSeqnum_Object = MibTableColumn
wfOsiL2LspHdrSeqnum = _WfOsiL2LspHdrSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 8, 1, 3),
    _WfOsiL2LspHdrSeqnum_Type()
)
wfOsiL2LspHdrSeqnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2LspHdrSeqnum.setStatus("mandatory")
_WfOsiL2LspHdrFlags_Type = OctetString
_WfOsiL2LspHdrFlags_Object = MibTableColumn
wfOsiL2LspHdrFlags = _WfOsiL2LspHdrFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 8, 1, 4),
    _WfOsiL2LspHdrFlags_Type()
)
wfOsiL2LspHdrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2LspHdrFlags.setStatus("mandatory")
_WfOsiL2LspHdrCksum_Type = OctetString
_WfOsiL2LspHdrCksum_Object = MibTableColumn
wfOsiL2LspHdrCksum = _WfOsiL2LspHdrCksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 8, 1, 5),
    _WfOsiL2LspHdrCksum_Type()
)
wfOsiL2LspHdrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2LspHdrCksum.setStatus("mandatory")
_WfOsiDynAdjTable_Object = MibTable
wfOsiDynAdjTable = _WfOsiDynAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9)
)
if mibBuilder.loadTexts:
    wfOsiDynAdjTable.setStatus("mandatory")
_WfOsiDynAdjEntry_Object = MibTableRow
wfOsiDynAdjEntry = _WfOsiDynAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1)
)
wfOsiDynAdjEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiDynAdjId"),
)
if mibBuilder.loadTexts:
    wfOsiDynAdjEntry.setStatus("mandatory")
_WfOsiDynAdjId_Type = Integer32
_WfOsiDynAdjId_Object = MibTableColumn
wfOsiDynAdjId = _WfOsiDynAdjId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 1),
    _WfOsiDynAdjId_Type()
)
wfOsiDynAdjId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjId.setStatus("mandatory")
_WfOsiDynAdjDatabase_Type = Integer32
_WfOsiDynAdjDatabase_Object = MibTableColumn
wfOsiDynAdjDatabase = _WfOsiDynAdjDatabase_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 2),
    _WfOsiDynAdjDatabase_Type()
)
wfOsiDynAdjDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjDatabase.setStatus("mandatory")
_WfOsiDynAdjType_Type = Integer32
_WfOsiDynAdjType_Object = MibTableColumn
wfOsiDynAdjType = _WfOsiDynAdjType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 3),
    _WfOsiDynAdjType_Type()
)
wfOsiDynAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjType.setStatus("mandatory")
_WfOsiDynAdjState_Type = Integer32
_WfOsiDynAdjState_Object = MibTableColumn
wfOsiDynAdjState = _WfOsiDynAdjState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 4),
    _WfOsiDynAdjState_Type()
)
wfOsiDynAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjState.setStatus("mandatory")
_WfOsiDynAdjCircuitId_Type = Integer32
_WfOsiDynAdjCircuitId_Object = MibTableColumn
wfOsiDynAdjCircuitId = _WfOsiDynAdjCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 5),
    _WfOsiDynAdjCircuitId_Type()
)
wfOsiDynAdjCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjCircuitId.setStatus("mandatory")
_WfOsiDynAdjHoldTime_Type = Integer32
_WfOsiDynAdjHoldTime_Object = MibTableColumn
wfOsiDynAdjHoldTime = _WfOsiDynAdjHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 6),
    _WfOsiDynAdjHoldTime_Type()
)
wfOsiDynAdjHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjHoldTime.setStatus("mandatory")
_WfOsiDynAdjPriority_Type = Integer32
_WfOsiDynAdjPriority_Object = MibTableColumn
wfOsiDynAdjPriority = _WfOsiDynAdjPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 7),
    _WfOsiDynAdjPriority_Type()
)
wfOsiDynAdjPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjPriority.setStatus("mandatory")
_WfOsiDynAdjSnpaAddr_Type = OctetString
_WfOsiDynAdjSnpaAddr_Object = MibTableColumn
wfOsiDynAdjSnpaAddr = _WfOsiDynAdjSnpaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 8),
    _WfOsiDynAdjSnpaAddr_Type()
)
wfOsiDynAdjSnpaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjSnpaAddr.setStatus("mandatory")
_WfOsiDynAdjNsapAddr_Type = OctetString
_WfOsiDynAdjNsapAddr_Object = MibTableColumn
wfOsiDynAdjNsapAddr = _WfOsiDynAdjNsapAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 9),
    _WfOsiDynAdjNsapAddr_Type()
)
wfOsiDynAdjNsapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjNsapAddr.setStatus("mandatory")
_WfOsiDynAdjLanId_Type = OctetString
_WfOsiDynAdjLanId_Object = MibTableColumn
wfOsiDynAdjLanId = _WfOsiDynAdjLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 9, 1, 10),
    _WfOsiDynAdjLanId_Type()
)
wfOsiDynAdjLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDynAdjLanId.setStatus("mandatory")
_WfOsiL1RoutesTable_Object = MibTable
wfOsiL1RoutesTable = _WfOsiL1RoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10)
)
if mibBuilder.loadTexts:
    wfOsiL1RoutesTable.setStatus("mandatory")
_WfOsiL1RouteEntry_Object = MibTableRow
wfOsiL1RouteEntry = _WfOsiL1RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1)
)
wfOsiL1RouteEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiL1RouteType"),
    (0, "Wellfleet-OSI-MIB", "wfOsiL1RoutePathSplit"),
    (0, "Wellfleet-OSI-MIB", "wfOsiL1RouteId"),
)
if mibBuilder.loadTexts:
    wfOsiL1RouteEntry.setStatus("mandatory")


class _WfOsiL1RouteId_Type(OctetString):
    """Custom type wfOsiL1RouteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfOsiL1RouteId_Type.__name__ = "OctetString"
_WfOsiL1RouteId_Object = MibTableColumn
wfOsiL1RouteId = _WfOsiL1RouteId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1, 1),
    _WfOsiL1RouteId_Type()
)
wfOsiL1RouteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1RouteId.setStatus("mandatory")
_WfOsiL1RoutePathSplit_Type = Integer32
_WfOsiL1RoutePathSplit_Object = MibTableColumn
wfOsiL1RoutePathSplit = _WfOsiL1RoutePathSplit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1, 2),
    _WfOsiL1RoutePathSplit_Type()
)
wfOsiL1RoutePathSplit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1RoutePathSplit.setStatus("mandatory")
_WfOsiL1RouteType_Type = Integer32
_WfOsiL1RouteType_Object = MibTableColumn
wfOsiL1RouteType = _WfOsiL1RouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1, 3),
    _WfOsiL1RouteType_Type()
)
wfOsiL1RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1RouteType.setStatus("mandatory")
_WfOsiL1RouteNextHopSnpa_Type = OctetString
_WfOsiL1RouteNextHopSnpa_Object = MibTableColumn
wfOsiL1RouteNextHopSnpa = _WfOsiL1RouteNextHopSnpa_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1, 4),
    _WfOsiL1RouteNextHopSnpa_Type()
)
wfOsiL1RouteNextHopSnpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1RouteNextHopSnpa.setStatus("mandatory")
_WfOsiL1RouteNextHopId_Type = OctetString
_WfOsiL1RouteNextHopId_Object = MibTableColumn
wfOsiL1RouteNextHopId = _WfOsiL1RouteNextHopId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1, 5),
    _WfOsiL1RouteNextHopId_Type()
)
wfOsiL1RouteNextHopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1RouteNextHopId.setStatus("mandatory")
_WfOsiL1RouteNextHopType_Type = Integer32
_WfOsiL1RouteNextHopType_Object = MibTableColumn
wfOsiL1RouteNextHopType = _WfOsiL1RouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1, 6),
    _WfOsiL1RouteNextHopType_Type()
)
wfOsiL1RouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1RouteNextHopType.setStatus("mandatory")
_WfOsiL1RouteNextHopCircuit_Type = Integer32
_WfOsiL1RouteNextHopCircuit_Object = MibTableColumn
wfOsiL1RouteNextHopCircuit = _WfOsiL1RouteNextHopCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1, 7),
    _WfOsiL1RouteNextHopCircuit_Type()
)
wfOsiL1RouteNextHopCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1RouteNextHopCircuit.setStatus("mandatory")
_WfOsiL1RouteDefaultMetricCost_Type = Integer32
_WfOsiL1RouteDefaultMetricCost_Object = MibTableColumn
wfOsiL1RouteDefaultMetricCost = _WfOsiL1RouteDefaultMetricCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 10, 1, 8),
    _WfOsiL1RouteDefaultMetricCost_Type()
)
wfOsiL1RouteDefaultMetricCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL1RouteDefaultMetricCost.setStatus("mandatory")
_WfOsiL2RoutesTable_Object = MibTable
wfOsiL2RoutesTable = _WfOsiL2RoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11)
)
if mibBuilder.loadTexts:
    wfOsiL2RoutesTable.setStatus("mandatory")
_WfOsiL2RouteEntry_Object = MibTableRow
wfOsiL2RouteEntry = _WfOsiL2RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1)
)
wfOsiL2RouteEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiL2RouteType"),
    (0, "Wellfleet-OSI-MIB", "wfOsiL2RoutePathSplit"),
    (0, "Wellfleet-OSI-MIB", "wfOsiL2RouteId"),
)
if mibBuilder.loadTexts:
    wfOsiL2RouteEntry.setStatus("mandatory")


class _WfOsiL2RouteId_Type(OctetString):
    """Custom type wfOsiL2RouteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_WfOsiL2RouteId_Type.__name__ = "OctetString"
_WfOsiL2RouteId_Object = MibTableColumn
wfOsiL2RouteId = _WfOsiL2RouteId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1, 1),
    _WfOsiL2RouteId_Type()
)
wfOsiL2RouteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2RouteId.setStatus("mandatory")
_WfOsiL2RoutePathSplit_Type = Integer32
_WfOsiL2RoutePathSplit_Object = MibTableColumn
wfOsiL2RoutePathSplit = _WfOsiL2RoutePathSplit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1, 2),
    _WfOsiL2RoutePathSplit_Type()
)
wfOsiL2RoutePathSplit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2RoutePathSplit.setStatus("mandatory")
_WfOsiL2RouteType_Type = Integer32
_WfOsiL2RouteType_Object = MibTableColumn
wfOsiL2RouteType = _WfOsiL2RouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1, 3),
    _WfOsiL2RouteType_Type()
)
wfOsiL2RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2RouteType.setStatus("mandatory")
_WfOsiL2RouteNextHopSnpa_Type = OctetString
_WfOsiL2RouteNextHopSnpa_Object = MibTableColumn
wfOsiL2RouteNextHopSnpa = _WfOsiL2RouteNextHopSnpa_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1, 4),
    _WfOsiL2RouteNextHopSnpa_Type()
)
wfOsiL2RouteNextHopSnpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2RouteNextHopSnpa.setStatus("mandatory")
_WfOsiL2RouteNextHopId_Type = OctetString
_WfOsiL2RouteNextHopId_Object = MibTableColumn
wfOsiL2RouteNextHopId = _WfOsiL2RouteNextHopId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1, 5),
    _WfOsiL2RouteNextHopId_Type()
)
wfOsiL2RouteNextHopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2RouteNextHopId.setStatus("mandatory")
_WfOsiL2RouteNextHopType_Type = Integer32
_WfOsiL2RouteNextHopType_Object = MibTableColumn
wfOsiL2RouteNextHopType = _WfOsiL2RouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1, 6),
    _WfOsiL2RouteNextHopType_Type()
)
wfOsiL2RouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2RouteNextHopType.setStatus("mandatory")
_WfOsiL2RouteNextHopCircuit_Type = Integer32
_WfOsiL2RouteNextHopCircuit_Object = MibTableColumn
wfOsiL2RouteNextHopCircuit = _WfOsiL2RouteNextHopCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1, 7),
    _WfOsiL2RouteNextHopCircuit_Type()
)
wfOsiL2RouteNextHopCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2RouteNextHopCircuit.setStatus("mandatory")
_WfOsiL2RouteDefaultMetricCost_Type = Integer32
_WfOsiL2RouteDefaultMetricCost_Object = MibTableColumn
wfOsiL2RouteDefaultMetricCost = _WfOsiL2RouteDefaultMetricCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 11, 1, 8),
    _WfOsiL2RouteDefaultMetricCost_Type()
)
wfOsiL2RouteDefaultMetricCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiL2RouteDefaultMetricCost.setStatus("mandatory")
_WfOsiDecnetTrans_ObjectIdentity = ObjectIdentity
wfOsiDecnetTrans = _WfOsiDecnetTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12)
)


class _WfOsiDecnetTransDelete_Type(Integer32):
    """Custom type wfOsiDecnetTransDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiDecnetTransDelete_Type.__name__ = "Integer32"
_WfOsiDecnetTransDelete_Object = MibScalar
wfOsiDecnetTransDelete = _WfOsiDecnetTransDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12, 1),
    _WfOsiDecnetTransDelete_Type()
)
wfOsiDecnetTransDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiDecnetTransDelete.setStatus("mandatory")


class _WfOsiDecnetTransDisable_Type(Integer32):
    """Custom type wfOsiDecnetTransDisable based on Integer32"""
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


_WfOsiDecnetTransDisable_Type.__name__ = "Integer32"
_WfOsiDecnetTransDisable_Object = MibScalar
wfOsiDecnetTransDisable = _WfOsiDecnetTransDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12, 2),
    _WfOsiDecnetTransDisable_Type()
)
wfOsiDecnetTransDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiDecnetTransDisable.setStatus("mandatory")


class _WfOsiDecnetTransState_Type(Integer32):
    """Custom type wfOsiDecnetTransState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfOsiDecnetTransState_Type.__name__ = "Integer32"
_WfOsiDecnetTransState_Object = MibScalar
wfOsiDecnetTransState = _WfOsiDecnetTransState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12, 3),
    _WfOsiDecnetTransState_Type()
)
wfOsiDecnetTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDecnetTransState.setStatus("mandatory")
_WfOsiDecnetTransPhase4Pkts_Type = Counter32
_WfOsiDecnetTransPhase4Pkts_Object = MibScalar
wfOsiDecnetTransPhase4Pkts = _WfOsiDecnetTransPhase4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12, 4),
    _WfOsiDecnetTransPhase4Pkts_Type()
)
wfOsiDecnetTransPhase4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDecnetTransPhase4Pkts.setStatus("mandatory")
_WfOsiDecnetTransSegFail_Type = Counter32
_WfOsiDecnetTransSegFail_Object = MibScalar
wfOsiDecnetTransSegFail = _WfOsiDecnetTransSegFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12, 5),
    _WfOsiDecnetTransSegFail_Type()
)
wfOsiDecnetTransSegFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDecnetTransSegFail.setStatus("mandatory")
_WfOsiDecnetTransNselFail_Type = Counter32
_WfOsiDecnetTransNselFail_Object = MibScalar
wfOsiDecnetTransNselFail = _WfOsiDecnetTransNselFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12, 6),
    _WfOsiDecnetTransNselFail_Type()
)
wfOsiDecnetTransNselFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDecnetTransNselFail.setStatus("mandatory")
_WfOsiDecnetTransUnrFail_Type = Counter32
_WfOsiDecnetTransUnrFail_Object = MibScalar
wfOsiDecnetTransUnrFail = _WfOsiDecnetTransUnrFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12, 7),
    _WfOsiDecnetTransUnrFail_Type()
)
wfOsiDecnetTransUnrFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDecnetTransUnrFail.setStatus("mandatory")
_WfOsiDecnetTransNumPhase4Es_Type = Counter32
_WfOsiDecnetTransNumPhase4Es_Object = MibScalar
wfOsiDecnetTransNumPhase4Es = _WfOsiDecnetTransNumPhase4Es_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 12, 8),
    _WfOsiDecnetTransNumPhase4Es_Type()
)
wfOsiDecnetTransNumPhase4Es.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiDecnetTransNumPhase4Es.setStatus("mandatory")
_WfOsiAreaAddressTable_Object = MibTable
wfOsiAreaAddressTable = _WfOsiAreaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 13)
)
if mibBuilder.loadTexts:
    wfOsiAreaAddressTable.setStatus("mandatory")
_WfOsiAreaAddressEntry_Object = MibTableRow
wfOsiAreaAddressEntry = _WfOsiAreaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 13, 1)
)
wfOsiAreaAddressEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiAreaAddress"),
)
if mibBuilder.loadTexts:
    wfOsiAreaAddressEntry.setStatus("mandatory")


class _WfOsiAreaAddrDelete_Type(Integer32):
    """Custom type wfOsiAreaAddrDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiAreaAddrDelete_Type.__name__ = "Integer32"
_WfOsiAreaAddrDelete_Object = MibTableColumn
wfOsiAreaAddrDelete = _WfOsiAreaAddrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 13, 1, 1),
    _WfOsiAreaAddrDelete_Type()
)
wfOsiAreaAddrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiAreaAddrDelete.setStatus("mandatory")


class _WfOsiAreaAddrDisable_Type(Integer32):
    """Custom type wfOsiAreaAddrDisable based on Integer32"""
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


_WfOsiAreaAddrDisable_Type.__name__ = "Integer32"
_WfOsiAreaAddrDisable_Object = MibTableColumn
wfOsiAreaAddrDisable = _WfOsiAreaAddrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 13, 1, 2),
    _WfOsiAreaAddrDisable_Type()
)
wfOsiAreaAddrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiAreaAddrDisable.setStatus("mandatory")


class _WfOsiAreaAddress_Type(OctetString):
    """Custom type wfOsiAreaAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 13),
    )


_WfOsiAreaAddress_Type.__name__ = "OctetString"
_WfOsiAreaAddress_Object = MibTableColumn
wfOsiAreaAddress = _WfOsiAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 13, 1, 3),
    _WfOsiAreaAddress_Type()
)
wfOsiAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiAreaAddress.setStatus("mandatory")
_WfOsiTarpEntry_ObjectIdentity = ObjectIdentity
wfOsiTarpEntry = _WfOsiTarpEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14)
)


class _WfOsiTarpCreate_Type(Integer32):
    """Custom type wfOsiTarpCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiTarpCreate_Type.__name__ = "Integer32"
_WfOsiTarpCreate_Object = MibScalar
wfOsiTarpCreate = _WfOsiTarpCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 1),
    _WfOsiTarpCreate_Type()
)
wfOsiTarpCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpCreate.setStatus("mandatory")


class _WfOsiTarpEnable_Type(Integer32):
    """Custom type wfOsiTarpEnable based on Integer32"""
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


_WfOsiTarpEnable_Type.__name__ = "Integer32"
_WfOsiTarpEnable_Object = MibScalar
wfOsiTarpEnable = _WfOsiTarpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 2),
    _WfOsiTarpEnable_Type()
)
wfOsiTarpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpEnable.setStatus("mandatory")


class _WfOsiTarpState_Type(Integer32):
    """Custom type wfOsiTarpState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfOsiTarpState_Type.__name__ = "Integer32"
_WfOsiTarpState_Object = MibScalar
wfOsiTarpState = _WfOsiTarpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 3),
    _WfOsiTarpState_Type()
)
wfOsiTarpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpState.setStatus("mandatory")
_WfOsiTarpTID_Type = DisplayString
_WfOsiTarpTID_Object = MibScalar
wfOsiTarpTID = _WfOsiTarpTID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 4),
    _WfOsiTarpTID_Type()
)
wfOsiTarpTID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpTID.setStatus("mandatory")


class _WfOsiTarpOriginate_Type(Integer32):
    """Custom type wfOsiTarpOriginate based on Integer32"""
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


_WfOsiTarpOriginate_Type.__name__ = "Integer32"
_WfOsiTarpOriginate_Object = MibScalar
wfOsiTarpOriginate = _WfOsiTarpOriginate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 5),
    _WfOsiTarpOriginate_Type()
)
wfOsiTarpOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpOriginate.setStatus("mandatory")


class _WfOsiTarpLifetime_Type(Integer32):
    """Custom type wfOsiTarpLifetime based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfOsiTarpLifetime_Type.__name__ = "Integer32"
_WfOsiTarpLifetime_Object = MibScalar
wfOsiTarpLifetime = _WfOsiTarpLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 6),
    _WfOsiTarpLifetime_Type()
)
wfOsiTarpLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpLifetime.setStatus("mandatory")


class _WfOsiTarpStartSeq_Type(Integer32):
    """Custom type wfOsiTarpStartSeq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfOsiTarpStartSeq_Type.__name__ = "Integer32"
_WfOsiTarpStartSeq_Object = MibScalar
wfOsiTarpStartSeq = _WfOsiTarpStartSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 7),
    _WfOsiTarpStartSeq_Type()
)
wfOsiTarpStartSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpStartSeq.setStatus("mandatory")


class _WfOsiTarpNextSeq_Type(Integer32):
    """Custom type wfOsiTarpNextSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfOsiTarpNextSeq_Type.__name__ = "Integer32"
_WfOsiTarpNextSeq_Object = MibScalar
wfOsiTarpNextSeq = _WfOsiTarpNextSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 8),
    _WfOsiTarpNextSeq_Type()
)
wfOsiTarpNextSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpNextSeq.setStatus("mandatory")


class _WfOsiTarpTarPro_Type(Integer32):
    """Custom type wfOsiTarpTarPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfOsiTarpTarPro_Type.__name__ = "Integer32"
_WfOsiTarpTarPro_Object = MibScalar
wfOsiTarpTarPro = _WfOsiTarpTarPro_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 9),
    _WfOsiTarpTarPro_Type()
)
wfOsiTarpTarPro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpTarPro.setStatus("mandatory")


class _WfOsiTarpTDC_Type(Integer32):
    """Custom type wfOsiTarpTDC based on Integer32"""
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


_WfOsiTarpTDC_Type.__name__ = "Integer32"
_WfOsiTarpTDC_Object = MibScalar
wfOsiTarpTDC = _WfOsiTarpTDC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 10),
    _WfOsiTarpTDC_Type()
)
wfOsiTarpTDC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpTDC.setStatus("mandatory")


class _WfOsiTarpL2TDC_Type(Integer32):
    """Custom type wfOsiTarpL2TDC based on Integer32"""
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


_WfOsiTarpL2TDC_Type.__name__ = "Integer32"
_WfOsiTarpL2TDC_Object = MibScalar
wfOsiTarpL2TDC = _WfOsiTarpL2TDC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 11),
    _WfOsiTarpL2TDC_Type()
)
wfOsiTarpL2TDC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpL2TDC.setStatus("mandatory")


class _WfOsiTarpT1_Type(Integer32):
    """Custom type wfOsiTarpT1 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_WfOsiTarpT1_Type.__name__ = "Integer32"
_WfOsiTarpT1_Object = MibScalar
wfOsiTarpT1 = _WfOsiTarpT1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 12),
    _WfOsiTarpT1_Type()
)
wfOsiTarpT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpT1.setStatus("mandatory")


class _WfOsiTarpT2_Type(Integer32):
    """Custom type wfOsiTarpT2 based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_WfOsiTarpT2_Type.__name__ = "Integer32"
_WfOsiTarpT2_Object = MibScalar
wfOsiTarpT2 = _WfOsiTarpT2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 13),
    _WfOsiTarpT2_Type()
)
wfOsiTarpT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpT2.setStatus("mandatory")


class _WfOsiTarpT3_Type(Integer32):
    """Custom type wfOsiTarpT3 based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_WfOsiTarpT3_Type.__name__ = "Integer32"
_WfOsiTarpT3_Object = MibScalar
wfOsiTarpT3 = _WfOsiTarpT3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 14),
    _WfOsiTarpT3_Type()
)
wfOsiTarpT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpT3.setStatus("mandatory")


class _WfOsiTarpT4_Type(Integer32):
    """Custom type wfOsiTarpT4 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_WfOsiTarpT4_Type.__name__ = "Integer32"
_WfOsiTarpT4_Object = MibScalar
wfOsiTarpT4 = _WfOsiTarpT4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 15),
    _WfOsiTarpT4_Type()
)
wfOsiTarpT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpT4.setStatus("mandatory")


class _WfOsiTarpLDBTimer_Type(Integer32):
    """Custom type wfOsiTarpLDBTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WfOsiTarpLDBTimer_Type.__name__ = "Integer32"
_WfOsiTarpLDBTimer_Object = MibScalar
wfOsiTarpLDBTimer = _WfOsiTarpLDBTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 16),
    _WfOsiTarpLDBTimer_Type()
)
wfOsiTarpLDBTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpLDBTimer.setStatus("mandatory")


class _WfOsiTarpLDBFlush_Type(Integer32):
    """Custom type wfOsiTarpLDBFlush based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_WfOsiTarpLDBFlush_Type.__name__ = "Integer32"
_WfOsiTarpLDBFlush_Object = MibScalar
wfOsiTarpLDBFlush = _WfOsiTarpLDBFlush_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 17),
    _WfOsiTarpLDBFlush_Type()
)
wfOsiTarpLDBFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpLDBFlush.setStatus("mandatory")


class _WfOsiTarpLDBSize_Type(Integer32):
    """Custom type wfOsiTarpLDBSize based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_WfOsiTarpLDBSize_Type.__name__ = "Integer32"
_WfOsiTarpLDBSize_Object = MibScalar
wfOsiTarpLDBSize = _WfOsiTarpLDBSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 18),
    _WfOsiTarpLDBSize_Type()
)
wfOsiTarpLDBSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpLDBSize.setStatus("mandatory")
_WfOsiTarpType1Rcv_Type = Counter32
_WfOsiTarpType1Rcv_Object = MibScalar
wfOsiTarpType1Rcv = _WfOsiTarpType1Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 19),
    _WfOsiTarpType1Rcv_Type()
)
wfOsiTarpType1Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType1Rcv.setStatus("mandatory")
_WfOsiTarpType1Xmt_Type = Counter32
_WfOsiTarpType1Xmt_Object = MibScalar
wfOsiTarpType1Xmt = _WfOsiTarpType1Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 20),
    _WfOsiTarpType1Xmt_Type()
)
wfOsiTarpType1Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType1Xmt.setStatus("mandatory")
_WfOsiTarpType2Rcv_Type = Counter32
_WfOsiTarpType2Rcv_Object = MibScalar
wfOsiTarpType2Rcv = _WfOsiTarpType2Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 21),
    _WfOsiTarpType2Rcv_Type()
)
wfOsiTarpType2Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType2Rcv.setStatus("mandatory")
_WfOsiTarpType2Xmt_Type = Counter32
_WfOsiTarpType2Xmt_Object = MibScalar
wfOsiTarpType2Xmt = _WfOsiTarpType2Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 22),
    _WfOsiTarpType2Xmt_Type()
)
wfOsiTarpType2Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType2Xmt.setStatus("mandatory")
_WfOsiTarpType3Rcv_Type = Counter32
_WfOsiTarpType3Rcv_Object = MibScalar
wfOsiTarpType3Rcv = _WfOsiTarpType3Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 23),
    _WfOsiTarpType3Rcv_Type()
)
wfOsiTarpType3Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType3Rcv.setStatus("mandatory")
_WfOsiTarpType3Xmt_Type = Counter32
_WfOsiTarpType3Xmt_Object = MibScalar
wfOsiTarpType3Xmt = _WfOsiTarpType3Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 24),
    _WfOsiTarpType3Xmt_Type()
)
wfOsiTarpType3Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType3Xmt.setStatus("mandatory")
_WfOsiTarpType4Rcv_Type = Counter32
_WfOsiTarpType4Rcv_Object = MibScalar
wfOsiTarpType4Rcv = _WfOsiTarpType4Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 25),
    _WfOsiTarpType4Rcv_Type()
)
wfOsiTarpType4Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType4Rcv.setStatus("mandatory")
_WfOsiTarpType4Xmt_Type = Counter32
_WfOsiTarpType4Xmt_Object = MibScalar
wfOsiTarpType4Xmt = _WfOsiTarpType4Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 26),
    _WfOsiTarpType4Xmt_Type()
)
wfOsiTarpType4Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType4Xmt.setStatus("mandatory")
_WfOsiTarpType5Rcv_Type = Counter32
_WfOsiTarpType5Rcv_Object = MibScalar
wfOsiTarpType5Rcv = _WfOsiTarpType5Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 27),
    _WfOsiTarpType5Rcv_Type()
)
wfOsiTarpType5Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType5Rcv.setStatus("mandatory")
_WfOsiTarpType5Xmt_Type = Counter32
_WfOsiTarpType5Xmt_Object = MibScalar
wfOsiTarpType5Xmt = _WfOsiTarpType5Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 14, 28),
    _WfOsiTarpType5Xmt_Type()
)
wfOsiTarpType5Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpType5Xmt.setStatus("mandatory")
_WfOsiTarpCircuitTable_Object = MibTable
wfOsiTarpCircuitTable = _WfOsiTarpCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15)
)
if mibBuilder.loadTexts:
    wfOsiTarpCircuitTable.setStatus("mandatory")
_WfOsiTarpCircuitEntry_Object = MibTableRow
wfOsiTarpCircuitEntry = _WfOsiTarpCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1)
)
wfOsiTarpCircuitEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiTarpCircuitCct"),
)
if mibBuilder.loadTexts:
    wfOsiTarpCircuitEntry.setStatus("mandatory")


class _WfOsiTarpCircuitCreate_Type(Integer32):
    """Custom type wfOsiTarpCircuitCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiTarpCircuitCreate_Type.__name__ = "Integer32"
_WfOsiTarpCircuitCreate_Object = MibTableColumn
wfOsiTarpCircuitCreate = _WfOsiTarpCircuitCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 1),
    _WfOsiTarpCircuitCreate_Type()
)
wfOsiTarpCircuitCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitCreate.setStatus("mandatory")


class _WfOsiTarpCircuitEnable_Type(Integer32):
    """Custom type wfOsiTarpCircuitEnable based on Integer32"""
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


_WfOsiTarpCircuitEnable_Type.__name__ = "Integer32"
_WfOsiTarpCircuitEnable_Object = MibTableColumn
wfOsiTarpCircuitEnable = _WfOsiTarpCircuitEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 2),
    _WfOsiTarpCircuitEnable_Type()
)
wfOsiTarpCircuitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitEnable.setStatus("mandatory")


class _WfOsiTarpCircuitState_Type(Integer32):
    """Custom type wfOsiTarpCircuitState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfOsiTarpCircuitState_Type.__name__ = "Integer32"
_WfOsiTarpCircuitState_Object = MibTableColumn
wfOsiTarpCircuitState = _WfOsiTarpCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 3),
    _WfOsiTarpCircuitState_Type()
)
wfOsiTarpCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitState.setStatus("mandatory")
_WfOsiTarpCircuitCct_Type = Integer32
_WfOsiTarpCircuitCct_Object = MibTableColumn
wfOsiTarpCircuitCct = _WfOsiTarpCircuitCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 4),
    _WfOsiTarpCircuitCct_Type()
)
wfOsiTarpCircuitCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitCct.setStatus("mandatory")


class _WfOsiTarpCircuitPropagate_Type(Integer32):
    """Custom type wfOsiTarpCircuitPropagate based on Integer32"""
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


_WfOsiTarpCircuitPropagate_Type.__name__ = "Integer32"
_WfOsiTarpCircuitPropagate_Object = MibTableColumn
wfOsiTarpCircuitPropagate = _WfOsiTarpCircuitPropagate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 5),
    _WfOsiTarpCircuitPropagate_Type()
)
wfOsiTarpCircuitPropagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitPropagate.setStatus("mandatory")


class _WfOsiTarpCircuitOriginate_Type(Integer32):
    """Custom type wfOsiTarpCircuitOriginate based on Integer32"""
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


_WfOsiTarpCircuitOriginate_Type.__name__ = "Integer32"
_WfOsiTarpCircuitOriginate_Object = MibTableColumn
wfOsiTarpCircuitOriginate = _WfOsiTarpCircuitOriginate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 6),
    _WfOsiTarpCircuitOriginate_Type()
)
wfOsiTarpCircuitOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitOriginate.setStatus("mandatory")
_WfOsiTarpCircuitType1Rcv_Type = Counter32
_WfOsiTarpCircuitType1Rcv_Object = MibTableColumn
wfOsiTarpCircuitType1Rcv = _WfOsiTarpCircuitType1Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 7),
    _WfOsiTarpCircuitType1Rcv_Type()
)
wfOsiTarpCircuitType1Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType1Rcv.setStatus("mandatory")
_WfOsiTarpCircuitType1Xmt_Type = Counter32
_WfOsiTarpCircuitType1Xmt_Object = MibTableColumn
wfOsiTarpCircuitType1Xmt = _WfOsiTarpCircuitType1Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 8),
    _WfOsiTarpCircuitType1Xmt_Type()
)
wfOsiTarpCircuitType1Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType1Xmt.setStatus("mandatory")
_WfOsiTarpCircuitType2Rcv_Type = Counter32
_WfOsiTarpCircuitType2Rcv_Object = MibTableColumn
wfOsiTarpCircuitType2Rcv = _WfOsiTarpCircuitType2Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 9),
    _WfOsiTarpCircuitType2Rcv_Type()
)
wfOsiTarpCircuitType2Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType2Rcv.setStatus("mandatory")
_WfOsiTarpCircuitType2Xmt_Type = Counter32
_WfOsiTarpCircuitType2Xmt_Object = MibTableColumn
wfOsiTarpCircuitType2Xmt = _WfOsiTarpCircuitType2Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 10),
    _WfOsiTarpCircuitType2Xmt_Type()
)
wfOsiTarpCircuitType2Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType2Xmt.setStatus("mandatory")
_WfOsiTarpCircuitType3Rcv_Type = Counter32
_WfOsiTarpCircuitType3Rcv_Object = MibTableColumn
wfOsiTarpCircuitType3Rcv = _WfOsiTarpCircuitType3Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 11),
    _WfOsiTarpCircuitType3Rcv_Type()
)
wfOsiTarpCircuitType3Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType3Rcv.setStatus("mandatory")
_WfOsiTarpCircuitType3Xmt_Type = Counter32
_WfOsiTarpCircuitType3Xmt_Object = MibTableColumn
wfOsiTarpCircuitType3Xmt = _WfOsiTarpCircuitType3Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 12),
    _WfOsiTarpCircuitType3Xmt_Type()
)
wfOsiTarpCircuitType3Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType3Xmt.setStatus("mandatory")
_WfOsiTarpCircuitType4Rcv_Type = Counter32
_WfOsiTarpCircuitType4Rcv_Object = MibTableColumn
wfOsiTarpCircuitType4Rcv = _WfOsiTarpCircuitType4Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 13),
    _WfOsiTarpCircuitType4Rcv_Type()
)
wfOsiTarpCircuitType4Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType4Rcv.setStatus("mandatory")
_WfOsiTarpCircuitType4Xmt_Type = Counter32
_WfOsiTarpCircuitType4Xmt_Object = MibTableColumn
wfOsiTarpCircuitType4Xmt = _WfOsiTarpCircuitType4Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 14),
    _WfOsiTarpCircuitType4Xmt_Type()
)
wfOsiTarpCircuitType4Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType4Xmt.setStatus("mandatory")
_WfOsiTarpCircuitType5Rcv_Type = Counter32
_WfOsiTarpCircuitType5Rcv_Object = MibTableColumn
wfOsiTarpCircuitType5Rcv = _WfOsiTarpCircuitType5Rcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 15),
    _WfOsiTarpCircuitType5Rcv_Type()
)
wfOsiTarpCircuitType5Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType5Rcv.setStatus("mandatory")
_WfOsiTarpCircuitType5Xmt_Type = Counter32
_WfOsiTarpCircuitType5Xmt_Object = MibTableColumn
wfOsiTarpCircuitType5Xmt = _WfOsiTarpCircuitType5Xmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 16),
    _WfOsiTarpCircuitType5Xmt_Type()
)
wfOsiTarpCircuitType5Xmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitType5Xmt.setStatus("mandatory")
_WfOsiTarpCircuitNoBufs_Type = Counter32
_WfOsiTarpCircuitNoBufs_Object = MibTableColumn
wfOsiTarpCircuitNoBufs = _WfOsiTarpCircuitNoBufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 15, 1, 17),
    _WfOsiTarpCircuitNoBufs_Type()
)
wfOsiTarpCircuitNoBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpCircuitNoBufs.setStatus("mandatory")
_WfOsiTarpLDBTable_Object = MibTable
wfOsiTarpLDBTable = _WfOsiTarpLDBTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 16)
)
if mibBuilder.loadTexts:
    wfOsiTarpLDBTable.setStatus("mandatory")
_WfOsiTarpLDBEntry_Object = MibTableRow
wfOsiTarpLDBEntry = _WfOsiTarpLDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 16, 1)
)
wfOsiTarpLDBEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiTarpLDBNSAP"),
)
if mibBuilder.loadTexts:
    wfOsiTarpLDBEntry.setStatus("mandatory")


class _WfOsiTarpLDBCreate_Type(Integer32):
    """Custom type wfOsiTarpLDBCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiTarpLDBCreate_Type.__name__ = "Integer32"
_WfOsiTarpLDBCreate_Object = MibTableColumn
wfOsiTarpLDBCreate = _WfOsiTarpLDBCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 16, 1, 1),
    _WfOsiTarpLDBCreate_Type()
)
wfOsiTarpLDBCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpLDBCreate.setStatus("mandatory")
_WfOsiTarpLDBNSAP_Type = OctetString
_WfOsiTarpLDBNSAP_Object = MibTableColumn
wfOsiTarpLDBNSAP = _WfOsiTarpLDBNSAP_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 16, 1, 2),
    _WfOsiTarpLDBNSAP_Type()
)
wfOsiTarpLDBNSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpLDBNSAP.setStatus("mandatory")


class _WfOsiTarpLDBSequence_Type(Integer32):
    """Custom type wfOsiTarpLDBSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfOsiTarpLDBSequence_Type.__name__ = "Integer32"
_WfOsiTarpLDBSequence_Object = MibTableColumn
wfOsiTarpLDBSequence = _WfOsiTarpLDBSequence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 16, 1, 3),
    _WfOsiTarpLDBSequence_Type()
)
wfOsiTarpLDBSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpLDBSequence.setStatus("mandatory")


class _WfOsiTarpLDBCurrentTimer_Type(Integer32):
    """Custom type wfOsiTarpLDBCurrentTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WfOsiTarpLDBCurrentTimer_Type.__name__ = "Integer32"
_WfOsiTarpLDBCurrentTimer_Object = MibTableColumn
wfOsiTarpLDBCurrentTimer = _WfOsiTarpLDBCurrentTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 16, 1, 4),
    _WfOsiTarpLDBCurrentTimer_Type()
)
wfOsiTarpLDBCurrentTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpLDBCurrentTimer.setStatus("mandatory")
_WfOsiTarpStaticAdjTable_Object = MibTable
wfOsiTarpStaticAdjTable = _WfOsiTarpStaticAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 17)
)
if mibBuilder.loadTexts:
    wfOsiTarpStaticAdjTable.setStatus("mandatory")
_WfOsiTarpStaticAdjEntry_Object = MibTableRow
wfOsiTarpStaticAdjEntry = _WfOsiTarpStaticAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 17, 1)
)
wfOsiTarpStaticAdjEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiTarpStaticAdjNSAP"),
)
if mibBuilder.loadTexts:
    wfOsiTarpStaticAdjEntry.setStatus("mandatory")


class _WfOsiTarpStaticAdjCreate_Type(Integer32):
    """Custom type wfOsiTarpStaticAdjCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiTarpStaticAdjCreate_Type.__name__ = "Integer32"
_WfOsiTarpStaticAdjCreate_Object = MibTableColumn
wfOsiTarpStaticAdjCreate = _WfOsiTarpStaticAdjCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 17, 1, 1),
    _WfOsiTarpStaticAdjCreate_Type()
)
wfOsiTarpStaticAdjCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpStaticAdjCreate.setStatus("mandatory")


class _WfOsiTarpStaticAdjEnable_Type(Integer32):
    """Custom type wfOsiTarpStaticAdjEnable based on Integer32"""
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


_WfOsiTarpStaticAdjEnable_Type.__name__ = "Integer32"
_WfOsiTarpStaticAdjEnable_Object = MibTableColumn
wfOsiTarpStaticAdjEnable = _WfOsiTarpStaticAdjEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 17, 1, 2),
    _WfOsiTarpStaticAdjEnable_Type()
)
wfOsiTarpStaticAdjEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpStaticAdjEnable.setStatus("mandatory")


class _WfOsiTarpStaticAdjNSAP_Type(OctetString):
    """Custom type wfOsiTarpStaticAdjNSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WfOsiTarpStaticAdjNSAP_Type.__name__ = "OctetString"
_WfOsiTarpStaticAdjNSAP_Object = MibTableColumn
wfOsiTarpStaticAdjNSAP = _WfOsiTarpStaticAdjNSAP_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 17, 1, 3),
    _WfOsiTarpStaticAdjNSAP_Type()
)
wfOsiTarpStaticAdjNSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpStaticAdjNSAP.setStatus("mandatory")
_WfOsiTarpStaticNibbleLength_Type = Integer32
_WfOsiTarpStaticNibbleLength_Object = MibTableColumn
wfOsiTarpStaticNibbleLength = _WfOsiTarpStaticNibbleLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 17, 1, 4),
    _WfOsiTarpStaticNibbleLength_Type()
)
wfOsiTarpStaticNibbleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpStaticNibbleLength.setStatus("mandatory")
_WfOsiTarpIgnoreAdjTable_Object = MibTable
wfOsiTarpIgnoreAdjTable = _WfOsiTarpIgnoreAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 18)
)
if mibBuilder.loadTexts:
    wfOsiTarpIgnoreAdjTable.setStatus("mandatory")
_WfOsiTarpIgnoreAdjEntry_Object = MibTableRow
wfOsiTarpIgnoreAdjEntry = _WfOsiTarpIgnoreAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 18, 1)
)
wfOsiTarpIgnoreAdjEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiTarpIgnoreAdjNSAP"),
)
if mibBuilder.loadTexts:
    wfOsiTarpIgnoreAdjEntry.setStatus("mandatory")


class _WfOsiTarpIgnoreAdjCreate_Type(Integer32):
    """Custom type wfOsiTarpIgnoreAdjCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiTarpIgnoreAdjCreate_Type.__name__ = "Integer32"
_WfOsiTarpIgnoreAdjCreate_Object = MibTableColumn
wfOsiTarpIgnoreAdjCreate = _WfOsiTarpIgnoreAdjCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 18, 1, 1),
    _WfOsiTarpIgnoreAdjCreate_Type()
)
wfOsiTarpIgnoreAdjCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpIgnoreAdjCreate.setStatus("mandatory")


class _WfOsiTarpIgnoreAdjEnable_Type(Integer32):
    """Custom type wfOsiTarpIgnoreAdjEnable based on Integer32"""
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


_WfOsiTarpIgnoreAdjEnable_Type.__name__ = "Integer32"
_WfOsiTarpIgnoreAdjEnable_Object = MibTableColumn
wfOsiTarpIgnoreAdjEnable = _WfOsiTarpIgnoreAdjEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 18, 1, 2),
    _WfOsiTarpIgnoreAdjEnable_Type()
)
wfOsiTarpIgnoreAdjEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpIgnoreAdjEnable.setStatus("mandatory")


class _WfOsiTarpIgnoreAdjNSAP_Type(OctetString):
    """Custom type wfOsiTarpIgnoreAdjNSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WfOsiTarpIgnoreAdjNSAP_Type.__name__ = "OctetString"
_WfOsiTarpIgnoreAdjNSAP_Object = MibTableColumn
wfOsiTarpIgnoreAdjNSAP = _WfOsiTarpIgnoreAdjNSAP_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 18, 1, 3),
    _WfOsiTarpIgnoreAdjNSAP_Type()
)
wfOsiTarpIgnoreAdjNSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiTarpIgnoreAdjNSAP.setStatus("mandatory")
_WfOsiTarpIgnoreNibbleLength_Type = Integer32
_WfOsiTarpIgnoreNibbleLength_Object = MibTableColumn
wfOsiTarpIgnoreNibbleLength = _WfOsiTarpIgnoreNibbleLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 18, 1, 4),
    _WfOsiTarpIgnoreNibbleLength_Type()
)
wfOsiTarpIgnoreNibbleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiTarpIgnoreNibbleLength.setStatus("mandatory")
_WfOsiGreAdjTable_Object = MibTable
wfOsiGreAdjTable = _WfOsiGreAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 19)
)
if mibBuilder.loadTexts:
    wfOsiGreAdjTable.setStatus("mandatory")
_WfOsiGreAdjEntry_Object = MibTableRow
wfOsiGreAdjEntry = _WfOsiGreAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 19, 1)
)
wfOsiGreAdjEntry.setIndexNames(
    (0, "Wellfleet-OSI-MIB", "wfOsiGreAdjTnlNum"),
    (0, "Wellfleet-OSI-MIB", "wfOsiGreAdjConnNum"),
)
if mibBuilder.loadTexts:
    wfOsiGreAdjEntry.setStatus("mandatory")


class _WfOsiGreAdjDelete_Type(Integer32):
    """Custom type wfOsiGreAdjDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOsiGreAdjDelete_Type.__name__ = "Integer32"
_WfOsiGreAdjDelete_Object = MibTableColumn
wfOsiGreAdjDelete = _WfOsiGreAdjDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 19, 1, 1),
    _WfOsiGreAdjDelete_Type()
)
wfOsiGreAdjDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiGreAdjDelete.setStatus("mandatory")


class _WfOsiGreAdjDisable_Type(Integer32):
    """Custom type wfOsiGreAdjDisable based on Integer32"""
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


_WfOsiGreAdjDisable_Type.__name__ = "Integer32"
_WfOsiGreAdjDisable_Object = MibTableColumn
wfOsiGreAdjDisable = _WfOsiGreAdjDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 19, 1, 2),
    _WfOsiGreAdjDisable_Type()
)
wfOsiGreAdjDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiGreAdjDisable.setStatus("mandatory")
_WfOsiGreAdjTnlNum_Type = Integer32
_WfOsiGreAdjTnlNum_Object = MibTableColumn
wfOsiGreAdjTnlNum = _WfOsiGreAdjTnlNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 19, 1, 3),
    _WfOsiGreAdjTnlNum_Type()
)
wfOsiGreAdjTnlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiGreAdjTnlNum.setStatus("mandatory")
_WfOsiGreAdjConnNum_Type = Integer32
_WfOsiGreAdjConnNum_Object = MibTableColumn
wfOsiGreAdjConnNum = _WfOsiGreAdjConnNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 19, 1, 4),
    _WfOsiGreAdjConnNum_Type()
)
wfOsiGreAdjConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOsiGreAdjConnNum.setStatus("mandatory")
_WfOsiGreAdjRemoteISId_Type = IpAddress
_WfOsiGreAdjRemoteISId_Object = MibTableColumn
wfOsiGreAdjRemoteISId = _WfOsiGreAdjRemoteISId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 19, 1, 5),
    _WfOsiGreAdjRemoteISId_Type()
)
wfOsiGreAdjRemoteISId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiGreAdjRemoteISId.setStatus("mandatory")
_WfOsiGreAdjCircuitId_Type = Integer32
_WfOsiGreAdjCircuitId_Object = MibTableColumn
wfOsiGreAdjCircuitId = _WfOsiGreAdjCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6, 19, 1, 6),
    _WfOsiGreAdjCircuitId_Type()
)
wfOsiGreAdjCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOsiGreAdjCircuitId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-OSI-MIB",
    **{"wfOsi": wfOsi,
       "wfOsiDelete": wfOsiDelete,
       "wfOsiDisable": wfOsiDisable,
       "wfOsiState": wfOsiState,
       "wfOsiIsisVersion": wfOsiIsisVersion,
       "wfOsiRouterType": wfOsiRouterType,
       "wfOsiRouterId": wfOsiRouterId,
       "wfOsiLoadBal": wfOsiLoadBal,
       "wfOsiMaxAreas": wfOsiMaxAreas,
       "wfOsiMaxEs": wfOsiMaxEs,
       "wfOsiMaxL1Is": wfOsiMaxL1Is,
       "wfOsiMaxL2Is": wfOsiMaxL2Is,
       "wfOsiMaxExtAddr": wfOsiMaxExtAddr,
       "wfOsiCksumIsPdus": wfOsiCksumIsPdus,
       "wfOsiL1LspPassword": wfOsiL1LspPassword,
       "wfOsiL2LspPassword": wfOsiL2LspPassword,
       "wfOsiAreaAddr": wfOsiAreaAddr,
       "wfOsiAreaAddrAlias1": wfOsiAreaAddrAlias1,
       "wfOsiAreaAddrAlias2": wfOsiAreaAddrAlias2,
       "wfOsiCorruptedLsps": wfOsiCorruptedLsps,
       "wfOsiL1LspDbOverloads": wfOsiL1LspDbOverloads,
       "wfOsiL2LspDbOverloads": wfOsiL2LspDbOverloads,
       "wfOsiManAddrDroppedAreas": wfOsiManAddrDroppedAreas,
       "wfOsiSeqNumberSkips": wfOsiSeqNumberSkips,
       "wfOsiOwnLspPurges": wfOsiOwnLspPurges,
       "wfOsiOthLspPurges": wfOsiOthLspPurges,
       "wfOsiExceedMaxSeqNums": wfOsiExceedMaxSeqNums,
       "wfOsiNearestL2Is": wfOsiNearestL2Is,
       "wfOsiMaxDynEs": wfOsiMaxDynEs,
       "wfOsiMaxDynL1Is": wfOsiMaxDynL1Is,
       "wfOsiMaxDynL2Is": wfOsiMaxDynL2Is,
       "wfOsiNumDynEsAdjs": wfOsiNumDynEsAdjs,
       "wfOsiNumDynL1Adjs": wfOsiNumDynL1Adjs,
       "wfOsiNumDynL2Adjs": wfOsiNumDynL2Adjs,
       "wfOsiNumL1Routes": wfOsiNumL1Routes,
       "wfOsiNumL2Routes": wfOsiNumL2Routes,
       "wfOsiNumDynPtpEsAdjs": wfOsiNumDynPtpEsAdjs,
       "wfOsiNumDynPtpIsAdjs": wfOsiNumDynPtpIsAdjs,
       "wfOsiClnpSrcRtOptionDisable": wfOsiClnpSrcRtOptionDisable,
       "wfOsiNumL1Lsps": wfOsiNumL1Lsps,
       "wfOsiNumL2Lsps": wfOsiNumL2Lsps,
       "wfOsiFletchRelaxedEnable": wfOsiFletchRelaxedEnable,
       "wfOsiStaticRouteTable": wfOsiStaticRouteTable,
       "wfOsiStaticRouteEntry": wfOsiStaticRouteEntry,
       "wfOsiStaticRouteDelete": wfOsiStaticRouteDelete,
       "wfOsiStaticRouteDisable": wfOsiStaticRouteDisable,
       "wfOsiStaticRouteAddr": wfOsiStaticRouteAddr,
       "wfOsiStaticRouteNibbleLength": wfOsiStaticRouteNibbleLength,
       "wfOsiStaticRouteNextHopIs": wfOsiStaticRouteNextHopIs,
       "wfOsiStaticRouteType": wfOsiStaticRouteType,
       "wfOsiStaticRouteCost": wfOsiStaticRouteCost,
       "wfOsiCircuitTable": wfOsiCircuitTable,
       "wfOsiCircuitEntry": wfOsiCircuitEntry,
       "wfOsiCircuitDelete": wfOsiCircuitDelete,
       "wfOsiCircuitDisable": wfOsiCircuitDisable,
       "wfOsiCircuitState": wfOsiCircuitState,
       "wfOsiCircuitId": wfOsiCircuitId,
       "wfOsiCircuitRouterLevel": wfOsiCircuitRouterLevel,
       "wfOsiCircuitL1DefaultMetric": wfOsiCircuitL1DefaultMetric,
       "wfOsiCircuitL2DefaultMetric": wfOsiCircuitL2DefaultMetric,
       "wfOsiCircuitL1DrPriority": wfOsiCircuitL1DrPriority,
       "wfOsiCircuitL2DrPriority": wfOsiCircuitL2DrPriority,
       "wfOsiCircuitIsisHelloTimer": wfOsiCircuitIsisHelloTimer,
       "wfOsiCircuitEsisHelloTimer": wfOsiCircuitEsisHelloTimer,
       "wfOsiCircuitEshConfigTime": wfOsiCircuitEshConfigTime,
       "wfOsiCircuitPassword": wfOsiCircuitPassword,
       "wfOsiCircuitReceivedPkts": wfOsiCircuitReceivedPkts,
       "wfOsiCircuitSentPkts": wfOsiCircuitSentPkts,
       "wfOsiCircuitDroppedPkts": wfOsiCircuitDroppedPkts,
       "wfOsiCircuitFragmentedPdus": wfOsiCircuitFragmentedPdus,
       "wfOsiCircuitCongestionDiscards": wfOsiCircuitCongestionDiscards,
       "wfOsiCircuitAddrUnreachDiscards": wfOsiCircuitAddrUnreachDiscards,
       "wfOsiCircuitAgedPduDiscards": wfOsiCircuitAgedPduDiscards,
       "wfOsiCircuitPduFormatErrDiscards": wfOsiCircuitPduFormatErrDiscards,
       "wfOsiCircuitUnsuppOptsDiscards": wfOsiCircuitUnsuppOptsDiscards,
       "wfOsiCircuitSentErrorReports": wfOsiCircuitSentErrorReports,
       "wfOsiCircuitReceivedControlPdus": wfOsiCircuitReceivedControlPdus,
       "wfOsiCircuitSentControlPdus": wfOsiCircuitSentControlPdus,
       "wfOsiCircuitStateChanges": wfOsiCircuitStateChanges,
       "wfOsiCircuitAdjStateChanges": wfOsiCircuitAdjStateChanges,
       "wfOsiCircuitInitFailures": wfOsiCircuitInitFailures,
       "wfOsiCircuitRejectedAdjs": wfOsiCircuitRejectedAdjs,
       "wfOsiCircuitReceivedBadLsps": wfOsiCircuitReceivedBadLsps,
       "wfOsiCircuitReceivedBadSnps": wfOsiCircuitReceivedBadSnps,
       "wfOsiCircuitReceivedBadEshs": wfOsiCircuitReceivedBadEshs,
       "wfOsiCircuitReceivedBadL1Iihs": wfOsiCircuitReceivedBadL1Iihs,
       "wfOsiCircuitReceivedBadL2Iihs": wfOsiCircuitReceivedBadL2Iihs,
       "wfOsiCircuitL1DrChanges": wfOsiCircuitL1DrChanges,
       "wfOsiCircuitL2DrChanges": wfOsiCircuitL2DrChanges,
       "wfOsiCircuitClnpForwarding": wfOsiCircuitClnpForwarding,
       "wfOsiCircuitClnpDefaultLifeTime": wfOsiCircuitClnpDefaultLifeTime,
       "wfOsiCircuitClnpInReceives": wfOsiCircuitClnpInReceives,
       "wfOsiCircuitClnpInAddrErrors": wfOsiCircuitClnpInAddrErrors,
       "wfOsiCircuitClnpForwPdus": wfOsiCircuitClnpForwPdus,
       "wfOsiCircuitClnpInUnknownNlps": wfOsiCircuitClnpInUnknownNlps,
       "wfOsiCircuitClnpInDelivers": wfOsiCircuitClnpInDelivers,
       "wfOsiCircuitClnpInUnknownUlps": wfOsiCircuitClnpInUnknownUlps,
       "wfOsiCircuitClnpSegCreates": wfOsiCircuitClnpSegCreates,
       "wfOsiCircuitClnpInOpts": wfOsiCircuitClnpInOpts,
       "wfOsiCircuitClnpOutOpts": wfOsiCircuitClnpOutOpts,
       "wfOsiCircuitEsisEshIns": wfOsiCircuitEsisEshIns,
       "wfOsiCircuitEsisIshOuts": wfOsiCircuitEsisIshOuts,
       "wfOsiCircuitEsisRduOuts": wfOsiCircuitEsisRduOuts,
       "wfOsiCircuitL1DesignatedRouter": wfOsiCircuitL1DesignatedRouter,
       "wfOsiCircuitL2DesignatedRouter": wfOsiCircuitL2DesignatedRouter,
       "wfOsiCircuitClnpOutEchoReplies": wfOsiCircuitClnpOutEchoReplies,
       "wfOsiCircuitClnpOutEchoRequests": wfOsiCircuitClnpOutEchoRequests,
       "wfOsiCircuitClnpInEchoReplies": wfOsiCircuitClnpInEchoReplies,
       "wfOsiCircuitClnpInEchoRequests": wfOsiCircuitClnpInEchoRequests,
       "wfOsiCircuitNumDynEsAdjs": wfOsiCircuitNumDynEsAdjs,
       "wfOsiCircuitNumDynL1Adjs": wfOsiCircuitNumDynL1Adjs,
       "wfOsiCircuitNumDynL2Adjs": wfOsiCircuitNumDynL2Adjs,
       "wfOsiCircuitNumDynPtpIsAdjs": wfOsiCircuitNumDynPtpIsAdjs,
       "wfOsiCircuitNumDynPtpEsAdjs": wfOsiCircuitNumDynPtpEsAdjs,
       "wfOsiCircuitBadIshReceived": wfOsiCircuitBadIshReceived,
       "wfOsiCircuitEsisIshIns": wfOsiCircuitEsisIshIns,
       "wfOsiCircuitIihHoldMultiplier": wfOsiCircuitIihHoldMultiplier,
       "wfOsiCircuitIshHoldMultiplier": wfOsiCircuitIshHoldMultiplier,
       "wfOsiCircuitDisableRedirect": wfOsiCircuitDisableRedirect,
       "wfOsiExternalAddressTable": wfOsiExternalAddressTable,
       "wfOsiExternalAddressEntry": wfOsiExternalAddressEntry,
       "wfOsiExtAddrDelete": wfOsiExtAddrDelete,
       "wfOsiExtAddrDisable": wfOsiExtAddrDisable,
       "wfOsiExtAddr": wfOsiExtAddr,
       "wfOsiExtAddrCircuit": wfOsiExtAddrCircuit,
       "wfOsiExtAddrNibbleLength": wfOsiExtAddrNibbleLength,
       "wfOsiExtAddrSnpa": wfOsiExtAddrSnpa,
       "wfOsiExtAddrCost": wfOsiExtAddrCost,
       "wfOsiStaticEsTable": wfOsiStaticEsTable,
       "wfOsiStaticEsEntry": wfOsiStaticEsEntry,
       "wfOsiStaticEsDelete": wfOsiStaticEsDelete,
       "wfOsiStaticEsDisable": wfOsiStaticEsDisable,
       "wfOsiStaticEsId": wfOsiStaticEsId,
       "wfOsiStaticEsCircuit": wfOsiStaticEsCircuit,
       "wfOsiStaticEsSnpa": wfOsiStaticEsSnpa,
       "wfOsiTrafficFilterTable": wfOsiTrafficFilterTable,
       "wfOsiTrafficFilterEntry": wfOsiTrafficFilterEntry,
       "wfOsiTrafficFilterDelete": wfOsiTrafficFilterDelete,
       "wfOsiTrafficFilterDisable": wfOsiTrafficFilterDisable,
       "wfOsiTrafficFilterStatus": wfOsiTrafficFilterStatus,
       "wfOsiTrafficFilterCounter": wfOsiTrafficFilterCounter,
       "wfOsiTrafficFilterDefinition": wfOsiTrafficFilterDefinition,
       "wfOsiTrafficFilterReserved": wfOsiTrafficFilterReserved,
       "wfOsiTrafficFilterCircuit": wfOsiTrafficFilterCircuit,
       "wfOsiTrafficFilterRuleNumber": wfOsiTrafficFilterRuleNumber,
       "wfOsiTrafficFilterFragment": wfOsiTrafficFilterFragment,
       "wfOsiTrafficFilterName": wfOsiTrafficFilterName,
       "wfOsiL1LspHdrTable": wfOsiL1LspHdrTable,
       "wfOsiL1LspHdrEntry": wfOsiL1LspHdrEntry,
       "wfOsiL1LspHdrLspId": wfOsiL1LspHdrLspId,
       "wfOsiL1LspHdrLifetime": wfOsiL1LspHdrLifetime,
       "wfOsiL1LspHdrSeqnum": wfOsiL1LspHdrSeqnum,
       "wfOsiL1LspHdrFlags": wfOsiL1LspHdrFlags,
       "wfOsiL1LspHdrCksum": wfOsiL1LspHdrCksum,
       "wfOsiL2LspHdrTable": wfOsiL2LspHdrTable,
       "wfOsiL2LspHdrEntry": wfOsiL2LspHdrEntry,
       "wfOsiL2LspHdrLspId": wfOsiL2LspHdrLspId,
       "wfOsiL2LspHdrLifetime": wfOsiL2LspHdrLifetime,
       "wfOsiL2LspHdrSeqnum": wfOsiL2LspHdrSeqnum,
       "wfOsiL2LspHdrFlags": wfOsiL2LspHdrFlags,
       "wfOsiL2LspHdrCksum": wfOsiL2LspHdrCksum,
       "wfOsiDynAdjTable": wfOsiDynAdjTable,
       "wfOsiDynAdjEntry": wfOsiDynAdjEntry,
       "wfOsiDynAdjId": wfOsiDynAdjId,
       "wfOsiDynAdjDatabase": wfOsiDynAdjDatabase,
       "wfOsiDynAdjType": wfOsiDynAdjType,
       "wfOsiDynAdjState": wfOsiDynAdjState,
       "wfOsiDynAdjCircuitId": wfOsiDynAdjCircuitId,
       "wfOsiDynAdjHoldTime": wfOsiDynAdjHoldTime,
       "wfOsiDynAdjPriority": wfOsiDynAdjPriority,
       "wfOsiDynAdjSnpaAddr": wfOsiDynAdjSnpaAddr,
       "wfOsiDynAdjNsapAddr": wfOsiDynAdjNsapAddr,
       "wfOsiDynAdjLanId": wfOsiDynAdjLanId,
       "wfOsiL1RoutesTable": wfOsiL1RoutesTable,
       "wfOsiL1RouteEntry": wfOsiL1RouteEntry,
       "wfOsiL1RouteId": wfOsiL1RouteId,
       "wfOsiL1RoutePathSplit": wfOsiL1RoutePathSplit,
       "wfOsiL1RouteType": wfOsiL1RouteType,
       "wfOsiL1RouteNextHopSnpa": wfOsiL1RouteNextHopSnpa,
       "wfOsiL1RouteNextHopId": wfOsiL1RouteNextHopId,
       "wfOsiL1RouteNextHopType": wfOsiL1RouteNextHopType,
       "wfOsiL1RouteNextHopCircuit": wfOsiL1RouteNextHopCircuit,
       "wfOsiL1RouteDefaultMetricCost": wfOsiL1RouteDefaultMetricCost,
       "wfOsiL2RoutesTable": wfOsiL2RoutesTable,
       "wfOsiL2RouteEntry": wfOsiL2RouteEntry,
       "wfOsiL2RouteId": wfOsiL2RouteId,
       "wfOsiL2RoutePathSplit": wfOsiL2RoutePathSplit,
       "wfOsiL2RouteType": wfOsiL2RouteType,
       "wfOsiL2RouteNextHopSnpa": wfOsiL2RouteNextHopSnpa,
       "wfOsiL2RouteNextHopId": wfOsiL2RouteNextHopId,
       "wfOsiL2RouteNextHopType": wfOsiL2RouteNextHopType,
       "wfOsiL2RouteNextHopCircuit": wfOsiL2RouteNextHopCircuit,
       "wfOsiL2RouteDefaultMetricCost": wfOsiL2RouteDefaultMetricCost,
       "wfOsiDecnetTrans": wfOsiDecnetTrans,
       "wfOsiDecnetTransDelete": wfOsiDecnetTransDelete,
       "wfOsiDecnetTransDisable": wfOsiDecnetTransDisable,
       "wfOsiDecnetTransState": wfOsiDecnetTransState,
       "wfOsiDecnetTransPhase4Pkts": wfOsiDecnetTransPhase4Pkts,
       "wfOsiDecnetTransSegFail": wfOsiDecnetTransSegFail,
       "wfOsiDecnetTransNselFail": wfOsiDecnetTransNselFail,
       "wfOsiDecnetTransUnrFail": wfOsiDecnetTransUnrFail,
       "wfOsiDecnetTransNumPhase4Es": wfOsiDecnetTransNumPhase4Es,
       "wfOsiAreaAddressTable": wfOsiAreaAddressTable,
       "wfOsiAreaAddressEntry": wfOsiAreaAddressEntry,
       "wfOsiAreaAddrDelete": wfOsiAreaAddrDelete,
       "wfOsiAreaAddrDisable": wfOsiAreaAddrDisable,
       "wfOsiAreaAddress": wfOsiAreaAddress,
       "wfOsiTarpEntry": wfOsiTarpEntry,
       "wfOsiTarpCreate": wfOsiTarpCreate,
       "wfOsiTarpEnable": wfOsiTarpEnable,
       "wfOsiTarpState": wfOsiTarpState,
       "wfOsiTarpTID": wfOsiTarpTID,
       "wfOsiTarpOriginate": wfOsiTarpOriginate,
       "wfOsiTarpLifetime": wfOsiTarpLifetime,
       "wfOsiTarpStartSeq": wfOsiTarpStartSeq,
       "wfOsiTarpNextSeq": wfOsiTarpNextSeq,
       "wfOsiTarpTarPro": wfOsiTarpTarPro,
       "wfOsiTarpTDC": wfOsiTarpTDC,
       "wfOsiTarpL2TDC": wfOsiTarpL2TDC,
       "wfOsiTarpT1": wfOsiTarpT1,
       "wfOsiTarpT2": wfOsiTarpT2,
       "wfOsiTarpT3": wfOsiTarpT3,
       "wfOsiTarpT4": wfOsiTarpT4,
       "wfOsiTarpLDBTimer": wfOsiTarpLDBTimer,
       "wfOsiTarpLDBFlush": wfOsiTarpLDBFlush,
       "wfOsiTarpLDBSize": wfOsiTarpLDBSize,
       "wfOsiTarpType1Rcv": wfOsiTarpType1Rcv,
       "wfOsiTarpType1Xmt": wfOsiTarpType1Xmt,
       "wfOsiTarpType2Rcv": wfOsiTarpType2Rcv,
       "wfOsiTarpType2Xmt": wfOsiTarpType2Xmt,
       "wfOsiTarpType3Rcv": wfOsiTarpType3Rcv,
       "wfOsiTarpType3Xmt": wfOsiTarpType3Xmt,
       "wfOsiTarpType4Rcv": wfOsiTarpType4Rcv,
       "wfOsiTarpType4Xmt": wfOsiTarpType4Xmt,
       "wfOsiTarpType5Rcv": wfOsiTarpType5Rcv,
       "wfOsiTarpType5Xmt": wfOsiTarpType5Xmt,
       "wfOsiTarpCircuitTable": wfOsiTarpCircuitTable,
       "wfOsiTarpCircuitEntry": wfOsiTarpCircuitEntry,
       "wfOsiTarpCircuitCreate": wfOsiTarpCircuitCreate,
       "wfOsiTarpCircuitEnable": wfOsiTarpCircuitEnable,
       "wfOsiTarpCircuitState": wfOsiTarpCircuitState,
       "wfOsiTarpCircuitCct": wfOsiTarpCircuitCct,
       "wfOsiTarpCircuitPropagate": wfOsiTarpCircuitPropagate,
       "wfOsiTarpCircuitOriginate": wfOsiTarpCircuitOriginate,
       "wfOsiTarpCircuitType1Rcv": wfOsiTarpCircuitType1Rcv,
       "wfOsiTarpCircuitType1Xmt": wfOsiTarpCircuitType1Xmt,
       "wfOsiTarpCircuitType2Rcv": wfOsiTarpCircuitType2Rcv,
       "wfOsiTarpCircuitType2Xmt": wfOsiTarpCircuitType2Xmt,
       "wfOsiTarpCircuitType3Rcv": wfOsiTarpCircuitType3Rcv,
       "wfOsiTarpCircuitType3Xmt": wfOsiTarpCircuitType3Xmt,
       "wfOsiTarpCircuitType4Rcv": wfOsiTarpCircuitType4Rcv,
       "wfOsiTarpCircuitType4Xmt": wfOsiTarpCircuitType4Xmt,
       "wfOsiTarpCircuitType5Rcv": wfOsiTarpCircuitType5Rcv,
       "wfOsiTarpCircuitType5Xmt": wfOsiTarpCircuitType5Xmt,
       "wfOsiTarpCircuitNoBufs": wfOsiTarpCircuitNoBufs,
       "wfOsiTarpLDBTable": wfOsiTarpLDBTable,
       "wfOsiTarpLDBEntry": wfOsiTarpLDBEntry,
       "wfOsiTarpLDBCreate": wfOsiTarpLDBCreate,
       "wfOsiTarpLDBNSAP": wfOsiTarpLDBNSAP,
       "wfOsiTarpLDBSequence": wfOsiTarpLDBSequence,
       "wfOsiTarpLDBCurrentTimer": wfOsiTarpLDBCurrentTimer,
       "wfOsiTarpStaticAdjTable": wfOsiTarpStaticAdjTable,
       "wfOsiTarpStaticAdjEntry": wfOsiTarpStaticAdjEntry,
       "wfOsiTarpStaticAdjCreate": wfOsiTarpStaticAdjCreate,
       "wfOsiTarpStaticAdjEnable": wfOsiTarpStaticAdjEnable,
       "wfOsiTarpStaticAdjNSAP": wfOsiTarpStaticAdjNSAP,
       "wfOsiTarpStaticNibbleLength": wfOsiTarpStaticNibbleLength,
       "wfOsiTarpIgnoreAdjTable": wfOsiTarpIgnoreAdjTable,
       "wfOsiTarpIgnoreAdjEntry": wfOsiTarpIgnoreAdjEntry,
       "wfOsiTarpIgnoreAdjCreate": wfOsiTarpIgnoreAdjCreate,
       "wfOsiTarpIgnoreAdjEnable": wfOsiTarpIgnoreAdjEnable,
       "wfOsiTarpIgnoreAdjNSAP": wfOsiTarpIgnoreAdjNSAP,
       "wfOsiTarpIgnoreNibbleLength": wfOsiTarpIgnoreNibbleLength,
       "wfOsiGreAdjTable": wfOsiGreAdjTable,
       "wfOsiGreAdjEntry": wfOsiGreAdjEntry,
       "wfOsiGreAdjDelete": wfOsiGreAdjDelete,
       "wfOsiGreAdjDisable": wfOsiGreAdjDisable,
       "wfOsiGreAdjTnlNum": wfOsiGreAdjTnlNum,
       "wfOsiGreAdjConnNum": wfOsiGreAdjConnNum,
       "wfOsiGreAdjRemoteISId": wfOsiGreAdjRemoteISId,
       "wfOsiGreAdjCircuitId": wfOsiGreAdjCircuitId}
)
