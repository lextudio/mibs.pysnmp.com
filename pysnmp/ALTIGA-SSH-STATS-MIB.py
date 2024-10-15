# SNMP MIB module (ALTIGA-SSH-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-SSH-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:22 2024
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

(alSshMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alSshMibModule")

(alSshGroup,
 alStatsSsh) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alSshGroup",
    "alStatsSsh")

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

altigaSshStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 40, 2)
)
altigaSshStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaSshStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaSshStatsMibConformance = _AltigaSshStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 40, 2, 1)
)
_AltigaSshStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaSshStatsMibCompliances = _AltigaSshStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 40, 2, 1, 1)
)
_AlStatsSshGlobal_ObjectIdentity = ObjectIdentity
alStatsSshGlobal = _AlStatsSshGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 1)
)
_AlSshStatsOctetsSent_Type = Counter32
_AlSshStatsOctetsSent_Object = MibScalar
alSshStatsOctetsSent = _AlSshStatsOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 1, 1),
    _AlSshStatsOctetsSent_Type()
)
alSshStatsOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsOctetsSent.setStatus("current")
_AlSshStatsOctetsRcvd_Type = Counter32
_AlSshStatsOctetsRcvd_Object = MibScalar
alSshStatsOctetsRcvd = _AlSshStatsOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 1, 2),
    _AlSshStatsOctetsRcvd_Type()
)
alSshStatsOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsOctetsRcvd.setStatus("current")
_AlSshStatsPacketsSent_Type = Counter32
_AlSshStatsPacketsSent_Object = MibScalar
alSshStatsPacketsSent = _AlSshStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 1, 3),
    _AlSshStatsPacketsSent_Type()
)
alSshStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsPacketsSent.setStatus("current")
_AlSshStatsPacketsRcvd_Type = Counter32
_AlSshStatsPacketsRcvd_Object = MibScalar
alSshStatsPacketsRcvd = _AlSshStatsPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 1, 4),
    _AlSshStatsPacketsRcvd_Type()
)
alSshStatsPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsPacketsRcvd.setStatus("current")
_AlSshStatsTotalSessions_Type = Counter32
_AlSshStatsTotalSessions_Object = MibScalar
alSshStatsTotalSessions = _AlSshStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 1, 5),
    _AlSshStatsTotalSessions_Type()
)
alSshStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsTotalSessions.setStatus("current")
_AlSshStatsActiveSessions_Type = Gauge32
_AlSshStatsActiveSessions_Object = MibScalar
alSshStatsActiveSessions = _AlSshStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 1, 6),
    _AlSshStatsActiveSessions_Type()
)
alSshStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsActiveSessions.setStatus("current")
_AlSshStatsMaxSessions_Type = Counter32
_AlSshStatsMaxSessions_Object = MibScalar
alSshStatsMaxSessions = _AlSshStatsMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 1, 7),
    _AlSshStatsMaxSessions_Type()
)
alSshStatsMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsMaxSessions.setStatus("current")
_AlSshStatsSessionTable_Object = MibTable
alSshStatsSessionTable = _AlSshStatsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2)
)
if mibBuilder.loadTexts:
    alSshStatsSessionTable.setStatus("current")
_AlSshStatsSessionEntry_Object = MibTableRow
alSshStatsSessionEntry = _AlSshStatsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1)
)
alSshStatsSessionEntry.setIndexNames(
    (0, "ALTIGA-SSH-STATS-MIB", "alSshStatsSessionIndex"),
)
if mibBuilder.loadTexts:
    alSshStatsSessionEntry.setStatus("current")
_AlSshStatsSessionIndex_Type = Integer32
_AlSshStatsSessionIndex_Object = MibTableColumn
alSshStatsSessionIndex = _AlSshStatsSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 1),
    _AlSshStatsSessionIndex_Type()
)
alSshStatsSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionIndex.setStatus("current")
_AlSshStatsSessionName_Type = DisplayString
_AlSshStatsSessionName_Object = MibTableColumn
alSshStatsSessionName = _AlSshStatsSessionName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 2),
    _AlSshStatsSessionName_Type()
)
alSshStatsSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionName.setStatus("current")
_AlSshStatsSessionIpAddr_Type = IpAddress
_AlSshStatsSessionIpAddr_Object = MibTableColumn
alSshStatsSessionIpAddr = _AlSshStatsSessionIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 3),
    _AlSshStatsSessionIpAddr_Type()
)
alSshStatsSessionIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionIpAddr.setStatus("current")
_AlSshStatsSessionPort_Type = Unsigned32
_AlSshStatsSessionPort_Object = MibTableColumn
alSshStatsSessionPort = _AlSshStatsSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 4),
    _AlSshStatsSessionPort_Type()
)
alSshStatsSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionPort.setStatus("current")
_AlSshStatsSessionStartTime_Type = TimeTicks
_AlSshStatsSessionStartTime_Object = MibTableColumn
alSshStatsSessionStartTime = _AlSshStatsSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 5),
    _AlSshStatsSessionStartTime_Type()
)
alSshStatsSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionStartTime.setStatus("current")
_AlSshStatsSessionLoginTime_Type = Unsigned32
_AlSshStatsSessionLoginTime_Object = MibTableColumn
alSshStatsSessionLoginTime = _AlSshStatsSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 6),
    _AlSshStatsSessionLoginTime_Type()
)
alSshStatsSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionLoginTime.setStatus("current")
_AlSshStatsSessionEncr_Type = EncryptionAlgorithm
_AlSshStatsSessionEncr_Object = MibTableColumn
alSshStatsSessionEncr = _AlSshStatsSessionEncr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 7),
    _AlSshStatsSessionEncr_Type()
)
alSshStatsSessionEncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionEncr.setStatus("current")
_AlSshStatsSessionOctetsSent_Type = Counter32
_AlSshStatsSessionOctetsSent_Object = MibTableColumn
alSshStatsSessionOctetsSent = _AlSshStatsSessionOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 8),
    _AlSshStatsSessionOctetsSent_Type()
)
alSshStatsSessionOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionOctetsSent.setStatus("current")
_AlSshStatsSessionOctetsRcvd_Type = Counter32
_AlSshStatsSessionOctetsRcvd_Object = MibTableColumn
alSshStatsSessionOctetsRcvd = _AlSshStatsSessionOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 9),
    _AlSshStatsSessionOctetsRcvd_Type()
)
alSshStatsSessionOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionOctetsRcvd.setStatus("current")
_AlSshStatsSessionPacketsSent_Type = Counter32
_AlSshStatsSessionPacketsSent_Object = MibTableColumn
alSshStatsSessionPacketsSent = _AlSshStatsSessionPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 10),
    _AlSshStatsSessionPacketsSent_Type()
)
alSshStatsSessionPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionPacketsSent.setStatus("current")
_AlSshStatsSessionPacketsRcvd_Type = Counter32
_AlSshStatsSessionPacketsRcvd_Object = MibTableColumn
alSshStatsSessionPacketsRcvd = _AlSshStatsSessionPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 35, 2, 1, 11),
    _AlSshStatsSessionPacketsRcvd_Type()
)
alSshStatsSessionPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSshStatsSessionPacketsRcvd.setStatus("current")

# Managed Objects groups

altigaSshStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 35, 2)
)
altigaSshStatsGroup.setObjects(
      *(("ALTIGA-SSH-STATS-MIB", "alSshStatsOctetsSent"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsOctetsRcvd"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsPacketsSent"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsPacketsRcvd"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsTotalSessions"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsActiveSessions"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsMaxSessions"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionIndex"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionName"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionIpAddr"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionPort"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionStartTime"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionLoginTime"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionEncr"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionOctetsSent"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionOctetsRcvd"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionPacketsSent"),
        ("ALTIGA-SSH-STATS-MIB", "alSshStatsSessionPacketsRcvd"))
)
if mibBuilder.loadTexts:
    altigaSshStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaSshStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 40, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaSshStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-SSH-STATS-MIB",
    **{"altigaSshStatsMibModule": altigaSshStatsMibModule,
       "altigaSshStatsMibConformance": altigaSshStatsMibConformance,
       "altigaSshStatsMibCompliances": altigaSshStatsMibCompliances,
       "altigaSshStatsMibCompliance": altigaSshStatsMibCompliance,
       "altigaSshStatsGroup": altigaSshStatsGroup,
       "alStatsSshGlobal": alStatsSshGlobal,
       "alSshStatsOctetsSent": alSshStatsOctetsSent,
       "alSshStatsOctetsRcvd": alSshStatsOctetsRcvd,
       "alSshStatsPacketsSent": alSshStatsPacketsSent,
       "alSshStatsPacketsRcvd": alSshStatsPacketsRcvd,
       "alSshStatsTotalSessions": alSshStatsTotalSessions,
       "alSshStatsActiveSessions": alSshStatsActiveSessions,
       "alSshStatsMaxSessions": alSshStatsMaxSessions,
       "alSshStatsSessionTable": alSshStatsSessionTable,
       "alSshStatsSessionEntry": alSshStatsSessionEntry,
       "alSshStatsSessionIndex": alSshStatsSessionIndex,
       "alSshStatsSessionName": alSshStatsSessionName,
       "alSshStatsSessionIpAddr": alSshStatsSessionIpAddr,
       "alSshStatsSessionPort": alSshStatsSessionPort,
       "alSshStatsSessionStartTime": alSshStatsSessionStartTime,
       "alSshStatsSessionLoginTime": alSshStatsSessionLoginTime,
       "alSshStatsSessionEncr": alSshStatsSessionEncr,
       "alSshStatsSessionOctetsSent": alSshStatsSessionOctetsSent,
       "alSshStatsSessionOctetsRcvd": alSshStatsSessionOctetsRcvd,
       "alSshStatsSessionPacketsSent": alSshStatsSessionPacketsSent,
       "alSshStatsSessionPacketsRcvd": alSshStatsSessionPacketsRcvd}
)
