# SNMP MIB module (ALTIGA-CERT-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-CERT-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:06 2024
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

(alCertMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alCertMibModule")

(alCertGroup,
 alStatsCert) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alCertGroup",
    "alStatsCert")

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

altigaCertStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 32, 2)
)
altigaCertStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaCertStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaCertStatsMibConformance = _AltigaCertStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 32, 2, 1)
)
_AltigaCertStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaCertStatsMibCompliances = _AltigaCertStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 32, 2, 1, 1)
)
_AlStatsCertGlobal_ObjectIdentity = ObjectIdentity
alStatsCertGlobal = _AlStatsCertGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 1)
)
_AlCertStatsServerTable_Object = MibTable
alCertStatsServerTable = _AlCertStatsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2)
)
if mibBuilder.loadTexts:
    alCertStatsServerTable.setStatus("current")
_AlCertStatsServerEntry_Object = MibTableRow
alCertStatsServerEntry = _AlCertStatsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1)
)
alCertStatsServerEntry.setIndexNames(
    (0, "ALTIGA-CERT-STATS-MIB", "alCertStatsServerIndex"),
)
if mibBuilder.loadTexts:
    alCertStatsServerEntry.setStatus("current")
_AlCertStatsServerIndex_Type = Integer32
_AlCertStatsServerIndex_Object = MibTableColumn
alCertStatsServerIndex = _AlCertStatsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 1),
    _AlCertStatsServerIndex_Type()
)
alCertStatsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerIndex.setStatus("current")
_AlCertStatsServerAddress_Type = IpAddress
_AlCertStatsServerAddress_Object = MibTableColumn
alCertStatsServerAddress = _AlCertStatsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 2),
    _AlCertStatsServerAddress_Type()
)
alCertStatsServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerAddress.setStatus("current")
_AlCertStatsServerPortNumber_Type = Integer32
_AlCertStatsServerPortNumber_Object = MibTableColumn
alCertStatsServerPortNumber = _AlCertStatsServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 3),
    _AlCertStatsServerPortNumber_Type()
)
alCertStatsServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerPortNumber.setStatus("current")
_AlCertStatsServerCertRequests_Type = Counter32
_AlCertStatsServerCertRequests_Object = MibTableColumn
alCertStatsServerCertRequests = _AlCertStatsServerCertRequests_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 4),
    _AlCertStatsServerCertRequests_Type()
)
alCertStatsServerCertRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCertRequests.setStatus("current")
_AlCertStatsServerCertRetransmissions_Type = Counter32
_AlCertStatsServerCertRetransmissions_Object = MibTableColumn
alCertStatsServerCertRetransmissions = _AlCertStatsServerCertRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 5),
    _AlCertStatsServerCertRetransmissions_Type()
)
alCertStatsServerCertRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCertRetransmissions.setStatus("current")
_AlCertStatsServerCertRcvd_Type = Counter32
_AlCertStatsServerCertRcvd_Object = MibTableColumn
alCertStatsServerCertRcvd = _AlCertStatsServerCertRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 6),
    _AlCertStatsServerCertRcvd_Type()
)
alCertStatsServerCertRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCertRcvd.setStatus("current")
_AlCertStatsServerCertPendingRequests_Type = Gauge32
_AlCertStatsServerCertPendingRequests_Object = MibTableColumn
alCertStatsServerCertPendingRequests = _AlCertStatsServerCertPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 7),
    _AlCertStatsServerCertPendingRequests_Type()
)
alCertStatsServerCertPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCertPendingRequests.setStatus("current")
_AlCertStatsServerCertTimeouts_Type = Counter32
_AlCertStatsServerCertTimeouts_Object = MibTableColumn
alCertStatsServerCertTimeouts = _AlCertStatsServerCertTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 8),
    _AlCertStatsServerCertTimeouts_Type()
)
alCertStatsServerCertTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCertTimeouts.setStatus("current")
_AlCertStatsServerCRLRequests_Type = Counter32
_AlCertStatsServerCRLRequests_Object = MibTableColumn
alCertStatsServerCRLRequests = _AlCertStatsServerCRLRequests_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 9),
    _AlCertStatsServerCRLRequests_Type()
)
alCertStatsServerCRLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCRLRequests.setStatus("current")
_AlCertStatsServerCRLRetransmissions_Type = Counter32
_AlCertStatsServerCRLRetransmissions_Object = MibTableColumn
alCertStatsServerCRLRetransmissions = _AlCertStatsServerCRLRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 10),
    _AlCertStatsServerCRLRetransmissions_Type()
)
alCertStatsServerCRLRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCRLRetransmissions.setStatus("current")
_AlCertStatsServerCRLRcvd_Type = Counter32
_AlCertStatsServerCRLRcvd_Object = MibTableColumn
alCertStatsServerCRLRcvd = _AlCertStatsServerCRLRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 11),
    _AlCertStatsServerCRLRcvd_Type()
)
alCertStatsServerCRLRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCRLRcvd.setStatus("current")
_AlCertStatsServerCRLPendingRequests_Type = Gauge32
_AlCertStatsServerCRLPendingRequests_Object = MibTableColumn
alCertStatsServerCRLPendingRequests = _AlCertStatsServerCRLPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 12),
    _AlCertStatsServerCRLPendingRequests_Type()
)
alCertStatsServerCRLPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCRLPendingRequests.setStatus("current")
_AlCertStatsServerCRLTimeouts_Type = Counter32
_AlCertStatsServerCRLTimeouts_Object = MibTableColumn
alCertStatsServerCRLTimeouts = _AlCertStatsServerCRLTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 13),
    _AlCertStatsServerCRLTimeouts_Type()
)
alCertStatsServerCRLTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCertStatsServerCRLTimeouts.setStatus("current")

# Managed Objects groups

altigaCertStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 27, 2)
)
altigaCertStatsGroup.setObjects(
      *(("ALTIGA-CERT-STATS-MIB", "alCertStatsServerIndex"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerAddress"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerPortNumber"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertRequests"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertRetransmissions"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertRcvd"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertPendingRequests"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertTimeouts"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLRequests"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLRetransmissions"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLRcvd"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLPendingRequests"),
        ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLTimeouts"))
)
if mibBuilder.loadTexts:
    altigaCertStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaCertStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 32, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaCertStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-CERT-STATS-MIB",
    **{"altigaCertStatsMibModule": altigaCertStatsMibModule,
       "altigaCertStatsMibConformance": altigaCertStatsMibConformance,
       "altigaCertStatsMibCompliances": altigaCertStatsMibCompliances,
       "altigaCertStatsMibCompliance": altigaCertStatsMibCompliance,
       "altigaCertStatsGroup": altigaCertStatsGroup,
       "alStatsCertGlobal": alStatsCertGlobal,
       "alCertStatsServerTable": alCertStatsServerTable,
       "alCertStatsServerEntry": alCertStatsServerEntry,
       "alCertStatsServerIndex": alCertStatsServerIndex,
       "alCertStatsServerAddress": alCertStatsServerAddress,
       "alCertStatsServerPortNumber": alCertStatsServerPortNumber,
       "alCertStatsServerCertRequests": alCertStatsServerCertRequests,
       "alCertStatsServerCertRetransmissions": alCertStatsServerCertRetransmissions,
       "alCertStatsServerCertRcvd": alCertStatsServerCertRcvd,
       "alCertStatsServerCertPendingRequests": alCertStatsServerCertPendingRequests,
       "alCertStatsServerCertTimeouts": alCertStatsServerCertTimeouts,
       "alCertStatsServerCRLRequests": alCertStatsServerCRLRequests,
       "alCertStatsServerCRLRetransmissions": alCertStatsServerCRLRetransmissions,
       "alCertStatsServerCRLRcvd": alCertStatsServerCRLRcvd,
       "alCertStatsServerCRLPendingRequests": alCertStatsServerCRLPendingRequests,
       "alCertStatsServerCRLTimeouts": alCertStatsServerCRLTimeouts}
)
