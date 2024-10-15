# SNMP MIB module (SPIDCOM-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SPIDCOM-TRAPS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:22 2024
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

(plcBasePortIndex,) = mibBuilder.importSymbols(
    "SPC200",
    "plcBasePortIndex")

(ItuAlarmProbableCause,
 ItuAlarmType,
 neAlarmActivePhoto) = mibBuilder.importSymbols(
    "SPIDCOM-ALARM-MIB",
    "ItuAlarmProbableCause",
    "ItuAlarmType",
    "neAlarmActivePhoto")

(specificSpidcomTrap,) = mibBuilder.importSymbols(
    "SPIDCOM-NOTIFICATION-MIB",
    "specificSpidcomTrap")


# MODULE-IDENTITY

trapsDefinition = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

deviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 1)
)
if mibBuilder.loadTexts:
    deviceDown.setStatus(
        "current"
    )

deviceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 2)
)
if mibBuilder.loadTexts:
    deviceUp.setStatus(
        "current"
    )

maxAttenuation = NotificationType(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 3)
)
if mibBuilder.loadTexts:
    maxAttenuation.setStatus(
        "current"
    )

maxNoise = NotificationType(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 4)
)
if mibBuilder.loadTexts:
    maxNoise.setStatus(
        "current"
    )


# Notifications groups

linkUpDownNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 11)
)
linkUpDownNotificationsGroup.setObjects(
      *(("SPIDCOM-TRAPS", "deviceUp"),
        ("SPIDCOM-TRAPS", "deviceDown"))
)
if mibBuilder.loadTexts:
    linkUpDownNotificationsGroup.setStatus(
        "current"
    )

maxAttenuationNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 12)
)
maxAttenuationNotificationsGroup.setObjects(
    ("SPIDCOM-TRAPS", "maxAttenuation")
)
if mibBuilder.loadTexts:
    maxAttenuationNotificationsGroup.setStatus(
        "current"
    )

maxNoiseNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 13)
)
maxNoiseNotificationsGroup.setObjects(
    ("SPIDCOM-TRAPS", "maxNoise")
)
if mibBuilder.loadTexts:
    maxNoiseNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPIDCOM-TRAPS",
    **{"trapsDefinition": trapsDefinition,
       "deviceDown": deviceDown,
       "deviceUp": deviceUp,
       "maxAttenuation": maxAttenuation,
       "maxNoise": maxNoise,
       "linkUpDownNotificationsGroup": linkUpDownNotificationsGroup,
       "maxAttenuationNotificationsGroup": maxAttenuationNotificationsGroup,
       "maxNoiseNotificationsGroup": maxNoiseNotificationsGroup}
)
