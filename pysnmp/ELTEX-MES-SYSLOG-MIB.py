# SNMP MIB module (ELTEX-MES-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:02 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(EltCPURateLimiterTrafficType,) = mibBuilder.importSymbols(
    "ELTEX-MES-SWITCH-RATE-LIMITER-MIB",
    "EltCPURateLimiterTrafficType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltSyslogEventsVRRPEventType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eltSyslogEventsVRRPEventNewMaster", 2),
          ("eltSyslogEventsVRRPEventProtocolError", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EltSyslogCPURateLimiterTable_Object = MibTable
eltSyslogCPURateLimiterTable = _EltSyslogCPURateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 1)
)
if mibBuilder.loadTexts:
    eltSyslogCPURateLimiterTable.setStatus("current")
_EltSyslogCPURateLimiterEntry_Object = MibTableRow
eltSyslogCPURateLimiterEntry = _EltSyslogCPURateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 1, 1)
)
eltSyslogCPURateLimiterEntry.setIndexNames(
    (0, "ELTEX-MES-SYSLOG-MIB", "eltSyslogCPURateLimiterIndex"),
)
if mibBuilder.loadTexts:
    eltSyslogCPURateLimiterEntry.setStatus("current")
_EltSyslogCPURateLimiterIndex_Type = EltCPURateLimiterTrafficType
_EltSyslogCPURateLimiterIndex_Object = MibTableColumn
eltSyslogCPURateLimiterIndex = _EltSyslogCPURateLimiterIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 1, 1, 1),
    _EltSyslogCPURateLimiterIndex_Type()
)
eltSyslogCPURateLimiterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSyslogCPURateLimiterIndex.setStatus("current")
_EltSyslogCPURateLimiterEnabled_Type = TruthValue
_EltSyslogCPURateLimiterEnabled_Object = MibTableColumn
eltSyslogCPURateLimiterEnabled = _EltSyslogCPURateLimiterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 1, 1, 2),
    _EltSyslogCPURateLimiterEnabled_Type()
)
eltSyslogCPURateLimiterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSyslogCPURateLimiterEnabled.setStatus("current")
_EltMesSyslogEvents_ObjectIdentity = ObjectIdentity
eltMesSyslogEvents = _EltMesSyslogEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2)
)
_EltSyslogEventsVrrpTable_Object = MibTable
eltSyslogEventsVrrpTable = _EltSyslogEventsVrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2, 1)
)
if mibBuilder.loadTexts:
    eltSyslogEventsVrrpTable.setStatus("current")
_EltSyslogEventsVrrpEntry_Object = MibTableRow
eltSyslogEventsVrrpEntry = _EltSyslogEventsVrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2, 1, 1)
)
eltSyslogEventsVrrpEntry.setIndexNames(
    (0, "ELTEX-MES-SYSLOG-MIB", "eltSyslogEventsVRRPEventIndex"),
)
if mibBuilder.loadTexts:
    eltSyslogEventsVrrpEntry.setStatus("current")
_EltSyslogEventsVRRPEventIndex_Type = EltSyslogEventsVRRPEventType
_EltSyslogEventsVRRPEventIndex_Object = MibTableColumn
eltSyslogEventsVRRPEventIndex = _EltSyslogEventsVRRPEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2, 1, 1, 1),
    _EltSyslogEventsVRRPEventIndex_Type()
)
eltSyslogEventsVRRPEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSyslogEventsVRRPEventIndex.setStatus("current")
_EltSyslogEventsVRRPEventEnabled_Type = TruthValue
_EltSyslogEventsVRRPEventEnabled_Object = MibTableColumn
eltSyslogEventsVRRPEventEnabled = _EltSyslogEventsVRRPEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 2, 1, 1, 2),
    _EltSyslogEventsVRRPEventEnabled_Type()
)
eltSyslogEventsVRRPEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSyslogEventsVRRPEventEnabled.setStatus("current")


class _EltSyslogUserCmdEnable_Type(TruthValue):
    """Custom type eltSyslogUserCmdEnable based on TruthValue"""


_EltSyslogUserCmdEnable_Object = MibScalar
eltSyslogUserCmdEnable = _EltSyslogUserCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 10, 3),
    _EltSyslogUserCmdEnable_Type()
)
eltSyslogUserCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSyslogUserCmdEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-SYSLOG-MIB",
    **{"EltSyslogEventsVRRPEventType": EltSyslogEventsVRRPEventType,
       "eltMesSyslog": eltMesSyslog,
       "eltSyslogCPURateLimiterTable": eltSyslogCPURateLimiterTable,
       "eltSyslogCPURateLimiterEntry": eltSyslogCPURateLimiterEntry,
       "eltSyslogCPURateLimiterIndex": eltSyslogCPURateLimiterIndex,
       "eltSyslogCPURateLimiterEnabled": eltSyslogCPURateLimiterEnabled,
       "eltMesSyslogEvents": eltMesSyslogEvents,
       "eltSyslogEventsVrrpTable": eltSyslogEventsVrrpTable,
       "eltSyslogEventsVrrpEntry": eltSyslogEventsVrrpEntry,
       "eltSyslogEventsVRRPEventIndex": eltSyslogEventsVRRPEventIndex,
       "eltSyslogEventsVRRPEventEnabled": eltSyslogEventsVRRPEventEnabled,
       "eltSyslogUserCmdEnable": eltSyslogUserCmdEnable}
)
