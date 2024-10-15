# SNMP MIB module (H3C-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:31 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63)
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
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

_H3cSyslogObjects_ObjectIdentity = ObjectIdentity
h3cSyslogObjects = _H3cSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1)
)
_H3cSyslogObject_ObjectIdentity = ObjectIdentity
h3cSyslogObject = _H3cSyslogObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1)
)
_H3cSyslogState_Type = TruthValue
_H3cSyslogState_Object = MibScalar
h3cSyslogState = _H3cSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 1),
    _H3cSyslogState_Type()
)
h3cSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogState.setStatus("current")
_H3cSyslogMaxLoghost_Type = Integer32
_H3cSyslogMaxLoghost_Object = MibScalar
h3cSyslogMaxLoghost = _H3cSyslogMaxLoghost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 2),
    _H3cSyslogMaxLoghost_Type()
)
h3cSyslogMaxLoghost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSyslogMaxLoghost.setStatus("current")
_H3cSyslogMaxChannel_Type = Integer32
_H3cSyslogMaxChannel_Object = MibScalar
h3cSyslogMaxChannel = _H3cSyslogMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 3),
    _H3cSyslogMaxChannel_Type()
)
h3cSyslogMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSyslogMaxChannel.setStatus("current")
_H3cSyslogMaxLogbufferSize_Type = Integer32
_H3cSyslogMaxLogbufferSize_Object = MibScalar
h3cSyslogMaxLogbufferSize = _H3cSyslogMaxLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 4),
    _H3cSyslogMaxLogbufferSize_Type()
)
h3cSyslogMaxLogbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSyslogMaxLogbufferSize.setStatus("current")
_H3cSyslogMaxTrapbufferSize_Type = Integer32
_H3cSyslogMaxTrapbufferSize_Object = MibScalar
h3cSyslogMaxTrapbufferSize = _H3cSyslogMaxTrapbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 5),
    _H3cSyslogMaxTrapbufferSize_Type()
)
h3cSyslogMaxTrapbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSyslogMaxTrapbufferSize.setStatus("current")
_H3cSyslogConsole_ObjectIdentity = ObjectIdentity
h3cSyslogConsole = _H3cSyslogConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 2)
)


class _H3cSyslogConsoleChannel_Type(Integer32):
    """Custom type h3cSyslogConsoleChannel based on Integer32"""
    defaultValue = 0


_H3cSyslogConsoleChannel_Object = MibScalar
h3cSyslogConsoleChannel = _H3cSyslogConsoleChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 2, 1),
    _H3cSyslogConsoleChannel_Type()
)
h3cSyslogConsoleChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogConsoleChannel.setStatus("current")
_H3cSyslogMonitor_ObjectIdentity = ObjectIdentity
h3cSyslogMonitor = _H3cSyslogMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 3)
)


class _H3cSyslogMonitorChannel_Type(Integer32):
    """Custom type h3cSyslogMonitorChannel based on Integer32"""
    defaultValue = 1


_H3cSyslogMonitorChannel_Object = MibScalar
h3cSyslogMonitorChannel = _H3cSyslogMonitorChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 3, 1),
    _H3cSyslogMonitorChannel_Type()
)
h3cSyslogMonitorChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogMonitorChannel.setStatus("current")
_H3cSyslogSnmp_ObjectIdentity = ObjectIdentity
h3cSyslogSnmp = _H3cSyslogSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 4)
)


class _H3cSyslogSnmpChannel_Type(Integer32):
    """Custom type h3cSyslogSnmpChannel based on Integer32"""
    defaultValue = 5


_H3cSyslogSnmpChannel_Object = MibScalar
h3cSyslogSnmpChannel = _H3cSyslogSnmpChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 4, 1),
    _H3cSyslogSnmpChannel_Type()
)
h3cSyslogSnmpChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogSnmpChannel.setStatus("current")
_H3cSyslogLogbuffer_ObjectIdentity = ObjectIdentity
h3cSyslogLogbuffer = _H3cSyslogLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5)
)


class _H3cSyslogLogbufferChannel_Type(Integer32):
    """Custom type h3cSyslogLogbufferChannel based on Integer32"""
    defaultValue = 4


_H3cSyslogLogbufferChannel_Object = MibScalar
h3cSyslogLogbufferChannel = _H3cSyslogLogbufferChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 1),
    _H3cSyslogLogbufferChannel_Type()
)
h3cSyslogLogbufferChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogLogbufferChannel.setStatus("current")


class _H3cSyslogLogbufferSize_Type(Integer32):
    """Custom type h3cSyslogLogbufferSize based on Integer32"""
    defaultValue = 512


_H3cSyslogLogbufferSize_Object = MibScalar
h3cSyslogLogbufferSize = _H3cSyslogLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 2),
    _H3cSyslogLogbufferSize_Type()
)
h3cSyslogLogbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogLogbufferSize.setStatus("current")
_H3cSyslogLogbufferTable_Object = MibTable
h3cSyslogLogbufferTable = _H3cSyslogLogbufferTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3)
)
if mibBuilder.loadTexts:
    h3cSyslogLogbufferTable.setStatus("current")
_H3cSyslogLogbufferEntry_Object = MibTableRow
h3cSyslogLogbufferEntry = _H3cSyslogLogbufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1)
)
h3cSyslogLogbufferEntry.setIndexNames(
    (0, "H3C-SYSLOG-MIB", "h3cLogbufferIndex"),
)
if mibBuilder.loadTexts:
    h3cSyslogLogbufferEntry.setStatus("current")
_H3cLogbufferIndex_Type = Integer32
_H3cLogbufferIndex_Object = MibTableColumn
h3cLogbufferIndex = _H3cLogbufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1, 1),
    _H3cLogbufferIndex_Type()
)
h3cLogbufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLogbufferIndex.setStatus("current")
_H3cLogbufferCurrentMessages_Type = Unsigned32
_H3cLogbufferCurrentMessages_Object = MibTableColumn
h3cLogbufferCurrentMessages = _H3cLogbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1, 2),
    _H3cLogbufferCurrentMessages_Type()
)
h3cLogbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLogbufferCurrentMessages.setStatus("current")
_H3cLogbufferOverwrittenMessages_Type = Counter32
_H3cLogbufferOverwrittenMessages_Object = MibTableColumn
h3cLogbufferOverwrittenMessages = _H3cLogbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1, 3),
    _H3cLogbufferOverwrittenMessages_Type()
)
h3cLogbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLogbufferOverwrittenMessages.setStatus("current")
_H3cLogbufferDroppedMessages_Type = Counter32
_H3cLogbufferDroppedMessages_Object = MibTableColumn
h3cLogbufferDroppedMessages = _H3cLogbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1, 4),
    _H3cLogbufferDroppedMessages_Type()
)
h3cLogbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLogbufferDroppedMessages.setStatus("current")
_H3cSyslogTrapbuffer_ObjectIdentity = ObjectIdentity
h3cSyslogTrapbuffer = _H3cSyslogTrapbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6)
)


class _H3cSyslogTrapbufferChannel_Type(Integer32):
    """Custom type h3cSyslogTrapbufferChannel based on Integer32"""
    defaultValue = 3


_H3cSyslogTrapbufferChannel_Object = MibScalar
h3cSyslogTrapbufferChannel = _H3cSyslogTrapbufferChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 1),
    _H3cSyslogTrapbufferChannel_Type()
)
h3cSyslogTrapbufferChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogTrapbufferChannel.setStatus("current")


class _H3cSyslogTrapbufferSize_Type(Integer32):
    """Custom type h3cSyslogTrapbufferSize based on Integer32"""
    defaultValue = 256


_H3cSyslogTrapbufferSize_Object = MibScalar
h3cSyslogTrapbufferSize = _H3cSyslogTrapbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 2),
    _H3cSyslogTrapbufferSize_Type()
)
h3cSyslogTrapbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogTrapbufferSize.setStatus("current")
_H3cSyslogTrapbufferTable_Object = MibTable
h3cSyslogTrapbufferTable = _H3cSyslogTrapbufferTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3)
)
if mibBuilder.loadTexts:
    h3cSyslogTrapbufferTable.setStatus("current")
_H3cSyslogTrapbufferEntry_Object = MibTableRow
h3cSyslogTrapbufferEntry = _H3cSyslogTrapbufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1)
)
h3cSyslogTrapbufferEntry.setIndexNames(
    (0, "H3C-SYSLOG-MIB", "h3cTrapbufferIndex"),
)
if mibBuilder.loadTexts:
    h3cSyslogTrapbufferEntry.setStatus("current")
_H3cTrapbufferIndex_Type = Integer32
_H3cTrapbufferIndex_Object = MibTableColumn
h3cTrapbufferIndex = _H3cTrapbufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1, 1),
    _H3cTrapbufferIndex_Type()
)
h3cTrapbufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTrapbufferIndex.setStatus("current")
_H3cTrapbufferCurrentMessages_Type = Unsigned32
_H3cTrapbufferCurrentMessages_Object = MibTableColumn
h3cTrapbufferCurrentMessages = _H3cTrapbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1, 2),
    _H3cTrapbufferCurrentMessages_Type()
)
h3cTrapbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTrapbufferCurrentMessages.setStatus("current")
_H3cTrapbufferOverwrittenMessages_Type = Counter32
_H3cTrapbufferOverwrittenMessages_Object = MibTableColumn
h3cTrapbufferOverwrittenMessages = _H3cTrapbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1, 3),
    _H3cTrapbufferOverwrittenMessages_Type()
)
h3cTrapbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTrapbufferOverwrittenMessages.setStatus("current")
_H3cTrapbufferDroppedMessages_Type = Counter32
_H3cTrapbufferDroppedMessages_Object = MibTableColumn
h3cTrapbufferDroppedMessages = _H3cTrapbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1, 4),
    _H3cTrapbufferDroppedMessages_Type()
)
h3cTrapbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTrapbufferDroppedMessages.setStatus("current")
_H3cSyslogLoghost_ObjectIdentity = ObjectIdentity
h3cSyslogLoghost = _H3cSyslogLoghost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7)
)
_H3cSyslogLoghostSourceInterface_Type = Integer32
_H3cSyslogLoghostSourceInterface_Object = MibScalar
h3cSyslogLoghostSourceInterface = _H3cSyslogLoghostSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 1),
    _H3cSyslogLoghostSourceInterface_Type()
)
h3cSyslogLoghostSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogLoghostSourceInterface.setStatus("current")


class _H3cSyslogLoghostTimestampType_Type(TimeStampType):
    """Custom type h3cSyslogLoghostTimestampType based on TimeStampType"""


_H3cSyslogLoghostTimestampType_Object = MibScalar
h3cSyslogLoghostTimestampType = _H3cSyslogLoghostTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 2),
    _H3cSyslogLoghostTimestampType_Type()
)
h3cSyslogLoghostTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogLoghostTimestampType.setStatus("current")
_H3cSyslogLoghostTable_Object = MibTable
h3cSyslogLoghostTable = _H3cSyslogLoghostTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3)
)
if mibBuilder.loadTexts:
    h3cSyslogLoghostTable.setStatus("current")
_H3cSyslogLoghostEntry_Object = MibTableRow
h3cSyslogLoghostEntry = _H3cSyslogLoghostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1)
)
h3cSyslogLoghostEntry.setIndexNames(
    (0, "H3C-SYSLOG-MIB", "h3cSyslogLoghostIndex"),
)
if mibBuilder.loadTexts:
    h3cSyslogLoghostEntry.setStatus("current")


class _H3cSyslogLoghostIndex_Type(Integer32):
    """Custom type h3cSyslogLoghostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cSyslogLoghostIndex_Type.__name__ = "Integer32"
_H3cSyslogLoghostIndex_Object = MibTableColumn
h3cSyslogLoghostIndex = _H3cSyslogLoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 1),
    _H3cSyslogLoghostIndex_Type()
)
h3cSyslogLoghostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSyslogLoghostIndex.setStatus("current")


class _H3cSyslogLoghostChannel_Type(Integer32):
    """Custom type h3cSyslogLoghostChannel based on Integer32"""
    defaultValue = 2


_H3cSyslogLoghostChannel_Object = MibTableColumn
h3cSyslogLoghostChannel = _H3cSyslogLoghostChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 2),
    _H3cSyslogLoghostChannel_Type()
)
h3cSyslogLoghostChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLoghostChannel.setStatus("current")


class _H3cSyslogLoghostIpaddressType_Type(InetAddressType):
    """Custom type h3cSyslogLoghostIpaddressType based on InetAddressType"""


_H3cSyslogLoghostIpaddressType_Object = MibTableColumn
h3cSyslogLoghostIpaddressType = _H3cSyslogLoghostIpaddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 3),
    _H3cSyslogLoghostIpaddressType_Type()
)
h3cSyslogLoghostIpaddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLoghostIpaddressType.setStatus("current")
_H3cSyslogLoghostIpaddress_Type = InetAddress
_H3cSyslogLoghostIpaddress_Object = MibTableColumn
h3cSyslogLoghostIpaddress = _H3cSyslogLoghostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 4),
    _H3cSyslogLoghostIpaddress_Type()
)
h3cSyslogLoghostIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLoghostIpaddress.setStatus("current")


class _H3cSyslogLoghostFacility_Type(FacilityType):
    """Custom type h3cSyslogLoghostFacility based on FacilityType"""


_H3cSyslogLoghostFacility_Object = MibTableColumn
h3cSyslogLoghostFacility = _H3cSyslogLoghostFacility_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 5),
    _H3cSyslogLoghostFacility_Type()
)
h3cSyslogLoghostFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLoghostFacility.setStatus("current")


class _H3cSyslogLoghostLanguage_Type(Integer32):
    """Custom type h3cSyslogLoghostLanguage based on Integer32"""
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


_H3cSyslogLoghostLanguage_Type.__name__ = "Integer32"
_H3cSyslogLoghostLanguage_Object = MibTableColumn
h3cSyslogLoghostLanguage = _H3cSyslogLoghostLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 6),
    _H3cSyslogLoghostLanguage_Type()
)
h3cSyslogLoghostLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLoghostLanguage.setStatus("current")
_H3cSyslogLoghostOperateRowStatus_Type = RowStatus
_H3cSyslogLoghostOperateRowStatus_Object = MibTableColumn
h3cSyslogLoghostOperateRowStatus = _H3cSyslogLoghostOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 7),
    _H3cSyslogLoghostOperateRowStatus_Type()
)
h3cSyslogLoghostOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLoghostOperateRowStatus.setStatus("current")


class _H3cSyslogLoghostIpaddressPort_Type(Integer32):
    """Custom type h3cSyslogLoghostIpaddressPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cSyslogLoghostIpaddressPort_Type.__name__ = "Integer32"
_H3cSyslogLoghostIpaddressPort_Object = MibTableColumn
h3cSyslogLoghostIpaddressPort = _H3cSyslogLoghostIpaddressPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 8),
    _H3cSyslogLoghostIpaddressPort_Type()
)
h3cSyslogLoghostIpaddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLoghostIpaddressPort.setStatus("current")
_H3cSyslogChannel_ObjectIdentity = ObjectIdentity
h3cSyslogChannel = _H3cSyslogChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8)
)
_H3cSyslogChannelTable_Object = MibTable
h3cSyslogChannelTable = _H3cSyslogChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8, 1)
)
if mibBuilder.loadTexts:
    h3cSyslogChannelTable.setStatus("current")
_H3cSyslogChannelEntry_Object = MibTableRow
h3cSyslogChannelEntry = _H3cSyslogChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8, 1, 1)
)
h3cSyslogChannelEntry.setIndexNames(
    (0, "H3C-SYSLOG-MIB", "h3cSyslogChannelIndex"),
)
if mibBuilder.loadTexts:
    h3cSyslogChannelEntry.setStatus("current")
_H3cSyslogChannelIndex_Type = Integer32
_H3cSyslogChannelIndex_Object = MibTableColumn
h3cSyslogChannelIndex = _H3cSyslogChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8, 1, 1, 1),
    _H3cSyslogChannelIndex_Type()
)
h3cSyslogChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSyslogChannelIndex.setStatus("current")


class _H3cSyslogChannelName_Type(DisplayString):
    """Custom type h3cSyslogChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_H3cSyslogChannelName_Type.__name__ = "DisplayString"
_H3cSyslogChannelName_Object = MibTableColumn
h3cSyslogChannelName = _H3cSyslogChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8, 1, 1, 2),
    _H3cSyslogChannelName_Type()
)
h3cSyslogChannelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogChannelName.setStatus("current")
_H3cSyslogModule_ObjectIdentity = ObjectIdentity
h3cSyslogModule = _H3cSyslogModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9)
)
_H3cSyslogModuleTable_Object = MibTable
h3cSyslogModuleTable = _H3cSyslogModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9, 1)
)
if mibBuilder.loadTexts:
    h3cSyslogModuleTable.setStatus("current")
_H3cSyslogModuleEntry_Object = MibTableRow
h3cSyslogModuleEntry = _H3cSyslogModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9, 1, 1)
)
h3cSyslogModuleEntry.setIndexNames(
    (0, "H3C-SYSLOG-MIB", "h3cSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    h3cSyslogModuleEntry.setStatus("current")
_H3cSyslogModuleIndex_Type = Integer32
_H3cSyslogModuleIndex_Object = MibTableColumn
h3cSyslogModuleIndex = _H3cSyslogModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9, 1, 1, 1),
    _H3cSyslogModuleIndex_Type()
)
h3cSyslogModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSyslogModuleIndex.setStatus("current")


class _H3cSyslogModuleName_Type(DisplayString):
    """Custom type h3cSyslogModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_H3cSyslogModuleName_Type.__name__ = "DisplayString"
_H3cSyslogModuleName_Object = MibTableColumn
h3cSyslogModuleName = _H3cSyslogModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9, 1, 1, 2),
    _H3cSyslogModuleName_Type()
)
h3cSyslogModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSyslogModuleName.setStatus("current")
_H3cSyslogLog_ObjectIdentity = ObjectIdentity
h3cSyslogLog = _H3cSyslogLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10)
)


class _H3cSyslogLogTimestampType_Type(TimeStampType):
    """Custom type h3cSyslogLogTimestampType based on TimeStampType"""


_H3cSyslogLogTimestampType_Object = MibScalar
h3cSyslogLogTimestampType = _H3cSyslogLogTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 1),
    _H3cSyslogLogTimestampType_Type()
)
h3cSyslogLogTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogLogTimestampType.setStatus("current")
_H3cSyslogLogTable_Object = MibTable
h3cSyslogLogTable = _H3cSyslogLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2)
)
if mibBuilder.loadTexts:
    h3cSyslogLogTable.setStatus("current")
_H3cSyslogLogEntry_Object = MibTableRow
h3cSyslogLogEntry = _H3cSyslogLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2, 1)
)
h3cSyslogLogEntry.setIndexNames(
    (0, "H3C-SYSLOG-MIB", "h3cSyslogChannelIndex"),
    (0, "H3C-SYSLOG-MIB", "h3cSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    h3cSyslogLogEntry.setStatus("current")
_H3cSyslogLogState_Type = TruthValue
_H3cSyslogLogState_Object = MibTableColumn
h3cSyslogLogState = _H3cSyslogLogState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2, 1, 1),
    _H3cSyslogLogState_Type()
)
h3cSyslogLogState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLogState.setStatus("current")
_H3cSyslogLogLevel_Type = MessageLevelType
_H3cSyslogLogLevel_Object = MibTableColumn
h3cSyslogLogLevel = _H3cSyslogLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2, 1, 2),
    _H3cSyslogLogLevel_Type()
)
h3cSyslogLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLogLevel.setStatus("current")
_H3cSyslogLogRowStatus_Type = RowStatus
_H3cSyslogLogRowStatus_Object = MibTableColumn
h3cSyslogLogRowStatus = _H3cSyslogLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2, 1, 3),
    _H3cSyslogLogRowStatus_Type()
)
h3cSyslogLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogLogRowStatus.setStatus("current")
_H3cSyslogTrap_ObjectIdentity = ObjectIdentity
h3cSyslogTrap = _H3cSyslogTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11)
)


class _H3cSyslogTrapTimestampType_Type(TimeStampType):
    """Custom type h3cSyslogTrapTimestampType based on TimeStampType"""


_H3cSyslogTrapTimestampType_Object = MibScalar
h3cSyslogTrapTimestampType = _H3cSyslogTrapTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 1),
    _H3cSyslogTrapTimestampType_Type()
)
h3cSyslogTrapTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogTrapTimestampType.setStatus("current")
_H3cSyslogTrapTable_Object = MibTable
h3cSyslogTrapTable = _H3cSyslogTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2)
)
if mibBuilder.loadTexts:
    h3cSyslogTrapTable.setStatus("current")
_H3cSyslogTrapEntry_Object = MibTableRow
h3cSyslogTrapEntry = _H3cSyslogTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2, 1)
)
h3cSyslogTrapEntry.setIndexNames(
    (0, "H3C-SYSLOG-MIB", "h3cSyslogChannelIndex"),
    (0, "H3C-SYSLOG-MIB", "h3cSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    h3cSyslogTrapEntry.setStatus("current")
_H3cSyslogTrapState_Type = TruthValue
_H3cSyslogTrapState_Object = MibTableColumn
h3cSyslogTrapState = _H3cSyslogTrapState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2, 1, 1),
    _H3cSyslogTrapState_Type()
)
h3cSyslogTrapState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogTrapState.setStatus("current")
_H3cSyslogTrapLevel_Type = MessageLevelType
_H3cSyslogTrapLevel_Object = MibTableColumn
h3cSyslogTrapLevel = _H3cSyslogTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2, 1, 2),
    _H3cSyslogTrapLevel_Type()
)
h3cSyslogTrapLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogTrapLevel.setStatus("current")
_H3cSyslogTrapRowStatus_Type = RowStatus
_H3cSyslogTrapRowStatus_Object = MibTableColumn
h3cSyslogTrapRowStatus = _H3cSyslogTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2, 1, 3),
    _H3cSyslogTrapRowStatus_Type()
)
h3cSyslogTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogTrapRowStatus.setStatus("current")
_H3cSyslogDebug_ObjectIdentity = ObjectIdentity
h3cSyslogDebug = _H3cSyslogDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12)
)


class _H3cSyslogDebugTimestampType_Type(TimeStampType):
    """Custom type h3cSyslogDebugTimestampType based on TimeStampType"""


_H3cSyslogDebugTimestampType_Object = MibScalar
h3cSyslogDebugTimestampType = _H3cSyslogDebugTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 1),
    _H3cSyslogDebugTimestampType_Type()
)
h3cSyslogDebugTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSyslogDebugTimestampType.setStatus("current")
_H3cSyslogDebugTable_Object = MibTable
h3cSyslogDebugTable = _H3cSyslogDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2)
)
if mibBuilder.loadTexts:
    h3cSyslogDebugTable.setStatus("current")
_H3cSyslogDebugEntry_Object = MibTableRow
h3cSyslogDebugEntry = _H3cSyslogDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2, 1)
)
h3cSyslogDebugEntry.setIndexNames(
    (0, "H3C-SYSLOG-MIB", "h3cSyslogChannelIndex"),
    (0, "H3C-SYSLOG-MIB", "h3cSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    h3cSyslogDebugEntry.setStatus("current")
_H3cSyslogDebugState_Type = TruthValue
_H3cSyslogDebugState_Object = MibTableColumn
h3cSyslogDebugState = _H3cSyslogDebugState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2, 1, 1),
    _H3cSyslogDebugState_Type()
)
h3cSyslogDebugState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogDebugState.setStatus("current")
_H3cSyslogDebugLevel_Type = MessageLevelType
_H3cSyslogDebugLevel_Object = MibTableColumn
h3cSyslogDebugLevel = _H3cSyslogDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2, 1, 2),
    _H3cSyslogDebugLevel_Type()
)
h3cSyslogDebugLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogDebugLevel.setStatus("current")
_H3cSyslogDebugRowStatus_Type = RowStatus
_H3cSyslogDebugRowStatus_Object = MibTableColumn
h3cSyslogDebugRowStatus = _H3cSyslogDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2, 1, 3),
    _H3cSyslogDebugRowStatus_Type()
)
h3cSyslogDebugRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSyslogDebugRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SYSLOG-MIB",
    **{"MessageLevelType": MessageLevelType,
       "TimeStampType": TimeStampType,
       "FacilityType": FacilityType,
       "h3cSyslog": h3cSyslog,
       "h3cSyslogObjects": h3cSyslogObjects,
       "h3cSyslogObject": h3cSyslogObject,
       "h3cSyslogState": h3cSyslogState,
       "h3cSyslogMaxLoghost": h3cSyslogMaxLoghost,
       "h3cSyslogMaxChannel": h3cSyslogMaxChannel,
       "h3cSyslogMaxLogbufferSize": h3cSyslogMaxLogbufferSize,
       "h3cSyslogMaxTrapbufferSize": h3cSyslogMaxTrapbufferSize,
       "h3cSyslogConsole": h3cSyslogConsole,
       "h3cSyslogConsoleChannel": h3cSyslogConsoleChannel,
       "h3cSyslogMonitor": h3cSyslogMonitor,
       "h3cSyslogMonitorChannel": h3cSyslogMonitorChannel,
       "h3cSyslogSnmp": h3cSyslogSnmp,
       "h3cSyslogSnmpChannel": h3cSyslogSnmpChannel,
       "h3cSyslogLogbuffer": h3cSyslogLogbuffer,
       "h3cSyslogLogbufferChannel": h3cSyslogLogbufferChannel,
       "h3cSyslogLogbufferSize": h3cSyslogLogbufferSize,
       "h3cSyslogLogbufferTable": h3cSyslogLogbufferTable,
       "h3cSyslogLogbufferEntry": h3cSyslogLogbufferEntry,
       "h3cLogbufferIndex": h3cLogbufferIndex,
       "h3cLogbufferCurrentMessages": h3cLogbufferCurrentMessages,
       "h3cLogbufferOverwrittenMessages": h3cLogbufferOverwrittenMessages,
       "h3cLogbufferDroppedMessages": h3cLogbufferDroppedMessages,
       "h3cSyslogTrapbuffer": h3cSyslogTrapbuffer,
       "h3cSyslogTrapbufferChannel": h3cSyslogTrapbufferChannel,
       "h3cSyslogTrapbufferSize": h3cSyslogTrapbufferSize,
       "h3cSyslogTrapbufferTable": h3cSyslogTrapbufferTable,
       "h3cSyslogTrapbufferEntry": h3cSyslogTrapbufferEntry,
       "h3cTrapbufferIndex": h3cTrapbufferIndex,
       "h3cTrapbufferCurrentMessages": h3cTrapbufferCurrentMessages,
       "h3cTrapbufferOverwrittenMessages": h3cTrapbufferOverwrittenMessages,
       "h3cTrapbufferDroppedMessages": h3cTrapbufferDroppedMessages,
       "h3cSyslogLoghost": h3cSyslogLoghost,
       "h3cSyslogLoghostSourceInterface": h3cSyslogLoghostSourceInterface,
       "h3cSyslogLoghostTimestampType": h3cSyslogLoghostTimestampType,
       "h3cSyslogLoghostTable": h3cSyslogLoghostTable,
       "h3cSyslogLoghostEntry": h3cSyslogLoghostEntry,
       "h3cSyslogLoghostIndex": h3cSyslogLoghostIndex,
       "h3cSyslogLoghostChannel": h3cSyslogLoghostChannel,
       "h3cSyslogLoghostIpaddressType": h3cSyslogLoghostIpaddressType,
       "h3cSyslogLoghostIpaddress": h3cSyslogLoghostIpaddress,
       "h3cSyslogLoghostFacility": h3cSyslogLoghostFacility,
       "h3cSyslogLoghostLanguage": h3cSyslogLoghostLanguage,
       "h3cSyslogLoghostOperateRowStatus": h3cSyslogLoghostOperateRowStatus,
       "h3cSyslogLoghostIpaddressPort": h3cSyslogLoghostIpaddressPort,
       "h3cSyslogChannel": h3cSyslogChannel,
       "h3cSyslogChannelTable": h3cSyslogChannelTable,
       "h3cSyslogChannelEntry": h3cSyslogChannelEntry,
       "h3cSyslogChannelIndex": h3cSyslogChannelIndex,
       "h3cSyslogChannelName": h3cSyslogChannelName,
       "h3cSyslogModule": h3cSyslogModule,
       "h3cSyslogModuleTable": h3cSyslogModuleTable,
       "h3cSyslogModuleEntry": h3cSyslogModuleEntry,
       "h3cSyslogModuleIndex": h3cSyslogModuleIndex,
       "h3cSyslogModuleName": h3cSyslogModuleName,
       "h3cSyslogLog": h3cSyslogLog,
       "h3cSyslogLogTimestampType": h3cSyslogLogTimestampType,
       "h3cSyslogLogTable": h3cSyslogLogTable,
       "h3cSyslogLogEntry": h3cSyslogLogEntry,
       "h3cSyslogLogState": h3cSyslogLogState,
       "h3cSyslogLogLevel": h3cSyslogLogLevel,
       "h3cSyslogLogRowStatus": h3cSyslogLogRowStatus,
       "h3cSyslogTrap": h3cSyslogTrap,
       "h3cSyslogTrapTimestampType": h3cSyslogTrapTimestampType,
       "h3cSyslogTrapTable": h3cSyslogTrapTable,
       "h3cSyslogTrapEntry": h3cSyslogTrapEntry,
       "h3cSyslogTrapState": h3cSyslogTrapState,
       "h3cSyslogTrapLevel": h3cSyslogTrapLevel,
       "h3cSyslogTrapRowStatus": h3cSyslogTrapRowStatus,
       "h3cSyslogDebug": h3cSyslogDebug,
       "h3cSyslogDebugTimestampType": h3cSyslogDebugTimestampType,
       "h3cSyslogDebugTable": h3cSyslogDebugTable,
       "h3cSyslogDebugEntry": h3cSyslogDebugEntry,
       "h3cSyslogDebugState": h3cSyslogDebugState,
       "h3cSyslogDebugLevel": h3cSyslogDebugLevel,
       "h3cSyslogDebugRowStatus": h3cSyslogDebugRowStatus}
)
