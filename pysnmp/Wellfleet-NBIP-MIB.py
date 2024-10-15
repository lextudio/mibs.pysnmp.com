# SNMP MIB module (Wellfleet-NBIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-NBIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:45 2024
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

(wfNetBIOSIpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfNetBIOSIpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfNetbiosIp_ObjectIdentity = ObjectIdentity
wfNetbiosIp = _WfNetbiosIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1)
)


class _WfNetbiosIpDelete_Type(Integer32):
    """Custom type wfNetbiosIpDelete based on Integer32"""
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


_WfNetbiosIpDelete_Type.__name__ = "Integer32"
_WfNetbiosIpDelete_Object = MibScalar
wfNetbiosIpDelete = _WfNetbiosIpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 1),
    _WfNetbiosIpDelete_Type()
)
wfNetbiosIpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpDelete.setStatus("mandatory")


class _WfNetbiosIpDisable_Type(Integer32):
    """Custom type wfNetbiosIpDisable based on Integer32"""
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


_WfNetbiosIpDisable_Type.__name__ = "Integer32"
_WfNetbiosIpDisable_Object = MibScalar
wfNetbiosIpDisable = _WfNetbiosIpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 2),
    _WfNetbiosIpDisable_Type()
)
wfNetbiosIpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpDisable.setStatus("mandatory")


class _WfNetbiosIpState_Type(Integer32):
    """Custom type wfNetbiosIpState based on Integer32"""
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
          ("notpres", 4),
          ("up", 1))
    )


_WfNetbiosIpState_Type.__name__ = "Integer32"
_WfNetbiosIpState_Object = MibScalar
wfNetbiosIpState = _WfNetbiosIpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 3),
    _WfNetbiosIpState_Type()
)
wfNetbiosIpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpState.setStatus("mandatory")


class _WfNetbiosIpNameCacheDisable_Type(Integer32):
    """Custom type wfNetbiosIpNameCacheDisable based on Integer32"""
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


_WfNetbiosIpNameCacheDisable_Type.__name__ = "Integer32"
_WfNetbiosIpNameCacheDisable_Object = MibScalar
wfNetbiosIpNameCacheDisable = _WfNetbiosIpNameCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 4),
    _WfNetbiosIpNameCacheDisable_Type()
)
wfNetbiosIpNameCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpNameCacheDisable.setStatus("mandatory")


class _WfNetbiosIp15CharacterDisable_Type(Integer32):
    """Custom type wfNetbiosIp15CharacterDisable based on Integer32"""
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


_WfNetbiosIp15CharacterDisable_Type.__name__ = "Integer32"
_WfNetbiosIp15CharacterDisable_Object = MibScalar
wfNetbiosIp15CharacterDisable = _WfNetbiosIp15CharacterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 5),
    _WfNetbiosIp15CharacterDisable_Type()
)
wfNetbiosIp15CharacterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIp15CharacterDisable.setStatus("mandatory")


class _WfNetbiosIpNameCacheMibDisable_Type(Integer32):
    """Custom type wfNetbiosIpNameCacheMibDisable based on Integer32"""
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


_WfNetbiosIpNameCacheMibDisable_Type.__name__ = "Integer32"
_WfNetbiosIpNameCacheMibDisable_Object = MibScalar
wfNetbiosIpNameCacheMibDisable = _WfNetbiosIpNameCacheMibDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 6),
    _WfNetbiosIpNameCacheMibDisable_Type()
)
wfNetbiosIpNameCacheMibDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpNameCacheMibDisable.setStatus("mandatory")


class _WfNetbiosIpNameCacheMaximumEntries_Type(Integer32):
    """Custom type wfNetbiosIpNameCacheMaximumEntries based on Integer32"""
    defaultValue = 100


_WfNetbiosIpNameCacheMaximumEntries_Object = MibScalar
wfNetbiosIpNameCacheMaximumEntries = _WfNetbiosIpNameCacheMaximumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 7),
    _WfNetbiosIpNameCacheMaximumEntries_Type()
)
wfNetbiosIpNameCacheMaximumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpNameCacheMaximumEntries.setStatus("mandatory")
_WfNetbiosIpNameCacheCurrentEntries_Type = Integer32
_WfNetbiosIpNameCacheCurrentEntries_Object = MibScalar
wfNetbiosIpNameCacheCurrentEntries = _WfNetbiosIpNameCacheCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 8),
    _WfNetbiosIpNameCacheCurrentEntries_Type()
)
wfNetbiosIpNameCacheCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpNameCacheCurrentEntries.setStatus("mandatory")


class _WfNetbiosIpNameCacheAgeTime_Type(Integer32):
    """Custom type wfNetbiosIpNameCacheAgeTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 604800),
    )


_WfNetbiosIpNameCacheAgeTime_Type.__name__ = "Integer32"
_WfNetbiosIpNameCacheAgeTime_Object = MibScalar
wfNetbiosIpNameCacheAgeTime = _WfNetbiosIpNameCacheAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 9),
    _WfNetbiosIpNameCacheAgeTime_Type()
)
wfNetbiosIpNameCacheAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpNameCacheAgeTime.setStatus("mandatory")


class _WfNetbiosIpNameCacheHashEntries_Type(Integer32):
    """Custom type wfNetbiosIpNameCacheHashEntries based on Integer32"""
    defaultValue = 253


_WfNetbiosIpNameCacheHashEntries_Object = MibScalar
wfNetbiosIpNameCacheHashEntries = _WfNetbiosIpNameCacheHashEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 10),
    _WfNetbiosIpNameCacheHashEntries_Type()
)
wfNetbiosIpNameCacheHashEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpNameCacheHashEntries.setStatus("mandatory")
_WfNetbiosIpNameCacheHits_Type = Counter32
_WfNetbiosIpNameCacheHits_Object = MibScalar
wfNetbiosIpNameCacheHits = _WfNetbiosIpNameCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 11),
    _WfNetbiosIpNameCacheHits_Type()
)
wfNetbiosIpNameCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpNameCacheHits.setStatus("mandatory")
_WfNetbiosIpNameCacheMisses_Type = Counter32
_WfNetbiosIpNameCacheMisses_Object = MibScalar
wfNetbiosIpNameCacheMisses = _WfNetbiosIpNameCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 12),
    _WfNetbiosIpNameCacheMisses_Type()
)
wfNetbiosIpNameCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpNameCacheMisses.setStatus("mandatory")


class _WfNetbiosIpRebroadcastTTL_Type(Integer32):
    """Custom type wfNetbiosIpRebroadcastTTL based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfNetbiosIpRebroadcastTTL_Type.__name__ = "Integer32"
_WfNetbiosIpRebroadcastTTL_Object = MibScalar
wfNetbiosIpRebroadcastTTL = _WfNetbiosIpRebroadcastTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 13),
    _WfNetbiosIpRebroadcastTTL_Type()
)
wfNetbiosIpRebroadcastTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpRebroadcastTTL.setStatus("mandatory")


class _WfNetbiosIpRebroadcastRecordRoute_Type(Integer32):
    """Custom type wfNetbiosIpRebroadcastRecordRoute based on Integer32"""
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


_WfNetbiosIpRebroadcastRecordRoute_Type.__name__ = "Integer32"
_WfNetbiosIpRebroadcastRecordRoute_Object = MibScalar
wfNetbiosIpRebroadcastRecordRoute = _WfNetbiosIpRebroadcastRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 14),
    _WfNetbiosIpRebroadcastRecordRoute_Type()
)
wfNetbiosIpRebroadcastRecordRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpRebroadcastRecordRoute.setStatus("mandatory")
_WfNetbiosIpInterfaceTable_Object = MibTable
wfNetbiosIpInterfaceTable = _WfNetbiosIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2)
)
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceTable.setStatus("mandatory")
_WfNetbiosIpInterfaceEntry_Object = MibTableRow
wfNetbiosIpInterfaceEntry = _WfNetbiosIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1)
)
wfNetbiosIpInterfaceEntry.setIndexNames(
    (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceEntry.setStatus("mandatory")


class _WfNetbiosIpInterfaceDelete_Type(Integer32):
    """Custom type wfNetbiosIpInterfaceDelete based on Integer32"""
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


_WfNetbiosIpInterfaceDelete_Type.__name__ = "Integer32"
_WfNetbiosIpInterfaceDelete_Object = MibTableColumn
wfNetbiosIpInterfaceDelete = _WfNetbiosIpInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 1),
    _WfNetbiosIpInterfaceDelete_Type()
)
wfNetbiosIpInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceDelete.setStatus("mandatory")


class _WfNetbiosIpInterfaceDisable_Type(Integer32):
    """Custom type wfNetbiosIpInterfaceDisable based on Integer32"""
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


_WfNetbiosIpInterfaceDisable_Type.__name__ = "Integer32"
_WfNetbiosIpInterfaceDisable_Object = MibTableColumn
wfNetbiosIpInterfaceDisable = _WfNetbiosIpInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 2),
    _WfNetbiosIpInterfaceDisable_Type()
)
wfNetbiosIpInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceDisable.setStatus("mandatory")


class _WfNetbiosIpInterfaceState_Type(Integer32):
    """Custom type wfNetbiosIpInterfaceState based on Integer32"""
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
          ("notpres", 4),
          ("up", 1))
    )


_WfNetbiosIpInterfaceState_Type.__name__ = "Integer32"
_WfNetbiosIpInterfaceState_Object = MibTableColumn
wfNetbiosIpInterfaceState = _WfNetbiosIpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 3),
    _WfNetbiosIpInterfaceState_Type()
)
wfNetbiosIpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceState.setStatus("mandatory")
_WfNetbiosIpInterfaceIndex_Type = IpAddress
_WfNetbiosIpInterfaceIndex_Object = MibTableColumn
wfNetbiosIpInterfaceIndex = _WfNetbiosIpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 4),
    _WfNetbiosIpInterfaceIndex_Type()
)
wfNetbiosIpInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceIndex.setStatus("mandatory")
_WfNetbiosIpInterfaceReceivedFrames_Type = Counter32
_WfNetbiosIpInterfaceReceivedFrames_Object = MibTableColumn
wfNetbiosIpInterfaceReceivedFrames = _WfNetbiosIpInterfaceReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 5),
    _WfNetbiosIpInterfaceReceivedFrames_Type()
)
wfNetbiosIpInterfaceReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceReceivedFrames.setStatus("mandatory")
_WfNetbiosIpInterfaceReceivedBadFrames_Type = Counter32
_WfNetbiosIpInterfaceReceivedBadFrames_Object = MibTableColumn
wfNetbiosIpInterfaceReceivedBadFrames = _WfNetbiosIpInterfaceReceivedBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 6),
    _WfNetbiosIpInterfaceReceivedBadFrames_Type()
)
wfNetbiosIpInterfaceReceivedBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceReceivedBadFrames.setStatus("mandatory")
_WfNetbiosIpInterfaceTransmittedFrames_Type = Counter32
_WfNetbiosIpInterfaceTransmittedFrames_Object = MibTableColumn
wfNetbiosIpInterfaceTransmittedFrames = _WfNetbiosIpInterfaceTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 7),
    _WfNetbiosIpInterfaceTransmittedFrames_Type()
)
wfNetbiosIpInterfaceTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceTransmittedFrames.setStatus("mandatory")


class _WfNetbiosIpInterfaceNameCacheDisable_Type(Integer32):
    """Custom type wfNetbiosIpInterfaceNameCacheDisable based on Integer32"""
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


_WfNetbiosIpInterfaceNameCacheDisable_Type.__name__ = "Integer32"
_WfNetbiosIpInterfaceNameCacheDisable_Object = MibTableColumn
wfNetbiosIpInterfaceNameCacheDisable = _WfNetbiosIpInterfaceNameCacheDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 8),
    _WfNetbiosIpInterfaceNameCacheDisable_Type()
)
wfNetbiosIpInterfaceNameCacheDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceNameCacheDisable.setStatus("mandatory")


class _WfNetbiosIpInterfaceInBroadcastDisable_Type(Integer32):
    """Custom type wfNetbiosIpInterfaceInBroadcastDisable based on Integer32"""
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


_WfNetbiosIpInterfaceInBroadcastDisable_Type.__name__ = "Integer32"
_WfNetbiosIpInterfaceInBroadcastDisable_Object = MibTableColumn
wfNetbiosIpInterfaceInBroadcastDisable = _WfNetbiosIpInterfaceInBroadcastDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 9),
    _WfNetbiosIpInterfaceInBroadcastDisable_Type()
)
wfNetbiosIpInterfaceInBroadcastDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceInBroadcastDisable.setStatus("mandatory")


class _WfNetbiosIpInterfaceOutBroadcastDisable_Type(Integer32):
    """Custom type wfNetbiosIpInterfaceOutBroadcastDisable based on Integer32"""
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


_WfNetbiosIpInterfaceOutBroadcastDisable_Type.__name__ = "Integer32"
_WfNetbiosIpInterfaceOutBroadcastDisable_Object = MibTableColumn
wfNetbiosIpInterfaceOutBroadcastDisable = _WfNetbiosIpInterfaceOutBroadcastDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 10),
    _WfNetbiosIpInterfaceOutBroadcastDisable_Type()
)
wfNetbiosIpInterfaceOutBroadcastDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceOutBroadcastDisable.setStatus("mandatory")
_WfNetbiosIpInterfaceRebroadcastAddr_Type = IpAddress
_WfNetbiosIpInterfaceRebroadcastAddr_Object = MibTableColumn
wfNetbiosIpInterfaceRebroadcastAddr = _WfNetbiosIpInterfaceRebroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 11),
    _WfNetbiosIpInterfaceRebroadcastAddr_Type()
)
wfNetbiosIpInterfaceRebroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpInterfaceRebroadcastAddr.setStatus("mandatory")
_WfNetbiosIpNameTable_Object = MibTable
wfNetbiosIpNameTable = _WfNetbiosIpNameTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3)
)
if mibBuilder.loadTexts:
    wfNetbiosIpNameTable.setStatus("mandatory")
_WfNetbiosIpNameEntry_Object = MibTableRow
wfNetbiosIpNameEntry = _WfNetbiosIpNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1)
)
wfNetbiosIpNameEntry.setIndexNames(
    (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpName"),
    (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpAddress"),
    (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpIdNumber"),
)
if mibBuilder.loadTexts:
    wfNetbiosIpNameEntry.setStatus("mandatory")


class _WfNetbiosIpName_Type(OctetString):
    """Custom type wfNetbiosIpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WfNetbiosIpName_Type.__name__ = "OctetString"
_WfNetbiosIpName_Object = MibTableColumn
wfNetbiosIpName = _WfNetbiosIpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 1),
    _WfNetbiosIpName_Type()
)
wfNetbiosIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpName.setStatus("mandatory")
_WfNetbiosIpScopeId_Type = OctetString
_WfNetbiosIpScopeId_Object = MibTableColumn
wfNetbiosIpScopeId = _WfNetbiosIpScopeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 2),
    _WfNetbiosIpScopeId_Type()
)
wfNetbiosIpScopeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpScopeId.setStatus("mandatory")
_WfNetbiosIpAddress_Type = IpAddress
_WfNetbiosIpAddress_Object = MibTableColumn
wfNetbiosIpAddress = _WfNetbiosIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 3),
    _WfNetbiosIpAddress_Type()
)
wfNetbiosIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpAddress.setStatus("mandatory")


class _WfNetbiosIpStatic_Type(Integer32):
    """Custom type wfNetbiosIpStatic based on Integer32"""
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


_WfNetbiosIpStatic_Type.__name__ = "Integer32"
_WfNetbiosIpStatic_Object = MibTableColumn
wfNetbiosIpStatic = _WfNetbiosIpStatic_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 4),
    _WfNetbiosIpStatic_Type()
)
wfNetbiosIpStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpStatic.setStatus("mandatory")
_WfNetbiosIpCacheHits_Type = Counter32
_WfNetbiosIpCacheHits_Object = MibTableColumn
wfNetbiosIpCacheHits = _WfNetbiosIpCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 5),
    _WfNetbiosIpCacheHits_Type()
)
wfNetbiosIpCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpCacheHits.setStatus("mandatory")
_WfNetbiosIpIdNumber_Type = Integer32
_WfNetbiosIpIdNumber_Object = MibTableColumn
wfNetbiosIpIdNumber = _WfNetbiosIpIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 6),
    _WfNetbiosIpIdNumber_Type()
)
wfNetbiosIpIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpIdNumber.setStatus("mandatory")
_WfNetbiosIpStaticTable_Object = MibTable
wfNetbiosIpStaticTable = _WfNetbiosIpStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4)
)
if mibBuilder.loadTexts:
    wfNetbiosIpStaticTable.setStatus("mandatory")
_WfNetbiosIpStaticEntry_Object = MibTableRow
wfNetbiosIpStaticEntry = _WfNetbiosIpStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1)
)
wfNetbiosIpStaticEntry.setIndexNames(
    (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpStaticName"),
    (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpStaticIpAddress"),
    (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpStaticIdNumber"),
)
if mibBuilder.loadTexts:
    wfNetbiosIpStaticEntry.setStatus("mandatory")


class _WfNetbiosIpStaticDelete_Type(Integer32):
    """Custom type wfNetbiosIpStaticDelete based on Integer32"""
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


_WfNetbiosIpStaticDelete_Type.__name__ = "Integer32"
_WfNetbiosIpStaticDelete_Object = MibTableColumn
wfNetbiosIpStaticDelete = _WfNetbiosIpStaticDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 1),
    _WfNetbiosIpStaticDelete_Type()
)
wfNetbiosIpStaticDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpStaticDelete.setStatus("mandatory")


class _WfNetbiosIpStaticDisable_Type(Integer32):
    """Custom type wfNetbiosIpStaticDisable based on Integer32"""
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


_WfNetbiosIpStaticDisable_Type.__name__ = "Integer32"
_WfNetbiosIpStaticDisable_Object = MibTableColumn
wfNetbiosIpStaticDisable = _WfNetbiosIpStaticDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 2),
    _WfNetbiosIpStaticDisable_Type()
)
wfNetbiosIpStaticDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpStaticDisable.setStatus("mandatory")


class _WfNetbiosIpStaticState_Type(Integer32):
    """Custom type wfNetbiosIpStaticState based on Integer32"""
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


_WfNetbiosIpStaticState_Type.__name__ = "Integer32"
_WfNetbiosIpStaticState_Object = MibTableColumn
wfNetbiosIpStaticState = _WfNetbiosIpStaticState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 3),
    _WfNetbiosIpStaticState_Type()
)
wfNetbiosIpStaticState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpStaticState.setStatus("mandatory")


class _WfNetbiosIpStaticName_Type(OctetString):
    """Custom type wfNetbiosIpStaticName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WfNetbiosIpStaticName_Type.__name__ = "OctetString"
_WfNetbiosIpStaticName_Object = MibTableColumn
wfNetbiosIpStaticName = _WfNetbiosIpStaticName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 4),
    _WfNetbiosIpStaticName_Type()
)
wfNetbiosIpStaticName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpStaticName.setStatus("mandatory")
_WfNetbiosIpStaticScopeId_Type = OctetString
_WfNetbiosIpStaticScopeId_Object = MibTableColumn
wfNetbiosIpStaticScopeId = _WfNetbiosIpStaticScopeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 5),
    _WfNetbiosIpStaticScopeId_Type()
)
wfNetbiosIpStaticScopeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbiosIpStaticScopeId.setStatus("mandatory")
_WfNetbiosIpStaticIpAddress_Type = IpAddress
_WfNetbiosIpStaticIpAddress_Object = MibTableColumn
wfNetbiosIpStaticIpAddress = _WfNetbiosIpStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 6),
    _WfNetbiosIpStaticIpAddress_Type()
)
wfNetbiosIpStaticIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpStaticIpAddress.setStatus("mandatory")
_WfNetbiosIpStaticIdNumber_Type = Integer32
_WfNetbiosIpStaticIdNumber_Object = MibTableColumn
wfNetbiosIpStaticIdNumber = _WfNetbiosIpStaticIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 7),
    _WfNetbiosIpStaticIdNumber_Type()
)
wfNetbiosIpStaticIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbiosIpStaticIdNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-NBIP-MIB",
    **{"wfNetbiosIp": wfNetbiosIp,
       "wfNetbiosIpDelete": wfNetbiosIpDelete,
       "wfNetbiosIpDisable": wfNetbiosIpDisable,
       "wfNetbiosIpState": wfNetbiosIpState,
       "wfNetbiosIpNameCacheDisable": wfNetbiosIpNameCacheDisable,
       "wfNetbiosIp15CharacterDisable": wfNetbiosIp15CharacterDisable,
       "wfNetbiosIpNameCacheMibDisable": wfNetbiosIpNameCacheMibDisable,
       "wfNetbiosIpNameCacheMaximumEntries": wfNetbiosIpNameCacheMaximumEntries,
       "wfNetbiosIpNameCacheCurrentEntries": wfNetbiosIpNameCacheCurrentEntries,
       "wfNetbiosIpNameCacheAgeTime": wfNetbiosIpNameCacheAgeTime,
       "wfNetbiosIpNameCacheHashEntries": wfNetbiosIpNameCacheHashEntries,
       "wfNetbiosIpNameCacheHits": wfNetbiosIpNameCacheHits,
       "wfNetbiosIpNameCacheMisses": wfNetbiosIpNameCacheMisses,
       "wfNetbiosIpRebroadcastTTL": wfNetbiosIpRebroadcastTTL,
       "wfNetbiosIpRebroadcastRecordRoute": wfNetbiosIpRebroadcastRecordRoute,
       "wfNetbiosIpInterfaceTable": wfNetbiosIpInterfaceTable,
       "wfNetbiosIpInterfaceEntry": wfNetbiosIpInterfaceEntry,
       "wfNetbiosIpInterfaceDelete": wfNetbiosIpInterfaceDelete,
       "wfNetbiosIpInterfaceDisable": wfNetbiosIpInterfaceDisable,
       "wfNetbiosIpInterfaceState": wfNetbiosIpInterfaceState,
       "wfNetbiosIpInterfaceIndex": wfNetbiosIpInterfaceIndex,
       "wfNetbiosIpInterfaceReceivedFrames": wfNetbiosIpInterfaceReceivedFrames,
       "wfNetbiosIpInterfaceReceivedBadFrames": wfNetbiosIpInterfaceReceivedBadFrames,
       "wfNetbiosIpInterfaceTransmittedFrames": wfNetbiosIpInterfaceTransmittedFrames,
       "wfNetbiosIpInterfaceNameCacheDisable": wfNetbiosIpInterfaceNameCacheDisable,
       "wfNetbiosIpInterfaceInBroadcastDisable": wfNetbiosIpInterfaceInBroadcastDisable,
       "wfNetbiosIpInterfaceOutBroadcastDisable": wfNetbiosIpInterfaceOutBroadcastDisable,
       "wfNetbiosIpInterfaceRebroadcastAddr": wfNetbiosIpInterfaceRebroadcastAddr,
       "wfNetbiosIpNameTable": wfNetbiosIpNameTable,
       "wfNetbiosIpNameEntry": wfNetbiosIpNameEntry,
       "wfNetbiosIpName": wfNetbiosIpName,
       "wfNetbiosIpScopeId": wfNetbiosIpScopeId,
       "wfNetbiosIpAddress": wfNetbiosIpAddress,
       "wfNetbiosIpStatic": wfNetbiosIpStatic,
       "wfNetbiosIpCacheHits": wfNetbiosIpCacheHits,
       "wfNetbiosIpIdNumber": wfNetbiosIpIdNumber,
       "wfNetbiosIpStaticTable": wfNetbiosIpStaticTable,
       "wfNetbiosIpStaticEntry": wfNetbiosIpStaticEntry,
       "wfNetbiosIpStaticDelete": wfNetbiosIpStaticDelete,
       "wfNetbiosIpStaticDisable": wfNetbiosIpStaticDisable,
       "wfNetbiosIpStaticState": wfNetbiosIpStaticState,
       "wfNetbiosIpStaticName": wfNetbiosIpStaticName,
       "wfNetbiosIpStaticScopeId": wfNetbiosIpStaticScopeId,
       "wfNetbiosIpStaticIpAddress": wfNetbiosIpStaticIpAddress,
       "wfNetbiosIpStaticIdNumber": wfNetbiosIpStaticIdNumber}
)
