# SNMP MIB module (ALTIGA-DHCP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-DHCP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:07 2024
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

(alDhcpMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alDhcpMibModule")

(alDhcpGroup,
 alStatsDhcp) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alDhcpGroup",
    "alStatsDhcp")

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

altigaDhcpStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 25, 2)
)
altigaDhcpStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaDhcpStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaDhcpStatsMibConformance = _AltigaDhcpStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 25, 2, 1)
)
_AltigaDhcpStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaDhcpStatsMibCompliances = _AltigaDhcpStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 25, 2, 1, 1)
)
_AlStatsDhcpGlobal_ObjectIdentity = ObjectIdentity
alStatsDhcpGlobal = _AlStatsDhcpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1)
)
_AlDhcpStatsActiveLeases_Type = Gauge32
_AlDhcpStatsActiveLeases_Object = MibScalar
alDhcpStatsActiveLeases = _AlDhcpStatsActiveLeases_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 1),
    _AlDhcpStatsActiveLeases_Type()
)
alDhcpStatsActiveLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsActiveLeases.setStatus("current")
_AlDhcpStatsMaximumLeases_Type = Gauge32
_AlDhcpStatsMaximumLeases_Object = MibScalar
alDhcpStatsMaximumLeases = _AlDhcpStatsMaximumLeases_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 2),
    _AlDhcpStatsMaximumLeases_Type()
)
alDhcpStatsMaximumLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsMaximumLeases.setStatus("current")
_AlDhcpStatsDiscoversSent_Type = Gauge32
_AlDhcpStatsDiscoversSent_Object = MibScalar
alDhcpStatsDiscoversSent = _AlDhcpStatsDiscoversSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 3),
    _AlDhcpStatsDiscoversSent_Type()
)
alDhcpStatsDiscoversSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsDiscoversSent.setStatus("current")
_AlDhcpStatsOffersRcvd_Type = Gauge32
_AlDhcpStatsOffersRcvd_Object = MibScalar
alDhcpStatsOffersRcvd = _AlDhcpStatsOffersRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 4),
    _AlDhcpStatsOffersRcvd_Type()
)
alDhcpStatsOffersRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsOffersRcvd.setStatus("current")
_AlDhcpStatsInitRequestsSent_Type = Gauge32
_AlDhcpStatsInitRequestsSent_Object = MibScalar
alDhcpStatsInitRequestsSent = _AlDhcpStatsInitRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 5),
    _AlDhcpStatsInitRequestsSent_Type()
)
alDhcpStatsInitRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsInitRequestsSent.setStatus("current")
_AlDhcpStatsT1RequestsSent_Type = Gauge32
_AlDhcpStatsT1RequestsSent_Object = MibScalar
alDhcpStatsT1RequestsSent = _AlDhcpStatsT1RequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 6),
    _AlDhcpStatsT1RequestsSent_Type()
)
alDhcpStatsT1RequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsT1RequestsSent.setStatus("current")
_AlDhcpStatsT2RequestsSent_Type = Gauge32
_AlDhcpStatsT2RequestsSent_Object = MibScalar
alDhcpStatsT2RequestsSent = _AlDhcpStatsT2RequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 7),
    _AlDhcpStatsT2RequestsSent_Type()
)
alDhcpStatsT2RequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsT2RequestsSent.setStatus("current")
_AlDhcpStatsInitAcksRcvd_Type = Gauge32
_AlDhcpStatsInitAcksRcvd_Object = MibScalar
alDhcpStatsInitAcksRcvd = _AlDhcpStatsInitAcksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 8),
    _AlDhcpStatsInitAcksRcvd_Type()
)
alDhcpStatsInitAcksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsInitAcksRcvd.setStatus("current")
_AlDhcpStatsInitNaksRcvd_Type = Gauge32
_AlDhcpStatsInitNaksRcvd_Object = MibScalar
alDhcpStatsInitNaksRcvd = _AlDhcpStatsInitNaksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 9),
    _AlDhcpStatsInitNaksRcvd_Type()
)
alDhcpStatsInitNaksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsInitNaksRcvd.setStatus("current")
_AlDhcpStatsT1AcksRcvd_Type = Gauge32
_AlDhcpStatsT1AcksRcvd_Object = MibScalar
alDhcpStatsT1AcksRcvd = _AlDhcpStatsT1AcksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 10),
    _AlDhcpStatsT1AcksRcvd_Type()
)
alDhcpStatsT1AcksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsT1AcksRcvd.setStatus("current")
_AlDhcpStatsT1NaksRcvd_Type = Gauge32
_AlDhcpStatsT1NaksRcvd_Object = MibScalar
alDhcpStatsT1NaksRcvd = _AlDhcpStatsT1NaksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 11),
    _AlDhcpStatsT1NaksRcvd_Type()
)
alDhcpStatsT1NaksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsT1NaksRcvd.setStatus("current")
_AlDhcpStatsT2AcksRcvd_Type = Gauge32
_AlDhcpStatsT2AcksRcvd_Object = MibScalar
alDhcpStatsT2AcksRcvd = _AlDhcpStatsT2AcksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 12),
    _AlDhcpStatsT2AcksRcvd_Type()
)
alDhcpStatsT2AcksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsT2AcksRcvd.setStatus("current")
_AlDhcpStatsT2NaksRcvd_Type = Gauge32
_AlDhcpStatsT2NaksRcvd_Object = MibScalar
alDhcpStatsT2NaksRcvd = _AlDhcpStatsT2NaksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 13),
    _AlDhcpStatsT2NaksRcvd_Type()
)
alDhcpStatsT2NaksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsT2NaksRcvd.setStatus("current")
_AlDhcpStatsT1Timeouts_Type = Gauge32
_AlDhcpStatsT1Timeouts_Object = MibScalar
alDhcpStatsT1Timeouts = _AlDhcpStatsT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 14),
    _AlDhcpStatsT1Timeouts_Type()
)
alDhcpStatsT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsT1Timeouts.setStatus("current")
_AlDhcpStatsT2Timeouts_Type = Gauge32
_AlDhcpStatsT2Timeouts_Object = MibScalar
alDhcpStatsT2Timeouts = _AlDhcpStatsT2Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 15),
    _AlDhcpStatsT2Timeouts_Type()
)
alDhcpStatsT2Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsT2Timeouts.setStatus("current")
_AlDhcpStatsApiRequests_Type = Gauge32
_AlDhcpStatsApiRequests_Object = MibScalar
alDhcpStatsApiRequests = _AlDhcpStatsApiRequests_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 16),
    _AlDhcpStatsApiRequests_Type()
)
alDhcpStatsApiRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsApiRequests.setStatus("current")
_AlDhcpStatsLeaseTimeouts_Type = Gauge32
_AlDhcpStatsLeaseTimeouts_Object = MibScalar
alDhcpStatsLeaseTimeouts = _AlDhcpStatsLeaseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 1, 17),
    _AlDhcpStatsLeaseTimeouts_Type()
)
alDhcpStatsLeaseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsLeaseTimeouts.setStatus("current")
_AlDhcpStatsSessTable_Object = MibTable
alDhcpStatsSessTable = _AlDhcpStatsSessTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    alDhcpStatsSessTable.setStatus("current")
_AlDhcpStatsSessEntry_Object = MibTableRow
alDhcpStatsSessEntry = _AlDhcpStatsSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1)
)
alDhcpStatsSessEntry.setIndexNames(
    (0, "ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessIpAddr"),
)
if mibBuilder.loadTexts:
    alDhcpStatsSessEntry.setStatus("current")
_AlDhcpStatsSessRowStatus_Type = RowStatus
_AlDhcpStatsSessRowStatus_Object = MibTableColumn
alDhcpStatsSessRowStatus = _AlDhcpStatsSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 1),
    _AlDhcpStatsSessRowStatus_Type()
)
alDhcpStatsSessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDhcpStatsSessRowStatus.setStatus("current")
_AlDhcpStatsSessId_Type = Integer32
_AlDhcpStatsSessId_Object = MibTableColumn
alDhcpStatsSessId = _AlDhcpStatsSessId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 2),
    _AlDhcpStatsSessId_Type()
)
alDhcpStatsSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessId.setStatus("current")
_AlDhcpStatsSessKey_Type = Integer32
_AlDhcpStatsSessKey_Object = MibTableColumn
alDhcpStatsSessKey = _AlDhcpStatsSessKey_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 3),
    _AlDhcpStatsSessKey_Type()
)
alDhcpStatsSessKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessKey.setStatus("current")
_AlDhcpStatsSessIpAddr_Type = IpAddress
_AlDhcpStatsSessIpAddr_Object = MibTableColumn
alDhcpStatsSessIpAddr = _AlDhcpStatsSessIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 4),
    _AlDhcpStatsSessIpAddr_Type()
)
alDhcpStatsSessIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessIpAddr.setStatus("current")
_AlDhcpStatsSessUpTime_Type = Integer32
_AlDhcpStatsSessUpTime_Object = MibTableColumn
alDhcpStatsSessUpTime = _AlDhcpStatsSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 5),
    _AlDhcpStatsSessUpTime_Type()
)
alDhcpStatsSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessUpTime.setStatus("current")
_AlDhcpStatsSessLeaseDuration_Type = Integer32
_AlDhcpStatsSessLeaseDuration_Object = MibTableColumn
alDhcpStatsSessLeaseDuration = _AlDhcpStatsSessLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 6),
    _AlDhcpStatsSessLeaseDuration_Type()
)
alDhcpStatsSessLeaseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessLeaseDuration.setStatus("current")
_AlDhcpStatsSessLeaseExpire_Type = Integer32
_AlDhcpStatsSessLeaseExpire_Object = MibTableColumn
alDhcpStatsSessLeaseExpire = _AlDhcpStatsSessLeaseExpire_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 7),
    _AlDhcpStatsSessLeaseExpire_Type()
)
alDhcpStatsSessLeaseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessLeaseExpire.setStatus("current")
_AlDhcpStatsSessState_Type = DisplayString
_AlDhcpStatsSessState_Object = MibTableColumn
alDhcpStatsSessState = _AlDhcpStatsSessState_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 8),
    _AlDhcpStatsSessState_Type()
)
alDhcpStatsSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessState.setStatus("current")
_AlDhcpStatsSessClientId_Type = DisplayString
_AlDhcpStatsSessClientId_Object = MibTableColumn
alDhcpStatsSessClientId = _AlDhcpStatsSessClientId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 9),
    _AlDhcpStatsSessClientId_Type()
)
alDhcpStatsSessClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessClientId.setStatus("current")
_AlDhcpStatsSessSrvrIpAddr_Type = IpAddress
_AlDhcpStatsSessSrvrIpAddr_Object = MibTableColumn
alDhcpStatsSessSrvrIpAddr = _AlDhcpStatsSessSrvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 20, 2, 1, 10),
    _AlDhcpStatsSessSrvrIpAddr_Type()
)
alDhcpStatsSessSrvrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpStatsSessSrvrIpAddr.setStatus("current")

# Managed Objects groups

altigaDhcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 20, 2)
)
altigaDhcpStatsGroup.setObjects(
      *(("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsActiveLeases"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsMaximumLeases"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsDiscoversSent"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsOffersRcvd"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsInitRequestsSent"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsT1RequestsSent"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsT2RequestsSent"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsInitAcksRcvd"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsInitNaksRcvd"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsT1AcksRcvd"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsT1NaksRcvd"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsT2AcksRcvd"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsT2NaksRcvd"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsT1Timeouts"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsT2Timeouts"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsApiRequests"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsLeaseTimeouts"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessRowStatus"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessId"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessKey"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessIpAddr"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessUpTime"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessLeaseDuration"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessLeaseExpire"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessState"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessClientId"),
        ("ALTIGA-DHCP-STATS-MIB", "alDhcpStatsSessSrvrIpAddr"))
)
if mibBuilder.loadTexts:
    altigaDhcpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaDhcpStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 25, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaDhcpStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-DHCP-STATS-MIB",
    **{"altigaDhcpStatsMibModule": altigaDhcpStatsMibModule,
       "altigaDhcpStatsMibConformance": altigaDhcpStatsMibConformance,
       "altigaDhcpStatsMibCompliances": altigaDhcpStatsMibCompliances,
       "altigaDhcpStatsMibCompliance": altigaDhcpStatsMibCompliance,
       "altigaDhcpStatsGroup": altigaDhcpStatsGroup,
       "alStatsDhcpGlobal": alStatsDhcpGlobal,
       "alDhcpStatsActiveLeases": alDhcpStatsActiveLeases,
       "alDhcpStatsMaximumLeases": alDhcpStatsMaximumLeases,
       "alDhcpStatsDiscoversSent": alDhcpStatsDiscoversSent,
       "alDhcpStatsOffersRcvd": alDhcpStatsOffersRcvd,
       "alDhcpStatsInitRequestsSent": alDhcpStatsInitRequestsSent,
       "alDhcpStatsT1RequestsSent": alDhcpStatsT1RequestsSent,
       "alDhcpStatsT2RequestsSent": alDhcpStatsT2RequestsSent,
       "alDhcpStatsInitAcksRcvd": alDhcpStatsInitAcksRcvd,
       "alDhcpStatsInitNaksRcvd": alDhcpStatsInitNaksRcvd,
       "alDhcpStatsT1AcksRcvd": alDhcpStatsT1AcksRcvd,
       "alDhcpStatsT1NaksRcvd": alDhcpStatsT1NaksRcvd,
       "alDhcpStatsT2AcksRcvd": alDhcpStatsT2AcksRcvd,
       "alDhcpStatsT2NaksRcvd": alDhcpStatsT2NaksRcvd,
       "alDhcpStatsT1Timeouts": alDhcpStatsT1Timeouts,
       "alDhcpStatsT2Timeouts": alDhcpStatsT2Timeouts,
       "alDhcpStatsApiRequests": alDhcpStatsApiRequests,
       "alDhcpStatsLeaseTimeouts": alDhcpStatsLeaseTimeouts,
       "alDhcpStatsSessTable": alDhcpStatsSessTable,
       "alDhcpStatsSessEntry": alDhcpStatsSessEntry,
       "alDhcpStatsSessRowStatus": alDhcpStatsSessRowStatus,
       "alDhcpStatsSessId": alDhcpStatsSessId,
       "alDhcpStatsSessKey": alDhcpStatsSessKey,
       "alDhcpStatsSessIpAddr": alDhcpStatsSessIpAddr,
       "alDhcpStatsSessUpTime": alDhcpStatsSessUpTime,
       "alDhcpStatsSessLeaseDuration": alDhcpStatsSessLeaseDuration,
       "alDhcpStatsSessLeaseExpire": alDhcpStatsSessLeaseExpire,
       "alDhcpStatsSessState": alDhcpStatsSessState,
       "alDhcpStatsSessClientId": alDhcpStatsSessClientId,
       "alDhcpStatsSessSrvrIpAddr": alDhcpStatsSessSrvrIpAddr}
)
