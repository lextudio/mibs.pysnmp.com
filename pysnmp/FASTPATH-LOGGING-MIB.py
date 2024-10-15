# SNMP MIB module (FASTPATH-LOGGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-LOGGING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:54 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "BROADCOM-REF-MIB",
    "fastPath")

(agentInventoryComponentIndex,) = mibBuilder.importSymbols(
    "FASTPATH-INVENTORY-MIB",
    "agentInventoryComponentIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathLogging = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14)
)
fastPathLogging.setRevisions(
        ("2007-05-23 00:00",
         "2004-10-26 13:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentLogFacility(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("alert", 14),
          ("audit", 13),
          ("auth", 10),
          ("clock", 15),
          ("cron", 9),
          ("ftp", 11),
          ("kernel", 0),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("lpr", 6),
          ("mail", 2),
          ("nntp", 7),
          ("ntp", 12),
          ("security", 4),
          ("syslog", 5),
          ("system", 3),
          ("user", 1),
          ("uucp", 8))
    )



class AgentLogSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("informational", 6),
          ("notice", 5),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AgentLogConfigGroup_ObjectIdentity = ObjectIdentity
agentLogConfigGroup = _AgentLogConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1)
)
_AgentLogInMemoryConfigGroup_ObjectIdentity = ObjectIdentity
agentLogInMemoryConfigGroup = _AgentLogInMemoryConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1)
)


class _AgentLogInMemoryAdminStatus_Type(Integer32):
    """Custom type agentLogInMemoryAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLogInMemoryAdminStatus_Type.__name__ = "Integer32"
_AgentLogInMemoryAdminStatus_Object = MibScalar
agentLogInMemoryAdminStatus = _AgentLogInMemoryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1, 1),
    _AgentLogInMemoryAdminStatus_Type()
)
agentLogInMemoryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogInMemoryAdminStatus.setStatus("current")


class _AgentLogInMemoryBehavior_Type(Integer32):
    """Custom type agentLogInMemoryBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop-on-full", 2),
          ("wrap", 1))
    )


_AgentLogInMemoryBehavior_Type.__name__ = "Integer32"
_AgentLogInMemoryBehavior_Object = MibScalar
agentLogInMemoryBehavior = _AgentLogInMemoryBehavior_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1, 4),
    _AgentLogInMemoryBehavior_Type()
)
agentLogInMemoryBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogInMemoryBehavior.setStatus("current")
_AgentLogConsoleConfigGroup_ObjectIdentity = ObjectIdentity
agentLogConsoleConfigGroup = _AgentLogConsoleConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2)
)


class _AgentLogConsoleAdminStatus_Type(Integer32):
    """Custom type agentLogConsoleAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLogConsoleAdminStatus_Type.__name__ = "Integer32"
_AgentLogConsoleAdminStatus_Object = MibScalar
agentLogConsoleAdminStatus = _AgentLogConsoleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2, 1),
    _AgentLogConsoleAdminStatus_Type()
)
agentLogConsoleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogConsoleAdminStatus.setStatus("current")
_AgentLogConsoleSeverityFilter_Type = AgentLogSeverity
_AgentLogConsoleSeverityFilter_Object = MibScalar
agentLogConsoleSeverityFilter = _AgentLogConsoleSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2, 2),
    _AgentLogConsoleSeverityFilter_Type()
)
agentLogConsoleSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogConsoleSeverityFilter.setStatus("current")
_AgentLogPersistentConfigGroup_ObjectIdentity = ObjectIdentity
agentLogPersistentConfigGroup = _AgentLogPersistentConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 3)
)


class _AgentLogPersistentAdminStatus_Type(Integer32):
    """Custom type agentLogPersistentAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLogPersistentAdminStatus_Type.__name__ = "Integer32"
_AgentLogPersistentAdminStatus_Object = MibScalar
agentLogPersistentAdminStatus = _AgentLogPersistentAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 3, 1),
    _AgentLogPersistentAdminStatus_Type()
)
agentLogPersistentAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogPersistentAdminStatus.setStatus("current")
_AgentLogPersistentSeverityFilter_Type = AgentLogSeverity
_AgentLogPersistentSeverityFilter_Object = MibScalar
agentLogPersistentSeverityFilter = _AgentLogPersistentSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 3, 2),
    _AgentLogPersistentSeverityFilter_Type()
)
agentLogPersistentSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogPersistentSeverityFilter.setStatus("current")
_AgentLogSysLogConfigGroup_ObjectIdentity = ObjectIdentity
agentLogSysLogConfigGroup = _AgentLogSysLogConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4)
)


class _AgentLogSyslogAdminStatus_Type(Integer32):
    """Custom type agentLogSyslogAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLogSyslogAdminStatus_Type.__name__ = "Integer32"
_AgentLogSyslogAdminStatus_Object = MibScalar
agentLogSyslogAdminStatus = _AgentLogSyslogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 1),
    _AgentLogSyslogAdminStatus_Type()
)
agentLogSyslogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogSyslogAdminStatus.setStatus("current")


class _AgentLogSyslogLocalPort_Type(Unsigned32):
    """Custom type agentLogSyslogLocalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentLogSyslogLocalPort_Type.__name__ = "Unsigned32"
_AgentLogSyslogLocalPort_Object = MibScalar
agentLogSyslogLocalPort = _AgentLogSyslogLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 3),
    _AgentLogSyslogLocalPort_Type()
)
agentLogSyslogLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogSyslogLocalPort.setStatus("current")
_AgentLogSyslogMaxHosts_Type = Unsigned32
_AgentLogSyslogMaxHosts_Object = MibScalar
agentLogSyslogMaxHosts = _AgentLogSyslogMaxHosts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 4),
    _AgentLogSyslogMaxHosts_Type()
)
agentLogSyslogMaxHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogSyslogMaxHosts.setStatus("current")
_AgentLogSyslogHostTable_Object = MibTable
agentLogSyslogHostTable = _AgentLogSyslogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5)
)
if mibBuilder.loadTexts:
    agentLogSyslogHostTable.setStatus("current")
_AgentLogSyslogHostEntry_Object = MibTableRow
agentLogSyslogHostEntry = _AgentLogSyslogHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1)
)
agentLogSyslogHostEntry.setIndexNames(
    (0, "FASTPATH-LOGGING-MIB", "agentLogHostTableIndex"),
)
if mibBuilder.loadTexts:
    agentLogSyslogHostEntry.setStatus("current")
_AgentLogHostTableIndex_Type = Unsigned32
_AgentLogHostTableIndex_Object = MibTableColumn
agentLogHostTableIndex = _AgentLogHostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 1),
    _AgentLogHostTableIndex_Type()
)
agentLogHostTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLogHostTableIndex.setStatus("current")
_AgentLogHostTableIpAddressType_Type = InetAddressType
_AgentLogHostTableIpAddressType_Object = MibTableColumn
agentLogHostTableIpAddressType = _AgentLogHostTableIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 2),
    _AgentLogHostTableIpAddressType_Type()
)
agentLogHostTableIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogHostTableIpAddressType.setStatus("current")
_AgentLogHostTableIpAddress_Type = InetAddress
_AgentLogHostTableIpAddress_Object = MibTableColumn
agentLogHostTableIpAddress = _AgentLogHostTableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 3),
    _AgentLogHostTableIpAddress_Type()
)
agentLogHostTableIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogHostTableIpAddress.setStatus("current")


class _AgentLogHostTablePort_Type(Unsigned32):
    """Custom type agentLogHostTablePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentLogHostTablePort_Type.__name__ = "Unsigned32"
_AgentLogHostTablePort_Object = MibTableColumn
agentLogHostTablePort = _AgentLogHostTablePort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 4),
    _AgentLogHostTablePort_Type()
)
agentLogHostTablePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogHostTablePort.setStatus("current")
_AgentLogHostTableSeverityFilter_Type = AgentLogSeverity
_AgentLogHostTableSeverityFilter_Object = MibTableColumn
agentLogHostTableSeverityFilter = _AgentLogHostTableSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 5),
    _AgentLogHostTableSeverityFilter_Type()
)
agentLogHostTableSeverityFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogHostTableSeverityFilter.setStatus("current")
_AgentLogHostTableRowStatus_Type = RowStatus
_AgentLogHostTableRowStatus_Object = MibTableColumn
agentLogHostTableRowStatus = _AgentLogHostTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 7),
    _AgentLogHostTableRowStatus_Type()
)
agentLogHostTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogHostTableRowStatus.setStatus("current")
_AgentLogCliCommandsConfigGroup_ObjectIdentity = ObjectIdentity
agentLogCliCommandsConfigGroup = _AgentLogCliCommandsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 5)
)


class _AgentLogCliCommandsAdminStatus_Type(Integer32):
    """Custom type agentLogCliCommandsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLogCliCommandsAdminStatus_Type.__name__ = "Integer32"
_AgentLogCliCommandsAdminStatus_Object = MibScalar
agentLogCliCommandsAdminStatus = _AgentLogCliCommandsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 5, 1),
    _AgentLogCliCommandsAdminStatus_Type()
)
agentLogCliCommandsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogCliCommandsAdminStatus.setStatus("current")
_AgentLogStatisticsGroup_ObjectIdentity = ObjectIdentity
agentLogStatisticsGroup = _AgentLogStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2)
)
_AgentLogMessagesReceived_Type = Counter32
_AgentLogMessagesReceived_Object = MibScalar
agentLogMessagesReceived = _AgentLogMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 1),
    _AgentLogMessagesReceived_Type()
)
agentLogMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogMessagesReceived.setStatus("current")
_AgentLogMessagesDropped_Type = Counter32
_AgentLogMessagesDropped_Object = MibScalar
agentLogMessagesDropped = _AgentLogMessagesDropped_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 2),
    _AgentLogMessagesDropped_Type()
)
agentLogMessagesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogMessagesDropped.setStatus("current")
_AgentLogSyslogMessagesRelayed_Type = Counter32
_AgentLogSyslogMessagesRelayed_Object = MibScalar
agentLogSyslogMessagesRelayed = _AgentLogSyslogMessagesRelayed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 3),
    _AgentLogSyslogMessagesRelayed_Type()
)
agentLogSyslogMessagesRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogSyslogMessagesRelayed.setStatus("current")
_AgentLogSyslogMessagesIgnored_Type = Counter32
_AgentLogSyslogMessagesIgnored_Object = MibScalar
agentLogSyslogMessagesIgnored = _AgentLogSyslogMessagesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 4),
    _AgentLogSyslogMessagesIgnored_Type()
)
agentLogSyslogMessagesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogSyslogMessagesIgnored.setStatus("deprecated")
_AgentLogMessageReceivedTime_Type = DateAndTime
_AgentLogMessageReceivedTime_Object = MibScalar
agentLogMessageReceivedTime = _AgentLogMessageReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 5),
    _AgentLogMessageReceivedTime_Type()
)
agentLogMessageReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogMessageReceivedTime.setStatus("current")
_AgentLogSyslogMessageDeliveredTime_Type = DateAndTime
_AgentLogSyslogMessageDeliveredTime_Object = MibScalar
agentLogSyslogMessageDeliveredTime = _AgentLogSyslogMessageDeliveredTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 6),
    _AgentLogSyslogMessageDeliveredTime_Type()
)
agentLogSyslogMessageDeliveredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogSyslogMessageDeliveredTime.setStatus("current")
_AgentLogInMemoryGroup_ObjectIdentity = ObjectIdentity
agentLogInMemoryGroup = _AgentLogInMemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3)
)
_AgentLogInMemoryLogCount_Type = Gauge32
_AgentLogInMemoryLogCount_Object = MibScalar
agentLogInMemoryLogCount = _AgentLogInMemoryLogCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 1),
    _AgentLogInMemoryLogCount_Type()
)
agentLogInMemoryLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogInMemoryLogCount.setStatus("current")
_AgentLogInMemoryTable_Object = MibTable
agentLogInMemoryTable = _AgentLogInMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2)
)
if mibBuilder.loadTexts:
    agentLogInMemoryTable.setStatus("current")
_AgentLogInMemoryEntry_Object = MibTableRow
agentLogInMemoryEntry = _AgentLogInMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1)
)
agentLogInMemoryEntry.setIndexNames(
    (0, "FASTPATH-LOGGING-MIB", "agentLogInMemoryMsgIndex"),
)
if mibBuilder.loadTexts:
    agentLogInMemoryEntry.setStatus("current")
_AgentLogInMemoryMsgIndex_Type = Unsigned32
_AgentLogInMemoryMsgIndex_Object = MibTableColumn
agentLogInMemoryMsgIndex = _AgentLogInMemoryMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1, 1),
    _AgentLogInMemoryMsgIndex_Type()
)
agentLogInMemoryMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLogInMemoryMsgIndex.setStatus("current")
_AgentLogInMemoryMsgText_Type = DisplayString
_AgentLogInMemoryMsgText_Object = MibTableColumn
agentLogInMemoryMsgText = _AgentLogInMemoryMsgText_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1, 2),
    _AgentLogInMemoryMsgText_Type()
)
agentLogInMemoryMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogInMemoryMsgText.setStatus("current")
_AgentLogPersistentGroup_ObjectIdentity = ObjectIdentity
agentLogPersistentGroup = _AgentLogPersistentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4)
)
_AgentLogPersistentLogCount_Type = Counter32
_AgentLogPersistentLogCount_Object = MibScalar
agentLogPersistentLogCount = _AgentLogPersistentLogCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 1),
    _AgentLogPersistentLogCount_Type()
)
agentLogPersistentLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogPersistentLogCount.setStatus("current")
_AgentLogPersistentTable_Object = MibTable
agentLogPersistentTable = _AgentLogPersistentTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 4)
)
if mibBuilder.loadTexts:
    agentLogPersistentTable.setStatus("current")
_AgentLogPersistentEntry_Object = MibTableRow
agentLogPersistentEntry = _AgentLogPersistentEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 4, 1)
)
agentLogPersistentEntry.setIndexNames(
    (0, "FASTPATH-LOGGING-MIB", "agentLogMsgPersistentMsgIndex"),
)
if mibBuilder.loadTexts:
    agentLogPersistentEntry.setStatus("current")
_AgentLogMsgPersistentMsgIndex_Type = Unsigned32
_AgentLogMsgPersistentMsgIndex_Object = MibTableColumn
agentLogMsgPersistentMsgIndex = _AgentLogMsgPersistentMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 4, 1, 1),
    _AgentLogMsgPersistentMsgIndex_Type()
)
agentLogMsgPersistentMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLogMsgPersistentMsgIndex.setStatus("current")
_AgentLogMsgPersistentMsgText_Type = DisplayString
_AgentLogMsgPersistentMsgText_Object = MibTableColumn
agentLogMsgPersistentMsgText = _AgentLogMsgPersistentMsgText_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 4, 1, 2),
    _AgentLogMsgPersistentMsgText_Type()
)
agentLogMsgPersistentMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogMsgPersistentMsgText.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-LOGGING-MIB",
    **{"AgentLogFacility": AgentLogFacility,
       "AgentLogSeverity": AgentLogSeverity,
       "fastPathLogging": fastPathLogging,
       "agentLogConfigGroup": agentLogConfigGroup,
       "agentLogInMemoryConfigGroup": agentLogInMemoryConfigGroup,
       "agentLogInMemoryAdminStatus": agentLogInMemoryAdminStatus,
       "agentLogInMemoryBehavior": agentLogInMemoryBehavior,
       "agentLogConsoleConfigGroup": agentLogConsoleConfigGroup,
       "agentLogConsoleAdminStatus": agentLogConsoleAdminStatus,
       "agentLogConsoleSeverityFilter": agentLogConsoleSeverityFilter,
       "agentLogPersistentConfigGroup": agentLogPersistentConfigGroup,
       "agentLogPersistentAdminStatus": agentLogPersistentAdminStatus,
       "agentLogPersistentSeverityFilter": agentLogPersistentSeverityFilter,
       "agentLogSysLogConfigGroup": agentLogSysLogConfigGroup,
       "agentLogSyslogAdminStatus": agentLogSyslogAdminStatus,
       "agentLogSyslogLocalPort": agentLogSyslogLocalPort,
       "agentLogSyslogMaxHosts": agentLogSyslogMaxHosts,
       "agentLogSyslogHostTable": agentLogSyslogHostTable,
       "agentLogSyslogHostEntry": agentLogSyslogHostEntry,
       "agentLogHostTableIndex": agentLogHostTableIndex,
       "agentLogHostTableIpAddressType": agentLogHostTableIpAddressType,
       "agentLogHostTableIpAddress": agentLogHostTableIpAddress,
       "agentLogHostTablePort": agentLogHostTablePort,
       "agentLogHostTableSeverityFilter": agentLogHostTableSeverityFilter,
       "agentLogHostTableRowStatus": agentLogHostTableRowStatus,
       "agentLogCliCommandsConfigGroup": agentLogCliCommandsConfigGroup,
       "agentLogCliCommandsAdminStatus": agentLogCliCommandsAdminStatus,
       "agentLogStatisticsGroup": agentLogStatisticsGroup,
       "agentLogMessagesReceived": agentLogMessagesReceived,
       "agentLogMessagesDropped": agentLogMessagesDropped,
       "agentLogSyslogMessagesRelayed": agentLogSyslogMessagesRelayed,
       "agentLogSyslogMessagesIgnored": agentLogSyslogMessagesIgnored,
       "agentLogMessageReceivedTime": agentLogMessageReceivedTime,
       "agentLogSyslogMessageDeliveredTime": agentLogSyslogMessageDeliveredTime,
       "agentLogInMemoryGroup": agentLogInMemoryGroup,
       "agentLogInMemoryLogCount": agentLogInMemoryLogCount,
       "agentLogInMemoryTable": agentLogInMemoryTable,
       "agentLogInMemoryEntry": agentLogInMemoryEntry,
       "agentLogInMemoryMsgIndex": agentLogInMemoryMsgIndex,
       "agentLogInMemoryMsgText": agentLogInMemoryMsgText,
       "agentLogPersistentGroup": agentLogPersistentGroup,
       "agentLogPersistentLogCount": agentLogPersistentLogCount,
       "agentLogPersistentTable": agentLogPersistentTable,
       "agentLogPersistentEntry": agentLogPersistentEntry,
       "agentLogMsgPersistentMsgIndex": agentLogMsgPersistentMsgIndex,
       "agentLogMsgPersistentMsgText": agentLogMsgPersistentMsgText}
)
