# SNMP MIB module (JUNIPER-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:18 2024
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

(jnxMibs,
 jnxSyslogNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxSyslogNotifications")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxSyslogSeverity(Integer32, TextualConvention):
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
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )



class JnxSyslogFacility(Integer32, TextualConvention):
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("auth", 5),
          ("authPriv", 11),
          ("change", 23),
          ("conflict", 22),
          ("console", 15),
          ("cron", 10),
          ("daemon", 4),
          ("dfc", 18),
          ("firewall", 20),
          ("ftp", 12),
          ("interact", 24),
          ("kernel", 1),
          ("local0", 17),
          ("local2", 19),
          ("lpr", 7),
          ("mail", 3),
          ("news", 8),
          ("ntp", 13),
          ("pfe", 21),
          ("security", 14),
          ("syslog", 6),
          ("user", 2),
          ("uucp", 9))
    )



# MIB Managed Objects in the order of their OIDs

_JnxSyslogNotifyVars_ObjectIdentity = ObjectIdentity
jnxSyslogNotifyVars = _JnxSyslogNotifyVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1)
)
if mibBuilder.loadTexts:
    jnxSyslogNotifyVars.setStatus("current")
_JnxSyslogTable_Object = MibTable
jnxSyslogTable = _JnxSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSyslogTable.setStatus("current")
_JnxSyslogEntry_Object = MibTableRow
jnxSyslogEntry = _JnxSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1)
)
jnxSyslogEntry.setIndexNames(
    (0, "JUNIPER-SYSLOG-MIB", "jnxSyslogId"),
)
if mibBuilder.loadTexts:
    jnxSyslogEntry.setStatus("current")
_JnxSyslogId_Type = Unsigned32
_JnxSyslogId_Object = MibTableColumn
jnxSyslogId = _JnxSyslogId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 1),
    _JnxSyslogId_Type()
)
jnxSyslogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSyslogId.setStatus("current")
_JnxSyslogEventName_Type = DisplayString
_JnxSyslogEventName_Object = MibTableColumn
jnxSyslogEventName = _JnxSyslogEventName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 2),
    _JnxSyslogEventName_Type()
)
jnxSyslogEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogEventName.setStatus("current")
_JnxSyslogTimestamp_Type = DateAndTime
_JnxSyslogTimestamp_Object = MibTableColumn
jnxSyslogTimestamp = _JnxSyslogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 3),
    _JnxSyslogTimestamp_Type()
)
jnxSyslogTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogTimestamp.setStatus("current")
_JnxSyslogSeverity_Type = JnxSyslogSeverity
_JnxSyslogSeverity_Object = MibTableColumn
jnxSyslogSeverity = _JnxSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 4),
    _JnxSyslogSeverity_Type()
)
jnxSyslogSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogSeverity.setStatus("current")
_JnxSyslogFacility_Type = JnxSyslogFacility
_JnxSyslogFacility_Object = MibTableColumn
jnxSyslogFacility = _JnxSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 5),
    _JnxSyslogFacility_Type()
)
jnxSyslogFacility.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogFacility.setStatus("current")
_JnxSyslogProcessId_Type = Unsigned32
_JnxSyslogProcessId_Object = MibTableColumn
jnxSyslogProcessId = _JnxSyslogProcessId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 6),
    _JnxSyslogProcessId_Type()
)
jnxSyslogProcessId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogProcessId.setStatus("current")
_JnxSyslogProcessName_Type = DisplayString
_JnxSyslogProcessName_Object = MibTableColumn
jnxSyslogProcessName = _JnxSyslogProcessName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 7),
    _JnxSyslogProcessName_Type()
)
jnxSyslogProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogProcessName.setStatus("current")
_JnxSyslogHostName_Type = DisplayString
_JnxSyslogHostName_Object = MibTableColumn
jnxSyslogHostName = _JnxSyslogHostName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 8),
    _JnxSyslogHostName_Type()
)
jnxSyslogHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogHostName.setStatus("current")
_JnxSyslogMessage_Type = OctetString
_JnxSyslogMessage_Object = MibTableColumn
jnxSyslogMessage = _JnxSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 9),
    _JnxSyslogMessage_Type()
)
jnxSyslogMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogMessage.setStatus("current")
_JnxSyslogAvTable_Object = MibTable
jnxSyslogAvTable = _JnxSyslogAvTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2)
)
if mibBuilder.loadTexts:
    jnxSyslogAvTable.setStatus("current")
_JnxSyslogAvEntry_Object = MibTableRow
jnxSyslogAvEntry = _JnxSyslogAvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1)
)
jnxSyslogAvEntry.setIndexNames(
    (0, "JUNIPER-SYSLOG-MIB", "jnxSyslogId"),
    (0, "JUNIPER-SYSLOG-MIB", "jnxSyslogAvIndex"),
)
if mibBuilder.loadTexts:
    jnxSyslogAvEntry.setStatus("current")
_JnxSyslogAvIndex_Type = Unsigned32
_JnxSyslogAvIndex_Object = MibTableColumn
jnxSyslogAvIndex = _JnxSyslogAvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 1),
    _JnxSyslogAvIndex_Type()
)
jnxSyslogAvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSyslogAvIndex.setStatus("current")
_JnxSyslogAvAttribute_Type = DisplayString
_JnxSyslogAvAttribute_Object = MibTableColumn
jnxSyslogAvAttribute = _JnxSyslogAvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 2),
    _JnxSyslogAvAttribute_Type()
)
jnxSyslogAvAttribute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogAvAttribute.setStatus("current")
_JnxSyslogAvValue_Type = DisplayString
_JnxSyslogAvValue_Object = MibTableColumn
jnxSyslogAvValue = _JnxSyslogAvValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 3),
    _JnxSyslogAvValue_Type()
)
jnxSyslogAvValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogAvValue.setStatus("current")
_JnxSyslogNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxSyslogNotificationPrefix = _JnxSyslogNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0)
)
if mibBuilder.loadTexts:
    jnxSyslogNotificationPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 1)
)
jnxSyslogTrap.setObjects(
      *(("JUNIPER-SYSLOG-MIB", "jnxSyslogEventName"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogTimestamp"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogSeverity"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogFacility"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogProcessId"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogProcessName"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogHostName"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogMessage"))
)
if mibBuilder.loadTexts:
    jnxSyslogTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SYSLOG-MIB",
    **{"JnxSyslogSeverity": JnxSyslogSeverity,
       "JnxSyslogFacility": JnxSyslogFacility,
       "jnxSyslog": jnxSyslog,
       "jnxSyslogNotifyVars": jnxSyslogNotifyVars,
       "jnxSyslogTable": jnxSyslogTable,
       "jnxSyslogEntry": jnxSyslogEntry,
       "jnxSyslogId": jnxSyslogId,
       "jnxSyslogEventName": jnxSyslogEventName,
       "jnxSyslogTimestamp": jnxSyslogTimestamp,
       "jnxSyslogSeverity": jnxSyslogSeverity,
       "jnxSyslogFacility": jnxSyslogFacility,
       "jnxSyslogProcessId": jnxSyslogProcessId,
       "jnxSyslogProcessName": jnxSyslogProcessName,
       "jnxSyslogHostName": jnxSyslogHostName,
       "jnxSyslogMessage": jnxSyslogMessage,
       "jnxSyslogAvTable": jnxSyslogAvTable,
       "jnxSyslogAvEntry": jnxSyslogAvEntry,
       "jnxSyslogAvIndex": jnxSyslogAvIndex,
       "jnxSyslogAvAttribute": jnxSyslogAvAttribute,
       "jnxSyslogAvValue": jnxSyslogAvValue,
       "jnxSyslogNotificationPrefix": jnxSyslogNotificationPrefix,
       "jnxSyslogTrap": jnxSyslogTrap}
)
