# SNMP MIB module (MPLS-LDP-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LDP-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:14 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(mplsLdpEntityIndex,
 mplsLdpEntityLdpId,
 mplsLdpEntityObjects) = mibBuilder.importSymbols(
    "MPLS-LDP-MIB",
    "mplsLdpEntityIndex",
    "mplsLdpEntityLdpId",
    "mplsLdpEntityObjects")

(mplsMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-MIB",
    "mplsMIB")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

mplsLdpGenericMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9999, 6)
)
mplsLdpGenericMIB.setRevisions(
        ("2002-08-08 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLdpGenericObjects_ObjectIdentity = ObjectIdentity
mplsLdpGenericObjects = _MplsLdpGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9999, 6, 1)
)
_MplsLdpGenericConformance_ObjectIdentity = ObjectIdentity
mplsLdpGenericConformance = _MplsLdpGenericConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9999, 6, 3)
)
_MplsLdpGenericGroups_ObjectIdentity = ObjectIdentity
mplsLdpGenericGroups = _MplsLdpGenericGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 1)
)
_MplsLdpGenericCompliances_ObjectIdentity = ObjectIdentity
mplsLdpGenericCompliances = _MplsLdpGenericCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 2)
)
_MplsLdpEntityGenericObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityGenericObjects = _MplsLdpEntityGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 2, 5)
)
_MplsLdpEntityGenLRTable_Object = MibTable
mplsLdpEntityGenLRTable = _MplsLdpEntityGenLRTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityGenLRTable.setStatus("current")
_MplsLdpEntityGenLREntry_Object = MibTableRow
mplsLdpEntityGenLREntry = _MplsLdpEntityGenLREntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1)
)
mplsLdpEntityGenLREntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenLRMin"),
    (0, "MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenLRMax"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityGenLREntry.setStatus("current")


class _MplsLdpEntityGenLRMin_Type(Unsigned32):
    """Custom type mplsLdpEntityGenLRMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpEntityGenLRMin_Type.__name__ = "Unsigned32"
_MplsLdpEntityGenLRMin_Object = MibTableColumn
mplsLdpEntityGenLRMin = _MplsLdpEntityGenLRMin_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 1),
    _MplsLdpEntityGenLRMin_Type()
)
mplsLdpEntityGenLRMin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityGenLRMin.setStatus("current")


class _MplsLdpEntityGenLRMax_Type(Unsigned32):
    """Custom type mplsLdpEntityGenLRMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpEntityGenLRMax_Type.__name__ = "Unsigned32"
_MplsLdpEntityGenLRMax_Object = MibTableColumn
mplsLdpEntityGenLRMax = _MplsLdpEntityGenLRMax_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 2),
    _MplsLdpEntityGenLRMax_Type()
)
mplsLdpEntityGenLRMax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityGenLRMax.setStatus("current")
_MplsLdpEntityGenIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityGenIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityGenIfIndexOrZero = _MplsLdpEntityGenIfIndexOrZero_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 3),
    _MplsLdpEntityGenIfIndexOrZero_Type()
)
mplsLdpEntityGenIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityGenIfIndexOrZero.setStatus("current")
_MplsLdpEntityGenLRStorageType_Type = StorageType
_MplsLdpEntityGenLRStorageType_Object = MibTableColumn
mplsLdpEntityGenLRStorageType = _MplsLdpEntityGenLRStorageType_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 4),
    _MplsLdpEntityGenLRStorageType_Type()
)
mplsLdpEntityGenLRStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityGenLRStorageType.setStatus("current")
_MplsLdpEntityGenLRRowStatus_Type = RowStatus
_MplsLdpEntityGenLRRowStatus_Object = MibTableColumn
mplsLdpEntityGenLRRowStatus = _MplsLdpEntityGenLRRowStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 5),
    _MplsLdpEntityGenLRRowStatus_Type()
)
mplsLdpEntityGenLRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityGenLRRowStatus.setStatus("current")

# Managed Objects groups

mplsLdpGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 1, 1)
)
mplsLdpGenericGroup.setObjects(
      *(("MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenIfIndexOrZero"),
        ("MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenLRStorageType"),
        ("MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenLRRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLdpGenericGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsLdpGenModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpGenModuleFullCompliance.setStatus(
        "current"
    )

mplsLdpGenModuleROCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLdpGenModuleROCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LDP-GENERIC-MIB",
    **{"mplsLdpGenericMIB": mplsLdpGenericMIB,
       "mplsLdpGenericObjects": mplsLdpGenericObjects,
       "mplsLdpGenericConformance": mplsLdpGenericConformance,
       "mplsLdpGenericGroups": mplsLdpGenericGroups,
       "mplsLdpGenericGroup": mplsLdpGenericGroup,
       "mplsLdpGenericCompliances": mplsLdpGenericCompliances,
       "mplsLdpGenModuleFullCompliance": mplsLdpGenModuleFullCompliance,
       "mplsLdpGenModuleROCompliance": mplsLdpGenModuleROCompliance,
       "mplsLdpEntityGenericObjects": mplsLdpEntityGenericObjects,
       "mplsLdpEntityGenLRTable": mplsLdpEntityGenLRTable,
       "mplsLdpEntityGenLREntry": mplsLdpEntityGenLREntry,
       "mplsLdpEntityGenLRMin": mplsLdpEntityGenLRMin,
       "mplsLdpEntityGenLRMax": mplsLdpEntityGenLRMax,
       "mplsLdpEntityGenIfIndexOrZero": mplsLdpEntityGenIfIndexOrZero,
       "mplsLdpEntityGenLRStorageType": mplsLdpEntityGenLRStorageType,
       "mplsLdpEntityGenLRRowStatus": mplsLdpEntityGenLRRowStatus}
)
