# SNMP MIB module (PANASAS-SYSTEM-MIB-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANASAS-SYSTEM-MIB-V1
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:37 2024
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

(panFs,) = mibBuilder.importSymbols(
    "PANASAS-PANFS-MIB-V1",
    "panFs")

(PanSerialNumber,) = mibBuilder.importSymbols(
    "PANASAS-TC-MIB",
    "PanSerialNumber")

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

panSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2)
)
panSystem.setRevisions(
        ("2011-04-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanSystemCluster_ObjectIdentity = ObjectIdentity
panSystemCluster = _PanSystemCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1)
)


class _PanSystemClusterName_Type(DisplayString):
    """Custom type panSystemClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PanSystemClusterName_Type.__name__ = "DisplayString"
_PanSystemClusterName_Object = MibScalar
panSystemClusterName = _PanSystemClusterName_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 1),
    _PanSystemClusterName_Type()
)
panSystemClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemClusterName.setStatus("current")
_PanSystemClusterManagementAddress_Type = IpAddress
_PanSystemClusterManagementAddress_Object = MibScalar
panSystemClusterManagementAddress = _PanSystemClusterManagementAddress_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 2),
    _PanSystemClusterManagementAddress_Type()
)
panSystemClusterManagementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemClusterManagementAddress.setStatus("current")
_PanSystemClusterRepsetTable_Object = MibTable
panSystemClusterRepsetTable = _PanSystemClusterRepsetTable_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    panSystemClusterRepsetTable.setStatus("current")
_PanSystemClusterRepsetEntry_Object = MibTableRow
panSystemClusterRepsetEntry = _PanSystemClusterRepsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3, 1)
)
panSystemClusterRepsetEntry.setIndexNames(
    (0, "PANASAS-SYSTEM-MIB-V1", "panSystemClusterRepsetEntryIndex"),
)
if mibBuilder.loadTexts:
    panSystemClusterRepsetEntry.setStatus("current")


class _PanSystemClusterRepsetEntryIndex_Type(Integer32):
    """Custom type panSystemClusterRepsetEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_PanSystemClusterRepsetEntryIndex_Type.__name__ = "Integer32"
_PanSystemClusterRepsetEntryIndex_Object = MibTableColumn
panSystemClusterRepsetEntryIndex = _PanSystemClusterRepsetEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3, 1, 1),
    _PanSystemClusterRepsetEntryIndex_Type()
)
panSystemClusterRepsetEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemClusterRepsetEntryIndex.setStatus("current")
_PanSystemClusterRepsetEntryIpAddr_Type = IpAddress
_PanSystemClusterRepsetEntryIpAddr_Object = MibTableColumn
panSystemClusterRepsetEntryIpAddr = _PanSystemClusterRepsetEntryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3, 1, 2),
    _PanSystemClusterRepsetEntryIpAddr_Type()
)
panSystemClusterRepsetEntryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemClusterRepsetEntryIpAddr.setStatus("current")
_PanSystemClusterRepsetEntryBladeHwSN_Type = PanSerialNumber
_PanSystemClusterRepsetEntryBladeHwSN_Object = MibTableColumn
panSystemClusterRepsetEntryBladeHwSN = _PanSystemClusterRepsetEntryBladeHwSN_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3, 1, 3),
    _PanSystemClusterRepsetEntryBladeHwSN_Type()
)
panSystemClusterRepsetEntryBladeHwSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemClusterRepsetEntryBladeHwSN.setStatus("current")
_PanSystemServicesTable_Object = MibTable
panSystemServicesTable = _PanSystemServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    panSystemServicesTable.setStatus("current")
_PanSystemServicesEntry_Object = MibTableRow
panSystemServicesEntry = _PanSystemServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1)
)
panSystemServicesEntry.setIndexNames(
    (0, "PANASAS-SYSTEM-MIB-V1", "panSystemServicesId"),
)
if mibBuilder.loadTexts:
    panSystemServicesEntry.setStatus("current")
_PanSystemServicesId_Type = PanSerialNumber
_PanSystemServicesId_Object = MibTableColumn
panSystemServicesId = _PanSystemServicesId_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 1),
    _PanSystemServicesId_Type()
)
panSystemServicesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemServicesId.setStatus("current")
_PanSystemServicesBladeHwSN_Type = PanSerialNumber
_PanSystemServicesBladeHwSN_Object = MibTableColumn
panSystemServicesBladeHwSN = _PanSystemServicesBladeHwSN_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 2),
    _PanSystemServicesBladeHwSN_Type()
)
panSystemServicesBladeHwSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemServicesBladeHwSN.setStatus("current")
_PanSystemServicesType_Type = DisplayString
_PanSystemServicesType_Object = MibTableColumn
panSystemServicesType = _PanSystemServicesType_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 3),
    _PanSystemServicesType_Type()
)
panSystemServicesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemServicesType.setStatus("current")
_PanSystemServicesInfo_Type = DisplayString
_PanSystemServicesInfo_Object = MibTableColumn
panSystemServicesInfo = _PanSystemServicesInfo_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 4),
    _PanSystemServicesInfo_Type()
)
panSystemServicesInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemServicesInfo.setStatus("current")
_PanSystemServicesBackupBladeHwSN_Type = PanSerialNumber
_PanSystemServicesBackupBladeHwSN_Object = MibTableColumn
panSystemServicesBackupBladeHwSN = _PanSystemServicesBackupBladeHwSN_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 5),
    _PanSystemServicesBackupBladeHwSN_Type()
)
panSystemServicesBackupBladeHwSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemServicesBackupBladeHwSN.setStatus("current")
_PanSystemVolServiceTable_Object = MibTable
panSystemVolServiceTable = _PanSystemVolServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    panSystemVolServiceTable.setStatus("current")
_PanSystemVolServiceEntry_Object = MibTableRow
panSystemVolServiceEntry = _PanSystemVolServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 3, 1)
)
panSystemVolServiceEntry.setIndexNames(
    (0, "PANASAS-SYSTEM-MIB-V1", "panSystemServicesId"),
    (0, "PANASAS-SYSTEM-MIB-V1", "panSystemVolServiceVolIndex"),
)
if mibBuilder.loadTexts:
    panSystemVolServiceEntry.setStatus("current")


class _PanSystemVolServiceVolIndex_Type(Integer32):
    """Custom type panSystemVolServiceVolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_PanSystemVolServiceVolIndex_Type.__name__ = "Integer32"
_PanSystemVolServiceVolIndex_Object = MibTableColumn
panSystemVolServiceVolIndex = _PanSystemVolServiceVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 3, 1, 1),
    _PanSystemVolServiceVolIndex_Type()
)
panSystemVolServiceVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemVolServiceVolIndex.setStatus("current")
_PanSystemVolServiceVolPath_Type = DisplayString
_PanSystemVolServiceVolPath_Object = MibTableColumn
panSystemVolServiceVolPath = _PanSystemVolServiceVolPath_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 3, 1, 2),
    _PanSystemVolServiceVolPath_Type()
)
panSystemVolServiceVolPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSystemVolServiceVolPath.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANASAS-SYSTEM-MIB-V1",
    **{"panSystem": panSystem,
       "panSystemCluster": panSystemCluster,
       "panSystemClusterName": panSystemClusterName,
       "panSystemClusterManagementAddress": panSystemClusterManagementAddress,
       "panSystemClusterRepsetTable": panSystemClusterRepsetTable,
       "panSystemClusterRepsetEntry": panSystemClusterRepsetEntry,
       "panSystemClusterRepsetEntryIndex": panSystemClusterRepsetEntryIndex,
       "panSystemClusterRepsetEntryIpAddr": panSystemClusterRepsetEntryIpAddr,
       "panSystemClusterRepsetEntryBladeHwSN": panSystemClusterRepsetEntryBladeHwSN,
       "panSystemServicesTable": panSystemServicesTable,
       "panSystemServicesEntry": panSystemServicesEntry,
       "panSystemServicesId": panSystemServicesId,
       "panSystemServicesBladeHwSN": panSystemServicesBladeHwSN,
       "panSystemServicesType": panSystemServicesType,
       "panSystemServicesInfo": panSystemServicesInfo,
       "panSystemServicesBackupBladeHwSN": panSystemServicesBackupBladeHwSN,
       "panSystemVolServiceTable": panSystemVolServiceTable,
       "panSystemVolServiceEntry": panSystemVolServiceEntry,
       "panSystemVolServiceVolIndex": panSystemVolServiceVolIndex,
       "panSystemVolServiceVolPath": panSystemVolServiceVolPath}
)
