# SNMP MIB module (DLINK-3100-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:24 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

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

rlSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82)
)
rlSyslog.setRevisions(
        ("2006-02-12 00:00",
         "2003-09-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlSyslogSeverity(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notActive", 8),
          ("notice", 5),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RlSyslogPrivate_ObjectIdentity = ObjectIdentity
rlSyslogPrivate = _RlSyslogPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2)
)


class _RlSyslogGlobalEnable_Type(TruthValue):
    """Custom type rlSyslogGlobalEnable based on TruthValue"""


_RlSyslogGlobalEnable_Object = MibScalar
rlSyslogGlobalEnable = _RlSyslogGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 1),
    _RlSyslogGlobalEnable_Type()
)
rlSyslogGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogGlobalEnable.setStatus("current")


class _RlSyslogMinLogToConsoleSeverity_Type(RlSyslogSeverity):
    """Custom type rlSyslogMinLogToConsoleSeverity based on RlSyslogSeverity"""


_RlSyslogMinLogToConsoleSeverity_Object = MibScalar
rlSyslogMinLogToConsoleSeverity = _RlSyslogMinLogToConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 2),
    _RlSyslogMinLogToConsoleSeverity_Type()
)
rlSyslogMinLogToConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogMinLogToConsoleSeverity.setStatus("current")


class _RlSyslogMinLogToFileSeverity_Type(RlSyslogSeverity):
    """Custom type rlSyslogMinLogToFileSeverity based on RlSyslogSeverity"""


_RlSyslogMinLogToFileSeverity_Object = MibScalar
rlSyslogMinLogToFileSeverity = _RlSyslogMinLogToFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 3),
    _RlSyslogMinLogToFileSeverity_Type()
)
rlSyslogMinLogToFileSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogMinLogToFileSeverity.setStatus("current")


class _RlSyslogMinLogToCacheSeverity_Type(RlSyslogSeverity):
    """Custom type rlSyslogMinLogToCacheSeverity based on RlSyslogSeverity"""


_RlSyslogMinLogToCacheSeverity_Object = MibScalar
rlSyslogMinLogToCacheSeverity = _RlSyslogMinLogToCacheSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 4),
    _RlSyslogMinLogToCacheSeverity_Type()
)
rlSyslogMinLogToCacheSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogMinLogToCacheSeverity.setStatus("current")
_RlSyslogClearLogfile_Type = Unsigned32
_RlSyslogClearLogfile_Object = MibScalar
rlSyslogClearLogfile = _RlSyslogClearLogfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 5),
    _RlSyslogClearLogfile_Type()
)
rlSyslogClearLogfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogClearLogfile.setStatus("current")
_RlSyslogClearCache_Type = Unsigned32
_RlSyslogClearCache_Object = MibScalar
rlSyslogClearCache = _RlSyslogClearCache_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 6),
    _RlSyslogClearCache_Type()
)
rlSyslogClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogClearCache.setStatus("current")
_RlSyslogMibVersion_Type = Integer32
_RlSyslogMibVersion_Object = MibScalar
rlSyslogMibVersion = _RlSyslogMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 7),
    _RlSyslogMibVersion_Type()
)
rlSyslogMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogMibVersion.setStatus("current")
_RlSyslogLogTable_Object = MibTable
rlSyslogLogTable = _RlSyslogLogTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8)
)
if mibBuilder.loadTexts:
    rlSyslogLogTable.setStatus("current")
_RlSyslogLogEntry_Object = MibTableRow
rlSyslogLogEntry = _RlSyslogLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1)
)
rlSyslogLogEntry.setIndexNames(
    (0, "DLINK-3100-SYSLOG-MIB", "rlSyslogLogCounter"),
)
if mibBuilder.loadTexts:
    rlSyslogLogEntry.setStatus("current")
_RlSyslogLogCounter_Type = Unsigned32
_RlSyslogLogCounter_Object = MibTableColumn
rlSyslogLogCounter = _RlSyslogLogCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 1),
    _RlSyslogLogCounter_Type()
)
rlSyslogLogCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCounter.setStatus("current")


class _RlSyslogLogDateTime_Type(DisplayString):
    """Custom type rlSyslogLogDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogLogDateTime_Type.__name__ = "DisplayString"
_RlSyslogLogDateTime_Object = MibTableColumn
rlSyslogLogDateTime = _RlSyslogLogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 2),
    _RlSyslogLogDateTime_Type()
)
rlSyslogLogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogDateTime.setStatus("current")


class _RlSyslogLogAppMnemonic_Type(DisplayString):
    """Custom type rlSyslogLogAppMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RlSyslogLogAppMnemonic_Type.__name__ = "DisplayString"
_RlSyslogLogAppMnemonic_Object = MibTableColumn
rlSyslogLogAppMnemonic = _RlSyslogLogAppMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 3),
    _RlSyslogLogAppMnemonic_Type()
)
rlSyslogLogAppMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogAppMnemonic.setStatus("current")
_RlSyslogLogSeverity_Type = RlSyslogSeverity
_RlSyslogLogSeverity_Object = MibTableColumn
rlSyslogLogSeverity = _RlSyslogLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 4),
    _RlSyslogLogSeverity_Type()
)
rlSyslogLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogSeverity.setStatus("current")


class _RlSyslogLogMessageMnemonic_Type(DisplayString):
    """Custom type rlSyslogLogMessageMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogLogMessageMnemonic_Type.__name__ = "DisplayString"
_RlSyslogLogMessageMnemonic_Object = MibTableColumn
rlSyslogLogMessageMnemonic = _RlSyslogLogMessageMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 5),
    _RlSyslogLogMessageMnemonic_Type()
)
rlSyslogLogMessageMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogMessageMnemonic.setStatus("current")


class _RlSyslogLogText1_Type(DisplayString):
    """Custom type rlSyslogLogText1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogLogText1_Type.__name__ = "DisplayString"
_RlSyslogLogText1_Object = MibTableColumn
rlSyslogLogText1 = _RlSyslogLogText1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 6),
    _RlSyslogLogText1_Type()
)
rlSyslogLogText1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogText1.setStatus("current")


class _RlSyslogLogText2_Type(DisplayString):
    """Custom type rlSyslogLogText2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogLogText2_Type.__name__ = "DisplayString"
_RlSyslogLogText2_Object = MibTableColumn
rlSyslogLogText2 = _RlSyslogLogText2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 7),
    _RlSyslogLogText2_Type()
)
rlSyslogLogText2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogText2.setStatus("current")


class _RlSyslogLogText3_Type(DisplayString):
    """Custom type rlSyslogLogText3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogLogText3_Type.__name__ = "DisplayString"
_RlSyslogLogText3_Object = MibTableColumn
rlSyslogLogText3 = _RlSyslogLogText3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 8),
    _RlSyslogLogText3_Type()
)
rlSyslogLogText3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogText3.setStatus("current")


class _RlSyslogLogText4_Type(DisplayString):
    """Custom type rlSyslogLogText4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSyslogLogText4_Type.__name__ = "DisplayString"
_RlSyslogLogText4_Object = MibTableColumn
rlSyslogLogText4 = _RlSyslogLogText4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 8, 1, 9),
    _RlSyslogLogText4_Type()
)
rlSyslogLogText4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogText4.setStatus("current")
_RlSyslogLogCacheTable_Object = MibTable
rlSyslogLogCacheTable = _RlSyslogLogCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9)
)
if mibBuilder.loadTexts:
    rlSyslogLogCacheTable.setStatus("current")
_RlSyslogLogCacheEntry_Object = MibTableRow
rlSyslogLogCacheEntry = _RlSyslogLogCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1)
)
rlSyslogLogCacheEntry.setIndexNames(
    (0, "DLINK-3100-SYSLOG-MIB", "rlSyslogLogCacheCounter"),
)
if mibBuilder.loadTexts:
    rlSyslogLogCacheEntry.setStatus("current")
_RlSyslogLogCacheCounter_Type = Unsigned32
_RlSyslogLogCacheCounter_Object = MibTableColumn
rlSyslogLogCacheCounter = _RlSyslogLogCacheCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 1),
    _RlSyslogLogCacheCounter_Type()
)
rlSyslogLogCacheCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheCounter.setStatus("current")


class _RlSyslogLogCacheDateTime_Type(DisplayString):
    """Custom type rlSyslogLogCacheDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogLogCacheDateTime_Type.__name__ = "DisplayString"
_RlSyslogLogCacheDateTime_Object = MibTableColumn
rlSyslogLogCacheDateTime = _RlSyslogLogCacheDateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 2),
    _RlSyslogLogCacheDateTime_Type()
)
rlSyslogLogCacheDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheDateTime.setStatus("current")


class _RlSyslogLogCacheAppMnemonic_Type(DisplayString):
    """Custom type rlSyslogLogCacheAppMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RlSyslogLogCacheAppMnemonic_Type.__name__ = "DisplayString"
_RlSyslogLogCacheAppMnemonic_Object = MibTableColumn
rlSyslogLogCacheAppMnemonic = _RlSyslogLogCacheAppMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 3),
    _RlSyslogLogCacheAppMnemonic_Type()
)
rlSyslogLogCacheAppMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheAppMnemonic.setStatus("current")
_RlSyslogLogCacheSeverity_Type = RlSyslogSeverity
_RlSyslogLogCacheSeverity_Object = MibTableColumn
rlSyslogLogCacheSeverity = _RlSyslogLogCacheSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 4),
    _RlSyslogLogCacheSeverity_Type()
)
rlSyslogLogCacheSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheSeverity.setStatus("current")


class _RlSyslogLogCacheMessageMnemonic_Type(DisplayString):
    """Custom type rlSyslogLogCacheMessageMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlSyslogLogCacheMessageMnemonic_Type.__name__ = "DisplayString"
_RlSyslogLogCacheMessageMnemonic_Object = MibTableColumn
rlSyslogLogCacheMessageMnemonic = _RlSyslogLogCacheMessageMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 5),
    _RlSyslogLogCacheMessageMnemonic_Type()
)
rlSyslogLogCacheMessageMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheMessageMnemonic.setStatus("current")


class _RlSyslogLogCacheText1_Type(DisplayString):
    """Custom type rlSyslogLogCacheText1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogLogCacheText1_Type.__name__ = "DisplayString"
_RlSyslogLogCacheText1_Object = MibTableColumn
rlSyslogLogCacheText1 = _RlSyslogLogCacheText1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 6),
    _RlSyslogLogCacheText1_Type()
)
rlSyslogLogCacheText1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheText1.setStatus("current")


class _RlSyslogLogCacheText2_Type(DisplayString):
    """Custom type rlSyslogLogCacheText2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogLogCacheText2_Type.__name__ = "DisplayString"
_RlSyslogLogCacheText2_Object = MibTableColumn
rlSyslogLogCacheText2 = _RlSyslogLogCacheText2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 7),
    _RlSyslogLogCacheText2_Type()
)
rlSyslogLogCacheText2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheText2.setStatus("current")


class _RlSyslogLogCacheText3_Type(DisplayString):
    """Custom type rlSyslogLogCacheText3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogLogCacheText3_Type.__name__ = "DisplayString"
_RlSyslogLogCacheText3_Object = MibTableColumn
rlSyslogLogCacheText3 = _RlSyslogLogCacheText3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 8),
    _RlSyslogLogCacheText3_Type()
)
rlSyslogLogCacheText3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheText3.setStatus("current")


class _RlSyslogLogCacheText4_Type(DisplayString):
    """Custom type rlSyslogLogCacheText4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlSyslogLogCacheText4_Type.__name__ = "DisplayString"
_RlSyslogLogCacheText4_Object = MibTableColumn
rlSyslogLogCacheText4 = _RlSyslogLogCacheText4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 9, 1, 9),
    _RlSyslogLogCacheText4_Type()
)
rlSyslogLogCacheText4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogLogCacheText4.setStatus("current")
_RlSyslogConsoleMessagesIgnored_Type = Counter32
_RlSyslogConsoleMessagesIgnored_Object = MibScalar
rlSyslogConsoleMessagesIgnored = _RlSyslogConsoleMessagesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 10),
    _RlSyslogConsoleMessagesIgnored_Type()
)
rlSyslogConsoleMessagesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogConsoleMessagesIgnored.setStatus("current")
_RlSyslogFileMessagesIgnored_Type = Counter32
_RlSyslogFileMessagesIgnored_Object = MibScalar
rlSyslogFileMessagesIgnored = _RlSyslogFileMessagesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 11),
    _RlSyslogFileMessagesIgnored_Type()
)
rlSyslogFileMessagesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogFileMessagesIgnored.setStatus("current")
_RlSyslogFileMessagesLogged_Type = Counter32
_RlSyslogFileMessagesLogged_Object = MibScalar
rlSyslogFileMessagesLogged = _RlSyslogFileMessagesLogged_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 12),
    _RlSyslogFileMessagesLogged_Type()
)
rlSyslogFileMessagesLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogFileMessagesLogged.setStatus("current")
_RlSyslogCacheTotalMessages_Type = Counter32
_RlSyslogCacheTotalMessages_Object = MibScalar
rlSyslogCacheTotalMessages = _RlSyslogCacheTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 13),
    _RlSyslogCacheTotalMessages_Type()
)
rlSyslogCacheTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSyslogCacheTotalMessages.setStatus("current")
_RlSyslogAggregationEnable_Type = TruthValue
_RlSyslogAggregationEnable_Object = MibScalar
rlSyslogAggregationEnable = _RlSyslogAggregationEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 14),
    _RlSyslogAggregationEnable_Type()
)
rlSyslogAggregationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogAggregationEnable.setStatus("current")


class _RlSyslogAggregationAgingTime_Type(Unsigned32):
    """Custom type rlSyslogAggregationAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 3600),
    )


_RlSyslogAggregationAgingTime_Type.__name__ = "Unsigned32"
_RlSyslogAggregationAgingTime_Object = MibScalar
rlSyslogAggregationAgingTime = _RlSyslogAggregationAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 2, 15),
    _RlSyslogAggregationAgingTime_Type()
)
rlSyslogAggregationAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogAggregationAgingTime.setStatus("current")
_RlSyslogPhaseOneTests_ObjectIdentity = ObjectIdentity
rlSyslogPhaseOneTests = _RlSyslogPhaseOneTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 3)
)


class _RlSyslogPhaseOneTestGenerator_Type(Integer32):
    """Custom type rlSyslogPhaseOneTestGenerator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              14,
              15,
              16,
              17,
              21,
              22,
              23,
              24,
              25,
              31,
              32,
              33,
              34,
              35,
              36,
              41,
              42,
              43,
              47,
              62)
        )
    )
    namedValues = NamedValues(
        *(("fatalErrorThroughNonFatalInterface", 42),
          ("incorrectParams", 33),
          ("insufficientParams", 32),
          ("logWithBadApplicationID", 24),
          ("logWithBadMessageID", 25),
          ("logWithInvalidComponentID", 23),
          ("logWithUnregisteredComponentID", 22),
          ("nestedFatalErrors", 47),
          ("nonFatalErrorThroughFatalInterface", 43),
          ("oversizedParams", 35),
          ("paramFormatting", 31),
          ("regTheSameComponentTwice", 12),
          ("regWithInvalidApplicationID", 14),
          ("regWithInvalidApplicationList", 17),
          ("regWithInvalidComponentID", 13),
          ("regWithInvalidMessageList", 16),
          ("regWithInvalidMessageString", 15),
          ("snmpAccessToLongMessage", 62),
          ("successfulFatalError", 41),
          ("successfulLoggingWithNoParams", 21),
          ("successfulRegistration", 11),
          ("tooManyParams", 34),
          ("trapParams", 36))
    )


_RlSyslogPhaseOneTestGenerator_Type.__name__ = "Integer32"
_RlSyslogPhaseOneTestGenerator_Object = MibScalar
rlSyslogPhaseOneTestGenerator = _RlSyslogPhaseOneTestGenerator_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 82, 3, 1),
    _RlSyslogPhaseOneTestGenerator_Type()
)
rlSyslogPhaseOneTestGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSyslogPhaseOneTestGenerator.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-SYSLOG-MIB",
    **{"RlSyslogSeverity": RlSyslogSeverity,
       "rlSyslog": rlSyslog,
       "rlSyslogPrivate": rlSyslogPrivate,
       "rlSyslogGlobalEnable": rlSyslogGlobalEnable,
       "rlSyslogMinLogToConsoleSeverity": rlSyslogMinLogToConsoleSeverity,
       "rlSyslogMinLogToFileSeverity": rlSyslogMinLogToFileSeverity,
       "rlSyslogMinLogToCacheSeverity": rlSyslogMinLogToCacheSeverity,
       "rlSyslogClearLogfile": rlSyslogClearLogfile,
       "rlSyslogClearCache": rlSyslogClearCache,
       "rlSyslogMibVersion": rlSyslogMibVersion,
       "rlSyslogLogTable": rlSyslogLogTable,
       "rlSyslogLogEntry": rlSyslogLogEntry,
       "rlSyslogLogCounter": rlSyslogLogCounter,
       "rlSyslogLogDateTime": rlSyslogLogDateTime,
       "rlSyslogLogAppMnemonic": rlSyslogLogAppMnemonic,
       "rlSyslogLogSeverity": rlSyslogLogSeverity,
       "rlSyslogLogMessageMnemonic": rlSyslogLogMessageMnemonic,
       "rlSyslogLogText1": rlSyslogLogText1,
       "rlSyslogLogText2": rlSyslogLogText2,
       "rlSyslogLogText3": rlSyslogLogText3,
       "rlSyslogLogText4": rlSyslogLogText4,
       "rlSyslogLogCacheTable": rlSyslogLogCacheTable,
       "rlSyslogLogCacheEntry": rlSyslogLogCacheEntry,
       "rlSyslogLogCacheCounter": rlSyslogLogCacheCounter,
       "rlSyslogLogCacheDateTime": rlSyslogLogCacheDateTime,
       "rlSyslogLogCacheAppMnemonic": rlSyslogLogCacheAppMnemonic,
       "rlSyslogLogCacheSeverity": rlSyslogLogCacheSeverity,
       "rlSyslogLogCacheMessageMnemonic": rlSyslogLogCacheMessageMnemonic,
       "rlSyslogLogCacheText1": rlSyslogLogCacheText1,
       "rlSyslogLogCacheText2": rlSyslogLogCacheText2,
       "rlSyslogLogCacheText3": rlSyslogLogCacheText3,
       "rlSyslogLogCacheText4": rlSyslogLogCacheText4,
       "rlSyslogConsoleMessagesIgnored": rlSyslogConsoleMessagesIgnored,
       "rlSyslogFileMessagesIgnored": rlSyslogFileMessagesIgnored,
       "rlSyslogFileMessagesLogged": rlSyslogFileMessagesLogged,
       "rlSyslogCacheTotalMessages": rlSyslogCacheTotalMessages,
       "rlSyslogAggregationEnable": rlSyslogAggregationEnable,
       "rlSyslogAggregationAgingTime": rlSyslogAggregationAgingTime,
       "rlSyslogPhaseOneTests": rlSyslogPhaseOneTests,
       "rlSyslogPhaseOneTestGenerator": rlSyslogPhaseOneTestGenerator}
)
