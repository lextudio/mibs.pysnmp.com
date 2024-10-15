# SNMP MIB module (ADTRAN-AOS-SIP-REGISTRATION) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-SIP-REGISTRATION
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:15 2024
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

(adGenAOSConformance,
 adGenAOSVoice) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSVoice")

(adIdentityShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenAOSSipRegistration = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 4)
)
adGenAOSSipRegistration.setRevisions(
        ("2010-11-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdSipRegistration_ObjectIdentity = ObjectIdentity
adSipRegistration = _AdSipRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4)
)
_AdSipRegistrationTraps_ObjectIdentity = ObjectIdentity
adSipRegistrationTraps = _AdSipRegistrationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0)
)
_AdSipTrunkRegistrationAlarmTrunkIdentity_Type = DisplayString
_AdSipTrunkRegistrationAlarmTrunkIdentity_Object = MibScalar
adSipTrunkRegistrationAlarmTrunkIdentity = _AdSipTrunkRegistrationAlarmTrunkIdentity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 1),
    _AdSipTrunkRegistrationAlarmTrunkIdentity_Type()
)
adSipTrunkRegistrationAlarmTrunkIdentity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarmTrunkIdentity.setStatus("current")
_AdSipTrunkRegistrationAlarmSipIdentity_Type = DisplayString
_AdSipTrunkRegistrationAlarmSipIdentity_Object = MibScalar
adSipTrunkRegistrationAlarmSipIdentity = _AdSipTrunkRegistrationAlarmSipIdentity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 2),
    _AdSipTrunkRegistrationAlarmSipIdentity_Type()
)
adSipTrunkRegistrationAlarmSipIdentity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarmSipIdentity.setStatus("current")
_AdSipTrunkRegistrationAlarmRegistrar_Type = IpAddress
_AdSipTrunkRegistrationAlarmRegistrar_Object = MibScalar
adSipTrunkRegistrationAlarmRegistrar = _AdSipTrunkRegistrationAlarmRegistrar_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 3),
    _AdSipTrunkRegistrationAlarmRegistrar_Type()
)
adSipTrunkRegistrationAlarmRegistrar.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarmRegistrar.setStatus("current")
_AdSipTrunkRegistrationAlarmTimestamp_Type = Unsigned32
_AdSipTrunkRegistrationAlarmTimestamp_Object = MibScalar
adSipTrunkRegistrationAlarmTimestamp = _AdSipTrunkRegistrationAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 4),
    _AdSipTrunkRegistrationAlarmTimestamp_Type()
)
adSipTrunkRegistrationAlarmTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarmTimestamp.setStatus("current")
_AdSipRegistrationConformance_ObjectIdentity = ObjectIdentity
adSipRegistrationConformance = _AdSipRegistrationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12)
)
_AdSipRegistrationGroups_ObjectIdentity = ObjectIdentity
adSipRegistrationGroups = _AdSipRegistrationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1)
)
_AdSipRegistrationCompliances_ObjectIdentity = ObjectIdentity
adSipRegistrationCompliances = _AdSipRegistrationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2)
)

# Managed Objects groups

adSipRegistrationNotificationUtilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 2)
)
adSipRegistrationNotificationUtilityGroup.setObjects(
      *(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
)
if mibBuilder.loadTexts:
    adSipRegistrationNotificationUtilityGroup.setStatus("current")


# Notification objects

adSipTrunkRegistrationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0, 1)
)
adSipTrunkRegistrationAlarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
)
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarm.setStatus(
        "current"
    )


# Notifications groups

adSipRegistrationNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 1)
)
adSipRegistrationNotificationGroup.setObjects(
    ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarm")
)
if mibBuilder.loadTexts:
    adSipRegistrationNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adSipRegistrationFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2, 1)
)
if mibBuilder.loadTexts:
    adSipRegistrationFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-SIP-REGISTRATION",
    **{"adSipRegistration": adSipRegistration,
       "adSipRegistrationTraps": adSipRegistrationTraps,
       "adSipTrunkRegistrationAlarm": adSipTrunkRegistrationAlarm,
       "adSipTrunkRegistrationAlarmTrunkIdentity": adSipTrunkRegistrationAlarmTrunkIdentity,
       "adSipTrunkRegistrationAlarmSipIdentity": adSipTrunkRegistrationAlarmSipIdentity,
       "adSipTrunkRegistrationAlarmRegistrar": adSipTrunkRegistrationAlarmRegistrar,
       "adSipTrunkRegistrationAlarmTimestamp": adSipTrunkRegistrationAlarmTimestamp,
       "adSipRegistrationConformance": adSipRegistrationConformance,
       "adSipRegistrationGroups": adSipRegistrationGroups,
       "adSipRegistrationNotificationGroup": adSipRegistrationNotificationGroup,
       "adSipRegistrationNotificationUtilityGroup": adSipRegistrationNotificationUtilityGroup,
       "adSipRegistrationCompliances": adSipRegistrationCompliances,
       "adSipRegistrationFullCompliance": adSipRegistrationFullCompliance,
       "adGenAOSSipRegistration": adGenAOSSipRegistration}
)
