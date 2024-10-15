# SNMP MIB module (NTWS-REGISTRATION-DEVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:59 2024
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

(ntwsRegistration,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsRegistration")

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

ntwsRegistrationDevicesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 6)
)
ntwsRegistrationDevicesMib.setRevisions(
        ("2008-08-08 00:01",
         "2007-08-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtwsWirelessSwitch_ObjectIdentity = ObjectIdentity
ntwsWirelessSwitch = _NtwsWirelessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1)
)
_NtwsSwitch2360_ObjectIdentity = ObjectIdentity
ntwsSwitch2360 = _NtwsSwitch2360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 2)
)
_NtwsSwitch2380_ObjectIdentity = ObjectIdentity
ntwsSwitch2380 = _NtwsSwitch2380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 3)
)
_NtwsSwitch2350_ObjectIdentity = ObjectIdentity
ntwsSwitch2350 = _NtwsSwitch2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 4)
)
_NtwsSwitch2372_ObjectIdentity = ObjectIdentity
ntwsSwitch2372 = _NtwsSwitch2372_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 5)
)
_NtwsSwitch2382_ObjectIdentity = ObjectIdentity
ntwsSwitch2382 = _NtwsSwitch2382_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 6)
)
_NtwsSwitch2800_ObjectIdentity = ObjectIdentity
ntwsSwitch2800 = _NtwsSwitch2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-REGISTRATION-DEVICES-MIB",
    **{"ntwsWirelessSwitch": ntwsWirelessSwitch,
       "ntwsSwitch2360": ntwsSwitch2360,
       "ntwsSwitch2380": ntwsSwitch2380,
       "ntwsSwitch2350": ntwsSwitch2350,
       "ntwsSwitch2372": ntwsSwitch2372,
       "ntwsSwitch2382": ntwsSwitch2382,
       "ntwsSwitch2800": ntwsSwitch2800,
       "ntwsRegistrationDevicesMib": ntwsRegistrationDevicesMib}
)
