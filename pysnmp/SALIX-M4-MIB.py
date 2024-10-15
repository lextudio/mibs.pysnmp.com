# SNMP MIB module (SALIX-M4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-M4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:30 2024
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

(atmfM4CellProtoHistIndex,
 atmfM4EquipHolderEntry,
 atmfM4PlugInUnitEntry,
 atmfM4TcAdaptorEntry,
 atmfM4TrapAlarmSeverity) = mibBuilder.importSymbols(
    "ATM-FORUM-M4-MIB",
    "atmfM4CellProtoHistIndex",
    "atmfM4EquipHolderEntry",
    "atmfM4PlugInUnitEntry",
    "atmfM4TcAdaptorEntry",
    "atmfM4TrapAlarmSeverity")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(hrSWInstalledIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrSWInstalledIndex")

(salixGeneric,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "salixGeneric")

(SalixPlugInUnitType,) = mibBuilder.importSymbols(
    "SALIX-PRODUCT-PLUGIN-MIB",
    "SalixPlugInUnitType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

salixM4MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SalixAtmfM4SwitchoverReasons(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("administrative", 1),
          ("failure", 3),
          ("pluginRemoved", 2))
    )



# MIB Managed Objects in the order of their OIDs

_SalixM4MIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixM4MIBTrapPrefix = _SalixM4MIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 0)
)
_SalixM4MIBObjects_ObjectIdentity = ObjectIdentity
salixM4MIBObjects = _SalixM4MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1)
)
_SalixAtmfM4EquipHolderTable_Object = MibTable
salixAtmfM4EquipHolderTable = _SalixAtmfM4EquipHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    salixAtmfM4EquipHolderTable.setStatus("current")
_SalixAtmfM4EquipHolderEntry_Object = MibTableRow
salixAtmfM4EquipHolderEntry = _SalixAtmfM4EquipHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    salixAtmfM4EquipHolderEntry.setStatus("current")


class _SalixAtmfM4EquipHolderDownloadState_Type(Integer32):
    """Custom type salixAtmfM4EquipHolderDownloadState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 4),
          ("failed", 5),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_SalixAtmfM4EquipHolderDownloadState_Type.__name__ = "Integer32"
_SalixAtmfM4EquipHolderDownloadState_Object = MibTableColumn
salixAtmfM4EquipHolderDownloadState = _SalixAtmfM4EquipHolderDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 2, 1, 1),
    _SalixAtmfM4EquipHolderDownloadState_Type()
)
salixAtmfM4EquipHolderDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAtmfM4EquipHolderDownloadState.setStatus("current")


class _SalixAtmfM4EquipHolderDownloadStatusMessage_Type(OctetString):
    """Custom type salixAtmfM4EquipHolderDownloadStatusMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_SalixAtmfM4EquipHolderDownloadStatusMessage_Type.__name__ = "OctetString"
_SalixAtmfM4EquipHolderDownloadStatusMessage_Object = MibTableColumn
salixAtmfM4EquipHolderDownloadStatusMessage = _SalixAtmfM4EquipHolderDownloadStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 2, 1, 2),
    _SalixAtmfM4EquipHolderDownloadStatusMessage_Type()
)
salixAtmfM4EquipHolderDownloadStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAtmfM4EquipHolderDownloadStatusMessage.setStatus("current")
_SalixAtmfM4PlugInUnitTable_Object = MibTable
salixAtmfM4PlugInUnitTable = _SalixAtmfM4PlugInUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitTable.setStatus("current")
_SalixAtmfM4PlugInUnitEntry_Object = MibTableRow
salixAtmfM4PlugInUnitEntry = _SalixAtmfM4PlugInUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitEntry.setStatus("current")


class _SalixAtmfM4PlugInUnitSerialNumber_Type(DisplayString):
    """Custom type salixAtmfM4PlugInUnitSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SalixAtmfM4PlugInUnitSerialNumber_Type.__name__ = "DisplayString"
_SalixAtmfM4PlugInUnitSerialNumber_Object = MibTableColumn
salixAtmfM4PlugInUnitSerialNumber = _SalixAtmfM4PlugInUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 1),
    _SalixAtmfM4PlugInUnitSerialNumber_Type()
)
salixAtmfM4PlugInUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitSerialNumber.setStatus("current")
_SalixAtmfM4PlugInUnitType_Type = SalixPlugInUnitType
_SalixAtmfM4PlugInUnitType_Object = MibTableColumn
salixAtmfM4PlugInUnitType = _SalixAtmfM4PlugInUnitType_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 2),
    _SalixAtmfM4PlugInUnitType_Type()
)
salixAtmfM4PlugInUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitType.setStatus("current")


class _SalixAtmfM4PlugInUnitReset_Type(Integer32):
    """Custom type salixAtmfM4PlugInUnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("none", 0),
          ("warm", 2))
    )


_SalixAtmfM4PlugInUnitReset_Type.__name__ = "Integer32"
_SalixAtmfM4PlugInUnitReset_Object = MibTableColumn
salixAtmfM4PlugInUnitReset = _SalixAtmfM4PlugInUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 3),
    _SalixAtmfM4PlugInUnitReset_Type()
)
salixAtmfM4PlugInUnitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitReset.setStatus("current")


class _SalixAtmfM4PlugInUnitHwRevision_Type(DisplayString):
    """Custom type salixAtmfM4PlugInUnitHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SalixAtmfM4PlugInUnitHwRevision_Type.__name__ = "DisplayString"
_SalixAtmfM4PlugInUnitHwRevision_Object = MibTableColumn
salixAtmfM4PlugInUnitHwRevision = _SalixAtmfM4PlugInUnitHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 4),
    _SalixAtmfM4PlugInUnitHwRevision_Type()
)
salixAtmfM4PlugInUnitHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitHwRevision.setStatus("current")


class _SalixAtmfM4PlugInUnitLedStatus_Type(Integer32):
    """Custom type salixAtmfM4PlugInUnitLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SalixAtmfM4PlugInUnitLedStatus_Type.__name__ = "Integer32"
_SalixAtmfM4PlugInUnitLedStatus_Object = MibTableColumn
salixAtmfM4PlugInUnitLedStatus = _SalixAtmfM4PlugInUnitLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 5),
    _SalixAtmfM4PlugInUnitLedStatus_Type()
)
salixAtmfM4PlugInUnitLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitLedStatus.setStatus("current")


class _SalixAtmfM4PlugInUnitRedundancyConfig_Type(Integer32):
    """Custom type salixAtmfM4PlugInUnitRedundancyConfig based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("protect", 2),
          ("working", 1))
    )


_SalixAtmfM4PlugInUnitRedundancyConfig_Type.__name__ = "Integer32"
_SalixAtmfM4PlugInUnitRedundancyConfig_Object = MibTableColumn
salixAtmfM4PlugInUnitRedundancyConfig = _SalixAtmfM4PlugInUnitRedundancyConfig_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 6),
    _SalixAtmfM4PlugInUnitRedundancyConfig_Type()
)
salixAtmfM4PlugInUnitRedundancyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitRedundancyConfig.setStatus("current")
_SalixAtmfM4PlugInUnitRedundancyPartnerModule_Type = PhysicalIndex
_SalixAtmfM4PlugInUnitRedundancyPartnerModule_Object = MibTableColumn
salixAtmfM4PlugInUnitRedundancyPartnerModule = _SalixAtmfM4PlugInUnitRedundancyPartnerModule_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 7),
    _SalixAtmfM4PlugInUnitRedundancyPartnerModule_Type()
)
salixAtmfM4PlugInUnitRedundancyPartnerModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitRedundancyPartnerModule.setStatus("current")


class _SalixAtmfM4PlugInUnitRedundancyPairStatus_Type(Integer32):
    """Custom type salixAtmfM4PlugInUnitRedundancyPairStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("configured", 3),
          ("created", 2),
          ("none", 1))
    )


_SalixAtmfM4PlugInUnitRedundancyPairStatus_Type.__name__ = "Integer32"
_SalixAtmfM4PlugInUnitRedundancyPairStatus_Object = MibTableColumn
salixAtmfM4PlugInUnitRedundancyPairStatus = _SalixAtmfM4PlugInUnitRedundancyPairStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 8),
    _SalixAtmfM4PlugInUnitRedundancyPairStatus_Type()
)
salixAtmfM4PlugInUnitRedundancyPairStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitRedundancyPairStatus.setStatus("current")


class _SalixAtmfM4PlugInUnitRedundancyStatusMessage_Type(OctetString):
    """Custom type salixAtmfM4PlugInUnitRedundancyStatusMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_SalixAtmfM4PlugInUnitRedundancyStatusMessage_Type.__name__ = "OctetString"
_SalixAtmfM4PlugInUnitRedundancyStatusMessage_Object = MibTableColumn
salixAtmfM4PlugInUnitRedundancyStatusMessage = _SalixAtmfM4PlugInUnitRedundancyStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 3, 1, 9),
    _SalixAtmfM4PlugInUnitRedundancyStatusMessage_Type()
)
salixAtmfM4PlugInUnitRedundancyStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitRedundancyStatusMessage.setStatus("current")
_SalixAtmfM4TrapSwitchoverReason_Type = SalixAtmfM4SwitchoverReasons
_SalixAtmfM4TrapSwitchoverReason_Object = MibScalar
salixAtmfM4TrapSwitchoverReason = _SalixAtmfM4TrapSwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 1, 4),
    _SalixAtmfM4TrapSwitchoverReason_Type()
)
salixAtmfM4TrapSwitchoverReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    salixAtmfM4TrapSwitchoverReason.setStatus("current")
_SalixM4MIBTraps_ObjectIdentity = ObjectIdentity
salixM4MIBTraps = _SalixM4MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 2)
)
_SalixM4MIBCompliance_ObjectIdentity = ObjectIdentity
salixM4MIBCompliance = _SalixM4MIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 3)
)
_SalixM4Groups_ObjectIdentity = ObjectIdentity
salixM4Groups = _SalixM4Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 3, 1)
)
_SalixM4Compliances_ObjectIdentity = ObjectIdentity
salixM4Compliances = _SalixM4Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 3, 2)
)
atmfM4EquipHolderEntry.registerAugmentions(
    ("SALIX-M4-MIB",
     "salixAtmfM4EquipHolderEntry")
)
salixAtmfM4EquipHolderEntry.setIndexNames(*atmfM4EquipHolderEntry.getIndexNames())
atmfM4PlugInUnitEntry.registerAugmentions(
    ("SALIX-M4-MIB",
     "salixAtmfM4PlugInUnitEntry")
)
salixAtmfM4PlugInUnitEntry.setIndexNames(*atmfM4PlugInUnitEntry.getIndexNames())

# Managed Objects groups

salixM4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 3, 1, 1)
)
salixM4Group.setObjects(
      *(("SALIX-M4-MIB", "salixAtmfM4EquipHolderDownloadState"),
        ("SALIX-M4-MIB", "salixAtmfM4EquipHolderDownloadStatusMessage"))
)
if mibBuilder.loadTexts:
    salixM4Group.setStatus("current")


# Notification objects

salixAtmfM4HwSwDownloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 0, 1)
)
salixAtmfM4HwSwDownloadSuccess.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("HOST-RESOURCES-MIB", "hrSWInstalledIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    salixAtmfM4HwSwDownloadSuccess.setStatus(
        "current"
    )

salixAtmfM4PlugInUnitRedundancyPairCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 0, 2)
)
salixAtmfM4PlugInUnitRedundancyPairCreated.setObjects(
      *(("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyConfig"),
        ("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyConfig"))
)
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitRedundancyPairCreated.setStatus(
        "current"
    )

salixAtmfM4PlugInUnitRedundancyPairDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 0, 3)
)
salixAtmfM4PlugInUnitRedundancyPairDestroyed.setObjects(
      *(("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyConfig"),
        ("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyConfig"))
)
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitRedundancyPairDestroyed.setStatus(
        "current"
    )

salixAtmfM4PlugInUnitRedundancyPairSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 0, 4)
)
salixAtmfM4PlugInUnitRedundancyPairSwitchover.setObjects(
      *(("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyConfig"),
        ("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyConfig"),
        ("SALIX-M4-MIB", "salixAtmfM4TrapSwitchoverReason"))
)
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitRedundancyPairSwitchover.setStatus(
        "current"
    )

salixAtmfM4PlugInUnitRedundancyPairStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 0, 5)
)
salixAtmfM4PlugInUnitRedundancyPairStatusChange.setObjects(
      *(("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyConfig"),
        ("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyConfig"),
        ("SALIX-M4-MIB", "salixAtmfM4PlugInUnitRedundancyPairStatus"))
)
if mibBuilder.loadTexts:
    salixAtmfM4PlugInUnitRedundancyPairStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

salixM4Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 2, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixM4Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-M4-MIB",
    **{"SalixAtmfM4SwitchoverReasons": SalixAtmfM4SwitchoverReasons,
       "salixM4MIB": salixM4MIB,
       "salixM4MIBTrapPrefix": salixM4MIBTrapPrefix,
       "salixAtmfM4HwSwDownloadSuccess": salixAtmfM4HwSwDownloadSuccess,
       "salixAtmfM4PlugInUnitRedundancyPairCreated": salixAtmfM4PlugInUnitRedundancyPairCreated,
       "salixAtmfM4PlugInUnitRedundancyPairDestroyed": salixAtmfM4PlugInUnitRedundancyPairDestroyed,
       "salixAtmfM4PlugInUnitRedundancyPairSwitchover": salixAtmfM4PlugInUnitRedundancyPairSwitchover,
       "salixAtmfM4PlugInUnitRedundancyPairStatusChange": salixAtmfM4PlugInUnitRedundancyPairStatusChange,
       "salixM4MIBObjects": salixM4MIBObjects,
       "salixAtmfM4EquipHolderTable": salixAtmfM4EquipHolderTable,
       "salixAtmfM4EquipHolderEntry": salixAtmfM4EquipHolderEntry,
       "salixAtmfM4EquipHolderDownloadState": salixAtmfM4EquipHolderDownloadState,
       "salixAtmfM4EquipHolderDownloadStatusMessage": salixAtmfM4EquipHolderDownloadStatusMessage,
       "salixAtmfM4PlugInUnitTable": salixAtmfM4PlugInUnitTable,
       "salixAtmfM4PlugInUnitEntry": salixAtmfM4PlugInUnitEntry,
       "salixAtmfM4PlugInUnitSerialNumber": salixAtmfM4PlugInUnitSerialNumber,
       "salixAtmfM4PlugInUnitType": salixAtmfM4PlugInUnitType,
       "salixAtmfM4PlugInUnitReset": salixAtmfM4PlugInUnitReset,
       "salixAtmfM4PlugInUnitHwRevision": salixAtmfM4PlugInUnitHwRevision,
       "salixAtmfM4PlugInUnitLedStatus": salixAtmfM4PlugInUnitLedStatus,
       "salixAtmfM4PlugInUnitRedundancyConfig": salixAtmfM4PlugInUnitRedundancyConfig,
       "salixAtmfM4PlugInUnitRedundancyPartnerModule": salixAtmfM4PlugInUnitRedundancyPartnerModule,
       "salixAtmfM4PlugInUnitRedundancyPairStatus": salixAtmfM4PlugInUnitRedundancyPairStatus,
       "salixAtmfM4PlugInUnitRedundancyStatusMessage": salixAtmfM4PlugInUnitRedundancyStatusMessage,
       "salixAtmfM4TrapSwitchoverReason": salixAtmfM4TrapSwitchoverReason,
       "salixM4MIBTraps": salixM4MIBTraps,
       "salixM4MIBCompliance": salixM4MIBCompliance,
       "salixM4Groups": salixM4Groups,
       "salixM4Group": salixM4Group,
       "salixM4Compliances": salixM4Compliances,
       "salixM4Compliance": salixM4Compliance}
)
