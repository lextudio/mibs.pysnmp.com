# SNMP MIB module (SONUS-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:11 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusPortIndex,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusPortIndex",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusCircuitMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusCircuitMIBs")

(SonusAdminAction,
 SonusAdminState,
 SonusName,
 SonusServiceState,
 SonusShelfIndex,
 SonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminAction",
    "SonusAdminState",
    "SonusName",
    "SonusServiceState",
    "SonusShelfIndex",
    "SonusSlotIndex")


# MODULE-IDENTITY

sonusSonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusSonetObjects_ObjectIdentity = ObjectIdentity
sonusSonetObjects = _SonusSonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1)
)
_SonusSonetPortAdmn_ObjectIdentity = ObjectIdentity
sonusSonetPortAdmn = _SonusSonetPortAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1)
)
_SonusSonetPortAdmnTable_Object = MibTable
sonusSonetPortAdmnTable = _SonusSonetPortAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sonusSonetPortAdmnTable.setStatus("current")
_SonusSonetPortAdmnEntry_Object = MibTableRow
sonusSonetPortAdmnEntry = _SonusSonetPortAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1)
)
sonusSonetPortAdmnEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetPortAdmnIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetPortAdmnEntry.setStatus("current")
_SonusSonetPortAdmnIfIndex_Type = Integer32
_SonusSonetPortAdmnIfIndex_Object = MibTableColumn
sonusSonetPortAdmnIfIndex = _SonusSonetPortAdmnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 1),
    _SonusSonetPortAdmnIfIndex_Type()
)
sonusSonetPortAdmnIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnIfIndex.setStatus("current")
_SonusSonetPortAdmnShelfIndex_Type = SonusShelfIndex
_SonusSonetPortAdmnShelfIndex_Object = MibTableColumn
sonusSonetPortAdmnShelfIndex = _SonusSonetPortAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 2),
    _SonusSonetPortAdmnShelfIndex_Type()
)
sonusSonetPortAdmnShelfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnShelfIndex.setStatus("current")
_SonusSonetPortAdmnSlotIndex_Type = SonusSlotIndex
_SonusSonetPortAdmnSlotIndex_Object = MibTableColumn
sonusSonetPortAdmnSlotIndex = _SonusSonetPortAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 3),
    _SonusSonetPortAdmnSlotIndex_Type()
)
sonusSonetPortAdmnSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnSlotIndex.setStatus("current")


class _SonusSonetPortAdmnPortIndex_Type(Integer32):
    """Custom type sonusSonetPortAdmnPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SonusSonetPortAdmnPortIndex_Type.__name__ = "Integer32"
_SonusSonetPortAdmnPortIndex_Object = MibTableColumn
sonusSonetPortAdmnPortIndex = _SonusSonetPortAdmnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 4),
    _SonusSonetPortAdmnPortIndex_Type()
)
sonusSonetPortAdmnPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnPortIndex.setStatus("current")
_SonusSonetPortAdmnRowStatus_Type = RowStatus
_SonusSonetPortAdmnRowStatus_Object = MibTableColumn
sonusSonetPortAdmnRowStatus = _SonusSonetPortAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 5),
    _SonusSonetPortAdmnRowStatus_Type()
)
sonusSonetPortAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnRowStatus.setStatus("current")
_SonusSonetPortAdmnName_Type = SonusName
_SonusSonetPortAdmnName_Object = MibTableColumn
sonusSonetPortAdmnName = _SonusSonetPortAdmnName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 6),
    _SonusSonetPortAdmnName_Type()
)
sonusSonetPortAdmnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnName.setStatus("current")


class _SonusSonetPortAdmnState_Type(SonusAdminState):
    """Custom type sonusSonetPortAdmnState based on SonusAdminState"""


_SonusSonetPortAdmnState_Object = MibTableColumn
sonusSonetPortAdmnState = _SonusSonetPortAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 7),
    _SonusSonetPortAdmnState_Type()
)
sonusSonetPortAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnState.setStatus("current")


class _SonusSonetPortAdmnMode_Type(SonusServiceState):
    """Custom type sonusSonetPortAdmnMode based on SonusServiceState"""


_SonusSonetPortAdmnMode_Object = MibTableColumn
sonusSonetPortAdmnMode = _SonusSonetPortAdmnMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 8),
    _SonusSonetPortAdmnMode_Type()
)
sonusSonetPortAdmnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnMode.setStatus("current")


class _SonusSonetPortAdmnAction_Type(SonusAdminAction):
    """Custom type sonusSonetPortAdmnAction based on SonusAdminAction"""


_SonusSonetPortAdmnAction_Object = MibTableColumn
sonusSonetPortAdmnAction = _SonusSonetPortAdmnAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 9),
    _SonusSonetPortAdmnAction_Type()
)
sonusSonetPortAdmnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnAction.setStatus("current")


class _SonusSonetPortAdmnTimeout_Type(Integer32):
    """Custom type sonusSonetPortAdmnTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SonusSonetPortAdmnTimeout_Type.__name__ = "Integer32"
_SonusSonetPortAdmnTimeout_Object = MibTableColumn
sonusSonetPortAdmnTimeout = _SonusSonetPortAdmnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 10),
    _SonusSonetPortAdmnTimeout_Type()
)
sonusSonetPortAdmnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnTimeout.setStatus("current")


class _SonusSonetPortAdmnStatAction_Type(Integer32):
    """Custom type sonusSonetPortAdmnStatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("init15MinuteFarEnd", 2),
          ("init15MinuteNearEnd", 1),
          ("init24HourFarEnd", 8),
          ("init24HourNearEnd", 4))
    )


_SonusSonetPortAdmnStatAction_Type.__name__ = "Integer32"
_SonusSonetPortAdmnStatAction_Object = MibTableColumn
sonusSonetPortAdmnStatAction = _SonusSonetPortAdmnStatAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 11),
    _SonusSonetPortAdmnStatAction_Type()
)
sonusSonetPortAdmnStatAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnStatAction.setStatus("current")


class _SonusSonetPortAdmnLaserState_Type(Integer32):
    """Custom type sonusSonetPortAdmnLaserState based on Integer32"""
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


_SonusSonetPortAdmnLaserState_Type.__name__ = "Integer32"
_SonusSonetPortAdmnLaserState_Object = MibTableColumn
sonusSonetPortAdmnLaserState = _SonusSonetPortAdmnLaserState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 12),
    _SonusSonetPortAdmnLaserState_Type()
)
sonusSonetPortAdmnLaserState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnLaserState.setStatus("current")


class _SonusSonetPortAdmn24hTimeElapsed_Type(Integer32):
    """Custom type sonusSonetPortAdmn24hTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SonusSonetPortAdmn24hTimeElapsed_Type.__name__ = "Integer32"
_SonusSonetPortAdmn24hTimeElapsed_Object = MibTableColumn
sonusSonetPortAdmn24hTimeElapsed = _SonusSonetPortAdmn24hTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 13),
    _SonusSonetPortAdmn24hTimeElapsed_Type()
)
sonusSonetPortAdmn24hTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPortAdmn24hTimeElapsed.setStatus("current")


class _SonusSonetPortAdmnOperStatus_Type(Integer32):
    """Custom type sonusSonetPortAdmnOperStatus based on Integer32"""
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
        *(("disabled", 5),
          ("down", 7),
          ("dryingUp", 4),
          ("enabledDown", 3),
          ("enabledInService", 1),
          ("enabledOutOfService", 2),
          ("up", 6))
    )


_SonusSonetPortAdmnOperStatus_Type.__name__ = "Integer32"
_SonusSonetPortAdmnOperStatus_Object = MibTableColumn
sonusSonetPortAdmnOperStatus = _SonusSonetPortAdmnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 14),
    _SonusSonetPortAdmnOperStatus_Type()
)
sonusSonetPortAdmnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnOperStatus.setStatus("current")


class _SonusSonetPortAdmnDs3ModeOverride_Type(SonusAdminState):
    """Custom type sonusSonetPortAdmnDs3ModeOverride based on SonusAdminState"""


_SonusSonetPortAdmnDs3ModeOverride_Object = MibTableColumn
sonusSonetPortAdmnDs3ModeOverride = _SonusSonetPortAdmnDs3ModeOverride_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 15),
    _SonusSonetPortAdmnDs3ModeOverride_Type()
)
sonusSonetPortAdmnDs3ModeOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnDs3ModeOverride.setStatus("current")


class _SonusSonetPortAdmnStsXmtScramble_Type(SonusAdminState):
    """Custom type sonusSonetPortAdmnStsXmtScramble based on SonusAdminState"""


_SonusSonetPortAdmnStsXmtScramble_Object = MibTableColumn
sonusSonetPortAdmnStsXmtScramble = _SonusSonetPortAdmnStsXmtScramble_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 16),
    _SonusSonetPortAdmnStsXmtScramble_Type()
)
sonusSonetPortAdmnStsXmtScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnStsXmtScramble.setStatus("current")


class _SonusSonetPortAdmnStsRcvDescramble_Type(SonusAdminState):
    """Custom type sonusSonetPortAdmnStsRcvDescramble based on SonusAdminState"""


_SonusSonetPortAdmnStsRcvDescramble_Object = MibTableColumn
sonusSonetPortAdmnStsRcvDescramble = _SonusSonetPortAdmnStsRcvDescramble_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 17),
    _SonusSonetPortAdmnStsRcvDescramble_Type()
)
sonusSonetPortAdmnStsRcvDescramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnStsRcvDescramble.setStatus("current")


class _SonusSonetPortAdmnAtmXmtScramble_Type(SonusAdminState):
    """Custom type sonusSonetPortAdmnAtmXmtScramble based on SonusAdminState"""


_SonusSonetPortAdmnAtmXmtScramble_Object = MibTableColumn
sonusSonetPortAdmnAtmXmtScramble = _SonusSonetPortAdmnAtmXmtScramble_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 18),
    _SonusSonetPortAdmnAtmXmtScramble_Type()
)
sonusSonetPortAdmnAtmXmtScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnAtmXmtScramble.setStatus("current")


class _SonusSonetPortAdmnAtmRcvDescramble_Type(SonusAdminState):
    """Custom type sonusSonetPortAdmnAtmRcvDescramble based on SonusAdminState"""


_SonusSonetPortAdmnAtmRcvDescramble_Object = MibTableColumn
sonusSonetPortAdmnAtmRcvDescramble = _SonusSonetPortAdmnAtmRcvDescramble_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 1, 1, 1, 19),
    _SonusSonetPortAdmnAtmRcvDescramble_Type()
)
sonusSonetPortAdmnAtmRcvDescramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPortAdmnAtmRcvDescramble.setStatus("current")
_SonusSonetSection_ObjectIdentity = ObjectIdentity
sonusSonetSection = _SonusSonetSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2)
)
_SonusSonetSectionThresholdTable_Object = MibTable
sonusSonetSectionThresholdTable = _SonusSonetSectionThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sonusSonetSectionThresholdTable.setStatus("current")
_SonusSonetSectionThresholdEntry_Object = MibTableRow
sonusSonetSectionThresholdEntry = _SonusSonetSectionThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1)
)
sonusSonetSectionThresholdEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetSectionThresholdIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetSectionThresholdEntry.setStatus("current")
_SonusSonetSectionThresholdIfIndex_Type = Integer32
_SonusSonetSectionThresholdIfIndex_Object = MibTableColumn
sonusSonetSectionThresholdIfIndex = _SonusSonetSectionThresholdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 1),
    _SonusSonetSectionThresholdIfIndex_Type()
)
sonusSonetSectionThresholdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetSectionThresholdIfIndex.setStatus("current")


class _SonusSonetSectionThreshold15mCVs_Type(Integer32):
    """Custom type sonusSonetSectionThreshold15mCVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusSonetSectionThreshold15mCVs_Type.__name__ = "Integer32"
_SonusSonetSectionThreshold15mCVs_Object = MibTableColumn
sonusSonetSectionThreshold15mCVs = _SonusSonetSectionThreshold15mCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 2),
    _SonusSonetSectionThreshold15mCVs_Type()
)
sonusSonetSectionThreshold15mCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetSectionThreshold15mCVs.setStatus("current")


class _SonusSonetSectionThreshold15mESs_Type(Integer32):
    """Custom type sonusSonetSectionThreshold15mESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusSonetSectionThreshold15mESs_Type.__name__ = "Integer32"
_SonusSonetSectionThreshold15mESs_Object = MibTableColumn
sonusSonetSectionThreshold15mESs = _SonusSonetSectionThreshold15mESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 3),
    _SonusSonetSectionThreshold15mESs_Type()
)
sonusSonetSectionThreshold15mESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetSectionThreshold15mESs.setStatus("current")


class _SonusSonetSectionThreshold15mSESs_Type(Integer32):
    """Custom type sonusSonetSectionThreshold15mSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonusSonetSectionThreshold15mSESs_Type.__name__ = "Integer32"
_SonusSonetSectionThreshold15mSESs_Object = MibTableColumn
sonusSonetSectionThreshold15mSESs = _SonusSonetSectionThreshold15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 4),
    _SonusSonetSectionThreshold15mSESs_Type()
)
sonusSonetSectionThreshold15mSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetSectionThreshold15mSESs.setStatus("current")


class _SonusSonetSectionThreshold15mSEFSs_Type(Integer32):
    """Custom type sonusSonetSectionThreshold15mSEFSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonusSonetSectionThreshold15mSEFSs_Type.__name__ = "Integer32"
_SonusSonetSectionThreshold15mSEFSs_Object = MibTableColumn
sonusSonetSectionThreshold15mSEFSs = _SonusSonetSectionThreshold15mSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 5),
    _SonusSonetSectionThreshold15mSEFSs_Type()
)
sonusSonetSectionThreshold15mSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetSectionThreshold15mSEFSs.setStatus("current")


class _SonusSonetSectionThreshold24hCVs_Type(Integer32):
    """Custom type sonusSonetSectionThreshold24hCVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_SonusSonetSectionThreshold24hCVs_Type.__name__ = "Integer32"
_SonusSonetSectionThreshold24hCVs_Object = MibTableColumn
sonusSonetSectionThreshold24hCVs = _SonusSonetSectionThreshold24hCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 6),
    _SonusSonetSectionThreshold24hCVs_Type()
)
sonusSonetSectionThreshold24hCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetSectionThreshold24hCVs.setStatus("current")


class _SonusSonetSectionThreshold24hESs_Type(Integer32):
    """Custom type sonusSonetSectionThreshold24hESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetSectionThreshold24hESs_Type.__name__ = "Integer32"
_SonusSonetSectionThreshold24hESs_Object = MibTableColumn
sonusSonetSectionThreshold24hESs = _SonusSonetSectionThreshold24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 7),
    _SonusSonetSectionThreshold24hESs_Type()
)
sonusSonetSectionThreshold24hESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetSectionThreshold24hESs.setStatus("current")


class _SonusSonetSectionThreshold24hSESs_Type(Integer32):
    """Custom type sonusSonetSectionThreshold24hSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetSectionThreshold24hSESs_Type.__name__ = "Integer32"
_SonusSonetSectionThreshold24hSESs_Object = MibTableColumn
sonusSonetSectionThreshold24hSESs = _SonusSonetSectionThreshold24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 8),
    _SonusSonetSectionThreshold24hSESs_Type()
)
sonusSonetSectionThreshold24hSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetSectionThreshold24hSESs.setStatus("current")


class _SonusSonetSectionThreshold24hSEFSs_Type(Integer32):
    """Custom type sonusSonetSectionThreshold24hSEFSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetSectionThreshold24hSEFSs_Type.__name__ = "Integer32"
_SonusSonetSectionThreshold24hSEFSs_Object = MibTableColumn
sonusSonetSectionThreshold24hSEFSs = _SonusSonetSectionThreshold24hSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 1, 1, 9),
    _SonusSonetSectionThreshold24hSEFSs_Type()
)
sonusSonetSectionThreshold24hSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetSectionThreshold24hSEFSs.setStatus("current")
_SonusSonetSectionCurrentTable_Object = MibTable
sonusSonetSectionCurrentTable = _SonusSonetSectionCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusSonetSectionCurrentTable.setStatus("current")
_SonusSonetSectionCurrentEntry_Object = MibTableRow
sonusSonetSectionCurrentEntry = _SonusSonetSectionCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 2, 1)
)
sonusSonetSectionCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetSectionCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetSectionCurrentEntry.setStatus("current")
_SonusSonetSectionCurrentIfIndex_Type = Integer32
_SonusSonetSectionCurrentIfIndex_Object = MibTableColumn
sonusSonetSectionCurrentIfIndex = _SonusSonetSectionCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 2, 1, 1),
    _SonusSonetSectionCurrentIfIndex_Type()
)
sonusSonetSectionCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetSectionCurrentIfIndex.setStatus("current")


class _SonusSonetSectionCurrentStatus_Type(Integer32):
    """Custom type sonusSonetSectionCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusSonetSectionCurrentStatus_Type.__name__ = "Integer32"
_SonusSonetSectionCurrentStatus_Object = MibTableColumn
sonusSonetSectionCurrentStatus = _SonusSonetSectionCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 2, 1, 2),
    _SonusSonetSectionCurrentStatus_Type()
)
sonusSonetSectionCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionCurrentStatus.setStatus("current")
_SonusSonetSectionCurrentESs_Type = PerfCurrentCount
_SonusSonetSectionCurrentESs_Object = MibTableColumn
sonusSonetSectionCurrentESs = _SonusSonetSectionCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 2, 1, 3),
    _SonusSonetSectionCurrentESs_Type()
)
sonusSonetSectionCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionCurrentESs.setStatus("current")
_SonusSonetSectionCurrentSESs_Type = PerfCurrentCount
_SonusSonetSectionCurrentSESs_Object = MibTableColumn
sonusSonetSectionCurrentSESs = _SonusSonetSectionCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 2, 1, 4),
    _SonusSonetSectionCurrentSESs_Type()
)
sonusSonetSectionCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionCurrentSESs.setStatus("current")
_SonusSonetSectionCurrentSEFSs_Type = PerfCurrentCount
_SonusSonetSectionCurrentSEFSs_Object = MibTableColumn
sonusSonetSectionCurrentSEFSs = _SonusSonetSectionCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 2, 1, 5),
    _SonusSonetSectionCurrentSEFSs_Type()
)
sonusSonetSectionCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionCurrentSEFSs.setStatus("current")
_SonusSonetSectionCurrentCVs_Type = PerfCurrentCount
_SonusSonetSectionCurrentCVs_Object = MibTableColumn
sonusSonetSectionCurrentCVs = _SonusSonetSectionCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 2, 1, 6),
    _SonusSonetSectionCurrentCVs_Type()
)
sonusSonetSectionCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionCurrentCVs.setStatus("current")
_SonusSonetSectionIntervalTable_Object = MibTable
sonusSonetSectionIntervalTable = _SonusSonetSectionIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalTable.setStatus("current")
_SonusSonetSectionIntervalEntry_Object = MibTableRow
sonusSonetSectionIntervalEntry = _SonusSonetSectionIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3, 1)
)
sonusSonetSectionIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetSectionIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetSectionIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalEntry.setStatus("current")
_SonusSonetSectionIntervalIfIndex_Type = Integer32
_SonusSonetSectionIntervalIfIndex_Object = MibTableColumn
sonusSonetSectionIntervalIfIndex = _SonusSonetSectionIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3, 1, 1),
    _SonusSonetSectionIntervalIfIndex_Type()
)
sonusSonetSectionIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalIfIndex.setStatus("current")


class _SonusSonetSectionIntervalNumber_Type(Integer32):
    """Custom type sonusSonetSectionIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonusSonetSectionIntervalNumber_Type.__name__ = "Integer32"
_SonusSonetSectionIntervalNumber_Object = MibTableColumn
sonusSonetSectionIntervalNumber = _SonusSonetSectionIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3, 1, 2),
    _SonusSonetSectionIntervalNumber_Type()
)
sonusSonetSectionIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalNumber.setStatus("current")
_SonusSonetSectionIntervalESs_Type = PerfCurrentCount
_SonusSonetSectionIntervalESs_Object = MibTableColumn
sonusSonetSectionIntervalESs = _SonusSonetSectionIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3, 1, 3),
    _SonusSonetSectionIntervalESs_Type()
)
sonusSonetSectionIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalESs.setStatus("current")
_SonusSonetSectionIntervalSESs_Type = PerfCurrentCount
_SonusSonetSectionIntervalSESs_Object = MibTableColumn
sonusSonetSectionIntervalSESs = _SonusSonetSectionIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3, 1, 4),
    _SonusSonetSectionIntervalSESs_Type()
)
sonusSonetSectionIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalSESs.setStatus("current")
_SonusSonetSectionIntervalSEFSs_Type = PerfCurrentCount
_SonusSonetSectionIntervalSEFSs_Object = MibTableColumn
sonusSonetSectionIntervalSEFSs = _SonusSonetSectionIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3, 1, 5),
    _SonusSonetSectionIntervalSEFSs_Type()
)
sonusSonetSectionIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalSEFSs.setStatus("current")
_SonusSonetSectionIntervalCVs_Type = PerfCurrentCount
_SonusSonetSectionIntervalCVs_Object = MibTableColumn
sonusSonetSectionIntervalCVs = _SonusSonetSectionIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3, 1, 6),
    _SonusSonetSectionIntervalCVs_Type()
)
sonusSonetSectionIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalCVs.setStatus("current")
_SonusSonetSectionIntervalValidData_Type = TruthValue
_SonusSonetSectionIntervalValidData_Object = MibTableColumn
sonusSonetSectionIntervalValidData = _SonusSonetSectionIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 2, 3, 1, 7),
    _SonusSonetSectionIntervalValidData_Type()
)
sonusSonetSectionIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetSectionIntervalValidData.setStatus("current")
_SonusSonetLine_ObjectIdentity = ObjectIdentity
sonusSonetLine = _SonusSonetLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3)
)
_SonusSonetLineThresholdTable_Object = MibTable
sonusSonetLineThresholdTable = _SonusSonetLineThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sonusSonetLineThresholdTable.setStatus("current")
_SonusSonetLineThresholdEntry_Object = MibTableRow
sonusSonetLineThresholdEntry = _SonusSonetLineThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1)
)
sonusSonetLineThresholdEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetLineThresholdIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetLineThresholdEntry.setStatus("current")
_SonusSonetLineThresholdIfIndex_Type = Integer32
_SonusSonetLineThresholdIfIndex_Object = MibTableColumn
sonusSonetLineThresholdIfIndex = _SonusSonetLineThresholdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 1),
    _SonusSonetLineThresholdIfIndex_Type()
)
sonusSonetLineThresholdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLineThresholdIfIndex.setStatus("current")


class _SonusSonetLineThreshold15mCVs_Type(Integer32):
    """Custom type sonusSonetLineThreshold15mCVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusSonetLineThreshold15mCVs_Type.__name__ = "Integer32"
_SonusSonetLineThreshold15mCVs_Object = MibTableColumn
sonusSonetLineThreshold15mCVs = _SonusSonetLineThreshold15mCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 2),
    _SonusSonetLineThreshold15mCVs_Type()
)
sonusSonetLineThreshold15mCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetLineThreshold15mCVs.setStatus("current")


class _SonusSonetLineThreshold15mESs_Type(Integer32):
    """Custom type sonusSonetLineThreshold15mESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonusSonetLineThreshold15mESs_Type.__name__ = "Integer32"
_SonusSonetLineThreshold15mESs_Object = MibTableColumn
sonusSonetLineThreshold15mESs = _SonusSonetLineThreshold15mESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 3),
    _SonusSonetLineThreshold15mESs_Type()
)
sonusSonetLineThreshold15mESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetLineThreshold15mESs.setStatus("current")


class _SonusSonetLineThreshold15mSESs_Type(Integer32):
    """Custom type sonusSonetLineThreshold15mSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonusSonetLineThreshold15mSESs_Type.__name__ = "Integer32"
_SonusSonetLineThreshold15mSESs_Object = MibTableColumn
sonusSonetLineThreshold15mSESs = _SonusSonetLineThreshold15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 4),
    _SonusSonetLineThreshold15mSESs_Type()
)
sonusSonetLineThreshold15mSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetLineThreshold15mSESs.setStatus("current")


class _SonusSonetLineThreshold15mUASs_Type(Integer32):
    """Custom type sonusSonetLineThreshold15mUASs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonusSonetLineThreshold15mUASs_Type.__name__ = "Integer32"
_SonusSonetLineThreshold15mUASs_Object = MibTableColumn
sonusSonetLineThreshold15mUASs = _SonusSonetLineThreshold15mUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 5),
    _SonusSonetLineThreshold15mUASs_Type()
)
sonusSonetLineThreshold15mUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetLineThreshold15mUASs.setStatus("current")


class _SonusSonetLineThreshold24hCVs_Type(Integer32):
    """Custom type sonusSonetLineThreshold24hCVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_SonusSonetLineThreshold24hCVs_Type.__name__ = "Integer32"
_SonusSonetLineThreshold24hCVs_Object = MibTableColumn
sonusSonetLineThreshold24hCVs = _SonusSonetLineThreshold24hCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 6),
    _SonusSonetLineThreshold24hCVs_Type()
)
sonusSonetLineThreshold24hCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetLineThreshold24hCVs.setStatus("current")


class _SonusSonetLineThreshold24hESs_Type(Integer32):
    """Custom type sonusSonetLineThreshold24hESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetLineThreshold24hESs_Type.__name__ = "Integer32"
_SonusSonetLineThreshold24hESs_Object = MibTableColumn
sonusSonetLineThreshold24hESs = _SonusSonetLineThreshold24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 7),
    _SonusSonetLineThreshold24hESs_Type()
)
sonusSonetLineThreshold24hESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetLineThreshold24hESs.setStatus("current")


class _SonusSonetLineThreshold24hSESs_Type(Integer32):
    """Custom type sonusSonetLineThreshold24hSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetLineThreshold24hSESs_Type.__name__ = "Integer32"
_SonusSonetLineThreshold24hSESs_Object = MibTableColumn
sonusSonetLineThreshold24hSESs = _SonusSonetLineThreshold24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 8),
    _SonusSonetLineThreshold24hSESs_Type()
)
sonusSonetLineThreshold24hSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetLineThreshold24hSESs.setStatus("current")


class _SonusSonetLineThreshold24hUASs_Type(Integer32):
    """Custom type sonusSonetLineThreshold24hUASs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetLineThreshold24hUASs_Type.__name__ = "Integer32"
_SonusSonetLineThreshold24hUASs_Object = MibTableColumn
sonusSonetLineThreshold24hUASs = _SonusSonetLineThreshold24hUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 1, 1, 9),
    _SonusSonetLineThreshold24hUASs_Type()
)
sonusSonetLineThreshold24hUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetLineThreshold24hUASs.setStatus("current")
_SonusSonetLineCurrentTable_Object = MibTable
sonusSonetLineCurrentTable = _SonusSonetLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonusSonetLineCurrentTable.setStatus("current")
_SonusSonetLineCurrentEntry_Object = MibTableRow
sonusSonetLineCurrentEntry = _SonusSonetLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2, 1)
)
sonusSonetLineCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetLineCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetLineCurrentEntry.setStatus("current")
_SonusSonetLineCurrentIfIndex_Type = Integer32
_SonusSonetLineCurrentIfIndex_Object = MibTableColumn
sonusSonetLineCurrentIfIndex = _SonusSonetLineCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2, 1, 1),
    _SonusSonetLineCurrentIfIndex_Type()
)
sonusSonetLineCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLineCurrentIfIndex.setStatus("current")


class _SonusSonetLineCurrentStatus_Type(Integer32):
    """Custom type sonusSonetLineCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusSonetLineCurrentStatus_Type.__name__ = "Integer32"
_SonusSonetLineCurrentStatus_Object = MibTableColumn
sonusSonetLineCurrentStatus = _SonusSonetLineCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2, 1, 2),
    _SonusSonetLineCurrentStatus_Type()
)
sonusSonetLineCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineCurrentStatus.setStatus("current")
_SonusSonetLineCurrentESs_Type = PerfCurrentCount
_SonusSonetLineCurrentESs_Object = MibTableColumn
sonusSonetLineCurrentESs = _SonusSonetLineCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2, 1, 3),
    _SonusSonetLineCurrentESs_Type()
)
sonusSonetLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineCurrentESs.setStatus("current")
_SonusSonetLineCurrentSESs_Type = PerfCurrentCount
_SonusSonetLineCurrentSESs_Object = MibTableColumn
sonusSonetLineCurrentSESs = _SonusSonetLineCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2, 1, 4),
    _SonusSonetLineCurrentSESs_Type()
)
sonusSonetLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineCurrentSESs.setStatus("current")
_SonusSonetLineCurrentUASs_Type = PerfCurrentCount
_SonusSonetLineCurrentUASs_Object = MibTableColumn
sonusSonetLineCurrentUASs = _SonusSonetLineCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2, 1, 5),
    _SonusSonetLineCurrentUASs_Type()
)
sonusSonetLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineCurrentUASs.setStatus("current")
_SonusSonetLineCurrentCVs_Type = PerfCurrentCount
_SonusSonetLineCurrentCVs_Object = MibTableColumn
sonusSonetLineCurrentCVs = _SonusSonetLineCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2, 1, 6),
    _SonusSonetLineCurrentCVs_Type()
)
sonusSonetLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineCurrentCVs.setStatus("current")
_SonusSonetLineCurrentFCs_Type = PerfCurrentCount
_SonusSonetLineCurrentFCs_Object = MibTableColumn
sonusSonetLineCurrentFCs = _SonusSonetLineCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 2, 1, 7),
    _SonusSonetLineCurrentFCs_Type()
)
sonusSonetLineCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineCurrentFCs.setStatus("current")
_SonusSonetLineIntervalTable_Object = MibTable
sonusSonetLineIntervalTable = _SonusSonetLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    sonusSonetLineIntervalTable.setStatus("current")
_SonusSonetLineIntervalEntry_Object = MibTableRow
sonusSonetLineIntervalEntry = _SonusSonetLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1)
)
sonusSonetLineIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetLineIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetLineIntervalEntry.setStatus("current")
_SonusSonetLineIntervalIfIndex_Type = Integer32
_SonusSonetLineIntervalIfIndex_Object = MibTableColumn
sonusSonetLineIntervalIfIndex = _SonusSonetLineIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1, 1),
    _SonusSonetLineIntervalIfIndex_Type()
)
sonusSonetLineIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLineIntervalIfIndex.setStatus("current")


class _SonusSonetLineIntervalNumber_Type(Integer32):
    """Custom type sonusSonetLineIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonusSonetLineIntervalNumber_Type.__name__ = "Integer32"
_SonusSonetLineIntervalNumber_Object = MibTableColumn
sonusSonetLineIntervalNumber = _SonusSonetLineIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1, 2),
    _SonusSonetLineIntervalNumber_Type()
)
sonusSonetLineIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLineIntervalNumber.setStatus("current")
_SonusSonetLineIntervalESs_Type = PerfIntervalCount
_SonusSonetLineIntervalESs_Object = MibTableColumn
sonusSonetLineIntervalESs = _SonusSonetLineIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1, 3),
    _SonusSonetLineIntervalESs_Type()
)
sonusSonetLineIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineIntervalESs.setStatus("current")
_SonusSonetLineIntervalSESs_Type = PerfIntervalCount
_SonusSonetLineIntervalSESs_Object = MibTableColumn
sonusSonetLineIntervalSESs = _SonusSonetLineIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1, 4),
    _SonusSonetLineIntervalSESs_Type()
)
sonusSonetLineIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineIntervalSESs.setStatus("current")
_SonusSonetLineIntervalUASs_Type = PerfIntervalCount
_SonusSonetLineIntervalUASs_Object = MibTableColumn
sonusSonetLineIntervalUASs = _SonusSonetLineIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1, 5),
    _SonusSonetLineIntervalUASs_Type()
)
sonusSonetLineIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineIntervalUASs.setStatus("current")
_SonusSonetLineIntervalCVs_Type = PerfIntervalCount
_SonusSonetLineIntervalCVs_Object = MibTableColumn
sonusSonetLineIntervalCVs = _SonusSonetLineIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1, 6),
    _SonusSonetLineIntervalCVs_Type()
)
sonusSonetLineIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineIntervalCVs.setStatus("current")
_SonusSonetLineIntervalFCs_Type = PerfIntervalCount
_SonusSonetLineIntervalFCs_Object = MibTableColumn
sonusSonetLineIntervalFCs = _SonusSonetLineIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1, 7),
    _SonusSonetLineIntervalFCs_Type()
)
sonusSonetLineIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineIntervalFCs.setStatus("current")
_SonusSonetLineIntervalValidData_Type = TruthValue
_SonusSonetLineIntervalValidData_Object = MibTableColumn
sonusSonetLineIntervalValidData = _SonusSonetLineIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 3, 1, 8),
    _SonusSonetLineIntervalValidData_Type()
)
sonusSonetLineIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineIntervalValidData.setStatus("current")
_SonusSonetFarEndLineCurrentTable_Object = MibTable
sonusSonetFarEndLineCurrentTable = _SonusSonetFarEndLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    sonusSonetFarEndLineCurrentTable.setStatus("current")
_SonusSonetFarEndLineCurrentEntry_Object = MibTableRow
sonusSonetFarEndLineCurrentEntry = _SonusSonetFarEndLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 4, 1)
)
sonusSonetFarEndLineCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndLineCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetFarEndLineCurrentEntry.setStatus("current")
_SonusSonetFarEndLineCurrentIfIndex_Type = Integer32
_SonusSonetFarEndLineCurrentIfIndex_Object = MibTableColumn
sonusSonetFarEndLineCurrentIfIndex = _SonusSonetFarEndLineCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 4, 1, 1),
    _SonusSonetFarEndLineCurrentIfIndex_Type()
)
sonusSonetFarEndLineCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineCurrentIfIndex.setStatus("current")
_SonusSonetFarEndLineCurrentESs_Type = PerfCurrentCount
_SonusSonetFarEndLineCurrentESs_Object = MibTableColumn
sonusSonetFarEndLineCurrentESs = _SonusSonetFarEndLineCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 4, 1, 2),
    _SonusSonetFarEndLineCurrentESs_Type()
)
sonusSonetFarEndLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineCurrentESs.setStatus("current")
_SonusSonetFarEndLineCurrentSESs_Type = PerfCurrentCount
_SonusSonetFarEndLineCurrentSESs_Object = MibTableColumn
sonusSonetFarEndLineCurrentSESs = _SonusSonetFarEndLineCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 4, 1, 3),
    _SonusSonetFarEndLineCurrentSESs_Type()
)
sonusSonetFarEndLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineCurrentSESs.setStatus("current")
_SonusSonetFarEndLineCurrentUASs_Type = PerfCurrentCount
_SonusSonetFarEndLineCurrentUASs_Object = MibTableColumn
sonusSonetFarEndLineCurrentUASs = _SonusSonetFarEndLineCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 4, 1, 4),
    _SonusSonetFarEndLineCurrentUASs_Type()
)
sonusSonetFarEndLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineCurrentUASs.setStatus("current")
_SonusSonetFarEndLineCurrentCVs_Type = PerfCurrentCount
_SonusSonetFarEndLineCurrentCVs_Object = MibTableColumn
sonusSonetFarEndLineCurrentCVs = _SonusSonetFarEndLineCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 4, 1, 5),
    _SonusSonetFarEndLineCurrentCVs_Type()
)
sonusSonetFarEndLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineCurrentCVs.setStatus("current")
_SonusSonetFarEndLineCurrentFCs_Type = PerfCurrentCount
_SonusSonetFarEndLineCurrentFCs_Object = MibTableColumn
sonusSonetFarEndLineCurrentFCs = _SonusSonetFarEndLineCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 4, 1, 6),
    _SonusSonetFarEndLineCurrentFCs_Type()
)
sonusSonetFarEndLineCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineCurrentFCs.setStatus("current")
_SonusSonetFarEndLineIntervalTable_Object = MibTable
sonusSonetFarEndLineIntervalTable = _SonusSonetFarEndLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalTable.setStatus("current")
_SonusSonetFarEndLineIntervalEntry_Object = MibTableRow
sonusSonetFarEndLineIntervalEntry = _SonusSonetFarEndLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1)
)
sonusSonetFarEndLineIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndLineIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalEntry.setStatus("current")
_SonusSonetFarEndLineIntervalIfIndex_Type = Integer32
_SonusSonetFarEndLineIntervalIfIndex_Object = MibTableColumn
sonusSonetFarEndLineIntervalIfIndex = _SonusSonetFarEndLineIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1, 1),
    _SonusSonetFarEndLineIntervalIfIndex_Type()
)
sonusSonetFarEndLineIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalIfIndex.setStatus("current")


class _SonusSonetFarEndLineIntervalNumber_Type(Integer32):
    """Custom type sonusSonetFarEndLineIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonusSonetFarEndLineIntervalNumber_Type.__name__ = "Integer32"
_SonusSonetFarEndLineIntervalNumber_Object = MibTableColumn
sonusSonetFarEndLineIntervalNumber = _SonusSonetFarEndLineIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1, 2),
    _SonusSonetFarEndLineIntervalNumber_Type()
)
sonusSonetFarEndLineIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalNumber.setStatus("current")
_SonusSonetFarEndLineIntervalESs_Type = PerfIntervalCount
_SonusSonetFarEndLineIntervalESs_Object = MibTableColumn
sonusSonetFarEndLineIntervalESs = _SonusSonetFarEndLineIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1, 3),
    _SonusSonetFarEndLineIntervalESs_Type()
)
sonusSonetFarEndLineIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalESs.setStatus("current")
_SonusSonetFarEndLineIntervalSESs_Type = PerfIntervalCount
_SonusSonetFarEndLineIntervalSESs_Object = MibTableColumn
sonusSonetFarEndLineIntervalSESs = _SonusSonetFarEndLineIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1, 4),
    _SonusSonetFarEndLineIntervalSESs_Type()
)
sonusSonetFarEndLineIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalSESs.setStatus("current")
_SonusSonetFarEndLineIntervalUASs_Type = PerfIntervalCount
_SonusSonetFarEndLineIntervalUASs_Object = MibTableColumn
sonusSonetFarEndLineIntervalUASs = _SonusSonetFarEndLineIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1, 5),
    _SonusSonetFarEndLineIntervalUASs_Type()
)
sonusSonetFarEndLineIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalUASs.setStatus("current")
_SonusSonetFarEndLineIntervalCVs_Type = PerfIntervalCount
_SonusSonetFarEndLineIntervalCVs_Object = MibTableColumn
sonusSonetFarEndLineIntervalCVs = _SonusSonetFarEndLineIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1, 6),
    _SonusSonetFarEndLineIntervalCVs_Type()
)
sonusSonetFarEndLineIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalCVs.setStatus("current")
_SonusSonetFarEndLineIntervalFCs_Type = PerfIntervalCount
_SonusSonetFarEndLineIntervalFCs_Object = MibTableColumn
sonusSonetFarEndLineIntervalFCs = _SonusSonetFarEndLineIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1, 7),
    _SonusSonetFarEndLineIntervalFCs_Type()
)
sonusSonetFarEndLineIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalFCs.setStatus("current")
_SonusSonetFarEndLineIntervalValidData_Type = TruthValue
_SonusSonetFarEndLineIntervalValidData_Object = MibTableColumn
sonusSonetFarEndLineIntervalValidData = _SonusSonetFarEndLineIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 5, 1, 8),
    _SonusSonetFarEndLineIntervalValidData_Type()
)
sonusSonetFarEndLineIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineIntervalValidData.setStatus("current")
_SonusSonetLineFailureCurrentTable_Object = MibTable
sonusSonetLineFailureCurrentTable = _SonusSonetLineFailureCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 6)
)
if mibBuilder.loadTexts:
    sonusSonetLineFailureCurrentTable.setStatus("current")
_SonusSonetLineFailureCurrentEntry_Object = MibTableRow
sonusSonetLineFailureCurrentEntry = _SonusSonetLineFailureCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 6, 1)
)
sonusSonetLineFailureCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetLineFailureCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetLineFailureCurrentEntry.setStatus("current")
_SonusSonetLineFailureCurrentIfIndex_Type = Integer32
_SonusSonetLineFailureCurrentIfIndex_Object = MibTableColumn
sonusSonetLineFailureCurrentIfIndex = _SonusSonetLineFailureCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 6, 1, 1),
    _SonusSonetLineFailureCurrentIfIndex_Type()
)
sonusSonetLineFailureCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLineFailureCurrentIfIndex.setStatus("current")
_SonusSonetLineFailureCurrentFCs_Type = PerfCurrentCount
_SonusSonetLineFailureCurrentFCs_Object = MibTableColumn
sonusSonetLineFailureCurrentFCs = _SonusSonetLineFailureCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 6, 1, 2),
    _SonusSonetLineFailureCurrentFCs_Type()
)
sonusSonetLineFailureCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineFailureCurrentFCs.setStatus("current")
_SonusSonetLineFailureIntervalTable_Object = MibTable
sonusSonetLineFailureIntervalTable = _SonusSonetLineFailureIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 7)
)
if mibBuilder.loadTexts:
    sonusSonetLineFailureIntervalTable.setStatus("current")
_SonusSonetLineFailureIntervalEntry_Object = MibTableRow
sonusSonetLineFailureIntervalEntry = _SonusSonetLineFailureIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 7, 1)
)
sonusSonetLineFailureIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetLineFailureIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetLineFailureIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetLineFailureIntervalEntry.setStatus("current")
_SonusSonetLineFailureIntervalIfIndex_Type = Integer32
_SonusSonetLineFailureIntervalIfIndex_Object = MibTableColumn
sonusSonetLineFailureIntervalIfIndex = _SonusSonetLineFailureIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 7, 1, 1),
    _SonusSonetLineFailureIntervalIfIndex_Type()
)
sonusSonetLineFailureIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLineFailureIntervalIfIndex.setStatus("current")
_SonusSonetLineFailureIntervalNumber_Type = Integer32
_SonusSonetLineFailureIntervalNumber_Object = MibTableColumn
sonusSonetLineFailureIntervalNumber = _SonusSonetLineFailureIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 7, 1, 2),
    _SonusSonetLineFailureIntervalNumber_Type()
)
sonusSonetLineFailureIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLineFailureIntervalNumber.setStatus("current")
_SonusSonetLineFailureIntervalFCs_Type = PerfCurrentCount
_SonusSonetLineFailureIntervalFCs_Object = MibTableColumn
sonusSonetLineFailureIntervalFCs = _SonusSonetLineFailureIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 7, 1, 3),
    _SonusSonetLineFailureIntervalFCs_Type()
)
sonusSonetLineFailureIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLineFailureIntervalFCs.setStatus("current")
_SonusSonetFarEndLineFailureCurrentTable_Object = MibTable
sonusSonetFarEndLineFailureCurrentTable = _SonusSonetFarEndLineFailureCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 8)
)
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureCurrentTable.setStatus("current")
_SonusSonetFarEndLineFailureCurrentEntry_Object = MibTableRow
sonusSonetFarEndLineFailureCurrentEntry = _SonusSonetFarEndLineFailureCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 8, 1)
)
sonusSonetFarEndLineFailureCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndLineFailureCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureCurrentEntry.setStatus("current")
_SonusSonetFarEndLineFailureCurrentIfIndex_Type = Integer32
_SonusSonetFarEndLineFailureCurrentIfIndex_Object = MibTableColumn
sonusSonetFarEndLineFailureCurrentIfIndex = _SonusSonetFarEndLineFailureCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 8, 1, 1),
    _SonusSonetFarEndLineFailureCurrentIfIndex_Type()
)
sonusSonetFarEndLineFailureCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureCurrentIfIndex.setStatus("current")
_SonusSonetFarEndLineFailureCurrentFCs_Type = PerfCurrentCount
_SonusSonetFarEndLineFailureCurrentFCs_Object = MibTableColumn
sonusSonetFarEndLineFailureCurrentFCs = _SonusSonetFarEndLineFailureCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 8, 1, 2),
    _SonusSonetFarEndLineFailureCurrentFCs_Type()
)
sonusSonetFarEndLineFailureCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureCurrentFCs.setStatus("current")
_SonusSonetFarEndLineFailureIntervalTable_Object = MibTable
sonusSonetFarEndLineFailureIntervalTable = _SonusSonetFarEndLineFailureIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 9)
)
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureIntervalTable.setStatus("current")
_SonusSonetFarEndLineFailureIntervalEntry_Object = MibTableRow
sonusSonetFarEndLineFailureIntervalEntry = _SonusSonetFarEndLineFailureIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 9, 1)
)
sonusSonetFarEndLineFailureIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndLineFailureIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndLineFailureIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureIntervalEntry.setStatus("current")
_SonusSonetFarEndLineFailureIntervalIfIndex_Type = Integer32
_SonusSonetFarEndLineFailureIntervalIfIndex_Object = MibTableColumn
sonusSonetFarEndLineFailureIntervalIfIndex = _SonusSonetFarEndLineFailureIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 9, 1, 1),
    _SonusSonetFarEndLineFailureIntervalIfIndex_Type()
)
sonusSonetFarEndLineFailureIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureIntervalIfIndex.setStatus("current")
_SonusSonetFarEndLineFailureIntervalNumber_Type = Integer32
_SonusSonetFarEndLineFailureIntervalNumber_Object = MibTableColumn
sonusSonetFarEndLineFailureIntervalNumber = _SonusSonetFarEndLineFailureIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 9, 1, 2),
    _SonusSonetFarEndLineFailureIntervalNumber_Type()
)
sonusSonetFarEndLineFailureIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureIntervalNumber.setStatus("current")
_SonusSonetFarEndLineFailureIntervalFCs_Type = PerfCurrentCount
_SonusSonetFarEndLineFailureIntervalFCs_Object = MibTableColumn
sonusSonetFarEndLineFailureIntervalFCs = _SonusSonetFarEndLineFailureIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 3, 9, 1, 3),
    _SonusSonetFarEndLineFailureIntervalFCs_Type()
)
sonusSonetFarEndLineFailureIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndLineFailureIntervalFCs.setStatus("current")
_SonusSonetLayer_ObjectIdentity = ObjectIdentity
sonusSonetLayer = _SonusSonetLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 4)
)
_SonusSonetLayerTable_Object = MibTable
sonusSonetLayerTable = _SonusSonetLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sonusSonetLayerTable.setStatus("current")
_SonusSonetLayerEntry_Object = MibTableRow
sonusSonetLayerEntry = _SonusSonetLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 4, 1, 1)
)
sonusSonetLayerEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetLayerShelfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetLayerSlotIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetLayerPortIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetLayerEntry.setStatus("current")
_SonusSonetLayerShelfIndex_Type = SonusShelfIndex
_SonusSonetLayerShelfIndex_Object = MibTableColumn
sonusSonetLayerShelfIndex = _SonusSonetLayerShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 4, 1, 1, 1),
    _SonusSonetLayerShelfIndex_Type()
)
sonusSonetLayerShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLayerShelfIndex.setStatus("current")
_SonusSonetLayerSlotIndex_Type = SonusSlotIndex
_SonusSonetLayerSlotIndex_Object = MibTableColumn
sonusSonetLayerSlotIndex = _SonusSonetLayerSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 4, 1, 1, 2),
    _SonusSonetLayerSlotIndex_Type()
)
sonusSonetLayerSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLayerSlotIndex.setStatus("current")
_SonusSonetLayerPortIndex_Type = Integer32
_SonusSonetLayerPortIndex_Object = MibTableColumn
sonusSonetLayerPortIndex = _SonusSonetLayerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 4, 1, 1, 3),
    _SonusSonetLayerPortIndex_Type()
)
sonusSonetLayerPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetLayerPortIndex.setStatus("current")
_SonusSonetLayerIfIndex_Type = Integer32
_SonusSonetLayerIfIndex_Object = MibTableColumn
sonusSonetLayerIfIndex = _SonusSonetLayerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 4, 1, 1, 4),
    _SonusSonetLayerIfIndex_Type()
)
sonusSonetLayerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetLayerIfIndex.setStatus("current")
_SonusSonetLayerRowStatus_Type = RowStatus
_SonusSonetLayerRowStatus_Object = MibTableColumn
sonusSonetLayerRowStatus = _SonusSonetLayerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 1, 4, 1, 1, 5),
    _SonusSonetLayerRowStatus_Type()
)
sonusSonetLayerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusSonetLayerRowStatus.setStatus("current")
_SonusSonetObjectsPath_ObjectIdentity = ObjectIdentity
sonusSonetObjectsPath = _SonusSonetObjectsPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2)
)
_SonusSonetPathAdmn_ObjectIdentity = ObjectIdentity
sonusSonetPathAdmn = _SonusSonetPathAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1)
)
_SonusSonetPathAdmnTable_Object = MibTable
sonusSonetPathAdmnTable = _SonusSonetPathAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sonusSonetPathAdmnTable.setStatus("current")
_SonusSonetPathAdmnEntry_Object = MibTableRow
sonusSonetPathAdmnEntry = _SonusSonetPathAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1)
)
sonusSonetPathAdmnEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetPathAdmnIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetPathAdmnEntry.setStatus("current")
_SonusSonetPathAdmnIfIndex_Type = Integer32
_SonusSonetPathAdmnIfIndex_Object = MibTableColumn
sonusSonetPathAdmnIfIndex = _SonusSonetPathAdmnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 1),
    _SonusSonetPathAdmnIfIndex_Type()
)
sonusSonetPathAdmnIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnIfIndex.setStatus("current")
_SonusSonetPathAdmnShelfIndex_Type = SonusShelfIndex
_SonusSonetPathAdmnShelfIndex_Object = MibTableColumn
sonusSonetPathAdmnShelfIndex = _SonusSonetPathAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 2),
    _SonusSonetPathAdmnShelfIndex_Type()
)
sonusSonetPathAdmnShelfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnShelfIndex.setStatus("current")
_SonusSonetPathAdmnSlotIndex_Type = SonusSlotIndex
_SonusSonetPathAdmnSlotIndex_Object = MibTableColumn
sonusSonetPathAdmnSlotIndex = _SonusSonetPathAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 3),
    _SonusSonetPathAdmnSlotIndex_Type()
)
sonusSonetPathAdmnSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnSlotIndex.setStatus("current")


class _SonusSonetPathAdmnPortIndex_Type(Integer32):
    """Custom type sonusSonetPathAdmnPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SonusSonetPathAdmnPortIndex_Type.__name__ = "Integer32"
_SonusSonetPathAdmnPortIndex_Object = MibTableColumn
sonusSonetPathAdmnPortIndex = _SonusSonetPathAdmnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 4),
    _SonusSonetPathAdmnPortIndex_Type()
)
sonusSonetPathAdmnPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnPortIndex.setStatus("current")


class _SonusSonetPathAdmnPathIndex_Type(Integer32):
    """Custom type sonusSonetPathAdmnPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetPathAdmnPathIndex_Type.__name__ = "Integer32"
_SonusSonetPathAdmnPathIndex_Object = MibTableColumn
sonusSonetPathAdmnPathIndex = _SonusSonetPathAdmnPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 5),
    _SonusSonetPathAdmnPathIndex_Type()
)
sonusSonetPathAdmnPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnPathIndex.setStatus("current")
_SonusSonetPathAdmnRowStatus_Type = RowStatus
_SonusSonetPathAdmnRowStatus_Object = MibTableColumn
sonusSonetPathAdmnRowStatus = _SonusSonetPathAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 6),
    _SonusSonetPathAdmnRowStatus_Type()
)
sonusSonetPathAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnRowStatus.setStatus("current")


class _SonusSonetPathAdmnState_Type(SonusAdminState):
    """Custom type sonusSonetPathAdmnState based on SonusAdminState"""


_SonusSonetPathAdmnState_Object = MibTableColumn
sonusSonetPathAdmnState = _SonusSonetPathAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 7),
    _SonusSonetPathAdmnState_Type()
)
sonusSonetPathAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnState.setStatus("current")


class _SonusSonetPathAdmnMode_Type(SonusServiceState):
    """Custom type sonusSonetPathAdmnMode based on SonusServiceState"""


_SonusSonetPathAdmnMode_Object = MibTableColumn
sonusSonetPathAdmnMode = _SonusSonetPathAdmnMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 8),
    _SonusSonetPathAdmnMode_Type()
)
sonusSonetPathAdmnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnMode.setStatus("current")


class _SonusSonetPathAdmnAction_Type(SonusAdminAction):
    """Custom type sonusSonetPathAdmnAction based on SonusAdminAction"""


_SonusSonetPathAdmnAction_Object = MibTableColumn
sonusSonetPathAdmnAction = _SonusSonetPathAdmnAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 9),
    _SonusSonetPathAdmnAction_Type()
)
sonusSonetPathAdmnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnAction.setStatus("current")


class _SonusSonetPathAdmnTimeout_Type(Integer32):
    """Custom type sonusSonetPathAdmnTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SonusSonetPathAdmnTimeout_Type.__name__ = "Integer32"
_SonusSonetPathAdmnTimeout_Object = MibTableColumn
sonusSonetPathAdmnTimeout = _SonusSonetPathAdmnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 10),
    _SonusSonetPathAdmnTimeout_Type()
)
sonusSonetPathAdmnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnTimeout.setStatus("current")


class _SonusSonetPathAdmnStatAction_Type(Integer32):
    """Custom type sonusSonetPathAdmnStatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("init15MinuteFarEnd", 2),
          ("init15MinuteNearEnd", 1),
          ("init24HourFarEnd", 8),
          ("init24HourNearEnd", 4))
    )


_SonusSonetPathAdmnStatAction_Type.__name__ = "Integer32"
_SonusSonetPathAdmnStatAction_Object = MibTableColumn
sonusSonetPathAdmnStatAction = _SonusSonetPathAdmnStatAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 11),
    _SonusSonetPathAdmnStatAction_Type()
)
sonusSonetPathAdmnStatAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnStatAction.setStatus("current")


class _SonusSonetPathAdmnRDIMode_Type(Integer32):
    """Custom type sonusSonetPathAdmnRDIMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enhanced", 2),
          ("normal", 1))
    )


_SonusSonetPathAdmnRDIMode_Type.__name__ = "Integer32"
_SonusSonetPathAdmnRDIMode_Object = MibTableColumn
sonusSonetPathAdmnRDIMode = _SonusSonetPathAdmnRDIMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 12),
    _SonusSonetPathAdmnRDIMode_Type()
)
sonusSonetPathAdmnRDIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnRDIMode.setStatus("current")


class _SonusSonetPathAdmnTraceState_Type(SonusAdminState):
    """Custom type sonusSonetPathAdmnTraceState based on SonusAdminState"""


_SonusSonetPathAdmnTraceState_Object = MibTableColumn
sonusSonetPathAdmnTraceState = _SonusSonetPathAdmnTraceState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 13),
    _SonusSonetPathAdmnTraceState_Type()
)
sonusSonetPathAdmnTraceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnTraceState.setStatus("current")


class _SonusSonetPathAdmnTraceExpMsg_Type(DisplayString):
    """Custom type sonusSonetPathAdmnTraceExpMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 61),
    )


_SonusSonetPathAdmnTraceExpMsg_Type.__name__ = "DisplayString"
_SonusSonetPathAdmnTraceExpMsg_Object = MibTableColumn
sonusSonetPathAdmnTraceExpMsg = _SonusSonetPathAdmnTraceExpMsg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 14),
    _SonusSonetPathAdmnTraceExpMsg_Type()
)
sonusSonetPathAdmnTraceExpMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnTraceExpMsg.setStatus("current")


class _SonusSonetPathAdmnTraceXmtMsg_Type(DisplayString):
    """Custom type sonusSonetPathAdmnTraceXmtMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 61),
    )


_SonusSonetPathAdmnTraceXmtMsg_Type.__name__ = "DisplayString"
_SonusSonetPathAdmnTraceXmtMsg_Object = MibTableColumn
sonusSonetPathAdmnTraceXmtMsg = _SonusSonetPathAdmnTraceXmtMsg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 15),
    _SonusSonetPathAdmnTraceXmtMsg_Type()
)
sonusSonetPathAdmnTraceXmtMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnTraceXmtMsg.setStatus("current")


class _SonusSonetPathAdmnTraceRcvMsg_Type(DisplayString):
    """Custom type sonusSonetPathAdmnTraceRcvMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 61),
    )


_SonusSonetPathAdmnTraceRcvMsg_Type.__name__ = "DisplayString"
_SonusSonetPathAdmnTraceRcvMsg_Object = MibTableColumn
sonusSonetPathAdmnTraceRcvMsg = _SonusSonetPathAdmnTraceRcvMsg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 16),
    _SonusSonetPathAdmnTraceRcvMsg_Type()
)
sonusSonetPathAdmnTraceRcvMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnTraceRcvMsg.setStatus("current")


class _SonusSonetPathAdmnOperStatus_Type(Integer32):
    """Custom type sonusSonetPathAdmnOperStatus based on Integer32"""
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
        *(("disabled", 5),
          ("down", 7),
          ("dryingUp", 4),
          ("enabledDown", 3),
          ("enabledInService", 1),
          ("enabledOutOfService", 2),
          ("up", 6))
    )


_SonusSonetPathAdmnOperStatus_Type.__name__ = "Integer32"
_SonusSonetPathAdmnOperStatus_Object = MibTableColumn
sonusSonetPathAdmnOperStatus = _SonusSonetPathAdmnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 17),
    _SonusSonetPathAdmnOperStatus_Type()
)
sonusSonetPathAdmnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnOperStatus.setStatus("current")


class _SonusSonetPathAdmnDs3ModeOverride_Type(SonusAdminState):
    """Custom type sonusSonetPathAdmnDs3ModeOverride based on SonusAdminState"""


_SonusSonetPathAdmnDs3ModeOverride_Object = MibTableColumn
sonusSonetPathAdmnDs3ModeOverride = _SonusSonetPathAdmnDs3ModeOverride_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 1, 1, 1, 18),
    _SonusSonetPathAdmnDs3ModeOverride_Type()
)
sonusSonetPathAdmnDs3ModeOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathAdmnDs3ModeOverride.setStatus("current")
_SonusSonetPath_ObjectIdentity = ObjectIdentity
sonusSonetPath = _SonusSonetPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2)
)
_SonusSonetPathThresholdTable_Object = MibTable
sonusSonetPathThresholdTable = _SonusSonetPathThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sonusSonetPathThresholdTable.setStatus("current")
_SonusSonetPathThresholdEntry_Object = MibTableRow
sonusSonetPathThresholdEntry = _SonusSonetPathThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1)
)
sonusSonetPathThresholdEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetPathThresholdIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetPathThresholdEntry.setStatus("current")
_SonusSonetPathThresholdIfIndex_Type = Integer32
_SonusSonetPathThresholdIfIndex_Object = MibTableColumn
sonusSonetPathThresholdIfIndex = _SonusSonetPathThresholdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 1),
    _SonusSonetPathThresholdIfIndex_Type()
)
sonusSonetPathThresholdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPathThresholdIfIndex.setStatus("current")


class _SonusSonetPathThresholdPathIndex_Type(Integer32):
    """Custom type sonusSonetPathThresholdPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetPathThresholdPathIndex_Type.__name__ = "Integer32"
_SonusSonetPathThresholdPathIndex_Object = MibTableColumn
sonusSonetPathThresholdPathIndex = _SonusSonetPathThresholdPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 2),
    _SonusSonetPathThresholdPathIndex_Type()
)
sonusSonetPathThresholdPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathThresholdPathIndex.setStatus("current")


class _SonusSonetPathThreshold15mCVs_Type(Integer32):
    """Custom type sonusSonetPathThreshold15mCVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusSonetPathThreshold15mCVs_Type.__name__ = "Integer32"
_SonusSonetPathThreshold15mCVs_Object = MibTableColumn
sonusSonetPathThreshold15mCVs = _SonusSonetPathThreshold15mCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 3),
    _SonusSonetPathThreshold15mCVs_Type()
)
sonusSonetPathThreshold15mCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathThreshold15mCVs.setStatus("current")


class _SonusSonetPathThreshold15mESs_Type(Integer32):
    """Custom type sonusSonetPathThreshold15mESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonusSonetPathThreshold15mESs_Type.__name__ = "Integer32"
_SonusSonetPathThreshold15mESs_Object = MibTableColumn
sonusSonetPathThreshold15mESs = _SonusSonetPathThreshold15mESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 4),
    _SonusSonetPathThreshold15mESs_Type()
)
sonusSonetPathThreshold15mESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathThreshold15mESs.setStatus("current")


class _SonusSonetPathThreshold15mSESs_Type(Integer32):
    """Custom type sonusSonetPathThreshold15mSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonusSonetPathThreshold15mSESs_Type.__name__ = "Integer32"
_SonusSonetPathThreshold15mSESs_Object = MibTableColumn
sonusSonetPathThreshold15mSESs = _SonusSonetPathThreshold15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 5),
    _SonusSonetPathThreshold15mSESs_Type()
)
sonusSonetPathThreshold15mSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathThreshold15mSESs.setStatus("current")


class _SonusSonetPathThreshold15mUASs_Type(Integer32):
    """Custom type sonusSonetPathThreshold15mUASs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonusSonetPathThreshold15mUASs_Type.__name__ = "Integer32"
_SonusSonetPathThreshold15mUASs_Object = MibTableColumn
sonusSonetPathThreshold15mUASs = _SonusSonetPathThreshold15mUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 6),
    _SonusSonetPathThreshold15mUASs_Type()
)
sonusSonetPathThreshold15mUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathThreshold15mUASs.setStatus("current")


class _SonusSonetPathThreshold24hCVs_Type(Integer32):
    """Custom type sonusSonetPathThreshold24hCVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_SonusSonetPathThreshold24hCVs_Type.__name__ = "Integer32"
_SonusSonetPathThreshold24hCVs_Object = MibTableColumn
sonusSonetPathThreshold24hCVs = _SonusSonetPathThreshold24hCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 7),
    _SonusSonetPathThreshold24hCVs_Type()
)
sonusSonetPathThreshold24hCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathThreshold24hCVs.setStatus("current")


class _SonusSonetPathThreshold24hESs_Type(Integer32):
    """Custom type sonusSonetPathThreshold24hESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetPathThreshold24hESs_Type.__name__ = "Integer32"
_SonusSonetPathThreshold24hESs_Object = MibTableColumn
sonusSonetPathThreshold24hESs = _SonusSonetPathThreshold24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 8),
    _SonusSonetPathThreshold24hESs_Type()
)
sonusSonetPathThreshold24hESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathThreshold24hESs.setStatus("current")


class _SonusSonetPathThreshold24hSESs_Type(Integer32):
    """Custom type sonusSonetPathThreshold24hSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetPathThreshold24hSESs_Type.__name__ = "Integer32"
_SonusSonetPathThreshold24hSESs_Object = MibTableColumn
sonusSonetPathThreshold24hSESs = _SonusSonetPathThreshold24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 9),
    _SonusSonetPathThreshold24hSESs_Type()
)
sonusSonetPathThreshold24hSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathThreshold24hSESs.setStatus("current")


class _SonusSonetPathThreshold24hUASs_Type(Integer32):
    """Custom type sonusSonetPathThreshold24hUASs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSonetPathThreshold24hUASs_Type.__name__ = "Integer32"
_SonusSonetPathThreshold24hUASs_Object = MibTableColumn
sonusSonetPathThreshold24hUASs = _SonusSonetPathThreshold24hUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 1, 1, 10),
    _SonusSonetPathThreshold24hUASs_Type()
)
sonusSonetPathThreshold24hUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSonetPathThreshold24hUASs.setStatus("current")
_SonusSonetPathCurrentTable_Object = MibTable
sonusSonetPathCurrentTable = _SonusSonetPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sonusSonetPathCurrentTable.setStatus("current")
_SonusSonetPathCurrentEntry_Object = MibTableRow
sonusSonetPathCurrentEntry = _SonusSonetPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1)
)
sonusSonetPathCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetPathCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetPathCurrentEntry.setStatus("current")
_SonusSonetPathCurrentIfIndex_Type = Integer32
_SonusSonetPathCurrentIfIndex_Object = MibTableColumn
sonusSonetPathCurrentIfIndex = _SonusSonetPathCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 1),
    _SonusSonetPathCurrentIfIndex_Type()
)
sonusSonetPathCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentIfIndex.setStatus("current")


class _SonusSonetPathCurrentPathIndex_Type(Integer32):
    """Custom type sonusSonetPathCurrentPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetPathCurrentPathIndex_Type.__name__ = "Integer32"
_SonusSonetPathCurrentPathIndex_Object = MibTableColumn
sonusSonetPathCurrentPathIndex = _SonusSonetPathCurrentPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 2),
    _SonusSonetPathCurrentPathIndex_Type()
)
sonusSonetPathCurrentPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentPathIndex.setStatus("current")


class _SonusSonetPathCurrentWidth_Type(Integer32):
    """Custom type sonusSonetPathCurrentWidth based on Integer32"""
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
        *(("sts1", 1),
          ("sts12cSTM4", 3),
          ("sts24c", 4),
          ("sts3cSTM1", 2),
          ("sts48cSTM16", 5))
    )


_SonusSonetPathCurrentWidth_Type.__name__ = "Integer32"
_SonusSonetPathCurrentWidth_Object = MibTableColumn
sonusSonetPathCurrentWidth = _SonusSonetPathCurrentWidth_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 3),
    _SonusSonetPathCurrentWidth_Type()
)
sonusSonetPathCurrentWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentWidth.setStatus("current")


class _SonusSonetPathCurrentStatus_Type(Integer32):
    """Custom type sonusSonetPathCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 62),
    )


_SonusSonetPathCurrentStatus_Type.__name__ = "Integer32"
_SonusSonetPathCurrentStatus_Object = MibTableColumn
sonusSonetPathCurrentStatus = _SonusSonetPathCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 4),
    _SonusSonetPathCurrentStatus_Type()
)
sonusSonetPathCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentStatus.setStatus("current")
_SonusSonetPathCurrentESs_Type = PerfCurrentCount
_SonusSonetPathCurrentESs_Object = MibTableColumn
sonusSonetPathCurrentESs = _SonusSonetPathCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 5),
    _SonusSonetPathCurrentESs_Type()
)
sonusSonetPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentESs.setStatus("current")
_SonusSonetPathCurrentSESs_Type = PerfCurrentCount
_SonusSonetPathCurrentSESs_Object = MibTableColumn
sonusSonetPathCurrentSESs = _SonusSonetPathCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 6),
    _SonusSonetPathCurrentSESs_Type()
)
sonusSonetPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentSESs.setStatus("current")
_SonusSonetPathCurrentUASs_Type = PerfCurrentCount
_SonusSonetPathCurrentUASs_Object = MibTableColumn
sonusSonetPathCurrentUASs = _SonusSonetPathCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 7),
    _SonusSonetPathCurrentUASs_Type()
)
sonusSonetPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentUASs.setStatus("current")
_SonusSonetPathCurrentCVs_Type = PerfCurrentCount
_SonusSonetPathCurrentCVs_Object = MibTableColumn
sonusSonetPathCurrentCVs = _SonusSonetPathCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 8),
    _SonusSonetPathCurrentCVs_Type()
)
sonusSonetPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentCVs.setStatus("current")
_SonusSonetPathCurrentFCs_Type = PerfCurrentCount
_SonusSonetPathCurrentFCs_Object = MibTableColumn
sonusSonetPathCurrentFCs = _SonusSonetPathCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 9),
    _SonusSonetPathCurrentFCs_Type()
)
sonusSonetPathCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentFCs.setStatus("current")


class _SonusSonetPathCurrentTraceStatus_Type(Integer32):
    """Custom type sonusSonetPathCurrentTraceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodefect", 1),
          ("tracemismatch", 2))
    )


_SonusSonetPathCurrentTraceStatus_Type.__name__ = "Integer32"
_SonusSonetPathCurrentTraceStatus_Object = MibTableColumn
sonusSonetPathCurrentTraceStatus = _SonusSonetPathCurrentTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 2, 1, 10),
    _SonusSonetPathCurrentTraceStatus_Type()
)
sonusSonetPathCurrentTraceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathCurrentTraceStatus.setStatus("current")
_SonusSonetPathIntervalTable_Object = MibTable
sonusSonetPathIntervalTable = _SonusSonetPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    sonusSonetPathIntervalTable.setStatus("current")
_SonusSonetPathIntervalEntry_Object = MibTableRow
sonusSonetPathIntervalEntry = _SonusSonetPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1)
)
sonusSonetPathIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetPathIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetPathIntervalEntry.setStatus("current")
_SonusSonetPathIntervalIfIndex_Type = Integer32
_SonusSonetPathIntervalIfIndex_Object = MibTableColumn
sonusSonetPathIntervalIfIndex = _SonusSonetPathIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 1),
    _SonusSonetPathIntervalIfIndex_Type()
)
sonusSonetPathIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalIfIndex.setStatus("current")


class _SonusSonetPathIntervalPathIndex_Type(Integer32):
    """Custom type sonusSonetPathIntervalPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetPathIntervalPathIndex_Type.__name__ = "Integer32"
_SonusSonetPathIntervalPathIndex_Object = MibTableColumn
sonusSonetPathIntervalPathIndex = _SonusSonetPathIntervalPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 2),
    _SonusSonetPathIntervalPathIndex_Type()
)
sonusSonetPathIntervalPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalPathIndex.setStatus("current")


class _SonusSonetPathIntervalNumber_Type(Integer32):
    """Custom type sonusSonetPathIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonusSonetPathIntervalNumber_Type.__name__ = "Integer32"
_SonusSonetPathIntervalNumber_Object = MibTableColumn
sonusSonetPathIntervalNumber = _SonusSonetPathIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 3),
    _SonusSonetPathIntervalNumber_Type()
)
sonusSonetPathIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalNumber.setStatus("current")
_SonusSonetPathIntervalESs_Type = PerfIntervalCount
_SonusSonetPathIntervalESs_Object = MibTableColumn
sonusSonetPathIntervalESs = _SonusSonetPathIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 4),
    _SonusSonetPathIntervalESs_Type()
)
sonusSonetPathIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalESs.setStatus("current")
_SonusSonetPathIntervalSESs_Type = PerfIntervalCount
_SonusSonetPathIntervalSESs_Object = MibTableColumn
sonusSonetPathIntervalSESs = _SonusSonetPathIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 5),
    _SonusSonetPathIntervalSESs_Type()
)
sonusSonetPathIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalSESs.setStatus("current")
_SonusSonetPathIntervalUASs_Type = PerfIntervalCount
_SonusSonetPathIntervalUASs_Object = MibTableColumn
sonusSonetPathIntervalUASs = _SonusSonetPathIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 6),
    _SonusSonetPathIntervalUASs_Type()
)
sonusSonetPathIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalUASs.setStatus("current")
_SonusSonetPathIntervalCVs_Type = PerfIntervalCount
_SonusSonetPathIntervalCVs_Object = MibTableColumn
sonusSonetPathIntervalCVs = _SonusSonetPathIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 7),
    _SonusSonetPathIntervalCVs_Type()
)
sonusSonetPathIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalCVs.setStatus("current")
_SonusSonetPathIntervalFCs_Type = PerfIntervalCount
_SonusSonetPathIntervalFCs_Object = MibTableColumn
sonusSonetPathIntervalFCs = _SonusSonetPathIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 8),
    _SonusSonetPathIntervalFCs_Type()
)
sonusSonetPathIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalFCs.setStatus("current")
_SonusSonetPathIntervalValidData_Type = TruthValue
_SonusSonetPathIntervalValidData_Object = MibTableColumn
sonusSonetPathIntervalValidData = _SonusSonetPathIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 3, 1, 9),
    _SonusSonetPathIntervalValidData_Type()
)
sonusSonetPathIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathIntervalValidData.setStatus("current")
_SonusSonetFarEndPathCurrentTable_Object = MibTable
sonusSonetFarEndPathCurrentTable = _SonusSonetFarEndPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentTable.setStatus("current")
_SonusSonetFarEndPathCurrentEntry_Object = MibTableRow
sonusSonetFarEndPathCurrentEntry = _SonusSonetFarEndPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4, 1)
)
sonusSonetFarEndPathCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndPathCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentEntry.setStatus("current")
_SonusSonetFarEndPathCurrentIfIndex_Type = Integer32
_SonusSonetFarEndPathCurrentIfIndex_Object = MibTableColumn
sonusSonetFarEndPathCurrentIfIndex = _SonusSonetFarEndPathCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4, 1, 1),
    _SonusSonetFarEndPathCurrentIfIndex_Type()
)
sonusSonetFarEndPathCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentIfIndex.setStatus("current")


class _SonusSonetFarEndPathCurrentPathIndex_Type(Integer32):
    """Custom type sonusSonetFarEndPathCurrentPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetFarEndPathCurrentPathIndex_Type.__name__ = "Integer32"
_SonusSonetFarEndPathCurrentPathIndex_Object = MibTableColumn
sonusSonetFarEndPathCurrentPathIndex = _SonusSonetFarEndPathCurrentPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4, 1, 2),
    _SonusSonetFarEndPathCurrentPathIndex_Type()
)
sonusSonetFarEndPathCurrentPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentPathIndex.setStatus("current")
_SonusSonetFarEndPathCurrentESs_Type = PerfCurrentCount
_SonusSonetFarEndPathCurrentESs_Object = MibTableColumn
sonusSonetFarEndPathCurrentESs = _SonusSonetFarEndPathCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4, 1, 3),
    _SonusSonetFarEndPathCurrentESs_Type()
)
sonusSonetFarEndPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentESs.setStatus("current")
_SonusSonetFarEndPathCurrentSESs_Type = PerfCurrentCount
_SonusSonetFarEndPathCurrentSESs_Object = MibTableColumn
sonusSonetFarEndPathCurrentSESs = _SonusSonetFarEndPathCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4, 1, 4),
    _SonusSonetFarEndPathCurrentSESs_Type()
)
sonusSonetFarEndPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentSESs.setStatus("current")
_SonusSonetFarEndPathCurrentUASs_Type = PerfCurrentCount
_SonusSonetFarEndPathCurrentUASs_Object = MibTableColumn
sonusSonetFarEndPathCurrentUASs = _SonusSonetFarEndPathCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4, 1, 5),
    _SonusSonetFarEndPathCurrentUASs_Type()
)
sonusSonetFarEndPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentUASs.setStatus("current")
_SonusSonetFarEndPathCurrentCVs_Type = PerfCurrentCount
_SonusSonetFarEndPathCurrentCVs_Object = MibTableColumn
sonusSonetFarEndPathCurrentCVs = _SonusSonetFarEndPathCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4, 1, 6),
    _SonusSonetFarEndPathCurrentCVs_Type()
)
sonusSonetFarEndPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentCVs.setStatus("current")
_SonusSonetFarEndPathCurrentFCs_Type = PerfCurrentCount
_SonusSonetFarEndPathCurrentFCs_Object = MibTableColumn
sonusSonetFarEndPathCurrentFCs = _SonusSonetFarEndPathCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 4, 1, 7),
    _SonusSonetFarEndPathCurrentFCs_Type()
)
sonusSonetFarEndPathCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathCurrentFCs.setStatus("current")
_SonusSonetFarEndPathIntervalTable_Object = MibTable
sonusSonetFarEndPathIntervalTable = _SonusSonetFarEndPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalTable.setStatus("current")
_SonusSonetFarEndPathIntervalEntry_Object = MibTableRow
sonusSonetFarEndPathIntervalEntry = _SonusSonetFarEndPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1)
)
sonusSonetFarEndPathIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndPathIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalEntry.setStatus("current")
_SonusSonetFarEndPathIntervalIfIndex_Type = Integer32
_SonusSonetFarEndPathIntervalIfIndex_Object = MibTableColumn
sonusSonetFarEndPathIntervalIfIndex = _SonusSonetFarEndPathIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 1),
    _SonusSonetFarEndPathIntervalIfIndex_Type()
)
sonusSonetFarEndPathIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalIfIndex.setStatus("current")


class _SonusSonetFarEndPathIntervalPathIndex_Type(Integer32):
    """Custom type sonusSonetFarEndPathIntervalPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetFarEndPathIntervalPathIndex_Type.__name__ = "Integer32"
_SonusSonetFarEndPathIntervalPathIndex_Object = MibTableColumn
sonusSonetFarEndPathIntervalPathIndex = _SonusSonetFarEndPathIntervalPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 2),
    _SonusSonetFarEndPathIntervalPathIndex_Type()
)
sonusSonetFarEndPathIntervalPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalPathIndex.setStatus("current")


class _SonusSonetFarEndPathIntervalNumber_Type(Integer32):
    """Custom type sonusSonetFarEndPathIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonusSonetFarEndPathIntervalNumber_Type.__name__ = "Integer32"
_SonusSonetFarEndPathIntervalNumber_Object = MibTableColumn
sonusSonetFarEndPathIntervalNumber = _SonusSonetFarEndPathIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 3),
    _SonusSonetFarEndPathIntervalNumber_Type()
)
sonusSonetFarEndPathIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalNumber.setStatus("current")
_SonusSonetFarEndPathIntervalESs_Type = PerfIntervalCount
_SonusSonetFarEndPathIntervalESs_Object = MibTableColumn
sonusSonetFarEndPathIntervalESs = _SonusSonetFarEndPathIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 4),
    _SonusSonetFarEndPathIntervalESs_Type()
)
sonusSonetFarEndPathIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalESs.setStatus("current")
_SonusSonetFarEndPathIntervalSESs_Type = PerfIntervalCount
_SonusSonetFarEndPathIntervalSESs_Object = MibTableColumn
sonusSonetFarEndPathIntervalSESs = _SonusSonetFarEndPathIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 5),
    _SonusSonetFarEndPathIntervalSESs_Type()
)
sonusSonetFarEndPathIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalSESs.setStatus("current")
_SonusSonetFarEndPathIntervalUASs_Type = PerfIntervalCount
_SonusSonetFarEndPathIntervalUASs_Object = MibTableColumn
sonusSonetFarEndPathIntervalUASs = _SonusSonetFarEndPathIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 6),
    _SonusSonetFarEndPathIntervalUASs_Type()
)
sonusSonetFarEndPathIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalUASs.setStatus("current")
_SonusSonetFarEndPathIntervalCVs_Type = PerfIntervalCount
_SonusSonetFarEndPathIntervalCVs_Object = MibTableColumn
sonusSonetFarEndPathIntervalCVs = _SonusSonetFarEndPathIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 7),
    _SonusSonetFarEndPathIntervalCVs_Type()
)
sonusSonetFarEndPathIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalCVs.setStatus("current")
_SonusSonetFarEndPathIntervalFCs_Type = PerfIntervalCount
_SonusSonetFarEndPathIntervalFCs_Object = MibTableColumn
sonusSonetFarEndPathIntervalFCs = _SonusSonetFarEndPathIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 8),
    _SonusSonetFarEndPathIntervalFCs_Type()
)
sonusSonetFarEndPathIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalFCs.setStatus("current")
_SonusSonetFarEndPathIntervalValidData_Type = TruthValue
_SonusSonetFarEndPathIntervalValidData_Object = MibTableColumn
sonusSonetFarEndPathIntervalValidData = _SonusSonetFarEndPathIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 5, 1, 9),
    _SonusSonetFarEndPathIntervalValidData_Type()
)
sonusSonetFarEndPathIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathIntervalValidData.setStatus("current")
_SonusSonetPathFailureCurrentTable_Object = MibTable
sonusSonetPathFailureCurrentTable = _SonusSonetPathFailureCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    sonusSonetPathFailureCurrentTable.setStatus("current")
_SonusSonetPathFailureCurrentEntry_Object = MibTableRow
sonusSonetPathFailureCurrentEntry = _SonusSonetPathFailureCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 6, 1)
)
sonusSonetPathFailureCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetPathFailureCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetPathFailureCurrentEntry.setStatus("current")
_SonusSonetPathFailureCurrentIfIndex_Type = Integer32
_SonusSonetPathFailureCurrentIfIndex_Object = MibTableColumn
sonusSonetPathFailureCurrentIfIndex = _SonusSonetPathFailureCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 6, 1, 1),
    _SonusSonetPathFailureCurrentIfIndex_Type()
)
sonusSonetPathFailureCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPathFailureCurrentIfIndex.setStatus("current")


class _SonusSonetPathFailureCurrentPathIndex_Type(Integer32):
    """Custom type sonusSonetPathFailureCurrentPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetPathFailureCurrentPathIndex_Type.__name__ = "Integer32"
_SonusSonetPathFailureCurrentPathIndex_Object = MibTableColumn
sonusSonetPathFailureCurrentPathIndex = _SonusSonetPathFailureCurrentPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 6, 1, 2),
    _SonusSonetPathFailureCurrentPathIndex_Type()
)
sonusSonetPathFailureCurrentPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathFailureCurrentPathIndex.setStatus("current")
_SonusSonetPathFailureCurrentFCs_Type = PerfCurrentCount
_SonusSonetPathFailureCurrentFCs_Object = MibTableColumn
sonusSonetPathFailureCurrentFCs = _SonusSonetPathFailureCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 6, 1, 3),
    _SonusSonetPathFailureCurrentFCs_Type()
)
sonusSonetPathFailureCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathFailureCurrentFCs.setStatus("current")


class _SonusSonetPathFailureCurrentTraceStatus_Type(Integer32):
    """Custom type sonusSonetPathFailureCurrentTraceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodefect", 1),
          ("tracemismatch", 2))
    )


_SonusSonetPathFailureCurrentTraceStatus_Type.__name__ = "Integer32"
_SonusSonetPathFailureCurrentTraceStatus_Object = MibTableColumn
sonusSonetPathFailureCurrentTraceStatus = _SonusSonetPathFailureCurrentTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 6, 1, 4),
    _SonusSonetPathFailureCurrentTraceStatus_Type()
)
sonusSonetPathFailureCurrentTraceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathFailureCurrentTraceStatus.setStatus("current")
_SonusSonetPathFailureIntervalTable_Object = MibTable
sonusSonetPathFailureIntervalTable = _SonusSonetPathFailureIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 7)
)
if mibBuilder.loadTexts:
    sonusSonetPathFailureIntervalTable.setStatus("current")
_SonusSonetPathFailureIntervalEntry_Object = MibTableRow
sonusSonetPathFailureIntervalEntry = _SonusSonetPathFailureIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 7, 1)
)
sonusSonetPathFailureIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetPathFailureIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetPathFailureIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetPathFailureIntervalEntry.setStatus("current")
_SonusSonetPathFailureIntervalIfIndex_Type = Integer32
_SonusSonetPathFailureIntervalIfIndex_Object = MibTableColumn
sonusSonetPathFailureIntervalIfIndex = _SonusSonetPathFailureIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 7, 1, 1),
    _SonusSonetPathFailureIntervalIfIndex_Type()
)
sonusSonetPathFailureIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPathFailureIntervalIfIndex.setStatus("current")


class _SonusSonetPathFailureIntervalPathIndex_Type(Integer32):
    """Custom type sonusSonetPathFailureIntervalPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetPathFailureIntervalPathIndex_Type.__name__ = "Integer32"
_SonusSonetPathFailureIntervalPathIndex_Object = MibTableColumn
sonusSonetPathFailureIntervalPathIndex = _SonusSonetPathFailureIntervalPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 7, 1, 2),
    _SonusSonetPathFailureIntervalPathIndex_Type()
)
sonusSonetPathFailureIntervalPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathFailureIntervalPathIndex.setStatus("current")
_SonusSonetPathFailureIntervalNumber_Type = Integer32
_SonusSonetPathFailureIntervalNumber_Object = MibTableColumn
sonusSonetPathFailureIntervalNumber = _SonusSonetPathFailureIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 7, 1, 3),
    _SonusSonetPathFailureIntervalNumber_Type()
)
sonusSonetPathFailureIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetPathFailureIntervalNumber.setStatus("current")
_SonusSonetPathFailureIntervalFCs_Type = PerfCurrentCount
_SonusSonetPathFailureIntervalFCs_Object = MibTableColumn
sonusSonetPathFailureIntervalFCs = _SonusSonetPathFailureIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 7, 1, 4),
    _SonusSonetPathFailureIntervalFCs_Type()
)
sonusSonetPathFailureIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetPathFailureIntervalFCs.setStatus("current")
_SonusSonetFarEndPathFailureCurrentTable_Object = MibTable
sonusSonetFarEndPathFailureCurrentTable = _SonusSonetFarEndPathFailureCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 8)
)
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureCurrentTable.setStatus("current")
_SonusSonetFarEndPathFailureCurrentEntry_Object = MibTableRow
sonusSonetFarEndPathFailureCurrentEntry = _SonusSonetFarEndPathFailureCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 8, 1)
)
sonusSonetFarEndPathFailureCurrentEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndPathFailureCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureCurrentEntry.setStatus("current")
_SonusSonetFarEndPathFailureCurrentIfIndex_Type = Integer32
_SonusSonetFarEndPathFailureCurrentIfIndex_Object = MibTableColumn
sonusSonetFarEndPathFailureCurrentIfIndex = _SonusSonetFarEndPathFailureCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 8, 1, 1),
    _SonusSonetFarEndPathFailureCurrentIfIndex_Type()
)
sonusSonetFarEndPathFailureCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureCurrentIfIndex.setStatus("current")


class _SonusSonetFarEndPathFailureCurrentPathIndex_Type(Integer32):
    """Custom type sonusSonetFarEndPathFailureCurrentPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetFarEndPathFailureCurrentPathIndex_Type.__name__ = "Integer32"
_SonusSonetFarEndPathFailureCurrentPathIndex_Object = MibTableColumn
sonusSonetFarEndPathFailureCurrentPathIndex = _SonusSonetFarEndPathFailureCurrentPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 8, 1, 2),
    _SonusSonetFarEndPathFailureCurrentPathIndex_Type()
)
sonusSonetFarEndPathFailureCurrentPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureCurrentPathIndex.setStatus("current")
_SonusSonetFarEndPathFailureCurrentFCs_Type = PerfCurrentCount
_SonusSonetFarEndPathFailureCurrentFCs_Object = MibTableColumn
sonusSonetFarEndPathFailureCurrentFCs = _SonusSonetFarEndPathFailureCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 8, 1, 3),
    _SonusSonetFarEndPathFailureCurrentFCs_Type()
)
sonusSonetFarEndPathFailureCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureCurrentFCs.setStatus("current")
_SonusSonetFarEndPathFailureIntervalTable_Object = MibTable
sonusSonetFarEndPathFailureIntervalTable = _SonusSonetFarEndPathFailureIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 9)
)
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureIntervalTable.setStatus("current")
_SonusSonetFarEndPathFailureIntervalEntry_Object = MibTableRow
sonusSonetFarEndPathFailureIntervalEntry = _SonusSonetFarEndPathFailureIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 9, 1)
)
sonusSonetFarEndPathFailureIntervalEntry.setIndexNames(
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndPathFailureIntervalIfIndex"),
    (0, "SONUS-SONET-MIB", "sonusSonetFarEndPathFailureIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureIntervalEntry.setStatus("current")
_SonusSonetFarEndPathFailureIntervalIfIndex_Type = Integer32
_SonusSonetFarEndPathFailureIntervalIfIndex_Object = MibTableColumn
sonusSonetFarEndPathFailureIntervalIfIndex = _SonusSonetFarEndPathFailureIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 9, 1, 1),
    _SonusSonetFarEndPathFailureIntervalIfIndex_Type()
)
sonusSonetFarEndPathFailureIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureIntervalIfIndex.setStatus("current")


class _SonusSonetFarEndPathFailureIntervalPathIndex_Type(Integer32):
    """Custom type sonusSonetFarEndPathFailureIntervalPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSonetFarEndPathFailureIntervalPathIndex_Type.__name__ = "Integer32"
_SonusSonetFarEndPathFailureIntervalPathIndex_Object = MibTableColumn
sonusSonetFarEndPathFailureIntervalPathIndex = _SonusSonetFarEndPathFailureIntervalPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 9, 1, 2),
    _SonusSonetFarEndPathFailureIntervalPathIndex_Type()
)
sonusSonetFarEndPathFailureIntervalPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureIntervalPathIndex.setStatus("current")
_SonusSonetFarEndPathFailureIntervalNumber_Type = Integer32
_SonusSonetFarEndPathFailureIntervalNumber_Object = MibTableColumn
sonusSonetFarEndPathFailureIntervalNumber = _SonusSonetFarEndPathFailureIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 9, 1, 3),
    _SonusSonetFarEndPathFailureIntervalNumber_Type()
)
sonusSonetFarEndPathFailureIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureIntervalNumber.setStatus("current")
_SonusSonetFarEndPathFailureIntervalFCs_Type = PerfCurrentCount
_SonusSonetFarEndPathFailureIntervalFCs_Object = MibTableColumn
sonusSonetFarEndPathFailureIntervalFCs = _SonusSonetFarEndPathFailureIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 2, 2, 9, 1, 4),
    _SonusSonetFarEndPathFailureIntervalFCs_Type()
)
sonusSonetFarEndPathFailureIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetFarEndPathFailureIntervalFCs.setStatus("current")
_SonusSonetNextIndex_Type = Integer32
_SonusSonetNextIndex_Object = MibScalar
sonusSonetNextIndex = _SonusSonetNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 3),
    _SonusSonetNextIndex_Type()
)
sonusSonetNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetNextIndex.setStatus("current")
_SonusSonetMIBNotifications_ObjectIdentity = ObjectIdentity
sonusSonetMIBNotifications = _SonusSonetMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4)
)
_SonusSonetMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusSonetMIBNotificationsPrefix = _SonusSonetMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0)
)
_SonusSonetMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusSonetMIBNotificationsObjects = _SonusSonetMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 1)
)


class _SonusSonetAdminStatus_Type(Integer32):
    """Custom type sonusSonetAdminStatus based on Integer32"""
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
        *(("deleted", 4),
          ("disabled", 3),
          ("dryingUp", 5),
          ("enabledInService", 1),
          ("enabledOutOfService", 2))
    )


_SonusSonetAdminStatus_Type.__name__ = "Integer32"
_SonusSonetAdminStatus_Object = MibScalar
sonusSonetAdminStatus = _SonusSonetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 1, 1),
    _SonusSonetAdminStatus_Type()
)
sonusSonetAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetAdminStatus.setStatus("current")


class _SonusSonetOperStatus_Type(Integer32):
    """Custom type sonusSonetOperStatus based on Integer32"""
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
        *(("disabled", 6),
          ("dryingUp", 3),
          ("inService", 1),
          ("inServiceDown", 4),
          ("outOfService", 2),
          ("outOfServiceDown", 5))
    )


_SonusSonetOperStatus_Type.__name__ = "Integer32"
_SonusSonetOperStatus_Object = MibScalar
sonusSonetOperStatus = _SonusSonetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 1, 2),
    _SonusSonetOperStatus_Type()
)
sonusSonetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetOperStatus.setStatus("obsolete")


class _SonusSonetAlarmStatus_Type(Integer32):
    """Custom type sonusSonetAlarmStatus based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("lAIS", 5),
          ("lAISClear", 6),
          ("lRFI", 7),
          ("lRFIClear", 8),
          ("lof", 3),
          ("lofClear", 4),
          ("los", 1),
          ("losClear", 2),
          ("pAIS", 9),
          ("pAISClear", 10),
          ("pLOP", 13),
          ("pLOPClear", 14),
          ("pPLM", 17),
          ("pPLMClear", 18),
          ("pRFI", 11),
          ("pRFIClear", 12),
          ("pTIM", 19),
          ("pTIMClear", 20),
          ("pUNEQ", 15),
          ("pUNEQClear", 16))
    )


_SonusSonetAlarmStatus_Type.__name__ = "Integer32"
_SonusSonetAlarmStatus_Object = MibScalar
sonusSonetAlarmStatus = _SonusSonetAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 1, 3),
    _SonusSonetAlarmStatus_Type()
)
sonusSonetAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetAlarmStatus.setStatus("current")


class _SonusSonetThresholdType_Type(Integer32):
    """Custom type sonusSonetThresholdType based on Integer32"""
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("lineFarendCodingViolation15min", 25),
          ("lineFarendCodingViolation24hr", 37),
          ("lineFarendErroredSec15min", 26),
          ("lineFarendErroredSec24hr", 38),
          ("lineFarendSeverelyErroredSec15min", 27),
          ("lineFarendSeverelyErroredSec24hr", 39),
          ("lineFarendUnavailableSec15min", 28),
          ("lineFarendUnavailableSec24hr", 40),
          ("lineNearendCodingViolation15min", 5),
          ("lineNearendCodingViolation24hr", 17),
          ("lineNearendErroredSec15min", 6),
          ("lineNearendErroredSec24hr", 18),
          ("lineNearendSeverelyErroredSec15min", 7),
          ("lineNearendSeverelyErroredSec24hr", 19),
          ("lineNearendUnavailableSec15min", 8),
          ("lineNearendUnavailableSec24hr", 20),
          ("pathFarendCodingViolation15min", 29),
          ("pathFarendCodingViolation24hr", 41),
          ("pathFarendErroredSec15min", 30),
          ("pathFarendErroredSec24hr", 42),
          ("pathFarendSeverelyErroredSec15min", 31),
          ("pathFarendSeverelyErroredSec24hr", 43),
          ("pathFarendUnavailableSec15min", 32),
          ("pathFarendUnavailableSec24hr", 44),
          ("pathNearendCodingViolation15min", 9),
          ("pathNearendCodingViolation24hr", 21),
          ("pathNearendErroredSec15min", 10),
          ("pathNearendErroredSec24hr", 22),
          ("pathNearendSeverelyErroredSec15min", 11),
          ("pathNearendSeverelyErroredSec24hr", 23),
          ("pathNearendUnavailableSec15min", 12),
          ("pathNearendUnavailableSec24hr", 24),
          ("sectionFarendCodingViolation24hr", 33),
          ("sectionFarendErroredSec24hr", 34),
          ("sectionFarendSeverelyErroredFrameSec24hr", 36),
          ("sectionFarendSeverelyErroredSec24hr", 35),
          ("sectionNearendCodingViolation15min", 1),
          ("sectionNearendCodingViolation24hr", 13),
          ("sectionNearendErroredSec15min", 2),
          ("sectionNearendErroredSec24hr", 14),
          ("sectionNearendSeverelyErroredFrameSec15min", 4),
          ("sectionNearendSeverelyErroredFrameSec24hr", 16),
          ("sectionNearendSeverelyErroredSec15min", 3),
          ("sectionNearendSeverelyErroredSec24hr", 15))
    )


_SonusSonetThresholdType_Type.__name__ = "Integer32"
_SonusSonetThresholdType_Object = MibScalar
sonusSonetThresholdType = _SonusSonetThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 1, 4),
    _SonusSonetThresholdType_Type()
)
sonusSonetThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetThresholdType.setStatus("current")


class _SonusPathIndex_Type(Integer32):
    """Custom type sonusPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusPathIndex_Type.__name__ = "Integer32"
_SonusPathIndex_Object = MibScalar
sonusPathIndex = _SonusPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 1, 5),
    _SonusPathIndex_Type()
)
sonusPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPathIndex.setStatus("current")


class _SonusSonetOutOfServiceReason_Type(Integer32):
    """Custom type sonusSonetOutOfServiceReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("hwFailure", 2))
    )


_SonusSonetOutOfServiceReason_Type.__name__ = "Integer32"
_SonusSonetOutOfServiceReason_Object = MibScalar
sonusSonetOutOfServiceReason = _SonusSonetOutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 1, 6),
    _SonusSonetOutOfServiceReason_Type()
)
sonusSonetOutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSonetOutOfServiceReason.setStatus("current")

# Managed Objects groups


# Notification objects

sonusSonetPortAdminStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 1)
)
sonusSonetPortAdminStatusNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusSonetAdminStatus"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetPortAdminStatusNotification.setStatus(
        "current"
    )

sonusSonetPortOperStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 2)
)
sonusSonetPortOperStatusNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusSonetOperStatus"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetPortOperStatusNotification.setStatus(
        "obsolete"
    )

sonusSonetLineAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 3)
)
sonusSonetLineAlarmNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusSonetAlarmStatus"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetLineAlarmNotification.setStatus(
        "current"
    )

sonusSonetLineThresholdCrossNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 4)
)
sonusSonetLineThresholdCrossNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusSonetThresholdType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetLineThresholdCrossNotification.setStatus(
        "current"
    )

sonusSonetPathAdminStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 5)
)
sonusSonetPathAdminStatusNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusPathIndex"),
        ("SONUS-SONET-MIB", "sonusSonetAdminStatus"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetPathAdminStatusNotification.setStatus(
        "current"
    )

sonusSonetPathOperStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 6)
)
sonusSonetPathOperStatusNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusPathIndex"),
        ("SONUS-SONET-MIB", "sonusSonetOperStatus"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetPathOperStatusNotification.setStatus(
        "obsolete"
    )

sonusSonetPathAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 7)
)
sonusSonetPathAlarmNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusPathIndex"),
        ("SONUS-SONET-MIB", "sonusSonetAlarmStatus"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetPathAlarmNotification.setStatus(
        "current"
    )

sonusSonetPathThresholdCrossNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 8)
)
sonusSonetPathThresholdCrossNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusPathIndex"),
        ("SONUS-SONET-MIB", "sonusSonetThresholdType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetPathThresholdCrossNotification.setStatus(
        "current"
    )

sonusSonetPortOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 9)
)
sonusSonetPortOutOfServiceNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusSonetOutOfServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetPortOutOfServiceNotification.setStatus(
        "current"
    )

sonusSonetPathOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 3, 4, 0, 10)
)
sonusSonetPathOutOfServiceNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-SONET-MIB", "sonusPathIndex"),
        ("SONUS-SONET-MIB", "sonusSonetOutOfServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSonetPathOutOfServiceNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-SONET-MIB",
    **{"sonusSonetMIB": sonusSonetMIB,
       "sonusSonetObjects": sonusSonetObjects,
       "sonusSonetPortAdmn": sonusSonetPortAdmn,
       "sonusSonetPortAdmnTable": sonusSonetPortAdmnTable,
       "sonusSonetPortAdmnEntry": sonusSonetPortAdmnEntry,
       "sonusSonetPortAdmnIfIndex": sonusSonetPortAdmnIfIndex,
       "sonusSonetPortAdmnShelfIndex": sonusSonetPortAdmnShelfIndex,
       "sonusSonetPortAdmnSlotIndex": sonusSonetPortAdmnSlotIndex,
       "sonusSonetPortAdmnPortIndex": sonusSonetPortAdmnPortIndex,
       "sonusSonetPortAdmnRowStatus": sonusSonetPortAdmnRowStatus,
       "sonusSonetPortAdmnName": sonusSonetPortAdmnName,
       "sonusSonetPortAdmnState": sonusSonetPortAdmnState,
       "sonusSonetPortAdmnMode": sonusSonetPortAdmnMode,
       "sonusSonetPortAdmnAction": sonusSonetPortAdmnAction,
       "sonusSonetPortAdmnTimeout": sonusSonetPortAdmnTimeout,
       "sonusSonetPortAdmnStatAction": sonusSonetPortAdmnStatAction,
       "sonusSonetPortAdmnLaserState": sonusSonetPortAdmnLaserState,
       "sonusSonetPortAdmn24hTimeElapsed": sonusSonetPortAdmn24hTimeElapsed,
       "sonusSonetPortAdmnOperStatus": sonusSonetPortAdmnOperStatus,
       "sonusSonetPortAdmnDs3ModeOverride": sonusSonetPortAdmnDs3ModeOverride,
       "sonusSonetPortAdmnStsXmtScramble": sonusSonetPortAdmnStsXmtScramble,
       "sonusSonetPortAdmnStsRcvDescramble": sonusSonetPortAdmnStsRcvDescramble,
       "sonusSonetPortAdmnAtmXmtScramble": sonusSonetPortAdmnAtmXmtScramble,
       "sonusSonetPortAdmnAtmRcvDescramble": sonusSonetPortAdmnAtmRcvDescramble,
       "sonusSonetSection": sonusSonetSection,
       "sonusSonetSectionThresholdTable": sonusSonetSectionThresholdTable,
       "sonusSonetSectionThresholdEntry": sonusSonetSectionThresholdEntry,
       "sonusSonetSectionThresholdIfIndex": sonusSonetSectionThresholdIfIndex,
       "sonusSonetSectionThreshold15mCVs": sonusSonetSectionThreshold15mCVs,
       "sonusSonetSectionThreshold15mESs": sonusSonetSectionThreshold15mESs,
       "sonusSonetSectionThreshold15mSESs": sonusSonetSectionThreshold15mSESs,
       "sonusSonetSectionThreshold15mSEFSs": sonusSonetSectionThreshold15mSEFSs,
       "sonusSonetSectionThreshold24hCVs": sonusSonetSectionThreshold24hCVs,
       "sonusSonetSectionThreshold24hESs": sonusSonetSectionThreshold24hESs,
       "sonusSonetSectionThreshold24hSESs": sonusSonetSectionThreshold24hSESs,
       "sonusSonetSectionThreshold24hSEFSs": sonusSonetSectionThreshold24hSEFSs,
       "sonusSonetSectionCurrentTable": sonusSonetSectionCurrentTable,
       "sonusSonetSectionCurrentEntry": sonusSonetSectionCurrentEntry,
       "sonusSonetSectionCurrentIfIndex": sonusSonetSectionCurrentIfIndex,
       "sonusSonetSectionCurrentStatus": sonusSonetSectionCurrentStatus,
       "sonusSonetSectionCurrentESs": sonusSonetSectionCurrentESs,
       "sonusSonetSectionCurrentSESs": sonusSonetSectionCurrentSESs,
       "sonusSonetSectionCurrentSEFSs": sonusSonetSectionCurrentSEFSs,
       "sonusSonetSectionCurrentCVs": sonusSonetSectionCurrentCVs,
       "sonusSonetSectionIntervalTable": sonusSonetSectionIntervalTable,
       "sonusSonetSectionIntervalEntry": sonusSonetSectionIntervalEntry,
       "sonusSonetSectionIntervalIfIndex": sonusSonetSectionIntervalIfIndex,
       "sonusSonetSectionIntervalNumber": sonusSonetSectionIntervalNumber,
       "sonusSonetSectionIntervalESs": sonusSonetSectionIntervalESs,
       "sonusSonetSectionIntervalSESs": sonusSonetSectionIntervalSESs,
       "sonusSonetSectionIntervalSEFSs": sonusSonetSectionIntervalSEFSs,
       "sonusSonetSectionIntervalCVs": sonusSonetSectionIntervalCVs,
       "sonusSonetSectionIntervalValidData": sonusSonetSectionIntervalValidData,
       "sonusSonetLine": sonusSonetLine,
       "sonusSonetLineThresholdTable": sonusSonetLineThresholdTable,
       "sonusSonetLineThresholdEntry": sonusSonetLineThresholdEntry,
       "sonusSonetLineThresholdIfIndex": sonusSonetLineThresholdIfIndex,
       "sonusSonetLineThreshold15mCVs": sonusSonetLineThreshold15mCVs,
       "sonusSonetLineThreshold15mESs": sonusSonetLineThreshold15mESs,
       "sonusSonetLineThreshold15mSESs": sonusSonetLineThreshold15mSESs,
       "sonusSonetLineThreshold15mUASs": sonusSonetLineThreshold15mUASs,
       "sonusSonetLineThreshold24hCVs": sonusSonetLineThreshold24hCVs,
       "sonusSonetLineThreshold24hESs": sonusSonetLineThreshold24hESs,
       "sonusSonetLineThreshold24hSESs": sonusSonetLineThreshold24hSESs,
       "sonusSonetLineThreshold24hUASs": sonusSonetLineThreshold24hUASs,
       "sonusSonetLineCurrentTable": sonusSonetLineCurrentTable,
       "sonusSonetLineCurrentEntry": sonusSonetLineCurrentEntry,
       "sonusSonetLineCurrentIfIndex": sonusSonetLineCurrentIfIndex,
       "sonusSonetLineCurrentStatus": sonusSonetLineCurrentStatus,
       "sonusSonetLineCurrentESs": sonusSonetLineCurrentESs,
       "sonusSonetLineCurrentSESs": sonusSonetLineCurrentSESs,
       "sonusSonetLineCurrentUASs": sonusSonetLineCurrentUASs,
       "sonusSonetLineCurrentCVs": sonusSonetLineCurrentCVs,
       "sonusSonetLineCurrentFCs": sonusSonetLineCurrentFCs,
       "sonusSonetLineIntervalTable": sonusSonetLineIntervalTable,
       "sonusSonetLineIntervalEntry": sonusSonetLineIntervalEntry,
       "sonusSonetLineIntervalIfIndex": sonusSonetLineIntervalIfIndex,
       "sonusSonetLineIntervalNumber": sonusSonetLineIntervalNumber,
       "sonusSonetLineIntervalESs": sonusSonetLineIntervalESs,
       "sonusSonetLineIntervalSESs": sonusSonetLineIntervalSESs,
       "sonusSonetLineIntervalUASs": sonusSonetLineIntervalUASs,
       "sonusSonetLineIntervalCVs": sonusSonetLineIntervalCVs,
       "sonusSonetLineIntervalFCs": sonusSonetLineIntervalFCs,
       "sonusSonetLineIntervalValidData": sonusSonetLineIntervalValidData,
       "sonusSonetFarEndLineCurrentTable": sonusSonetFarEndLineCurrentTable,
       "sonusSonetFarEndLineCurrentEntry": sonusSonetFarEndLineCurrentEntry,
       "sonusSonetFarEndLineCurrentIfIndex": sonusSonetFarEndLineCurrentIfIndex,
       "sonusSonetFarEndLineCurrentESs": sonusSonetFarEndLineCurrentESs,
       "sonusSonetFarEndLineCurrentSESs": sonusSonetFarEndLineCurrentSESs,
       "sonusSonetFarEndLineCurrentUASs": sonusSonetFarEndLineCurrentUASs,
       "sonusSonetFarEndLineCurrentCVs": sonusSonetFarEndLineCurrentCVs,
       "sonusSonetFarEndLineCurrentFCs": sonusSonetFarEndLineCurrentFCs,
       "sonusSonetFarEndLineIntervalTable": sonusSonetFarEndLineIntervalTable,
       "sonusSonetFarEndLineIntervalEntry": sonusSonetFarEndLineIntervalEntry,
       "sonusSonetFarEndLineIntervalIfIndex": sonusSonetFarEndLineIntervalIfIndex,
       "sonusSonetFarEndLineIntervalNumber": sonusSonetFarEndLineIntervalNumber,
       "sonusSonetFarEndLineIntervalESs": sonusSonetFarEndLineIntervalESs,
       "sonusSonetFarEndLineIntervalSESs": sonusSonetFarEndLineIntervalSESs,
       "sonusSonetFarEndLineIntervalUASs": sonusSonetFarEndLineIntervalUASs,
       "sonusSonetFarEndLineIntervalCVs": sonusSonetFarEndLineIntervalCVs,
       "sonusSonetFarEndLineIntervalFCs": sonusSonetFarEndLineIntervalFCs,
       "sonusSonetFarEndLineIntervalValidData": sonusSonetFarEndLineIntervalValidData,
       "sonusSonetLineFailureCurrentTable": sonusSonetLineFailureCurrentTable,
       "sonusSonetLineFailureCurrentEntry": sonusSonetLineFailureCurrentEntry,
       "sonusSonetLineFailureCurrentIfIndex": sonusSonetLineFailureCurrentIfIndex,
       "sonusSonetLineFailureCurrentFCs": sonusSonetLineFailureCurrentFCs,
       "sonusSonetLineFailureIntervalTable": sonusSonetLineFailureIntervalTable,
       "sonusSonetLineFailureIntervalEntry": sonusSonetLineFailureIntervalEntry,
       "sonusSonetLineFailureIntervalIfIndex": sonusSonetLineFailureIntervalIfIndex,
       "sonusSonetLineFailureIntervalNumber": sonusSonetLineFailureIntervalNumber,
       "sonusSonetLineFailureIntervalFCs": sonusSonetLineFailureIntervalFCs,
       "sonusSonetFarEndLineFailureCurrentTable": sonusSonetFarEndLineFailureCurrentTable,
       "sonusSonetFarEndLineFailureCurrentEntry": sonusSonetFarEndLineFailureCurrentEntry,
       "sonusSonetFarEndLineFailureCurrentIfIndex": sonusSonetFarEndLineFailureCurrentIfIndex,
       "sonusSonetFarEndLineFailureCurrentFCs": sonusSonetFarEndLineFailureCurrentFCs,
       "sonusSonetFarEndLineFailureIntervalTable": sonusSonetFarEndLineFailureIntervalTable,
       "sonusSonetFarEndLineFailureIntervalEntry": sonusSonetFarEndLineFailureIntervalEntry,
       "sonusSonetFarEndLineFailureIntervalIfIndex": sonusSonetFarEndLineFailureIntervalIfIndex,
       "sonusSonetFarEndLineFailureIntervalNumber": sonusSonetFarEndLineFailureIntervalNumber,
       "sonusSonetFarEndLineFailureIntervalFCs": sonusSonetFarEndLineFailureIntervalFCs,
       "sonusSonetLayer": sonusSonetLayer,
       "sonusSonetLayerTable": sonusSonetLayerTable,
       "sonusSonetLayerEntry": sonusSonetLayerEntry,
       "sonusSonetLayerShelfIndex": sonusSonetLayerShelfIndex,
       "sonusSonetLayerSlotIndex": sonusSonetLayerSlotIndex,
       "sonusSonetLayerPortIndex": sonusSonetLayerPortIndex,
       "sonusSonetLayerIfIndex": sonusSonetLayerIfIndex,
       "sonusSonetLayerRowStatus": sonusSonetLayerRowStatus,
       "sonusSonetObjectsPath": sonusSonetObjectsPath,
       "sonusSonetPathAdmn": sonusSonetPathAdmn,
       "sonusSonetPathAdmnTable": sonusSonetPathAdmnTable,
       "sonusSonetPathAdmnEntry": sonusSonetPathAdmnEntry,
       "sonusSonetPathAdmnIfIndex": sonusSonetPathAdmnIfIndex,
       "sonusSonetPathAdmnShelfIndex": sonusSonetPathAdmnShelfIndex,
       "sonusSonetPathAdmnSlotIndex": sonusSonetPathAdmnSlotIndex,
       "sonusSonetPathAdmnPortIndex": sonusSonetPathAdmnPortIndex,
       "sonusSonetPathAdmnPathIndex": sonusSonetPathAdmnPathIndex,
       "sonusSonetPathAdmnRowStatus": sonusSonetPathAdmnRowStatus,
       "sonusSonetPathAdmnState": sonusSonetPathAdmnState,
       "sonusSonetPathAdmnMode": sonusSonetPathAdmnMode,
       "sonusSonetPathAdmnAction": sonusSonetPathAdmnAction,
       "sonusSonetPathAdmnTimeout": sonusSonetPathAdmnTimeout,
       "sonusSonetPathAdmnStatAction": sonusSonetPathAdmnStatAction,
       "sonusSonetPathAdmnRDIMode": sonusSonetPathAdmnRDIMode,
       "sonusSonetPathAdmnTraceState": sonusSonetPathAdmnTraceState,
       "sonusSonetPathAdmnTraceExpMsg": sonusSonetPathAdmnTraceExpMsg,
       "sonusSonetPathAdmnTraceXmtMsg": sonusSonetPathAdmnTraceXmtMsg,
       "sonusSonetPathAdmnTraceRcvMsg": sonusSonetPathAdmnTraceRcvMsg,
       "sonusSonetPathAdmnOperStatus": sonusSonetPathAdmnOperStatus,
       "sonusSonetPathAdmnDs3ModeOverride": sonusSonetPathAdmnDs3ModeOverride,
       "sonusSonetPath": sonusSonetPath,
       "sonusSonetPathThresholdTable": sonusSonetPathThresholdTable,
       "sonusSonetPathThresholdEntry": sonusSonetPathThresholdEntry,
       "sonusSonetPathThresholdIfIndex": sonusSonetPathThresholdIfIndex,
       "sonusSonetPathThresholdPathIndex": sonusSonetPathThresholdPathIndex,
       "sonusSonetPathThreshold15mCVs": sonusSonetPathThreshold15mCVs,
       "sonusSonetPathThreshold15mESs": sonusSonetPathThreshold15mESs,
       "sonusSonetPathThreshold15mSESs": sonusSonetPathThreshold15mSESs,
       "sonusSonetPathThreshold15mUASs": sonusSonetPathThreshold15mUASs,
       "sonusSonetPathThreshold24hCVs": sonusSonetPathThreshold24hCVs,
       "sonusSonetPathThreshold24hESs": sonusSonetPathThreshold24hESs,
       "sonusSonetPathThreshold24hSESs": sonusSonetPathThreshold24hSESs,
       "sonusSonetPathThreshold24hUASs": sonusSonetPathThreshold24hUASs,
       "sonusSonetPathCurrentTable": sonusSonetPathCurrentTable,
       "sonusSonetPathCurrentEntry": sonusSonetPathCurrentEntry,
       "sonusSonetPathCurrentIfIndex": sonusSonetPathCurrentIfIndex,
       "sonusSonetPathCurrentPathIndex": sonusSonetPathCurrentPathIndex,
       "sonusSonetPathCurrentWidth": sonusSonetPathCurrentWidth,
       "sonusSonetPathCurrentStatus": sonusSonetPathCurrentStatus,
       "sonusSonetPathCurrentESs": sonusSonetPathCurrentESs,
       "sonusSonetPathCurrentSESs": sonusSonetPathCurrentSESs,
       "sonusSonetPathCurrentUASs": sonusSonetPathCurrentUASs,
       "sonusSonetPathCurrentCVs": sonusSonetPathCurrentCVs,
       "sonusSonetPathCurrentFCs": sonusSonetPathCurrentFCs,
       "sonusSonetPathCurrentTraceStatus": sonusSonetPathCurrentTraceStatus,
       "sonusSonetPathIntervalTable": sonusSonetPathIntervalTable,
       "sonusSonetPathIntervalEntry": sonusSonetPathIntervalEntry,
       "sonusSonetPathIntervalIfIndex": sonusSonetPathIntervalIfIndex,
       "sonusSonetPathIntervalPathIndex": sonusSonetPathIntervalPathIndex,
       "sonusSonetPathIntervalNumber": sonusSonetPathIntervalNumber,
       "sonusSonetPathIntervalESs": sonusSonetPathIntervalESs,
       "sonusSonetPathIntervalSESs": sonusSonetPathIntervalSESs,
       "sonusSonetPathIntervalUASs": sonusSonetPathIntervalUASs,
       "sonusSonetPathIntervalCVs": sonusSonetPathIntervalCVs,
       "sonusSonetPathIntervalFCs": sonusSonetPathIntervalFCs,
       "sonusSonetPathIntervalValidData": sonusSonetPathIntervalValidData,
       "sonusSonetFarEndPathCurrentTable": sonusSonetFarEndPathCurrentTable,
       "sonusSonetFarEndPathCurrentEntry": sonusSonetFarEndPathCurrentEntry,
       "sonusSonetFarEndPathCurrentIfIndex": sonusSonetFarEndPathCurrentIfIndex,
       "sonusSonetFarEndPathCurrentPathIndex": sonusSonetFarEndPathCurrentPathIndex,
       "sonusSonetFarEndPathCurrentESs": sonusSonetFarEndPathCurrentESs,
       "sonusSonetFarEndPathCurrentSESs": sonusSonetFarEndPathCurrentSESs,
       "sonusSonetFarEndPathCurrentUASs": sonusSonetFarEndPathCurrentUASs,
       "sonusSonetFarEndPathCurrentCVs": sonusSonetFarEndPathCurrentCVs,
       "sonusSonetFarEndPathCurrentFCs": sonusSonetFarEndPathCurrentFCs,
       "sonusSonetFarEndPathIntervalTable": sonusSonetFarEndPathIntervalTable,
       "sonusSonetFarEndPathIntervalEntry": sonusSonetFarEndPathIntervalEntry,
       "sonusSonetFarEndPathIntervalIfIndex": sonusSonetFarEndPathIntervalIfIndex,
       "sonusSonetFarEndPathIntervalPathIndex": sonusSonetFarEndPathIntervalPathIndex,
       "sonusSonetFarEndPathIntervalNumber": sonusSonetFarEndPathIntervalNumber,
       "sonusSonetFarEndPathIntervalESs": sonusSonetFarEndPathIntervalESs,
       "sonusSonetFarEndPathIntervalSESs": sonusSonetFarEndPathIntervalSESs,
       "sonusSonetFarEndPathIntervalUASs": sonusSonetFarEndPathIntervalUASs,
       "sonusSonetFarEndPathIntervalCVs": sonusSonetFarEndPathIntervalCVs,
       "sonusSonetFarEndPathIntervalFCs": sonusSonetFarEndPathIntervalFCs,
       "sonusSonetFarEndPathIntervalValidData": sonusSonetFarEndPathIntervalValidData,
       "sonusSonetPathFailureCurrentTable": sonusSonetPathFailureCurrentTable,
       "sonusSonetPathFailureCurrentEntry": sonusSonetPathFailureCurrentEntry,
       "sonusSonetPathFailureCurrentIfIndex": sonusSonetPathFailureCurrentIfIndex,
       "sonusSonetPathFailureCurrentPathIndex": sonusSonetPathFailureCurrentPathIndex,
       "sonusSonetPathFailureCurrentFCs": sonusSonetPathFailureCurrentFCs,
       "sonusSonetPathFailureCurrentTraceStatus": sonusSonetPathFailureCurrentTraceStatus,
       "sonusSonetPathFailureIntervalTable": sonusSonetPathFailureIntervalTable,
       "sonusSonetPathFailureIntervalEntry": sonusSonetPathFailureIntervalEntry,
       "sonusSonetPathFailureIntervalIfIndex": sonusSonetPathFailureIntervalIfIndex,
       "sonusSonetPathFailureIntervalPathIndex": sonusSonetPathFailureIntervalPathIndex,
       "sonusSonetPathFailureIntervalNumber": sonusSonetPathFailureIntervalNumber,
       "sonusSonetPathFailureIntervalFCs": sonusSonetPathFailureIntervalFCs,
       "sonusSonetFarEndPathFailureCurrentTable": sonusSonetFarEndPathFailureCurrentTable,
       "sonusSonetFarEndPathFailureCurrentEntry": sonusSonetFarEndPathFailureCurrentEntry,
       "sonusSonetFarEndPathFailureCurrentIfIndex": sonusSonetFarEndPathFailureCurrentIfIndex,
       "sonusSonetFarEndPathFailureCurrentPathIndex": sonusSonetFarEndPathFailureCurrentPathIndex,
       "sonusSonetFarEndPathFailureCurrentFCs": sonusSonetFarEndPathFailureCurrentFCs,
       "sonusSonetFarEndPathFailureIntervalTable": sonusSonetFarEndPathFailureIntervalTable,
       "sonusSonetFarEndPathFailureIntervalEntry": sonusSonetFarEndPathFailureIntervalEntry,
       "sonusSonetFarEndPathFailureIntervalIfIndex": sonusSonetFarEndPathFailureIntervalIfIndex,
       "sonusSonetFarEndPathFailureIntervalPathIndex": sonusSonetFarEndPathFailureIntervalPathIndex,
       "sonusSonetFarEndPathFailureIntervalNumber": sonusSonetFarEndPathFailureIntervalNumber,
       "sonusSonetFarEndPathFailureIntervalFCs": sonusSonetFarEndPathFailureIntervalFCs,
       "sonusSonetNextIndex": sonusSonetNextIndex,
       "sonusSonetMIBNotifications": sonusSonetMIBNotifications,
       "sonusSonetMIBNotificationsPrefix": sonusSonetMIBNotificationsPrefix,
       "sonusSonetPortAdminStatusNotification": sonusSonetPortAdminStatusNotification,
       "sonusSonetPortOperStatusNotification": sonusSonetPortOperStatusNotification,
       "sonusSonetLineAlarmNotification": sonusSonetLineAlarmNotification,
       "sonusSonetLineThresholdCrossNotification": sonusSonetLineThresholdCrossNotification,
       "sonusSonetPathAdminStatusNotification": sonusSonetPathAdminStatusNotification,
       "sonusSonetPathOperStatusNotification": sonusSonetPathOperStatusNotification,
       "sonusSonetPathAlarmNotification": sonusSonetPathAlarmNotification,
       "sonusSonetPathThresholdCrossNotification": sonusSonetPathThresholdCrossNotification,
       "sonusSonetPortOutOfServiceNotification": sonusSonetPortOutOfServiceNotification,
       "sonusSonetPathOutOfServiceNotification": sonusSonetPathOutOfServiceNotification,
       "sonusSonetMIBNotificationsObjects": sonusSonetMIBNotificationsObjects,
       "sonusSonetAdminStatus": sonusSonetAdminStatus,
       "sonusSonetOperStatus": sonusSonetOperStatus,
       "sonusSonetAlarmStatus": sonusSonetAlarmStatus,
       "sonusSonetThresholdType": sonusSonetThresholdType,
       "sonusPathIndex": sonusPathIndex,
       "sonusSonetOutOfServiceReason": sonusSonetOutOfServiceReason}
)
