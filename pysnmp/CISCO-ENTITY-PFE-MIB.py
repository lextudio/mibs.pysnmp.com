# SNMP MIB module (CISCO-ENTITY-PFE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-PFE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:39 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoEntityPfeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 265)
)
ciscoEntityPfeMib.setRevisions(
        ("2002-11-27 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CurrentUtilization(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class CurrentEfficiency(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class IntervalUtilization(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class IntervalEfficiency(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TotalUtilization(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TotalEfficiency(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class Percentage(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class EventType(Integer32, TextualConvention):
    status = "current"
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
        *(("log", 2),
          ("logAndNotify", 4),
          ("none", 1),
          ("notify", 3))
    )



class HistEventType(Integer32, TextualConvention):
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
        *(("restartEvent", 7),
          ("thld1MinEfficiencyEvent", 4),
          ("thld1MinUtilizationEvent", 3),
          ("thld5MinEfficiencyEvent", 6),
          ("thld5MinUtilizationEvent", 5),
          ("thldEfficiencyEvent", 2),
          ("thldUtilizationEvent", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CePfeMIBNotifications_ObjectIdentity = ObjectIdentity
cePfeMIBNotifications = _CePfeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 0)
)
_CePfeMIBObjects_ObjectIdentity = ObjectIdentity
cePfeMIBObjects = _CePfeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1)
)
_CePfePerformance_ObjectIdentity = ObjectIdentity
cePfePerformance = _CePfePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1)
)
_CePfePerfConfigTable_Object = MibTable
cePfePerfConfigTable = _CePfePerfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cePfePerfConfigTable.setStatus("current")
_CePfePerfConfigEntry_Object = MibTableRow
cePfePerfConfigEntry = _CePfePerfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1)
)
cePfePerfConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cePfePerfConfigEntry.setStatus("current")


class _CePfePerfConfigTimeElapsed_Type(Unsigned32):
    """Custom type cePfePerfConfigTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CePfePerfConfigTimeElapsed_Type.__name__ = "Unsigned32"
_CePfePerfConfigTimeElapsed_Object = MibTableColumn
cePfePerfConfigTimeElapsed = _CePfePerfConfigTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 1),
    _CePfePerfConfigTimeElapsed_Type()
)
cePfePerfConfigTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfConfigTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    cePfePerfConfigTimeElapsed.setUnits("seconds")


class _CePfePerfConfigValidIntervals_Type(Unsigned32):
    """Custom type cePfePerfConfigValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CePfePerfConfigValidIntervals_Type.__name__ = "Unsigned32"
_CePfePerfConfigValidIntervals_Object = MibTableColumn
cePfePerfConfigValidIntervals = _CePfePerfConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 2),
    _CePfePerfConfigValidIntervals_Type()
)
cePfePerfConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfConfigValidIntervals.setStatus("current")


class _CePfePerfConfigThldUtilization_Type(Percentage):
    """Custom type cePfePerfConfigThldUtilization based on Percentage"""
    defaultValue = 0


_CePfePerfConfigThldUtilization_Object = MibTableColumn
cePfePerfConfigThldUtilization = _CePfePerfConfigThldUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 3),
    _CePfePerfConfigThldUtilization_Type()
)
cePfePerfConfigThldUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cePfePerfConfigThldUtilization.setStatus("current")


class _CePfePerfConfigThldEfficiency_Type(Percentage):
    """Custom type cePfePerfConfigThldEfficiency based on Percentage"""
    defaultValue = 0


_CePfePerfConfigThldEfficiency_Object = MibTableColumn
cePfePerfConfigThldEfficiency = _CePfePerfConfigThldEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 4),
    _CePfePerfConfigThldEfficiency_Type()
)
cePfePerfConfigThldEfficiency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cePfePerfConfigThldEfficiency.setStatus("current")


class _CePfePerfConfigThld1MinUtilization_Type(Percentage):
    """Custom type cePfePerfConfigThld1MinUtilization based on Percentage"""
    defaultValue = 0


_CePfePerfConfigThld1MinUtilization_Object = MibTableColumn
cePfePerfConfigThld1MinUtilization = _CePfePerfConfigThld1MinUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 5),
    _CePfePerfConfigThld1MinUtilization_Type()
)
cePfePerfConfigThld1MinUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cePfePerfConfigThld1MinUtilization.setStatus("current")


class _CePfePerfConfigThld1MinEfficiency_Type(Percentage):
    """Custom type cePfePerfConfigThld1MinEfficiency based on Percentage"""
    defaultValue = 0


_CePfePerfConfigThld1MinEfficiency_Object = MibTableColumn
cePfePerfConfigThld1MinEfficiency = _CePfePerfConfigThld1MinEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 6),
    _CePfePerfConfigThld1MinEfficiency_Type()
)
cePfePerfConfigThld1MinEfficiency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cePfePerfConfigThld1MinEfficiency.setStatus("current")


class _CePfePerfConfigThld5MinUtilization_Type(Percentage):
    """Custom type cePfePerfConfigThld5MinUtilization based on Percentage"""
    defaultValue = 0


_CePfePerfConfigThld5MinUtilization_Object = MibTableColumn
cePfePerfConfigThld5MinUtilization = _CePfePerfConfigThld5MinUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 7),
    _CePfePerfConfigThld5MinUtilization_Type()
)
cePfePerfConfigThld5MinUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cePfePerfConfigThld5MinUtilization.setStatus("current")


class _CePfePerfConfigThld5MinEfficiency_Type(Percentage):
    """Custom type cePfePerfConfigThld5MinEfficiency based on Percentage"""
    defaultValue = 0


_CePfePerfConfigThld5MinEfficiency_Object = MibTableColumn
cePfePerfConfigThld5MinEfficiency = _CePfePerfConfigThld5MinEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 8),
    _CePfePerfConfigThld5MinEfficiency_Type()
)
cePfePerfConfigThld5MinEfficiency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cePfePerfConfigThld5MinEfficiency.setStatus("current")
_CePfePerfCurrentTable_Object = MibTable
cePfePerfCurrentTable = _CePfePerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cePfePerfCurrentTable.setStatus("current")
_CePfePerfCurrentEntry_Object = MibTableRow
cePfePerfCurrentEntry = _CePfePerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cePfePerfCurrentEntry.setStatus("current")
_CePfePerfCurrentUtilization_Type = CurrentUtilization
_CePfePerfCurrentUtilization_Object = MibTableColumn
cePfePerfCurrentUtilization = _CePfePerfCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 1),
    _CePfePerfCurrentUtilization_Type()
)
cePfePerfCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfCurrentUtilization.setStatus("current")
_CePfePerfCurrentEfficiency_Type = CurrentEfficiency
_CePfePerfCurrentEfficiency_Object = MibTableColumn
cePfePerfCurrentEfficiency = _CePfePerfCurrentEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 2),
    _CePfePerfCurrentEfficiency_Type()
)
cePfePerfCurrentEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfCurrentEfficiency.setStatus("current")
_CePfePerfCurrent1MinUtilization_Type = CurrentUtilization
_CePfePerfCurrent1MinUtilization_Object = MibTableColumn
cePfePerfCurrent1MinUtilization = _CePfePerfCurrent1MinUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 3),
    _CePfePerfCurrent1MinUtilization_Type()
)
cePfePerfCurrent1MinUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfCurrent1MinUtilization.setStatus("current")
_CePfePerfCurrent1MinEfficiency_Type = CurrentEfficiency
_CePfePerfCurrent1MinEfficiency_Object = MibTableColumn
cePfePerfCurrent1MinEfficiency = _CePfePerfCurrent1MinEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 4),
    _CePfePerfCurrent1MinEfficiency_Type()
)
cePfePerfCurrent1MinEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfCurrent1MinEfficiency.setStatus("current")
_CePfePerfCurrent5MinUtilization_Type = CurrentUtilization
_CePfePerfCurrent5MinUtilization_Object = MibTableColumn
cePfePerfCurrent5MinUtilization = _CePfePerfCurrent5MinUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 5),
    _CePfePerfCurrent5MinUtilization_Type()
)
cePfePerfCurrent5MinUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfCurrent5MinUtilization.setStatus("current")
_CePfePerfCurrent5MinEfficiency_Type = CurrentEfficiency
_CePfePerfCurrent5MinEfficiency_Object = MibTableColumn
cePfePerfCurrent5MinEfficiency = _CePfePerfCurrent5MinEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 6),
    _CePfePerfCurrent5MinEfficiency_Type()
)
cePfePerfCurrent5MinEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfCurrent5MinEfficiency.setStatus("current")
_CePfePerfIntervalTable_Object = MibTable
cePfePerfIntervalTable = _CePfePerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cePfePerfIntervalTable.setStatus("current")
_CePfePerfIntervalEntry_Object = MibTableRow
cePfePerfIntervalEntry = _CePfePerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1)
)
cePfePerfIntervalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    cePfePerfIntervalEntry.setStatus("current")


class _CePfePerfIntervalNumber_Type(Unsigned32):
    """Custom type cePfePerfIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CePfePerfIntervalNumber_Type.__name__ = "Unsigned32"
_CePfePerfIntervalNumber_Object = MibTableColumn
cePfePerfIntervalNumber = _CePfePerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 1),
    _CePfePerfIntervalNumber_Type()
)
cePfePerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cePfePerfIntervalNumber.setStatus("current")
_CePfePerfIntervalUtilization_Type = IntervalUtilization
_CePfePerfIntervalUtilization_Object = MibTableColumn
cePfePerfIntervalUtilization = _CePfePerfIntervalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 2),
    _CePfePerfIntervalUtilization_Type()
)
cePfePerfIntervalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfIntervalUtilization.setStatus("current")
_CePfePerfIntervalEfficiency_Type = IntervalEfficiency
_CePfePerfIntervalEfficiency_Object = MibTableColumn
cePfePerfIntervalEfficiency = _CePfePerfIntervalEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 3),
    _CePfePerfIntervalEfficiency_Type()
)
cePfePerfIntervalEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfIntervalEfficiency.setStatus("current")
_CePfePerfTotalTable_Object = MibTable
cePfePerfTotalTable = _CePfePerfTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cePfePerfTotalTable.setStatus("current")
_CePfePerfTotalEntry_Object = MibTableRow
cePfePerfTotalEntry = _CePfePerfTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1)
)
cePfePerfTotalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cePfePerfTotalEntry.setStatus("current")
_CePfePerfTotalUtilization_Type = TotalUtilization
_CePfePerfTotalUtilization_Object = MibTableColumn
cePfePerfTotalUtilization = _CePfePerfTotalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1, 1),
    _CePfePerfTotalUtilization_Type()
)
cePfePerfTotalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfTotalUtilization.setStatus("current")
_CePfePerfTotalEfficiency_Type = TotalEfficiency
_CePfePerfTotalEfficiency_Object = MibTableColumn
cePfePerfTotalEfficiency = _CePfePerfTotalEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1, 2),
    _CePfePerfTotalEfficiency_Type()
)
cePfePerfTotalEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfePerfTotalEfficiency.setStatus("current")
_CePfeHistory_ObjectIdentity = ObjectIdentity
cePfeHistory = _CePfeHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2)
)


class _CePfeHistNotifiesEnable_Type(EventType):
    """Custom type cePfeHistNotifiesEnable based on EventType"""


_CePfeHistNotifiesEnable_Object = MibScalar
cePfeHistNotifiesEnable = _CePfeHistNotifiesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 1),
    _CePfeHistNotifiesEnable_Type()
)
cePfeHistNotifiesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cePfeHistNotifiesEnable.setStatus("current")


class _CePfeHistTableSize_Type(Unsigned32):
    """Custom type cePfeHistTableSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CePfeHistTableSize_Type.__name__ = "Unsigned32"
_CePfeHistTableSize_Object = MibScalar
cePfeHistTableSize = _CePfeHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 2),
    _CePfeHistTableSize_Type()
)
cePfeHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cePfeHistTableSize.setStatus("current")


class _CePfeHistTableLastIndex_Type(Unsigned32):
    """Custom type cePfeHistTableLastIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CePfeHistTableLastIndex_Type.__name__ = "Unsigned32"
_CePfeHistTableLastIndex_Object = MibScalar
cePfeHistTableLastIndex = _CePfeHistTableLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 3),
    _CePfeHistTableLastIndex_Type()
)
cePfeHistTableLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfeHistTableLastIndex.setStatus("current")
_CePfeHistTable_Object = MibTable
cePfeHistTable = _CePfeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cePfeHistTable.setStatus("current")
_CePfeHistEntry_Object = MibTableRow
cePfeHistEntry = _CePfeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1)
)
cePfeHistEntry.setIndexNames(
    (0, "CISCO-ENTITY-PFE-MIB", "cePfeHistIndex"),
)
if mibBuilder.loadTexts:
    cePfeHistEntry.setStatus("current")


class _CePfeHistIndex_Type(Unsigned32):
    """Custom type cePfeHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CePfeHistIndex_Type.__name__ = "Unsigned32"
_CePfeHistIndex_Object = MibTableColumn
cePfeHistIndex = _CePfeHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 1),
    _CePfeHistIndex_Type()
)
cePfeHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cePfeHistIndex.setStatus("current")
_CePfeHistEntPhysIndex_Type = PhysicalIndex
_CePfeHistEntPhysIndex_Object = MibTableColumn
cePfeHistEntPhysIndex = _CePfeHistEntPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 2),
    _CePfeHistEntPhysIndex_Type()
)
cePfeHistEntPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfeHistEntPhysIndex.setStatus("current")
_CePfeHistType_Type = HistEventType
_CePfeHistType_Object = MibTableColumn
cePfeHistType = _CePfeHistType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 3),
    _CePfeHistType_Type()
)
cePfeHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfeHistType.setStatus("current")
_CePfeHistThld_Type = Percentage
_CePfeHistThld_Object = MibTableColumn
cePfeHistThld = _CePfeHistThld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 4),
    _CePfeHistThld_Type()
)
cePfeHistThld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfeHistThld.setStatus("current")
_CePfeHistValue_Type = Percentage
_CePfeHistValue_Object = MibTableColumn
cePfeHistValue = _CePfeHistValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 5),
    _CePfeHistValue_Type()
)
cePfeHistValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfeHistValue.setStatus("current")
_CePfeHistRestartReason_Type = DisplayString
_CePfeHistRestartReason_Object = MibTableColumn
cePfeHistRestartReason = _CePfeHistRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 6),
    _CePfeHistRestartReason_Type()
)
cePfeHistRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfeHistRestartReason.setStatus("current")
_CePfeHistTimeStamp_Type = TimeStamp
_CePfeHistTimeStamp_Object = MibTableColumn
cePfeHistTimeStamp = _CePfeHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 7),
    _CePfeHistTimeStamp_Type()
)
cePfeHistTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePfeHistTimeStamp.setStatus("current")
_CePfeMIBConformance_ObjectIdentity = ObjectIdentity
cePfeMIBConformance = _CePfeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2)
)
_CePfeMIBCompliances_ObjectIdentity = ObjectIdentity
cePfeMIBCompliances = _CePfeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 1)
)
_CePfeMIBGroups_ObjectIdentity = ObjectIdentity
cePfeMIBGroups = _CePfeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2)
)
cePfePerfConfigEntry.registerAugmentions(
    ("CISCO-ENTITY-PFE-MIB",
     "cePfePerfCurrentEntry")
)
cePfePerfCurrentEntry.setIndexNames(*cePfePerfConfigEntry.getIndexNames())

# Managed Objects groups

cePfeMIBPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 1)
)
cePfeMIBPerformanceGroup.setObjects(
      *(("CISCO-ENTITY-PFE-MIB", "cePfeHistTableSize"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistTableLastIndex"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistNotifiesEnable"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigTimeElapsed"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigValidIntervals"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThldUtilization"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThldEfficiency"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld1MinUtilization"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld1MinEfficiency"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld5MinUtilization"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld5MinEfficiency"))
)
if mibBuilder.loadTexts:
    cePfeMIBPerformanceGroup.setStatus("current")

cePfeMIBCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 2)
)
cePfeMIBCurrentGroup.setObjects(
      *(("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentUtilization"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentEfficiency"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent1MinUtilization"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent1MinEfficiency"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent5MinUtilization"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent5MinEfficiency"))
)
if mibBuilder.loadTexts:
    cePfeMIBCurrentGroup.setStatus("current")

cePfeMIBIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 3)
)
cePfeMIBIntervalGroup.setObjects(
      *(("CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalUtilization"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalEfficiency"))
)
if mibBuilder.loadTexts:
    cePfeMIBIntervalGroup.setStatus("current")

cePfeMIBTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 4)
)
cePfeMIBTotalGroup.setObjects(
      *(("CISCO-ENTITY-PFE-MIB", "cePfePerfTotalUtilization"),
        ("CISCO-ENTITY-PFE-MIB", "cePfePerfTotalEfficiency"))
)
if mibBuilder.loadTexts:
    cePfeMIBTotalGroup.setStatus("current")

cePfeMIBHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 5)
)
cePfeMIBHistGroup.setObjects(
      *(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistType"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistThld"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistValue"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartReason"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistTimeStamp"))
)
if mibBuilder.loadTexts:
    cePfeMIBHistGroup.setStatus("current")


# Notification objects

cePfeHistThldEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 0, 1)
)
cePfeHistThldEvent.setObjects(
      *(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistType"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistThld"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistValue"))
)
if mibBuilder.loadTexts:
    cePfeHistThldEvent.setStatus(
        "current"
    )

cePfeHistRestartEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 0, 2)
)
cePfeHistRestartEvent.setObjects(
      *(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartReason"))
)
if mibBuilder.loadTexts:
    cePfeHistRestartEvent.setStatus(
        "current"
    )


# Notifications groups

cePfeMIBHistEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 6)
)
cePfeMIBHistEventGroup.setObjects(
      *(("CISCO-ENTITY-PFE-MIB", "cePfeHistThldEvent"),
        ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartEvent"))
)
if mibBuilder.loadTexts:
    cePfeMIBHistEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cePfeMIBPerformanceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cePfeMIBPerformanceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-PFE-MIB",
    **{"CurrentUtilization": CurrentUtilization,
       "CurrentEfficiency": CurrentEfficiency,
       "IntervalUtilization": IntervalUtilization,
       "IntervalEfficiency": IntervalEfficiency,
       "TotalUtilization": TotalUtilization,
       "TotalEfficiency": TotalEfficiency,
       "Percentage": Percentage,
       "EventType": EventType,
       "HistEventType": HistEventType,
       "ciscoEntityPfeMib": ciscoEntityPfeMib,
       "cePfeMIBNotifications": cePfeMIBNotifications,
       "cePfeHistThldEvent": cePfeHistThldEvent,
       "cePfeHistRestartEvent": cePfeHistRestartEvent,
       "cePfeMIBObjects": cePfeMIBObjects,
       "cePfePerformance": cePfePerformance,
       "cePfePerfConfigTable": cePfePerfConfigTable,
       "cePfePerfConfigEntry": cePfePerfConfigEntry,
       "cePfePerfConfigTimeElapsed": cePfePerfConfigTimeElapsed,
       "cePfePerfConfigValidIntervals": cePfePerfConfigValidIntervals,
       "cePfePerfConfigThldUtilization": cePfePerfConfigThldUtilization,
       "cePfePerfConfigThldEfficiency": cePfePerfConfigThldEfficiency,
       "cePfePerfConfigThld1MinUtilization": cePfePerfConfigThld1MinUtilization,
       "cePfePerfConfigThld1MinEfficiency": cePfePerfConfigThld1MinEfficiency,
       "cePfePerfConfigThld5MinUtilization": cePfePerfConfigThld5MinUtilization,
       "cePfePerfConfigThld5MinEfficiency": cePfePerfConfigThld5MinEfficiency,
       "cePfePerfCurrentTable": cePfePerfCurrentTable,
       "cePfePerfCurrentEntry": cePfePerfCurrentEntry,
       "cePfePerfCurrentUtilization": cePfePerfCurrentUtilization,
       "cePfePerfCurrentEfficiency": cePfePerfCurrentEfficiency,
       "cePfePerfCurrent1MinUtilization": cePfePerfCurrent1MinUtilization,
       "cePfePerfCurrent1MinEfficiency": cePfePerfCurrent1MinEfficiency,
       "cePfePerfCurrent5MinUtilization": cePfePerfCurrent5MinUtilization,
       "cePfePerfCurrent5MinEfficiency": cePfePerfCurrent5MinEfficiency,
       "cePfePerfIntervalTable": cePfePerfIntervalTable,
       "cePfePerfIntervalEntry": cePfePerfIntervalEntry,
       "cePfePerfIntervalNumber": cePfePerfIntervalNumber,
       "cePfePerfIntervalUtilization": cePfePerfIntervalUtilization,
       "cePfePerfIntervalEfficiency": cePfePerfIntervalEfficiency,
       "cePfePerfTotalTable": cePfePerfTotalTable,
       "cePfePerfTotalEntry": cePfePerfTotalEntry,
       "cePfePerfTotalUtilization": cePfePerfTotalUtilization,
       "cePfePerfTotalEfficiency": cePfePerfTotalEfficiency,
       "cePfeHistory": cePfeHistory,
       "cePfeHistNotifiesEnable": cePfeHistNotifiesEnable,
       "cePfeHistTableSize": cePfeHistTableSize,
       "cePfeHistTableLastIndex": cePfeHistTableLastIndex,
       "cePfeHistTable": cePfeHistTable,
       "cePfeHistEntry": cePfeHistEntry,
       "cePfeHistIndex": cePfeHistIndex,
       "cePfeHistEntPhysIndex": cePfeHistEntPhysIndex,
       "cePfeHistType": cePfeHistType,
       "cePfeHistThld": cePfeHistThld,
       "cePfeHistValue": cePfeHistValue,
       "cePfeHistRestartReason": cePfeHistRestartReason,
       "cePfeHistTimeStamp": cePfeHistTimeStamp,
       "cePfeMIBConformance": cePfeMIBConformance,
       "cePfeMIBCompliances": cePfeMIBCompliances,
       "cePfeMIBPerformanceCompliance": cePfeMIBPerformanceCompliance,
       "cePfeMIBGroups": cePfeMIBGroups,
       "cePfeMIBPerformanceGroup": cePfeMIBPerformanceGroup,
       "cePfeMIBCurrentGroup": cePfeMIBCurrentGroup,
       "cePfeMIBIntervalGroup": cePfeMIBIntervalGroup,
       "cePfeMIBTotalGroup": cePfeMIBTotalGroup,
       "cePfeMIBHistGroup": cePfeMIBHistGroup,
       "cePfeMIBHistEventGroup": cePfeMIBHistEventGroup}
)
