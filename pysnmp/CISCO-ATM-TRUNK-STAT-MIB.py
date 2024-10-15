# SNMP MIB module (CISCO-ATM-TRUNK-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-TRUNK-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:07 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoAtmTrunkStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 407)
)
ciscoAtmTrunkStatMIB.setRevisions(
        ("2005-08-10 00:00",
         "2004-05-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAtmTrunkStatNotifs_ObjectIdentity = ObjectIdentity
ciscoAtmTrunkStatNotifs = _CiscoAtmTrunkStatNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 0)
)
_CiscoAtmTrunkStatObjects_ObjectIdentity = ObjectIdentity
ciscoAtmTrunkStatObjects = _CiscoAtmTrunkStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1)
)
_CatsStatistics_ObjectIdentity = ObjectIdentity
catsStatistics = _CatsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1)
)
_CatsPvcHistoryTable_Object = MibTable
catsPvcHistoryTable = _CatsPvcHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1)
)
if mibBuilder.loadTexts:
    catsPvcHistoryTable.setStatus("current")
_CatsPvcHistoryEntry_Object = MibTableRow
catsPvcHistoryEntry = _CatsPvcHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1)
)
catsPvcHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsPvcVpi"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsPvcVci"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsPvcIntervalIndex"),
)
if mibBuilder.loadTexts:
    catsPvcHistoryEntry.setStatus("current")
_CatsPvcVpi_Type = AtmVpIdentifier
_CatsPvcVpi_Object = MibTableColumn
catsPvcVpi = _CatsPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 1),
    _CatsPvcVpi_Type()
)
catsPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsPvcVpi.setStatus("current")
_CatsPvcVci_Type = AtmVcIdentifier
_CatsPvcVci_Object = MibTableColumn
catsPvcVci = _CatsPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 2),
    _CatsPvcVci_Type()
)
catsPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsPvcVci.setStatus("current")


class _CatsPvcIntervalIndex_Type(Unsigned32):
    """Custom type catsPvcIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CatsPvcIntervalIndex_Type.__name__ = "Unsigned32"
_CatsPvcIntervalIndex_Object = MibTableColumn
catsPvcIntervalIndex = _CatsPvcIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 3),
    _CatsPvcIntervalIndex_Type()
)
catsPvcIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsPvcIntervalIndex.setStatus("current")
_CatsPvcValidFlag_Type = TruthValue
_CatsPvcValidFlag_Object = MibTableColumn
catsPvcValidFlag = _CatsPvcValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 4),
    _CatsPvcValidFlag_Type()
)
catsPvcValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcValidFlag.setStatus("current")


class _CatsPvcDiscontinuityTime_Type(TimeStamp):
    """Custom type catsPvcDiscontinuityTime based on TimeStamp"""
    defaultValue = 0


_CatsPvcDiscontinuityTime_Object = MibTableColumn
catsPvcDiscontinuityTime = _CatsPvcDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 5),
    _CatsPvcDiscontinuityTime_Type()
)
catsPvcDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcDiscontinuityTime.setStatus("current")
_CatsPvcAtmXmtCells_Type = Counter32
_CatsPvcAtmXmtCells_Object = MibTableColumn
catsPvcAtmXmtCells = _CatsPvcAtmXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 6),
    _CatsPvcAtmXmtCells_Type()
)
catsPvcAtmXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcAtmXmtCells.setStatus("current")
_CatsPvcAtmRcvCells_Type = Counter32
_CatsPvcAtmRcvCells_Object = MibTableColumn
catsPvcAtmRcvCells = _CatsPvcAtmRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 7),
    _CatsPvcAtmRcvCells_Type()
)
catsPvcAtmRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcAtmRcvCells.setStatus("current")
_CatsPvcAvgAtmXmtCells_Type = Counter32
_CatsPvcAvgAtmXmtCells_Object = MibTableColumn
catsPvcAvgAtmXmtCells = _CatsPvcAvgAtmXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 8),
    _CatsPvcAvgAtmXmtCells_Type()
)
catsPvcAvgAtmXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcAvgAtmXmtCells.setStatus("current")
if mibBuilder.loadTexts:
    catsPvcAvgAtmXmtCells.setUnits("cells-per-sec")
_CatsPvcAvgAtmRcvCells_Type = Counter32
_CatsPvcAvgAtmRcvCells_Object = MibTableColumn
catsPvcAvgAtmRcvCells = _CatsPvcAvgAtmRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 9),
    _CatsPvcAvgAtmRcvCells_Type()
)
catsPvcAvgAtmRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcAvgAtmRcvCells.setStatus("current")
if mibBuilder.loadTexts:
    catsPvcAvgAtmRcvCells.setUnits("cells-per-sec")
_CatsPvcPeakAtmXmtCells_Type = Counter32
_CatsPvcPeakAtmXmtCells_Object = MibTableColumn
catsPvcPeakAtmXmtCells = _CatsPvcPeakAtmXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 10),
    _CatsPvcPeakAtmXmtCells_Type()
)
catsPvcPeakAtmXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcPeakAtmXmtCells.setStatus("current")
if mibBuilder.loadTexts:
    catsPvcPeakAtmXmtCells.setUnits("cells-per-sec")
_CatsPvcPeakAtmRcvCells_Type = Counter32
_CatsPvcPeakAtmRcvCells_Object = MibTableColumn
catsPvcPeakAtmRcvCells = _CatsPvcPeakAtmRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 11),
    _CatsPvcPeakAtmRcvCells_Type()
)
catsPvcPeakAtmRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcPeakAtmRcvCells.setStatus("current")
if mibBuilder.loadTexts:
    catsPvcPeakAtmRcvCells.setUnits("cells-per-sec")
_CatsPvcOamXmtEndLpbkCells_Type = Counter32
_CatsPvcOamXmtEndLpbkCells_Object = MibTableColumn
catsPvcOamXmtEndLpbkCells = _CatsPvcOamXmtEndLpbkCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 12),
    _CatsPvcOamXmtEndLpbkCells_Type()
)
catsPvcOamXmtEndLpbkCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcOamXmtEndLpbkCells.setStatus("current")
_CatsPvcOamRcvEndLpbkCells_Type = Counter32
_CatsPvcOamRcvEndLpbkCells_Object = MibTableColumn
catsPvcOamRcvEndLpbkCells = _CatsPvcOamRcvEndLpbkCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 13),
    _CatsPvcOamRcvEndLpbkCells_Type()
)
catsPvcOamRcvEndLpbkCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcOamRcvEndLpbkCells.setStatus("current")
_CatsPvcOamXmtSegLpbkCells_Type = Counter32
_CatsPvcOamXmtSegLpbkCells_Object = MibTableColumn
catsPvcOamXmtSegLpbkCells = _CatsPvcOamXmtSegLpbkCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 14),
    _CatsPvcOamXmtSegLpbkCells_Type()
)
catsPvcOamXmtSegLpbkCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcOamXmtSegLpbkCells.setStatus("current")
_CatsPvcOamRcvSegLpbkCells_Type = Counter32
_CatsPvcOamRcvSegLpbkCells_Object = MibTableColumn
catsPvcOamRcvSegLpbkCells = _CatsPvcOamRcvSegLpbkCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 15),
    _CatsPvcOamRcvSegLpbkCells_Type()
)
catsPvcOamRcvSegLpbkCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcOamRcvSegLpbkCells.setStatus("current")
_CatsPvcOamLpbkLostCells_Type = Counter32
_CatsPvcOamLpbkLostCells_Object = MibTableColumn
catsPvcOamLpbkLostCells = _CatsPvcOamLpbkLostCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 16),
    _CatsPvcOamLpbkLostCells_Type()
)
catsPvcOamLpbkLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcOamLpbkLostCells.setStatus("current")
_CatsPvcDiscardedRcvOamCells_Type = Counter32
_CatsPvcDiscardedRcvOamCells_Object = MibTableColumn
catsPvcDiscardedRcvOamCells = _CatsPvcDiscardedRcvOamCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 17),
    _CatsPvcDiscardedRcvOamCells_Type()
)
catsPvcDiscardedRcvOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcDiscardedRcvOamCells.setStatus("current")
_CatsPvcAisSuppressCnts_Type = Counter32
_CatsPvcAisSuppressCnts_Object = MibTableColumn
catsPvcAisSuppressCnts = _CatsPvcAisSuppressCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 18),
    _CatsPvcAisSuppressCnts_Type()
)
catsPvcAisSuppressCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcAisSuppressCnts.setStatus("current")
_CatsPvcXmtAisCnts_Type = Counter32
_CatsPvcXmtAisCnts_Object = MibTableColumn
catsPvcXmtAisCnts = _CatsPvcXmtAisCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 19),
    _CatsPvcXmtAisCnts_Type()
)
catsPvcXmtAisCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcXmtAisCnts.setStatus("current")
_CatsPvcRcvAisCnts_Type = Counter32
_CatsPvcRcvAisCnts_Object = MibTableColumn
catsPvcRcvAisCnts = _CatsPvcRcvAisCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 20),
    _CatsPvcRcvAisCnts_Type()
)
catsPvcRcvAisCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcRcvAisCnts.setStatus("current")
_CatsPvcXmtFerfCnts_Type = Counter32
_CatsPvcXmtFerfCnts_Object = MibTableColumn
catsPvcXmtFerfCnts = _CatsPvcXmtFerfCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 21),
    _CatsPvcXmtFerfCnts_Type()
)
catsPvcXmtFerfCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcXmtFerfCnts.setStatus("current")
_CatsPvcRcvFerfCnts_Type = Counter32
_CatsPvcRcvFerfCnts_Object = MibTableColumn
catsPvcRcvFerfCnts = _CatsPvcRcvFerfCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 22),
    _CatsPvcRcvFerfCnts_Type()
)
catsPvcRcvFerfCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcRcvFerfCnts.setStatus("current")
_CatsPvcXmtAisCells_Type = Counter32
_CatsPvcXmtAisCells_Object = MibTableColumn
catsPvcXmtAisCells = _CatsPvcXmtAisCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 23),
    _CatsPvcXmtAisCells_Type()
)
catsPvcXmtAisCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcXmtAisCells.setStatus("current")
_CatsPvcRcvAisCells_Type = Counter32
_CatsPvcRcvAisCells_Object = MibTableColumn
catsPvcRcvAisCells = _CatsPvcRcvAisCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 24),
    _CatsPvcRcvAisCells_Type()
)
catsPvcRcvAisCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcRcvAisCells.setStatus("current")
_CatsPvcXmtFerfCells_Type = Counter32
_CatsPvcXmtFerfCells_Object = MibTableColumn
catsPvcXmtFerfCells = _CatsPvcXmtFerfCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 25),
    _CatsPvcXmtFerfCells_Type()
)
catsPvcXmtFerfCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcXmtFerfCells.setStatus("current")
_CatsPvcRcvFerfCells_Type = Counter32
_CatsPvcRcvFerfCells_Object = MibTableColumn
catsPvcRcvFerfCells = _CatsPvcRcvFerfCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 26),
    _CatsPvcRcvFerfCells_Type()
)
catsPvcRcvFerfCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcRcvFerfCells.setStatus("current")
_CatsPvcOamLpbkTimeoutCnts_Type = Counter32
_CatsPvcOamLpbkTimeoutCnts_Object = MibTableColumn
catsPvcOamLpbkTimeoutCnts = _CatsPvcOamLpbkTimeoutCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 27),
    _CatsPvcOamLpbkTimeoutCnts_Type()
)
catsPvcOamLpbkTimeoutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcOamLpbkTimeoutCnts.setStatus("current")
_CatsPvcNewOamLpbkTimeoutDur_Type = Unsigned32
_CatsPvcNewOamLpbkTimeoutDur_Object = MibTableColumn
catsPvcNewOamLpbkTimeoutDur = _CatsPvcNewOamLpbkTimeoutDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 28),
    _CatsPvcNewOamLpbkTimeoutDur_Type()
)
catsPvcNewOamLpbkTimeoutDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcNewOamLpbkTimeoutDur.setStatus("current")
if mibBuilder.loadTexts:
    catsPvcNewOamLpbkTimeoutDur.setUnits("seconds")
_CatsPvcActiveOamLpbkTimeoutDur_Type = Unsigned32
_CatsPvcActiveOamLpbkTimeoutDur_Object = MibTableColumn
catsPvcActiveOamLpbkTimeoutDur = _CatsPvcActiveOamLpbkTimeoutDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 29),
    _CatsPvcActiveOamLpbkTimeoutDur_Type()
)
catsPvcActiveOamLpbkTimeoutDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcActiveOamLpbkTimeoutDur.setStatus("current")
if mibBuilder.loadTexts:
    catsPvcActiveOamLpbkTimeoutDur.setUnits("seconds")


class _CatsPvcOamLpbkTimeoutThreshold_Type(Unsigned32):
    """Custom type catsPvcOamLpbkTimeoutThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CatsPvcOamLpbkTimeoutThreshold_Type.__name__ = "Unsigned32"
_CatsPvcOamLpbkTimeoutThreshold_Object = MibTableColumn
catsPvcOamLpbkTimeoutThreshold = _CatsPvcOamLpbkTimeoutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 1, 1, 30),
    _CatsPvcOamLpbkTimeoutThreshold_Type()
)
catsPvcOamLpbkTimeoutThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsPvcOamLpbkTimeoutThreshold.setStatus("current")
if mibBuilder.loadTexts:
    catsPvcOamLpbkTimeoutThreshold.setUnits("seconds")
_CatsAal2PvcHistoryTable_Object = MibTable
catsAal2PvcHistoryTable = _CatsAal2PvcHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2)
)
if mibBuilder.loadTexts:
    catsAal2PvcHistoryTable.setStatus("current")
_CatsAal2PvcHistoryEntry_Object = MibTableRow
catsAal2PvcHistoryEntry = _CatsAal2PvcHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1)
)
catsAal2PvcHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcVpi"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcVci"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcIntervalIndex"),
)
if mibBuilder.loadTexts:
    catsAal2PvcHistoryEntry.setStatus("current")
_CatsAal2PvcVpi_Type = AtmVpIdentifier
_CatsAal2PvcVpi_Object = MibTableColumn
catsAal2PvcVpi = _CatsAal2PvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 1),
    _CatsAal2PvcVpi_Type()
)
catsAal2PvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsAal2PvcVpi.setStatus("current")
_CatsAal2PvcVci_Type = AtmVcIdentifier
_CatsAal2PvcVci_Object = MibTableColumn
catsAal2PvcVci = _CatsAal2PvcVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 2),
    _CatsAal2PvcVci_Type()
)
catsAal2PvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsAal2PvcVci.setStatus("current")


class _CatsAal2PvcIntervalIndex_Type(Unsigned32):
    """Custom type catsAal2PvcIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CatsAal2PvcIntervalIndex_Type.__name__ = "Unsigned32"
_CatsAal2PvcIntervalIndex_Object = MibTableColumn
catsAal2PvcIntervalIndex = _CatsAal2PvcIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 3),
    _CatsAal2PvcIntervalIndex_Type()
)
catsAal2PvcIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsAal2PvcIntervalIndex.setStatus("current")
_CatsAal2PvcValidFlag_Type = TruthValue
_CatsAal2PvcValidFlag_Object = MibTableColumn
catsAal2PvcValidFlag = _CatsAal2PvcValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 4),
    _CatsAal2PvcValidFlag_Type()
)
catsAal2PvcValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcValidFlag.setStatus("current")


class _CatsAal2PvcDiscontinuityTime_Type(TimeStamp):
    """Custom type catsAal2PvcDiscontinuityTime based on TimeStamp"""
    defaultValue = 0


_CatsAal2PvcDiscontinuityTime_Object = MibTableColumn
catsAal2PvcDiscontinuityTime = _CatsAal2PvcDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 5),
    _CatsAal2PvcDiscontinuityTime_Type()
)
catsAal2PvcDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcDiscontinuityTime.setStatus("current")
_CatsAal2PvcCpsSentPkts_Type = Counter32
_CatsAal2PvcCpsSentPkts_Object = MibTableColumn
catsAal2PvcCpsSentPkts = _CatsAal2PvcCpsSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 6),
    _CatsAal2PvcCpsSentPkts_Type()
)
catsAal2PvcCpsSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcCpsSentPkts.setStatus("current")
_CatsAal2PvcCpsRcvdPkts_Type = Counter32
_CatsAal2PvcCpsRcvdPkts_Object = MibTableColumn
catsAal2PvcCpsRcvdPkts = _CatsAal2PvcCpsRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 7),
    _CatsAal2PvcCpsRcvdPkts_Type()
)
catsAal2PvcCpsRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcCpsRcvdPkts.setStatus("current")
_CatsAal2PvcHecErrors_Type = Counter32
_CatsAal2PvcHecErrors_Object = MibTableColumn
catsAal2PvcHecErrors = _CatsAal2PvcHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 8),
    _CatsAal2PvcHecErrors_Type()
)
catsAal2PvcHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcHecErrors.setStatus("current")
_CatsAal2PvcCrcErrors_Type = Counter32
_CatsAal2PvcCrcErrors_Object = MibTableColumn
catsAal2PvcCrcErrors = _CatsAal2PvcCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 9),
    _CatsAal2PvcCrcErrors_Type()
)
catsAal2PvcCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcCrcErrors.setStatus("current")
_CatsAal2PvcInvOsfCells_Type = Counter32
_CatsAal2PvcInvOsfCells_Object = MibTableColumn
catsAal2PvcInvOsfCells = _CatsAal2PvcInvOsfCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 10),
    _CatsAal2PvcInvOsfCells_Type()
)
catsAal2PvcInvOsfCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcInvOsfCells.setStatus("current")
_CatsAal2PvcInvParCells_Type = Counter32
_CatsAal2PvcInvParCells_Object = MibTableColumn
catsAal2PvcInvParCells = _CatsAal2PvcInvParCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 11),
    _CatsAal2PvcInvParCells_Type()
)
catsAal2PvcInvParCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcInvParCells.setStatus("current")
_CatsAal2PvcCpsInvCidPkts_Type = Counter32
_CatsAal2PvcCpsInvCidPkts_Object = MibTableColumn
catsAal2PvcCpsInvCidPkts = _CatsAal2PvcCpsInvCidPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 12),
    _CatsAal2PvcCpsInvCidPkts_Type()
)
catsAal2PvcCpsInvCidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcCpsInvCidPkts.setStatus("current")
_CatsAal2PvcCpsInvUuiPkts_Type = Counter32
_CatsAal2PvcCpsInvUuiPkts_Object = MibTableColumn
catsAal2PvcCpsInvUuiPkts = _CatsAal2PvcCpsInvUuiPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 13),
    _CatsAal2PvcCpsInvUuiPkts_Type()
)
catsAal2PvcCpsInvUuiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcCpsInvUuiPkts.setStatus("current")
_CatsAal2PvcCpsInvLenPkts_Type = Counter32
_CatsAal2PvcCpsInvLenPkts_Object = MibTableColumn
catsAal2PvcCpsInvLenPkts = _CatsAal2PvcCpsInvLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 2, 1, 14),
    _CatsAal2PvcCpsInvLenPkts_Type()
)
catsAal2PvcCpsInvLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal2PvcCpsInvLenPkts.setStatus("current")
_CatsAal5PvcHistoryTable_Object = MibTable
catsAal5PvcHistoryTable = _CatsAal5PvcHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3)
)
if mibBuilder.loadTexts:
    catsAal5PvcHistoryTable.setStatus("current")
_CatsAal5PvcHistoryEntry_Object = MibTableRow
catsAal5PvcHistoryEntry = _CatsAal5PvcHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1)
)
catsAal5PvcHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcVpi"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcVci"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcIntervalIndex"),
)
if mibBuilder.loadTexts:
    catsAal5PvcHistoryEntry.setStatus("current")
_CatsAal5PvcVpi_Type = AtmVpIdentifier
_CatsAal5PvcVpi_Object = MibTableColumn
catsAal5PvcVpi = _CatsAal5PvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 1),
    _CatsAal5PvcVpi_Type()
)
catsAal5PvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsAal5PvcVpi.setStatus("current")
_CatsAal5PvcVci_Type = AtmVcIdentifier
_CatsAal5PvcVci_Object = MibTableColumn
catsAal5PvcVci = _CatsAal5PvcVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 2),
    _CatsAal5PvcVci_Type()
)
catsAal5PvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsAal5PvcVci.setStatus("current")


class _CatsAal5PvcIntervalIndex_Type(Unsigned32):
    """Custom type catsAal5PvcIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CatsAal5PvcIntervalIndex_Type.__name__ = "Unsigned32"
_CatsAal5PvcIntervalIndex_Object = MibTableColumn
catsAal5PvcIntervalIndex = _CatsAal5PvcIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 3),
    _CatsAal5PvcIntervalIndex_Type()
)
catsAal5PvcIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsAal5PvcIntervalIndex.setStatus("current")
_CatsAal5PvcValidFlag_Type = TruthValue
_CatsAal5PvcValidFlag_Object = MibTableColumn
catsAal5PvcValidFlag = _CatsAal5PvcValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 4),
    _CatsAal5PvcValidFlag_Type()
)
catsAal5PvcValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcValidFlag.setStatus("current")


class _CatsAal5PvcDiscontinuityTime_Type(TimeStamp):
    """Custom type catsAal5PvcDiscontinuityTime based on TimeStamp"""
    defaultValue = 0


_CatsAal5PvcDiscontinuityTime_Object = MibTableColumn
catsAal5PvcDiscontinuityTime = _CatsAal5PvcDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 5),
    _CatsAal5PvcDiscontinuityTime_Type()
)
catsAal5PvcDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcDiscontinuityTime.setStatus("current")
_CatsAal5PvcPduSentPkts_Type = Counter32
_CatsAal5PvcPduSentPkts_Object = MibTableColumn
catsAal5PvcPduSentPkts = _CatsAal5PvcPduSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 6),
    _CatsAal5PvcPduSentPkts_Type()
)
catsAal5PvcPduSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcPduSentPkts.setStatus("current")
_CatsAal5PvcPduRcvdPkts_Type = Counter32
_CatsAal5PvcPduRcvdPkts_Object = MibTableColumn
catsAal5PvcPduRcvdPkts = _CatsAal5PvcPduRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 7),
    _CatsAal5PvcPduRcvdPkts_Type()
)
catsAal5PvcPduRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcPduRcvdPkts.setStatus("current")
_CatsAal5PvcInvCpiPdus_Type = Counter32
_CatsAal5PvcInvCpiPdus_Object = MibTableColumn
catsAal5PvcInvCpiPdus = _CatsAal5PvcInvCpiPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 8),
    _CatsAal5PvcInvCpiPdus_Type()
)
catsAal5PvcInvCpiPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcInvCpiPdus.setStatus("current")
_CatsAal5PvcOverSizedSDUs_Type = Counter32
_CatsAal5PvcOverSizedSDUs_Object = MibTableColumn
catsAal5PvcOverSizedSDUs = _CatsAal5PvcOverSizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 9),
    _CatsAal5PvcOverSizedSDUs_Type()
)
catsAal5PvcOverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcOverSizedSDUs.setStatus("current")
_CatsAal5PvcInvLenPdus_Type = Counter32
_CatsAal5PvcInvLenPdus_Object = MibTableColumn
catsAal5PvcInvLenPdus = _CatsAal5PvcInvLenPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 10),
    _CatsAal5PvcInvLenPdus_Type()
)
catsAal5PvcInvLenPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcInvLenPdus.setStatus("current")
_CatsAal5PvcCrc32ErrorPdus_Type = Counter32
_CatsAal5PvcCrc32ErrorPdus_Object = MibTableColumn
catsAal5PvcCrc32ErrorPdus = _CatsAal5PvcCrc32ErrorPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 11),
    _CatsAal5PvcCrc32ErrorPdus_Type()
)
catsAal5PvcCrc32ErrorPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcCrc32ErrorPdus.setStatus("current")
_CatsAal5PvcReassemTimerExpiryPdus_Type = Counter32
_CatsAal5PvcReassemTimerExpiryPdus_Object = MibTableColumn
catsAal5PvcReassemTimerExpiryPdus = _CatsAal5PvcReassemTimerExpiryPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 3, 1, 12),
    _CatsAal5PvcReassemTimerExpiryPdus_Type()
)
catsAal5PvcReassemTimerExpiryPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsAal5PvcReassemTimerExpiryPdus.setStatus("current")
_CatsCidHistoryTable_Object = MibTable
catsCidHistoryTable = _CatsCidHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4)
)
if mibBuilder.loadTexts:
    catsCidHistoryTable.setStatus("current")
_CatsCidHistoryEntry_Object = MibTableRow
catsCidHistoryEntry = _CatsCidHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1)
)
catsCidHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsCidVpi"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsCidVci"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsCid"),
    (0, "CISCO-ATM-TRUNK-STAT-MIB", "catsCidIntervalIndex"),
)
if mibBuilder.loadTexts:
    catsCidHistoryEntry.setStatus("current")
_CatsCidVpi_Type = AtmVpIdentifier
_CatsCidVpi_Object = MibTableColumn
catsCidVpi = _CatsCidVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 1),
    _CatsCidVpi_Type()
)
catsCidVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsCidVpi.setStatus("current")
_CatsCidVci_Type = AtmVcIdentifier
_CatsCidVci_Object = MibTableColumn
catsCidVci = _CatsCidVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 2),
    _CatsCidVci_Type()
)
catsCidVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsCidVci.setStatus("current")


class _CatsCid_Type(Unsigned32):
    """Custom type catsCid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CatsCid_Type.__name__ = "Unsigned32"
_CatsCid_Object = MibTableColumn
catsCid = _CatsCid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 3),
    _CatsCid_Type()
)
catsCid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsCid.setStatus("current")


class _CatsCidIntervalIndex_Type(Unsigned32):
    """Custom type catsCidIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CatsCidIntervalIndex_Type.__name__ = "Unsigned32"
_CatsCidIntervalIndex_Object = MibTableColumn
catsCidIntervalIndex = _CatsCidIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 4),
    _CatsCidIntervalIndex_Type()
)
catsCidIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catsCidIntervalIndex.setStatus("current")
_CatsCidValidFlag_Type = TruthValue
_CatsCidValidFlag_Object = MibTableColumn
catsCidValidFlag = _CatsCidValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 5),
    _CatsCidValidFlag_Type()
)
catsCidValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidValidFlag.setStatus("current")


class _CatsCidDiscontinuityTime_Type(TimeStamp):
    """Custom type catsCidDiscontinuityTime based on TimeStamp"""
    defaultValue = 0


_CatsCidDiscontinuityTime_Object = MibTableColumn
catsCidDiscontinuityTime = _CatsCidDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 6),
    _CatsCidDiscontinuityTime_Type()
)
catsCidDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidDiscontinuityTime.setStatus("current")
_CatsCidAvgSentPkts_Type = Counter32
_CatsCidAvgSentPkts_Object = MibTableColumn
catsCidAvgSentPkts = _CatsCidAvgSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 7),
    _CatsCidAvgSentPkts_Type()
)
catsCidAvgSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidAvgSentPkts.setStatus("current")
if mibBuilder.loadTexts:
    catsCidAvgSentPkts.setUnits("packets-per-sec")
_CatsCidAvgRcvdPkts_Type = Counter32
_CatsCidAvgRcvdPkts_Object = MibTableColumn
catsCidAvgRcvdPkts = _CatsCidAvgRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 8),
    _CatsCidAvgRcvdPkts_Type()
)
catsCidAvgRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidAvgRcvdPkts.setStatus("current")
if mibBuilder.loadTexts:
    catsCidAvgRcvdPkts.setUnits("packets-per-sec")
_CatsCidSentPkts_Type = Counter32
_CatsCidSentPkts_Object = MibTableColumn
catsCidSentPkts = _CatsCidSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 9),
    _CatsCidSentPkts_Type()
)
catsCidSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidSentPkts.setStatus("current")
_CatsCidRcvdPkts_Type = Counter32
_CatsCidRcvdPkts_Object = MibTableColumn
catsCidRcvdPkts = _CatsCidRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 10),
    _CatsCidRcvdPkts_Type()
)
catsCidRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidRcvdPkts.setStatus("current")
_CatsCidSentOctets_Type = Counter32
_CatsCidSentOctets_Object = MibTableColumn
catsCidSentOctets = _CatsCidSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 11),
    _CatsCidSentOctets_Type()
)
catsCidSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidSentOctets.setStatus("current")
_CatsCidRcvdOctets_Type = Counter32
_CatsCidRcvdOctets_Object = MibTableColumn
catsCidRcvdOctets = _CatsCidRcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 12),
    _CatsCidRcvdOctets_Type()
)
catsCidRcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidRcvdOctets.setStatus("current")
_CatsCidSentPeakPkts_Type = Counter32
_CatsCidSentPeakPkts_Object = MibTableColumn
catsCidSentPeakPkts = _CatsCidSentPeakPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 13),
    _CatsCidSentPeakPkts_Type()
)
catsCidSentPeakPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidSentPeakPkts.setStatus("current")
if mibBuilder.loadTexts:
    catsCidSentPeakPkts.setUnits("packets-per-sec")
_CatsCidRcvdPeakPkts_Type = Counter32
_CatsCidRcvdPeakPkts_Object = MibTableColumn
catsCidRcvdPeakPkts = _CatsCidRcvdPeakPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 14),
    _CatsCidRcvdPeakPkts_Type()
)
catsCidRcvdPeakPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidRcvdPeakPkts.setStatus("current")
if mibBuilder.loadTexts:
    catsCidRcvdPeakPkts.setUnits("packets-per-sec")
_CatsCidExtAISRcvdPkts_Type = Counter32
_CatsCidExtAISRcvdPkts_Object = MibTableColumn
catsCidExtAISRcvdPkts = _CatsCidExtAISRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 15),
    _CatsCidExtAISRcvdPkts_Type()
)
catsCidExtAISRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtAISRcvdPkts.setStatus("current")
_CatsCidExtRAIRcvdPkts_Type = Counter32
_CatsCidExtRAIRcvdPkts_Object = MibTableColumn
catsCidExtRAIRcvdPkts = _CatsCidExtRAIRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 16),
    _CatsCidExtRAIRcvdPkts_Type()
)
catsCidExtRAIRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtRAIRcvdPkts.setStatus("current")
_CatsCidExtConnAISRcvdPkts_Type = Counter32
_CatsCidExtConnAISRcvdPkts_Object = MibTableColumn
catsCidExtConnAISRcvdPkts = _CatsCidExtConnAISRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 17),
    _CatsCidExtConnAISRcvdPkts_Type()
)
catsCidExtConnAISRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtConnAISRcvdPkts.setStatus("current")
_CatsCidExtConnRDIRcvdPkts_Type = Counter32
_CatsCidExtConnRDIRcvdPkts_Object = MibTableColumn
catsCidExtConnRDIRcvdPkts = _CatsCidExtConnRDIRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 18),
    _CatsCidExtConnRDIRcvdPkts_Type()
)
catsCidExtConnRDIRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtConnRDIRcvdPkts.setStatus("current")
_CatsCidExtAISRcvCnts_Type = Counter32
_CatsCidExtAISRcvCnts_Object = MibTableColumn
catsCidExtAISRcvCnts = _CatsCidExtAISRcvCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 19),
    _CatsCidExtAISRcvCnts_Type()
)
catsCidExtAISRcvCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtAISRcvCnts.setStatus("current")
_CatsCidExtRAIRcvCnts_Type = Counter32
_CatsCidExtRAIRcvCnts_Object = MibTableColumn
catsCidExtRAIRcvCnts = _CatsCidExtRAIRcvCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 20),
    _CatsCidExtRAIRcvCnts_Type()
)
catsCidExtRAIRcvCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtRAIRcvCnts.setStatus("current")
_CatsCidExtConnAISCnts_Type = Counter32
_CatsCidExtConnAISCnts_Object = MibTableColumn
catsCidExtConnAISCnts = _CatsCidExtConnAISCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 21),
    _CatsCidExtConnAISCnts_Type()
)
catsCidExtConnAISCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtConnAISCnts.setStatus("current")
_CatsCidExtConnRDICnts_Type = Counter32
_CatsCidExtConnRDICnts_Object = MibTableColumn
catsCidExtConnRDICnts = _CatsCidExtConnRDICnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 22),
    _CatsCidExtConnRDICnts_Type()
)
catsCidExtConnRDICnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtConnRDICnts.setStatus("current")
_CatsCidExtAISXmtCnts_Type = Counter32
_CatsCidExtAISXmtCnts_Object = MibTableColumn
catsCidExtAISXmtCnts = _CatsCidExtAISXmtCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 23),
    _CatsCidExtAISXmtCnts_Type()
)
catsCidExtAISXmtCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtAISXmtCnts.setStatus("current")
_CatsCidExtRAIXmtCnts_Type = Counter32
_CatsCidExtRAIXmtCnts_Object = MibTableColumn
catsCidExtRAIXmtCnts = _CatsCidExtRAIXmtCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 1, 1, 4, 1, 24),
    _CatsCidExtRAIXmtCnts_Type()
)
catsCidExtRAIXmtCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catsCidExtRAIXmtCnts.setStatus("current")
_CatsMIBConformance_ObjectIdentity = ObjectIdentity
catsMIBConformance = _CatsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2)
)
_CatsMIBGroups_ObjectIdentity = ObjectIdentity
catsMIBGroups = _CatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1)
)
_CatsMIBCompliances_ObjectIdentity = ObjectIdentity
catsMIBCompliances = _CatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 2)
)

# Managed Objects groups

catsPvcStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 1)
)
catsPvcStatGroup.setObjects(
      *(("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcValidFlag"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcDiscontinuityTime"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAtmXmtCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAtmRcvCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAvgAtmXmtCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAvgAtmRcvCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcPeakAtmXmtCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcPeakAtmRcvCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamXmtEndLpbkCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamRcvEndLpbkCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamXmtSegLpbkCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamRcvSegLpbkCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamLpbkLostCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcDiscardedRcvOamCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAisSuppressCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtAisCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvAisCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtFerfCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvFerfCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtAisCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvAisCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtFerfCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvFerfCells"))
)
if mibBuilder.loadTexts:
    catsPvcStatGroup.setStatus("deprecated")

catsAal2PvcStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 2)
)
catsAal2PvcStatGroup.setObjects(
      *(("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcValidFlag"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcDiscontinuityTime"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsSentPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsRcvdPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcHecErrors"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCrcErrors"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcInvOsfCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcInvParCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsInvCidPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsInvUuiPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal2PvcCpsInvLenPkts"))
)
if mibBuilder.loadTexts:
    catsAal2PvcStatGroup.setStatus("current")

catsAal5PvcStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 3)
)
catsAal5PvcStatGroup.setObjects(
      *(("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcValidFlag"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcDiscontinuityTime"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcPduSentPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcPduRcvdPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcInvCpiPdus"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcOverSizedSDUs"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcInvLenPdus"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcCrc32ErrorPdus"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsAal5PvcReassemTimerExpiryPdus"))
)
if mibBuilder.loadTexts:
    catsAal5PvcStatGroup.setStatus("current")

catsCidHistoryStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 4)
)
catsCidHistoryStatGroup.setObjects(
      *(("CISCO-ATM-TRUNK-STAT-MIB", "catsCidValidFlag"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidDiscontinuityTime"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidAvgSentPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidAvgRcvdPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidSentPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidRcvdPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidSentOctets"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidRcvdOctets"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidSentPeakPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidRcvdPeakPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtAISRcvdPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtRAIRcvdPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtConnAISRcvdPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtConnRDIRcvdPkts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtAISRcvCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtRAIRcvCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtConnAISCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtConnRDICnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtAISXmtCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsCidExtRAIXmtCnts"))
)
if mibBuilder.loadTexts:
    catsCidHistoryStatGroup.setStatus("current")

catsPvcStatGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 1, 5)
)
catsPvcStatGroupRev1.setObjects(
      *(("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcValidFlag"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcDiscontinuityTime"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAtmXmtCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAtmRcvCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAvgAtmXmtCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAvgAtmRcvCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcPeakAtmXmtCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcPeakAtmRcvCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamXmtEndLpbkCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamRcvEndLpbkCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamXmtSegLpbkCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamRcvSegLpbkCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamLpbkLostCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcDiscardedRcvOamCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcAisSuppressCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtAisCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvAisCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtFerfCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvFerfCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtAisCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvAisCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcXmtFerfCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcRcvFerfCells"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamLpbkTimeoutCnts"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcNewOamLpbkTimeoutDur"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcActiveOamLpbkTimeoutDur"),
        ("CISCO-ATM-TRUNK-STAT-MIB", "catsPvcOamLpbkTimeoutThreshold"))
)
if mibBuilder.loadTexts:
    catsPvcStatGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmPvcStatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmPvcStatMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAtmPvcStatMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 407, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoAtmPvcStatMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-TRUNK-STAT-MIB",
    **{"ciscoAtmTrunkStatMIB": ciscoAtmTrunkStatMIB,
       "ciscoAtmTrunkStatNotifs": ciscoAtmTrunkStatNotifs,
       "ciscoAtmTrunkStatObjects": ciscoAtmTrunkStatObjects,
       "catsStatistics": catsStatistics,
       "catsPvcHistoryTable": catsPvcHistoryTable,
       "catsPvcHistoryEntry": catsPvcHistoryEntry,
       "catsPvcVpi": catsPvcVpi,
       "catsPvcVci": catsPvcVci,
       "catsPvcIntervalIndex": catsPvcIntervalIndex,
       "catsPvcValidFlag": catsPvcValidFlag,
       "catsPvcDiscontinuityTime": catsPvcDiscontinuityTime,
       "catsPvcAtmXmtCells": catsPvcAtmXmtCells,
       "catsPvcAtmRcvCells": catsPvcAtmRcvCells,
       "catsPvcAvgAtmXmtCells": catsPvcAvgAtmXmtCells,
       "catsPvcAvgAtmRcvCells": catsPvcAvgAtmRcvCells,
       "catsPvcPeakAtmXmtCells": catsPvcPeakAtmXmtCells,
       "catsPvcPeakAtmRcvCells": catsPvcPeakAtmRcvCells,
       "catsPvcOamXmtEndLpbkCells": catsPvcOamXmtEndLpbkCells,
       "catsPvcOamRcvEndLpbkCells": catsPvcOamRcvEndLpbkCells,
       "catsPvcOamXmtSegLpbkCells": catsPvcOamXmtSegLpbkCells,
       "catsPvcOamRcvSegLpbkCells": catsPvcOamRcvSegLpbkCells,
       "catsPvcOamLpbkLostCells": catsPvcOamLpbkLostCells,
       "catsPvcDiscardedRcvOamCells": catsPvcDiscardedRcvOamCells,
       "catsPvcAisSuppressCnts": catsPvcAisSuppressCnts,
       "catsPvcXmtAisCnts": catsPvcXmtAisCnts,
       "catsPvcRcvAisCnts": catsPvcRcvAisCnts,
       "catsPvcXmtFerfCnts": catsPvcXmtFerfCnts,
       "catsPvcRcvFerfCnts": catsPvcRcvFerfCnts,
       "catsPvcXmtAisCells": catsPvcXmtAisCells,
       "catsPvcRcvAisCells": catsPvcRcvAisCells,
       "catsPvcXmtFerfCells": catsPvcXmtFerfCells,
       "catsPvcRcvFerfCells": catsPvcRcvFerfCells,
       "catsPvcOamLpbkTimeoutCnts": catsPvcOamLpbkTimeoutCnts,
       "catsPvcNewOamLpbkTimeoutDur": catsPvcNewOamLpbkTimeoutDur,
       "catsPvcActiveOamLpbkTimeoutDur": catsPvcActiveOamLpbkTimeoutDur,
       "catsPvcOamLpbkTimeoutThreshold": catsPvcOamLpbkTimeoutThreshold,
       "catsAal2PvcHistoryTable": catsAal2PvcHistoryTable,
       "catsAal2PvcHistoryEntry": catsAal2PvcHistoryEntry,
       "catsAal2PvcVpi": catsAal2PvcVpi,
       "catsAal2PvcVci": catsAal2PvcVci,
       "catsAal2PvcIntervalIndex": catsAal2PvcIntervalIndex,
       "catsAal2PvcValidFlag": catsAal2PvcValidFlag,
       "catsAal2PvcDiscontinuityTime": catsAal2PvcDiscontinuityTime,
       "catsAal2PvcCpsSentPkts": catsAal2PvcCpsSentPkts,
       "catsAal2PvcCpsRcvdPkts": catsAal2PvcCpsRcvdPkts,
       "catsAal2PvcHecErrors": catsAal2PvcHecErrors,
       "catsAal2PvcCrcErrors": catsAal2PvcCrcErrors,
       "catsAal2PvcInvOsfCells": catsAal2PvcInvOsfCells,
       "catsAal2PvcInvParCells": catsAal2PvcInvParCells,
       "catsAal2PvcCpsInvCidPkts": catsAal2PvcCpsInvCidPkts,
       "catsAal2PvcCpsInvUuiPkts": catsAal2PvcCpsInvUuiPkts,
       "catsAal2PvcCpsInvLenPkts": catsAal2PvcCpsInvLenPkts,
       "catsAal5PvcHistoryTable": catsAal5PvcHistoryTable,
       "catsAal5PvcHistoryEntry": catsAal5PvcHistoryEntry,
       "catsAal5PvcVpi": catsAal5PvcVpi,
       "catsAal5PvcVci": catsAal5PvcVci,
       "catsAal5PvcIntervalIndex": catsAal5PvcIntervalIndex,
       "catsAal5PvcValidFlag": catsAal5PvcValidFlag,
       "catsAal5PvcDiscontinuityTime": catsAal5PvcDiscontinuityTime,
       "catsAal5PvcPduSentPkts": catsAal5PvcPduSentPkts,
       "catsAal5PvcPduRcvdPkts": catsAal5PvcPduRcvdPkts,
       "catsAal5PvcInvCpiPdus": catsAal5PvcInvCpiPdus,
       "catsAal5PvcOverSizedSDUs": catsAal5PvcOverSizedSDUs,
       "catsAal5PvcInvLenPdus": catsAal5PvcInvLenPdus,
       "catsAal5PvcCrc32ErrorPdus": catsAal5PvcCrc32ErrorPdus,
       "catsAal5PvcReassemTimerExpiryPdus": catsAal5PvcReassemTimerExpiryPdus,
       "catsCidHistoryTable": catsCidHistoryTable,
       "catsCidHistoryEntry": catsCidHistoryEntry,
       "catsCidVpi": catsCidVpi,
       "catsCidVci": catsCidVci,
       "catsCid": catsCid,
       "catsCidIntervalIndex": catsCidIntervalIndex,
       "catsCidValidFlag": catsCidValidFlag,
       "catsCidDiscontinuityTime": catsCidDiscontinuityTime,
       "catsCidAvgSentPkts": catsCidAvgSentPkts,
       "catsCidAvgRcvdPkts": catsCidAvgRcvdPkts,
       "catsCidSentPkts": catsCidSentPkts,
       "catsCidRcvdPkts": catsCidRcvdPkts,
       "catsCidSentOctets": catsCidSentOctets,
       "catsCidRcvdOctets": catsCidRcvdOctets,
       "catsCidSentPeakPkts": catsCidSentPeakPkts,
       "catsCidRcvdPeakPkts": catsCidRcvdPeakPkts,
       "catsCidExtAISRcvdPkts": catsCidExtAISRcvdPkts,
       "catsCidExtRAIRcvdPkts": catsCidExtRAIRcvdPkts,
       "catsCidExtConnAISRcvdPkts": catsCidExtConnAISRcvdPkts,
       "catsCidExtConnRDIRcvdPkts": catsCidExtConnRDIRcvdPkts,
       "catsCidExtAISRcvCnts": catsCidExtAISRcvCnts,
       "catsCidExtRAIRcvCnts": catsCidExtRAIRcvCnts,
       "catsCidExtConnAISCnts": catsCidExtConnAISCnts,
       "catsCidExtConnRDICnts": catsCidExtConnRDICnts,
       "catsCidExtAISXmtCnts": catsCidExtAISXmtCnts,
       "catsCidExtRAIXmtCnts": catsCidExtRAIXmtCnts,
       "catsMIBConformance": catsMIBConformance,
       "catsMIBGroups": catsMIBGroups,
       "catsPvcStatGroup": catsPvcStatGroup,
       "catsAal2PvcStatGroup": catsAal2PvcStatGroup,
       "catsAal5PvcStatGroup": catsAal5PvcStatGroup,
       "catsCidHistoryStatGroup": catsCidHistoryStatGroup,
       "catsPvcStatGroupRev1": catsPvcStatGroupRev1,
       "catsMIBCompliances": catsMIBCompliances,
       "ciscoAtmPvcStatMIBCompliance": ciscoAtmPvcStatMIBCompliance,
       "ciscoAtmPvcStatMIBComplianceRev1": ciscoAtmPvcStatMIBComplianceRev1}
)
