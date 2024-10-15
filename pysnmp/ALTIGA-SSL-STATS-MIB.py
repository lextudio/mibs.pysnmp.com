# SNMP MIB module (ALTIGA-SSL-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-SSL-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:23 2024
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

(alSslMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alSslMibModule")

(alSslGroup,
 alStatsSsl) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alSslGroup",
    "alStatsSsl")

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

altigaSslStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2)
)
altigaSslStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaSslStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaSslStatsMibConformance = _AltigaSslStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1)
)
_AltigaSslStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaSslStatsMibCompliances = _AltigaSslStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1)
)
_AlStatsSslGlobal_ObjectIdentity = ObjectIdentity
alStatsSslGlobal = _AlStatsSslGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1)
)
_AlSslStatsTotalSessions_Type = Counter32
_AlSslStatsTotalSessions_Object = MibScalar
alSslStatsTotalSessions = _AlSslStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 1),
    _AlSslStatsTotalSessions_Type()
)
alSslStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSslStatsTotalSessions.setStatus("current")
_AlSslStatsActiveSessions_Type = Gauge32
_AlSslStatsActiveSessions_Object = MibScalar
alSslStatsActiveSessions = _AlSslStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 2),
    _AlSslStatsActiveSessions_Type()
)
alSslStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSslStatsActiveSessions.setStatus("current")
_AlSslStatsMaxSessions_Type = Gauge32
_AlSslStatsMaxSessions_Object = MibScalar
alSslStatsMaxSessions = _AlSslStatsMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 3),
    _AlSslStatsMaxSessions_Type()
)
alSslStatsMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSslStatsMaxSessions.setStatus("current")
_AlSslStatsPreDecryptOctets_Type = Counter32
_AlSslStatsPreDecryptOctets_Object = MibScalar
alSslStatsPreDecryptOctets = _AlSslStatsPreDecryptOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 4),
    _AlSslStatsPreDecryptOctets_Type()
)
alSslStatsPreDecryptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSslStatsPreDecryptOctets.setStatus("current")
_AlSslStatsPostDecryptOctets_Type = Counter32
_AlSslStatsPostDecryptOctets_Object = MibScalar
alSslStatsPostDecryptOctets = _AlSslStatsPostDecryptOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 5),
    _AlSslStatsPostDecryptOctets_Type()
)
alSslStatsPostDecryptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSslStatsPostDecryptOctets.setStatus("current")
_AlSslStatsPreEncryptOctets_Type = Counter32
_AlSslStatsPreEncryptOctets_Object = MibScalar
alSslStatsPreEncryptOctets = _AlSslStatsPreEncryptOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 6),
    _AlSslStatsPreEncryptOctets_Type()
)
alSslStatsPreEncryptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSslStatsPreEncryptOctets.setStatus("current")
_AlSslStatsPostEncryptOctets_Type = Counter32
_AlSslStatsPostEncryptOctets_Object = MibScalar
alSslStatsPostEncryptOctets = _AlSslStatsPostEncryptOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 7),
    _AlSslStatsPostEncryptOctets_Type()
)
alSslStatsPostEncryptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSslStatsPostEncryptOctets.setStatus("current")

# Managed Objects groups

altigaSslStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 26, 2)
)
altigaSslStatsGroup.setObjects(
      *(("ALTIGA-SSL-STATS-MIB", "alSslStatsTotalSessions"),
        ("ALTIGA-SSL-STATS-MIB", "alSslStatsActiveSessions"),
        ("ALTIGA-SSL-STATS-MIB", "alSslStatsMaxSessions"),
        ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreDecryptOctets"),
        ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostDecryptOctets"),
        ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreEncryptOctets"),
        ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostEncryptOctets"))
)
if mibBuilder.loadTexts:
    altigaSslStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaSslStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaSslStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-SSL-STATS-MIB",
    **{"altigaSslStatsMibModule": altigaSslStatsMibModule,
       "altigaSslStatsMibConformance": altigaSslStatsMibConformance,
       "altigaSslStatsMibCompliances": altigaSslStatsMibCompliances,
       "altigaSslStatsMibCompliance": altigaSslStatsMibCompliance,
       "altigaSslStatsGroup": altigaSslStatsGroup,
       "alStatsSslGlobal": alStatsSslGlobal,
       "alSslStatsTotalSessions": alSslStatsTotalSessions,
       "alSslStatsActiveSessions": alSslStatsActiveSessions,
       "alSslStatsMaxSessions": alSslStatsMaxSessions,
       "alSslStatsPreDecryptOctets": alSslStatsPreDecryptOctets,
       "alSslStatsPostDecryptOctets": alSslStatsPostDecryptOctets,
       "alSslStatsPreEncryptOctets": alSslStatsPreEncryptOctets,
       "alSslStatsPostEncryptOctets": alSslStatsPostEncryptOctets}
)
