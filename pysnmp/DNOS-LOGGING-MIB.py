# SNMP MIB module (DNOS-LOGGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-LOGGING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:03 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(agentInventoryComponentIndex,) = mibBuilder.importSymbols(
    "DNOS-INVENTORY-MIB",
    "agentInventoryComponentIndex")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
        ("2011-01-26 00:00",
         "2007-05-23 00:00",
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
    (0, "DNOS-LOGGING-MIB", "agentLogHostTableIndex"),
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
_AgentLogSyslogSourceInterface_Type = InterfaceIndexOrZero
_AgentLogSyslogSourceInterface_Object = MibScalar
agentLogSyslogSourceInterface = _AgentLogSyslogSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 6),
    _AgentLogSyslogSourceInterface_Type()
)
agentLogSyslogSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogSyslogSourceInterface.setStatus("current")
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
_AgentLogEmailAlertConfigGroup_ObjectIdentity = ObjectIdentity
agentLogEmailAlertConfigGroup = _AgentLogEmailAlertConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6)
)


class _AgentLogEmailAdminStatus_Type(Integer32):
    """Custom type agentLogEmailAdminStatus based on Integer32"""
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


_AgentLogEmailAdminStatus_Type.__name__ = "Integer32"
_AgentLogEmailAdminStatus_Object = MibScalar
agentLogEmailAdminStatus = _AgentLogEmailAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 1),
    _AgentLogEmailAdminStatus_Type()
)
agentLogEmailAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailAdminStatus.setStatus("current")
_AgentLogEmailfromAddr_Type = DisplayString
_AgentLogEmailfromAddr_Object = MibScalar
agentLogEmailfromAddr = _AgentLogEmailfromAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 2),
    _AgentLogEmailfromAddr_Type()
)
agentLogEmailfromAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailfromAddr.setStatus("current")


class _AgentLogEmaillogDuration_Type(Unsigned32):
    """Custom type agentLogEmaillogDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_AgentLogEmaillogDuration_Type.__name__ = "Unsigned32"
_AgentLogEmaillogDuration_Object = MibScalar
agentLogEmaillogDuration = _AgentLogEmaillogDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 3),
    _AgentLogEmaillogDuration_Type()
)
agentLogEmaillogDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmaillogDuration.setStatus("current")
_AgentLogEmailUrgentSeverity_Type = AgentLogSeverity
_AgentLogEmailUrgentSeverity_Object = MibScalar
agentLogEmailUrgentSeverity = _AgentLogEmailUrgentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 4),
    _AgentLogEmailUrgentSeverity_Type()
)
agentLogEmailUrgentSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailUrgentSeverity.setStatus("current")
_AgentLogEmailNonUrgentSeverity_Type = AgentLogSeverity
_AgentLogEmailNonUrgentSeverity_Object = MibScalar
agentLogEmailNonUrgentSeverity = _AgentLogEmailNonUrgentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 5),
    _AgentLogEmailNonUrgentSeverity_Type()
)
agentLogEmailNonUrgentSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailNonUrgentSeverity.setStatus("current")
_AgentLogEmailTrapsSeverity_Type = AgentLogSeverity
_AgentLogEmailTrapsSeverity_Object = MibScalar
agentLogEmailTrapsSeverity = _AgentLogEmailTrapsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 6),
    _AgentLogEmailTrapsSeverity_Type()
)
agentLogEmailTrapsSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailTrapsSeverity.setStatus("current")
_AgentLogEmailToAddrTable_Object = MibTable
agentLogEmailToAddrTable = _AgentLogEmailToAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7)
)
if mibBuilder.loadTexts:
    agentLogEmailToAddrTable.setStatus("current")
_AgentLogEmailToAddrEntry_Object = MibTableRow
agentLogEmailToAddrEntry = _AgentLogEmailToAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7, 1)
)
agentLogEmailToAddrEntry.setIndexNames(
    (0, "DNOS-LOGGING-MIB", "agentLogEmailToAddrMessageType"),
    (0, "DNOS-LOGGING-MIB", "agentLogEmailToAddr"),
)
if mibBuilder.loadTexts:
    agentLogEmailToAddrEntry.setStatus("current")


class _AgentLogEmailToAddrMessageType_Type(Integer32):
    """Custom type agentLogEmailToAddrMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("non-critical", 2))
    )


_AgentLogEmailToAddrMessageType_Type.__name__ = "Integer32"
_AgentLogEmailToAddrMessageType_Object = MibTableColumn
agentLogEmailToAddrMessageType = _AgentLogEmailToAddrMessageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7, 1, 1),
    _AgentLogEmailToAddrMessageType_Type()
)
agentLogEmailToAddrMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLogEmailToAddrMessageType.setStatus("current")
_AgentLogEmailToAddr_Type = DisplayString
_AgentLogEmailToAddr_Object = MibTableColumn
agentLogEmailToAddr = _AgentLogEmailToAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7, 1, 2),
    _AgentLogEmailToAddr_Type()
)
agentLogEmailToAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLogEmailToAddr.setStatus("current")
_AgentLogEmailToAddrEntryStatus_Type = RowStatus
_AgentLogEmailToAddrEntryStatus_Object = MibTableColumn
agentLogEmailToAddrEntryStatus = _AgentLogEmailToAddrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7, 1, 3),
    _AgentLogEmailToAddrEntryStatus_Type()
)
agentLogEmailToAddrEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogEmailToAddrEntryStatus.setStatus("current")
_AgentLogEmailSubjectTable_Object = MibTable
agentLogEmailSubjectTable = _AgentLogEmailSubjectTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8)
)
if mibBuilder.loadTexts:
    agentLogEmailSubjectTable.setStatus("current")
_AgentLogEmailSubjectEntry_Object = MibTableRow
agentLogEmailSubjectEntry = _AgentLogEmailSubjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8, 1)
)
agentLogEmailSubjectEntry.setIndexNames(
    (0, "DNOS-LOGGING-MIB", "agentLogEmailSubjectMessageType"),
)
if mibBuilder.loadTexts:
    agentLogEmailSubjectEntry.setStatus("current")


class _AgentLogEmailSubjectMessageType_Type(Integer32):
    """Custom type agentLogEmailSubjectMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("non-critical", 2))
    )


_AgentLogEmailSubjectMessageType_Type.__name__ = "Integer32"
_AgentLogEmailSubjectMessageType_Object = MibTableColumn
agentLogEmailSubjectMessageType = _AgentLogEmailSubjectMessageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8, 1, 1),
    _AgentLogEmailSubjectMessageType_Type()
)
agentLogEmailSubjectMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLogEmailSubjectMessageType.setStatus("current")
_AgentLogEmailSubject_Type = DisplayString
_AgentLogEmailSubject_Object = MibTableColumn
agentLogEmailSubject = _AgentLogEmailSubject_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8, 1, 2),
    _AgentLogEmailSubject_Type()
)
agentLogEmailSubject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogEmailSubject.setStatus("current")
_AgentLogEmailSubjectEntryStatus_Type = RowStatus
_AgentLogEmailSubjectEntryStatus_Object = MibTableColumn
agentLogEmailSubjectEntryStatus = _AgentLogEmailSubjectEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8, 1, 3),
    _AgentLogEmailSubjectEntryStatus_Type()
)
agentLogEmailSubjectEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogEmailSubjectEntryStatus.setStatus("current")
_AgentLogEmailMailServerTable_Object = MibTable
agentLogEmailMailServerTable = _AgentLogEmailMailServerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9)
)
if mibBuilder.loadTexts:
    agentLogEmailMailServerTable.setStatus("current")
_AgentLogEmailMailServerEntry_Object = MibTableRow
agentLogEmailMailServerEntry = _AgentLogEmailMailServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1)
)
agentLogEmailMailServerEntry.setIndexNames(
    (0, "DNOS-LOGGING-MIB", "agentLogEmailSmtpAddrType"),
    (0, "DNOS-LOGGING-MIB", "agentLogEmailSmtpAddr"),
)
if mibBuilder.loadTexts:
    agentLogEmailMailServerEntry.setStatus("current")
_AgentLogEmailSmtpAddrType_Type = InetAddressType
_AgentLogEmailSmtpAddrType_Object = MibTableColumn
agentLogEmailSmtpAddrType = _AgentLogEmailSmtpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 1),
    _AgentLogEmailSmtpAddrType_Type()
)
agentLogEmailSmtpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLogEmailSmtpAddrType.setStatus("current")
_AgentLogEmailSmtpAddr_Type = InetAddress
_AgentLogEmailSmtpAddr_Object = MibTableColumn
agentLogEmailSmtpAddr = _AgentLogEmailSmtpAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 2),
    _AgentLogEmailSmtpAddr_Type()
)
agentLogEmailSmtpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLogEmailSmtpAddr.setStatus("current")
_AgentLogEmailSmtpPort_Type = InetPortNumber
_AgentLogEmailSmtpPort_Object = MibTableColumn
agentLogEmailSmtpPort = _AgentLogEmailSmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 3),
    _AgentLogEmailSmtpPort_Type()
)
agentLogEmailSmtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailSmtpPort.setStatus("current")


class _AgentLogEmailSecurity_Type(Integer32):
    """Custom type agentLogEmailSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tlsv1", 2))
    )


_AgentLogEmailSecurity_Type.__name__ = "Integer32"
_AgentLogEmailSecurity_Object = MibTableColumn
agentLogEmailSecurity = _AgentLogEmailSecurity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 4),
    _AgentLogEmailSecurity_Type()
)
agentLogEmailSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailSecurity.setStatus("current")
_AgentLogEmailloginID_Type = DisplayString
_AgentLogEmailloginID_Object = MibTableColumn
agentLogEmailloginID = _AgentLogEmailloginID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 5),
    _AgentLogEmailloginID_Type()
)
agentLogEmailloginID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailloginID.setStatus("current")
_AgentLogEmailPassword_Type = DisplayString
_AgentLogEmailPassword_Object = MibTableColumn
agentLogEmailPassword = _AgentLogEmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 6),
    _AgentLogEmailPassword_Type()
)
agentLogEmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailPassword.setStatus("current")
_AgentLogEmailEntryStatus_Type = RowStatus
_AgentLogEmailEntryStatus_Object = MibTableColumn
agentLogEmailEntryStatus = _AgentLogEmailEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 7),
    _AgentLogEmailEntryStatus_Type()
)
agentLogEmailEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLogEmailEntryStatus.setStatus("current")
_AgentLogWebConfigGroup_ObjectIdentity = ObjectIdentity
agentLogWebConfigGroup = _AgentLogWebConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 7)
)


class _AgentLogWebAdminStatus_Type(Integer32):
    """Custom type agentLogWebAdminStatus based on Integer32"""
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


_AgentLogWebAdminStatus_Type.__name__ = "Integer32"
_AgentLogWebAdminStatus_Object = MibScalar
agentLogWebAdminStatus = _AgentLogWebAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 7, 1),
    _AgentLogWebAdminStatus_Type()
)
agentLogWebAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogWebAdminStatus.setStatus("current")
_AgentLogSnmpConfigGroup_ObjectIdentity = ObjectIdentity
agentLogSnmpConfigGroup = _AgentLogSnmpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 8)
)


class _AgentLogSnmpAdminStatus_Type(Integer32):
    """Custom type agentLogSnmpAdminStatus based on Integer32"""
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


_AgentLogSnmpAdminStatus_Type.__name__ = "Integer32"
_AgentLogSnmpAdminStatus_Object = MibScalar
agentLogSnmpAdminStatus = _AgentLogSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 8, 1),
    _AgentLogSnmpAdminStatus_Type()
)
agentLogSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogSnmpAdminStatus.setStatus("current")
_AgentLogAuditConfigGroup_ObjectIdentity = ObjectIdentity
agentLogAuditConfigGroup = _AgentLogAuditConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 9)
)


class _AgentLogAuditAdminStatus_Type(Integer32):
    """Custom type agentLogAuditAdminStatus based on Integer32"""
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


_AgentLogAuditAdminStatus_Type.__name__ = "Integer32"
_AgentLogAuditAdminStatus_Object = MibScalar
agentLogAuditAdminStatus = _AgentLogAuditAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 9, 1),
    _AgentLogAuditAdminStatus_Type()
)
agentLogAuditAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogAuditAdminStatus.setStatus("current")
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
_AgentLogEmailAlertStatsGroup_ObjectIdentity = ObjectIdentity
agentLogEmailAlertStatsGroup = _AgentLogEmailAlertStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7)
)
_AgentLogEmailStatsemailsSentCount_Type = Counter32
_AgentLogEmailStatsemailsSentCount_Object = MibScalar
agentLogEmailStatsemailsSentCount = _AgentLogEmailStatsemailsSentCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7, 1),
    _AgentLogEmailStatsemailsSentCount_Type()
)
agentLogEmailStatsemailsSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogEmailStatsemailsSentCount.setStatus("current")
_AgentLogEmailStatsemailsFailureCount_Type = Counter32
_AgentLogEmailStatsemailsFailureCount_Object = MibScalar
agentLogEmailStatsemailsFailureCount = _AgentLogEmailStatsemailsFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7, 2),
    _AgentLogEmailStatsemailsFailureCount_Type()
)
agentLogEmailStatsemailsFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogEmailStatsemailsFailureCount.setStatus("current")
_AgentLogEmailStatsTimeSinceLastEmailSent_Type = Unsigned32
_AgentLogEmailStatsTimeSinceLastEmailSent_Object = MibScalar
agentLogEmailStatsTimeSinceLastEmailSent = _AgentLogEmailStatsTimeSinceLastEmailSent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7, 3),
    _AgentLogEmailStatsTimeSinceLastEmailSent_Type()
)
agentLogEmailStatsTimeSinceLastEmailSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogEmailStatsTimeSinceLastEmailSent.setStatus("current")


class _AgentLogEmailStatsClear_Type(Integer32):
    """Custom type agentLogEmailStatsClear based on Integer32"""
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


_AgentLogEmailStatsClear_Type.__name__ = "Integer32"
_AgentLogEmailStatsClear_Object = MibScalar
agentLogEmailStatsClear = _AgentLogEmailStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7, 4),
    _AgentLogEmailStatsClear_Type()
)
agentLogEmailStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogEmailStatsClear.setStatus("current")
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
    (0, "DNOS-LOGGING-MIB", "agentLogInMemoryMsgIndex"),
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
_AgentLogTrapsGroup_ObjectIdentity = ObjectIdentity
agentLogTrapsGroup = _AgentLogTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 5)
)
_AgentLogEmailAlertTrapsGroup_ObjectIdentity = ObjectIdentity
agentLogEmailAlertTrapsGroup = _AgentLogEmailAlertTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 5, 1)
)

# Managed Objects groups


# Notification objects

agentLogEmailSendFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 5, 1, 1)
)
agentLogEmailSendFailed.setObjects(
    ("DNOS-LOGGING-MIB", "agentLogEmailStatsemailsFailureCount")
)
if mibBuilder.loadTexts:
    agentLogEmailSendFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-LOGGING-MIB",
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
       "agentLogSyslogSourceInterface": agentLogSyslogSourceInterface,
       "agentLogCliCommandsConfigGroup": agentLogCliCommandsConfigGroup,
       "agentLogCliCommandsAdminStatus": agentLogCliCommandsAdminStatus,
       "agentLogEmailAlertConfigGroup": agentLogEmailAlertConfigGroup,
       "agentLogEmailAdminStatus": agentLogEmailAdminStatus,
       "agentLogEmailfromAddr": agentLogEmailfromAddr,
       "agentLogEmaillogDuration": agentLogEmaillogDuration,
       "agentLogEmailUrgentSeverity": agentLogEmailUrgentSeverity,
       "agentLogEmailNonUrgentSeverity": agentLogEmailNonUrgentSeverity,
       "agentLogEmailTrapsSeverity": agentLogEmailTrapsSeverity,
       "agentLogEmailToAddrTable": agentLogEmailToAddrTable,
       "agentLogEmailToAddrEntry": agentLogEmailToAddrEntry,
       "agentLogEmailToAddrMessageType": agentLogEmailToAddrMessageType,
       "agentLogEmailToAddr": agentLogEmailToAddr,
       "agentLogEmailToAddrEntryStatus": agentLogEmailToAddrEntryStatus,
       "agentLogEmailSubjectTable": agentLogEmailSubjectTable,
       "agentLogEmailSubjectEntry": agentLogEmailSubjectEntry,
       "agentLogEmailSubjectMessageType": agentLogEmailSubjectMessageType,
       "agentLogEmailSubject": agentLogEmailSubject,
       "agentLogEmailSubjectEntryStatus": agentLogEmailSubjectEntryStatus,
       "agentLogEmailMailServerTable": agentLogEmailMailServerTable,
       "agentLogEmailMailServerEntry": agentLogEmailMailServerEntry,
       "agentLogEmailSmtpAddrType": agentLogEmailSmtpAddrType,
       "agentLogEmailSmtpAddr": agentLogEmailSmtpAddr,
       "agentLogEmailSmtpPort": agentLogEmailSmtpPort,
       "agentLogEmailSecurity": agentLogEmailSecurity,
       "agentLogEmailloginID": agentLogEmailloginID,
       "agentLogEmailPassword": agentLogEmailPassword,
       "agentLogEmailEntryStatus": agentLogEmailEntryStatus,
       "agentLogWebConfigGroup": agentLogWebConfigGroup,
       "agentLogWebAdminStatus": agentLogWebAdminStatus,
       "agentLogSnmpConfigGroup": agentLogSnmpConfigGroup,
       "agentLogSnmpAdminStatus": agentLogSnmpAdminStatus,
       "agentLogAuditConfigGroup": agentLogAuditConfigGroup,
       "agentLogAuditAdminStatus": agentLogAuditAdminStatus,
       "agentLogStatisticsGroup": agentLogStatisticsGroup,
       "agentLogMessagesReceived": agentLogMessagesReceived,
       "agentLogMessagesDropped": agentLogMessagesDropped,
       "agentLogSyslogMessagesRelayed": agentLogSyslogMessagesRelayed,
       "agentLogSyslogMessagesIgnored": agentLogSyslogMessagesIgnored,
       "agentLogMessageReceivedTime": agentLogMessageReceivedTime,
       "agentLogSyslogMessageDeliveredTime": agentLogSyslogMessageDeliveredTime,
       "agentLogEmailAlertStatsGroup": agentLogEmailAlertStatsGroup,
       "agentLogEmailStatsemailsSentCount": agentLogEmailStatsemailsSentCount,
       "agentLogEmailStatsemailsFailureCount": agentLogEmailStatsemailsFailureCount,
       "agentLogEmailStatsTimeSinceLastEmailSent": agentLogEmailStatsTimeSinceLastEmailSent,
       "agentLogEmailStatsClear": agentLogEmailStatsClear,
       "agentLogInMemoryGroup": agentLogInMemoryGroup,
       "agentLogInMemoryLogCount": agentLogInMemoryLogCount,
       "agentLogInMemoryTable": agentLogInMemoryTable,
       "agentLogInMemoryEntry": agentLogInMemoryEntry,
       "agentLogInMemoryMsgIndex": agentLogInMemoryMsgIndex,
       "agentLogInMemoryMsgText": agentLogInMemoryMsgText,
       "agentLogTrapsGroup": agentLogTrapsGroup,
       "agentLogEmailAlertTrapsGroup": agentLogEmailAlertTrapsGroup,
       "agentLogEmailSendFailed": agentLogEmailSendFailed}
)
