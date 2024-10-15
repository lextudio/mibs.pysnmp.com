# SNMP MIB module (RTBRICK-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RTBRICK-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:33 2024
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

(rtbrickModules,
 rtbrickSyslogNotifications,
 rtbrickTraps) = mibBuilder.importSymbols(
    "RTBRICK-MIB",
    "rtbrickModules",
    "rtbrickSyslogNotifications",
    "rtbrickTraps")

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

rtBrickSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2)
)
rtBrickSyslogMIB.setRevisions(
        ("2019-01-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogSeverity(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_RtbrickSyslogNotificationPrefix_ObjectIdentity = ObjectIdentity
rtbrickSyslogNotificationPrefix = _RtbrickSyslogNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 103, 1, 0)
)
if mibBuilder.loadTexts:
    rtbrickSyslogNotificationPrefix.setStatus("current")
_SyslogMessage_ObjectIdentity = ObjectIdentity
syslogMessage = _SyslogMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1)
)
_SyslogMsgNumber_Type = Unsigned32
_SyslogMsgNumber_Object = MibScalar
syslogMsgNumber = _SyslogMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 1),
    _SyslogMsgNumber_Type()
)
syslogMsgNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgNumber.setStatus("current")
_SyslogMsgFacility_Type = DisplayString
_SyslogMsgFacility_Object = MibScalar
syslogMsgFacility = _SyslogMsgFacility_Object(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 2),
    _SyslogMsgFacility_Type()
)
syslogMsgFacility.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgFacility.setStatus("current")
_SyslogMsgSeverity_Type = SyslogSeverity
_SyslogMsgSeverity_Object = MibScalar
syslogMsgSeverity = _SyslogMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 3),
    _SyslogMsgSeverity_Type()
)
syslogMsgSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgSeverity.setStatus("current")
_SyslogMsgText_Type = DisplayString
_SyslogMsgText_Object = MibScalar
syslogMsgText = _SyslogMsgText_Object(
    (1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 4),
    _SyslogMsgText_Type()
)
syslogMsgText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgText.setStatus("current")

# Managed Objects groups


# Notification objects

rtbrickSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50058, 103, 1, 0, 1)
)
if mibBuilder.loadTexts:
    rtbrickSyslogTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RTBRICK-SYSLOG-MIB",
    **{"SyslogSeverity": SyslogSeverity,
       "rtbrickSyslogNotificationPrefix": rtbrickSyslogNotificationPrefix,
       "rtbrickSyslogTrap": rtbrickSyslogTrap,
       "rtBrickSyslogMIB": rtBrickSyslogMIB,
       "syslogMessage": syslogMessage,
       "syslogMsgNumber": syslogMsgNumber,
       "syslogMsgFacility": syslogMsgFacility,
       "syslogMsgSeverity": syslogMsgSeverity,
       "syslogMsgText": syslogMsgText}
)
