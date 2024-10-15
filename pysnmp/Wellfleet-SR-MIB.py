# SNMP MIB module (Wellfleet-SR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:07 2024
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

(wfBridgeGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBridgeGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBrSourceRouting_ObjectIdentity = ObjectIdentity
wfBrSourceRouting = _WfBrSourceRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2)
)
_WfBrSr_ObjectIdentity = ObjectIdentity
wfBrSr = _WfBrSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1)
)


class _WfBrSrBaseDelete_Type(Integer32):
    """Custom type wfBrSrBaseDelete based on Integer32"""
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


_WfBrSrBaseDelete_Type.__name__ = "Integer32"
_WfBrSrBaseDelete_Object = MibScalar
wfBrSrBaseDelete = _WfBrSrBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 1),
    _WfBrSrBaseDelete_Type()
)
wfBrSrBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseDelete.setStatus("mandatory")


class _WfBrSrBaseDisable_Type(Integer32):
    """Custom type wfBrSrBaseDisable based on Integer32"""
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


_WfBrSrBaseDisable_Type.__name__ = "Integer32"
_WfBrSrBaseDisable_Object = MibScalar
wfBrSrBaseDisable = _WfBrSrBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 2),
    _WfBrSrBaseDisable_Type()
)
wfBrSrBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseDisable.setStatus("mandatory")


class _WfBrSrBaseState_Type(Integer32):
    """Custom type wfBrSrBaseState based on Integer32"""
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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfBrSrBaseState_Type.__name__ = "Integer32"
_WfBrSrBaseState_Object = MibScalar
wfBrSrBaseState = _WfBrSrBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 3),
    _WfBrSrBaseState_Type()
)
wfBrSrBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseState.setStatus("mandatory")
_WfBrSrBaseInternalLanId_Type = Integer32
_WfBrSrBaseInternalLanId_Object = MibScalar
wfBrSrBaseInternalLanId = _WfBrSrBaseInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 4),
    _WfBrSrBaseInternalLanId_Type()
)
wfBrSrBaseInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseInternalLanId.setStatus("mandatory")
_WfBrSrBaseBridgeId_Type = Integer32
_WfBrSrBaseBridgeId_Object = MibScalar
wfBrSrBaseBridgeId = _WfBrSrBaseBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 5),
    _WfBrSrBaseBridgeId_Type()
)
wfBrSrBaseBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseBridgeId.setStatus("mandatory")


class _WfBrSrBaseGroupLanId_Type(Integer32):
    """Custom type wfBrSrBaseGroupLanId based on Integer32"""
    defaultValue = 4095


_WfBrSrBaseGroupLanId_Object = MibScalar
wfBrSrBaseGroupLanId = _WfBrSrBaseGroupLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 6),
    _WfBrSrBaseGroupLanId_Type()
)
wfBrSrBaseGroupLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseGroupLanId.setStatus("mandatory")


class _WfBrSrBaseIpEncapsDisable_Type(Integer32):
    """Custom type wfBrSrBaseIpEncapsDisable based on Integer32"""
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


_WfBrSrBaseIpEncapsDisable_Type.__name__ = "Integer32"
_WfBrSrBaseIpEncapsDisable_Object = MibScalar
wfBrSrBaseIpEncapsDisable = _WfBrSrBaseIpEncapsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 7),
    _WfBrSrBaseIpEncapsDisable_Type()
)
wfBrSrBaseIpEncapsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseIpEncapsDisable.setStatus("mandatory")
_WfBrSrBaseIpNetworkRingId_Type = Integer32
_WfBrSrBaseIpNetworkRingId_Object = MibScalar
wfBrSrBaseIpNetworkRingId = _WfBrSrBaseIpNetworkRingId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 8),
    _WfBrSrBaseIpNetworkRingId_Type()
)
wfBrSrBaseIpNetworkRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseIpNetworkRingId.setStatus("mandatory")
_WfBrSrBaseIpInReceives_Type = Counter32
_WfBrSrBaseIpInReceives_Object = MibScalar
wfBrSrBaseIpInReceives = _WfBrSrBaseIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 9),
    _WfBrSrBaseIpInReceives_Type()
)
wfBrSrBaseIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseIpInReceives.setStatus("mandatory")
_WfBrSrBaseIpSeqErrors_Type = Counter32
_WfBrSrBaseIpSeqErrors_Object = MibScalar
wfBrSrBaseIpSeqErrors = _WfBrSrBaseIpSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 10),
    _WfBrSrBaseIpSeqErrors_Type()
)
wfBrSrBaseIpSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseIpSeqErrors.setStatus("mandatory")


class _WfBrSrBaseIpMtuSize_Type(Integer32):
    """Custom type wfBrSrBaseIpMtuSize based on Integer32"""
    defaultValue = 4562


_WfBrSrBaseIpMtuSize_Object = MibScalar
wfBrSrBaseIpMtuSize = _WfBrSrBaseIpMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 11),
    _WfBrSrBaseIpMtuSize_Type()
)
wfBrSrBaseIpMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseIpMtuSize.setStatus("mandatory")


class _WfBrSrBaseNbServerRifCacheDisable_Type(Integer32):
    """Custom type wfBrSrBaseNbServerRifCacheDisable based on Integer32"""
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


_WfBrSrBaseNbServerRifCacheDisable_Type.__name__ = "Integer32"
_WfBrSrBaseNbServerRifCacheDisable_Object = MibScalar
wfBrSrBaseNbServerRifCacheDisable = _WfBrSrBaseNbServerRifCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 12),
    _WfBrSrBaseNbServerRifCacheDisable_Type()
)
wfBrSrBaseNbServerRifCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbServerRifCacheDisable.setStatus("mandatory")


class _WfBrSrBaseNbClientRifCacheDisable_Type(Integer32):
    """Custom type wfBrSrBaseNbClientRifCacheDisable based on Integer32"""
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


_WfBrSrBaseNbClientRifCacheDisable_Type.__name__ = "Integer32"
_WfBrSrBaseNbClientRifCacheDisable_Object = MibScalar
wfBrSrBaseNbClientRifCacheDisable = _WfBrSrBaseNbClientRifCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 13),
    _WfBrSrBaseNbClientRifCacheDisable_Type()
)
wfBrSrBaseNbClientRifCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbClientRifCacheDisable.setStatus("mandatory")


class _WfBrSrBaseNbDatagramRifCacheDisable_Type(Integer32):
    """Custom type wfBrSrBaseNbDatagramRifCacheDisable based on Integer32"""
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


_WfBrSrBaseNbDatagramRifCacheDisable_Type.__name__ = "Integer32"
_WfBrSrBaseNbDatagramRifCacheDisable_Object = MibScalar
wfBrSrBaseNbDatagramRifCacheDisable = _WfBrSrBaseNbDatagramRifCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 14),
    _WfBrSrBaseNbDatagramRifCacheDisable_Type()
)
wfBrSrBaseNbDatagramRifCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbDatagramRifCacheDisable.setStatus("mandatory")


class _WfBrSrBaseNb15CharacterDisable_Type(Integer32):
    """Custom type wfBrSrBaseNb15CharacterDisable based on Integer32"""
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


_WfBrSrBaseNb15CharacterDisable_Type.__name__ = "Integer32"
_WfBrSrBaseNb15CharacterDisable_Object = MibScalar
wfBrSrBaseNb15CharacterDisable = _WfBrSrBaseNb15CharacterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 15),
    _WfBrSrBaseNb15CharacterDisable_Type()
)
wfBrSrBaseNb15CharacterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNb15CharacterDisable.setStatus("mandatory")


class _WfBrSrBaseNbRifMibDisable_Type(Integer32):
    """Custom type wfBrSrBaseNbRifMibDisable based on Integer32"""
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


_WfBrSrBaseNbRifMibDisable_Type.__name__ = "Integer32"
_WfBrSrBaseNbRifMibDisable_Object = MibScalar
wfBrSrBaseNbRifMibDisable = _WfBrSrBaseNbRifMibDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 16),
    _WfBrSrBaseNbRifMibDisable_Type()
)
wfBrSrBaseNbRifMibDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbRifMibDisable.setStatus("mandatory")


class _WfBrSrBaseNbMaximumRifEntries_Type(Integer32):
    """Custom type wfBrSrBaseNbMaximumRifEntries based on Integer32"""
    defaultValue = 100


_WfBrSrBaseNbMaximumRifEntries_Object = MibScalar
wfBrSrBaseNbMaximumRifEntries = _WfBrSrBaseNbMaximumRifEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 17),
    _WfBrSrBaseNbMaximumRifEntries_Type()
)
wfBrSrBaseNbMaximumRifEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbMaximumRifEntries.setStatus("mandatory")
_WfBrSrBaseNbCurrentRifEntries_Type = Integer32
_WfBrSrBaseNbCurrentRifEntries_Object = MibScalar
wfBrSrBaseNbCurrentRifEntries = _WfBrSrBaseNbCurrentRifEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 18),
    _WfBrSrBaseNbCurrentRifEntries_Type()
)
wfBrSrBaseNbCurrentRifEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseNbCurrentRifEntries.setStatus("mandatory")


class _WfBrSrBaseNbRifAgeTime_Type(Integer32):
    """Custom type wfBrSrBaseNbRifAgeTime based on Integer32"""
    defaultValue = 300


_WfBrSrBaseNbRifAgeTime_Object = MibScalar
wfBrSrBaseNbRifAgeTime = _WfBrSrBaseNbRifAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 19),
    _WfBrSrBaseNbRifAgeTime_Type()
)
wfBrSrBaseNbRifAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbRifAgeTime.setStatus("mandatory")


class _WfBrSrBaseNbRifHashEntries_Type(Integer32):
    """Custom type wfBrSrBaseNbRifHashEntries based on Integer32"""
    defaultValue = 253

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(253, 2147483647),
    )


_WfBrSrBaseNbRifHashEntries_Type.__name__ = "Integer32"
_WfBrSrBaseNbRifHashEntries_Object = MibScalar
wfBrSrBaseNbRifHashEntries = _WfBrSrBaseNbRifHashEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 20),
    _WfBrSrBaseNbRifHashEntries_Type()
)
wfBrSrBaseNbRifHashEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbRifHashEntries.setStatus("mandatory")
_WfBrSrBaseNbRifCacheHits_Type = Counter32
_WfBrSrBaseNbRifCacheHits_Object = MibScalar
wfBrSrBaseNbRifCacheHits = _WfBrSrBaseNbRifCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 21),
    _WfBrSrBaseNbRifCacheHits_Type()
)
wfBrSrBaseNbRifCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseNbRifCacheHits.setStatus("mandatory")
_WfBrSrBaseNbRifCacheMisses_Type = Counter32
_WfBrSrBaseNbRifCacheMisses_Object = MibScalar
wfBrSrBaseNbRifCacheMisses = _WfBrSrBaseNbRifCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 22),
    _WfBrSrBaseNbRifCacheMisses_Type()
)
wfBrSrBaseNbRifCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseNbRifCacheMisses.setStatus("mandatory")
_WfBrSrBaseNbRifDroppedFrames_Type = Counter32
_WfBrSrBaseNbRifDroppedFrames_Object = MibScalar
wfBrSrBaseNbRifDroppedFrames = _WfBrSrBaseNbRifDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 23),
    _WfBrSrBaseNbRifDroppedFrames_Type()
)
wfBrSrBaseNbRifDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseNbRifDroppedFrames.setStatus("mandatory")


class _WfBrSrBaseNbQueryCacheDisable_Type(Integer32):
    """Custom type wfBrSrBaseNbQueryCacheDisable based on Integer32"""
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


_WfBrSrBaseNbQueryCacheDisable_Type.__name__ = "Integer32"
_WfBrSrBaseNbQueryCacheDisable_Object = MibScalar
wfBrSrBaseNbQueryCacheDisable = _WfBrSrBaseNbQueryCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 24),
    _WfBrSrBaseNbQueryCacheDisable_Type()
)
wfBrSrBaseNbQueryCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbQueryCacheDisable.setStatus("mandatory")


class _WfBrSrBaseNbQueryMibDisable_Type(Integer32):
    """Custom type wfBrSrBaseNbQueryMibDisable based on Integer32"""
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


_WfBrSrBaseNbQueryMibDisable_Type.__name__ = "Integer32"
_WfBrSrBaseNbQueryMibDisable_Object = MibScalar
wfBrSrBaseNbQueryMibDisable = _WfBrSrBaseNbQueryMibDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 25),
    _WfBrSrBaseNbQueryMibDisable_Type()
)
wfBrSrBaseNbQueryMibDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbQueryMibDisable.setStatus("mandatory")


class _WfBrSrBaseNbMaximumQueryEntries_Type(Integer32):
    """Custom type wfBrSrBaseNbMaximumQueryEntries based on Integer32"""
    defaultValue = 100


_WfBrSrBaseNbMaximumQueryEntries_Object = MibScalar
wfBrSrBaseNbMaximumQueryEntries = _WfBrSrBaseNbMaximumQueryEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 26),
    _WfBrSrBaseNbMaximumQueryEntries_Type()
)
wfBrSrBaseNbMaximumQueryEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbMaximumQueryEntries.setStatus("mandatory")
_WfBrSrBaseNbCurrentQueryEntries_Type = Integer32
_WfBrSrBaseNbCurrentQueryEntries_Object = MibScalar
wfBrSrBaseNbCurrentQueryEntries = _WfBrSrBaseNbCurrentQueryEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 27),
    _WfBrSrBaseNbCurrentQueryEntries_Type()
)
wfBrSrBaseNbCurrentQueryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseNbCurrentQueryEntries.setStatus("mandatory")


class _WfBrSrBaseNbQueryAgeTime_Type(Integer32):
    """Custom type wfBrSrBaseNbQueryAgeTime based on Integer32"""
    defaultValue = 15


_WfBrSrBaseNbQueryAgeTime_Object = MibScalar
wfBrSrBaseNbQueryAgeTime = _WfBrSrBaseNbQueryAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 28),
    _WfBrSrBaseNbQueryAgeTime_Type()
)
wfBrSrBaseNbQueryAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbQueryAgeTime.setStatus("mandatory")
_WfBrSrBaseNbQueryFilteredFrames_Type = Counter32
_WfBrSrBaseNbQueryFilteredFrames_Object = MibScalar
wfBrSrBaseNbQueryFilteredFrames = _WfBrSrBaseNbQueryFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 29),
    _WfBrSrBaseNbQueryFilteredFrames_Type()
)
wfBrSrBaseNbQueryFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseNbQueryFilteredFrames.setStatus("mandatory")


class _WfBrSrBaseStpEnable_Type(Integer32):
    """Custom type wfBrSrBaseStpEnable based on Integer32"""
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


_WfBrSrBaseStpEnable_Type.__name__ = "Integer32"
_WfBrSrBaseStpEnable_Object = MibScalar
wfBrSrBaseStpEnable = _WfBrSrBaseStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 30),
    _WfBrSrBaseStpEnable_Type()
)
wfBrSrBaseStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseStpEnable.setStatus("mandatory")


class _WfBrSrBaseStpState_Type(Integer32):
    """Custom type wfBrSrBaseStpState based on Integer32"""
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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfBrSrBaseStpState_Type.__name__ = "Integer32"
_WfBrSrBaseStpState_Object = MibScalar
wfBrSrBaseStpState = _WfBrSrBaseStpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 31),
    _WfBrSrBaseStpState_Type()
)
wfBrSrBaseStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpState.setStatus("mandatory")


class _WfBrSrBaseStpProtocolSpecification_Type(Integer32):
    """Custom type wfBrSrBaseStpProtocolSpecification based on Integer32"""
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
        *(("declb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_WfBrSrBaseStpProtocolSpecification_Type.__name__ = "Integer32"
_WfBrSrBaseStpProtocolSpecification_Object = MibScalar
wfBrSrBaseStpProtocolSpecification = _WfBrSrBaseStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 32),
    _WfBrSrBaseStpProtocolSpecification_Type()
)
wfBrSrBaseStpProtocolSpecification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseStpProtocolSpecification.setStatus("mandatory")
_WfBrSrBaseStpBridgeID_Type = OctetString
_WfBrSrBaseStpBridgeID_Object = MibScalar
wfBrSrBaseStpBridgeID = _WfBrSrBaseStpBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 33),
    _WfBrSrBaseStpBridgeID_Type()
)
wfBrSrBaseStpBridgeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseStpBridgeID.setStatus("mandatory")
_WfBrSrBaseStpTimeSinceTopologyChange_Type = Counter32
_WfBrSrBaseStpTimeSinceTopologyChange_Object = MibScalar
wfBrSrBaseStpTimeSinceTopologyChange = _WfBrSrBaseStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 34),
    _WfBrSrBaseStpTimeSinceTopologyChange_Type()
)
wfBrSrBaseStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpTimeSinceTopologyChange.setStatus("mandatory")
_WfBrSrBaseStpTopChanges_Type = Counter32
_WfBrSrBaseStpTopChanges_Object = MibScalar
wfBrSrBaseStpTopChanges = _WfBrSrBaseStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 35),
    _WfBrSrBaseStpTopChanges_Type()
)
wfBrSrBaseStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpTopChanges.setStatus("mandatory")
_WfBrSrBaseStpDesignatedRoot_Type = OctetString
_WfBrSrBaseStpDesignatedRoot_Object = MibScalar
wfBrSrBaseStpDesignatedRoot = _WfBrSrBaseStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 36),
    _WfBrSrBaseStpDesignatedRoot_Type()
)
wfBrSrBaseStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpDesignatedRoot.setStatus("mandatory")
_WfBrSrBaseStpRootCost_Type = Integer32
_WfBrSrBaseStpRootCost_Object = MibScalar
wfBrSrBaseStpRootCost = _WfBrSrBaseStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 37),
    _WfBrSrBaseStpRootCost_Type()
)
wfBrSrBaseStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpRootCost.setStatus("mandatory")
_WfBrSrBaseStpRootPort_Type = Integer32
_WfBrSrBaseStpRootPort_Object = MibScalar
wfBrSrBaseStpRootPort = _WfBrSrBaseStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 38),
    _WfBrSrBaseStpRootPort_Type()
)
wfBrSrBaseStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpRootPort.setStatus("mandatory")
_WfBrSrBaseStpMaxAge_Type = Integer32
_WfBrSrBaseStpMaxAge_Object = MibScalar
wfBrSrBaseStpMaxAge = _WfBrSrBaseStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 39),
    _WfBrSrBaseStpMaxAge_Type()
)
wfBrSrBaseStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpMaxAge.setStatus("mandatory")
_WfBrSrBaseStpHelloTime_Type = Integer32
_WfBrSrBaseStpHelloTime_Object = MibScalar
wfBrSrBaseStpHelloTime = _WfBrSrBaseStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 40),
    _WfBrSrBaseStpHelloTime_Type()
)
wfBrSrBaseStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpHelloTime.setStatus("mandatory")


class _WfBrSrBaseStpHoldTime_Type(Integer32):
    """Custom type wfBrSrBaseStpHoldTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("time", 100)
    )


_WfBrSrBaseStpHoldTime_Type.__name__ = "Integer32"
_WfBrSrBaseStpHoldTime_Object = MibScalar
wfBrSrBaseStpHoldTime = _WfBrSrBaseStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 41),
    _WfBrSrBaseStpHoldTime_Type()
)
wfBrSrBaseStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpHoldTime.setStatus("mandatory")
_WfBrSrBaseStpForwardDelay_Type = Integer32
_WfBrSrBaseStpForwardDelay_Object = MibScalar
wfBrSrBaseStpForwardDelay = _WfBrSrBaseStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 42),
    _WfBrSrBaseStpForwardDelay_Type()
)
wfBrSrBaseStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBaseStpForwardDelay.setStatus("mandatory")


class _WfBrSrBaseStpBridgeMaxAge_Type(Integer32):
    """Custom type wfBrSrBaseStpBridgeMaxAge based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_WfBrSrBaseStpBridgeMaxAge_Type.__name__ = "Integer32"
_WfBrSrBaseStpBridgeMaxAge_Object = MibScalar
wfBrSrBaseStpBridgeMaxAge = _WfBrSrBaseStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 43),
    _WfBrSrBaseStpBridgeMaxAge_Type()
)
wfBrSrBaseStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseStpBridgeMaxAge.setStatus("mandatory")


class _WfBrSrBaseStpBridgeHelloTime_Type(Integer32):
    """Custom type wfBrSrBaseStpBridgeHelloTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_WfBrSrBaseStpBridgeHelloTime_Type.__name__ = "Integer32"
_WfBrSrBaseStpBridgeHelloTime_Object = MibScalar
wfBrSrBaseStpBridgeHelloTime = _WfBrSrBaseStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 44),
    _WfBrSrBaseStpBridgeHelloTime_Type()
)
wfBrSrBaseStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseStpBridgeHelloTime.setStatus("mandatory")


class _WfBrSrBaseStpBridgeForwardDelay_Type(Integer32):
    """Custom type wfBrSrBaseStpBridgeForwardDelay based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_WfBrSrBaseStpBridgeForwardDelay_Type.__name__ = "Integer32"
_WfBrSrBaseStpBridgeForwardDelay_Object = MibScalar
wfBrSrBaseStpBridgeForwardDelay = _WfBrSrBaseStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 45),
    _WfBrSrBaseStpBridgeForwardDelay_Type()
)
wfBrSrBaseStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseStpBridgeForwardDelay.setStatus("mandatory")


class _WfBrSrBaseNbNameQueryCacheDisable_Type(Integer32):
    """Custom type wfBrSrBaseNbNameQueryCacheDisable based on Integer32"""
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


_WfBrSrBaseNbNameQueryCacheDisable_Type.__name__ = "Integer32"
_WfBrSrBaseNbNameQueryCacheDisable_Object = MibScalar
wfBrSrBaseNbNameQueryCacheDisable = _WfBrSrBaseNbNameQueryCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 46),
    _WfBrSrBaseNbNameQueryCacheDisable_Type()
)
wfBrSrBaseNbNameQueryCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseNbNameQueryCacheDisable.setStatus("mandatory")


class _WfBrSrBaseAreHopCntLimit_Type(Integer32):
    """Custom type wfBrSrBaseAreHopCntLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("areonly", 1),
          ("areste", 2))
    )


_WfBrSrBaseAreHopCntLimit_Type.__name__ = "Integer32"
_WfBrSrBaseAreHopCntLimit_Object = MibScalar
wfBrSrBaseAreHopCntLimit = _WfBrSrBaseAreHopCntLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 1, 47),
    _WfBrSrBaseAreHopCntLimit_Type()
)
wfBrSrBaseAreHopCntLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBaseAreHopCntLimit.setStatus("mandatory")
_WfBrSrInterfaceTable_Object = MibTable
wfBrSrInterfaceTable = _WfBrSrInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wfBrSrInterfaceTable.setStatus("mandatory")
_WfBrSrInterfaceEntry_Object = MibTableRow
wfBrSrInterfaceEntry = _WfBrSrInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1)
)
wfBrSrInterfaceEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfBrSrInterfaceEntry.setStatus("mandatory")


class _WfBrSrInterfaceDelete_Type(Integer32):
    """Custom type wfBrSrInterfaceDelete based on Integer32"""
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


_WfBrSrInterfaceDelete_Type.__name__ = "Integer32"
_WfBrSrInterfaceDelete_Object = MibTableColumn
wfBrSrInterfaceDelete = _WfBrSrInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 1),
    _WfBrSrInterfaceDelete_Type()
)
wfBrSrInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDelete.setStatus("mandatory")


class _WfBrSrInterfaceDisable_Type(Integer32):
    """Custom type wfBrSrInterfaceDisable based on Integer32"""
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


_WfBrSrInterfaceDisable_Type.__name__ = "Integer32"
_WfBrSrInterfaceDisable_Object = MibTableColumn
wfBrSrInterfaceDisable = _WfBrSrInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 2),
    _WfBrSrInterfaceDisable_Type()
)
wfBrSrInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDisable.setStatus("mandatory")


class _WfBrSrInterfaceState_Type(Integer32):
    """Custom type wfBrSrInterfaceState based on Integer32"""
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
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfBrSrInterfaceState_Type.__name__ = "Integer32"
_WfBrSrInterfaceState_Object = MibTableColumn
wfBrSrInterfaceState = _WfBrSrInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 3),
    _WfBrSrInterfaceState_Type()
)
wfBrSrInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceState.setStatus("mandatory")
_WfBrSrInterfaceCircuit_Type = Integer32
_WfBrSrInterfaceCircuit_Object = MibTableColumn
wfBrSrInterfaceCircuit = _WfBrSrInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 4),
    _WfBrSrInterfaceCircuit_Type()
)
wfBrSrInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceCircuit.setStatus("mandatory")


class _WfBrSrInterfaceMaxRds_Type(Integer32):
    """Custom type wfBrSrInterfaceMaxRds based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_WfBrSrInterfaceMaxRds_Type.__name__ = "Integer32"
_WfBrSrInterfaceMaxRds_Object = MibTableColumn
wfBrSrInterfaceMaxRds = _WfBrSrInterfaceMaxRds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 5),
    _WfBrSrInterfaceMaxRds_Type()
)
wfBrSrInterfaceMaxRds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceMaxRds.setStatus("mandatory")
_WfBrSrInterfaceRing_Type = Integer32
_WfBrSrInterfaceRing_Object = MibTableColumn
wfBrSrInterfaceRing = _WfBrSrInterfaceRing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 6),
    _WfBrSrInterfaceRing_Type()
)
wfBrSrInterfaceRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceRing.setStatus("mandatory")


class _WfBrSrInterfaceBlockOutSte_Type(Integer32):
    """Custom type wfBrSrInterfaceBlockOutSte based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("block", 1))
    )


_WfBrSrInterfaceBlockOutSte_Type.__name__ = "Integer32"
_WfBrSrInterfaceBlockOutSte_Object = MibTableColumn
wfBrSrInterfaceBlockOutSte = _WfBrSrInterfaceBlockOutSte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 7),
    _WfBrSrInterfaceBlockOutSte_Type()
)
wfBrSrInterfaceBlockOutSte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceBlockOutSte.setStatus("mandatory")


class _WfBrSrInterfaceBlockInSte_Type(Integer32):
    """Custom type wfBrSrInterfaceBlockInSte based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("block", 1))
    )


_WfBrSrInterfaceBlockInSte_Type.__name__ = "Integer32"
_WfBrSrInterfaceBlockInSte_Object = MibTableColumn
wfBrSrInterfaceBlockInSte = _WfBrSrInterfaceBlockInSte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 8),
    _WfBrSrInterfaceBlockInSte_Type()
)
wfBrSrInterfaceBlockInSte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceBlockInSte.setStatus("mandatory")


class _WfBrSrInterfaceBlockIp_Type(Integer32):
    """Custom type wfBrSrInterfaceBlockIp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("block", 1))
    )


_WfBrSrInterfaceBlockIp_Type.__name__ = "Integer32"
_WfBrSrInterfaceBlockIp_Object = MibTableColumn
wfBrSrInterfaceBlockIp = _WfBrSrInterfaceBlockIp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 9),
    _WfBrSrInterfaceBlockIp_Type()
)
wfBrSrInterfaceBlockIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceBlockIp.setStatus("mandatory")
_WfBrSrInterfaceIpAddress_Type = IpAddress
_WfBrSrInterfaceIpAddress_Object = MibTableColumn
wfBrSrInterfaceIpAddress = _WfBrSrInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 10),
    _WfBrSrInterfaceIpAddress_Type()
)
wfBrSrInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceIpAddress.setStatus("mandatory")
_WfBrSrInterfaceInFrames_Type = Counter32
_WfBrSrInterfaceInFrames_Object = MibTableColumn
wfBrSrInterfaceInFrames = _WfBrSrInterfaceInFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 11),
    _WfBrSrInterfaceInFrames_Type()
)
wfBrSrInterfaceInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceInFrames.setStatus("mandatory")
_WfBrSrInterfaceOutFrames_Type = Counter32
_WfBrSrInterfaceOutFrames_Object = MibTableColumn
wfBrSrInterfaceOutFrames = _WfBrSrInterfaceOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 12),
    _WfBrSrInterfaceOutFrames_Type()
)
wfBrSrInterfaceOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceOutFrames.setStatus("mandatory")
_WfBrSrInterfaceOutIpFrames_Type = Counter32
_WfBrSrInterfaceOutIpFrames_Object = MibTableColumn
wfBrSrInterfaceOutIpFrames = _WfBrSrInterfaceOutIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 13),
    _WfBrSrInterfaceOutIpFrames_Type()
)
wfBrSrInterfaceOutIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceOutIpFrames.setStatus("mandatory")
_WfBrSrInterfaceDropInvalidRcs_Type = Counter32
_WfBrSrInterfaceDropInvalidRcs_Object = MibTableColumn
wfBrSrInterfaceDropInvalidRcs = _WfBrSrInterfaceDropInvalidRcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 14),
    _WfBrSrInterfaceDropInvalidRcs_Type()
)
wfBrSrInterfaceDropInvalidRcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDropInvalidRcs.setStatus("mandatory")
_WfBrSrInterfaceDropInvalidRings_Type = Counter32
_WfBrSrInterfaceDropInvalidRings_Object = MibTableColumn
wfBrSrInterfaceDropInvalidRings = _WfBrSrInterfaceDropInvalidRings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 15),
    _WfBrSrInterfaceDropInvalidRings_Type()
)
wfBrSrInterfaceDropInvalidRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDropInvalidRings.setStatus("mandatory")
_WfBrSrInterfaceDropSrfs_Type = Counter32
_WfBrSrInterfaceDropSrfs_Object = MibTableColumn
wfBrSrInterfaceDropSrfs = _WfBrSrInterfaceDropSrfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 16),
    _WfBrSrInterfaceDropSrfs_Type()
)
wfBrSrInterfaceDropSrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceDropSrfs.setStatus("mandatory")


class _WfBrSrInterfaceNbServerRifCacheDisable_Type(Integer32):
    """Custom type wfBrSrInterfaceNbServerRifCacheDisable based on Integer32"""
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


_WfBrSrInterfaceNbServerRifCacheDisable_Type.__name__ = "Integer32"
_WfBrSrInterfaceNbServerRifCacheDisable_Object = MibTableColumn
wfBrSrInterfaceNbServerRifCacheDisable = _WfBrSrInterfaceNbServerRifCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 17),
    _WfBrSrInterfaceNbServerRifCacheDisable_Type()
)
wfBrSrInterfaceNbServerRifCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceNbServerRifCacheDisable.setStatus("mandatory")


class _WfBrSrInterfaceNbClientRifCacheDisable_Type(Integer32):
    """Custom type wfBrSrInterfaceNbClientRifCacheDisable based on Integer32"""
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


_WfBrSrInterfaceNbClientRifCacheDisable_Type.__name__ = "Integer32"
_WfBrSrInterfaceNbClientRifCacheDisable_Object = MibTableColumn
wfBrSrInterfaceNbClientRifCacheDisable = _WfBrSrInterfaceNbClientRifCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 18),
    _WfBrSrInterfaceNbClientRifCacheDisable_Type()
)
wfBrSrInterfaceNbClientRifCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceNbClientRifCacheDisable.setStatus("mandatory")


class _WfBrSrInterfaceNbDatagramRifCacheDisable_Type(Integer32):
    """Custom type wfBrSrInterfaceNbDatagramRifCacheDisable based on Integer32"""
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


_WfBrSrInterfaceNbDatagramRifCacheDisable_Type.__name__ = "Integer32"
_WfBrSrInterfaceNbDatagramRifCacheDisable_Object = MibTableColumn
wfBrSrInterfaceNbDatagramRifCacheDisable = _WfBrSrInterfaceNbDatagramRifCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 19),
    _WfBrSrInterfaceNbDatagramRifCacheDisable_Type()
)
wfBrSrInterfaceNbDatagramRifCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceNbDatagramRifCacheDisable.setStatus("mandatory")


class _WfBrSrInterfaceNbQueryCacheDisable_Type(Integer32):
    """Custom type wfBrSrInterfaceNbQueryCacheDisable based on Integer32"""
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


_WfBrSrInterfaceNbQueryCacheDisable_Type.__name__ = "Integer32"
_WfBrSrInterfaceNbQueryCacheDisable_Object = MibTableColumn
wfBrSrInterfaceNbQueryCacheDisable = _WfBrSrInterfaceNbQueryCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 20),
    _WfBrSrInterfaceNbQueryCacheDisable_Type()
)
wfBrSrInterfaceNbQueryCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceNbQueryCacheDisable.setStatus("mandatory")
_WfBrSrInterfaceXbInFrames_Type = Counter32
_WfBrSrInterfaceXbInFrames_Object = MibTableColumn
wfBrSrInterfaceXbInFrames = _WfBrSrInterfaceXbInFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 21),
    _WfBrSrInterfaceXbInFrames_Type()
)
wfBrSrInterfaceXbInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceXbInFrames.setStatus("mandatory")
_WfBrSrInterfaceXbDropFrames_Type = Counter32
_WfBrSrInterfaceXbDropFrames_Object = MibTableColumn
wfBrSrInterfaceXbDropFrames = _WfBrSrInterfaceXbDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 22),
    _WfBrSrInterfaceXbDropFrames_Type()
)
wfBrSrInterfaceXbDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceXbDropFrames.setStatus("mandatory")


class _WfBrSrInterfaceFrBcastDlci_Type(Integer32):
    """Custom type wfBrSrInterfaceFrBcastDlci based on Integer32"""
    defaultValue = 2147483647


_WfBrSrInterfaceFrBcastDlci_Object = MibTableColumn
wfBrSrInterfaceFrBcastDlci = _WfBrSrInterfaceFrBcastDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 23),
    _WfBrSrInterfaceFrBcastDlci_Type()
)
wfBrSrInterfaceFrBcastDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceFrBcastDlci.setStatus("mandatory")


class _WfBrSrInterfaceEncapsFormat_Type(Integer32):
    """Custom type wfBrSrInterfaceEncapsFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proprietary", 1),
          ("standard", 2))
    )


_WfBrSrInterfaceEncapsFormat_Type.__name__ = "Integer32"
_WfBrSrInterfaceEncapsFormat_Object = MibTableColumn
wfBrSrInterfaceEncapsFormat = _WfBrSrInterfaceEncapsFormat_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 24),
    _WfBrSrInterfaceEncapsFormat_Type()
)
wfBrSrInterfaceEncapsFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceEncapsFormat.setStatus("mandatory")


class _WfBrSrInterfaceStpEnable_Type(Integer32):
    """Custom type wfBrSrInterfaceStpEnable based on Integer32"""
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


_WfBrSrInterfaceStpEnable_Type.__name__ = "Integer32"
_WfBrSrInterfaceStpEnable_Object = MibTableColumn
wfBrSrInterfaceStpEnable = _WfBrSrInterfaceStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 25),
    _WfBrSrInterfaceStpEnable_Type()
)
wfBrSrInterfaceStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpEnable.setStatus("mandatory")


class _WfBrSrInterfaceStpState_Type(Integer32):
    """Custom type wfBrSrInterfaceStpState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_WfBrSrInterfaceStpState_Type.__name__ = "Integer32"
_WfBrSrInterfaceStpState_Object = MibTableColumn
wfBrSrInterfaceStpState = _WfBrSrInterfaceStpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 26),
    _WfBrSrInterfaceStpState_Type()
)
wfBrSrInterfaceStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpState.setStatus("mandatory")
_WfBrSrInterfaceStpMultiCastAddr_Type = OctetString
_WfBrSrInterfaceStpMultiCastAddr_Object = MibTableColumn
wfBrSrInterfaceStpMultiCastAddr = _WfBrSrInterfaceStpMultiCastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 27),
    _WfBrSrInterfaceStpMultiCastAddr_Type()
)
wfBrSrInterfaceStpMultiCastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpMultiCastAddr.setStatus("mandatory")


class _WfBrSrInterfaceStpPathCost_Type(Integer32):
    """Custom type wfBrSrInterfaceStpPathCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfBrSrInterfaceStpPathCost_Type.__name__ = "Integer32"
_WfBrSrInterfaceStpPathCost_Object = MibTableColumn
wfBrSrInterfaceStpPathCost = _WfBrSrInterfaceStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 28),
    _WfBrSrInterfaceStpPathCost_Type()
)
wfBrSrInterfaceStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpPathCost.setStatus("mandatory")
_WfBrSrInterfaceStpDesignatedRoot_Type = OctetString
_WfBrSrInterfaceStpDesignatedRoot_Object = MibTableColumn
wfBrSrInterfaceStpDesignatedRoot = _WfBrSrInterfaceStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 29),
    _WfBrSrInterfaceStpDesignatedRoot_Type()
)
wfBrSrInterfaceStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpDesignatedRoot.setStatus("mandatory")
_WfBrSrInterfaceStpDesignatedCost_Type = Integer32
_WfBrSrInterfaceStpDesignatedCost_Object = MibTableColumn
wfBrSrInterfaceStpDesignatedCost = _WfBrSrInterfaceStpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 30),
    _WfBrSrInterfaceStpDesignatedCost_Type()
)
wfBrSrInterfaceStpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpDesignatedCost.setStatus("mandatory")
_WfBrSrInterfaceStpDesignatedBridge_Type = OctetString
_WfBrSrInterfaceStpDesignatedBridge_Object = MibTableColumn
wfBrSrInterfaceStpDesignatedBridge = _WfBrSrInterfaceStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 31),
    _WfBrSrInterfaceStpDesignatedBridge_Type()
)
wfBrSrInterfaceStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpDesignatedBridge.setStatus("mandatory")
_WfBrSrInterfaceStpDesignatedPort_Type = Integer32
_WfBrSrInterfaceStpDesignatedPort_Object = MibTableColumn
wfBrSrInterfaceStpDesignatedPort = _WfBrSrInterfaceStpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 32),
    _WfBrSrInterfaceStpDesignatedPort_Type()
)
wfBrSrInterfaceStpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpDesignatedPort.setStatus("mandatory")
_WfBrSrInterfaceStpForwardTransitions_Type = Counter32
_WfBrSrInterfaceStpForwardTransitions_Object = MibTableColumn
wfBrSrInterfaceStpForwardTransitions = _WfBrSrInterfaceStpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 33),
    _WfBrSrInterfaceStpForwardTransitions_Type()
)
wfBrSrInterfaceStpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpForwardTransitions.setStatus("mandatory")
_WfBrSrInterfaceStpPktsXmitd_Type = Counter32
_WfBrSrInterfaceStpPktsXmitd_Object = MibTableColumn
wfBrSrInterfaceStpPktsXmitd = _WfBrSrInterfaceStpPktsXmitd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 34),
    _WfBrSrInterfaceStpPktsXmitd_Type()
)
wfBrSrInterfaceStpPktsXmitd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpPktsXmitd.setStatus("mandatory")
_WfBrSrInterfaceStpPktsRcvd_Type = Counter32
_WfBrSrInterfaceStpPktsRcvd_Object = MibTableColumn
wfBrSrInterfaceStpPktsRcvd = _WfBrSrInterfaceStpPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 35),
    _WfBrSrInterfaceStpPktsRcvd_Type()
)
wfBrSrInterfaceStpPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpPktsRcvd.setStatus("mandatory")


class _WfBrSrInterfaceStpTranslationDisable_Type(Integer32):
    """Custom type wfBrSrInterfaceStpTranslationDisable based on Integer32"""
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


_WfBrSrInterfaceStpTranslationDisable_Type.__name__ = "Integer32"
_WfBrSrInterfaceStpTranslationDisable_Object = MibTableColumn
wfBrSrInterfaceStpTranslationDisable = _WfBrSrInterfaceStpTranslationDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 36),
    _WfBrSrInterfaceStpTranslationDisable_Type()
)
wfBrSrInterfaceStpTranslationDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceStpTranslationDisable.setStatus("mandatory")


class _WfBrSrInterfaceMaxLfField_Type(Integer32):
    """Custom type wfBrSrInterfaceMaxLfField based on Integer32"""
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
        *(("sr1500", 1),
          ("sr2052", 2),
          ("sr4472", 3))
    )


_WfBrSrInterfaceMaxLfField_Type.__name__ = "Integer32"
_WfBrSrInterfaceMaxLfField_Object = MibTableColumn
wfBrSrInterfaceMaxLfField = _WfBrSrInterfaceMaxLfField_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 37),
    _WfBrSrInterfaceMaxLfField_Type()
)
wfBrSrInterfaceMaxLfField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceMaxLfField.setStatus("mandatory")


class _WfBrSrInterfaceFilterAddress_Type(Integer32):
    """Custom type wfBrSrInterfaceFilterAddress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destinationaddress", 2),
          ("groupaddress", 1))
    )


_WfBrSrInterfaceFilterAddress_Type.__name__ = "Integer32"
_WfBrSrInterfaceFilterAddress_Object = MibTableColumn
wfBrSrInterfaceFilterAddress = _WfBrSrInterfaceFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 2, 1, 38),
    _WfBrSrInterfaceFilterAddress_Type()
)
wfBrSrInterfaceFilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrInterfaceFilterAddress.setStatus("mandatory")
_WfBrSrBridgeTable_Object = MibTable
wfBrSrBridgeTable = _WfBrSrBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wfBrSrBridgeTable.setStatus("mandatory")
_WfBrSrBridgeEntry_Object = MibTableRow
wfBrSrBridgeEntry = _WfBrSrBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 3, 1)
)
wfBrSrBridgeEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrBridgeId"),
)
if mibBuilder.loadTexts:
    wfBrSrBridgeEntry.setStatus("mandatory")


class _WfBrSrBridgeDelete_Type(Integer32):
    """Custom type wfBrSrBridgeDelete based on Integer32"""
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


_WfBrSrBridgeDelete_Type.__name__ = "Integer32"
_WfBrSrBridgeDelete_Object = MibTableColumn
wfBrSrBridgeDelete = _WfBrSrBridgeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 3, 1, 1),
    _WfBrSrBridgeDelete_Type()
)
wfBrSrBridgeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrBridgeDelete.setStatus("mandatory")
_WfBrSrBridgeId_Type = Integer32
_WfBrSrBridgeId_Object = MibTableColumn
wfBrSrBridgeId = _WfBrSrBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 3, 1, 2),
    _WfBrSrBridgeId_Type()
)
wfBrSrBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrBridgeId.setStatus("mandatory")
_WfBrSrIpExplorerTable_Object = MibTable
wfBrSrIpExplorerTable = _WfBrSrIpExplorerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wfBrSrIpExplorerTable.setStatus("mandatory")
_WfBrSrIpExplorerEntry_Object = MibTableRow
wfBrSrIpExplorerEntry = _WfBrSrIpExplorerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4, 1)
)
wfBrSrIpExplorerEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrIpExplorerAddr"),
)
if mibBuilder.loadTexts:
    wfBrSrIpExplorerEntry.setStatus("mandatory")


class _WfBrSrIpExplorerDelete_Type(Integer32):
    """Custom type wfBrSrIpExplorerDelete based on Integer32"""
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


_WfBrSrIpExplorerDelete_Type.__name__ = "Integer32"
_WfBrSrIpExplorerDelete_Object = MibTableColumn
wfBrSrIpExplorerDelete = _WfBrSrIpExplorerDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4, 1, 1),
    _WfBrSrIpExplorerDelete_Type()
)
wfBrSrIpExplorerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrIpExplorerDelete.setStatus("mandatory")
_WfBrSrIpExplorerAddr_Type = IpAddress
_WfBrSrIpExplorerAddr_Object = MibTableColumn
wfBrSrIpExplorerAddr = _WfBrSrIpExplorerAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4, 1, 2),
    _WfBrSrIpExplorerAddr_Type()
)
wfBrSrIpExplorerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpExplorerAddr.setStatus("mandatory")
_WfBrSrIpExplorerProtocol_Type = Integer32
_WfBrSrIpExplorerProtocol_Object = MibTableColumn
wfBrSrIpExplorerProtocol = _WfBrSrIpExplorerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 4, 1, 3),
    _WfBrSrIpExplorerProtocol_Type()
)
wfBrSrIpExplorerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrIpExplorerProtocol.setStatus("obsolete")
_WfBrSrIpEncapsTable_Object = MibTable
wfBrSrIpEncapsTable = _WfBrSrIpEncapsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wfBrSrIpEncapsTable.setStatus("obsolete")
_WfBrSrIpEncapsEntry_Object = MibTableRow
wfBrSrIpEncapsEntry = _WfBrSrIpEncapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5, 1)
)
wfBrSrIpEncapsEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrIpEncapsRing"),
)
if mibBuilder.loadTexts:
    wfBrSrIpEncapsEntry.setStatus("obsolete")
_WfBrSrIpEncapsRing_Type = Integer32
_WfBrSrIpEncapsRing_Object = MibTableColumn
wfBrSrIpEncapsRing = _WfBrSrIpEncapsRing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5, 1, 1),
    _WfBrSrIpEncapsRing_Type()
)
wfBrSrIpEncapsRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsRing.setStatus("obsolete")
_WfBrSrIpEncapsIpAddress_Type = IpAddress
_WfBrSrIpEncapsIpAddress_Object = MibTableColumn
wfBrSrIpEncapsIpAddress = _WfBrSrIpEncapsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5, 1, 2),
    _WfBrSrIpEncapsIpAddress_Type()
)
wfBrSrIpEncapsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsIpAddress.setStatus("obsolete")


class _WfBrSrIpEncapsStatus_Type(Integer32):
    """Custom type wfBrSrIpEncapsStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("learned", 3)
    )


_WfBrSrIpEncapsStatus_Type.__name__ = "Integer32"
_WfBrSrIpEncapsStatus_Object = MibTableColumn
wfBrSrIpEncapsStatus = _WfBrSrIpEncapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 5, 1, 3),
    _WfBrSrIpEncapsStatus_Type()
)
wfBrSrIpEncapsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsStatus.setStatus("obsolete")
_WfBrSrTrafficFilterTable_Object = MibTable
wfBrSrTrafficFilterTable = _WfBrSrTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterTable.setStatus("mandatory")
_WfBrSrTrafficFilterEntry_Object = MibTableRow
wfBrSrTrafficFilterEntry = _WfBrSrTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1)
)
wfBrSrTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrTrafficFilterCircuit"),
    (0, "Wellfleet-SR-MIB", "wfBrSrTrafficFilterRuleNumber"),
    (0, "Wellfleet-SR-MIB", "wfBrSrTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterEntry.setStatus("mandatory")


class _WfBrSrTrafficFilterCreate_Type(Integer32):
    """Custom type wfBrSrTrafficFilterCreate based on Integer32"""
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


_WfBrSrTrafficFilterCreate_Type.__name__ = "Integer32"
_WfBrSrTrafficFilterCreate_Object = MibTableColumn
wfBrSrTrafficFilterCreate = _WfBrSrTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 1),
    _WfBrSrTrafficFilterCreate_Type()
)
wfBrSrTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterCreate.setStatus("mandatory")


class _WfBrSrTrafficFilterEnable_Type(Integer32):
    """Custom type wfBrSrTrafficFilterEnable based on Integer32"""
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


_WfBrSrTrafficFilterEnable_Type.__name__ = "Integer32"
_WfBrSrTrafficFilterEnable_Object = MibTableColumn
wfBrSrTrafficFilterEnable = _WfBrSrTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 2),
    _WfBrSrTrafficFilterEnable_Type()
)
wfBrSrTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterEnable.setStatus("mandatory")


class _WfBrSrTrafficFilterStatus_Type(Integer32):
    """Custom type wfBrSrTrafficFilterStatus based on Integer32"""
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


_WfBrSrTrafficFilterStatus_Type.__name__ = "Integer32"
_WfBrSrTrafficFilterStatus_Object = MibTableColumn
wfBrSrTrafficFilterStatus = _WfBrSrTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 3),
    _WfBrSrTrafficFilterStatus_Type()
)
wfBrSrTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterStatus.setStatus("mandatory")
_WfBrSrTrafficFilterCounter_Type = Counter32
_WfBrSrTrafficFilterCounter_Object = MibTableColumn
wfBrSrTrafficFilterCounter = _WfBrSrTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 4),
    _WfBrSrTrafficFilterCounter_Type()
)
wfBrSrTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterCounter.setStatus("mandatory")
_WfBrSrTrafficFilterDefinition_Type = OctetString
_WfBrSrTrafficFilterDefinition_Object = MibTableColumn
wfBrSrTrafficFilterDefinition = _WfBrSrTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 5),
    _WfBrSrTrafficFilterDefinition_Type()
)
wfBrSrTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterDefinition.setStatus("mandatory")
_WfBrSrTrafficFilterReserved_Type = Integer32
_WfBrSrTrafficFilterReserved_Object = MibTableColumn
wfBrSrTrafficFilterReserved = _WfBrSrTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 6),
    _WfBrSrTrafficFilterReserved_Type()
)
wfBrSrTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterReserved.setStatus("mandatory")
_WfBrSrTrafficFilterCircuit_Type = Integer32
_WfBrSrTrafficFilterCircuit_Object = MibTableColumn
wfBrSrTrafficFilterCircuit = _WfBrSrTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 7),
    _WfBrSrTrafficFilterCircuit_Type()
)
wfBrSrTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterCircuit.setStatus("mandatory")
_WfBrSrTrafficFilterRuleNumber_Type = Integer32
_WfBrSrTrafficFilterRuleNumber_Object = MibTableColumn
wfBrSrTrafficFilterRuleNumber = _WfBrSrTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 8),
    _WfBrSrTrafficFilterRuleNumber_Type()
)
wfBrSrTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterRuleNumber.setStatus("mandatory")
_WfBrSrTrafficFilterFragment_Type = Integer32
_WfBrSrTrafficFilterFragment_Object = MibTableColumn
wfBrSrTrafficFilterFragment = _WfBrSrTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 9),
    _WfBrSrTrafficFilterFragment_Type()
)
wfBrSrTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterFragment.setStatus("mandatory")
_WfBrSrTrafficFilterName_Type = DisplayString
_WfBrSrTrafficFilterName_Object = MibTableColumn
wfBrSrTrafficFilterName = _WfBrSrTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 6, 1, 10),
    _WfBrSrTrafficFilterName_Type()
)
wfBrSrTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrTrafficFilterName.setStatus("mandatory")
_WfBrSrEsRifTable_Object = MibTable
wfBrSrEsRifTable = _WfBrSrEsRifTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    wfBrSrEsRifTable.setStatus("mandatory")
_WfBrSrEsRifEntry_Object = MibTableRow
wfBrSrEsRifEntry = _WfBrSrEsRifEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1)
)
wfBrSrEsRifEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrEsRifCircuit"),
    (0, "Wellfleet-SR-MIB", "wfBrSrEsRifProtocol"),
    (0, "Wellfleet-SR-MIB", "wfBrSrEsRifMacAddr"),
)
if mibBuilder.loadTexts:
    wfBrSrEsRifEntry.setStatus("mandatory")
_WfBrSrEsRifCircuit_Type = Integer32
_WfBrSrEsRifCircuit_Object = MibTableColumn
wfBrSrEsRifCircuit = _WfBrSrEsRifCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1, 1),
    _WfBrSrEsRifCircuit_Type()
)
wfBrSrEsRifCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrEsRifCircuit.setStatus("mandatory")


class _WfBrSrEsRifProtocol_Type(OctetString):
    """Custom type wfBrSrEsRifProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfBrSrEsRifProtocol_Type.__name__ = "OctetString"
_WfBrSrEsRifProtocol_Object = MibTableColumn
wfBrSrEsRifProtocol = _WfBrSrEsRifProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1, 2),
    _WfBrSrEsRifProtocol_Type()
)
wfBrSrEsRifProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrEsRifProtocol.setStatus("mandatory")


class _WfBrSrEsRifMacAddr_Type(OctetString):
    """Custom type wfBrSrEsRifMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfBrSrEsRifMacAddr_Type.__name__ = "OctetString"
_WfBrSrEsRifMacAddr_Object = MibTableColumn
wfBrSrEsRifMacAddr = _WfBrSrEsRifMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1, 3),
    _WfBrSrEsRifMacAddr_Type()
)
wfBrSrEsRifMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrEsRifMacAddr.setStatus("mandatory")
_WfBrSrEsRifRoute_Type = OctetString
_WfBrSrEsRifRoute_Object = MibTableColumn
wfBrSrEsRifRoute = _WfBrSrEsRifRoute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 7, 1, 4),
    _WfBrSrEsRifRoute_Type()
)
wfBrSrEsRifRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrEsRifRoute.setStatus("mandatory")
_WfBrSrNbRifTable_Object = MibTable
wfBrSrNbRifTable = _WfBrSrNbRifTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    wfBrSrNbRifTable.setStatus("mandatory")
_WfBrSrNbRifEntry_Object = MibTableRow
wfBrSrNbRifEntry = _WfBrSrNbRifEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 8, 1)
)
wfBrSrNbRifEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrNbName"),
)
if mibBuilder.loadTexts:
    wfBrSrNbRifEntry.setStatus("mandatory")


class _WfBrSrNbName_Type(OctetString):
    """Custom type wfBrSrNbName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WfBrSrNbName_Type.__name__ = "OctetString"
_WfBrSrNbName_Object = MibTableColumn
wfBrSrNbName = _WfBrSrNbName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 8, 1, 1),
    _WfBrSrNbName_Type()
)
wfBrSrNbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbName.setStatus("mandatory")
_WfBrSrNbMacAddress_Type = OctetString
_WfBrSrNbMacAddress_Object = MibTableColumn
wfBrSrNbMacAddress = _WfBrSrNbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 8, 1, 2),
    _WfBrSrNbMacAddress_Type()
)
wfBrSrNbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbMacAddress.setStatus("mandatory")


class _WfBrSrNbStatic_Type(Integer32):
    """Custom type wfBrSrNbStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learned", 2),
          ("static", 1))
    )


_WfBrSrNbStatic_Type.__name__ = "Integer32"
_WfBrSrNbStatic_Object = MibTableColumn
wfBrSrNbStatic = _WfBrSrNbStatic_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 8, 1, 3),
    _WfBrSrNbStatic_Type()
)
wfBrSrNbStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbStatic.setStatus("mandatory")
_WfBrSrNbRif_Type = OctetString
_WfBrSrNbRif_Object = MibTableColumn
wfBrSrNbRif = _WfBrSrNbRif_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 8, 1, 4),
    _WfBrSrNbRif_Type()
)
wfBrSrNbRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbRif.setStatus("mandatory")
_WfBrSrNbRifCacheHits_Type = Counter32
_WfBrSrNbRifCacheHits_Object = MibTableColumn
wfBrSrNbRifCacheHits = _WfBrSrNbRifCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 8, 1, 5),
    _WfBrSrNbRifCacheHits_Type()
)
wfBrSrNbRifCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbRifCacheHits.setStatus("mandatory")
_WfBrSrNbQueryTable_Object = MibTable
wfBrSrNbQueryTable = _WfBrSrNbQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    wfBrSrNbQueryTable.setStatus("mandatory")
_WfBrSrNbQueryEntry_Object = MibTableRow
wfBrSrNbQueryEntry = _WfBrSrNbQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 9, 1)
)
wfBrSrNbQueryEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrNbQueryMacAddress"),
    (0, "Wellfleet-SR-MIB", "wfBrSrNbRspCorrelator"),
)
if mibBuilder.loadTexts:
    wfBrSrNbQueryEntry.setStatus("mandatory")


class _WfBrSrNbQueryMacAddress_Type(OctetString):
    """Custom type wfBrSrNbQueryMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfBrSrNbQueryMacAddress_Type.__name__ = "OctetString"
_WfBrSrNbQueryMacAddress_Object = MibTableColumn
wfBrSrNbQueryMacAddress = _WfBrSrNbQueryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 9, 1, 1),
    _WfBrSrNbQueryMacAddress_Type()
)
wfBrSrNbQueryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbQueryMacAddress.setStatus("mandatory")
_WfBrSrNbRspCorrelator_Type = Integer32
_WfBrSrNbRspCorrelator_Object = MibTableColumn
wfBrSrNbRspCorrelator = _WfBrSrNbRspCorrelator_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 9, 1, 2),
    _WfBrSrNbRspCorrelator_Type()
)
wfBrSrNbRspCorrelator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbRspCorrelator.setStatus("mandatory")
_WfBrSrNbQuery_Type = OctetString
_WfBrSrNbQuery_Object = MibTableColumn
wfBrSrNbQuery = _WfBrSrNbQuery_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 9, 1, 3),
    _WfBrSrNbQuery_Type()
)
wfBrSrNbQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbQuery.setStatus("mandatory")
_WfBrSrNbQueryFilteredFrames_Type = Counter32
_WfBrSrNbQueryFilteredFrames_Object = MibTableColumn
wfBrSrNbQueryFilteredFrames = _WfBrSrNbQueryFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 9, 1, 4),
    _WfBrSrNbQueryFilteredFrames_Type()
)
wfBrSrNbQueryFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbQueryFilteredFrames.setStatus("mandatory")
_WfBrSrNbStaticTable_Object = MibTable
wfBrSrNbStaticTable = _WfBrSrNbStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    wfBrSrNbStaticTable.setStatus("mandatory")
_WfBrSrNbStaticEntry_Object = MibTableRow
wfBrSrNbStaticEntry = _WfBrSrNbStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 10, 1)
)
wfBrSrNbStaticEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrNbStaticName"),
)
if mibBuilder.loadTexts:
    wfBrSrNbStaticEntry.setStatus("mandatory")


class _WfBrSrNbStaticDelete_Type(Integer32):
    """Custom type wfBrSrNbStaticDelete based on Integer32"""
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


_WfBrSrNbStaticDelete_Type.__name__ = "Integer32"
_WfBrSrNbStaticDelete_Object = MibTableColumn
wfBrSrNbStaticDelete = _WfBrSrNbStaticDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 10, 1, 1),
    _WfBrSrNbStaticDelete_Type()
)
wfBrSrNbStaticDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrNbStaticDelete.setStatus("mandatory")


class _WfBrSrNbStaticDisable_Type(Integer32):
    """Custom type wfBrSrNbStaticDisable based on Integer32"""
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


_WfBrSrNbStaticDisable_Type.__name__ = "Integer32"
_WfBrSrNbStaticDisable_Object = MibTableColumn
wfBrSrNbStaticDisable = _WfBrSrNbStaticDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 10, 1, 2),
    _WfBrSrNbStaticDisable_Type()
)
wfBrSrNbStaticDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrNbStaticDisable.setStatus("mandatory")


class _WfBrSrNbStaticState_Type(Integer32):
    """Custom type wfBrSrNbStaticState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfBrSrNbStaticState_Type.__name__ = "Integer32"
_WfBrSrNbStaticState_Object = MibTableColumn
wfBrSrNbStaticState = _WfBrSrNbStaticState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 10, 1, 3),
    _WfBrSrNbStaticState_Type()
)
wfBrSrNbStaticState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbStaticState.setStatus("mandatory")


class _WfBrSrNbStaticName_Type(OctetString):
    """Custom type wfBrSrNbStaticName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WfBrSrNbStaticName_Type.__name__ = "OctetString"
_WfBrSrNbStaticName_Object = MibTableColumn
wfBrSrNbStaticName = _WfBrSrNbStaticName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 10, 1, 4),
    _WfBrSrNbStaticName_Type()
)
wfBrSrNbStaticName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrNbStaticName.setStatus("mandatory")
_WfBrSrNbStaticMacAddress_Type = OctetString
_WfBrSrNbStaticMacAddress_Object = MibTableColumn
wfBrSrNbStaticMacAddress = _WfBrSrNbStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 10, 1, 5),
    _WfBrSrNbStaticMacAddress_Type()
)
wfBrSrNbStaticMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrNbStaticMacAddress.setStatus("mandatory")
_WfBrSrNbStaticRif_Type = OctetString
_WfBrSrNbStaticRif_Object = MibTableColumn
wfBrSrNbStaticRif = _WfBrSrNbStaticRif_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 10, 1, 6),
    _WfBrSrNbStaticRif_Type()
)
wfBrSrNbStaticRif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrSrNbStaticRif.setStatus("mandatory")
_WfBrXb_ObjectIdentity = ObjectIdentity
wfBrXb = _WfBrXb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11)
)


class _WfBrXbBaseDelete_Type(Integer32):
    """Custom type wfBrXbBaseDelete based on Integer32"""
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


_WfBrXbBaseDelete_Type.__name__ = "Integer32"
_WfBrXbBaseDelete_Object = MibScalar
wfBrXbBaseDelete = _WfBrXbBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 1),
    _WfBrXbBaseDelete_Type()
)
wfBrXbBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseDelete.setStatus("mandatory")


class _WfBrXbBaseDisable_Type(Integer32):
    """Custom type wfBrXbBaseDisable based on Integer32"""
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


_WfBrXbBaseDisable_Type.__name__ = "Integer32"
_WfBrXbBaseDisable_Object = MibScalar
wfBrXbBaseDisable = _WfBrXbBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 2),
    _WfBrXbBaseDisable_Type()
)
wfBrXbBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseDisable.setStatus("mandatory")


class _WfBrXbBaseEthernetLanId_Type(Integer32):
    """Custom type wfBrXbBaseEthernetLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WfBrXbBaseEthernetLanId_Type.__name__ = "Integer32"
_WfBrXbBaseEthernetLanId_Object = MibScalar
wfBrXbBaseEthernetLanId = _WfBrXbBaseEthernetLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 3),
    _WfBrXbBaseEthernetLanId_Type()
)
wfBrXbBaseEthernetLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseEthernetLanId.setStatus("mandatory")


class _WfBrXbBaseMaxRifEntries_Type(Integer32):
    """Custom type wfBrXbBaseMaxRifEntries based on Integer32"""
    defaultValue = 255


_WfBrXbBaseMaxRifEntries_Object = MibScalar
wfBrXbBaseMaxRifEntries = _WfBrXbBaseMaxRifEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 4),
    _WfBrXbBaseMaxRifEntries_Type()
)
wfBrXbBaseMaxRifEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseMaxRifEntries.setStatus("mandatory")
_WfBrXbBaseCurrentRifEntries_Type = Integer32
_WfBrXbBaseCurrentRifEntries_Object = MibScalar
wfBrXbBaseCurrentRifEntries = _WfBrXbBaseCurrentRifEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 5),
    _WfBrXbBaseCurrentRifEntries_Type()
)
wfBrXbBaseCurrentRifEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrXbBaseCurrentRifEntries.setStatus("mandatory")


class _WfBrXbBaseAgeTime_Type(Integer32):
    """Custom type wfBrXbBaseAgeTime based on Integer32"""
    defaultValue = 300


_WfBrXbBaseAgeTime_Object = MibScalar
wfBrXbBaseAgeTime = _WfBrXbBaseAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 6),
    _WfBrXbBaseAgeTime_Type()
)
wfBrXbBaseAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseAgeTime.setStatus("mandatory")


class _WfBrXbBaseBcastAddressConversionDisable_Type(Integer32):
    """Custom type wfBrXbBaseBcastAddressConversionDisable based on Integer32"""
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


_WfBrXbBaseBcastAddressConversionDisable_Type.__name__ = "Integer32"
_WfBrXbBaseBcastAddressConversionDisable_Object = MibScalar
wfBrXbBaseBcastAddressConversionDisable = _WfBrXbBaseBcastAddressConversionDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 7),
    _WfBrXbBaseBcastAddressConversionDisable_Type()
)
wfBrXbBaseBcastAddressConversionDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseBcastAddressConversionDisable.setStatus("mandatory")


class _WfBrXbBaseDefaultMode_Type(Integer32):
    """Custom type wfBrXbBaseDefaultMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8023", 2))
    )


_WfBrXbBaseDefaultMode_Type.__name__ = "Integer32"
_WfBrXbBaseDefaultMode_Object = MibScalar
wfBrXbBaseDefaultMode = _WfBrXbBaseDefaultMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 8),
    _WfBrXbBaseDefaultMode_Type()
)
wfBrXbBaseDefaultMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseDefaultMode.setStatus("mandatory")


class _WfBrXbBaseBcastMode_Type(Integer32):
    """Custom type wfBrXbBaseBcastMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("are", 1),
          ("ste", 2))
    )


_WfBrXbBaseBcastMode_Type.__name__ = "Integer32"
_WfBrXbBaseBcastMode_Object = MibScalar
wfBrXbBaseBcastMode = _WfBrXbBaseBcastMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 9),
    _WfBrXbBaseBcastMode_Type()
)
wfBrXbBaseBcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseBcastMode.setStatus("mandatory")
_WfBrXbBaseSaps_Type = OctetString
_WfBrXbBaseSaps_Object = MibScalar
wfBrXbBaseSaps = _WfBrXbBaseSaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 10),
    _WfBrXbBaseSaps_Type()
)
wfBrXbBaseSaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbBaseSaps.setStatus("mandatory")


class _WfBrXbFddiBridge_Type(Integer32):
    """Custom type wfBrXbFddiBridge based on Integer32"""
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


_WfBrXbFddiBridge_Type.__name__ = "Integer32"
_WfBrXbFddiBridge_Object = MibScalar
wfBrXbFddiBridge = _WfBrXbFddiBridge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 11, 11),
    _WfBrXbFddiBridge_Type()
)
wfBrXbFddiBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbFddiBridge.setStatus("mandatory")
_WfBrXbAddressMapTable_Object = MibTable
wfBrXbAddressMapTable = _WfBrXbAddressMapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    wfBrXbAddressMapTable.setStatus("mandatory")
_WfBrXbAddressMapEntry_Object = MibTableRow
wfBrXbAddressMapEntry = _WfBrXbAddressMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 12, 1)
)
wfBrXbAddressMapEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrXbAddressMapEthernetAddress"),
)
if mibBuilder.loadTexts:
    wfBrXbAddressMapEntry.setStatus("mandatory")


class _WfBrXbAddressMapDelete_Type(Integer32):
    """Custom type wfBrXbAddressMapDelete based on Integer32"""
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


_WfBrXbAddressMapDelete_Type.__name__ = "Integer32"
_WfBrXbAddressMapDelete_Object = MibTableColumn
wfBrXbAddressMapDelete = _WfBrXbAddressMapDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 12, 1, 1),
    _WfBrXbAddressMapDelete_Type()
)
wfBrXbAddressMapDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbAddressMapDelete.setStatus("mandatory")


class _WfBrXbAddressMapEthernetAddress_Type(OctetString):
    """Custom type wfBrXbAddressMapEthernetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfBrXbAddressMapEthernetAddress_Type.__name__ = "OctetString"
_WfBrXbAddressMapEthernetAddress_Object = MibTableColumn
wfBrXbAddressMapEthernetAddress = _WfBrXbAddressMapEthernetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 12, 1, 2),
    _WfBrXbAddressMapEthernetAddress_Type()
)
wfBrXbAddressMapEthernetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrXbAddressMapEthernetAddress.setStatus("mandatory")
_WfBrXbAddressMapTokenRingAddress_Type = OctetString
_WfBrXbAddressMapTokenRingAddress_Object = MibTableColumn
wfBrXbAddressMapTokenRingAddress = _WfBrXbAddressMapTokenRingAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 12, 1, 3),
    _WfBrXbAddressMapTokenRingAddress_Type()
)
wfBrXbAddressMapTokenRingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbAddressMapTokenRingAddress.setStatus("mandatory")
_WfBrXbRifTable_Object = MibTable
wfBrXbRifTable = _WfBrXbRifTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    wfBrXbRifTable.setStatus("mandatory")
_WfBrXbRifEntry_Object = MibTableRow
wfBrXbRifEntry = _WfBrXbRifEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 13, 1)
)
wfBrXbRifEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrXbRifMacAddress"),
)
if mibBuilder.loadTexts:
    wfBrXbRifEntry.setStatus("mandatory")


class _WfBrXbRifMacAddress_Type(OctetString):
    """Custom type wfBrXbRifMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfBrXbRifMacAddress_Type.__name__ = "OctetString"
_WfBrXbRifMacAddress_Object = MibTableColumn
wfBrXbRifMacAddress = _WfBrXbRifMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 13, 1, 1),
    _WfBrXbRifMacAddress_Type()
)
wfBrXbRifMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrXbRifMacAddress.setStatus("mandatory")
_WfBrXbRifField_Type = OctetString
_WfBrXbRifField_Object = MibTableColumn
wfBrXbRifField = _WfBrXbRifField_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 13, 1, 2),
    _WfBrXbRifField_Type()
)
wfBrXbRifField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrXbRifField.setStatus("mandatory")
_WfBrXbStationTypeTable_Object = MibTable
wfBrXbStationTypeTable = _WfBrXbStationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    wfBrXbStationTypeTable.setStatus("mandatory")
_WfBrXbStationTypeEntry_Object = MibTableRow
wfBrXbStationTypeEntry = _WfBrXbStationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 14, 1)
)
wfBrXbStationTypeEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrXbStationTypeEthernetAddress"),
)
if mibBuilder.loadTexts:
    wfBrXbStationTypeEntry.setStatus("mandatory")


class _WfBrXbStationTypeDelete_Type(Integer32):
    """Custom type wfBrXbStationTypeDelete based on Integer32"""
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


_WfBrXbStationTypeDelete_Type.__name__ = "Integer32"
_WfBrXbStationTypeDelete_Object = MibTableColumn
wfBrXbStationTypeDelete = _WfBrXbStationTypeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 14, 1, 1),
    _WfBrXbStationTypeDelete_Type()
)
wfBrXbStationTypeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbStationTypeDelete.setStatus("mandatory")


class _WfBrXbStationTypeEthernetAddress_Type(OctetString):
    """Custom type wfBrXbStationTypeEthernetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfBrXbStationTypeEthernetAddress_Type.__name__ = "OctetString"
_WfBrXbStationTypeEthernetAddress_Object = MibTableColumn
wfBrXbStationTypeEthernetAddress = _WfBrXbStationTypeEthernetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 14, 1, 2),
    _WfBrXbStationTypeEthernetAddress_Type()
)
wfBrXbStationTypeEthernetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrXbStationTypeEthernetAddress.setStatus("mandatory")


class _WfBrXbStationTypeIndicator_Type(Integer32):
    """Custom type wfBrXbStationTypeIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8023", 2))
    )


_WfBrXbStationTypeIndicator_Type.__name__ = "Integer32"
_WfBrXbStationTypeIndicator_Object = MibTableColumn
wfBrXbStationTypeIndicator = _WfBrXbStationTypeIndicator_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 14, 1, 3),
    _WfBrXbStationTypeIndicator_Type()
)
wfBrXbStationTypeIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrXbStationTypeIndicator.setStatus("mandatory")
_WfBrSrIpEncapsRBTable_Object = MibTable
wfBrSrIpEncapsRBTable = _WfBrSrIpEncapsRBTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    wfBrSrIpEncapsRBTable.setStatus("mandatory")
_WfBrSrIpEncapsRBEntry_Object = MibTableRow
wfBrSrIpEncapsRBEntry = _WfBrSrIpEncapsRBEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 15, 1)
)
wfBrSrIpEncapsRBEntry.setIndexNames(
    (0, "Wellfleet-SR-MIB", "wfBrSrIpEncapsRBRing"),
    (0, "Wellfleet-SR-MIB", "wfBrSrIpEncapsRBBridge"),
)
if mibBuilder.loadTexts:
    wfBrSrIpEncapsRBEntry.setStatus("mandatory")
_WfBrSrIpEncapsRBRing_Type = Integer32
_WfBrSrIpEncapsRBRing_Object = MibTableColumn
wfBrSrIpEncapsRBRing = _WfBrSrIpEncapsRBRing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 15, 1, 1),
    _WfBrSrIpEncapsRBRing_Type()
)
wfBrSrIpEncapsRBRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsRBRing.setStatus("mandatory")
_WfBrSrIpEncapsRBBridge_Type = Integer32
_WfBrSrIpEncapsRBBridge_Object = MibTableColumn
wfBrSrIpEncapsRBBridge = _WfBrSrIpEncapsRBBridge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 15, 1, 2),
    _WfBrSrIpEncapsRBBridge_Type()
)
wfBrSrIpEncapsRBBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsRBBridge.setStatus("mandatory")
_WfBrSrIpEncapsRBIpAddress_Type = IpAddress
_WfBrSrIpEncapsRBIpAddress_Object = MibTableColumn
wfBrSrIpEncapsRBIpAddress = _WfBrSrIpEncapsRBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 15, 1, 3),
    _WfBrSrIpEncapsRBIpAddress_Type()
)
wfBrSrIpEncapsRBIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsRBIpAddress.setStatus("mandatory")


class _WfBrSrIpEncapsRBStatus_Type(Integer32):
    """Custom type wfBrSrIpEncapsRBStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("learned", 3)
    )


_WfBrSrIpEncapsRBStatus_Type.__name__ = "Integer32"
_WfBrSrIpEncapsRBStatus_Object = MibTableColumn
wfBrSrIpEncapsRBStatus = _WfBrSrIpEncapsRBStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 2, 15, 1, 4),
    _WfBrSrIpEncapsRBStatus_Type()
)
wfBrSrIpEncapsRBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrSrIpEncapsRBStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SR-MIB",
    **{"wfBrSourceRouting": wfBrSourceRouting,
       "wfBrSr": wfBrSr,
       "wfBrSrBaseDelete": wfBrSrBaseDelete,
       "wfBrSrBaseDisable": wfBrSrBaseDisable,
       "wfBrSrBaseState": wfBrSrBaseState,
       "wfBrSrBaseInternalLanId": wfBrSrBaseInternalLanId,
       "wfBrSrBaseBridgeId": wfBrSrBaseBridgeId,
       "wfBrSrBaseGroupLanId": wfBrSrBaseGroupLanId,
       "wfBrSrBaseIpEncapsDisable": wfBrSrBaseIpEncapsDisable,
       "wfBrSrBaseIpNetworkRingId": wfBrSrBaseIpNetworkRingId,
       "wfBrSrBaseIpInReceives": wfBrSrBaseIpInReceives,
       "wfBrSrBaseIpSeqErrors": wfBrSrBaseIpSeqErrors,
       "wfBrSrBaseIpMtuSize": wfBrSrBaseIpMtuSize,
       "wfBrSrBaseNbServerRifCacheDisable": wfBrSrBaseNbServerRifCacheDisable,
       "wfBrSrBaseNbClientRifCacheDisable": wfBrSrBaseNbClientRifCacheDisable,
       "wfBrSrBaseNbDatagramRifCacheDisable": wfBrSrBaseNbDatagramRifCacheDisable,
       "wfBrSrBaseNb15CharacterDisable": wfBrSrBaseNb15CharacterDisable,
       "wfBrSrBaseNbRifMibDisable": wfBrSrBaseNbRifMibDisable,
       "wfBrSrBaseNbMaximumRifEntries": wfBrSrBaseNbMaximumRifEntries,
       "wfBrSrBaseNbCurrentRifEntries": wfBrSrBaseNbCurrentRifEntries,
       "wfBrSrBaseNbRifAgeTime": wfBrSrBaseNbRifAgeTime,
       "wfBrSrBaseNbRifHashEntries": wfBrSrBaseNbRifHashEntries,
       "wfBrSrBaseNbRifCacheHits": wfBrSrBaseNbRifCacheHits,
       "wfBrSrBaseNbRifCacheMisses": wfBrSrBaseNbRifCacheMisses,
       "wfBrSrBaseNbRifDroppedFrames": wfBrSrBaseNbRifDroppedFrames,
       "wfBrSrBaseNbQueryCacheDisable": wfBrSrBaseNbQueryCacheDisable,
       "wfBrSrBaseNbQueryMibDisable": wfBrSrBaseNbQueryMibDisable,
       "wfBrSrBaseNbMaximumQueryEntries": wfBrSrBaseNbMaximumQueryEntries,
       "wfBrSrBaseNbCurrentQueryEntries": wfBrSrBaseNbCurrentQueryEntries,
       "wfBrSrBaseNbQueryAgeTime": wfBrSrBaseNbQueryAgeTime,
       "wfBrSrBaseNbQueryFilteredFrames": wfBrSrBaseNbQueryFilteredFrames,
       "wfBrSrBaseStpEnable": wfBrSrBaseStpEnable,
       "wfBrSrBaseStpState": wfBrSrBaseStpState,
       "wfBrSrBaseStpProtocolSpecification": wfBrSrBaseStpProtocolSpecification,
       "wfBrSrBaseStpBridgeID": wfBrSrBaseStpBridgeID,
       "wfBrSrBaseStpTimeSinceTopologyChange": wfBrSrBaseStpTimeSinceTopologyChange,
       "wfBrSrBaseStpTopChanges": wfBrSrBaseStpTopChanges,
       "wfBrSrBaseStpDesignatedRoot": wfBrSrBaseStpDesignatedRoot,
       "wfBrSrBaseStpRootCost": wfBrSrBaseStpRootCost,
       "wfBrSrBaseStpRootPort": wfBrSrBaseStpRootPort,
       "wfBrSrBaseStpMaxAge": wfBrSrBaseStpMaxAge,
       "wfBrSrBaseStpHelloTime": wfBrSrBaseStpHelloTime,
       "wfBrSrBaseStpHoldTime": wfBrSrBaseStpHoldTime,
       "wfBrSrBaseStpForwardDelay": wfBrSrBaseStpForwardDelay,
       "wfBrSrBaseStpBridgeMaxAge": wfBrSrBaseStpBridgeMaxAge,
       "wfBrSrBaseStpBridgeHelloTime": wfBrSrBaseStpBridgeHelloTime,
       "wfBrSrBaseStpBridgeForwardDelay": wfBrSrBaseStpBridgeForwardDelay,
       "wfBrSrBaseNbNameQueryCacheDisable": wfBrSrBaseNbNameQueryCacheDisable,
       "wfBrSrBaseAreHopCntLimit": wfBrSrBaseAreHopCntLimit,
       "wfBrSrInterfaceTable": wfBrSrInterfaceTable,
       "wfBrSrInterfaceEntry": wfBrSrInterfaceEntry,
       "wfBrSrInterfaceDelete": wfBrSrInterfaceDelete,
       "wfBrSrInterfaceDisable": wfBrSrInterfaceDisable,
       "wfBrSrInterfaceState": wfBrSrInterfaceState,
       "wfBrSrInterfaceCircuit": wfBrSrInterfaceCircuit,
       "wfBrSrInterfaceMaxRds": wfBrSrInterfaceMaxRds,
       "wfBrSrInterfaceRing": wfBrSrInterfaceRing,
       "wfBrSrInterfaceBlockOutSte": wfBrSrInterfaceBlockOutSte,
       "wfBrSrInterfaceBlockInSte": wfBrSrInterfaceBlockInSte,
       "wfBrSrInterfaceBlockIp": wfBrSrInterfaceBlockIp,
       "wfBrSrInterfaceIpAddress": wfBrSrInterfaceIpAddress,
       "wfBrSrInterfaceInFrames": wfBrSrInterfaceInFrames,
       "wfBrSrInterfaceOutFrames": wfBrSrInterfaceOutFrames,
       "wfBrSrInterfaceOutIpFrames": wfBrSrInterfaceOutIpFrames,
       "wfBrSrInterfaceDropInvalidRcs": wfBrSrInterfaceDropInvalidRcs,
       "wfBrSrInterfaceDropInvalidRings": wfBrSrInterfaceDropInvalidRings,
       "wfBrSrInterfaceDropSrfs": wfBrSrInterfaceDropSrfs,
       "wfBrSrInterfaceNbServerRifCacheDisable": wfBrSrInterfaceNbServerRifCacheDisable,
       "wfBrSrInterfaceNbClientRifCacheDisable": wfBrSrInterfaceNbClientRifCacheDisable,
       "wfBrSrInterfaceNbDatagramRifCacheDisable": wfBrSrInterfaceNbDatagramRifCacheDisable,
       "wfBrSrInterfaceNbQueryCacheDisable": wfBrSrInterfaceNbQueryCacheDisable,
       "wfBrSrInterfaceXbInFrames": wfBrSrInterfaceXbInFrames,
       "wfBrSrInterfaceXbDropFrames": wfBrSrInterfaceXbDropFrames,
       "wfBrSrInterfaceFrBcastDlci": wfBrSrInterfaceFrBcastDlci,
       "wfBrSrInterfaceEncapsFormat": wfBrSrInterfaceEncapsFormat,
       "wfBrSrInterfaceStpEnable": wfBrSrInterfaceStpEnable,
       "wfBrSrInterfaceStpState": wfBrSrInterfaceStpState,
       "wfBrSrInterfaceStpMultiCastAddr": wfBrSrInterfaceStpMultiCastAddr,
       "wfBrSrInterfaceStpPathCost": wfBrSrInterfaceStpPathCost,
       "wfBrSrInterfaceStpDesignatedRoot": wfBrSrInterfaceStpDesignatedRoot,
       "wfBrSrInterfaceStpDesignatedCost": wfBrSrInterfaceStpDesignatedCost,
       "wfBrSrInterfaceStpDesignatedBridge": wfBrSrInterfaceStpDesignatedBridge,
       "wfBrSrInterfaceStpDesignatedPort": wfBrSrInterfaceStpDesignatedPort,
       "wfBrSrInterfaceStpForwardTransitions": wfBrSrInterfaceStpForwardTransitions,
       "wfBrSrInterfaceStpPktsXmitd": wfBrSrInterfaceStpPktsXmitd,
       "wfBrSrInterfaceStpPktsRcvd": wfBrSrInterfaceStpPktsRcvd,
       "wfBrSrInterfaceStpTranslationDisable": wfBrSrInterfaceStpTranslationDisable,
       "wfBrSrInterfaceMaxLfField": wfBrSrInterfaceMaxLfField,
       "wfBrSrInterfaceFilterAddress": wfBrSrInterfaceFilterAddress,
       "wfBrSrBridgeTable": wfBrSrBridgeTable,
       "wfBrSrBridgeEntry": wfBrSrBridgeEntry,
       "wfBrSrBridgeDelete": wfBrSrBridgeDelete,
       "wfBrSrBridgeId": wfBrSrBridgeId,
       "wfBrSrIpExplorerTable": wfBrSrIpExplorerTable,
       "wfBrSrIpExplorerEntry": wfBrSrIpExplorerEntry,
       "wfBrSrIpExplorerDelete": wfBrSrIpExplorerDelete,
       "wfBrSrIpExplorerAddr": wfBrSrIpExplorerAddr,
       "wfBrSrIpExplorerProtocol": wfBrSrIpExplorerProtocol,
       "wfBrSrIpEncapsTable": wfBrSrIpEncapsTable,
       "wfBrSrIpEncapsEntry": wfBrSrIpEncapsEntry,
       "wfBrSrIpEncapsRing": wfBrSrIpEncapsRing,
       "wfBrSrIpEncapsIpAddress": wfBrSrIpEncapsIpAddress,
       "wfBrSrIpEncapsStatus": wfBrSrIpEncapsStatus,
       "wfBrSrTrafficFilterTable": wfBrSrTrafficFilterTable,
       "wfBrSrTrafficFilterEntry": wfBrSrTrafficFilterEntry,
       "wfBrSrTrafficFilterCreate": wfBrSrTrafficFilterCreate,
       "wfBrSrTrafficFilterEnable": wfBrSrTrafficFilterEnable,
       "wfBrSrTrafficFilterStatus": wfBrSrTrafficFilterStatus,
       "wfBrSrTrafficFilterCounter": wfBrSrTrafficFilterCounter,
       "wfBrSrTrafficFilterDefinition": wfBrSrTrafficFilterDefinition,
       "wfBrSrTrafficFilterReserved": wfBrSrTrafficFilterReserved,
       "wfBrSrTrafficFilterCircuit": wfBrSrTrafficFilterCircuit,
       "wfBrSrTrafficFilterRuleNumber": wfBrSrTrafficFilterRuleNumber,
       "wfBrSrTrafficFilterFragment": wfBrSrTrafficFilterFragment,
       "wfBrSrTrafficFilterName": wfBrSrTrafficFilterName,
       "wfBrSrEsRifTable": wfBrSrEsRifTable,
       "wfBrSrEsRifEntry": wfBrSrEsRifEntry,
       "wfBrSrEsRifCircuit": wfBrSrEsRifCircuit,
       "wfBrSrEsRifProtocol": wfBrSrEsRifProtocol,
       "wfBrSrEsRifMacAddr": wfBrSrEsRifMacAddr,
       "wfBrSrEsRifRoute": wfBrSrEsRifRoute,
       "wfBrSrNbRifTable": wfBrSrNbRifTable,
       "wfBrSrNbRifEntry": wfBrSrNbRifEntry,
       "wfBrSrNbName": wfBrSrNbName,
       "wfBrSrNbMacAddress": wfBrSrNbMacAddress,
       "wfBrSrNbStatic": wfBrSrNbStatic,
       "wfBrSrNbRif": wfBrSrNbRif,
       "wfBrSrNbRifCacheHits": wfBrSrNbRifCacheHits,
       "wfBrSrNbQueryTable": wfBrSrNbQueryTable,
       "wfBrSrNbQueryEntry": wfBrSrNbQueryEntry,
       "wfBrSrNbQueryMacAddress": wfBrSrNbQueryMacAddress,
       "wfBrSrNbRspCorrelator": wfBrSrNbRspCorrelator,
       "wfBrSrNbQuery": wfBrSrNbQuery,
       "wfBrSrNbQueryFilteredFrames": wfBrSrNbQueryFilteredFrames,
       "wfBrSrNbStaticTable": wfBrSrNbStaticTable,
       "wfBrSrNbStaticEntry": wfBrSrNbStaticEntry,
       "wfBrSrNbStaticDelete": wfBrSrNbStaticDelete,
       "wfBrSrNbStaticDisable": wfBrSrNbStaticDisable,
       "wfBrSrNbStaticState": wfBrSrNbStaticState,
       "wfBrSrNbStaticName": wfBrSrNbStaticName,
       "wfBrSrNbStaticMacAddress": wfBrSrNbStaticMacAddress,
       "wfBrSrNbStaticRif": wfBrSrNbStaticRif,
       "wfBrXb": wfBrXb,
       "wfBrXbBaseDelete": wfBrXbBaseDelete,
       "wfBrXbBaseDisable": wfBrXbBaseDisable,
       "wfBrXbBaseEthernetLanId": wfBrXbBaseEthernetLanId,
       "wfBrXbBaseMaxRifEntries": wfBrXbBaseMaxRifEntries,
       "wfBrXbBaseCurrentRifEntries": wfBrXbBaseCurrentRifEntries,
       "wfBrXbBaseAgeTime": wfBrXbBaseAgeTime,
       "wfBrXbBaseBcastAddressConversionDisable": wfBrXbBaseBcastAddressConversionDisable,
       "wfBrXbBaseDefaultMode": wfBrXbBaseDefaultMode,
       "wfBrXbBaseBcastMode": wfBrXbBaseBcastMode,
       "wfBrXbBaseSaps": wfBrXbBaseSaps,
       "wfBrXbFddiBridge": wfBrXbFddiBridge,
       "wfBrXbAddressMapTable": wfBrXbAddressMapTable,
       "wfBrXbAddressMapEntry": wfBrXbAddressMapEntry,
       "wfBrXbAddressMapDelete": wfBrXbAddressMapDelete,
       "wfBrXbAddressMapEthernetAddress": wfBrXbAddressMapEthernetAddress,
       "wfBrXbAddressMapTokenRingAddress": wfBrXbAddressMapTokenRingAddress,
       "wfBrXbRifTable": wfBrXbRifTable,
       "wfBrXbRifEntry": wfBrXbRifEntry,
       "wfBrXbRifMacAddress": wfBrXbRifMacAddress,
       "wfBrXbRifField": wfBrXbRifField,
       "wfBrXbStationTypeTable": wfBrXbStationTypeTable,
       "wfBrXbStationTypeEntry": wfBrXbStationTypeEntry,
       "wfBrXbStationTypeDelete": wfBrXbStationTypeDelete,
       "wfBrXbStationTypeEthernetAddress": wfBrXbStationTypeEthernetAddress,
       "wfBrXbStationTypeIndicator": wfBrXbStationTypeIndicator,
       "wfBrSrIpEncapsRBTable": wfBrSrIpEncapsRBTable,
       "wfBrSrIpEncapsRBEntry": wfBrSrIpEncapsRBEntry,
       "wfBrSrIpEncapsRBRing": wfBrSrIpEncapsRBRing,
       "wfBrSrIpEncapsRBBridge": wfBrSrIpEncapsRBBridge,
       "wfBrSrIpEncapsRBIpAddress": wfBrSrIpEncapsRBIpAddress,
       "wfBrSrIpEncapsRBStatus": wfBrSrIpEncapsRBStatus}
)
