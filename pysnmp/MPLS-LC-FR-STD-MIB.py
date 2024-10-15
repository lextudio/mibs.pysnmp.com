# SNMP MIB module (MPLS-LC-FR-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LC-FR-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:09 2024
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

(DLCI,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "DLCI")

(mplsInterfaceIndex,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "mplsInterfaceIndex")

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

mplsLcFrStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 10)
)
mplsLcFrStdMIB.setRevisions(
        ("2006-01-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLcFrStdNotifications_ObjectIdentity = ObjectIdentity
mplsLcFrStdNotifications = _MplsLcFrStdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 0)
)
_MplsLcFrStdObjects_ObjectIdentity = ObjectIdentity
mplsLcFrStdObjects = _MplsLcFrStdObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1)
)
_MplsLcFrStdInterfaceConfTable_Object = MibTable
mplsLcFrStdInterfaceConfTable = _MplsLcFrStdInterfaceConfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLcFrStdInterfaceConfTable.setStatus("current")
_MplsLcFrStdInterfaceConfEntry_Object = MibTableRow
mplsLcFrStdInterfaceConfEntry = _MplsLcFrStdInterfaceConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1)
)
mplsLcFrStdInterfaceConfEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mplsLcFrStdInterfaceConfEntry.setStatus("current")
_MplsLcFrStdTrafficMinDlci_Type = DLCI
_MplsLcFrStdTrafficMinDlci_Object = MibTableColumn
mplsLcFrStdTrafficMinDlci = _MplsLcFrStdTrafficMinDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 1),
    _MplsLcFrStdTrafficMinDlci_Type()
)
mplsLcFrStdTrafficMinDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcFrStdTrafficMinDlci.setStatus("current")
_MplsLcFrStdTrafficMaxDlci_Type = DLCI
_MplsLcFrStdTrafficMaxDlci_Object = MibTableColumn
mplsLcFrStdTrafficMaxDlci = _MplsLcFrStdTrafficMaxDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 2),
    _MplsLcFrStdTrafficMaxDlci_Type()
)
mplsLcFrStdTrafficMaxDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcFrStdTrafficMaxDlci.setStatus("current")
_MplsLcFrStdCtrlMinDlci_Type = DLCI
_MplsLcFrStdCtrlMinDlci_Object = MibTableColumn
mplsLcFrStdCtrlMinDlci = _MplsLcFrStdCtrlMinDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 3),
    _MplsLcFrStdCtrlMinDlci_Type()
)
mplsLcFrStdCtrlMinDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcFrStdCtrlMinDlci.setStatus("current")
_MplsLcFrStdCtrlMaxDlci_Type = DLCI
_MplsLcFrStdCtrlMaxDlci_Object = MibTableColumn
mplsLcFrStdCtrlMaxDlci = _MplsLcFrStdCtrlMaxDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 4),
    _MplsLcFrStdCtrlMaxDlci_Type()
)
mplsLcFrStdCtrlMaxDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcFrStdCtrlMaxDlci.setStatus("current")
_MplsLcFrStdInterfaceConfRowStatus_Type = RowStatus
_MplsLcFrStdInterfaceConfRowStatus_Object = MibTableColumn
mplsLcFrStdInterfaceConfRowStatus = _MplsLcFrStdInterfaceConfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 5),
    _MplsLcFrStdInterfaceConfRowStatus_Type()
)
mplsLcFrStdInterfaceConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcFrStdInterfaceConfRowStatus.setStatus("current")


class _MplsLcFrStdInterfaceConfStorageType_Type(StorageType):
    """Custom type mplsLcFrStdInterfaceConfStorageType based on StorageType"""


_MplsLcFrStdInterfaceConfStorageType_Object = MibTableColumn
mplsLcFrStdInterfaceConfStorageType = _MplsLcFrStdInterfaceConfStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 6),
    _MplsLcFrStdInterfaceConfStorageType_Type()
)
mplsLcFrStdInterfaceConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLcFrStdInterfaceConfStorageType.setStatus("current")
_MplsLcFrStdConformance_ObjectIdentity = ObjectIdentity
mplsLcFrStdConformance = _MplsLcFrStdConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 2)
)
_MplsLcFrStdCompliances_ObjectIdentity = ObjectIdentity
mplsLcFrStdCompliances = _MplsLcFrStdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1)
)
_MplsLcFrStdGroups_ObjectIdentity = ObjectIdentity
mplsLcFrStdGroups = _MplsLcFrStdGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2)
)

# Managed Objects groups

mplsLcFrStdIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2, 1)
)
mplsLcFrStdIfGroup.setObjects(
      *(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdTrafficMinDlci"),
        ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdTrafficMaxDlci"),
        ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdCtrlMinDlci"),
        ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdCtrlMaxDlci"),
        ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdInterfaceConfRowStatus"),
        ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdInterfaceConfStorageType"))
)
if mibBuilder.loadTexts:
    mplsLcFrStdIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsLcFrStdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLcFrStdModuleFullCompliance.setStatus(
        "current"
    )

mplsLcFrStdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsLcFrStdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LC-FR-STD-MIB",
    **{"mplsLcFrStdMIB": mplsLcFrStdMIB,
       "mplsLcFrStdNotifications": mplsLcFrStdNotifications,
       "mplsLcFrStdObjects": mplsLcFrStdObjects,
       "mplsLcFrStdInterfaceConfTable": mplsLcFrStdInterfaceConfTable,
       "mplsLcFrStdInterfaceConfEntry": mplsLcFrStdInterfaceConfEntry,
       "mplsLcFrStdTrafficMinDlci": mplsLcFrStdTrafficMinDlci,
       "mplsLcFrStdTrafficMaxDlci": mplsLcFrStdTrafficMaxDlci,
       "mplsLcFrStdCtrlMinDlci": mplsLcFrStdCtrlMinDlci,
       "mplsLcFrStdCtrlMaxDlci": mplsLcFrStdCtrlMaxDlci,
       "mplsLcFrStdInterfaceConfRowStatus": mplsLcFrStdInterfaceConfRowStatus,
       "mplsLcFrStdInterfaceConfStorageType": mplsLcFrStdInterfaceConfStorageType,
       "mplsLcFrStdConformance": mplsLcFrStdConformance,
       "mplsLcFrStdCompliances": mplsLcFrStdCompliances,
       "mplsLcFrStdModuleFullCompliance": mplsLcFrStdModuleFullCompliance,
       "mplsLcFrStdModuleReadOnlyCompliance": mplsLcFrStdModuleReadOnlyCompliance,
       "mplsLcFrStdGroups": mplsLcFrStdGroups,
       "mplsLcFrStdIfGroup": mplsLcFrStdIfGroup}
)
