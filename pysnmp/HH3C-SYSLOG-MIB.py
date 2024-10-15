# SNMP MIB module (HH3C-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:04 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

(DisplayString,
 RowStatus,
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63)
)
hh3cSyslog.setRevisions(
        ("2010-06-09 10:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MessageLevelType(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("invalid", 9),
          ("notice", 6),
          ("warning", 5))
    )



class TimeStampType(Integer32, TextualConvention):
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
        *(("boot", 3),
          ("date", 2),
          ("dateWithoutYear", 4),
          ("none", 1))
    )



class FacilityType(Integer32, TextualConvention):
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
        *(("clockDaemon", 9),
          ("clockDaemon2", 15),
          ("ftpDaemon", 11),
          ("internallyMessages", 5),
          ("kernel", 0),
          ("linePrinter", 6),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("logAlert", 14),
          ("logAudit", 13),
          ("mailSystem", 2),
          ("networkNews", 7),
          ("ntp", 12),
          ("securityAuthorization", 4),
          ("securityAuthorization2", 10),
          ("systemDaemons", 3),
          ("userLevel", 1),
          ("uucp", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cSyslogObjects_ObjectIdentity = ObjectIdentity
hh3cSyslogObjects = _Hh3cSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1)
)
_Hh3cSyslogObject_ObjectIdentity = ObjectIdentity
hh3cSyslogObject = _Hh3cSyslogObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1)
)
_Hh3cSyslogState_Type = TruthValue
_Hh3cSyslogState_Object = MibScalar
hh3cSyslogState = _Hh3cSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 1),
    _Hh3cSyslogState_Type()
)
hh3cSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogState.setStatus("current")
_Hh3cSyslogMaxLoghost_Type = Integer32
_Hh3cSyslogMaxLoghost_Object = MibScalar
hh3cSyslogMaxLoghost = _Hh3cSyslogMaxLoghost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 2),
    _Hh3cSyslogMaxLoghost_Type()
)
hh3cSyslogMaxLoghost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSyslogMaxLoghost.setStatus("current")
_Hh3cSyslogMaxChannel_Type = Integer32
_Hh3cSyslogMaxChannel_Object = MibScalar
hh3cSyslogMaxChannel = _Hh3cSyslogMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 3),
    _Hh3cSyslogMaxChannel_Type()
)
hh3cSyslogMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSyslogMaxChannel.setStatus("current")
_Hh3cSyslogMaxLogbufferSize_Type = Integer32
_Hh3cSyslogMaxLogbufferSize_Object = MibScalar
hh3cSyslogMaxLogbufferSize = _Hh3cSyslogMaxLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 4),
    _Hh3cSyslogMaxLogbufferSize_Type()
)
hh3cSyslogMaxLogbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSyslogMaxLogbufferSize.setStatus("current")
_Hh3cSyslogMaxTrapbufferSize_Type = Integer32
_Hh3cSyslogMaxTrapbufferSize_Object = MibScalar
hh3cSyslogMaxTrapbufferSize = _Hh3cSyslogMaxTrapbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 5),
    _Hh3cSyslogMaxTrapbufferSize_Type()
)
hh3cSyslogMaxTrapbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSyslogMaxTrapbufferSize.setStatus("current")
_Hh3cSyslogConsole_ObjectIdentity = ObjectIdentity
hh3cSyslogConsole = _Hh3cSyslogConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 2)
)


class _Hh3cSyslogConsoleChannel_Type(Integer32):
    """Custom type hh3cSyslogConsoleChannel based on Integer32"""
    defaultValue = 0


_Hh3cSyslogConsoleChannel_Object = MibScalar
hh3cSyslogConsoleChannel = _Hh3cSyslogConsoleChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 2, 1),
    _Hh3cSyslogConsoleChannel_Type()
)
hh3cSyslogConsoleChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogConsoleChannel.setStatus("current")
_Hh3cSyslogMonitor_ObjectIdentity = ObjectIdentity
hh3cSyslogMonitor = _Hh3cSyslogMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 3)
)


class _Hh3cSyslogMonitorChannel_Type(Integer32):
    """Custom type hh3cSyslogMonitorChannel based on Integer32"""
    defaultValue = 1


_Hh3cSyslogMonitorChannel_Object = MibScalar
hh3cSyslogMonitorChannel = _Hh3cSyslogMonitorChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 3, 1),
    _Hh3cSyslogMonitorChannel_Type()
)
hh3cSyslogMonitorChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogMonitorChannel.setStatus("current")
_Hh3cSyslogSnmp_ObjectIdentity = ObjectIdentity
hh3cSyslogSnmp = _Hh3cSyslogSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 4)
)


class _Hh3cSyslogSnmpChannel_Type(Integer32):
    """Custom type hh3cSyslogSnmpChannel based on Integer32"""
    defaultValue = 5


_Hh3cSyslogSnmpChannel_Object = MibScalar
hh3cSyslogSnmpChannel = _Hh3cSyslogSnmpChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 4, 1),
    _Hh3cSyslogSnmpChannel_Type()
)
hh3cSyslogSnmpChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogSnmpChannel.setStatus("current")
_Hh3cSyslogLogbuffer_ObjectIdentity = ObjectIdentity
hh3cSyslogLogbuffer = _Hh3cSyslogLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5)
)


class _Hh3cSyslogLogbufferChannel_Type(Integer32):
    """Custom type hh3cSyslogLogbufferChannel based on Integer32"""
    defaultValue = 4


_Hh3cSyslogLogbufferChannel_Object = MibScalar
hh3cSyslogLogbufferChannel = _Hh3cSyslogLogbufferChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 1),
    _Hh3cSyslogLogbufferChannel_Type()
)
hh3cSyslogLogbufferChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogLogbufferChannel.setStatus("current")


class _Hh3cSyslogLogbufferSize_Type(Integer32):
    """Custom type hh3cSyslogLogbufferSize based on Integer32"""
    defaultValue = 512


_Hh3cSyslogLogbufferSize_Object = MibScalar
hh3cSyslogLogbufferSize = _Hh3cSyslogLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 2),
    _Hh3cSyslogLogbufferSize_Type()
)
hh3cSyslogLogbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogLogbufferSize.setStatus("current")
_Hh3cSyslogLogbufferTable_Object = MibTable
hh3cSyslogLogbufferTable = _Hh3cSyslogLogbufferTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hh3cSyslogLogbufferTable.setStatus("current")
_Hh3cSyslogLogbufferEntry_Object = MibTableRow
hh3cSyslogLogbufferEntry = _Hh3cSyslogLogbufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1)
)
hh3cSyslogLogbufferEntry.setIndexNames(
    (0, "HH3C-SYSLOG-MIB", "hh3cLogbufferIndex"),
)
if mibBuilder.loadTexts:
    hh3cSyslogLogbufferEntry.setStatus("current")
_Hh3cLogbufferIndex_Type = Integer32
_Hh3cLogbufferIndex_Object = MibTableColumn
hh3cLogbufferIndex = _Hh3cLogbufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1, 1),
    _Hh3cLogbufferIndex_Type()
)
hh3cLogbufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cLogbufferIndex.setStatus("current")
_Hh3cLogbufferCurrentMessages_Type = Unsigned32
_Hh3cLogbufferCurrentMessages_Object = MibTableColumn
hh3cLogbufferCurrentMessages = _Hh3cLogbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1, 2),
    _Hh3cLogbufferCurrentMessages_Type()
)
hh3cLogbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLogbufferCurrentMessages.setStatus("current")
_Hh3cLogbufferOverwrittenMessages_Type = Counter32
_Hh3cLogbufferOverwrittenMessages_Object = MibTableColumn
hh3cLogbufferOverwrittenMessages = _Hh3cLogbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1, 3),
    _Hh3cLogbufferOverwrittenMessages_Type()
)
hh3cLogbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLogbufferOverwrittenMessages.setStatus("current")
_Hh3cLogbufferDroppedMessages_Type = Counter32
_Hh3cLogbufferDroppedMessages_Object = MibTableColumn
hh3cLogbufferDroppedMessages = _Hh3cLogbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1, 4),
    _Hh3cLogbufferDroppedMessages_Type()
)
hh3cLogbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLogbufferDroppedMessages.setStatus("current")
_Hh3cSyslogTrapbuffer_ObjectIdentity = ObjectIdentity
hh3cSyslogTrapbuffer = _Hh3cSyslogTrapbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6)
)


class _Hh3cSyslogTrapbufferChannel_Type(Integer32):
    """Custom type hh3cSyslogTrapbufferChannel based on Integer32"""
    defaultValue = 3


_Hh3cSyslogTrapbufferChannel_Object = MibScalar
hh3cSyslogTrapbufferChannel = _Hh3cSyslogTrapbufferChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 1),
    _Hh3cSyslogTrapbufferChannel_Type()
)
hh3cSyslogTrapbufferChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogTrapbufferChannel.setStatus("current")


class _Hh3cSyslogTrapbufferSize_Type(Integer32):
    """Custom type hh3cSyslogTrapbufferSize based on Integer32"""
    defaultValue = 256


_Hh3cSyslogTrapbufferSize_Object = MibScalar
hh3cSyslogTrapbufferSize = _Hh3cSyslogTrapbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 2),
    _Hh3cSyslogTrapbufferSize_Type()
)
hh3cSyslogTrapbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogTrapbufferSize.setStatus("current")
_Hh3cSyslogTrapbufferTable_Object = MibTable
hh3cSyslogTrapbufferTable = _Hh3cSyslogTrapbufferTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3)
)
if mibBuilder.loadTexts:
    hh3cSyslogTrapbufferTable.setStatus("current")
_Hh3cSyslogTrapbufferEntry_Object = MibTableRow
hh3cSyslogTrapbufferEntry = _Hh3cSyslogTrapbufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1)
)
hh3cSyslogTrapbufferEntry.setIndexNames(
    (0, "HH3C-SYSLOG-MIB", "hh3cTrapbufferIndex"),
)
if mibBuilder.loadTexts:
    hh3cSyslogTrapbufferEntry.setStatus("current")
_Hh3cTrapbufferIndex_Type = Integer32
_Hh3cTrapbufferIndex_Object = MibTableColumn
hh3cTrapbufferIndex = _Hh3cTrapbufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1, 1),
    _Hh3cTrapbufferIndex_Type()
)
hh3cTrapbufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrapbufferIndex.setStatus("current")
_Hh3cTrapbufferCurrentMessages_Type = Unsigned32
_Hh3cTrapbufferCurrentMessages_Object = MibTableColumn
hh3cTrapbufferCurrentMessages = _Hh3cTrapbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1, 2),
    _Hh3cTrapbufferCurrentMessages_Type()
)
hh3cTrapbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTrapbufferCurrentMessages.setStatus("current")
_Hh3cTrapbufferOverwrittenMessages_Type = Counter32
_Hh3cTrapbufferOverwrittenMessages_Object = MibTableColumn
hh3cTrapbufferOverwrittenMessages = _Hh3cTrapbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1, 3),
    _Hh3cTrapbufferOverwrittenMessages_Type()
)
hh3cTrapbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTrapbufferOverwrittenMessages.setStatus("current")
_Hh3cTrapbufferDroppedMessages_Type = Counter32
_Hh3cTrapbufferDroppedMessages_Object = MibTableColumn
hh3cTrapbufferDroppedMessages = _Hh3cTrapbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1, 4),
    _Hh3cTrapbufferDroppedMessages_Type()
)
hh3cTrapbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTrapbufferDroppedMessages.setStatus("current")
_Hh3cSyslogLoghost_ObjectIdentity = ObjectIdentity
hh3cSyslogLoghost = _Hh3cSyslogLoghost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7)
)
_Hh3cSyslogLoghostSourceInterface_Type = Integer32
_Hh3cSyslogLoghostSourceInterface_Object = MibScalar
hh3cSyslogLoghostSourceInterface = _Hh3cSyslogLoghostSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 1),
    _Hh3cSyslogLoghostSourceInterface_Type()
)
hh3cSyslogLoghostSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostSourceInterface.setStatus("current")


class _Hh3cSyslogLoghostTimestampType_Type(TimeStampType):
    """Custom type hh3cSyslogLoghostTimestampType based on TimeStampType"""


_Hh3cSyslogLoghostTimestampType_Object = MibScalar
hh3cSyslogLoghostTimestampType = _Hh3cSyslogLoghostTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 2),
    _Hh3cSyslogLoghostTimestampType_Type()
)
hh3cSyslogLoghostTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostTimestampType.setStatus("current")
_Hh3cSyslogLoghostTable_Object = MibTable
hh3cSyslogLoghostTable = _Hh3cSyslogLoghostTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hh3cSyslogLoghostTable.setStatus("current")
_Hh3cSyslogLoghostEntry_Object = MibTableRow
hh3cSyslogLoghostEntry = _Hh3cSyslogLoghostEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1)
)
hh3cSyslogLoghostEntry.setIndexNames(
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogLoghostIndex"),
)
if mibBuilder.loadTexts:
    hh3cSyslogLoghostEntry.setStatus("current")


class _Hh3cSyslogLoghostIndex_Type(Integer32):
    """Custom type hh3cSyslogLoghostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cSyslogLoghostIndex_Type.__name__ = "Integer32"
_Hh3cSyslogLoghostIndex_Object = MibTableColumn
hh3cSyslogLoghostIndex = _Hh3cSyslogLoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 1),
    _Hh3cSyslogLoghostIndex_Type()
)
hh3cSyslogLoghostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostIndex.setStatus("current")


class _Hh3cSyslogLoghostChannel_Type(Integer32):
    """Custom type hh3cSyslogLoghostChannel based on Integer32"""
    defaultValue = 2


_Hh3cSyslogLoghostChannel_Object = MibTableColumn
hh3cSyslogLoghostChannel = _Hh3cSyslogLoghostChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 2),
    _Hh3cSyslogLoghostChannel_Type()
)
hh3cSyslogLoghostChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostChannel.setStatus("current")


class _Hh3cSyslogLoghostIpaddressType_Type(InetAddressType):
    """Custom type hh3cSyslogLoghostIpaddressType based on InetAddressType"""


_Hh3cSyslogLoghostIpaddressType_Object = MibTableColumn
hh3cSyslogLoghostIpaddressType = _Hh3cSyslogLoghostIpaddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 3),
    _Hh3cSyslogLoghostIpaddressType_Type()
)
hh3cSyslogLoghostIpaddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostIpaddressType.setStatus("current")
_Hh3cSyslogLoghostIpaddress_Type = InetAddress
_Hh3cSyslogLoghostIpaddress_Object = MibTableColumn
hh3cSyslogLoghostIpaddress = _Hh3cSyslogLoghostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 4),
    _Hh3cSyslogLoghostIpaddress_Type()
)
hh3cSyslogLoghostIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostIpaddress.setStatus("current")


class _Hh3cSyslogLoghostFacility_Type(FacilityType):
    """Custom type hh3cSyslogLoghostFacility based on FacilityType"""


_Hh3cSyslogLoghostFacility_Object = MibTableColumn
hh3cSyslogLoghostFacility = _Hh3cSyslogLoghostFacility_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 5),
    _Hh3cSyslogLoghostFacility_Type()
)
hh3cSyslogLoghostFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostFacility.setStatus("current")


class _Hh3cSyslogLoghostLanguage_Type(Integer32):
    """Custom type hh3cSyslogLoghostLanguage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chinese", 1),
          ("english", 2))
    )


_Hh3cSyslogLoghostLanguage_Type.__name__ = "Integer32"
_Hh3cSyslogLoghostLanguage_Object = MibTableColumn
hh3cSyslogLoghostLanguage = _Hh3cSyslogLoghostLanguage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 6),
    _Hh3cSyslogLoghostLanguage_Type()
)
hh3cSyslogLoghostLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostLanguage.setStatus("current")
_Hh3cSyslogLoghostOperateRowStatus_Type = RowStatus
_Hh3cSyslogLoghostOperateRowStatus_Object = MibTableColumn
hh3cSyslogLoghostOperateRowStatus = _Hh3cSyslogLoghostOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 7),
    _Hh3cSyslogLoghostOperateRowStatus_Type()
)
hh3cSyslogLoghostOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostOperateRowStatus.setStatus("current")


class _Hh3cSyslogLoghostIpaddressPort_Type(Integer32):
    """Custom type hh3cSyslogLoghostIpaddressPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cSyslogLoghostIpaddressPort_Type.__name__ = "Integer32"
_Hh3cSyslogLoghostIpaddressPort_Object = MibTableColumn
hh3cSyslogLoghostIpaddressPort = _Hh3cSyslogLoghostIpaddressPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 8),
    _Hh3cSyslogLoghostIpaddressPort_Type()
)
hh3cSyslogLoghostIpaddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostIpaddressPort.setStatus("current")
_Hh3cSyslogLoghostTAddress_Type = TAddress
_Hh3cSyslogLoghostTAddress_Object = MibTableColumn
hh3cSyslogLoghostTAddress = _Hh3cSyslogLoghostTAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 9),
    _Hh3cSyslogLoghostTAddress_Type()
)
hh3cSyslogLoghostTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLoghostTAddress.setStatus("current")
_Hh3cSyslogChannel_ObjectIdentity = ObjectIdentity
hh3cSyslogChannel = _Hh3cSyslogChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8)
)
_Hh3cSyslogChannelTable_Object = MibTable
hh3cSyslogChannelTable = _Hh3cSyslogChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cSyslogChannelTable.setStatus("current")
_Hh3cSyslogChannelEntry_Object = MibTableRow
hh3cSyslogChannelEntry = _Hh3cSyslogChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8, 1, 1)
)
hh3cSyslogChannelEntry.setIndexNames(
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogChannelIndex"),
)
if mibBuilder.loadTexts:
    hh3cSyslogChannelEntry.setStatus("current")
_Hh3cSyslogChannelIndex_Type = Integer32
_Hh3cSyslogChannelIndex_Object = MibTableColumn
hh3cSyslogChannelIndex = _Hh3cSyslogChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8, 1, 1, 1),
    _Hh3cSyslogChannelIndex_Type()
)
hh3cSyslogChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSyslogChannelIndex.setStatus("current")


class _Hh3cSyslogChannelName_Type(DisplayString):
    """Custom type hh3cSyslogChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_Hh3cSyslogChannelName_Type.__name__ = "DisplayString"
_Hh3cSyslogChannelName_Object = MibTableColumn
hh3cSyslogChannelName = _Hh3cSyslogChannelName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8, 1, 1, 2),
    _Hh3cSyslogChannelName_Type()
)
hh3cSyslogChannelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogChannelName.setStatus("current")
_Hh3cSyslogModule_ObjectIdentity = ObjectIdentity
hh3cSyslogModule = _Hh3cSyslogModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9)
)
_Hh3cSyslogModuleTable_Object = MibTable
hh3cSyslogModuleTable = _Hh3cSyslogModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hh3cSyslogModuleTable.setStatus("current")
_Hh3cSyslogModuleEntry_Object = MibTableRow
hh3cSyslogModuleEntry = _Hh3cSyslogModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9, 1, 1)
)
hh3cSyslogModuleEntry.setIndexNames(
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cSyslogModuleEntry.setStatus("current")
_Hh3cSyslogModuleIndex_Type = Integer32
_Hh3cSyslogModuleIndex_Object = MibTableColumn
hh3cSyslogModuleIndex = _Hh3cSyslogModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9, 1, 1, 1),
    _Hh3cSyslogModuleIndex_Type()
)
hh3cSyslogModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSyslogModuleIndex.setStatus("current")


class _Hh3cSyslogModuleName_Type(DisplayString):
    """Custom type hh3cSyslogModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hh3cSyslogModuleName_Type.__name__ = "DisplayString"
_Hh3cSyslogModuleName_Object = MibTableColumn
hh3cSyslogModuleName = _Hh3cSyslogModuleName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9, 1, 1, 2),
    _Hh3cSyslogModuleName_Type()
)
hh3cSyslogModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSyslogModuleName.setStatus("current")
_Hh3cSyslogLog_ObjectIdentity = ObjectIdentity
hh3cSyslogLog = _Hh3cSyslogLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10)
)


class _Hh3cSyslogLogTimestampType_Type(TimeStampType):
    """Custom type hh3cSyslogLogTimestampType based on TimeStampType"""


_Hh3cSyslogLogTimestampType_Object = MibScalar
hh3cSyslogLogTimestampType = _Hh3cSyslogLogTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 1),
    _Hh3cSyslogLogTimestampType_Type()
)
hh3cSyslogLogTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogLogTimestampType.setStatus("current")
_Hh3cSyslogLogTable_Object = MibTable
hh3cSyslogLogTable = _Hh3cSyslogLogTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2)
)
if mibBuilder.loadTexts:
    hh3cSyslogLogTable.setStatus("current")
_Hh3cSyslogLogEntry_Object = MibTableRow
hh3cSyslogLogEntry = _Hh3cSyslogLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2, 1)
)
hh3cSyslogLogEntry.setIndexNames(
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogChannelIndex"),
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cSyslogLogEntry.setStatus("current")
_Hh3cSyslogLogState_Type = TruthValue
_Hh3cSyslogLogState_Object = MibTableColumn
hh3cSyslogLogState = _Hh3cSyslogLogState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2, 1, 1),
    _Hh3cSyslogLogState_Type()
)
hh3cSyslogLogState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLogState.setStatus("current")
_Hh3cSyslogLogLevel_Type = MessageLevelType
_Hh3cSyslogLogLevel_Object = MibTableColumn
hh3cSyslogLogLevel = _Hh3cSyslogLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2, 1, 2),
    _Hh3cSyslogLogLevel_Type()
)
hh3cSyslogLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLogLevel.setStatus("current")
_Hh3cSyslogLogRowStatus_Type = RowStatus
_Hh3cSyslogLogRowStatus_Object = MibTableColumn
hh3cSyslogLogRowStatus = _Hh3cSyslogLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2, 1, 3),
    _Hh3cSyslogLogRowStatus_Type()
)
hh3cSyslogLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogLogRowStatus.setStatus("current")
_Hh3cSyslogLogGlobalLevel_Type = MessageLevelType
_Hh3cSyslogLogGlobalLevel_Object = MibScalar
hh3cSyslogLogGlobalLevel = _Hh3cSyslogLogGlobalLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 3),
    _Hh3cSyslogLogGlobalLevel_Type()
)
hh3cSyslogLogGlobalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogLogGlobalLevel.setStatus("current")
_Hh3cSyslogTrap_ObjectIdentity = ObjectIdentity
hh3cSyslogTrap = _Hh3cSyslogTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11)
)


class _Hh3cSyslogTrapTimestampType_Type(TimeStampType):
    """Custom type hh3cSyslogTrapTimestampType based on TimeStampType"""


_Hh3cSyslogTrapTimestampType_Object = MibScalar
hh3cSyslogTrapTimestampType = _Hh3cSyslogTrapTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 1),
    _Hh3cSyslogTrapTimestampType_Type()
)
hh3cSyslogTrapTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogTrapTimestampType.setStatus("current")
_Hh3cSyslogTrapTable_Object = MibTable
hh3cSyslogTrapTable = _Hh3cSyslogTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2)
)
if mibBuilder.loadTexts:
    hh3cSyslogTrapTable.setStatus("current")
_Hh3cSyslogTrapEntry_Object = MibTableRow
hh3cSyslogTrapEntry = _Hh3cSyslogTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2, 1)
)
hh3cSyslogTrapEntry.setIndexNames(
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogChannelIndex"),
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cSyslogTrapEntry.setStatus("current")
_Hh3cSyslogTrapState_Type = TruthValue
_Hh3cSyslogTrapState_Object = MibTableColumn
hh3cSyslogTrapState = _Hh3cSyslogTrapState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2, 1, 1),
    _Hh3cSyslogTrapState_Type()
)
hh3cSyslogTrapState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogTrapState.setStatus("current")
_Hh3cSyslogTrapLevel_Type = MessageLevelType
_Hh3cSyslogTrapLevel_Object = MibTableColumn
hh3cSyslogTrapLevel = _Hh3cSyslogTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2, 1, 2),
    _Hh3cSyslogTrapLevel_Type()
)
hh3cSyslogTrapLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogTrapLevel.setStatus("current")
_Hh3cSyslogTrapRowStatus_Type = RowStatus
_Hh3cSyslogTrapRowStatus_Object = MibTableColumn
hh3cSyslogTrapRowStatus = _Hh3cSyslogTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2, 1, 3),
    _Hh3cSyslogTrapRowStatus_Type()
)
hh3cSyslogTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogTrapRowStatus.setStatus("current")
_Hh3cSyslogDebug_ObjectIdentity = ObjectIdentity
hh3cSyslogDebug = _Hh3cSyslogDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12)
)


class _Hh3cSyslogDebugTimestampType_Type(TimeStampType):
    """Custom type hh3cSyslogDebugTimestampType based on TimeStampType"""


_Hh3cSyslogDebugTimestampType_Object = MibScalar
hh3cSyslogDebugTimestampType = _Hh3cSyslogDebugTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 1),
    _Hh3cSyslogDebugTimestampType_Type()
)
hh3cSyslogDebugTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSyslogDebugTimestampType.setStatus("current")
_Hh3cSyslogDebugTable_Object = MibTable
hh3cSyslogDebugTable = _Hh3cSyslogDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2)
)
if mibBuilder.loadTexts:
    hh3cSyslogDebugTable.setStatus("current")
_Hh3cSyslogDebugEntry_Object = MibTableRow
hh3cSyslogDebugEntry = _Hh3cSyslogDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2, 1)
)
hh3cSyslogDebugEntry.setIndexNames(
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogChannelIndex"),
    (0, "HH3C-SYSLOG-MIB", "hh3cSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cSyslogDebugEntry.setStatus("current")
_Hh3cSyslogDebugState_Type = TruthValue
_Hh3cSyslogDebugState_Object = MibTableColumn
hh3cSyslogDebugState = _Hh3cSyslogDebugState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2, 1, 1),
    _Hh3cSyslogDebugState_Type()
)
hh3cSyslogDebugState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogDebugState.setStatus("current")
_Hh3cSyslogDebugLevel_Type = MessageLevelType
_Hh3cSyslogDebugLevel_Object = MibTableColumn
hh3cSyslogDebugLevel = _Hh3cSyslogDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2, 1, 2),
    _Hh3cSyslogDebugLevel_Type()
)
hh3cSyslogDebugLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogDebugLevel.setStatus("current")
_Hh3cSyslogDebugRowStatus_Type = RowStatus
_Hh3cSyslogDebugRowStatus_Object = MibTableColumn
hh3cSyslogDebugRowStatus = _Hh3cSyslogDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2, 1, 3),
    _Hh3cSyslogDebugRowStatus_Type()
)
hh3cSyslogDebugRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSyslogDebugRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SYSLOG-MIB",
    **{"MessageLevelType": MessageLevelType,
       "TimeStampType": TimeStampType,
       "FacilityType": FacilityType,
       "hh3cSyslog": hh3cSyslog,
       "hh3cSyslogObjects": hh3cSyslogObjects,
       "hh3cSyslogObject": hh3cSyslogObject,
       "hh3cSyslogState": hh3cSyslogState,
       "hh3cSyslogMaxLoghost": hh3cSyslogMaxLoghost,
       "hh3cSyslogMaxChannel": hh3cSyslogMaxChannel,
       "hh3cSyslogMaxLogbufferSize": hh3cSyslogMaxLogbufferSize,
       "hh3cSyslogMaxTrapbufferSize": hh3cSyslogMaxTrapbufferSize,
       "hh3cSyslogConsole": hh3cSyslogConsole,
       "hh3cSyslogConsoleChannel": hh3cSyslogConsoleChannel,
       "hh3cSyslogMonitor": hh3cSyslogMonitor,
       "hh3cSyslogMonitorChannel": hh3cSyslogMonitorChannel,
       "hh3cSyslogSnmp": hh3cSyslogSnmp,
       "hh3cSyslogSnmpChannel": hh3cSyslogSnmpChannel,
       "hh3cSyslogLogbuffer": hh3cSyslogLogbuffer,
       "hh3cSyslogLogbufferChannel": hh3cSyslogLogbufferChannel,
       "hh3cSyslogLogbufferSize": hh3cSyslogLogbufferSize,
       "hh3cSyslogLogbufferTable": hh3cSyslogLogbufferTable,
       "hh3cSyslogLogbufferEntry": hh3cSyslogLogbufferEntry,
       "hh3cLogbufferIndex": hh3cLogbufferIndex,
       "hh3cLogbufferCurrentMessages": hh3cLogbufferCurrentMessages,
       "hh3cLogbufferOverwrittenMessages": hh3cLogbufferOverwrittenMessages,
       "hh3cLogbufferDroppedMessages": hh3cLogbufferDroppedMessages,
       "hh3cSyslogTrapbuffer": hh3cSyslogTrapbuffer,
       "hh3cSyslogTrapbufferChannel": hh3cSyslogTrapbufferChannel,
       "hh3cSyslogTrapbufferSize": hh3cSyslogTrapbufferSize,
       "hh3cSyslogTrapbufferTable": hh3cSyslogTrapbufferTable,
       "hh3cSyslogTrapbufferEntry": hh3cSyslogTrapbufferEntry,
       "hh3cTrapbufferIndex": hh3cTrapbufferIndex,
       "hh3cTrapbufferCurrentMessages": hh3cTrapbufferCurrentMessages,
       "hh3cTrapbufferOverwrittenMessages": hh3cTrapbufferOverwrittenMessages,
       "hh3cTrapbufferDroppedMessages": hh3cTrapbufferDroppedMessages,
       "hh3cSyslogLoghost": hh3cSyslogLoghost,
       "hh3cSyslogLoghostSourceInterface": hh3cSyslogLoghostSourceInterface,
       "hh3cSyslogLoghostTimestampType": hh3cSyslogLoghostTimestampType,
       "hh3cSyslogLoghostTable": hh3cSyslogLoghostTable,
       "hh3cSyslogLoghostEntry": hh3cSyslogLoghostEntry,
       "hh3cSyslogLoghostIndex": hh3cSyslogLoghostIndex,
       "hh3cSyslogLoghostChannel": hh3cSyslogLoghostChannel,
       "hh3cSyslogLoghostIpaddressType": hh3cSyslogLoghostIpaddressType,
       "hh3cSyslogLoghostIpaddress": hh3cSyslogLoghostIpaddress,
       "hh3cSyslogLoghostFacility": hh3cSyslogLoghostFacility,
       "hh3cSyslogLoghostLanguage": hh3cSyslogLoghostLanguage,
       "hh3cSyslogLoghostOperateRowStatus": hh3cSyslogLoghostOperateRowStatus,
       "hh3cSyslogLoghostIpaddressPort": hh3cSyslogLoghostIpaddressPort,
       "hh3cSyslogLoghostTAddress": hh3cSyslogLoghostTAddress,
       "hh3cSyslogChannel": hh3cSyslogChannel,
       "hh3cSyslogChannelTable": hh3cSyslogChannelTable,
       "hh3cSyslogChannelEntry": hh3cSyslogChannelEntry,
       "hh3cSyslogChannelIndex": hh3cSyslogChannelIndex,
       "hh3cSyslogChannelName": hh3cSyslogChannelName,
       "hh3cSyslogModule": hh3cSyslogModule,
       "hh3cSyslogModuleTable": hh3cSyslogModuleTable,
       "hh3cSyslogModuleEntry": hh3cSyslogModuleEntry,
       "hh3cSyslogModuleIndex": hh3cSyslogModuleIndex,
       "hh3cSyslogModuleName": hh3cSyslogModuleName,
       "hh3cSyslogLog": hh3cSyslogLog,
       "hh3cSyslogLogTimestampType": hh3cSyslogLogTimestampType,
       "hh3cSyslogLogTable": hh3cSyslogLogTable,
       "hh3cSyslogLogEntry": hh3cSyslogLogEntry,
       "hh3cSyslogLogState": hh3cSyslogLogState,
       "hh3cSyslogLogLevel": hh3cSyslogLogLevel,
       "hh3cSyslogLogRowStatus": hh3cSyslogLogRowStatus,
       "hh3cSyslogLogGlobalLevel": hh3cSyslogLogGlobalLevel,
       "hh3cSyslogTrap": hh3cSyslogTrap,
       "hh3cSyslogTrapTimestampType": hh3cSyslogTrapTimestampType,
       "hh3cSyslogTrapTable": hh3cSyslogTrapTable,
       "hh3cSyslogTrapEntry": hh3cSyslogTrapEntry,
       "hh3cSyslogTrapState": hh3cSyslogTrapState,
       "hh3cSyslogTrapLevel": hh3cSyslogTrapLevel,
       "hh3cSyslogTrapRowStatus": hh3cSyslogTrapRowStatus,
       "hh3cSyslogDebug": hh3cSyslogDebug,
       "hh3cSyslogDebugTimestampType": hh3cSyslogDebugTimestampType,
       "hh3cSyslogDebugTable": hh3cSyslogDebugTable,
       "hh3cSyslogDebugEntry": hh3cSyslogDebugEntry,
       "hh3cSyslogDebugState": hh3cSyslogDebugState,
       "hh3cSyslogDebugLevel": hh3cSyslogDebugLevel,
       "hh3cSyslogDebugRowStatus": hh3cSyslogDebugRowStatus}
)
