# SNMP MIB module (CADANT-CMTS-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:40 2024
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

(trapCounter,
 trapSeverity) = mibBuilder.importSymbols(
    "CADANT-CMTS-EQUIPMENT-MIB",
    "trapCounter",
    "trapSeverity")

(cadNotification,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadNotification")

(ifAdminStatus,
 ifDescr,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex",
    "ifOperStatus")

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

cadNotificationMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1)
)
cadNotificationMib.setRevisions(
        ("2015-09-14 00:00",
         "2006-05-03 00:00",
         "2005-09-28 00:00",
         "2003-03-26 00:00",
         "2002-07-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadTrapMibObjects_ObjectIdentity = ObjectIdentity
cadTrapMibObjects = _CadTrapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1)
)
_CadTraps_ObjectIdentity = ObjectIdentity
cadTraps = _CadTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0)
)
_CadTrapsInfo_ObjectIdentity = ObjectIdentity
cadTrapsInfo = _CadTrapsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 1)
)
_SecurityInfo_Type = DisplayString
_SecurityInfo_Object = MibScalar
securityInfo = _SecurityInfo_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 1, 1),
    _SecurityInfo_Type()
)
securityInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    securityInfo.setStatus("current")
_IpdrInfo_Type = DisplayString
_IpdrInfo_Object = MibScalar
ipdrInfo = _IpdrInfo_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 1, 2),
    _IpdrInfo_Type()
)
ipdrInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipdrInfo.setStatus("current")

# Managed Objects groups


# Notification objects

aaaServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 1)
)
aaaServerUnreachableTrap.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
)
if mibBuilder.loadTexts:
    aaaServerUnreachableTrap.setStatus(
        "current"
    )

aaaServerGroupUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 2)
)
aaaServerGroupUnreachableTrap.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
)
if mibBuilder.loadTexts:
    aaaServerGroupUnreachableTrap.setStatus(
        "current"
    )

aaaServerAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 3)
)
aaaServerAuthFailTrap.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
)
if mibBuilder.loadTexts:
    aaaServerAuthFailTrap.setStatus(
        "current"
    )

secuLocalAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 4)
)
secuLocalAuthFailTrap.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
)
if mibBuilder.loadTexts:
    secuLocalAuthFailTrap.setStatus(
        "current"
    )

secuLineAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 5)
)
secuLineAuthFailTrap.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
)
if mibBuilder.loadTexts:
    secuLineAuthFailTrap.setStatus(
        "current"
    )

rip2AuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 6)
)
rip2AuthFailTrap.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
)
if mibBuilder.loadTexts:
    rip2AuthFailTrap.setStatus(
        "current"
    )

cadIpdrNoPrimaryCollector = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 7)
)
cadIpdrNoPrimaryCollector.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "ipdrInfo"))
)
if mibBuilder.loadTexts:
    cadIpdrNoPrimaryCollector.setStatus(
        "current"
    )

cadIpdrStreamingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 8)
)
cadIpdrStreamingDisabled.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "ipdrInfo"))
)
if mibBuilder.loadTexts:
    cadIpdrStreamingDisabled.setStatus(
        "current"
    )

cadIpdrReportCycleMissed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 9)
)
cadIpdrReportCycleMissed.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-NOTIFICATION-MIB", "ipdrInfo"))
)
if mibBuilder.loadTexts:
    cadIpdrReportCycleMissed.setStatus(
        "current"
    )

cadLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 10)
)
cadLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    cadLinkUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-NOTIFICATION-MIB",
    **{"cadNotificationMib": cadNotificationMib,
       "cadTrapMibObjects": cadTrapMibObjects,
       "cadTraps": cadTraps,
       "aaaServerUnreachableTrap": aaaServerUnreachableTrap,
       "aaaServerGroupUnreachableTrap": aaaServerGroupUnreachableTrap,
       "aaaServerAuthFailTrap": aaaServerAuthFailTrap,
       "secuLocalAuthFailTrap": secuLocalAuthFailTrap,
       "secuLineAuthFailTrap": secuLineAuthFailTrap,
       "rip2AuthFailTrap": rip2AuthFailTrap,
       "cadIpdrNoPrimaryCollector": cadIpdrNoPrimaryCollector,
       "cadIpdrStreamingDisabled": cadIpdrStreamingDisabled,
       "cadIpdrReportCycleMissed": cadIpdrReportCycleMissed,
       "cadLinkUp": cadLinkUp,
       "cadTrapsInfo": cadTrapsInfo,
       "securityInfo": securityInfo,
       "ipdrInfo": ipdrInfo}
)
