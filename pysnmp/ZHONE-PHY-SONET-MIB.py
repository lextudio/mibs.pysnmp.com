# SNMP MIB module (ZHONE-PHY-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-PHY-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:39 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(sonetLineCurrentStatus,
 sonetMediumEntry,
 sonetPathCurrentStatus,
 sonetSectionCurrentStatus) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetLineCurrentStatus",
    "sonetMediumEntry",
    "sonetPathCurrentStatus",
    "sonetSectionCurrentStatus")

(zhoneModules,
 zhoneSonet) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneSonet")


# MODULE-IDENTITY

phySonet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 16)
)
phySonet.setRevisions(
        ("2004-08-18 11:47",
         "2003-07-10 13:30",
         "2002-03-26 14:30",
         "2001-09-12 15:08",
         "2001-07-19 18:00",
         "2001-02-22 11:35",
         "2000-12-19 15:23",
         "2000-12-18 16:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetClockTable_Object = MibTable
sonetClockTable = _SonetClockTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 1)
)
if mibBuilder.loadTexts:
    sonetClockTable.setStatus("current")
_SonetClockEntry_Object = MibTableRow
sonetClockEntry = _SonetClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sonetClockEntry.setStatus("current")


class _SonetClockExternalRecovery_Type(Integer32):
    """Custom type sonetClockExternalRecovery based on Integer32"""
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


_SonetClockExternalRecovery_Type.__name__ = "Integer32"
_SonetClockExternalRecovery_Object = MibTableColumn
sonetClockExternalRecovery = _SonetClockExternalRecovery_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 1, 1, 1),
    _SonetClockExternalRecovery_Type()
)
sonetClockExternalRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClockExternalRecovery.setStatus("current")


class _SonetClockTransmitSource_Type(Integer32):
    """Custom type sonetClockTransmitSource based on Integer32"""
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
        *(("external155MHz", 4),
          ("localTiming", 3),
          ("loopTiming", 1),
          ("throughTiming", 2))
    )


_SonetClockTransmitSource_Type.__name__ = "Integer32"
_SonetClockTransmitSource_Object = MibTableColumn
sonetClockTransmitSource = _SonetClockTransmitSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 1, 1, 2),
    _SonetClockTransmitSource_Type()
)
sonetClockTransmitSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClockTransmitSource.setStatus("current")
_SonetMediumExtTable_Object = MibTable
sonetMediumExtTable = _SonetMediumExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 2)
)
if mibBuilder.loadTexts:
    sonetMediumExtTable.setStatus("current")
_SonetMediumExtEntry_Object = MibTableRow
sonetMediumExtEntry = _SonetMediumExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 2, 1)
)
if mibBuilder.loadTexts:
    sonetMediumExtEntry.setStatus("current")


class _SonetMediumExtScrambleEnabled_Type(TruthValue):
    """Custom type sonetMediumExtScrambleEnabled based on TruthValue"""


_SonetMediumExtScrambleEnabled_Object = MibTableColumn
sonetMediumExtScrambleEnabled = _SonetMediumExtScrambleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 2, 1, 1),
    _SonetMediumExtScrambleEnabled_Type()
)
sonetMediumExtScrambleEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetMediumExtScrambleEnabled.setStatus("current")


class _SonetMediumExtLineScrmEnabled_Type(TruthValue):
    """Custom type sonetMediumExtLineScrmEnabled based on TruthValue"""


_SonetMediumExtLineScrmEnabled_Object = MibTableColumn
sonetMediumExtLineScrmEnabled = _SonetMediumExtLineScrmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 2, 1, 2),
    _SonetMediumExtLineScrmEnabled_Type()
)
sonetMediumExtLineScrmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetMediumExtLineScrmEnabled.setStatus("current")
_SonetTraps_ObjectIdentity = ObjectIdentity
sonetTraps = _SonetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 3)
)
if mibBuilder.loadTexts:
    sonetTraps.setStatus("current")
_SonetV2Traps_ObjectIdentity = ObjectIdentity
sonetV2Traps = _SonetV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 3, 0)
)
if mibBuilder.loadTexts:
    sonetV2Traps.setStatus("current")
_ZhoneSonetErrorStatsTable_Object = MibTable
zhoneSonetErrorStatsTable = _ZhoneSonetErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6)
)
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsTable.setStatus("current")
_ZhoneSonetErrorStatsEntry_Object = MibTableRow
zhoneSonetErrorStatsEntry = _ZhoneSonetErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1)
)
zhoneSonetErrorStatsEntry.setIndexNames(
    (0, "ZHONE-PHY-SONET-MIB", "zhoneSonetErrorStatsIndex"),
)
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsEntry.setStatus("current")
_ZhoneSonetErrorStatsIndex_Type = InterfaceIndex
_ZhoneSonetErrorStatsIndex_Object = MibTableColumn
zhoneSonetErrorStatsIndex = _ZhoneSonetErrorStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 1),
    _ZhoneSonetErrorStatsIndex_Type()
)
zhoneSonetErrorStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsIndex.setStatus("current")
_ZhoneSonetErrorStatsLineFebeCount_Type = Integer32
_ZhoneSonetErrorStatsLineFebeCount_Object = MibTableColumn
zhoneSonetErrorStatsLineFebeCount = _ZhoneSonetErrorStatsLineFebeCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 2),
    _ZhoneSonetErrorStatsLineFebeCount_Type()
)
zhoneSonetErrorStatsLineFebeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsLineFebeCount.setStatus("current")
_ZhoneSonetErrorStatsPathFebeCount_Type = Integer32
_ZhoneSonetErrorStatsPathFebeCount_Object = MibTableColumn
zhoneSonetErrorStatsPathFebeCount = _ZhoneSonetErrorStatsPathFebeCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 3),
    _ZhoneSonetErrorStatsPathFebeCount_Type()
)
zhoneSonetErrorStatsPathFebeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsPathFebeCount.setStatus("current")
_ZhoneSonetErrorStatsLineBipCount_Type = Integer32
_ZhoneSonetErrorStatsLineBipCount_Object = MibTableColumn
zhoneSonetErrorStatsLineBipCount = _ZhoneSonetErrorStatsLineBipCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 4),
    _ZhoneSonetErrorStatsLineBipCount_Type()
)
zhoneSonetErrorStatsLineBipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsLineBipCount.setStatus("current")
_ZhoneSonetErrorStatsSectionBipCount_Type = Integer32
_ZhoneSonetErrorStatsSectionBipCount_Object = MibTableColumn
zhoneSonetErrorStatsSectionBipCount = _ZhoneSonetErrorStatsSectionBipCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 5),
    _ZhoneSonetErrorStatsSectionBipCount_Type()
)
zhoneSonetErrorStatsSectionBipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsSectionBipCount.setStatus("current")
_ZhoneSonetErrorStatsPathBipCount_Type = Integer32
_ZhoneSonetErrorStatsPathBipCount_Object = MibTableColumn
zhoneSonetErrorStatsPathBipCount = _ZhoneSonetErrorStatsPathBipCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 6),
    _ZhoneSonetErrorStatsPathBipCount_Type()
)
zhoneSonetErrorStatsPathBipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsPathBipCount.setStatus("current")
_ZhoneSonetErrorStatsOofCount_Type = Integer32
_ZhoneSonetErrorStatsOofCount_Object = MibTableColumn
zhoneSonetErrorStatsOofCount = _ZhoneSonetErrorStatsOofCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 7),
    _ZhoneSonetErrorStatsOofCount_Type()
)
zhoneSonetErrorStatsOofCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsOofCount.setStatus("current")
_ZhoneSonetErrorStatsRxCellCount_Type = Integer32
_ZhoneSonetErrorStatsRxCellCount_Object = MibTableColumn
zhoneSonetErrorStatsRxCellCount = _ZhoneSonetErrorStatsRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 8),
    _ZhoneSonetErrorStatsRxCellCount_Type()
)
zhoneSonetErrorStatsRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsRxCellCount.setStatus("current")
_ZhoneSonetErrorStatsTxCellCount_Type = Integer32
_ZhoneSonetErrorStatsTxCellCount_Object = MibTableColumn
zhoneSonetErrorStatsTxCellCount = _ZhoneSonetErrorStatsTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 9),
    _ZhoneSonetErrorStatsTxCellCount_Type()
)
zhoneSonetErrorStatsTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsTxCellCount.setStatus("current")
_ZhoneSonetErrorStatsHecCorrectedCount_Type = Integer32
_ZhoneSonetErrorStatsHecCorrectedCount_Object = MibTableColumn
zhoneSonetErrorStatsHecCorrectedCount = _ZhoneSonetErrorStatsHecCorrectedCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 10),
    _ZhoneSonetErrorStatsHecCorrectedCount_Type()
)
zhoneSonetErrorStatsHecCorrectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsHecCorrectedCount.setStatus("current")
_ZhoneSonetErrorStatsHecUncorrectedCount_Type = Integer32
_ZhoneSonetErrorStatsHecUncorrectedCount_Object = MibTableColumn
zhoneSonetErrorStatsHecUncorrectedCount = _ZhoneSonetErrorStatsHecUncorrectedCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 11),
    _ZhoneSonetErrorStatsHecUncorrectedCount_Type()
)
zhoneSonetErrorStatsHecUncorrectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsHecUncorrectedCount.setStatus("current")
_ZhoneSonetErrorStatsCellFifoOverflowCount_Type = Integer32
_ZhoneSonetErrorStatsCellFifoOverflowCount_Object = MibTableColumn
zhoneSonetErrorStatsCellFifoOverflowCount = _ZhoneSonetErrorStatsCellFifoOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 12),
    _ZhoneSonetErrorStatsCellFifoOverflowCount_Type()
)
zhoneSonetErrorStatsCellFifoOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsCellFifoOverflowCount.setStatus("current")
_ZhoneSonetErrorStatsLocdCount_Type = Integer32
_ZhoneSonetErrorStatsLocdCount_Object = MibTableColumn
zhoneSonetErrorStatsLocdCount = _ZhoneSonetErrorStatsLocdCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 6, 1, 13),
    _ZhoneSonetErrorStatsLocdCount_Type()
)
zhoneSonetErrorStatsLocdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSonetErrorStatsLocdCount.setStatus("current")
sonetMediumEntry.registerAugmentions(
    ("ZHONE-PHY-SONET-MIB",
     "sonetClockEntry")
)
sonetClockEntry.setIndexNames(*sonetMediumEntry.getIndexNames())
sonetMediumEntry.registerAugmentions(
    ("ZHONE-PHY-SONET-MIB",
     "sonetMediumExtEntry")
)
sonetMediumExtEntry.setIndexNames(*sonetMediumEntry.getIndexNames())

# Managed Objects groups


# Notification objects

sonetClockTransmitSourceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 3, 0, 1)
)
sonetClockTransmitSourceChange.setObjects(
      *(("ZHONE-PHY-SONET-MIB", "sonetClockExternalRecovery"),
        ("ZHONE-PHY-SONET-MIB", "sonetClockTransmitSource"))
)
if mibBuilder.loadTexts:
    sonetClockTransmitSourceChange.setStatus(
        "current"
    )

sonetSectionStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 3, 0, 2)
)
sonetSectionStatusChange.setObjects(
    ("SONET-MIB", "sonetSectionCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetSectionStatusChange.setStatus(
        "current"
    )

sonetLineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 3, 0, 3)
)
sonetLineStatusChange.setObjects(
    ("SONET-MIB", "sonetLineCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetLineStatusChange.setStatus(
        "current"
    )

sonetPathStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 9, 3, 0, 4)
)
sonetPathStatusChange.setObjects(
    ("SONET-MIB", "sonetPathCurrentStatus")
)
if mibBuilder.loadTexts:
    sonetPathStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-PHY-SONET-MIB",
    **{"sonetClockTable": sonetClockTable,
       "sonetClockEntry": sonetClockEntry,
       "sonetClockExternalRecovery": sonetClockExternalRecovery,
       "sonetClockTransmitSource": sonetClockTransmitSource,
       "sonetMediumExtTable": sonetMediumExtTable,
       "sonetMediumExtEntry": sonetMediumExtEntry,
       "sonetMediumExtScrambleEnabled": sonetMediumExtScrambleEnabled,
       "sonetMediumExtLineScrmEnabled": sonetMediumExtLineScrmEnabled,
       "sonetTraps": sonetTraps,
       "sonetV2Traps": sonetV2Traps,
       "sonetClockTransmitSourceChange": sonetClockTransmitSourceChange,
       "sonetSectionStatusChange": sonetSectionStatusChange,
       "sonetLineStatusChange": sonetLineStatusChange,
       "sonetPathStatusChange": sonetPathStatusChange,
       "zhoneSonetErrorStatsTable": zhoneSonetErrorStatsTable,
       "zhoneSonetErrorStatsEntry": zhoneSonetErrorStatsEntry,
       "zhoneSonetErrorStatsIndex": zhoneSonetErrorStatsIndex,
       "zhoneSonetErrorStatsLineFebeCount": zhoneSonetErrorStatsLineFebeCount,
       "zhoneSonetErrorStatsPathFebeCount": zhoneSonetErrorStatsPathFebeCount,
       "zhoneSonetErrorStatsLineBipCount": zhoneSonetErrorStatsLineBipCount,
       "zhoneSonetErrorStatsSectionBipCount": zhoneSonetErrorStatsSectionBipCount,
       "zhoneSonetErrorStatsPathBipCount": zhoneSonetErrorStatsPathBipCount,
       "zhoneSonetErrorStatsOofCount": zhoneSonetErrorStatsOofCount,
       "zhoneSonetErrorStatsRxCellCount": zhoneSonetErrorStatsRxCellCount,
       "zhoneSonetErrorStatsTxCellCount": zhoneSonetErrorStatsTxCellCount,
       "zhoneSonetErrorStatsHecCorrectedCount": zhoneSonetErrorStatsHecCorrectedCount,
       "zhoneSonetErrorStatsHecUncorrectedCount": zhoneSonetErrorStatsHecUncorrectedCount,
       "zhoneSonetErrorStatsCellFifoOverflowCount": zhoneSonetErrorStatsCellFifoOverflowCount,
       "zhoneSonetErrorStatsLocdCount": zhoneSonetErrorStatsLocdCount,
       "phySonet": phySonet}
)
