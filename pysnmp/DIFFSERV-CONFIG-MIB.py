# SNMP MIB module (DIFFSERV-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DIFFSERV-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:09 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

diffServConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 108)
)
diffServConfigMib.setRevisions(
        ("2004-01-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DiffServConfigMIBObjects_ObjectIdentity = ObjectIdentity
diffServConfigMIBObjects = _DiffServConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 108, 1)
)
_DiffServConfigTable_Object = MibTable
diffServConfigTable = _DiffServConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2)
)
if mibBuilder.loadTexts:
    diffServConfigTable.setStatus("current")
_DiffServConfigEntry_Object = MibTableRow
diffServConfigEntry = _DiffServConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2, 1)
)
diffServConfigEntry.setIndexNames(
    (0, "DIFFSERV-CONFIG-MIB", "diffServConfigId"),
)
if mibBuilder.loadTexts:
    diffServConfigEntry.setStatus("current")


class _DiffServConfigId_Type(SnmpAdminString):
    """Custom type diffServConfigId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 116),
    )


_DiffServConfigId_Type.__name__ = "SnmpAdminString"
_DiffServConfigId_Object = MibTableColumn
diffServConfigId = _DiffServConfigId_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 1),
    _DiffServConfigId_Type()
)
diffServConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServConfigId.setStatus("current")
_DiffServConfigDescr_Type = SnmpAdminString
_DiffServConfigDescr_Object = MibTableColumn
diffServConfigDescr = _DiffServConfigDescr_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 2),
    _DiffServConfigDescr_Type()
)
diffServConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServConfigDescr.setStatus("current")
_DiffServConfigOwner_Type = SnmpAdminString
_DiffServConfigOwner_Object = MibTableColumn
diffServConfigOwner = _DiffServConfigOwner_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 3),
    _DiffServConfigOwner_Type()
)
diffServConfigOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServConfigOwner.setStatus("current")
_DiffServConfigLastChange_Type = DateAndTime
_DiffServConfigLastChange_Object = MibTableColumn
diffServConfigLastChange = _DiffServConfigLastChange_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 4),
    _DiffServConfigLastChange_Type()
)
diffServConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServConfigLastChange.setStatus("current")


class _DiffServConfigStart_Type(RowPointer):
    """Custom type diffServConfigStart based on RowPointer"""
    defaultValue = (0, 0)


_DiffServConfigStart_Object = MibTableColumn
diffServConfigStart = _DiffServConfigStart_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 5),
    _DiffServConfigStart_Type()
)
diffServConfigStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServConfigStart.setStatus("current")


class _DiffServConfigStorage_Type(StorageType):
    """Custom type diffServConfigStorage based on StorageType"""


_DiffServConfigStorage_Object = MibTableColumn
diffServConfigStorage = _DiffServConfigStorage_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 6),
    _DiffServConfigStorage_Type()
)
diffServConfigStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServConfigStorage.setStatus("current")


class _DiffServConfigStatus_Type(RowStatus):
    """Custom type diffServConfigStatus based on RowStatus"""


_DiffServConfigStatus_Object = MibTableColumn
diffServConfigStatus = _DiffServConfigStatus_Object(
    (1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 7),
    _DiffServConfigStatus_Type()
)
diffServConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServConfigStatus.setStatus("current")
_DiffServConfigMIBConformance_ObjectIdentity = ObjectIdentity
diffServConfigMIBConformance = _DiffServConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 108, 2)
)
_DiffServConfigMIBCompliances_ObjectIdentity = ObjectIdentity
diffServConfigMIBCompliances = _DiffServConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 108, 2, 1)
)
_DiffServConfigMIBGroups_ObjectIdentity = ObjectIdentity
diffServConfigMIBGroups = _DiffServConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 108, 2, 2)
)

# Managed Objects groups

diffServConfigMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 108, 2, 2, 1)
)
diffServConfigMIBConfigGroup.setObjects(
      *(("DIFFSERV-CONFIG-MIB", "diffServConfigDescr"),
        ("DIFFSERV-CONFIG-MIB", "diffServConfigOwner"),
        ("DIFFSERV-CONFIG-MIB", "diffServConfigLastChange"),
        ("DIFFSERV-CONFIG-MIB", "diffServConfigStart"),
        ("DIFFSERV-CONFIG-MIB", "diffServConfigStorage"),
        ("DIFFSERV-CONFIG-MIB", "diffServConfigStatus"))
)
if mibBuilder.loadTexts:
    diffServConfigMIBConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

diffServConfigMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 108, 2, 1, 1)
)
if mibBuilder.loadTexts:
    diffServConfigMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIFFSERV-CONFIG-MIB",
    **{"diffServConfigMib": diffServConfigMib,
       "diffServConfigMIBObjects": diffServConfigMIBObjects,
       "diffServConfigTable": diffServConfigTable,
       "diffServConfigEntry": diffServConfigEntry,
       "diffServConfigId": diffServConfigId,
       "diffServConfigDescr": diffServConfigDescr,
       "diffServConfigOwner": diffServConfigOwner,
       "diffServConfigLastChange": diffServConfigLastChange,
       "diffServConfigStart": diffServConfigStart,
       "diffServConfigStorage": diffServConfigStorage,
       "diffServConfigStatus": diffServConfigStatus,
       "diffServConfigMIBConformance": diffServConfigMIBConformance,
       "diffServConfigMIBCompliances": diffServConfigMIBCompliances,
       "diffServConfigMIBFullCompliance": diffServConfigMIBFullCompliance,
       "diffServConfigMIBGroups": diffServConfigMIBGroups,
       "diffServConfigMIBConfigGroup": diffServConfigMIBConfigGroup}
)
