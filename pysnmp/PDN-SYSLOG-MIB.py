# SNMP MIB module (PDN-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:11 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(pdn_syslog,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-syslog")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

pdnSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1)
)
pdnSyslog.setRevisions(
        ("2003-02-13 00:00",
         "2001-11-15 00:00",
         "2001-04-10 00:00",
         "2001-08-09 00:00",
         "2000-04-24 00:00",
         "2000-02-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PdnSyslogStatus_Type(Integer32):
    """Custom type pdnSyslogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PdnSyslogStatus_Type.__name__ = "Integer32"
_PdnSyslogStatus_Object = MibScalar
pdnSyslogStatus = _PdnSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 1),
    _PdnSyslogStatus_Type()
)
pdnSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogStatus.setStatus("current")
_PdnSyslogIPAddr_Type = IpAddress
_PdnSyslogIPAddr_Object = MibScalar
pdnSyslogIPAddr = _PdnSyslogIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 2),
    _PdnSyslogIPAddr_Type()
)
pdnSyslogIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogIPAddr.setStatus("current")


class _PdnSyslogLevel_Type(Integer32):
    """Custom type pdnSyslogLevel based on Integer32"""
    defaultValue = 3

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
        *(("emerg", 1),
          ("err", 2),
          ("info", 4),
          ("norm", 3))
    )


_PdnSyslogLevel_Type.__name__ = "Integer32"
_PdnSyslogLevel_Object = MibScalar
pdnSyslogLevel = _PdnSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 3),
    _PdnSyslogLevel_Type()
)
pdnSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogLevel.setStatus("deprecated")


class _PdnSyslogPort_Type(Integer32):
    """Custom type pdnSyslogPort based on Integer32"""
    defaultValue = 514


_PdnSyslogPort_Object = MibScalar
pdnSyslogPort = _PdnSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 4),
    _PdnSyslogPort_Type()
)
pdnSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogPort.setStatus("current")


class _PdnSyslogSeverityThreshold_Type(Integer32):
    """Custom type pdnSyslogSeverityThreshold based on Integer32"""
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
          ("emerg", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_PdnSyslogSeverityThreshold_Type.__name__ = "Integer32"
_PdnSyslogSeverityThreshold_Object = MibScalar
pdnSyslogSeverityThreshold = _PdnSyslogSeverityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 5),
    _PdnSyslogSeverityThreshold_Type()
)
pdnSyslogSeverityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogSeverityThreshold.setStatus("current")


class _PdnSyslogRemoteDaemon_Type(Integer32):
    """Custom type pdnSyslogRemoteDaemon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PdnSyslogRemoteDaemon_Type.__name__ = "Integer32"
_PdnSyslogRemoteDaemon_Object = MibScalar
pdnSyslogRemoteDaemon = _PdnSyslogRemoteDaemon_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 6),
    _PdnSyslogRemoteDaemon_Type()
)
pdnSyslogRemoteDaemon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogRemoteDaemon.setStatus("current")
_PdnSyslogTable_Object = MibTable
pdnSyslogTable = _PdnSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 7)
)
if mibBuilder.loadTexts:
    pdnSyslogTable.setStatus("current")
_PdnSyslogEntry_Object = MibTableRow
pdnSyslogEntry = _PdnSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 7, 1)
)
pdnSyslogEntry.setIndexNames(
    (0, "PDN-SYSLOG-MIB", "pdnSyslogNumber"),
)
if mibBuilder.loadTexts:
    pdnSyslogEntry.setStatus("current")
_PdnSyslogNumber_Type = Integer32
_PdnSyslogNumber_Object = MibTableColumn
pdnSyslogNumber = _PdnSyslogNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 7, 1, 1),
    _PdnSyslogNumber_Type()
)
pdnSyslogNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnSyslogNumber.setStatus("current")


class _PdnSyslogMessage_Type(OctetString):
    """Custom type pdnSyslogMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1024, 1024),
    )


_PdnSyslogMessage_Type.__name__ = "OctetString"
_PdnSyslogMessage_Object = MibTableColumn
pdnSyslogMessage = _PdnSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 7, 1, 2),
    _PdnSyslogMessage_Type()
)
pdnSyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnSyslogMessage.setStatus("current")
_PdnSyslogNumOfMsgInTable_Type = Integer32
_PdnSyslogNumOfMsgInTable_Object = MibScalar
pdnSyslogNumOfMsgInTable = _PdnSyslogNumOfMsgInTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 8),
    _PdnSyslogNumOfMsgInTable_Type()
)
pdnSyslogNumOfMsgInTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnSyslogNumOfMsgInTable.setStatus("current")
_PdnSyslogMaxTableSize_Type = Integer32
_PdnSyslogMaxTableSize_Object = MibScalar
pdnSyslogMaxTableSize = _PdnSyslogMaxTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 9),
    _PdnSyslogMaxTableSize_Type()
)
pdnSyslogMaxTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnSyslogMaxTableSize.setStatus("current")


class _PdnSyslogClearTable_Type(Integer32):
    """Custom type pdnSyslogClearTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noOp", 1))
    )


_PdnSyslogClearTable_Type.__name__ = "Integer32"
_PdnSyslogClearTable_Object = MibScalar
pdnSyslogClearTable = _PdnSyslogClearTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 10),
    _PdnSyslogClearTable_Type()
)
pdnSyslogClearTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogClearTable.setStatus("current")


class _PdnSyslogMsgToConsole_Type(Integer32):
    """Custom type pdnSyslogMsgToConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PdnSyslogMsgToConsole_Type.__name__ = "Integer32"
_PdnSyslogMsgToConsole_Object = MibScalar
pdnSyslogMsgToConsole = _PdnSyslogMsgToConsole_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 11),
    _PdnSyslogMsgToConsole_Type()
)
pdnSyslogMsgToConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogMsgToConsole.setStatus("current")


class _PdnSyslogRateLimiting_Type(Integer32):
    """Custom type pdnSyslogRateLimiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PdnSyslogRateLimiting_Type.__name__ = "Integer32"
_PdnSyslogRateLimiting_Object = MibScalar
pdnSyslogRateLimiting = _PdnSyslogRateLimiting_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 12),
    _PdnSyslogRateLimiting_Type()
)
pdnSyslogRateLimiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnSyslogRateLimiting.setStatus("current")
_PdnEntitySyslogTable_Object = MibTable
pdnEntitySyslogTable = _PdnEntitySyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 13)
)
if mibBuilder.loadTexts:
    pdnEntitySyslogTable.setStatus("current")
_PdnEntitySyslogEntry_Object = MibTableRow
pdnEntitySyslogEntry = _PdnEntitySyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 13, 1)
)
pdnEntitySyslogEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "PDN-SYSLOG-MIB", "pdnEntitySyslogNumber"),
)
if mibBuilder.loadTexts:
    pdnEntitySyslogEntry.setStatus("current")
_PdnEntitySyslogNumber_Type = Integer32
_PdnEntitySyslogNumber_Object = MibTableColumn
pdnEntitySyslogNumber = _PdnEntitySyslogNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 13, 1, 1),
    _PdnEntitySyslogNumber_Type()
)
pdnEntitySyslogNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnEntitySyslogNumber.setStatus("current")


class _PdnEntitySyslogMessage_Type(OctetString):
    """Custom type pdnEntitySyslogMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1024, 1024),
    )


_PdnEntitySyslogMessage_Type.__name__ = "OctetString"
_PdnEntitySyslogMessage_Object = MibTableColumn
pdnEntitySyslogMessage = _PdnEntitySyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 1, 13, 1, 2),
    _PdnEntitySyslogMessage_Type()
)
pdnEntitySyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnEntitySyslogMessage.setStatus("current")
_PdnSyslogConformance_ObjectIdentity = ObjectIdentity
pdnSyslogConformance = _PdnSyslogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 14)
)
_PdnSyslogCompliances_ObjectIdentity = ObjectIdentity
pdnSyslogCompliances = _PdnSyslogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 14, 1)
)
_PdnSyslogGroups_ObjectIdentity = ObjectIdentity
pdnSyslogGroups = _PdnSyslogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 14, 2)
)

# Managed Objects groups

pdnSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 14, 2, 1)
)
pdnSyslogGroup.setObjects(
      *(("PDN-SYSLOG-MIB", "pdnSyslogStatus"),
        ("PDN-SYSLOG-MIB", "pdnSyslogIPAddr"),
        ("PDN-SYSLOG-MIB", "pdnSyslogPort"),
        ("PDN-SYSLOG-MIB", "pdnSyslogSeverityThreshold"),
        ("PDN-SYSLOG-MIB", "pdnSyslogRemoteDaemon"),
        ("PDN-SYSLOG-MIB", "pdnSyslogMessage"),
        ("PDN-SYSLOG-MIB", "pdnSyslogNumOfMsgInTable"),
        ("PDN-SYSLOG-MIB", "pdnSyslogMaxTableSize"),
        ("PDN-SYSLOG-MIB", "pdnSyslogClearTable"),
        ("PDN-SYSLOG-MIB", "pdnSyslogMsgToConsole"),
        ("PDN-SYSLOG-MIB", "pdnSyslogRateLimiting"))
)
if mibBuilder.loadTexts:
    pdnSyslogGroup.setStatus("current")

pdnSyslogOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 14, 2, 2)
)
pdnSyslogOptionalGroup.setObjects(
    ("PDN-SYSLOG-MIB", "pdnEntitySyslogMessage")
)
if mibBuilder.loadTexts:
    pdnSyslogOptionalGroup.setStatus("current")

pdnSyslogDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 14, 2, 3)
)
pdnSyslogDeprecatedGroup.setObjects(
    ("PDN-SYSLOG-MIB", "pdnSyslogLevel")
)
if mibBuilder.loadTexts:
    pdnSyslogDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnSyslogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31, 14, 1, 1)
)
if mibBuilder.loadTexts:
    pdnSyslogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-SYSLOG-MIB",
    **{"pdnSyslog": pdnSyslog,
       "pdnSyslogStatus": pdnSyslogStatus,
       "pdnSyslogIPAddr": pdnSyslogIPAddr,
       "pdnSyslogLevel": pdnSyslogLevel,
       "pdnSyslogPort": pdnSyslogPort,
       "pdnSyslogSeverityThreshold": pdnSyslogSeverityThreshold,
       "pdnSyslogRemoteDaemon": pdnSyslogRemoteDaemon,
       "pdnSyslogTable": pdnSyslogTable,
       "pdnSyslogEntry": pdnSyslogEntry,
       "pdnSyslogNumber": pdnSyslogNumber,
       "pdnSyslogMessage": pdnSyslogMessage,
       "pdnSyslogNumOfMsgInTable": pdnSyslogNumOfMsgInTable,
       "pdnSyslogMaxTableSize": pdnSyslogMaxTableSize,
       "pdnSyslogClearTable": pdnSyslogClearTable,
       "pdnSyslogMsgToConsole": pdnSyslogMsgToConsole,
       "pdnSyslogRateLimiting": pdnSyslogRateLimiting,
       "pdnEntitySyslogTable": pdnEntitySyslogTable,
       "pdnEntitySyslogEntry": pdnEntitySyslogEntry,
       "pdnEntitySyslogNumber": pdnEntitySyslogNumber,
       "pdnEntitySyslogMessage": pdnEntitySyslogMessage,
       "pdnSyslogConformance": pdnSyslogConformance,
       "pdnSyslogCompliances": pdnSyslogCompliances,
       "pdnSyslogCompliance": pdnSyslogCompliance,
       "pdnSyslogGroups": pdnSyslogGroups,
       "pdnSyslogGroup": pdnSyslogGroup,
       "pdnSyslogOptionalGroup": pdnSyslogOptionalGroup,
       "pdnSyslogDeprecatedGroup": pdnSyslogDeprecatedGroup}
)
