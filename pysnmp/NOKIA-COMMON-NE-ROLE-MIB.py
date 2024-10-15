# SNMP MIB module (NOKIA-COMMON-NE-ROLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-COMMON-NE-ROLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:36 2024
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

(ntcCommonMibs,) = mibBuilder.importSymbols(
    "NOKIA-COMMON-MIB-OID-REGISTRATION-MIB",
    "ntcCommonMibs")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetCommonNERole_ObjectIdentity = ObjectIdentity
netCommonNERole = _NetCommonNERole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6)
)
_ConeRoleTable_Object = MibTable
coneRoleTable = _ConeRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1)
)
if mibBuilder.loadTexts:
    coneRoleTable.setStatus("mandatory")
_ConeRoleEntry_Object = MibTableRow
coneRoleEntry = _ConeRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1, 1)
)
coneRoleEntry.setIndexNames(
    (0, "NOKIA-COMMON-NE-ROLE-MIB", "coneRoleIndex"),
)
if mibBuilder.loadTexts:
    coneRoleEntry.setStatus("mandatory")


class _ConeRoleIndex_Type(Integer32):
    """Custom type coneRoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConeRoleIndex_Type.__name__ = "Integer32"
_ConeRoleIndex_Object = MibTableColumn
coneRoleIndex = _ConeRoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1, 1, 1),
    _ConeRoleIndex_Type()
)
coneRoleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coneRoleIndex.setStatus("mandatory")
_ConeRowIdx_Type = ObjectIdentifier
_ConeRowIdx_Object = MibTableColumn
coneRowIdx = _ConeRowIdx_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1, 1, 2),
    _ConeRowIdx_Type()
)
coneRowIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coneRowIdx.setStatus("mandatory")
_ConeInfo_Type = OctetString
_ConeInfo_Object = MibTableColumn
coneInfo = _ConeInfo_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 6, 1, 1, 3),
    _ConeInfo_Type()
)
coneInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coneInfo.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-COMMON-NE-ROLE-MIB",
    **{"netCommonNERole": netCommonNERole,
       "coneRoleTable": coneRoleTable,
       "coneRoleEntry": coneRoleEntry,
       "coneRoleIndex": coneRoleIndex,
       "coneRowIdx": coneRowIdx,
       "coneInfo": coneInfo}
)
