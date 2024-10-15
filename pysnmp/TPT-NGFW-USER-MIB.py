# SNMP MIB module (TPT-NGFW-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-NGFW-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:04 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(tpt_ngfw_compls,
 tpt_ngfw_eventsV2,
 tpt_ngfw_groups,
 tpt_ngfw_objs,
 tpt_ngfw_params,
 tptNgfwNotifySeverity) = mibBuilder.importSymbols(
    "TPT-NGFW-REG-MIB",
    "tpt-ngfw-compls",
    "tpt-ngfw-eventsV2",
    "tpt-ngfw-groups",
    "tpt-ngfw-objs",
    "tpt-ngfw-params",
    "tptNgfwNotifySeverity")

(tptNgfwSystemSerial,) = mibBuilder.importSymbols(
    "TPT-NGFW-SYSTEM-INFO-MIB",
    "tptNgfwSystemSerial")


# MODULE-IDENTITY

tptNgfwPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 4)
)
tptNgfwPolicy.setRevisions(
        ("2016-05-25 18:54",
         "2013-04-03 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _TptNgfwUserAuthName_Type(SnmpAdminString):
    """Custom type tptNgfwUserAuthName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptNgfwUserAuthName_Type.__name__ = "SnmpAdminString"
_TptNgfwUserAuthName_Object = MibScalar
tptNgfwUserAuthName = _TptNgfwUserAuthName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 73),
    _TptNgfwUserAuthName_Type()
)
tptNgfwUserAuthName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwUserAuthName.setStatus("current")


class _TptNgfwUserAuthFailNotifyReason_Type(SnmpAdminString):
    """Custom type tptNgfwUserAuthFailNotifyReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptNgfwUserAuthFailNotifyReason_Type.__name__ = "SnmpAdminString"
_TptNgfwUserAuthFailNotifyReason_Object = MibScalar
tptNgfwUserAuthFailNotifyReason = _TptNgfwUserAuthFailNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 74),
    _TptNgfwUserAuthFailNotifyReason_Type()
)
tptNgfwUserAuthFailNotifyReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwUserAuthFailNotifyReason.setStatus("current")
_TptNgfwUserAuthSrcIpAddrType_Type = InetAddressType
_TptNgfwUserAuthSrcIpAddrType_Object = MibScalar
tptNgfwUserAuthSrcIpAddrType = _TptNgfwUserAuthSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 75),
    _TptNgfwUserAuthSrcIpAddrType_Type()
)
tptNgfwUserAuthSrcIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwUserAuthSrcIpAddrType.setStatus("current")
_TptNgfwUserAuthSrcIpAddr_Type = InetAddress
_TptNgfwUserAuthSrcIpAddr_Object = MibScalar
tptNgfwUserAuthSrcIpAddr = _TptNgfwUserAuthSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 76),
    _TptNgfwUserAuthSrcIpAddr_Type()
)
tptNgfwUserAuthSrcIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwUserAuthSrcIpAddr.setStatus("current")


class _TptNgfwUserAuthNotifySource_Type(SnmpAdminString):
    """Custom type tptNgfwUserAuthNotifySource based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptNgfwUserAuthNotifySource_Type.__name__ = "SnmpAdminString"
_TptNgfwUserAuthNotifySource_Object = MibScalar
tptNgfwUserAuthNotifySource = _TptNgfwUserAuthNotifySource_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 77),
    _TptNgfwUserAuthNotifySource_Type()
)
tptNgfwUserAuthNotifySource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwUserAuthNotifySource.setStatus("current")
_TptNgfwUserAuthLockedTime_Type = DateAndTime
_TptNgfwUserAuthLockedTime_Object = MibScalar
tptNgfwUserAuthLockedTime = _TptNgfwUserAuthLockedTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 78),
    _TptNgfwUserAuthLockedTime_Type()
)
tptNgfwUserAuthLockedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwUserAuthLockedTime.setStatus("current")

# Managed Objects groups

tptNgfwUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 11)
)
tptNgfwUserGroup.setObjects(
      *(("TPT-NGFW-USER-MIB", "tptNgfwUserAuthName"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthFailNotifyReason"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddrType"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddr"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthNotifySource"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedTime"))
)
if mibBuilder.loadTexts:
    tptNgfwUserGroup.setStatus("current")


# Notification objects

tptNgfwUserAuthFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 18)
)
tptNgfwUserAuthFailNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthName"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthFailNotifyReason"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddrType"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddr"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthNotifySource"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwUserAuthFailNotify.setStatus(
        "current"
    )

tptNgfwUserAuthLockedAccountNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 19)
)
tptNgfwUserAuthLockedAccountNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthName"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddrType"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddr"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedTime"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthNotifySource"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwUserAuthLockedAccountNotify.setStatus(
        "current"
    )

tptNgfwUserAuthLockedIpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 20)
)
tptNgfwUserAuthLockedIpNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddrType"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddr"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedTime"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwUserAuthLockedIpNotify.setStatus(
        "current"
    )


# Notifications groups

tptNgfwUserNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 12)
)
tptNgfwUserNotificationGroup.setObjects(
      *(("TPT-NGFW-USER-MIB", "tptNgfwUserAuthFailNotify"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedAccountNotify"),
        ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedIpNotify"))
)
if mibBuilder.loadTexts:
    tptNgfwUserNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tptNgfwUserCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tptNgfwUserCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-NGFW-USER-MIB",
    **{"tptNgfwUserGroup": tptNgfwUserGroup,
       "tptNgfwUserNotificationGroup": tptNgfwUserNotificationGroup,
       "tptNgfwUserCompl": tptNgfwUserCompl,
       "tptNgfwPolicy": tptNgfwPolicy,
       "tptNgfwUserAuthFailNotify": tptNgfwUserAuthFailNotify,
       "tptNgfwUserAuthLockedAccountNotify": tptNgfwUserAuthLockedAccountNotify,
       "tptNgfwUserAuthLockedIpNotify": tptNgfwUserAuthLockedIpNotify,
       "tptNgfwUserAuthName": tptNgfwUserAuthName,
       "tptNgfwUserAuthFailNotifyReason": tptNgfwUserAuthFailNotifyReason,
       "tptNgfwUserAuthSrcIpAddrType": tptNgfwUserAuthSrcIpAddrType,
       "tptNgfwUserAuthSrcIpAddr": tptNgfwUserAuthSrcIpAddr,
       "tptNgfwUserAuthNotifySource": tptNgfwUserAuthNotifySource,
       "tptNgfwUserAuthLockedTime": tptNgfwUserAuthLockedTime}
)
