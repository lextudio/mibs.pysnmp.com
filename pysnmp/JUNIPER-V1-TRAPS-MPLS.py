# SNMP MIB module (JUNIPER-V1-TRAPS-MPLS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-V1-TRAPS-MPLS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:25 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniperMIB_ObjectIdentity = ObjectIdentity
juniperMIB = _JuniperMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636)
)
_JnxMibs_ObjectIdentity = ObjectIdentity
jnxMibs = _JnxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3)
)
_Mpls_ObjectIdentity = ObjectIdentity
mpls = _Mpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2)
)
_MplsLspList_ObjectIdentity = ObjectIdentity
mplsLspList = _MplsLspList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3)
)
_MplsLspEntry_ObjectIdentity = ObjectIdentity
mplsLspEntry = _MplsLspEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1)
)
_MplsLspName_ObjectIdentity = ObjectIdentity
mplsLspName = _MplsLspName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 1)
)
_MplsPathName_ObjectIdentity = ObjectIdentity
mplsPathName = _MplsPathName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 17)
)

# Managed Objects groups


# Notification objects

mplsLspUpV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 1)
)
mplsLspUpV1.setObjects(
      *(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"),
        ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspUpV1.setStatus(
        ""
    )

mplsLspDownV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 2)
)
mplsLspDownV1.setObjects(
      *(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"),
        ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspDownV1.setStatus(
        ""
    )

mplsLspChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 3)
)
mplsLspChangeV1.setObjects(
      *(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"),
        ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspChangeV1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-V1-TRAPS-MPLS",
    **{"juniperMIB": juniperMIB,
       "mplsLspUpV1": mplsLspUpV1,
       "mplsLspDownV1": mplsLspDownV1,
       "mplsLspChangeV1": mplsLspChangeV1,
       "jnxMibs": jnxMibs,
       "mpls": mpls,
       "mplsLspList": mplsLspList,
       "mplsLspEntry": mplsLspEntry,
       "mplsLspName": mplsLspName,
       "mplsPathName": mplsPathName}
)
