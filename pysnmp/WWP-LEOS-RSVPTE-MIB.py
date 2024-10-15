# SNMP MIB module (WWP-LEOS-RSVPTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-RSVPTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:08 2024
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

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosRsvpteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30)
)
wwpLeosRsvpteMIB.setRevisions(
        ("2011-07-06 00:00",
         "2005-08-08 17:00")
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



# MIB Managed Objects in the order of their OIDs

_WwpLeosRsvpteMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosRsvpteMIBObjects = _WwpLeosRsvpteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1)
)
_WwpLeosRsvpteObjects_ObjectIdentity = ObjectIdentity
wwpLeosRsvpteObjects = _WwpLeosRsvpteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1)
)


class _WwpLeosRsvpteAdminStatus_Type(Integer32):
    """Custom type wwpLeosRsvpteAdminStatus based on Integer32"""
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


_WwpLeosRsvpteAdminStatus_Type.__name__ = "Integer32"
_WwpLeosRsvpteAdminStatus_Object = MibScalar
wwpLeosRsvpteAdminStatus = _WwpLeosRsvpteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 1),
    _WwpLeosRsvpteAdminStatus_Type()
)
wwpLeosRsvpteAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRsvpteAdminStatus.setStatus("current")


class _WwpLeosRsvpteOperStatus_Type(Integer32):
    """Custom type wwpLeosRsvpteOperStatus based on Integer32"""
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
        *(("actFailed", 5),
          ("down", 2),
          ("goingDown", 4),
          ("goingUp", 3),
          ("up", 1))
    )


_WwpLeosRsvpteOperStatus_Type.__name__ = "Integer32"
_WwpLeosRsvpteOperStatus_Object = MibScalar
wwpLeosRsvpteOperStatus = _WwpLeosRsvpteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 2),
    _WwpLeosRsvpteOperStatus_Type()
)
wwpLeosRsvpteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteOperStatus.setStatus("current")


class _WwpLeosRsvpteRetryInterval_Type(Unsigned32):
    """Custom type wwpLeosRsvpteRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65),
    )


_WwpLeosRsvpteRetryInterval_Type.__name__ = "Unsigned32"
_WwpLeosRsvpteRetryInterval_Object = MibScalar
wwpLeosRsvpteRetryInterval = _WwpLeosRsvpteRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 3),
    _WwpLeosRsvpteRetryInterval_Type()
)
wwpLeosRsvpteRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRetryInterval.setUnits("seconds")


class _WwpLeosRsvpteRetryInfiniteState_Type(Integer32):
    """Custom type wwpLeosRsvpteRetryInfiniteState based on Integer32"""
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


_WwpLeosRsvpteRetryInfiniteState_Type.__name__ = "Integer32"
_WwpLeosRsvpteRetryInfiniteState_Object = MibScalar
wwpLeosRsvpteRetryInfiniteState = _WwpLeosRsvpteRetryInfiniteState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 4),
    _WwpLeosRsvpteRetryInfiniteState_Type()
)
wwpLeosRsvpteRetryInfiniteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRetryInfiniteState.setStatus("current")


class _WwpLeosRsvpteRetryMax_Type(Integer32):
    """Custom type wwpLeosRsvpteRetryMax based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpLeosRsvpteRetryMax_Type.__name__ = "Integer32"
_WwpLeosRsvpteRetryMax_Object = MibScalar
wwpLeosRsvpteRetryMax = _WwpLeosRsvpteRetryMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 5),
    _WwpLeosRsvpteRetryMax_Type()
)
wwpLeosRsvpteRetryMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRetryMax.setStatus("current")


class _WwpLeosRsvpteRefreshInterval_Type(Integer32):
    """Custom type wwpLeosRsvpteRefreshInterval based on Integer32"""
    defaultValue = 30000


_WwpLeosRsvpteRefreshInterval_Object = MibScalar
wwpLeosRsvpteRefreshInterval = _WwpLeosRsvpteRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 6),
    _WwpLeosRsvpteRefreshInterval_Type()
)
wwpLeosRsvpteRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRefreshInterval.setUnits("milliseconds")


class _WwpLeosRsvpteRefreshMultiple_Type(Integer32):
    """Custom type wwpLeosRsvpteRefreshMultiple based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_WwpLeosRsvpteRefreshMultiple_Type.__name__ = "Integer32"
_WwpLeosRsvpteRefreshMultiple_Object = MibScalar
wwpLeosRsvpteRefreshMultiple = _WwpLeosRsvpteRefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 7),
    _WwpLeosRsvpteRefreshMultiple_Type()
)
wwpLeosRsvpteRefreshMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRefreshMultiple.setStatus("current")


class _WwpLeosRsvpteRfrshSlewDenom_Type(Integer32):
    """Custom type wwpLeosRsvpteRfrshSlewDenom based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_WwpLeosRsvpteRfrshSlewDenom_Type.__name__ = "Integer32"
_WwpLeosRsvpteRfrshSlewDenom_Object = MibScalar
wwpLeosRsvpteRfrshSlewDenom = _WwpLeosRsvpteRfrshSlewDenom_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 8),
    _WwpLeosRsvpteRfrshSlewDenom_Type()
)
wwpLeosRsvpteRfrshSlewDenom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRfrshSlewDenom.setStatus("current")


class _WwpLeosRsvpteRfrshSlewNumerator_Type(Integer32):
    """Custom type wwpLeosRsvpteRfrshSlewNumerator based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_WwpLeosRsvpteRfrshSlewNumerator_Type.__name__ = "Integer32"
_WwpLeosRsvpteRfrshSlewNumerator_Object = MibScalar
wwpLeosRsvpteRfrshSlewNumerator = _WwpLeosRsvpteRfrshSlewNumerator_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 9),
    _WwpLeosRsvpteRfrshSlewNumerator_Type()
)
wwpLeosRsvpteRfrshSlewNumerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRfrshSlewNumerator.setStatus("current")


class _WwpLeosRsvpteBlockadeMultiple_Type(Integer32):
    """Custom type wwpLeosRsvpteBlockadeMultiple based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_WwpLeosRsvpteBlockadeMultiple_Type.__name__ = "Integer32"
_WwpLeosRsvpteBlockadeMultiple_Object = MibScalar
wwpLeosRsvpteBlockadeMultiple = _WwpLeosRsvpteBlockadeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 10),
    _WwpLeosRsvpteBlockadeMultiple_Type()
)
wwpLeosRsvpteBlockadeMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteBlockadeMultiple.setStatus("current")


class _WwpLeosRsvpteLSPSetupPriority_Type(Integer32):
    """Custom type wwpLeosRsvpteLSPSetupPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosRsvpteLSPSetupPriority_Type.__name__ = "Integer32"
_WwpLeosRsvpteLSPSetupPriority_Object = MibScalar
wwpLeosRsvpteLSPSetupPriority = _WwpLeosRsvpteLSPSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 11),
    _WwpLeosRsvpteLSPSetupPriority_Type()
)
wwpLeosRsvpteLSPSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteLSPSetupPriority.setStatus("current")


class _WwpLeosRsvpteLSPHoldingPriority_Type(Integer32):
    """Custom type wwpLeosRsvpteLSPHoldingPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosRsvpteLSPHoldingPriority_Type.__name__ = "Integer32"
_WwpLeosRsvpteLSPHoldingPriority_Object = MibScalar
wwpLeosRsvpteLSPHoldingPriority = _WwpLeosRsvpteLSPHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 12),
    _WwpLeosRsvpteLSPHoldingPriority_Type()
)
wwpLeosRsvpteLSPHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteLSPHoldingPriority.setStatus("current")


class _WwpLeosRsvpteUseHopByHop_Type(TruthValue):
    """Custom type wwpLeosRsvpteUseHopByHop based on TruthValue"""


_WwpLeosRsvpteUseHopByHop_Object = MibScalar
wwpLeosRsvpteUseHopByHop = _WwpLeosRsvpteUseHopByHop_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 13),
    _WwpLeosRsvpteUseHopByHop_Type()
)
wwpLeosRsvpteUseHopByHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteUseHopByHop.setStatus("current")


class _WwpLeosRsvpteRestartCapable_Type(TruthValue):
    """Custom type wwpLeosRsvpteRestartCapable based on TruthValue"""


_WwpLeosRsvpteRestartCapable_Object = MibScalar
wwpLeosRsvpteRestartCapable = _WwpLeosRsvpteRestartCapable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 14),
    _WwpLeosRsvpteRestartCapable_Type()
)
wwpLeosRsvpteRestartCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRestartCapable.setStatus("current")


class _WwpLeosRsvpteRestartTime_Type(Unsigned32):
    """Custom type wwpLeosRsvpteRestartTime based on Unsigned32"""
    defaultValue = 10000


_WwpLeosRsvpteRestartTime_Object = MibScalar
wwpLeosRsvpteRestartTime = _WwpLeosRsvpteRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 15),
    _WwpLeosRsvpteRestartTime_Type()
)
wwpLeosRsvpteRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRestartTime.setStatus("current")


class _WwpLeosRsvpteRecoveryTime_Type(Unsigned32):
    """Custom type wwpLeosRsvpteRecoveryTime based on Unsigned32"""
    defaultValue = 10000


_WwpLeosRsvpteRecoveryTime_Object = MibScalar
wwpLeosRsvpteRecoveryTime = _WwpLeosRsvpteRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 16),
    _WwpLeosRsvpteRecoveryTime_Type()
)
wwpLeosRsvpteRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteRecoveryTime.setStatus("current")


class _WwpLeosRsvpteMinPeerRestart_Type(Integer32):
    """Custom type wwpLeosRsvpteMinPeerRestart based on Integer32"""
    defaultValue = 0


_WwpLeosRsvpteMinPeerRestart_Object = MibScalar
wwpLeosRsvpteMinPeerRestart = _WwpLeosRsvpteMinPeerRestart_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 1, 17),
    _WwpLeosRsvpteMinPeerRestart_Type()
)
wwpLeosRsvpteMinPeerRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteMinPeerRestart.setStatus("current")
_WwpLeosRsvpte_ObjectIdentity = ObjectIdentity
wwpLeosRsvpte = _WwpLeosRsvpte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2)
)
_WwpLeosRsvpteIfTable_Object = MibTable
wwpLeosRsvpteIfTable = _WwpLeosRsvpteIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfTable.setStatus("current")
_WwpLeosRsvpteIfEntry_Object = MibTableRow
wwpLeosRsvpteIfEntry = _WwpLeosRsvpteIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1)
)
wwpLeosRsvpteIfEntry.setIndexNames(
    (0, "WWP-LEOS-RSVPTE-MIB", "wwpLeosRsvpteIfIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfEntry.setStatus("current")


class _WwpLeosRsvpteIfName_Type(DisplayString):
    """Custom type wwpLeosRsvpteIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosRsvpteIfName_Type.__name__ = "DisplayString"
_WwpLeosRsvpteIfName_Object = MibTableColumn
wwpLeosRsvpteIfName = _WwpLeosRsvpteIfName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 1),
    _WwpLeosRsvpteIfName_Type()
)
wwpLeosRsvpteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfName.setStatus("current")


class _WwpLeosRsvpteIfIndex_Type(Integer32):
    """Custom type wwpLeosRsvpteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosRsvpteIfIndex_Type.__name__ = "Integer32"
_WwpLeosRsvpteIfIndex_Object = MibTableColumn
wwpLeosRsvpteIfIndex = _WwpLeosRsvpteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 2),
    _WwpLeosRsvpteIfIndex_Type()
)
wwpLeosRsvpteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfIndex.setStatus("current")
_WwpLeosRsvpteIfIpAddr_Type = IpAddress
_WwpLeosRsvpteIfIpAddr_Object = MibTableColumn
wwpLeosRsvpteIfIpAddr = _WwpLeosRsvpteIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 3),
    _WwpLeosRsvpteIfIpAddr_Type()
)
wwpLeosRsvpteIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfIpAddr.setStatus("current")


class _WwpLeosRsvpteIfMtu_Type(Integer32):
    """Custom type wwpLeosRsvpteIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 9216),
    )


_WwpLeosRsvpteIfMtu_Type.__name__ = "Integer32"
_WwpLeosRsvpteIfMtu_Object = MibTableColumn
wwpLeosRsvpteIfMtu = _WwpLeosRsvpteIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 4),
    _WwpLeosRsvpteIfMtu_Type()
)
wwpLeosRsvpteIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfMtu.setStatus("current")


class _WwpLeosRsvpteIfAdminStatus_Type(Integer32):
    """Custom type wwpLeosRsvpteIfAdminStatus based on Integer32"""
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


_WwpLeosRsvpteIfAdminStatus_Type.__name__ = "Integer32"
_WwpLeosRsvpteIfAdminStatus_Object = MibTableColumn
wwpLeosRsvpteIfAdminStatus = _WwpLeosRsvpteIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 5),
    _WwpLeosRsvpteIfAdminStatus_Type()
)
wwpLeosRsvpteIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfAdminStatus.setStatus("current")


class _WwpLeosRsvpteIfOperStatus_Type(Integer32):
    """Custom type wwpLeosRsvpteIfOperStatus based on Integer32"""
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


_WwpLeosRsvpteIfOperStatus_Type.__name__ = "Integer32"
_WwpLeosRsvpteIfOperStatus_Object = MibTableColumn
wwpLeosRsvpteIfOperStatus = _WwpLeosRsvpteIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 6),
    _WwpLeosRsvpteIfOperStatus_Type()
)
wwpLeosRsvpteIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfOperStatus.setStatus("current")


class _WwpLeosRsvpteIfHelloInterval_Type(Unsigned32):
    """Custom type wwpLeosRsvpteIfHelloInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WwpLeosRsvpteIfHelloInterval_Type.__name__ = "Unsigned32"
_WwpLeosRsvpteIfHelloInterval_Object = MibTableColumn
wwpLeosRsvpteIfHelloInterval = _WwpLeosRsvpteIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 7),
    _WwpLeosRsvpteIfHelloInterval_Type()
)
wwpLeosRsvpteIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfHelloInterval.setUnits("seconds")


class _WwpLeosRsvpteIfHelloTolerance_Type(Unsigned32):
    """Custom type wwpLeosRsvpteIfHelloTolerance based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WwpLeosRsvpteIfHelloTolerance_Type.__name__ = "Unsigned32"
_WwpLeosRsvpteIfHelloTolerance_Object = MibTableColumn
wwpLeosRsvpteIfHelloTolerance = _WwpLeosRsvpteIfHelloTolerance_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 8),
    _WwpLeosRsvpteIfHelloTolerance_Type()
)
wwpLeosRsvpteIfHelloTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfHelloTolerance.setStatus("current")


class _WwpLeosRsvpteIfAdvertisedLabel_Type(AdvertisedLabel):
    """Custom type wwpLeosRsvpteIfAdvertisedLabel based on AdvertisedLabel"""
    defaultValue = 99


_WwpLeosRsvpteIfAdvertisedLabel_Object = MibTableColumn
wwpLeosRsvpteIfAdvertisedLabel = _WwpLeosRsvpteIfAdvertisedLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 30, 1, 2, 1, 1, 9),
    _WwpLeosRsvpteIfAdvertisedLabel_Type()
)
wwpLeosRsvpteIfAdvertisedLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRsvpteIfAdvertisedLabel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-RSVPTE-MIB",
    **{"AdvertisedLabel": AdvertisedLabel,
       "wwpLeosRsvpteMIB": wwpLeosRsvpteMIB,
       "wwpLeosRsvpteMIBObjects": wwpLeosRsvpteMIBObjects,
       "wwpLeosRsvpteObjects": wwpLeosRsvpteObjects,
       "wwpLeosRsvpteAdminStatus": wwpLeosRsvpteAdminStatus,
       "wwpLeosRsvpteOperStatus": wwpLeosRsvpteOperStatus,
       "wwpLeosRsvpteRetryInterval": wwpLeosRsvpteRetryInterval,
       "wwpLeosRsvpteRetryInfiniteState": wwpLeosRsvpteRetryInfiniteState,
       "wwpLeosRsvpteRetryMax": wwpLeosRsvpteRetryMax,
       "wwpLeosRsvpteRefreshInterval": wwpLeosRsvpteRefreshInterval,
       "wwpLeosRsvpteRefreshMultiple": wwpLeosRsvpteRefreshMultiple,
       "wwpLeosRsvpteRfrshSlewDenom": wwpLeosRsvpteRfrshSlewDenom,
       "wwpLeosRsvpteRfrshSlewNumerator": wwpLeosRsvpteRfrshSlewNumerator,
       "wwpLeosRsvpteBlockadeMultiple": wwpLeosRsvpteBlockadeMultiple,
       "wwpLeosRsvpteLSPSetupPriority": wwpLeosRsvpteLSPSetupPriority,
       "wwpLeosRsvpteLSPHoldingPriority": wwpLeosRsvpteLSPHoldingPriority,
       "wwpLeosRsvpteUseHopByHop": wwpLeosRsvpteUseHopByHop,
       "wwpLeosRsvpteRestartCapable": wwpLeosRsvpteRestartCapable,
       "wwpLeosRsvpteRestartTime": wwpLeosRsvpteRestartTime,
       "wwpLeosRsvpteRecoveryTime": wwpLeosRsvpteRecoveryTime,
       "wwpLeosRsvpteMinPeerRestart": wwpLeosRsvpteMinPeerRestart,
       "wwpLeosRsvpte": wwpLeosRsvpte,
       "wwpLeosRsvpteIfTable": wwpLeosRsvpteIfTable,
       "wwpLeosRsvpteIfEntry": wwpLeosRsvpteIfEntry,
       "wwpLeosRsvpteIfName": wwpLeosRsvpteIfName,
       "wwpLeosRsvpteIfIndex": wwpLeosRsvpteIfIndex,
       "wwpLeosRsvpteIfIpAddr": wwpLeosRsvpteIfIpAddr,
       "wwpLeosRsvpteIfMtu": wwpLeosRsvpteIfMtu,
       "wwpLeosRsvpteIfAdminStatus": wwpLeosRsvpteIfAdminStatus,
       "wwpLeosRsvpteIfOperStatus": wwpLeosRsvpteIfOperStatus,
       "wwpLeosRsvpteIfHelloInterval": wwpLeosRsvpteIfHelloInterval,
       "wwpLeosRsvpteIfHelloTolerance": wwpLeosRsvpteIfHelloTolerance,
       "wwpLeosRsvpteIfAdvertisedLabel": wwpLeosRsvpteIfAdvertisedLabel}
)
