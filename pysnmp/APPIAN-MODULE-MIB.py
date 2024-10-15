# SNMP MIB module (APPIAN-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:37 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcAdminStatus,
 AcNodeId,
 AcOpStatus,
 AcSlotNumber,
 AcSwVersion,
 acOsap) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "AcSlotNumber",
    "AcSwVersion",
    "acOsap")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2)
)
acModule.setRevisions(
        ("1999-11-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcModuleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("bits-s3", 2),
          ("ds1-14-mc", 12),
          ("ds1-7-io", 13),
          ("ds3-access", 15),
          ("ds3-io", 16),
          ("ds3-network", 14),
          ("e1", 33),
          ("e1-io", 34),
          ("e3", 35),
          ("e3-io", 36),
          ("enet-agg", 37),
          ("fe16-mc", 4),
          ("fe8-fx-io", 6),
          ("fe8-tx-io", 5),
          ("gbe-lx", 8),
          ("gbe-sfp", 9),
          ("gbe-sx", 7),
          ("not-present", 1),
          ("oc12-ir-1", 25),
          ("oc12-ir-1-oc3c-ir-4", 24),
          ("oc12-ir-2", 26),
          ("oc12-ir-4", 27),
          ("oc12-lr-1", 28),
          ("oc12-lr-2", 29),
          ("oc3-ir-1", 17),
          ("oc3-ir-2", 18),
          ("oc3-lr-1", 21),
          ("oc3-lr-2", 22),
          ("oc3-sr-1", 19),
          ("oc3-sr-2", 20),
          ("oc3c-ir-4", 23),
          ("oc48-ir-1", 11),
          ("oc48-ir-1-oc12-ir-4", 30),
          ("oc48-ir-2", 10),
          ("oc48-lr-1", 32),
          ("oc48-lr-2", 31),
          ("svcproc-1", 3),
          ("unknown", 0))
    )



class AcModuleNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class AcMediaSlotNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )



# MIB Managed Objects in the order of their OIDs

_AcModuleTraps_ObjectIdentity = ObjectIdentity
acModuleTraps = _AcModuleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 0)
)
_AcModuleTable_Object = MibTable
acModuleTable = _AcModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1)
)
if mibBuilder.loadTexts:
    acModuleTable.setStatus("current")
_AcModuleEntry_Object = MibTableRow
acModuleEntry = _AcModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1)
)
acModuleEntry.setIndexNames(
    (0, "APPIAN-MODULE-MIB", "acModuleNodeId"),
    (0, "APPIAN-MODULE-MIB", "acModuleSlot"),
    (0, "APPIAN-MODULE-MIB", "acModuleNumber"),
)
if mibBuilder.loadTexts:
    acModuleEntry.setStatus("current")
_AcModuleNodeId_Type = AcNodeId
_AcModuleNodeId_Object = MibTableColumn
acModuleNodeId = _AcModuleNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 1),
    _AcModuleNodeId_Type()
)
acModuleNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acModuleNodeId.setStatus("current")
_AcModuleSlot_Type = AcSlotNumber
_AcModuleSlot_Object = MibTableColumn
acModuleSlot = _AcModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 2),
    _AcModuleSlot_Type()
)
acModuleSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acModuleSlot.setStatus("current")
_AcModuleNumber_Type = AcModuleNumber
_AcModuleNumber_Object = MibTableColumn
acModuleNumber = _AcModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 3),
    _AcModuleNumber_Type()
)
acModuleNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acModuleNumber.setStatus("current")


class _AcModuleAdminStatus_Type(AcAdminStatus):
    """Custom type acModuleAdminStatus based on AcAdminStatus"""


_AcModuleAdminStatus_Object = MibTableColumn
acModuleAdminStatus = _AcModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 4),
    _AcModuleAdminStatus_Type()
)
acModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acModuleAdminStatus.setStatus("current")


class _AcModuleCfgType_Type(AcModuleType):
    """Custom type acModuleCfgType based on AcModuleType"""


_AcModuleCfgType_Object = MibTableColumn
acModuleCfgType = _AcModuleCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 5),
    _AcModuleCfgType_Type()
)
acModuleCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acModuleCfgType.setStatus("current")
_AcModuleType_Type = AcModuleType
_AcModuleType_Object = MibTableColumn
acModuleType = _AcModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 6),
    _AcModuleType_Type()
)
acModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleType.setStatus("current")
_AcModuleOpStatus_Type = AcOpStatus
_AcModuleOpStatus_Object = MibTableColumn
acModuleOpStatus = _AcModuleOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 7),
    _AcModuleOpStatus_Type()
)
acModuleOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleOpStatus.setStatus("current")


class _AcModuleRevision_Type(Integer32):
    """Custom type acModuleRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcModuleRevision_Type.__name__ = "Integer32"
_AcModuleRevision_Object = MibTableColumn
acModuleRevision = _AcModuleRevision_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 8),
    _AcModuleRevision_Type()
)
acModuleRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleRevision.setStatus("current")


class _AcModuleSerialNumber_Type(DisplayString):
    """Custom type acModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcModuleSerialNumber_Type.__name__ = "DisplayString"
_AcModuleSerialNumber_Object = MibTableColumn
acModuleSerialNumber = _AcModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 9),
    _AcModuleSerialNumber_Type()
)
acModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleSerialNumber.setStatus("current")


class _AcModuleProductionDate_Type(DisplayString):
    """Custom type acModuleProductionDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_AcModuleProductionDate_Type.__name__ = "DisplayString"
_AcModuleProductionDate_Object = MibTableColumn
acModuleProductionDate = _AcModuleProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 10),
    _AcModuleProductionDate_Type()
)
acModuleProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleProductionDate.setStatus("current")


class _AcModuleFirmwareName_Type(DisplayString):
    """Custom type acModuleFirmwareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcModuleFirmwareName_Type.__name__ = "DisplayString"
_AcModuleFirmwareName_Object = MibTableColumn
acModuleFirmwareName = _AcModuleFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 11),
    _AcModuleFirmwareName_Type()
)
acModuleFirmwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleFirmwareName.setStatus("current")


class _AcModuleFirmwareRevision_Type(Integer32):
    """Custom type acModuleFirmwareRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcModuleFirmwareRevision_Type.__name__ = "Integer32"
_AcModuleFirmwareRevision_Object = MibTableColumn
acModuleFirmwareRevision = _AcModuleFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 12),
    _AcModuleFirmwareRevision_Type()
)
acModuleFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleFirmwareRevision.setStatus("current")
_AcModuleNumberFailures_Type = Counter32
_AcModuleNumberFailures_Object = MibTableColumn
acModuleNumberFailures = _AcModuleNumberFailures_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 13),
    _AcModuleNumberFailures_Type()
)
acModuleNumberFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleNumberFailures.setStatus("current")


class _AcModuleReset_Type(TruthValue):
    """Custom type acModuleReset based on TruthValue"""


_AcModuleReset_Object = MibTableColumn
acModuleReset = _AcModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 14),
    _AcModuleReset_Type()
)
acModuleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acModuleReset.setStatus("current")


class _AcModuleNumberPorts_Type(Integer32):
    """Custom type acModuleNumberPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcModuleNumberPorts_Type.__name__ = "Integer32"
_AcModuleNumberPorts_Object = MibTableColumn
acModuleNumberPorts = _AcModuleNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 15),
    _AcModuleNumberPorts_Type()
)
acModuleNumberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleNumberPorts.setStatus("current")


class _AcModuleName_Type(DisplayString):
    """Custom type acModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_AcModuleName_Type.__name__ = "DisplayString"
_AcModuleName_Object = MibTableColumn
acModuleName = _AcModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 16),
    _AcModuleName_Type()
)
acModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleName.setStatus("current")
_AcModuleSwVersion_Type = AcSwVersion
_AcModuleSwVersion_Object = MibTableColumn
acModuleSwVersion = _AcModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 17),
    _AcModuleSwVersion_Type()
)
acModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleSwVersion.setStatus("current")


class _AcModuleDiagTestMode_Type(Integer32):
    """Custom type acModuleDiagTestMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 2),
          ("basic", 1),
          ("stress", 3))
    )


_AcModuleDiagTestMode_Type.__name__ = "Integer32"
_AcModuleDiagTestMode_Object = MibTableColumn
acModuleDiagTestMode = _AcModuleDiagTestMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 18),
    _AcModuleDiagTestMode_Type()
)
acModuleDiagTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acModuleDiagTestMode.setStatus("current")
_AcModuleDiagStatus_Type = Integer32
_AcModuleDiagStatus_Object = MibTableColumn
acModuleDiagStatus = _AcModuleDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 19),
    _AcModuleDiagStatus_Type()
)
acModuleDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleDiagStatus.setStatus("current")


class _AcModuleDiagResultString_Type(DisplayString):
    """Custom type acModuleDiagResultString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcModuleDiagResultString_Type.__name__ = "DisplayString"
_AcModuleDiagResultString_Object = MibTableColumn
acModuleDiagResultString = _AcModuleDiagResultString_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 20),
    _AcModuleDiagResultString_Type()
)
acModuleDiagResultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleDiagResultString.setStatus("current")
_AcModuleActiveSlot_Type = AcMediaSlotNumber
_AcModuleActiveSlot_Object = MibTableColumn
acModuleActiveSlot = _AcModuleActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 21),
    _AcModuleActiveSlot_Type()
)
acModuleActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleActiveSlot.setStatus("current")
_AcModulePrimarySlot_Type = AcMediaSlotNumber
_AcModulePrimarySlot_Object = MibTableColumn
acModulePrimarySlot = _AcModulePrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 22),
    _AcModulePrimarySlot_Type()
)
acModulePrimarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModulePrimarySlot.setStatus("current")
_AcModuleBackupSlot_Type = AcMediaSlotNumber
_AcModuleBackupSlot_Object = MibTableColumn
acModuleBackupSlot = _AcModuleBackupSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 23),
    _AcModuleBackupSlot_Type()
)
acModuleBackupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModuleBackupSlot.setStatus("current")

# Managed Objects groups


# Notification objects

acModuleCfgMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 1)
)
acModuleCfgMismatchTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-MODULE-MIB", "acModuleNodeId"),
        ("APPIAN-MODULE-MIB", "acModuleSlot"),
        ("APPIAN-MODULE-MIB", "acModuleCfgType"),
        ("APPIAN-MODULE-MIB", "acModuleType"))
)
if mibBuilder.loadTexts:
    acModuleCfgMismatchTrap.setStatus(
        "current"
    )

acModuleResetFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 2)
)
acModuleResetFailedTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-MODULE-MIB", "acModuleNodeId"),
        ("APPIAN-MODULE-MIB", "acModuleReset"),
        ("APPIAN-MODULE-MIB", "acModuleSlot"))
)
if mibBuilder.loadTexts:
    acModuleResetFailedTrap.setStatus(
        "current"
    )

acModuleSwVersionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 3)
)
acModuleSwVersionTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-MODULE-MIB", "acModuleNodeId"),
        ("APPIAN-MODULE-MIB", "acModuleSlot"),
        ("APPIAN-MODULE-MIB", "acModuleSwVersion"))
)
if mibBuilder.loadTexts:
    acModuleSwVersionTrap.setStatus(
        "current"
    )

acModuleRemovalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 4)
)
acModuleRemovalTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-MODULE-MIB", "acModuleNodeId"),
        ("APPIAN-MODULE-MIB", "acModuleSlot"))
)
if mibBuilder.loadTexts:
    acModuleRemovalTrap.setStatus(
        "current"
    )

acModuleInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 5)
)
acModuleInsertedTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-MODULE-MIB", "acModuleNodeId"),
        ("APPIAN-MODULE-MIB", "acModuleSlot"),
        ("APPIAN-MODULE-MIB", "acModuleType"))
)
if mibBuilder.loadTexts:
    acModuleInsertedTrap.setStatus(
        "current"
    )

acModuleFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 6)
)
acModuleFailureTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-MODULE-MIB", "acModuleNodeId"),
        ("APPIAN-MODULE-MIB", "acModuleSlot"),
        ("APPIAN-MODULE-MIB", "acModuleType"),
        ("APPIAN-MODULE-MIB", "acModuleDiagStatus"),
        ("APPIAN-MODULE-MIB", "acModuleDiagResultString"))
)
if mibBuilder.loadTexts:
    acModuleFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-MODULE-MIB",
    **{"AcModuleType": AcModuleType,
       "AcModuleNumber": AcModuleNumber,
       "AcMediaSlotNumber": AcMediaSlotNumber,
       "acModule": acModule,
       "acModuleTraps": acModuleTraps,
       "acModuleCfgMismatchTrap": acModuleCfgMismatchTrap,
       "acModuleResetFailedTrap": acModuleResetFailedTrap,
       "acModuleSwVersionTrap": acModuleSwVersionTrap,
       "acModuleRemovalTrap": acModuleRemovalTrap,
       "acModuleInsertedTrap": acModuleInsertedTrap,
       "acModuleFailureTrap": acModuleFailureTrap,
       "acModuleTable": acModuleTable,
       "acModuleEntry": acModuleEntry,
       "acModuleNodeId": acModuleNodeId,
       "acModuleSlot": acModuleSlot,
       "acModuleNumber": acModuleNumber,
       "acModuleAdminStatus": acModuleAdminStatus,
       "acModuleCfgType": acModuleCfgType,
       "acModuleType": acModuleType,
       "acModuleOpStatus": acModuleOpStatus,
       "acModuleRevision": acModuleRevision,
       "acModuleSerialNumber": acModuleSerialNumber,
       "acModuleProductionDate": acModuleProductionDate,
       "acModuleFirmwareName": acModuleFirmwareName,
       "acModuleFirmwareRevision": acModuleFirmwareRevision,
       "acModuleNumberFailures": acModuleNumberFailures,
       "acModuleReset": acModuleReset,
       "acModuleNumberPorts": acModuleNumberPorts,
       "acModuleName": acModuleName,
       "acModuleSwVersion": acModuleSwVersion,
       "acModuleDiagTestMode": acModuleDiagTestMode,
       "acModuleDiagStatus": acModuleDiagStatus,
       "acModuleDiagResultString": acModuleDiagResultString,
       "acModuleActiveSlot": acModuleActiveSlot,
       "acModulePrimarySlot": acModulePrimarySlot,
       "acModuleBackupSlot": acModuleBackupSlot}
)
