# SNMP MIB module (TPLINK-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:45 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24)
)
tplinkSyslogMIB.setRevisions(
        ("2012-11-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MessageLevelType(Integer32, TextualConvention):
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

_TplinkSyslogMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSyslogMIBObjects = _TplinkSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1)
)
_TpSyslogBuffer_ObjectIdentity = ObjectIdentity
tpSyslogBuffer = _TpSyslogBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 1)
)
_TpSyslogBufferSeverity_Type = MessageLevelType
_TpSyslogBufferSeverity_Object = MibScalar
tpSyslogBufferSeverity = _TpSyslogBufferSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 1, 1),
    _TpSyslogBufferSeverity_Type()
)
tpSyslogBufferSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogBufferSeverity.setStatus("current")


class _TpSyslogBufferState_Type(Integer32):
    """Custom type tpSyslogBufferState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSyslogBufferState_Type.__name__ = "Integer32"
_TpSyslogBufferState_Object = MibScalar
tpSyslogBufferState = _TpSyslogBufferState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 1, 2),
    _TpSyslogBufferState_Type()
)
tpSyslogBufferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogBufferState.setStatus("current")
_TpSyslogConsole_ObjectIdentity = ObjectIdentity
tpSyslogConsole = _TpSyslogConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 2)
)
_TpSyslogConsoleSeverity_Type = MessageLevelType
_TpSyslogConsoleSeverity_Object = MibScalar
tpSyslogConsoleSeverity = _TpSyslogConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 2, 1),
    _TpSyslogConsoleSeverity_Type()
)
tpSyslogConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogConsoleSeverity.setStatus("current")


class _TpSyslogConsoleState_Type(Integer32):
    """Custom type tpSyslogConsoleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSyslogConsoleState_Type.__name__ = "Integer32"
_TpSyslogConsoleState_Object = MibScalar
tpSyslogConsoleState = _TpSyslogConsoleState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 2, 2),
    _TpSyslogConsoleState_Type()
)
tpSyslogConsoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogConsoleState.setStatus("current")
_TpSyslogFlash_ObjectIdentity = ObjectIdentity
tpSyslogFlash = _TpSyslogFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 3)
)
_TpSyslogFlashSeverity_Type = MessageLevelType
_TpSyslogFlashSeverity_Object = MibScalar
tpSyslogFlashSeverity = _TpSyslogFlashSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 3, 1),
    _TpSyslogFlashSeverity_Type()
)
tpSyslogFlashSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogFlashSeverity.setStatus("current")


class _TpSyslogFlashState_Type(Integer32):
    """Custom type tpSyslogFlashState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSyslogFlashState_Type.__name__ = "Integer32"
_TpSyslogFlashState_Object = MibScalar
tpSyslogFlashState = _TpSyslogFlashState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 3, 2),
    _TpSyslogFlashState_Type()
)
tpSyslogFlashState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogFlashState.setStatus("current")


class _TpSyslogFlashSyncFrequency_Type(Integer32):
    """Custom type tpSyslogFlashSyncFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_TpSyslogFlashSyncFrequency_Type.__name__ = "Integer32"
_TpSyslogFlashSyncFrequency_Object = MibScalar
tpSyslogFlashSyncFrequency = _TpSyslogFlashSyncFrequency_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 3, 3),
    _TpSyslogFlashSyncFrequency_Type()
)
tpSyslogFlashSyncFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogFlashSyncFrequency.setStatus("current")
_TpSyslogMonitor_ObjectIdentity = ObjectIdentity
tpSyslogMonitor = _TpSyslogMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 4)
)
_TpSyslogMonitorSeverity_Type = MessageLevelType
_TpSyslogMonitorSeverity_Object = MibScalar
tpSyslogMonitorSeverity = _TpSyslogMonitorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 4, 1),
    _TpSyslogMonitorSeverity_Type()
)
tpSyslogMonitorSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogMonitorSeverity.setStatus("current")


class _TpSyslogMonitorState_Type(Integer32):
    """Custom type tpSyslogMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSyslogMonitorState_Type.__name__ = "Integer32"
_TpSyslogMonitorState_Object = MibScalar
tpSyslogMonitorState = _TpSyslogMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 4, 2),
    _TpSyslogMonitorState_Type()
)
tpSyslogMonitorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogMonitorState.setStatus("current")
_TpSyslogHostTable_Object = MibTable
tpSyslogHostTable = _TpSyslogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 5)
)
if mibBuilder.loadTexts:
    tpSyslogHostTable.setStatus("current")
_TpSyslogHostEntry_Object = MibTableRow
tpSyslogHostEntry = _TpSyslogHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 5, 1)
)
tpSyslogHostEntry.setIndexNames(
    (0, "TPLINK-SYSLOG-MIB", "tpSyslogHostIndex"),
)
if mibBuilder.loadTexts:
    tpSyslogHostEntry.setStatus("current")


class _TpSyslogHostIndex_Type(Integer32):
    """Custom type tpSyslogHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TpSyslogHostIndex_Type.__name__ = "Integer32"
_TpSyslogHostIndex_Object = MibTableColumn
tpSyslogHostIndex = _TpSyslogHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 5, 1, 1),
    _TpSyslogHostIndex_Type()
)
tpSyslogHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSyslogHostIndex.setStatus("current")
_TpSyslogHostIPAddress_Type = IpAddress
_TpSyslogHostIPAddress_Object = MibTableColumn
tpSyslogHostIPAddress = _TpSyslogHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 5, 1, 2),
    _TpSyslogHostIPAddress_Type()
)
tpSyslogHostIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogHostIPAddress.setStatus("current")
_TpSyslogHostSeverity_Type = MessageLevelType
_TpSyslogHostSeverity_Object = MibTableColumn
tpSyslogHostSeverity = _TpSyslogHostSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 5, 1, 3),
    _TpSyslogHostSeverity_Type()
)
tpSyslogHostSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogHostSeverity.setStatus("current")


class _TpSyslogHostState_Type(Integer32):
    """Custom type tpSyslogHostState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSyslogHostState_Type.__name__ = "Integer32"
_TpSyslogHostState_Object = MibTableColumn
tpSyslogHostState = _TpSyslogHostState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 1, 5, 1, 4),
    _TpSyslogHostState_Type()
)
tpSyslogHostState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSyslogHostState.setStatus("current")
_TplinkSyslogNotifications_ObjectIdentity = ObjectIdentity
tplinkSyslogNotifications = _TplinkSyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 24, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SYSLOG-MIB",
    **{"MessageLevelType": MessageLevelType,
       "tplinkSyslogMIB": tplinkSyslogMIB,
       "tplinkSyslogMIBObjects": tplinkSyslogMIBObjects,
       "tpSyslogBuffer": tpSyslogBuffer,
       "tpSyslogBufferSeverity": tpSyslogBufferSeverity,
       "tpSyslogBufferState": tpSyslogBufferState,
       "tpSyslogConsole": tpSyslogConsole,
       "tpSyslogConsoleSeverity": tpSyslogConsoleSeverity,
       "tpSyslogConsoleState": tpSyslogConsoleState,
       "tpSyslogFlash": tpSyslogFlash,
       "tpSyslogFlashSeverity": tpSyslogFlashSeverity,
       "tpSyslogFlashState": tpSyslogFlashState,
       "tpSyslogFlashSyncFrequency": tpSyslogFlashSyncFrequency,
       "tpSyslogMonitor": tpSyslogMonitor,
       "tpSyslogMonitorSeverity": tpSyslogMonitorSeverity,
       "tpSyslogMonitorState": tpSyslogMonitorState,
       "tpSyslogHostTable": tpSyslogHostTable,
       "tpSyslogHostEntry": tpSyslogHostEntry,
       "tpSyslogHostIndex": tpSyslogHostIndex,
       "tpSyslogHostIPAddress": tpSyslogHostIPAddress,
       "tpSyslogHostSeverity": tpSyslogHostSeverity,
       "tpSyslogHostState": tpSyslogHostState,
       "tplinkSyslogNotifications": tplinkSyslogNotifications}
)
