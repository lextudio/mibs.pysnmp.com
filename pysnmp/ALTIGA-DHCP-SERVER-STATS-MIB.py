# SNMP MIB module (ALTIGA-DHCP-SERVER-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-DHCP-SERVER-STATS-MIB
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

(alDhcpServerMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alDhcpServerMibModule")

(alDhcpServerGroup,
 alStatsDhcpServer) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alDhcpServerGroup",
    "alStatsDhcpServer")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

altigaDhcpServerStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 42, 2)
)
altigaDhcpServerStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaDhcpServerStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaDhcpServerStatsMibConformance = _AltigaDhcpServerStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 42, 2, 1)
)
_AltigaDhcpServerStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaDhcpServerStatsMibCompliances = _AltigaDhcpServerStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 42, 2, 1, 1)
)
_AlStatsDhcpServerGlobal_ObjectIdentity = ObjectIdentity
alStatsDhcpServerGlobal = _AlStatsDhcpServerGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 1)
)
_AlDhcpServerStatsActiveLeases_Type = Gauge32
_AlDhcpServerStatsActiveLeases_Object = MibScalar
alDhcpServerStatsActiveLeases = _AlDhcpServerStatsActiveLeases_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 1, 1),
    _AlDhcpServerStatsActiveLeases_Type()
)
alDhcpServerStatsActiveLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsActiveLeases.setStatus("current")
_AlDhcpServerStatsMaximumLeases_Type = Counter32
_AlDhcpServerStatsMaximumLeases_Object = MibScalar
alDhcpServerStatsMaximumLeases = _AlDhcpServerStatsMaximumLeases_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 1, 2),
    _AlDhcpServerStatsMaximumLeases_Type()
)
alDhcpServerStatsMaximumLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsMaximumLeases.setStatus("current")
_AlDhcpServerStatsDiscoversRcvd_Type = Counter32
_AlDhcpServerStatsDiscoversRcvd_Object = MibScalar
alDhcpServerStatsDiscoversRcvd = _AlDhcpServerStatsDiscoversRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 1, 3),
    _AlDhcpServerStatsDiscoversRcvd_Type()
)
alDhcpServerStatsDiscoversRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsDiscoversRcvd.setStatus("current")
_AlDhcpServerStatsOffersSent_Type = Counter32
_AlDhcpServerStatsOffersSent_Object = MibScalar
alDhcpServerStatsOffersSent = _AlDhcpServerStatsOffersSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 1, 4),
    _AlDhcpServerStatsOffersSent_Type()
)
alDhcpServerStatsOffersSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsOffersSent.setStatus("current")
_AlDhcpServerStatsAcksSent_Type = Counter32
_AlDhcpServerStatsAcksSent_Object = MibScalar
alDhcpServerStatsAcksSent = _AlDhcpServerStatsAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 1, 5),
    _AlDhcpServerStatsAcksSent_Type()
)
alDhcpServerStatsAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsAcksSent.setStatus("current")
_AlDhcpServerStatsNaksSent_Type = Counter32
_AlDhcpServerStatsNaksSent_Object = MibScalar
alDhcpServerStatsNaksSent = _AlDhcpServerStatsNaksSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 1, 6),
    _AlDhcpServerStatsNaksSent_Type()
)
alDhcpServerStatsNaksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsNaksSent.setStatus("current")
_AlDhcpServerStatsReqTimeouts_Type = Counter32
_AlDhcpServerStatsReqTimeouts_Object = MibScalar
alDhcpServerStatsReqTimeouts = _AlDhcpServerStatsReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 1, 7),
    _AlDhcpServerStatsReqTimeouts_Type()
)
alDhcpServerStatsReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsReqTimeouts.setStatus("current")
_AlDhcpServerStatsSessTable_Object = MibTable
alDhcpServerStatsSessTable = _AlDhcpServerStatsSessTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 2)
)
if mibBuilder.loadTexts:
    alDhcpServerStatsSessTable.setStatus("current")
_AlDhcpServerStatsSessEntry_Object = MibTableRow
alDhcpServerStatsSessEntry = _AlDhcpServerStatsSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 2, 1)
)
alDhcpServerStatsSessEntry.setIndexNames(
    (0, "ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsSessId"),
)
if mibBuilder.loadTexts:
    alDhcpServerStatsSessEntry.setStatus("current")
_AlDhcpServerStatsSessRowStatus_Type = RowStatus
_AlDhcpServerStatsSessRowStatus_Object = MibTableColumn
alDhcpServerStatsSessRowStatus = _AlDhcpServerStatsSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 2, 1, 1),
    _AlDhcpServerStatsSessRowStatus_Type()
)
alDhcpServerStatsSessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDhcpServerStatsSessRowStatus.setStatus("current")
_AlDhcpServerStatsSessId_Type = Integer32
_AlDhcpServerStatsSessId_Object = MibTableColumn
alDhcpServerStatsSessId = _AlDhcpServerStatsSessId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 2, 1, 2),
    _AlDhcpServerStatsSessId_Type()
)
alDhcpServerStatsSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsSessId.setStatus("current")
_AlDhcpServerStatsSessIpAddr_Type = IpAddress
_AlDhcpServerStatsSessIpAddr_Object = MibTableColumn
alDhcpServerStatsSessIpAddr = _AlDhcpServerStatsSessIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 2, 1, 3),
    _AlDhcpServerStatsSessIpAddr_Type()
)
alDhcpServerStatsSessIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsSessIpAddr.setStatus("current")
_AlDhcpServerStatsSessLeaseExpire_Type = Gauge32
_AlDhcpServerStatsSessLeaseExpire_Object = MibTableColumn
alDhcpServerStatsSessLeaseExpire = _AlDhcpServerStatsSessLeaseExpire_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 2, 1, 4),
    _AlDhcpServerStatsSessLeaseExpire_Type()
)
alDhcpServerStatsSessLeaseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsSessLeaseExpire.setStatus("current")
_AlDhcpServerStatsSessMacAddr_Type = MacAddress
_AlDhcpServerStatsSessMacAddr_Object = MibTableColumn
alDhcpServerStatsSessMacAddr = _AlDhcpServerStatsSessMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 2, 1, 5),
    _AlDhcpServerStatsSessMacAddr_Type()
)
alDhcpServerStatsSessMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsSessMacAddr.setStatus("current")
_AlDhcpServerStatsSessHostName_Type = DisplayString
_AlDhcpServerStatsSessHostName_Object = MibTableColumn
alDhcpServerStatsSessHostName = _AlDhcpServerStatsSessHostName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 37, 2, 1, 6),
    _AlDhcpServerStatsSessHostName_Type()
)
alDhcpServerStatsSessHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDhcpServerStatsSessHostName.setStatus("current")

# Managed Objects groups

altigaDhcpServerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 37, 2)
)
altigaDhcpServerStatsGroup.setObjects(
      *(("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsActiveLeases"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsMaximumLeases"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsDiscoversRcvd"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsOffersSent"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsAcksSent"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsNaksSent"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsReqTimeouts"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsSessRowStatus"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsSessId"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsSessIpAddr"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsSessLeaseExpire"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsSessMacAddr"),
        ("ALTIGA-DHCP-SERVER-STATS-MIB", "alDhcpServerStatsSessHostName"))
)
if mibBuilder.loadTexts:
    altigaDhcpServerStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaDhcpServerStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 42, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaDhcpServerStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-DHCP-SERVER-STATS-MIB",
    **{"altigaDhcpServerStatsMibModule": altigaDhcpServerStatsMibModule,
       "altigaDhcpServerStatsMibConformance": altigaDhcpServerStatsMibConformance,
       "altigaDhcpServerStatsMibCompliances": altigaDhcpServerStatsMibCompliances,
       "altigaDhcpServerStatsMibCompliance": altigaDhcpServerStatsMibCompliance,
       "altigaDhcpServerStatsGroup": altigaDhcpServerStatsGroup,
       "alStatsDhcpServerGlobal": alStatsDhcpServerGlobal,
       "alDhcpServerStatsActiveLeases": alDhcpServerStatsActiveLeases,
       "alDhcpServerStatsMaximumLeases": alDhcpServerStatsMaximumLeases,
       "alDhcpServerStatsDiscoversRcvd": alDhcpServerStatsDiscoversRcvd,
       "alDhcpServerStatsOffersSent": alDhcpServerStatsOffersSent,
       "alDhcpServerStatsAcksSent": alDhcpServerStatsAcksSent,
       "alDhcpServerStatsNaksSent": alDhcpServerStatsNaksSent,
       "alDhcpServerStatsReqTimeouts": alDhcpServerStatsReqTimeouts,
       "alDhcpServerStatsSessTable": alDhcpServerStatsSessTable,
       "alDhcpServerStatsSessEntry": alDhcpServerStatsSessEntry,
       "alDhcpServerStatsSessRowStatus": alDhcpServerStatsSessRowStatus,
       "alDhcpServerStatsSessId": alDhcpServerStatsSessId,
       "alDhcpServerStatsSessIpAddr": alDhcpServerStatsSessIpAddr,
       "alDhcpServerStatsSessLeaseExpire": alDhcpServerStatsSessLeaseExpire,
       "alDhcpServerStatsSessMacAddr": alDhcpServerStatsSessMacAddr,
       "alDhcpServerStatsSessHostName": alDhcpServerStatsSessHostName}
)
