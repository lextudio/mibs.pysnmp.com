# SNMP MIB module (ALCATEL-IND1-DRCTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DRCTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:56 2024
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

(routingIND1Tm,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Tm")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

alcatelIND1DrcTmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1)
)
alcatelIND1DrcTmMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1DrcTmMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1DrcTmMIBObjects = _AlcatelIND1DrcTmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1)
)
_AlaDrcTmConfig_ObjectIdentity = ObjectIdentity
alaDrcTmConfig = _AlaDrcTmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1)
)
_AlaDrcTmIPRouterPrimaryAddress_Type = IpAddress
_AlaDrcTmIPRouterPrimaryAddress_Object = MibScalar
alaDrcTmIPRouterPrimaryAddress = _AlaDrcTmIPRouterPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 1),
    _AlaDrcTmIPRouterPrimaryAddress_Type()
)
alaDrcTmIPRouterPrimaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPRouterPrimaryAddress.setStatus("current")
_AlaDrcTmIPRouterId_Type = IpAddress
_AlaDrcTmIPRouterId_Object = MibScalar
alaDrcTmIPRouterId = _AlaDrcTmIPRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 2),
    _AlaDrcTmIPRouterId_Type()
)
alaDrcTmIPRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPRouterId.setStatus("current")


class _AlaDrcTmIPRipStatus_Type(Integer32):
    """Custom type alaDrcTmIPRipStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPRipStatus_Type.__name__ = "Integer32"
_AlaDrcTmIPRipStatus_Object = MibScalar
alaDrcTmIPRipStatus = _AlaDrcTmIPRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 3),
    _AlaDrcTmIPRipStatus_Type()
)
alaDrcTmIPRipStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPRipStatus.setStatus("current")


class _AlaDrcTmIPOspfStatus_Type(Integer32):
    """Custom type alaDrcTmIPOspfStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPOspfStatus_Type.__name__ = "Integer32"
_AlaDrcTmIPOspfStatus_Object = MibScalar
alaDrcTmIPOspfStatus = _AlaDrcTmIPOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 4),
    _AlaDrcTmIPOspfStatus_Type()
)
alaDrcTmIPOspfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPOspfStatus.setStatus("current")


class _AlaDrcTmIPBgpStatus_Type(Integer32):
    """Custom type alaDrcTmIPBgpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPBgpStatus_Type.__name__ = "Integer32"
_AlaDrcTmIPBgpStatus_Object = MibScalar
alaDrcTmIPBgpStatus = _AlaDrcTmIPBgpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 5),
    _AlaDrcTmIPBgpStatus_Type()
)
alaDrcTmIPBgpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPBgpStatus.setStatus("current")


class _AlaDrcTmIPDvmrpStatus_Type(Integer32):
    """Custom type alaDrcTmIPDvmrpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPDvmrpStatus_Type.__name__ = "Integer32"
_AlaDrcTmIPDvmrpStatus_Object = MibScalar
alaDrcTmIPDvmrpStatus = _AlaDrcTmIPDvmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 6),
    _AlaDrcTmIPDvmrpStatus_Type()
)
alaDrcTmIPDvmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPDvmrpStatus.setStatus("current")


class _AlaDrcTmIPPimStatus_Type(Integer32):
    """Custom type alaDrcTmIPPimStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPPimStatus_Type.__name__ = "Integer32"
_AlaDrcTmIPPimStatus_Object = MibScalar
alaDrcTmIPPimStatus = _AlaDrcTmIPPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 7),
    _AlaDrcTmIPPimStatus_Type()
)
alaDrcTmIPPimStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPPimStatus.setStatus("current")


class _AlaDrcTmIPMsdpStatus_Type(Integer32):
    """Custom type alaDrcTmIPMsdpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPMsdpStatus_Type.__name__ = "Integer32"
_AlaDrcTmIPMsdpStatus_Object = MibScalar
alaDrcTmIPMsdpStatus = _AlaDrcTmIPMsdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 8),
    _AlaDrcTmIPMsdpStatus_Type()
)
alaDrcTmIPMsdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPMsdpStatus.setStatus("current")


class _AlaDrcTmIPRipngStatus_Type(Integer32):
    """Custom type alaDrcTmIPRipngStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPRipngStatus_Type.__name__ = "Integer32"
_AlaDrcTmIPRipngStatus_Object = MibScalar
alaDrcTmIPRipngStatus = _AlaDrcTmIPRipngStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 9),
    _AlaDrcTmIPRipngStatus_Type()
)
alaDrcTmIPRipngStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPRipngStatus.setStatus("current")


class _AlaDrcTmIPOspf3Status_Type(Integer32):
    """Custom type alaDrcTmIPOspf3Status based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPOspf3Status_Type.__name__ = "Integer32"
_AlaDrcTmIPOspf3Status_Object = MibScalar
alaDrcTmIPOspf3Status = _AlaDrcTmIPOspf3Status_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 10),
    _AlaDrcTmIPOspf3Status_Type()
)
alaDrcTmIPOspf3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPOspf3Status.setStatus("current")


class _AlaDrcTmIPIsisStatus_Type(Integer32):
    """Custom type alaDrcTmIPIsisStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaDrcTmIPIsisStatus_Type.__name__ = "Integer32"
_AlaDrcTmIPIsisStatus_Object = MibScalar
alaDrcTmIPIsisStatus = _AlaDrcTmIPIsisStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 1, 11),
    _AlaDrcTmIPIsisStatus_Type()
)
alaDrcTmIPIsisStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIPIsisStatus.setStatus("current")
_AlaDrcTmDebug_ObjectIdentity = ObjectIdentity
alaDrcTmDebug = _AlaDrcTmDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2)
)


class _AlaDrcTmDebugLevel_Type(Integer32):
    """Custom type alaDrcTmDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugLevel_Type.__name__ = "Integer32"
_AlaDrcTmDebugLevel_Object = MibScalar
alaDrcTmDebugLevel = _AlaDrcTmDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 1),
    _AlaDrcTmDebugLevel_Type()
)
alaDrcTmDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugLevel.setStatus("obsolete")


class _AlaDrcTmDebugError_Type(Integer32):
    """Custom type alaDrcTmDebugError based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugError_Type.__name__ = "Integer32"
_AlaDrcTmDebugError_Object = MibScalar
alaDrcTmDebugError = _AlaDrcTmDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 2),
    _AlaDrcTmDebugError_Type()
)
alaDrcTmDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugError.setStatus("current")


class _AlaDrcTmDebugUnusedA_Type(Integer32):
    """Custom type alaDrcTmDebugUnusedA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugUnusedA_Type.__name__ = "Integer32"
_AlaDrcTmDebugUnusedA_Object = MibScalar
alaDrcTmDebugUnusedA = _AlaDrcTmDebugUnusedA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 3),
    _AlaDrcTmDebugUnusedA_Type()
)
alaDrcTmDebugUnusedA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugUnusedA.setStatus("current")


class _AlaDrcTmDebugTaskInfo_Type(Integer32):
    """Custom type alaDrcTmDebugTaskInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugTaskInfo_Type.__name__ = "Integer32"
_AlaDrcTmDebugTaskInfo_Object = MibScalar
alaDrcTmDebugTaskInfo = _AlaDrcTmDebugTaskInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 4),
    _AlaDrcTmDebugTaskInfo_Type()
)
alaDrcTmDebugTaskInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugTaskInfo.setStatus("current")


class _AlaDrcTmDebugEvents_Type(Integer32):
    """Custom type alaDrcTmDebugEvents based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugEvents_Type.__name__ = "Integer32"
_AlaDrcTmDebugEvents_Object = MibScalar
alaDrcTmDebugEvents = _AlaDrcTmDebugEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 5),
    _AlaDrcTmDebugEvents_Type()
)
alaDrcTmDebugEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugEvents.setStatus("current")


class _AlaDrcTmDebugMip_Type(Integer32):
    """Custom type alaDrcTmDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmDebugMip_Object = MibScalar
alaDrcTmDebugMip = _AlaDrcTmDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 6),
    _AlaDrcTmDebugMip_Type()
)
alaDrcTmDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugMip.setStatus("current")


class _AlaDrcTmDebugUnusedB_Type(Integer32):
    """Custom type alaDrcTmDebugUnusedB based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugUnusedB_Type.__name__ = "Integer32"
_AlaDrcTmDebugUnusedB_Object = MibScalar
alaDrcTmDebugUnusedB = _AlaDrcTmDebugUnusedB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 7),
    _AlaDrcTmDebugUnusedB_Type()
)
alaDrcTmDebugUnusedB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugUnusedB.setStatus("current")


class _AlaDrcTmDebugMisc_Type(Integer32):
    """Custom type alaDrcTmDebugMisc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugMisc_Type.__name__ = "Integer32"
_AlaDrcTmDebugMisc_Object = MibScalar
alaDrcTmDebugMisc = _AlaDrcTmDebugMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 8),
    _AlaDrcTmDebugMisc_Type()
)
alaDrcTmDebugMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugMisc.setStatus("current")


class _AlaDrcTmDebugUnused1_Type(Integer32):
    """Custom type alaDrcTmDebugUnused1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugUnused1_Type.__name__ = "Integer32"
_AlaDrcTmDebugUnused1_Object = MibScalar
alaDrcTmDebugUnused1 = _AlaDrcTmDebugUnused1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 9),
    _AlaDrcTmDebugUnused1_Type()
)
alaDrcTmDebugUnused1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugUnused1.setStatus("current")


class _AlaDrcTmDebugUnused2_Type(Integer32):
    """Custom type alaDrcTmDebugUnused2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugUnused2_Type.__name__ = "Integer32"
_AlaDrcTmDebugUnused2_Object = MibScalar
alaDrcTmDebugUnused2 = _AlaDrcTmDebugUnused2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 10),
    _AlaDrcTmDebugUnused2_Type()
)
alaDrcTmDebugUnused2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugUnused2.setStatus("current")


class _AlaDrcTmDebugUnused3_Type(Integer32):
    """Custom type alaDrcTmDebugUnused3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugUnused3_Type.__name__ = "Integer32"
_AlaDrcTmDebugUnused3_Object = MibScalar
alaDrcTmDebugUnused3 = _AlaDrcTmDebugUnused3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 11),
    _AlaDrcTmDebugUnused3_Type()
)
alaDrcTmDebugUnused3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugUnused3.setStatus("current")


class _AlaDrcTmDebugUnused4_Type(Integer32):
    """Custom type alaDrcTmDebugUnused4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugUnused4_Type.__name__ = "Integer32"
_AlaDrcTmDebugUnused4_Object = MibScalar
alaDrcTmDebugUnused4 = _AlaDrcTmDebugUnused4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 12),
    _AlaDrcTmDebugUnused4_Type()
)
alaDrcTmDebugUnused4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugUnused4.setStatus("current")


class _AlaDrcTmDebugAll_Type(Integer32):
    """Custom type alaDrcTmDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmDebugAll_Object = MibScalar
alaDrcTmDebugAll = _AlaDrcTmDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 2, 13),
    _AlaDrcTmDebugAll_Type()
)
alaDrcTmDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDebugAll.setStatus("current")
_AlaDrcTmRipDebug_ObjectIdentity = ObjectIdentity
alaDrcTmRipDebug = _AlaDrcTmRipDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3)
)


class _AlaDrcTmRipDebugError_Type(Integer32):
    """Custom type alaDrcTmRipDebugError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugError_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugError_Object = MibScalar
alaDrcTmRipDebugError = _AlaDrcTmRipDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 1),
    _AlaDrcTmRipDebugError_Type()
)
alaDrcTmRipDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugError.setStatus("current")


class _AlaDrcTmRipDebugWarning_Type(Integer32):
    """Custom type alaDrcTmRipDebugWarning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugWarning_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugWarning_Object = MibScalar
alaDrcTmRipDebugWarning = _AlaDrcTmRipDebugWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 2),
    _AlaDrcTmRipDebugWarning_Type()
)
alaDrcTmRipDebugWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugWarning.setStatus("current")


class _AlaDrcTmRipDebugRecv_Type(Integer32):
    """Custom type alaDrcTmRipDebugRecv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugRecv_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugRecv_Object = MibScalar
alaDrcTmRipDebugRecv = _AlaDrcTmRipDebugRecv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 3),
    _AlaDrcTmRipDebugRecv_Type()
)
alaDrcTmRipDebugRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugRecv.setStatus("current")


class _AlaDrcTmRipDebugSend_Type(Integer32):
    """Custom type alaDrcTmRipDebugSend based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugSend_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugSend_Object = MibScalar
alaDrcTmRipDebugSend = _AlaDrcTmRipDebugSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 4),
    _AlaDrcTmRipDebugSend_Type()
)
alaDrcTmRipDebugSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugSend.setStatus("current")


class _AlaDrcTmRipDebugRdb_Type(Integer32):
    """Custom type alaDrcTmRipDebugRdb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugRdb_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugRdb_Object = MibScalar
alaDrcTmRipDebugRdb = _AlaDrcTmRipDebugRdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 5),
    _AlaDrcTmRipDebugRdb_Type()
)
alaDrcTmRipDebugRdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugRdb.setStatus("current")


class _AlaDrcTmRipDebugAge_Type(Integer32):
    """Custom type alaDrcTmRipDebugAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugAge_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugAge_Object = MibScalar
alaDrcTmRipDebugAge = _AlaDrcTmRipDebugAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 6),
    _AlaDrcTmRipDebugAge_Type()
)
alaDrcTmRipDebugAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugAge.setStatus("current")


class _AlaDrcTmRipDebugConfig_Type(Integer32):
    """Custom type alaDrcTmRipDebugConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugConfig_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugConfig_Object = MibScalar
alaDrcTmRipDebugConfig = _AlaDrcTmRipDebugConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 7),
    _AlaDrcTmRipDebugConfig_Type()
)
alaDrcTmRipDebugConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugConfig.setStatus("current")


class _AlaDrcTmRipDebugRedist_Type(Integer32):
    """Custom type alaDrcTmRipDebugRedist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugRedist_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugRedist_Object = MibScalar
alaDrcTmRipDebugRedist = _AlaDrcTmRipDebugRedist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 8),
    _AlaDrcTmRipDebugRedist_Type()
)
alaDrcTmRipDebugRedist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugRedist.setStatus("current")


class _AlaDrcTmRipDebugInfo_Type(Integer32):
    """Custom type alaDrcTmRipDebugInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugInfo_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugInfo_Object = MibScalar
alaDrcTmRipDebugInfo = _AlaDrcTmRipDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 9),
    _AlaDrcTmRipDebugInfo_Type()
)
alaDrcTmRipDebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugInfo.setStatus("current")


class _AlaDrcTmRipDebugSetup_Type(Integer32):
    """Custom type alaDrcTmRipDebugSetup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugSetup_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugSetup_Object = MibScalar
alaDrcTmRipDebugSetup = _AlaDrcTmRipDebugSetup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 10),
    _AlaDrcTmRipDebugSetup_Type()
)
alaDrcTmRipDebugSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugSetup.setStatus("current")


class _AlaDrcTmRipDebugTime_Type(Integer32):
    """Custom type alaDrcTmRipDebugTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugTime_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugTime_Object = MibScalar
alaDrcTmRipDebugTime = _AlaDrcTmRipDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 11),
    _AlaDrcTmRipDebugTime_Type()
)
alaDrcTmRipDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugTime.setStatus("current")


class _AlaDrcTmRipDebugAll_Type(Integer32):
    """Custom type alaDrcTmRipDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmRipDebugAll_Object = MibScalar
alaDrcTmRipDebugAll = _AlaDrcTmRipDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 3, 12),
    _AlaDrcTmRipDebugAll_Type()
)
alaDrcTmRipDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipDebugAll.setStatus("current")
_AlaDrcTmOspfDebug_ObjectIdentity = ObjectIdentity
alaDrcTmOspfDebug = _AlaDrcTmOspfDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4)
)


class _AlaDrcTmOspfDebugError_Type(Integer32):
    """Custom type alaDrcTmOspfDebugError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugError_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugError_Object = MibScalar
alaDrcTmOspfDebugError = _AlaDrcTmOspfDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 1),
    _AlaDrcTmOspfDebugError_Type()
)
alaDrcTmOspfDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugError.setStatus("current")


class _AlaDrcTmOspfDebugWarning_Type(Integer32):
    """Custom type alaDrcTmOspfDebugWarning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugWarning_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugWarning_Object = MibScalar
alaDrcTmOspfDebugWarning = _AlaDrcTmOspfDebugWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 2),
    _AlaDrcTmOspfDebugWarning_Type()
)
alaDrcTmOspfDebugWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugWarning.setStatus("current")


class _AlaDrcTmOspfDebugState_Type(Integer32):
    """Custom type alaDrcTmOspfDebugState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugState_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugState_Object = MibScalar
alaDrcTmOspfDebugState = _AlaDrcTmOspfDebugState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 3),
    _AlaDrcTmOspfDebugState_Type()
)
alaDrcTmOspfDebugState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugState.setStatus("current")


class _AlaDrcTmOspfDebugRecv_Type(Integer32):
    """Custom type alaDrcTmOspfDebugRecv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugRecv_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugRecv_Object = MibScalar
alaDrcTmOspfDebugRecv = _AlaDrcTmOspfDebugRecv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 4),
    _AlaDrcTmOspfDebugRecv_Type()
)
alaDrcTmOspfDebugRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugRecv.setStatus("current")


class _AlaDrcTmOspfDebugSend_Type(Integer32):
    """Custom type alaDrcTmOspfDebugSend based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugSend_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugSend_Object = MibScalar
alaDrcTmOspfDebugSend = _AlaDrcTmOspfDebugSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 5),
    _AlaDrcTmOspfDebugSend_Type()
)
alaDrcTmOspfDebugSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugSend.setStatus("current")


class _AlaDrcTmOspfDebugFlood_Type(Integer32):
    """Custom type alaDrcTmOspfDebugFlood based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugFlood_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugFlood_Object = MibScalar
alaDrcTmOspfDebugFlood = _AlaDrcTmOspfDebugFlood_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 6),
    _AlaDrcTmOspfDebugFlood_Type()
)
alaDrcTmOspfDebugFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugFlood.setStatus("current")


class _AlaDrcTmOspfDebugSPF_Type(Integer32):
    """Custom type alaDrcTmOspfDebugSPF based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugSPF_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugSPF_Object = MibScalar
alaDrcTmOspfDebugSPF = _AlaDrcTmOspfDebugSPF_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 7),
    _AlaDrcTmOspfDebugSPF_Type()
)
alaDrcTmOspfDebugSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugSPF.setStatus("current")


class _AlaDrcTmOspfDebugLsdb_Type(Integer32):
    """Custom type alaDrcTmOspfDebugLsdb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugLsdb_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugLsdb_Object = MibScalar
alaDrcTmOspfDebugLsdb = _AlaDrcTmOspfDebugLsdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 8),
    _AlaDrcTmOspfDebugLsdb_Type()
)
alaDrcTmOspfDebugLsdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugLsdb.setStatus("current")


class _AlaDrcTmOspfDebugRdb_Type(Integer32):
    """Custom type alaDrcTmOspfDebugRdb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugRdb_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugRdb_Object = MibScalar
alaDrcTmOspfDebugRdb = _AlaDrcTmOspfDebugRdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 9),
    _AlaDrcTmOspfDebugRdb_Type()
)
alaDrcTmOspfDebugRdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugRdb.setStatus("current")


class _AlaDrcTmOspfDebugAge_Type(Integer32):
    """Custom type alaDrcTmOspfDebugAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugAge_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugAge_Object = MibScalar
alaDrcTmOspfDebugAge = _AlaDrcTmOspfDebugAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 10),
    _AlaDrcTmOspfDebugAge_Type()
)
alaDrcTmOspfDebugAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugAge.setStatus("current")


class _AlaDrcTmOspfDebugVlink_Type(Integer32):
    """Custom type alaDrcTmOspfDebugVlink based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugVlink_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugVlink_Object = MibScalar
alaDrcTmOspfDebugVlink = _AlaDrcTmOspfDebugVlink_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 11),
    _AlaDrcTmOspfDebugVlink_Type()
)
alaDrcTmOspfDebugVlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugVlink.setStatus("current")


class _AlaDrcTmOspfDebugRedist_Type(Integer32):
    """Custom type alaDrcTmOspfDebugRedist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugRedist_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugRedist_Object = MibScalar
alaDrcTmOspfDebugRedist = _AlaDrcTmOspfDebugRedist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 12),
    _AlaDrcTmOspfDebugRedist_Type()
)
alaDrcTmOspfDebugRedist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugRedist.setStatus("current")


class _AlaDrcTmOspfDebugSummary_Type(Integer32):
    """Custom type alaDrcTmOspfDebugSummary based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugSummary_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugSummary_Object = MibScalar
alaDrcTmOspfDebugSummary = _AlaDrcTmOspfDebugSummary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 13),
    _AlaDrcTmOspfDebugSummary_Type()
)
alaDrcTmOspfDebugSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugSummary.setStatus("current")


class _AlaDrcTmOspfDebugDbexch_Type(Integer32):
    """Custom type alaDrcTmOspfDebugDbexch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugDbexch_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugDbexch_Object = MibScalar
alaDrcTmOspfDebugDbexch = _AlaDrcTmOspfDebugDbexch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 14),
    _AlaDrcTmOspfDebugDbexch_Type()
)
alaDrcTmOspfDebugDbexch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugDbexch.setStatus("current")


class _AlaDrcTmOspfDebugHello_Type(Integer32):
    """Custom type alaDrcTmOspfDebugHello based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugHello_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugHello_Object = MibScalar
alaDrcTmOspfDebugHello = _AlaDrcTmOspfDebugHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 15),
    _AlaDrcTmOspfDebugHello_Type()
)
alaDrcTmOspfDebugHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugHello.setStatus("current")


class _AlaDrcTmOspfDebugAuth_Type(Integer32):
    """Custom type alaDrcTmOspfDebugAuth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugAuth_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugAuth_Object = MibScalar
alaDrcTmOspfDebugAuth = _AlaDrcTmOspfDebugAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 16),
    _AlaDrcTmOspfDebugAuth_Type()
)
alaDrcTmOspfDebugAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugAuth.setStatus("current")


class _AlaDrcTmOspfDebugArea_Type(Integer32):
    """Custom type alaDrcTmOspfDebugArea based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugArea_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugArea_Object = MibScalar
alaDrcTmOspfDebugArea = _AlaDrcTmOspfDebugArea_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 17),
    _AlaDrcTmOspfDebugArea_Type()
)
alaDrcTmOspfDebugArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugArea.setStatus("current")


class _AlaDrcTmOspfDebugIntf_Type(Integer32):
    """Custom type alaDrcTmOspfDebugIntf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugIntf_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugIntf_Object = MibScalar
alaDrcTmOspfDebugIntf = _AlaDrcTmOspfDebugIntf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 18),
    _AlaDrcTmOspfDebugIntf_Type()
)
alaDrcTmOspfDebugIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugIntf.setStatus("current")


class _AlaDrcTmOspfDebugMip_Type(Integer32):
    """Custom type alaDrcTmOspfDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugMip_Object = MibScalar
alaDrcTmOspfDebugMip = _AlaDrcTmOspfDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 19),
    _AlaDrcTmOspfDebugMip_Type()
)
alaDrcTmOspfDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugMip.setStatus("current")


class _AlaDrcTmOspfDebugInfo_Type(Integer32):
    """Custom type alaDrcTmOspfDebugInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugInfo_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugInfo_Object = MibScalar
alaDrcTmOspfDebugInfo = _AlaDrcTmOspfDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 20),
    _AlaDrcTmOspfDebugInfo_Type()
)
alaDrcTmOspfDebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugInfo.setStatus("current")


class _AlaDrcTmOspfDebugSetup_Type(Integer32):
    """Custom type alaDrcTmOspfDebugSetup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugSetup_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugSetup_Object = MibScalar
alaDrcTmOspfDebugSetup = _AlaDrcTmOspfDebugSetup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 21),
    _AlaDrcTmOspfDebugSetup_Type()
)
alaDrcTmOspfDebugSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugSetup.setStatus("current")


class _AlaDrcTmOspfDebugTime_Type(Integer32):
    """Custom type alaDrcTmOspfDebugTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugTime_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugTime_Object = MibScalar
alaDrcTmOspfDebugTime = _AlaDrcTmOspfDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 22),
    _AlaDrcTmOspfDebugTime_Type()
)
alaDrcTmOspfDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugTime.setStatus("current")


class _AlaDrcTmOspfDebugTm_Type(Integer32):
    """Custom type alaDrcTmOspfDebugTm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugTm_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugTm_Object = MibScalar
alaDrcTmOspfDebugTm = _AlaDrcTmOspfDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 23),
    _AlaDrcTmOspfDebugTm_Type()
)
alaDrcTmOspfDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugTm.setStatus("current")


class _AlaDrcTmOspfDebugRestart_Type(Integer32):
    """Custom type alaDrcTmOspfDebugRestart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugRestart_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugRestart_Object = MibScalar
alaDrcTmOspfDebugRestart = _AlaDrcTmOspfDebugRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 24),
    _AlaDrcTmOspfDebugRestart_Type()
)
alaDrcTmOspfDebugRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugRestart.setStatus("current")


class _AlaDrcTmOspfDebugHelper_Type(Integer32):
    """Custom type alaDrcTmOspfDebugHelper based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugHelper_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugHelper_Object = MibScalar
alaDrcTmOspfDebugHelper = _AlaDrcTmOspfDebugHelper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 25),
    _AlaDrcTmOspfDebugHelper_Type()
)
alaDrcTmOspfDebugHelper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugHelper.setStatus("current")


class _AlaDrcTmOspfDebugAll_Type(Integer32):
    """Custom type alaDrcTmOspfDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspfDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmOspfDebugAll_Object = MibScalar
alaDrcTmOspfDebugAll = _AlaDrcTmOspfDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 4, 26),
    _AlaDrcTmOspfDebugAll_Type()
)
alaDrcTmOspfDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugAll.setStatus("current")
_AlaDrcTmBgpDebug_ObjectIdentity = ObjectIdentity
alaDrcTmBgpDebug = _AlaDrcTmBgpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5)
)


class _AlaDrcTmBgpDebugDamp_Type(Integer32):
    """Custom type alaDrcTmBgpDebugDamp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugDamp_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugDamp_Object = MibScalar
alaDrcTmBgpDebugDamp = _AlaDrcTmBgpDebugDamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 1),
    _AlaDrcTmBgpDebugDamp_Type()
)
alaDrcTmBgpDebugDamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugDamp.setStatus("current")


class _AlaDrcTmBgpDebugFsm_Type(Integer32):
    """Custom type alaDrcTmBgpDebugFsm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugFsm_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugFsm_Object = MibScalar
alaDrcTmBgpDebugFsm = _AlaDrcTmBgpDebugFsm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 2),
    _AlaDrcTmBgpDebugFsm_Type()
)
alaDrcTmBgpDebugFsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugFsm.setStatus("current")


class _AlaDrcTmBgpDebugRecvUpd_Type(Integer32):
    """Custom type alaDrcTmBgpDebugRecvUpd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugRecvUpd_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugRecvUpd_Object = MibScalar
alaDrcTmBgpDebugRecvUpd = _AlaDrcTmBgpDebugRecvUpd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 3),
    _AlaDrcTmBgpDebugRecvUpd_Type()
)
alaDrcTmBgpDebugRecvUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugRecvUpd.setStatus("current")


class _AlaDrcTmBgpDebugSendUpd_Type(Integer32):
    """Custom type alaDrcTmBgpDebugSendUpd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugSendUpd_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugSendUpd_Object = MibScalar
alaDrcTmBgpDebugSendUpd = _AlaDrcTmBgpDebugSendUpd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 4),
    _AlaDrcTmBgpDebugSendUpd_Type()
)
alaDrcTmBgpDebugSendUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugSendUpd.setStatus("current")


class _AlaDrcTmBgpDebugOpen_Type(Integer32):
    """Custom type alaDrcTmBgpDebugOpen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugOpen_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugOpen_Object = MibScalar
alaDrcTmBgpDebugOpen = _AlaDrcTmBgpDebugOpen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 5),
    _AlaDrcTmBgpDebugOpen_Type()
)
alaDrcTmBgpDebugOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugOpen.setStatus("current")


class _AlaDrcTmBgpDebugKeepAlive_Type(Integer32):
    """Custom type alaDrcTmBgpDebugKeepAlive based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugKeepAlive_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugKeepAlive_Object = MibScalar
alaDrcTmBgpDebugKeepAlive = _AlaDrcTmBgpDebugKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 6),
    _AlaDrcTmBgpDebugKeepAlive_Type()
)
alaDrcTmBgpDebugKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugKeepAlive.setStatus("current")


class _AlaDrcTmBgpDebugNotify_Type(Integer32):
    """Custom type alaDrcTmBgpDebugNotify based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugNotify_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugNotify_Object = MibScalar
alaDrcTmBgpDebugNotify = _AlaDrcTmBgpDebugNotify_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 7),
    _AlaDrcTmBgpDebugNotify_Type()
)
alaDrcTmBgpDebugNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugNotify.setStatus("current")


class _AlaDrcTmBgpDebugPolicy_Type(Integer32):
    """Custom type alaDrcTmBgpDebugPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugPolicy_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugPolicy_Object = MibScalar
alaDrcTmBgpDebugPolicy = _AlaDrcTmBgpDebugPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 8),
    _AlaDrcTmBgpDebugPolicy_Type()
)
alaDrcTmBgpDebugPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugPolicy.setStatus("current")


class _AlaDrcTmBgpDebugRoute_Type(Integer32):
    """Custom type alaDrcTmBgpDebugRoute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugRoute_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugRoute_Object = MibScalar
alaDrcTmBgpDebugRoute = _AlaDrcTmBgpDebugRoute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 9),
    _AlaDrcTmBgpDebugRoute_Type()
)
alaDrcTmBgpDebugRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugRoute.setStatus("current")


class _AlaDrcTmBgpDebugSync_Type(Integer32):
    """Custom type alaDrcTmBgpDebugSync based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugSync_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugSync_Object = MibScalar
alaDrcTmBgpDebugSync = _AlaDrcTmBgpDebugSync_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 10),
    _AlaDrcTmBgpDebugSync_Type()
)
alaDrcTmBgpDebugSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugSync.setStatus("current")


class _AlaDrcTmBgpDebugAggr_Type(Integer32):
    """Custom type alaDrcTmBgpDebugAggr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugAggr_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugAggr_Object = MibScalar
alaDrcTmBgpDebugAggr = _AlaDrcTmBgpDebugAggr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 11),
    _AlaDrcTmBgpDebugAggr_Type()
)
alaDrcTmBgpDebugAggr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugAggr.setStatus("current")


class _AlaDrcTmBgpDebugTcp_Type(Integer32):
    """Custom type alaDrcTmBgpDebugTcp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugTcp_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugTcp_Object = MibScalar
alaDrcTmBgpDebugTcp = _AlaDrcTmBgpDebugTcp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 12),
    _AlaDrcTmBgpDebugTcp_Type()
)
alaDrcTmBgpDebugTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugTcp.setStatus("current")


class _AlaDrcTmBgpDebugWarnings_Type(Integer32):
    """Custom type alaDrcTmBgpDebugWarnings based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugWarnings_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugWarnings_Object = MibScalar
alaDrcTmBgpDebugWarnings = _AlaDrcTmBgpDebugWarnings_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 13),
    _AlaDrcTmBgpDebugWarnings_Type()
)
alaDrcTmBgpDebugWarnings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugWarnings.setStatus("current")


class _AlaDrcTmBgpDebugErrors_Type(Integer32):
    """Custom type alaDrcTmBgpDebugErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugErrors_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugErrors_Object = MibScalar
alaDrcTmBgpDebugErrors = _AlaDrcTmBgpDebugErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 14),
    _AlaDrcTmBgpDebugErrors_Type()
)
alaDrcTmBgpDebugErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugErrors.setStatus("current")


class _AlaDrcTmBgpDebugRedist_Type(Integer32):
    """Custom type alaDrcTmBgpDebugRedist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugRedist_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugRedist_Object = MibScalar
alaDrcTmBgpDebugRedist = _AlaDrcTmBgpDebugRedist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 15),
    _AlaDrcTmBgpDebugRedist_Type()
)
alaDrcTmBgpDebugRedist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugRedist.setStatus("current")


class _AlaDrcTmBgpDebugPeer_Type(Integer32):
    """Custom type alaDrcTmBgpDebugPeer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugPeer_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugPeer_Object = MibScalar
alaDrcTmBgpDebugPeer = _AlaDrcTmBgpDebugPeer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 16),
    _AlaDrcTmBgpDebugPeer_Type()
)
alaDrcTmBgpDebugPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugPeer.setStatus("current")


class _AlaDrcTmBgpDebugLocal_Type(Integer32):
    """Custom type alaDrcTmBgpDebugLocal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugLocal_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugLocal_Object = MibScalar
alaDrcTmBgpDebugLocal = _AlaDrcTmBgpDebugLocal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 17),
    _AlaDrcTmBgpDebugLocal_Type()
)
alaDrcTmBgpDebugLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugLocal.setStatus("current")


class _AlaDrcTmBgpDebugMip_Type(Integer32):
    """Custom type alaDrcTmBgpDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugMip_Object = MibScalar
alaDrcTmBgpDebugMip = _AlaDrcTmBgpDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 18),
    _AlaDrcTmBgpDebugMip_Type()
)
alaDrcTmBgpDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugMip.setStatus("current")


class _AlaDrcTmBgpDebugTm_Type(Integer32):
    """Custom type alaDrcTmBgpDebugTm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugTm_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugTm_Object = MibScalar
alaDrcTmBgpDebugTm = _AlaDrcTmBgpDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 19),
    _AlaDrcTmBgpDebugTm_Type()
)
alaDrcTmBgpDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugTm.setStatus("current")


class _AlaDrcTmBgpDebugInfo_Type(Integer32):
    """Custom type alaDrcTmBgpDebugInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugInfo_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugInfo_Object = MibScalar
alaDrcTmBgpDebugInfo = _AlaDrcTmBgpDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 20),
    _AlaDrcTmBgpDebugInfo_Type()
)
alaDrcTmBgpDebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugInfo.setStatus("current")


class _AlaDrcTmBgpDebugRestart_Type(Integer32):
    """Custom type alaDrcTmBgpDebugRestart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugRestart_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugRestart_Object = MibScalar
alaDrcTmBgpDebugRestart = _AlaDrcTmBgpDebugRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 21),
    _AlaDrcTmBgpDebugRestart_Type()
)
alaDrcTmBgpDebugRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugRestart.setStatus("current")


class _AlaDrcTmBgpDebugAll_Type(Integer32):
    """Custom type alaDrcTmBgpDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugAll_Object = MibScalar
alaDrcTmBgpDebugAll = _AlaDrcTmBgpDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 22),
    _AlaDrcTmBgpDebugAll_Type()
)
alaDrcTmBgpDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugAll.setStatus("current")


class _AlaDrcTmBgpDebugPeer6_Type(Integer32):
    """Custom type alaDrcTmBgpDebugPeer6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugPeer6_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugPeer6_Object = MibScalar
alaDrcTmBgpDebugPeer6 = _AlaDrcTmBgpDebugPeer6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 23),
    _AlaDrcTmBgpDebugPeer6_Type()
)
alaDrcTmBgpDebugPeer6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugPeer6.setStatus("current")


class _AlaDrcTmBgpDebugRoute6_Type(Integer32):
    """Custom type alaDrcTmBgpDebugRoute6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmBgpDebugRoute6_Type.__name__ = "Integer32"
_AlaDrcTmBgpDebugRoute6_Object = MibScalar
alaDrcTmBgpDebugRoute6 = _AlaDrcTmBgpDebugRoute6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 5, 24),
    _AlaDrcTmBgpDebugRoute6_Type()
)
alaDrcTmBgpDebugRoute6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugRoute6.setStatus("current")
_AlaDrcTmDvmrpDebug_ObjectIdentity = ObjectIdentity
alaDrcTmDvmrpDebug = _AlaDrcTmDvmrpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6)
)


class _AlaDrcTmDvmrpDebugError_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugError based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugError_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugError_Object = MibScalar
alaDrcTmDvmrpDebugError = _AlaDrcTmDvmrpDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 1),
    _AlaDrcTmDvmrpDebugError_Type()
)
alaDrcTmDvmrpDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugError.setStatus("current")


class _AlaDrcTmDvmrpDebugNbr_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugNbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugNbr_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugNbr_Object = MibScalar
alaDrcTmDvmrpDebugNbr = _AlaDrcTmDvmrpDebugNbr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 2),
    _AlaDrcTmDvmrpDebugNbr_Type()
)
alaDrcTmDvmrpDebugNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugNbr.setStatus("current")


class _AlaDrcTmDvmrpDebugRoutes_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugRoutes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugRoutes_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugRoutes_Object = MibScalar
alaDrcTmDvmrpDebugRoutes = _AlaDrcTmDvmrpDebugRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 3),
    _AlaDrcTmDvmrpDebugRoutes_Type()
)
alaDrcTmDvmrpDebugRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugRoutes.setStatus("current")


class _AlaDrcTmDvmrpDebugProbes_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugProbes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugProbes_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugProbes_Object = MibScalar
alaDrcTmDvmrpDebugProbes = _AlaDrcTmDvmrpDebugProbes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 4),
    _AlaDrcTmDvmrpDebugProbes_Type()
)
alaDrcTmDvmrpDebugProbes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugProbes.setStatus("current")


class _AlaDrcTmDvmrpDebugPrunes_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugPrunes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugPrunes_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugPrunes_Object = MibScalar
alaDrcTmDvmrpDebugPrunes = _AlaDrcTmDvmrpDebugPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 5),
    _AlaDrcTmDvmrpDebugPrunes_Type()
)
alaDrcTmDvmrpDebugPrunes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugPrunes.setStatus("current")


class _AlaDrcTmDvmrpDebugGrafts_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugGrafts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugGrafts_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugGrafts_Object = MibScalar
alaDrcTmDvmrpDebugGrafts = _AlaDrcTmDvmrpDebugGrafts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 6),
    _AlaDrcTmDvmrpDebugGrafts_Type()
)
alaDrcTmDvmrpDebugGrafts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugGrafts.setStatus("current")


class _AlaDrcTmDvmrpDebugTime_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugTime_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugTime_Object = MibScalar
alaDrcTmDvmrpDebugTime = _AlaDrcTmDvmrpDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 7),
    _AlaDrcTmDvmrpDebugTime_Type()
)
alaDrcTmDvmrpDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugTime.setStatus("current")


class _AlaDrcTmDvmrpDebugIgmp_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugIgmp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugIgmp_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugIgmp_Object = MibScalar
alaDrcTmDvmrpDebugIgmp = _AlaDrcTmDvmrpDebugIgmp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 8),
    _AlaDrcTmDvmrpDebugIgmp_Type()
)
alaDrcTmDvmrpDebugIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugIgmp.setStatus("current")


class _AlaDrcTmDvmrpDebugFlash_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugFlash based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugFlash_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugFlash_Object = MibScalar
alaDrcTmDvmrpDebugFlash = _AlaDrcTmDvmrpDebugFlash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 9),
    _AlaDrcTmDvmrpDebugFlash_Type()
)
alaDrcTmDvmrpDebugFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugFlash.setStatus("current")


class _AlaDrcTmDvmrpDebugMip_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugMip_Object = MibScalar
alaDrcTmDvmrpDebugMip = _AlaDrcTmDvmrpDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 10),
    _AlaDrcTmDvmrpDebugMip_Type()
)
alaDrcTmDvmrpDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugMip.setStatus("current")


class _AlaDrcTmDvmrpDebugInit_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugInit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugInit_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugInit_Object = MibScalar
alaDrcTmDvmrpDebugInit = _AlaDrcTmDvmrpDebugInit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 11),
    _AlaDrcTmDvmrpDebugInit_Type()
)
alaDrcTmDvmrpDebugInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugInit.setStatus("current")


class _AlaDrcTmDvmrpDebugTm_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugTm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugTm_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugTm_Object = MibScalar
alaDrcTmDvmrpDebugTm = _AlaDrcTmDvmrpDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 12),
    _AlaDrcTmDvmrpDebugTm_Type()
)
alaDrcTmDvmrpDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugTm.setStatus("current")


class _AlaDrcTmDvmrpDebugIpmrm_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugIpmrm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugIpmrm_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugIpmrm_Object = MibScalar
alaDrcTmDvmrpDebugIpmrm = _AlaDrcTmDvmrpDebugIpmrm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 13),
    _AlaDrcTmDvmrpDebugIpmrm_Type()
)
alaDrcTmDvmrpDebugIpmrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugIpmrm.setStatus("current")


class _AlaDrcTmDvmrpDebugMisc_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugMisc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugMisc_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugMisc_Object = MibScalar
alaDrcTmDvmrpDebugMisc = _AlaDrcTmDvmrpDebugMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 14),
    _AlaDrcTmDvmrpDebugMisc_Type()
)
alaDrcTmDvmrpDebugMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugMisc.setStatus("current")


class _AlaDrcTmDvmrpDebugAll_Type(Integer32):
    """Custom type alaDrcTmDvmrpDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmDvmrpDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmDvmrpDebugAll_Object = MibScalar
alaDrcTmDvmrpDebugAll = _AlaDrcTmDvmrpDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 6, 15),
    _AlaDrcTmDvmrpDebugAll_Type()
)
alaDrcTmDvmrpDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugAll.setStatus("current")
_AlaDrcTmPimDebug_ObjectIdentity = ObjectIdentity
alaDrcTmPimDebug = _AlaDrcTmPimDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7)
)


class _AlaDrcTmPimDebugError_Type(Integer32):
    """Custom type alaDrcTmPimDebugError based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugError_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugError_Object = MibScalar
alaDrcTmPimDebugError = _AlaDrcTmPimDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 1),
    _AlaDrcTmPimDebugError_Type()
)
alaDrcTmPimDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugError.setStatus("current")


class _AlaDrcTmPimDebugMip_Type(Integer32):
    """Custom type alaDrcTmPimDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugMip_Object = MibScalar
alaDrcTmPimDebugMip = _AlaDrcTmPimDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 2),
    _AlaDrcTmPimDebugMip_Type()
)
alaDrcTmPimDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugMip.setStatus("current")


class _AlaDrcTmPimDebugInit_Type(Integer32):
    """Custom type alaDrcTmPimDebugInit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugInit_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugInit_Object = MibScalar
alaDrcTmPimDebugInit = _AlaDrcTmPimDebugInit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 3),
    _AlaDrcTmPimDebugInit_Type()
)
alaDrcTmPimDebugInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugInit.setStatus("current")


class _AlaDrcTmPimDebugBootstrap_Type(Integer32):
    """Custom type alaDrcTmPimDebugBootstrap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugBootstrap_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugBootstrap_Object = MibScalar
alaDrcTmPimDebugBootstrap = _AlaDrcTmPimDebugBootstrap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 4),
    _AlaDrcTmPimDebugBootstrap_Type()
)
alaDrcTmPimDebugBootstrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugBootstrap.setStatus("current")


class _AlaDrcTmPimDebugCRP_Type(Integer32):
    """Custom type alaDrcTmPimDebugCRP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugCRP_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugCRP_Object = MibScalar
alaDrcTmPimDebugCRP = _AlaDrcTmPimDebugCRP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 5),
    _AlaDrcTmPimDebugCRP_Type()
)
alaDrcTmPimDebugCRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugCRP.setStatus("current")


class _AlaDrcTmPimDebugTime_Type(Integer32):
    """Custom type alaDrcTmPimDebugTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugTime_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugTime_Object = MibScalar
alaDrcTmPimDebugTime = _AlaDrcTmPimDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 6),
    _AlaDrcTmPimDebugTime_Type()
)
alaDrcTmPimDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugTime.setStatus("current")


class _AlaDrcTmPimDebugSpt_Type(Integer32):
    """Custom type alaDrcTmPimDebugSpt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSpt_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSpt_Object = MibScalar
alaDrcTmPimDebugSpt = _AlaDrcTmPimDebugSpt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 7),
    _AlaDrcTmPimDebugSpt_Type()
)
alaDrcTmPimDebugSpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSpt.setStatus("current")


class _AlaDrcTmPimDebugSmNbr_Type(Integer32):
    """Custom type alaDrcTmPimDebugSmNbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSmNbr_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSmNbr_Object = MibScalar
alaDrcTmPimDebugSmNbr = _AlaDrcTmPimDebugSmNbr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 8),
    _AlaDrcTmPimDebugSmNbr_Type()
)
alaDrcTmPimDebugSmNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSmNbr.setStatus("current")


class _AlaDrcTmPimDebugSmHello_Type(Integer32):
    """Custom type alaDrcTmPimDebugSmHello based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSmHello_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSmHello_Object = MibScalar
alaDrcTmPimDebugSmHello = _AlaDrcTmPimDebugSmHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 9),
    _AlaDrcTmPimDebugSmHello_Type()
)
alaDrcTmPimDebugSmHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSmHello.setStatus("current")


class _AlaDrcTmPimDebugSmRoute_Type(Integer32):
    """Custom type alaDrcTmPimDebugSmRoute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSmRoute_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSmRoute_Object = MibScalar
alaDrcTmPimDebugSmRoute = _AlaDrcTmPimDebugSmRoute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 10),
    _AlaDrcTmPimDebugSmRoute_Type()
)
alaDrcTmPimDebugSmRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSmRoute.setStatus("current")


class _AlaDrcTmPimDebugSmJoinPrune_Type(Integer32):
    """Custom type alaDrcTmPimDebugSmJoinPrune based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSmJoinPrune_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSmJoinPrune_Object = MibScalar
alaDrcTmPimDebugSmJoinPrune = _AlaDrcTmPimDebugSmJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 11),
    _AlaDrcTmPimDebugSmJoinPrune_Type()
)
alaDrcTmPimDebugSmJoinPrune.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSmJoinPrune.setStatus("current")


class _AlaDrcTmPimDebugSmAssert_Type(Integer32):
    """Custom type alaDrcTmPimDebugSmAssert based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSmAssert_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSmAssert_Object = MibScalar
alaDrcTmPimDebugSmAssert = _AlaDrcTmPimDebugSmAssert_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 12),
    _AlaDrcTmPimDebugSmAssert_Type()
)
alaDrcTmPimDebugSmAssert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSmAssert.setStatus("current")


class _AlaDrcTmPimDebugSmIgmp_Type(Integer32):
    """Custom type alaDrcTmPimDebugSmIgmp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSmIgmp_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSmIgmp_Object = MibScalar
alaDrcTmPimDebugSmIgmp = _AlaDrcTmPimDebugSmIgmp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 13),
    _AlaDrcTmPimDebugSmIgmp_Type()
)
alaDrcTmPimDebugSmIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSmIgmp.setStatus("current")


class _AlaDrcTmPimDebugSmIpmrm_Type(Integer32):
    """Custom type alaDrcTmPimDebugSmIpmrm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSmIpmrm_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSmIpmrm_Object = MibScalar
alaDrcTmPimDebugSmIpmrm = _AlaDrcTmPimDebugSmIpmrm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 14),
    _AlaDrcTmPimDebugSmIpmrm_Type()
)
alaDrcTmPimDebugSmIpmrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSmIpmrm.setStatus("current")


class _AlaDrcTmPimDebugSmMisc_Type(Integer32):
    """Custom type alaDrcTmPimDebugSmMisc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugSmMisc_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugSmMisc_Object = MibScalar
alaDrcTmPimDebugSmMisc = _AlaDrcTmPimDebugSmMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 15),
    _AlaDrcTmPimDebugSmMisc_Type()
)
alaDrcTmPimDebugSmMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugSmMisc.setStatus("current")


class _AlaDrcTmPimDebugDmNbr_Type(Integer32):
    """Custom type alaDrcTmPimDebugDmNbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugDmNbr_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugDmNbr_Object = MibScalar
alaDrcTmPimDebugDmNbr = _AlaDrcTmPimDebugDmNbr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 16),
    _AlaDrcTmPimDebugDmNbr_Type()
)
alaDrcTmPimDebugDmNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugDmNbr.setStatus("current")


class _AlaDrcTmPimDebugDmHello_Type(Integer32):
    """Custom type alaDrcTmPimDebugDmHello based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugDmHello_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugDmHello_Object = MibScalar
alaDrcTmPimDebugDmHello = _AlaDrcTmPimDebugDmHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 17),
    _AlaDrcTmPimDebugDmHello_Type()
)
alaDrcTmPimDebugDmHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugDmHello.setStatus("current")


class _AlaDrcTmPimDebugDmRoute_Type(Integer32):
    """Custom type alaDrcTmPimDebugDmRoute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugDmRoute_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugDmRoute_Object = MibScalar
alaDrcTmPimDebugDmRoute = _AlaDrcTmPimDebugDmRoute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 18),
    _AlaDrcTmPimDebugDmRoute_Type()
)
alaDrcTmPimDebugDmRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugDmRoute.setStatus("current")


class _AlaDrcTmPimDebugDmJoinPrune_Type(Integer32):
    """Custom type alaDrcTmPimDebugDmJoinPrune based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugDmJoinPrune_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugDmJoinPrune_Object = MibScalar
alaDrcTmPimDebugDmJoinPrune = _AlaDrcTmPimDebugDmJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 19),
    _AlaDrcTmPimDebugDmJoinPrune_Type()
)
alaDrcTmPimDebugDmJoinPrune.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugDmJoinPrune.setStatus("current")


class _AlaDrcTmPimDebugDmAssert_Type(Integer32):
    """Custom type alaDrcTmPimDebugDmAssert based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugDmAssert_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugDmAssert_Object = MibScalar
alaDrcTmPimDebugDmAssert = _AlaDrcTmPimDebugDmAssert_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 20),
    _AlaDrcTmPimDebugDmAssert_Type()
)
alaDrcTmPimDebugDmAssert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugDmAssert.setStatus("current")


class _AlaDrcTmPimDebugDmIgmp_Type(Integer32):
    """Custom type alaDrcTmPimDebugDmIgmp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugDmIgmp_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugDmIgmp_Object = MibScalar
alaDrcTmPimDebugDmIgmp = _AlaDrcTmPimDebugDmIgmp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 21),
    _AlaDrcTmPimDebugDmIgmp_Type()
)
alaDrcTmPimDebugDmIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugDmIgmp.setStatus("current")


class _AlaDrcTmPimDebugDmIpmrm_Type(Integer32):
    """Custom type alaDrcTmPimDebugDmIpmrm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugDmIpmrm_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugDmIpmrm_Object = MibScalar
alaDrcTmPimDebugDmIpmrm = _AlaDrcTmPimDebugDmIpmrm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 22),
    _AlaDrcTmPimDebugDmIpmrm_Type()
)
alaDrcTmPimDebugDmIpmrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugDmIpmrm.setStatus("current")


class _AlaDrcTmPimDebugDmMisc_Type(Integer32):
    """Custom type alaDrcTmPimDebugDmMisc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugDmMisc_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugDmMisc_Object = MibScalar
alaDrcTmPimDebugDmMisc = _AlaDrcTmPimDebugDmMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 23),
    _AlaDrcTmPimDebugDmMisc_Type()
)
alaDrcTmPimDebugDmMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugDmMisc.setStatus("current")


class _AlaDrcTmPimDebugGraft_Type(Integer32):
    """Custom type alaDrcTmPimDebugGraft based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugGraft_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugGraft_Object = MibScalar
alaDrcTmPimDebugGraft = _AlaDrcTmPimDebugGraft_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 24),
    _AlaDrcTmPimDebugGraft_Type()
)
alaDrcTmPimDebugGraft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugGraft.setStatus("current")


class _AlaDrcTmPimDebugStateRefresh_Type(Integer32):
    """Custom type alaDrcTmPimDebugStateRefresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugStateRefresh_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugStateRefresh_Object = MibScalar
alaDrcTmPimDebugStateRefresh = _AlaDrcTmPimDebugStateRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 25),
    _AlaDrcTmPimDebugStateRefresh_Type()
)
alaDrcTmPimDebugStateRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugStateRefresh.setStatus("current")


class _AlaDrcTmPimDebugAll_Type(Integer32):
    """Custom type alaDrcTmPimDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmPimDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmPimDebugAll_Object = MibScalar
alaDrcTmPimDebugAll = _AlaDrcTmPimDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 7, 26),
    _AlaDrcTmPimDebugAll_Type()
)
alaDrcTmPimDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmPimDebugAll.setStatus("current")
_AlaDrcTmRipngDebug_ObjectIdentity = ObjectIdentity
alaDrcTmRipngDebug = _AlaDrcTmRipngDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8)
)


class _AlaDrcTmRipngDebugError_Type(Integer32):
    """Custom type alaDrcTmRipngDebugError based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugError_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugError_Object = MibScalar
alaDrcTmRipngDebugError = _AlaDrcTmRipngDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 1),
    _AlaDrcTmRipngDebugError_Type()
)
alaDrcTmRipngDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugError.setStatus("current")


class _AlaDrcTmRipngDebugWarning_Type(Integer32):
    """Custom type alaDrcTmRipngDebugWarning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugWarning_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugWarning_Object = MibScalar
alaDrcTmRipngDebugWarning = _AlaDrcTmRipngDebugWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 2),
    _AlaDrcTmRipngDebugWarning_Type()
)
alaDrcTmRipngDebugWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugWarning.setStatus("current")


class _AlaDrcTmRipngDebugRecv_Type(Integer32):
    """Custom type alaDrcTmRipngDebugRecv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugRecv_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugRecv_Object = MibScalar
alaDrcTmRipngDebugRecv = _AlaDrcTmRipngDebugRecv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 3),
    _AlaDrcTmRipngDebugRecv_Type()
)
alaDrcTmRipngDebugRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugRecv.setStatus("current")


class _AlaDrcTmRipngDebugSend_Type(Integer32):
    """Custom type alaDrcTmRipngDebugSend based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugSend_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugSend_Object = MibScalar
alaDrcTmRipngDebugSend = _AlaDrcTmRipngDebugSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 4),
    _AlaDrcTmRipngDebugSend_Type()
)
alaDrcTmRipngDebugSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugSend.setStatus("current")


class _AlaDrcTmRipngDebugRdb_Type(Integer32):
    """Custom type alaDrcTmRipngDebugRdb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugRdb_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugRdb_Object = MibScalar
alaDrcTmRipngDebugRdb = _AlaDrcTmRipngDebugRdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 5),
    _AlaDrcTmRipngDebugRdb_Type()
)
alaDrcTmRipngDebugRdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugRdb.setStatus("current")


class _AlaDrcTmRipngDebugAge_Type(Integer32):
    """Custom type alaDrcTmRipngDebugAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugAge_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugAge_Object = MibScalar
alaDrcTmRipngDebugAge = _AlaDrcTmRipngDebugAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 6),
    _AlaDrcTmRipngDebugAge_Type()
)
alaDrcTmRipngDebugAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugAge.setStatus("current")


class _AlaDrcTmRipngDebugMip_Type(Integer32):
    """Custom type alaDrcTmRipngDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugMip_Object = MibScalar
alaDrcTmRipngDebugMip = _AlaDrcTmRipngDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 7),
    _AlaDrcTmRipngDebugMip_Type()
)
alaDrcTmRipngDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugMip.setStatus("current")


class _AlaDrcTmRipngDebugInfo_Type(Integer32):
    """Custom type alaDrcTmRipngDebugInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugInfo_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugInfo_Object = MibScalar
alaDrcTmRipngDebugInfo = _AlaDrcTmRipngDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 8),
    _AlaDrcTmRipngDebugInfo_Type()
)
alaDrcTmRipngDebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugInfo.setStatus("current")


class _AlaDrcTmRipngDebugSetup_Type(Integer32):
    """Custom type alaDrcTmRipngDebugSetup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugSetup_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugSetup_Object = MibScalar
alaDrcTmRipngDebugSetup = _AlaDrcTmRipngDebugSetup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 9),
    _AlaDrcTmRipngDebugSetup_Type()
)
alaDrcTmRipngDebugSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugSetup.setStatus("current")


class _AlaDrcTmRipngDebugTime_Type(Integer32):
    """Custom type alaDrcTmRipngDebugTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugTime_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugTime_Object = MibScalar
alaDrcTmRipngDebugTime = _AlaDrcTmRipngDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 10),
    _AlaDrcTmRipngDebugTime_Type()
)
alaDrcTmRipngDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugTime.setStatus("current")


class _AlaDrcTmRipngDebugTm_Type(Integer32):
    """Custom type alaDrcTmRipngDebugTm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugTm_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugTm_Object = MibScalar
alaDrcTmRipngDebugTm = _AlaDrcTmRipngDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 11),
    _AlaDrcTmRipngDebugTm_Type()
)
alaDrcTmRipngDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugTm.setStatus("current")


class _AlaDrcTmRipngDebugRouteFilter_Type(Integer32):
    """Custom type alaDrcTmRipngDebugRouteFilter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugRouteFilter_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugRouteFilter_Object = MibScalar
alaDrcTmRipngDebugRouteFilter = _AlaDrcTmRipngDebugRouteFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 12),
    _AlaDrcTmRipngDebugRouteFilter_Type()
)
alaDrcTmRipngDebugRouteFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugRouteFilter.setStatus("current")


class _AlaDrcTmRipngDebugNexthopFilter_Type(Integer32):
    """Custom type alaDrcTmRipngDebugNexthopFilter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugNexthopFilter_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugNexthopFilter_Object = MibScalar
alaDrcTmRipngDebugNexthopFilter = _AlaDrcTmRipngDebugNexthopFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 13),
    _AlaDrcTmRipngDebugNexthopFilter_Type()
)
alaDrcTmRipngDebugNexthopFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugNexthopFilter.setStatus("current")


class _AlaDrcTmRipngDebugSummary_Type(Integer32):
    """Custom type alaDrcTmRipngDebugSummary based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugSummary_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugSummary_Object = MibScalar
alaDrcTmRipngDebugSummary = _AlaDrcTmRipngDebugSummary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 14),
    _AlaDrcTmRipngDebugSummary_Type()
)
alaDrcTmRipngDebugSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugSummary.setStatus("current")


class _AlaDrcTmRipngDebugAll_Type(Integer32):
    """Custom type alaDrcTmRipngDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugAll_Object = MibScalar
alaDrcTmRipngDebugAll = _AlaDrcTmRipngDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 15),
    _AlaDrcTmRipngDebugAll_Type()
)
alaDrcTmRipngDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugAll.setStatus("current")


class _AlaDrcTmRipngDebugRedist_Type(Integer32):
    """Custom type alaDrcTmRipngDebugRedist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmRipngDebugRedist_Type.__name__ = "Integer32"
_AlaDrcTmRipngDebugRedist_Object = MibScalar
alaDrcTmRipngDebugRedist = _AlaDrcTmRipngDebugRedist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 8, 16),
    _AlaDrcTmRipngDebugRedist_Type()
)
alaDrcTmRipngDebugRedist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugRedist.setStatus("current")
_AlaDrcTmIprmDebug_ObjectIdentity = ObjectIdentity
alaDrcTmIprmDebug = _AlaDrcTmIprmDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9)
)


class _AlaDrcTmIprmDebugError_Type(Integer32):
    """Custom type alaDrcTmIprmDebugError based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugError_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugError_Object = MibScalar
alaDrcTmIprmDebugError = _AlaDrcTmIprmDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 1),
    _AlaDrcTmIprmDebugError_Type()
)
alaDrcTmIprmDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugError.setStatus("current")


class _AlaDrcTmIprmDebugAccesslist_Type(Integer32):
    """Custom type alaDrcTmIprmDebugAccesslist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugAccesslist_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugAccesslist_Object = MibScalar
alaDrcTmIprmDebugAccesslist = _AlaDrcTmIprmDebugAccesslist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 2),
    _AlaDrcTmIprmDebugAccesslist_Type()
)
alaDrcTmIprmDebugAccesslist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugAccesslist.setStatus("current")


class _AlaDrcTmIprmDebugIntf_Type(Integer32):
    """Custom type alaDrcTmIprmDebugIntf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugIntf_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugIntf_Object = MibScalar
alaDrcTmIprmDebugIntf = _AlaDrcTmIprmDebugIntf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 3),
    _AlaDrcTmIprmDebugIntf_Type()
)
alaDrcTmIprmDebugIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugIntf.setStatus("current")


class _AlaDrcTmIprmDebugMip_Type(Integer32):
    """Custom type alaDrcTmIprmDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugMip_Object = MibScalar
alaDrcTmIprmDebugMip = _AlaDrcTmIprmDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 4),
    _AlaDrcTmIprmDebugMip_Type()
)
alaDrcTmIprmDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugMip.setStatus("current")


class _AlaDrcTmIprmDebugMisc_Type(Integer32):
    """Custom type alaDrcTmIprmDebugMisc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugMisc_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugMisc_Object = MibScalar
alaDrcTmIprmDebugMisc = _AlaDrcTmIprmDebugMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 5),
    _AlaDrcTmIprmDebugMisc_Type()
)
alaDrcTmIprmDebugMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugMisc.setStatus("current")


class _AlaDrcTmIprmDebugNhs_Type(Integer32):
    """Custom type alaDrcTmIprmDebugNhs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugNhs_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugNhs_Object = MibScalar
alaDrcTmIprmDebugNhs = _AlaDrcTmIprmDebugNhs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 6),
    _AlaDrcTmIprmDebugNhs_Type()
)
alaDrcTmIprmDebugNhs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugNhs.setStatus("current")


class _AlaDrcTmIprmDebugPrefix_Type(Integer32):
    """Custom type alaDrcTmIprmDebugPrefix based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugPrefix_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugPrefix_Object = MibScalar
alaDrcTmIprmDebugPrefix = _AlaDrcTmIprmDebugPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 7),
    _AlaDrcTmIprmDebugPrefix_Type()
)
alaDrcTmIprmDebugPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugPrefix.setStatus("current")


class _AlaDrcTmIprmDebugRedist_Type(Integer32):
    """Custom type alaDrcTmIprmDebugRedist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugRedist_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugRedist_Object = MibScalar
alaDrcTmIprmDebugRedist = _AlaDrcTmIprmDebugRedist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 8),
    _AlaDrcTmIprmDebugRedist_Type()
)
alaDrcTmIprmDebugRedist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugRedist.setStatus("current")


class _AlaDrcTmIprmDebugRoute4_Type(Integer32):
    """Custom type alaDrcTmIprmDebugRoute4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugRoute4_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugRoute4_Object = MibScalar
alaDrcTmIprmDebugRoute4 = _AlaDrcTmIprmDebugRoute4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 9),
    _AlaDrcTmIprmDebugRoute4_Type()
)
alaDrcTmIprmDebugRoute4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugRoute4.setStatus("current")


class _AlaDrcTmIprmDebugRoute6_Type(Integer32):
    """Custom type alaDrcTmIprmDebugRoute6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugRoute6_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugRoute6_Object = MibScalar
alaDrcTmIprmDebugRoute6 = _AlaDrcTmIprmDebugRoute6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 10),
    _AlaDrcTmIprmDebugRoute6_Type()
)
alaDrcTmIprmDebugRoute6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugRoute6.setStatus("current")


class _AlaDrcTmIprmDebugRoutemap_Type(Integer32):
    """Custom type alaDrcTmIprmDebugRoutemap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugRoutemap_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugRoutemap_Object = MibScalar
alaDrcTmIprmDebugRoutemap = _AlaDrcTmIprmDebugRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 11),
    _AlaDrcTmIprmDebugRoutemap_Type()
)
alaDrcTmIprmDebugRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugRoutemap.setStatus("current")


class _AlaDrcTmIprmDebugRoutepref_Type(Integer32):
    """Custom type alaDrcTmIprmDebugRoutepref based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugRoutepref_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugRoutepref_Object = MibScalar
alaDrcTmIprmDebugRoutepref = _AlaDrcTmIprmDebugRoutepref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 12),
    _AlaDrcTmIprmDebugRoutepref_Type()
)
alaDrcTmIprmDebugRoutepref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugRoutepref.setStatus("current")


class _AlaDrcTmIprmDebugStatic_Type(Integer32):
    """Custom type alaDrcTmIprmDebugStatic based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugStatic_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugStatic_Object = MibScalar
alaDrcTmIprmDebugStatic = _AlaDrcTmIprmDebugStatic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 13),
    _AlaDrcTmIprmDebugStatic_Type()
)
alaDrcTmIprmDebugStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugStatic.setStatus("current")


class _AlaDrcTmIprmDebugAll_Type(Integer32):
    """Custom type alaDrcTmIprmDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugAll_Object = MibScalar
alaDrcTmIprmDebugAll = _AlaDrcTmIprmDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 14),
    _AlaDrcTmIprmDebugAll_Type()
)
alaDrcTmIprmDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugAll.setStatus("current")


class _AlaDrcTmIprmDebugBfd_Type(Integer32):
    """Custom type alaDrcTmIprmDebugBfd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIprmDebugBfd_Type.__name__ = "Integer32"
_AlaDrcTmIprmDebugBfd_Object = MibScalar
alaDrcTmIprmDebugBfd = _AlaDrcTmIprmDebugBfd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 9, 15),
    _AlaDrcTmIprmDebugBfd_Type()
)
alaDrcTmIprmDebugBfd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugBfd.setStatus("current")
_AlaDrcTmIpmrmDebug_ObjectIdentity = ObjectIdentity
alaDrcTmIpmrmDebug = _AlaDrcTmIpmrmDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10)
)


class _AlaDrcTmIpmrmDebugError_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugError based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugError_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugError_Object = MibScalar
alaDrcTmIpmrmDebugError = _AlaDrcTmIpmrmDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 1),
    _AlaDrcTmIpmrmDebugError_Type()
)
alaDrcTmIpmrmDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugError.setStatus("current")


class _AlaDrcTmIpmrmDebugFib_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugFib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugFib_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugFib_Object = MibScalar
alaDrcTmIpmrmDebugFib = _AlaDrcTmIpmrmDebugFib_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 2),
    _AlaDrcTmIpmrmDebugFib_Type()
)
alaDrcTmIpmrmDebugFib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugFib.setStatus("current")


class _AlaDrcTmIpmrmDebugAging_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugAging based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugAging_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugAging_Object = MibScalar
alaDrcTmIpmrmDebugAging = _AlaDrcTmIpmrmDebugAging_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 3),
    _AlaDrcTmIpmrmDebugAging_Type()
)
alaDrcTmIpmrmDebugAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugAging.setStatus("current")


class _AlaDrcTmIpmrmDebugProtos_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugProtos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugProtos_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugProtos_Object = MibScalar
alaDrcTmIpmrmDebugProtos = _AlaDrcTmIpmrmDebugProtos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 4),
    _AlaDrcTmIpmrmDebugProtos_Type()
)
alaDrcTmIpmrmDebugProtos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugProtos.setStatus("current")


class _AlaDrcTmIpmrmDebugIpms_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugIpms based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugIpms_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugIpms_Object = MibScalar
alaDrcTmIpmrmDebugIpms = _AlaDrcTmIpmrmDebugIpms_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 5),
    _AlaDrcTmIpmrmDebugIpms_Type()
)
alaDrcTmIpmrmDebugIpms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugIpms.setStatus("current")


class _AlaDrcTmIpmrmDebugMip_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugMip_Object = MibScalar
alaDrcTmIpmrmDebugMip = _AlaDrcTmIpmrmDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 6),
    _AlaDrcTmIpmrmDebugMip_Type()
)
alaDrcTmIpmrmDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugMip.setStatus("current")


class _AlaDrcTmIpmrmDebugInit_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugInit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugInit_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugInit_Object = MibScalar
alaDrcTmIpmrmDebugInit = _AlaDrcTmIpmrmDebugInit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 7),
    _AlaDrcTmIpmrmDebugInit_Type()
)
alaDrcTmIpmrmDebugInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugInit.setStatus("current")


class _AlaDrcTmIpmrmDebugTm_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugTm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugTm_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugTm_Object = MibScalar
alaDrcTmIpmrmDebugTm = _AlaDrcTmIpmrmDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 8),
    _AlaDrcTmIpmrmDebugTm_Type()
)
alaDrcTmIpmrmDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugTm.setStatus("current")


class _AlaDrcTmIpmrmDebugMisc_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugMisc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugMisc_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugMisc_Object = MibScalar
alaDrcTmIpmrmDebugMisc = _AlaDrcTmIpmrmDebugMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 9),
    _AlaDrcTmIpmrmDebugMisc_Type()
)
alaDrcTmIpmrmDebugMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugMisc.setStatus("current")


class _AlaDrcTmIpmrmDebugAll_Type(Integer32):
    """Custom type alaDrcTmIpmrmDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIpmrmDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmIpmrmDebugAll_Object = MibScalar
alaDrcTmIpmrmDebugAll = _AlaDrcTmIpmrmDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 10, 10),
    _AlaDrcTmIpmrmDebugAll_Type()
)
alaDrcTmIpmrmDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugAll.setStatus("current")
_AlaDrcTmOspf3Debug_ObjectIdentity = ObjectIdentity
alaDrcTmOspf3Debug = _AlaDrcTmOspf3Debug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11)
)


class _AlaDrcTmOspf3DebugError_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugError based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugError_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugError_Object = MibScalar
alaDrcTmOspf3DebugError = _AlaDrcTmOspf3DebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 1),
    _AlaDrcTmOspf3DebugError_Type()
)
alaDrcTmOspf3DebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugError.setStatus("current")


class _AlaDrcTmOspf3DebugInfo_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugInfo_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugInfo_Object = MibScalar
alaDrcTmOspf3DebugInfo = _AlaDrcTmOspf3DebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 2),
    _AlaDrcTmOspf3DebugInfo_Type()
)
alaDrcTmOspf3DebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugInfo.setStatus("current")


class _AlaDrcTmOspf3DebugIntf_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugIntf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugIntf_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugIntf_Object = MibScalar
alaDrcTmOspf3DebugIntf = _AlaDrcTmOspf3DebugIntf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 3),
    _AlaDrcTmOspf3DebugIntf_Type()
)
alaDrcTmOspf3DebugIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugIntf.setStatus("current")


class _AlaDrcTmOspf3DebugRecv_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugRecv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugRecv_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugRecv_Object = MibScalar
alaDrcTmOspf3DebugRecv = _AlaDrcTmOspf3DebugRecv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 4),
    _AlaDrcTmOspf3DebugRecv_Type()
)
alaDrcTmOspf3DebugRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugRecv.setStatus("current")


class _AlaDrcTmOspf3DebugSend_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugSend based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugSend_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugSend_Object = MibScalar
alaDrcTmOspf3DebugSend = _AlaDrcTmOspf3DebugSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 5),
    _AlaDrcTmOspf3DebugSend_Type()
)
alaDrcTmOspf3DebugSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugSend.setStatus("current")


class _AlaDrcTmOspf3DebugNbr_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugNbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugNbr_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugNbr_Object = MibScalar
alaDrcTmOspf3DebugNbr = _AlaDrcTmOspf3DebugNbr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 6),
    _AlaDrcTmOspf3DebugNbr_Type()
)
alaDrcTmOspf3DebugNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugNbr.setStatus("current")


class _AlaDrcTmOspf3DebugState_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugState_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugState_Object = MibScalar
alaDrcTmOspf3DebugState = _AlaDrcTmOspf3DebugState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 7),
    _AlaDrcTmOspf3DebugState_Type()
)
alaDrcTmOspf3DebugState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugState.setStatus("current")


class _AlaDrcTmOspf3DebugArea_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugArea based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugArea_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugArea_Object = MibScalar
alaDrcTmOspf3DebugArea = _AlaDrcTmOspf3DebugArea_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 8),
    _AlaDrcTmOspf3DebugArea_Type()
)
alaDrcTmOspf3DebugArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugArea.setStatus("current")


class _AlaDrcTmOspf3DebugLsa_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugLsa based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugLsa_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugLsa_Object = MibScalar
alaDrcTmOspf3DebugLsa = _AlaDrcTmOspf3DebugLsa_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 9),
    _AlaDrcTmOspf3DebugLsa_Type()
)
alaDrcTmOspf3DebugLsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugLsa.setStatus("current")


class _AlaDrcTmOspf3DebugFlood_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugFlood based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugFlood_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugFlood_Object = MibScalar
alaDrcTmOspf3DebugFlood = _AlaDrcTmOspf3DebugFlood_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 10),
    _AlaDrcTmOspf3DebugFlood_Type()
)
alaDrcTmOspf3DebugFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugFlood.setStatus("current")


class _AlaDrcTmOspf3DebugSpf_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugSpf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugSpf_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugSpf_Object = MibScalar
alaDrcTmOspf3DebugSpf = _AlaDrcTmOspf3DebugSpf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 11),
    _AlaDrcTmOspf3DebugSpf_Type()
)
alaDrcTmOspf3DebugSpf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugSpf.setStatus("current")


class _AlaDrcTmOspf3DebugRdb_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugRdb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugRdb_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugRdb_Object = MibScalar
alaDrcTmOspf3DebugRdb = _AlaDrcTmOspf3DebugRdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 12),
    _AlaDrcTmOspf3DebugRdb_Type()
)
alaDrcTmOspf3DebugRdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugRdb.setStatus("current")


class _AlaDrcTmOspf3DebugVlink_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugVlink based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugVlink_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugVlink_Object = MibScalar
alaDrcTmOspf3DebugVlink = _AlaDrcTmOspf3DebugVlink_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 13),
    _AlaDrcTmOspf3DebugVlink_Type()
)
alaDrcTmOspf3DebugVlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugVlink.setStatus("current")


class _AlaDrcTmOspf3DebugMip_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugMip_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugMip_Object = MibScalar
alaDrcTmOspf3DebugMip = _AlaDrcTmOspf3DebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 14),
    _AlaDrcTmOspf3DebugMip_Type()
)
alaDrcTmOspf3DebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugMip.setStatus("current")


class _AlaDrcTmOspf3DebugAll_Type(Integer32):
    """Custom type alaDrcTmOspf3DebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmOspf3DebugAll_Type.__name__ = "Integer32"
_AlaDrcTmOspf3DebugAll_Object = MibScalar
alaDrcTmOspf3DebugAll = _AlaDrcTmOspf3DebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 11, 15),
    _AlaDrcTmOspf3DebugAll_Type()
)
alaDrcTmOspf3DebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugAll.setStatus("current")
_AlaDrcTmLogDestination_ObjectIdentity = ObjectIdentity
alaDrcTmLogDestination = _AlaDrcTmLogDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12)
)


class _AlaDrcTmLogToSysFacility_Type(Integer32):
    """Custom type alaDrcTmLogToSysFacility based on Integer32"""
    defaultValue = 1

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
        *(("printf", 1),
          ("ringBuffer", 7),
          ("session", 2),
          ("swLog", 3),
          ("sysLog", 5),
          ("sysTrace", 4),
          ("truncBuffer", 6))
    )


_AlaDrcTmLogToSysFacility_Type.__name__ = "Integer32"
_AlaDrcTmLogToSysFacility_Object = MibScalar
alaDrcTmLogToSysFacility = _AlaDrcTmLogToSysFacility_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 1),
    _AlaDrcTmLogToSysFacility_Type()
)
alaDrcTmLogToSysFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogToSysFacility.setStatus("current")


class _AlaDrcTmLogToSessionId_Type(Integer32):
    """Custom type alaDrcTmLogToSessionId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaDrcTmLogToSessionId_Type.__name__ = "Integer32"
_AlaDrcTmLogToSessionId_Object = MibScalar
alaDrcTmLogToSessionId = _AlaDrcTmLogToSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 2),
    _AlaDrcTmLogToSessionId_Type()
)
alaDrcTmLogToSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogToSessionId.setStatus("current")


class _AlaDrcTmLogBufferSize_Type(Integer32):
    """Custom type alaDrcTmLogBufferSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AlaDrcTmLogBufferSize_Type.__name__ = "Integer32"
_AlaDrcTmLogBufferSize_Object = MibScalar
alaDrcTmLogBufferSize = _AlaDrcTmLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 3),
    _AlaDrcTmLogBufferSize_Type()
)
alaDrcTmLogBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogBufferSize.setStatus("current")


class _AlaDrcTmLogBufferDumpfile_Type(DisplayString):
    """Custom type alaDrcTmLogBufferDumpfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDrcTmLogBufferDumpfile_Type.__name__ = "DisplayString"
_AlaDrcTmLogBufferDumpfile_Object = MibScalar
alaDrcTmLogBufferDumpfile = _AlaDrcTmLogBufferDumpfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 4),
    _AlaDrcTmLogBufferDumpfile_Type()
)
alaDrcTmLogBufferDumpfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogBufferDumpfile.setStatus("current")


class _AlaDrcTmLogCriticalBufferDumpfile_Type(DisplayString):
    """Custom type alaDrcTmLogCriticalBufferDumpfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDrcTmLogCriticalBufferDumpfile_Type.__name__ = "DisplayString"
_AlaDrcTmLogCriticalBufferDumpfile_Object = MibScalar
alaDrcTmLogCriticalBufferDumpfile = _AlaDrcTmLogCriticalBufferDumpfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 5),
    _AlaDrcTmLogCriticalBufferDumpfile_Type()
)
alaDrcTmLogCriticalBufferDumpfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogCriticalBufferDumpfile.setStatus("current")


class _AlaDrcTmLogShowTask_Type(Integer32):
    """Custom type alaDrcTmLogShowTask based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDrcTmLogShowTask_Type.__name__ = "Integer32"
_AlaDrcTmLogShowTask_Object = MibScalar
alaDrcTmLogShowTask = _AlaDrcTmLogShowTask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 6),
    _AlaDrcTmLogShowTask_Type()
)
alaDrcTmLogShowTask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogShowTask.setStatus("current")


class _AlaDrcTmLogShowFunction_Type(Integer32):
    """Custom type alaDrcTmLogShowFunction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDrcTmLogShowFunction_Type.__name__ = "Integer32"
_AlaDrcTmLogShowFunction_Object = MibScalar
alaDrcTmLogShowFunction = _AlaDrcTmLogShowFunction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 7),
    _AlaDrcTmLogShowFunction_Type()
)
alaDrcTmLogShowFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogShowFunction.setStatus("current")


class _AlaDrcTmLogShowLine_Type(Integer32):
    """Custom type alaDrcTmLogShowLine based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDrcTmLogShowLine_Type.__name__ = "Integer32"
_AlaDrcTmLogShowLine_Object = MibScalar
alaDrcTmLogShowLine = _AlaDrcTmLogShowLine_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 8),
    _AlaDrcTmLogShowLine_Type()
)
alaDrcTmLogShowLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogShowLine.setStatus("current")


class _AlaDrcTmLogShowDate_Type(Integer32):
    """Custom type alaDrcTmLogShowDate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDrcTmLogShowDate_Type.__name__ = "Integer32"
_AlaDrcTmLogShowDate_Object = MibScalar
alaDrcTmLogShowDate = _AlaDrcTmLogShowDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 9),
    _AlaDrcTmLogShowDate_Type()
)
alaDrcTmLogShowDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogShowDate.setStatus("current")


class _AlaDrcTmLogShowTime_Type(Integer32):
    """Custom type alaDrcTmLogShowTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDrcTmLogShowTime_Type.__name__ = "Integer32"
_AlaDrcTmLogShowTime_Object = MibScalar
alaDrcTmLogShowTime = _AlaDrcTmLogShowTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 10),
    _AlaDrcTmLogShowTime_Type()
)
alaDrcTmLogShowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogShowTime.setStatus("current")


class _AlaDrcTmLogClearBuffer_Type(Integer32):
    """Custom type alaDrcTmLogClearBuffer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("buffer", 1),
          ("criticalbuffer", 2))
    )


_AlaDrcTmLogClearBuffer_Type.__name__ = "Integer32"
_AlaDrcTmLogClearBuffer_Object = MibScalar
alaDrcTmLogClearBuffer = _AlaDrcTmLogClearBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 12, 11),
    _AlaDrcTmLogClearBuffer_Type()
)
alaDrcTmLogClearBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmLogClearBuffer.setStatus("current")
_AlaDrcTmIsisDebug_ObjectIdentity = ObjectIdentity
alaDrcTmIsisDebug = _AlaDrcTmIsisDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13)
)


class _AlaDrcTmIsisDebugError_Type(Integer32):
    """Custom type alaDrcTmIsisDebugError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugError_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugError_Object = MibScalar
alaDrcTmIsisDebugError = _AlaDrcTmIsisDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 1),
    _AlaDrcTmIsisDebugError_Type()
)
alaDrcTmIsisDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugError.setStatus("current")


class _AlaDrcTmIsisDebugWarn_Type(Integer32):
    """Custom type alaDrcTmIsisDebugWarn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugWarn_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugWarn_Object = MibScalar
alaDrcTmIsisDebugWarn = _AlaDrcTmIsisDebugWarn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 2),
    _AlaDrcTmIsisDebugWarn_Type()
)
alaDrcTmIsisDebugWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugWarn.setStatus("current")


class _AlaDrcTmIsisDebugPkt_Type(Integer32):
    """Custom type alaDrcTmIsisDebugPkt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugPkt_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugPkt_Object = MibScalar
alaDrcTmIsisDebugPkt = _AlaDrcTmIsisDebugPkt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 3),
    _AlaDrcTmIsisDebugPkt_Type()
)
alaDrcTmIsisDebugPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugPkt.setStatus("current")


class _AlaDrcTmIsisDebugAdj_Type(Integer32):
    """Custom type alaDrcTmIsisDebugAdj based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugAdj_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugAdj_Object = MibScalar
alaDrcTmIsisDebugAdj = _AlaDrcTmIsisDebugAdj_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 4),
    _AlaDrcTmIsisDebugAdj_Type()
)
alaDrcTmIsisDebugAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugAdj.setStatus("current")


class _AlaDrcTmIsisDebugCkt_Type(Integer32):
    """Custom type alaDrcTmIsisDebugCkt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugCkt_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugCkt_Object = MibScalar
alaDrcTmIsisDebugCkt = _AlaDrcTmIsisDebugCkt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 5),
    _AlaDrcTmIsisDebugCkt_Type()
)
alaDrcTmIsisDebugCkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugCkt.setStatus("current")


class _AlaDrcTmIsisDebugSpf_Type(Integer32):
    """Custom type alaDrcTmIsisDebugSpf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugSpf_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugSpf_Object = MibScalar
alaDrcTmIsisDebugSpf = _AlaDrcTmIsisDebugSpf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 6),
    _AlaDrcTmIsisDebugSpf_Type()
)
alaDrcTmIsisDebugSpf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugSpf.setStatus("current")


class _AlaDrcTmIsisDebugLsp_Type(Integer32):
    """Custom type alaDrcTmIsisDebugLsp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugLsp_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugLsp_Object = MibScalar
alaDrcTmIsisDebugLsp = _AlaDrcTmIsisDebugLsp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 7),
    _AlaDrcTmIsisDebugLsp_Type()
)
alaDrcTmIsisDebugLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugLsp.setStatus("current")


class _AlaDrcTmIsisDebugFlood_Type(Integer32):
    """Custom type alaDrcTmIsisDebugFlood based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugFlood_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugFlood_Object = MibScalar
alaDrcTmIsisDebugFlood = _AlaDrcTmIsisDebugFlood_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 8),
    _AlaDrcTmIsisDebugFlood_Type()
)
alaDrcTmIsisDebugFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugFlood.setStatus("current")


class _AlaDrcTmIsisDebugIntf_Type(Integer32):
    """Custom type alaDrcTmIsisDebugIntf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugIntf_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugIntf_Object = MibScalar
alaDrcTmIsisDebugIntf = _AlaDrcTmIsisDebugIntf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 9),
    _AlaDrcTmIsisDebugIntf_Type()
)
alaDrcTmIsisDebugIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugIntf.setStatus("current")


class _AlaDrcTmIsisDebugIprm_Type(Integer32):
    """Custom type alaDrcTmIsisDebugIprm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugIprm_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugIprm_Object = MibScalar
alaDrcTmIsisDebugIprm = _AlaDrcTmIsisDebugIprm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 10),
    _AlaDrcTmIsisDebugIprm_Type()
)
alaDrcTmIsisDebugIprm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugIprm.setStatus("current")


class _AlaDrcTmIsisDebugMip_Type(Integer32):
    """Custom type alaDrcTmIsisDebugMip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugMip_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugMip_Object = MibScalar
alaDrcTmIsisDebugMip = _AlaDrcTmIsisDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 11),
    _AlaDrcTmIsisDebugMip_Type()
)
alaDrcTmIsisDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugMip.setStatus("current")


class _AlaDrcTmIsisDebugMsg_Type(Integer32):
    """Custom type alaDrcTmIsisDebugMsg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugMsg_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugMsg_Object = MibScalar
alaDrcTmIsisDebugMsg = _AlaDrcTmIsisDebugMsg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 12),
    _AlaDrcTmIsisDebugMsg_Type()
)
alaDrcTmIsisDebugMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugMsg.setStatus("current")


class _AlaDrcTmIsisDebugLeak_Type(Integer32):
    """Custom type alaDrcTmIsisDebugLeak based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugLeak_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugLeak_Object = MibScalar
alaDrcTmIsisDebugLeak = _AlaDrcTmIsisDebugLeak_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 13),
    _AlaDrcTmIsisDebugLeak_Type()
)
alaDrcTmIsisDebugLeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugLeak.setStatus("current")


class _AlaDrcTmIsisDebugSummary_Type(Integer32):
    """Custom type alaDrcTmIsisDebugSummary based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugSummary_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugSummary_Object = MibScalar
alaDrcTmIsisDebugSummary = _AlaDrcTmIsisDebugSummary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 14),
    _AlaDrcTmIsisDebugSummary_Type()
)
alaDrcTmIsisDebugSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugSummary.setStatus("current")


class _AlaDrcTmIsisDebugRestart_Type(Integer32):
    """Custom type alaDrcTmIsisDebugRestart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugRestart_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugRestart_Object = MibScalar
alaDrcTmIsisDebugRestart = _AlaDrcTmIsisDebugRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 15),
    _AlaDrcTmIsisDebugRestart_Type()
)
alaDrcTmIsisDebugRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugRestart.setStatus("current")


class _AlaDrcTmIsisDebugAll_Type(Integer32):
    """Custom type alaDrcTmIsisDebugAll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDrcTmIsisDebugAll_Type.__name__ = "Integer32"
_AlaDrcTmIsisDebugAll_Object = MibScalar
alaDrcTmIsisDebugAll = _AlaDrcTmIsisDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 1, 13, 16),
    _AlaDrcTmIsisDebugAll_Type()
)
alaDrcTmIsisDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugAll.setStatus("current")
_AlcatelIND1DrcTmMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1DrcTmMIBConformance = _AlcatelIND1DrcTmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2)
)
_AlcatelIND1DrcTmMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1DrcTmMIBCompliances = _AlcatelIND1DrcTmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 1)
)
_AlcatelIND1DrcTmMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1DrcTmMIBGroups = _AlcatelIND1DrcTmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2)
)

# Managed Objects groups

alaDrcTmConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 1)
)
alaDrcTmConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPRouterPrimaryAddress"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPRouterId"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPRipStatus"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPOspfStatus"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPBgpStatus"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPDvmrpStatus"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPPimStatus"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPMsdpStatus"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPRipngStatus"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPOspf3Status"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIPIsisStatus"))
)
if mibBuilder.loadTexts:
    alaDrcTmConfigMIBGroup.setStatus("current")

alaDrcTmDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 2)
)
alaDrcTmDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDebugTaskInfo"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDebugEvents"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDebugMisc"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmDebugMIBGroup.setStatus("current")

alaDrcTmRipDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 3)
)
alaDrcTmRipDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugWarning"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugRecv"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugSend"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugRdb"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugAge"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugConfig"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugRedist"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugInfo"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugSetup"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugTime"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipDebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmRipDebugMIBGroup.setStatus("current")

alaDrcTmOspfDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 4)
)
alaDrcTmOspfDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugWarning"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugState"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugRecv"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugSend"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugFlood"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugSPF"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugLsdb"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugRdb"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugAge"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugVlink"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugRedist"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugSummary"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugDbexch"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugHello"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugAuth"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugArea"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugIntf"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugInfo"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugSetup"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugTime"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugTm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspfDebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmOspfDebugMIBGroup.setStatus("current")

alaDrcTmBgpDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 5)
)
alaDrcTmBgpDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugDamp"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugFsm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugRecvUpd"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugSendUpd"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugOpen"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugKeepAlive"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugNotify"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugPolicy"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugRoute"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugSync"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugAggr"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugTcp"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugWarnings"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugErrors"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugRedist"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugPeer"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugLocal"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugTm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugInfo"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugRestart"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugAll"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugPeer6"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmBgpDebugRoute6"))
)
if mibBuilder.loadTexts:
    alaDrcTmBgpDebugMIBGroup.setStatus("current")

alaDrcTmDvmrpDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 6)
)
alaDrcTmDvmrpDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugNbr"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugRoutes"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugProbes"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugPrunes"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugGrafts"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugTime"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugIgmp"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugFlash"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugInit"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugTm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugIpmrm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugMisc"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmDvmrpDebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmDvmrpDebugMIBGroup.setStatus("current")

alaDrcTmPimDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 7)
)
alaDrcTmPimDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugInit"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugBootstrap"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugCRP"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugTime"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSpt"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSmNbr"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSmHello"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSmRoute"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSmJoinPrune"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSmAssert"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSmIgmp"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSmIpmrm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugSmMisc"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugDmNbr"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugDmHello"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugDmRoute"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugDmJoinPrune"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugDmAssert"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugDmIgmp"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugDmIpmrm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugDmMisc"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugGraft"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugStateRefresh"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmPimDebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmPimDebugMIBGroup.setStatus("current")

alaDrcTmRipngDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 8)
)
alaDrcTmRipngDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugWarning"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugRecv"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugSend"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugRdb"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugAge"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugInfo"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugSetup"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugTime"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugTm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugRouteFilter"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugNexthopFilter"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugSummary"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugAll"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmRipngDebugRedist"))
)
if mibBuilder.loadTexts:
    alaDrcTmRipngDebugMIBGroup.setStatus("current")

alaDrcTmIprmDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 9)
)
alaDrcTmIprmDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugAccesslist"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugIntf"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugMisc"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugNhs"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugPrefix"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugRedist"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugRoute4"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugRoute6"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugRoutemap"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugRoutepref"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugStatic"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugBfd"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIprmDebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmIprmDebugMIBGroup.setStatus("current")

alaDrcTmIpmrmDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 10)
)
alaDrcTmIpmrmDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugFib"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugAging"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugProtos"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugIpms"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugInit"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugTm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugMisc"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIpmrmDebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmIpmrmDebugMIBGroup.setStatus("current")

alaDrcTmOspf3DebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 11)
)
alaDrcTmOspf3DebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugInfo"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugIntf"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugRecv"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugSend"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugNbr"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugState"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugArea"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugLsa"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugFlood"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugSpf"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugRdb"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugVlink"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmOspf3DebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmOspf3DebugMIBGroup.setStatus("current")

alaDrcTmLogDestinationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 12)
)
alaDrcTmLogDestinationMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmLogToSysFacility"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmLogToSessionId"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmLogBufferSize"))
)
if mibBuilder.loadTexts:
    alaDrcTmLogDestinationMIBGroup.setStatus("current")

alaDrcTmIsisDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 2, 13)
)
alaDrcTmIsisDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugError"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugWarn"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugPkt"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugAdj"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugCkt"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugSpf"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugLsp"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugFlood"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugIntf"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugIprm"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugMip"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugMsg"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugLeak"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugSummary"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugRestart"),
        ("ALCATEL-IND1-DRCTM-MIB", "alaDrcTmIsisDebugAll"))
)
if mibBuilder.loadTexts:
    alaDrcTmIsisDebugMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaDrcTmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaDrcTmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DRCTM-MIB",
    **{"alcatelIND1DrcTmMIB": alcatelIND1DrcTmMIB,
       "alcatelIND1DrcTmMIBObjects": alcatelIND1DrcTmMIBObjects,
       "alaDrcTmConfig": alaDrcTmConfig,
       "alaDrcTmIPRouterPrimaryAddress": alaDrcTmIPRouterPrimaryAddress,
       "alaDrcTmIPRouterId": alaDrcTmIPRouterId,
       "alaDrcTmIPRipStatus": alaDrcTmIPRipStatus,
       "alaDrcTmIPOspfStatus": alaDrcTmIPOspfStatus,
       "alaDrcTmIPBgpStatus": alaDrcTmIPBgpStatus,
       "alaDrcTmIPDvmrpStatus": alaDrcTmIPDvmrpStatus,
       "alaDrcTmIPPimStatus": alaDrcTmIPPimStatus,
       "alaDrcTmIPMsdpStatus": alaDrcTmIPMsdpStatus,
       "alaDrcTmIPRipngStatus": alaDrcTmIPRipngStatus,
       "alaDrcTmIPOspf3Status": alaDrcTmIPOspf3Status,
       "alaDrcTmIPIsisStatus": alaDrcTmIPIsisStatus,
       "alaDrcTmDebug": alaDrcTmDebug,
       "alaDrcTmDebugLevel": alaDrcTmDebugLevel,
       "alaDrcTmDebugError": alaDrcTmDebugError,
       "alaDrcTmDebugUnusedA": alaDrcTmDebugUnusedA,
       "alaDrcTmDebugTaskInfo": alaDrcTmDebugTaskInfo,
       "alaDrcTmDebugEvents": alaDrcTmDebugEvents,
       "alaDrcTmDebugMip": alaDrcTmDebugMip,
       "alaDrcTmDebugUnusedB": alaDrcTmDebugUnusedB,
       "alaDrcTmDebugMisc": alaDrcTmDebugMisc,
       "alaDrcTmDebugUnused1": alaDrcTmDebugUnused1,
       "alaDrcTmDebugUnused2": alaDrcTmDebugUnused2,
       "alaDrcTmDebugUnused3": alaDrcTmDebugUnused3,
       "alaDrcTmDebugUnused4": alaDrcTmDebugUnused4,
       "alaDrcTmDebugAll": alaDrcTmDebugAll,
       "alaDrcTmRipDebug": alaDrcTmRipDebug,
       "alaDrcTmRipDebugError": alaDrcTmRipDebugError,
       "alaDrcTmRipDebugWarning": alaDrcTmRipDebugWarning,
       "alaDrcTmRipDebugRecv": alaDrcTmRipDebugRecv,
       "alaDrcTmRipDebugSend": alaDrcTmRipDebugSend,
       "alaDrcTmRipDebugRdb": alaDrcTmRipDebugRdb,
       "alaDrcTmRipDebugAge": alaDrcTmRipDebugAge,
       "alaDrcTmRipDebugConfig": alaDrcTmRipDebugConfig,
       "alaDrcTmRipDebugRedist": alaDrcTmRipDebugRedist,
       "alaDrcTmRipDebugInfo": alaDrcTmRipDebugInfo,
       "alaDrcTmRipDebugSetup": alaDrcTmRipDebugSetup,
       "alaDrcTmRipDebugTime": alaDrcTmRipDebugTime,
       "alaDrcTmRipDebugAll": alaDrcTmRipDebugAll,
       "alaDrcTmOspfDebug": alaDrcTmOspfDebug,
       "alaDrcTmOspfDebugError": alaDrcTmOspfDebugError,
       "alaDrcTmOspfDebugWarning": alaDrcTmOspfDebugWarning,
       "alaDrcTmOspfDebugState": alaDrcTmOspfDebugState,
       "alaDrcTmOspfDebugRecv": alaDrcTmOspfDebugRecv,
       "alaDrcTmOspfDebugSend": alaDrcTmOspfDebugSend,
       "alaDrcTmOspfDebugFlood": alaDrcTmOspfDebugFlood,
       "alaDrcTmOspfDebugSPF": alaDrcTmOspfDebugSPF,
       "alaDrcTmOspfDebugLsdb": alaDrcTmOspfDebugLsdb,
       "alaDrcTmOspfDebugRdb": alaDrcTmOspfDebugRdb,
       "alaDrcTmOspfDebugAge": alaDrcTmOspfDebugAge,
       "alaDrcTmOspfDebugVlink": alaDrcTmOspfDebugVlink,
       "alaDrcTmOspfDebugRedist": alaDrcTmOspfDebugRedist,
       "alaDrcTmOspfDebugSummary": alaDrcTmOspfDebugSummary,
       "alaDrcTmOspfDebugDbexch": alaDrcTmOspfDebugDbexch,
       "alaDrcTmOspfDebugHello": alaDrcTmOspfDebugHello,
       "alaDrcTmOspfDebugAuth": alaDrcTmOspfDebugAuth,
       "alaDrcTmOspfDebugArea": alaDrcTmOspfDebugArea,
       "alaDrcTmOspfDebugIntf": alaDrcTmOspfDebugIntf,
       "alaDrcTmOspfDebugMip": alaDrcTmOspfDebugMip,
       "alaDrcTmOspfDebugInfo": alaDrcTmOspfDebugInfo,
       "alaDrcTmOspfDebugSetup": alaDrcTmOspfDebugSetup,
       "alaDrcTmOspfDebugTime": alaDrcTmOspfDebugTime,
       "alaDrcTmOspfDebugTm": alaDrcTmOspfDebugTm,
       "alaDrcTmOspfDebugRestart": alaDrcTmOspfDebugRestart,
       "alaDrcTmOspfDebugHelper": alaDrcTmOspfDebugHelper,
       "alaDrcTmOspfDebugAll": alaDrcTmOspfDebugAll,
       "alaDrcTmBgpDebug": alaDrcTmBgpDebug,
       "alaDrcTmBgpDebugDamp": alaDrcTmBgpDebugDamp,
       "alaDrcTmBgpDebugFsm": alaDrcTmBgpDebugFsm,
       "alaDrcTmBgpDebugRecvUpd": alaDrcTmBgpDebugRecvUpd,
       "alaDrcTmBgpDebugSendUpd": alaDrcTmBgpDebugSendUpd,
       "alaDrcTmBgpDebugOpen": alaDrcTmBgpDebugOpen,
       "alaDrcTmBgpDebugKeepAlive": alaDrcTmBgpDebugKeepAlive,
       "alaDrcTmBgpDebugNotify": alaDrcTmBgpDebugNotify,
       "alaDrcTmBgpDebugPolicy": alaDrcTmBgpDebugPolicy,
       "alaDrcTmBgpDebugRoute": alaDrcTmBgpDebugRoute,
       "alaDrcTmBgpDebugSync": alaDrcTmBgpDebugSync,
       "alaDrcTmBgpDebugAggr": alaDrcTmBgpDebugAggr,
       "alaDrcTmBgpDebugTcp": alaDrcTmBgpDebugTcp,
       "alaDrcTmBgpDebugWarnings": alaDrcTmBgpDebugWarnings,
       "alaDrcTmBgpDebugErrors": alaDrcTmBgpDebugErrors,
       "alaDrcTmBgpDebugRedist": alaDrcTmBgpDebugRedist,
       "alaDrcTmBgpDebugPeer": alaDrcTmBgpDebugPeer,
       "alaDrcTmBgpDebugLocal": alaDrcTmBgpDebugLocal,
       "alaDrcTmBgpDebugMip": alaDrcTmBgpDebugMip,
       "alaDrcTmBgpDebugTm": alaDrcTmBgpDebugTm,
       "alaDrcTmBgpDebugInfo": alaDrcTmBgpDebugInfo,
       "alaDrcTmBgpDebugRestart": alaDrcTmBgpDebugRestart,
       "alaDrcTmBgpDebugAll": alaDrcTmBgpDebugAll,
       "alaDrcTmBgpDebugPeer6": alaDrcTmBgpDebugPeer6,
       "alaDrcTmBgpDebugRoute6": alaDrcTmBgpDebugRoute6,
       "alaDrcTmDvmrpDebug": alaDrcTmDvmrpDebug,
       "alaDrcTmDvmrpDebugError": alaDrcTmDvmrpDebugError,
       "alaDrcTmDvmrpDebugNbr": alaDrcTmDvmrpDebugNbr,
       "alaDrcTmDvmrpDebugRoutes": alaDrcTmDvmrpDebugRoutes,
       "alaDrcTmDvmrpDebugProbes": alaDrcTmDvmrpDebugProbes,
       "alaDrcTmDvmrpDebugPrunes": alaDrcTmDvmrpDebugPrunes,
       "alaDrcTmDvmrpDebugGrafts": alaDrcTmDvmrpDebugGrafts,
       "alaDrcTmDvmrpDebugTime": alaDrcTmDvmrpDebugTime,
       "alaDrcTmDvmrpDebugIgmp": alaDrcTmDvmrpDebugIgmp,
       "alaDrcTmDvmrpDebugFlash": alaDrcTmDvmrpDebugFlash,
       "alaDrcTmDvmrpDebugMip": alaDrcTmDvmrpDebugMip,
       "alaDrcTmDvmrpDebugInit": alaDrcTmDvmrpDebugInit,
       "alaDrcTmDvmrpDebugTm": alaDrcTmDvmrpDebugTm,
       "alaDrcTmDvmrpDebugIpmrm": alaDrcTmDvmrpDebugIpmrm,
       "alaDrcTmDvmrpDebugMisc": alaDrcTmDvmrpDebugMisc,
       "alaDrcTmDvmrpDebugAll": alaDrcTmDvmrpDebugAll,
       "alaDrcTmPimDebug": alaDrcTmPimDebug,
       "alaDrcTmPimDebugError": alaDrcTmPimDebugError,
       "alaDrcTmPimDebugMip": alaDrcTmPimDebugMip,
       "alaDrcTmPimDebugInit": alaDrcTmPimDebugInit,
       "alaDrcTmPimDebugBootstrap": alaDrcTmPimDebugBootstrap,
       "alaDrcTmPimDebugCRP": alaDrcTmPimDebugCRP,
       "alaDrcTmPimDebugTime": alaDrcTmPimDebugTime,
       "alaDrcTmPimDebugSpt": alaDrcTmPimDebugSpt,
       "alaDrcTmPimDebugSmNbr": alaDrcTmPimDebugSmNbr,
       "alaDrcTmPimDebugSmHello": alaDrcTmPimDebugSmHello,
       "alaDrcTmPimDebugSmRoute": alaDrcTmPimDebugSmRoute,
       "alaDrcTmPimDebugSmJoinPrune": alaDrcTmPimDebugSmJoinPrune,
       "alaDrcTmPimDebugSmAssert": alaDrcTmPimDebugSmAssert,
       "alaDrcTmPimDebugSmIgmp": alaDrcTmPimDebugSmIgmp,
       "alaDrcTmPimDebugSmIpmrm": alaDrcTmPimDebugSmIpmrm,
       "alaDrcTmPimDebugSmMisc": alaDrcTmPimDebugSmMisc,
       "alaDrcTmPimDebugDmNbr": alaDrcTmPimDebugDmNbr,
       "alaDrcTmPimDebugDmHello": alaDrcTmPimDebugDmHello,
       "alaDrcTmPimDebugDmRoute": alaDrcTmPimDebugDmRoute,
       "alaDrcTmPimDebugDmJoinPrune": alaDrcTmPimDebugDmJoinPrune,
       "alaDrcTmPimDebugDmAssert": alaDrcTmPimDebugDmAssert,
       "alaDrcTmPimDebugDmIgmp": alaDrcTmPimDebugDmIgmp,
       "alaDrcTmPimDebugDmIpmrm": alaDrcTmPimDebugDmIpmrm,
       "alaDrcTmPimDebugDmMisc": alaDrcTmPimDebugDmMisc,
       "alaDrcTmPimDebugGraft": alaDrcTmPimDebugGraft,
       "alaDrcTmPimDebugStateRefresh": alaDrcTmPimDebugStateRefresh,
       "alaDrcTmPimDebugAll": alaDrcTmPimDebugAll,
       "alaDrcTmRipngDebug": alaDrcTmRipngDebug,
       "alaDrcTmRipngDebugError": alaDrcTmRipngDebugError,
       "alaDrcTmRipngDebugWarning": alaDrcTmRipngDebugWarning,
       "alaDrcTmRipngDebugRecv": alaDrcTmRipngDebugRecv,
       "alaDrcTmRipngDebugSend": alaDrcTmRipngDebugSend,
       "alaDrcTmRipngDebugRdb": alaDrcTmRipngDebugRdb,
       "alaDrcTmRipngDebugAge": alaDrcTmRipngDebugAge,
       "alaDrcTmRipngDebugMip": alaDrcTmRipngDebugMip,
       "alaDrcTmRipngDebugInfo": alaDrcTmRipngDebugInfo,
       "alaDrcTmRipngDebugSetup": alaDrcTmRipngDebugSetup,
       "alaDrcTmRipngDebugTime": alaDrcTmRipngDebugTime,
       "alaDrcTmRipngDebugTm": alaDrcTmRipngDebugTm,
       "alaDrcTmRipngDebugRouteFilter": alaDrcTmRipngDebugRouteFilter,
       "alaDrcTmRipngDebugNexthopFilter": alaDrcTmRipngDebugNexthopFilter,
       "alaDrcTmRipngDebugSummary": alaDrcTmRipngDebugSummary,
       "alaDrcTmRipngDebugAll": alaDrcTmRipngDebugAll,
       "alaDrcTmRipngDebugRedist": alaDrcTmRipngDebugRedist,
       "alaDrcTmIprmDebug": alaDrcTmIprmDebug,
       "alaDrcTmIprmDebugError": alaDrcTmIprmDebugError,
       "alaDrcTmIprmDebugAccesslist": alaDrcTmIprmDebugAccesslist,
       "alaDrcTmIprmDebugIntf": alaDrcTmIprmDebugIntf,
       "alaDrcTmIprmDebugMip": alaDrcTmIprmDebugMip,
       "alaDrcTmIprmDebugMisc": alaDrcTmIprmDebugMisc,
       "alaDrcTmIprmDebugNhs": alaDrcTmIprmDebugNhs,
       "alaDrcTmIprmDebugPrefix": alaDrcTmIprmDebugPrefix,
       "alaDrcTmIprmDebugRedist": alaDrcTmIprmDebugRedist,
       "alaDrcTmIprmDebugRoute4": alaDrcTmIprmDebugRoute4,
       "alaDrcTmIprmDebugRoute6": alaDrcTmIprmDebugRoute6,
       "alaDrcTmIprmDebugRoutemap": alaDrcTmIprmDebugRoutemap,
       "alaDrcTmIprmDebugRoutepref": alaDrcTmIprmDebugRoutepref,
       "alaDrcTmIprmDebugStatic": alaDrcTmIprmDebugStatic,
       "alaDrcTmIprmDebugAll": alaDrcTmIprmDebugAll,
       "alaDrcTmIprmDebugBfd": alaDrcTmIprmDebugBfd,
       "alaDrcTmIpmrmDebug": alaDrcTmIpmrmDebug,
       "alaDrcTmIpmrmDebugError": alaDrcTmIpmrmDebugError,
       "alaDrcTmIpmrmDebugFib": alaDrcTmIpmrmDebugFib,
       "alaDrcTmIpmrmDebugAging": alaDrcTmIpmrmDebugAging,
       "alaDrcTmIpmrmDebugProtos": alaDrcTmIpmrmDebugProtos,
       "alaDrcTmIpmrmDebugIpms": alaDrcTmIpmrmDebugIpms,
       "alaDrcTmIpmrmDebugMip": alaDrcTmIpmrmDebugMip,
       "alaDrcTmIpmrmDebugInit": alaDrcTmIpmrmDebugInit,
       "alaDrcTmIpmrmDebugTm": alaDrcTmIpmrmDebugTm,
       "alaDrcTmIpmrmDebugMisc": alaDrcTmIpmrmDebugMisc,
       "alaDrcTmIpmrmDebugAll": alaDrcTmIpmrmDebugAll,
       "alaDrcTmOspf3Debug": alaDrcTmOspf3Debug,
       "alaDrcTmOspf3DebugError": alaDrcTmOspf3DebugError,
       "alaDrcTmOspf3DebugInfo": alaDrcTmOspf3DebugInfo,
       "alaDrcTmOspf3DebugIntf": alaDrcTmOspf3DebugIntf,
       "alaDrcTmOspf3DebugRecv": alaDrcTmOspf3DebugRecv,
       "alaDrcTmOspf3DebugSend": alaDrcTmOspf3DebugSend,
       "alaDrcTmOspf3DebugNbr": alaDrcTmOspf3DebugNbr,
       "alaDrcTmOspf3DebugState": alaDrcTmOspf3DebugState,
       "alaDrcTmOspf3DebugArea": alaDrcTmOspf3DebugArea,
       "alaDrcTmOspf3DebugLsa": alaDrcTmOspf3DebugLsa,
       "alaDrcTmOspf3DebugFlood": alaDrcTmOspf3DebugFlood,
       "alaDrcTmOspf3DebugSpf": alaDrcTmOspf3DebugSpf,
       "alaDrcTmOspf3DebugRdb": alaDrcTmOspf3DebugRdb,
       "alaDrcTmOspf3DebugVlink": alaDrcTmOspf3DebugVlink,
       "alaDrcTmOspf3DebugMip": alaDrcTmOspf3DebugMip,
       "alaDrcTmOspf3DebugAll": alaDrcTmOspf3DebugAll,
       "alaDrcTmLogDestination": alaDrcTmLogDestination,
       "alaDrcTmLogToSysFacility": alaDrcTmLogToSysFacility,
       "alaDrcTmLogToSessionId": alaDrcTmLogToSessionId,
       "alaDrcTmLogBufferSize": alaDrcTmLogBufferSize,
       "alaDrcTmLogBufferDumpfile": alaDrcTmLogBufferDumpfile,
       "alaDrcTmLogCriticalBufferDumpfile": alaDrcTmLogCriticalBufferDumpfile,
       "alaDrcTmLogShowTask": alaDrcTmLogShowTask,
       "alaDrcTmLogShowFunction": alaDrcTmLogShowFunction,
       "alaDrcTmLogShowLine": alaDrcTmLogShowLine,
       "alaDrcTmLogShowDate": alaDrcTmLogShowDate,
       "alaDrcTmLogShowTime": alaDrcTmLogShowTime,
       "alaDrcTmLogClearBuffer": alaDrcTmLogClearBuffer,
       "alaDrcTmIsisDebug": alaDrcTmIsisDebug,
       "alaDrcTmIsisDebugError": alaDrcTmIsisDebugError,
       "alaDrcTmIsisDebugWarn": alaDrcTmIsisDebugWarn,
       "alaDrcTmIsisDebugPkt": alaDrcTmIsisDebugPkt,
       "alaDrcTmIsisDebugAdj": alaDrcTmIsisDebugAdj,
       "alaDrcTmIsisDebugCkt": alaDrcTmIsisDebugCkt,
       "alaDrcTmIsisDebugSpf": alaDrcTmIsisDebugSpf,
       "alaDrcTmIsisDebugLsp": alaDrcTmIsisDebugLsp,
       "alaDrcTmIsisDebugFlood": alaDrcTmIsisDebugFlood,
       "alaDrcTmIsisDebugIntf": alaDrcTmIsisDebugIntf,
       "alaDrcTmIsisDebugIprm": alaDrcTmIsisDebugIprm,
       "alaDrcTmIsisDebugMip": alaDrcTmIsisDebugMip,
       "alaDrcTmIsisDebugMsg": alaDrcTmIsisDebugMsg,
       "alaDrcTmIsisDebugLeak": alaDrcTmIsisDebugLeak,
       "alaDrcTmIsisDebugSummary": alaDrcTmIsisDebugSummary,
       "alaDrcTmIsisDebugRestart": alaDrcTmIsisDebugRestart,
       "alaDrcTmIsisDebugAll": alaDrcTmIsisDebugAll,
       "alcatelIND1DrcTmMIBConformance": alcatelIND1DrcTmMIBConformance,
       "alcatelIND1DrcTmMIBCompliances": alcatelIND1DrcTmMIBCompliances,
       "alaDrcTmCompliance": alaDrcTmCompliance,
       "alcatelIND1DrcTmMIBGroups": alcatelIND1DrcTmMIBGroups,
       "alaDrcTmConfigMIBGroup": alaDrcTmConfigMIBGroup,
       "alaDrcTmDebugMIBGroup": alaDrcTmDebugMIBGroup,
       "alaDrcTmRipDebugMIBGroup": alaDrcTmRipDebugMIBGroup,
       "alaDrcTmOspfDebugMIBGroup": alaDrcTmOspfDebugMIBGroup,
       "alaDrcTmBgpDebugMIBGroup": alaDrcTmBgpDebugMIBGroup,
       "alaDrcTmDvmrpDebugMIBGroup": alaDrcTmDvmrpDebugMIBGroup,
       "alaDrcTmPimDebugMIBGroup": alaDrcTmPimDebugMIBGroup,
       "alaDrcTmRipngDebugMIBGroup": alaDrcTmRipngDebugMIBGroup,
       "alaDrcTmIprmDebugMIBGroup": alaDrcTmIprmDebugMIBGroup,
       "alaDrcTmIpmrmDebugMIBGroup": alaDrcTmIpmrmDebugMIBGroup,
       "alaDrcTmOspf3DebugMIBGroup": alaDrcTmOspf3DebugMIBGroup,
       "alaDrcTmLogDestinationMIBGroup": alaDrcTmLogDestinationMIBGroup,
       "alaDrcTmIsisDebugMIBGroup": alaDrcTmIsisDebugMIBGroup}
)
