# SNMP MIB module (ALTIGA-HTTP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-HTTP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:13 2024
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

(alHttpMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alHttpMibModule")

(alHttpGroup,
 alStatsHttp) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alHttpGroup",
    "alStatsHttp")

(EncryptionAlgorithm,) = mibBuilder.importSymbols(
    "ALTIGA-SESSION-STATS-MIB",
    "EncryptionAlgorithm")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

altigaHttpStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 12, 2)
)
altigaHttpStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaHttpStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaHttpStatsMibConformance = _AltigaHttpStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 12, 2, 1)
)
_AltigaHttpStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaHttpStatsMibCompliances = _AltigaHttpStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 12, 2, 1, 1)
)
_AlStatsHttpGlobal_ObjectIdentity = ObjectIdentity
alStatsHttpGlobal = _AlStatsHttpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1)
)
_AlHttpStatsOctetsSent_Type = Counter32
_AlHttpStatsOctetsSent_Object = MibScalar
alHttpStatsOctetsSent = _AlHttpStatsOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 1),
    _AlHttpStatsOctetsSent_Type()
)
alHttpStatsOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsOctetsSent.setStatus("current")
_AlHttpStatsOctetsRcvd_Type = Counter32
_AlHttpStatsOctetsRcvd_Object = MibScalar
alHttpStatsOctetsRcvd = _AlHttpStatsOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 2),
    _AlHttpStatsOctetsRcvd_Type()
)
alHttpStatsOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsOctetsRcvd.setStatus("current")
_AlHttpStatsPacketsSent_Type = Counter32
_AlHttpStatsPacketsSent_Object = MibScalar
alHttpStatsPacketsSent = _AlHttpStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 3),
    _AlHttpStatsPacketsSent_Type()
)
alHttpStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsPacketsSent.setStatus("current")
_AlHttpStatsPacketsRcvd_Type = Counter32
_AlHttpStatsPacketsRcvd_Object = MibScalar
alHttpStatsPacketsRcvd = _AlHttpStatsPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 4),
    _AlHttpStatsPacketsRcvd_Type()
)
alHttpStatsPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsPacketsRcvd.setStatus("current")
_AlHttpStatsActiveConnections_Type = Gauge32
_AlHttpStatsActiveConnections_Object = MibScalar
alHttpStatsActiveConnections = _AlHttpStatsActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 5),
    _AlHttpStatsActiveConnections_Type()
)
alHttpStatsActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsActiveConnections.setStatus("current")
_AlHttpStatsMaxConnections_Type = Counter32
_AlHttpStatsMaxConnections_Object = MibScalar
alHttpStatsMaxConnections = _AlHttpStatsMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 6),
    _AlHttpStatsMaxConnections_Type()
)
alHttpStatsMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsMaxConnections.setStatus("current")
_AlHttpStatsActiveSessions_Type = Gauge32
_AlHttpStatsActiveSessions_Object = MibScalar
alHttpStatsActiveSessions = _AlHttpStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 7),
    _AlHttpStatsActiveSessions_Type()
)
alHttpStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsActiveSessions.setStatus("current")
_AlHttpStatsMaxSessions_Type = Counter32
_AlHttpStatsMaxSessions_Object = MibScalar
alHttpStatsMaxSessions = _AlHttpStatsMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 8),
    _AlHttpStatsMaxSessions_Type()
)
alHttpStatsMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsMaxSessions.setStatus("current")
_AlHttpStatsTotalConnections_Type = Counter32
_AlHttpStatsTotalConnections_Object = MibScalar
alHttpStatsTotalConnections = _AlHttpStatsTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 9),
    _AlHttpStatsTotalConnections_Type()
)
alHttpStatsTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsTotalConnections.setStatus("current")
_AlHttpStatsTotalSessions_Type = Counter32
_AlHttpStatsTotalSessions_Object = MibScalar
alHttpStatsTotalSessions = _AlHttpStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 1, 10),
    _AlHttpStatsTotalSessions_Type()
)
alHttpStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsTotalSessions.setStatus("current")
_AlHttpStatsSessionTable_Object = MibTable
alHttpStatsSessionTable = _AlHttpStatsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    alHttpStatsSessionTable.setStatus("current")
_AlHttpStatsSessionEntry_Object = MibTableRow
alHttpStatsSessionEntry = _AlHttpStatsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1)
)
alHttpStatsSessionEntry.setIndexNames(
    (0, "ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionIndex"),
)
if mibBuilder.loadTexts:
    alHttpStatsSessionEntry.setStatus("current")
_AlHttpStatsSessionIndex_Type = Integer32
_AlHttpStatsSessionIndex_Object = MibTableColumn
alHttpStatsSessionIndex = _AlHttpStatsSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 1),
    _AlHttpStatsSessionIndex_Type()
)
alHttpStatsSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionIndex.setStatus("current")
_AlHttpStatsSessionName_Type = DisplayString
_AlHttpStatsSessionName_Object = MibTableColumn
alHttpStatsSessionName = _AlHttpStatsSessionName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 2),
    _AlHttpStatsSessionName_Type()
)
alHttpStatsSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionName.setStatus("current")
_AlHttpStatsSessionIpAddr_Type = IpAddress
_AlHttpStatsSessionIpAddr_Object = MibTableColumn
alHttpStatsSessionIpAddr = _AlHttpStatsSessionIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 3),
    _AlHttpStatsSessionIpAddr_Type()
)
alHttpStatsSessionIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionIpAddr.setStatus("current")
_AlHttpStatsSessionStartTime_Type = TimeTicks
_AlHttpStatsSessionStartTime_Object = MibTableColumn
alHttpStatsSessionStartTime = _AlHttpStatsSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 4),
    _AlHttpStatsSessionStartTime_Type()
)
alHttpStatsSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionStartTime.setStatus("current")
_AlHttpStatsSessionLoginTime_Type = Unsigned32
_AlHttpStatsSessionLoginTime_Object = MibTableColumn
alHttpStatsSessionLoginTime = _AlHttpStatsSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 5),
    _AlHttpStatsSessionLoginTime_Type()
)
alHttpStatsSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionLoginTime.setStatus("current")
_AlHttpStatsSessionEncr_Type = EncryptionAlgorithm
_AlHttpStatsSessionEncr_Object = MibTableColumn
alHttpStatsSessionEncr = _AlHttpStatsSessionEncr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 6),
    _AlHttpStatsSessionEncr_Type()
)
alHttpStatsSessionEncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionEncr.setStatus("current")
_AlHttpStatsSessionOctetsSent_Type = Counter32
_AlHttpStatsSessionOctetsSent_Object = MibTableColumn
alHttpStatsSessionOctetsSent = _AlHttpStatsSessionOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 7),
    _AlHttpStatsSessionOctetsSent_Type()
)
alHttpStatsSessionOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionOctetsSent.setStatus("current")
_AlHttpStatsSessionOctetsRcvd_Type = Counter32
_AlHttpStatsSessionOctetsRcvd_Object = MibTableColumn
alHttpStatsSessionOctetsRcvd = _AlHttpStatsSessionOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 8),
    _AlHttpStatsSessionOctetsRcvd_Type()
)
alHttpStatsSessionOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionOctetsRcvd.setStatus("current")
_AlHttpStatsSessionPacketsSent_Type = Counter32
_AlHttpStatsSessionPacketsSent_Object = MibTableColumn
alHttpStatsSessionPacketsSent = _AlHttpStatsSessionPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 9),
    _AlHttpStatsSessionPacketsSent_Type()
)
alHttpStatsSessionPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionPacketsSent.setStatus("current")
_AlHttpStatsSessionPacketsRcvd_Type = Counter32
_AlHttpStatsSessionPacketsRcvd_Object = MibTableColumn
alHttpStatsSessionPacketsRcvd = _AlHttpStatsSessionPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 10),
    _AlHttpStatsSessionPacketsRcvd_Type()
)
alHttpStatsSessionPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionPacketsRcvd.setStatus("current")
_AlHttpStatsSessionActiveConnections_Type = Gauge32
_AlHttpStatsSessionActiveConnections_Object = MibTableColumn
alHttpStatsSessionActiveConnections = _AlHttpStatsSessionActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 11),
    _AlHttpStatsSessionActiveConnections_Type()
)
alHttpStatsSessionActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionActiveConnections.setStatus("current")
_AlHttpStatsSessionMaxConnections_Type = Counter32
_AlHttpStatsSessionMaxConnections_Object = MibTableColumn
alHttpStatsSessionMaxConnections = _AlHttpStatsSessionMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 12),
    _AlHttpStatsSessionMaxConnections_Type()
)
alHttpStatsSessionMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionMaxConnections.setStatus("current")
_AlHttpStatsSessionTotalConnections_Type = Counter32
_AlHttpStatsSessionTotalConnections_Object = MibTableColumn
alHttpStatsSessionTotalConnections = _AlHttpStatsSessionTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 7, 2, 1, 13),
    _AlHttpStatsSessionTotalConnections_Type()
)
alHttpStatsSessionTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHttpStatsSessionTotalConnections.setStatus("current")

# Managed Objects groups

altigaHttpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 7, 2)
)
altigaHttpStatsGroup.setObjects(
      *(("ALTIGA-HTTP-STATS-MIB", "alHttpStatsOctetsSent"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsOctetsRcvd"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsPacketsSent"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsPacketsRcvd"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsActiveConnections"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsMaxConnections"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsActiveSessions"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsMaxSessions"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsTotalConnections"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsTotalSessions"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionIndex"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionName"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionIpAddr"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionStartTime"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionLoginTime"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionEncr"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionOctetsSent"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionOctetsRcvd"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionPacketsSent"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionPacketsRcvd"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionActiveConnections"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionMaxConnections"),
        ("ALTIGA-HTTP-STATS-MIB", "alHttpStatsSessionTotalConnections"))
)
if mibBuilder.loadTexts:
    altigaHttpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaHttpStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 12, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaHttpStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-HTTP-STATS-MIB",
    **{"altigaHttpStatsMibModule": altigaHttpStatsMibModule,
       "altigaHttpStatsMibConformance": altigaHttpStatsMibConformance,
       "altigaHttpStatsMibCompliances": altigaHttpStatsMibCompliances,
       "altigaHttpStatsMibCompliance": altigaHttpStatsMibCompliance,
       "altigaHttpStatsGroup": altigaHttpStatsGroup,
       "alStatsHttpGlobal": alStatsHttpGlobal,
       "alHttpStatsOctetsSent": alHttpStatsOctetsSent,
       "alHttpStatsOctetsRcvd": alHttpStatsOctetsRcvd,
       "alHttpStatsPacketsSent": alHttpStatsPacketsSent,
       "alHttpStatsPacketsRcvd": alHttpStatsPacketsRcvd,
       "alHttpStatsActiveConnections": alHttpStatsActiveConnections,
       "alHttpStatsMaxConnections": alHttpStatsMaxConnections,
       "alHttpStatsActiveSessions": alHttpStatsActiveSessions,
       "alHttpStatsMaxSessions": alHttpStatsMaxSessions,
       "alHttpStatsTotalConnections": alHttpStatsTotalConnections,
       "alHttpStatsTotalSessions": alHttpStatsTotalSessions,
       "alHttpStatsSessionTable": alHttpStatsSessionTable,
       "alHttpStatsSessionEntry": alHttpStatsSessionEntry,
       "alHttpStatsSessionIndex": alHttpStatsSessionIndex,
       "alHttpStatsSessionName": alHttpStatsSessionName,
       "alHttpStatsSessionIpAddr": alHttpStatsSessionIpAddr,
       "alHttpStatsSessionStartTime": alHttpStatsSessionStartTime,
       "alHttpStatsSessionLoginTime": alHttpStatsSessionLoginTime,
       "alHttpStatsSessionEncr": alHttpStatsSessionEncr,
       "alHttpStatsSessionOctetsSent": alHttpStatsSessionOctetsSent,
       "alHttpStatsSessionOctetsRcvd": alHttpStatsSessionOctetsRcvd,
       "alHttpStatsSessionPacketsSent": alHttpStatsSessionPacketsSent,
       "alHttpStatsSessionPacketsRcvd": alHttpStatsSessionPacketsRcvd,
       "alHttpStatsSessionActiveConnections": alHttpStatsSessionActiveConnections,
       "alHttpStatsSessionMaxConnections": alHttpStatsSessionMaxConnections,
       "alHttpStatsSessionTotalConnections": alHttpStatsSessionTotalConnections}
)
