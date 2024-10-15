# SNMP MIB module (PINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:49 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(sysApplInstallPkgEntry,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "sysApplInstallPkgEntry")


# MODULE-IDENTITY

pintMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 93)
)
pintMib.setRevisions(
        ("2001-02-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PintServiceType(Integer32, TextualConvention):
    status = "current"
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
        *(("r2C", 1),
          ("r2F", 2),
          ("r2FB", 3),
          ("r2HC", 4))
    )



class PintPerfStatPeriod(Integer32, TextualConvention):
    status = "current"
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
        *(("last15min", 2),
          ("last24Hr", 3),
          ("last30sec", 1),
          ("sinceReboot", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PintServerConfig_ObjectIdentity = ObjectIdentity
pintServerConfig = _PintServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 1)
)
_PintReleaseNumber_Type = SnmpAdminString
_PintReleaseNumber_Object = MibScalar
pintReleaseNumber = _PintReleaseNumber_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 1),
    _PintReleaseNumber_Type()
)
pintReleaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintReleaseNumber.setStatus("current")
_PintSysContact_Type = SnmpAdminString
_PintSysContact_Object = MibScalar
pintSysContact = _PintSysContact_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 2),
    _PintSysContact_Type()
)
pintSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pintSysContact.setStatus("current")
_PintApplInstallPkgTable_Object = MibTable
pintApplInstallPkgTable = _PintApplInstallPkgTable_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 3)
)
if mibBuilder.loadTexts:
    pintApplInstallPkgTable.setStatus("current")
_PintApplInstallPkgEntry_Object = MibTableRow
pintApplInstallPkgEntry = _PintApplInstallPkgEntry_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pintApplInstallPkgEntry.setStatus("current")
_PintApplInstallPkgDescription_Type = SnmpAdminString
_PintApplInstallPkgDescription_Object = MibTableColumn
pintApplInstallPkgDescription = _PintApplInstallPkgDescription_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 3, 1, 1),
    _PintApplInstallPkgDescription_Type()
)
pintApplInstallPkgDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintApplInstallPkgDescription.setStatus("current")
_PintRegisteredGatewayTable_Object = MibTable
pintRegisteredGatewayTable = _PintRegisteredGatewayTable_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 4)
)
if mibBuilder.loadTexts:
    pintRegisteredGatewayTable.setStatus("current")
_PintRegisteredGatewayEntry_Object = MibTableRow
pintRegisteredGatewayEntry = _PintRegisteredGatewayEntry_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pintRegisteredGatewayEntry.setStatus("current")
_PintRegisteredGatewayName_Type = SnmpAdminString
_PintRegisteredGatewayName_Object = MibTableColumn
pintRegisteredGatewayName = _PintRegisteredGatewayName_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 4, 1, 1),
    _PintRegisteredGatewayName_Type()
)
pintRegisteredGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintRegisteredGatewayName.setStatus("current")
_PintRegisteredGatewayDescription_Type = SnmpAdminString
_PintRegisteredGatewayDescription_Object = MibTableColumn
pintRegisteredGatewayDescription = _PintRegisteredGatewayDescription_Object(
    (1, 3, 6, 1, 2, 1, 93, 1, 4, 1, 2),
    _PintRegisteredGatewayDescription_Type()
)
pintRegisteredGatewayDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintRegisteredGatewayDescription.setStatus("current")
_PintServerMonitor_ObjectIdentity = ObjectIdentity
pintServerMonitor = _PintServerMonitor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 2)
)
_PintServerGlobalPerf_ObjectIdentity = ObjectIdentity
pintServerGlobalPerf = _PintServerGlobalPerf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 2, 1)
)
_PintServerGlobalStatsTable_Object = MibTable
pintServerGlobalStatsTable = _PintServerGlobalStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pintServerGlobalStatsTable.setStatus("current")
_PintServerGlobalStatsEntry_Object = MibTableRow
pintServerGlobalStatsEntry = _PintServerGlobalStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1)
)
pintServerGlobalStatsEntry.setIndexNames(
    (0, "PINT-MIB", "pintServerServiceTypeIndex"),
    (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"),
)
if mibBuilder.loadTexts:
    pintServerGlobalStatsEntry.setStatus("current")
_PintServerServiceTypeIndex_Type = PintServiceType
_PintServerServiceTypeIndex_Object = MibTableColumn
pintServerServiceTypeIndex = _PintServerServiceTypeIndex_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 1),
    _PintServerServiceTypeIndex_Type()
)
pintServerServiceTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pintServerServiceTypeIndex.setStatus("current")
_PintServerPerfStatPeriodIndex_Type = PintPerfStatPeriod
_PintServerPerfStatPeriodIndex_Object = MibTableColumn
pintServerPerfStatPeriodIndex = _PintServerPerfStatPeriodIndex_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 2),
    _PintServerPerfStatPeriodIndex_Type()
)
pintServerPerfStatPeriodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pintServerPerfStatPeriodIndex.setStatus("current")
_PintServerGlobalCallsReceived_Type = Counter32
_PintServerGlobalCallsReceived_Object = MibTableColumn
pintServerGlobalCallsReceived = _PintServerGlobalCallsReceived_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 3),
    _PintServerGlobalCallsReceived_Type()
)
pintServerGlobalCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGlobalCallsReceived.setStatus("current")
_PintServerGlobalSuccessfulCalls_Type = Counter32
_PintServerGlobalSuccessfulCalls_Object = MibTableColumn
pintServerGlobalSuccessfulCalls = _PintServerGlobalSuccessfulCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 4),
    _PintServerGlobalSuccessfulCalls_Type()
)
pintServerGlobalSuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGlobalSuccessfulCalls.setStatus("current")
_PintServerGlobalDisconnectedCalls_Type = Counter32
_PintServerGlobalDisconnectedCalls_Object = MibTableColumn
pintServerGlobalDisconnectedCalls = _PintServerGlobalDisconnectedCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 5),
    _PintServerGlobalDisconnectedCalls_Type()
)
pintServerGlobalDisconnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGlobalDisconnectedCalls.setStatus("current")
_PintServerGlobalDisCUAutFCalls_Type = Counter32
_PintServerGlobalDisCUAutFCalls_Object = MibTableColumn
pintServerGlobalDisCUAutFCalls = _PintServerGlobalDisCUAutFCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 6),
    _PintServerGlobalDisCUAutFCalls_Type()
)
pintServerGlobalDisCUAutFCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGlobalDisCUAutFCalls.setStatus("current")
_PintServerGlobalDisServProbCalls_Type = Counter32
_PintServerGlobalDisServProbCalls_Object = MibTableColumn
pintServerGlobalDisServProbCalls = _PintServerGlobalDisServProbCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 7),
    _PintServerGlobalDisServProbCalls_Type()
)
pintServerGlobalDisServProbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGlobalDisServProbCalls.setStatus("current")
_PintServerGlobalDisGatProbCalls_Type = Counter32
_PintServerGlobalDisGatProbCalls_Object = MibTableColumn
pintServerGlobalDisGatProbCalls = _PintServerGlobalDisGatProbCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 8),
    _PintServerGlobalDisGatProbCalls_Type()
)
pintServerGlobalDisGatProbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGlobalDisGatProbCalls.setStatus("current")
_PintServerClientPerf_ObjectIdentity = ObjectIdentity
pintServerClientPerf = _PintServerClientPerf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 2, 2)
)
_PintServerClientStatsTable_Object = MibTable
pintServerClientStatsTable = _PintServerClientStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pintServerClientStatsTable.setStatus("current")
_PintServerClientStatsEntry_Object = MibTableRow
pintServerClientStatsEntry = _PintServerClientStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1)
)
pintServerClientStatsEntry.setIndexNames(
    (0, "PINT-MIB", "pintServerClientAddress"),
    (0, "PINT-MIB", "pintServerServiceTypeIndex"),
    (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"),
)
if mibBuilder.loadTexts:
    pintServerClientStatsEntry.setStatus("current")
_PintServerClientAddress_Type = SnmpAdminString
_PintServerClientAddress_Object = MibTableColumn
pintServerClientAddress = _PintServerClientAddress_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 1),
    _PintServerClientAddress_Type()
)
pintServerClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pintServerClientAddress.setStatus("current")
_PintServerClientCallsReceived_Type = Counter32
_PintServerClientCallsReceived_Object = MibTableColumn
pintServerClientCallsReceived = _PintServerClientCallsReceived_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 2),
    _PintServerClientCallsReceived_Type()
)
pintServerClientCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerClientCallsReceived.setStatus("current")
_PintServerClientSuccessfulCalls_Type = Counter32
_PintServerClientSuccessfulCalls_Object = MibTableColumn
pintServerClientSuccessfulCalls = _PintServerClientSuccessfulCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 3),
    _PintServerClientSuccessfulCalls_Type()
)
pintServerClientSuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerClientSuccessfulCalls.setStatus("current")
_PintServerClientDisconnectedCalls_Type = Counter32
_PintServerClientDisconnectedCalls_Object = MibTableColumn
pintServerClientDisconnectedCalls = _PintServerClientDisconnectedCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 4),
    _PintServerClientDisconnectedCalls_Type()
)
pintServerClientDisconnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerClientDisconnectedCalls.setStatus("current")
_PintServerClientDisCAutFCalls_Type = Counter32
_PintServerClientDisCAutFCalls_Object = MibTableColumn
pintServerClientDisCAutFCalls = _PintServerClientDisCAutFCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 5),
    _PintServerClientDisCAutFCalls_Type()
)
pintServerClientDisCAutFCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerClientDisCAutFCalls.setStatus("current")
_PintServerClientDisEFProbCalls_Type = Counter32
_PintServerClientDisEFProbCalls_Object = MibTableColumn
pintServerClientDisEFProbCalls = _PintServerClientDisEFProbCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 6),
    _PintServerClientDisEFProbCalls_Type()
)
pintServerClientDisEFProbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerClientDisEFProbCalls.setStatus("current")
_PintServerUserIdPerf_ObjectIdentity = ObjectIdentity
pintServerUserIdPerf = _PintServerUserIdPerf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 2, 3)
)
_PintServerUserIdStatsTable_Object = MibTable
pintServerUserIdStatsTable = _PintServerUserIdStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pintServerUserIdStatsTable.setStatus("current")
_PintServerUserIdStatsEntry_Object = MibTableRow
pintServerUserIdStatsEntry = _PintServerUserIdStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1)
)
pintServerUserIdStatsEntry.setIndexNames(
    (0, "PINT-MIB", "pintServerUserIdName"),
    (0, "PINT-MIB", "pintServerServiceTypeIndex"),
    (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"),
)
if mibBuilder.loadTexts:
    pintServerUserIdStatsEntry.setStatus("current")


class _PintServerUserIdName_Type(SnmpAdminString):
    """Custom type pintServerUserIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PintServerUserIdName_Type.__name__ = "SnmpAdminString"
_PintServerUserIdName_Object = MibTableColumn
pintServerUserIdName = _PintServerUserIdName_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 1),
    _PintServerUserIdName_Type()
)
pintServerUserIdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pintServerUserIdName.setStatus("current")
_PintServerUserIdCallsReceived_Type = Counter32
_PintServerUserIdCallsReceived_Object = MibTableColumn
pintServerUserIdCallsReceived = _PintServerUserIdCallsReceived_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 2),
    _PintServerUserIdCallsReceived_Type()
)
pintServerUserIdCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerUserIdCallsReceived.setStatus("current")
_PintServerUserIdSuccessfulCalls_Type = Counter32
_PintServerUserIdSuccessfulCalls_Object = MibTableColumn
pintServerUserIdSuccessfulCalls = _PintServerUserIdSuccessfulCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 3),
    _PintServerUserIdSuccessfulCalls_Type()
)
pintServerUserIdSuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerUserIdSuccessfulCalls.setStatus("current")
_PintServerUserIdDisconnectedCalls_Type = Counter32
_PintServerUserIdDisconnectedCalls_Object = MibTableColumn
pintServerUserIdDisconnectedCalls = _PintServerUserIdDisconnectedCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 4),
    _PintServerUserIdDisconnectedCalls_Type()
)
pintServerUserIdDisconnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerUserIdDisconnectedCalls.setStatus("current")
_PintServerUserIdDiscUIdAFailCalls_Type = Counter32
_PintServerUserIdDiscUIdAFailCalls_Object = MibTableColumn
pintServerUserIdDiscUIdAFailCalls = _PintServerUserIdDiscUIdAFailCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 5),
    _PintServerUserIdDiscUIdAFailCalls_Type()
)
pintServerUserIdDiscUIdAFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerUserIdDiscUIdAFailCalls.setStatus("current")
_PintServerUserIdEFProbCalls_Type = Counter32
_PintServerUserIdEFProbCalls_Object = MibTableColumn
pintServerUserIdEFProbCalls = _PintServerUserIdEFProbCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 6),
    _PintServerUserIdEFProbCalls_Type()
)
pintServerUserIdEFProbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerUserIdEFProbCalls.setStatus("current")
_PintServerGatewayPerf_ObjectIdentity = ObjectIdentity
pintServerGatewayPerf = _PintServerGatewayPerf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 2, 4)
)
_PintServerGatewayStatsTable_Object = MibTable
pintServerGatewayStatsTable = _PintServerGatewayStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 4, 1)
)
if mibBuilder.loadTexts:
    pintServerGatewayStatsTable.setStatus("current")
_PintServerGatewayStatsEntry_Object = MibTableRow
pintServerGatewayStatsEntry = _PintServerGatewayStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1)
)
pintServerGatewayStatsEntry.setIndexNames(
    (0, "PINT-MIB", "pintRegisteredGatewayName"),
    (0, "PINT-MIB", "pintServerServiceTypeIndex"),
    (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"),
)
if mibBuilder.loadTexts:
    pintServerGatewayStatsEntry.setStatus("current")
_PintServerGatewayCallsReceived_Type = Counter32
_PintServerGatewayCallsReceived_Object = MibTableColumn
pintServerGatewayCallsReceived = _PintServerGatewayCallsReceived_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 1),
    _PintServerGatewayCallsReceived_Type()
)
pintServerGatewayCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGatewayCallsReceived.setStatus("current")
_PintServerGatewaySuccessfulCalls_Type = Counter32
_PintServerGatewaySuccessfulCalls_Object = MibTableColumn
pintServerGatewaySuccessfulCalls = _PintServerGatewaySuccessfulCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 2),
    _PintServerGatewaySuccessfulCalls_Type()
)
pintServerGatewaySuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGatewaySuccessfulCalls.setStatus("current")
_PintServerGatewayDisconnectedCalls_Type = Counter32
_PintServerGatewayDisconnectedCalls_Object = MibTableColumn
pintServerGatewayDisconnectedCalls = _PintServerGatewayDisconnectedCalls_Object(
    (1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 3),
    _PintServerGatewayDisconnectedCalls_Type()
)
pintServerGatewayDisconnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pintServerGatewayDisconnectedCalls.setStatus("current")
_PintMibConformance_ObjectIdentity = ObjectIdentity
pintMibConformance = _PintMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 3)
)
_PintMibCompliances_ObjectIdentity = ObjectIdentity
pintMibCompliances = _PintMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 3, 1)
)
_PintMibGroups_ObjectIdentity = ObjectIdentity
pintMibGroups = _PintMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 93, 3, 2)
)
sysApplInstallPkgEntry.registerAugmentions(
    ("PINT-MIB",
     "pintApplInstallPkgEntry")
)
pintApplInstallPkgEntry.setIndexNames(*sysApplInstallPkgEntry.getIndexNames())
sysApplInstallPkgEntry.registerAugmentions(
    ("PINT-MIB",
     "pintRegisteredGatewayEntry")
)
pintRegisteredGatewayEntry.setIndexNames(*sysApplInstallPkgEntry.getIndexNames())

# Managed Objects groups

pintMibConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 93, 3, 2, 1)
)
pintMibConfigGroup.setObjects(
      *(("PINT-MIB", "pintReleaseNumber"),
        ("PINT-MIB", "pintSysContact"),
        ("PINT-MIB", "pintApplInstallPkgDescription"),
        ("PINT-MIB", "pintRegisteredGatewayName"),
        ("PINT-MIB", "pintRegisteredGatewayDescription"))
)
if mibBuilder.loadTexts:
    pintMibConfigGroup.setStatus("current")

pintMibMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 93, 3, 2, 2)
)
pintMibMonitorGroup.setObjects(
      *(("PINT-MIB", "pintServerGlobalCallsReceived"),
        ("PINT-MIB", "pintServerGlobalSuccessfulCalls"),
        ("PINT-MIB", "pintServerGlobalDisconnectedCalls"),
        ("PINT-MIB", "pintServerGlobalDisCUAutFCalls"),
        ("PINT-MIB", "pintServerGlobalDisServProbCalls"),
        ("PINT-MIB", "pintServerGlobalDisGatProbCalls"),
        ("PINT-MIB", "pintServerClientCallsReceived"),
        ("PINT-MIB", "pintServerClientSuccessfulCalls"),
        ("PINT-MIB", "pintServerClientDisconnectedCalls"),
        ("PINT-MIB", "pintServerClientDisCAutFCalls"),
        ("PINT-MIB", "pintServerClientDisEFProbCalls"),
        ("PINT-MIB", "pintServerUserIdCallsReceived"),
        ("PINT-MIB", "pintServerUserIdSuccessfulCalls"),
        ("PINT-MIB", "pintServerUserIdDisconnectedCalls"),
        ("PINT-MIB", "pintServerUserIdDiscUIdAFailCalls"),
        ("PINT-MIB", "pintServerUserIdEFProbCalls"),
        ("PINT-MIB", "pintServerGatewayCallsReceived"),
        ("PINT-MIB", "pintServerGatewaySuccessfulCalls"),
        ("PINT-MIB", "pintServerGatewayDisconnectedCalls"))
)
if mibBuilder.loadTexts:
    pintMibMonitorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pintMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 93, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pintMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PINT-MIB",
    **{"PintServiceType": PintServiceType,
       "PintPerfStatPeriod": PintPerfStatPeriod,
       "pintMib": pintMib,
       "pintServerConfig": pintServerConfig,
       "pintReleaseNumber": pintReleaseNumber,
       "pintSysContact": pintSysContact,
       "pintApplInstallPkgTable": pintApplInstallPkgTable,
       "pintApplInstallPkgEntry": pintApplInstallPkgEntry,
       "pintApplInstallPkgDescription": pintApplInstallPkgDescription,
       "pintRegisteredGatewayTable": pintRegisteredGatewayTable,
       "pintRegisteredGatewayEntry": pintRegisteredGatewayEntry,
       "pintRegisteredGatewayName": pintRegisteredGatewayName,
       "pintRegisteredGatewayDescription": pintRegisteredGatewayDescription,
       "pintServerMonitor": pintServerMonitor,
       "pintServerGlobalPerf": pintServerGlobalPerf,
       "pintServerGlobalStatsTable": pintServerGlobalStatsTable,
       "pintServerGlobalStatsEntry": pintServerGlobalStatsEntry,
       "pintServerServiceTypeIndex": pintServerServiceTypeIndex,
       "pintServerPerfStatPeriodIndex": pintServerPerfStatPeriodIndex,
       "pintServerGlobalCallsReceived": pintServerGlobalCallsReceived,
       "pintServerGlobalSuccessfulCalls": pintServerGlobalSuccessfulCalls,
       "pintServerGlobalDisconnectedCalls": pintServerGlobalDisconnectedCalls,
       "pintServerGlobalDisCUAutFCalls": pintServerGlobalDisCUAutFCalls,
       "pintServerGlobalDisServProbCalls": pintServerGlobalDisServProbCalls,
       "pintServerGlobalDisGatProbCalls": pintServerGlobalDisGatProbCalls,
       "pintServerClientPerf": pintServerClientPerf,
       "pintServerClientStatsTable": pintServerClientStatsTable,
       "pintServerClientStatsEntry": pintServerClientStatsEntry,
       "pintServerClientAddress": pintServerClientAddress,
       "pintServerClientCallsReceived": pintServerClientCallsReceived,
       "pintServerClientSuccessfulCalls": pintServerClientSuccessfulCalls,
       "pintServerClientDisconnectedCalls": pintServerClientDisconnectedCalls,
       "pintServerClientDisCAutFCalls": pintServerClientDisCAutFCalls,
       "pintServerClientDisEFProbCalls": pintServerClientDisEFProbCalls,
       "pintServerUserIdPerf": pintServerUserIdPerf,
       "pintServerUserIdStatsTable": pintServerUserIdStatsTable,
       "pintServerUserIdStatsEntry": pintServerUserIdStatsEntry,
       "pintServerUserIdName": pintServerUserIdName,
       "pintServerUserIdCallsReceived": pintServerUserIdCallsReceived,
       "pintServerUserIdSuccessfulCalls": pintServerUserIdSuccessfulCalls,
       "pintServerUserIdDisconnectedCalls": pintServerUserIdDisconnectedCalls,
       "pintServerUserIdDiscUIdAFailCalls": pintServerUserIdDiscUIdAFailCalls,
       "pintServerUserIdEFProbCalls": pintServerUserIdEFProbCalls,
       "pintServerGatewayPerf": pintServerGatewayPerf,
       "pintServerGatewayStatsTable": pintServerGatewayStatsTable,
       "pintServerGatewayStatsEntry": pintServerGatewayStatsEntry,
       "pintServerGatewayCallsReceived": pintServerGatewayCallsReceived,
       "pintServerGatewaySuccessfulCalls": pintServerGatewaySuccessfulCalls,
       "pintServerGatewayDisconnectedCalls": pintServerGatewayDisconnectedCalls,
       "pintMibConformance": pintMibConformance,
       "pintMibCompliances": pintMibCompliances,
       "pintMibCompliance": pintMibCompliance,
       "pintMibGroups": pintMibGroups,
       "pintMibConfigGroup": pintMibConfigGroup,
       "pintMibMonitorGroup": pintMibMonitorGroup}
)
