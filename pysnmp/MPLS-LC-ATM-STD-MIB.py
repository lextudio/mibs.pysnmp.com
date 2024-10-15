# SNMP MIB module (MPLS-LC-ATM-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LC-ATM-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:06 2024
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

(AtmVpIdentifier,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVpIdentifier")

(mplsInterfaceIndex,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "mplsInterfaceIndex")

(MplsAtmVcIdentifier,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsAtmVcIdentifier",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mplsLcAtmStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 9)
)
mplsLcAtmStdMIB.setRevisions(
        ("2006-01-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLcAtmStdNotifications_ObjectIdentity = ObjectIdentity
mplsLcAtmStdNotifications = _MplsLcAtmStdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 0)
)
_MplsLcAtmStdObjects_ObjectIdentity = ObjectIdentity
mplsLcAtmStdObjects = _MplsLcAtmStdObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1)
)
_MplsLcAtmStdInterfaceConfTable_Object = MibTable
mplsLcAtmStdInterfaceConfTable = _MplsLcAtmStdInterfaceConfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLcAtmStdInterfaceConfTable.setStatus("current")
_MplsLcAtmStdInterfaceConfEntry_Object = MibTableRow
mplsLcAtmStdInterfaceConfEntry = _MplsLcAtmStdInterfaceConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1)
)
mplsLcAtmStdInterfaceConfEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mplsLcAtmStdInterfaceConfEntry.setStatus("current")
_MplsLcAtmStdCtrlVpi_Type = AtmVpIdentifier
_MplsLcAtmStdCtrlVpi_Object = MibTableColumn
mplsLcAtmStdCtrlVpi = _MplsLcAtmStdCtrlVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 1),
    _MplsLcAtmStdCtrlVpi_Type()
)
mplsLcAtmStdCtrlVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmStdCtrlVpi.setStatus("current")
_MplsLcAtmStdCtrlVci_Type = MplsAtmVcIdentifier
_MplsLcAtmStdCtrlVci_Object = MibTableColumn
mplsLcAtmStdCtrlVci = _MplsLcAtmStdCtrlVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 2),
    _MplsLcAtmStdCtrlVci_Type()
)
mplsLcAtmStdCtrlVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmStdCtrlVci.setStatus("current")
_MplsLcAtmStdUnlabTrafVpi_Type = AtmVpIdentifier
_MplsLcAtmStdUnlabTrafVpi_Object = MibTableColumn
mplsLcAtmStdUnlabTrafVpi = _MplsLcAtmStdUnlabTrafVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 3),
    _MplsLcAtmStdUnlabTrafVpi_Type()
)
mplsLcAtmStdUnlabTrafVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmStdUnlabTrafVpi.setStatus("current")
_MplsLcAtmStdUnlabTrafVci_Type = MplsAtmVcIdentifier
_MplsLcAtmStdUnlabTrafVci_Object = MibTableColumn
mplsLcAtmStdUnlabTrafVci = _MplsLcAtmStdUnlabTrafVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 4),
    _MplsLcAtmStdUnlabTrafVci_Type()
)
mplsLcAtmStdUnlabTrafVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmStdUnlabTrafVci.setStatus("current")


class _MplsLcAtmStdVcMerge_Type(TruthValue):
    """Custom type mplsLcAtmStdVcMerge based on TruthValue"""


_MplsLcAtmStdVcMerge_Object = MibTableColumn
mplsLcAtmStdVcMerge = _MplsLcAtmStdVcMerge_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 5),
    _MplsLcAtmStdVcMerge_Type()
)
mplsLcAtmStdVcMerge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmStdVcMerge.setStatus("current")


class _MplsLcAtmVcDirectlyConnected_Type(TruthValue):
    """Custom type mplsLcAtmVcDirectlyConnected based on TruthValue"""


_MplsLcAtmVcDirectlyConnected_Object = MibTableColumn
mplsLcAtmVcDirectlyConnected = _MplsLcAtmVcDirectlyConnected_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 6),
    _MplsLcAtmVcDirectlyConnected_Type()
)
mplsLcAtmVcDirectlyConnected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmVcDirectlyConnected.setStatus("current")


class _MplsLcAtmLcAtmVPI_Type(AtmVpIdentifier):
    """Custom type mplsLcAtmLcAtmVPI based on AtmVpIdentifier"""
    defaultValue = 0


_MplsLcAtmLcAtmVPI_Object = MibTableColumn
mplsLcAtmLcAtmVPI = _MplsLcAtmLcAtmVPI_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 7),
    _MplsLcAtmLcAtmVPI_Type()
)
mplsLcAtmLcAtmVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmLcAtmVPI.setStatus("current")
_MplsLcAtmStdIfConfRowStatus_Type = RowStatus
_MplsLcAtmStdIfConfRowStatus_Object = MibTableColumn
mplsLcAtmStdIfConfRowStatus = _MplsLcAtmStdIfConfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 8),
    _MplsLcAtmStdIfConfRowStatus_Type()
)
mplsLcAtmStdIfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmStdIfConfRowStatus.setStatus("current")


class _MplsLcAtmStdIfConfStorageType_Type(StorageType):
    """Custom type mplsLcAtmStdIfConfStorageType based on StorageType"""


_MplsLcAtmStdIfConfStorageType_Object = MibTableColumn
mplsLcAtmStdIfConfStorageType = _MplsLcAtmStdIfConfStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 9),
    _MplsLcAtmStdIfConfStorageType_Type()
)
mplsLcAtmStdIfConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcAtmStdIfConfStorageType.setStatus("current")
_MplsLcAtmStdConformance_ObjectIdentity = ObjectIdentity
mplsLcAtmStdConformance = _MplsLcAtmStdConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 2)
)
_MplsLcAtmStdCompliances_ObjectIdentity = ObjectIdentity
mplsLcAtmStdCompliances = _MplsLcAtmStdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1)
)
_MplsLcAtmStdGroups_ObjectIdentity = ObjectIdentity
mplsLcAtmStdGroups = _MplsLcAtmStdGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 2)
)

# Managed Objects groups

mplsLcAtmStdIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 2, 1)
)
mplsLcAtmStdIfGroup.setObjects(
      *(("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdCtrlVpi"),
        ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdCtrlVci"),
        ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdUnlabTrafVpi"),
        ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdUnlabTrafVci"),
        ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdVcMerge"),
        ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmVcDirectlyConnected"),
        ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmLcAtmVPI"),
        ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfConfRowStatus"),
        ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfConfStorageType"))
)
if mibBuilder.loadTexts:
    mplsLcAtmStdIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsLcAtmStdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLcAtmStdModuleFullCompliance.setStatus(
        "current"
    )

mplsLcAtmStdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsLcAtmStdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LC-ATM-STD-MIB",
    **{"mplsLcAtmStdMIB": mplsLcAtmStdMIB,
       "mplsLcAtmStdNotifications": mplsLcAtmStdNotifications,
       "mplsLcAtmStdObjects": mplsLcAtmStdObjects,
       "mplsLcAtmStdInterfaceConfTable": mplsLcAtmStdInterfaceConfTable,
       "mplsLcAtmStdInterfaceConfEntry": mplsLcAtmStdInterfaceConfEntry,
       "mplsLcAtmStdCtrlVpi": mplsLcAtmStdCtrlVpi,
       "mplsLcAtmStdCtrlVci": mplsLcAtmStdCtrlVci,
       "mplsLcAtmStdUnlabTrafVpi": mplsLcAtmStdUnlabTrafVpi,
       "mplsLcAtmStdUnlabTrafVci": mplsLcAtmStdUnlabTrafVci,
       "mplsLcAtmStdVcMerge": mplsLcAtmStdVcMerge,
       "mplsLcAtmVcDirectlyConnected": mplsLcAtmVcDirectlyConnected,
       "mplsLcAtmLcAtmVPI": mplsLcAtmLcAtmVPI,
       "mplsLcAtmStdIfConfRowStatus": mplsLcAtmStdIfConfRowStatus,
       "mplsLcAtmStdIfConfStorageType": mplsLcAtmStdIfConfStorageType,
       "mplsLcAtmStdConformance": mplsLcAtmStdConformance,
       "mplsLcAtmStdCompliances": mplsLcAtmStdCompliances,
       "mplsLcAtmStdModuleFullCompliance": mplsLcAtmStdModuleFullCompliance,
       "mplsLcAtmStdModuleReadOnlyCompliance": mplsLcAtmStdModuleReadOnlyCompliance,
       "mplsLcAtmStdGroups": mplsLcAtmStdGroups,
       "mplsLcAtmStdIfGroup": mplsLcAtmStdIfGroup}
)
