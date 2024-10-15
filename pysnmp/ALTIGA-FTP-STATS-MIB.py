# SNMP MIB module (ALTIGA-FTP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-FTP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:10 2024
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

(alFtpMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alFtpMibModule")

(alFtpGroup,
 alStatsFtp) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alFtpGroup",
    "alStatsFtp")

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

altigaFtpStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 17, 2)
)
altigaFtpStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaFtpStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaFtpStatsMibConformance = _AltigaFtpStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 17, 2, 1)
)
_AltigaFtpStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaFtpStatsMibCompliances = _AltigaFtpStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 17, 2, 1, 1)
)
_AlStatsFtpServerGlobal_ObjectIdentity = ObjectIdentity
alStatsFtpServerGlobal = _AlStatsFtpServerGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 1)
)
_AlStatsFtpClientGlobal_ObjectIdentity = ObjectIdentity
alStatsFtpClientGlobal = _AlStatsFtpClientGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2)
)
_AlFtpClientStatsMaxSess_Type = Gauge32
_AlFtpClientStatsMaxSess_Object = MibScalar
alFtpClientStatsMaxSess = _AlFtpClientStatsMaxSess_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 1),
    _AlFtpClientStatsMaxSess_Type()
)
alFtpClientStatsMaxSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsMaxSess.setStatus("current")
_AlFtpClientStatsTotalSess_Type = Counter32
_AlFtpClientStatsTotalSess_Object = MibScalar
alFtpClientStatsTotalSess = _AlFtpClientStatsTotalSess_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 2),
    _AlFtpClientStatsTotalSess_Type()
)
alFtpClientStatsTotalSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsTotalSess.setStatus("current")
_AlFtpClientStatsGoodConns_Type = Counter32
_AlFtpClientStatsGoodConns_Object = MibScalar
alFtpClientStatsGoodConns = _AlFtpClientStatsGoodConns_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 3),
    _AlFtpClientStatsGoodConns_Type()
)
alFtpClientStatsGoodConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsGoodConns.setStatus("current")
_AlFtpClientStatsBadConns_Type = Counter32
_AlFtpClientStatsBadConns_Object = MibScalar
alFtpClientStatsBadConns = _AlFtpClientStatsBadConns_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 4),
    _AlFtpClientStatsBadConns_Type()
)
alFtpClientStatsBadConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsBadConns.setStatus("current")
_AlFtpClientStatsGoodDataConns_Type = Counter32
_AlFtpClientStatsGoodDataConns_Object = MibScalar
alFtpClientStatsGoodDataConns = _AlFtpClientStatsGoodDataConns_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 5),
    _AlFtpClientStatsGoodDataConns_Type()
)
alFtpClientStatsGoodDataConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsGoodDataConns.setStatus("current")
_AlFtpClientStatsBadDataConns_Type = Counter32
_AlFtpClientStatsBadDataConns_Object = MibScalar
alFtpClientStatsBadDataConns = _AlFtpClientStatsBadDataConns_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 6),
    _AlFtpClientStatsBadDataConns_Type()
)
alFtpClientStatsBadDataConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsBadDataConns.setStatus("current")
_AlFtpClientStatsGoodFileXfers_Type = Counter32
_AlFtpClientStatsGoodFileXfers_Object = MibScalar
alFtpClientStatsGoodFileXfers = _AlFtpClientStatsGoodFileXfers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 7),
    _AlFtpClientStatsGoodFileXfers_Type()
)
alFtpClientStatsGoodFileXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsGoodFileXfers.setStatus("current")
_AlFtpClientStatsBadFileXfers_Type = Counter32
_AlFtpClientStatsBadFileXfers_Object = MibScalar
alFtpClientStatsBadFileXfers = _AlFtpClientStatsBadFileXfers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 8),
    _AlFtpClientStatsBadFileXfers_Type()
)
alFtpClientStatsBadFileXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsBadFileXfers.setStatus("current")
_AlFtpClientStatsAsciiXfers_Type = Counter32
_AlFtpClientStatsAsciiXfers_Object = MibScalar
alFtpClientStatsAsciiXfers = _AlFtpClientStatsAsciiXfers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 9),
    _AlFtpClientStatsAsciiXfers_Type()
)
alFtpClientStatsAsciiXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsAsciiXfers.setStatus("current")
_AlFtpClientStatsBinaryXfers_Type = Counter32
_AlFtpClientStatsBinaryXfers_Object = MibScalar
alFtpClientStatsBinaryXfers = _AlFtpClientStatsBinaryXfers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 10),
    _AlFtpClientStatsBinaryXfers_Type()
)
alFtpClientStatsBinaryXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsBinaryXfers.setStatus("current")
_AlFtpClientStatsOctetsXmit_Type = Counter32
_AlFtpClientStatsOctetsXmit_Object = MibScalar
alFtpClientStatsOctetsXmit = _AlFtpClientStatsOctetsXmit_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 11),
    _AlFtpClientStatsOctetsXmit_Type()
)
alFtpClientStatsOctetsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsOctetsXmit.setStatus("current")
_AlFtpClientStatsOctetsRecv_Type = Counter32
_AlFtpClientStatsOctetsRecv_Object = MibScalar
alFtpClientStatsOctetsRecv = _AlFtpClientStatsOctetsRecv_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 12),
    _AlFtpClientStatsOctetsRecv_Type()
)
alFtpClientStatsOctetsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsOctetsRecv.setStatus("current")
_AlFtpClientStatsTimeouts_Type = Counter32
_AlFtpClientStatsTimeouts_Object = MibScalar
alFtpClientStatsTimeouts = _AlFtpClientStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 12, 2, 13),
    _AlFtpClientStatsTimeouts_Type()
)
alFtpClientStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFtpClientStatsTimeouts.setStatus("current")

# Managed Objects groups

altigaFtpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 12, 2)
)
altigaFtpStatsGroup.setObjects(
      *(("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsMaxSess"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsTotalSess"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsGoodConns"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsBadConns"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsGoodDataConns"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsBadDataConns"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsGoodFileXfers"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsBadFileXfers"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsAsciiXfers"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsBinaryXfers"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsOctetsXmit"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsOctetsRecv"),
        ("ALTIGA-FTP-STATS-MIB", "alFtpClientStatsTimeouts"))
)
if mibBuilder.loadTexts:
    altigaFtpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaFtpStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 17, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaFtpStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-FTP-STATS-MIB",
    **{"altigaFtpStatsMibModule": altigaFtpStatsMibModule,
       "altigaFtpStatsMibConformance": altigaFtpStatsMibConformance,
       "altigaFtpStatsMibCompliances": altigaFtpStatsMibCompliances,
       "altigaFtpStatsMibCompliance": altigaFtpStatsMibCompliance,
       "altigaFtpStatsGroup": altigaFtpStatsGroup,
       "alStatsFtpServerGlobal": alStatsFtpServerGlobal,
       "alStatsFtpClientGlobal": alStatsFtpClientGlobal,
       "alFtpClientStatsMaxSess": alFtpClientStatsMaxSess,
       "alFtpClientStatsTotalSess": alFtpClientStatsTotalSess,
       "alFtpClientStatsGoodConns": alFtpClientStatsGoodConns,
       "alFtpClientStatsBadConns": alFtpClientStatsBadConns,
       "alFtpClientStatsGoodDataConns": alFtpClientStatsGoodDataConns,
       "alFtpClientStatsBadDataConns": alFtpClientStatsBadDataConns,
       "alFtpClientStatsGoodFileXfers": alFtpClientStatsGoodFileXfers,
       "alFtpClientStatsBadFileXfers": alFtpClientStatsBadFileXfers,
       "alFtpClientStatsAsciiXfers": alFtpClientStatsAsciiXfers,
       "alFtpClientStatsBinaryXfers": alFtpClientStatsBinaryXfers,
       "alFtpClientStatsOctetsXmit": alFtpClientStatsOctetsXmit,
       "alFtpClientStatsOctetsRecv": alFtpClientStatsOctetsRecv,
       "alFtpClientStatsTimeouts": alFtpClientStatsTimeouts}
)
