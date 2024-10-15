# SNMP MIB module (HPN-ICF-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:58 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63)
)
hpnicfSyslog.setRevisions(
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

_HpnicfSyslogObjects_ObjectIdentity = ObjectIdentity
hpnicfSyslogObjects = _HpnicfSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1)
)
_HpnicfSyslogObject_ObjectIdentity = ObjectIdentity
hpnicfSyslogObject = _HpnicfSyslogObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 1)
)
_HpnicfSyslogState_Type = TruthValue
_HpnicfSyslogState_Object = MibScalar
hpnicfSyslogState = _HpnicfSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 1, 1),
    _HpnicfSyslogState_Type()
)
hpnicfSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogState.setStatus("current")
_HpnicfSyslogMaxLoghost_Type = Integer32
_HpnicfSyslogMaxLoghost_Object = MibScalar
hpnicfSyslogMaxLoghost = _HpnicfSyslogMaxLoghost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 1, 2),
    _HpnicfSyslogMaxLoghost_Type()
)
hpnicfSyslogMaxLoghost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSyslogMaxLoghost.setStatus("current")
_HpnicfSyslogMaxChannel_Type = Integer32
_HpnicfSyslogMaxChannel_Object = MibScalar
hpnicfSyslogMaxChannel = _HpnicfSyslogMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 1, 3),
    _HpnicfSyslogMaxChannel_Type()
)
hpnicfSyslogMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSyslogMaxChannel.setStatus("current")
_HpnicfSyslogMaxLogbufferSize_Type = Integer32
_HpnicfSyslogMaxLogbufferSize_Object = MibScalar
hpnicfSyslogMaxLogbufferSize = _HpnicfSyslogMaxLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 1, 4),
    _HpnicfSyslogMaxLogbufferSize_Type()
)
hpnicfSyslogMaxLogbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSyslogMaxLogbufferSize.setStatus("current")
_HpnicfSyslogMaxTrapbufferSize_Type = Integer32
_HpnicfSyslogMaxTrapbufferSize_Object = MibScalar
hpnicfSyslogMaxTrapbufferSize = _HpnicfSyslogMaxTrapbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 1, 5),
    _HpnicfSyslogMaxTrapbufferSize_Type()
)
hpnicfSyslogMaxTrapbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSyslogMaxTrapbufferSize.setStatus("current")


class _HpnicfSyslogState2_Type(Integer32):
    """Custom type hpnicfSyslogState2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HpnicfSyslogState2_Type.__name__ = "Integer32"
_HpnicfSyslogState2_Object = MibScalar
hpnicfSyslogState2 = _HpnicfSyslogState2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 1, 6),
    _HpnicfSyslogState2_Type()
)
hpnicfSyslogState2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogState2.setStatus("current")
_HpnicfSyslogConsole_ObjectIdentity = ObjectIdentity
hpnicfSyslogConsole = _HpnicfSyslogConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 2)
)


class _HpnicfSyslogConsoleChannel_Type(Integer32):
    """Custom type hpnicfSyslogConsoleChannel based on Integer32"""
    defaultValue = 0


_HpnicfSyslogConsoleChannel_Object = MibScalar
hpnicfSyslogConsoleChannel = _HpnicfSyslogConsoleChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 2, 1),
    _HpnicfSyslogConsoleChannel_Type()
)
hpnicfSyslogConsoleChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogConsoleChannel.setStatus("current")
_HpnicfSyslogMonitor_ObjectIdentity = ObjectIdentity
hpnicfSyslogMonitor = _HpnicfSyslogMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 3)
)


class _HpnicfSyslogMonitorChannel_Type(Integer32):
    """Custom type hpnicfSyslogMonitorChannel based on Integer32"""
    defaultValue = 1


_HpnicfSyslogMonitorChannel_Object = MibScalar
hpnicfSyslogMonitorChannel = _HpnicfSyslogMonitorChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 3, 1),
    _HpnicfSyslogMonitorChannel_Type()
)
hpnicfSyslogMonitorChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogMonitorChannel.setStatus("current")
_HpnicfSyslogSnmp_ObjectIdentity = ObjectIdentity
hpnicfSyslogSnmp = _HpnicfSyslogSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 4)
)


class _HpnicfSyslogSnmpChannel_Type(Integer32):
    """Custom type hpnicfSyslogSnmpChannel based on Integer32"""
    defaultValue = 5


_HpnicfSyslogSnmpChannel_Object = MibScalar
hpnicfSyslogSnmpChannel = _HpnicfSyslogSnmpChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 4, 1),
    _HpnicfSyslogSnmpChannel_Type()
)
hpnicfSyslogSnmpChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogSnmpChannel.setStatus("current")
_HpnicfSyslogLogbuffer_ObjectIdentity = ObjectIdentity
hpnicfSyslogLogbuffer = _HpnicfSyslogLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5)
)


class _HpnicfSyslogLogbufferChannel_Type(Integer32):
    """Custom type hpnicfSyslogLogbufferChannel based on Integer32"""
    defaultValue = 4


_HpnicfSyslogLogbufferChannel_Object = MibScalar
hpnicfSyslogLogbufferChannel = _HpnicfSyslogLogbufferChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 1),
    _HpnicfSyslogLogbufferChannel_Type()
)
hpnicfSyslogLogbufferChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogLogbufferChannel.setStatus("current")


class _HpnicfSyslogLogbufferSize_Type(Integer32):
    """Custom type hpnicfSyslogLogbufferSize based on Integer32"""
    defaultValue = 512


_HpnicfSyslogLogbufferSize_Object = MibScalar
hpnicfSyslogLogbufferSize = _HpnicfSyslogLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 2),
    _HpnicfSyslogLogbufferSize_Type()
)
hpnicfSyslogLogbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogLogbufferSize.setStatus("current")
_HpnicfSyslogLogbufferTable_Object = MibTable
hpnicfSyslogLogbufferTable = _HpnicfSyslogLogbufferTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hpnicfSyslogLogbufferTable.setStatus("current")
_HpnicfSyslogLogbufferEntry_Object = MibTableRow
hpnicfSyslogLogbufferEntry = _HpnicfSyslogLogbufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 3, 1)
)
hpnicfSyslogLogbufferEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfLogbufferIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogLogbufferEntry.setStatus("current")
_HpnicfLogbufferIndex_Type = Integer32
_HpnicfLogbufferIndex_Object = MibTableColumn
hpnicfLogbufferIndex = _HpnicfLogbufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 3, 1, 1),
    _HpnicfLogbufferIndex_Type()
)
hpnicfLogbufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLogbufferIndex.setStatus("current")
_HpnicfLogbufferCurrentMessages_Type = Unsigned32
_HpnicfLogbufferCurrentMessages_Object = MibTableColumn
hpnicfLogbufferCurrentMessages = _HpnicfLogbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 3, 1, 2),
    _HpnicfLogbufferCurrentMessages_Type()
)
hpnicfLogbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLogbufferCurrentMessages.setStatus("current")
_HpnicfLogbufferOverwrittenMessages_Type = Counter32
_HpnicfLogbufferOverwrittenMessages_Object = MibTableColumn
hpnicfLogbufferOverwrittenMessages = _HpnicfLogbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 3, 1, 3),
    _HpnicfLogbufferOverwrittenMessages_Type()
)
hpnicfLogbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLogbufferOverwrittenMessages.setStatus("current")
_HpnicfLogbufferDroppedMessages_Type = Counter32
_HpnicfLogbufferDroppedMessages_Object = MibTableColumn
hpnicfLogbufferDroppedMessages = _HpnicfLogbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 3, 1, 4),
    _HpnicfLogbufferDroppedMessages_Type()
)
hpnicfLogbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLogbufferDroppedMessages.setStatus("current")
_HpnicfSyslogLogbufContTable_Object = MibTable
hpnicfSyslogLogbufContTable = _HpnicfSyslogLogbufContTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 4)
)
if mibBuilder.loadTexts:
    hpnicfSyslogLogbufContTable.setStatus("current")
_HpnicfSyslogLogbufContEntry_Object = MibTableRow
hpnicfSyslogLogbufContEntry = _HpnicfSyslogLogbufContEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 4, 1)
)
hpnicfSyslogLogbufContEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfLogbufContIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogLogbufContEntry.setStatus("current")


class _HpnicfLogbufContIndex_Type(Integer32):
    """Custom type hpnicfLogbufContIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfLogbufContIndex_Type.__name__ = "Integer32"
_HpnicfLogbufContIndex_Object = MibTableColumn
hpnicfLogbufContIndex = _HpnicfLogbufContIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 4, 1, 1),
    _HpnicfLogbufContIndex_Type()
)
hpnicfLogbufContIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLogbufContIndex.setStatus("current")


class _HpnicfLogbufContDescription_Type(DisplayString):
    """Custom type hpnicfLogbufContDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_HpnicfLogbufContDescription_Type.__name__ = "DisplayString"
_HpnicfLogbufContDescription_Object = MibTableColumn
hpnicfLogbufContDescription = _HpnicfLogbufContDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 5, 4, 1, 2),
    _HpnicfLogbufContDescription_Type()
)
hpnicfLogbufContDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLogbufContDescription.setStatus("current")
_HpnicfSyslogTrapbuffer_ObjectIdentity = ObjectIdentity
hpnicfSyslogTrapbuffer = _HpnicfSyslogTrapbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6)
)


class _HpnicfSyslogTrapbufferChannel_Type(Integer32):
    """Custom type hpnicfSyslogTrapbufferChannel based on Integer32"""
    defaultValue = 3


_HpnicfSyslogTrapbufferChannel_Object = MibScalar
hpnicfSyslogTrapbufferChannel = _HpnicfSyslogTrapbufferChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6, 1),
    _HpnicfSyslogTrapbufferChannel_Type()
)
hpnicfSyslogTrapbufferChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogTrapbufferChannel.setStatus("current")


class _HpnicfSyslogTrapbufferSize_Type(Integer32):
    """Custom type hpnicfSyslogTrapbufferSize based on Integer32"""
    defaultValue = 256


_HpnicfSyslogTrapbufferSize_Object = MibScalar
hpnicfSyslogTrapbufferSize = _HpnicfSyslogTrapbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6, 2),
    _HpnicfSyslogTrapbufferSize_Type()
)
hpnicfSyslogTrapbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogTrapbufferSize.setStatus("current")
_HpnicfSyslogTrapbufferTable_Object = MibTable
hpnicfSyslogTrapbufferTable = _HpnicfSyslogTrapbufferTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6, 3)
)
if mibBuilder.loadTexts:
    hpnicfSyslogTrapbufferTable.setStatus("current")
_HpnicfSyslogTrapbufferEntry_Object = MibTableRow
hpnicfSyslogTrapbufferEntry = _HpnicfSyslogTrapbufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6, 3, 1)
)
hpnicfSyslogTrapbufferEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfTrapbufferIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogTrapbufferEntry.setStatus("current")
_HpnicfTrapbufferIndex_Type = Integer32
_HpnicfTrapbufferIndex_Object = MibTableColumn
hpnicfTrapbufferIndex = _HpnicfTrapbufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6, 3, 1, 1),
    _HpnicfTrapbufferIndex_Type()
)
hpnicfTrapbufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrapbufferIndex.setStatus("current")
_HpnicfTrapbufferCurrentMessages_Type = Unsigned32
_HpnicfTrapbufferCurrentMessages_Object = MibTableColumn
hpnicfTrapbufferCurrentMessages = _HpnicfTrapbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6, 3, 1, 2),
    _HpnicfTrapbufferCurrentMessages_Type()
)
hpnicfTrapbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTrapbufferCurrentMessages.setStatus("current")
_HpnicfTrapbufferOverwrittenMessages_Type = Counter32
_HpnicfTrapbufferOverwrittenMessages_Object = MibTableColumn
hpnicfTrapbufferOverwrittenMessages = _HpnicfTrapbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6, 3, 1, 3),
    _HpnicfTrapbufferOverwrittenMessages_Type()
)
hpnicfTrapbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTrapbufferOverwrittenMessages.setStatus("current")
_HpnicfTrapbufferDroppedMessages_Type = Counter32
_HpnicfTrapbufferDroppedMessages_Object = MibTableColumn
hpnicfTrapbufferDroppedMessages = _HpnicfTrapbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 6, 3, 1, 4),
    _HpnicfTrapbufferDroppedMessages_Type()
)
hpnicfTrapbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTrapbufferDroppedMessages.setStatus("current")
_HpnicfSyslogLoghost_ObjectIdentity = ObjectIdentity
hpnicfSyslogLoghost = _HpnicfSyslogLoghost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7)
)
_HpnicfSyslogLoghostSourceInterface_Type = Integer32
_HpnicfSyslogLoghostSourceInterface_Object = MibScalar
hpnicfSyslogLoghostSourceInterface = _HpnicfSyslogLoghostSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 1),
    _HpnicfSyslogLoghostSourceInterface_Type()
)
hpnicfSyslogLoghostSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostSourceInterface.setStatus("current")


class _HpnicfSyslogLoghostTimestampType_Type(TimeStampType):
    """Custom type hpnicfSyslogLoghostTimestampType based on TimeStampType"""


_HpnicfSyslogLoghostTimestampType_Object = MibScalar
hpnicfSyslogLoghostTimestampType = _HpnicfSyslogLoghostTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 2),
    _HpnicfSyslogLoghostTimestampType_Type()
)
hpnicfSyslogLoghostTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostTimestampType.setStatus("current")
_HpnicfSyslogLoghostTable_Object = MibTable
hpnicfSyslogLoghostTable = _HpnicfSyslogLoghostTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostTable.setStatus("current")
_HpnicfSyslogLoghostEntry_Object = MibTableRow
hpnicfSyslogLoghostEntry = _HpnicfSyslogLoghostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1)
)
hpnicfSyslogLoghostEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogLoghostIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostEntry.setStatus("current")


class _HpnicfSyslogLoghostIndex_Type(Integer32):
    """Custom type hpnicfSyslogLoghostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfSyslogLoghostIndex_Type.__name__ = "Integer32"
_HpnicfSyslogLoghostIndex_Object = MibTableColumn
hpnicfSyslogLoghostIndex = _HpnicfSyslogLoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 1),
    _HpnicfSyslogLoghostIndex_Type()
)
hpnicfSyslogLoghostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostIndex.setStatus("current")


class _HpnicfSyslogLoghostChannel_Type(Integer32):
    """Custom type hpnicfSyslogLoghostChannel based on Integer32"""
    defaultValue = 2


_HpnicfSyslogLoghostChannel_Object = MibTableColumn
hpnicfSyslogLoghostChannel = _HpnicfSyslogLoghostChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 2),
    _HpnicfSyslogLoghostChannel_Type()
)
hpnicfSyslogLoghostChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostChannel.setStatus("current")


class _HpnicfSyslogLoghostIpaddressType_Type(InetAddressType):
    """Custom type hpnicfSyslogLoghostIpaddressType based on InetAddressType"""


_HpnicfSyslogLoghostIpaddressType_Object = MibTableColumn
hpnicfSyslogLoghostIpaddressType = _HpnicfSyslogLoghostIpaddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 3),
    _HpnicfSyslogLoghostIpaddressType_Type()
)
hpnicfSyslogLoghostIpaddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostIpaddressType.setStatus("current")
_HpnicfSyslogLoghostIpaddress_Type = InetAddress
_HpnicfSyslogLoghostIpaddress_Object = MibTableColumn
hpnicfSyslogLoghostIpaddress = _HpnicfSyslogLoghostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 4),
    _HpnicfSyslogLoghostIpaddress_Type()
)
hpnicfSyslogLoghostIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostIpaddress.setStatus("current")


class _HpnicfSyslogLoghostFacility_Type(FacilityType):
    """Custom type hpnicfSyslogLoghostFacility based on FacilityType"""


_HpnicfSyslogLoghostFacility_Object = MibTableColumn
hpnicfSyslogLoghostFacility = _HpnicfSyslogLoghostFacility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 5),
    _HpnicfSyslogLoghostFacility_Type()
)
hpnicfSyslogLoghostFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostFacility.setStatus("current")


class _HpnicfSyslogLoghostLanguage_Type(Integer32):
    """Custom type hpnicfSyslogLoghostLanguage based on Integer32"""
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


_HpnicfSyslogLoghostLanguage_Type.__name__ = "Integer32"
_HpnicfSyslogLoghostLanguage_Object = MibTableColumn
hpnicfSyslogLoghostLanguage = _HpnicfSyslogLoghostLanguage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 6),
    _HpnicfSyslogLoghostLanguage_Type()
)
hpnicfSyslogLoghostLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostLanguage.setStatus("current")
_HpnicfSyslogLoghostOperateRowStatus_Type = RowStatus
_HpnicfSyslogLoghostOperateRowStatus_Object = MibTableColumn
hpnicfSyslogLoghostOperateRowStatus = _HpnicfSyslogLoghostOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 7),
    _HpnicfSyslogLoghostOperateRowStatus_Type()
)
hpnicfSyslogLoghostOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostOperateRowStatus.setStatus("current")


class _HpnicfSyslogLoghostIpaddressPort_Type(Integer32):
    """Custom type hpnicfSyslogLoghostIpaddressPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfSyslogLoghostIpaddressPort_Type.__name__ = "Integer32"
_HpnicfSyslogLoghostIpaddressPort_Object = MibTableColumn
hpnicfSyslogLoghostIpaddressPort = _HpnicfSyslogLoghostIpaddressPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 8),
    _HpnicfSyslogLoghostIpaddressPort_Type()
)
hpnicfSyslogLoghostIpaddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostIpaddressPort.setStatus("current")
_HpnicfSyslogLoghostTAddress_Type = TAddress
_HpnicfSyslogLoghostTAddress_Object = MibTableColumn
hpnicfSyslogLoghostTAddress = _HpnicfSyslogLoghostTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 7, 3, 1, 9),
    _HpnicfSyslogLoghostTAddress_Type()
)
hpnicfSyslogLoghostTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLoghostTAddress.setStatus("current")
_HpnicfSyslogChannel_ObjectIdentity = ObjectIdentity
hpnicfSyslogChannel = _HpnicfSyslogChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 8)
)
_HpnicfSyslogChannelTable_Object = MibTable
hpnicfSyslogChannelTable = _HpnicfSyslogChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hpnicfSyslogChannelTable.setStatus("current")
_HpnicfSyslogChannelEntry_Object = MibTableRow
hpnicfSyslogChannelEntry = _HpnicfSyslogChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 8, 1, 1)
)
hpnicfSyslogChannelEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogChannelIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogChannelEntry.setStatus("current")
_HpnicfSyslogChannelIndex_Type = Integer32
_HpnicfSyslogChannelIndex_Object = MibTableColumn
hpnicfSyslogChannelIndex = _HpnicfSyslogChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 8, 1, 1, 1),
    _HpnicfSyslogChannelIndex_Type()
)
hpnicfSyslogChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSyslogChannelIndex.setStatus("current")


class _HpnicfSyslogChannelName_Type(DisplayString):
    """Custom type hpnicfSyslogChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HpnicfSyslogChannelName_Type.__name__ = "DisplayString"
_HpnicfSyslogChannelName_Object = MibTableColumn
hpnicfSyslogChannelName = _HpnicfSyslogChannelName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 8, 1, 1, 2),
    _HpnicfSyslogChannelName_Type()
)
hpnicfSyslogChannelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogChannelName.setStatus("current")
_HpnicfSyslogModule_ObjectIdentity = ObjectIdentity
hpnicfSyslogModule = _HpnicfSyslogModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 9)
)
_HpnicfSyslogModuleTable_Object = MibTable
hpnicfSyslogModuleTable = _HpnicfSyslogModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hpnicfSyslogModuleTable.setStatus("current")
_HpnicfSyslogModuleEntry_Object = MibTableRow
hpnicfSyslogModuleEntry = _HpnicfSyslogModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 9, 1, 1)
)
hpnicfSyslogModuleEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogModuleEntry.setStatus("current")
_HpnicfSyslogModuleIndex_Type = Integer32
_HpnicfSyslogModuleIndex_Object = MibTableColumn
hpnicfSyslogModuleIndex = _HpnicfSyslogModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 9, 1, 1, 1),
    _HpnicfSyslogModuleIndex_Type()
)
hpnicfSyslogModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSyslogModuleIndex.setStatus("current")


class _HpnicfSyslogModuleName_Type(DisplayString):
    """Custom type hpnicfSyslogModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HpnicfSyslogModuleName_Type.__name__ = "DisplayString"
_HpnicfSyslogModuleName_Object = MibTableColumn
hpnicfSyslogModuleName = _HpnicfSyslogModuleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 9, 1, 1, 2),
    _HpnicfSyslogModuleName_Type()
)
hpnicfSyslogModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSyslogModuleName.setStatus("current")
_HpnicfSyslogLog_ObjectIdentity = ObjectIdentity
hpnicfSyslogLog = _HpnicfSyslogLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10)
)


class _HpnicfSyslogLogTimestampType_Type(TimeStampType):
    """Custom type hpnicfSyslogLogTimestampType based on TimeStampType"""


_HpnicfSyslogLogTimestampType_Object = MibScalar
hpnicfSyslogLogTimestampType = _HpnicfSyslogLogTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10, 1),
    _HpnicfSyslogLogTimestampType_Type()
)
hpnicfSyslogLogTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogLogTimestampType.setStatus("current")
_HpnicfSyslogLogTable_Object = MibTable
hpnicfSyslogLogTable = _HpnicfSyslogLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10, 2)
)
if mibBuilder.loadTexts:
    hpnicfSyslogLogTable.setStatus("current")
_HpnicfSyslogLogEntry_Object = MibTableRow
hpnicfSyslogLogEntry = _HpnicfSyslogLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10, 2, 1)
)
hpnicfSyslogLogEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogChannelIndex"),
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogLogEntry.setStatus("current")
_HpnicfSyslogLogState_Type = TruthValue
_HpnicfSyslogLogState_Object = MibTableColumn
hpnicfSyslogLogState = _HpnicfSyslogLogState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10, 2, 1, 1),
    _HpnicfSyslogLogState_Type()
)
hpnicfSyslogLogState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLogState.setStatus("current")
_HpnicfSyslogLogLevel_Type = MessageLevelType
_HpnicfSyslogLogLevel_Object = MibTableColumn
hpnicfSyslogLogLevel = _HpnicfSyslogLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10, 2, 1, 2),
    _HpnicfSyslogLogLevel_Type()
)
hpnicfSyslogLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLogLevel.setStatus("current")
_HpnicfSyslogLogRowStatus_Type = RowStatus
_HpnicfSyslogLogRowStatus_Object = MibTableColumn
hpnicfSyslogLogRowStatus = _HpnicfSyslogLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10, 2, 1, 3),
    _HpnicfSyslogLogRowStatus_Type()
)
hpnicfSyslogLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogLogRowStatus.setStatus("current")
_HpnicfSyslogLogGlobalLevel_Type = MessageLevelType
_HpnicfSyslogLogGlobalLevel_Object = MibScalar
hpnicfSyslogLogGlobalLevel = _HpnicfSyslogLogGlobalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10, 3),
    _HpnicfSyslogLogGlobalLevel_Type()
)
hpnicfSyslogLogGlobalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogLogGlobalLevel.setStatus("obsolete")


class _HpnicfSyslogLogGlobalLevelRfc_Type(Integer32):
    """Custom type hpnicfSyslogLogGlobalLevelRfc based on Integer32"""
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


_HpnicfSyslogLogGlobalLevelRfc_Type.__name__ = "Integer32"
_HpnicfSyslogLogGlobalLevelRfc_Object = MibScalar
hpnicfSyslogLogGlobalLevelRfc = _HpnicfSyslogLogGlobalLevelRfc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 10, 4),
    _HpnicfSyslogLogGlobalLevelRfc_Type()
)
hpnicfSyslogLogGlobalLevelRfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogLogGlobalLevelRfc.setStatus("current")
_HpnicfSyslogTrap_ObjectIdentity = ObjectIdentity
hpnicfSyslogTrap = _HpnicfSyslogTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 11)
)


class _HpnicfSyslogTrapTimestampType_Type(TimeStampType):
    """Custom type hpnicfSyslogTrapTimestampType based on TimeStampType"""


_HpnicfSyslogTrapTimestampType_Object = MibScalar
hpnicfSyslogTrapTimestampType = _HpnicfSyslogTrapTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 11, 1),
    _HpnicfSyslogTrapTimestampType_Type()
)
hpnicfSyslogTrapTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogTrapTimestampType.setStatus("current")
_HpnicfSyslogTrapTable_Object = MibTable
hpnicfSyslogTrapTable = _HpnicfSyslogTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 11, 2)
)
if mibBuilder.loadTexts:
    hpnicfSyslogTrapTable.setStatus("current")
_HpnicfSyslogTrapEntry_Object = MibTableRow
hpnicfSyslogTrapEntry = _HpnicfSyslogTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 11, 2, 1)
)
hpnicfSyslogTrapEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogChannelIndex"),
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogTrapEntry.setStatus("current")
_HpnicfSyslogTrapState_Type = TruthValue
_HpnicfSyslogTrapState_Object = MibTableColumn
hpnicfSyslogTrapState = _HpnicfSyslogTrapState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 11, 2, 1, 1),
    _HpnicfSyslogTrapState_Type()
)
hpnicfSyslogTrapState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogTrapState.setStatus("current")
_HpnicfSyslogTrapLevel_Type = MessageLevelType
_HpnicfSyslogTrapLevel_Object = MibTableColumn
hpnicfSyslogTrapLevel = _HpnicfSyslogTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 11, 2, 1, 2),
    _HpnicfSyslogTrapLevel_Type()
)
hpnicfSyslogTrapLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogTrapLevel.setStatus("current")
_HpnicfSyslogTrapRowStatus_Type = RowStatus
_HpnicfSyslogTrapRowStatus_Object = MibTableColumn
hpnicfSyslogTrapRowStatus = _HpnicfSyslogTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 11, 2, 1, 3),
    _HpnicfSyslogTrapRowStatus_Type()
)
hpnicfSyslogTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogTrapRowStatus.setStatus("current")
_HpnicfSyslogDebug_ObjectIdentity = ObjectIdentity
hpnicfSyslogDebug = _HpnicfSyslogDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 12)
)


class _HpnicfSyslogDebugTimestampType_Type(TimeStampType):
    """Custom type hpnicfSyslogDebugTimestampType based on TimeStampType"""


_HpnicfSyslogDebugTimestampType_Object = MibScalar
hpnicfSyslogDebugTimestampType = _HpnicfSyslogDebugTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 12, 1),
    _HpnicfSyslogDebugTimestampType_Type()
)
hpnicfSyslogDebugTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSyslogDebugTimestampType.setStatus("current")
_HpnicfSyslogDebugTable_Object = MibTable
hpnicfSyslogDebugTable = _HpnicfSyslogDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 12, 2)
)
if mibBuilder.loadTexts:
    hpnicfSyslogDebugTable.setStatus("current")
_HpnicfSyslogDebugEntry_Object = MibTableRow
hpnicfSyslogDebugEntry = _HpnicfSyslogDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 12, 2, 1)
)
hpnicfSyslogDebugEntry.setIndexNames(
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogChannelIndex"),
    (0, "HPN-ICF-SYSLOG-MIB", "hpnicfSyslogModuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSyslogDebugEntry.setStatus("current")
_HpnicfSyslogDebugState_Type = TruthValue
_HpnicfSyslogDebugState_Object = MibTableColumn
hpnicfSyslogDebugState = _HpnicfSyslogDebugState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 12, 2, 1, 1),
    _HpnicfSyslogDebugState_Type()
)
hpnicfSyslogDebugState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogDebugState.setStatus("current")
_HpnicfSyslogDebugLevel_Type = MessageLevelType
_HpnicfSyslogDebugLevel_Object = MibTableColumn
hpnicfSyslogDebugLevel = _HpnicfSyslogDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 12, 2, 1, 2),
    _HpnicfSyslogDebugLevel_Type()
)
hpnicfSyslogDebugLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogDebugLevel.setStatus("current")
_HpnicfSyslogDebugRowStatus_Type = RowStatus
_HpnicfSyslogDebugRowStatus_Object = MibTableColumn
hpnicfSyslogDebugRowStatus = _HpnicfSyslogDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63, 1, 12, 2, 1, 3),
    _HpnicfSyslogDebugRowStatus_Type()
)
hpnicfSyslogDebugRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSyslogDebugRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SYSLOG-MIB",
    **{"MessageLevelType": MessageLevelType,
       "TimeStampType": TimeStampType,
       "FacilityType": FacilityType,
       "hpnicfSyslog": hpnicfSyslog,
       "hpnicfSyslogObjects": hpnicfSyslogObjects,
       "hpnicfSyslogObject": hpnicfSyslogObject,
       "hpnicfSyslogState": hpnicfSyslogState,
       "hpnicfSyslogMaxLoghost": hpnicfSyslogMaxLoghost,
       "hpnicfSyslogMaxChannel": hpnicfSyslogMaxChannel,
       "hpnicfSyslogMaxLogbufferSize": hpnicfSyslogMaxLogbufferSize,
       "hpnicfSyslogMaxTrapbufferSize": hpnicfSyslogMaxTrapbufferSize,
       "hpnicfSyslogState2": hpnicfSyslogState2,
       "hpnicfSyslogConsole": hpnicfSyslogConsole,
       "hpnicfSyslogConsoleChannel": hpnicfSyslogConsoleChannel,
       "hpnicfSyslogMonitor": hpnicfSyslogMonitor,
       "hpnicfSyslogMonitorChannel": hpnicfSyslogMonitorChannel,
       "hpnicfSyslogSnmp": hpnicfSyslogSnmp,
       "hpnicfSyslogSnmpChannel": hpnicfSyslogSnmpChannel,
       "hpnicfSyslogLogbuffer": hpnicfSyslogLogbuffer,
       "hpnicfSyslogLogbufferChannel": hpnicfSyslogLogbufferChannel,
       "hpnicfSyslogLogbufferSize": hpnicfSyslogLogbufferSize,
       "hpnicfSyslogLogbufferTable": hpnicfSyslogLogbufferTable,
       "hpnicfSyslogLogbufferEntry": hpnicfSyslogLogbufferEntry,
       "hpnicfLogbufferIndex": hpnicfLogbufferIndex,
       "hpnicfLogbufferCurrentMessages": hpnicfLogbufferCurrentMessages,
       "hpnicfLogbufferOverwrittenMessages": hpnicfLogbufferOverwrittenMessages,
       "hpnicfLogbufferDroppedMessages": hpnicfLogbufferDroppedMessages,
       "hpnicfSyslogLogbufContTable": hpnicfSyslogLogbufContTable,
       "hpnicfSyslogLogbufContEntry": hpnicfSyslogLogbufContEntry,
       "hpnicfLogbufContIndex": hpnicfLogbufContIndex,
       "hpnicfLogbufContDescription": hpnicfLogbufContDescription,
       "hpnicfSyslogTrapbuffer": hpnicfSyslogTrapbuffer,
       "hpnicfSyslogTrapbufferChannel": hpnicfSyslogTrapbufferChannel,
       "hpnicfSyslogTrapbufferSize": hpnicfSyslogTrapbufferSize,
       "hpnicfSyslogTrapbufferTable": hpnicfSyslogTrapbufferTable,
       "hpnicfSyslogTrapbufferEntry": hpnicfSyslogTrapbufferEntry,
       "hpnicfTrapbufferIndex": hpnicfTrapbufferIndex,
       "hpnicfTrapbufferCurrentMessages": hpnicfTrapbufferCurrentMessages,
       "hpnicfTrapbufferOverwrittenMessages": hpnicfTrapbufferOverwrittenMessages,
       "hpnicfTrapbufferDroppedMessages": hpnicfTrapbufferDroppedMessages,
       "hpnicfSyslogLoghost": hpnicfSyslogLoghost,
       "hpnicfSyslogLoghostSourceInterface": hpnicfSyslogLoghostSourceInterface,
       "hpnicfSyslogLoghostTimestampType": hpnicfSyslogLoghostTimestampType,
       "hpnicfSyslogLoghostTable": hpnicfSyslogLoghostTable,
       "hpnicfSyslogLoghostEntry": hpnicfSyslogLoghostEntry,
       "hpnicfSyslogLoghostIndex": hpnicfSyslogLoghostIndex,
       "hpnicfSyslogLoghostChannel": hpnicfSyslogLoghostChannel,
       "hpnicfSyslogLoghostIpaddressType": hpnicfSyslogLoghostIpaddressType,
       "hpnicfSyslogLoghostIpaddress": hpnicfSyslogLoghostIpaddress,
       "hpnicfSyslogLoghostFacility": hpnicfSyslogLoghostFacility,
       "hpnicfSyslogLoghostLanguage": hpnicfSyslogLoghostLanguage,
       "hpnicfSyslogLoghostOperateRowStatus": hpnicfSyslogLoghostOperateRowStatus,
       "hpnicfSyslogLoghostIpaddressPort": hpnicfSyslogLoghostIpaddressPort,
       "hpnicfSyslogLoghostTAddress": hpnicfSyslogLoghostTAddress,
       "hpnicfSyslogChannel": hpnicfSyslogChannel,
       "hpnicfSyslogChannelTable": hpnicfSyslogChannelTable,
       "hpnicfSyslogChannelEntry": hpnicfSyslogChannelEntry,
       "hpnicfSyslogChannelIndex": hpnicfSyslogChannelIndex,
       "hpnicfSyslogChannelName": hpnicfSyslogChannelName,
       "hpnicfSyslogModule": hpnicfSyslogModule,
       "hpnicfSyslogModuleTable": hpnicfSyslogModuleTable,
       "hpnicfSyslogModuleEntry": hpnicfSyslogModuleEntry,
       "hpnicfSyslogModuleIndex": hpnicfSyslogModuleIndex,
       "hpnicfSyslogModuleName": hpnicfSyslogModuleName,
       "hpnicfSyslogLog": hpnicfSyslogLog,
       "hpnicfSyslogLogTimestampType": hpnicfSyslogLogTimestampType,
       "hpnicfSyslogLogTable": hpnicfSyslogLogTable,
       "hpnicfSyslogLogEntry": hpnicfSyslogLogEntry,
       "hpnicfSyslogLogState": hpnicfSyslogLogState,
       "hpnicfSyslogLogLevel": hpnicfSyslogLogLevel,
       "hpnicfSyslogLogRowStatus": hpnicfSyslogLogRowStatus,
       "hpnicfSyslogLogGlobalLevel": hpnicfSyslogLogGlobalLevel,
       "hpnicfSyslogLogGlobalLevelRfc": hpnicfSyslogLogGlobalLevelRfc,
       "hpnicfSyslogTrap": hpnicfSyslogTrap,
       "hpnicfSyslogTrapTimestampType": hpnicfSyslogTrapTimestampType,
       "hpnicfSyslogTrapTable": hpnicfSyslogTrapTable,
       "hpnicfSyslogTrapEntry": hpnicfSyslogTrapEntry,
       "hpnicfSyslogTrapState": hpnicfSyslogTrapState,
       "hpnicfSyslogTrapLevel": hpnicfSyslogTrapLevel,
       "hpnicfSyslogTrapRowStatus": hpnicfSyslogTrapRowStatus,
       "hpnicfSyslogDebug": hpnicfSyslogDebug,
       "hpnicfSyslogDebugTimestampType": hpnicfSyslogDebugTimestampType,
       "hpnicfSyslogDebugTable": hpnicfSyslogDebugTable,
       "hpnicfSyslogDebugEntry": hpnicfSyslogDebugEntry,
       "hpnicfSyslogDebugState": hpnicfSyslogDebugState,
       "hpnicfSyslogDebugLevel": hpnicfSyslogDebugLevel,
       "hpnicfSyslogDebugRowStatus": hpnicfSyslogDebugRowStatus}
)
