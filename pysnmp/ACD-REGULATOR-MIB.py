# SNMP MIB module (ACD-REGULATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-REGULATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:23 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdRegulator = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6)
)
acdRegulator.setRevisions(
        ("2012-01-10 01:00",
         "2011-10-10 01:00",
         "2010-11-10 01:00",
         "2008-05-01 01:00",
         "2008-02-06 01:00",
         "2007-03-28 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdRegulatorTable_Object = MibTable
acdRegulatorTable = _AcdRegulatorTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1)
)
if mibBuilder.loadTexts:
    acdRegulatorTable.setStatus("current")
_AcdRegulatorEntry_Object = MibTableRow
acdRegulatorEntry = _AcdRegulatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1)
)
acdRegulatorEntry.setIndexNames(
    (0, "ACD-REGULATOR-MIB", "acdRegulatorID"),
)
if mibBuilder.loadTexts:
    acdRegulatorEntry.setStatus("current")
_AcdRegulatorID_Type = Unsigned32
_AcdRegulatorID_Object = MibTableColumn
acdRegulatorID = _AcdRegulatorID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 1),
    _AcdRegulatorID_Type()
)
acdRegulatorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdRegulatorID.setStatus("current")


class _AcdRegulatorName_Type(DisplayString):
    """Custom type acdRegulatorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdRegulatorName_Type.__name__ = "DisplayString"
_AcdRegulatorName_Object = MibTableColumn
acdRegulatorName = _AcdRegulatorName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 2),
    _AcdRegulatorName_Type()
)
acdRegulatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorName.setStatus("current")


class _AcdRegulatorCir_Type(Unsigned32):
    """Custom type acdRegulatorCir based on Unsigned32"""
    defaultValue = 20000


_AcdRegulatorCir_Object = MibTableColumn
acdRegulatorCir = _AcdRegulatorCir_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 3),
    _AcdRegulatorCir_Type()
)
acdRegulatorCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorCir.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorCir.setUnits("Kbps")


class _AcdRegulatorCbs_Type(Unsigned32):
    """Custom type acdRegulatorCbs based on Unsigned32"""
    defaultValue = 8


_AcdRegulatorCbs_Object = MibTableColumn
acdRegulatorCbs = _AcdRegulatorCbs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 4),
    _AcdRegulatorCbs_Type()
)
acdRegulatorCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorCbs.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorCbs.setUnits("Kbytes")


class _AcdRegulatorEir_Type(Unsigned32):
    """Custom type acdRegulatorEir based on Unsigned32"""
    defaultValue = 1000


_AcdRegulatorEir_Object = MibTableColumn
acdRegulatorEir = _AcdRegulatorEir_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 5),
    _AcdRegulatorEir_Type()
)
acdRegulatorEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorEir.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorEir.setUnits("Kbps")


class _AcdRegulatorEbs_Type(Unsigned32):
    """Custom type acdRegulatorEbs based on Unsigned32"""
    defaultValue = 8


_AcdRegulatorEbs_Object = MibTableColumn
acdRegulatorEbs = _AcdRegulatorEbs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 6),
    _AcdRegulatorEbs_Type()
)
acdRegulatorEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorEbs.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorEbs.setUnits("Kbytes")


class _AcdRegulatorIsBlind_Type(TruthValue):
    """Custom type acdRegulatorIsBlind based on TruthValue"""


_AcdRegulatorIsBlind_Object = MibTableColumn
acdRegulatorIsBlind = _AcdRegulatorIsBlind_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 7),
    _AcdRegulatorIsBlind_Type()
)
acdRegulatorIsBlind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorIsBlind.setStatus("current")


class _AcdRegulatorIsCouple_Type(TruthValue):
    """Custom type acdRegulatorIsCouple based on TruthValue"""


_AcdRegulatorIsCouple_Object = MibTableColumn
acdRegulatorIsCouple = _AcdRegulatorIsCouple_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 8),
    _AcdRegulatorIsCouple_Type()
)
acdRegulatorIsCouple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorIsCouple.setStatus("current")
_AcdRegulatorRowStatus_Type = RowStatus
_AcdRegulatorRowStatus_Object = MibTableColumn
acdRegulatorRowStatus = _AcdRegulatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 9),
    _AcdRegulatorRowStatus_Type()
)
acdRegulatorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorRowStatus.setStatus("current")


class _AcdRegulatorWorkingRate_Type(Integer32):
    """Custom type acdRegulatorWorkingRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer1", 1),
          ("layer2", 2))
    )


_AcdRegulatorWorkingRate_Type.__name__ = "Integer32"
_AcdRegulatorWorkingRate_Object = MibTableColumn
acdRegulatorWorkingRate = _AcdRegulatorWorkingRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 10),
    _AcdRegulatorWorkingRate_Type()
)
acdRegulatorWorkingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorWorkingRate.setStatus("current")
_AcdRegulatorStatsTable_Object = MibTable
acdRegulatorStatsTable = _AcdRegulatorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2)
)
if mibBuilder.loadTexts:
    acdRegulatorStatsTable.setStatus("current")
_AcdRegulatorStatsEntry_Object = MibTableRow
acdRegulatorStatsEntry = _AcdRegulatorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1)
)
acdRegulatorStatsEntry.setIndexNames(
    (0, "ACD-REGULATOR-MIB", "acdRegulatorStatsID"),
)
if mibBuilder.loadTexts:
    acdRegulatorStatsEntry.setStatus("current")
_AcdRegulatorStatsID_Type = Unsigned32
_AcdRegulatorStatsID_Object = MibTableColumn
acdRegulatorStatsID = _AcdRegulatorStatsID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 1),
    _AcdRegulatorStatsID_Type()
)
acdRegulatorStatsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdRegulatorStatsID.setStatus("current")
_AcdRegulatorStatsAcceptOctets_Type = Counter32
_AcdRegulatorStatsAcceptOctets_Object = MibTableColumn
acdRegulatorStatsAcceptOctets = _AcdRegulatorStatsAcceptOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 2),
    _AcdRegulatorStatsAcceptOctets_Type()
)
acdRegulatorStatsAcceptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOctets.setUnits("Octets")
_AcdRegulatorStatsAcceptOverflowOctets_Type = Counter32
_AcdRegulatorStatsAcceptOverflowOctets_Object = MibTableColumn
acdRegulatorStatsAcceptOverflowOctets = _AcdRegulatorStatsAcceptOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 3),
    _AcdRegulatorStatsAcceptOverflowOctets_Type()
)
acdRegulatorStatsAcceptOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOverflowOctets.setUnits("Octets")
_AcdRegulatorStatsAcceptHCOctets_Type = Counter64
_AcdRegulatorStatsAcceptHCOctets_Object = MibTableColumn
acdRegulatorStatsAcceptHCOctets = _AcdRegulatorStatsAcceptHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 4),
    _AcdRegulatorStatsAcceptHCOctets_Type()
)
acdRegulatorStatsAcceptHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptHCOctets.setUnits("Octets")
_AcdRegulatorStatsAcceptPkts_Type = Counter32
_AcdRegulatorStatsAcceptPkts_Object = MibTableColumn
acdRegulatorStatsAcceptPkts = _AcdRegulatorStatsAcceptPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 5),
    _AcdRegulatorStatsAcceptPkts_Type()
)
acdRegulatorStatsAcceptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptPkts.setUnits("Packets")
_AcdRegulatorStatsAcceptOverflowPkts_Type = Counter32
_AcdRegulatorStatsAcceptOverflowPkts_Object = MibTableColumn
acdRegulatorStatsAcceptOverflowPkts = _AcdRegulatorStatsAcceptOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 6),
    _AcdRegulatorStatsAcceptOverflowPkts_Type()
)
acdRegulatorStatsAcceptOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOverflowPkts.setUnits("Packets")
_AcdRegulatorStatsAcceptHCPkts_Type = Counter64
_AcdRegulatorStatsAcceptHCPkts_Object = MibTableColumn
acdRegulatorStatsAcceptHCPkts = _AcdRegulatorStatsAcceptHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 7),
    _AcdRegulatorStatsAcceptHCPkts_Type()
)
acdRegulatorStatsAcceptHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptHCPkts.setUnits("Octets")
_AcdRegulatorStatsAcceptRate_Type = Gauge32
_AcdRegulatorStatsAcceptRate_Object = MibTableColumn
acdRegulatorStatsAcceptRate = _AcdRegulatorStatsAcceptRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 8),
    _AcdRegulatorStatsAcceptRate_Type()
)
acdRegulatorStatsAcceptRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptRate.setUnits("Kbps")
_AcdRegulatorStatsDropOctets_Type = Counter32
_AcdRegulatorStatsDropOctets_Object = MibTableColumn
acdRegulatorStatsDropOctets = _AcdRegulatorStatsDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 9),
    _AcdRegulatorStatsDropOctets_Type()
)
acdRegulatorStatsDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOctets.setUnits("Octets")
_AcdRegulatorStatsDropOverflowOctets_Type = Counter32
_AcdRegulatorStatsDropOverflowOctets_Object = MibTableColumn
acdRegulatorStatsDropOverflowOctets = _AcdRegulatorStatsDropOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 10),
    _AcdRegulatorStatsDropOverflowOctets_Type()
)
acdRegulatorStatsDropOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOverflowOctets.setUnits("Octets")
_AcdRegulatorStatsDropHCOctets_Type = Counter64
_AcdRegulatorStatsDropHCOctets_Object = MibTableColumn
acdRegulatorStatsDropHCOctets = _AcdRegulatorStatsDropHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 11),
    _AcdRegulatorStatsDropHCOctets_Type()
)
acdRegulatorStatsDropHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropHCOctets.setUnits("Octets")
_AcdRegulatorStatsDropPkts_Type = Counter32
_AcdRegulatorStatsDropPkts_Object = MibTableColumn
acdRegulatorStatsDropPkts = _AcdRegulatorStatsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 12),
    _AcdRegulatorStatsDropPkts_Type()
)
acdRegulatorStatsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropPkts.setUnits("Packets")
_AcdRegulatorStatsDropOverflowPkts_Type = Counter32
_AcdRegulatorStatsDropOverflowPkts_Object = MibTableColumn
acdRegulatorStatsDropOverflowPkts = _AcdRegulatorStatsDropOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 13),
    _AcdRegulatorStatsDropOverflowPkts_Type()
)
acdRegulatorStatsDropOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOverflowPkts.setUnits("Packets")
_AcdRegulatorStatsDropHCPkts_Type = Counter64
_AcdRegulatorStatsDropHCPkts_Object = MibTableColumn
acdRegulatorStatsDropHCPkts = _AcdRegulatorStatsDropHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 14),
    _AcdRegulatorStatsDropHCPkts_Type()
)
acdRegulatorStatsDropHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropHCPkts.setUnits("Octets")
_AcdRegulatorStatsDropRate_Type = Gauge32
_AcdRegulatorStatsDropRate_Object = MibTableColumn
acdRegulatorStatsDropRate = _AcdRegulatorStatsDropRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 15),
    _AcdRegulatorStatsDropRate_Type()
)
acdRegulatorStatsDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropRate.setUnits("Kbps")
_AcdRegulatorHistStatsTable_Object = MibTable
acdRegulatorHistStatsTable = _AcdRegulatorHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3)
)
if mibBuilder.loadTexts:
    acdRegulatorHistStatsTable.setStatus("current")
_AcdRegulatorHistStatsEntry_Object = MibTableRow
acdRegulatorHistStatsEntry = _AcdRegulatorHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1)
)
acdRegulatorHistStatsEntry.setIndexNames(
    (0, "ACD-REGULATOR-MIB", "acdRegulatorHistStatsID"),
    (0, "ACD-REGULATOR-MIB", "acdRegulatorHistStatsSampleIndex"),
)
if mibBuilder.loadTexts:
    acdRegulatorHistStatsEntry.setStatus("current")
_AcdRegulatorHistStatsID_Type = Unsigned32
_AcdRegulatorHistStatsID_Object = MibTableColumn
acdRegulatorHistStatsID = _AcdRegulatorHistStatsID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 1),
    _AcdRegulatorHistStatsID_Type()
)
acdRegulatorHistStatsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsID.setStatus("current")
_AcdRegulatorHistStatsSampleIndex_Type = Unsigned32
_AcdRegulatorHistStatsSampleIndex_Object = MibTableColumn
acdRegulatorHistStatsSampleIndex = _AcdRegulatorHistStatsSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 2),
    _AcdRegulatorHistStatsSampleIndex_Type()
)
acdRegulatorHistStatsSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsSampleIndex.setStatus("current")


class _AcdRegulatorHistStatsStatus_Type(Integer32):
    """Custom type acdRegulatorHistStatsStatus based on Integer32"""
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


_AcdRegulatorHistStatsStatus_Type.__name__ = "Integer32"
_AcdRegulatorHistStatsStatus_Object = MibTableColumn
acdRegulatorHistStatsStatus = _AcdRegulatorHistStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 3),
    _AcdRegulatorHistStatsStatus_Type()
)
acdRegulatorHistStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsStatus.setStatus("current")
_AcdRegulatorHistStatsDuration_Type = Unsigned32
_AcdRegulatorHistStatsDuration_Object = MibTableColumn
acdRegulatorHistStatsDuration = _AcdRegulatorHistStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 4),
    _AcdRegulatorHistStatsDuration_Type()
)
acdRegulatorHistStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDuration.setStatus("current")
_AcdRegulatorHistStatsIntervalEnd_Type = DateAndTime
_AcdRegulatorHistStatsIntervalEnd_Object = MibTableColumn
acdRegulatorHistStatsIntervalEnd = _AcdRegulatorHistStatsIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 5),
    _AcdRegulatorHistStatsIntervalEnd_Type()
)
acdRegulatorHistStatsIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsIntervalEnd.setStatus("current")
_AcdRegulatorHistStatsAcceptOctets_Type = Counter32
_AcdRegulatorHistStatsAcceptOctets_Object = MibTableColumn
acdRegulatorHistStatsAcceptOctets = _AcdRegulatorHistStatsAcceptOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 6),
    _AcdRegulatorHistStatsAcceptOctets_Type()
)
acdRegulatorHistStatsAcceptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOctets.setUnits("Octets")
_AcdRegulatorHistStatsAcceptOverflowOctets_Type = Counter32
_AcdRegulatorHistStatsAcceptOverflowOctets_Object = MibTableColumn
acdRegulatorHistStatsAcceptOverflowOctets = _AcdRegulatorHistStatsAcceptOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 7),
    _AcdRegulatorHistStatsAcceptOverflowOctets_Type()
)
acdRegulatorHistStatsAcceptOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOverflowOctets.setUnits("Octets")
_AcdRegulatorHistStatsAcceptHCOctets_Type = Counter64
_AcdRegulatorHistStatsAcceptHCOctets_Object = MibTableColumn
acdRegulatorHistStatsAcceptHCOctets = _AcdRegulatorHistStatsAcceptHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 8),
    _AcdRegulatorHistStatsAcceptHCOctets_Type()
)
acdRegulatorHistStatsAcceptHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptHCOctets.setUnits("Octets")
_AcdRegulatorHistStatsAcceptPkts_Type = Counter32
_AcdRegulatorHistStatsAcceptPkts_Object = MibTableColumn
acdRegulatorHistStatsAcceptPkts = _AcdRegulatorHistStatsAcceptPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 9),
    _AcdRegulatorHistStatsAcceptPkts_Type()
)
acdRegulatorHistStatsAcceptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptPkts.setUnits("Packets")
_AcdRegulatorHistStatsAcceptOverflowPkts_Type = Counter32
_AcdRegulatorHistStatsAcceptOverflowPkts_Object = MibTableColumn
acdRegulatorHistStatsAcceptOverflowPkts = _AcdRegulatorHistStatsAcceptOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 10),
    _AcdRegulatorHistStatsAcceptOverflowPkts_Type()
)
acdRegulatorHistStatsAcceptOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOverflowPkts.setUnits("Packets")
_AcdRegulatorHistStatsAcceptHCPkts_Type = Counter64
_AcdRegulatorHistStatsAcceptHCPkts_Object = MibTableColumn
acdRegulatorHistStatsAcceptHCPkts = _AcdRegulatorHistStatsAcceptHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 11),
    _AcdRegulatorHistStatsAcceptHCPkts_Type()
)
acdRegulatorHistStatsAcceptHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptHCPkts.setUnits("Octets")
_AcdRegulatorHistStatsAcceptAvgRate_Type = Gauge32
_AcdRegulatorHistStatsAcceptAvgRate_Object = MibTableColumn
acdRegulatorHistStatsAcceptAvgRate = _AcdRegulatorHistStatsAcceptAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 12),
    _AcdRegulatorHistStatsAcceptAvgRate_Type()
)
acdRegulatorHistStatsAcceptAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptAvgRate.setUnits("Kbps")
_AcdRegulatorHistStatsAcceptMinRate_Type = Gauge32
_AcdRegulatorHistStatsAcceptMinRate_Object = MibTableColumn
acdRegulatorHistStatsAcceptMinRate = _AcdRegulatorHistStatsAcceptMinRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 13),
    _AcdRegulatorHistStatsAcceptMinRate_Type()
)
acdRegulatorHistStatsAcceptMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptMinRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptMinRate.setUnits("Kbps")
_AcdRegulatorHistStatsAcceptMaxRate_Type = Gauge32
_AcdRegulatorHistStatsAcceptMaxRate_Object = MibTableColumn
acdRegulatorHistStatsAcceptMaxRate = _AcdRegulatorHistStatsAcceptMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 14),
    _AcdRegulatorHistStatsAcceptMaxRate_Type()
)
acdRegulatorHistStatsAcceptMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptMaxRate.setUnits("Kbps")
_AcdRegulatorHistStatsDropOctets_Type = Counter32
_AcdRegulatorHistStatsDropOctets_Object = MibTableColumn
acdRegulatorHistStatsDropOctets = _AcdRegulatorHistStatsDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 15),
    _AcdRegulatorHistStatsDropOctets_Type()
)
acdRegulatorHistStatsDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOctets.setUnits("Octets")
_AcdRegulatorHistStatsDropOverflowOctets_Type = Counter32
_AcdRegulatorHistStatsDropOverflowOctets_Object = MibTableColumn
acdRegulatorHistStatsDropOverflowOctets = _AcdRegulatorHistStatsDropOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 16),
    _AcdRegulatorHistStatsDropOverflowOctets_Type()
)
acdRegulatorHistStatsDropOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOverflowOctets.setUnits("Octets")
_AcdRegulatorHistStatsDropHCOctets_Type = Counter64
_AcdRegulatorHistStatsDropHCOctets_Object = MibTableColumn
acdRegulatorHistStatsDropHCOctets = _AcdRegulatorHistStatsDropHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 17),
    _AcdRegulatorHistStatsDropHCOctets_Type()
)
acdRegulatorHistStatsDropHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropHCOctets.setUnits("Octets")
_AcdRegulatorHistStatsDropPkts_Type = Counter32
_AcdRegulatorHistStatsDropPkts_Object = MibTableColumn
acdRegulatorHistStatsDropPkts = _AcdRegulatorHistStatsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 18),
    _AcdRegulatorHistStatsDropPkts_Type()
)
acdRegulatorHistStatsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropPkts.setUnits("Packets")
_AcdRegulatorHistStatsDropOverflowPkts_Type = Counter32
_AcdRegulatorHistStatsDropOverflowPkts_Object = MibTableColumn
acdRegulatorHistStatsDropOverflowPkts = _AcdRegulatorHistStatsDropOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 19),
    _AcdRegulatorHistStatsDropOverflowPkts_Type()
)
acdRegulatorHistStatsDropOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOverflowPkts.setUnits("Packets")
_AcdRegulatorHistStatsDropHCPkts_Type = Counter64
_AcdRegulatorHistStatsDropHCPkts_Object = MibTableColumn
acdRegulatorHistStatsDropHCPkts = _AcdRegulatorHistStatsDropHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 20),
    _AcdRegulatorHistStatsDropHCPkts_Type()
)
acdRegulatorHistStatsDropHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropHCPkts.setUnits("Octets")
_AcdRegulatorHistStatsDropAvgRate_Type = Gauge32
_AcdRegulatorHistStatsDropAvgRate_Object = MibTableColumn
acdRegulatorHistStatsDropAvgRate = _AcdRegulatorHistStatsDropAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 21),
    _AcdRegulatorHistStatsDropAvgRate_Type()
)
acdRegulatorHistStatsDropAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropAvgRate.setUnits("Kbps")
_AcdRegulatorHistStatsDropMinRate_Type = Gauge32
_AcdRegulatorHistStatsDropMinRate_Object = MibTableColumn
acdRegulatorHistStatsDropMinRate = _AcdRegulatorHistStatsDropMinRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 22),
    _AcdRegulatorHistStatsDropMinRate_Type()
)
acdRegulatorHistStatsDropMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropMinRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropMinRate.setUnits("Kbps")
_AcdRegulatorHistStatsDropMaxRate_Type = Gauge32
_AcdRegulatorHistStatsDropMaxRate_Object = MibTableColumn
acdRegulatorHistStatsDropMaxRate = _AcdRegulatorHistStatsDropMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 23),
    _AcdRegulatorHistStatsDropMaxRate_Type()
)
acdRegulatorHistStatsDropMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropMaxRate.setUnits("Kbps")
_AcdRegulatorNotifications_ObjectIdentity = ObjectIdentity
acdRegulatorNotifications = _AcdRegulatorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 4)
)
_AcdRegulatorMIBObjects_ObjectIdentity = ObjectIdentity
acdRegulatorMIBObjects = _AcdRegulatorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 5)
)
_AcdRegulatorTableTid_ObjectIdentity = ObjectIdentity
acdRegulatorTableTid = _AcdRegulatorTableTid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 5, 1)
)
_AcdRegulatorTableLastChangeTid_Type = Unsigned32
_AcdRegulatorTableLastChangeTid_Object = MibScalar
acdRegulatorTableLastChangeTid = _AcdRegulatorTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 5, 1, 1),
    _AcdRegulatorTableLastChangeTid_Type()
)
acdRegulatorTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorTableLastChangeTid.setStatus("current")
_AcdRegulatorConformance_ObjectIdentity = ObjectIdentity
acdRegulatorConformance = _AcdRegulatorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6)
)
_AcdRegulatorCompliances_ObjectIdentity = ObjectIdentity
acdRegulatorCompliances = _AcdRegulatorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 1)
)
_AcdRegulatorGroups_ObjectIdentity = ObjectIdentity
acdRegulatorGroups = _AcdRegulatorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2)
)

# Managed Objects groups

acdRegulatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 1)
)
acdRegulatorGroup.setObjects(
      *(("ACD-REGULATOR-MIB", "acdRegulatorName"),
        ("ACD-REGULATOR-MIB", "acdRegulatorCir"),
        ("ACD-REGULATOR-MIB", "acdRegulatorCbs"),
        ("ACD-REGULATOR-MIB", "acdRegulatorEir"),
        ("ACD-REGULATOR-MIB", "acdRegulatorEbs"),
        ("ACD-REGULATOR-MIB", "acdRegulatorIsBlind"),
        ("ACD-REGULATOR-MIB", "acdRegulatorIsCouple"),
        ("ACD-REGULATOR-MIB", "acdRegulatorRowStatus"),
        ("ACD-REGULATOR-MIB", "acdRegulatorWorkingRate"))
)
if mibBuilder.loadTexts:
    acdRegulatorGroup.setStatus("current")

acdRegulatorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 2)
)
acdRegulatorStatsGroup.setObjects(
      *(("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOverflowOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOverflowPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOverflowOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOverflowPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropRate"))
)
if mibBuilder.loadTexts:
    acdRegulatorStatsGroup.setStatus("current")

acdRegulatorHistStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 3)
)
acdRegulatorHistStatsGroup.setObjects(
      *(("ACD-REGULATOR-MIB", "acdRegulatorHistStatsStatus"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDuration"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsIntervalEnd"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOverflowOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOverflowPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptAvgRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptMinRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptMaxRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOverflowOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOverflowPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropAvgRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropMinRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropMaxRate"))
)
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGroup.setStatus("current")

acdRegulatorTidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 4)
)
acdRegulatorTidGroup.setObjects(
    ("ACD-REGULATOR-MIB", "acdRegulatorTableLastChangeTid")
)
if mibBuilder.loadTexts:
    acdRegulatorTidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdRegulatorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    acdRegulatorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-REGULATOR-MIB",
    **{"acdRegulator": acdRegulator,
       "acdRegulatorTable": acdRegulatorTable,
       "acdRegulatorEntry": acdRegulatorEntry,
       "acdRegulatorID": acdRegulatorID,
       "acdRegulatorName": acdRegulatorName,
       "acdRegulatorCir": acdRegulatorCir,
       "acdRegulatorCbs": acdRegulatorCbs,
       "acdRegulatorEir": acdRegulatorEir,
       "acdRegulatorEbs": acdRegulatorEbs,
       "acdRegulatorIsBlind": acdRegulatorIsBlind,
       "acdRegulatorIsCouple": acdRegulatorIsCouple,
       "acdRegulatorRowStatus": acdRegulatorRowStatus,
       "acdRegulatorWorkingRate": acdRegulatorWorkingRate,
       "acdRegulatorStatsTable": acdRegulatorStatsTable,
       "acdRegulatorStatsEntry": acdRegulatorStatsEntry,
       "acdRegulatorStatsID": acdRegulatorStatsID,
       "acdRegulatorStatsAcceptOctets": acdRegulatorStatsAcceptOctets,
       "acdRegulatorStatsAcceptOverflowOctets": acdRegulatorStatsAcceptOverflowOctets,
       "acdRegulatorStatsAcceptHCOctets": acdRegulatorStatsAcceptHCOctets,
       "acdRegulatorStatsAcceptPkts": acdRegulatorStatsAcceptPkts,
       "acdRegulatorStatsAcceptOverflowPkts": acdRegulatorStatsAcceptOverflowPkts,
       "acdRegulatorStatsAcceptHCPkts": acdRegulatorStatsAcceptHCPkts,
       "acdRegulatorStatsAcceptRate": acdRegulatorStatsAcceptRate,
       "acdRegulatorStatsDropOctets": acdRegulatorStatsDropOctets,
       "acdRegulatorStatsDropOverflowOctets": acdRegulatorStatsDropOverflowOctets,
       "acdRegulatorStatsDropHCOctets": acdRegulatorStatsDropHCOctets,
       "acdRegulatorStatsDropPkts": acdRegulatorStatsDropPkts,
       "acdRegulatorStatsDropOverflowPkts": acdRegulatorStatsDropOverflowPkts,
       "acdRegulatorStatsDropHCPkts": acdRegulatorStatsDropHCPkts,
       "acdRegulatorStatsDropRate": acdRegulatorStatsDropRate,
       "acdRegulatorHistStatsTable": acdRegulatorHistStatsTable,
       "acdRegulatorHistStatsEntry": acdRegulatorHistStatsEntry,
       "acdRegulatorHistStatsID": acdRegulatorHistStatsID,
       "acdRegulatorHistStatsSampleIndex": acdRegulatorHistStatsSampleIndex,
       "acdRegulatorHistStatsStatus": acdRegulatorHistStatsStatus,
       "acdRegulatorHistStatsDuration": acdRegulatorHistStatsDuration,
       "acdRegulatorHistStatsIntervalEnd": acdRegulatorHistStatsIntervalEnd,
       "acdRegulatorHistStatsAcceptOctets": acdRegulatorHistStatsAcceptOctets,
       "acdRegulatorHistStatsAcceptOverflowOctets": acdRegulatorHistStatsAcceptOverflowOctets,
       "acdRegulatorHistStatsAcceptHCOctets": acdRegulatorHistStatsAcceptHCOctets,
       "acdRegulatorHistStatsAcceptPkts": acdRegulatorHistStatsAcceptPkts,
       "acdRegulatorHistStatsAcceptOverflowPkts": acdRegulatorHistStatsAcceptOverflowPkts,
       "acdRegulatorHistStatsAcceptHCPkts": acdRegulatorHistStatsAcceptHCPkts,
       "acdRegulatorHistStatsAcceptAvgRate": acdRegulatorHistStatsAcceptAvgRate,
       "acdRegulatorHistStatsAcceptMinRate": acdRegulatorHistStatsAcceptMinRate,
       "acdRegulatorHistStatsAcceptMaxRate": acdRegulatorHistStatsAcceptMaxRate,
       "acdRegulatorHistStatsDropOctets": acdRegulatorHistStatsDropOctets,
       "acdRegulatorHistStatsDropOverflowOctets": acdRegulatorHistStatsDropOverflowOctets,
       "acdRegulatorHistStatsDropHCOctets": acdRegulatorHistStatsDropHCOctets,
       "acdRegulatorHistStatsDropPkts": acdRegulatorHistStatsDropPkts,
       "acdRegulatorHistStatsDropOverflowPkts": acdRegulatorHistStatsDropOverflowPkts,
       "acdRegulatorHistStatsDropHCPkts": acdRegulatorHistStatsDropHCPkts,
       "acdRegulatorHistStatsDropAvgRate": acdRegulatorHistStatsDropAvgRate,
       "acdRegulatorHistStatsDropMinRate": acdRegulatorHistStatsDropMinRate,
       "acdRegulatorHistStatsDropMaxRate": acdRegulatorHistStatsDropMaxRate,
       "acdRegulatorNotifications": acdRegulatorNotifications,
       "acdRegulatorMIBObjects": acdRegulatorMIBObjects,
       "acdRegulatorTableTid": acdRegulatorTableTid,
       "acdRegulatorTableLastChangeTid": acdRegulatorTableLastChangeTid,
       "acdRegulatorConformance": acdRegulatorConformance,
       "acdRegulatorCompliances": acdRegulatorCompliances,
       "acdRegulatorCompliance": acdRegulatorCompliance,
       "acdRegulatorGroups": acdRegulatorGroups,
       "acdRegulatorGroup": acdRegulatorGroup,
       "acdRegulatorStatsGroup": acdRegulatorStatsGroup,
       "acdRegulatorHistStatsGroup": acdRegulatorHistStatsGroup,
       "acdRegulatorTidGroup": acdRegulatorTidGroup}
)
