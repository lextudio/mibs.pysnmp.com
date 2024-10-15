# SNMP MIB module (BENU-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:01 2024
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

(benuPlatform,) = mibBuilder.importSymbols(
    "BENU-PLATFORM-MIB",
    "benuPlatform")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

benuSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3)
)
benuSyslog.setRevisions(
        ("2015-01-09 00:00",
         "2014-11-06 00:00",
         "2013-11-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BSyslogNotifications_ObjectIdentity = ObjectIdentity
bSyslogNotifications = _BSyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 0)
)
_BSyslogSize_Type = Unsigned32
_BSyslogSize_Object = MibScalar
bSyslogSize = _BSyslogSize_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 1),
    _BSyslogSize_Type()
)
bSyslogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSyslogSize.setStatus("current")


class _BSyslogMaxSize_Type(Integer32):
    """Custom type bSyslogMaxSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 5242880),
    )


_BSyslogMaxSize_Type.__name__ = "Integer32"
_BSyslogMaxSize_Object = MibScalar
bSyslogMaxSize = _BSyslogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 2),
    _BSyslogMaxSize_Type()
)
bSyslogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSyslogMaxSize.setStatus("current")


class _BSyslogServerEnable_Type(Integer32):
    """Custom type bSyslogServerEnable based on Integer32"""
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


_BSyslogServerEnable_Type.__name__ = "Integer32"
_BSyslogServerEnable_Object = MibScalar
bSyslogServerEnable = _BSyslogServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 3),
    _BSyslogServerEnable_Type()
)
bSyslogServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSyslogServerEnable.setStatus("current")
_BSyslogServerTable_Object = MibTable
bSyslogServerTable = _BSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 4)
)
if mibBuilder.loadTexts:
    bSyslogServerTable.setStatus("current")
_BSyslogServerEntry_Object = MibTableRow
bSyslogServerEntry = _BSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1)
)
bSyslogServerEntry.setIndexNames(
    (0, "BENU-SYSLOG-MIB", "bSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    bSyslogServerEntry.setStatus("current")
_BSyslogServerIndex_Type = Unsigned32
_BSyslogServerIndex_Object = MibTableColumn
bSyslogServerIndex = _BSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 1),
    _BSyslogServerIndex_Type()
)
bSyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bSyslogServerIndex.setStatus("current")
_BSyslogServerAddress_Type = IpAddress
_BSyslogServerAddress_Object = MibTableColumn
bSyslogServerAddress = _BSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 2),
    _BSyslogServerAddress_Type()
)
bSyslogServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSyslogServerAddress.setStatus("current")
_BSyslogServerPort_Type = InetPortNumber
_BSyslogServerPort_Object = MibTableColumn
bSyslogServerPort = _BSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 3),
    _BSyslogServerPort_Type()
)
bSyslogServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSyslogServerPort.setStatus("current")


class _BSyslogSeverity_Type(Integer32):
    """Custom type bSyslogSeverity based on Integer32"""
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
        *(("alerts", 1),
          ("critical", 2),
          ("debugging", 7),
          ("emergencies", 0),
          ("errors", 3),
          ("informational", 6),
          ("notifications", 5),
          ("warnings", 4))
    )


_BSyslogSeverity_Type.__name__ = "Integer32"
_BSyslogSeverity_Object = MibScalar
bSyslogSeverity = _BSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 5),
    _BSyslogSeverity_Type()
)
bSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSyslogSeverity.setStatus("current")


class _BSyslogConsoleSeverity_Type(Integer32):
    """Custom type bSyslogConsoleSeverity based on Integer32"""
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
        *(("alerts", 1),
          ("critical", 2),
          ("debugging", 7),
          ("emergencies", 0),
          ("errors", 3),
          ("informational", 6),
          ("notifications", 5),
          ("warnings", 4))
    )


_BSyslogConsoleSeverity_Type.__name__ = "Integer32"
_BSyslogConsoleSeverity_Object = MibScalar
bSyslogConsoleSeverity = _BSyslogConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 6),
    _BSyslogConsoleSeverity_Type()
)
bSyslogConsoleSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSyslogConsoleSeverity.setStatus("current")


class _BSyslogClear_Type(Integer32):
    """Custom type bSyslogClear based on Integer32"""
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


_BSyslogClear_Type.__name__ = "Integer32"
_BSyslogClear_Object = MibScalar
bSyslogClear = _BSyslogClear_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 3, 7),
    _BSyslogClear_Type()
)
bSyslogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSyslogClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-SYSLOG-MIB",
    **{"benuSyslog": benuSyslog,
       "bSyslogNotifications": bSyslogNotifications,
       "bSyslogSize": bSyslogSize,
       "bSyslogMaxSize": bSyslogMaxSize,
       "bSyslogServerEnable": bSyslogServerEnable,
       "bSyslogServerTable": bSyslogServerTable,
       "bSyslogServerEntry": bSyslogServerEntry,
       "bSyslogServerIndex": bSyslogServerIndex,
       "bSyslogServerAddress": bSyslogServerAddress,
       "bSyslogServerPort": bSyslogServerPort,
       "bSyslogSeverity": bSyslogSeverity,
       "bSyslogConsoleSeverity": bSyslogConsoleSeverity,
       "bSyslogClear": bSyslogClear}
)
