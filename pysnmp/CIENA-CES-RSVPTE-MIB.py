# SNMP MIB module (CIENA-CES-RSVPTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-RSVPTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:07 2024
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

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesRsvpteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16)
)
cienaCesRsvpteMIB.setRevisions(
        ("2016-07-15 00:00",
         "2016-07-14 00:00",
         "2016-07-04 00:00",
         "2013-05-08 00:00",
         "2011-02-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdvertisedLabel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("implicitnull", 1),
          ("nonreserved", 99))
    )



class RsvpOperStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



class RsvpGRMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("helpNeighbor", 1),
          ("notApplicable", 3),
          ("restartCapable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesRsvpteMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesRsvpteMIBObjects = _CienaCesRsvpteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1)
)
_CienaCesRsvpteObjects_ObjectIdentity = ObjectIdentity
cienaCesRsvpteObjects = _CienaCesRsvpteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1)
)
_CienaCesRsvpteAdminStatus_Type = CienaGlobalState
_CienaCesRsvpteAdminStatus_Object = MibScalar
cienaCesRsvpteAdminStatus = _CienaCesRsvpteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 1),
    _CienaCesRsvpteAdminStatus_Type()
)
cienaCesRsvpteAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteAdminStatus.setStatus("current")
_CienaCesRsvpteOperStatus_Type = RsvpOperStatus
_CienaCesRsvpteOperStatus_Object = MibScalar
cienaCesRsvpteOperStatus = _CienaCesRsvpteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 2),
    _CienaCesRsvpteOperStatus_Type()
)
cienaCesRsvpteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteOperStatus.setStatus("current")


class _CienaCesRsvpteRetryInterval_Type(Unsigned32):
    """Custom type cienaCesRsvpteRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65),
    )


_CienaCesRsvpteRetryInterval_Type.__name__ = "Unsigned32"
_CienaCesRsvpteRetryInterval_Object = MibScalar
cienaCesRsvpteRetryInterval = _CienaCesRsvpteRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 3),
    _CienaCesRsvpteRetryInterval_Type()
)
cienaCesRsvpteRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRsvpteRetryInterval.setUnits("seconds")


class _CienaCesRsvpteRetryInfiniteState_Type(Integer32):
    """Custom type cienaCesRsvpteRetryInfiniteState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesRsvpteRetryInfiniteState_Type.__name__ = "Integer32"
_CienaCesRsvpteRetryInfiniteState_Object = MibScalar
cienaCesRsvpteRetryInfiniteState = _CienaCesRsvpteRetryInfiniteState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 4),
    _CienaCesRsvpteRetryInfiniteState_Type()
)
cienaCesRsvpteRetryInfiniteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRetryInfiniteState.setStatus("current")


class _CienaCesRsvpteRetryMax_Type(Integer32):
    """Custom type cienaCesRsvpteRetryMax based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesRsvpteRetryMax_Type.__name__ = "Integer32"
_CienaCesRsvpteRetryMax_Object = MibScalar
cienaCesRsvpteRetryMax = _CienaCesRsvpteRetryMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 5),
    _CienaCesRsvpteRetryMax_Type()
)
cienaCesRsvpteRetryMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRetryMax.setStatus("current")


class _CienaCesRsvpteRefreshInterval_Type(Integer32):
    """Custom type cienaCesRsvpteRefreshInterval based on Integer32"""
    defaultValue = 30000


_CienaCesRsvpteRefreshInterval_Object = MibScalar
cienaCesRsvpteRefreshInterval = _CienaCesRsvpteRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 6),
    _CienaCesRsvpteRefreshInterval_Type()
)
cienaCesRsvpteRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRsvpteRefreshInterval.setUnits("milliseconds")


class _CienaCesRsvpteRefreshMultiple_Type(Integer32):
    """Custom type cienaCesRsvpteRefreshMultiple based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_CienaCesRsvpteRefreshMultiple_Type.__name__ = "Integer32"
_CienaCesRsvpteRefreshMultiple_Object = MibScalar
cienaCesRsvpteRefreshMultiple = _CienaCesRsvpteRefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 7),
    _CienaCesRsvpteRefreshMultiple_Type()
)
cienaCesRsvpteRefreshMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRefreshMultiple.setStatus("current")


class _CienaCesRsvpteRfrshSlewDenom_Type(Integer32):
    """Custom type cienaCesRsvpteRfrshSlewDenom based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_CienaCesRsvpteRfrshSlewDenom_Type.__name__ = "Integer32"
_CienaCesRsvpteRfrshSlewDenom_Object = MibScalar
cienaCesRsvpteRfrshSlewDenom = _CienaCesRsvpteRfrshSlewDenom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 8),
    _CienaCesRsvpteRfrshSlewDenom_Type()
)
cienaCesRsvpteRfrshSlewDenom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRfrshSlewDenom.setStatus("deprecated")


class _CienaCesRsvpteRfrshSlewNumerator_Type(Integer32):
    """Custom type cienaCesRsvpteRfrshSlewNumerator based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_CienaCesRsvpteRfrshSlewNumerator_Type.__name__ = "Integer32"
_CienaCesRsvpteRfrshSlewNumerator_Object = MibScalar
cienaCesRsvpteRfrshSlewNumerator = _CienaCesRsvpteRfrshSlewNumerator_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 9),
    _CienaCesRsvpteRfrshSlewNumerator_Type()
)
cienaCesRsvpteRfrshSlewNumerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRfrshSlewNumerator.setStatus("deprecated")


class _CienaCesRsvpteBlockadeMultiple_Type(Integer32):
    """Custom type cienaCesRsvpteBlockadeMultiple based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_CienaCesRsvpteBlockadeMultiple_Type.__name__ = "Integer32"
_CienaCesRsvpteBlockadeMultiple_Object = MibScalar
cienaCesRsvpteBlockadeMultiple = _CienaCesRsvpteBlockadeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 10),
    _CienaCesRsvpteBlockadeMultiple_Type()
)
cienaCesRsvpteBlockadeMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteBlockadeMultiple.setStatus("current")


class _CienaCesRsvpteLSPSetupPriority_Type(Integer32):
    """Custom type cienaCesRsvpteLSPSetupPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesRsvpteLSPSetupPriority_Type.__name__ = "Integer32"
_CienaCesRsvpteLSPSetupPriority_Object = MibScalar
cienaCesRsvpteLSPSetupPriority = _CienaCesRsvpteLSPSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 11),
    _CienaCesRsvpteLSPSetupPriority_Type()
)
cienaCesRsvpteLSPSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteLSPSetupPriority.setStatus("current")


class _CienaCesRsvpteLSPHoldingPriority_Type(Integer32):
    """Custom type cienaCesRsvpteLSPHoldingPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesRsvpteLSPHoldingPriority_Type.__name__ = "Integer32"
_CienaCesRsvpteLSPHoldingPriority_Object = MibScalar
cienaCesRsvpteLSPHoldingPriority = _CienaCesRsvpteLSPHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 12),
    _CienaCesRsvpteLSPHoldingPriority_Type()
)
cienaCesRsvpteLSPHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteLSPHoldingPriority.setStatus("current")


class _CienaCesRsvpteUseHopByHop_Type(TruthValue):
    """Custom type cienaCesRsvpteUseHopByHop based on TruthValue"""


_CienaCesRsvpteUseHopByHop_Object = MibScalar
cienaCesRsvpteUseHopByHop = _CienaCesRsvpteUseHopByHop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 13),
    _CienaCesRsvpteUseHopByHop_Type()
)
cienaCesRsvpteUseHopByHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteUseHopByHop.setStatus("current")


class _CienaCesRsvpteRestartCapable_Type(TruthValue):
    """Custom type cienaCesRsvpteRestartCapable based on TruthValue"""


_CienaCesRsvpteRestartCapable_Object = MibScalar
cienaCesRsvpteRestartCapable = _CienaCesRsvpteRestartCapable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 14),
    _CienaCesRsvpteRestartCapable_Type()
)
cienaCesRsvpteRestartCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRestartCapable.setStatus("current")


class _CienaCesRsvpteRestartTime_Type(Unsigned32):
    """Custom type cienaCesRsvpteRestartTime based on Unsigned32"""
    defaultValue = 60000


_CienaCesRsvpteRestartTime_Object = MibScalar
cienaCesRsvpteRestartTime = _CienaCesRsvpteRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 15),
    _CienaCesRsvpteRestartTime_Type()
)
cienaCesRsvpteRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRestartTime.setStatus("current")


class _CienaCesRsvpteRecoveryTime_Type(Unsigned32):
    """Custom type cienaCesRsvpteRecoveryTime based on Unsigned32"""
    defaultValue = 120000


_CienaCesRsvpteRecoveryTime_Object = MibScalar
cienaCesRsvpteRecoveryTime = _CienaCesRsvpteRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 16),
    _CienaCesRsvpteRecoveryTime_Type()
)
cienaCesRsvpteRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRecoveryTime.setStatus("current")


class _CienaCesRsvpteMinPeerRestart_Type(Integer32):
    """Custom type cienaCesRsvpteMinPeerRestart based on Integer32"""
    defaultValue = 0


_CienaCesRsvpteMinPeerRestart_Object = MibScalar
cienaCesRsvpteMinPeerRestart = _CienaCesRsvpteMinPeerRestart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 17),
    _CienaCesRsvpteMinPeerRestart_Type()
)
cienaCesRsvpteMinPeerRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteMinPeerRestart.setStatus("current")


class _CienaCesRsvpteRefreshSlewDenominator_Type(Integer32):
    """Custom type cienaCesRsvpteRefreshSlewDenominator based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_CienaCesRsvpteRefreshSlewDenominator_Type.__name__ = "Integer32"
_CienaCesRsvpteRefreshSlewDenominator_Object = MibScalar
cienaCesRsvpteRefreshSlewDenominator = _CienaCesRsvpteRefreshSlewDenominator_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 18),
    _CienaCesRsvpteRefreshSlewDenominator_Type()
)
cienaCesRsvpteRefreshSlewDenominator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRefreshSlewDenominator.setStatus("current")


class _CienaCesRsvpteRefreshSlewNumerator_Type(Integer32):
    """Custom type cienaCesRsvpteRefreshSlewNumerator based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_CienaCesRsvpteRefreshSlewNumerator_Type.__name__ = "Integer32"
_CienaCesRsvpteRefreshSlewNumerator_Object = MibScalar
cienaCesRsvpteRefreshSlewNumerator = _CienaCesRsvpteRefreshSlewNumerator_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 19),
    _CienaCesRsvpteRefreshSlewNumerator_Type()
)
cienaCesRsvpteRefreshSlewNumerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteRefreshSlewNumerator.setStatus("current")
_CienaCesRsvpteGRAdminStatus_Type = CienaGlobalState
_CienaCesRsvpteGRAdminStatus_Object = MibScalar
cienaCesRsvpteGRAdminStatus = _CienaCesRsvpteGRAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 20),
    _CienaCesRsvpteGRAdminStatus_Type()
)
cienaCesRsvpteGRAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteGRAdminStatus.setStatus("current")
_CienaCesRsvpteGRMode_Type = RsvpGRMode
_CienaCesRsvpteGRMode_Object = MibScalar
cienaCesRsvpteGRMode = _CienaCesRsvpteGRMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 21),
    _CienaCesRsvpteGRMode_Type()
)
cienaCesRsvpteGRMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteGRMode.setStatus("current")
_CienaCesRsvpte_ObjectIdentity = ObjectIdentity
cienaCesRsvpte = _CienaCesRsvpte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2)
)
_CienaCesRsvpteIfTable_Object = MibTable
cienaCesRsvpteIfTable = _CienaCesRsvpteIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesRsvpteIfTable.setStatus("current")
_CienaCesRsvpteIfEntry_Object = MibTableRow
cienaCesRsvpteIfEntry = _CienaCesRsvpteIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1)
)
cienaCesRsvpteIfEntry.setIndexNames(
    (0, "CIENA-CES-RSVPTE-MIB", "cienaCesRsvpteIfIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRsvpteIfEntry.setStatus("current")


class _CienaCesRsvpteIfIndex_Type(Integer32):
    """Custom type cienaCesRsvpteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CienaCesRsvpteIfIndex_Type.__name__ = "Integer32"
_CienaCesRsvpteIfIndex_Object = MibTableColumn
cienaCesRsvpteIfIndex = _CienaCesRsvpteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 1),
    _CienaCesRsvpteIfIndex_Type()
)
cienaCesRsvpteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfIndex.setStatus("current")


class _CienaCesRsvpteIfName_Type(OctetString):
    """Custom type cienaCesRsvpteIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesRsvpteIfName_Type.__name__ = "OctetString"
_CienaCesRsvpteIfName_Object = MibTableColumn
cienaCesRsvpteIfName = _CienaCesRsvpteIfName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 2),
    _CienaCesRsvpteIfName_Type()
)
cienaCesRsvpteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfName.setStatus("current")
_CienaCesRsvpteIfIpAddr_Type = IpAddress
_CienaCesRsvpteIfIpAddr_Object = MibTableColumn
cienaCesRsvpteIfIpAddr = _CienaCesRsvpteIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 3),
    _CienaCesRsvpteIfIpAddr_Type()
)
cienaCesRsvpteIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfIpAddr.setStatus("current")


class _CienaCesRsvpteIfMtu_Type(Integer32):
    """Custom type cienaCesRsvpteIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 9216),
    )


_CienaCesRsvpteIfMtu_Type.__name__ = "Integer32"
_CienaCesRsvpteIfMtu_Object = MibTableColumn
cienaCesRsvpteIfMtu = _CienaCesRsvpteIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 4),
    _CienaCesRsvpteIfMtu_Type()
)
cienaCesRsvpteIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfMtu.setStatus("deprecated")
_CienaCesRsvpteIfAdminStatus_Type = CienaGlobalState
_CienaCesRsvpteIfAdminStatus_Object = MibTableColumn
cienaCesRsvpteIfAdminStatus = _CienaCesRsvpteIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 5),
    _CienaCesRsvpteIfAdminStatus_Type()
)
cienaCesRsvpteIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfAdminStatus.setStatus("current")


class _CienaCesRsvpteIfOperStatus_Type(Integer32):
    """Custom type cienaCesRsvpteIfOperStatus based on Integer32"""
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


_CienaCesRsvpteIfOperStatus_Type.__name__ = "Integer32"
_CienaCesRsvpteIfOperStatus_Object = MibTableColumn
cienaCesRsvpteIfOperStatus = _CienaCesRsvpteIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 6),
    _CienaCesRsvpteIfOperStatus_Type()
)
cienaCesRsvpteIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfOperStatus.setStatus("current")


class _CienaCesRsvpteIfHelloInterval_Type(Unsigned32):
    """Custom type cienaCesRsvpteIfHelloInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CienaCesRsvpteIfHelloInterval_Type.__name__ = "Unsigned32"
_CienaCesRsvpteIfHelloInterval_Object = MibTableColumn
cienaCesRsvpteIfHelloInterval = _CienaCesRsvpteIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 7),
    _CienaCesRsvpteIfHelloInterval_Type()
)
cienaCesRsvpteIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfHelloInterval.setUnits("seconds")


class _CienaCesRsvpteIfHelloTolerance_Type(Unsigned32):
    """Custom type cienaCesRsvpteIfHelloTolerance based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CienaCesRsvpteIfHelloTolerance_Type.__name__ = "Unsigned32"
_CienaCesRsvpteIfHelloTolerance_Object = MibTableColumn
cienaCesRsvpteIfHelloTolerance = _CienaCesRsvpteIfHelloTolerance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 8),
    _CienaCesRsvpteIfHelloTolerance_Type()
)
cienaCesRsvpteIfHelloTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfHelloTolerance.setStatus("current")


class _CienaCesRsvpteIfAdvertisedLabel_Type(AdvertisedLabel):
    """Custom type cienaCesRsvpteIfAdvertisedLabel based on AdvertisedLabel"""
    defaultValue = 99


_CienaCesRsvpteIfAdvertisedLabel_Object = MibTableColumn
cienaCesRsvpteIfAdvertisedLabel = _CienaCesRsvpteIfAdvertisedLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 9),
    _CienaCesRsvpteIfAdvertisedLabel_Type()
)
cienaCesRsvpteIfAdvertisedLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRsvpteIfAdvertisedLabel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-RSVPTE-MIB",
    **{"AdvertisedLabel": AdvertisedLabel,
       "RsvpOperStatus": RsvpOperStatus,
       "RsvpGRMode": RsvpGRMode,
       "cienaCesRsvpteMIB": cienaCesRsvpteMIB,
       "cienaCesRsvpteMIBObjects": cienaCesRsvpteMIBObjects,
       "cienaCesRsvpteObjects": cienaCesRsvpteObjects,
       "cienaCesRsvpteAdminStatus": cienaCesRsvpteAdminStatus,
       "cienaCesRsvpteOperStatus": cienaCesRsvpteOperStatus,
       "cienaCesRsvpteRetryInterval": cienaCesRsvpteRetryInterval,
       "cienaCesRsvpteRetryInfiniteState": cienaCesRsvpteRetryInfiniteState,
       "cienaCesRsvpteRetryMax": cienaCesRsvpteRetryMax,
       "cienaCesRsvpteRefreshInterval": cienaCesRsvpteRefreshInterval,
       "cienaCesRsvpteRefreshMultiple": cienaCesRsvpteRefreshMultiple,
       "cienaCesRsvpteRfrshSlewDenom": cienaCesRsvpteRfrshSlewDenom,
       "cienaCesRsvpteRfrshSlewNumerator": cienaCesRsvpteRfrshSlewNumerator,
       "cienaCesRsvpteBlockadeMultiple": cienaCesRsvpteBlockadeMultiple,
       "cienaCesRsvpteLSPSetupPriority": cienaCesRsvpteLSPSetupPriority,
       "cienaCesRsvpteLSPHoldingPriority": cienaCesRsvpteLSPHoldingPriority,
       "cienaCesRsvpteUseHopByHop": cienaCesRsvpteUseHopByHop,
       "cienaCesRsvpteRestartCapable": cienaCesRsvpteRestartCapable,
       "cienaCesRsvpteRestartTime": cienaCesRsvpteRestartTime,
       "cienaCesRsvpteRecoveryTime": cienaCesRsvpteRecoveryTime,
       "cienaCesRsvpteMinPeerRestart": cienaCesRsvpteMinPeerRestart,
       "cienaCesRsvpteRefreshSlewDenominator": cienaCesRsvpteRefreshSlewDenominator,
       "cienaCesRsvpteRefreshSlewNumerator": cienaCesRsvpteRefreshSlewNumerator,
       "cienaCesRsvpteGRAdminStatus": cienaCesRsvpteGRAdminStatus,
       "cienaCesRsvpteGRMode": cienaCesRsvpteGRMode,
       "cienaCesRsvpte": cienaCesRsvpte,
       "cienaCesRsvpteIfTable": cienaCesRsvpteIfTable,
       "cienaCesRsvpteIfEntry": cienaCesRsvpteIfEntry,
       "cienaCesRsvpteIfIndex": cienaCesRsvpteIfIndex,
       "cienaCesRsvpteIfName": cienaCesRsvpteIfName,
       "cienaCesRsvpteIfIpAddr": cienaCesRsvpteIfIpAddr,
       "cienaCesRsvpteIfMtu": cienaCesRsvpteIfMtu,
       "cienaCesRsvpteIfAdminStatus": cienaCesRsvpteIfAdminStatus,
       "cienaCesRsvpteIfOperStatus": cienaCesRsvpteIfOperStatus,
       "cienaCesRsvpteIfHelloInterval": cienaCesRsvpteIfHelloInterval,
       "cienaCesRsvpteIfHelloTolerance": cienaCesRsvpteIfHelloTolerance,
       "cienaCesRsvpteIfAdvertisedLabel": cienaCesRsvpteIfAdvertisedLabel}
)
