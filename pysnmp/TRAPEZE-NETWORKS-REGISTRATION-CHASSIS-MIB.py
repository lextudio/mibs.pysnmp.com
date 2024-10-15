# SNMP MIB module (TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:35 2024
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

(trpzRegistration,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzRegistration")


# MODULE-IDENTITY

trpzRegistrationChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 5)
)
trpzRegistrationChassisMib.setRevisions(
        ("2007-08-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrpzChassisComponents_ObjectIdentity = ObjectIdentity
trpzChassisComponents = _TrpzChassisComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4)
)
_TrpzChasCompPowerSupplies_ObjectIdentity = ObjectIdentity
trpzChasCompPowerSupplies = _TrpzChasCompPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 1)
)
_TrpzChasCompPowerSupply1_ObjectIdentity = ObjectIdentity
trpzChasCompPowerSupply1 = _TrpzChasCompPowerSupply1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 1)
)
_TrpzChasCompPowerSupply2_ObjectIdentity = ObjectIdentity
trpzChasCompPowerSupply2 = _TrpzChasCompPowerSupply2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 2)
)
_TrpzChasCompFans_ObjectIdentity = ObjectIdentity
trpzChasCompFans = _TrpzChasCompFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 2)
)
_TrpzChasCompFan1_ObjectIdentity = ObjectIdentity
trpzChasCompFan1 = _TrpzChasCompFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 1)
)
_TrpzChasCompFan2_ObjectIdentity = ObjectIdentity
trpzChasCompFan2 = _TrpzChasCompFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 2)
)
_TrpzChasCompFan3_ObjectIdentity = ObjectIdentity
trpzChasCompFan3 = _TrpzChasCompFan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB",
    **{"trpzChassisComponents": trpzChassisComponents,
       "trpzChasCompPowerSupplies": trpzChasCompPowerSupplies,
       "trpzChasCompPowerSupply1": trpzChasCompPowerSupply1,
       "trpzChasCompPowerSupply2": trpzChasCompPowerSupply2,
       "trpzChasCompFans": trpzChasCompFans,
       "trpzChasCompFan1": trpzChasCompFan1,
       "trpzChasCompFan2": trpzChasCompFan2,
       "trpzChasCompFan3": trpzChasCompFan3,
       "trpzRegistrationChassisMib": trpzRegistrationChassisMib}
)
