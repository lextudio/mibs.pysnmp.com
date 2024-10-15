# SNMP MIB module (BLUECOAT-SG-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-SG-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:21 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

devicePolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 6)
)
devicePolicyMIB.setRevisions(
        ("2007-11-05 03:00",
         "2002-08-28 03:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PolicyMessageString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_DevicePolicyMIBObjects_ObjectIdentity = ObjectIdentity
devicePolicyMIBObjects = _DevicePolicyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 6, 1)
)
_DevicePolicyValues_ObjectIdentity = ObjectIdentity
devicePolicyValues = _DevicePolicyValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 6, 1, 1)
)
_DevicePolicyMessage_Type = PolicyMessageString
_DevicePolicyMessage_Object = MibScalar
devicePolicyMessage = _DevicePolicyMessage_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 6, 1, 1, 1),
    _DevicePolicyMessage_Type()
)
devicePolicyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    devicePolicyMessage.setStatus("current")
_DevicePolicyMIBNotifications_ObjectIdentity = ObjectIdentity
devicePolicyMIBNotifications = _DevicePolicyMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 6, 2)
)
_DevicePolicyMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
devicePolicyMIBNotificationsPrefix = _DevicePolicyMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 6, 2, 0)
)

# Managed Objects groups


# Notification objects

devicePolicyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 6, 2, 0, 1)
)
devicePolicyTrap.setObjects(
    ("BLUECOAT-SG-POLICY-MIB", "devicePolicyMessage")
)
if mibBuilder.loadTexts:
    devicePolicyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-POLICY-MIB",
    **{"PolicyMessageString": PolicyMessageString,
       "devicePolicyMIB": devicePolicyMIB,
       "devicePolicyMIBObjects": devicePolicyMIBObjects,
       "devicePolicyValues": devicePolicyValues,
       "devicePolicyMessage": devicePolicyMessage,
       "devicePolicyMIBNotifications": devicePolicyMIBNotifications,
       "devicePolicyMIBNotificationsPrefix": devicePolicyMIBNotificationsPrefix,
       "devicePolicyTrap": devicePolicyTrap}
)
