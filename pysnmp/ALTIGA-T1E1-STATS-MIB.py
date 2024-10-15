# SNMP MIB module (ALTIGA-T1E1-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-T1E1-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:25 2024
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

(alT1E1MibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alT1E1MibModule")

(alStatsT1E1,
 alT1E1Group) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alStatsT1E1",
    "alT1E1Group")

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

altigaT1E1StatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 38, 2)
)
altigaT1E1StatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaT1E1StatsMibConformance_ObjectIdentity = ObjectIdentity
altigaT1E1StatsMibConformance = _AltigaT1E1StatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 38, 2, 1)
)
_AltigaT1E1StatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaT1E1StatsMibCompliances = _AltigaT1E1StatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 38, 2, 1, 1)
)
_AlStatsT1E1Global_ObjectIdentity = ObjectIdentity
alStatsT1E1Global = _AlStatsT1E1Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 1)
)
_AlT1E1StatsTable_Object = MibTable
alT1E1StatsTable = _AlT1E1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2)
)
if mibBuilder.loadTexts:
    alT1E1StatsTable.setStatus("current")
_AlT1E1StatsEntry_Object = MibTableRow
alT1E1StatsEntry = _AlT1E1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1)
)
alT1E1StatsEntry.setIndexNames(
    (0, "ALTIGA-T1E1-STATS-MIB", "alT1E1StatsSlot"),
    (0, "ALTIGA-T1E1-STATS-MIB", "alT1E1StatsConn"),
)
if mibBuilder.loadTexts:
    alT1E1StatsEntry.setStatus("current")
_AlT1E1StatsRowStatus_Type = RowStatus
_AlT1E1StatsRowStatus_Object = MibTableColumn
alT1E1StatsRowStatus = _AlT1E1StatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 1),
    _AlT1E1StatsRowStatus_Type()
)
alT1E1StatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alT1E1StatsRowStatus.setStatus("current")
_AlT1E1StatsSlot_Type = Integer32
_AlT1E1StatsSlot_Object = MibTableColumn
alT1E1StatsSlot = _AlT1E1StatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 2),
    _AlT1E1StatsSlot_Type()
)
alT1E1StatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsSlot.setStatus("current")
_AlT1E1StatsConn_Type = Integer32
_AlT1E1StatsConn_Object = MibTableColumn
alT1E1StatsConn = _AlT1E1StatsConn_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 3),
    _AlT1E1StatsConn_Type()
)
alT1E1StatsConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsConn.setStatus("current")


class _AlT1E1StatsLineStatus_Type(Integer32):
    """Custom type alT1E1StatsLineStatus based on Integer32"""
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
        *(("blue", 4),
          ("init", 1),
          ("loopback", 6),
          ("red", 3),
          ("up", 2),
          ("yellow", 5))
    )


_AlT1E1StatsLineStatus_Type.__name__ = "Integer32"
_AlT1E1StatsLineStatus_Object = MibTableColumn
alT1E1StatsLineStatus = _AlT1E1StatsLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 4),
    _AlT1E1StatsLineStatus_Type()
)
alT1E1StatsLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsLineStatus.setStatus("current")
_AlT1E1StatsElapsedSecs_Type = Counter32
_AlT1E1StatsElapsedSecs_Object = MibTableColumn
alT1E1StatsElapsedSecs = _AlT1E1StatsElapsedSecs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 5),
    _AlT1E1StatsElapsedSecs_Type()
)
alT1E1StatsElapsedSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsElapsedSecs.setStatus("current")
_AlT1E1StatsBPVs_Type = Counter32
_AlT1E1StatsBPVs_Object = MibTableColumn
alT1E1StatsBPVs = _AlT1E1StatsBPVs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 6),
    _AlT1E1StatsBPVs_Type()
)
alT1E1StatsBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsBPVs.setStatus("current")
_AlT1E1StatsESs_Type = Counter32
_AlT1E1StatsESs_Object = MibTableColumn
alT1E1StatsESs = _AlT1E1StatsESs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 7),
    _AlT1E1StatsESs_Type()
)
alT1E1StatsESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsESs.setStatus("current")
_AlT1E1StatsSESs_Type = Counter32
_AlT1E1StatsSESs_Object = MibTableColumn
alT1E1StatsSESs = _AlT1E1StatsSESs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 8),
    _AlT1E1StatsSESs_Type()
)
alT1E1StatsSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsSESs.setStatus("current")
_AlT1E1StatsBESs_Type = Counter32
_AlT1E1StatsBESs_Object = MibTableColumn
alT1E1StatsBESs = _AlT1E1StatsBESs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 9),
    _AlT1E1StatsBESs_Type()
)
alT1E1StatsBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsBESs.setStatus("current")
_AlT1E1StatsSEFSs_Type = Counter32
_AlT1E1StatsSEFSs_Object = MibTableColumn
alT1E1StatsSEFSs = _AlT1E1StatsSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 10),
    _AlT1E1StatsSEFSs_Type()
)
alT1E1StatsSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsSEFSs.setStatus("current")
_AlT1E1StatsUASs_Type = Counter32
_AlT1E1StatsUASs_Object = MibTableColumn
alT1E1StatsUASs = _AlT1E1StatsUASs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 11),
    _AlT1E1StatsUASs_Type()
)
alT1E1StatsUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsUASs.setStatus("current")
_AlT1E1StatsLCVs_Type = Counter32
_AlT1E1StatsLCVs_Object = MibTableColumn
alT1E1StatsLCVs = _AlT1E1StatsLCVs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 12),
    _AlT1E1StatsLCVs_Type()
)
alT1E1StatsLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsLCVs.setStatus("current")
_AlT1E1StatsCSSs_Type = Counter32
_AlT1E1StatsCSSs_Object = MibTableColumn
alT1E1StatsCSSs = _AlT1E1StatsCSSs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 13),
    _AlT1E1StatsCSSs_Type()
)
alT1E1StatsCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsCSSs.setStatus("current")
_AlT1E1StatsDMs_Type = Counter32
_AlT1E1StatsDMs_Object = MibTableColumn
alT1E1StatsDMs = _AlT1E1StatsDMs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 14),
    _AlT1E1StatsDMs_Type()
)
alT1E1StatsDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsDMs.setStatus("current")
_AlT1E1StatsPCVs_Type = Counter32
_AlT1E1StatsPCVs_Object = MibTableColumn
alT1E1StatsPCVs = _AlT1E1StatsPCVs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 15),
    _AlT1E1StatsPCVs_Type()
)
alT1E1StatsPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsPCVs.setStatus("current")
_AlT1E1StatsLESs_Type = Counter32
_AlT1E1StatsLESs_Object = MibTableColumn
alT1E1StatsLESs = _AlT1E1StatsLESs_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 33, 2, 1, 16),
    _AlT1E1StatsLESs_Type()
)
alT1E1StatsLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alT1E1StatsLESs.setStatus("current")

# Managed Objects groups

altigaT1E1StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 33, 2)
)
altigaT1E1StatsGroup.setObjects(
      *(("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsRowStatus"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsSlot"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsConn"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsLineStatus"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsElapsedSecs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsBPVs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsESs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsSESs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsBESs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsSEFSs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsUASs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsLCVs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsCSSs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsDMs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsPCVs"),
        ("ALTIGA-T1E1-STATS-MIB", "alT1E1StatsLESs"))
)
if mibBuilder.loadTexts:
    altigaT1E1StatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaT1E1StatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 38, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaT1E1StatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-T1E1-STATS-MIB",
    **{"altigaT1E1StatsMibModule": altigaT1E1StatsMibModule,
       "altigaT1E1StatsMibConformance": altigaT1E1StatsMibConformance,
       "altigaT1E1StatsMibCompliances": altigaT1E1StatsMibCompliances,
       "altigaT1E1StatsMibCompliance": altigaT1E1StatsMibCompliance,
       "altigaT1E1StatsGroup": altigaT1E1StatsGroup,
       "alStatsT1E1Global": alStatsT1E1Global,
       "alT1E1StatsTable": alT1E1StatsTable,
       "alT1E1StatsEntry": alT1E1StatsEntry,
       "alT1E1StatsRowStatus": alT1E1StatsRowStatus,
       "alT1E1StatsSlot": alT1E1StatsSlot,
       "alT1E1StatsConn": alT1E1StatsConn,
       "alT1E1StatsLineStatus": alT1E1StatsLineStatus,
       "alT1E1StatsElapsedSecs": alT1E1StatsElapsedSecs,
       "alT1E1StatsBPVs": alT1E1StatsBPVs,
       "alT1E1StatsESs": alT1E1StatsESs,
       "alT1E1StatsSESs": alT1E1StatsSESs,
       "alT1E1StatsBESs": alT1E1StatsBESs,
       "alT1E1StatsSEFSs": alT1E1StatsSEFSs,
       "alT1E1StatsUASs": alT1E1StatsUASs,
       "alT1E1StatsLCVs": alT1E1StatsLCVs,
       "alT1E1StatsCSSs": alT1E1StatsCSSs,
       "alT1E1StatsDMs": alT1E1StatsDMs,
       "alT1E1StatsPCVs": alT1E1StatsPCVs,
       "alT1E1StatsLESs": alT1E1StatsLESs}
)
