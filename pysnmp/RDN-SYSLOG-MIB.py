# SNMP MIB module (RDN-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:16 2024
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

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

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

rdnSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 3)
)
rdnSyslog.setRevisions(
        ("2008-08-08 00:00",
         "2004-01-23 00:00",
         "2003-11-05 00:00",
         "2003-01-30 00:00",
         "2000-06-14 00:00",
         "2000-06-08 00:00",
         "2000-05-23 00:00",
         "2000-05-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnSyslogMIB_ObjectIdentity = ObjectIdentity
rdnSyslogMIB = _RdnSyslogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 3, 0)
)
_RdnSyslogTraps_ObjectIdentity = ObjectIdentity
rdnSyslogTraps = _RdnSyslogTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 3, 0, 0)
)
_RdnSyslogSize_Type = Integer32
_RdnSyslogSize_Object = MibScalar
rdnSyslogSize = _RdnSyslogSize_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 1),
    _RdnSyslogSize_Type()
)
rdnSyslogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSyslogSize.setStatus("current")


class _RdnSyslogMaxSize_Type(Integer32):
    """Custom type rdnSyslogMaxSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 5242880),
    )


_RdnSyslogMaxSize_Type.__name__ = "Integer32"
_RdnSyslogMaxSize_Object = MibScalar
rdnSyslogMaxSize = _RdnSyslogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 2),
    _RdnSyslogMaxSize_Type()
)
rdnSyslogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogMaxSize.setStatus("current")


class _RdnSyslogServerEnable_Type(Integer32):
    """Custom type rdnSyslogServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RdnSyslogServerEnable_Type.__name__ = "Integer32"
_RdnSyslogServerEnable_Object = MibScalar
rdnSyslogServerEnable = _RdnSyslogServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 3),
    _RdnSyslogServerEnable_Type()
)
rdnSyslogServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogServerEnable.setStatus("current")
_RdnSyslogServerTable_Object = MibTable
rdnSyslogServerTable = _RdnSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 4)
)
if mibBuilder.loadTexts:
    rdnSyslogServerTable.setStatus("current")
_RdnSyslogServerEntry_Object = MibTableRow
rdnSyslogServerEntry = _RdnSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 4, 1)
)
rdnSyslogServerEntry.setIndexNames(
    (0, "RDN-SYSLOG-MIB", "rdnSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    rdnSyslogServerEntry.setStatus("current")
_RdnSyslogServerIndex_Type = Integer32
_RdnSyslogServerIndex_Object = MibTableColumn
rdnSyslogServerIndex = _RdnSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 4, 1, 1),
    _RdnSyslogServerIndex_Type()
)
rdnSyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnSyslogServerIndex.setStatus("current")
_RdnSyslogServerAddress_Type = IpAddress
_RdnSyslogServerAddress_Object = MibTableColumn
rdnSyslogServerAddress = _RdnSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 4, 1, 2),
    _RdnSyslogServerAddress_Type()
)
rdnSyslogServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogServerAddress.setStatus("current")


class _RdnSyslogServerStatus_Type(Integer32):
    """Custom type rdnSyslogServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RdnSyslogServerStatus_Type.__name__ = "Integer32"
_RdnSyslogServerStatus_Object = MibTableColumn
rdnSyslogServerStatus = _RdnSyslogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 4, 1, 3),
    _RdnSyslogServerStatus_Type()
)
rdnSyslogServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogServerStatus.setStatus("current")


class _RdnSyslogSeverity_Type(Integer32):
    """Custom type rdnSyslogSeverity based on Integer32"""
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
        *(("alerts", 6),
          ("critical", 5),
          ("disable", 0),
          ("emergencies", 7),
          ("errors", 4),
          ("informational", 1),
          ("notifications", 2),
          ("warnings", 3))
    )


_RdnSyslogSeverity_Type.__name__ = "Integer32"
_RdnSyslogSeverity_Object = MibScalar
rdnSyslogSeverity = _RdnSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 5),
    _RdnSyslogSeverity_Type()
)
rdnSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogSeverity.setStatus("current")


class _RdnSyslogConsoleSeverity_Type(Integer32):
    """Custom type rdnSyslogConsoleSeverity based on Integer32"""
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
        *(("alerts", 6),
          ("critical", 5),
          ("disable", 0),
          ("emergencies", 7),
          ("errors", 4),
          ("informational", 1),
          ("notifications", 2),
          ("warnings", 3))
    )


_RdnSyslogConsoleSeverity_Type.__name__ = "Integer32"
_RdnSyslogConsoleSeverity_Object = MibScalar
rdnSyslogConsoleSeverity = _RdnSyslogConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 6),
    _RdnSyslogConsoleSeverity_Type()
)
rdnSyslogConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogConsoleSeverity.setStatus("current")


class _RdnSyslogClear_Type(Integer32):
    """Custom type rdnSyslogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_RdnSyslogClear_Type.__name__ = "Integer32"
_RdnSyslogClear_Object = MibScalar
rdnSyslogClear = _RdnSyslogClear_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 7),
    _RdnSyslogClear_Type()
)
rdnSyslogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogClear.setStatus("current")


class _RdnSyslogTrapSeverity_Type(Integer32):
    """Custom type rdnSyslogTrapSeverity based on Integer32"""
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
        *(("alerts", 6),
          ("critical", 5),
          ("disable", 0),
          ("emergencies", 7),
          ("errors", 4),
          ("informational", 1),
          ("notifications", 2),
          ("warnings", 3))
    )


_RdnSyslogTrapSeverity_Type.__name__ = "Integer32"
_RdnSyslogTrapSeverity_Object = MibScalar
rdnSyslogTrapSeverity = _RdnSyslogTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 8),
    _RdnSyslogTrapSeverity_Type()
)
rdnSyslogTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogTrapSeverity.setStatus("current")
_RdnSyslogMessageTable_Object = MibTable
rdnSyslogMessageTable = _RdnSyslogMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 9)
)
if mibBuilder.loadTexts:
    rdnSyslogMessageTable.setStatus("current")
_RdnSyslogMessageTableEntry_Object = MibTableRow
rdnSyslogMessageTableEntry = _RdnSyslogMessageTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 9, 1)
)
rdnSyslogMessageTableEntry.setIndexNames(
    (0, "RDN-SYSLOG-MIB", "rdnSyslogMessageIndex"),
)
if mibBuilder.loadTexts:
    rdnSyslogMessageTableEntry.setStatus("current")
_RdnSyslogMessageIndex_Type = Integer32
_RdnSyslogMessageIndex_Object = MibTableColumn
rdnSyslogMessageIndex = _RdnSyslogMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 9, 1, 1),
    _RdnSyslogMessageIndex_Type()
)
rdnSyslogMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnSyslogMessageIndex.setStatus("current")


class _RdnSyslogMessageString_Type(OctetString):
    """Custom type rdnSyslogMessageString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RdnSyslogMessageString_Type.__name__ = "OctetString"
_RdnSyslogMessageString_Object = MibTableColumn
rdnSyslogMessageString = _RdnSyslogMessageString_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 9, 1, 2),
    _RdnSyslogMessageString_Type()
)
rdnSyslogMessageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSyslogMessageString.setStatus("current")


class _RdnSyslogRateLimitAutoRestart_Type(Integer32):
    """Custom type rdnSyslogRateLimitAutoRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RdnSyslogRateLimitAutoRestart_Type.__name__ = "Integer32"
_RdnSyslogRateLimitAutoRestart_Object = MibScalar
rdnSyslogRateLimitAutoRestart = _RdnSyslogRateLimitAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 4981, 3, 10),
    _RdnSyslogRateLimitAutoRestart_Type()
)
rdnSyslogRateLimitAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnSyslogRateLimitAutoRestart.setStatus("obsolete")

# Managed Objects groups


# Notification objects

rdnSyslogSeverityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 3, 0, 0, 1)
)
rdnSyslogSeverityTrap.setObjects(
    ("RDN-SYSLOG-MIB", "rdnSyslogTrapSeverity")
)
if mibBuilder.loadTexts:
    rdnSyslogSeverityTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-SYSLOG-MIB",
    **{"rdnSyslog": rdnSyslog,
       "rdnSyslogMIB": rdnSyslogMIB,
       "rdnSyslogTraps": rdnSyslogTraps,
       "rdnSyslogSeverityTrap": rdnSyslogSeverityTrap,
       "rdnSyslogSize": rdnSyslogSize,
       "rdnSyslogMaxSize": rdnSyslogMaxSize,
       "rdnSyslogServerEnable": rdnSyslogServerEnable,
       "rdnSyslogServerTable": rdnSyslogServerTable,
       "rdnSyslogServerEntry": rdnSyslogServerEntry,
       "rdnSyslogServerIndex": rdnSyslogServerIndex,
       "rdnSyslogServerAddress": rdnSyslogServerAddress,
       "rdnSyslogServerStatus": rdnSyslogServerStatus,
       "rdnSyslogSeverity": rdnSyslogSeverity,
       "rdnSyslogConsoleSeverity": rdnSyslogConsoleSeverity,
       "rdnSyslogClear": rdnSyslogClear,
       "rdnSyslogTrapSeverity": rdnSyslogTrapSeverity,
       "rdnSyslogMessageTable": rdnSyslogMessageTable,
       "rdnSyslogMessageTableEntry": rdnSyslogMessageTableEntry,
       "rdnSyslogMessageIndex": rdnSyslogMessageIndex,
       "rdnSyslogMessageString": rdnSyslogMessageString,
       "rdnSyslogRateLimitAutoRestart": rdnSyslogRateLimitAutoRestart}
)
