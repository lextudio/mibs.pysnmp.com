# SNMP MIB module (MPLS-LDP-GENERIC-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LDP-GENERIC-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:15 2024
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
 mplsLdpEntityLdpId) = mibBuilder.importSymbols(
    "MPLS-LDP-STD-MIB",
    "mplsLdpEntityIndex",
    "mplsLdpEntityLdpId")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

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

mplsLdpGenericStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 7)
)
mplsLdpGenericStdMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLdpGenericObjects_ObjectIdentity = ObjectIdentity
mplsLdpGenericObjects = _MplsLdpGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1)
)
_MplsLdpEntityGenericObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityGenericObjects = _MplsLdpEntityGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1)
)
_MplsLdpEntityGenericLRTable_Object = MibTable
mplsLdpEntityGenericLRTable = _MplsLdpEntityGenericLRTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRTable.setStatus("current")
_MplsLdpEntityGenericLREntry_Object = MibTableRow
mplsLdpEntityGenericLREntry = _MplsLdpEntityGenericLREntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1)
)
mplsLdpEntityGenericLREntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMin"),
    (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMax"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLREntry.setStatus("current")


class _MplsLdpEntityGenericLRMin_Type(Unsigned32):
    """Custom type mplsLdpEntityGenericLRMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpEntityGenericLRMin_Type.__name__ = "Unsigned32"
_MplsLdpEntityGenericLRMin_Object = MibTableColumn
mplsLdpEntityGenericLRMin = _MplsLdpEntityGenericLRMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 1),
    _MplsLdpEntityGenericLRMin_Type()
)
mplsLdpEntityGenericLRMin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRMin.setStatus("current")


class _MplsLdpEntityGenericLRMax_Type(Unsigned32):
    """Custom type mplsLdpEntityGenericLRMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpEntityGenericLRMax_Type.__name__ = "Unsigned32"
_MplsLdpEntityGenericLRMax_Object = MibTableColumn
mplsLdpEntityGenericLRMax = _MplsLdpEntityGenericLRMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 2),
    _MplsLdpEntityGenericLRMax_Type()
)
mplsLdpEntityGenericLRMax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRMax.setStatus("current")


class _MplsLdpEntityGenericLabelSpace_Type(Integer32):
    """Custom type mplsLdpEntityGenericLabelSpace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perInterface", 2),
          ("perPlatform", 1))
    )


_MplsLdpEntityGenericLabelSpace_Type.__name__ = "Integer32"
_MplsLdpEntityGenericLabelSpace_Object = MibTableColumn
mplsLdpEntityGenericLabelSpace = _MplsLdpEntityGenericLabelSpace_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 3),
    _MplsLdpEntityGenericLabelSpace_Type()
)
mplsLdpEntityGenericLabelSpace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLabelSpace.setStatus("current")
_MplsLdpEntityGenericIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityGenericIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityGenericIfIndexOrZero = _MplsLdpEntityGenericIfIndexOrZero_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 4),
    _MplsLdpEntityGenericIfIndexOrZero_Type()
)
mplsLdpEntityGenericIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericIfIndexOrZero.setStatus("current")


class _MplsLdpEntityGenericLRStorageType_Type(StorageType):
    """Custom type mplsLdpEntityGenericLRStorageType based on StorageType"""


_MplsLdpEntityGenericLRStorageType_Object = MibTableColumn
mplsLdpEntityGenericLRStorageType = _MplsLdpEntityGenericLRStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 5),
    _MplsLdpEntityGenericLRStorageType_Type()
)
mplsLdpEntityGenericLRStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRStorageType.setStatus("current")
_MplsLdpEntityGenericLRRowStatus_Type = RowStatus
_MplsLdpEntityGenericLRRowStatus_Object = MibTableColumn
mplsLdpEntityGenericLRRowStatus = _MplsLdpEntityGenericLRRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 6),
    _MplsLdpEntityGenericLRRowStatus_Type()
)
mplsLdpEntityGenericLRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRRowStatus.setStatus("current")
_MplsLdpGenericConformance_ObjectIdentity = ObjectIdentity
mplsLdpGenericConformance = _MplsLdpGenericConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 2)
)
_MplsLdpGenericGroups_ObjectIdentity = ObjectIdentity
mplsLdpGenericGroups = _MplsLdpGenericGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 1)
)
_MplsLdpGenericCompliances_ObjectIdentity = ObjectIdentity
mplsLdpGenericCompliances = _MplsLdpGenericCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2)
)

# Managed Objects groups

mplsLdpGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 1, 1)
)
mplsLdpGenericGroup.setObjects(
      *(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLabelSpace"),
        ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericIfIndexOrZero"),
        ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRStorageType"),
        ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLdpGenericGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsLdpGenericModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpGenericModuleFullCompliance.setStatus(
        "current"
    )

mplsLdpGenericModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLdpGenericModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LDP-GENERIC-STD-MIB",
    **{"mplsLdpGenericStdMIB": mplsLdpGenericStdMIB,
       "mplsLdpGenericObjects": mplsLdpGenericObjects,
       "mplsLdpEntityGenericObjects": mplsLdpEntityGenericObjects,
       "mplsLdpEntityGenericLRTable": mplsLdpEntityGenericLRTable,
       "mplsLdpEntityGenericLREntry": mplsLdpEntityGenericLREntry,
       "mplsLdpEntityGenericLRMin": mplsLdpEntityGenericLRMin,
       "mplsLdpEntityGenericLRMax": mplsLdpEntityGenericLRMax,
       "mplsLdpEntityGenericLabelSpace": mplsLdpEntityGenericLabelSpace,
       "mplsLdpEntityGenericIfIndexOrZero": mplsLdpEntityGenericIfIndexOrZero,
       "mplsLdpEntityGenericLRStorageType": mplsLdpEntityGenericLRStorageType,
       "mplsLdpEntityGenericLRRowStatus": mplsLdpEntityGenericLRRowStatus,
       "mplsLdpGenericConformance": mplsLdpGenericConformance,
       "mplsLdpGenericGroups": mplsLdpGenericGroups,
       "mplsLdpGenericGroup": mplsLdpGenericGroup,
       "mplsLdpGenericCompliances": mplsLdpGenericCompliances,
       "mplsLdpGenericModuleFullCompliance": mplsLdpGenericModuleFullCompliance,
       "mplsLdpGenericModuleReadOnlyCompliance": mplsLdpGenericModuleReadOnlyCompliance}
)
