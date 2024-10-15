# SNMP MIB module (OPENBSD-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPENBSD-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:17 2024
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

openBSD = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30155)
)
openBSD.setRevisions(
        ("2012-01-31 00:00",
         "2008-12-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PfMIBObjects_ObjectIdentity = ObjectIdentity
pfMIBObjects = _PfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1)
)
_SensorsMIBObjects_ObjectIdentity = ObjectIdentity
sensorsMIBObjects = _SensorsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 2)
)
_MemMIBObjects_ObjectIdentity = ObjectIdentity
memMIBObjects = _MemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 5)
)
_CarpMIBObjects_ObjectIdentity = ObjectIdentity
carpMIBObjects = _CarpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 6)
)
_LocalSystem_ObjectIdentity = ObjectIdentity
localSystem = _LocalSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 23)
)
_OpenBSDDefaultObjectID_ObjectIdentity = ObjectIdentity
openBSDDefaultObjectID = _OpenBSDDefaultObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 23, 1)
)
_LocalTest_ObjectIdentity = ObjectIdentity
localTest = _LocalTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 42)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPENBSD-BASE-MIB",
    **{"openBSD": openBSD,
       "pfMIBObjects": pfMIBObjects,
       "sensorsMIBObjects": sensorsMIBObjects,
       "memMIBObjects": memMIBObjects,
       "carpMIBObjects": carpMIBObjects,
       "localSystem": localSystem,
       "openBSDDefaultObjectID": openBSDDefaultObjectID,
       "localTest": localTest}
)
