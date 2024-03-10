"""SNMP MIB module (AISYSCFG-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISYSCFG-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 01:53:51 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(enterprises,
 Unsigned32,
 Integer32,
 ModuleIdentity,
 iso,
 Gauge32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 IpAddress,
 ObjectIdentity,
 Counter64,
 MibIdentifier,
 TimeTicks,
 Bits,
 NotificationType,
 Counter32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "enterprises",
    "Unsigned32",
    "Integer32",
    "ModuleIdentity",
    "iso",
    "Gauge32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "IpAddress",
    "ObjectIdentity",
    "Counter64",
    "MibIdentifier",
    "TimeTicks",
    "Bits",
    "NotificationType",
    "Counter32")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aiSysCfg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32)
)

aiSysCfgSoftware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 1)
)

aiSysCfgTime = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 2)
)

aiSysCfgPower = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 3)
)

aiSysCfgFan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 4)
)

aiSysCfgTemp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISYSCFG-MIB",
    **{"aii": aii,
       "aiSysCfg": aiSysCfg,
       "aiSysCfgSoftware": aiSysCfgSoftware,
       "aiSysCfgTime": aiSysCfgTime,
       "aiSysCfgPower": aiSysCfgPower,
       "aiSysCfgFan": aiSysCfgFan,
       "aiSysCfgTemp": aiSysCfgTemp}
)
