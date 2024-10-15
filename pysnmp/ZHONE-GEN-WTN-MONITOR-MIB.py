# SNMP MIB module (ZHONE-GEN-WTN-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-GEN-WTN-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:34 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(zhoneGenWtn,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneGenWtn",
    "zhoneModules")


# MODULE-IDENTITY

zhoneGenWtnMonitorModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 102)
)
zhoneGenWtnMonitorModule.setRevisions(
        ("1901-05-25 21:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WtnMonitor_ObjectIdentity = ObjectIdentity
wtnMonitor = _WtnMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 9, 1)
)
if mibBuilder.loadTexts:
    wtnMonitor.setStatus("current")


class _WtnLedStatus_Type(Bits):
    """Custom type wtnLedStatus based on Bits"""
    namedValues = NamedValues(
        *(("diag", 0),
          ("lineInterface", 2),
          ("local", 4),
          ("operational", 1),
          ("radio", 3),
          ("remote", 5))
    )

_WtnLedStatus_Type.__name__ = "Bits"
_WtnLedStatus_Object = MibScalar
wtnLedStatus = _WtnLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 9, 1, 1),
    _WtnLedStatus_Type()
)
wtnLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnLedStatus.setStatus("current")


class _WtnAlarmStatus_Type(Bits):
    """Custom type wtnAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("criticalAlarm", 1),
          ("minorAlarm", 0))
    )

_WtnAlarmStatus_Type.__name__ = "Bits"
_WtnAlarmStatus_Object = MibScalar
wtnAlarmStatus = _WtnAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 9, 1, 2),
    _WtnAlarmStatus_Type()
)
wtnAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtnAlarmStatus.setStatus("current")
_RadioLinkConfiguration_ObjectIdentity = ObjectIdentity
radioLinkConfiguration = _RadioLinkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 9, 2)
)
if mibBuilder.loadTexts:
    radioLinkConfiguration.setStatus("current")
_WtnLinkName_Type = SnmpAdminString
_WtnLinkName_Object = MibScalar
wtnLinkName = _WtnLinkName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 9, 2, 1),
    _WtnLinkName_Type()
)
wtnLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtnLinkName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-GEN-WTN-MONITOR-MIB",
    **{"wtnMonitor": wtnMonitor,
       "wtnLedStatus": wtnLedStatus,
       "wtnAlarmStatus": wtnAlarmStatus,
       "radioLinkConfiguration": radioLinkConfiguration,
       "wtnLinkName": wtnLinkName,
       "zhoneGenWtnMonitorModule": zhoneGenWtnMonitorModule}
)
