# SNMP MIB module (ALCATEL-IND1-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:44 2024
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

(routingIND1Bgp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Bgp")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1BGPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1BGPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1BGPMIBObjects = _AlcatelIND1BGPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1BGPMIBObjects.setStatus("current")
_AlaBgpGlobal_ObjectIdentity = ObjectIdentity
alaBgpGlobal = _AlaBgpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1)
)


class _AlaBgpProtoStatus_Type(Integer32):
    """Custom type alaBgpProtoStatus based on Integer32"""
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


_AlaBgpProtoStatus_Type.__name__ = "Integer32"
_AlaBgpProtoStatus_Object = MibScalar
alaBgpProtoStatus = _AlaBgpProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 1),
    _AlaBgpProtoStatus_Type()
)
alaBgpProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpProtoStatus.setStatus("current")


class _AlaBgpAutonomousSystemNumber_Type(Integer32):
    """Custom type alaBgpAutonomousSystemNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaBgpAutonomousSystemNumber_Type.__name__ = "Integer32"
_AlaBgpAutonomousSystemNumber_Object = MibScalar
alaBgpAutonomousSystemNumber = _AlaBgpAutonomousSystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 2),
    _AlaBgpAutonomousSystemNumber_Type()
)
alaBgpAutonomousSystemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpAutonomousSystemNumber.setStatus("current")


class _AlaBgpRouterId_Type(IpAddress):
    """Custom type alaBgpRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_AlaBgpRouterId_Object = MibScalar
alaBgpRouterId = _AlaBgpRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 3),
    _AlaBgpRouterId_Type()
)
alaBgpRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouterId.setStatus("current")


class _AlaBgpIgpSynchStatus_Type(Integer32):
    """Custom type alaBgpIgpSynchStatus based on Integer32"""
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


_AlaBgpIgpSynchStatus_Type.__name__ = "Integer32"
_AlaBgpIgpSynchStatus_Object = MibScalar
alaBgpIgpSynchStatus = _AlaBgpIgpSynchStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 4),
    _AlaBgpIgpSynchStatus_Type()
)
alaBgpIgpSynchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpIgpSynchStatus.setStatus("current")


class _AlaBgpMedAlways_Type(Integer32):
    """Custom type alaBgpMedAlways based on Integer32"""
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


_AlaBgpMedAlways_Type.__name__ = "Integer32"
_AlaBgpMedAlways_Object = MibScalar
alaBgpMedAlways = _AlaBgpMedAlways_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 5),
    _AlaBgpMedAlways_Type()
)
alaBgpMedAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpMedAlways.setStatus("current")


class _AlaBgpDefaultLocalPref_Type(Gauge32):
    """Custom type alaBgpDefaultLocalPref based on Gauge32"""
    defaultValue = 100

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpDefaultLocalPref_Type.__name__ = "Gauge32"
_AlaBgpDefaultLocalPref_Object = MibScalar
alaBgpDefaultLocalPref = _AlaBgpDefaultLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 6),
    _AlaBgpDefaultLocalPref_Type()
)
alaBgpDefaultLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDefaultLocalPref.setStatus("current")


class _AlaBgpMissingMed_Type(Integer32):
    """Custom type alaBgpMissingMed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("best", 2),
          ("worst", 1))
    )


_AlaBgpMissingMed_Type.__name__ = "Integer32"
_AlaBgpMissingMed_Object = MibScalar
alaBgpMissingMed = _AlaBgpMissingMed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 7),
    _AlaBgpMissingMed_Type()
)
alaBgpMissingMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpMissingMed.setStatus("current")


class _AlaBgpManualTag_Type(Gauge32):
    """Custom type alaBgpManualTag based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpManualTag_Type.__name__ = "Gauge32"
_AlaBgpManualTag_Object = MibScalar
alaBgpManualTag = _AlaBgpManualTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 8),
    _AlaBgpManualTag_Type()
)
alaBgpManualTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpManualTag.setStatus("current")


class _AlaBgpPromiscuousNeighbours_Type(Integer32):
    """Custom type alaBgpPromiscuousNeighbours based on Integer32"""
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


_AlaBgpPromiscuousNeighbours_Type.__name__ = "Integer32"
_AlaBgpPromiscuousNeighbours_Object = MibScalar
alaBgpPromiscuousNeighbours = _AlaBgpPromiscuousNeighbours_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 9),
    _AlaBgpPromiscuousNeighbours_Type()
)
alaBgpPromiscuousNeighbours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPromiscuousNeighbours.setStatus("deprecated")


class _AlaBgpConfedId_Type(Integer32):
    """Custom type alaBgpConfedId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpConfedId_Type.__name__ = "Integer32"
_AlaBgpConfedId_Object = MibScalar
alaBgpConfedId = _AlaBgpConfedId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 10),
    _AlaBgpConfedId_Type()
)
alaBgpConfedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpConfedId.setStatus("current")


class _AlaBgpDampening_Type(Integer32):
    """Custom type alaBgpDampening based on Integer32"""
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


_AlaBgpDampening_Type.__name__ = "Integer32"
_AlaBgpDampening_Object = MibScalar
alaBgpDampening = _AlaBgpDampening_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 11),
    _AlaBgpDampening_Type()
)
alaBgpDampening.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDampening.setStatus("current")


class _AlaBgpDampHalfLifeReach_Type(Integer32):
    """Custom type alaBgpDampHalfLifeReach based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpDampHalfLifeReach_Type.__name__ = "Integer32"
_AlaBgpDampHalfLifeReach_Object = MibScalar
alaBgpDampHalfLifeReach = _AlaBgpDampHalfLifeReach_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 12),
    _AlaBgpDampHalfLifeReach_Type()
)
alaBgpDampHalfLifeReach.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBgpDampHalfLifeReach.setStatus("deprecated")


class _AlaBgpDampHalfLifeUnReach_Type(Integer32):
    """Custom type alaBgpDampHalfLifeUnReach based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpDampHalfLifeUnReach_Type.__name__ = "Integer32"
_AlaBgpDampHalfLifeUnReach_Object = MibScalar
alaBgpDampHalfLifeUnReach = _AlaBgpDampHalfLifeUnReach_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 13),
    _AlaBgpDampHalfLifeUnReach_Type()
)
alaBgpDampHalfLifeUnReach.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBgpDampHalfLifeUnReach.setStatus("deprecated")


class _AlaBgpDampMaxFlapHistory_Type(Integer32):
    """Custom type alaBgpDampMaxFlapHistory based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpDampMaxFlapHistory_Type.__name__ = "Integer32"
_AlaBgpDampMaxFlapHistory_Object = MibScalar
alaBgpDampMaxFlapHistory = _AlaBgpDampMaxFlapHistory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 14),
    _AlaBgpDampMaxFlapHistory_Type()
)
alaBgpDampMaxFlapHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDampMaxFlapHistory.setStatus("current")


class _AlaBgpDebugLevel_Type(Integer32):
    """Custom type alaBgpDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaBgpDebugLevel_Type.__name__ = "Integer32"
_AlaBgpDebugLevel_Object = MibScalar
alaBgpDebugLevel = _AlaBgpDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 15),
    _AlaBgpDebugLevel_Type()
)
alaBgpDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDebugLevel.setStatus("deprecated")


class _AlaBgpFastExternalFailOver_Type(Integer32):
    """Custom type alaBgpFastExternalFailOver based on Integer32"""
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


_AlaBgpFastExternalFailOver_Type.__name__ = "Integer32"
_AlaBgpFastExternalFailOver_Object = MibScalar
alaBgpFastExternalFailOver = _AlaBgpFastExternalFailOver_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 16),
    _AlaBgpFastExternalFailOver_Type()
)
alaBgpFastExternalFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpFastExternalFailOver.setStatus("current")


class _AlaBgpPeerChanges_Type(Integer32):
    """Custom type alaBgpPeerChanges based on Integer32"""
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


_AlaBgpPeerChanges_Type.__name__ = "Integer32"
_AlaBgpPeerChanges_Object = MibScalar
alaBgpPeerChanges = _AlaBgpPeerChanges_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 17),
    _AlaBgpPeerChanges_Type()
)
alaBgpPeerChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeerChanges.setStatus("current")


class _AlaBgpVersion_Type(Integer32):
    """Custom type alaBgpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaBgpVersion_Type.__name__ = "Integer32"
_AlaBgpVersion_Object = MibScalar
alaBgpVersion = _AlaBgpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 18),
    _AlaBgpVersion_Type()
)
alaBgpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpVersion.setStatus("current")


class _AlaBgpProtoOperState_Type(Integer32):
    """Custom type alaBgpProtoOperState based on Integer32"""
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


_AlaBgpProtoOperState_Type.__name__ = "Integer32"
_AlaBgpProtoOperState_Object = MibScalar
alaBgpProtoOperState = _AlaBgpProtoOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 19),
    _AlaBgpProtoOperState_Type()
)
alaBgpProtoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpProtoOperState.setStatus("current")


class _AlaBgpMaxPeers_Type(Integer32):
    """Custom type alaBgpMaxPeers based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AlaBgpMaxPeers_Type.__name__ = "Integer32"
_AlaBgpMaxPeers_Object = MibScalar
alaBgpMaxPeers = _AlaBgpMaxPeers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 20),
    _AlaBgpMaxPeers_Type()
)
alaBgpMaxPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpMaxPeers.setStatus("current")
_AlaBgpNumActiveRoutes_Type = Gauge32
_AlaBgpNumActiveRoutes_Object = MibScalar
alaBgpNumActiveRoutes = _AlaBgpNumActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 21),
    _AlaBgpNumActiveRoutes_Type()
)
alaBgpNumActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNumActiveRoutes.setStatus("current")
_AlaBgpNumEstabExternalPeers_Type = Counter32
_AlaBgpNumEstabExternalPeers_Object = MibScalar
alaBgpNumEstabExternalPeers = _AlaBgpNumEstabExternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 22),
    _AlaBgpNumEstabExternalPeers_Type()
)
alaBgpNumEstabExternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNumEstabExternalPeers.setStatus("current")
_AlaBgpNumEstabInternalPeers_Type = Counter32
_AlaBgpNumEstabInternalPeers_Object = MibScalar
alaBgpNumEstabInternalPeers = _AlaBgpNumEstabInternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 23),
    _AlaBgpNumEstabInternalPeers_Type()
)
alaBgpNumEstabInternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNumEstabInternalPeers.setStatus("current")
_AlaBgpNumPaths_Type = Counter32
_AlaBgpNumPaths_Object = MibScalar
alaBgpNumPaths = _AlaBgpNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 24),
    _AlaBgpNumPaths_Type()
)
alaBgpNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNumPaths.setStatus("current")
_AlaBgpNumFeasiblePaths_Type = Counter32
_AlaBgpNumFeasiblePaths_Object = MibScalar
alaBgpNumFeasiblePaths = _AlaBgpNumFeasiblePaths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 25),
    _AlaBgpNumFeasiblePaths_Type()
)
alaBgpNumFeasiblePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNumFeasiblePaths.setStatus("current")
_AlaBgpNumDampenedPaths_Type = Counter32
_AlaBgpNumDampenedPaths_Object = MibScalar
alaBgpNumDampenedPaths = _AlaBgpNumDampenedPaths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 26),
    _AlaBgpNumDampenedPaths_Type()
)
alaBgpNumDampenedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNumDampenedPaths.setStatus("current")
_AlaBgpNumIgpSyncWaitPaths_Type = Counter32
_AlaBgpNumIgpSyncWaitPaths_Object = MibScalar
alaBgpNumIgpSyncWaitPaths = _AlaBgpNumIgpSyncWaitPaths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 27),
    _AlaBgpNumIgpSyncWaitPaths_Type()
)
alaBgpNumIgpSyncWaitPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNumIgpSyncWaitPaths.setStatus("current")
_AlaBgpNumPolicyChgPaths_Type = Counter32
_AlaBgpNumPolicyChgPaths_Object = MibScalar
alaBgpNumPolicyChgPaths = _AlaBgpNumPolicyChgPaths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 28),
    _AlaBgpNumPolicyChgPaths_Type()
)
alaBgpNumPolicyChgPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNumPolicyChgPaths.setStatus("current")


class _AlaBgpMultiPath_Type(Integer32):
    """Custom type alaBgpMultiPath based on Integer32"""
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


_AlaBgpMultiPath_Type.__name__ = "Integer32"
_AlaBgpMultiPath_Object = MibScalar
alaBgpMultiPath = _AlaBgpMultiPath_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 29),
    _AlaBgpMultiPath_Type()
)
alaBgpMultiPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpMultiPath.setStatus("current")


class _AlaBgpRouteReflection_Type(Integer32):
    """Custom type alaBgpRouteReflection based on Integer32"""
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


_AlaBgpRouteReflection_Type.__name__ = "Integer32"
_AlaBgpRouteReflection_Object = MibScalar
alaBgpRouteReflection = _AlaBgpRouteReflection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 30),
    _AlaBgpRouteReflection_Type()
)
alaBgpRouteReflection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteReflection.setStatus("current")


class _AlaBgpClusterId_Type(IpAddress):
    """Custom type alaBgpClusterId based on IpAddress"""
    defaultHexValue = "00000000"


_AlaBgpClusterId_Object = MibScalar
alaBgpClusterId = _AlaBgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 31),
    _AlaBgpClusterId_Type()
)
alaBgpClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpClusterId.setStatus("current")


class _AlaBgpDampeningClear_Type(Integer32):
    """Custom type alaBgpDampeningClear based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaBgpDampeningClear_Type.__name__ = "Integer32"
_AlaBgpDampeningClear_Object = MibScalar
alaBgpDampeningClear = _AlaBgpDampeningClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 32),
    _AlaBgpDampeningClear_Type()
)
alaBgpDampeningClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDampeningClear.setStatus("current")


class _AlaBgpDampCutOff_Type(Integer32):
    """Custom type alaBgpDampCutOff based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AlaBgpDampCutOff_Type.__name__ = "Integer32"
_AlaBgpDampCutOff_Object = MibScalar
alaBgpDampCutOff = _AlaBgpDampCutOff_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 33),
    _AlaBgpDampCutOff_Type()
)
alaBgpDampCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDampCutOff.setStatus("current")


class _AlaBgpDampReuse_Type(Integer32):
    """Custom type alaBgpDampReuse based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AlaBgpDampReuse_Type.__name__ = "Integer32"
_AlaBgpDampReuse_Object = MibScalar
alaBgpDampReuse = _AlaBgpDampReuse_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 34),
    _AlaBgpDampReuse_Type()
)
alaBgpDampReuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDampReuse.setStatus("current")


class _AlaBgpDampCeil_Type(Integer32):
    """Custom type alaBgpDampCeil based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9999),
    )


_AlaBgpDampCeil_Type.__name__ = "Integer32"
_AlaBgpDampCeil_Object = MibScalar
alaBgpDampCeil = _AlaBgpDampCeil_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 35),
    _AlaBgpDampCeil_Type()
)
alaBgpDampCeil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampCeil.setStatus("current")


class _AlaBgpAspathCompare_Type(Integer32):
    """Custom type alaBgpAspathCompare based on Integer32"""
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


_AlaBgpAspathCompare_Type.__name__ = "Integer32"
_AlaBgpAspathCompare_Object = MibScalar
alaBgpAspathCompare = _AlaBgpAspathCompare_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 36),
    _AlaBgpAspathCompare_Type()
)
alaBgpAspathCompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpAspathCompare.setStatus("current")


class _AlaBgpAsOriginInterval_Type(Integer32):
    """Custom type alaBgpAsOriginInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaBgpAsOriginInterval_Type.__name__ = "Integer32"
_AlaBgpAsOriginInterval_Object = MibScalar
alaBgpAsOriginInterval = _AlaBgpAsOriginInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 37),
    _AlaBgpAsOriginInterval_Type()
)
alaBgpAsOriginInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpAsOriginInterval.setStatus("current")


class _AlaBgpDampHalfLife_Type(Integer32):
    """Custom type alaBgpDampHalfLife based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpDampHalfLife_Type.__name__ = "Integer32"
_AlaBgpDampHalfLife_Object = MibScalar
alaBgpDampHalfLife = _AlaBgpDampHalfLife_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 38),
    _AlaBgpDampHalfLife_Type()
)
alaBgpDampHalfLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDampHalfLife.setStatus("current")


class _AlaBgpGracefulRestart_Type(Integer32):
    """Custom type alaBgpGracefulRestart based on Integer32"""
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


_AlaBgpGracefulRestart_Type.__name__ = "Integer32"
_AlaBgpGracefulRestart_Object = MibScalar
alaBgpGracefulRestart = _AlaBgpGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 39),
    _AlaBgpGracefulRestart_Type()
)
alaBgpGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpGracefulRestart.setStatus("current")


class _AlaBgpRestartInterval_Type(Integer32):
    """Custom type alaBgpRestartInterval based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlaBgpRestartInterval_Type.__name__ = "Integer32"
_AlaBgpRestartInterval_Object = MibScalar
alaBgpRestartInterval = _AlaBgpRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 40),
    _AlaBgpRestartInterval_Type()
)
alaBgpRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRestartInterval.setStatus("current")


class _AlaBgpRestartStatus_Type(Integer32):
    """Custom type alaBgpRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 2),
          ("notRestarting", 1))
    )


_AlaBgpRestartStatus_Type.__name__ = "Integer32"
_AlaBgpRestartStatus_Object = MibScalar
alaBgpRestartStatus = _AlaBgpRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 41),
    _AlaBgpRestartStatus_Type()
)
alaBgpRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRestartStatus.setStatus("current")


class _AlaBgpMultiProtocolIpv4_Type(Integer32):
    """Custom type alaBgpMultiProtocolIpv4 based on Integer32"""
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


_AlaBgpMultiProtocolIpv4_Type.__name__ = "Integer32"
_AlaBgpMultiProtocolIpv4_Object = MibScalar
alaBgpMultiProtocolIpv4 = _AlaBgpMultiProtocolIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 42),
    _AlaBgpMultiProtocolIpv4_Type()
)
alaBgpMultiProtocolIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpMultiProtocolIpv4.setStatus("current")


class _AlaBgpMultiProtocolIpv6_Type(Integer32):
    """Custom type alaBgpMultiProtocolIpv6 based on Integer32"""
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


_AlaBgpMultiProtocolIpv6_Type.__name__ = "Integer32"
_AlaBgpMultiProtocolIpv6_Object = MibScalar
alaBgpMultiProtocolIpv6 = _AlaBgpMultiProtocolIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 43),
    _AlaBgpMultiProtocolIpv6_Type()
)
alaBgpMultiProtocolIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpMultiProtocolIpv6.setStatus("current")


class _AlaBgpBfdStatus_Type(Integer32):
    """Custom type alaBgpBfdStatus based on Integer32"""
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


_AlaBgpBfdStatus_Type.__name__ = "Integer32"
_AlaBgpBfdStatus_Object = MibScalar
alaBgpBfdStatus = _AlaBgpBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 44),
    _AlaBgpBfdStatus_Type()
)
alaBgpBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpBfdStatus.setStatus("current")


class _AlaBgpBfdAllNeighborStatus_Type(Integer32):
    """Custom type alaBgpBfdAllNeighborStatus based on Integer32"""
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


_AlaBgpBfdAllNeighborStatus_Type.__name__ = "Integer32"
_AlaBgpBfdAllNeighborStatus_Object = MibScalar
alaBgpBfdAllNeighborStatus = _AlaBgpBfdAllNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 1, 45),
    _AlaBgpBfdAllNeighborStatus_Type()
)
alaBgpBfdAllNeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpBfdAllNeighborStatus.setStatus("current")
_AlaBgpPeerTable_Object = MibTable
alaBgpPeerTable = _AlaBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaBgpPeerTable.setStatus("current")
_AlaBgpPeerEntry_Object = MibTableRow
alaBgpPeerEntry = _AlaBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1)
)
alaBgpPeerEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPeerAddr"),
)
if mibBuilder.loadTexts:
    alaBgpPeerEntry.setStatus("current")
_AlaBgpPeerAddr_Type = IpAddress
_AlaBgpPeerAddr_Object = MibTableColumn
alaBgpPeerAddr = _AlaBgpPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 1),
    _AlaBgpPeerAddr_Type()
)
alaBgpPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerAddr.setStatus("current")


class _AlaBgpPeerAS_Type(Integer32):
    """Custom type alaBgpPeerAS based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaBgpPeerAS_Type.__name__ = "Integer32"
_AlaBgpPeerAS_Object = MibTableColumn
alaBgpPeerAS = _AlaBgpPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 2),
    _AlaBgpPeerAS_Type()
)
alaBgpPeerAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerAS.setStatus("current")


class _AlaBgpPeerPassive_Type(Integer32):
    """Custom type alaBgpPeerPassive based on Integer32"""
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


_AlaBgpPeerPassive_Type.__name__ = "Integer32"
_AlaBgpPeerPassive_Object = MibTableColumn
alaBgpPeerPassive = _AlaBgpPeerPassive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 3),
    _AlaBgpPeerPassive_Type()
)
alaBgpPeerPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerPassive.setStatus("current")


class _AlaBgpPeerName_Type(DisplayString):
    """Custom type alaBgpPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AlaBgpPeerName_Type.__name__ = "DisplayString"
_AlaBgpPeerName_Object = MibTableColumn
alaBgpPeerName = _AlaBgpPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 4),
    _AlaBgpPeerName_Type()
)
alaBgpPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerName.setStatus("current")


class _AlaBgpPeerMultiHop_Type(Integer32):
    """Custom type alaBgpPeerMultiHop based on Integer32"""
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


_AlaBgpPeerMultiHop_Type.__name__ = "Integer32"
_AlaBgpPeerMultiHop_Object = MibTableColumn
alaBgpPeerMultiHop = _AlaBgpPeerMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 5),
    _AlaBgpPeerMultiHop_Type()
)
alaBgpPeerMultiHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerMultiHop.setStatus("current")


class _AlaBgpPeerMaxPrefix_Type(Gauge32):
    """Custom type alaBgpPeerMaxPrefix based on Gauge32"""
    defaultValue = 5000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaBgpPeerMaxPrefix_Type.__name__ = "Gauge32"
_AlaBgpPeerMaxPrefix_Object = MibTableColumn
alaBgpPeerMaxPrefix = _AlaBgpPeerMaxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 6),
    _AlaBgpPeerMaxPrefix_Type()
)
alaBgpPeerMaxPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerMaxPrefix.setStatus("current")


class _AlaBgpPeerMaxPrefixWarnOnly_Type(Integer32):
    """Custom type alaBgpPeerMaxPrefixWarnOnly based on Integer32"""
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


_AlaBgpPeerMaxPrefixWarnOnly_Type.__name__ = "Integer32"
_AlaBgpPeerMaxPrefixWarnOnly_Object = MibTableColumn
alaBgpPeerMaxPrefixWarnOnly = _AlaBgpPeerMaxPrefixWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 7),
    _AlaBgpPeerMaxPrefixWarnOnly_Type()
)
alaBgpPeerMaxPrefixWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerMaxPrefixWarnOnly.setStatus("current")


class _AlaBgpPeerNextHopSelf_Type(Integer32):
    """Custom type alaBgpPeerNextHopSelf based on Integer32"""
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


_AlaBgpPeerNextHopSelf_Type.__name__ = "Integer32"
_AlaBgpPeerNextHopSelf_Object = MibTableColumn
alaBgpPeerNextHopSelf = _AlaBgpPeerNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 8),
    _AlaBgpPeerNextHopSelf_Type()
)
alaBgpPeerNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerNextHopSelf.setStatus("current")


class _AlaBgpPeerSoftReconfig_Type(Integer32):
    """Custom type alaBgpPeerSoftReconfig based on Integer32"""
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


_AlaBgpPeerSoftReconfig_Type.__name__ = "Integer32"
_AlaBgpPeerSoftReconfig_Object = MibTableColumn
alaBgpPeerSoftReconfig = _AlaBgpPeerSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 9),
    _AlaBgpPeerSoftReconfig_Type()
)
alaBgpPeerSoftReconfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerSoftReconfig.setStatus("current")


class _AlaBgpPeerInSoftReset_Type(Integer32):
    """Custom type alaBgpPeerInSoftReset based on Integer32"""
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


_AlaBgpPeerInSoftReset_Type.__name__ = "Integer32"
_AlaBgpPeerInSoftReset_Object = MibTableColumn
alaBgpPeerInSoftReset = _AlaBgpPeerInSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 10),
    _AlaBgpPeerInSoftReset_Type()
)
alaBgpPeerInSoftReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerInSoftReset.setStatus("current")


class _AlaBgpPeerIpv4Unicast_Type(Integer32):
    """Custom type alaBgpPeerIpv4Unicast based on Integer32"""
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


_AlaBgpPeerIpv4Unicast_Type.__name__ = "Integer32"
_AlaBgpPeerIpv4Unicast_Object = MibTableColumn
alaBgpPeerIpv4Unicast = _AlaBgpPeerIpv4Unicast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 11),
    _AlaBgpPeerIpv4Unicast_Type()
)
alaBgpPeerIpv4Unicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerIpv4Unicast.setStatus("current")


class _AlaBgpPeerIpv4Multicast_Type(Integer32):
    """Custom type alaBgpPeerIpv4Multicast based on Integer32"""
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


_AlaBgpPeerIpv4Multicast_Type.__name__ = "Integer32"
_AlaBgpPeerIpv4Multicast_Object = MibTableColumn
alaBgpPeerIpv4Multicast = _AlaBgpPeerIpv4Multicast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 12),
    _AlaBgpPeerIpv4Multicast_Type()
)
alaBgpPeerIpv4Multicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerIpv4Multicast.setStatus("current")
_AlaBgpPeerRcvdRtRefreshMsgs_Type = Counter32
_AlaBgpPeerRcvdRtRefreshMsgs_Object = MibTableColumn
alaBgpPeerRcvdRtRefreshMsgs = _AlaBgpPeerRcvdRtRefreshMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 13),
    _AlaBgpPeerRcvdRtRefreshMsgs_Type()
)
alaBgpPeerRcvdRtRefreshMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerRcvdRtRefreshMsgs.setStatus("current")
_AlaBgpPeerSentRtRefreshMsgs_Type = Counter32
_AlaBgpPeerSentRtRefreshMsgs_Object = MibTableColumn
alaBgpPeerSentRtRefreshMsgs = _AlaBgpPeerSentRtRefreshMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 14),
    _AlaBgpPeerSentRtRefreshMsgs_Type()
)
alaBgpPeerSentRtRefreshMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerSentRtRefreshMsgs.setStatus("current")


class _AlaBgpPeerRouteMapOut_Type(DisplayString):
    """Custom type alaBgpPeerRouteMapOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerRouteMapOut_Type.__name__ = "DisplayString"
_AlaBgpPeerRouteMapOut_Object = MibTableColumn
alaBgpPeerRouteMapOut = _AlaBgpPeerRouteMapOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 15),
    _AlaBgpPeerRouteMapOut_Type()
)
alaBgpPeerRouteMapOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerRouteMapOut.setStatus("current")


class _AlaBgpPeerRouteMapIn_Type(DisplayString):
    """Custom type alaBgpPeerRouteMapIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerRouteMapIn_Type.__name__ = "DisplayString"
_AlaBgpPeerRouteMapIn_Object = MibTableColumn
alaBgpPeerRouteMapIn = _AlaBgpPeerRouteMapIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 16),
    _AlaBgpPeerRouteMapIn_Type()
)
alaBgpPeerRouteMapIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerRouteMapIn.setStatus("current")


class _AlaBgpPeerLocalAddr_Type(IpAddress):
    """Custom type alaBgpPeerLocalAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaBgpPeerLocalAddr_Object = MibTableColumn
alaBgpPeerLocalAddr = _AlaBgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 17),
    _AlaBgpPeerLocalAddr_Type()
)
alaBgpPeerLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerLocalAddr.setStatus("current")


class _AlaBgpPeerLastDownReason_Type(Integer32):
    """Custom type alaBgpPeerLastDownReason based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("badMsg", 4),
          ("connectionTimeout", 2),
          ("fsmUnexpectedEvent", 5),
          ("holdTimeout", 3),
          ("none", 9),
          ("peerClosed", 6),
          ("peerNotify", 7),
          ("transportError", 8),
          ("userRequest", 1))
    )


_AlaBgpPeerLastDownReason_Type.__name__ = "Integer32"
_AlaBgpPeerLastDownReason_Object = MibTableColumn
alaBgpPeerLastDownReason = _AlaBgpPeerLastDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 18),
    _AlaBgpPeerLastDownReason_Type()
)
alaBgpPeerLastDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLastDownReason.setStatus("current")
_AlaBgpPeerLastDownTime_Type = TimeTicks
_AlaBgpPeerLastDownTime_Object = MibTableColumn
alaBgpPeerLastDownTime = _AlaBgpPeerLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 19),
    _AlaBgpPeerLastDownTime_Type()
)
alaBgpPeerLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLastDownTime.setStatus("current")
_AlaBgpPeerLastReadTime_Type = TimeTicks
_AlaBgpPeerLastReadTime_Object = MibTableColumn
alaBgpPeerLastReadTime = _AlaBgpPeerLastReadTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 20),
    _AlaBgpPeerLastReadTime_Type()
)
alaBgpPeerLastReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLastReadTime.setStatus("current")
_AlaBgpPeerRcvdNotifyMsgs_Type = Counter32
_AlaBgpPeerRcvdNotifyMsgs_Object = MibTableColumn
alaBgpPeerRcvdNotifyMsgs = _AlaBgpPeerRcvdNotifyMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 21),
    _AlaBgpPeerRcvdNotifyMsgs_Type()
)
alaBgpPeerRcvdNotifyMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerRcvdNotifyMsgs.setStatus("current")
_AlaBgpPeerSentNotifyMsgs_Type = Counter32
_AlaBgpPeerSentNotifyMsgs_Object = MibTableColumn
alaBgpPeerSentNotifyMsgs = _AlaBgpPeerSentNotifyMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 22),
    _AlaBgpPeerSentNotifyMsgs_Type()
)
alaBgpPeerSentNotifyMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerSentNotifyMsgs.setStatus("current")


class _AlaBgpPeerLastSentNotifyReason_Type(Integer32):
    """Custom type alaBgpPeerLastSentNotifyReason based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("ceaseAdminReset", 27),
          ("ceaseAdminShutdown", 25),
          ("ceaseConnCollisionResolution", 30),
          ("ceaseConnRejected", 28),
          ("ceaseMaxPrefixReached", 24),
          ("ceaseOtherConfChange", 29),
          ("ceaseOutOfResources", 31),
          ("ceasePeerDeconfigured", 26),
          ("fsmError", 23),
          ("holdTimeout", 22),
          ("msghdrBadLen", 2),
          ("msghdrBadType", 3),
          ("msghdrNoSync", 1),
          ("none", 32),
          ("openAuthFail", 8),
          ("openBadAs", 5),
          ("openBadHoldtime", 9),
          ("openBadId", 6),
          ("openUnsuppCapability", 10),
          ("openUnsuppOption", 7),
          ("openUnsuppVersion", 4),
          ("updateAsLoop", 17),
          ("updateBadAspath", 21),
          ("updateBadAttrFlags", 14),
          ("updateBadAttrLen", 15),
          ("updateBadNet", 20),
          ("updateBadNexthop", 18),
          ("updateBadOptAttr", 19),
          ("updateBadOrigin", 16),
          ("updateMalformAttr", 11),
          ("updateMissingWknwnAttr", 13),
          ("updateUnsuppWknwnAttr", 12))
    )


_AlaBgpPeerLastSentNotifyReason_Type.__name__ = "Integer32"
_AlaBgpPeerLastSentNotifyReason_Object = MibTableColumn
alaBgpPeerLastSentNotifyReason = _AlaBgpPeerLastSentNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 23),
    _AlaBgpPeerLastSentNotifyReason_Type()
)
alaBgpPeerLastSentNotifyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLastSentNotifyReason.setStatus("current")


class _AlaBgpPeerLastRecvNotifyReason_Type(Integer32):
    """Custom type alaBgpPeerLastRecvNotifyReason based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("ceaseAdminReset", 27),
          ("ceaseAdminShutdown", 25),
          ("ceaseConnCollisionResolution", 30),
          ("ceaseConnRejected", 28),
          ("ceaseMaxPrefixReached", 24),
          ("ceaseOtherConfChange", 29),
          ("ceaseOutOfResources", 31),
          ("ceasePeerDeconfigured", 26),
          ("fsmError", 23),
          ("holdTimeout", 22),
          ("msghdrBadLen", 2),
          ("msghdrBadType", 3),
          ("msghdrNoSync", 1),
          ("none", 32),
          ("openAuthFail", 8),
          ("openBadAs", 5),
          ("openBadHoldtime", 9),
          ("openBadId", 6),
          ("openUnsuppCapability", 10),
          ("openUnsuppOption", 7),
          ("openUnsuppVersion", 4),
          ("updateAsLoop", 17),
          ("updateBadAspath", 21),
          ("updateBadAttrFlags", 14),
          ("updateBadAttrLen", 15),
          ("updateBadNet", 20),
          ("updateBadNexthop", 18),
          ("updateBadOptAttr", 19),
          ("updateBadOrigin", 16),
          ("updateMalformAttr", 11),
          ("updateMissingWknwnAttr", 13),
          ("updateUnsuppWknwnAttr", 12))
    )


_AlaBgpPeerLastRecvNotifyReason_Type.__name__ = "Integer32"
_AlaBgpPeerLastRecvNotifyReason_Object = MibTableColumn
alaBgpPeerLastRecvNotifyReason = _AlaBgpPeerLastRecvNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 24),
    _AlaBgpPeerLastRecvNotifyReason_Type()
)
alaBgpPeerLastRecvNotifyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLastRecvNotifyReason.setStatus("current")
_AlaBgpPeerRcvdPrefixes_Type = Counter32
_AlaBgpPeerRcvdPrefixes_Object = MibTableColumn
alaBgpPeerRcvdPrefixes = _AlaBgpPeerRcvdPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 25),
    _AlaBgpPeerRcvdPrefixes_Type()
)
alaBgpPeerRcvdPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerRcvdPrefixes.setStatus("current")
_AlaBgpPeerDownTransitions_Type = Counter32
_AlaBgpPeerDownTransitions_Object = MibTableColumn
alaBgpPeerDownTransitions = _AlaBgpPeerDownTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 26),
    _AlaBgpPeerDownTransitions_Type()
)
alaBgpPeerDownTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerDownTransitions.setStatus("current")


class _AlaBgpPeerType_Type(Integer32):
    """Custom type alaBgpPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_AlaBgpPeerType_Type.__name__ = "Integer32"
_AlaBgpPeerType_Object = MibTableColumn
alaBgpPeerType = _AlaBgpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 27),
    _AlaBgpPeerType_Type()
)
alaBgpPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerType.setStatus("current")


class _AlaBgpPeerClearCounter_Type(Integer32):
    """Custom type alaBgpPeerClearCounter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaBgpPeerClearCounter_Type.__name__ = "Integer32"
_AlaBgpPeerClearCounter_Object = MibTableColumn
alaBgpPeerClearCounter = _AlaBgpPeerClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 28),
    _AlaBgpPeerClearCounter_Type()
)
alaBgpPeerClearCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerClearCounter.setStatus("current")


class _AlaBgpPeerAutoReStart_Type(Integer32):
    """Custom type alaBgpPeerAutoReStart based on Integer32"""
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


_AlaBgpPeerAutoReStart_Type.__name__ = "Integer32"
_AlaBgpPeerAutoReStart_Object = MibTableColumn
alaBgpPeerAutoReStart = _AlaBgpPeerAutoReStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 29),
    _AlaBgpPeerAutoReStart_Type()
)
alaBgpPeerAutoReStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerAutoReStart.setStatus("current")


class _AlaBgpPeerClientStatus_Type(Integer32):
    """Custom type alaBgpPeerClientStatus based on Integer32"""
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


_AlaBgpPeerClientStatus_Type.__name__ = "Integer32"
_AlaBgpPeerClientStatus_Object = MibTableColumn
alaBgpPeerClientStatus = _AlaBgpPeerClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 30),
    _AlaBgpPeerClientStatus_Type()
)
alaBgpPeerClientStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerClientStatus.setStatus("current")


class _AlaBgpPeerConfedStatus_Type(Integer32):
    """Custom type alaBgpPeerConfedStatus based on Integer32"""
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


_AlaBgpPeerConfedStatus_Type.__name__ = "Integer32"
_AlaBgpPeerConfedStatus_Object = MibTableColumn
alaBgpPeerConfedStatus = _AlaBgpPeerConfedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 31),
    _AlaBgpPeerConfedStatus_Type()
)
alaBgpPeerConfedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerConfedStatus.setStatus("current")


class _AlaBgpPeerRemovePrivateAs_Type(Integer32):
    """Custom type alaBgpPeerRemovePrivateAs based on Integer32"""
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


_AlaBgpPeerRemovePrivateAs_Type.__name__ = "Integer32"
_AlaBgpPeerRemovePrivateAs_Object = MibTableColumn
alaBgpPeerRemovePrivateAs = _AlaBgpPeerRemovePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 32),
    _AlaBgpPeerRemovePrivateAs_Type()
)
alaBgpPeerRemovePrivateAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerRemovePrivateAs.setStatus("current")


class _AlaBgpPeerTTL_Type(Integer32):
    """Custom type alaBgpPeerTTL based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaBgpPeerTTL_Type.__name__ = "Integer32"
_AlaBgpPeerTTL_Object = MibTableColumn
alaBgpPeerTTL = _AlaBgpPeerTTL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 33),
    _AlaBgpPeerTTL_Type()
)
alaBgpPeerTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerTTL.setStatus("current")


class _AlaBgpPeerAspathListOut_Type(DisplayString):
    """Custom type alaBgpPeerAspathListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerAspathListOut_Type.__name__ = "DisplayString"
_AlaBgpPeerAspathListOut_Object = MibTableColumn
alaBgpPeerAspathListOut = _AlaBgpPeerAspathListOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 34),
    _AlaBgpPeerAspathListOut_Type()
)
alaBgpPeerAspathListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerAspathListOut.setStatus("current")


class _AlaBgpPeerAspathListIn_Type(DisplayString):
    """Custom type alaBgpPeerAspathListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerAspathListIn_Type.__name__ = "DisplayString"
_AlaBgpPeerAspathListIn_Object = MibTableColumn
alaBgpPeerAspathListIn = _AlaBgpPeerAspathListIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 35),
    _AlaBgpPeerAspathListIn_Type()
)
alaBgpPeerAspathListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerAspathListIn.setStatus("current")


class _AlaBgpPeerPrefixListOut_Type(DisplayString):
    """Custom type alaBgpPeerPrefixListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerPrefixListOut_Type.__name__ = "DisplayString"
_AlaBgpPeerPrefixListOut_Object = MibTableColumn
alaBgpPeerPrefixListOut = _AlaBgpPeerPrefixListOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 36),
    _AlaBgpPeerPrefixListOut_Type()
)
alaBgpPeerPrefixListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerPrefixListOut.setStatus("current")


class _AlaBgpPeerPrefixListIn_Type(DisplayString):
    """Custom type alaBgpPeerPrefixListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerPrefixListIn_Type.__name__ = "DisplayString"
_AlaBgpPeerPrefixListIn_Object = MibTableColumn
alaBgpPeerPrefixListIn = _AlaBgpPeerPrefixListIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 37),
    _AlaBgpPeerPrefixListIn_Type()
)
alaBgpPeerPrefixListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerPrefixListIn.setStatus("current")


class _AlaBgpPeerCommunityListOut_Type(DisplayString):
    """Custom type alaBgpPeerCommunityListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerCommunityListOut_Type.__name__ = "DisplayString"
_AlaBgpPeerCommunityListOut_Object = MibTableColumn
alaBgpPeerCommunityListOut = _AlaBgpPeerCommunityListOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 38),
    _AlaBgpPeerCommunityListOut_Type()
)
alaBgpPeerCommunityListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerCommunityListOut.setStatus("current")


class _AlaBgpPeerCommunityListIn_Type(DisplayString):
    """Custom type alaBgpPeerCommunityListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerCommunityListIn_Type.__name__ = "DisplayString"
_AlaBgpPeerCommunityListIn_Object = MibTableColumn
alaBgpPeerCommunityListIn = _AlaBgpPeerCommunityListIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 39),
    _AlaBgpPeerCommunityListIn_Type()
)
alaBgpPeerCommunityListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerCommunityListIn.setStatus("current")


class _AlaBgpPeerRestart_Type(Integer32):
    """Custom type alaBgpPeerRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_AlaBgpPeerRestart_Type.__name__ = "Integer32"
_AlaBgpPeerRestart_Object = MibTableColumn
alaBgpPeerRestart = _AlaBgpPeerRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 40),
    _AlaBgpPeerRestart_Type()
)
alaBgpPeerRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerRestart.setStatus("current")


class _AlaBgpPeerDefaultOriginate_Type(Integer32):
    """Custom type alaBgpPeerDefaultOriginate based on Integer32"""
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


_AlaBgpPeerDefaultOriginate_Type.__name__ = "Integer32"
_AlaBgpPeerDefaultOriginate_Object = MibTableColumn
alaBgpPeerDefaultOriginate = _AlaBgpPeerDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 41),
    _AlaBgpPeerDefaultOriginate_Type()
)
alaBgpPeerDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerDefaultOriginate.setStatus("current")


class _AlaBgpPeerReconfigureInBound_Type(Integer32):
    """Custom type alaBgpPeerReconfigureInBound based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reconfigure", 1)
    )


_AlaBgpPeerReconfigureInBound_Type.__name__ = "Integer32"
_AlaBgpPeerReconfigureInBound_Object = MibTableColumn
alaBgpPeerReconfigureInBound = _AlaBgpPeerReconfigureInBound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 42),
    _AlaBgpPeerReconfigureInBound_Type()
)
alaBgpPeerReconfigureInBound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerReconfigureInBound.setStatus("current")


class _AlaBgpPeerReconfigureOutBound_Type(Integer32):
    """Custom type alaBgpPeerReconfigureOutBound based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reconfigure", 1)
    )


_AlaBgpPeerReconfigureOutBound_Type.__name__ = "Integer32"
_AlaBgpPeerReconfigureOutBound_Object = MibTableColumn
alaBgpPeerReconfigureOutBound = _AlaBgpPeerReconfigureOutBound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 43),
    _AlaBgpPeerReconfigureOutBound_Type()
)
alaBgpPeerReconfigureOutBound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerReconfigureOutBound.setStatus("current")


class _AlaBgpPeerMD5Key_Type(DisplayString):
    """Custom type alaBgpPeerMD5Key based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AlaBgpPeerMD5Key_Type.__name__ = "DisplayString"
_AlaBgpPeerMD5Key_Object = MibTableColumn
alaBgpPeerMD5Key = _AlaBgpPeerMD5Key_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 44),
    _AlaBgpPeerMD5Key_Type()
)
alaBgpPeerMD5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerMD5Key.setStatus("current")


class _AlaBgpPeerMD5KeyEncrypt_Type(OctetString):
    """Custom type alaBgpPeerMD5KeyEncrypt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AlaBgpPeerMD5KeyEncrypt_Type.__name__ = "OctetString"
_AlaBgpPeerMD5KeyEncrypt_Object = MibTableColumn
alaBgpPeerMD5KeyEncrypt = _AlaBgpPeerMD5KeyEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 45),
    _AlaBgpPeerMD5KeyEncrypt_Type()
)
alaBgpPeerMD5KeyEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerMD5KeyEncrypt.setStatus("current")


class _AlaBgpPeerRowStatus_Type(RowStatus):
    """Custom type alaBgpPeerRowStatus based on RowStatus"""


_AlaBgpPeerRowStatus_Object = MibTableColumn
alaBgpPeerRowStatus = _AlaBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 46),
    _AlaBgpPeerRowStatus_Type()
)
alaBgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerRowStatus.setStatus("current")
_AlaBgpPeerUpTransitions_Type = Counter32
_AlaBgpPeerUpTransitions_Object = MibTableColumn
alaBgpPeerUpTransitions = _AlaBgpPeerUpTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 47),
    _AlaBgpPeerUpTransitions_Type()
)
alaBgpPeerUpTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerUpTransitions.setStatus("current")
_AlaBgpPeerLastWriteTime_Type = TimeTicks
_AlaBgpPeerLastWriteTime_Object = MibTableColumn
alaBgpPeerLastWriteTime = _AlaBgpPeerLastWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 48),
    _AlaBgpPeerLastWriteTime_Type()
)
alaBgpPeerLastWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLastWriteTime.setStatus("current")
_AlaBgpPeerRcvdMsgs_Type = Counter32
_AlaBgpPeerRcvdMsgs_Object = MibTableColumn
alaBgpPeerRcvdMsgs = _AlaBgpPeerRcvdMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 49),
    _AlaBgpPeerRcvdMsgs_Type()
)
alaBgpPeerRcvdMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerRcvdMsgs.setStatus("current")
_AlaBgpPeerSentMsgs_Type = Counter32
_AlaBgpPeerSentMsgs_Object = MibTableColumn
alaBgpPeerSentMsgs = _AlaBgpPeerSentMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 50),
    _AlaBgpPeerSentMsgs_Type()
)
alaBgpPeerSentMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerSentMsgs.setStatus("current")
_AlaBgpPeerRcvdUpdMsgs_Type = Counter32
_AlaBgpPeerRcvdUpdMsgs_Object = MibTableColumn
alaBgpPeerRcvdUpdMsgs = _AlaBgpPeerRcvdUpdMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 51),
    _AlaBgpPeerRcvdUpdMsgs_Type()
)
alaBgpPeerRcvdUpdMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerRcvdUpdMsgs.setStatus("current")
_AlaBgpPeerSentUpdMsgs_Type = Counter32
_AlaBgpPeerSentUpdMsgs_Object = MibTableColumn
alaBgpPeerSentUpdMsgs = _AlaBgpPeerSentUpdMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 52),
    _AlaBgpPeerSentUpdMsgs_Type()
)
alaBgpPeerSentUpdMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerSentUpdMsgs.setStatus("current")
_AlaBgpPeerLastTransitionTime_Type = TimeTicks
_AlaBgpPeerLastTransitionTime_Object = MibTableColumn
alaBgpPeerLastTransitionTime = _AlaBgpPeerLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 53),
    _AlaBgpPeerLastTransitionTime_Type()
)
alaBgpPeerLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLastTransitionTime.setStatus("current")
_AlaBgpPeerLastUpTime_Type = TimeTicks
_AlaBgpPeerLastUpTime_Object = MibTableColumn
alaBgpPeerLastUpTime = _AlaBgpPeerLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 54),
    _AlaBgpPeerLastUpTime_Type()
)
alaBgpPeerLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLastUpTime.setStatus("current")
_AlaBgpPeerBgpId_Type = IpAddress
_AlaBgpPeerBgpId_Object = MibTableColumn
alaBgpPeerBgpId = _AlaBgpPeerBgpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 55),
    _AlaBgpPeerBgpId_Type()
)
alaBgpPeerBgpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerBgpId.setStatus("current")
_AlaBgpPeerLocalIntfName_Type = DisplayString
_AlaBgpPeerLocalIntfName_Object = MibTableColumn
alaBgpPeerLocalIntfName = _AlaBgpPeerLocalIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 56),
    _AlaBgpPeerLocalIntfName_Type()
)
alaBgpPeerLocalIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLocalIntfName.setStatus("current")


class _AlaBgpPeerRestartTime_Type(Integer32):
    """Custom type alaBgpPeerRestartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AlaBgpPeerRestartTime_Type.__name__ = "Integer32"
_AlaBgpPeerRestartTime_Object = MibTableColumn
alaBgpPeerRestartTime = _AlaBgpPeerRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 57),
    _AlaBgpPeerRestartTime_Type()
)
alaBgpPeerRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerRestartTime.setStatus("current")


class _AlaBgpPeerRestartState_Type(Integer32):
    """Custom type alaBgpPeerRestartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("notRestarting", 1),
          ("restarting", 2))
    )


_AlaBgpPeerRestartState_Type.__name__ = "Integer32"
_AlaBgpPeerRestartState_Object = MibTableColumn
alaBgpPeerRestartState = _AlaBgpPeerRestartState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 58),
    _AlaBgpPeerRestartState_Type()
)
alaBgpPeerRestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerRestartState.setStatus("current")


class _AlaBgpPeerRestartFwdState_Type(Integer32):
    """Custom type alaBgpPeerRestartFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPreserved", 1),
          ("preserved", 2))
    )


_AlaBgpPeerRestartFwdState_Type.__name__ = "Integer32"
_AlaBgpPeerRestartFwdState_Object = MibTableColumn
alaBgpPeerRestartFwdState = _AlaBgpPeerRestartFwdState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 59),
    _AlaBgpPeerRestartFwdState_Type()
)
alaBgpPeerRestartFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerRestartFwdState.setStatus("current")


class _AlaBgpPeerIpv6Unicast_Type(Integer32):
    """Custom type alaBgpPeerIpv6Unicast based on Integer32"""
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


_AlaBgpPeerIpv6Unicast_Type.__name__ = "Integer32"
_AlaBgpPeerIpv6Unicast_Object = MibTableColumn
alaBgpPeerIpv6Unicast = _AlaBgpPeerIpv6Unicast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 60),
    _AlaBgpPeerIpv6Unicast_Type()
)
alaBgpPeerIpv6Unicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerIpv6Unicast.setStatus("current")
_AlaBgpPeerIpv6NextHop_Type = Ipv6Address
_AlaBgpPeerIpv6NextHop_Object = MibTableColumn
alaBgpPeerIpv6NextHop = _AlaBgpPeerIpv6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 61),
    _AlaBgpPeerIpv6NextHop_Type()
)
alaBgpPeerIpv6NextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerIpv6NextHop.setStatus("current")


class _AlaBgpPeerLocalPort_Type(Integer32):
    """Custom type alaBgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpPeerLocalPort_Type.__name__ = "Integer32"
_AlaBgpPeerLocalPort_Object = MibTableColumn
alaBgpPeerLocalPort = _AlaBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 62),
    _AlaBgpPeerLocalPort_Type()
)
alaBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerLocalPort.setStatus("current")


class _AlaBgpPeerTcpWindowSize_Type(Integer32):
    """Custom type alaBgpPeerTcpWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpPeerTcpWindowSize_Type.__name__ = "Integer32"
_AlaBgpPeerTcpWindowSize_Object = MibTableColumn
alaBgpPeerTcpWindowSize = _AlaBgpPeerTcpWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 63),
    _AlaBgpPeerTcpWindowSize_Type()
)
alaBgpPeerTcpWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeerTcpWindowSize.setStatus("current")


class _AlaBgpPeerActivateIpv6_Type(Integer32):
    """Custom type alaBgpPeerActivateIpv6 based on Integer32"""
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


_AlaBgpPeerActivateIpv6_Type.__name__ = "Integer32"
_AlaBgpPeerActivateIpv6_Object = MibTableColumn
alaBgpPeerActivateIpv6 = _AlaBgpPeerActivateIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 64),
    _AlaBgpPeerActivateIpv6_Type()
)
alaBgpPeerActivateIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerActivateIpv6.setStatus("current")


class _AlaBgpPeerBfdStatus_Type(Integer32):
    """Custom type alaBgpPeerBfdStatus based on Integer32"""
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


_AlaBgpPeerBfdStatus_Type.__name__ = "Integer32"
_AlaBgpPeerBfdStatus_Object = MibTableColumn
alaBgpPeerBfdStatus = _AlaBgpPeerBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 65),
    _AlaBgpPeerBfdStatus_Type()
)
alaBgpPeerBfdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerBfdStatus.setStatus("current")


class _AlaBgpPeerPrefix6ListOut_Type(DisplayString):
    """Custom type alaBgpPeerPrefix6ListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerPrefix6ListOut_Type.__name__ = "DisplayString"
_AlaBgpPeerPrefix6ListOut_Object = MibTableColumn
alaBgpPeerPrefix6ListOut = _AlaBgpPeerPrefix6ListOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 66),
    _AlaBgpPeerPrefix6ListOut_Type()
)
alaBgpPeerPrefix6ListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerPrefix6ListOut.setStatus("current")


class _AlaBgpPeerPrefix6ListIn_Type(DisplayString):
    """Custom type alaBgpPeerPrefix6ListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeerPrefix6ListIn_Type.__name__ = "DisplayString"
_AlaBgpPeerPrefix6ListIn_Object = MibTableColumn
alaBgpPeerPrefix6ListIn = _AlaBgpPeerPrefix6ListIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 2, 1, 67),
    _AlaBgpPeerPrefix6ListIn_Type()
)
alaBgpPeerPrefix6ListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPeerPrefix6ListIn.setStatus("current")
_AlaBgpAggrTable_Object = MibTable
alaBgpAggrTable = _AlaBgpAggrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaBgpAggrTable.setStatus("current")
_AlaBgpAggrEntry_Object = MibTableRow
alaBgpAggrEntry = _AlaBgpAggrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1)
)
alaBgpAggrEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpAggrAddr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpAggrMask"),
)
if mibBuilder.loadTexts:
    alaBgpAggrEntry.setStatus("current")
_AlaBgpAggrAddr_Type = IpAddress
_AlaBgpAggrAddr_Object = MibTableColumn
alaBgpAggrAddr = _AlaBgpAggrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 1),
    _AlaBgpAggrAddr_Type()
)
alaBgpAggrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAggrAddr.setStatus("current")
_AlaBgpAggrMask_Type = IpAddress
_AlaBgpAggrMask_Object = MibTableColumn
alaBgpAggrMask = _AlaBgpAggrMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 2),
    _AlaBgpAggrMask_Type()
)
alaBgpAggrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAggrMask.setStatus("current")


class _AlaBgpAggrSummarize_Type(Integer32):
    """Custom type alaBgpAggrSummarize based on Integer32"""
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


_AlaBgpAggrSummarize_Type.__name__ = "Integer32"
_AlaBgpAggrSummarize_Object = MibTableColumn
alaBgpAggrSummarize = _AlaBgpAggrSummarize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 3),
    _AlaBgpAggrSummarize_Type()
)
alaBgpAggrSummarize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpAggrSummarize.setStatus("current")


class _AlaBgpAggrSet_Type(Integer32):
    """Custom type alaBgpAggrSet based on Integer32"""
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


_AlaBgpAggrSet_Type.__name__ = "Integer32"
_AlaBgpAggrSet_Object = MibTableColumn
alaBgpAggrSet = _AlaBgpAggrSet_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 4),
    _AlaBgpAggrSet_Type()
)
alaBgpAggrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpAggrSet.setStatus("current")


class _AlaBgpAggrState_Type(Integer32):
    """Custom type alaBgpAggrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaBgpAggrState_Type.__name__ = "Integer32"
_AlaBgpAggrState_Object = MibTableColumn
alaBgpAggrState = _AlaBgpAggrState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 5),
    _AlaBgpAggrState_Type()
)
alaBgpAggrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAggrState.setStatus("current")


class _AlaBgpAggrMetric_Type(Gauge32):
    """Custom type alaBgpAggrMetric based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpAggrMetric_Type.__name__ = "Gauge32"
_AlaBgpAggrMetric_Object = MibTableColumn
alaBgpAggrMetric = _AlaBgpAggrMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 6),
    _AlaBgpAggrMetric_Type()
)
alaBgpAggrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpAggrMetric.setStatus("current")


class _AlaBgpAggrLocalPref_Type(Gauge32):
    """Custom type alaBgpAggrLocalPref based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpAggrLocalPref_Type.__name__ = "Gauge32"
_AlaBgpAggrLocalPref_Object = MibTableColumn
alaBgpAggrLocalPref = _AlaBgpAggrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 7),
    _AlaBgpAggrLocalPref_Type()
)
alaBgpAggrLocalPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpAggrLocalPref.setStatus("current")


class _AlaBgpAggrCommunity_Type(DisplayString):
    """Custom type alaBgpAggrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpAggrCommunity_Type.__name__ = "DisplayString"
_AlaBgpAggrCommunity_Object = MibTableColumn
alaBgpAggrCommunity = _AlaBgpAggrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 8),
    _AlaBgpAggrCommunity_Type()
)
alaBgpAggrCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpAggrCommunity.setStatus("current")


class _AlaBgpAggrRowStatus_Type(RowStatus):
    """Custom type alaBgpAggrRowStatus based on RowStatus"""


_AlaBgpAggrRowStatus_Object = MibTableColumn
alaBgpAggrRowStatus = _AlaBgpAggrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 3, 1, 9),
    _AlaBgpAggrRowStatus_Type()
)
alaBgpAggrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpAggrRowStatus.setStatus("current")
_AlaBgpNetworkTable_Object = MibTable
alaBgpNetworkTable = _AlaBgpNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaBgpNetworkTable.setStatus("current")
_AlaBgpNetworkEntry_Object = MibTableRow
alaBgpNetworkEntry = _AlaBgpNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4, 1)
)
alaBgpNetworkEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpNetworkAddr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpNetworkMask"),
)
if mibBuilder.loadTexts:
    alaBgpNetworkEntry.setStatus("current")
_AlaBgpNetworkAddr_Type = IpAddress
_AlaBgpNetworkAddr_Object = MibTableColumn
alaBgpNetworkAddr = _AlaBgpNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4, 1, 1),
    _AlaBgpNetworkAddr_Type()
)
alaBgpNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNetworkAddr.setStatus("current")
_AlaBgpNetworkMask_Type = IpAddress
_AlaBgpNetworkMask_Object = MibTableColumn
alaBgpNetworkMask = _AlaBgpNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4, 1, 2),
    _AlaBgpNetworkMask_Type()
)
alaBgpNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNetworkMask.setStatus("current")


class _AlaBgpNetworkState_Type(Integer32):
    """Custom type alaBgpNetworkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaBgpNetworkState_Type.__name__ = "Integer32"
_AlaBgpNetworkState_Object = MibTableColumn
alaBgpNetworkState = _AlaBgpNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4, 1, 3),
    _AlaBgpNetworkState_Type()
)
alaBgpNetworkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNetworkState.setStatus("current")


class _AlaBgpNetworkMetric_Type(Gauge32):
    """Custom type alaBgpNetworkMetric based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpNetworkMetric_Type.__name__ = "Gauge32"
_AlaBgpNetworkMetric_Object = MibTableColumn
alaBgpNetworkMetric = _AlaBgpNetworkMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4, 1, 4),
    _AlaBgpNetworkMetric_Type()
)
alaBgpNetworkMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpNetworkMetric.setStatus("current")


class _AlaBgpNetworkLocalPref_Type(Gauge32):
    """Custom type alaBgpNetworkLocalPref based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpNetworkLocalPref_Type.__name__ = "Gauge32"
_AlaBgpNetworkLocalPref_Object = MibTableColumn
alaBgpNetworkLocalPref = _AlaBgpNetworkLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4, 1, 5),
    _AlaBgpNetworkLocalPref_Type()
)
alaBgpNetworkLocalPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpNetworkLocalPref.setStatus("current")


class _AlaBgpNetworkCommunity_Type(DisplayString):
    """Custom type alaBgpNetworkCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpNetworkCommunity_Type.__name__ = "DisplayString"
_AlaBgpNetworkCommunity_Object = MibTableColumn
alaBgpNetworkCommunity = _AlaBgpNetworkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4, 1, 6),
    _AlaBgpNetworkCommunity_Type()
)
alaBgpNetworkCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpNetworkCommunity.setStatus("current")


class _AlaBgpNetworkRowStatus_Type(RowStatus):
    """Custom type alaBgpNetworkRowStatus based on RowStatus"""


_AlaBgpNetworkRowStatus_Object = MibTableColumn
alaBgpNetworkRowStatus = _AlaBgpNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 4, 1, 7),
    _AlaBgpNetworkRowStatus_Type()
)
alaBgpNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpNetworkRowStatus.setStatus("current")
_AlaBgpRouteTable_Object = MibTable
alaBgpRouteTable = _AlaBgpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaBgpRouteTable.setStatus("current")
_AlaBgpRouteEntry_Object = MibTableRow
alaBgpRouteEntry = _AlaBgpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1)
)
alaBgpRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRouteAddr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRouteMask"),
)
if mibBuilder.loadTexts:
    alaBgpRouteEntry.setStatus("current")
_AlaBgpRouteAddr_Type = IpAddress
_AlaBgpRouteAddr_Object = MibTableColumn
alaBgpRouteAddr = _AlaBgpRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 1),
    _AlaBgpRouteAddr_Type()
)
alaBgpRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteAddr.setStatus("current")
_AlaBgpRouteMask_Type = IpAddress
_AlaBgpRouteMask_Object = MibTableColumn
alaBgpRouteMask = _AlaBgpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 2),
    _AlaBgpRouteMask_Type()
)
alaBgpRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteMask.setStatus("current")


class _AlaBgpRouteState_Type(Integer32):
    """Custom type alaBgpRouteState based on Integer32"""
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


_AlaBgpRouteState_Type.__name__ = "Integer32"
_AlaBgpRouteState_Object = MibTableColumn
alaBgpRouteState = _AlaBgpRouteState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 3),
    _AlaBgpRouteState_Type()
)
alaBgpRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteState.setStatus("current")
_AlaBgpRoutePaths_Type = Counter32
_AlaBgpRoutePaths_Object = MibTableColumn
alaBgpRoutePaths = _AlaBgpRoutePaths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 4),
    _AlaBgpRoutePaths_Type()
)
alaBgpRoutePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoutePaths.setStatus("current")
_AlaBgpRouteFeasiblePaths_Type = Counter32
_AlaBgpRouteFeasiblePaths_Object = MibTableColumn
alaBgpRouteFeasiblePaths = _AlaBgpRouteFeasiblePaths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 5),
    _AlaBgpRouteFeasiblePaths_Type()
)
alaBgpRouteFeasiblePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteFeasiblePaths.setStatus("current")
_AlaBgpRouteNextHop_Type = IpAddress
_AlaBgpRouteNextHop_Object = MibTableColumn
alaBgpRouteNextHop = _AlaBgpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 6),
    _AlaBgpRouteNextHop_Type()
)
alaBgpRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteNextHop.setStatus("current")
_AlaBgpRouteIgpNextHop_Type = IpAddress
_AlaBgpRouteIgpNextHop_Object = MibTableColumn
alaBgpRouteIgpNextHop = _AlaBgpRouteIgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 7),
    _AlaBgpRouteIgpNextHop_Type()
)
alaBgpRouteIgpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIgpNextHop.setStatus("current")


class _AlaBgpRouteIsHidden_Type(Integer32):
    """Custom type alaBgpRouteIsHidden based on Integer32"""
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


_AlaBgpRouteIsHidden_Type.__name__ = "Integer32"
_AlaBgpRouteIsHidden_Object = MibTableColumn
alaBgpRouteIsHidden = _AlaBgpRouteIsHidden_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 8),
    _AlaBgpRouteIsHidden_Type()
)
alaBgpRouteIsHidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsHidden.setStatus("current")


class _AlaBgpRouteIsAggregate_Type(Integer32):
    """Custom type alaBgpRouteIsAggregate based on Integer32"""
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


_AlaBgpRouteIsAggregate_Type.__name__ = "Integer32"
_AlaBgpRouteIsAggregate_Object = MibTableColumn
alaBgpRouteIsAggregate = _AlaBgpRouteIsAggregate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 9),
    _AlaBgpRouteIsAggregate_Type()
)
alaBgpRouteIsAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsAggregate.setStatus("current")


class _AlaBgpRouteIsAggregateContributor_Type(Integer32):
    """Custom type alaBgpRouteIsAggregateContributor based on Integer32"""
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


_AlaBgpRouteIsAggregateContributor_Type.__name__ = "Integer32"
_AlaBgpRouteIsAggregateContributor_Object = MibTableColumn
alaBgpRouteIsAggregateContributor = _AlaBgpRouteIsAggregateContributor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 10),
    _AlaBgpRouteIsAggregateContributor_Type()
)
alaBgpRouteIsAggregateContributor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsAggregateContributor.setStatus("current")


class _AlaBgpRouteAdvNeighbors_Type(DisplayString):
    """Custom type alaBgpRouteAdvNeighbors based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpRouteAdvNeighbors_Type.__name__ = "DisplayString"
_AlaBgpRouteAdvNeighbors_Object = MibTableColumn
alaBgpRouteAdvNeighbors = _AlaBgpRouteAdvNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 11),
    _AlaBgpRouteAdvNeighbors_Type()
)
alaBgpRouteAdvNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteAdvNeighbors.setStatus("current")


class _AlaBgpRouteIsAggregateList_Type(Integer32):
    """Custom type alaBgpRouteIsAggregateList based on Integer32"""
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


_AlaBgpRouteIsAggregateList_Type.__name__ = "Integer32"
_AlaBgpRouteIsAggregateList_Object = MibTableColumn
alaBgpRouteIsAggregateList = _AlaBgpRouteIsAggregateList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 12),
    _AlaBgpRouteIsAggregateList_Type()
)
alaBgpRouteIsAggregateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsAggregateList.setStatus("current")


class _AlaBgpRouteIsAggregateWait_Type(Integer32):
    """Custom type alaBgpRouteIsAggregateWait based on Integer32"""
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


_AlaBgpRouteIsAggregateWait_Type.__name__ = "Integer32"
_AlaBgpRouteIsAggregateWait_Object = MibTableColumn
alaBgpRouteIsAggregateWait = _AlaBgpRouteIsAggregateWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 13),
    _AlaBgpRouteIsAggregateWait_Type()
)
alaBgpRouteIsAggregateWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsAggregateWait.setStatus("current")


class _AlaBgpRouteIsOnEbgpChgList_Type(Integer32):
    """Custom type alaBgpRouteIsOnEbgpChgList based on Integer32"""
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


_AlaBgpRouteIsOnEbgpChgList_Type.__name__ = "Integer32"
_AlaBgpRouteIsOnEbgpChgList_Object = MibTableColumn
alaBgpRouteIsOnEbgpChgList = _AlaBgpRouteIsOnEbgpChgList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 14),
    _AlaBgpRouteIsOnEbgpChgList_Type()
)
alaBgpRouteIsOnEbgpChgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsOnEbgpChgList.setStatus("current")


class _AlaBgpRouteIsOnIbgpClientChgList_Type(Integer32):
    """Custom type alaBgpRouteIsOnIbgpClientChgList based on Integer32"""
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


_AlaBgpRouteIsOnIbgpClientChgList_Type.__name__ = "Integer32"
_AlaBgpRouteIsOnIbgpClientChgList_Object = MibTableColumn
alaBgpRouteIsOnIbgpClientChgList = _AlaBgpRouteIsOnIbgpClientChgList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 15),
    _AlaBgpRouteIsOnIbgpClientChgList_Type()
)
alaBgpRouteIsOnIbgpClientChgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsOnIbgpClientChgList.setStatus("current")


class _AlaBgpRouteIsOnIbgpChgList_Type(Integer32):
    """Custom type alaBgpRouteIsOnIbgpChgList based on Integer32"""
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


_AlaBgpRouteIsOnIbgpChgList_Type.__name__ = "Integer32"
_AlaBgpRouteIsOnIbgpChgList_Object = MibTableColumn
alaBgpRouteIsOnIbgpChgList = _AlaBgpRouteIsOnIbgpChgList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 16),
    _AlaBgpRouteIsOnIbgpChgList_Type()
)
alaBgpRouteIsOnIbgpChgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsOnIbgpChgList.setStatus("current")


class _AlaBgpRouteIsOnLocalChgList_Type(Integer32):
    """Custom type alaBgpRouteIsOnLocalChgList based on Integer32"""
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


_AlaBgpRouteIsOnLocalChgList_Type.__name__ = "Integer32"
_AlaBgpRouteIsOnLocalChgList_Object = MibTableColumn
alaBgpRouteIsOnLocalChgList = _AlaBgpRouteIsOnLocalChgList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 17),
    _AlaBgpRouteIsOnLocalChgList_Type()
)
alaBgpRouteIsOnLocalChgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsOnLocalChgList.setStatus("current")


class _AlaBgpRouteIsOnDeleteList_Type(Integer32):
    """Custom type alaBgpRouteIsOnDeleteList based on Integer32"""
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


_AlaBgpRouteIsOnDeleteList_Type.__name__ = "Integer32"
_AlaBgpRouteIsOnDeleteList_Object = MibTableColumn
alaBgpRouteIsOnDeleteList = _AlaBgpRouteIsOnDeleteList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 18),
    _AlaBgpRouteIsOnDeleteList_Type()
)
alaBgpRouteIsOnDeleteList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsOnDeleteList.setStatus("current")


class _AlaBgpRouteIsDampened_Type(Integer32):
    """Custom type alaBgpRouteIsDampened based on Integer32"""
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


_AlaBgpRouteIsDampened_Type.__name__ = "Integer32"
_AlaBgpRouteIsDampened_Object = MibTableColumn
alaBgpRouteIsDampened = _AlaBgpRouteIsDampened_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 5, 1, 19),
    _AlaBgpRouteIsDampened_Type()
)
alaBgpRouteIsDampened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteIsDampened.setStatus("current")
_AlaBgpPathTable_Object = MibTable
alaBgpPathTable = _AlaBgpPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaBgpPathTable.setStatus("current")
_AlaBgpPathEntry_Object = MibTableRow
alaBgpPathEntry = _AlaBgpPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1)
)
alaBgpPathEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPathAddr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPathMask"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPathPeerAddr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPathSrcProto"),
)
if mibBuilder.loadTexts:
    alaBgpPathEntry.setStatus("current")
_AlaBgpPathAddr_Type = IpAddress
_AlaBgpPathAddr_Object = MibTableColumn
alaBgpPathAddr = _AlaBgpPathAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 1),
    _AlaBgpPathAddr_Type()
)
alaBgpPathAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathAddr.setStatus("current")
_AlaBgpPathMask_Type = IpAddress
_AlaBgpPathMask_Object = MibTableColumn
alaBgpPathMask = _AlaBgpPathMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 2),
    _AlaBgpPathMask_Type()
)
alaBgpPathMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathMask.setStatus("current")
_AlaBgpPathPeerAddr_Type = IpAddress
_AlaBgpPathPeerAddr_Object = MibTableColumn
alaBgpPathPeerAddr = _AlaBgpPathPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 3),
    _AlaBgpPathPeerAddr_Type()
)
alaBgpPathPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathPeerAddr.setStatus("current")


class _AlaBgpPathSrcProto_Type(Integer32):
    """Custom type alaBgpPathSrcProto based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 11),
          ("directHost", 4),
          ("ebgp", 9),
          ("ibgp", 10),
          ("isis", 7),
          ("local", 2),
          ("network", 12),
          ("ospf", 6),
          ("other", 1),
          ("rip", 5),
          ("static", 3))
    )


_AlaBgpPathSrcProto_Type.__name__ = "Integer32"
_AlaBgpPathSrcProto_Object = MibTableColumn
alaBgpPathSrcProto = _AlaBgpPathSrcProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 4),
    _AlaBgpPathSrcProto_Type()
)
alaBgpPathSrcProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathSrcProto.setStatus("current")


class _AlaBgpPathWeight_Type(Integer32):
    """Custom type alaBgpPathWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaBgpPathWeight_Type.__name__ = "Integer32"
_AlaBgpPathWeight_Object = MibTableColumn
alaBgpPathWeight = _AlaBgpPathWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 5),
    _AlaBgpPathWeight_Type()
)
alaBgpPathWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathWeight.setStatus("current")
_AlaBgpPathPref_Type = Gauge32
_AlaBgpPathPref_Object = MibTableColumn
alaBgpPathPref = _AlaBgpPathPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 6),
    _AlaBgpPathPref_Type()
)
alaBgpPathPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathPref.setStatus("current")


class _AlaBgpPathState_Type(Integer32):
    """Custom type alaBgpPathState based on Integer32"""
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
        *(("best", 1),
          ("dampened", 5),
          ("feasible", 2),
          ("none", 6),
          ("policyWait", 3),
          ("stale", 7),
          ("unSynchronized", 4))
    )


_AlaBgpPathState_Type.__name__ = "Integer32"
_AlaBgpPathState_Object = MibTableColumn
alaBgpPathState = _AlaBgpPathState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 7),
    _AlaBgpPathState_Type()
)
alaBgpPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathState.setStatus("current")


class _AlaBgpPathOrigin_Type(Integer32):
    """Custom type alaBgpPathOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3),
          ("none", 9))
    )


_AlaBgpPathOrigin_Type.__name__ = "Integer32"
_AlaBgpPathOrigin_Object = MibTableColumn
alaBgpPathOrigin = _AlaBgpPathOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 8),
    _AlaBgpPathOrigin_Type()
)
alaBgpPathOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathOrigin.setStatus("current")
_AlaBgpPathNextHop_Type = IpAddress
_AlaBgpPathNextHop_Object = MibTableColumn
alaBgpPathNextHop = _AlaBgpPathNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 9),
    _AlaBgpPathNextHop_Type()
)
alaBgpPathNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathNextHop.setStatus("current")


class _AlaBgpPathAs_Type(DisplayString):
    """Custom type alaBgpPathAs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpPathAs_Type.__name__ = "DisplayString"
_AlaBgpPathAs_Object = MibTableColumn
alaBgpPathAs = _AlaBgpPathAs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 10),
    _AlaBgpPathAs_Type()
)
alaBgpPathAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathAs.setStatus("current")


class _AlaBgpPathLocalPref_Type(Integer32):
    """Custom type alaBgpPathLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AlaBgpPathLocalPref_Type.__name__ = "Integer32"
_AlaBgpPathLocalPref_Object = MibTableColumn
alaBgpPathLocalPref = _AlaBgpPathLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 11),
    _AlaBgpPathLocalPref_Type()
)
alaBgpPathLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathLocalPref.setStatus("current")


class _AlaBgpPathMed_Type(Gauge32):
    """Custom type alaBgpPathMed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpPathMed_Type.__name__ = "Gauge32"
_AlaBgpPathMed_Object = MibTableColumn
alaBgpPathMed = _AlaBgpPathMed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 12),
    _AlaBgpPathMed_Type()
)
alaBgpPathMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathMed.setStatus("current")


class _AlaBgpPathAtomic_Type(Integer32):
    """Custom type alaBgpPathAtomic based on Integer32"""
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


_AlaBgpPathAtomic_Type.__name__ = "Integer32"
_AlaBgpPathAtomic_Object = MibTableColumn
alaBgpPathAtomic = _AlaBgpPathAtomic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 13),
    _AlaBgpPathAtomic_Type()
)
alaBgpPathAtomic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathAtomic.setStatus("current")


class _AlaBgpPathAggregatorAs_Type(Integer32):
    """Custom type alaBgpPathAggregatorAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpPathAggregatorAs_Type.__name__ = "Integer32"
_AlaBgpPathAggregatorAs_Object = MibTableColumn
alaBgpPathAggregatorAs = _AlaBgpPathAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 14),
    _AlaBgpPathAggregatorAs_Type()
)
alaBgpPathAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathAggregatorAs.setStatus("current")
_AlaBgpPathAggregatorAddr_Type = IpAddress
_AlaBgpPathAggregatorAddr_Object = MibTableColumn
alaBgpPathAggregatorAddr = _AlaBgpPathAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 15),
    _AlaBgpPathAggregatorAddr_Type()
)
alaBgpPathAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathAggregatorAddr.setStatus("current")


class _AlaBgpPathCommunity_Type(DisplayString):
    """Custom type alaBgpPathCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpPathCommunity_Type.__name__ = "DisplayString"
_AlaBgpPathCommunity_Object = MibTableColumn
alaBgpPathCommunity = _AlaBgpPathCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 16),
    _AlaBgpPathCommunity_Type()
)
alaBgpPathCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathCommunity.setStatus("current")


class _AlaBgpPathUnknownAttr_Type(OctetString):
    """Custom type alaBgpPathUnknownAttr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpPathUnknownAttr_Type.__name__ = "OctetString"
_AlaBgpPathUnknownAttr_Object = MibTableColumn
alaBgpPathUnknownAttr = _AlaBgpPathUnknownAttr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 17),
    _AlaBgpPathUnknownAttr_Type()
)
alaBgpPathUnknownAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathUnknownAttr.setStatus("current")
_AlaBgpPathOriginatorId_Type = IpAddress
_AlaBgpPathOriginatorId_Object = MibTableColumn
alaBgpPathOriginatorId = _AlaBgpPathOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 18),
    _AlaBgpPathOriginatorId_Type()
)
alaBgpPathOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathOriginatorId.setStatus("current")


class _AlaBgpPathClusterList_Type(DisplayString):
    """Custom type alaBgpPathClusterList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpPathClusterList_Type.__name__ = "DisplayString"
_AlaBgpPathClusterList_Object = MibTableColumn
alaBgpPathClusterList = _AlaBgpPathClusterList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 19),
    _AlaBgpPathClusterList_Type()
)
alaBgpPathClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathClusterList.setStatus("current")


class _AlaBgpPathPeerInetType_Type(Integer32):
    """Custom type alaBgpPathPeerInetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("unknown", 0))
    )


_AlaBgpPathPeerInetType_Type.__name__ = "Integer32"
_AlaBgpPathPeerInetType_Object = MibTableColumn
alaBgpPathPeerInetType = _AlaBgpPathPeerInetType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 20),
    _AlaBgpPathPeerInetType_Type()
)
alaBgpPathPeerInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathPeerInetType.setStatus("current")


class _AlaBgpPathPeerName_Type(DisplayString):
    """Custom type alaBgpPathPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AlaBgpPathPeerName_Type.__name__ = "DisplayString"
_AlaBgpPathPeerName_Object = MibTableColumn
alaBgpPathPeerName = _AlaBgpPathPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 6, 1, 21),
    _AlaBgpPathPeerName_Type()
)
alaBgpPathPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPathPeerName.setStatus("current")
_AlaBgpDampTable_Object = MibTable
alaBgpDampTable = _AlaBgpDampTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaBgpDampTable.setStatus("current")
_AlaBgpDampEntry_Object = MibTableRow
alaBgpDampEntry = _AlaBgpDampEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1)
)
alaBgpDampEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpDampAddr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpDampMask"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpDampPeerAddr"),
)
if mibBuilder.loadTexts:
    alaBgpDampEntry.setStatus("current")
_AlaBgpDampAddr_Type = IpAddress
_AlaBgpDampAddr_Object = MibTableColumn
alaBgpDampAddr = _AlaBgpDampAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 1),
    _AlaBgpDampAddr_Type()
)
alaBgpDampAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampAddr.setStatus("current")
_AlaBgpDampMask_Type = IpAddress
_AlaBgpDampMask_Object = MibTableColumn
alaBgpDampMask = _AlaBgpDampMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 2),
    _AlaBgpDampMask_Type()
)
alaBgpDampMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampMask.setStatus("current")
_AlaBgpDampPeerAddr_Type = IpAddress
_AlaBgpDampPeerAddr_Object = MibTableColumn
alaBgpDampPeerAddr = _AlaBgpDampPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 3),
    _AlaBgpDampPeerAddr_Type()
)
alaBgpDampPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampPeerAddr.setStatus("current")


class _AlaBgpDampFigureOfMerit_Type(Integer32):
    """Custom type alaBgpDampFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaBgpDampFigureOfMerit_Type.__name__ = "Integer32"
_AlaBgpDampFigureOfMerit_Object = MibTableColumn
alaBgpDampFigureOfMerit = _AlaBgpDampFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 4),
    _AlaBgpDampFigureOfMerit_Type()
)
alaBgpDampFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampFigureOfMerit.setStatus("current")
_AlaBgpDampFlaps_Type = Counter32
_AlaBgpDampFlaps_Object = MibTableColumn
alaBgpDampFlaps = _AlaBgpDampFlaps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 5),
    _AlaBgpDampFlaps_Type()
)
alaBgpDampFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampFlaps.setStatus("current")
_AlaBgpDampDuration_Type = TimeTicks
_AlaBgpDampDuration_Object = MibTableColumn
alaBgpDampDuration = _AlaBgpDampDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 6),
    _AlaBgpDampDuration_Type()
)
alaBgpDampDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampDuration.setStatus("current")
_AlaBgpDampLastUpdateTime_Type = TimeTicks
_AlaBgpDampLastUpdateTime_Object = MibTableColumn
alaBgpDampLastUpdateTime = _AlaBgpDampLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 7),
    _AlaBgpDampLastUpdateTime_Type()
)
alaBgpDampLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampLastUpdateTime.setStatus("current")
_AlaBgpDampReuseTime_Type = TimeTicks
_AlaBgpDampReuseTime_Object = MibTableColumn
alaBgpDampReuseTime = _AlaBgpDampReuseTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 8),
    _AlaBgpDampReuseTime_Type()
)
alaBgpDampReuseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDampReuseTime.setStatus("current")


class _AlaBgpDampClear_Type(Integer32):
    """Custom type alaBgpDampClear based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaBgpDampClear_Type.__name__ = "Integer32"
_AlaBgpDampClear_Object = MibTableColumn
alaBgpDampClear = _AlaBgpDampClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 7, 1, 9),
    _AlaBgpDampClear_Type()
)
alaBgpDampClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDampClear.setStatus("current")
_AlaBgpPolicy_ObjectIdentity = ObjectIdentity
alaBgpPolicy = _AlaBgpPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8)
)
_AlaBgpRouteMapTable_Object = MibTable
alaBgpRouteMapTable = _AlaBgpRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaBgpRouteMapTable.setStatus("current")
_AlaBgpRouteMapEntry_Object = MibTableRow
alaBgpRouteMapEntry = _AlaBgpRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1)
)
alaBgpRouteMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapName"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapInst"),
)
if mibBuilder.loadTexts:
    alaBgpRouteMapEntry.setStatus("current")


class _AlaBgpRouteMapName_Type(DisplayString):
    """Custom type alaBgpRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpRouteMapName_Type.__name__ = "DisplayString"
_AlaBgpRouteMapName_Object = MibTableColumn
alaBgpRouteMapName = _AlaBgpRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 1),
    _AlaBgpRouteMapName_Type()
)
alaBgpRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteMapName.setStatus("current")


class _AlaBgpRouteMapInst_Type(Integer32):
    """Custom type alaBgpRouteMapInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaBgpRouteMapInst_Type.__name__ = "Integer32"
_AlaBgpRouteMapInst_Object = MibTableColumn
alaBgpRouteMapInst = _AlaBgpRouteMapInst_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 2),
    _AlaBgpRouteMapInst_Type()
)
alaBgpRouteMapInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRouteMapInst.setStatus("current")


class _AlaBgpRouteMapAsPathMatchListId_Type(DisplayString):
    """Custom type alaBgpRouteMapAsPathMatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpRouteMapAsPathMatchListId_Type.__name__ = "DisplayString"
_AlaBgpRouteMapAsPathMatchListId_Object = MibTableColumn
alaBgpRouteMapAsPathMatchListId = _AlaBgpRouteMapAsPathMatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 3),
    _AlaBgpRouteMapAsPathMatchListId_Type()
)
alaBgpRouteMapAsPathMatchListId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapAsPathMatchListId.setStatus("current")


class _AlaBgpRouteMapPrefixMatchListId_Type(DisplayString):
    """Custom type alaBgpRouteMapPrefixMatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpRouteMapPrefixMatchListId_Type.__name__ = "DisplayString"
_AlaBgpRouteMapPrefixMatchListId_Object = MibTableColumn
alaBgpRouteMapPrefixMatchListId = _AlaBgpRouteMapPrefixMatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 4),
    _AlaBgpRouteMapPrefixMatchListId_Type()
)
alaBgpRouteMapPrefixMatchListId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapPrefixMatchListId.setStatus("current")


class _AlaBgpRouteMapCommunityMatchListId_Type(DisplayString):
    """Custom type alaBgpRouteMapCommunityMatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpRouteMapCommunityMatchListId_Type.__name__ = "DisplayString"
_AlaBgpRouteMapCommunityMatchListId_Object = MibTableColumn
alaBgpRouteMapCommunityMatchListId = _AlaBgpRouteMapCommunityMatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 5),
    _AlaBgpRouteMapCommunityMatchListId_Type()
)
alaBgpRouteMapCommunityMatchListId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapCommunityMatchListId.setStatus("current")


class _AlaBgpRouteMapOrigin_Type(Integer32):
    """Custom type alaBgpRouteMapOrigin based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3),
          ("none", 255))
    )


_AlaBgpRouteMapOrigin_Type.__name__ = "Integer32"
_AlaBgpRouteMapOrigin_Object = MibTableColumn
alaBgpRouteMapOrigin = _AlaBgpRouteMapOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 6),
    _AlaBgpRouteMapOrigin_Type()
)
alaBgpRouteMapOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapOrigin.setStatus("current")


class _AlaBgpRouteMapLocalPref_Type(Gauge32):
    """Custom type alaBgpRouteMapLocalPref based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpRouteMapLocalPref_Type.__name__ = "Gauge32"
_AlaBgpRouteMapLocalPref_Object = MibTableColumn
alaBgpRouteMapLocalPref = _AlaBgpRouteMapLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 7),
    _AlaBgpRouteMapLocalPref_Type()
)
alaBgpRouteMapLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapLocalPref.setStatus("current")


class _AlaBgpRouteMapLocalPrefMode_Type(Integer32):
    """Custom type alaBgpRouteMapLocalPrefMode based on Integer32"""
    defaultValue = 1

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
        *(("dec", 3),
          ("inc", 2),
          ("none", 1),
          ("rep", 4))
    )


_AlaBgpRouteMapLocalPrefMode_Type.__name__ = "Integer32"
_AlaBgpRouteMapLocalPrefMode_Object = MibTableColumn
alaBgpRouteMapLocalPrefMode = _AlaBgpRouteMapLocalPrefMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 8),
    _AlaBgpRouteMapLocalPrefMode_Type()
)
alaBgpRouteMapLocalPrefMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapLocalPrefMode.setStatus("current")


class _AlaBgpRouteMapMed_Type(Gauge32):
    """Custom type alaBgpRouteMapMed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpRouteMapMed_Type.__name__ = "Gauge32"
_AlaBgpRouteMapMed_Object = MibTableColumn
alaBgpRouteMapMed = _AlaBgpRouteMapMed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 9),
    _AlaBgpRouteMapMed_Type()
)
alaBgpRouteMapMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapMed.setStatus("current")


class _AlaBgpRouteMapMedMode_Type(Integer32):
    """Custom type alaBgpRouteMapMedMode based on Integer32"""
    defaultValue = 1

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
        *(("dec", 3),
          ("inc", 2),
          ("none", 1),
          ("rep", 4))
    )


_AlaBgpRouteMapMedMode_Type.__name__ = "Integer32"
_AlaBgpRouteMapMedMode_Object = MibTableColumn
alaBgpRouteMapMedMode = _AlaBgpRouteMapMedMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 10),
    _AlaBgpRouteMapMedMode_Type()
)
alaBgpRouteMapMedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapMedMode.setStatus("current")


class _AlaBgpRouteMapAsPrepend_Type(DisplayString):
    """Custom type alaBgpRouteMapAsPrepend based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpRouteMapAsPrepend_Type.__name__ = "DisplayString"
_AlaBgpRouteMapAsPrepend_Object = MibTableColumn
alaBgpRouteMapAsPrepend = _AlaBgpRouteMapAsPrepend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 11),
    _AlaBgpRouteMapAsPrepend_Type()
)
alaBgpRouteMapAsPrepend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapAsPrepend.setStatus("current")


class _AlaBgpRouteMapSetCommunityMode_Type(Integer32):
    """Custom type alaBgpRouteMapSetCommunityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("replace", 2))
    )


_AlaBgpRouteMapSetCommunityMode_Type.__name__ = "Integer32"
_AlaBgpRouteMapSetCommunityMode_Object = MibTableColumn
alaBgpRouteMapSetCommunityMode = _AlaBgpRouteMapSetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 12),
    _AlaBgpRouteMapSetCommunityMode_Type()
)
alaBgpRouteMapSetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapSetCommunityMode.setStatus("current")


class _AlaBgpRouteMapCommunity_Type(DisplayString):
    """Custom type alaBgpRouteMapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpRouteMapCommunity_Type.__name__ = "DisplayString"
_AlaBgpRouteMapCommunity_Object = MibTableColumn
alaBgpRouteMapCommunity = _AlaBgpRouteMapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 13),
    _AlaBgpRouteMapCommunity_Type()
)
alaBgpRouteMapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapCommunity.setStatus("current")


class _AlaBgpRouteMapMatchAsRegExp_Type(DisplayString):
    """Custom type alaBgpRouteMapMatchAsRegExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpRouteMapMatchAsRegExp_Type.__name__ = "DisplayString"
_AlaBgpRouteMapMatchAsRegExp_Object = MibTableColumn
alaBgpRouteMapMatchAsRegExp = _AlaBgpRouteMapMatchAsRegExp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 14),
    _AlaBgpRouteMapMatchAsRegExp_Type()
)
alaBgpRouteMapMatchAsRegExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapMatchAsRegExp.setStatus("current")


class _AlaBgpRouteMapMatchPrefix_Type(IpAddress):
    """Custom type alaBgpRouteMapMatchPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_AlaBgpRouteMapMatchPrefix_Object = MibTableColumn
alaBgpRouteMapMatchPrefix = _AlaBgpRouteMapMatchPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 15),
    _AlaBgpRouteMapMatchPrefix_Type()
)
alaBgpRouteMapMatchPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapMatchPrefix.setStatus("current")


class _AlaBgpRouteMapMatchMask_Type(IpAddress):
    """Custom type alaBgpRouteMapMatchMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaBgpRouteMapMatchMask_Object = MibTableColumn
alaBgpRouteMapMatchMask = _AlaBgpRouteMapMatchMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 16),
    _AlaBgpRouteMapMatchMask_Type()
)
alaBgpRouteMapMatchMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapMatchMask.setStatus("current")


class _AlaBgpRouteMapMatchCommunity_Type(DisplayString):
    """Custom type alaBgpRouteMapMatchCommunity based on DisplayString"""
    defaultValue = OctetString(" ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpRouteMapMatchCommunity_Type.__name__ = "DisplayString"
_AlaBgpRouteMapMatchCommunity_Object = MibTableColumn
alaBgpRouteMapMatchCommunity = _AlaBgpRouteMapMatchCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 17),
    _AlaBgpRouteMapMatchCommunity_Type()
)
alaBgpRouteMapMatchCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapMatchCommunity.setStatus("current")


class _AlaBgpRouteMapWeight_Type(Integer32):
    """Custom type alaBgpRouteMapWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpRouteMapWeight_Type.__name__ = "Integer32"
_AlaBgpRouteMapWeight_Object = MibTableColumn
alaBgpRouteMapWeight = _AlaBgpRouteMapWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 18),
    _AlaBgpRouteMapWeight_Type()
)
alaBgpRouteMapWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapWeight.setStatus("current")


class _AlaBgpRouteMapAction_Type(Integer32):
    """Custom type alaBgpRouteMapAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AlaBgpRouteMapAction_Type.__name__ = "Integer32"
_AlaBgpRouteMapAction_Object = MibTableColumn
alaBgpRouteMapAction = _AlaBgpRouteMapAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 19),
    _AlaBgpRouteMapAction_Type()
)
alaBgpRouteMapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapAction.setStatus("current")


class _AlaBgpRouteMapRowStatus_Type(RowStatus):
    """Custom type alaBgpRouteMapRowStatus based on RowStatus"""


_AlaBgpRouteMapRowStatus_Object = MibTableColumn
alaBgpRouteMapRowStatus = _AlaBgpRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 1, 1, 20),
    _AlaBgpRouteMapRowStatus_Type()
)
alaBgpRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRouteMapRowStatus.setStatus("current")
_AlaBgpAspathMatchListTable_Object = MibTable
alaBgpAspathMatchListTable = _AlaBgpAspathMatchListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    alaBgpAspathMatchListTable.setStatus("current")
_AlaBgpAspathMatchListEntry_Object = MibTableRow
alaBgpAspathMatchListEntry = _AlaBgpAspathMatchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 2, 1)
)
alaBgpAspathMatchListEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpAspathMatchListId"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpAspathMatchListRegExp"),
)
if mibBuilder.loadTexts:
    alaBgpAspathMatchListEntry.setStatus("current")


class _AlaBgpAspathMatchListId_Type(DisplayString):
    """Custom type alaBgpAspathMatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpAspathMatchListId_Type.__name__ = "DisplayString"
_AlaBgpAspathMatchListId_Object = MibTableColumn
alaBgpAspathMatchListId = _AlaBgpAspathMatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 2, 1, 1),
    _AlaBgpAspathMatchListId_Type()
)
alaBgpAspathMatchListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathMatchListId.setStatus("current")


class _AlaBgpAspathMatchListRegExp_Type(DisplayString):
    """Custom type alaBgpAspathMatchListRegExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpAspathMatchListRegExp_Type.__name__ = "DisplayString"
_AlaBgpAspathMatchListRegExp_Object = MibTableColumn
alaBgpAspathMatchListRegExp = _AlaBgpAspathMatchListRegExp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 2, 1, 2),
    _AlaBgpAspathMatchListRegExp_Type()
)
alaBgpAspathMatchListRegExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathMatchListRegExp.setStatus("current")


class _AlaBgpAspathMatchListPriority_Type(Integer32):
    """Custom type alaBgpAspathMatchListPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaBgpAspathMatchListPriority_Type.__name__ = "Integer32"
_AlaBgpAspathMatchListPriority_Object = MibTableColumn
alaBgpAspathMatchListPriority = _AlaBgpAspathMatchListPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 2, 1, 3),
    _AlaBgpAspathMatchListPriority_Type()
)
alaBgpAspathMatchListPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpAspathMatchListPriority.setStatus("current")


class _AlaBgpAspathMatchListAction_Type(Integer32):
    """Custom type alaBgpAspathMatchListAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AlaBgpAspathMatchListAction_Type.__name__ = "Integer32"
_AlaBgpAspathMatchListAction_Object = MibTableColumn
alaBgpAspathMatchListAction = _AlaBgpAspathMatchListAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 2, 1, 4),
    _AlaBgpAspathMatchListAction_Type()
)
alaBgpAspathMatchListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpAspathMatchListAction.setStatus("current")


class _AlaBgpAspathMatchListRowStatus_Type(RowStatus):
    """Custom type alaBgpAspathMatchListRowStatus based on RowStatus"""


_AlaBgpAspathMatchListRowStatus_Object = MibTableColumn
alaBgpAspathMatchListRowStatus = _AlaBgpAspathMatchListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 2, 1, 5),
    _AlaBgpAspathMatchListRowStatus_Type()
)
alaBgpAspathMatchListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpAspathMatchListRowStatus.setStatus("current")


class _AlaBgpAspathMatchListSubIndex_Type(Integer32):
    """Custom type alaBgpAspathMatchListSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaBgpAspathMatchListSubIndex_Type.__name__ = "Integer32"
_AlaBgpAspathMatchListSubIndex_Object = MibTableColumn
alaBgpAspathMatchListSubIndex = _AlaBgpAspathMatchListSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 2, 1, 6),
    _AlaBgpAspathMatchListSubIndex_Type()
)
alaBgpAspathMatchListSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathMatchListSubIndex.setStatus("current")
_AlaBgpPrefixMatchListTable_Object = MibTable
alaBgpPrefixMatchListTable = _AlaBgpPrefixMatchListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListTable.setStatus("current")
_AlaBgpPrefixMatchListEntry_Object = MibTableRow
alaBgpPrefixMatchListEntry = _AlaBgpPrefixMatchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3, 1)
)
alaBgpPrefixMatchListEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListId"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListAddr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListMask"),
)
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListEntry.setStatus("current")


class _AlaBgpPrefixMatchListId_Type(DisplayString):
    """Custom type alaBgpPrefixMatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpPrefixMatchListId_Type.__name__ = "DisplayString"
_AlaBgpPrefixMatchListId_Object = MibTableColumn
alaBgpPrefixMatchListId = _AlaBgpPrefixMatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3, 1, 1),
    _AlaBgpPrefixMatchListId_Type()
)
alaBgpPrefixMatchListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListId.setStatus("current")
_AlaBgpPrefixMatchListAddr_Type = IpAddress
_AlaBgpPrefixMatchListAddr_Object = MibTableColumn
alaBgpPrefixMatchListAddr = _AlaBgpPrefixMatchListAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3, 1, 2),
    _AlaBgpPrefixMatchListAddr_Type()
)
alaBgpPrefixMatchListAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListAddr.setStatus("current")
_AlaBgpPrefixMatchListMask_Type = IpAddress
_AlaBgpPrefixMatchListMask_Object = MibTableColumn
alaBgpPrefixMatchListMask = _AlaBgpPrefixMatchListMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3, 1, 3),
    _AlaBgpPrefixMatchListMask_Type()
)
alaBgpPrefixMatchListMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListMask.setStatus("current")


class _AlaBgpPrefixMatchListGE_Type(Integer32):
    """Custom type alaBgpPrefixMatchListGE based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AlaBgpPrefixMatchListGE_Type.__name__ = "Integer32"
_AlaBgpPrefixMatchListGE_Object = MibTableColumn
alaBgpPrefixMatchListGE = _AlaBgpPrefixMatchListGE_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3, 1, 4),
    _AlaBgpPrefixMatchListGE_Type()
)
alaBgpPrefixMatchListGE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListGE.setStatus("current")


class _AlaBgpPrefixMatchListLE_Type(Integer32):
    """Custom type alaBgpPrefixMatchListLE based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AlaBgpPrefixMatchListLE_Type.__name__ = "Integer32"
_AlaBgpPrefixMatchListLE_Object = MibTableColumn
alaBgpPrefixMatchListLE = _AlaBgpPrefixMatchListLE_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3, 1, 5),
    _AlaBgpPrefixMatchListLE_Type()
)
alaBgpPrefixMatchListLE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListLE.setStatus("current")


class _AlaBgpPrefixMatchListAction_Type(Integer32):
    """Custom type alaBgpPrefixMatchListAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AlaBgpPrefixMatchListAction_Type.__name__ = "Integer32"
_AlaBgpPrefixMatchListAction_Object = MibTableColumn
alaBgpPrefixMatchListAction = _AlaBgpPrefixMatchListAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3, 1, 6),
    _AlaBgpPrefixMatchListAction_Type()
)
alaBgpPrefixMatchListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListAction.setStatus("current")


class _AlaBgpPrefixMatchListRowStatus_Type(RowStatus):
    """Custom type alaBgpPrefixMatchListRowStatus based on RowStatus"""


_AlaBgpPrefixMatchListRowStatus_Object = MibTableColumn
alaBgpPrefixMatchListRowStatus = _AlaBgpPrefixMatchListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 3, 1, 7),
    _AlaBgpPrefixMatchListRowStatus_Type()
)
alaBgpPrefixMatchListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPrefixMatchListRowStatus.setStatus("current")
_AlaBgpCommunityMatchListTable_Object = MibTable
alaBgpCommunityMatchListTable = _AlaBgpCommunityMatchListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4)
)
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListTable.setStatus("current")
_AlaBgpCommunityMatchListEntry_Object = MibTableRow
alaBgpCommunityMatchListEntry = _AlaBgpCommunityMatchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4, 1)
)
alaBgpCommunityMatchListEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListId"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListString"),
)
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListEntry.setStatus("current")


class _AlaBgpCommunityMatchListId_Type(DisplayString):
    """Custom type alaBgpCommunityMatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpCommunityMatchListId_Type.__name__ = "DisplayString"
_AlaBgpCommunityMatchListId_Object = MibTableColumn
alaBgpCommunityMatchListId = _AlaBgpCommunityMatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4, 1, 1),
    _AlaBgpCommunityMatchListId_Type()
)
alaBgpCommunityMatchListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListId.setStatus("current")


class _AlaBgpCommunityMatchListString_Type(DisplayString):
    """Custom type alaBgpCommunityMatchListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpCommunityMatchListString_Type.__name__ = "DisplayString"
_AlaBgpCommunityMatchListString_Object = MibTableColumn
alaBgpCommunityMatchListString = _AlaBgpCommunityMatchListString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4, 1, 2),
    _AlaBgpCommunityMatchListString_Type()
)
alaBgpCommunityMatchListString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListString.setStatus("current")


class _AlaBgpCommunityMatchListPriority_Type(Integer32):
    """Custom type alaBgpCommunityMatchListPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaBgpCommunityMatchListPriority_Type.__name__ = "Integer32"
_AlaBgpCommunityMatchListPriority_Object = MibTableColumn
alaBgpCommunityMatchListPriority = _AlaBgpCommunityMatchListPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4, 1, 3),
    _AlaBgpCommunityMatchListPriority_Type()
)
alaBgpCommunityMatchListPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListPriority.setStatus("current")


class _AlaBgpCommunityMatchListType_Type(Integer32):
    """Custom type alaBgpCommunityMatchListType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("occur", 2))
    )


_AlaBgpCommunityMatchListType_Type.__name__ = "Integer32"
_AlaBgpCommunityMatchListType_Object = MibTableColumn
alaBgpCommunityMatchListType = _AlaBgpCommunityMatchListType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4, 1, 4),
    _AlaBgpCommunityMatchListType_Type()
)
alaBgpCommunityMatchListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListType.setStatus("current")


class _AlaBgpCommunityMatchListAction_Type(Integer32):
    """Custom type alaBgpCommunityMatchListAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AlaBgpCommunityMatchListAction_Type.__name__ = "Integer32"
_AlaBgpCommunityMatchListAction_Object = MibTableColumn
alaBgpCommunityMatchListAction = _AlaBgpCommunityMatchListAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4, 1, 5),
    _AlaBgpCommunityMatchListAction_Type()
)
alaBgpCommunityMatchListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListAction.setStatus("current")


class _AlaBgpCommunityMatchListRowStatus_Type(RowStatus):
    """Custom type alaBgpCommunityMatchListRowStatus based on RowStatus"""


_AlaBgpCommunityMatchListRowStatus_Object = MibTableColumn
alaBgpCommunityMatchListRowStatus = _AlaBgpCommunityMatchListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4, 1, 6),
    _AlaBgpCommunityMatchListRowStatus_Type()
)
alaBgpCommunityMatchListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListRowStatus.setStatus("current")


class _AlaBgpCommunityMatchListSubIndex_Type(Integer32):
    """Custom type alaBgpCommunityMatchListSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaBgpCommunityMatchListSubIndex_Type.__name__ = "Integer32"
_AlaBgpCommunityMatchListSubIndex_Object = MibTableColumn
alaBgpCommunityMatchListSubIndex = _AlaBgpCommunityMatchListSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 4, 1, 7),
    _AlaBgpCommunityMatchListSubIndex_Type()
)
alaBgpCommunityMatchListSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityMatchListSubIndex.setStatus("current")
_AlaBgpAspathPriMatchListTable_Object = MibTable
alaBgpAspathPriMatchListTable = _AlaBgpAspathPriMatchListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    alaBgpAspathPriMatchListTable.setStatus("current")
_AlaBgpAspathPriMatchListEntry_Object = MibTableRow
alaBgpAspathPriMatchListEntry = _AlaBgpAspathPriMatchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 5, 1)
)
alaBgpAspathPriMatchListEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListId"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListPriority"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListIntIdx"),
)
if mibBuilder.loadTexts:
    alaBgpAspathPriMatchListEntry.setStatus("current")


class _AlaBgpAspathPriMatchListId_Type(DisplayString):
    """Custom type alaBgpAspathPriMatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpAspathPriMatchListId_Type.__name__ = "DisplayString"
_AlaBgpAspathPriMatchListId_Object = MibTableColumn
alaBgpAspathPriMatchListId = _AlaBgpAspathPriMatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 5, 1, 1),
    _AlaBgpAspathPriMatchListId_Type()
)
alaBgpAspathPriMatchListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathPriMatchListId.setStatus("current")


class _AlaBgpAspathPriMatchListPriority_Type(Integer32):
    """Custom type alaBgpAspathPriMatchListPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaBgpAspathPriMatchListPriority_Type.__name__ = "Integer32"
_AlaBgpAspathPriMatchListPriority_Object = MibTableColumn
alaBgpAspathPriMatchListPriority = _AlaBgpAspathPriMatchListPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 5, 1, 2),
    _AlaBgpAspathPriMatchListPriority_Type()
)
alaBgpAspathPriMatchListPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathPriMatchListPriority.setStatus("current")


class _AlaBgpAspathPriMatchListIntIdx_Type(Integer32):
    """Custom type alaBgpAspathPriMatchListIntIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaBgpAspathPriMatchListIntIdx_Type.__name__ = "Integer32"
_AlaBgpAspathPriMatchListIntIdx_Object = MibTableColumn
alaBgpAspathPriMatchListIntIdx = _AlaBgpAspathPriMatchListIntIdx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 5, 1, 3),
    _AlaBgpAspathPriMatchListIntIdx_Type()
)
alaBgpAspathPriMatchListIntIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathPriMatchListIntIdx.setStatus("current")


class _AlaBgpAspathPriMatchListRegExp_Type(DisplayString):
    """Custom type alaBgpAspathPriMatchListRegExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpAspathPriMatchListRegExp_Type.__name__ = "DisplayString"
_AlaBgpAspathPriMatchListRegExp_Object = MibTableColumn
alaBgpAspathPriMatchListRegExp = _AlaBgpAspathPriMatchListRegExp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 5, 1, 4),
    _AlaBgpAspathPriMatchListRegExp_Type()
)
alaBgpAspathPriMatchListRegExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathPriMatchListRegExp.setStatus("current")


class _AlaBgpAspathPriMatchListAction_Type(Integer32):
    """Custom type alaBgpAspathPriMatchListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AlaBgpAspathPriMatchListAction_Type.__name__ = "Integer32"
_AlaBgpAspathPriMatchListAction_Object = MibTableColumn
alaBgpAspathPriMatchListAction = _AlaBgpAspathPriMatchListAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 5, 1, 5),
    _AlaBgpAspathPriMatchListAction_Type()
)
alaBgpAspathPriMatchListAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathPriMatchListAction.setStatus("current")
_AlaBgpAspathPriMatchListRowStatus_Type = RowStatus
_AlaBgpAspathPriMatchListRowStatus_Object = MibTableColumn
alaBgpAspathPriMatchListRowStatus = _AlaBgpAspathPriMatchListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 5, 1, 6),
    _AlaBgpAspathPriMatchListRowStatus_Type()
)
alaBgpAspathPriMatchListRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpAspathPriMatchListRowStatus.setStatus("current")
_AlaBgpCommunityPriMatchListTable_Object = MibTable
alaBgpCommunityPriMatchListTable = _AlaBgpCommunityPriMatchListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6)
)
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListTable.setStatus("current")
_AlaBgpCommunityPriMatchListEntry_Object = MibTableRow
alaBgpCommunityPriMatchListEntry = _AlaBgpCommunityPriMatchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6, 1)
)
alaBgpCommunityPriMatchListEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListId"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListPriority"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListIntIdx"),
)
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListEntry.setStatus("current")


class _AlaBgpCommunityPriMatchListId_Type(DisplayString):
    """Custom type alaBgpCommunityPriMatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpCommunityPriMatchListId_Type.__name__ = "DisplayString"
_AlaBgpCommunityPriMatchListId_Object = MibTableColumn
alaBgpCommunityPriMatchListId = _AlaBgpCommunityPriMatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6, 1, 1),
    _AlaBgpCommunityPriMatchListId_Type()
)
alaBgpCommunityPriMatchListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListId.setStatus("current")


class _AlaBgpCommunityPriMatchListPriority_Type(Integer32):
    """Custom type alaBgpCommunityPriMatchListPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaBgpCommunityPriMatchListPriority_Type.__name__ = "Integer32"
_AlaBgpCommunityPriMatchListPriority_Object = MibTableColumn
alaBgpCommunityPriMatchListPriority = _AlaBgpCommunityPriMatchListPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6, 1, 2),
    _AlaBgpCommunityPriMatchListPriority_Type()
)
alaBgpCommunityPriMatchListPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListPriority.setStatus("current")


class _AlaBgpCommunityPriMatchListIntIdx_Type(Integer32):
    """Custom type alaBgpCommunityPriMatchListIntIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaBgpCommunityPriMatchListIntIdx_Type.__name__ = "Integer32"
_AlaBgpCommunityPriMatchListIntIdx_Object = MibTableColumn
alaBgpCommunityPriMatchListIntIdx = _AlaBgpCommunityPriMatchListIntIdx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6, 1, 3),
    _AlaBgpCommunityPriMatchListIntIdx_Type()
)
alaBgpCommunityPriMatchListIntIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListIntIdx.setStatus("current")


class _AlaBgpCommunityPriMatchListString_Type(DisplayString):
    """Custom type alaBgpCommunityPriMatchListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpCommunityPriMatchListString_Type.__name__ = "DisplayString"
_AlaBgpCommunityPriMatchListString_Object = MibTableColumn
alaBgpCommunityPriMatchListString = _AlaBgpCommunityPriMatchListString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6, 1, 4),
    _AlaBgpCommunityPriMatchListString_Type()
)
alaBgpCommunityPriMatchListString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListString.setStatus("current")


class _AlaBgpCommunityPriMatchListType_Type(Integer32):
    """Custom type alaBgpCommunityPriMatchListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("occur", 2))
    )


_AlaBgpCommunityPriMatchListType_Type.__name__ = "Integer32"
_AlaBgpCommunityPriMatchListType_Object = MibTableColumn
alaBgpCommunityPriMatchListType = _AlaBgpCommunityPriMatchListType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6, 1, 5),
    _AlaBgpCommunityPriMatchListType_Type()
)
alaBgpCommunityPriMatchListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListType.setStatus("current")


class _AlaBgpCommunityPriMatchListAction_Type(Integer32):
    """Custom type alaBgpCommunityPriMatchListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AlaBgpCommunityPriMatchListAction_Type.__name__ = "Integer32"
_AlaBgpCommunityPriMatchListAction_Object = MibTableColumn
alaBgpCommunityPriMatchListAction = _AlaBgpCommunityPriMatchListAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6, 1, 6),
    _AlaBgpCommunityPriMatchListAction_Type()
)
alaBgpCommunityPriMatchListAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListAction.setStatus("current")
_AlaBgpCommunityPriMatchListRowStatus_Type = RowStatus
_AlaBgpCommunityPriMatchListRowStatus_Object = MibTableColumn
alaBgpCommunityPriMatchListRowStatus = _AlaBgpCommunityPriMatchListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 6, 1, 7),
    _AlaBgpCommunityPriMatchListRowStatus_Type()
)
alaBgpCommunityPriMatchListRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpCommunityPriMatchListRowStatus.setStatus("current")
_AlaBgpPrefix6MatchListTable_Object = MibTable
alaBgpPrefix6MatchListTable = _AlaBgpPrefix6MatchListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7)
)
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListTable.setStatus("current")
_AlaBgpPrefix6MatchListEntry_Object = MibTableRow
alaBgpPrefix6MatchListEntry = _AlaBgpPrefix6MatchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7, 1)
)
alaBgpPrefix6MatchListEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPrefix6MatchListId"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPrefix6MatchListAddr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPrefix6MatchListAddrLength"),
)
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListEntry.setStatus("current")


class _AlaBgpPrefix6MatchListId_Type(DisplayString):
    """Custom type alaBgpPrefix6MatchListId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )


_AlaBgpPrefix6MatchListId_Type.__name__ = "DisplayString"
_AlaBgpPrefix6MatchListId_Object = MibTableColumn
alaBgpPrefix6MatchListId = _AlaBgpPrefix6MatchListId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7, 1, 1),
    _AlaBgpPrefix6MatchListId_Type()
)
alaBgpPrefix6MatchListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListId.setStatus("current")
_AlaBgpPrefix6MatchListAddr_Type = Ipv6Address
_AlaBgpPrefix6MatchListAddr_Object = MibTableColumn
alaBgpPrefix6MatchListAddr = _AlaBgpPrefix6MatchListAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7, 1, 2),
    _AlaBgpPrefix6MatchListAddr_Type()
)
alaBgpPrefix6MatchListAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListAddr.setStatus("current")


class _AlaBgpPrefix6MatchListAddrLength_Type(Integer32):
    """Custom type alaBgpPrefix6MatchListAddrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaBgpPrefix6MatchListAddrLength_Type.__name__ = "Integer32"
_AlaBgpPrefix6MatchListAddrLength_Object = MibTableColumn
alaBgpPrefix6MatchListAddrLength = _AlaBgpPrefix6MatchListAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7, 1, 3),
    _AlaBgpPrefix6MatchListAddrLength_Type()
)
alaBgpPrefix6MatchListAddrLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListAddrLength.setStatus("current")


class _AlaBgpPrefix6MatchListGE_Type(Integer32):
    """Custom type alaBgpPrefix6MatchListGE based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AlaBgpPrefix6MatchListGE_Type.__name__ = "Integer32"
_AlaBgpPrefix6MatchListGE_Object = MibTableColumn
alaBgpPrefix6MatchListGE = _AlaBgpPrefix6MatchListGE_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7, 1, 4),
    _AlaBgpPrefix6MatchListGE_Type()
)
alaBgpPrefix6MatchListGE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListGE.setStatus("current")


class _AlaBgpPrefix6MatchListLE_Type(Integer32):
    """Custom type alaBgpPrefix6MatchListLE based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AlaBgpPrefix6MatchListLE_Type.__name__ = "Integer32"
_AlaBgpPrefix6MatchListLE_Object = MibTableColumn
alaBgpPrefix6MatchListLE = _AlaBgpPrefix6MatchListLE_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7, 1, 5),
    _AlaBgpPrefix6MatchListLE_Type()
)
alaBgpPrefix6MatchListLE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListLE.setStatus("current")


class _AlaBgpPrefix6MatchListAction_Type(Integer32):
    """Custom type alaBgpPrefix6MatchListAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AlaBgpPrefix6MatchListAction_Type.__name__ = "Integer32"
_AlaBgpPrefix6MatchListAction_Object = MibTableColumn
alaBgpPrefix6MatchListAction = _AlaBgpPrefix6MatchListAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7, 1, 6),
    _AlaBgpPrefix6MatchListAction_Type()
)
alaBgpPrefix6MatchListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListAction.setStatus("current")


class _AlaBgpPrefix6MatchListRowStatus_Type(RowStatus):
    """Custom type alaBgpPrefix6MatchListRowStatus based on RowStatus"""


_AlaBgpPrefix6MatchListRowStatus_Object = MibTableColumn
alaBgpPrefix6MatchListRowStatus = _AlaBgpPrefix6MatchListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 8, 7, 1, 7),
    _AlaBgpPrefix6MatchListRowStatus_Type()
)
alaBgpPrefix6MatchListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBgpPrefix6MatchListRowStatus.setStatus("current")
_AlaBgpRedistRouteTable_Object = MibTable
alaBgpRedistRouteTable = _AlaBgpRedistRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaBgpRedistRouteTable.setStatus("deprecated")
_AlaBgpRedistRouteEntry_Object = MibTableRow
alaBgpRedistRouteEntry = _AlaBgpRedistRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1)
)
alaBgpRedistRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteProto"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteDest"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteMask"),
)
if mibBuilder.loadTexts:
    alaBgpRedistRouteEntry.setStatus("deprecated")


class _AlaBgpRedistRouteProto_Type(Integer32):
    """Custom type alaBgpRedistRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              38,
              70,
              102,
              134,
              166,
              198,
              230)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("ospf", 6),
          ("ospf2", 38),
          ("ospf3", 70),
          ("ospf4", 102),
          ("ospf5", 134),
          ("ospf6", 166),
          ("ospf7", 198),
          ("ospf8", 230),
          ("rip", 5),
          ("static", 3))
    )


_AlaBgpRedistRouteProto_Type.__name__ = "Integer32"
_AlaBgpRedistRouteProto_Object = MibTableColumn
alaBgpRedistRouteProto = _AlaBgpRedistRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 1),
    _AlaBgpRedistRouteProto_Type()
)
alaBgpRedistRouteProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRedistRouteProto.setStatus("deprecated")
_AlaBgpRedistRouteDest_Type = IpAddress
_AlaBgpRedistRouteDest_Object = MibTableColumn
alaBgpRedistRouteDest = _AlaBgpRedistRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 2),
    _AlaBgpRedistRouteDest_Type()
)
alaBgpRedistRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRedistRouteDest.setStatus("deprecated")
_AlaBgpRedistRouteMask_Type = IpAddress
_AlaBgpRedistRouteMask_Object = MibTableColumn
alaBgpRedistRouteMask = _AlaBgpRedistRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 3),
    _AlaBgpRedistRouteMask_Type()
)
alaBgpRedistRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRedistRouteMask.setStatus("deprecated")


class _AlaBgpRedistRouteMetric_Type(Gauge32):
    """Custom type alaBgpRedistRouteMetric based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpRedistRouteMetric_Type.__name__ = "Gauge32"
_AlaBgpRedistRouteMetric_Object = MibTableColumn
alaBgpRedistRouteMetric = _AlaBgpRedistRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 4),
    _AlaBgpRedistRouteMetric_Type()
)
alaBgpRedistRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRedistRouteMetric.setStatus("deprecated")


class _AlaBgpRedistRouteLocalPref_Type(Gauge32):
    """Custom type alaBgpRedistRouteLocalPref based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpRedistRouteLocalPref_Type.__name__ = "Gauge32"
_AlaBgpRedistRouteLocalPref_Object = MibTableColumn
alaBgpRedistRouteLocalPref = _AlaBgpRedistRouteLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 5),
    _AlaBgpRedistRouteLocalPref_Type()
)
alaBgpRedistRouteLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRedistRouteLocalPref.setStatus("deprecated")


class _AlaBgpRedistRouteCommunity_Type(DisplayString):
    """Custom type alaBgpRedistRouteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpRedistRouteCommunity_Type.__name__ = "DisplayString"
_AlaBgpRedistRouteCommunity_Object = MibTableColumn
alaBgpRedistRouteCommunity = _AlaBgpRedistRouteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 6),
    _AlaBgpRedistRouteCommunity_Type()
)
alaBgpRedistRouteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRedistRouteCommunity.setStatus("deprecated")


class _AlaBgpRedistRouteSubnetMatch_Type(Integer32):
    """Custom type alaBgpRedistRouteSubnetMatch based on Integer32"""
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


_AlaBgpRedistRouteSubnetMatch_Type.__name__ = "Integer32"
_AlaBgpRedistRouteSubnetMatch_Object = MibTableColumn
alaBgpRedistRouteSubnetMatch = _AlaBgpRedistRouteSubnetMatch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 7),
    _AlaBgpRedistRouteSubnetMatch_Type()
)
alaBgpRedistRouteSubnetMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRedistRouteSubnetMatch.setStatus("deprecated")


class _AlaBgpRedistRouteEffect_Type(Integer32):
    """Custom type alaBgpRedistRouteEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotRedistribute", 2),
          ("redistribute", 1))
    )


_AlaBgpRedistRouteEffect_Type.__name__ = "Integer32"
_AlaBgpRedistRouteEffect_Object = MibTableColumn
alaBgpRedistRouteEffect = _AlaBgpRedistRouteEffect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 8),
    _AlaBgpRedistRouteEffect_Type()
)
alaBgpRedistRouteEffect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRedistRouteEffect.setStatus("deprecated")


class _AlaBgpRedistRouteRowStatus_Type(RowStatus):
    """Custom type alaBgpRedistRouteRowStatus based on RowStatus"""


_AlaBgpRedistRouteRowStatus_Object = MibTableColumn
alaBgpRedistRouteRowStatus = _AlaBgpRedistRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 9, 1, 9),
    _AlaBgpRedistRouteRowStatus_Type()
)
alaBgpRedistRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpRedistRouteRowStatus.setStatus("deprecated")
_AlaBgpDebugTable_Object = MibTable
alaBgpDebugTable = _AlaBgpDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaBgpDebugTable.setStatus("deprecated")
_AlaBgpDebugEntry_Object = MibTableRow
alaBgpDebugEntry = _AlaBgpDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 10, 1)
)
alaBgpDebugEntry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpDebugEvent"),
)
if mibBuilder.loadTexts:
    alaBgpDebugEntry.setStatus("deprecated")


class _AlaBgpDebugEvent_Type(Integer32):
    """Custom type alaBgpDebugEvent based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("aggr", 11),
          ("all", 22),
          ("damp", 1),
          ("errors", 14),
          ("fsm", 2),
          ("info", 20),
          ("keepalive", 6),
          ("local", 17),
          ("mip", 18),
          ("notify", 7),
          ("open", 5),
          ("peer", 16),
          ("policy", 8),
          ("recvupd", 3),
          ("redist", 15),
          ("restart", 21),
          ("route", 9),
          ("sendupd", 4),
          ("sync", 10),
          ("tcp", 12),
          ("tm", 19),
          ("warnings", 13))
    )


_AlaBgpDebugEvent_Type.__name__ = "Integer32"
_AlaBgpDebugEvent_Object = MibTableColumn
alaBgpDebugEvent = _AlaBgpDebugEvent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 10, 1, 1),
    _AlaBgpDebugEvent_Type()
)
alaBgpDebugEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDebugEvent.setStatus("deprecated")


class _AlaBgpDebugStatus_Type(Integer32):
    """Custom type alaBgpDebugStatus based on Integer32"""
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


_AlaBgpDebugStatus_Type.__name__ = "Integer32"
_AlaBgpDebugStatus_Object = MibTableColumn
alaBgpDebugStatus = _AlaBgpDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 10, 1, 2),
    _AlaBgpDebugStatus_Type()
)
alaBgpDebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpDebugStatus.setStatus("deprecated")


class _AlaBgpDebugDescription_Type(DisplayString):
    """Custom type alaBgpDebugDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpDebugDescription_Type.__name__ = "DisplayString"
_AlaBgpDebugDescription_Object = MibTableColumn
alaBgpDebugDescription = _AlaBgpDebugDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 10, 1, 3),
    _AlaBgpDebugDescription_Type()
)
alaBgpDebugDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpDebugDescription.setStatus("deprecated")
_AlaBgpNetwork6Table_Object = MibTable
alaBgpNetwork6Table = _AlaBgpNetwork6Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaBgpNetwork6Table.setStatus("current")
_AlaBgpNetwork6Entry_Object = MibTableRow
alaBgpNetwork6Entry = _AlaBgpNetwork6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11, 1)
)
alaBgpNetwork6Entry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6Addr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6MaskLen"),
)
if mibBuilder.loadTexts:
    alaBgpNetwork6Entry.setStatus("current")


class _AlaBgpNetwork6Addr_Type(Ipv6Address):
    """Custom type alaBgpNetwork6Addr based on Ipv6Address"""
    subtypeSpec = Ipv6Address.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AlaBgpNetwork6Addr_Type.__name__ = "Ipv6Address"
_AlaBgpNetwork6Addr_Object = MibTableColumn
alaBgpNetwork6Addr = _AlaBgpNetwork6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11, 1, 1),
    _AlaBgpNetwork6Addr_Type()
)
alaBgpNetwork6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpNetwork6Addr.setStatus("current")


class _AlaBgpNetwork6MaskLen_Type(Unsigned32):
    """Custom type alaBgpNetwork6MaskLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaBgpNetwork6MaskLen_Type.__name__ = "Unsigned32"
_AlaBgpNetwork6MaskLen_Object = MibTableColumn
alaBgpNetwork6MaskLen = _AlaBgpNetwork6MaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11, 1, 2),
    _AlaBgpNetwork6MaskLen_Type()
)
alaBgpNetwork6MaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpNetwork6MaskLen.setStatus("current")


class _AlaBgpNetwork6State_Type(Integer32):
    """Custom type alaBgpNetwork6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaBgpNetwork6State_Type.__name__ = "Integer32"
_AlaBgpNetwork6State_Object = MibTableColumn
alaBgpNetwork6State = _AlaBgpNetwork6State_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11, 1, 3),
    _AlaBgpNetwork6State_Type()
)
alaBgpNetwork6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpNetwork6State.setStatus("current")


class _AlaBgpNetwork6Metric_Type(Gauge32):
    """Custom type alaBgpNetwork6Metric based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpNetwork6Metric_Type.__name__ = "Gauge32"
_AlaBgpNetwork6Metric_Object = MibTableColumn
alaBgpNetwork6Metric = _AlaBgpNetwork6Metric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11, 1, 4),
    _AlaBgpNetwork6Metric_Type()
)
alaBgpNetwork6Metric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpNetwork6Metric.setStatus("current")


class _AlaBgpNetwork6LocalPref_Type(Gauge32):
    """Custom type alaBgpNetwork6LocalPref based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpNetwork6LocalPref_Type.__name__ = "Gauge32"
_AlaBgpNetwork6LocalPref_Object = MibTableColumn
alaBgpNetwork6LocalPref = _AlaBgpNetwork6LocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11, 1, 5),
    _AlaBgpNetwork6LocalPref_Type()
)
alaBgpNetwork6LocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpNetwork6LocalPref.setStatus("current")


class _AlaBgpNetwork6Community_Type(DisplayString):
    """Custom type alaBgpNetwork6Community based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpNetwork6Community_Type.__name__ = "DisplayString"
_AlaBgpNetwork6Community_Object = MibTableColumn
alaBgpNetwork6Community = _AlaBgpNetwork6Community_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11, 1, 6),
    _AlaBgpNetwork6Community_Type()
)
alaBgpNetwork6Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpNetwork6Community.setStatus("current")


class _AlaBgpNetwork6RowStatus_Type(RowStatus):
    """Custom type alaBgpNetwork6RowStatus based on RowStatus"""


_AlaBgpNetwork6RowStatus_Object = MibTableColumn
alaBgpNetwork6RowStatus = _AlaBgpNetwork6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 11, 1, 7),
    _AlaBgpNetwork6RowStatus_Type()
)
alaBgpNetwork6RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpNetwork6RowStatus.setStatus("current")
_AlaBgpRoute6Table_Object = MibTable
alaBgpRoute6Table = _AlaBgpRoute6Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaBgpRoute6Table.setStatus("current")
_AlaBgpRoute6Entry_Object = MibTableRow
alaBgpRoute6Entry = _AlaBgpRoute6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1)
)
alaBgpRoute6Entry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRoute6Addr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpRoute6MaskLen"),
)
if mibBuilder.loadTexts:
    alaBgpRoute6Entry.setStatus("current")
_AlaBgpRoute6Addr_Type = Ipv6Address
_AlaBgpRoute6Addr_Object = MibTableColumn
alaBgpRoute6Addr = _AlaBgpRoute6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 1),
    _AlaBgpRoute6Addr_Type()
)
alaBgpRoute6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6Addr.setStatus("current")


class _AlaBgpRoute6MaskLen_Type(Unsigned32):
    """Custom type alaBgpRoute6MaskLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaBgpRoute6MaskLen_Type.__name__ = "Unsigned32"
_AlaBgpRoute6MaskLen_Object = MibTableColumn
alaBgpRoute6MaskLen = _AlaBgpRoute6MaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 2),
    _AlaBgpRoute6MaskLen_Type()
)
alaBgpRoute6MaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6MaskLen.setStatus("current")


class _AlaBgpRoute6State_Type(Integer32):
    """Custom type alaBgpRoute6State based on Integer32"""
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


_AlaBgpRoute6State_Type.__name__ = "Integer32"
_AlaBgpRoute6State_Object = MibTableColumn
alaBgpRoute6State = _AlaBgpRoute6State_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 3),
    _AlaBgpRoute6State_Type()
)
alaBgpRoute6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6State.setStatus("current")
_AlaBgpRoute6Paths_Type = Counter32
_AlaBgpRoute6Paths_Object = MibTableColumn
alaBgpRoute6Paths = _AlaBgpRoute6Paths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 4),
    _AlaBgpRoute6Paths_Type()
)
alaBgpRoute6Paths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6Paths.setStatus("current")
_AlaBgpRoute6FeasiblePaths_Type = Counter32
_AlaBgpRoute6FeasiblePaths_Object = MibTableColumn
alaBgpRoute6FeasiblePaths = _AlaBgpRoute6FeasiblePaths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 5),
    _AlaBgpRoute6FeasiblePaths_Type()
)
alaBgpRoute6FeasiblePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6FeasiblePaths.setStatus("current")
_AlaBgpRoute6NextHop_Type = Ipv6Address
_AlaBgpRoute6NextHop_Object = MibTableColumn
alaBgpRoute6NextHop = _AlaBgpRoute6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 6),
    _AlaBgpRoute6NextHop_Type()
)
alaBgpRoute6NextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6NextHop.setStatus("current")
_AlaBgpRoute6IgpNextHop_Type = Ipv6Address
_AlaBgpRoute6IgpNextHop_Object = MibTableColumn
alaBgpRoute6IgpNextHop = _AlaBgpRoute6IgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 7),
    _AlaBgpRoute6IgpNextHop_Type()
)
alaBgpRoute6IgpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IgpNextHop.setStatus("current")


class _AlaBgpRoute6IsHidden_Type(Integer32):
    """Custom type alaBgpRoute6IsHidden based on Integer32"""
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


_AlaBgpRoute6IsHidden_Type.__name__ = "Integer32"
_AlaBgpRoute6IsHidden_Object = MibTableColumn
alaBgpRoute6IsHidden = _AlaBgpRoute6IsHidden_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 8),
    _AlaBgpRoute6IsHidden_Type()
)
alaBgpRoute6IsHidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsHidden.setStatus("current")


class _AlaBgpRoute6IsAggregate_Type(Integer32):
    """Custom type alaBgpRoute6IsAggregate based on Integer32"""
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


_AlaBgpRoute6IsAggregate_Type.__name__ = "Integer32"
_AlaBgpRoute6IsAggregate_Object = MibTableColumn
alaBgpRoute6IsAggregate = _AlaBgpRoute6IsAggregate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 9),
    _AlaBgpRoute6IsAggregate_Type()
)
alaBgpRoute6IsAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsAggregate.setStatus("current")


class _AlaBgpRoute6IsAggregateContributor_Type(Integer32):
    """Custom type alaBgpRoute6IsAggregateContributor based on Integer32"""
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


_AlaBgpRoute6IsAggregateContributor_Type.__name__ = "Integer32"
_AlaBgpRoute6IsAggregateContributor_Object = MibTableColumn
alaBgpRoute6IsAggregateContributor = _AlaBgpRoute6IsAggregateContributor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 10),
    _AlaBgpRoute6IsAggregateContributor_Type()
)
alaBgpRoute6IsAggregateContributor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsAggregateContributor.setStatus("current")


class _AlaBgpRoute6AdvNeighbors_Type(DisplayString):
    """Custom type alaBgpRoute6AdvNeighbors based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpRoute6AdvNeighbors_Type.__name__ = "DisplayString"
_AlaBgpRoute6AdvNeighbors_Object = MibTableColumn
alaBgpRoute6AdvNeighbors = _AlaBgpRoute6AdvNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 11),
    _AlaBgpRoute6AdvNeighbors_Type()
)
alaBgpRoute6AdvNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6AdvNeighbors.setStatus("current")


class _AlaBgpRoute6IsAggregateList_Type(Integer32):
    """Custom type alaBgpRoute6IsAggregateList based on Integer32"""
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


_AlaBgpRoute6IsAggregateList_Type.__name__ = "Integer32"
_AlaBgpRoute6IsAggregateList_Object = MibTableColumn
alaBgpRoute6IsAggregateList = _AlaBgpRoute6IsAggregateList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 12),
    _AlaBgpRoute6IsAggregateList_Type()
)
alaBgpRoute6IsAggregateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsAggregateList.setStatus("current")


class _AlaBgpRoute6IsAggregateWait_Type(Integer32):
    """Custom type alaBgpRoute6IsAggregateWait based on Integer32"""
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


_AlaBgpRoute6IsAggregateWait_Type.__name__ = "Integer32"
_AlaBgpRoute6IsAggregateWait_Object = MibTableColumn
alaBgpRoute6IsAggregateWait = _AlaBgpRoute6IsAggregateWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 13),
    _AlaBgpRoute6IsAggregateWait_Type()
)
alaBgpRoute6IsAggregateWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsAggregateWait.setStatus("current")


class _AlaBgpRoute6IsOnEbgpChgList_Type(Integer32):
    """Custom type alaBgpRoute6IsOnEbgpChgList based on Integer32"""
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


_AlaBgpRoute6IsOnEbgpChgList_Type.__name__ = "Integer32"
_AlaBgpRoute6IsOnEbgpChgList_Object = MibTableColumn
alaBgpRoute6IsOnEbgpChgList = _AlaBgpRoute6IsOnEbgpChgList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 14),
    _AlaBgpRoute6IsOnEbgpChgList_Type()
)
alaBgpRoute6IsOnEbgpChgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsOnEbgpChgList.setStatus("current")


class _AlaBgpRoute6IsOnIbgpClientChgList_Type(Integer32):
    """Custom type alaBgpRoute6IsOnIbgpClientChgList based on Integer32"""
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


_AlaBgpRoute6IsOnIbgpClientChgList_Type.__name__ = "Integer32"
_AlaBgpRoute6IsOnIbgpClientChgList_Object = MibTableColumn
alaBgpRoute6IsOnIbgpClientChgList = _AlaBgpRoute6IsOnIbgpClientChgList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 15),
    _AlaBgpRoute6IsOnIbgpClientChgList_Type()
)
alaBgpRoute6IsOnIbgpClientChgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsOnIbgpClientChgList.setStatus("current")


class _AlaBgpRoute6IsOnIbgpChgList_Type(Integer32):
    """Custom type alaBgpRoute6IsOnIbgpChgList based on Integer32"""
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


_AlaBgpRoute6IsOnIbgpChgList_Type.__name__ = "Integer32"
_AlaBgpRoute6IsOnIbgpChgList_Object = MibTableColumn
alaBgpRoute6IsOnIbgpChgList = _AlaBgpRoute6IsOnIbgpChgList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 16),
    _AlaBgpRoute6IsOnIbgpChgList_Type()
)
alaBgpRoute6IsOnIbgpChgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsOnIbgpChgList.setStatus("current")


class _AlaBgpRoute6IsOnLocalChgList_Type(Integer32):
    """Custom type alaBgpRoute6IsOnLocalChgList based on Integer32"""
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


_AlaBgpRoute6IsOnLocalChgList_Type.__name__ = "Integer32"
_AlaBgpRoute6IsOnLocalChgList_Object = MibTableColumn
alaBgpRoute6IsOnLocalChgList = _AlaBgpRoute6IsOnLocalChgList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 17),
    _AlaBgpRoute6IsOnLocalChgList_Type()
)
alaBgpRoute6IsOnLocalChgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsOnLocalChgList.setStatus("current")


class _AlaBgpRoute6IsOnDeleteList_Type(Integer32):
    """Custom type alaBgpRoute6IsOnDeleteList based on Integer32"""
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


_AlaBgpRoute6IsOnDeleteList_Type.__name__ = "Integer32"
_AlaBgpRoute6IsOnDeleteList_Object = MibTableColumn
alaBgpRoute6IsOnDeleteList = _AlaBgpRoute6IsOnDeleteList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 18),
    _AlaBgpRoute6IsOnDeleteList_Type()
)
alaBgpRoute6IsOnDeleteList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsOnDeleteList.setStatus("current")


class _AlaBgpRoute6IsDampened_Type(Integer32):
    """Custom type alaBgpRoute6IsDampened based on Integer32"""
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


_AlaBgpRoute6IsDampened_Type.__name__ = "Integer32"
_AlaBgpRoute6IsDampened_Object = MibTableColumn
alaBgpRoute6IsDampened = _AlaBgpRoute6IsDampened_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 12, 1, 19),
    _AlaBgpRoute6IsDampened_Type()
)
alaBgpRoute6IsDampened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpRoute6IsDampened.setStatus("current")
_AlaBgpPath6Table_Object = MibTable
alaBgpPath6Table = _AlaBgpPath6Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaBgpPath6Table.setStatus("current")
_AlaBgpPath6Entry_Object = MibTableRow
alaBgpPath6Entry = _AlaBgpPath6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1)
)
alaBgpPath6Entry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPath6Addr"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPath6MaskLen"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPath6PeerBgpId"),
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPath6SrcProto"),
)
if mibBuilder.loadTexts:
    alaBgpPath6Entry.setStatus("current")
_AlaBgpPath6Addr_Type = Ipv6Address
_AlaBgpPath6Addr_Object = MibTableColumn
alaBgpPath6Addr = _AlaBgpPath6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 1),
    _AlaBgpPath6Addr_Type()
)
alaBgpPath6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6Addr.setStatus("current")


class _AlaBgpPath6MaskLen_Type(Unsigned32):
    """Custom type alaBgpPath6MaskLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaBgpPath6MaskLen_Type.__name__ = "Unsigned32"
_AlaBgpPath6MaskLen_Object = MibTableColumn
alaBgpPath6MaskLen = _AlaBgpPath6MaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 2),
    _AlaBgpPath6MaskLen_Type()
)
alaBgpPath6MaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6MaskLen.setStatus("current")
_AlaBgpPath6PeerBgpId_Type = IpAddress
_AlaBgpPath6PeerBgpId_Object = MibTableColumn
alaBgpPath6PeerBgpId = _AlaBgpPath6PeerBgpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 3),
    _AlaBgpPath6PeerBgpId_Type()
)
alaBgpPath6PeerBgpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6PeerBgpId.setStatus("current")


class _AlaBgpPath6SrcProto_Type(Integer32):
    """Custom type alaBgpPath6SrcProto based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 11),
          ("directHost", 4),
          ("ebgp", 9),
          ("ibgp", 10),
          ("isis", 7),
          ("local", 2),
          ("network", 12),
          ("ospf", 6),
          ("other", 1),
          ("rip", 5),
          ("static", 3))
    )


_AlaBgpPath6SrcProto_Type.__name__ = "Integer32"
_AlaBgpPath6SrcProto_Object = MibTableColumn
alaBgpPath6SrcProto = _AlaBgpPath6SrcProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 4),
    _AlaBgpPath6SrcProto_Type()
)
alaBgpPath6SrcProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6SrcProto.setStatus("current")


class _AlaBgpPath6Weight_Type(Integer32):
    """Custom type alaBgpPath6Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaBgpPath6Weight_Type.__name__ = "Integer32"
_AlaBgpPath6Weight_Object = MibTableColumn
alaBgpPath6Weight = _AlaBgpPath6Weight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 5),
    _AlaBgpPath6Weight_Type()
)
alaBgpPath6Weight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6Weight.setStatus("current")
_AlaBgpPath6Pref_Type = Gauge32
_AlaBgpPath6Pref_Object = MibTableColumn
alaBgpPath6Pref = _AlaBgpPath6Pref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 6),
    _AlaBgpPath6Pref_Type()
)
alaBgpPath6Pref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6Pref.setStatus("current")


class _AlaBgpPath6State_Type(Integer32):
    """Custom type alaBgpPath6State based on Integer32"""
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
        *(("best", 1),
          ("dampened", 5),
          ("feasible", 2),
          ("none", 6),
          ("policyWait", 3),
          ("stale", 7),
          ("unSynchronized", 4))
    )


_AlaBgpPath6State_Type.__name__ = "Integer32"
_AlaBgpPath6State_Object = MibTableColumn
alaBgpPath6State = _AlaBgpPath6State_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 7),
    _AlaBgpPath6State_Type()
)
alaBgpPath6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6State.setStatus("current")


class _AlaBgpPath6Origin_Type(Integer32):
    """Custom type alaBgpPath6Origin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3),
          ("none", 9))
    )


_AlaBgpPath6Origin_Type.__name__ = "Integer32"
_AlaBgpPath6Origin_Object = MibTableColumn
alaBgpPath6Origin = _AlaBgpPath6Origin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 8),
    _AlaBgpPath6Origin_Type()
)
alaBgpPath6Origin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6Origin.setStatus("current")
_AlaBgpPath6NextHop_Type = Ipv6Address
_AlaBgpPath6NextHop_Object = MibTableColumn
alaBgpPath6NextHop = _AlaBgpPath6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 9),
    _AlaBgpPath6NextHop_Type()
)
alaBgpPath6NextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6NextHop.setStatus("current")


class _AlaBgpPath6As_Type(DisplayString):
    """Custom type alaBgpPath6As based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpPath6As_Type.__name__ = "DisplayString"
_AlaBgpPath6As_Object = MibTableColumn
alaBgpPath6As = _AlaBgpPath6As_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 10),
    _AlaBgpPath6As_Type()
)
alaBgpPath6As.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6As.setStatus("current")


class _AlaBgpPath6LocalPref_Type(Integer32):
    """Custom type alaBgpPath6LocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AlaBgpPath6LocalPref_Type.__name__ = "Integer32"
_AlaBgpPath6LocalPref_Object = MibTableColumn
alaBgpPath6LocalPref = _AlaBgpPath6LocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 11),
    _AlaBgpPath6LocalPref_Type()
)
alaBgpPath6LocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6LocalPref.setStatus("current")


class _AlaBgpPath6Med_Type(Gauge32):
    """Custom type alaBgpPath6Med based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaBgpPath6Med_Type.__name__ = "Gauge32"
_AlaBgpPath6Med_Object = MibTableColumn
alaBgpPath6Med = _AlaBgpPath6Med_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 12),
    _AlaBgpPath6Med_Type()
)
alaBgpPath6Med.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6Med.setStatus("current")


class _AlaBgpPath6Atomic_Type(Integer32):
    """Custom type alaBgpPath6Atomic based on Integer32"""
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


_AlaBgpPath6Atomic_Type.__name__ = "Integer32"
_AlaBgpPath6Atomic_Object = MibTableColumn
alaBgpPath6Atomic = _AlaBgpPath6Atomic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 13),
    _AlaBgpPath6Atomic_Type()
)
alaBgpPath6Atomic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6Atomic.setStatus("current")


class _AlaBgpPath6AggregatorAs_Type(Integer32):
    """Custom type alaBgpPath6AggregatorAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpPath6AggregatorAs_Type.__name__ = "Integer32"
_AlaBgpPath6AggregatorAs_Object = MibTableColumn
alaBgpPath6AggregatorAs = _AlaBgpPath6AggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 14),
    _AlaBgpPath6AggregatorAs_Type()
)
alaBgpPath6AggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6AggregatorAs.setStatus("current")
_AlaBgpPath6AggregatorAddr_Type = IpAddress
_AlaBgpPath6AggregatorAddr_Object = MibTableColumn
alaBgpPath6AggregatorAddr = _AlaBgpPath6AggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 15),
    _AlaBgpPath6AggregatorAddr_Type()
)
alaBgpPath6AggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6AggregatorAddr.setStatus("current")


class _AlaBgpPath6Community_Type(DisplayString):
    """Custom type alaBgpPath6Community based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpPath6Community_Type.__name__ = "DisplayString"
_AlaBgpPath6Community_Object = MibTableColumn
alaBgpPath6Community = _AlaBgpPath6Community_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 16),
    _AlaBgpPath6Community_Type()
)
alaBgpPath6Community.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6Community.setStatus("current")


class _AlaBgpPath6UnknownAttr_Type(OctetString):
    """Custom type alaBgpPath6UnknownAttr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpPath6UnknownAttr_Type.__name__ = "OctetString"
_AlaBgpPath6UnknownAttr_Object = MibTableColumn
alaBgpPath6UnknownAttr = _AlaBgpPath6UnknownAttr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 17),
    _AlaBgpPath6UnknownAttr_Type()
)
alaBgpPath6UnknownAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6UnknownAttr.setStatus("current")
_AlaBgpPath6OriginatorId_Type = IpAddress
_AlaBgpPath6OriginatorId_Object = MibTableColumn
alaBgpPath6OriginatorId = _AlaBgpPath6OriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 18),
    _AlaBgpPath6OriginatorId_Type()
)
alaBgpPath6OriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6OriginatorId.setStatus("current")


class _AlaBgpPath6ClusterList_Type(DisplayString):
    """Custom type alaBgpPath6ClusterList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaBgpPath6ClusterList_Type.__name__ = "DisplayString"
_AlaBgpPath6ClusterList_Object = MibTableColumn
alaBgpPath6ClusterList = _AlaBgpPath6ClusterList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 19),
    _AlaBgpPath6ClusterList_Type()
)
alaBgpPath6ClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6ClusterList.setStatus("current")


class _AlaBgpPath6PeerName_Type(DisplayString):
    """Custom type alaBgpPath6PeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AlaBgpPath6PeerName_Type.__name__ = "DisplayString"
_AlaBgpPath6PeerName_Object = MibTableColumn
alaBgpPath6PeerName = _AlaBgpPath6PeerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 13, 1, 20),
    _AlaBgpPath6PeerName_Type()
)
alaBgpPath6PeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPath6PeerName.setStatus("current")
_AlaBgpPeer6Table_Object = MibTable
alaBgpPeer6Table = _AlaBgpPeer6Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaBgpPeer6Table.setStatus("current")
_AlaBgpPeer6Entry_Object = MibTableRow
alaBgpPeer6Entry = _AlaBgpPeer6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1)
)
alaBgpPeer6Entry.setIndexNames(
    (0, "ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Addr"),
)
if mibBuilder.loadTexts:
    alaBgpPeer6Entry.setStatus("current")
_AlaBgpPeer6Addr_Type = Ipv6Address
_AlaBgpPeer6Addr_Object = MibTableColumn
alaBgpPeer6Addr = _AlaBgpPeer6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 1),
    _AlaBgpPeer6Addr_Type()
)
alaBgpPeer6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6Addr.setStatus("current")


class _AlaBgpPeer6AS_Type(Integer32):
    """Custom type alaBgpPeer6AS based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaBgpPeer6AS_Type.__name__ = "Integer32"
_AlaBgpPeer6AS_Object = MibTableColumn
alaBgpPeer6AS = _AlaBgpPeer6AS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 2),
    _AlaBgpPeer6AS_Type()
)
alaBgpPeer6AS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6AS.setStatus("current")


class _AlaBgpPeer6Passive_Type(Integer32):
    """Custom type alaBgpPeer6Passive based on Integer32"""
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


_AlaBgpPeer6Passive_Type.__name__ = "Integer32"
_AlaBgpPeer6Passive_Object = MibTableColumn
alaBgpPeer6Passive = _AlaBgpPeer6Passive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 3),
    _AlaBgpPeer6Passive_Type()
)
alaBgpPeer6Passive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6Passive.setStatus("current")


class _AlaBgpPeer6Name_Type(DisplayString):
    """Custom type alaBgpPeer6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AlaBgpPeer6Name_Type.__name__ = "DisplayString"
_AlaBgpPeer6Name_Object = MibTableColumn
alaBgpPeer6Name = _AlaBgpPeer6Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 4),
    _AlaBgpPeer6Name_Type()
)
alaBgpPeer6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6Name.setStatus("current")


class _AlaBgpPeer6MultiHop_Type(Integer32):
    """Custom type alaBgpPeer6MultiHop based on Integer32"""
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


_AlaBgpPeer6MultiHop_Type.__name__ = "Integer32"
_AlaBgpPeer6MultiHop_Object = MibTableColumn
alaBgpPeer6MultiHop = _AlaBgpPeer6MultiHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 5),
    _AlaBgpPeer6MultiHop_Type()
)
alaBgpPeer6MultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6MultiHop.setStatus("current")


class _AlaBgpPeer6MaxPrefix_Type(Gauge32):
    """Custom type alaBgpPeer6MaxPrefix based on Gauge32"""
    defaultValue = 5000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaBgpPeer6MaxPrefix_Type.__name__ = "Gauge32"
_AlaBgpPeer6MaxPrefix_Object = MibTableColumn
alaBgpPeer6MaxPrefix = _AlaBgpPeer6MaxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 6),
    _AlaBgpPeer6MaxPrefix_Type()
)
alaBgpPeer6MaxPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6MaxPrefix.setStatus("current")


class _AlaBgpPeer6MaxPrefixWarnOnly_Type(Integer32):
    """Custom type alaBgpPeer6MaxPrefixWarnOnly based on Integer32"""
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


_AlaBgpPeer6MaxPrefixWarnOnly_Type.__name__ = "Integer32"
_AlaBgpPeer6MaxPrefixWarnOnly_Object = MibTableColumn
alaBgpPeer6MaxPrefixWarnOnly = _AlaBgpPeer6MaxPrefixWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 7),
    _AlaBgpPeer6MaxPrefixWarnOnly_Type()
)
alaBgpPeer6MaxPrefixWarnOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6MaxPrefixWarnOnly.setStatus("current")


class _AlaBgpPeer6NextHopSelf_Type(Integer32):
    """Custom type alaBgpPeer6NextHopSelf based on Integer32"""
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


_AlaBgpPeer6NextHopSelf_Type.__name__ = "Integer32"
_AlaBgpPeer6NextHopSelf_Object = MibTableColumn
alaBgpPeer6NextHopSelf = _AlaBgpPeer6NextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 8),
    _AlaBgpPeer6NextHopSelf_Type()
)
alaBgpPeer6NextHopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6NextHopSelf.setStatus("current")


class _AlaBgpPeer6SoftReconfig_Type(Integer32):
    """Custom type alaBgpPeer6SoftReconfig based on Integer32"""
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


_AlaBgpPeer6SoftReconfig_Type.__name__ = "Integer32"
_AlaBgpPeer6SoftReconfig_Object = MibTableColumn
alaBgpPeer6SoftReconfig = _AlaBgpPeer6SoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 9),
    _AlaBgpPeer6SoftReconfig_Type()
)
alaBgpPeer6SoftReconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6SoftReconfig.setStatus("current")


class _AlaBgpPeer6InSoftReset_Type(Integer32):
    """Custom type alaBgpPeer6InSoftReset based on Integer32"""
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


_AlaBgpPeer6InSoftReset_Type.__name__ = "Integer32"
_AlaBgpPeer6InSoftReset_Object = MibTableColumn
alaBgpPeer6InSoftReset = _AlaBgpPeer6InSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 10),
    _AlaBgpPeer6InSoftReset_Type()
)
alaBgpPeer6InSoftReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6InSoftReset.setStatus("current")


class _AlaBgpPeer6Ipv4Unicast_Type(Integer32):
    """Custom type alaBgpPeer6Ipv4Unicast based on Integer32"""
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


_AlaBgpPeer6Ipv4Unicast_Type.__name__ = "Integer32"
_AlaBgpPeer6Ipv4Unicast_Object = MibTableColumn
alaBgpPeer6Ipv4Unicast = _AlaBgpPeer6Ipv4Unicast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 11),
    _AlaBgpPeer6Ipv4Unicast_Type()
)
alaBgpPeer6Ipv4Unicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6Ipv4Unicast.setStatus("current")


class _AlaBgpPeer6Ipv4Multicast_Type(Integer32):
    """Custom type alaBgpPeer6Ipv4Multicast based on Integer32"""
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


_AlaBgpPeer6Ipv4Multicast_Type.__name__ = "Integer32"
_AlaBgpPeer6Ipv4Multicast_Object = MibTableColumn
alaBgpPeer6Ipv4Multicast = _AlaBgpPeer6Ipv4Multicast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 12),
    _AlaBgpPeer6Ipv4Multicast_Type()
)
alaBgpPeer6Ipv4Multicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6Ipv4Multicast.setStatus("current")
_AlaBgpPeer6RcvdRtRefreshMsgs_Type = Counter32
_AlaBgpPeer6RcvdRtRefreshMsgs_Object = MibTableColumn
alaBgpPeer6RcvdRtRefreshMsgs = _AlaBgpPeer6RcvdRtRefreshMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 13),
    _AlaBgpPeer6RcvdRtRefreshMsgs_Type()
)
alaBgpPeer6RcvdRtRefreshMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6RcvdRtRefreshMsgs.setStatus("current")
_AlaBgpPeer6SentRtRefreshMsgs_Type = Counter32
_AlaBgpPeer6SentRtRefreshMsgs_Object = MibTableColumn
alaBgpPeer6SentRtRefreshMsgs = _AlaBgpPeer6SentRtRefreshMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 14),
    _AlaBgpPeer6SentRtRefreshMsgs_Type()
)
alaBgpPeer6SentRtRefreshMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6SentRtRefreshMsgs.setStatus("current")


class _AlaBgpPeer6RouteMapOut_Type(DisplayString):
    """Custom type alaBgpPeer6RouteMapOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6RouteMapOut_Type.__name__ = "DisplayString"
_AlaBgpPeer6RouteMapOut_Object = MibTableColumn
alaBgpPeer6RouteMapOut = _AlaBgpPeer6RouteMapOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 15),
    _AlaBgpPeer6RouteMapOut_Type()
)
alaBgpPeer6RouteMapOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6RouteMapOut.setStatus("current")


class _AlaBgpPeer6RouteMapIn_Type(DisplayString):
    """Custom type alaBgpPeer6RouteMapIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6RouteMapIn_Type.__name__ = "DisplayString"
_AlaBgpPeer6RouteMapIn_Object = MibTableColumn
alaBgpPeer6RouteMapIn = _AlaBgpPeer6RouteMapIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 16),
    _AlaBgpPeer6RouteMapIn_Type()
)
alaBgpPeer6RouteMapIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6RouteMapIn.setStatus("current")
_AlaBgpPeer6LocalAddr_Type = Ipv6Address
_AlaBgpPeer6LocalAddr_Object = MibTableColumn
alaBgpPeer6LocalAddr = _AlaBgpPeer6LocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 17),
    _AlaBgpPeer6LocalAddr_Type()
)
alaBgpPeer6LocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6LocalAddr.setStatus("current")


class _AlaBgpPeer6LastDownReason_Type(Integer32):
    """Custom type alaBgpPeer6LastDownReason based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("badMsg", 4),
          ("connectionTimeout", 2),
          ("fsmUnexpectedEvent", 5),
          ("holdTimeout", 3),
          ("none", 9),
          ("peerClosed", 6),
          ("peerNotify", 7),
          ("transportError", 8),
          ("userRequest", 1))
    )


_AlaBgpPeer6LastDownReason_Type.__name__ = "Integer32"
_AlaBgpPeer6LastDownReason_Object = MibTableColumn
alaBgpPeer6LastDownReason = _AlaBgpPeer6LastDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 18),
    _AlaBgpPeer6LastDownReason_Type()
)
alaBgpPeer6LastDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LastDownReason.setStatus("current")
_AlaBgpPeer6LastDownTime_Type = TimeTicks
_AlaBgpPeer6LastDownTime_Object = MibTableColumn
alaBgpPeer6LastDownTime = _AlaBgpPeer6LastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 19),
    _AlaBgpPeer6LastDownTime_Type()
)
alaBgpPeer6LastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LastDownTime.setStatus("current")
_AlaBgpPeer6LastReadTime_Type = TimeTicks
_AlaBgpPeer6LastReadTime_Object = MibTableColumn
alaBgpPeer6LastReadTime = _AlaBgpPeer6LastReadTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 20),
    _AlaBgpPeer6LastReadTime_Type()
)
alaBgpPeer6LastReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LastReadTime.setStatus("current")
_AlaBgpPeer6RcvdNotifyMsgs_Type = Counter32
_AlaBgpPeer6RcvdNotifyMsgs_Object = MibTableColumn
alaBgpPeer6RcvdNotifyMsgs = _AlaBgpPeer6RcvdNotifyMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 21),
    _AlaBgpPeer6RcvdNotifyMsgs_Type()
)
alaBgpPeer6RcvdNotifyMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6RcvdNotifyMsgs.setStatus("current")
_AlaBgpPeer6SentNotifyMsgs_Type = Counter32
_AlaBgpPeer6SentNotifyMsgs_Object = MibTableColumn
alaBgpPeer6SentNotifyMsgs = _AlaBgpPeer6SentNotifyMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 22),
    _AlaBgpPeer6SentNotifyMsgs_Type()
)
alaBgpPeer6SentNotifyMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6SentNotifyMsgs.setStatus("current")


class _AlaBgpPeer6LastSentNotifyReason_Type(Integer32):
    """Custom type alaBgpPeer6LastSentNotifyReason based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("ceaseAdminReset", 27),
          ("ceaseAdminShutdown", 25),
          ("ceaseConnCollisionResolution", 30),
          ("ceaseConnRejected", 28),
          ("ceaseMaxPrefixReached", 24),
          ("ceaseOtherConfChange", 29),
          ("ceaseOutOfResources", 31),
          ("ceasePeerDeconfigured", 26),
          ("fsmError", 23),
          ("holdTimeout", 22),
          ("msghdrBadLen", 2),
          ("msghdrBadType", 3),
          ("msghdrNoSync", 1),
          ("none", 32),
          ("openAuthFail", 8),
          ("openBadAs", 5),
          ("openBadHoldtime", 9),
          ("openBadId", 6),
          ("openUnsuppCapability", 10),
          ("openUnsuppOption", 7),
          ("openUnsuppVersion", 4),
          ("updateAsLoop", 17),
          ("updateBadAspath", 21),
          ("updateBadAttrFlags", 14),
          ("updateBadAttrLen", 15),
          ("updateBadNet", 20),
          ("updateBadNexthop", 18),
          ("updateBadOptAttr", 19),
          ("updateBadOrigin", 16),
          ("updateMalformAttr", 11),
          ("updateMissingWknwnAttr", 13),
          ("updateUnsuppWknwnAttr", 12))
    )


_AlaBgpPeer6LastSentNotifyReason_Type.__name__ = "Integer32"
_AlaBgpPeer6LastSentNotifyReason_Object = MibTableColumn
alaBgpPeer6LastSentNotifyReason = _AlaBgpPeer6LastSentNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 23),
    _AlaBgpPeer6LastSentNotifyReason_Type()
)
alaBgpPeer6LastSentNotifyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LastSentNotifyReason.setStatus("current")


class _AlaBgpPeer6LastRecvNotifyReason_Type(Integer32):
    """Custom type alaBgpPeer6LastRecvNotifyReason based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("ceaseAdminReset", 27),
          ("ceaseAdminShutdown", 25),
          ("ceaseConnCollisionResolution", 30),
          ("ceaseConnRejected", 28),
          ("ceaseMaxPrefixReached", 24),
          ("ceaseOtherConfChange", 29),
          ("ceaseOutOfResources", 31),
          ("ceasePeerDeconfigured", 26),
          ("fsmError", 23),
          ("holdTimeout", 22),
          ("msghdrBadLen", 2),
          ("msghdrBadType", 3),
          ("msghdrNoSync", 1),
          ("none", 32),
          ("openAuthFail", 8),
          ("openBadAs", 5),
          ("openBadHoldtime", 9),
          ("openBadId", 6),
          ("openUnsuppCapability", 10),
          ("openUnsuppOption", 7),
          ("openUnsuppVersion", 4),
          ("updateAsLoop", 17),
          ("updateBadAspath", 21),
          ("updateBadAttrFlags", 14),
          ("updateBadAttrLen", 15),
          ("updateBadNet", 20),
          ("updateBadNexthop", 18),
          ("updateBadOptAttr", 19),
          ("updateBadOrigin", 16),
          ("updateMalformAttr", 11),
          ("updateMissingWknwnAttr", 13),
          ("updateUnsuppWknwnAttr", 12))
    )


_AlaBgpPeer6LastRecvNotifyReason_Type.__name__ = "Integer32"
_AlaBgpPeer6LastRecvNotifyReason_Object = MibTableColumn
alaBgpPeer6LastRecvNotifyReason = _AlaBgpPeer6LastRecvNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 24),
    _AlaBgpPeer6LastRecvNotifyReason_Type()
)
alaBgpPeer6LastRecvNotifyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LastRecvNotifyReason.setStatus("current")
_AlaBgpPeer6RcvdPrefixes_Type = Counter32
_AlaBgpPeer6RcvdPrefixes_Object = MibTableColumn
alaBgpPeer6RcvdPrefixes = _AlaBgpPeer6RcvdPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 25),
    _AlaBgpPeer6RcvdPrefixes_Type()
)
alaBgpPeer6RcvdPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6RcvdPrefixes.setStatus("current")
_AlaBgpPeer6DownTransitions_Type = Counter32
_AlaBgpPeer6DownTransitions_Object = MibTableColumn
alaBgpPeer6DownTransitions = _AlaBgpPeer6DownTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 26),
    _AlaBgpPeer6DownTransitions_Type()
)
alaBgpPeer6DownTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6DownTransitions.setStatus("current")


class _AlaBgpPeer6Type_Type(Integer32):
    """Custom type alaBgpPeer6Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_AlaBgpPeer6Type_Type.__name__ = "Integer32"
_AlaBgpPeer6Type_Object = MibTableColumn
alaBgpPeer6Type = _AlaBgpPeer6Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 27),
    _AlaBgpPeer6Type_Type()
)
alaBgpPeer6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6Type.setStatus("current")


class _AlaBgpPeer6ClearCounter_Type(Integer32):
    """Custom type alaBgpPeer6ClearCounter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaBgpPeer6ClearCounter_Type.__name__ = "Integer32"
_AlaBgpPeer6ClearCounter_Object = MibTableColumn
alaBgpPeer6ClearCounter = _AlaBgpPeer6ClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 28),
    _AlaBgpPeer6ClearCounter_Type()
)
alaBgpPeer6ClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6ClearCounter.setStatus("current")


class _AlaBgpPeer6AutoReStart_Type(Integer32):
    """Custom type alaBgpPeer6AutoReStart based on Integer32"""
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


_AlaBgpPeer6AutoReStart_Type.__name__ = "Integer32"
_AlaBgpPeer6AutoReStart_Object = MibTableColumn
alaBgpPeer6AutoReStart = _AlaBgpPeer6AutoReStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 29),
    _AlaBgpPeer6AutoReStart_Type()
)
alaBgpPeer6AutoReStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6AutoReStart.setStatus("current")


class _AlaBgpPeer6ClientStatus_Type(Integer32):
    """Custom type alaBgpPeer6ClientStatus based on Integer32"""
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


_AlaBgpPeer6ClientStatus_Type.__name__ = "Integer32"
_AlaBgpPeer6ClientStatus_Object = MibTableColumn
alaBgpPeer6ClientStatus = _AlaBgpPeer6ClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 30),
    _AlaBgpPeer6ClientStatus_Type()
)
alaBgpPeer6ClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6ClientStatus.setStatus("current")


class _AlaBgpPeer6ConfedStatus_Type(Integer32):
    """Custom type alaBgpPeer6ConfedStatus based on Integer32"""
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


_AlaBgpPeer6ConfedStatus_Type.__name__ = "Integer32"
_AlaBgpPeer6ConfedStatus_Object = MibTableColumn
alaBgpPeer6ConfedStatus = _AlaBgpPeer6ConfedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 31),
    _AlaBgpPeer6ConfedStatus_Type()
)
alaBgpPeer6ConfedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6ConfedStatus.setStatus("current")


class _AlaBgpPeer6RemovePrivateAs_Type(Integer32):
    """Custom type alaBgpPeer6RemovePrivateAs based on Integer32"""
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


_AlaBgpPeer6RemovePrivateAs_Type.__name__ = "Integer32"
_AlaBgpPeer6RemovePrivateAs_Object = MibTableColumn
alaBgpPeer6RemovePrivateAs = _AlaBgpPeer6RemovePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 32),
    _AlaBgpPeer6RemovePrivateAs_Type()
)
alaBgpPeer6RemovePrivateAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6RemovePrivateAs.setStatus("current")


class _AlaBgpPeer6TTL_Type(Integer32):
    """Custom type alaBgpPeer6TTL based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaBgpPeer6TTL_Type.__name__ = "Integer32"
_AlaBgpPeer6TTL_Object = MibTableColumn
alaBgpPeer6TTL = _AlaBgpPeer6TTL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 33),
    _AlaBgpPeer6TTL_Type()
)
alaBgpPeer6TTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6TTL.setStatus("current")


class _AlaBgpPeer6AspathListOut_Type(DisplayString):
    """Custom type alaBgpPeer6AspathListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6AspathListOut_Type.__name__ = "DisplayString"
_AlaBgpPeer6AspathListOut_Object = MibTableColumn
alaBgpPeer6AspathListOut = _AlaBgpPeer6AspathListOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 34),
    _AlaBgpPeer6AspathListOut_Type()
)
alaBgpPeer6AspathListOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6AspathListOut.setStatus("current")


class _AlaBgpPeer6AspathListIn_Type(DisplayString):
    """Custom type alaBgpPeer6AspathListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6AspathListIn_Type.__name__ = "DisplayString"
_AlaBgpPeer6AspathListIn_Object = MibTableColumn
alaBgpPeer6AspathListIn = _AlaBgpPeer6AspathListIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 35),
    _AlaBgpPeer6AspathListIn_Type()
)
alaBgpPeer6AspathListIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6AspathListIn.setStatus("current")


class _AlaBgpPeer6PrefixListOut_Type(DisplayString):
    """Custom type alaBgpPeer6PrefixListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6PrefixListOut_Type.__name__ = "DisplayString"
_AlaBgpPeer6PrefixListOut_Object = MibTableColumn
alaBgpPeer6PrefixListOut = _AlaBgpPeer6PrefixListOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 36),
    _AlaBgpPeer6PrefixListOut_Type()
)
alaBgpPeer6PrefixListOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6PrefixListOut.setStatus("current")


class _AlaBgpPeer6PrefixListIn_Type(DisplayString):
    """Custom type alaBgpPeer6PrefixListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6PrefixListIn_Type.__name__ = "DisplayString"
_AlaBgpPeer6PrefixListIn_Object = MibTableColumn
alaBgpPeer6PrefixListIn = _AlaBgpPeer6PrefixListIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 37),
    _AlaBgpPeer6PrefixListIn_Type()
)
alaBgpPeer6PrefixListIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6PrefixListIn.setStatus("current")


class _AlaBgpPeer6CommunityListOut_Type(DisplayString):
    """Custom type alaBgpPeer6CommunityListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6CommunityListOut_Type.__name__ = "DisplayString"
_AlaBgpPeer6CommunityListOut_Object = MibTableColumn
alaBgpPeer6CommunityListOut = _AlaBgpPeer6CommunityListOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 38),
    _AlaBgpPeer6CommunityListOut_Type()
)
alaBgpPeer6CommunityListOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6CommunityListOut.setStatus("current")


class _AlaBgpPeer6CommunityListIn_Type(DisplayString):
    """Custom type alaBgpPeer6CommunityListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6CommunityListIn_Type.__name__ = "DisplayString"
_AlaBgpPeer6CommunityListIn_Object = MibTableColumn
alaBgpPeer6CommunityListIn = _AlaBgpPeer6CommunityListIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 39),
    _AlaBgpPeer6CommunityListIn_Type()
)
alaBgpPeer6CommunityListIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6CommunityListIn.setStatus("current")


class _AlaBgpPeer6Restart_Type(Integer32):
    """Custom type alaBgpPeer6Restart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_AlaBgpPeer6Restart_Type.__name__ = "Integer32"
_AlaBgpPeer6Restart_Object = MibTableColumn
alaBgpPeer6Restart = _AlaBgpPeer6Restart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 40),
    _AlaBgpPeer6Restart_Type()
)
alaBgpPeer6Restart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6Restart.setStatus("current")


class _AlaBgpPeer6DefaultOriginate_Type(Integer32):
    """Custom type alaBgpPeer6DefaultOriginate based on Integer32"""
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


_AlaBgpPeer6DefaultOriginate_Type.__name__ = "Integer32"
_AlaBgpPeer6DefaultOriginate_Object = MibTableColumn
alaBgpPeer6DefaultOriginate = _AlaBgpPeer6DefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 41),
    _AlaBgpPeer6DefaultOriginate_Type()
)
alaBgpPeer6DefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6DefaultOriginate.setStatus("current")


class _AlaBgpPeer6ReconfigureInBound_Type(Integer32):
    """Custom type alaBgpPeer6ReconfigureInBound based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reconfigure", 1)
    )


_AlaBgpPeer6ReconfigureInBound_Type.__name__ = "Integer32"
_AlaBgpPeer6ReconfigureInBound_Object = MibTableColumn
alaBgpPeer6ReconfigureInBound = _AlaBgpPeer6ReconfigureInBound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 42),
    _AlaBgpPeer6ReconfigureInBound_Type()
)
alaBgpPeer6ReconfigureInBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6ReconfigureInBound.setStatus("current")


class _AlaBgpPeer6ReconfigureOutBound_Type(Integer32):
    """Custom type alaBgpPeer6ReconfigureOutBound based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reconfigure", 1)
    )


_AlaBgpPeer6ReconfigureOutBound_Type.__name__ = "Integer32"
_AlaBgpPeer6ReconfigureOutBound_Object = MibTableColumn
alaBgpPeer6ReconfigureOutBound = _AlaBgpPeer6ReconfigureOutBound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 43),
    _AlaBgpPeer6ReconfigureOutBound_Type()
)
alaBgpPeer6ReconfigureOutBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6ReconfigureOutBound.setStatus("current")


class _AlaBgpPeer6MD5Key_Type(DisplayString):
    """Custom type alaBgpPeer6MD5Key based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AlaBgpPeer6MD5Key_Type.__name__ = "DisplayString"
_AlaBgpPeer6MD5Key_Object = MibTableColumn
alaBgpPeer6MD5Key = _AlaBgpPeer6MD5Key_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 44),
    _AlaBgpPeer6MD5Key_Type()
)
alaBgpPeer6MD5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6MD5Key.setStatus("current")


class _AlaBgpPeer6MD5KeyEncrypt_Type(OctetString):
    """Custom type alaBgpPeer6MD5KeyEncrypt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AlaBgpPeer6MD5KeyEncrypt_Type.__name__ = "OctetString"
_AlaBgpPeer6MD5KeyEncrypt_Object = MibTableColumn
alaBgpPeer6MD5KeyEncrypt = _AlaBgpPeer6MD5KeyEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 45),
    _AlaBgpPeer6MD5KeyEncrypt_Type()
)
alaBgpPeer6MD5KeyEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6MD5KeyEncrypt.setStatus("current")


class _AlaBgpPeer6RowStatus_Type(RowStatus):
    """Custom type alaBgpPeer6RowStatus based on RowStatus"""


_AlaBgpPeer6RowStatus_Object = MibTableColumn
alaBgpPeer6RowStatus = _AlaBgpPeer6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 46),
    _AlaBgpPeer6RowStatus_Type()
)
alaBgpPeer6RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6RowStatus.setStatus("current")
_AlaBgpPeer6UpTransitions_Type = Counter32
_AlaBgpPeer6UpTransitions_Object = MibTableColumn
alaBgpPeer6UpTransitions = _AlaBgpPeer6UpTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 47),
    _AlaBgpPeer6UpTransitions_Type()
)
alaBgpPeer6UpTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6UpTransitions.setStatus("current")
_AlaBgpPeer6LastWriteTime_Type = TimeTicks
_AlaBgpPeer6LastWriteTime_Object = MibTableColumn
alaBgpPeer6LastWriteTime = _AlaBgpPeer6LastWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 48),
    _AlaBgpPeer6LastWriteTime_Type()
)
alaBgpPeer6LastWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LastWriteTime.setStatus("current")
_AlaBgpPeer6RcvdMsgs_Type = Counter32
_AlaBgpPeer6RcvdMsgs_Object = MibTableColumn
alaBgpPeer6RcvdMsgs = _AlaBgpPeer6RcvdMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 49),
    _AlaBgpPeer6RcvdMsgs_Type()
)
alaBgpPeer6RcvdMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6RcvdMsgs.setStatus("current")
_AlaBgpPeer6SentMsgs_Type = Counter32
_AlaBgpPeer6SentMsgs_Object = MibTableColumn
alaBgpPeer6SentMsgs = _AlaBgpPeer6SentMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 50),
    _AlaBgpPeer6SentMsgs_Type()
)
alaBgpPeer6SentMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6SentMsgs.setStatus("current")
_AlaBgpPeer6RcvdUpdMsgs_Type = Counter32
_AlaBgpPeer6RcvdUpdMsgs_Object = MibTableColumn
alaBgpPeer6RcvdUpdMsgs = _AlaBgpPeer6RcvdUpdMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 51),
    _AlaBgpPeer6RcvdUpdMsgs_Type()
)
alaBgpPeer6RcvdUpdMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6RcvdUpdMsgs.setStatus("current")
_AlaBgpPeer6SentUpdMsgs_Type = Counter32
_AlaBgpPeer6SentUpdMsgs_Object = MibTableColumn
alaBgpPeer6SentUpdMsgs = _AlaBgpPeer6SentUpdMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 52),
    _AlaBgpPeer6SentUpdMsgs_Type()
)
alaBgpPeer6SentUpdMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6SentUpdMsgs.setStatus("current")
_AlaBgpPeer6LastTransitionTime_Type = TimeTicks
_AlaBgpPeer6LastTransitionTime_Object = MibTableColumn
alaBgpPeer6LastTransitionTime = _AlaBgpPeer6LastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 53),
    _AlaBgpPeer6LastTransitionTime_Type()
)
alaBgpPeer6LastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LastTransitionTime.setStatus("current")
_AlaBgpPeer6LastUpTime_Type = TimeTicks
_AlaBgpPeer6LastUpTime_Object = MibTableColumn
alaBgpPeer6LastUpTime = _AlaBgpPeer6LastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 54),
    _AlaBgpPeer6LastUpTime_Type()
)
alaBgpPeer6LastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LastUpTime.setStatus("current")
_AlaBgpPeer6BgpId_Type = IpAddress
_AlaBgpPeer6BgpId_Object = MibTableColumn
alaBgpPeer6BgpId = _AlaBgpPeer6BgpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 55),
    _AlaBgpPeer6BgpId_Type()
)
alaBgpPeer6BgpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6BgpId.setStatus("current")


class _AlaBgpPeer6LocalIntfName_Type(DisplayString):
    """Custom type alaBgpPeer6LocalIntfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaBgpPeer6LocalIntfName_Type.__name__ = "DisplayString"
_AlaBgpPeer6LocalIntfName_Object = MibTableColumn
alaBgpPeer6LocalIntfName = _AlaBgpPeer6LocalIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 56),
    _AlaBgpPeer6LocalIntfName_Type()
)
alaBgpPeer6LocalIntfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6LocalIntfName.setStatus("current")


class _AlaBgpPeer6RestartTime_Type(Integer32):
    """Custom type alaBgpPeer6RestartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AlaBgpPeer6RestartTime_Type.__name__ = "Integer32"
_AlaBgpPeer6RestartTime_Object = MibTableColumn
alaBgpPeer6RestartTime = _AlaBgpPeer6RestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 57),
    _AlaBgpPeer6RestartTime_Type()
)
alaBgpPeer6RestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6RestartTime.setStatus("current")


class _AlaBgpPeer6RestartState_Type(Integer32):
    """Custom type alaBgpPeer6RestartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("notRestarting", 1),
          ("restarting", 2))
    )


_AlaBgpPeer6RestartState_Type.__name__ = "Integer32"
_AlaBgpPeer6RestartState_Object = MibTableColumn
alaBgpPeer6RestartState = _AlaBgpPeer6RestartState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 58),
    _AlaBgpPeer6RestartState_Type()
)
alaBgpPeer6RestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6RestartState.setStatus("current")


class _AlaBgpPeer6RestartFwdState_Type(Integer32):
    """Custom type alaBgpPeer6RestartFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPreserved", 1),
          ("preserved", 2))
    )


_AlaBgpPeer6RestartFwdState_Type.__name__ = "Integer32"
_AlaBgpPeer6RestartFwdState_Object = MibTableColumn
alaBgpPeer6RestartFwdState = _AlaBgpPeer6RestartFwdState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 59),
    _AlaBgpPeer6RestartFwdState_Type()
)
alaBgpPeer6RestartFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6RestartFwdState.setStatus("current")


class _AlaBgpPeer6Ipv6Unicast_Type(Integer32):
    """Custom type alaBgpPeer6Ipv6Unicast based on Integer32"""
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


_AlaBgpPeer6Ipv6Unicast_Type.__name__ = "Integer32"
_AlaBgpPeer6Ipv6Unicast_Object = MibTableColumn
alaBgpPeer6Ipv6Unicast = _AlaBgpPeer6Ipv6Unicast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 60),
    _AlaBgpPeer6Ipv6Unicast_Type()
)
alaBgpPeer6Ipv6Unicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6Ipv6Unicast.setStatus("current")


class _AlaBgpPeer6HoldTime_Type(Integer32):
    """Custom type alaBgpPeer6HoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_AlaBgpPeer6HoldTime_Type.__name__ = "Integer32"
_AlaBgpPeer6HoldTime_Object = MibTableColumn
alaBgpPeer6HoldTime = _AlaBgpPeer6HoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 61),
    _AlaBgpPeer6HoldTime_Type()
)
alaBgpPeer6HoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6HoldTime.setStatus("current")


class _AlaBgpPeer6KeepAlive_Type(Integer32):
    """Custom type alaBgpPeer6KeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_AlaBgpPeer6KeepAlive_Type.__name__ = "Integer32"
_AlaBgpPeer6KeepAlive_Object = MibTableColumn
alaBgpPeer6KeepAlive = _AlaBgpPeer6KeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 62),
    _AlaBgpPeer6KeepAlive_Type()
)
alaBgpPeer6KeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6KeepAlive.setStatus("current")


class _AlaBgpPeer6ConnRetryInterval_Type(Integer32):
    """Custom type alaBgpPeer6ConnRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaBgpPeer6ConnRetryInterval_Type.__name__ = "Integer32"
_AlaBgpPeer6ConnRetryInterval_Object = MibTableColumn
alaBgpPeer6ConnRetryInterval = _AlaBgpPeer6ConnRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 63),
    _AlaBgpPeer6ConnRetryInterval_Type()
)
alaBgpPeer6ConnRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6ConnRetryInterval.setStatus("current")


class _AlaBgpPeer6HoldTimeConfigured_Type(Integer32):
    """Custom type alaBgpPeer6HoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_AlaBgpPeer6HoldTimeConfigured_Type.__name__ = "Integer32"
_AlaBgpPeer6HoldTimeConfigured_Object = MibTableColumn
alaBgpPeer6HoldTimeConfigured = _AlaBgpPeer6HoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 64),
    _AlaBgpPeer6HoldTimeConfigured_Type()
)
alaBgpPeer6HoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6HoldTimeConfigured.setStatus("current")


class _AlaBgpPeer6KeepAliveConfigured_Type(Integer32):
    """Custom type alaBgpPeer6KeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_AlaBgpPeer6KeepAliveConfigured_Type.__name__ = "Integer32"
_AlaBgpPeer6KeepAliveConfigured_Object = MibTableColumn
alaBgpPeer6KeepAliveConfigured = _AlaBgpPeer6KeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 65),
    _AlaBgpPeer6KeepAliveConfigured_Type()
)
alaBgpPeer6KeepAliveConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6KeepAliveConfigured.setStatus("current")
_AlaBgpPeer6Ipv4NextHop_Type = IpAddress
_AlaBgpPeer6Ipv4NextHop_Object = MibTableColumn
alaBgpPeer6Ipv4NextHop = _AlaBgpPeer6Ipv4NextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 66),
    _AlaBgpPeer6Ipv4NextHop_Type()
)
alaBgpPeer6Ipv4NextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6Ipv4NextHop.setStatus("current")
_AlaBgpPeer6Ipv6NextHop_Type = Ipv6Address
_AlaBgpPeer6Ipv6NextHop_Object = MibTableColumn
alaBgpPeer6Ipv6NextHop = _AlaBgpPeer6Ipv6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 67),
    _AlaBgpPeer6Ipv6NextHop_Type()
)
alaBgpPeer6Ipv6NextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6Ipv6NextHop.setStatus("current")


class _AlaBgpPeer6AdminStatus_Type(Integer32):
    """Custom type alaBgpPeer6AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 2),
          ("stop", 1))
    )


_AlaBgpPeer6AdminStatus_Type.__name__ = "Integer32"
_AlaBgpPeer6AdminStatus_Object = MibTableColumn
alaBgpPeer6AdminStatus = _AlaBgpPeer6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 68),
    _AlaBgpPeer6AdminStatus_Type()
)
alaBgpPeer6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6AdminStatus.setStatus("current")


class _AlaBgpPeer6State_Type(Integer32):
    """Custom type alaBgpPeer6State based on Integer32"""
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_AlaBgpPeer6State_Type.__name__ = "Integer32"
_AlaBgpPeer6State_Object = MibTableColumn
alaBgpPeer6State = _AlaBgpPeer6State_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 69),
    _AlaBgpPeer6State_Type()
)
alaBgpPeer6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6State.setStatus("current")


class _AlaBgpPeer6LocalPort_Type(Integer32):
    """Custom type alaBgpPeer6LocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpPeer6LocalPort_Type.__name__ = "Integer32"
_AlaBgpPeer6LocalPort_Object = MibTableColumn
alaBgpPeer6LocalPort = _AlaBgpPeer6LocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 70),
    _AlaBgpPeer6LocalPort_Type()
)
alaBgpPeer6LocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6LocalPort.setStatus("current")


class _AlaBgpPeer6TcpWindowSize_Type(Integer32):
    """Custom type alaBgpPeer6TcpWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaBgpPeer6TcpWindowSize_Type.__name__ = "Integer32"
_AlaBgpPeer6TcpWindowSize_Object = MibTableColumn
alaBgpPeer6TcpWindowSize = _AlaBgpPeer6TcpWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 71),
    _AlaBgpPeer6TcpWindowSize_Type()
)
alaBgpPeer6TcpWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBgpPeer6TcpWindowSize.setStatus("current")


class _AlaBgpPeer6ActivateIpv6_Type(Integer32):
    """Custom type alaBgpPeer6ActivateIpv6 based on Integer32"""
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


_AlaBgpPeer6ActivateIpv6_Type.__name__ = "Integer32"
_AlaBgpPeer6ActivateIpv6_Object = MibTableColumn
alaBgpPeer6ActivateIpv6 = _AlaBgpPeer6ActivateIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 72),
    _AlaBgpPeer6ActivateIpv6_Type()
)
alaBgpPeer6ActivateIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6ActivateIpv6.setStatus("current")


class _AlaBgpPeer6MinRouteAdvertisementInterval_Type(Integer32):
    """Custom type alaBgpPeer6MinRouteAdvertisementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaBgpPeer6MinRouteAdvertisementInterval_Type.__name__ = "Integer32"
_AlaBgpPeer6MinRouteAdvertisementInterval_Object = MibTableColumn
alaBgpPeer6MinRouteAdvertisementInterval = _AlaBgpPeer6MinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 73),
    _AlaBgpPeer6MinRouteAdvertisementInterval_Type()
)
alaBgpPeer6MinRouteAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6MinRouteAdvertisementInterval.setStatus("current")


class _AlaBgpPeer6Prefix6ListOut_Type(DisplayString):
    """Custom type alaBgpPeer6Prefix6ListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6Prefix6ListOut_Type.__name__ = "DisplayString"
_AlaBgpPeer6Prefix6ListOut_Object = MibTableColumn
alaBgpPeer6Prefix6ListOut = _AlaBgpPeer6Prefix6ListOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 74),
    _AlaBgpPeer6Prefix6ListOut_Type()
)
alaBgpPeer6Prefix6ListOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6Prefix6ListOut.setStatus("current")


class _AlaBgpPeer6Prefix6ListIn_Type(DisplayString):
    """Custom type alaBgpPeer6Prefix6ListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AlaBgpPeer6Prefix6ListIn_Type.__name__ = "DisplayString"
_AlaBgpPeer6Prefix6ListIn_Object = MibTableColumn
alaBgpPeer6Prefix6ListIn = _AlaBgpPeer6Prefix6ListIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 1, 14, 1, 75),
    _AlaBgpPeer6Prefix6ListIn_Type()
)
alaBgpPeer6Prefix6ListIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBgpPeer6Prefix6ListIn.setStatus("current")
_AlcatelIND1BGPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1BGPMIBConformance = _AlcatelIND1BGPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1BGPMIBConformance.setStatus("current")
_AlcatelIND1BGPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1BGPMIBGroups = _AlcatelIND1BGPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1BGPMIBGroups.setStatus("current")
_AlcatelIND1BGPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1BGPMIBCompliances = _AlcatelIND1BGPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1BGPMIBCompliances.setStatus("current")

# Managed Objects groups

alabgpMIBGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 1)
)
alabgpMIBGlobalsGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpProtoStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAutonomousSystemNumber"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouterId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpIgpSynchStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpMedAlways"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDefaultLocalPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpMissingMed"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpManualTag"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPromiscuousNeighbours"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpConfedId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampening"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampHalfLife"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampMaxFlapHistory"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDebugLevel"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpFastExternalFailOver"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerChanges"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpVersion"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpProtoOperState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpMaxPeers"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNumActiveRoutes"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNumEstabExternalPeers"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNumEstabInternalPeers"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNumPaths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNumFeasiblePaths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNumDampenedPaths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNumIgpSyncWaitPaths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNumPolicyChgPaths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpMultiPath"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteReflection"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpClusterId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampeningClear"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampCutOff"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampReuse"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampCeil"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathCompare"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAsOriginInterval"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpMultiProtocolIpv4"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpMultiProtocolIpv6"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpBfdStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpBfdAllNeighborStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpGracefulRestart"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRestartInterval"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRestartStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBGlobalsGroup.setStatus("current")

alabgpMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 2)
)
alabgpMIBPeerGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpPeerAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerAS"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerPassive"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerName"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerMultiHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerMaxPrefix"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerMaxPrefixWarnOnly"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerNextHopSelf"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerSoftReconfig"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerInSoftReset"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerIpv4Unicast"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerIpv4Multicast"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRcvdRtRefreshMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerSentRtRefreshMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRouteMapOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRouteMapIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLocalAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLastDownReason"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLastDownTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLastReadTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRcvdNotifyMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerSentNotifyMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLastSentNotifyReason"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLastRecvNotifyReason"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRcvdPrefixes"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerDownTransitions"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerType"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerAutoReStart"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerClientStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerConfedStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRemovePrivateAs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerClearCounter"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerTTL"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerAspathListOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerAspathListIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerPrefixListOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerPrefixListIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerCommunityListOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerCommunityListIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRestart"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerDefaultOriginate"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerReconfigureInBound"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerReconfigureOutBound"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerMD5Key"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerMD5KeyEncrypt"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRowStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerUpTransitions"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLastWriteTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRcvdMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerSentMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRcvdUpdMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerSentUpdMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerIpv6Unicast"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerIpv6NextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLocalPort"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerTcpWindowSize"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerActivateIpv6"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerBfdStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerPrefix6ListOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerPrefix6ListIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLastTransitionTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLastUpTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerLocalIntfName"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRestartFwdState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRestartState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerRestartTime"))
)
if mibBuilder.loadTexts:
    alabgpMIBPeerGroup.setStatus("current")

alabgpMIBAggrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 3)
)
alabgpMIBAggrGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpAggrAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAggrMask"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAggrSummarize"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAggrSet"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAggrState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAggrMetric"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAggrLocalPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAggrCommunity"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAggrRowStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBAggrGroup.setStatus("current")

alabgpMIBNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 4)
)
alabgpMIBNetworkGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpNetworkAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetworkMask"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetworkState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetworkMetric"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetworkLocalPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetworkCommunity"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetworkRowStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBNetworkGroup.setStatus("current")

alabgpMIBRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 5)
)
alabgpMIBRouteGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpRouteAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMask"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoutePaths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteFeasiblePaths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteNextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIgpNextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsHidden"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsAggregate"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsAggregateContributor"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteAdvNeighbors"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsAggregateList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsAggregateWait"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsOnEbgpChgList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsOnIbgpClientChgList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsOnIbgpChgList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsOnLocalChgList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsOnDeleteList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteIsDampened"))
)
if mibBuilder.loadTexts:
    alabgpMIBRouteGroup.setStatus("current")

alabgpMIBPathAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 6)
)
alabgpMIBPathAttrGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpPathAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathMask"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathPeerAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathSrcProto"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathWeight"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathOrigin"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathNextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathAs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathLocalPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathMed"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathAtomic"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathAggregatorAs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathAggregatorAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathCommunity"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathUnknownAttr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathOriginatorId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathClusterList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathPeerInetType"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPathPeerName"))
)
if mibBuilder.loadTexts:
    alabgpMIBPathAttrGroup.setStatus("current")

alabgpMIBDampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 7)
)
alabgpMIBDampGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpDampAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampMask"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampPeerAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampFigureOfMerit"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampFlaps"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampDuration"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampLastUpdateTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampReuseTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDampClear"))
)
if mibBuilder.loadTexts:
    alabgpMIBDampGroup.setStatus("current")

alabgpMIBRouteMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 8)
)
alabgpMIBRouteMapGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapName"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapInst"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapAsPathMatchListId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapPrefixMatchListId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapCommunityMatchListId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapOrigin"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapLocalPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapLocalPrefMode"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapMed"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapMedMode"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapAsPrepend"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapSetCommunityMode"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapCommunity"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapMatchAsRegExp"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapMatchPrefix"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapMatchMask"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapMatchCommunity"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapWeight"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapAction"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRouteMapRowStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBRouteMapGroup.setStatus("current")

alabgpMIBAspathListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 9)
)
alabgpMIBAspathListGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpAspathMatchListId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathMatchListRegExp"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathMatchListPriority"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathMatchListAction"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathMatchListRowStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathMatchListSubIndex"))
)
if mibBuilder.loadTexts:
    alabgpMIBAspathListGroup.setStatus("current")

alabgpMIBPrefixListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 10)
)
alabgpMIBPrefixListGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListMask"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListGE"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListLE"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListAction"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefixMatchListRowStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefix6MatchListAction"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefix6MatchListGE"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefix6MatchListLE"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPrefix6MatchListRowStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBPrefixListGroup.setStatus("current")

alabgpMIBCommunityListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 11)
)
alabgpMIBCommunityListGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListString"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListPriority"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListType"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListAction"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListRowStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityMatchListSubIndex"))
)
if mibBuilder.loadTexts:
    alabgpMIBCommunityListGroup.setStatus("current")

alabgpMIBAspathPriListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 12)
)
alabgpMIBAspathPriListGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListPriority"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListIntIdx"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListRegExp"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListAction"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpAspathPriMatchListRowStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBAspathPriListGroup.setStatus("current")

alabgpMIBCommunityPriListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 13)
)
alabgpMIBCommunityPriListGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListPriority"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListIntIdx"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListString"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListType"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListAction"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpCommunityPriMatchListRowStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBCommunityPriListGroup.setStatus("current")

alabgpMIBRedistRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 14)
)
alabgpMIBRedistRouteGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteProto"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteDest"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteMask"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteMetric"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteLocalPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteCommunity"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteSubnetMatch"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteEffect"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRedistRouteRowStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBRedistRouteGroup.setStatus("deprecated")

alabgpMIBDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 15)
)
alabgpMIBDebugGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpDebugEvent"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDebugStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpDebugDescription"))
)
if mibBuilder.loadTexts:
    alabgpMIBDebugGroup.setStatus("current")

alabgpMIBNetwork6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 16)
)
alabgpMIBNetwork6Group.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6Addr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6MaskLen"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6State"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6Metric"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6LocalPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6Community"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpNetwork6RowStatus"))
)
if mibBuilder.loadTexts:
    alabgpMIBNetwork6Group.setStatus("current")

alabgpMIBRoute6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 17)
)
alabgpMIBRoute6Group.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6Addr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6MaskLen"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6State"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6Paths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6FeasiblePaths"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6NextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IgpNextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsHidden"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsAggregate"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsAggregateContributor"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6AdvNeighbors"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsAggregateList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsAggregateWait"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsOnEbgpChgList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsOnIbgpClientChgList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsOnIbgpChgList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsOnLocalChgList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsOnDeleteList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpRoute6IsDampened"))
)
if mibBuilder.loadTexts:
    alabgpMIBRoute6Group.setStatus("current")

alabgpMIBPath6AttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 18)
)
alabgpMIBPath6AttrGroup.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpPath6Addr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6MaskLen"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6PeerBgpId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6SrcProto"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6Weight"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6Pref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6State"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6Origin"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6NextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6As"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6LocalPref"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6Med"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6Atomic"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6AggregatorAs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6AggregatorAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6Community"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6UnknownAttr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6OriginatorId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6ClusterList"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPath6PeerName"))
)
if mibBuilder.loadTexts:
    alabgpMIBPath6AttrGroup.setStatus("current")

alabgpMIBPeer6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 1, 19)
)
alabgpMIBPeer6Group.setObjects(
      *(("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Addr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6AS"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Passive"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Name"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6MultiHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6MaxPrefix"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6MaxPrefixWarnOnly"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6NextHopSelf"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6SoftReconfig"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6InSoftReset"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Ipv4Unicast"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Ipv4Multicast"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RcvdRtRefreshMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6SentRtRefreshMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RouteMapOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RouteMapIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LocalAddr"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LastDownReason"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LastDownTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LastReadTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RcvdNotifyMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6SentNotifyMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LastSentNotifyReason"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LastRecvNotifyReason"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RcvdPrefixes"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6DownTransitions"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Type"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6AutoReStart"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6ClientStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6ConfedStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RemovePrivateAs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6ClearCounter"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6TTL"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6AspathListOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6AspathListIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6PrefixListOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6PrefixListIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6CommunityListOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6CommunityListIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Restart"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6DefaultOriginate"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6ReconfigureInBound"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6ReconfigureOutBound"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6MD5Key"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6MD5KeyEncrypt"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RowStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6UpTransitions"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LastWriteTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RcvdMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6SentMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RcvdUpdMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6SentUpdMsgs"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Ipv6Unicast"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6HoldTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6KeepAlive"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6ConnRetryInterval"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6HoldTimeConfigured"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6KeepAliveConfigured"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Ipv4NextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Ipv6NextHop"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6AdminStatus"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6State"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LocalPort"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6TcpWindowSize"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6ActivateIpv6"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6MinRouteAdvertisementInterval"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Prefix6ListOut"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6Prefix6ListIn"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6BgpId"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LastUpTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LocalIntfName"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RestartFwdState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RestartState"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6RestartTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeer6LastTransitionTime"),
        ("ALCATEL-IND1-BGP-MIB", "alaBgpPeerBgpId"))
)
if mibBuilder.loadTexts:
    alabgpMIBPeer6Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1BGPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1BGPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-BGP-MIB",
    **{"alcatelIND1BGPMIB": alcatelIND1BGPMIB,
       "alcatelIND1BGPMIBObjects": alcatelIND1BGPMIBObjects,
       "alaBgpGlobal": alaBgpGlobal,
       "alaBgpProtoStatus": alaBgpProtoStatus,
       "alaBgpAutonomousSystemNumber": alaBgpAutonomousSystemNumber,
       "alaBgpRouterId": alaBgpRouterId,
       "alaBgpIgpSynchStatus": alaBgpIgpSynchStatus,
       "alaBgpMedAlways": alaBgpMedAlways,
       "alaBgpDefaultLocalPref": alaBgpDefaultLocalPref,
       "alaBgpMissingMed": alaBgpMissingMed,
       "alaBgpManualTag": alaBgpManualTag,
       "alaBgpPromiscuousNeighbours": alaBgpPromiscuousNeighbours,
       "alaBgpConfedId": alaBgpConfedId,
       "alaBgpDampening": alaBgpDampening,
       "alaBgpDampHalfLifeReach": alaBgpDampHalfLifeReach,
       "alaBgpDampHalfLifeUnReach": alaBgpDampHalfLifeUnReach,
       "alaBgpDampMaxFlapHistory": alaBgpDampMaxFlapHistory,
       "alaBgpDebugLevel": alaBgpDebugLevel,
       "alaBgpFastExternalFailOver": alaBgpFastExternalFailOver,
       "alaBgpPeerChanges": alaBgpPeerChanges,
       "alaBgpVersion": alaBgpVersion,
       "alaBgpProtoOperState": alaBgpProtoOperState,
       "alaBgpMaxPeers": alaBgpMaxPeers,
       "alaBgpNumActiveRoutes": alaBgpNumActiveRoutes,
       "alaBgpNumEstabExternalPeers": alaBgpNumEstabExternalPeers,
       "alaBgpNumEstabInternalPeers": alaBgpNumEstabInternalPeers,
       "alaBgpNumPaths": alaBgpNumPaths,
       "alaBgpNumFeasiblePaths": alaBgpNumFeasiblePaths,
       "alaBgpNumDampenedPaths": alaBgpNumDampenedPaths,
       "alaBgpNumIgpSyncWaitPaths": alaBgpNumIgpSyncWaitPaths,
       "alaBgpNumPolicyChgPaths": alaBgpNumPolicyChgPaths,
       "alaBgpMultiPath": alaBgpMultiPath,
       "alaBgpRouteReflection": alaBgpRouteReflection,
       "alaBgpClusterId": alaBgpClusterId,
       "alaBgpDampeningClear": alaBgpDampeningClear,
       "alaBgpDampCutOff": alaBgpDampCutOff,
       "alaBgpDampReuse": alaBgpDampReuse,
       "alaBgpDampCeil": alaBgpDampCeil,
       "alaBgpAspathCompare": alaBgpAspathCompare,
       "alaBgpAsOriginInterval": alaBgpAsOriginInterval,
       "alaBgpDampHalfLife": alaBgpDampHalfLife,
       "alaBgpGracefulRestart": alaBgpGracefulRestart,
       "alaBgpRestartInterval": alaBgpRestartInterval,
       "alaBgpRestartStatus": alaBgpRestartStatus,
       "alaBgpMultiProtocolIpv4": alaBgpMultiProtocolIpv4,
       "alaBgpMultiProtocolIpv6": alaBgpMultiProtocolIpv6,
       "alaBgpBfdStatus": alaBgpBfdStatus,
       "alaBgpBfdAllNeighborStatus": alaBgpBfdAllNeighborStatus,
       "alaBgpPeerTable": alaBgpPeerTable,
       "alaBgpPeerEntry": alaBgpPeerEntry,
       "alaBgpPeerAddr": alaBgpPeerAddr,
       "alaBgpPeerAS": alaBgpPeerAS,
       "alaBgpPeerPassive": alaBgpPeerPassive,
       "alaBgpPeerName": alaBgpPeerName,
       "alaBgpPeerMultiHop": alaBgpPeerMultiHop,
       "alaBgpPeerMaxPrefix": alaBgpPeerMaxPrefix,
       "alaBgpPeerMaxPrefixWarnOnly": alaBgpPeerMaxPrefixWarnOnly,
       "alaBgpPeerNextHopSelf": alaBgpPeerNextHopSelf,
       "alaBgpPeerSoftReconfig": alaBgpPeerSoftReconfig,
       "alaBgpPeerInSoftReset": alaBgpPeerInSoftReset,
       "alaBgpPeerIpv4Unicast": alaBgpPeerIpv4Unicast,
       "alaBgpPeerIpv4Multicast": alaBgpPeerIpv4Multicast,
       "alaBgpPeerRcvdRtRefreshMsgs": alaBgpPeerRcvdRtRefreshMsgs,
       "alaBgpPeerSentRtRefreshMsgs": alaBgpPeerSentRtRefreshMsgs,
       "alaBgpPeerRouteMapOut": alaBgpPeerRouteMapOut,
       "alaBgpPeerRouteMapIn": alaBgpPeerRouteMapIn,
       "alaBgpPeerLocalAddr": alaBgpPeerLocalAddr,
       "alaBgpPeerLastDownReason": alaBgpPeerLastDownReason,
       "alaBgpPeerLastDownTime": alaBgpPeerLastDownTime,
       "alaBgpPeerLastReadTime": alaBgpPeerLastReadTime,
       "alaBgpPeerRcvdNotifyMsgs": alaBgpPeerRcvdNotifyMsgs,
       "alaBgpPeerSentNotifyMsgs": alaBgpPeerSentNotifyMsgs,
       "alaBgpPeerLastSentNotifyReason": alaBgpPeerLastSentNotifyReason,
       "alaBgpPeerLastRecvNotifyReason": alaBgpPeerLastRecvNotifyReason,
       "alaBgpPeerRcvdPrefixes": alaBgpPeerRcvdPrefixes,
       "alaBgpPeerDownTransitions": alaBgpPeerDownTransitions,
       "alaBgpPeerType": alaBgpPeerType,
       "alaBgpPeerClearCounter": alaBgpPeerClearCounter,
       "alaBgpPeerAutoReStart": alaBgpPeerAutoReStart,
       "alaBgpPeerClientStatus": alaBgpPeerClientStatus,
       "alaBgpPeerConfedStatus": alaBgpPeerConfedStatus,
       "alaBgpPeerRemovePrivateAs": alaBgpPeerRemovePrivateAs,
       "alaBgpPeerTTL": alaBgpPeerTTL,
       "alaBgpPeerAspathListOut": alaBgpPeerAspathListOut,
       "alaBgpPeerAspathListIn": alaBgpPeerAspathListIn,
       "alaBgpPeerPrefixListOut": alaBgpPeerPrefixListOut,
       "alaBgpPeerPrefixListIn": alaBgpPeerPrefixListIn,
       "alaBgpPeerCommunityListOut": alaBgpPeerCommunityListOut,
       "alaBgpPeerCommunityListIn": alaBgpPeerCommunityListIn,
       "alaBgpPeerRestart": alaBgpPeerRestart,
       "alaBgpPeerDefaultOriginate": alaBgpPeerDefaultOriginate,
       "alaBgpPeerReconfigureInBound": alaBgpPeerReconfigureInBound,
       "alaBgpPeerReconfigureOutBound": alaBgpPeerReconfigureOutBound,
       "alaBgpPeerMD5Key": alaBgpPeerMD5Key,
       "alaBgpPeerMD5KeyEncrypt": alaBgpPeerMD5KeyEncrypt,
       "alaBgpPeerRowStatus": alaBgpPeerRowStatus,
       "alaBgpPeerUpTransitions": alaBgpPeerUpTransitions,
       "alaBgpPeerLastWriteTime": alaBgpPeerLastWriteTime,
       "alaBgpPeerRcvdMsgs": alaBgpPeerRcvdMsgs,
       "alaBgpPeerSentMsgs": alaBgpPeerSentMsgs,
       "alaBgpPeerRcvdUpdMsgs": alaBgpPeerRcvdUpdMsgs,
       "alaBgpPeerSentUpdMsgs": alaBgpPeerSentUpdMsgs,
       "alaBgpPeerLastTransitionTime": alaBgpPeerLastTransitionTime,
       "alaBgpPeerLastUpTime": alaBgpPeerLastUpTime,
       "alaBgpPeerBgpId": alaBgpPeerBgpId,
       "alaBgpPeerLocalIntfName": alaBgpPeerLocalIntfName,
       "alaBgpPeerRestartTime": alaBgpPeerRestartTime,
       "alaBgpPeerRestartState": alaBgpPeerRestartState,
       "alaBgpPeerRestartFwdState": alaBgpPeerRestartFwdState,
       "alaBgpPeerIpv6Unicast": alaBgpPeerIpv6Unicast,
       "alaBgpPeerIpv6NextHop": alaBgpPeerIpv6NextHop,
       "alaBgpPeerLocalPort": alaBgpPeerLocalPort,
       "alaBgpPeerTcpWindowSize": alaBgpPeerTcpWindowSize,
       "alaBgpPeerActivateIpv6": alaBgpPeerActivateIpv6,
       "alaBgpPeerBfdStatus": alaBgpPeerBfdStatus,
       "alaBgpPeerPrefix6ListOut": alaBgpPeerPrefix6ListOut,
       "alaBgpPeerPrefix6ListIn": alaBgpPeerPrefix6ListIn,
       "alaBgpAggrTable": alaBgpAggrTable,
       "alaBgpAggrEntry": alaBgpAggrEntry,
       "alaBgpAggrAddr": alaBgpAggrAddr,
       "alaBgpAggrMask": alaBgpAggrMask,
       "alaBgpAggrSummarize": alaBgpAggrSummarize,
       "alaBgpAggrSet": alaBgpAggrSet,
       "alaBgpAggrState": alaBgpAggrState,
       "alaBgpAggrMetric": alaBgpAggrMetric,
       "alaBgpAggrLocalPref": alaBgpAggrLocalPref,
       "alaBgpAggrCommunity": alaBgpAggrCommunity,
       "alaBgpAggrRowStatus": alaBgpAggrRowStatus,
       "alaBgpNetworkTable": alaBgpNetworkTable,
       "alaBgpNetworkEntry": alaBgpNetworkEntry,
       "alaBgpNetworkAddr": alaBgpNetworkAddr,
       "alaBgpNetworkMask": alaBgpNetworkMask,
       "alaBgpNetworkState": alaBgpNetworkState,
       "alaBgpNetworkMetric": alaBgpNetworkMetric,
       "alaBgpNetworkLocalPref": alaBgpNetworkLocalPref,
       "alaBgpNetworkCommunity": alaBgpNetworkCommunity,
       "alaBgpNetworkRowStatus": alaBgpNetworkRowStatus,
       "alaBgpRouteTable": alaBgpRouteTable,
       "alaBgpRouteEntry": alaBgpRouteEntry,
       "alaBgpRouteAddr": alaBgpRouteAddr,
       "alaBgpRouteMask": alaBgpRouteMask,
       "alaBgpRouteState": alaBgpRouteState,
       "alaBgpRoutePaths": alaBgpRoutePaths,
       "alaBgpRouteFeasiblePaths": alaBgpRouteFeasiblePaths,
       "alaBgpRouteNextHop": alaBgpRouteNextHop,
       "alaBgpRouteIgpNextHop": alaBgpRouteIgpNextHop,
       "alaBgpRouteIsHidden": alaBgpRouteIsHidden,
       "alaBgpRouteIsAggregate": alaBgpRouteIsAggregate,
       "alaBgpRouteIsAggregateContributor": alaBgpRouteIsAggregateContributor,
       "alaBgpRouteAdvNeighbors": alaBgpRouteAdvNeighbors,
       "alaBgpRouteIsAggregateList": alaBgpRouteIsAggregateList,
       "alaBgpRouteIsAggregateWait": alaBgpRouteIsAggregateWait,
       "alaBgpRouteIsOnEbgpChgList": alaBgpRouteIsOnEbgpChgList,
       "alaBgpRouteIsOnIbgpClientChgList": alaBgpRouteIsOnIbgpClientChgList,
       "alaBgpRouteIsOnIbgpChgList": alaBgpRouteIsOnIbgpChgList,
       "alaBgpRouteIsOnLocalChgList": alaBgpRouteIsOnLocalChgList,
       "alaBgpRouteIsOnDeleteList": alaBgpRouteIsOnDeleteList,
       "alaBgpRouteIsDampened": alaBgpRouteIsDampened,
       "alaBgpPathTable": alaBgpPathTable,
       "alaBgpPathEntry": alaBgpPathEntry,
       "alaBgpPathAddr": alaBgpPathAddr,
       "alaBgpPathMask": alaBgpPathMask,
       "alaBgpPathPeerAddr": alaBgpPathPeerAddr,
       "alaBgpPathSrcProto": alaBgpPathSrcProto,
       "alaBgpPathWeight": alaBgpPathWeight,
       "alaBgpPathPref": alaBgpPathPref,
       "alaBgpPathState": alaBgpPathState,
       "alaBgpPathOrigin": alaBgpPathOrigin,
       "alaBgpPathNextHop": alaBgpPathNextHop,
       "alaBgpPathAs": alaBgpPathAs,
       "alaBgpPathLocalPref": alaBgpPathLocalPref,
       "alaBgpPathMed": alaBgpPathMed,
       "alaBgpPathAtomic": alaBgpPathAtomic,
       "alaBgpPathAggregatorAs": alaBgpPathAggregatorAs,
       "alaBgpPathAggregatorAddr": alaBgpPathAggregatorAddr,
       "alaBgpPathCommunity": alaBgpPathCommunity,
       "alaBgpPathUnknownAttr": alaBgpPathUnknownAttr,
       "alaBgpPathOriginatorId": alaBgpPathOriginatorId,
       "alaBgpPathClusterList": alaBgpPathClusterList,
       "alaBgpPathPeerInetType": alaBgpPathPeerInetType,
       "alaBgpPathPeerName": alaBgpPathPeerName,
       "alaBgpDampTable": alaBgpDampTable,
       "alaBgpDampEntry": alaBgpDampEntry,
       "alaBgpDampAddr": alaBgpDampAddr,
       "alaBgpDampMask": alaBgpDampMask,
       "alaBgpDampPeerAddr": alaBgpDampPeerAddr,
       "alaBgpDampFigureOfMerit": alaBgpDampFigureOfMerit,
       "alaBgpDampFlaps": alaBgpDampFlaps,
       "alaBgpDampDuration": alaBgpDampDuration,
       "alaBgpDampLastUpdateTime": alaBgpDampLastUpdateTime,
       "alaBgpDampReuseTime": alaBgpDampReuseTime,
       "alaBgpDampClear": alaBgpDampClear,
       "alaBgpPolicy": alaBgpPolicy,
       "alaBgpRouteMapTable": alaBgpRouteMapTable,
       "alaBgpRouteMapEntry": alaBgpRouteMapEntry,
       "alaBgpRouteMapName": alaBgpRouteMapName,
       "alaBgpRouteMapInst": alaBgpRouteMapInst,
       "alaBgpRouteMapAsPathMatchListId": alaBgpRouteMapAsPathMatchListId,
       "alaBgpRouteMapPrefixMatchListId": alaBgpRouteMapPrefixMatchListId,
       "alaBgpRouteMapCommunityMatchListId": alaBgpRouteMapCommunityMatchListId,
       "alaBgpRouteMapOrigin": alaBgpRouteMapOrigin,
       "alaBgpRouteMapLocalPref": alaBgpRouteMapLocalPref,
       "alaBgpRouteMapLocalPrefMode": alaBgpRouteMapLocalPrefMode,
       "alaBgpRouteMapMed": alaBgpRouteMapMed,
       "alaBgpRouteMapMedMode": alaBgpRouteMapMedMode,
       "alaBgpRouteMapAsPrepend": alaBgpRouteMapAsPrepend,
       "alaBgpRouteMapSetCommunityMode": alaBgpRouteMapSetCommunityMode,
       "alaBgpRouteMapCommunity": alaBgpRouteMapCommunity,
       "alaBgpRouteMapMatchAsRegExp": alaBgpRouteMapMatchAsRegExp,
       "alaBgpRouteMapMatchPrefix": alaBgpRouteMapMatchPrefix,
       "alaBgpRouteMapMatchMask": alaBgpRouteMapMatchMask,
       "alaBgpRouteMapMatchCommunity": alaBgpRouteMapMatchCommunity,
       "alaBgpRouteMapWeight": alaBgpRouteMapWeight,
       "alaBgpRouteMapAction": alaBgpRouteMapAction,
       "alaBgpRouteMapRowStatus": alaBgpRouteMapRowStatus,
       "alaBgpAspathMatchListTable": alaBgpAspathMatchListTable,
       "alaBgpAspathMatchListEntry": alaBgpAspathMatchListEntry,
       "alaBgpAspathMatchListId": alaBgpAspathMatchListId,
       "alaBgpAspathMatchListRegExp": alaBgpAspathMatchListRegExp,
       "alaBgpAspathMatchListPriority": alaBgpAspathMatchListPriority,
       "alaBgpAspathMatchListAction": alaBgpAspathMatchListAction,
       "alaBgpAspathMatchListRowStatus": alaBgpAspathMatchListRowStatus,
       "alaBgpAspathMatchListSubIndex": alaBgpAspathMatchListSubIndex,
       "alaBgpPrefixMatchListTable": alaBgpPrefixMatchListTable,
       "alaBgpPrefixMatchListEntry": alaBgpPrefixMatchListEntry,
       "alaBgpPrefixMatchListId": alaBgpPrefixMatchListId,
       "alaBgpPrefixMatchListAddr": alaBgpPrefixMatchListAddr,
       "alaBgpPrefixMatchListMask": alaBgpPrefixMatchListMask,
       "alaBgpPrefixMatchListGE": alaBgpPrefixMatchListGE,
       "alaBgpPrefixMatchListLE": alaBgpPrefixMatchListLE,
       "alaBgpPrefixMatchListAction": alaBgpPrefixMatchListAction,
       "alaBgpPrefixMatchListRowStatus": alaBgpPrefixMatchListRowStatus,
       "alaBgpCommunityMatchListTable": alaBgpCommunityMatchListTable,
       "alaBgpCommunityMatchListEntry": alaBgpCommunityMatchListEntry,
       "alaBgpCommunityMatchListId": alaBgpCommunityMatchListId,
       "alaBgpCommunityMatchListString": alaBgpCommunityMatchListString,
       "alaBgpCommunityMatchListPriority": alaBgpCommunityMatchListPriority,
       "alaBgpCommunityMatchListType": alaBgpCommunityMatchListType,
       "alaBgpCommunityMatchListAction": alaBgpCommunityMatchListAction,
       "alaBgpCommunityMatchListRowStatus": alaBgpCommunityMatchListRowStatus,
       "alaBgpCommunityMatchListSubIndex": alaBgpCommunityMatchListSubIndex,
       "alaBgpAspathPriMatchListTable": alaBgpAspathPriMatchListTable,
       "alaBgpAspathPriMatchListEntry": alaBgpAspathPriMatchListEntry,
       "alaBgpAspathPriMatchListId": alaBgpAspathPriMatchListId,
       "alaBgpAspathPriMatchListPriority": alaBgpAspathPriMatchListPriority,
       "alaBgpAspathPriMatchListIntIdx": alaBgpAspathPriMatchListIntIdx,
       "alaBgpAspathPriMatchListRegExp": alaBgpAspathPriMatchListRegExp,
       "alaBgpAspathPriMatchListAction": alaBgpAspathPriMatchListAction,
       "alaBgpAspathPriMatchListRowStatus": alaBgpAspathPriMatchListRowStatus,
       "alaBgpCommunityPriMatchListTable": alaBgpCommunityPriMatchListTable,
       "alaBgpCommunityPriMatchListEntry": alaBgpCommunityPriMatchListEntry,
       "alaBgpCommunityPriMatchListId": alaBgpCommunityPriMatchListId,
       "alaBgpCommunityPriMatchListPriority": alaBgpCommunityPriMatchListPriority,
       "alaBgpCommunityPriMatchListIntIdx": alaBgpCommunityPriMatchListIntIdx,
       "alaBgpCommunityPriMatchListString": alaBgpCommunityPriMatchListString,
       "alaBgpCommunityPriMatchListType": alaBgpCommunityPriMatchListType,
       "alaBgpCommunityPriMatchListAction": alaBgpCommunityPriMatchListAction,
       "alaBgpCommunityPriMatchListRowStatus": alaBgpCommunityPriMatchListRowStatus,
       "alaBgpPrefix6MatchListTable": alaBgpPrefix6MatchListTable,
       "alaBgpPrefix6MatchListEntry": alaBgpPrefix6MatchListEntry,
       "alaBgpPrefix6MatchListId": alaBgpPrefix6MatchListId,
       "alaBgpPrefix6MatchListAddr": alaBgpPrefix6MatchListAddr,
       "alaBgpPrefix6MatchListAddrLength": alaBgpPrefix6MatchListAddrLength,
       "alaBgpPrefix6MatchListGE": alaBgpPrefix6MatchListGE,
       "alaBgpPrefix6MatchListLE": alaBgpPrefix6MatchListLE,
       "alaBgpPrefix6MatchListAction": alaBgpPrefix6MatchListAction,
       "alaBgpPrefix6MatchListRowStatus": alaBgpPrefix6MatchListRowStatus,
       "alaBgpRedistRouteTable": alaBgpRedistRouteTable,
       "alaBgpRedistRouteEntry": alaBgpRedistRouteEntry,
       "alaBgpRedistRouteProto": alaBgpRedistRouteProto,
       "alaBgpRedistRouteDest": alaBgpRedistRouteDest,
       "alaBgpRedistRouteMask": alaBgpRedistRouteMask,
       "alaBgpRedistRouteMetric": alaBgpRedistRouteMetric,
       "alaBgpRedistRouteLocalPref": alaBgpRedistRouteLocalPref,
       "alaBgpRedistRouteCommunity": alaBgpRedistRouteCommunity,
       "alaBgpRedistRouteSubnetMatch": alaBgpRedistRouteSubnetMatch,
       "alaBgpRedistRouteEffect": alaBgpRedistRouteEffect,
       "alaBgpRedistRouteRowStatus": alaBgpRedistRouteRowStatus,
       "alaBgpDebugTable": alaBgpDebugTable,
       "alaBgpDebugEntry": alaBgpDebugEntry,
       "alaBgpDebugEvent": alaBgpDebugEvent,
       "alaBgpDebugStatus": alaBgpDebugStatus,
       "alaBgpDebugDescription": alaBgpDebugDescription,
       "alaBgpNetwork6Table": alaBgpNetwork6Table,
       "alaBgpNetwork6Entry": alaBgpNetwork6Entry,
       "alaBgpNetwork6Addr": alaBgpNetwork6Addr,
       "alaBgpNetwork6MaskLen": alaBgpNetwork6MaskLen,
       "alaBgpNetwork6State": alaBgpNetwork6State,
       "alaBgpNetwork6Metric": alaBgpNetwork6Metric,
       "alaBgpNetwork6LocalPref": alaBgpNetwork6LocalPref,
       "alaBgpNetwork6Community": alaBgpNetwork6Community,
       "alaBgpNetwork6RowStatus": alaBgpNetwork6RowStatus,
       "alaBgpRoute6Table": alaBgpRoute6Table,
       "alaBgpRoute6Entry": alaBgpRoute6Entry,
       "alaBgpRoute6Addr": alaBgpRoute6Addr,
       "alaBgpRoute6MaskLen": alaBgpRoute6MaskLen,
       "alaBgpRoute6State": alaBgpRoute6State,
       "alaBgpRoute6Paths": alaBgpRoute6Paths,
       "alaBgpRoute6FeasiblePaths": alaBgpRoute6FeasiblePaths,
       "alaBgpRoute6NextHop": alaBgpRoute6NextHop,
       "alaBgpRoute6IgpNextHop": alaBgpRoute6IgpNextHop,
       "alaBgpRoute6IsHidden": alaBgpRoute6IsHidden,
       "alaBgpRoute6IsAggregate": alaBgpRoute6IsAggregate,
       "alaBgpRoute6IsAggregateContributor": alaBgpRoute6IsAggregateContributor,
       "alaBgpRoute6AdvNeighbors": alaBgpRoute6AdvNeighbors,
       "alaBgpRoute6IsAggregateList": alaBgpRoute6IsAggregateList,
       "alaBgpRoute6IsAggregateWait": alaBgpRoute6IsAggregateWait,
       "alaBgpRoute6IsOnEbgpChgList": alaBgpRoute6IsOnEbgpChgList,
       "alaBgpRoute6IsOnIbgpClientChgList": alaBgpRoute6IsOnIbgpClientChgList,
       "alaBgpRoute6IsOnIbgpChgList": alaBgpRoute6IsOnIbgpChgList,
       "alaBgpRoute6IsOnLocalChgList": alaBgpRoute6IsOnLocalChgList,
       "alaBgpRoute6IsOnDeleteList": alaBgpRoute6IsOnDeleteList,
       "alaBgpRoute6IsDampened": alaBgpRoute6IsDampened,
       "alaBgpPath6Table": alaBgpPath6Table,
       "alaBgpPath6Entry": alaBgpPath6Entry,
       "alaBgpPath6Addr": alaBgpPath6Addr,
       "alaBgpPath6MaskLen": alaBgpPath6MaskLen,
       "alaBgpPath6PeerBgpId": alaBgpPath6PeerBgpId,
       "alaBgpPath6SrcProto": alaBgpPath6SrcProto,
       "alaBgpPath6Weight": alaBgpPath6Weight,
       "alaBgpPath6Pref": alaBgpPath6Pref,
       "alaBgpPath6State": alaBgpPath6State,
       "alaBgpPath6Origin": alaBgpPath6Origin,
       "alaBgpPath6NextHop": alaBgpPath6NextHop,
       "alaBgpPath6As": alaBgpPath6As,
       "alaBgpPath6LocalPref": alaBgpPath6LocalPref,
       "alaBgpPath6Med": alaBgpPath6Med,
       "alaBgpPath6Atomic": alaBgpPath6Atomic,
       "alaBgpPath6AggregatorAs": alaBgpPath6AggregatorAs,
       "alaBgpPath6AggregatorAddr": alaBgpPath6AggregatorAddr,
       "alaBgpPath6Community": alaBgpPath6Community,
       "alaBgpPath6UnknownAttr": alaBgpPath6UnknownAttr,
       "alaBgpPath6OriginatorId": alaBgpPath6OriginatorId,
       "alaBgpPath6ClusterList": alaBgpPath6ClusterList,
       "alaBgpPath6PeerName": alaBgpPath6PeerName,
       "alaBgpPeer6Table": alaBgpPeer6Table,
       "alaBgpPeer6Entry": alaBgpPeer6Entry,
       "alaBgpPeer6Addr": alaBgpPeer6Addr,
       "alaBgpPeer6AS": alaBgpPeer6AS,
       "alaBgpPeer6Passive": alaBgpPeer6Passive,
       "alaBgpPeer6Name": alaBgpPeer6Name,
       "alaBgpPeer6MultiHop": alaBgpPeer6MultiHop,
       "alaBgpPeer6MaxPrefix": alaBgpPeer6MaxPrefix,
       "alaBgpPeer6MaxPrefixWarnOnly": alaBgpPeer6MaxPrefixWarnOnly,
       "alaBgpPeer6NextHopSelf": alaBgpPeer6NextHopSelf,
       "alaBgpPeer6SoftReconfig": alaBgpPeer6SoftReconfig,
       "alaBgpPeer6InSoftReset": alaBgpPeer6InSoftReset,
       "alaBgpPeer6Ipv4Unicast": alaBgpPeer6Ipv4Unicast,
       "alaBgpPeer6Ipv4Multicast": alaBgpPeer6Ipv4Multicast,
       "alaBgpPeer6RcvdRtRefreshMsgs": alaBgpPeer6RcvdRtRefreshMsgs,
       "alaBgpPeer6SentRtRefreshMsgs": alaBgpPeer6SentRtRefreshMsgs,
       "alaBgpPeer6RouteMapOut": alaBgpPeer6RouteMapOut,
       "alaBgpPeer6RouteMapIn": alaBgpPeer6RouteMapIn,
       "alaBgpPeer6LocalAddr": alaBgpPeer6LocalAddr,
       "alaBgpPeer6LastDownReason": alaBgpPeer6LastDownReason,
       "alaBgpPeer6LastDownTime": alaBgpPeer6LastDownTime,
       "alaBgpPeer6LastReadTime": alaBgpPeer6LastReadTime,
       "alaBgpPeer6RcvdNotifyMsgs": alaBgpPeer6RcvdNotifyMsgs,
       "alaBgpPeer6SentNotifyMsgs": alaBgpPeer6SentNotifyMsgs,
       "alaBgpPeer6LastSentNotifyReason": alaBgpPeer6LastSentNotifyReason,
       "alaBgpPeer6LastRecvNotifyReason": alaBgpPeer6LastRecvNotifyReason,
       "alaBgpPeer6RcvdPrefixes": alaBgpPeer6RcvdPrefixes,
       "alaBgpPeer6DownTransitions": alaBgpPeer6DownTransitions,
       "alaBgpPeer6Type": alaBgpPeer6Type,
       "alaBgpPeer6ClearCounter": alaBgpPeer6ClearCounter,
       "alaBgpPeer6AutoReStart": alaBgpPeer6AutoReStart,
       "alaBgpPeer6ClientStatus": alaBgpPeer6ClientStatus,
       "alaBgpPeer6ConfedStatus": alaBgpPeer6ConfedStatus,
       "alaBgpPeer6RemovePrivateAs": alaBgpPeer6RemovePrivateAs,
       "alaBgpPeer6TTL": alaBgpPeer6TTL,
       "alaBgpPeer6AspathListOut": alaBgpPeer6AspathListOut,
       "alaBgpPeer6AspathListIn": alaBgpPeer6AspathListIn,
       "alaBgpPeer6PrefixListOut": alaBgpPeer6PrefixListOut,
       "alaBgpPeer6PrefixListIn": alaBgpPeer6PrefixListIn,
       "alaBgpPeer6CommunityListOut": alaBgpPeer6CommunityListOut,
       "alaBgpPeer6CommunityListIn": alaBgpPeer6CommunityListIn,
       "alaBgpPeer6Restart": alaBgpPeer6Restart,
       "alaBgpPeer6DefaultOriginate": alaBgpPeer6DefaultOriginate,
       "alaBgpPeer6ReconfigureInBound": alaBgpPeer6ReconfigureInBound,
       "alaBgpPeer6ReconfigureOutBound": alaBgpPeer6ReconfigureOutBound,
       "alaBgpPeer6MD5Key": alaBgpPeer6MD5Key,
       "alaBgpPeer6MD5KeyEncrypt": alaBgpPeer6MD5KeyEncrypt,
       "alaBgpPeer6RowStatus": alaBgpPeer6RowStatus,
       "alaBgpPeer6UpTransitions": alaBgpPeer6UpTransitions,
       "alaBgpPeer6LastWriteTime": alaBgpPeer6LastWriteTime,
       "alaBgpPeer6RcvdMsgs": alaBgpPeer6RcvdMsgs,
       "alaBgpPeer6SentMsgs": alaBgpPeer6SentMsgs,
       "alaBgpPeer6RcvdUpdMsgs": alaBgpPeer6RcvdUpdMsgs,
       "alaBgpPeer6SentUpdMsgs": alaBgpPeer6SentUpdMsgs,
       "alaBgpPeer6LastTransitionTime": alaBgpPeer6LastTransitionTime,
       "alaBgpPeer6LastUpTime": alaBgpPeer6LastUpTime,
       "alaBgpPeer6BgpId": alaBgpPeer6BgpId,
       "alaBgpPeer6LocalIntfName": alaBgpPeer6LocalIntfName,
       "alaBgpPeer6RestartTime": alaBgpPeer6RestartTime,
       "alaBgpPeer6RestartState": alaBgpPeer6RestartState,
       "alaBgpPeer6RestartFwdState": alaBgpPeer6RestartFwdState,
       "alaBgpPeer6Ipv6Unicast": alaBgpPeer6Ipv6Unicast,
       "alaBgpPeer6HoldTime": alaBgpPeer6HoldTime,
       "alaBgpPeer6KeepAlive": alaBgpPeer6KeepAlive,
       "alaBgpPeer6ConnRetryInterval": alaBgpPeer6ConnRetryInterval,
       "alaBgpPeer6HoldTimeConfigured": alaBgpPeer6HoldTimeConfigured,
       "alaBgpPeer6KeepAliveConfigured": alaBgpPeer6KeepAliveConfigured,
       "alaBgpPeer6Ipv4NextHop": alaBgpPeer6Ipv4NextHop,
       "alaBgpPeer6Ipv6NextHop": alaBgpPeer6Ipv6NextHop,
       "alaBgpPeer6AdminStatus": alaBgpPeer6AdminStatus,
       "alaBgpPeer6State": alaBgpPeer6State,
       "alaBgpPeer6LocalPort": alaBgpPeer6LocalPort,
       "alaBgpPeer6TcpWindowSize": alaBgpPeer6TcpWindowSize,
       "alaBgpPeer6ActivateIpv6": alaBgpPeer6ActivateIpv6,
       "alaBgpPeer6MinRouteAdvertisementInterval": alaBgpPeer6MinRouteAdvertisementInterval,
       "alaBgpPeer6Prefix6ListOut": alaBgpPeer6Prefix6ListOut,
       "alaBgpPeer6Prefix6ListIn": alaBgpPeer6Prefix6ListIn,
       "alcatelIND1BGPMIBConformance": alcatelIND1BGPMIBConformance,
       "alcatelIND1BGPMIBGroups": alcatelIND1BGPMIBGroups,
       "alabgpMIBGlobalsGroup": alabgpMIBGlobalsGroup,
       "alabgpMIBPeerGroup": alabgpMIBPeerGroup,
       "alabgpMIBAggrGroup": alabgpMIBAggrGroup,
       "alabgpMIBNetworkGroup": alabgpMIBNetworkGroup,
       "alabgpMIBRouteGroup": alabgpMIBRouteGroup,
       "alabgpMIBPathAttrGroup": alabgpMIBPathAttrGroup,
       "alabgpMIBDampGroup": alabgpMIBDampGroup,
       "alabgpMIBRouteMapGroup": alabgpMIBRouteMapGroup,
       "alabgpMIBAspathListGroup": alabgpMIBAspathListGroup,
       "alabgpMIBPrefixListGroup": alabgpMIBPrefixListGroup,
       "alabgpMIBCommunityListGroup": alabgpMIBCommunityListGroup,
       "alabgpMIBAspathPriListGroup": alabgpMIBAspathPriListGroup,
       "alabgpMIBCommunityPriListGroup": alabgpMIBCommunityPriListGroup,
       "alabgpMIBRedistRouteGroup": alabgpMIBRedistRouteGroup,
       "alabgpMIBDebugGroup": alabgpMIBDebugGroup,
       "alabgpMIBNetwork6Group": alabgpMIBNetwork6Group,
       "alabgpMIBRoute6Group": alabgpMIBRoute6Group,
       "alabgpMIBPath6AttrGroup": alabgpMIBPath6AttrGroup,
       "alabgpMIBPeer6Group": alabgpMIBPeer6Group,
       "alcatelIND1BGPMIBCompliances": alcatelIND1BGPMIBCompliances,
       "alcatelIND1BGPMIBCompliance": alcatelIND1BGPMIBCompliance}
)
