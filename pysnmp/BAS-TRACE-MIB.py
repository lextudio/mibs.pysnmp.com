# SNMP MIB module (BAS-TRACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-TRACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:36 2024
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

basTraceLog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasTraceLogNotifyComponentId_Type = Integer32
_BasTraceLogNotifyComponentId_Object = MibScalar
basTraceLogNotifyComponentId = _BasTraceLogNotifyComponentId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 1),
    _BasTraceLogNotifyComponentId_Type()
)
basTraceLogNotifyComponentId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTraceLogNotifyComponentId.setStatus("current")


class _BasTraceLogNotifyString_Type(OctetString):
    """Custom type basTraceLogNotifyString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_BasTraceLogNotifyString_Type.__name__ = "OctetString"
_BasTraceLogNotifyString_Object = MibScalar
basTraceLogNotifyString = _BasTraceLogNotifyString_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 2),
    _BasTraceLogNotifyString_Type()
)
basTraceLogNotifyString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTraceLogNotifyString.setStatus("current")
_BasTraceLogTable_Object = MibTable
basTraceLogTable = _BasTraceLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 3)
)
if mibBuilder.loadTexts:
    basTraceLogTable.setStatus("current")
_BasTraceLogEntry_Object = MibTableRow
basTraceLogEntry = _BasTraceLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 3, 1)
)
basTraceLogEntry.setIndexNames(
    (0, "BAS-TRACE-MIB", "basTraceLogChassis"),
    (0, "BAS-TRACE-MIB", "basTraceLogSlot"),
    (0, "BAS-TRACE-MIB", "basTraceLogIf"),
    (0, "BAS-TRACE-MIB", "basTraceLogLPort"),
    (0, "BAS-TRACE-MIB", "basTraceLogComponentId"),
)
if mibBuilder.loadTexts:
    basTraceLogEntry.setStatus("current")
_BasTraceLogChassis_Type = BasChassisId
_BasTraceLogChassis_Object = MibTableColumn
basTraceLogChassis = _BasTraceLogChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 3, 1, 1),
    _BasTraceLogChassis_Type()
)
basTraceLogChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTraceLogChassis.setStatus("current")
_BasTraceLogSlot_Type = BasSlotId
_BasTraceLogSlot_Object = MibTableColumn
basTraceLogSlot = _BasTraceLogSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 3, 1, 2),
    _BasTraceLogSlot_Type()
)
basTraceLogSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTraceLogSlot.setStatus("current")
_BasTraceLogIf_Type = BasInterfaceId
_BasTraceLogIf_Object = MibTableColumn
basTraceLogIf = _BasTraceLogIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 3, 1, 3),
    _BasTraceLogIf_Type()
)
basTraceLogIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTraceLogIf.setStatus("current")
_BasTraceLogLPort_Type = BasLogicalPortId
_BasTraceLogLPort_Object = MibTableColumn
basTraceLogLPort = _BasTraceLogLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 3, 1, 4),
    _BasTraceLogLPort_Type()
)
basTraceLogLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTraceLogLPort.setStatus("current")


class _BasTraceLogComponentId_Type(Integer32):
    """Custom type basTraceLogComponentId based on Integer32"""
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


_BasTraceLogComponentId_Type.__name__ = "Integer32"
_BasTraceLogComponentId_Object = MibTableColumn
basTraceLogComponentId = _BasTraceLogComponentId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 3, 1, 5),
    _BasTraceLogComponentId_Type()
)
basTraceLogComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTraceLogComponentId.setStatus("current")


class _BasTraceLogLevel_Type(Integer32):
    """Custom type basTraceLogLevel based on Integer32"""
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


_BasTraceLogLevel_Type.__name__ = "Integer32"
_BasTraceLogLevel_Object = MibTableColumn
basTraceLogLevel = _BasTraceLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14, 1, 3, 1, 6),
    _BasTraceLogLevel_Type()
)
basTraceLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basTraceLogLevel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-TRACE-MIB",
    **{"basTraceLog": basTraceLog,
       "basTraceLogNotifyComponentId": basTraceLogNotifyComponentId,
       "basTraceLogNotifyString": basTraceLogNotifyString,
       "basTraceLogTable": basTraceLogTable,
       "basTraceLogEntry": basTraceLogEntry,
       "basTraceLogChassis": basTraceLogChassis,
       "basTraceLogSlot": basTraceLogSlot,
       "basTraceLogIf": basTraceLogIf,
       "basTraceLogLPort": basTraceLogLPort,
       "basTraceLogComponentId": basTraceLogComponentId,
       "basTraceLogLevel": basTraceLogLevel}
)
