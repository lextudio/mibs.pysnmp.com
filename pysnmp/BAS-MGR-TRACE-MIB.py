# SNMP MIB module (BAS-MGR-TRACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-MGR-TRACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:27 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basTrace) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basTrace")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

basMgrTraceLog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasMgrTraceLogTable_Object = MibTable
basMgrTraceLogTable = _BasMgrTraceLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2, 1)
)
if mibBuilder.loadTexts:
    basMgrTraceLogTable.setStatus("current")
_BasMgrTraceLogEntry_Object = MibTableRow
basMgrTraceLogEntry = _BasMgrTraceLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2, 1, 1)
)
basMgrTraceLogEntry.setIndexNames(
    (0, "BAS-MGR-TRACE-MIB", "basMgrTraceLogChassis"),
    (0, "BAS-MGR-TRACE-MIB", "basMgrTraceLogSlot"),
    (0, "BAS-MGR-TRACE-MIB", "basMgrTraceLogIf"),
    (0, "BAS-MGR-TRACE-MIB", "basMgrTraceLogLPort"),
    (0, "BAS-MGR-TRACE-MIB", "basMgrTraceLogComponentId"),
)
if mibBuilder.loadTexts:
    basMgrTraceLogEntry.setStatus("current")
_BasMgrTraceLogChassis_Type = BasChassisId
_BasMgrTraceLogChassis_Object = MibTableColumn
basMgrTraceLogChassis = _BasMgrTraceLogChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2, 1, 1, 1),
    _BasMgrTraceLogChassis_Type()
)
basMgrTraceLogChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basMgrTraceLogChassis.setStatus("current")
_BasMgrTraceLogSlot_Type = BasSlotId
_BasMgrTraceLogSlot_Object = MibTableColumn
basMgrTraceLogSlot = _BasMgrTraceLogSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2, 1, 1, 2),
    _BasMgrTraceLogSlot_Type()
)
basMgrTraceLogSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basMgrTraceLogSlot.setStatus("current")
_BasMgrTraceLogIf_Type = BasInterfaceId
_BasMgrTraceLogIf_Object = MibTableColumn
basMgrTraceLogIf = _BasMgrTraceLogIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2, 1, 1, 3),
    _BasMgrTraceLogIf_Type()
)
basMgrTraceLogIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basMgrTraceLogIf.setStatus("current")
_BasMgrTraceLogLPort_Type = BasLogicalPortId
_BasMgrTraceLogLPort_Object = MibTableColumn
basMgrTraceLogLPort = _BasMgrTraceLogLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2, 1, 1, 4),
    _BasMgrTraceLogLPort_Type()
)
basMgrTraceLogLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basMgrTraceLogLPort.setStatus("current")


class _BasMgrTraceLogComponentId_Type(Integer32):
    """Custom type basMgrTraceLogComponentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("agentx", 10),
          ("bas-rip-gen", 68),
          ("bas-rip-mem", 69),
          ("bas-rip-route", 67),
          ("bas-rip-rx", 63),
          ("bas-rip-state", 70),
          ("bas-rip-task", 65),
          ("bas-rip-timer", 66),
          ("bas-rip-tx", 64),
          ("ca", 19),
          ("cfgRmiServ", 14),
          ("cfm", 1),
          ("cli", 34),
          ("cmts", 6),
          ("cmts-0", 38),
          ("cmts-1", 39),
          ("cmts-10", 48),
          ("cmts-11", 49),
          ("cmts-12", 50),
          ("cmts-13", 51),
          ("cmts-14", 52),
          ("cmts-15", 53),
          ("cmts-17", 57),
          ("cmts-2", 40),
          ("cmts-3", 41),
          ("cmts-4", 42),
          ("cmts-5", 43),
          ("cmts-6", 44),
          ("cmts-7", 45),
          ("cmts-8", 46),
          ("cmts-9", 47),
          ("cmts-docsis-err", 54),
          ("cmts-generic", 37),
          ("cmtsBpi", 8),
          ("cmtsMac", 7),
          ("crp", 21),
          ("dhcpRelay", 11),
          ("dhcpServ", 30),
          ("faultsRmiServ", 16),
          ("ftd", 22),
          ("icmp", 29),
          ("idle", 55),
          ("ip", 25),
          ("ip-debug", 62),
          ("javaRmiServ", 13),
          ("jni", 18),
          ("la", 3),
          ("last-app", 71),
          ("ldap", 17),
          ("ldp", 5),
          ("log", 35),
          ("ma", 2),
          ("mal", 12),
          ("ospf", 24),
          ("ospf-debug", 61),
          ("provRmiServ", 15),
          ("rbp", 20),
          ("rcv", 56),
          ("rip", 23),
          ("rip-console", 59),
          ("rip-debug", 58),
          ("rm", 4),
          ("routing-trace", 60),
          ("snmp", 9),
          ("sw", 28),
          ("syslogServ", 32),
          ("tcp", 27),
          ("tftpServ", 33),
          ("timeServ", 31),
          ("tracelogd", 36),
          ("udp", 26))
    )


_BasMgrTraceLogComponentId_Type.__name__ = "Integer32"
_BasMgrTraceLogComponentId_Object = MibTableColumn
basMgrTraceLogComponentId = _BasMgrTraceLogComponentId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2, 1, 1, 5),
    _BasMgrTraceLogComponentId_Type()
)
basMgrTraceLogComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basMgrTraceLogComponentId.setStatus("current")


class _BasMgrTraceLogLevel_Type(Integer32):
    """Custom type basMgrTraceLogLevel based on Integer32"""
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
        *(("critical", 2),
          ("info", 4),
          ("init", 1),
          ("warning", 3))
    )


_BasMgrTraceLogLevel_Type.__name__ = "Integer32"
_BasMgrTraceLogLevel_Object = MibTableColumn
basMgrTraceLogLevel = _BasMgrTraceLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 2, 1, 1, 6),
    _BasMgrTraceLogLevel_Type()
)
basMgrTraceLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basMgrTraceLogLevel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-MGR-TRACE-MIB",
    **{"basMgrTraceLog": basMgrTraceLog,
       "basMgrTraceLogTable": basMgrTraceLogTable,
       "basMgrTraceLogEntry": basMgrTraceLogEntry,
       "basMgrTraceLogChassis": basMgrTraceLogChassis,
       "basMgrTraceLogSlot": basMgrTraceLogSlot,
       "basMgrTraceLogIf": basMgrTraceLogIf,
       "basMgrTraceLogLPort": basMgrTraceLogLPort,
       "basMgrTraceLogComponentId": basMgrTraceLogComponentId,
       "basMgrTraceLogLevel": basMgrTraceLogLevel}
)
