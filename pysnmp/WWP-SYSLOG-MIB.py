# SNMP MIB module (WWP-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:24 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpSyslogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27)
)
wwpSyslogMib.setRevisions(
        ("2006-03-09 17:00",
         "2001-07-25 10:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpSyslogObjects_ObjectIdentity = ObjectIdentity
wwpSyslogObjects = _WwpSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1)
)
_WwpSyslog_ObjectIdentity = ObjectIdentity
wwpSyslog = _WwpSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1)
)


class _WwpSyslogSeverity_Type(Integer32):
    """Custom type wwpSyslogSeverity based on Integer32"""
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
        *(("logAlert", 1),
          ("logCritical", 2),
          ("logDebugging", 7),
          ("logEmergency", 0),
          ("logErrors", 3),
          ("logInformational", 6),
          ("logNotifications", 5),
          ("logWarnings", 4))
    )


_WwpSyslogSeverity_Type.__name__ = "Integer32"
_WwpSyslogSeverity_Object = MibScalar
wwpSyslogSeverity = _WwpSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 1),
    _WwpSyslogSeverity_Type()
)
wwpSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSyslogSeverity.setStatus("current")
_WwpSyslogServerTable_Object = MibTable
wwpSyslogServerTable = _WwpSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpSyslogServerTable.setStatus("current")
_WwpSyslogServerEntry_Object = MibTableRow
wwpSyslogServerEntry = _WwpSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1)
)
wwpSyslogServerEntry.setIndexNames(
    (0, "WWP-SYSLOG-MIB", "wwpSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    wwpSyslogServerEntry.setStatus("current")


class _WwpSyslogServerIndex_Type(Integer32):
    """Custom type wwpSyslogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_WwpSyslogServerIndex_Type.__name__ = "Integer32"
_WwpSyslogServerIndex_Object = MibTableColumn
wwpSyslogServerIndex = _WwpSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 1),
    _WwpSyslogServerIndex_Type()
)
wwpSyslogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSyslogServerIndex.setStatus("current")
_WwpSyslogServerIPAddress_Type = IpAddress
_WwpSyslogServerIPAddress_Object = MibTableColumn
wwpSyslogServerIPAddress = _WwpSyslogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 2),
    _WwpSyslogServerIPAddress_Type()
)
wwpSyslogServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSyslogServerIPAddress.setStatus("current")


class _WwpSyslogServerPort_Type(Integer32):
    """Custom type wwpSyslogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpSyslogServerPort_Type.__name__ = "Integer32"
_WwpSyslogServerPort_Object = MibTableColumn
wwpSyslogServerPort = _WwpSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 3),
    _WwpSyslogServerPort_Type()
)
wwpSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSyslogServerPort.setStatus("current")
_WwpSyslogServerStatus_Type = RowStatus
_WwpSyslogServerStatus_Object = MibTableColumn
wwpSyslogServerStatus = _WwpSyslogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 4),
    _WwpSyslogServerStatus_Type()
)
wwpSyslogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpSyslogServerStatus.setStatus("current")


class _WwpSyslogServerCustomPrefix_Type(DisplayString):
    """Custom type wwpSyslogServerCustomPrefix based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpSyslogServerCustomPrefix_Type.__name__ = "DisplayString"
_WwpSyslogServerCustomPrefix_Object = MibTableColumn
wwpSyslogServerCustomPrefix = _WwpSyslogServerCustomPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 5),
    _WwpSyslogServerCustomPrefix_Type()
)
wwpSyslogServerCustomPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpSyslogServerCustomPrefix.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-SYSLOG-MIB",
    **{"wwpSyslogMib": wwpSyslogMib,
       "wwpSyslogObjects": wwpSyslogObjects,
       "wwpSyslog": wwpSyslog,
       "wwpSyslogSeverity": wwpSyslogSeverity,
       "wwpSyslogServerTable": wwpSyslogServerTable,
       "wwpSyslogServerEntry": wwpSyslogServerEntry,
       "wwpSyslogServerIndex": wwpSyslogServerIndex,
       "wwpSyslogServerIPAddress": wwpSyslogServerIPAddress,
       "wwpSyslogServerPort": wwpSyslogServerPort,
       "wwpSyslogServerStatus": wwpSyslogServerStatus,
       "wwpSyslogServerCustomPrefix": wwpSyslogServerCustomPrefix}
)
