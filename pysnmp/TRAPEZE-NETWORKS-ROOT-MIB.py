# SNMP MIB module (TRAPEZE-NETWORKS-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:25 2024
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

trpzRootMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525)
)
trpzRootMib.setRevisions(
        ("2008-05-22 00:08",
         "2007-11-28 00:07",
         "2006-04-14 00:06",
         "2005-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrpzProducts_ObjectIdentity = ObjectIdentity
trpzProducts = _TrpzProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 1)
)
_TrpzTemporary_ObjectIdentity = ObjectIdentity
trpzTemporary = _TrpzTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 2)
)
_TrpzRegistration_ObjectIdentity = ObjectIdentity
trpzRegistration = _TrpzRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3)
)
_TrpzMibs_ObjectIdentity = ObjectIdentity
trpzMibs = _TrpzMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4)
)
_TrpzTraps_ObjectIdentity = ObjectIdentity
trpzTraps = _TrpzTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 5)
)
_TrpzMgmtAppMibs_ObjectIdentity = ObjectIdentity
trpzMgmtAppMibs = _TrpzMgmtAppMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    **{"trpzRootMib": trpzRootMib,
       "trpzProducts": trpzProducts,
       "trpzTemporary": trpzTemporary,
       "trpzRegistration": trpzRegistration,
       "trpzMibs": trpzMibs,
       "trpzTraps": trpzTraps,
       "trpzMgmtAppMibs": trpzMgmtAppMibs}
)
