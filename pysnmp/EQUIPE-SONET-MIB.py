# SNMP MIB module (EQUIPE-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQUIPE-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:18 2024
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

eqSonetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EqSonetApsCfgStatus(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("forcedSwitchProtectingToWorking", 6),
          ("forcedSwitchWorkingToProtecting", 5),
          ("lockoutProtecting", 4),
          ("manualSwitchProtectingToWorking", 8),
          ("manualSwitchWorkingToProtecting", 7),
          ("none", 1),
          ("protecting", 3),
          ("working", 2))
    )



class EqSonetApsCfgAction(Integer32, TextualConvention):
    status = "current"
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
        *(("clear", 2),
          ("forcedSwitchProtectingToWorking", 5),
          ("forcedSwitchWorkingToProtecting", 4),
          ("lockoutProtecting", 3),
          ("manualSwitchProtectingToWorking", 7),
          ("manualSwitchWorkingToProtecting", 6),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Equipe_ObjectIdentity = ObjectIdentity
equipe = _Equipe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022)
)
_EqSonetApsCfgTable_Object = MibTable
eqSonetApsCfgTable = _EqSonetApsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 1)
)
if mibBuilder.loadTexts:
    eqSonetApsCfgTable.setStatus("current")
_EqSonetApsCfgEntry_Object = MibTableRow
eqSonetApsCfgEntry = _EqSonetApsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 1, 1)
)
eqSonetApsCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eqSonetApsCfgEntry.setStatus("current")
_EqSonetApsCfgStatus_Type = EqSonetApsCfgStatus
_EqSonetApsCfgStatus_Object = MibTableColumn
eqSonetApsCfgStatus = _EqSonetApsCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 1, 1, 1),
    _EqSonetApsCfgStatus_Type()
)
eqSonetApsCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetApsCfgStatus.setStatus("current")
_EqSonetApsCfgAction_Type = EqSonetApsCfgAction
_EqSonetApsCfgAction_Object = MibTableColumn
eqSonetApsCfgAction = _EqSonetApsCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 1, 1, 2),
    _EqSonetApsCfgAction_Type()
)
eqSonetApsCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqSonetApsCfgAction.setStatus("current")
_EqSonetApsCfgLastAction_Type = EqSonetApsCfgAction
_EqSonetApsCfgLastAction_Object = MibTableColumn
eqSonetApsCfgLastAction = _EqSonetApsCfgLastAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 1, 1, 3),
    _EqSonetApsCfgLastAction_Type()
)
eqSonetApsCfgLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetApsCfgLastAction.setStatus("current")


class _EqSonetApsCfgPortActive_Type(Integer32):
    """Custom type eqSonetApsCfgPortActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_EqSonetApsCfgPortActive_Type.__name__ = "Integer32"
_EqSonetApsCfgPortActive_Object = MibTableColumn
eqSonetApsCfgPortActive = _EqSonetApsCfgPortActive_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 1, 1, 4),
    _EqSonetApsCfgPortActive_Type()
)
eqSonetApsCfgPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetApsCfgPortActive.setStatus("current")
_EqSonetPathTable_Object = MibTable
eqSonetPathTable = _EqSonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 2)
)
if mibBuilder.loadTexts:
    eqSonetPathTable.setStatus("current")
_EqSonetPathEntry_Object = MibTableRow
eqSonetPathEntry = _EqSonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 2, 1)
)
eqSonetPathEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eqSonetPathEntry.setStatus("current")


class _EqSonetPathActualPort_Type(Integer32):
    """Custom type eqSonetPathActualPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqSonetPathActualPort_Type.__name__ = "Integer32"
_EqSonetPathActualPort_Object = MibTableColumn
eqSonetPathActualPort = _EqSonetPathActualPort_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 2, 1, 1),
    _EqSonetPathActualPort_Type()
)
eqSonetPathActualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetPathActualPort.setStatus("current")
_EqSonetStatsTable_Object = MibTable
eqSonetStatsTable = _EqSonetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3)
)
if mibBuilder.loadTexts:
    eqSonetStatsTable.setStatus("current")
_EqSonetStatsEntry_Object = MibTableRow
eqSonetStatsEntry = _EqSonetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3, 1)
)
eqSonetStatsEntry.setIndexNames(
    (0, "EQUIPE-SONET-MIB", "eqSonetStatsIfIndex"),
)
if mibBuilder.loadTexts:
    eqSonetStatsEntry.setStatus("current")


class _EqSonetStatsIfIndex_Type(Integer32):
    """Custom type eqSonetStatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqSonetStatsIfIndex_Type.__name__ = "Integer32"
_EqSonetStatsIfIndex_Object = MibTableColumn
eqSonetStatsIfIndex = _EqSonetStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3, 1, 1),
    _EqSonetStatsIfIndex_Type()
)
eqSonetStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetStatsIfIndex.setStatus("current")
_EqSonetStatsLineFailures_Type = Counter32
_EqSonetStatsLineFailures_Object = MibTableColumn
eqSonetStatsLineFailures = _EqSonetStatsLineFailures_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3, 1, 2),
    _EqSonetStatsLineFailures_Type()
)
eqSonetStatsLineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetStatsLineFailures.setStatus("current")
_EqSonetStatsLineApsCount_Type = Counter32
_EqSonetStatsLineApsCount_Object = MibTableColumn
eqSonetStatsLineApsCount = _EqSonetStatsLineApsCount_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3, 1, 3),
    _EqSonetStatsLineApsCount_Type()
)
eqSonetStatsLineApsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetStatsLineApsCount.setStatus("current")
_EqSonetStatsLineApsSwitchDuration_Type = Counter32
_EqSonetStatsLineApsSwitchDuration_Object = MibTableColumn
eqSonetStatsLineApsSwitchDuration = _EqSonetStatsLineApsSwitchDuration_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3, 1, 4),
    _EqSonetStatsLineApsSwitchDuration_Type()
)
eqSonetStatsLineApsSwitchDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetStatsLineApsSwitchDuration.setStatus("current")
_EqSonetStatsLineStsPtrAdjustments_Type = Counter32
_EqSonetStatsLineStsPtrAdjustments_Object = MibTableColumn
eqSonetStatsLineStsPtrAdjustments = _EqSonetStatsLineStsPtrAdjustments_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3, 1, 5),
    _EqSonetStatsLineStsPtrAdjustments_Type()
)
eqSonetStatsLineStsPtrAdjustments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetStatsLineStsPtrAdjustments.setStatus("current")
_EqSonetStatsPathFailures_Type = Counter32
_EqSonetStatsPathFailures_Object = MibTableColumn
eqSonetStatsPathFailures = _EqSonetStatsPathFailures_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3, 1, 6),
    _EqSonetStatsPathFailures_Type()
)
eqSonetStatsPathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetStatsPathFailures.setStatus("current")


class _EqSonetStatsTimeElapsed_Type(Integer32):
    """Custom type eqSonetStatsTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_EqSonetStatsTimeElapsed_Type.__name__ = "Integer32"
_EqSonetStatsTimeElapsed_Object = MibTableColumn
eqSonetStatsTimeElapsed = _EqSonetStatsTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5022, 3, 3, 1, 7),
    _EqSonetStatsTimeElapsed_Type()
)
eqSonetStatsTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSonetStatsTimeElapsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQUIPE-SONET-MIB",
    **{"EqSonetApsCfgStatus": EqSonetApsCfgStatus,
       "EqSonetApsCfgAction": EqSonetApsCfgAction,
       "equipe": equipe,
       "eqSonetMib": eqSonetMib,
       "eqSonetApsCfgTable": eqSonetApsCfgTable,
       "eqSonetApsCfgEntry": eqSonetApsCfgEntry,
       "eqSonetApsCfgStatus": eqSonetApsCfgStatus,
       "eqSonetApsCfgAction": eqSonetApsCfgAction,
       "eqSonetApsCfgLastAction": eqSonetApsCfgLastAction,
       "eqSonetApsCfgPortActive": eqSonetApsCfgPortActive,
       "eqSonetPathTable": eqSonetPathTable,
       "eqSonetPathEntry": eqSonetPathEntry,
       "eqSonetPathActualPort": eqSonetPathActualPort,
       "eqSonetStatsTable": eqSonetStatsTable,
       "eqSonetStatsEntry": eqSonetStatsEntry,
       "eqSonetStatsIfIndex": eqSonetStatsIfIndex,
       "eqSonetStatsLineFailures": eqSonetStatsLineFailures,
       "eqSonetStatsLineApsCount": eqSonetStatsLineApsCount,
       "eqSonetStatsLineApsSwitchDuration": eqSonetStatsLineApsSwitchDuration,
       "eqSonetStatsLineStsPtrAdjustments": eqSonetStatsLineStsPtrAdjustments,
       "eqSonetStatsPathFailures": eqSonetStatsPathFailures,
       "eqSonetStatsTimeElapsed": eqSonetStatsTimeElapsed}
)
