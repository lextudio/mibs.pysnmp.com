# SNMP MIB module (RBTWS-REGISTRATION-DEVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:37 2024
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

(rbtwsRegistration,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsRegistration")

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

rbtwsRegistrationDevicesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 6)
)
rbtwsRegistrationDevicesMib.setRevisions(
        ("2007-08-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbtwsWirelessSwitch_ObjectIdentity = ObjectIdentity
rbtwsWirelessSwitch = _RbtwsWirelessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1)
)
_RbtwsSwitch8100_ObjectIdentity = ObjectIdentity
rbtwsSwitch8100 = _RbtwsSwitch8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 1)
)
_RbtwsSwitch8200_ObjectIdentity = ObjectIdentity
rbtwsSwitch8200 = _RbtwsSwitch8200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 2)
)
_RbtwsSwitch8400_ObjectIdentity = ObjectIdentity
rbtwsSwitch8400 = _RbtwsSwitch8400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 3)
)
_RbtwsSwitch8110_ObjectIdentity = ObjectIdentity
rbtwsSwitch8110 = _RbtwsSwitch8110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 4)
)
_RbtwsSwitch8500_ObjectIdentity = ObjectIdentity
rbtwsSwitch8500 = _RbtwsSwitch8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-REGISTRATION-DEVICES-MIB",
    **{"rbtwsWirelessSwitch": rbtwsWirelessSwitch,
       "rbtwsSwitch8100": rbtwsSwitch8100,
       "rbtwsSwitch8200": rbtwsSwitch8200,
       "rbtwsSwitch8400": rbtwsSwitch8400,
       "rbtwsSwitch8110": rbtwsSwitch8110,
       "rbtwsSwitch8500": rbtwsSwitch8500,
       "rbtwsRegistrationDevicesMib": rbtwsRegistrationDevicesMib}
)
