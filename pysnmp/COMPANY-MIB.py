# SNMP MIB module (COMPANY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMPANY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:46 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

allotCom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2603)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NeTraps_ObjectIdentity = ObjectIdentity
neTraps = _NeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 2)
)

# Managed Objects groups


# Notification objects

nePrimaryActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 2, 11)
)
if mibBuilder.loadTexts:
    nePrimaryActive.setStatus(
        "current"
    )

nePrimaryBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 2, 12)
)
if mibBuilder.loadTexts:
    nePrimaryBypass.setStatus(
        "current"
    )

neSecondaryActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 2, 13)
)
if mibBuilder.loadTexts:
    neSecondaryActive.setStatus(
        "current"
    )

neSecondaryStandBy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 2, 14)
)
if mibBuilder.loadTexts:
    neSecondaryStandBy.setStatus(
        "current"
    )

neSecondaryBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 2, 15)
)
if mibBuilder.loadTexts:
    neSecondaryBypass.setStatus(
        "current"
    )

collTableOverFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 2, 21)
)
if mibBuilder.loadTexts:
    collTableOverFlow.setStatus(
        "current"
    )

neAlertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 2, 22)
)
if mibBuilder.loadTexts:
    neAlertEvent.setStatus(
        "current"
    )


# Notifications groups

neNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2603, 3)
)
neNotificationsGroup.setObjects(
      *(("COMPANY-MIB", "nePrimaryActive"),
        ("COMPANY-MIB", "nePrimaryBypass"),
        ("COMPANY-MIB", "neSecondaryActive"),
        ("COMPANY-MIB", "neSecondaryStandBy"),
        ("COMPANY-MIB", "neSecondaryBypass"),
        ("COMPANY-MIB", "collTableOverFlow"),
        ("COMPANY-MIB", "neAlertEvent"))
)
if mibBuilder.loadTexts:
    neNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMPANY-MIB",
    **{"allotCom": allotCom,
       "neTraps": neTraps,
       "nePrimaryActive": nePrimaryActive,
       "nePrimaryBypass": nePrimaryBypass,
       "neSecondaryActive": neSecondaryActive,
       "neSecondaryStandBy": neSecondaryStandBy,
       "neSecondaryBypass": neSecondaryBypass,
       "collTableOverFlow": collTableOverFlow,
       "neAlertEvent": neAlertEvent,
       "neNotificationsGroup": neNotificationsGroup}
)
