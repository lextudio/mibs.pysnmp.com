# SNMP MIB module (PANASAS-PANFS-MIB-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANASAS-PANFS-MIB-V1
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:35 2024
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

(panProducts,) = mibBuilder.importSymbols(
    "PANASAS-ROOT-MIB",
    "panProducts")

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

panFs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3)
)
panFs.setRevisions(
        ("2011-04-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanEvents_ObjectIdentity = ObjectIdentity
panEvents = _PanEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 1)
)
_PanSystem_ObjectIdentity = ObjectIdentity
panSystem = _PanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2)
)
_PanBSet_ObjectIdentity = ObjectIdentity
panBSet = _PanBSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3)
)
_PanVol_ObjectIdentity = ObjectIdentity
panVol = _PanVol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4)
)
_PanPerf_ObjectIdentity = ObjectIdentity
panPerf = _PanPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANASAS-PANFS-MIB-V1",
    **{"panFs": panFs,
       "panEvents": panEvents,
       "panSystem": panSystem,
       "panBSet": panBSet,
       "panVol": panVol,
       "panPerf": panPerf}
)
