# SNMP MIB module (RBTWS-REGISTRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-REGISTRATION-MIB
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

rbtwsRegistrationMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 3)
)
rbtwsRegistrationMib.setRevisions(
        ("2006-05-22 00:08",
         "2005-01-01 00:00")
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
_RbtwsChassisComponents_ObjectIdentity = ObjectIdentity
rbtwsChassisComponents = _RbtwsChassisComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4)
)
_RbtwsChasCompPowerSupplies_ObjectIdentity = ObjectIdentity
rbtwsChasCompPowerSupplies = _RbtwsChasCompPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1)
)
_RbtwsChasCompPowerSupply1_ObjectIdentity = ObjectIdentity
rbtwsChasCompPowerSupply1 = _RbtwsChasCompPowerSupply1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 1)
)
_RbtwsChasCompPowerSupply2_ObjectIdentity = ObjectIdentity
rbtwsChasCompPowerSupply2 = _RbtwsChasCompPowerSupply2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 2)
)
_RbtwsChasCompFans_ObjectIdentity = ObjectIdentity
rbtwsChasCompFans = _RbtwsChasCompFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2)
)
_RbtwsChasCompFan1_ObjectIdentity = ObjectIdentity
rbtwsChasCompFan1 = _RbtwsChasCompFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 1)
)
_RbtwsChasCompFan2_ObjectIdentity = ObjectIdentity
rbtwsChasCompFan2 = _RbtwsChasCompFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 2)
)
_RbtwsChasCompFan3_ObjectIdentity = ObjectIdentity
rbtwsChasCompFan3 = _RbtwsChasCompFan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-REGISTRATION-MIB",
    **{"rbtwsWirelessSwitch": rbtwsWirelessSwitch,
       "rbtwsSwitch8100": rbtwsSwitch8100,
       "rbtwsSwitch8200": rbtwsSwitch8200,
       "rbtwsSwitch8400": rbtwsSwitch8400,
       "rbtwsRegistrationMib": rbtwsRegistrationMib,
       "rbtwsChassisComponents": rbtwsChassisComponents,
       "rbtwsChasCompPowerSupplies": rbtwsChasCompPowerSupplies,
       "rbtwsChasCompPowerSupply1": rbtwsChasCompPowerSupply1,
       "rbtwsChasCompPowerSupply2": rbtwsChasCompPowerSupply2,
       "rbtwsChasCompFans": rbtwsChasCompFans,
       "rbtwsChasCompFan1": rbtwsChasCompFan1,
       "rbtwsChasCompFan2": rbtwsChasCompFan2,
       "rbtwsChasCompFan3": rbtwsChasCompFan3}
)
