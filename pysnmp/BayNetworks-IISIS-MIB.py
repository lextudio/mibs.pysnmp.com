# SNMP MIB module (BayNetworks-IISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BayNetworks-IISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:20 2024
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

(wfIisisGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIisisGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIisisGeneralGroup_ObjectIdentity = ObjectIdentity
wfIisisGeneralGroup = _WfIisisGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1)
)


class _WfIisisGeneralDelete_Type(Integer32):
    """Custom type wfIisisGeneralDelete based on Integer32"""
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


_WfIisisGeneralDelete_Type.__name__ = "Integer32"
_WfIisisGeneralDelete_Object = MibScalar
wfIisisGeneralDelete = _WfIisisGeneralDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 1),
    _WfIisisGeneralDelete_Type()
)
wfIisisGeneralDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisGeneralDelete.setStatus("mandatory")


class _WfIisisGeneralDisable_Type(Integer32):
    """Custom type wfIisisGeneralDisable based on Integer32"""
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


_WfIisisGeneralDisable_Type.__name__ = "Integer32"
_WfIisisGeneralDisable_Object = MibScalar
wfIisisGeneralDisable = _WfIisisGeneralDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 2),
    _WfIisisGeneralDisable_Type()
)
wfIisisGeneralDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisGeneralDisable.setStatus("mandatory")


class _WfIisisGeneralState_Type(Integer32):
    """Custom type wfIisisGeneralState based on Integer32"""
    defaultValue = 2

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
          ("invalid", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIisisGeneralState_Type.__name__ = "Integer32"
_WfIisisGeneralState_Object = MibScalar
wfIisisGeneralState = _WfIisisGeneralState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 3),
    _WfIisisGeneralState_Type()
)
wfIisisGeneralState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisGeneralState.setStatus("mandatory")
_WfIisisRouterId_Type = OctetString
_WfIisisRouterId_Object = MibScalar
wfIisisRouterId = _WfIisisRouterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 4),
    _WfIisisRouterId_Type()
)
wfIisisRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisRouterId.setStatus("mandatory")
_WfIisisVersion_Type = DisplayString
_WfIisisVersion_Object = MibScalar
wfIisisVersion = _WfIisisVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 5),
    _WfIisisVersion_Type()
)
wfIisisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisVersion.setStatus("mandatory")


class _WfIisisRouterType_Type(Integer32):
    """Custom type wfIisisRouterType based on Integer32"""
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
        *(("l1l2", 3),
          ("l1only", 1),
          ("l2only", 2))
    )


_WfIisisRouterType_Type.__name__ = "Integer32"
_WfIisisRouterType_Object = MibScalar
wfIisisRouterType = _WfIisisRouterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 6),
    _WfIisisRouterType_Type()
)
wfIisisRouterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisRouterType.setStatus("mandatory")


class _WfIisisSpfHoldDown_Type(Integer32):
    """Custom type wfIisisSpfHoldDown based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_WfIisisSpfHoldDown_Type.__name__ = "Integer32"
_WfIisisSpfHoldDown_Object = MibScalar
wfIisisSpfHoldDown = _WfIisisSpfHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 7),
    _WfIisisSpfHoldDown_Type()
)
wfIisisSpfHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisSpfHoldDown.setStatus("mandatory")


class _WfIisisPrimaryLogMask_Type(Gauge32):
    """Custom type wfIisisPrimaryLogMask based on Gauge32"""
    defaultValue = 287


_WfIisisPrimaryLogMask_Object = MibScalar
wfIisisPrimaryLogMask = _WfIisisPrimaryLogMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 8),
    _WfIisisPrimaryLogMask_Type()
)
wfIisisPrimaryLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisPrimaryLogMask.setStatus("mandatory")


class _WfIisisMaximumPath_Type(Integer32):
    """Custom type wfIisisMaximumPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WfIisisMaximumPath_Type.__name__ = "Integer32"
_WfIisisMaximumPath_Object = MibScalar
wfIisisMaximumPath = _WfIisisMaximumPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 9),
    _WfIisisMaximumPath_Type()
)
wfIisisMaximumPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisMaximumPath.setStatus("mandatory")


class _WfIisisMaxAreas_Type(Integer32):
    """Custom type wfIisisMaxAreas based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WfIisisMaxAreas_Type.__name__ = "Integer32"
_WfIisisMaxAreas_Object = MibScalar
wfIisisMaxAreas = _WfIisisMaxAreas_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 10),
    _WfIisisMaxAreas_Type()
)
wfIisisMaxAreas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisMaxAreas.setStatus("mandatory")
_WfIisisNumL1Lsps_Type = Gauge32
_WfIisisNumL1Lsps_Object = MibScalar
wfIisisNumL1Lsps = _WfIisisNumL1Lsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 11),
    _WfIisisNumL1Lsps_Type()
)
wfIisisNumL1Lsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisNumL1Lsps.setStatus("mandatory")
_WfIisisNumL2Lsps_Type = Gauge32
_WfIisisNumL2Lsps_Object = MibScalar
wfIisisNumL2Lsps = _WfIisisNumL2Lsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 12),
    _WfIisisNumL2Lsps_Type()
)
wfIisisNumL2Lsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisNumL2Lsps.setStatus("mandatory")


class _WfIisisCksumIsPdus_Type(Integer32):
    """Custom type wfIisisCksumIsPdus based on Integer32"""
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


_WfIisisCksumIsPdus_Type.__name__ = "Integer32"
_WfIisisCksumIsPdus_Object = MibScalar
wfIisisCksumIsPdus = _WfIisisCksumIsPdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 13),
    _WfIisisCksumIsPdus_Type()
)
wfIisisCksumIsPdus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisCksumIsPdus.setStatus("mandatory")
_WfIisisL1LspPassword_Type = DisplayString
_WfIisisL1LspPassword_Object = MibScalar
wfIisisL1LspPassword = _WfIisisL1LspPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 14),
    _WfIisisL1LspPassword_Type()
)
wfIisisL1LspPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisL1LspPassword.setStatus("mandatory")
_WfIisisL2LspPassword_Type = DisplayString
_WfIisisL2LspPassword_Object = MibScalar
wfIisisL2LspPassword = _WfIisisL2LspPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 15),
    _WfIisisL2LspPassword_Type()
)
wfIisisL2LspPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisL2LspPassword.setStatus("mandatory")
_WfIisisAreaAddr_Type = OctetString
_WfIisisAreaAddr_Object = MibScalar
wfIisisAreaAddr = _WfIisisAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 16),
    _WfIisisAreaAddr_Type()
)
wfIisisAreaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisAreaAddr.setStatus("mandatory")
_WfIisisAreaAddrAlias1_Type = OctetString
_WfIisisAreaAddrAlias1_Object = MibScalar
wfIisisAreaAddrAlias1 = _WfIisisAreaAddrAlias1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 17),
    _WfIisisAreaAddrAlias1_Type()
)
wfIisisAreaAddrAlias1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisAreaAddrAlias1.setStatus("mandatory")
_WfIisisAreaAddrAlias2_Type = OctetString
_WfIisisAreaAddrAlias2_Object = MibScalar
wfIisisAreaAddrAlias2 = _WfIisisAreaAddrAlias2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 18),
    _WfIisisAreaAddrAlias2_Type()
)
wfIisisAreaAddrAlias2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisAreaAddrAlias2.setStatus("mandatory")
_WfIisisL1CorruptedLsps_Type = Counter32
_WfIisisL1CorruptedLsps_Object = MibScalar
wfIisisL1CorruptedLsps = _WfIisisL1CorruptedLsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 19),
    _WfIisisL1CorruptedLsps_Type()
)
wfIisisL1CorruptedLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL1CorruptedLsps.setStatus("mandatory")
_WfIisisL2CorruptedLsps_Type = Counter32
_WfIisisL2CorruptedLsps_Object = MibScalar
wfIisisL2CorruptedLsps = _WfIisisL2CorruptedLsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 20),
    _WfIisisL2CorruptedLsps_Type()
)
wfIisisL2CorruptedLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL2CorruptedLsps.setStatus("mandatory")
_WfIisisL1LspDbOverLoads_Type = Counter32
_WfIisisL1LspDbOverLoads_Object = MibScalar
wfIisisL1LspDbOverLoads = _WfIisisL1LspDbOverLoads_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 21),
    _WfIisisL1LspDbOverLoads_Type()
)
wfIisisL1LspDbOverLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL1LspDbOverLoads.setStatus("mandatory")
_WfIisisL2LspDbOverLoads_Type = Counter32
_WfIisisL2LspDbOverLoads_Object = MibScalar
wfIisisL2LspDbOverLoads = _WfIisisL2LspDbOverLoads_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 22),
    _WfIisisL2LspDbOverLoads_Type()
)
wfIisisL2LspDbOverLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL2LspDbOverLoads.setStatus("mandatory")
_WfIisisNearestL2Is_Type = OctetString
_WfIisisNearestL2Is_Object = MibScalar
wfIisisNearestL2Is = _WfIisisNearestL2Is_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 23),
    _WfIisisNearestL2Is_Type()
)
wfIisisNearestL2Is.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisNearestL2Is.setStatus("mandatory")
_WfIisisNumL1Routes_Type = Gauge32
_WfIisisNumL1Routes_Object = MibScalar
wfIisisNumL1Routes = _WfIisisNumL1Routes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 24),
    _WfIisisNumL1Routes_Type()
)
wfIisisNumL1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisNumL1Routes.setStatus("mandatory")
_WfIisisNumL2Routes_Type = Gauge32
_WfIisisNumL2Routes_Object = MibScalar
wfIisisNumL2Routes = _WfIisisNumL2Routes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 25),
    _WfIisisNumL2Routes_Type()
)
wfIisisNumL2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisNumL2Routes.setStatus("mandatory")


class _WfIisisMinLSPGenerationInterval_Type(Integer32):
    """Custom type wfIisisMinLSPGenerationInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_WfIisisMinLSPGenerationInterval_Type.__name__ = "Integer32"
_WfIisisMinLSPGenerationInterval_Object = MibScalar
wfIisisMinLSPGenerationInterval = _WfIisisMinLSPGenerationInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 26),
    _WfIisisMinLSPGenerationInterval_Type()
)
wfIisisMinLSPGenerationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisMinLSPGenerationInterval.setStatus("mandatory")


class _WfIisisMaxLSPGenerationInterval_Type(Integer32):
    """Custom type wfIisisMaxLSPGenerationInterval based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 27000),
    )


_WfIisisMaxLSPGenerationInterval_Type.__name__ = "Integer32"
_WfIisisMaxLSPGenerationInterval_Object = MibScalar
wfIisisMaxLSPGenerationInterval = _WfIisisMaxLSPGenerationInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 27),
    _WfIisisMaxLSPGenerationInterval_Type()
)
wfIisisMaxLSPGenerationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisMaxLSPGenerationInterval.setStatus("mandatory")


class _WfIisisMaxAge_Type(Integer32):
    """Custom type wfIisisMaxAge based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 7200),
    )


_WfIisisMaxAge_Type.__name__ = "Integer32"
_WfIisisMaxAge_Object = MibScalar
wfIisisMaxAge = _WfIisisMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 28),
    _WfIisisMaxAge_Type()
)
wfIisisMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisMaxAge.setStatus("mandatory")


class _WfIisisMinLSPXmtInterval_Type(Integer32):
    """Custom type wfIisisMinLSPXmtInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfIisisMinLSPXmtInterval_Type.__name__ = "Integer32"
_WfIisisMinLSPXmtInterval_Object = MibScalar
wfIisisMinLSPXmtInterval = _WfIisisMinLSPXmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 29),
    _WfIisisMinLSPXmtInterval_Type()
)
wfIisisMinLSPXmtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisMinLSPXmtInterval.setStatus("mandatory")


class _WfIisisPartialSNPInterval_Type(Integer32):
    """Custom type wfIisisPartialSNPInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WfIisisPartialSNPInterval_Type.__name__ = "Integer32"
_WfIisisPartialSNPInterval_Object = MibScalar
wfIisisPartialSNPInterval = _WfIisisPartialSNPInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 30),
    _WfIisisPartialSNPInterval_Type()
)
wfIisisPartialSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisPartialSNPInterval.setStatus("mandatory")


class _WfIisisZeroAgeLifetime_Type(Integer32):
    """Custom type wfIisisZeroAgeLifetime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_WfIisisZeroAgeLifetime_Type.__name__ = "Integer32"
_WfIisisZeroAgeLifetime_Object = MibScalar
wfIisisZeroAgeLifetime = _WfIisisZeroAgeLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 31),
    _WfIisisZeroAgeLifetime_Type()
)
wfIisisZeroAgeLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisZeroAgeLifetime.setStatus("mandatory")


class _WfIisisAgePend_Type(Integer32):
    """Custom type wfIisisAgePend based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_WfIisisAgePend_Type.__name__ = "Integer32"
_WfIisisAgePend_Object = MibScalar
wfIisisAgePend = _WfIisisAgePend_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 32),
    _WfIisisAgePend_Type()
)
wfIisisAgePend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisAgePend.setStatus("mandatory")


class _WfIisisCsnpBuildInterval_Type(Integer32):
    """Custom type wfIisisCsnpBuildInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1200),
    )


_WfIisisCsnpBuildInterval_Type.__name__ = "Integer32"
_WfIisisCsnpBuildInterval_Object = MibScalar
wfIisisCsnpBuildInterval = _WfIisisCsnpBuildInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 33),
    _WfIisisCsnpBuildInterval_Type()
)
wfIisisCsnpBuildInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisCsnpBuildInterval.setStatus("mandatory")


class _WfIisisL2LspBufferSize_Type(Integer32):
    """Custom type wfIisisL2LspBufferSize based on Integer32"""
    defaultValue = 1497

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16384),
    )


_WfIisisL2LspBufferSize_Type.__name__ = "Integer32"
_WfIisisL2LspBufferSize_Object = MibScalar
wfIisisL2LspBufferSize = _WfIisisL2LspBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 34),
    _WfIisisL2LspBufferSize_Type()
)
wfIisisL2LspBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisL2LspBufferSize.setStatus("mandatory")
_WfIisisL1SpfCnt_Type = Counter32
_WfIisisL1SpfCnt_Object = MibScalar
wfIisisL1SpfCnt = _WfIisisL1SpfCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 35),
    _WfIisisL1SpfCnt_Type()
)
wfIisisL1SpfCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL1SpfCnt.setStatus("mandatory")
_WfIisisL2SpfCnt_Type = Counter32
_WfIisisL2SpfCnt_Object = MibScalar
wfIisisL2SpfCnt = _WfIisisL2SpfCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 1, 36),
    _WfIisisL2SpfCnt_Type()
)
wfIisisL2SpfCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL2SpfCnt.setStatus("mandatory")
_WfIisisAreaTable_Object = MibTable
wfIisisAreaTable = _WfIisisAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 2)
)
if mibBuilder.loadTexts:
    wfIisisAreaTable.setStatus("mandatory")
_WfIisisAreaEntry_Object = MibTableRow
wfIisisAreaEntry = _WfIisisAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 2, 1)
)
wfIisisAreaEntry.setIndexNames(
    (0, "BayNetworks-IISIS-MIB", "wfIisisAreaId"),
)
if mibBuilder.loadTexts:
    wfIisisAreaEntry.setStatus("mandatory")


class _WfIisisAreaDelete_Type(Integer32):
    """Custom type wfIisisAreaDelete based on Integer32"""
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


_WfIisisAreaDelete_Type.__name__ = "Integer32"
_WfIisisAreaDelete_Object = MibTableColumn
wfIisisAreaDelete = _WfIisisAreaDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 2, 1, 1),
    _WfIisisAreaDelete_Type()
)
wfIisisAreaDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisAreaDelete.setStatus("mandatory")


class _WfIisisAreaDisable_Type(Integer32):
    """Custom type wfIisisAreaDisable based on Integer32"""
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


_WfIisisAreaDisable_Type.__name__ = "Integer32"
_WfIisisAreaDisable_Object = MibTableColumn
wfIisisAreaDisable = _WfIisisAreaDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 2, 1, 2),
    _WfIisisAreaDisable_Type()
)
wfIisisAreaDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisAreaDisable.setStatus("mandatory")


class _WfIisisAreaState_Type(Integer32):
    """Custom type wfIisisAreaState based on Integer32"""
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


_WfIisisAreaState_Type.__name__ = "Integer32"
_WfIisisAreaState_Object = MibTableColumn
wfIisisAreaState = _WfIisisAreaState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 2, 1, 3),
    _WfIisisAreaState_Type()
)
wfIisisAreaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisAreaState.setStatus("mandatory")
_WfIisisAreaId_Type = IpAddress
_WfIisisAreaId_Object = MibTableColumn
wfIisisAreaId = _WfIisisAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 2, 1, 4),
    _WfIisisAreaId_Type()
)
wfIisisAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisAreaId.setStatus("mandatory")
_WfIisisSpfCnt_Type = Counter32
_WfIisisSpfCnt_Object = MibTableColumn
wfIisisSpfCnt = _WfIisisSpfCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 2, 1, 5),
    _WfIisisSpfCnt_Type()
)
wfIisisSpfCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisSpfCnt.setStatus("mandatory")
_WfIisisL1LspHdrTable_Object = MibTable
wfIisisL1LspHdrTable = _WfIisisL1LspHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 3)
)
if mibBuilder.loadTexts:
    wfIisisL1LspHdrTable.setStatus("mandatory")
_WfIisisL1LspHdrEntry_Object = MibTableRow
wfIisisL1LspHdrEntry = _WfIisisL1LspHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 3, 1)
)
wfIisisL1LspHdrEntry.setIndexNames(
    (0, "BayNetworks-IISIS-MIB", "wfIisisL1LspHdrLspId"),
)
if mibBuilder.loadTexts:
    wfIisisL1LspHdrEntry.setStatus("mandatory")


class _WfIisisL1LspHdrLspId_Type(OctetString):
    """Custom type wfIisisL1LspHdrLspId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfIisisL1LspHdrLspId_Type.__name__ = "OctetString"
_WfIisisL1LspHdrLspId_Object = MibTableColumn
wfIisisL1LspHdrLspId = _WfIisisL1LspHdrLspId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 3, 1, 1),
    _WfIisisL1LspHdrLspId_Type()
)
wfIisisL1LspHdrLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL1LspHdrLspId.setStatus("mandatory")
_WfIisisL1LspHdrLifetime_Type = Integer32
_WfIisisL1LspHdrLifetime_Object = MibTableColumn
wfIisisL1LspHdrLifetime = _WfIisisL1LspHdrLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 3, 1, 2),
    _WfIisisL1LspHdrLifetime_Type()
)
wfIisisL1LspHdrLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL1LspHdrLifetime.setStatus("mandatory")
_WfIisisL1LspHdrSeqnum_Type = Integer32
_WfIisisL1LspHdrSeqnum_Object = MibTableColumn
wfIisisL1LspHdrSeqnum = _WfIisisL1LspHdrSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 3, 1, 3),
    _WfIisisL1LspHdrSeqnum_Type()
)
wfIisisL1LspHdrSeqnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL1LspHdrSeqnum.setStatus("mandatory")
_WfIisisL1LspHdrFlags_Type = Integer32
_WfIisisL1LspHdrFlags_Object = MibTableColumn
wfIisisL1LspHdrFlags = _WfIisisL1LspHdrFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 3, 1, 4),
    _WfIisisL1LspHdrFlags_Type()
)
wfIisisL1LspHdrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL1LspHdrFlags.setStatus("mandatory")
_WfIisisL1LspHdrCksum_Type = OctetString
_WfIisisL1LspHdrCksum_Object = MibTableColumn
wfIisisL1LspHdrCksum = _WfIisisL1LspHdrCksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 3, 1, 5),
    _WfIisisL1LspHdrCksum_Type()
)
wfIisisL1LspHdrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL1LspHdrCksum.setStatus("mandatory")
_WfIisisL2LspHdrTable_Object = MibTable
wfIisisL2LspHdrTable = _WfIisisL2LspHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 4)
)
if mibBuilder.loadTexts:
    wfIisisL2LspHdrTable.setStatus("mandatory")
_WfIisisL2LspHdrEntry_Object = MibTableRow
wfIisisL2LspHdrEntry = _WfIisisL2LspHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 4, 1)
)
wfIisisL2LspHdrEntry.setIndexNames(
    (0, "BayNetworks-IISIS-MIB", "wfIisisL2LspHdrLspId"),
)
if mibBuilder.loadTexts:
    wfIisisL2LspHdrEntry.setStatus("mandatory")


class _WfIisisL2LspHdrLspId_Type(OctetString):
    """Custom type wfIisisL2LspHdrLspId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WfIisisL2LspHdrLspId_Type.__name__ = "OctetString"
_WfIisisL2LspHdrLspId_Object = MibTableColumn
wfIisisL2LspHdrLspId = _WfIisisL2LspHdrLspId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 4, 1, 1),
    _WfIisisL2LspHdrLspId_Type()
)
wfIisisL2LspHdrLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL2LspHdrLspId.setStatus("mandatory")
_WfIisisL2LspHdrLifetime_Type = Integer32
_WfIisisL2LspHdrLifetime_Object = MibTableColumn
wfIisisL2LspHdrLifetime = _WfIisisL2LspHdrLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 4, 1, 2),
    _WfIisisL2LspHdrLifetime_Type()
)
wfIisisL2LspHdrLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL2LspHdrLifetime.setStatus("mandatory")
_WfIisisL2LspHdrSeqnum_Type = Integer32
_WfIisisL2LspHdrSeqnum_Object = MibTableColumn
wfIisisL2LspHdrSeqnum = _WfIisisL2LspHdrSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 4, 1, 3),
    _WfIisisL2LspHdrSeqnum_Type()
)
wfIisisL2LspHdrSeqnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL2LspHdrSeqnum.setStatus("mandatory")
_WfIisisL2LspHdrFlags_Type = Integer32
_WfIisisL2LspHdrFlags_Object = MibTableColumn
wfIisisL2LspHdrFlags = _WfIisisL2LspHdrFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 4, 1, 4),
    _WfIisisL2LspHdrFlags_Type()
)
wfIisisL2LspHdrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL2LspHdrFlags.setStatus("mandatory")
_WfIisisL2LspHdrCksum_Type = OctetString
_WfIisisL2LspHdrCksum_Object = MibTableColumn
wfIisisL2LspHdrCksum = _WfIisisL2LspHdrCksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 4, 1, 5),
    _WfIisisL2LspHdrCksum_Type()
)
wfIisisL2LspHdrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisL2LspHdrCksum.setStatus("mandatory")
_WfIisisIfTable_Object = MibTable
wfIisisIfTable = _WfIisisIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5)
)
if mibBuilder.loadTexts:
    wfIisisIfTable.setStatus("mandatory")
_WfIisisIfEntry_Object = MibTableRow
wfIisisIfEntry = _WfIisisIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1)
)
wfIisisIfEntry.setIndexNames(
    (0, "BayNetworks-IISIS-MIB", "wfIisisIfIpAddress"),
    (0, "BayNetworks-IISIS-MIB", "wfIisisAddressLessIf"),
)
if mibBuilder.loadTexts:
    wfIisisIfEntry.setStatus("mandatory")


class _WfIisisIfDelete_Type(Integer32):
    """Custom type wfIisisIfDelete based on Integer32"""
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


_WfIisisIfDelete_Type.__name__ = "Integer32"
_WfIisisIfDelete_Object = MibTableColumn
wfIisisIfDelete = _WfIisisIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 1),
    _WfIisisIfDelete_Type()
)
wfIisisIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfDelete.setStatus("mandatory")


class _WfIisisIfDisable_Type(Integer32):
    """Custom type wfIisisIfDisable based on Integer32"""
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


_WfIisisIfDisable_Type.__name__ = "Integer32"
_WfIisisIfDisable_Object = MibTableColumn
wfIisisIfDisable = _WfIisisIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 2),
    _WfIisisIfDisable_Type()
)
wfIisisIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfDisable.setStatus("mandatory")
_WfIisisIfIpAddress_Type = IpAddress
_WfIisisIfIpAddress_Object = MibTableColumn
wfIisisIfIpAddress = _WfIisisIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 3),
    _WfIisisIfIpAddress_Type()
)
wfIisisIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfIpAddress.setStatus("mandatory")
_WfIisisAddressLessIf_Type = Integer32
_WfIisisAddressLessIf_Object = MibTableColumn
wfIisisAddressLessIf = _WfIisisAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 4),
    _WfIisisAddressLessIf_Type()
)
wfIisisAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisAddressLessIf.setStatus("mandatory")


class _WfIisisIfRouterLevel_Type(Integer32):
    """Custom type wfIisisIfRouterLevel based on Integer32"""
    defaultValue = 2

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


_WfIisisIfRouterLevel_Type.__name__ = "Integer32"
_WfIisisIfRouterLevel_Object = MibTableColumn
wfIisisIfRouterLevel = _WfIisisIfRouterLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 5),
    _WfIisisIfRouterLevel_Type()
)
wfIisisIfRouterLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfRouterLevel.setStatus("mandatory")


class _WfIisisIfL1DefaultMetric_Type(Integer32):
    """Custom type wfIisisIfL1DefaultMetric based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfIisisIfL1DefaultMetric_Type.__name__ = "Integer32"
_WfIisisIfL1DefaultMetric_Object = MibTableColumn
wfIisisIfL1DefaultMetric = _WfIisisIfL1DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 6),
    _WfIisisIfL1DefaultMetric_Type()
)
wfIisisIfL1DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfL1DefaultMetric.setStatus("mandatory")


class _WfIisisIfL2DefaultMetric_Type(Integer32):
    """Custom type wfIisisIfL2DefaultMetric based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfIisisIfL2DefaultMetric_Type.__name__ = "Integer32"
_WfIisisIfL2DefaultMetric_Object = MibTableColumn
wfIisisIfL2DefaultMetric = _WfIisisIfL2DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 7),
    _WfIisisIfL2DefaultMetric_Type()
)
wfIisisIfL2DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfL2DefaultMetric.setStatus("mandatory")


class _WfIisisIfL1DrPriority_Type(Integer32):
    """Custom type wfIisisIfL1DrPriority based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfIisisIfL1DrPriority_Type.__name__ = "Integer32"
_WfIisisIfL1DrPriority_Object = MibTableColumn
wfIisisIfL1DrPriority = _WfIisisIfL1DrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 8),
    _WfIisisIfL1DrPriority_Type()
)
wfIisisIfL1DrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfL1DrPriority.setStatus("mandatory")


class _WfIisisIfL2DrPriority_Type(Integer32):
    """Custom type wfIisisIfL2DrPriority based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfIisisIfL2DrPriority_Type.__name__ = "Integer32"
_WfIisisIfL2DrPriority_Object = MibTableColumn
wfIisisIfL2DrPriority = _WfIisisIfL2DrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 9),
    _WfIisisIfL2DrPriority_Type()
)
wfIisisIfL2DrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfL2DrPriority.setStatus("mandatory")


class _WfIisisIfHelloTimer_Type(Integer32):
    """Custom type wfIisisIfHelloTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21845),
    )


_WfIisisIfHelloTimer_Type.__name__ = "Integer32"
_WfIisisIfHelloTimer_Object = MibTableColumn
wfIisisIfHelloTimer = _WfIisisIfHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 10),
    _WfIisisIfHelloTimer_Type()
)
wfIisisIfHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfHelloTimer.setStatus("mandatory")
_WfIisisIfPassword_Type = DisplayString
_WfIisisIfPassword_Object = MibTableColumn
wfIisisIfPassword = _WfIisisIfPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 11),
    _WfIisisIfPassword_Type()
)
wfIisisIfPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfPassword.setStatus("mandatory")


class _WfIisisIfHelloMtuSize_Type(Integer32):
    """Custom type wfIisisIfHelloMtuSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_WfIisisIfHelloMtuSize_Type.__name__ = "Integer32"
_WfIisisIfHelloMtuSize_Object = MibTableColumn
wfIisisIfHelloMtuSize = _WfIisisIfHelloMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 12),
    _WfIisisIfHelloMtuSize_Type()
)
wfIisisIfHelloMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfHelloMtuSize.setStatus("mandatory")


class _WfIisisIfIihHoldMultiplier_Type(Integer32):
    """Custom type wfIisisIfIihHoldMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WfIisisIfIihHoldMultiplier_Type.__name__ = "Integer32"
_WfIisisIfIihHoldMultiplier_Object = MibTableColumn
wfIisisIfIihHoldMultiplier = _WfIisisIfIihHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 13),
    _WfIisisIfIihHoldMultiplier_Type()
)
wfIisisIfIihHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfIihHoldMultiplier.setStatus("mandatory")


class _WfIisisIfIshHoldMultiplier_Type(Integer32):
    """Custom type wfIisisIfIshHoldMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WfIisisIfIshHoldMultiplier_Type.__name__ = "Integer32"
_WfIisisIfIshHoldMultiplier_Object = MibTableColumn
wfIisisIfIshHoldMultiplier = _WfIisisIfIshHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 14),
    _WfIisisIfIshHoldMultiplier_Type()
)
wfIisisIfIshHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfIshHoldMultiplier.setStatus("mandatory")


class _WfIisisIfType_Type(Integer32):
    """Custom type wfIisisIfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("pointtopoint", 2))
    )


_WfIisisIfType_Type.__name__ = "Integer32"
_WfIisisIfType_Object = MibTableColumn
wfIisisIfType = _WfIisisIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 15),
    _WfIisisIfType_Type()
)
wfIisisIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfType.setStatus("mandatory")


class _WfIisisIfCsnpTimer_Type(Integer32):
    """Custom type wfIisisIfCsnpTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_WfIisisIfCsnpTimer_Type.__name__ = "Integer32"
_WfIisisIfCsnpTimer_Object = MibTableColumn
wfIisisIfCsnpTimer = _WfIisisIfCsnpTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 5, 1, 16),
    _WfIisisIfCsnpTimer_Type()
)
wfIisisIfCsnpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIisisIfCsnpTimer.setStatus("mandatory")
_WfIisisIfStatsTable_Object = MibTable
wfIisisIfStatsTable = _WfIisisIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6)
)
if mibBuilder.loadTexts:
    wfIisisIfStatsTable.setStatus("mandatory")
_WfIisisIfStatsEntry_Object = MibTableRow
wfIisisIfStatsEntry = _WfIisisIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1)
)
wfIisisIfStatsEntry.setIndexNames(
    (0, "BayNetworks-IISIS-MIB", "wfIisisIfStatsIpAddress"),
    (0, "BayNetworks-IISIS-MIB", "wfIisisStatsAddressLessIf"),
)
if mibBuilder.loadTexts:
    wfIisisIfStatsEntry.setStatus("mandatory")
_WfIisisIfStatsIpAddress_Type = IpAddress
_WfIisisIfStatsIpAddress_Object = MibTableColumn
wfIisisIfStatsIpAddress = _WfIisisIfStatsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 1),
    _WfIisisIfStatsIpAddress_Type()
)
wfIisisIfStatsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsIpAddress.setStatus("mandatory")
_WfIisisStatsAddressLessIf_Type = Integer32
_WfIisisStatsAddressLessIf_Object = MibTableColumn
wfIisisStatsAddressLessIf = _WfIisisStatsAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 2),
    _WfIisisStatsAddressLessIf_Type()
)
wfIisisStatsAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisStatsAddressLessIf.setStatus("mandatory")


class _WfIisisIfStatsState_Type(Integer32):
    """Custom type wfIisisIfStatsState based on Integer32"""
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


_WfIisisIfStatsState_Type.__name__ = "Integer32"
_WfIisisIfStatsState_Object = MibTableColumn
wfIisisIfStatsState = _WfIisisIfStatsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 3),
    _WfIisisIfStatsState_Type()
)
wfIisisIfStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsState.setStatus("mandatory")
_WfIisisIfStatsCct_Type = Integer32
_WfIisisIfStatsCct_Object = MibTableColumn
wfIisisIfStatsCct = _WfIisisIfStatsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 4),
    _WfIisisIfStatsCct_Type()
)
wfIisisIfStatsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsCct.setStatus("mandatory")
_WfIisisIfStatsL1TxHellos_Type = Counter32
_WfIisisIfStatsL1TxHellos_Object = MibTableColumn
wfIisisIfStatsL1TxHellos = _WfIisisIfStatsL1TxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 5),
    _WfIisisIfStatsL1TxHellos_Type()
)
wfIisisIfStatsL1TxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL1TxHellos.setStatus("mandatory")
_WfIisisIfStatsL2TxHellos_Type = Counter32
_WfIisisIfStatsL2TxHellos_Object = MibTableColumn
wfIisisIfStatsL2TxHellos = _WfIisisIfStatsL2TxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 6),
    _WfIisisIfStatsL2TxHellos_Type()
)
wfIisisIfStatsL2TxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL2TxHellos.setStatus("mandatory")
_WfIisisIfStatsL1RxHellos_Type = Counter32
_WfIisisIfStatsL1RxHellos_Object = MibTableColumn
wfIisisIfStatsL1RxHellos = _WfIisisIfStatsL1RxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 7),
    _WfIisisIfStatsL1RxHellos_Type()
)
wfIisisIfStatsL1RxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL1RxHellos.setStatus("mandatory")
_WfIisisIfStatsL2RxHellos_Type = Counter32
_WfIisisIfStatsL2RxHellos_Object = MibTableColumn
wfIisisIfStatsL2RxHellos = _WfIisisIfStatsL2RxHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 8),
    _WfIisisIfStatsL2RxHellos_Type()
)
wfIisisIfStatsL2RxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL2RxHellos.setStatus("mandatory")
_WfIisisIfStatsL1Drops_Type = Counter32
_WfIisisIfStatsL1Drops_Object = MibTableColumn
wfIisisIfStatsL1Drops = _WfIisisIfStatsL1Drops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 9),
    _WfIisisIfStatsL1Drops_Type()
)
wfIisisIfStatsL1Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL1Drops.setStatus("mandatory")
_WfIisisIfStatsL2Drops_Type = Counter32
_WfIisisIfStatsL2Drops_Object = MibTableColumn
wfIisisIfStatsL2Drops = _WfIisisIfStatsL2Drops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 10),
    _WfIisisIfStatsL2Drops_Type()
)
wfIisisIfStatsL2Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL2Drops.setStatus("mandatory")
_WfIisisIfStatsL1DesignatedRouter_Type = OctetString
_WfIisisIfStatsL1DesignatedRouter_Object = MibTableColumn
wfIisisIfStatsL1DesignatedRouter = _WfIisisIfStatsL1DesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 11),
    _WfIisisIfStatsL1DesignatedRouter_Type()
)
wfIisisIfStatsL1DesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL1DesignatedRouter.setStatus("mandatory")
_WfIisisIfStatsL2DesignatedRouter_Type = OctetString
_WfIisisIfStatsL2DesignatedRouter_Object = MibTableColumn
wfIisisIfStatsL2DesignatedRouter = _WfIisisIfStatsL2DesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 12),
    _WfIisisIfStatsL2DesignatedRouter_Type()
)
wfIisisIfStatsL2DesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL2DesignatedRouter.setStatus("mandatory")
_WfIisisIfStatsTxL1Lsp_Type = Counter32
_WfIisisIfStatsTxL1Lsp_Object = MibTableColumn
wfIisisIfStatsTxL1Lsp = _WfIisisIfStatsTxL1Lsp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 13),
    _WfIisisIfStatsTxL1Lsp_Type()
)
wfIisisIfStatsTxL1Lsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsTxL1Lsp.setStatus("mandatory")
_WfIisisIfStatsTxL2Lsp_Type = Counter32
_WfIisisIfStatsTxL2Lsp_Object = MibTableColumn
wfIisisIfStatsTxL2Lsp = _WfIisisIfStatsTxL2Lsp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 14),
    _WfIisisIfStatsTxL2Lsp_Type()
)
wfIisisIfStatsTxL2Lsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsTxL2Lsp.setStatus("mandatory")
_WfIisisIfStatsTxL1Csnp_Type = Counter32
_WfIisisIfStatsTxL1Csnp_Object = MibTableColumn
wfIisisIfStatsTxL1Csnp = _WfIisisIfStatsTxL1Csnp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 15),
    _WfIisisIfStatsTxL1Csnp_Type()
)
wfIisisIfStatsTxL1Csnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsTxL1Csnp.setStatus("mandatory")
_WfIisisIfStatsTxL2Csnp_Type = Counter32
_WfIisisIfStatsTxL2Csnp_Object = MibTableColumn
wfIisisIfStatsTxL2Csnp = _WfIisisIfStatsTxL2Csnp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 16),
    _WfIisisIfStatsTxL2Csnp_Type()
)
wfIisisIfStatsTxL2Csnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsTxL2Csnp.setStatus("mandatory")
_WfIisisIfStatsTxL1Psnp_Type = Counter32
_WfIisisIfStatsTxL1Psnp_Object = MibTableColumn
wfIisisIfStatsTxL1Psnp = _WfIisisIfStatsTxL1Psnp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 17),
    _WfIisisIfStatsTxL1Psnp_Type()
)
wfIisisIfStatsTxL1Psnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsTxL1Psnp.setStatus("mandatory")
_WfIisisIfStatsTxL2Psnp_Type = Counter32
_WfIisisIfStatsTxL2Psnp_Object = MibTableColumn
wfIisisIfStatsTxL2Psnp = _WfIisisIfStatsTxL2Psnp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 18),
    _WfIisisIfStatsTxL2Psnp_Type()
)
wfIisisIfStatsTxL2Psnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsTxL2Psnp.setStatus("mandatory")
_WfIisisIfStatsRxL1Lsp_Type = Counter32
_WfIisisIfStatsRxL1Lsp_Object = MibTableColumn
wfIisisIfStatsRxL1Lsp = _WfIisisIfStatsRxL1Lsp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 19),
    _WfIisisIfStatsRxL1Lsp_Type()
)
wfIisisIfStatsRxL1Lsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsRxL1Lsp.setStatus("mandatory")
_WfIisisIfStatsRxL2Lsp_Type = Counter32
_WfIisisIfStatsRxL2Lsp_Object = MibTableColumn
wfIisisIfStatsRxL2Lsp = _WfIisisIfStatsRxL2Lsp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 20),
    _WfIisisIfStatsRxL2Lsp_Type()
)
wfIisisIfStatsRxL2Lsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsRxL2Lsp.setStatus("mandatory")
_WfIisisIfStatsRxL1Csnp_Type = Counter32
_WfIisisIfStatsRxL1Csnp_Object = MibTableColumn
wfIisisIfStatsRxL1Csnp = _WfIisisIfStatsRxL1Csnp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 21),
    _WfIisisIfStatsRxL1Csnp_Type()
)
wfIisisIfStatsRxL1Csnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsRxL1Csnp.setStatus("mandatory")
_WfIisisIfStatsRxL2Csnp_Type = Counter32
_WfIisisIfStatsRxL2Csnp_Object = MibTableColumn
wfIisisIfStatsRxL2Csnp = _WfIisisIfStatsRxL2Csnp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 22),
    _WfIisisIfStatsRxL2Csnp_Type()
)
wfIisisIfStatsRxL2Csnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsRxL2Csnp.setStatus("mandatory")
_WfIisisIfStatsRxL1Psnp_Type = Counter32
_WfIisisIfStatsRxL1Psnp_Object = MibTableColumn
wfIisisIfStatsRxL1Psnp = _WfIisisIfStatsRxL1Psnp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 23),
    _WfIisisIfStatsRxL1Psnp_Type()
)
wfIisisIfStatsRxL1Psnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsRxL1Psnp.setStatus("mandatory")
_WfIisisIfStatsRxL2Psnp_Type = Counter32
_WfIisisIfStatsRxL2Psnp_Object = MibTableColumn
wfIisisIfStatsRxL2Psnp = _WfIisisIfStatsRxL2Psnp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 24),
    _WfIisisIfStatsRxL2Psnp_Type()
)
wfIisisIfStatsRxL2Psnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsRxL2Psnp.setStatus("mandatory")
_WfIisisIfStatsL1NbrCount_Type = Gauge32
_WfIisisIfStatsL1NbrCount_Object = MibTableColumn
wfIisisIfStatsL1NbrCount = _WfIisisIfStatsL1NbrCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 25),
    _WfIisisIfStatsL1NbrCount_Type()
)
wfIisisIfStatsL1NbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL1NbrCount.setStatus("mandatory")
_WfIisisIfStatsL2NbrCount_Type = Gauge32
_WfIisisIfStatsL2NbrCount_Object = MibTableColumn
wfIisisIfStatsL2NbrCount = _WfIisisIfStatsL2NbrCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 26),
    _WfIisisIfStatsL2NbrCount_Type()
)
wfIisisIfStatsL2NbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL2NbrCount.setStatus("mandatory")
_WfIisisIfStatsL1AdjCount_Type = Gauge32
_WfIisisIfStatsL1AdjCount_Object = MibTableColumn
wfIisisIfStatsL1AdjCount = _WfIisisIfStatsL1AdjCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 27),
    _WfIisisIfStatsL1AdjCount_Type()
)
wfIisisIfStatsL1AdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL1AdjCount.setStatus("mandatory")
_WfIisisIfStatsL2AdjCount_Type = Gauge32
_WfIisisIfStatsL2AdjCount_Object = MibTableColumn
wfIisisIfStatsL2AdjCount = _WfIisisIfStatsL2AdjCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 6, 1, 28),
    _WfIisisIfStatsL2AdjCount_Type()
)
wfIisisIfStatsL2AdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisIfStatsL2AdjCount.setStatus("mandatory")
_WfIisisDynNbrTable_Object = MibTable
wfIisisDynNbrTable = _WfIisisDynNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7)
)
if mibBuilder.loadTexts:
    wfIisisDynNbrTable.setStatus("mandatory")
_WfIisisDynNbrEntry_Object = MibTableRow
wfIisisDynNbrEntry = _WfIisisDynNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1)
)
wfIisisDynNbrEntry.setIndexNames(
    (0, "BayNetworks-IISIS-MIB", "wfIisisDynNbrIpAddr"),
    (0, "BayNetworks-IISIS-MIB", "wfIisisDynNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    wfIisisDynNbrEntry.setStatus("mandatory")


class _WfIisisDynNbrState_Type(Integer32):
    """Custom type wfIisisDynNbrState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("init", 2),
          ("up", 3))
    )


_WfIisisDynNbrState_Type.__name__ = "Integer32"
_WfIisisDynNbrState_Object = MibTableColumn
wfIisisDynNbrState = _WfIisisDynNbrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 1),
    _WfIisisDynNbrState_Type()
)
wfIisisDynNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrState.setStatus("mandatory")
_WfIisisDynNbrIpAddr_Type = IpAddress
_WfIisisDynNbrIpAddr_Object = MibTableColumn
wfIisisDynNbrIpAddr = _WfIisisDynNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 2),
    _WfIisisDynNbrIpAddr_Type()
)
wfIisisDynNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrIpAddr.setStatus("mandatory")
_WfIisisDynNbrIfAddr_Type = IpAddress
_WfIisisDynNbrIfAddr_Object = MibTableColumn
wfIisisDynNbrIfAddr = _WfIisisDynNbrIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 3),
    _WfIisisDynNbrIfAddr_Type()
)
wfIisisDynNbrIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrIfAddr.setStatus("mandatory")
_WfIisisDynNbrAddressLessIndex_Type = Integer32
_WfIisisDynNbrAddressLessIndex_Object = MibTableColumn
wfIisisDynNbrAddressLessIndex = _WfIisisDynNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 4),
    _WfIisisDynNbrAddressLessIndex_Type()
)
wfIisisDynNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrAddressLessIndex.setStatus("mandatory")
_WfIisisDynNbrRtrId_Type = OctetString
_WfIisisDynNbrRtrId_Object = MibTableColumn
wfIisisDynNbrRtrId = _WfIisisDynNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 5),
    _WfIisisDynNbrRtrId_Type()
)
wfIisisDynNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrRtrId.setStatus("mandatory")


class _WfIisisDynNbrDatabase_Type(Integer32):
    """Custom type wfIisisDynNbrDatabase based on Integer32"""
    defaultValue = 3


_WfIisisDynNbrDatabase_Object = MibTableColumn
wfIisisDynNbrDatabase = _WfIisisDynNbrDatabase_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 6),
    _WfIisisDynNbrDatabase_Type()
)
wfIisisDynNbrDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrDatabase.setStatus("mandatory")


class _WfIisisDynNbrType_Type(Integer32):
    """Custom type wfIisisDynNbrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("pointtopoint", 2))
    )


_WfIisisDynNbrType_Type.__name__ = "Integer32"
_WfIisisDynNbrType_Object = MibTableColumn
wfIisisDynNbrType = _WfIisisDynNbrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 7),
    _WfIisisDynNbrType_Type()
)
wfIisisDynNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrType.setStatus("mandatory")
_WfIisisDynNbrPseudonodeId_Type = Integer32
_WfIisisDynNbrPseudonodeId_Object = MibTableColumn
wfIisisDynNbrPseudonodeId = _WfIisisDynNbrPseudonodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 8),
    _WfIisisDynNbrPseudonodeId_Type()
)
wfIisisDynNbrPseudonodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrPseudonodeId.setStatus("mandatory")
_WfIisisDynNbrHoldTime_Type = Integer32
_WfIisisDynNbrHoldTime_Object = MibTableColumn
wfIisisDynNbrHoldTime = _WfIisisDynNbrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 9),
    _WfIisisDynNbrHoldTime_Type()
)
wfIisisDynNbrHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrHoldTime.setStatus("mandatory")
_WfIisisDynNbrPriority_Type = Integer32
_WfIisisDynNbrPriority_Object = MibTableColumn
wfIisisDynNbrPriority = _WfIisisDynNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 10),
    _WfIisisDynNbrPriority_Type()
)
wfIisisDynNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrPriority.setStatus("mandatory")
_WfIisisDynNbrSnpaAddr_Type = OctetString
_WfIisisDynNbrSnpaAddr_Object = MibTableColumn
wfIisisDynNbrSnpaAddr = _WfIisisDynNbrSnpaAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 11),
    _WfIisisDynNbrSnpaAddr_Type()
)
wfIisisDynNbrSnpaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrSnpaAddr.setStatus("mandatory")
_WfIisisDynNbrLanId_Type = OctetString
_WfIisisDynNbrLanId_Object = MibTableColumn
wfIisisDynNbrLanId = _WfIisisDynNbrLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8, 7, 1, 12),
    _WfIisisDynNbrLanId_Type()
)
wfIisisDynNbrLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIisisDynNbrLanId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BayNetworks-IISIS-MIB",
    **{"wfIisisGeneralGroup": wfIisisGeneralGroup,
       "wfIisisGeneralDelete": wfIisisGeneralDelete,
       "wfIisisGeneralDisable": wfIisisGeneralDisable,
       "wfIisisGeneralState": wfIisisGeneralState,
       "wfIisisRouterId": wfIisisRouterId,
       "wfIisisVersion": wfIisisVersion,
       "wfIisisRouterType": wfIisisRouterType,
       "wfIisisSpfHoldDown": wfIisisSpfHoldDown,
       "wfIisisPrimaryLogMask": wfIisisPrimaryLogMask,
       "wfIisisMaximumPath": wfIisisMaximumPath,
       "wfIisisMaxAreas": wfIisisMaxAreas,
       "wfIisisNumL1Lsps": wfIisisNumL1Lsps,
       "wfIisisNumL2Lsps": wfIisisNumL2Lsps,
       "wfIisisCksumIsPdus": wfIisisCksumIsPdus,
       "wfIisisL1LspPassword": wfIisisL1LspPassword,
       "wfIisisL2LspPassword": wfIisisL2LspPassword,
       "wfIisisAreaAddr": wfIisisAreaAddr,
       "wfIisisAreaAddrAlias1": wfIisisAreaAddrAlias1,
       "wfIisisAreaAddrAlias2": wfIisisAreaAddrAlias2,
       "wfIisisL1CorruptedLsps": wfIisisL1CorruptedLsps,
       "wfIisisL2CorruptedLsps": wfIisisL2CorruptedLsps,
       "wfIisisL1LspDbOverLoads": wfIisisL1LspDbOverLoads,
       "wfIisisL2LspDbOverLoads": wfIisisL2LspDbOverLoads,
       "wfIisisNearestL2Is": wfIisisNearestL2Is,
       "wfIisisNumL1Routes": wfIisisNumL1Routes,
       "wfIisisNumL2Routes": wfIisisNumL2Routes,
       "wfIisisMinLSPGenerationInterval": wfIisisMinLSPGenerationInterval,
       "wfIisisMaxLSPGenerationInterval": wfIisisMaxLSPGenerationInterval,
       "wfIisisMaxAge": wfIisisMaxAge,
       "wfIisisMinLSPXmtInterval": wfIisisMinLSPXmtInterval,
       "wfIisisPartialSNPInterval": wfIisisPartialSNPInterval,
       "wfIisisZeroAgeLifetime": wfIisisZeroAgeLifetime,
       "wfIisisAgePend": wfIisisAgePend,
       "wfIisisCsnpBuildInterval": wfIisisCsnpBuildInterval,
       "wfIisisL2LspBufferSize": wfIisisL2LspBufferSize,
       "wfIisisL1SpfCnt": wfIisisL1SpfCnt,
       "wfIisisL2SpfCnt": wfIisisL2SpfCnt,
       "wfIisisAreaTable": wfIisisAreaTable,
       "wfIisisAreaEntry": wfIisisAreaEntry,
       "wfIisisAreaDelete": wfIisisAreaDelete,
       "wfIisisAreaDisable": wfIisisAreaDisable,
       "wfIisisAreaState": wfIisisAreaState,
       "wfIisisAreaId": wfIisisAreaId,
       "wfIisisSpfCnt": wfIisisSpfCnt,
       "wfIisisL1LspHdrTable": wfIisisL1LspHdrTable,
       "wfIisisL1LspHdrEntry": wfIisisL1LspHdrEntry,
       "wfIisisL1LspHdrLspId": wfIisisL1LspHdrLspId,
       "wfIisisL1LspHdrLifetime": wfIisisL1LspHdrLifetime,
       "wfIisisL1LspHdrSeqnum": wfIisisL1LspHdrSeqnum,
       "wfIisisL1LspHdrFlags": wfIisisL1LspHdrFlags,
       "wfIisisL1LspHdrCksum": wfIisisL1LspHdrCksum,
       "wfIisisL2LspHdrTable": wfIisisL2LspHdrTable,
       "wfIisisL2LspHdrEntry": wfIisisL2LspHdrEntry,
       "wfIisisL2LspHdrLspId": wfIisisL2LspHdrLspId,
       "wfIisisL2LspHdrLifetime": wfIisisL2LspHdrLifetime,
       "wfIisisL2LspHdrSeqnum": wfIisisL2LspHdrSeqnum,
       "wfIisisL2LspHdrFlags": wfIisisL2LspHdrFlags,
       "wfIisisL2LspHdrCksum": wfIisisL2LspHdrCksum,
       "wfIisisIfTable": wfIisisIfTable,
       "wfIisisIfEntry": wfIisisIfEntry,
       "wfIisisIfDelete": wfIisisIfDelete,
       "wfIisisIfDisable": wfIisisIfDisable,
       "wfIisisIfIpAddress": wfIisisIfIpAddress,
       "wfIisisAddressLessIf": wfIisisAddressLessIf,
       "wfIisisIfRouterLevel": wfIisisIfRouterLevel,
       "wfIisisIfL1DefaultMetric": wfIisisIfL1DefaultMetric,
       "wfIisisIfL2DefaultMetric": wfIisisIfL2DefaultMetric,
       "wfIisisIfL1DrPriority": wfIisisIfL1DrPriority,
       "wfIisisIfL2DrPriority": wfIisisIfL2DrPriority,
       "wfIisisIfHelloTimer": wfIisisIfHelloTimer,
       "wfIisisIfPassword": wfIisisIfPassword,
       "wfIisisIfHelloMtuSize": wfIisisIfHelloMtuSize,
       "wfIisisIfIihHoldMultiplier": wfIisisIfIihHoldMultiplier,
       "wfIisisIfIshHoldMultiplier": wfIisisIfIshHoldMultiplier,
       "wfIisisIfType": wfIisisIfType,
       "wfIisisIfCsnpTimer": wfIisisIfCsnpTimer,
       "wfIisisIfStatsTable": wfIisisIfStatsTable,
       "wfIisisIfStatsEntry": wfIisisIfStatsEntry,
       "wfIisisIfStatsIpAddress": wfIisisIfStatsIpAddress,
       "wfIisisStatsAddressLessIf": wfIisisStatsAddressLessIf,
       "wfIisisIfStatsState": wfIisisIfStatsState,
       "wfIisisIfStatsCct": wfIisisIfStatsCct,
       "wfIisisIfStatsL1TxHellos": wfIisisIfStatsL1TxHellos,
       "wfIisisIfStatsL2TxHellos": wfIisisIfStatsL2TxHellos,
       "wfIisisIfStatsL1RxHellos": wfIisisIfStatsL1RxHellos,
       "wfIisisIfStatsL2RxHellos": wfIisisIfStatsL2RxHellos,
       "wfIisisIfStatsL1Drops": wfIisisIfStatsL1Drops,
       "wfIisisIfStatsL2Drops": wfIisisIfStatsL2Drops,
       "wfIisisIfStatsL1DesignatedRouter": wfIisisIfStatsL1DesignatedRouter,
       "wfIisisIfStatsL2DesignatedRouter": wfIisisIfStatsL2DesignatedRouter,
       "wfIisisIfStatsTxL1Lsp": wfIisisIfStatsTxL1Lsp,
       "wfIisisIfStatsTxL2Lsp": wfIisisIfStatsTxL2Lsp,
       "wfIisisIfStatsTxL1Csnp": wfIisisIfStatsTxL1Csnp,
       "wfIisisIfStatsTxL2Csnp": wfIisisIfStatsTxL2Csnp,
       "wfIisisIfStatsTxL1Psnp": wfIisisIfStatsTxL1Psnp,
       "wfIisisIfStatsTxL2Psnp": wfIisisIfStatsTxL2Psnp,
       "wfIisisIfStatsRxL1Lsp": wfIisisIfStatsRxL1Lsp,
       "wfIisisIfStatsRxL2Lsp": wfIisisIfStatsRxL2Lsp,
       "wfIisisIfStatsRxL1Csnp": wfIisisIfStatsRxL1Csnp,
       "wfIisisIfStatsRxL2Csnp": wfIisisIfStatsRxL2Csnp,
       "wfIisisIfStatsRxL1Psnp": wfIisisIfStatsRxL1Psnp,
       "wfIisisIfStatsRxL2Psnp": wfIisisIfStatsRxL2Psnp,
       "wfIisisIfStatsL1NbrCount": wfIisisIfStatsL1NbrCount,
       "wfIisisIfStatsL2NbrCount": wfIisisIfStatsL2NbrCount,
       "wfIisisIfStatsL1AdjCount": wfIisisIfStatsL1AdjCount,
       "wfIisisIfStatsL2AdjCount": wfIisisIfStatsL2AdjCount,
       "wfIisisDynNbrTable": wfIisisDynNbrTable,
       "wfIisisDynNbrEntry": wfIisisDynNbrEntry,
       "wfIisisDynNbrState": wfIisisDynNbrState,
       "wfIisisDynNbrIpAddr": wfIisisDynNbrIpAddr,
       "wfIisisDynNbrIfAddr": wfIisisDynNbrIfAddr,
       "wfIisisDynNbrAddressLessIndex": wfIisisDynNbrAddressLessIndex,
       "wfIisisDynNbrRtrId": wfIisisDynNbrRtrId,
       "wfIisisDynNbrDatabase": wfIisisDynNbrDatabase,
       "wfIisisDynNbrType": wfIisisDynNbrType,
       "wfIisisDynNbrPseudonodeId": wfIisisDynNbrPseudonodeId,
       "wfIisisDynNbrHoldTime": wfIisisDynNbrHoldTime,
       "wfIisisDynNbrPriority": wfIisisDynNbrPriority,
       "wfIisisDynNbrSnpaAddr": wfIisisDynNbrSnpaAddr,
       "wfIisisDynNbrLanId": wfIisisDynNbrLanId}
)
