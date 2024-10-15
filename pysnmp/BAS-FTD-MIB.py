# SNMP MIB module (BAS-FTD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-FTD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:24 2024
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

(basFtd,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basFtd")

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


# MODULE-IDENTITY

basFtdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasFtdObjects_ObjectIdentity = ObjectIdentity
basFtdObjects = _BasFtdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1)
)


class _BasFtdHeartBeatTimer_Type(Integer32):
    """Custom type basFtdHeartBeatTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BasFtdHeartBeatTimer_Type.__name__ = "Integer32"
_BasFtdHeartBeatTimer_Object = MibScalar
basFtdHeartBeatTimer = _BasFtdHeartBeatTimer_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 1),
    _BasFtdHeartBeatTimer_Type()
)
basFtdHeartBeatTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basFtdHeartBeatTimer.setStatus("current")
_BasFtdTableEligibilityCounter_Type = Counter32
_BasFtdTableEligibilityCounter_Object = MibScalar
basFtdTableEligibilityCounter = _BasFtdTableEligibilityCounter_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 2),
    _BasFtdTableEligibilityCounter_Type()
)
basFtdTableEligibilityCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdTableEligibilityCounter.setStatus("current")


class _BasFtdTableEligibilityCounterThreshold_Type(Integer32):
    """Custom type basFtdTableEligibilityCounterThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BasFtdTableEligibilityCounterThreshold_Type.__name__ = "Integer32"
_BasFtdTableEligibilityCounterThreshold_Object = MibScalar
basFtdTableEligibilityCounterThreshold = _BasFtdTableEligibilityCounterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 3),
    _BasFtdTableEligibilityCounterThreshold_Type()
)
basFtdTableEligibilityCounterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basFtdTableEligibilityCounterThreshold.setStatus("current")
_BasFtdIdleCounter_Type = Counter32
_BasFtdIdleCounter_Object = MibScalar
basFtdIdleCounter = _BasFtdIdleCounter_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 4),
    _BasFtdIdleCounter_Type()
)
basFtdIdleCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdIdleCounter.setStatus("current")


class _BasFtdIdleCounterThreshold_Type(Integer32):
    """Custom type basFtdIdleCounterThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BasFtdIdleCounterThreshold_Type.__name__ = "Integer32"
_BasFtdIdleCounterThreshold_Object = MibScalar
basFtdIdleCounterThreshold = _BasFtdIdleCounterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 5),
    _BasFtdIdleCounterThreshold_Type()
)
basFtdIdleCounterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basFtdIdleCounterThreshold.setStatus("current")
_BasFtdTableRequestCounter_Type = Counter32
_BasFtdTableRequestCounter_Object = MibScalar
basFtdTableRequestCounter = _BasFtdTableRequestCounter_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 6),
    _BasFtdTableRequestCounter_Type()
)
basFtdTableRequestCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdTableRequestCounter.setStatus("current")
_BasFtdPendingCallbackCounter_Type = Counter32
_BasFtdPendingCallbackCounter_Object = MibScalar
basFtdPendingCallbackCounter = _BasFtdPendingCallbackCounter_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 7),
    _BasFtdPendingCallbackCounter_Type()
)
basFtdPendingCallbackCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdPendingCallbackCounter.setStatus("current")


class _BasFtdPendingCallbackThreshold_Type(Integer32):
    """Custom type basFtdPendingCallbackThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BasFtdPendingCallbackThreshold_Type.__name__ = "Integer32"
_BasFtdPendingCallbackThreshold_Object = MibScalar
basFtdPendingCallbackThreshold = _BasFtdPendingCallbackThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 8),
    _BasFtdPendingCallbackThreshold_Type()
)
basFtdPendingCallbackThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basFtdPendingCallbackThreshold.setStatus("current")


class _BasFtdBootState_Type(Integer32):
    """Custom type basFtdBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cold", 2),
          ("null", 1),
          ("warm", 3))
    )


_BasFtdBootState_Type.__name__ = "Integer32"
_BasFtdBootState_Object = MibScalar
basFtdBootState = _BasFtdBootState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 9),
    _BasFtdBootState_Type()
)
basFtdBootState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basFtdBootState.setStatus("current")


class _BasFtdPurgeConfiguration_Type(Integer32):
    """Custom type basFtdPurgeConfiguration based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delayed", 2),
          ("immediate", 1))
    )


_BasFtdPurgeConfiguration_Type.__name__ = "Integer32"
_BasFtdPurgeConfiguration_Object = MibScalar
basFtdPurgeConfiguration = _BasFtdPurgeConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 10),
    _BasFtdPurgeConfiguration_Type()
)
basFtdPurgeConfiguration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basFtdPurgeConfiguration.setStatus("current")
_BasFtdUpdateRequests_Type = Counter32
_BasFtdUpdateRequests_Object = MibScalar
basFtdUpdateRequests = _BasFtdUpdateRequests_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 11),
    _BasFtdUpdateRequests_Type()
)
basFtdUpdateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdUpdateRequests.setStatus("current")
_BasFtdUpdatepackets_Type = Counter32
_BasFtdUpdatepackets_Object = MibScalar
basFtdUpdatepackets = _BasFtdUpdatepackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 12),
    _BasFtdUpdatepackets_Type()
)
basFtdUpdatepackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdUpdatepackets.setStatus("current")
_BasFtdTableRequests_Type = Counter32
_BasFtdTableRequests_Object = MibScalar
basFtdTableRequests = _BasFtdTableRequests_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 13),
    _BasFtdTableRequests_Type()
)
basFtdTableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdTableRequests.setStatus("current")
_BasFtdTablePackets_Type = Counter32
_BasFtdTablePackets_Object = MibScalar
basFtdTablePackets = _BasFtdTablePackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 14),
    _BasFtdTablePackets_Type()
)
basFtdTablePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdTablePackets.setStatus("current")
_BasFtdAllocatedPackets_Type = Counter32
_BasFtdAllocatedPackets_Object = MibScalar
basFtdAllocatedPackets = _BasFtdAllocatedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 15),
    _BasFtdAllocatedPackets_Type()
)
basFtdAllocatedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdAllocatedPackets.setStatus("current")
_BasFtdSentPackets_Type = Counter32
_BasFtdSentPackets_Object = MibScalar
basFtdSentPackets = _BasFtdSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 16),
    _BasFtdSentPackets_Type()
)
basFtdSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdSentPackets.setStatus("current")
_BasFtdFreedPackets_Type = Counter32
_BasFtdFreedPackets_Object = MibScalar
basFtdFreedPackets = _BasFtdFreedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 17),
    _BasFtdFreedPackets_Type()
)
basFtdFreedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdFreedPackets.setStatus("current")
_BasFtdSpuriousUpdatePackets_Type = Counter32
_BasFtdSpuriousUpdatePackets_Object = MibScalar
basFtdSpuriousUpdatePackets = _BasFtdSpuriousUpdatePackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 18),
    _BasFtdSpuriousUpdatePackets_Type()
)
basFtdSpuriousUpdatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdSpuriousUpdatePackets.setStatus("current")
_BasFtdSpuriousTablePackets_Type = Counter32
_BasFtdSpuriousTablePackets_Object = MibScalar
basFtdSpuriousTablePackets = _BasFtdSpuriousTablePackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 19),
    _BasFtdSpuriousTablePackets_Type()
)
basFtdSpuriousTablePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdSpuriousTablePackets.setStatus("current")
_BasFtdIgnoredUpdatePackets_Type = Counter32
_BasFtdIgnoredUpdatePackets_Object = MibScalar
basFtdIgnoredUpdatePackets = _BasFtdIgnoredUpdatePackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 20),
    _BasFtdIgnoredUpdatePackets_Type()
)
basFtdIgnoredUpdatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdIgnoredUpdatePackets.setStatus("current")
_BasFtdIgnoredTablePackets_Type = Counter32
_BasFtdIgnoredTablePackets_Object = MibScalar
basFtdIgnoredTablePackets = _BasFtdIgnoredTablePackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 21),
    _BasFtdIgnoredTablePackets_Type()
)
basFtdIgnoredTablePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdIgnoredTablePackets.setStatus("current")
_BasFtdInstalledUpdatePackets_Type = Counter32
_BasFtdInstalledUpdatePackets_Object = MibScalar
basFtdInstalledUpdatePackets = _BasFtdInstalledUpdatePackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 22),
    _BasFtdInstalledUpdatePackets_Type()
)
basFtdInstalledUpdatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdInstalledUpdatePackets.setStatus("current")
_BasFtdInstalledTablePackets_Type = Counter32
_BasFtdInstalledTablePackets_Object = MibScalar
basFtdInstalledTablePackets = _BasFtdInstalledTablePackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 23),
    _BasFtdInstalledTablePackets_Type()
)
basFtdInstalledTablePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdInstalledTablePackets.setStatus("current")
_BasFtdStoredTablePackets_Type = Counter32
_BasFtdStoredTablePackets_Object = MibScalar
basFtdStoredTablePackets = _BasFtdStoredTablePackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 24),
    _BasFtdStoredTablePackets_Type()
)
basFtdStoredTablePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdStoredTablePackets.setStatus("current")
_BasFtdRevisionPackets_Type = Counter32
_BasFtdRevisionPackets_Object = MibScalar
basFtdRevisionPackets = _BasFtdRevisionPackets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 25),
    _BasFtdRevisionPackets_Type()
)
basFtdRevisionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdRevisionPackets.setStatus("current")


class _BasFtdFailureCode_Type(Integer32):
    """Custom type basFtdFailureCode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109)
        )
    )
    namedValues = NamedValues(
        *(("add-route-failure", 109),
          ("dequeue", 2),
          ("external", 100),
          ("finite-state-machine", 1),
          ("nonnull-table-pkt", 5),
          ("nonnull-update-pkt", 4),
          ("null-table-fia", 3),
          ("packet-allocation", 105),
          ("packet-corruption", 106),
          ("pending-threshold", 6),
          ("rbp-callback", 104),
          ("rbp-registration", 101),
          ("rbp-send", 103),
          ("rte-error-bad-prefix", 107),
          ("rte-error-bad-version", 108),
          ("uninitialized-storage", 7),
          ("unknown-pkt", 102))
    )


_BasFtdFailureCode_Type.__name__ = "Integer32"
_BasFtdFailureCode_Object = MibScalar
basFtdFailureCode = _BasFtdFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 26),
    _BasFtdFailureCode_Type()
)
basFtdFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdFailureCode.setStatus("current")
_BasFtdRevision_Type = Integer32
_BasFtdRevision_Object = MibScalar
basFtdRevision = _BasFtdRevision_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 27),
    _BasFtdRevision_Type()
)
basFtdRevision.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basFtdRevision.setStatus("current")
_BasFtdPresentFsmState_Type = Integer32
_BasFtdPresentFsmState_Object = MibScalar
basFtdPresentFsmState = _BasFtdPresentFsmState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 28),
    _BasFtdPresentFsmState_Type()
)
basFtdPresentFsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdPresentFsmState.setStatus("current")
_BasFtdFsmRestarts_Type = Counter32
_BasFtdFsmRestarts_Object = MibScalar
basFtdFsmRestarts = _BasFtdFsmRestarts_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 29),
    _BasFtdFsmRestarts_Type()
)
basFtdFsmRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basFtdFsmRestarts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-FTD-MIB",
    **{"basFtdMib": basFtdMib,
       "basFtdObjects": basFtdObjects,
       "basFtdHeartBeatTimer": basFtdHeartBeatTimer,
       "basFtdTableEligibilityCounter": basFtdTableEligibilityCounter,
       "basFtdTableEligibilityCounterThreshold": basFtdTableEligibilityCounterThreshold,
       "basFtdIdleCounter": basFtdIdleCounter,
       "basFtdIdleCounterThreshold": basFtdIdleCounterThreshold,
       "basFtdTableRequestCounter": basFtdTableRequestCounter,
       "basFtdPendingCallbackCounter": basFtdPendingCallbackCounter,
       "basFtdPendingCallbackThreshold": basFtdPendingCallbackThreshold,
       "basFtdBootState": basFtdBootState,
       "basFtdPurgeConfiguration": basFtdPurgeConfiguration,
       "basFtdUpdateRequests": basFtdUpdateRequests,
       "basFtdUpdatepackets": basFtdUpdatepackets,
       "basFtdTableRequests": basFtdTableRequests,
       "basFtdTablePackets": basFtdTablePackets,
       "basFtdAllocatedPackets": basFtdAllocatedPackets,
       "basFtdSentPackets": basFtdSentPackets,
       "basFtdFreedPackets": basFtdFreedPackets,
       "basFtdSpuriousUpdatePackets": basFtdSpuriousUpdatePackets,
       "basFtdSpuriousTablePackets": basFtdSpuriousTablePackets,
       "basFtdIgnoredUpdatePackets": basFtdIgnoredUpdatePackets,
       "basFtdIgnoredTablePackets": basFtdIgnoredTablePackets,
       "basFtdInstalledUpdatePackets": basFtdInstalledUpdatePackets,
       "basFtdInstalledTablePackets": basFtdInstalledTablePackets,
       "basFtdStoredTablePackets": basFtdStoredTablePackets,
       "basFtdRevisionPackets": basFtdRevisionPackets,
       "basFtdFailureCode": basFtdFailureCode,
       "basFtdRevision": basFtdRevision,
       "basFtdPresentFsmState": basFtdPresentFsmState,
       "basFtdFsmRestarts": basFtdFsmRestarts}
)
