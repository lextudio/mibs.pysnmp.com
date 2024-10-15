# SNMP MIB module (CISCO-SYSLOG-EVENT-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SYSLOG-EVENT-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:23 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SyslogSeverity,) = mibBuilder.importSymbols(
    "CISCO-SYSLOG-MIB",
    "SyslogSeverity")

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

ciscoSyslogEventExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 270)
)
ciscoSyslogEventExtMIB.setRevisions(
        ("2002-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CslogEventDisposition(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoSyslogEventExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSyslogEventExtMIBObjects = _CiscoSyslogEventExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1)
)
_CslogEventConfig_ObjectIdentity = ObjectIdentity
cslogEventConfig = _CslogEventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1)
)


class _CslogEventDetailDefault_Type(Integer32):
    """Custom type cslogEventDetailDefault based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("exhaustiveDetail", 5),
          ("noDisplay", 1),
          ("normalDetail", 3),
          ("sparseDetail", 2),
          ("verboseDetail", 4))
    )


_CslogEventDetailDefault_Type.__name__ = "Integer32"
_CslogEventDetailDefault_Object = MibScalar
cslogEventDetailDefault = _CslogEventDetailDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 1),
    _CslogEventDetailDefault_Type()
)
cslogEventDetailDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslogEventDetailDefault.setStatus("current")


class _CslogEventSeverityDispConsole_Type(SyslogSeverity):
    """Custom type cslogEventSeverityDispConsole based on SyslogSeverity"""


_CslogEventSeverityDispConsole_Object = MibScalar
cslogEventSeverityDispConsole = _CslogEventSeverityDispConsole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 2),
    _CslogEventSeverityDispConsole_Type()
)
cslogEventSeverityDispConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslogEventSeverityDispConsole.setStatus("current")


class _CslogEventSeverityDispHtmlGUI_Type(SyslogSeverity):
    """Custom type cslogEventSeverityDispHtmlGUI based on SyslogSeverity"""


_CslogEventSeverityDispHtmlGUI_Object = MibScalar
cslogEventSeverityDispHtmlGUI = _CslogEventSeverityDispHtmlGUI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 3),
    _CslogEventSeverityDispHtmlGUI_Type()
)
cslogEventSeverityDispHtmlGUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslogEventSeverityDispHtmlGUI.setStatus("current")


class _CslogEventSeverityDispHtmlConsol_Type(SyslogSeverity):
    """Custom type cslogEventSeverityDispHtmlConsol based on SyslogSeverity"""


_CslogEventSeverityDispHtmlConsol_Object = MibScalar
cslogEventSeverityDispHtmlConsol = _CslogEventSeverityDispHtmlConsol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 4),
    _CslogEventSeverityDispHtmlConsol_Type()
)
cslogEventSeverityDispHtmlConsol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslogEventSeverityDispHtmlConsol.setStatus("current")
_CslogEventDispositionTable_Object = MibTable
cslogEventDispositionTable = _CslogEventDispositionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cslogEventDispositionTable.setStatus("current")
_CslogEventDispositionEntry_Object = MibTableRow
cslogEventDispositionEntry = _CslogEventDispositionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1)
)
cslogEventDispositionEntry.setIndexNames(
    (0, "CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionSeverity"),
)
if mibBuilder.loadTexts:
    cslogEventDispositionEntry.setStatus("current")
_CslogEventDispositionSeverity_Type = SyslogSeverity
_CslogEventDispositionSeverity_Object = MibTableColumn
cslogEventDispositionSeverity = _CslogEventDispositionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 1),
    _CslogEventDispositionSeverity_Type()
)
cslogEventDispositionSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslogEventDispositionSeverity.setStatus("current")


class _CslogEventDisposition_Type(CslogEventDisposition):
    """Custom type cslogEventDisposition based on CslogEventDisposition"""
    defaultBinValue = "1"


_CslogEventDisposition_Object = MibTableColumn
cslogEventDisposition = _CslogEventDisposition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 2),
    _CslogEventDisposition_Type()
)
cslogEventDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslogEventDisposition.setStatus("current")
_CslogEventDispositionCount_Type = Counter32
_CslogEventDispositionCount_Object = MibTableColumn
cslogEventDispositionCount = _CslogEventDispositionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 3),
    _CslogEventDispositionCount_Type()
)
cslogEventDispositionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslogEventDispositionCount.setStatus("current")
_CiscoSlogEventExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSlogEventExtMIBConformance = _CiscoSlogEventExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 2)
)
_CiscoSlogEventExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSlogEventExtMIBCompliances = _CiscoSlogEventExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1)
)
_CiscoSlogEventExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSlogEventExtMIBGroups = _CiscoSlogEventExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2)
)

# Managed Objects groups

ciscoSlogEventExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 1)
)
ciscoSlogEventExtConfigGroup.setObjects(
      *(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDetailDefault"),
        ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispConsole"),
        ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlGUI"),
        ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlConsol"),
        ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDisposition"))
)
if mibBuilder.loadTexts:
    ciscoSlogEventExtConfigGroup.setStatus("current")

ciscoSlogEventExtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 2)
)
ciscoSlogEventExtStatsGroup.setObjects(
    ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionCount")
)
if mibBuilder.loadTexts:
    ciscoSlogEventExtStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSlogEventExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSlogEventExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SYSLOG-EVENT-EXT-MIB",
    **{"CslogEventDisposition": CslogEventDisposition,
       "ciscoSyslogEventExtMIB": ciscoSyslogEventExtMIB,
       "ciscoSyslogEventExtMIBObjects": ciscoSyslogEventExtMIBObjects,
       "cslogEventConfig": cslogEventConfig,
       "cslogEventDetailDefault": cslogEventDetailDefault,
       "cslogEventSeverityDispConsole": cslogEventSeverityDispConsole,
       "cslogEventSeverityDispHtmlGUI": cslogEventSeverityDispHtmlGUI,
       "cslogEventSeverityDispHtmlConsol": cslogEventSeverityDispHtmlConsol,
       "cslogEventDispositionTable": cslogEventDispositionTable,
       "cslogEventDispositionEntry": cslogEventDispositionEntry,
       "cslogEventDispositionSeverity": cslogEventDispositionSeverity,
       "cslogEventDisposition": cslogEventDisposition,
       "cslogEventDispositionCount": cslogEventDispositionCount,
       "ciscoSlogEventExtMIBConformance": ciscoSlogEventExtMIBConformance,
       "ciscoSlogEventExtMIBCompliances": ciscoSlogEventExtMIBCompliances,
       "ciscoSlogEventExtCompliance": ciscoSlogEventExtCompliance,
       "ciscoSlogEventExtMIBGroups": ciscoSlogEventExtMIBGroups,
       "ciscoSlogEventExtConfigGroup": ciscoSlogEventExtConfigGroup,
       "ciscoSlogEventExtStatsGroup": ciscoSlogEventExtStatsGroup}
)
