# SNMP MIB module (StorageManagement-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/StorageManagement-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:22 2024
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



class DellStatus(Integer32):
    """Custom type DellStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1)
)
_StorageManagement_ObjectIdentity = ObjectIdentity
storageManagement = _StorageManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20)
)


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("mandatory")


class _GlobalStatus_Type(Integer32):
    """Custom type globalStatus based on Integer32"""
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
        *(("critical", 1),
          ("normal", 3),
          ("unknown", 4),
          ("warning", 2))
    )


_GlobalStatus_Type.__name__ = "Integer32"
_GlobalStatus_Object = MibScalar
globalStatus = _GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 2),
    _GlobalStatus_Type()
)
globalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatus.setStatus("mandatory")


class _SoftwareManufacturer_Type(DisplayString):
    """Custom type softwareManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SoftwareManufacturer_Type.__name__ = "DisplayString"
_SoftwareManufacturer_Object = MibScalar
softwareManufacturer = _SoftwareManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 3),
    _SoftwareManufacturer_Type()
)
softwareManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareManufacturer.setStatus("mandatory")


class _SoftwareProduct_Type(DisplayString):
    """Custom type softwareProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SoftwareProduct_Type.__name__ = "DisplayString"
_SoftwareProduct_Object = MibScalar
softwareProduct = _SoftwareProduct_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 4),
    _SoftwareProduct_Type()
)
softwareProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareProduct.setStatus("mandatory")


class _SoftwareDescription_Type(DisplayString):
    """Custom type softwareDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SoftwareDescription_Type.__name__ = "DisplayString"
_SoftwareDescription_Object = MibScalar
softwareDescription = _SoftwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 5),
    _SoftwareDescription_Type()
)
softwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareDescription.setStatus("mandatory")
_StorageManagementInfo_ObjectIdentity = ObjectIdentity
storageManagementInfo = _StorageManagementInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 100)
)
_DisplayName_Type = DisplayString
_DisplayName_Object = MibScalar
displayName = _DisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 100, 1),
    _DisplayName_Type()
)
displayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    displayName.setStatus("mandatory")
_Description_Type = DisplayString
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 100, 2),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("mandatory")
_AgentVendor_Type = DisplayString
_AgentVendor_Object = MibScalar
agentVendor = _AgentVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 100, 3),
    _AgentVendor_Type()
)
agentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVendor.setStatus("mandatory")
_AgentVersion_Type = DisplayString
_AgentVersion_Object = MibScalar
agentVersion = _AgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 100, 4),
    _AgentVersion_Type()
)
agentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVersion.setStatus("obsolete")
_GlobalData_ObjectIdentity = ObjectIdentity
globalData = _GlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110)
)


class _AgentSystemGlobalStatus_Type(Integer32):
    """Custom type agentSystemGlobalStatus based on Integer32"""
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
        *(("failure", 4),
          ("nonCriticalError", 3),
          ("normal", 1),
          ("unknown", 5),
          ("warning", 2))
    )


_AgentSystemGlobalStatus_Type.__name__ = "Integer32"
_AgentSystemGlobalStatus_Object = MibScalar
agentSystemGlobalStatus = _AgentSystemGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 1),
    _AgentSystemGlobalStatus_Type()
)
agentSystemGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSystemGlobalStatus.setStatus("obsolete")


class _AgentLastGlobalStatus_Type(Integer32):
    """Custom type agentLastGlobalStatus based on Integer32"""
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
        *(("failure", 4),
          ("nonCriticalError", 3),
          ("normal", 1),
          ("unknown", 5),
          ("warning", 2))
    )


_AgentLastGlobalStatus_Type.__name__ = "Integer32"
_AgentLastGlobalStatus_Object = MibScalar
agentLastGlobalStatus = _AgentLastGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 2),
    _AgentLastGlobalStatus_Type()
)
agentLastGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLastGlobalStatus.setStatus("obsolete")
_AgentTimeStamp_Type = Integer32
_AgentTimeStamp_Object = MibScalar
agentTimeStamp = _AgentTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 3),
    _AgentTimeStamp_Type()
)
agentTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTimeStamp.setStatus("mandatory")


class _AgentGetTimeout_Type(Integer32):
    """Custom type agentGetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AgentGetTimeout_Type.__name__ = "Integer32"
_AgentGetTimeout_Object = MibScalar
agentGetTimeout = _AgentGetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 4),
    _AgentGetTimeout_Type()
)
agentGetTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGetTimeout.setStatus("mandatory")


class _AgentModifiers_Type(Integer32):
    """Custom type agentModifiers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AgentModifiers_Type.__name__ = "Integer32"
_AgentModifiers_Object = MibScalar
agentModifiers = _AgentModifiers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 5),
    _AgentModifiers_Type()
)
agentModifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentModifiers.setStatus("mandatory")


class _AgentRefreshRate_Type(Integer32):
    """Custom type agentRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AgentRefreshRate_Type.__name__ = "Integer32"
_AgentRefreshRate_Object = MibScalar
agentRefreshRate = _AgentRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 6),
    _AgentRefreshRate_Type()
)
agentRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRefreshRate.setStatus("mandatory")
_AgentHostname_Type = DisplayString
_AgentHostname_Object = MibScalar
agentHostname = _AgentHostname_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 7),
    _AgentHostname_Type()
)
agentHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentHostname.setStatus("obsolete")
_AgentIPAddress_Type = DisplayString
_AgentIPAddress_Object = MibScalar
agentIPAddress = _AgentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 8),
    _AgentIPAddress_Type()
)
agentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIPAddress.setStatus("obsolete")


class _AgentSoftwareStatus_Type(Integer32):
    """Custom type agentSoftwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databaseDown", 2),
          ("databaseUp", 1))
    )


_AgentSoftwareStatus_Type.__name__ = "Integer32"
_AgentSoftwareStatus_Object = MibScalar
agentSoftwareStatus = _AgentSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 9),
    _AgentSoftwareStatus_Type()
)
agentSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSoftwareStatus.setStatus("obsolete")
_AgentSnmpVersion_Type = DisplayString
_AgentSnmpVersion_Object = MibScalar
agentSnmpVersion = _AgentSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 10),
    _AgentSnmpVersion_Type()
)
agentSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSnmpVersion.setStatus("obsolete")
_AgentMibVersion_Type = DisplayString
_AgentMibVersion_Object = MibScalar
agentMibVersion = _AgentMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 11),
    _AgentMibVersion_Type()
)
agentMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibVersion.setStatus("mandatory")
_AgentManagementSoftwareURLName_Type = DisplayString
_AgentManagementSoftwareURLName_Object = MibScalar
agentManagementSoftwareURLName = _AgentManagementSoftwareURLName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 12),
    _AgentManagementSoftwareURLName_Type()
)
agentManagementSoftwareURLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentManagementSoftwareURLName.setStatus("mandatory")
_AgentGlobalSystemStatus_Type = DellStatus
_AgentGlobalSystemStatus_Object = MibScalar
agentGlobalSystemStatus = _AgentGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 13),
    _AgentGlobalSystemStatus_Type()
)
agentGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGlobalSystemStatus.setStatus("mandatory")
_AgentLastGlobalSystemStatus_Type = DellStatus
_AgentLastGlobalSystemStatus_Object = MibScalar
agentLastGlobalSystemStatus = _AgentLastGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 14),
    _AgentLastGlobalSystemStatus_Type()
)
agentLastGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLastGlobalSystemStatus.setStatus("mandatory")


class _AgentSmartThermalShutdown_Type(Integer32):
    """Custom type agentSmartThermalShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_AgentSmartThermalShutdown_Type.__name__ = "Integer32"
_AgentSmartThermalShutdown_Object = MibScalar
agentSmartThermalShutdown = _AgentSmartThermalShutdown_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 110, 15),
    _AgentSmartThermalShutdown_Type()
)
agentSmartThermalShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSmartThermalShutdown.setStatus("mandatory")
_PhysicalDevices_ObjectIdentity = ObjectIdentity
physicalDevices = _PhysicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130)
)
_ControllerTable_Object = MibTable
controllerTable = _ControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1)
)
if mibBuilder.loadTexts:
    controllerTable.setStatus("mandatory")
_ControllerEntry_Object = MibTableRow
controllerEntry = _ControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1)
)
controllerEntry.setIndexNames(
    (0, "StorageManagement-MIB", "controllerNumber"),
)
if mibBuilder.loadTexts:
    controllerEntry.setStatus("mandatory")


class _ControllerNumber_Type(Integer32):
    """Custom type controllerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ControllerNumber_Type.__name__ = "Integer32"
_ControllerNumber_Object = MibTableColumn
controllerNumber = _ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 1),
    _ControllerNumber_Type()
)
controllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNumber.setStatus("mandatory")
_ControllerName_Type = DisplayString
_ControllerName_Object = MibTableColumn
controllerName = _ControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 2),
    _ControllerName_Type()
)
controllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerName.setStatus("mandatory")
_ControllerVendor_Type = DisplayString
_ControllerVendor_Object = MibTableColumn
controllerVendor = _ControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 3),
    _ControllerVendor_Type()
)
controllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerVendor.setStatus("mandatory")


class _ControllerType_Type(Integer32):
    """Custom type controllerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ide", 4),
          ("pciessd", 9),
          ("pv660F", 2),
          ("pv662F", 3),
          ("sas", 6),
          ("sata", 5),
          ("scsi", 1))
    )


_ControllerType_Type.__name__ = "Integer32"
_ControllerType_Object = MibTableColumn
controllerType = _ControllerType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 4),
    _ControllerType_Type()
)
controllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerType.setStatus("mandatory")


class _ControllerState_Type(Integer32):
    """Custom type controllerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("offline", 4),
          ("online", 3),
          ("ready", 1))
    )


_ControllerState_Type.__name__ = "Integer32"
_ControllerState_Object = MibTableColumn
controllerState = _ControllerState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 5),
    _ControllerState_Type()
)
controllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerState.setStatus("mandatory")


class _ControllerSeverity_Type(Integer32):
    """Custom type controllerSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_ControllerSeverity_Type.__name__ = "Integer32"
_ControllerSeverity_Object = MibTableColumn
controllerSeverity = _ControllerSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 6),
    _ControllerSeverity_Type()
)
controllerSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSeverity.setStatus("obsolete")


class _ControllerRebuildRateInPercent_Type(Integer32):
    """Custom type controllerRebuildRateInPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerRebuildRateInPercent_Type.__name__ = "Integer32"
_ControllerRebuildRateInPercent_Object = MibTableColumn
controllerRebuildRateInPercent = _ControllerRebuildRateInPercent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 7),
    _ControllerRebuildRateInPercent_Type()
)
controllerRebuildRateInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRebuildRateInPercent.setStatus("mandatory")
_ControllerFWVersion_Type = DisplayString
_ControllerFWVersion_Object = MibTableColumn
controllerFWVersion = _ControllerFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 8),
    _ControllerFWVersion_Type()
)
controllerFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerFWVersion.setStatus("mandatory")
_ControllerCacheSizeInMB_Type = Integer32
_ControllerCacheSizeInMB_Object = MibTableColumn
controllerCacheSizeInMB = _ControllerCacheSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 9),
    _ControllerCacheSizeInMB_Type()
)
controllerCacheSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCacheSizeInMB.setStatus("mandatory")
_ControllerCacheSizeInBytes_Type = Integer32
_ControllerCacheSizeInBytes_Object = MibTableColumn
controllerCacheSizeInBytes = _ControllerCacheSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 10),
    _ControllerCacheSizeInBytes_Type()
)
controllerCacheSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCacheSizeInBytes.setStatus("mandatory")
_ControllerPhysicalDeviceCount_Type = Integer32
_ControllerPhysicalDeviceCount_Object = MibTableColumn
controllerPhysicalDeviceCount = _ControllerPhysicalDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 11),
    _ControllerPhysicalDeviceCount_Type()
)
controllerPhysicalDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPhysicalDeviceCount.setStatus("mandatory")
_ControllerLogicalDeviceCount_Type = Integer32
_ControllerLogicalDeviceCount_Object = MibTableColumn
controllerLogicalDeviceCount = _ControllerLogicalDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 12),
    _ControllerLogicalDeviceCount_Type()
)
controllerLogicalDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerLogicalDeviceCount.setStatus("mandatory")
_ControllerPartnerStatus_Type = DisplayString
_ControllerPartnerStatus_Object = MibTableColumn
controllerPartnerStatus = _ControllerPartnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 13),
    _ControllerPartnerStatus_Type()
)
controllerPartnerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPartnerStatus.setStatus("obsolete")
_ControllerHostPortCount_Type = Integer32
_ControllerHostPortCount_Object = MibTableColumn
controllerHostPortCount = _ControllerHostPortCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 14),
    _ControllerHostPortCount_Type()
)
controllerHostPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerHostPortCount.setStatus("obsolete")
_ControllerMemorySizeInMB_Type = Integer32
_ControllerMemorySizeInMB_Object = MibTableColumn
controllerMemorySizeInMB = _ControllerMemorySizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 15),
    _ControllerMemorySizeInMB_Type()
)
controllerMemorySizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerMemorySizeInMB.setStatus("mandatory")
_ControllerMemorySizeInBytes_Type = Integer32
_ControllerMemorySizeInBytes_Object = MibTableColumn
controllerMemorySizeInBytes = _ControllerMemorySizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 16),
    _ControllerMemorySizeInBytes_Type()
)
controllerMemorySizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerMemorySizeInBytes.setStatus("mandatory")


class _ControllerDriveChannelCount_Type(Integer32):
    """Custom type controllerDriveChannelCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ControllerDriveChannelCount_Type.__name__ = "Integer32"
_ControllerDriveChannelCount_Object = MibTableColumn
controllerDriveChannelCount = _ControllerDriveChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 17),
    _ControllerDriveChannelCount_Type()
)
controllerDriveChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerDriveChannelCount.setStatus("obsolete")


class _ControllerFaultTolerant_Type(Integer32):
    """Custom type controllerFaultTolerant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_ControllerFaultTolerant_Type.__name__ = "Integer32"
_ControllerFaultTolerant_Object = MibTableColumn
controllerFaultTolerant = _ControllerFaultTolerant_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 18),
    _ControllerFaultTolerant_Type()
)
controllerFaultTolerant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerFaultTolerant.setStatus("mandatory")
_ControllerC0Port0WWN_Type = DisplayString
_ControllerC0Port0WWN_Object = MibTableColumn
controllerC0Port0WWN = _ControllerC0Port0WWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 19),
    _ControllerC0Port0WWN_Type()
)
controllerC0Port0WWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Port0WWN.setStatus("obsolete")
_ControllerC0Port0Name_Type = DisplayString
_ControllerC0Port0Name_Object = MibTableColumn
controllerC0Port0Name = _ControllerC0Port0Name_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 20),
    _ControllerC0Port0Name_Type()
)
controllerC0Port0Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Port0Name.setStatus("obsolete")
_ControllerC0Port0ID_Type = Integer32
_ControllerC0Port0ID_Object = MibTableColumn
controllerC0Port0ID = _ControllerC0Port0ID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 21),
    _ControllerC0Port0ID_Type()
)
controllerC0Port0ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Port0ID.setStatus("obsolete")
_ControllerC0Target_Type = Integer32
_ControllerC0Target_Object = MibTableColumn
controllerC0Target = _ControllerC0Target_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 22),
    _ControllerC0Target_Type()
)
controllerC0Target.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Target.setStatus("obsolete")
_ControllerC0Channel_Type = Integer32
_ControllerC0Channel_Object = MibTableColumn
controllerC0Channel = _ControllerC0Channel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 23),
    _ControllerC0Channel_Type()
)
controllerC0Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Channel.setStatus("obsolete")
_ControllerC0OSController_Type = DisplayString
_ControllerC0OSController_Object = MibTableColumn
controllerC0OSController = _ControllerC0OSController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 24),
    _ControllerC0OSController_Type()
)
controllerC0OSController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0OSController.setStatus("obsolete")


class _ControllerC0BatteryState_Type(Integer32):
    """Custom type controllerC0BatteryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              9,
              10,
              12,
              21)
        )
    )
    namedValues = NamedValues(
        *(("charging", 12),
          ("failed", 2),
          ("high", 9),
          ("low", 10),
          ("missing", 21),
          ("ok", 1),
          ("reconditioning", 7))
    )


_ControllerC0BatteryState_Type.__name__ = "Integer32"
_ControllerC0BatteryState_Object = MibTableColumn
controllerC0BatteryState = _ControllerC0BatteryState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 25),
    _ControllerC0BatteryState_Type()
)
controllerC0BatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0BatteryState.setStatus("obsolete")
_ControllerC1Port0WWN_Type = DisplayString
_ControllerC1Port0WWN_Object = MibTableColumn
controllerC1Port0WWN = _ControllerC1Port0WWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 26),
    _ControllerC1Port0WWN_Type()
)
controllerC1Port0WWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Port0WWN.setStatus("obsolete")
_ControllerC1Port0Name_Type = DisplayString
_ControllerC1Port0Name_Object = MibTableColumn
controllerC1Port0Name = _ControllerC1Port0Name_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 27),
    _ControllerC1Port0Name_Type()
)
controllerC1Port0Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Port0Name.setStatus("obsolete")
_ControllerC1Port0ID_Type = Integer32
_ControllerC1Port0ID_Object = MibTableColumn
controllerC1Port0ID = _ControllerC1Port0ID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 28),
    _ControllerC1Port0ID_Type()
)
controllerC1Port0ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Port0ID.setStatus("obsolete")
_ControllerC1Target_Type = Integer32
_ControllerC1Target_Object = MibTableColumn
controllerC1Target = _ControllerC1Target_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 29),
    _ControllerC1Target_Type()
)
controllerC1Target.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Target.setStatus("obsolete")
_ControllerC1Channel_Type = Integer32
_ControllerC1Channel_Object = MibTableColumn
controllerC1Channel = _ControllerC1Channel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 30),
    _ControllerC1Channel_Type()
)
controllerC1Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Channel.setStatus("obsolete")
_ControllerC1OSController_Type = Integer32
_ControllerC1OSController_Object = MibTableColumn
controllerC1OSController = _ControllerC1OSController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 31),
    _ControllerC1OSController_Type()
)
controllerC1OSController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1OSController.setStatus("obsolete")


class _ControllerC1BatteryState_Type(Integer32):
    """Custom type controllerC1BatteryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              9,
              10,
              12,
              21)
        )
    )
    namedValues = NamedValues(
        *(("charging", 12),
          ("failed", 2),
          ("high", 9),
          ("low", 10),
          ("missing", 21),
          ("ok", 1),
          ("reconditioning", 7))
    )


_ControllerC1BatteryState_Type.__name__ = "Integer32"
_ControllerC1BatteryState_Object = MibTableColumn
controllerC1BatteryState = _ControllerC1BatteryState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 32),
    _ControllerC1BatteryState_Type()
)
controllerC1BatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1BatteryState.setStatus("obsolete")
_ControllerNodeWWN_Type = DisplayString
_ControllerNodeWWN_Object = MibTableColumn
controllerNodeWWN = _ControllerNodeWWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 33),
    _ControllerNodeWWN_Type()
)
controllerNodeWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNodeWWN.setStatus("obsolete")
_ControllerC0Port1WWN_Type = DisplayString
_ControllerC0Port1WWN_Object = MibTableColumn
controllerC0Port1WWN = _ControllerC0Port1WWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 34),
    _ControllerC0Port1WWN_Type()
)
controllerC0Port1WWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Port1WWN.setStatus("obsolete")
_ControllerC1Port1WWN_Type = DisplayString
_ControllerC1Port1WWN_Object = MibTableColumn
controllerC1Port1WWN = _ControllerC1Port1WWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 35),
    _ControllerC1Port1WWN_Type()
)
controllerC1Port1WWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Port1WWN.setStatus("obsolete")
_ControllerBatteryChargeCount_Type = Integer32
_ControllerBatteryChargeCount_Object = MibTableColumn
controllerBatteryChargeCount = _ControllerBatteryChargeCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 36),
    _ControllerBatteryChargeCount_Type()
)
controllerBatteryChargeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBatteryChargeCount.setStatus("obsolete")
_ControllerRollUpStatus_Type = DellStatus
_ControllerRollUpStatus_Object = MibTableColumn
controllerRollUpStatus = _ControllerRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 37),
    _ControllerRollUpStatus_Type()
)
controllerRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRollUpStatus.setStatus("mandatory")
_ControllerComponentStatus_Type = DellStatus
_ControllerComponentStatus_Object = MibTableColumn
controllerComponentStatus = _ControllerComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 38),
    _ControllerComponentStatus_Type()
)
controllerComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerComponentStatus.setStatus("mandatory")
_ControllerNexusID_Type = DisplayString
_ControllerNexusID_Object = MibTableColumn
controllerNexusID = _ControllerNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 39),
    _ControllerNexusID_Type()
)
controllerNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNexusID.setStatus("mandatory")


class _ControllerAlarmState_Type(Integer32):
    """Custom type controllerAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-applicable", 3))
    )


_ControllerAlarmState_Type.__name__ = "Integer32"
_ControllerAlarmState_Object = MibTableColumn
controllerAlarmState = _ControllerAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 40),
    _ControllerAlarmState_Type()
)
controllerAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerAlarmState.setStatus("mandatory")
_ControllerDriverVersion_Type = DisplayString
_ControllerDriverVersion_Object = MibTableColumn
controllerDriverVersion = _ControllerDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 41),
    _ControllerDriverVersion_Type()
)
controllerDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerDriverVersion.setStatus("mandatory")
_ControllerPCISlot_Type = DisplayString
_ControllerPCISlot_Object = MibTableColumn
controllerPCISlot = _ControllerPCISlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 42),
    _ControllerPCISlot_Type()
)
controllerPCISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPCISlot.setStatus("mandatory")


class _ControllerClusterMode_Type(Integer32):
    """Custom type controllerClusterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 99))
    )


_ControllerClusterMode_Type.__name__ = "Integer32"
_ControllerClusterMode_Object = MibTableColumn
controllerClusterMode = _ControllerClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 43),
    _ControllerClusterMode_Type()
)
controllerClusterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerClusterMode.setStatus("mandatory")
_ControllerMinFWVersion_Type = DisplayString
_ControllerMinFWVersion_Object = MibTableColumn
controllerMinFWVersion = _ControllerMinFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 44),
    _ControllerMinFWVersion_Type()
)
controllerMinFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerMinFWVersion.setStatus("mandatory")
_ControllerMinDriverVersion_Type = DisplayString
_ControllerMinDriverVersion_Object = MibTableColumn
controllerMinDriverVersion = _ControllerMinDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 45),
    _ControllerMinDriverVersion_Type()
)
controllerMinDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerMinDriverVersion.setStatus("mandatory")
_ControllerSCSIInitiatorID_Type = Integer32
_ControllerSCSIInitiatorID_Object = MibTableColumn
controllerSCSIInitiatorID = _ControllerSCSIInitiatorID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 46),
    _ControllerSCSIInitiatorID_Type()
)
controllerSCSIInitiatorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSCSIInitiatorID.setStatus("mandatory")
_ControllerChannelCount_Type = Integer32
_ControllerChannelCount_Object = MibTableColumn
controllerChannelCount = _ControllerChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 47),
    _ControllerChannelCount_Type()
)
controllerChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerChannelCount.setStatus("mandatory")
_ControllerReconstructRate_Type = Integer32
_ControllerReconstructRate_Object = MibTableColumn
controllerReconstructRate = _ControllerReconstructRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 48),
    _ControllerReconstructRate_Type()
)
controllerReconstructRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerReconstructRate.setStatus("mandatory")
_ControllerPatrolReadRate_Type = Integer32
_ControllerPatrolReadRate_Object = MibTableColumn
controllerPatrolReadRate = _ControllerPatrolReadRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 49),
    _ControllerPatrolReadRate_Type()
)
controllerPatrolReadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadRate.setStatus("mandatory")
_ControllerBGIRate_Type = Integer32
_ControllerBGIRate_Object = MibTableColumn
controllerBGIRate = _ControllerBGIRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 50),
    _ControllerBGIRate_Type()
)
controllerBGIRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBGIRate.setStatus("mandatory")
_ControllerCheckConsistencyRate_Type = Integer32
_ControllerCheckConsistencyRate_Object = MibTableColumn
controllerCheckConsistencyRate = _ControllerCheckConsistencyRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 51),
    _ControllerCheckConsistencyRate_Type()
)
controllerCheckConsistencyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCheckConsistencyRate.setStatus("mandatory")


class _ControllerPatrolReadMode_Type(Integer32):
    """Custom type controllerPatrolReadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("disabled", 3),
          ("manual", 2))
    )


_ControllerPatrolReadMode_Type.__name__ = "Integer32"
_ControllerPatrolReadMode_Object = MibTableColumn
controllerPatrolReadMode = _ControllerPatrolReadMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 52),
    _ControllerPatrolReadMode_Type()
)
controllerPatrolReadMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadMode.setStatus("mandatory")


class _ControllerPatrolReadState_Type(Integer32):
    """Custom type controllerPatrolReadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 8),
          ("active", 4),
          ("ready", 2),
          ("stopped", 1))
    )


_ControllerPatrolReadState_Type.__name__ = "Integer32"
_ControllerPatrolReadState_Object = MibTableColumn
controllerPatrolReadState = _ControllerPatrolReadState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 53),
    _ControllerPatrolReadState_Type()
)
controllerPatrolReadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadState.setStatus("mandatory")
_ControllerPatrolReadIterations_Type = Integer32
_ControllerPatrolReadIterations_Object = MibTableColumn
controllerPatrolReadIterations = _ControllerPatrolReadIterations_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 54),
    _ControllerPatrolReadIterations_Type()
)
controllerPatrolReadIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadIterations.setStatus("mandatory")
_ControllerStorportDriverVersion_Type = DisplayString
_ControllerStorportDriverVersion_Object = MibTableColumn
controllerStorportDriverVersion = _ControllerStorportDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 55),
    _ControllerStorportDriverVersion_Type()
)
controllerStorportDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerStorportDriverVersion.setStatus("mandatory")
_ControllerMinRequiredStorportVer_Type = DisplayString
_ControllerMinRequiredStorportVer_Object = MibTableColumn
controllerMinRequiredStorportVer = _ControllerMinRequiredStorportVer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 56),
    _ControllerMinRequiredStorportVer_Type()
)
controllerMinRequiredStorportVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerMinRequiredStorportVer.setStatus("mandatory")
_ControllerEncryptionCapable_Type = Integer32
_ControllerEncryptionCapable_Object = MibTableColumn
controllerEncryptionCapable = _ControllerEncryptionCapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 57),
    _ControllerEncryptionCapable_Type()
)
controllerEncryptionCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEncryptionCapable.setStatus("mandatory")
_ControllerEncryptionKeyPresent_Type = Integer32
_ControllerEncryptionKeyPresent_Object = MibTableColumn
controllerEncryptionKeyPresent = _ControllerEncryptionKeyPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 58),
    _ControllerEncryptionKeyPresent_Type()
)
controllerEncryptionKeyPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controllerEncryptionKeyPresent.setStatus("mandatory")


class _ControllerPersistentHotSpare_Type(Integer32):
    """Custom type controllerPersistentHotSpare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ControllerPersistentHotSpare_Type.__name__ = "Integer32"
_ControllerPersistentHotSpare_Object = MibTableColumn
controllerPersistentHotSpare = _ControllerPersistentHotSpare_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 59),
    _ControllerPersistentHotSpare_Type()
)
controllerPersistentHotSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPersistentHotSpare.setStatus("mandatory")


class _ControllerSpinDownUnconfiguredDrives_Type(Integer32):
    """Custom type controllerSpinDownUnconfiguredDrives based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ControllerSpinDownUnconfiguredDrives_Type.__name__ = "Integer32"
_ControllerSpinDownUnconfiguredDrives_Object = MibTableColumn
controllerSpinDownUnconfiguredDrives = _ControllerSpinDownUnconfiguredDrives_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 60),
    _ControllerSpinDownUnconfiguredDrives_Type()
)
controllerSpinDownUnconfiguredDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownUnconfiguredDrives.setStatus("mandatory")


class _ControllerSpinDownHotSpareDrives_Type(Integer32):
    """Custom type controllerSpinDownHotSpareDrives based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ControllerSpinDownHotSpareDrives_Type.__name__ = "Integer32"
_ControllerSpinDownHotSpareDrives_Object = MibTableColumn
controllerSpinDownHotSpareDrives = _ControllerSpinDownHotSpareDrives_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 61),
    _ControllerSpinDownHotSpareDrives_Type()
)
controllerSpinDownHotSpareDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownHotSpareDrives.setStatus("mandatory")


class _ControllerSpinDownTimeInterval_Type(Integer32):
    """Custom type controllerSpinDownTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_ControllerSpinDownTimeInterval_Type.__name__ = "Integer32"
_ControllerSpinDownTimeInterval_Object = MibTableColumn
controllerSpinDownTimeInterval = _ControllerSpinDownTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 62),
    _ControllerSpinDownTimeInterval_Type()
)
controllerSpinDownTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controllerSpinDownTimeInterval.setStatus("mandatory")
_ControllerEncryptionMode_Type = Integer32
_ControllerEncryptionMode_Object = MibTableColumn
controllerEncryptionMode = _ControllerEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 63),
    _ControllerEncryptionMode_Type()
)
controllerEncryptionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEncryptionMode.setStatus("mandatory")
_ControllerCacheCade_Type = Integer32
_ControllerCacheCade_Object = MibTableColumn
controllerCacheCade = _ControllerCacheCade_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 64),
    _ControllerCacheCade_Type()
)
controllerCacheCade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCacheCade.setStatus("mandatory")
_ControllerSpinDownConfiguredDrives_Type = Integer32
_ControllerSpinDownConfiguredDrives_Object = MibTableColumn
controllerSpinDownConfiguredDrives = _ControllerSpinDownConfiguredDrives_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 65),
    _ControllerSpinDownConfiguredDrives_Type()
)
controllerSpinDownConfiguredDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownConfiguredDrives.setStatus("mandatory")
_ControllerAutomaticPowerSaving_Type = Integer32
_ControllerAutomaticPowerSaving_Object = MibTableColumn
controllerAutomaticPowerSaving = _ControllerAutomaticPowerSaving_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 66),
    _ControllerAutomaticPowerSaving_Type()
)
controllerAutomaticPowerSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerAutomaticPowerSaving.setStatus("mandatory")
_ControllerConfiguredDrivesSpinUpTime_Type = DisplayString
_ControllerConfiguredDrivesSpinUpTime_Object = MibTableColumn
controllerConfiguredDrivesSpinUpTime = _ControllerConfiguredDrivesSpinUpTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 67),
    _ControllerConfiguredDrivesSpinUpTime_Type()
)
controllerConfiguredDrivesSpinUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerConfiguredDrivesSpinUpTime.setStatus("mandatory")


class _ControllerConfiguredDrivesSpinUpTimeInterval_Type(Integer32):
    """Custom type controllerConfiguredDrivesSpinUpTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_ControllerConfiguredDrivesSpinUpTimeInterval_Type.__name__ = "Integer32"
_ControllerConfiguredDrivesSpinUpTimeInterval_Object = MibTableColumn
controllerConfiguredDrivesSpinUpTimeInterval = _ControllerConfiguredDrivesSpinUpTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 68),
    _ControllerConfiguredDrivesSpinUpTimeInterval_Type()
)
controllerConfiguredDrivesSpinUpTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerConfiguredDrivesSpinUpTimeInterval.setStatus("mandatory")
_ControllerPreservedCache_Type = Integer32
_ControllerPreservedCache_Object = MibTableColumn
controllerPreservedCache = _ControllerPreservedCache_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 69),
    _ControllerPreservedCache_Type()
)
controllerPreservedCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPreservedCache.setStatus("mandatory")
_ControllerPIEnable_Type = Integer32
_ControllerPIEnable_Object = MibTableColumn
controllerPIEnable = _ControllerPIEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 1, 1, 70),
    _ControllerPIEnable_Type()
)
controllerPIEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPIEnable.setStatus("mandatory")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("mandatory")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1)
)
channelEntry.setIndexNames(
    (0, "StorageManagement-MIB", "channelNumber"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("mandatory")


class _ChannelNumber_Type(Integer32):
    """Custom type channelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChannelNumber_Type.__name__ = "Integer32"
_ChannelNumber_Object = MibTableColumn
channelNumber = _ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 1),
    _ChannelNumber_Type()
)
channelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumber.setStatus("mandatory")
_ChannelName_Type = DisplayString
_ChannelName_Object = MibTableColumn
channelName = _ChannelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 2),
    _ChannelName_Type()
)
channelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelName.setStatus("mandatory")


class _ChannelState_Type(Integer32):
    """Custom type channelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("offline", 4),
          ("online", 3),
          ("ready", 1))
    )


_ChannelState_Type.__name__ = "Integer32"
_ChannelState_Object = MibTableColumn
channelState = _ChannelState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 3),
    _ChannelState_Type()
)
channelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelState.setStatus("mandatory")


class _ChannelSeverity_Type(Integer32):
    """Custom type channelSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_ChannelSeverity_Type.__name__ = "Integer32"
_ChannelSeverity_Object = MibTableColumn
channelSeverity = _ChannelSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 4),
    _ChannelSeverity_Type()
)
channelSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelSeverity.setStatus("obsolete")


class _ChannelTermination_Type(Integer32):
    """Custom type channelTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 2),
          ("notTerminated", 3),
          ("wide", 1))
    )


_ChannelTermination_Type.__name__ = "Integer32"
_ChannelTermination_Object = MibTableColumn
channelTermination = _ChannelTermination_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 5),
    _ChannelTermination_Type()
)
channelTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelTermination.setStatus("mandatory")
_ChannelSCSIID_Type = Integer32
_ChannelSCSIID_Object = MibTableColumn
channelSCSIID = _ChannelSCSIID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 6),
    _ChannelSCSIID_Type()
)
channelSCSIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelSCSIID.setStatus("mandatory")
_ChannelRollUpStatus_Type = DellStatus
_ChannelRollUpStatus_Object = MibTableColumn
channelRollUpStatus = _ChannelRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 7),
    _ChannelRollUpStatus_Type()
)
channelRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelRollUpStatus.setStatus("mandatory")
_ChannelComponentStatus_Type = DellStatus
_ChannelComponentStatus_Object = MibTableColumn
channelComponentStatus = _ChannelComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 8),
    _ChannelComponentStatus_Type()
)
channelComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelComponentStatus.setStatus("mandatory")
_ChannelNexusID_Type = DisplayString
_ChannelNexusID_Object = MibTableColumn
channelNexusID = _ChannelNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 9),
    _ChannelNexusID_Type()
)
channelNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNexusID.setStatus("mandatory")
_ChannelDataRate_Type = DisplayString
_ChannelDataRate_Object = MibTableColumn
channelDataRate = _ChannelDataRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 10),
    _ChannelDataRate_Type()
)
channelDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelDataRate.setStatus("mandatory")


class _ChannelBusType_Type(Integer32):
    """Custom type channelBusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("fibreChannel", 3),
          ("ide", 2),
          ("pcie", 9),
          ("sas", 8),
          ("sata", 7),
          ("scsi", 1),
          ("ssa", 4),
          ("usb", 6))
    )


_ChannelBusType_Type.__name__ = "Integer32"
_ChannelBusType_Object = MibTableColumn
channelBusType = _ChannelBusType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 2, 1, 11),
    _ChannelBusType_Type()
)
channelBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBusType.setStatus("mandatory")
_EnclosureTable_Object = MibTable
enclosureTable = _EnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3)
)
if mibBuilder.loadTexts:
    enclosureTable.setStatus("mandatory")
_EnclosureEntry_Object = MibTableRow
enclosureEntry = _EnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1)
)
enclosureEntry.setIndexNames(
    (0, "StorageManagement-MIB", "enclosureNumber"),
)
if mibBuilder.loadTexts:
    enclosureEntry.setStatus("mandatory")


class _EnclosureNumber_Type(Integer32):
    """Custom type enclosureNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EnclosureNumber_Type.__name__ = "Integer32"
_EnclosureNumber_Object = MibTableColumn
enclosureNumber = _EnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 1),
    _EnclosureNumber_Type()
)
enclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNumber.setStatus("mandatory")
_EnclosureName_Type = DisplayString
_EnclosureName_Object = MibTableColumn
enclosureName = _EnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 2),
    _EnclosureName_Type()
)
enclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureName.setStatus("mandatory")
_EnclosureVendor_Type = DisplayString
_EnclosureVendor_Object = MibTableColumn
enclosureVendor = _EnclosureVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 3),
    _EnclosureVendor_Type()
)
enclosureVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureVendor.setStatus("mandatory")


class _EnclosureState_Type(Integer32):
    """Custom type enclosureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("offline", 4),
          ("online", 3),
          ("ready", 1))
    )


_EnclosureState_Type.__name__ = "Integer32"
_EnclosureState_Object = MibTableColumn
enclosureState = _EnclosureState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 4),
    _EnclosureState_Type()
)
enclosureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureState.setStatus("mandatory")


class _EnclosureSeverity_Type(Integer32):
    """Custom type enclosureSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_EnclosureSeverity_Type.__name__ = "Integer32"
_EnclosureSeverity_Object = MibTableColumn
enclosureSeverity = _EnclosureSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 5),
    _EnclosureSeverity_Type()
)
enclosureSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSeverity.setStatus("obsolete")
_EnclosureID_Type = DisplayString
_EnclosureID_Object = MibTableColumn
enclosureID = _EnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 6),
    _EnclosureID_Type()
)
enclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureID.setStatus("mandatory")
_EnclosureProcessorVersion_Type = DisplayString
_EnclosureProcessorVersion_Object = MibTableColumn
enclosureProcessorVersion = _EnclosureProcessorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 7),
    _EnclosureProcessorVersion_Type()
)
enclosureProcessorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureProcessorVersion.setStatus("obsolete")
_EnclosureServiceTag_Type = DisplayString
_EnclosureServiceTag_Object = MibTableColumn
enclosureServiceTag = _EnclosureServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 8),
    _EnclosureServiceTag_Type()
)
enclosureServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureServiceTag.setStatus("mandatory")
_EnclosureAssetTag_Type = DisplayString
_EnclosureAssetTag_Object = MibTableColumn
enclosureAssetTag = _EnclosureAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 9),
    _EnclosureAssetTag_Type()
)
enclosureAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAssetTag.setStatus("mandatory")
_EnclosureAssetName_Type = DisplayString
_EnclosureAssetName_Object = MibTableColumn
enclosureAssetName = _EnclosureAssetName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 10),
    _EnclosureAssetName_Type()
)
enclosureAssetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAssetName.setStatus("mandatory")
_EnclosureSplitBusPartNumber_Type = DisplayString
_EnclosureSplitBusPartNumber_Object = MibTableColumn
enclosureSplitBusPartNumber = _EnclosureSplitBusPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 11),
    _EnclosureSplitBusPartNumber_Type()
)
enclosureSplitBusPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSplitBusPartNumber.setStatus("mandatory")
_EnclosureProductID_Type = DisplayString
_EnclosureProductID_Object = MibTableColumn
enclosureProductID = _EnclosureProductID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 12),
    _EnclosureProductID_Type()
)
enclosureProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureProductID.setStatus("mandatory")
_EnclosureKernelVersion_Type = DisplayString
_EnclosureKernelVersion_Object = MibTableColumn
enclosureKernelVersion = _EnclosureKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 13),
    _EnclosureKernelVersion_Type()
)
enclosureKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureKernelVersion.setStatus("obsolete")
_EnclosureESM1PartNumber_Type = DisplayString
_EnclosureESM1PartNumber_Object = MibTableColumn
enclosureESM1PartNumber = _EnclosureESM1PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 14),
    _EnclosureESM1PartNumber_Type()
)
enclosureESM1PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureESM1PartNumber.setStatus("obsolete")
_EnclosureESM2PartNumber_Type = DisplayString
_EnclosureESM2PartNumber_Object = MibTableColumn
enclosureESM2PartNumber = _EnclosureESM2PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 15),
    _EnclosureESM2PartNumber_Type()
)
enclosureESM2PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureESM2PartNumber.setStatus("obsolete")


class _EnclosureType_Type(Integer32):
    """Custom type enclosureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("dELLPV200SPV201S", 2),
          ("dELLPV210SPV211S", 3),
          ("dELLPV220SPV221S", 4),
          ("dELLPV224F", 6),
          ("dELLPV660F", 5),
          ("dELLPV660F224F", 7),
          ("internal", 1),
          ("md1000", 8),
          ("md1120", 9),
          ("md1200", 10),
          ("md1220", 11))
    )


_EnclosureType_Type.__name__ = "Integer32"
_EnclosureType_Object = MibTableColumn
enclosureType = _EnclosureType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 16),
    _EnclosureType_Type()
)
enclosureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureType.setStatus("mandatory")
_EnclosureProcessor2Version_Type = DisplayString
_EnclosureProcessor2Version_Object = MibTableColumn
enclosureProcessor2Version = _EnclosureProcessor2Version_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 17),
    _EnclosureProcessor2Version_Type()
)
enclosureProcessor2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureProcessor2Version.setStatus("mandatory")


class _EnclosureConfig_Type(Integer32):
    """Custom type enclosureConfig based on Integer32"""
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
        *(("clustered", 3),
          ("joined", 1),
          ("splitBus", 2),
          ("unified", 4))
    )


_EnclosureConfig_Type.__name__ = "Integer32"
_EnclosureConfig_Object = MibTableColumn
enclosureConfig = _EnclosureConfig_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 18),
    _EnclosureConfig_Type()
)
enclosureConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureConfig.setStatus("mandatory")
_EnclosureChannelNumber_Type = Integer32
_EnclosureChannelNumber_Object = MibTableColumn
enclosureChannelNumber = _EnclosureChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 19),
    _EnclosureChannelNumber_Type()
)
enclosureChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureChannelNumber.setStatus("mandatory")


class _EnclosureAlarm_Type(Integer32):
    """Custom type enclosureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EnclosureAlarm_Type.__name__ = "Integer32"
_EnclosureAlarm_Object = MibTableColumn
enclosureAlarm = _EnclosureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 20),
    _EnclosureAlarm_Type()
)
enclosureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAlarm.setStatus("mandatory")
_EnclosureBackplanePartNumber_Type = DisplayString
_EnclosureBackplanePartNumber_Object = MibTableColumn
enclosureBackplanePartNumber = _EnclosureBackplanePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 21),
    _EnclosureBackplanePartNumber_Type()
)
enclosureBackplanePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureBackplanePartNumber.setStatus("mandatory")
_EnclosureSCSIID_Type = Integer32
_EnclosureSCSIID_Object = MibTableColumn
enclosureSCSIID = _EnclosureSCSIID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 22),
    _EnclosureSCSIID_Type()
)
enclosureSCSIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSCSIID.setStatus("mandatory")
_EnclosureRollUpStatus_Type = DellStatus
_EnclosureRollUpStatus_Object = MibTableColumn
enclosureRollUpStatus = _EnclosureRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 23),
    _EnclosureRollUpStatus_Type()
)
enclosureRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureRollUpStatus.setStatus("mandatory")
_EnclosureComponentStatus_Type = DellStatus
_EnclosureComponentStatus_Object = MibTableColumn
enclosureComponentStatus = _EnclosureComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 24),
    _EnclosureComponentStatus_Type()
)
enclosureComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureComponentStatus.setStatus("mandatory")
_EnclosureNexusID_Type = DisplayString
_EnclosureNexusID_Object = MibTableColumn
enclosureNexusID = _EnclosureNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 25),
    _EnclosureNexusID_Type()
)
enclosureNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNexusID.setStatus("mandatory")
_EnclosureFirmwareVersion_Type = DisplayString
_EnclosureFirmwareVersion_Object = MibTableColumn
enclosureFirmwareVersion = _EnclosureFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 26),
    _EnclosureFirmwareVersion_Type()
)
enclosureFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFirmwareVersion.setStatus("mandatory")
_EnclosureSCSIRate_Type = DisplayString
_EnclosureSCSIRate_Object = MibTableColumn
enclosureSCSIRate = _EnclosureSCSIRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 27),
    _EnclosureSCSIRate_Type()
)
enclosureSCSIRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSCSIRate.setStatus("mandatory")
_EnclosurePartNumber_Type = DisplayString
_EnclosurePartNumber_Object = MibTableColumn
enclosurePartNumber = _EnclosurePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 28),
    _EnclosurePartNumber_Type()
)
enclosurePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePartNumber.setStatus("mandatory")
_EnclosureSerialNumber_Type = DisplayString
_EnclosureSerialNumber_Object = MibTableColumn
enclosureSerialNumber = _EnclosureSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 29),
    _EnclosureSerialNumber_Type()
)
enclosureSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSerialNumber.setStatus("mandatory")
_EnclosureSASAddress_Type = DisplayString
_EnclosureSASAddress_Object = MibTableColumn
enclosureSASAddress = _EnclosureSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 30),
    _EnclosureSASAddress_Type()
)
enclosureSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSASAddress.setStatus("mandatory")
_EnclosureOccupiedSlotCount_Type = Integer32
_EnclosureOccupiedSlotCount_Object = MibTableColumn
enclosureOccupiedSlotCount = _EnclosureOccupiedSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 31),
    _EnclosureOccupiedSlotCount_Type()
)
enclosureOccupiedSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureOccupiedSlotCount.setStatus("mandatory")
_EnclosureTotalSlots_Type = Integer32
_EnclosureTotalSlots_Object = MibTableColumn
enclosureTotalSlots = _EnclosureTotalSlots_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 32),
    _EnclosureTotalSlots_Type()
)
enclosureTotalSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTotalSlots.setStatus("mandatory")
_EnclosureEmptySlotCount_Type = Integer32
_EnclosureEmptySlotCount_Object = MibTableColumn
enclosureEmptySlotCount = _EnclosureEmptySlotCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 33),
    _EnclosureEmptySlotCount_Type()
)
enclosureEmptySlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureEmptySlotCount.setStatus("mandatory")
_EnclosureExpressServiceCode_Type = DisplayString
_EnclosureExpressServiceCode_Object = MibTableColumn
enclosureExpressServiceCode = _EnclosureExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 3, 1, 34),
    _EnclosureExpressServiceCode_Type()
)
enclosureExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureExpressServiceCode.setStatus("mandatory")
_ArrayDiskTable_Object = MibTable
arrayDiskTable = _ArrayDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4)
)
if mibBuilder.loadTexts:
    arrayDiskTable.setStatus("mandatory")
_ArrayDiskEntry_Object = MibTableRow
arrayDiskEntry = _ArrayDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1)
)
arrayDiskEntry.setIndexNames(
    (0, "StorageManagement-MIB", "arrayDiskNumber"),
)
if mibBuilder.loadTexts:
    arrayDiskEntry.setStatus("mandatory")


class _ArrayDiskNumber_Type(Integer32):
    """Custom type arrayDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_ArrayDiskNumber_Type.__name__ = "Integer32"
_ArrayDiskNumber_Object = MibTableColumn
arrayDiskNumber = _ArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 1),
    _ArrayDiskNumber_Type()
)
arrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskNumber.setStatus("mandatory")
_ArrayDiskName_Type = DisplayString
_ArrayDiskName_Object = MibTableColumn
arrayDiskName = _ArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 2),
    _ArrayDiskName_Type()
)
arrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskName.setStatus("mandatory")
_ArrayDiskVendor_Type = DisplayString
_ArrayDiskVendor_Object = MibTableColumn
arrayDiskVendor = _ArrayDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 3),
    _ArrayDiskVendor_Type()
)
arrayDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskVendor.setStatus("mandatory")


class _ArrayDiskState_Type(Integer32):
    """Custom type arrayDiskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              11,
              13,
              14,
              15,
              22,
              23,
              24,
              25,
              26,
              28,
              34,
              35,
              39,
              40,
              41,
              53,
              56)
        )
    )
    namedValues = NamedValues(
        *(("clear", 40),
          ("degraded", 6),
          ("diagnostics", 28),
          ("failed", 2),
          ("foreign", 39),
          ("formatting", 26),
          ("incompatible", 53),
          ("initializing", 35),
          ("noMedia", 25),
          ("non-raid", 13),
          ("notReady", 14),
          ("offline", 4),
          ("online", 3),
          ("predictiveFailure", 34),
          ("readOnly", 56),
          ("ready", 1),
          ("rebuild", 24),
          ("recovering", 7),
          ("removed", 11),
          ("replacing", 22),
          ("resynching", 15),
          ("spinningDown", 23),
          ("unsupported", 41))
    )


_ArrayDiskState_Type.__name__ = "Integer32"
_ArrayDiskState_Object = MibTableColumn
arrayDiskState = _ArrayDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 4),
    _ArrayDiskState_Type()
)
arrayDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskState.setStatus("mandatory")


class _ArrayDiskSeverity_Type(Integer32):
    """Custom type arrayDiskSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_ArrayDiskSeverity_Type.__name__ = "Integer32"
_ArrayDiskSeverity_Object = MibTableColumn
arrayDiskSeverity = _ArrayDiskSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 5),
    _ArrayDiskSeverity_Type()
)
arrayDiskSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskSeverity.setStatus("obsolete")
_ArrayDiskProductID_Type = DisplayString
_ArrayDiskProductID_Object = MibTableColumn
arrayDiskProductID = _ArrayDiskProductID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 6),
    _ArrayDiskProductID_Type()
)
arrayDiskProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskProductID.setStatus("mandatory")
_ArrayDiskSerialNo_Type = DisplayString
_ArrayDiskSerialNo_Object = MibTableColumn
arrayDiskSerialNo = _ArrayDiskSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 7),
    _ArrayDiskSerialNo_Type()
)
arrayDiskSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskSerialNo.setStatus("mandatory")
_ArrayDiskRevision_Type = DisplayString
_ArrayDiskRevision_Object = MibTableColumn
arrayDiskRevision = _ArrayDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 8),
    _ArrayDiskRevision_Type()
)
arrayDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskRevision.setStatus("mandatory")
_ArrayDiskEnclosureID_Type = DisplayString
_ArrayDiskEnclosureID_Object = MibTableColumn
arrayDiskEnclosureID = _ArrayDiskEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 9),
    _ArrayDiskEnclosureID_Type()
)
arrayDiskEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureID.setStatus("mandatory")
_ArrayDiskChannel_Type = Integer32
_ArrayDiskChannel_Object = MibTableColumn
arrayDiskChannel = _ArrayDiskChannel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 10),
    _ArrayDiskChannel_Type()
)
arrayDiskChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannel.setStatus("mandatory")
_ArrayDiskLengthInMB_Type = Integer32
_ArrayDiskLengthInMB_Object = MibTableColumn
arrayDiskLengthInMB = _ArrayDiskLengthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 11),
    _ArrayDiskLengthInMB_Type()
)
arrayDiskLengthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLengthInMB.setStatus("mandatory")
_ArrayDiskLengthInBytes_Type = Integer32
_ArrayDiskLengthInBytes_Object = MibTableColumn
arrayDiskLengthInBytes = _ArrayDiskLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 12),
    _ArrayDiskLengthInBytes_Type()
)
arrayDiskLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLengthInBytes.setStatus("mandatory")
_ArrayDiskLargestContiguousFreeSpaceInMB_Type = Integer32
_ArrayDiskLargestContiguousFreeSpaceInMB_Object = MibTableColumn
arrayDiskLargestContiguousFreeSpaceInMB = _ArrayDiskLargestContiguousFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 13),
    _ArrayDiskLargestContiguousFreeSpaceInMB_Type()
)
arrayDiskLargestContiguousFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLargestContiguousFreeSpaceInMB.setStatus("mandatory")
_ArrayDiskLargestContiguousFreeSpaceInBytes_Type = Integer32
_ArrayDiskLargestContiguousFreeSpaceInBytes_Object = MibTableColumn
arrayDiskLargestContiguousFreeSpaceInBytes = _ArrayDiskLargestContiguousFreeSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 14),
    _ArrayDiskLargestContiguousFreeSpaceInBytes_Type()
)
arrayDiskLargestContiguousFreeSpaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLargestContiguousFreeSpaceInBytes.setStatus("mandatory")


class _ArrayDiskTargetID_Type(Integer32):
    """Custom type arrayDiskTargetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ArrayDiskTargetID_Type.__name__ = "Integer32"
_ArrayDiskTargetID_Object = MibTableColumn
arrayDiskTargetID = _ArrayDiskTargetID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 15),
    _ArrayDiskTargetID_Type()
)
arrayDiskTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskTargetID.setStatus("mandatory")
_ArrayDiskLunID_Type = Integer32
_ArrayDiskLunID_Object = MibTableColumn
arrayDiskLunID = _ArrayDiskLunID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 16),
    _ArrayDiskLunID_Type()
)
arrayDiskLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLunID.setStatus("mandatory")
_ArrayDiskUsedSpaceInMB_Type = Integer32
_ArrayDiskUsedSpaceInMB_Object = MibTableColumn
arrayDiskUsedSpaceInMB = _ArrayDiskUsedSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 17),
    _ArrayDiskUsedSpaceInMB_Type()
)
arrayDiskUsedSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskUsedSpaceInMB.setStatus("mandatory")
_ArrayDiskUsedSpaceInBytes_Type = Integer32
_ArrayDiskUsedSpaceInBytes_Object = MibTableColumn
arrayDiskUsedSpaceInBytes = _ArrayDiskUsedSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 18),
    _ArrayDiskUsedSpaceInBytes_Type()
)
arrayDiskUsedSpaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskUsedSpaceInBytes.setStatus("mandatory")
_ArrayDiskFreeSpaceInMB_Type = Integer32
_ArrayDiskFreeSpaceInMB_Object = MibTableColumn
arrayDiskFreeSpaceInMB = _ArrayDiskFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 19),
    _ArrayDiskFreeSpaceInMB_Type()
)
arrayDiskFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskFreeSpaceInMB.setStatus("mandatory")
_ArrayDiskFreeSpaceInBytes_Type = Integer32
_ArrayDiskFreeSpaceInBytes_Object = MibTableColumn
arrayDiskFreeSpaceInBytes = _ArrayDiskFreeSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 20),
    _ArrayDiskFreeSpaceInBytes_Type()
)
arrayDiskFreeSpaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskFreeSpaceInBytes.setStatus("mandatory")


class _ArrayDiskBusType_Type(Integer32):
    """Custom type arrayDiskBusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("fibre", 3),
          ("ide", 2),
          ("pcie", 9),
          ("sas", 8),
          ("sata", 7),
          ("scsi", 1),
          ("ssa", 4),
          ("usb", 6))
    )


_ArrayDiskBusType_Type.__name__ = "Integer32"
_ArrayDiskBusType_Object = MibTableColumn
arrayDiskBusType = _ArrayDiskBusType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 21),
    _ArrayDiskBusType_Type()
)
arrayDiskBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskBusType.setStatus("mandatory")


class _ArrayDiskSpareState_Type(Integer32):
    """Custom type arrayDiskSpareState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dedicatedHotSpare", 4),
          ("globalHotSpare", 3),
          ("memberDG", 2),
          ("memberVD", 1),
          ("notASpare", 5),
          ("notApplicable", 99))
    )


_ArrayDiskSpareState_Type.__name__ = "Integer32"
_ArrayDiskSpareState_Object = MibTableColumn
arrayDiskSpareState = _ArrayDiskSpareState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 22),
    _ArrayDiskSpareState_Type()
)
arrayDiskSpareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskSpareState.setStatus("mandatory")
_ArrayDiskRollUpStatus_Type = DellStatus
_ArrayDiskRollUpStatus_Object = MibTableColumn
arrayDiskRollUpStatus = _ArrayDiskRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 23),
    _ArrayDiskRollUpStatus_Type()
)
arrayDiskRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskRollUpStatus.setStatus("mandatory")
_ArrayDiskComponentStatus_Type = DellStatus
_ArrayDiskComponentStatus_Object = MibTableColumn
arrayDiskComponentStatus = _ArrayDiskComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 24),
    _ArrayDiskComponentStatus_Type()
)
arrayDiskComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskComponentStatus.setStatus("mandatory")
_ArrayDiskDeviceName_Type = DisplayString
_ArrayDiskDeviceName_Object = MibTableColumn
arrayDiskDeviceName = _ArrayDiskDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 25),
    _ArrayDiskDeviceName_Type()
)
arrayDiskDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskDeviceName.setStatus("mandatory")
_ArrayDiskNexusID_Type = DisplayString
_ArrayDiskNexusID_Object = MibTableColumn
arrayDiskNexusID = _ArrayDiskNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 26),
    _ArrayDiskNexusID_Type()
)
arrayDiskNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskNexusID.setStatus("mandatory")
_ArrayDiskPartNumber_Type = DisplayString
_ArrayDiskPartNumber_Object = MibTableColumn
arrayDiskPartNumber = _ArrayDiskPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 27),
    _ArrayDiskPartNumber_Type()
)
arrayDiskPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskPartNumber.setStatus("mandatory")
_ArrayDiskSASAddress_Type = DisplayString
_ArrayDiskSASAddress_Object = MibTableColumn
arrayDiskSASAddress = _ArrayDiskSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 28),
    _ArrayDiskSASAddress_Type()
)
arrayDiskSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskSASAddress.setStatus("mandatory")
_ArrayDiskNegotiatedSpeed_Type = Integer32
_ArrayDiskNegotiatedSpeed_Object = MibTableColumn
arrayDiskNegotiatedSpeed = _ArrayDiskNegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 29),
    _ArrayDiskNegotiatedSpeed_Type()
)
arrayDiskNegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskNegotiatedSpeed.setStatus("mandatory")
_ArrayDiskCapableSpeed_Type = Integer32
_ArrayDiskCapableSpeed_Object = MibTableColumn
arrayDiskCapableSpeed = _ArrayDiskCapableSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 30),
    _ArrayDiskCapableSpeed_Type()
)
arrayDiskCapableSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskCapableSpeed.setStatus("mandatory")


class _ArrayDiskSmartAlertIndication_Type(Integer32):
    """Custom type arrayDiskSmartAlertIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ArrayDiskSmartAlertIndication_Type.__name__ = "Integer32"
_ArrayDiskSmartAlertIndication_Object = MibTableColumn
arrayDiskSmartAlertIndication = _ArrayDiskSmartAlertIndication_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 31),
    _ArrayDiskSmartAlertIndication_Type()
)
arrayDiskSmartAlertIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskSmartAlertIndication.setStatus("mandatory")
_ArrayDiskManufactureDay_Type = DisplayString
_ArrayDiskManufactureDay_Object = MibTableColumn
arrayDiskManufactureDay = _ArrayDiskManufactureDay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 32),
    _ArrayDiskManufactureDay_Type()
)
arrayDiskManufactureDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskManufactureDay.setStatus("mandatory")
_ArrayDiskManufactureWeek_Type = DisplayString
_ArrayDiskManufactureWeek_Object = MibTableColumn
arrayDiskManufactureWeek = _ArrayDiskManufactureWeek_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 33),
    _ArrayDiskManufactureWeek_Type()
)
arrayDiskManufactureWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskManufactureWeek.setStatus("mandatory")
_ArrayDiskManufactureYear_Type = DisplayString
_ArrayDiskManufactureYear_Object = MibTableColumn
arrayDiskManufactureYear = _ArrayDiskManufactureYear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 34),
    _ArrayDiskManufactureYear_Type()
)
arrayDiskManufactureYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskManufactureYear.setStatus("mandatory")


class _ArrayDiskMediaType_Type(Integer32):
    """Custom type arrayDiskMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdd", 2),
          ("ssd", 3),
          ("unknown", 1))
    )


_ArrayDiskMediaType_Type.__name__ = "Integer32"
_ArrayDiskMediaType_Object = MibTableColumn
arrayDiskMediaType = _ArrayDiskMediaType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 35),
    _ArrayDiskMediaType_Type()
)
arrayDiskMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskMediaType.setStatus("mandatory")
_ArrayDiskDellCertified_Type = Integer32
_ArrayDiskDellCertified_Object = MibTableColumn
arrayDiskDellCertified = _ArrayDiskDellCertified_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 36),
    _ArrayDiskDellCertified_Type()
)
arrayDiskDellCertified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskDellCertified.setStatus("mandatory")
_ArrayDiskAltaVendorId_Type = DisplayString
_ArrayDiskAltaVendorId_Object = MibTableColumn
arrayDiskAltaVendorId = _ArrayDiskAltaVendorId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 37),
    _ArrayDiskAltaVendorId_Type()
)
arrayDiskAltaVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskAltaVendorId.setStatus("obsolete")
_ArrayDiskAltaProductId_Type = DisplayString
_ArrayDiskAltaProductId_Object = MibTableColumn
arrayDiskAltaProductId = _ArrayDiskAltaProductId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 38),
    _ArrayDiskAltaProductId_Type()
)
arrayDiskAltaProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskAltaProductId.setStatus("obsolete")
_ArrayDiskAltaRevisionId_Type = DisplayString
_ArrayDiskAltaRevisionId_Object = MibTableColumn
arrayDiskAltaRevisionId = _ArrayDiskAltaRevisionId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 39),
    _ArrayDiskAltaRevisionId_Type()
)
arrayDiskAltaRevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskAltaRevisionId.setStatus("obsolete")
_ArrayDiskEncryptionCapable_Type = Integer32
_ArrayDiskEncryptionCapable_Object = MibTableColumn
arrayDiskEncryptionCapable = _ArrayDiskEncryptionCapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 40),
    _ArrayDiskEncryptionCapable_Type()
)
arrayDiskEncryptionCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEncryptionCapable.setStatus("mandatory")
_ArrayDiskEncrypted_Type = Integer32
_ArrayDiskEncrypted_Object = MibTableColumn
arrayDiskEncrypted = _ArrayDiskEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 41),
    _ArrayDiskEncrypted_Type()
)
arrayDiskEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEncrypted.setStatus("mandatory")
_ArrayDiskPowerState_Type = Integer32
_ArrayDiskPowerState_Object = MibTableColumn
arrayDiskPowerState = _ArrayDiskPowerState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 42),
    _ArrayDiskPowerState_Type()
)
arrayDiskPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskPowerState.setStatus("mandatory")
_ArrayDiskDriveWriteCache_Type = Integer32
_ArrayDiskDriveWriteCache_Object = MibTableColumn
arrayDiskDriveWriteCache = _ArrayDiskDriveWriteCache_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 43),
    _ArrayDiskDriveWriteCache_Type()
)
arrayDiskDriveWriteCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskDriveWriteCache.setStatus("mandatory")
_ArrayDiskModelNumber_Type = DisplayString
_ArrayDiskModelNumber_Object = MibTableColumn
arrayDiskModelNumber = _ArrayDiskModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 44),
    _ArrayDiskModelNumber_Type()
)
arrayDiskModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskModelNumber.setStatus("mandatory")


class _ArrayDiskLifeRemaining_Type(Integer32):
    """Custom type arrayDiskLifeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArrayDiskLifeRemaining_Type.__name__ = "Integer32"
_ArrayDiskLifeRemaining_Object = MibTableColumn
arrayDiskLifeRemaining = _ArrayDiskLifeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 45),
    _ArrayDiskLifeRemaining_Type()
)
arrayDiskLifeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLifeRemaining.setStatus("mandatory")
_ArrayDiskDriverVersion_Type = DisplayString
_ArrayDiskDriverVersion_Object = MibTableColumn
arrayDiskDriverVersion = _ArrayDiskDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 46),
    _ArrayDiskDriverVersion_Type()
)
arrayDiskDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskDriverVersion.setStatus("mandatory")
_ArrayDiskDeviceLifeStatus_Type = Integer32
_ArrayDiskDeviceLifeStatus_Object = MibTableColumn
arrayDiskDeviceLifeStatus = _ArrayDiskDeviceLifeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 47),
    _ArrayDiskDeviceLifeStatus_Type()
)
arrayDiskDeviceLifeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskDeviceLifeStatus.setStatus("mandatory")
_ArrayDiskReadOnly_Type = DisplayString
_ArrayDiskReadOnly_Object = MibTableColumn
arrayDiskReadOnly = _ArrayDiskReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 48),
    _ArrayDiskReadOnly_Type()
)
arrayDiskReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskReadOnly.setStatus("mandatory")
_ArrayDiskRemainingRatedWriteEndurance_Type = DisplayString
_ArrayDiskRemainingRatedWriteEndurance_Object = MibTableColumn
arrayDiskRemainingRatedWriteEndurance = _ArrayDiskRemainingRatedWriteEndurance_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 49),
    _ArrayDiskRemainingRatedWriteEndurance_Type()
)
arrayDiskRemainingRatedWriteEndurance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskRemainingRatedWriteEndurance.setStatus("mandatory")
_ArrayDiskSectorSize_Type = Integer32
_ArrayDiskSectorSize_Object = MibTableColumn
arrayDiskSectorSize = _ArrayDiskSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 50),
    _ArrayDiskSectorSize_Type()
)
arrayDiskSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskSectorSize.setStatus("mandatory")
_ArrayDiskPICapable_Type = Integer32
_ArrayDiskPICapable_Object = MibTableColumn
arrayDiskPICapable = _ArrayDiskPICapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 51),
    _ArrayDiskPICapable_Type()
)
arrayDiskPICapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskPICapable.setStatus("mandatory")
_ArrayDiskMaxLinkWidth_Type = Integer32
_ArrayDiskMaxLinkWidth_Object = MibTableColumn
arrayDiskMaxLinkWidth = _ArrayDiskMaxLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 52),
    _ArrayDiskMaxLinkWidth_Type()
)
arrayDiskMaxLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskMaxLinkWidth.setStatus("mandatory")
_ArrayDiskNegotiatedLinkWidth_Type = Integer32
_ArrayDiskNegotiatedLinkWidth_Object = MibTableColumn
arrayDiskNegotiatedLinkWidth = _ArrayDiskNegotiatedLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 4, 1, 53),
    _ArrayDiskNegotiatedLinkWidth_Type()
)
arrayDiskNegotiatedLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskNegotiatedLinkWidth.setStatus("mandatory")
_ArrayDiskEnclosureConnectionTable_Object = MibTable
arrayDiskEnclosureConnectionTable = _ArrayDiskEnclosureConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5)
)
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionTable.setStatus("mandatory")
_ArrayDiskEnclosureConnectionEntry_Object = MibTableRow
arrayDiskEnclosureConnectionEntry = _ArrayDiskEnclosureConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5, 1)
)
arrayDiskEnclosureConnectionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "arrayDiskEnclosureConnectionNumber"),
)
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionEntry.setStatus("mandatory")


class _ArrayDiskEnclosureConnectionNumber_Type(Integer32):
    """Custom type arrayDiskEnclosureConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_ArrayDiskEnclosureConnectionNumber_Type.__name__ = "Integer32"
_ArrayDiskEnclosureConnectionNumber_Object = MibTableColumn
arrayDiskEnclosureConnectionNumber = _ArrayDiskEnclosureConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5, 1, 1),
    _ArrayDiskEnclosureConnectionNumber_Type()
)
arrayDiskEnclosureConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionNumber.setStatus("mandatory")
_ArrayDiskEnclosureConnectionArrayDiskName_Type = DisplayString
_ArrayDiskEnclosureConnectionArrayDiskName_Object = MibTableColumn
arrayDiskEnclosureConnectionArrayDiskName = _ArrayDiskEnclosureConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5, 1, 2),
    _ArrayDiskEnclosureConnectionArrayDiskName_Type()
)
arrayDiskEnclosureConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionArrayDiskName.setStatus("mandatory")
_ArrayDiskEnclosureConnectionArrayDiskNumber_Type = Integer32
_ArrayDiskEnclosureConnectionArrayDiskNumber_Object = MibTableColumn
arrayDiskEnclosureConnectionArrayDiskNumber = _ArrayDiskEnclosureConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5, 1, 3),
    _ArrayDiskEnclosureConnectionArrayDiskNumber_Type()
)
arrayDiskEnclosureConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionArrayDiskNumber.setStatus("mandatory")
_ArrayDiskEnclosureConnectionEnclosureName_Type = DisplayString
_ArrayDiskEnclosureConnectionEnclosureName_Object = MibTableColumn
arrayDiskEnclosureConnectionEnclosureName = _ArrayDiskEnclosureConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5, 1, 4),
    _ArrayDiskEnclosureConnectionEnclosureName_Type()
)
arrayDiskEnclosureConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionEnclosureName.setStatus("mandatory")
_ArrayDiskEnclosureConnectionEnclosureNumber_Type = Integer32
_ArrayDiskEnclosureConnectionEnclosureNumber_Object = MibTableColumn
arrayDiskEnclosureConnectionEnclosureNumber = _ArrayDiskEnclosureConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5, 1, 5),
    _ArrayDiskEnclosureConnectionEnclosureNumber_Type()
)
arrayDiskEnclosureConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionEnclosureNumber.setStatus("mandatory")
_ArrayDiskEnclosureConnectionControllerName_Type = DisplayString
_ArrayDiskEnclosureConnectionControllerName_Object = MibTableColumn
arrayDiskEnclosureConnectionControllerName = _ArrayDiskEnclosureConnectionControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5, 1, 6),
    _ArrayDiskEnclosureConnectionControllerName_Type()
)
arrayDiskEnclosureConnectionControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionControllerName.setStatus("mandatory")
_ArrayDiskEnclosureConnectionControllerNumber_Type = Integer32
_ArrayDiskEnclosureConnectionControllerNumber_Object = MibTableColumn
arrayDiskEnclosureConnectionControllerNumber = _ArrayDiskEnclosureConnectionControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 5, 1, 7),
    _ArrayDiskEnclosureConnectionControllerNumber_Type()
)
arrayDiskEnclosureConnectionControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionControllerNumber.setStatus("mandatory")
_ArrayDiskChannelConnectionTable_Object = MibTable
arrayDiskChannelConnectionTable = _ArrayDiskChannelConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6)
)
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionTable.setStatus("mandatory")
_ArrayDiskChannelConnectionEntry_Object = MibTableRow
arrayDiskChannelConnectionEntry = _ArrayDiskChannelConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6, 1)
)
arrayDiskChannelConnectionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "arrayDiskChannelConnectionNumber"),
)
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionEntry.setStatus("mandatory")


class _ArrayDiskChannelConnectionNumber_Type(Integer32):
    """Custom type arrayDiskChannelConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_ArrayDiskChannelConnectionNumber_Type.__name__ = "Integer32"
_ArrayDiskChannelConnectionNumber_Object = MibTableColumn
arrayDiskChannelConnectionNumber = _ArrayDiskChannelConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6, 1, 1),
    _ArrayDiskChannelConnectionNumber_Type()
)
arrayDiskChannelConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionNumber.setStatus("mandatory")
_ArrayDiskChannelConnectionArrayDiskName_Type = DisplayString
_ArrayDiskChannelConnectionArrayDiskName_Object = MibTableColumn
arrayDiskChannelConnectionArrayDiskName = _ArrayDiskChannelConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6, 1, 2),
    _ArrayDiskChannelConnectionArrayDiskName_Type()
)
arrayDiskChannelConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionArrayDiskName.setStatus("mandatory")
_ArrayDiskChannelConnectionArrayDiskNumber_Type = Integer32
_ArrayDiskChannelConnectionArrayDiskNumber_Object = MibTableColumn
arrayDiskChannelConnectionArrayDiskNumber = _ArrayDiskChannelConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6, 1, 3),
    _ArrayDiskChannelConnectionArrayDiskNumber_Type()
)
arrayDiskChannelConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionArrayDiskNumber.setStatus("mandatory")
_ArrayDiskChannelConnectionChannelName_Type = DisplayString
_ArrayDiskChannelConnectionChannelName_Object = MibTableColumn
arrayDiskChannelConnectionChannelName = _ArrayDiskChannelConnectionChannelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6, 1, 4),
    _ArrayDiskChannelConnectionChannelName_Type()
)
arrayDiskChannelConnectionChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionChannelName.setStatus("mandatory")
_ArrayDiskChannelConnectionChannelNumber_Type = Integer32
_ArrayDiskChannelConnectionChannelNumber_Object = MibTableColumn
arrayDiskChannelConnectionChannelNumber = _ArrayDiskChannelConnectionChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6, 1, 5),
    _ArrayDiskChannelConnectionChannelNumber_Type()
)
arrayDiskChannelConnectionChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionChannelNumber.setStatus("mandatory")
_ArrayDiskChannelConnectionControllerName_Type = DisplayString
_ArrayDiskChannelConnectionControllerName_Object = MibTableColumn
arrayDiskChannelConnectionControllerName = _ArrayDiskChannelConnectionControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6, 1, 6),
    _ArrayDiskChannelConnectionControllerName_Type()
)
arrayDiskChannelConnectionControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionControllerName.setStatus("mandatory")
_ArrayDiskChannelConnectionControllerNumber_Type = Integer32
_ArrayDiskChannelConnectionControllerNumber_Object = MibTableColumn
arrayDiskChannelConnectionControllerNumber = _ArrayDiskChannelConnectionControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 6, 1, 7),
    _ArrayDiskChannelConnectionControllerNumber_Type()
)
arrayDiskChannelConnectionControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionControllerNumber.setStatus("mandatory")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("mandatory")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1)
)
fanEntry.setIndexNames(
    (0, "StorageManagement-MIB", "fanNumber"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("mandatory")


class _FanNumber_Type(Integer32):
    """Custom type fanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_FanNumber_Type.__name__ = "Integer32"
_FanNumber_Object = MibTableColumn
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("mandatory")
_FanName_Type = DisplayString
_FanName_Object = MibTableColumn
fanName = _FanName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 2),
    _FanName_Type()
)
fanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanName.setStatus("mandatory")
_FanVendor_Type = DisplayString
_FanVendor_Object = MibTableColumn
fanVendor = _FanVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 3),
    _FanVendor_Type()
)
fanVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanVendor.setStatus("mandatory")


class _FanState_Type(Integer32):
    """Custom type fanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              11,
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("missing", 21),
          ("ready", 1),
          ("removed", 11))
    )


_FanState_Type.__name__ = "Integer32"
_FanState_Object = MibTableColumn
fanState = _FanState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 4),
    _FanState_Type()
)
fanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanState.setStatus("mandatory")


class _FanSeverity_Type(Integer32):
    """Custom type fanSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_FanSeverity_Type.__name__ = "Integer32"
_FanSeverity_Object = MibTableColumn
fanSeverity = _FanSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 5),
    _FanSeverity_Type()
)
fanSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSeverity.setStatus("obsolete")
_FanProbeUnit_Type = DisplayString
_FanProbeUnit_Object = MibTableColumn
fanProbeUnit = _FanProbeUnit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 6),
    _FanProbeUnit_Type()
)
fanProbeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeUnit.setStatus("obsolete")
_FanProbeMinWarning_Type = DisplayString
_FanProbeMinWarning_Object = MibTableColumn
fanProbeMinWarning = _FanProbeMinWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 7),
    _FanProbeMinWarning_Type()
)
fanProbeMinWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeMinWarning.setStatus("obsolete")
_FanProbeMinCritical_Type = DisplayString
_FanProbeMinCritical_Object = MibTableColumn
fanProbeMinCritical = _FanProbeMinCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 8),
    _FanProbeMinCritical_Type()
)
fanProbeMinCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeMinCritical.setStatus("obsolete")
_FanProbeMaxWarning_Type = DisplayString
_FanProbeMaxWarning_Object = MibTableColumn
fanProbeMaxWarning = _FanProbeMaxWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 9),
    _FanProbeMaxWarning_Type()
)
fanProbeMaxWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeMaxWarning.setStatus("obsolete")
_FanProbeMaxCritical_Type = DisplayString
_FanProbeMaxCritical_Object = MibTableColumn
fanProbeMaxCritical = _FanProbeMaxCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 10),
    _FanProbeMaxCritical_Type()
)
fanProbeMaxCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeMaxCritical.setStatus("obsolete")
_FanProbeCurrValue_Type = DisplayString
_FanProbeCurrValue_Object = MibTableColumn
fanProbeCurrValue = _FanProbeCurrValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 11),
    _FanProbeCurrValue_Type()
)
fanProbeCurrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeCurrValue.setStatus("mandatory")
_Fan1PartNumber_Type = DisplayString
_Fan1PartNumber_Object = MibTableColumn
fan1PartNumber = _Fan1PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 12),
    _Fan1PartNumber_Type()
)
fan1PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1PartNumber.setStatus("mandatory")
_Fan2PartNumber_Type = DisplayString
_Fan2PartNumber_Object = MibTableColumn
fan2PartNumber = _Fan2PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 13),
    _Fan2PartNumber_Type()
)
fan2PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2PartNumber.setStatus("obsolete")
_FanRollUpStatus_Type = DellStatus
_FanRollUpStatus_Object = MibTableColumn
fanRollUpStatus = _FanRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 14),
    _FanRollUpStatus_Type()
)
fanRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRollUpStatus.setStatus("mandatory")
_FanComponentStatus_Type = DellStatus
_FanComponentStatus_Object = MibTableColumn
fanComponentStatus = _FanComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 15),
    _FanComponentStatus_Type()
)
fanComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanComponentStatus.setStatus("mandatory")
_FanNexusID_Type = DisplayString
_FanNexusID_Object = MibTableColumn
fanNexusID = _FanNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 16),
    _FanNexusID_Type()
)
fanNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNexusID.setStatus("mandatory")
_FanRevision_Type = DisplayString
_FanRevision_Object = MibTableColumn
fanRevision = _FanRevision_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 7, 1, 17),
    _FanRevision_Type()
)
fanRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRevision.setStatus("mandatory")
_FanConnectionTable_Object = MibTable
fanConnectionTable = _FanConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 8)
)
if mibBuilder.loadTexts:
    fanConnectionTable.setStatus("mandatory")
_FanConnectionEntry_Object = MibTableRow
fanConnectionEntry = _FanConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 8, 1)
)
fanConnectionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "fanConnectionNumber"),
)
if mibBuilder.loadTexts:
    fanConnectionEntry.setStatus("mandatory")


class _FanConnectionNumber_Type(Integer32):
    """Custom type fanConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FanConnectionNumber_Type.__name__ = "Integer32"
_FanConnectionNumber_Object = MibTableColumn
fanConnectionNumber = _FanConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 8, 1, 1),
    _FanConnectionNumber_Type()
)
fanConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionNumber.setStatus("mandatory")
_FanConnectionFanName_Type = DisplayString
_FanConnectionFanName_Object = MibTableColumn
fanConnectionFanName = _FanConnectionFanName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 8, 1, 2),
    _FanConnectionFanName_Type()
)
fanConnectionFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionFanName.setStatus("mandatory")
_FanConnectionFanNumber_Type = Integer32
_FanConnectionFanNumber_Object = MibTableColumn
fanConnectionFanNumber = _FanConnectionFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 8, 1, 3),
    _FanConnectionFanNumber_Type()
)
fanConnectionFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionFanNumber.setStatus("mandatory")
_FanConnectionEnclosureName_Type = DisplayString
_FanConnectionEnclosureName_Object = MibTableColumn
fanConnectionEnclosureName = _FanConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 8, 1, 4),
    _FanConnectionEnclosureName_Type()
)
fanConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionEnclosureName.setStatus("mandatory")
_FanConnectionEnclosureNumber_Type = Integer32
_FanConnectionEnclosureNumber_Object = MibTableColumn
fanConnectionEnclosureNumber = _FanConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 8, 1, 5),
    _FanConnectionEnclosureNumber_Type()
)
fanConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionEnclosureNumber.setStatus("mandatory")
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("mandatory")
_PowerSupplyEntry_Object = MibTableRow
powerSupplyEntry = _PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1)
)
powerSupplyEntry.setIndexNames(
    (0, "StorageManagement-MIB", "powerSupplyNumber"),
)
if mibBuilder.loadTexts:
    powerSupplyEntry.setStatus("mandatory")


class _PowerSupplyNumber_Type(Integer32):
    """Custom type powerSupplyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PowerSupplyNumber_Type.__name__ = "Integer32"
_PowerSupplyNumber_Object = MibTableColumn
powerSupplyNumber = _PowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 1),
    _PowerSupplyNumber_Type()
)
powerSupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyNumber.setStatus("mandatory")
_PowerSupplyName_Type = DisplayString
_PowerSupplyName_Object = MibTableColumn
powerSupplyName = _PowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 2),
    _PowerSupplyName_Type()
)
powerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyName.setStatus("mandatory")
_PowerSupplyVendor_Type = DisplayString
_PowerSupplyVendor_Object = MibTableColumn
powerSupplyVendor = _PowerSupplyVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 3),
    _PowerSupplyVendor_Type()
)
powerSupplyVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyVendor.setStatus("mandatory")


class _PowerSupplyState_Type(Integer32):
    """Custom type powerSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              11,
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("missing", 21),
          ("notInstalled", 5),
          ("ready", 1),
          ("removed", 11))
    )


_PowerSupplyState_Type.__name__ = "Integer32"
_PowerSupplyState_Object = MibTableColumn
powerSupplyState = _PowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 4),
    _PowerSupplyState_Type()
)
powerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyState.setStatus("mandatory")


class _PowerSupplySeverity_Type(Integer32):
    """Custom type powerSupplySeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_PowerSupplySeverity_Type.__name__ = "Integer32"
_PowerSupplySeverity_Object = MibTableColumn
powerSupplySeverity = _PowerSupplySeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 5),
    _PowerSupplySeverity_Type()
)
powerSupplySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplySeverity.setStatus("obsolete")
_PowerSupply1PartNumber_Type = DisplayString
_PowerSupply1PartNumber_Object = MibTableColumn
powerSupply1PartNumber = _PowerSupply1PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 6),
    _PowerSupply1PartNumber_Type()
)
powerSupply1PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply1PartNumber.setStatus("mandatory")
_PowerSupply2PartNumber_Type = DisplayString
_PowerSupply2PartNumber_Object = MibTableColumn
powerSupply2PartNumber = _PowerSupply2PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 7),
    _PowerSupply2PartNumber_Type()
)
powerSupply2PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply2PartNumber.setStatus("obsolete")
_PowerSupplyRollUpStatus_Type = DellStatus
_PowerSupplyRollUpStatus_Object = MibTableColumn
powerSupplyRollUpStatus = _PowerSupplyRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 8),
    _PowerSupplyRollUpStatus_Type()
)
powerSupplyRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRollUpStatus.setStatus("mandatory")
_PowerSupplyComponentStatus_Type = DellStatus
_PowerSupplyComponentStatus_Object = MibTableColumn
powerSupplyComponentStatus = _PowerSupplyComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 9),
    _PowerSupplyComponentStatus_Type()
)
powerSupplyComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyComponentStatus.setStatus("mandatory")
_PowerSupplyNexusID_Type = DisplayString
_PowerSupplyNexusID_Object = MibTableColumn
powerSupplyNexusID = _PowerSupplyNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 10),
    _PowerSupplyNexusID_Type()
)
powerSupplyNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyNexusID.setStatus("mandatory")
_PowerSupplyRevision_Type = DisplayString
_PowerSupplyRevision_Object = MibTableColumn
powerSupplyRevision = _PowerSupplyRevision_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 9, 1, 11),
    _PowerSupplyRevision_Type()
)
powerSupplyRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRevision.setStatus("mandatory")
_PowerSupplyConnectionTable_Object = MibTable
powerSupplyConnectionTable = _PowerSupplyConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 10)
)
if mibBuilder.loadTexts:
    powerSupplyConnectionTable.setStatus("mandatory")
_PowerSupplyConnectionEntry_Object = MibTableRow
powerSupplyConnectionEntry = _PowerSupplyConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 10, 1)
)
powerSupplyConnectionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "powerSupplyConnectionNumber"),
)
if mibBuilder.loadTexts:
    powerSupplyConnectionEntry.setStatus("mandatory")


class _PowerSupplyConnectionNumber_Type(Integer32):
    """Custom type powerSupplyConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PowerSupplyConnectionNumber_Type.__name__ = "Integer32"
_PowerSupplyConnectionNumber_Object = MibTableColumn
powerSupplyConnectionNumber = _PowerSupplyConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 10, 1, 1),
    _PowerSupplyConnectionNumber_Type()
)
powerSupplyConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyConnectionNumber.setStatus("mandatory")
_PowerSupplyConnectionPowersupplyName_Type = DisplayString
_PowerSupplyConnectionPowersupplyName_Object = MibTableColumn
powerSupplyConnectionPowersupplyName = _PowerSupplyConnectionPowersupplyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 10, 1, 2),
    _PowerSupplyConnectionPowersupplyName_Type()
)
powerSupplyConnectionPowersupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyConnectionPowersupplyName.setStatus("mandatory")
_PowerSupplyConnectionPowersupplyNumber_Type = Integer32
_PowerSupplyConnectionPowersupplyNumber_Object = MibTableColumn
powerSupplyConnectionPowersupplyNumber = _PowerSupplyConnectionPowersupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 10, 1, 3),
    _PowerSupplyConnectionPowersupplyNumber_Type()
)
powerSupplyConnectionPowersupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyConnectionPowersupplyNumber.setStatus("mandatory")
_PowerSupplyConnectionEnclosureName_Type = DisplayString
_PowerSupplyConnectionEnclosureName_Object = MibTableColumn
powerSupplyConnectionEnclosureName = _PowerSupplyConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 10, 1, 4),
    _PowerSupplyConnectionEnclosureName_Type()
)
powerSupplyConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyConnectionEnclosureName.setStatus("mandatory")
_PowerSupplyConnectionEnclosureNumber_Type = Integer32
_PowerSupplyConnectionEnclosureNumber_Object = MibTableColumn
powerSupplyConnectionEnclosureNumber = _PowerSupplyConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 10, 1, 5),
    _PowerSupplyConnectionEnclosureNumber_Type()
)
powerSupplyConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyConnectionEnclosureNumber.setStatus("mandatory")
_PowerSupplyConnectionFirmwareVersion_Type = DisplayString
_PowerSupplyConnectionFirmwareVersion_Object = MibTableColumn
powerSupplyConnectionFirmwareVersion = _PowerSupplyConnectionFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 10, 1, 6),
    _PowerSupplyConnectionFirmwareVersion_Type()
)
powerSupplyConnectionFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyConnectionFirmwareVersion.setStatus("mandatory")
_TemperatureProbeTable_Object = MibTable
temperatureProbeTable = _TemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11)
)
if mibBuilder.loadTexts:
    temperatureProbeTable.setStatus("mandatory")
_TemperatureProbeEntry_Object = MibTableRow
temperatureProbeEntry = _TemperatureProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1)
)
temperatureProbeEntry.setIndexNames(
    (0, "StorageManagement-MIB", "temperatureProbeNumber"),
)
if mibBuilder.loadTexts:
    temperatureProbeEntry.setStatus("mandatory")


class _TemperatureProbeNumber_Type(Integer32):
    """Custom type temperatureProbeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TemperatureProbeNumber_Type.__name__ = "Integer32"
_TemperatureProbeNumber_Object = MibTableColumn
temperatureProbeNumber = _TemperatureProbeNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 1),
    _TemperatureProbeNumber_Type()
)
temperatureProbeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeNumber.setStatus("mandatory")
_TemperatureProbeName_Type = DisplayString
_TemperatureProbeName_Object = MibTableColumn
temperatureProbeName = _TemperatureProbeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 2),
    _TemperatureProbeName_Type()
)
temperatureProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeName.setStatus("mandatory")
_TemperatureProbeVendor_Type = DisplayString
_TemperatureProbeVendor_Object = MibTableColumn
temperatureProbeVendor = _TemperatureProbeVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 3),
    _TemperatureProbeVendor_Type()
)
temperatureProbeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeVendor.setStatus("mandatory")


class _TemperatureProbeState_Type(Integer32):
    """Custom type temperatureProbeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              9,
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("inactive", 9),
          ("missing", 21),
          ("offline", 4),
          ("ready", 1))
    )


_TemperatureProbeState_Type.__name__ = "Integer32"
_TemperatureProbeState_Object = MibTableColumn
temperatureProbeState = _TemperatureProbeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 4),
    _TemperatureProbeState_Type()
)
temperatureProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeState.setStatus("mandatory")


class _TemperatureProbeSeverity_Type(Integer32):
    """Custom type temperatureProbeSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_TemperatureProbeSeverity_Type.__name__ = "Integer32"
_TemperatureProbeSeverity_Object = MibTableColumn
temperatureProbeSeverity = _TemperatureProbeSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 5),
    _TemperatureProbeSeverity_Type()
)
temperatureProbeSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeSeverity.setStatus("obsolete")
_TemperatureProbeUnit_Type = DisplayString
_TemperatureProbeUnit_Object = MibTableColumn
temperatureProbeUnit = _TemperatureProbeUnit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 6),
    _TemperatureProbeUnit_Type()
)
temperatureProbeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUnit.setStatus("mandatory")
_TemperatureProbeMinWarning_Type = Integer32
_TemperatureProbeMinWarning_Object = MibTableColumn
temperatureProbeMinWarning = _TemperatureProbeMinWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 7),
    _TemperatureProbeMinWarning_Type()
)
temperatureProbeMinWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMinWarning.setStatus("mandatory")
_TemperatureProbeMinCritical_Type = Integer32
_TemperatureProbeMinCritical_Object = MibTableColumn
temperatureProbeMinCritical = _TemperatureProbeMinCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 8),
    _TemperatureProbeMinCritical_Type()
)
temperatureProbeMinCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMinCritical.setStatus("mandatory")
_TemperatureProbeMaxWarning_Type = Integer32
_TemperatureProbeMaxWarning_Object = MibTableColumn
temperatureProbeMaxWarning = _TemperatureProbeMaxWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 9),
    _TemperatureProbeMaxWarning_Type()
)
temperatureProbeMaxWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMaxWarning.setStatus("mandatory")
_TemperatureProbeMaxCritical_Type = Integer32
_TemperatureProbeMaxCritical_Object = MibTableColumn
temperatureProbeMaxCritical = _TemperatureProbeMaxCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 10),
    _TemperatureProbeMaxCritical_Type()
)
temperatureProbeMaxCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMaxCritical.setStatus("mandatory")
_TemperatureProbeCurValue_Type = Integer32
_TemperatureProbeCurValue_Object = MibTableColumn
temperatureProbeCurValue = _TemperatureProbeCurValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 11),
    _TemperatureProbeCurValue_Type()
)
temperatureProbeCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeCurValue.setStatus("mandatory")
_TemperatureProbeRollUpStatus_Type = DellStatus
_TemperatureProbeRollUpStatus_Object = MibTableColumn
temperatureProbeRollUpStatus = _TemperatureProbeRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 12),
    _TemperatureProbeRollUpStatus_Type()
)
temperatureProbeRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeRollUpStatus.setStatus("mandatory")
_TemperatureProbeComponentStatus_Type = DellStatus
_TemperatureProbeComponentStatus_Object = MibTableColumn
temperatureProbeComponentStatus = _TemperatureProbeComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 13),
    _TemperatureProbeComponentStatus_Type()
)
temperatureProbeComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeComponentStatus.setStatus("mandatory")
_TemperatureProbeNexusID_Type = DisplayString
_TemperatureProbeNexusID_Object = MibTableColumn
temperatureProbeNexusID = _TemperatureProbeNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 11, 1, 14),
    _TemperatureProbeNexusID_Type()
)
temperatureProbeNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeNexusID.setStatus("mandatory")
_TemperatureConnectionTable_Object = MibTable
temperatureConnectionTable = _TemperatureConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 12)
)
if mibBuilder.loadTexts:
    temperatureConnectionTable.setStatus("mandatory")
_TemperatureConnectionEntry_Object = MibTableRow
temperatureConnectionEntry = _TemperatureConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 12, 1)
)
temperatureConnectionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "temperatureConnectionNumber"),
)
if mibBuilder.loadTexts:
    temperatureConnectionEntry.setStatus("mandatory")


class _TemperatureConnectionNumber_Type(Integer32):
    """Custom type temperatureConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TemperatureConnectionNumber_Type.__name__ = "Integer32"
_TemperatureConnectionNumber_Object = MibTableColumn
temperatureConnectionNumber = _TemperatureConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 12, 1, 1),
    _TemperatureConnectionNumber_Type()
)
temperatureConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionNumber.setStatus("mandatory")
_TemperatureConnectionTemperatureName_Type = DisplayString
_TemperatureConnectionTemperatureName_Object = MibTableColumn
temperatureConnectionTemperatureName = _TemperatureConnectionTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 12, 1, 2),
    _TemperatureConnectionTemperatureName_Type()
)
temperatureConnectionTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionTemperatureName.setStatus("mandatory")
_TemperatureConnectionTemperatureNumber_Type = Integer32
_TemperatureConnectionTemperatureNumber_Object = MibTableColumn
temperatureConnectionTemperatureNumber = _TemperatureConnectionTemperatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 12, 1, 3),
    _TemperatureConnectionTemperatureNumber_Type()
)
temperatureConnectionTemperatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionTemperatureNumber.setStatus("mandatory")
_TemperatureConnectionEnclosureName_Type = DisplayString
_TemperatureConnectionEnclosureName_Object = MibTableColumn
temperatureConnectionEnclosureName = _TemperatureConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 12, 1, 4),
    _TemperatureConnectionEnclosureName_Type()
)
temperatureConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionEnclosureName.setStatus("mandatory")
_TemperatureConnectionEnclosureNumber_Type = Integer32
_TemperatureConnectionEnclosureNumber_Object = MibTableColumn
temperatureConnectionEnclosureNumber = _TemperatureConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 12, 1, 5),
    _TemperatureConnectionEnclosureNumber_Type()
)
temperatureConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionEnclosureNumber.setStatus("mandatory")
_EnclosureManagementModuleTable_Object = MibTable
enclosureManagementModuleTable = _EnclosureManagementModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13)
)
if mibBuilder.loadTexts:
    enclosureManagementModuleTable.setStatus("mandatory")
_EnclosureManagementModuleEntry_Object = MibTableRow
enclosureManagementModuleEntry = _EnclosureManagementModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1)
)
enclosureManagementModuleEntry.setIndexNames(
    (0, "StorageManagement-MIB", "enclosureManagementModuleNumber"),
)
if mibBuilder.loadTexts:
    enclosureManagementModuleEntry.setStatus("mandatory")


class _EnclosureManagementModuleNumber_Type(Integer32):
    """Custom type enclosureManagementModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EnclosureManagementModuleNumber_Type.__name__ = "Integer32"
_EnclosureManagementModuleNumber_Object = MibTableColumn
enclosureManagementModuleNumber = _EnclosureManagementModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 1),
    _EnclosureManagementModuleNumber_Type()
)
enclosureManagementModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleNumber.setStatus("mandatory")
_EnclosureManagementModuleName_Type = DisplayString
_EnclosureManagementModuleName_Object = MibTableColumn
enclosureManagementModuleName = _EnclosureManagementModuleName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 2),
    _EnclosureManagementModuleName_Type()
)
enclosureManagementModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleName.setStatus("mandatory")
_EnclosureManagementModuleVendor_Type = DisplayString
_EnclosureManagementModuleVendor_Object = MibTableColumn
enclosureManagementModuleVendor = _EnclosureManagementModuleVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 3),
    _EnclosureManagementModuleVendor_Type()
)
enclosureManagementModuleVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleVendor.setStatus("mandatory")


class _EnclosureManagementModuleState_Type(Integer32):
    """Custom type enclosureManagementModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("missing", 21),
          ("notInstalled", 5),
          ("offline", 4),
          ("online", 3),
          ("ready", 1))
    )


_EnclosureManagementModuleState_Type.__name__ = "Integer32"
_EnclosureManagementModuleState_Object = MibTableColumn
enclosureManagementModuleState = _EnclosureManagementModuleState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 4),
    _EnclosureManagementModuleState_Type()
)
enclosureManagementModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleState.setStatus("mandatory")


class _EnclosureManagementModuleSeverity_Type(Integer32):
    """Custom type enclosureManagementModuleSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_EnclosureManagementModuleSeverity_Type.__name__ = "Integer32"
_EnclosureManagementModuleSeverity_Object = MibTableColumn
enclosureManagementModuleSeverity = _EnclosureManagementModuleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 5),
    _EnclosureManagementModuleSeverity_Type()
)
enclosureManagementModuleSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleSeverity.setStatus("obsolete")
_EnclosureManagementModulePartNumber_Type = DisplayString
_EnclosureManagementModulePartNumber_Object = MibTableColumn
enclosureManagementModulePartNumber = _EnclosureManagementModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 6),
    _EnclosureManagementModulePartNumber_Type()
)
enclosureManagementModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModulePartNumber.setStatus("mandatory")


class _EnclosureManagementModuleType_Type(Integer32):
    """Custom type enclosureManagementModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eMM", 1),
          ("terminationCard", 2))
    )


_EnclosureManagementModuleType_Type.__name__ = "Integer32"
_EnclosureManagementModuleType_Object = MibTableColumn
enclosureManagementModuleType = _EnclosureManagementModuleType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 7),
    _EnclosureManagementModuleType_Type()
)
enclosureManagementModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleType.setStatus("mandatory")
_EnclosureManagementModuleFWVersion_Type = DisplayString
_EnclosureManagementModuleFWVersion_Object = MibTableColumn
enclosureManagementModuleFWVersion = _EnclosureManagementModuleFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 8),
    _EnclosureManagementModuleFWVersion_Type()
)
enclosureManagementModuleFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleFWVersion.setStatus("mandatory")
_EnclosureManagementModuleMaxSpeed_Type = DisplayString
_EnclosureManagementModuleMaxSpeed_Object = MibTableColumn
enclosureManagementModuleMaxSpeed = _EnclosureManagementModuleMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 9),
    _EnclosureManagementModuleMaxSpeed_Type()
)
enclosureManagementModuleMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleMaxSpeed.setStatus("mandatory")
_EnclosureManagementModuleRollUpStatus_Type = DellStatus
_EnclosureManagementModuleRollUpStatus_Object = MibTableColumn
enclosureManagementModuleRollUpStatus = _EnclosureManagementModuleRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 10),
    _EnclosureManagementModuleRollUpStatus_Type()
)
enclosureManagementModuleRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleRollUpStatus.setStatus("mandatory")
_EnclosureManagementModuleComponentStatus_Type = DellStatus
_EnclosureManagementModuleComponentStatus_Object = MibTableColumn
enclosureManagementModuleComponentStatus = _EnclosureManagementModuleComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 11),
    _EnclosureManagementModuleComponentStatus_Type()
)
enclosureManagementModuleComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleComponentStatus.setStatus("mandatory")
_EnclosureManagementModuleNexusID_Type = DisplayString
_EnclosureManagementModuleNexusID_Object = MibTableColumn
enclosureManagementModuleNexusID = _EnclosureManagementModuleNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 12),
    _EnclosureManagementModuleNexusID_Type()
)
enclosureManagementModuleNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleNexusID.setStatus("mandatory")
_EnclosureManagementModuleRevision_Type = DisplayString
_EnclosureManagementModuleRevision_Object = MibTableColumn
enclosureManagementModuleRevision = _EnclosureManagementModuleRevision_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 13, 1, 13),
    _EnclosureManagementModuleRevision_Type()
)
enclosureManagementModuleRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleRevision.setStatus("mandatory")
_EnclosureManagementModuleConnectionTable_Object = MibTable
enclosureManagementModuleConnectionTable = _EnclosureManagementModuleConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 14)
)
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionTable.setStatus("mandatory")
_EnclosureManagementModuleConnectionEntry_Object = MibTableRow
enclosureManagementModuleConnectionEntry = _EnclosureManagementModuleConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 14, 1)
)
enclosureManagementModuleConnectionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "enclosureManagementModuleConnectionNumber"),
)
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEntry.setStatus("mandatory")


class _EnclosureManagementModuleConnectionNumber_Type(Integer32):
    """Custom type enclosureManagementModuleConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EnclosureManagementModuleConnectionNumber_Type.__name__ = "Integer32"
_EnclosureManagementModuleConnectionNumber_Object = MibTableColumn
enclosureManagementModuleConnectionNumber = _EnclosureManagementModuleConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 14, 1, 1),
    _EnclosureManagementModuleConnectionNumber_Type()
)
enclosureManagementModuleConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionNumber.setStatus("mandatory")
_EnclosureManagementModuleConnectionEMMName_Type = DisplayString
_EnclosureManagementModuleConnectionEMMName_Object = MibTableColumn
enclosureManagementModuleConnectionEMMName = _EnclosureManagementModuleConnectionEMMName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 14, 1, 2),
    _EnclosureManagementModuleConnectionEMMName_Type()
)
enclosureManagementModuleConnectionEMMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEMMName.setStatus("mandatory")
_EnclosureManagementModuleConnectionEMMNumber_Type = Integer32
_EnclosureManagementModuleConnectionEMMNumber_Object = MibTableColumn
enclosureManagementModuleConnectionEMMNumber = _EnclosureManagementModuleConnectionEMMNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 14, 1, 3),
    _EnclosureManagementModuleConnectionEMMNumber_Type()
)
enclosureManagementModuleConnectionEMMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEMMNumber.setStatus("mandatory")
_EnclosureManagementModuleConnectionEnclosureName_Type = DisplayString
_EnclosureManagementModuleConnectionEnclosureName_Object = MibTableColumn
enclosureManagementModuleConnectionEnclosureName = _EnclosureManagementModuleConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 14, 1, 4),
    _EnclosureManagementModuleConnectionEnclosureName_Type()
)
enclosureManagementModuleConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEnclosureName.setStatus("mandatory")
_EnclosureManagementModuleConnectionEnclosureNumber_Type = Integer32
_EnclosureManagementModuleConnectionEnclosureNumber_Object = MibTableColumn
enclosureManagementModuleConnectionEnclosureNumber = _EnclosureManagementModuleConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 14, 1, 5),
    _EnclosureManagementModuleConnectionEnclosureNumber_Type()
)
enclosureManagementModuleConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEnclosureNumber.setStatus("mandatory")
_BatteryTable_Object = MibTable
batteryTable = _BatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15)
)
if mibBuilder.loadTexts:
    batteryTable.setStatus("mandatory")
_BatteryEntry_Object = MibTableRow
batteryEntry = _BatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1)
)
batteryEntry.setIndexNames(
    (0, "StorageManagement-MIB", "batteryNumber"),
)
if mibBuilder.loadTexts:
    batteryEntry.setStatus("mandatory")


class _BatteryNumber_Type(Integer32):
    """Custom type batteryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BatteryNumber_Type.__name__ = "Integer32"
_BatteryNumber_Object = MibTableColumn
batteryNumber = _BatteryNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 1),
    _BatteryNumber_Type()
)
batteryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNumber.setStatus("mandatory")
_BatteryName_Type = DisplayString
_BatteryName_Object = MibTableColumn
batteryName = _BatteryName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 2),
    _BatteryName_Type()
)
batteryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryName.setStatus("mandatory")
_BatteryVendor_Type = DisplayString
_BatteryVendor_Object = MibTableColumn
batteryVendor = _BatteryVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 3),
    _BatteryVendor_Type()
)
batteryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVendor.setStatus("mandatory")


class _BatteryState_Type(Integer32):
    """Custom type batteryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7,
              9,
              10,
              12,
              21,
              36)
        )
    )
    namedValues = NamedValues(
        *(("charging", 12),
          ("degraded", 6),
          ("failed", 2),
          ("high", 9),
          ("learning", 36),
          ("low", 10),
          ("missing", 21),
          ("ready", 1),
          ("reconditioning", 7))
    )


_BatteryState_Type.__name__ = "Integer32"
_BatteryState_Object = MibTableColumn
batteryState = _BatteryState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 4),
    _BatteryState_Type()
)
batteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryState.setStatus("mandatory")
_BatteryRollUpStatus_Type = DellStatus
_BatteryRollUpStatus_Object = MibTableColumn
batteryRollUpStatus = _BatteryRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 5),
    _BatteryRollUpStatus_Type()
)
batteryRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRollUpStatus.setStatus("mandatory")
_BatteryComponentStatus_Type = DellStatus
_BatteryComponentStatus_Object = MibTableColumn
batteryComponentStatus = _BatteryComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 6),
    _BatteryComponentStatus_Type()
)
batteryComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryComponentStatus.setStatus("mandatory")
_BatteryChargeCount_Type = Integer32
_BatteryChargeCount_Object = MibTableColumn
batteryChargeCount = _BatteryChargeCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 7),
    _BatteryChargeCount_Type()
)
batteryChargeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryChargeCount.setStatus("mandatory")
_BatteryMaxChargeCount_Type = Integer32
_BatteryMaxChargeCount_Object = MibTableColumn
batteryMaxChargeCount = _BatteryMaxChargeCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 8),
    _BatteryMaxChargeCount_Type()
)
batteryMaxChargeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMaxChargeCount.setStatus("mandatory")
_BatteryNexusID_Type = DisplayString
_BatteryNexusID_Object = MibTableColumn
batteryNexusID = _BatteryNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 9),
    _BatteryNexusID_Type()
)
batteryNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNexusID.setStatus("mandatory")


class _BatteryPredictedCapacity_Type(Integer32):
    """Custom type batteryPredictedCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ready", 2),
          ("unknown", 4))
    )


_BatteryPredictedCapacity_Type.__name__ = "Integer32"
_BatteryPredictedCapacity_Object = MibTableColumn
batteryPredictedCapacity = _BatteryPredictedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 10),
    _BatteryPredictedCapacity_Type()
)
batteryPredictedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryPredictedCapacity.setStatus("obsolete")
_BatteryNextLearnTime_Type = Integer32
_BatteryNextLearnTime_Object = MibTableColumn
batteryNextLearnTime = _BatteryNextLearnTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 11),
    _BatteryNextLearnTime_Type()
)
batteryNextLearnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNextLearnTime.setStatus("deprecated")


class _BatteryLearnState_Type(Integer32):
    """Custom type batteryLearnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("due", 32),
          ("failed", 1),
          ("idle", 16),
          ("requested", 8),
          ("timedOut", 4))
    )


_BatteryLearnState_Type.__name__ = "Integer32"
_BatteryLearnState_Object = MibTableColumn
batteryLearnState = _BatteryLearnState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 12),
    _BatteryLearnState_Type()
)
batteryLearnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLearnState.setStatus("deprecated")
_BatteryID_Type = Integer32
_BatteryID_Object = MibTableColumn
batteryID = _BatteryID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 13),
    _BatteryID_Type()
)
batteryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryID.setStatus("mandatory")
_BatteryMaxLearnDelay_Type = Integer32
_BatteryMaxLearnDelay_Object = MibTableColumn
batteryMaxLearnDelay = _BatteryMaxLearnDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 14),
    _BatteryMaxLearnDelay_Type()
)
batteryMaxLearnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMaxLearnDelay.setStatus("deprecated")


class _BatteryLearnMode_Type(Integer32):
    """Custom type batteryLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("autowarn", 4),
          ("unknown", 8),
          ("warn", 2))
    )


_BatteryLearnMode_Type.__name__ = "Integer32"
_BatteryLearnMode_Object = MibTableColumn
batteryLearnMode = _BatteryLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 15, 1, 15),
    _BatteryLearnMode_Type()
)
batteryLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLearnMode.setStatus("deprecated")
_BatteryConnectionTable_Object = MibTable
batteryConnectionTable = _BatteryConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 16)
)
if mibBuilder.loadTexts:
    batteryConnectionTable.setStatus("mandatory")
_BatteryConnectionEntry_Object = MibTableRow
batteryConnectionEntry = _BatteryConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 16, 1)
)
batteryConnectionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "batteryConnectionNumber"),
)
if mibBuilder.loadTexts:
    batteryConnectionEntry.setStatus("mandatory")


class _BatteryConnectionNumber_Type(Integer32):
    """Custom type batteryConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BatteryConnectionNumber_Type.__name__ = "Integer32"
_BatteryConnectionNumber_Object = MibTableColumn
batteryConnectionNumber = _BatteryConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 16, 1, 1),
    _BatteryConnectionNumber_Type()
)
batteryConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryConnectionNumber.setStatus("mandatory")
_BatteryConnectionBatteryName_Type = DisplayString
_BatteryConnectionBatteryName_Object = MibTableColumn
batteryConnectionBatteryName = _BatteryConnectionBatteryName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 16, 1, 2),
    _BatteryConnectionBatteryName_Type()
)
batteryConnectionBatteryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryConnectionBatteryName.setStatus("mandatory")
_BatteryConnectionBatteryNumber_Type = Integer32
_BatteryConnectionBatteryNumber_Object = MibTableColumn
batteryConnectionBatteryNumber = _BatteryConnectionBatteryNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 16, 1, 3),
    _BatteryConnectionBatteryNumber_Type()
)
batteryConnectionBatteryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryConnectionBatteryNumber.setStatus("mandatory")
_BatteryConnectionControllerName_Type = DisplayString
_BatteryConnectionControllerName_Object = MibTableColumn
batteryConnectionControllerName = _BatteryConnectionControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 16, 1, 4),
    _BatteryConnectionControllerName_Type()
)
batteryConnectionControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryConnectionControllerName.setStatus("mandatory")
_BatteryConnectionControllerNumber_Type = Integer32
_BatteryConnectionControllerNumber_Object = MibTableColumn
batteryConnectionControllerNumber = _BatteryConnectionControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 16, 1, 5),
    _BatteryConnectionControllerNumber_Type()
)
batteryConnectionControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryConnectionControllerNumber.setStatus("mandatory")
_TapeDriveTable_Object = MibTable
tapeDriveTable = _TapeDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17)
)
if mibBuilder.loadTexts:
    tapeDriveTable.setStatus("mandatory")
_TapeDriveEntry_Object = MibTableRow
tapeDriveEntry = _TapeDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1)
)
tapeDriveEntry.setIndexNames(
    (0, "StorageManagement-MIB", "tapeDriveNumber"),
)
if mibBuilder.loadTexts:
    tapeDriveEntry.setStatus("mandatory")


class _TapeDriveNumber_Type(Integer32):
    """Custom type tapeDriveNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TapeDriveNumber_Type.__name__ = "Integer32"
_TapeDriveNumber_Object = MibTableColumn
tapeDriveNumber = _TapeDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1, 1),
    _TapeDriveNumber_Type()
)
tapeDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveNumber.setStatus("mandatory")
_TapeDriveName_Type = DisplayString
_TapeDriveName_Object = MibTableColumn
tapeDriveName = _TapeDriveName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1, 2),
    _TapeDriveName_Type()
)
tapeDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveName.setStatus("mandatory")
_TapeDriveVendor_Type = DisplayString
_TapeDriveVendor_Object = MibTableColumn
tapeDriveVendor = _TapeDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1, 3),
    _TapeDriveVendor_Type()
)
tapeDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveVendor.setStatus("mandatory")
_TapeDriveProductID_Type = DisplayString
_TapeDriveProductID_Object = MibTableColumn
tapeDriveProductID = _TapeDriveProductID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1, 4),
    _TapeDriveProductID_Type()
)
tapeDriveProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveProductID.setStatus("mandatory")
_TapeDriveNexusID_Type = DisplayString
_TapeDriveNexusID_Object = MibTableColumn
tapeDriveNexusID = _TapeDriveNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1, 5),
    _TapeDriveNexusID_Type()
)
tapeDriveNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveNexusID.setStatus("mandatory")


class _TapeDriveBusType_Type(Integer32):
    """Custom type tapeDriveBusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("sas", 8)
    )


_TapeDriveBusType_Type.__name__ = "Integer32"
_TapeDriveBusType_Object = MibTableColumn
tapeDriveBusType = _TapeDriveBusType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1, 6),
    _TapeDriveBusType_Type()
)
tapeDriveBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveBusType.setStatus("mandatory")
_TapeDriveSASAddress_Type = DisplayString
_TapeDriveSASAddress_Object = MibTableColumn
tapeDriveSASAddress = _TapeDriveSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1, 7),
    _TapeDriveSASAddress_Type()
)
tapeDriveSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveSASAddress.setStatus("mandatory")


class _TapeDriveMediaType_Type(Integer32):
    """Custom type tapeDriveMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("tape", 4)
    )


_TapeDriveMediaType_Type.__name__ = "Integer32"
_TapeDriveMediaType_Object = MibTableColumn
tapeDriveMediaType = _TapeDriveMediaType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 130, 17, 1, 8),
    _TapeDriveMediaType_Type()
)
tapeDriveMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDriveMediaType.setStatus("mandatory")
_LogicalDevices_ObjectIdentity = ObjectIdentity
logicalDevices = _LogicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140)
)
_VirtualDiskTable_Object = MibTable
virtualDiskTable = _VirtualDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1)
)
if mibBuilder.loadTexts:
    virtualDiskTable.setStatus("mandatory")
_VirtualDiskEntry_Object = MibTableRow
virtualDiskEntry = _VirtualDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1)
)
virtualDiskEntry.setIndexNames(
    (0, "StorageManagement-MIB", "virtualDiskNumber"),
)
if mibBuilder.loadTexts:
    virtualDiskEntry.setStatus("mandatory")


class _VirtualDiskNumber_Type(Integer32):
    """Custom type virtualDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000000),
    )


_VirtualDiskNumber_Type.__name__ = "Integer32"
_VirtualDiskNumber_Object = MibTableColumn
virtualDiskNumber = _VirtualDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 1),
    _VirtualDiskNumber_Type()
)
virtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskNumber.setStatus("mandatory")
_VirtualDiskName_Type = DisplayString
_VirtualDiskName_Object = MibTableColumn
virtualDiskName = _VirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 2),
    _VirtualDiskName_Type()
)
virtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskName.setStatus("mandatory")
_VirtualDiskDeviceName_Type = DisplayString
_VirtualDiskDeviceName_Object = MibTableColumn
virtualDiskDeviceName = _VirtualDiskDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 3),
    _VirtualDiskDeviceName_Type()
)
virtualDiskDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskDeviceName.setStatus("mandatory")


class _VirtualDiskState_Type(Integer32):
    """Custom type virtualDiskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              15,
              16,
              18,
              24,
              26,
              32,
              35,
              36,
              52)
        )
    )
    namedValues = NamedValues(
        *(("backgroundInit", 36),
          ("degraded", 6),
          ("failed", 2),
          ("failedRedundancy", 18),
          ("formatting", 26),
          ("initializing", 35),
          ("offline", 4),
          ("online", 3),
          ("permanentlyDegraded", 52),
          ("ready", 1),
          ("rebuilding", 24),
          ("reconstructing", 32),
          ("regenerating", 16),
          ("resynching", 15),
          ("verifying", 7))
    )


_VirtualDiskState_Type.__name__ = "Integer32"
_VirtualDiskState_Object = MibTableColumn
virtualDiskState = _VirtualDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 4),
    _VirtualDiskState_Type()
)
virtualDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskState.setStatus("mandatory")


class _VirtualDiskSeverity_Type(Integer32):
    """Custom type virtualDiskSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("failure", 3),
          ("warning", 1))
    )


_VirtualDiskSeverity_Type.__name__ = "Integer32"
_VirtualDiskSeverity_Object = MibTableColumn
virtualDiskSeverity = _VirtualDiskSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 5),
    _VirtualDiskSeverity_Type()
)
virtualDiskSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskSeverity.setStatus("obsolete")
_VirtualDiskLengthInMB_Type = Integer32
_VirtualDiskLengthInMB_Object = MibTableColumn
virtualDiskLengthInMB = _VirtualDiskLengthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 6),
    _VirtualDiskLengthInMB_Type()
)
virtualDiskLengthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLengthInMB.setStatus("mandatory")
_VirtualDiskLengthInBytes_Type = Integer32
_VirtualDiskLengthInBytes_Object = MibTableColumn
virtualDiskLengthInBytes = _VirtualDiskLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 7),
    _VirtualDiskLengthInBytes_Type()
)
virtualDiskLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLengthInBytes.setStatus("mandatory")
_VirtualDiskFreeSpaceInMB_Type = Integer32
_VirtualDiskFreeSpaceInMB_Object = MibTableColumn
virtualDiskFreeSpaceInMB = _VirtualDiskFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 8),
    _VirtualDiskFreeSpaceInMB_Type()
)
virtualDiskFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskFreeSpaceInMB.setStatus("obsolete")
_VirtualDiskFreeSpaceInBytes_Type = Integer32
_VirtualDiskFreeSpaceInBytes_Object = MibTableColumn
virtualDiskFreeSpaceInBytes = _VirtualDiskFreeSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 9),
    _VirtualDiskFreeSpaceInBytes_Type()
)
virtualDiskFreeSpaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskFreeSpaceInBytes.setStatus("obsolete")


class _VirtualDiskWritePolicy_Type(Integer32):
    """Custom type virtualDiskWritePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledAlways", 5),
          ("enabledAlwaysSAS", 6),
          ("notApplicable", 9),
          ("writeBack", 3),
          ("writeThrough", 4))
    )


_VirtualDiskWritePolicy_Type.__name__ = "Integer32"
_VirtualDiskWritePolicy_Object = MibTableColumn
virtualDiskWritePolicy = _VirtualDiskWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 10),
    _VirtualDiskWritePolicy_Type()
)
virtualDiskWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskWritePolicy.setStatus("mandatory")


class _VirtualDiskReadPolicy_Type(Integer32):
    """Custom type virtualDiskReadPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveReadAhead", 4),
          ("disabled", 2),
          ("enabled", 1),
          ("noReadAhead", 5),
          ("notApplicable", 9),
          ("readAhead", 3))
    )


_VirtualDiskReadPolicy_Type.__name__ = "Integer32"
_VirtualDiskReadPolicy_Object = MibTableColumn
virtualDiskReadPolicy = _VirtualDiskReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 11),
    _VirtualDiskReadPolicy_Type()
)
virtualDiskReadPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskReadPolicy.setStatus("mandatory")


class _VirtualDiskCachePolicy_Type(Integer32):
    """Custom type virtualDiskCachePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("cachedIO", 2),
          ("directIO", 1),
          ("not-applicable", 99))
    )


_VirtualDiskCachePolicy_Type.__name__ = "Integer32"
_VirtualDiskCachePolicy_Object = MibTableColumn
virtualDiskCachePolicy = _VirtualDiskCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 12),
    _VirtualDiskCachePolicy_Type()
)
virtualDiskCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskCachePolicy.setStatus("mandatory")


class _VirtualDiskLayout_Type(Integer32):
    """Custom type virtualDiskLayout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("addSpares", 13),
          ("cacheCade", 25),
          ("concatRaid-1", 19),
          ("concatRaid-5", 20),
          ("concatenated", 1),
          ("deleteLogical", 14),
          ("noRaid", 21),
          ("raid-0", 2),
          ("raid-0-plus-1", 18),
          ("raid-1", 3),
          ("raid-10", 10),
          ("raid-2", 4),
          ("raid-3", 5),
          ("raid-30", 11),
          ("raid-4", 6),
          ("raid-5", 7),
          ("raid-50", 12),
          ("raid-6", 8),
          ("raid-60", 24),
          ("raid-7", 9),
          ("raidMorph", 23),
          ("transformLogical", 15),
          ("volume", 22))
    )


_VirtualDiskLayout_Type.__name__ = "Integer32"
_VirtualDiskLayout_Object = MibTableColumn
virtualDiskLayout = _VirtualDiskLayout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 13),
    _VirtualDiskLayout_Type()
)
virtualDiskLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLayout.setStatus("mandatory")
_VirtualDiskCurStripeSizeInMB_Type = Integer32
_VirtualDiskCurStripeSizeInMB_Object = MibTableColumn
virtualDiskCurStripeSizeInMB = _VirtualDiskCurStripeSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 14),
    _VirtualDiskCurStripeSizeInMB_Type()
)
virtualDiskCurStripeSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskCurStripeSizeInMB.setStatus("mandatory")
_VirtualDiskCurStripeSizeInBytes_Type = Integer32
_VirtualDiskCurStripeSizeInBytes_Object = MibTableColumn
virtualDiskCurStripeSizeInBytes = _VirtualDiskCurStripeSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 15),
    _VirtualDiskCurStripeSizeInBytes_Type()
)
virtualDiskCurStripeSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskCurStripeSizeInBytes.setStatus("mandatory")
_VirtualDiskChannel_Type = Integer32
_VirtualDiskChannel_Object = MibTableColumn
virtualDiskChannel = _VirtualDiskChannel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 16),
    _VirtualDiskChannel_Type()
)
virtualDiskChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskChannel.setStatus("obsolete")
_VirtualDiskTargetID_Type = Integer32
_VirtualDiskTargetID_Object = MibTableColumn
virtualDiskTargetID = _VirtualDiskTargetID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 17),
    _VirtualDiskTargetID_Type()
)
virtualDiskTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskTargetID.setStatus("mandatory")
_VirtualDiskLunID_Type = Integer32
_VirtualDiskLunID_Object = MibTableColumn
virtualDiskLunID = _VirtualDiskLunID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 18),
    _VirtualDiskLunID_Type()
)
virtualDiskLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLunID.setStatus("obsolete")
_VirtualDiskRollUpStatus_Type = DellStatus
_VirtualDiskRollUpStatus_Object = MibTableColumn
virtualDiskRollUpStatus = _VirtualDiskRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 19),
    _VirtualDiskRollUpStatus_Type()
)
virtualDiskRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskRollUpStatus.setStatus("mandatory")
_VirtualDiskComponentStatus_Type = DellStatus
_VirtualDiskComponentStatus_Object = MibTableColumn
virtualDiskComponentStatus = _VirtualDiskComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 20),
    _VirtualDiskComponentStatus_Type()
)
virtualDiskComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskComponentStatus.setStatus("mandatory")
_VirtualDiskNexusID_Type = DisplayString
_VirtualDiskNexusID_Object = MibTableColumn
virtualDiskNexusID = _VirtualDiskNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 21),
    _VirtualDiskNexusID_Type()
)
virtualDiskNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskNexusID.setStatus("mandatory")


class _VirtualDiskArrayDiskType_Type(Integer32):
    """Custom type virtualDiskArrayDiskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ide", 4),
          ("sas", 1),
          ("sata", 2),
          ("scsi", 3),
          ("unknown", 99))
    )


_VirtualDiskArrayDiskType_Type.__name__ = "Integer32"
_VirtualDiskArrayDiskType_Object = MibTableColumn
virtualDiskArrayDiskType = _VirtualDiskArrayDiskType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 22),
    _VirtualDiskArrayDiskType_Type()
)
virtualDiskArrayDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskArrayDiskType.setStatus("mandatory")
_VirtualDiskBadBlocksDetected_Type = Integer32
_VirtualDiskBadBlocksDetected_Object = MibTableColumn
virtualDiskBadBlocksDetected = _VirtualDiskBadBlocksDetected_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 23),
    _VirtualDiskBadBlocksDetected_Type()
)
virtualDiskBadBlocksDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskBadBlocksDetected.setStatus("mandatory")
_VirtualDiskEncrypted_Type = Integer32
_VirtualDiskEncrypted_Object = MibTableColumn
virtualDiskEncrypted = _VirtualDiskEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 24),
    _VirtualDiskEncrypted_Type()
)
virtualDiskEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskEncrypted.setStatus("mandatory")
_VirtualDiskIsCacheCade_Type = Integer32
_VirtualDiskIsCacheCade_Object = MibTableColumn
virtualDiskIsCacheCade = _VirtualDiskIsCacheCade_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 25),
    _VirtualDiskIsCacheCade_Type()
)
virtualDiskIsCacheCade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskIsCacheCade.setStatus("mandatory")
_VirtualDiskDiskCachePolicy_Type = Integer32
_VirtualDiskDiskCachePolicy_Object = MibTableColumn
virtualDiskDiskCachePolicy = _VirtualDiskDiskCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 26),
    _VirtualDiskDiskCachePolicy_Type()
)
virtualDiskDiskCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskDiskCachePolicy.setStatus("mandatory")
_VirtualDiskAssociatedFluidCacheStatus_Type = Integer32
_VirtualDiskAssociatedFluidCacheStatus_Object = MibTableColumn
virtualDiskAssociatedFluidCacheStatus = _VirtualDiskAssociatedFluidCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 27),
    _VirtualDiskAssociatedFluidCacheStatus_Type()
)
virtualDiskAssociatedFluidCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskAssociatedFluidCacheStatus.setStatus("mandatory")
_VirtualDiskPIEnable_Type = Integer32
_VirtualDiskPIEnable_Object = MibTableColumn
virtualDiskPIEnable = _VirtualDiskPIEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 1, 1, 28),
    _VirtualDiskPIEnable_Type()
)
virtualDiskPIEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskPIEnable.setStatus("mandatory")
_VirtualDiskPartitionTable_Object = MibTable
virtualDiskPartitionTable = _VirtualDiskPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 2)
)
if mibBuilder.loadTexts:
    virtualDiskPartitionTable.setStatus("mandatory")
_VirtualDiskPartitionEntry_Object = MibTableRow
virtualDiskPartitionEntry = _VirtualDiskPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 2, 1)
)
virtualDiskPartitionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "virtualDiskPartitionNumber"),
)
if mibBuilder.loadTexts:
    virtualDiskPartitionEntry.setStatus("mandatory")


class _VirtualDiskPartitionNumber_Type(Integer32):
    """Custom type virtualDiskPartitionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VirtualDiskPartitionNumber_Type.__name__ = "Integer32"
_VirtualDiskPartitionNumber_Object = MibTableColumn
virtualDiskPartitionNumber = _VirtualDiskPartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 2, 1, 1),
    _VirtualDiskPartitionNumber_Type()
)
virtualDiskPartitionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskPartitionNumber.setStatus("mandatory")
_VirtualDiskPartitionDeviceName_Type = OctetString
_VirtualDiskPartitionDeviceName_Object = MibTableColumn
virtualDiskPartitionDeviceName = _VirtualDiskPartitionDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 2, 1, 2),
    _VirtualDiskPartitionDeviceName_Type()
)
virtualDiskPartitionDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskPartitionDeviceName.setStatus("mandatory")


class _VirtualDiskPartitionState_Type(Integer32):
    """Custom type virtualDiskPartitionState based on Integer32"""
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
        *(("active", 1),
          ("failed", 4),
          ("no", 2),
          ("removing", 3))
    )


_VirtualDiskPartitionState_Type.__name__ = "Integer32"
_VirtualDiskPartitionState_Object = MibTableColumn
virtualDiskPartitionState = _VirtualDiskPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 2, 1, 3),
    _VirtualDiskPartitionState_Type()
)
virtualDiskPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskPartitionState.setStatus("mandatory")
_VirtualDiskPartitionSize_Type = Integer32
_VirtualDiskPartitionSize_Object = MibTableColumn
virtualDiskPartitionSize = _VirtualDiskPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 2, 1, 4),
    _VirtualDiskPartitionSize_Type()
)
virtualDiskPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskPartitionSize.setStatus("mandatory")
_VirtualDiskPartitionFluidCacheStatus_Type = OctetString
_VirtualDiskPartitionFluidCacheStatus_Object = MibTableColumn
virtualDiskPartitionFluidCacheStatus = _VirtualDiskPartitionFluidCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 2, 1, 5),
    _VirtualDiskPartitionFluidCacheStatus_Type()
)
virtualDiskPartitionFluidCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskPartitionFluidCacheStatus.setStatus("mandatory")
_VirtualDiskPartitionNexusID_Type = DisplayString
_VirtualDiskPartitionNexusID_Object = MibTableColumn
virtualDiskPartitionNexusID = _VirtualDiskPartitionNexusID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 2, 1, 6),
    _VirtualDiskPartitionNexusID_Type()
)
virtualDiskPartitionNexusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskPartitionNexusID.setStatus("mandatory")
_ArrayDiskLogicalConnectionTable_Object = MibTable
arrayDiskLogicalConnectionTable = _ArrayDiskLogicalConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3)
)
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionTable.setStatus("mandatory")
_ArrayDiskLogicalConnectionEntry_Object = MibTableRow
arrayDiskLogicalConnectionEntry = _ArrayDiskLogicalConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3, 1)
)
arrayDiskLogicalConnectionEntry.setIndexNames(
    (0, "StorageManagement-MIB", "arrayDiskLogicalConnectionNumber"),
)
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionEntry.setStatus("mandatory")


class _ArrayDiskLogicalConnectionNumber_Type(Integer32):
    """Custom type arrayDiskLogicalConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_ArrayDiskLogicalConnectionNumber_Type.__name__ = "Integer32"
_ArrayDiskLogicalConnectionNumber_Object = MibTableColumn
arrayDiskLogicalConnectionNumber = _ArrayDiskLogicalConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3, 1, 1),
    _ArrayDiskLogicalConnectionNumber_Type()
)
arrayDiskLogicalConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionNumber.setStatus("mandatory")
_ArrayDiskLogicalConnectionArrayDiskName_Type = DisplayString
_ArrayDiskLogicalConnectionArrayDiskName_Object = MibTableColumn
arrayDiskLogicalConnectionArrayDiskName = _ArrayDiskLogicalConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3, 1, 2),
    _ArrayDiskLogicalConnectionArrayDiskName_Type()
)
arrayDiskLogicalConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionArrayDiskName.setStatus("mandatory")
_ArrayDiskLogicalConnectionArrayDiskNumber_Type = Integer32
_ArrayDiskLogicalConnectionArrayDiskNumber_Object = MibTableColumn
arrayDiskLogicalConnectionArrayDiskNumber = _ArrayDiskLogicalConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3, 1, 3),
    _ArrayDiskLogicalConnectionArrayDiskNumber_Type()
)
arrayDiskLogicalConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionArrayDiskNumber.setStatus("mandatory")
_ArrayDiskLogicalConnectionVirtualDiskName_Type = DisplayString
_ArrayDiskLogicalConnectionVirtualDiskName_Object = MibTableColumn
arrayDiskLogicalConnectionVirtualDiskName = _ArrayDiskLogicalConnectionVirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3, 1, 4),
    _ArrayDiskLogicalConnectionVirtualDiskName_Type()
)
arrayDiskLogicalConnectionVirtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionVirtualDiskName.setStatus("mandatory")
_ArrayDiskLogicalConnectionVirtualDiskNumber_Type = Integer32
_ArrayDiskLogicalConnectionVirtualDiskNumber_Object = MibTableColumn
arrayDiskLogicalConnectionVirtualDiskNumber = _ArrayDiskLogicalConnectionVirtualDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3, 1, 5),
    _ArrayDiskLogicalConnectionVirtualDiskNumber_Type()
)
arrayDiskLogicalConnectionVirtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionVirtualDiskNumber.setStatus("mandatory")
_ArrayDiskLogicalConnectionDiskName_Type = DisplayString
_ArrayDiskLogicalConnectionDiskName_Object = MibTableColumn
arrayDiskLogicalConnectionDiskName = _ArrayDiskLogicalConnectionDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3, 1, 6),
    _ArrayDiskLogicalConnectionDiskName_Type()
)
arrayDiskLogicalConnectionDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionDiskName.setStatus("mandatory")
_ArrayDiskLogicalConnectionDiskNumber_Type = Integer32
_ArrayDiskLogicalConnectionDiskNumber_Object = MibTableColumn
arrayDiskLogicalConnectionDiskNumber = _ArrayDiskLogicalConnectionDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 3, 1, 7),
    _ArrayDiskLogicalConnectionDiskNumber_Type()
)
arrayDiskLogicalConnectionDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionDiskNumber.setStatus("mandatory")
_FluidCacheTable_Object = MibTable
fluidCacheTable = _FluidCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4)
)
if mibBuilder.loadTexts:
    fluidCacheTable.setStatus("mandatory")
_FluidCacheEntry_Object = MibTableRow
fluidCacheEntry = _FluidCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1)
)
fluidCacheEntry.setIndexNames(
    (0, "StorageManagement-MIB", "fluidCacheNumber"),
)
if mibBuilder.loadTexts:
    fluidCacheEntry.setStatus("mandatory")


class _FluidCacheNumber_Type(Integer32):
    """Custom type fluidCacheNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FluidCacheNumber_Type.__name__ = "Integer32"
_FluidCacheNumber_Object = MibTableColumn
fluidCacheNumber = _FluidCacheNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 1),
    _FluidCacheNumber_Type()
)
fluidCacheNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheNumber.setStatus("mandatory")
_FluidCacheName_Type = OctetString
_FluidCacheName_Object = MibTableColumn
fluidCacheName = _FluidCacheName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 2),
    _FluidCacheName_Type()
)
fluidCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheName.setStatus("mandatory")
_FluidCacheLicenseState_Type = OctetString
_FluidCacheLicenseState_Object = MibTableColumn
fluidCacheLicenseState = _FluidCacheLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 3),
    _FluidCacheLicenseState_Type()
)
fluidCacheLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseState.setStatus("mandatory")
_FluidCacheLicenseValidity_Type = Integer32
_FluidCacheLicenseValidity_Object = MibTableColumn
fluidCacheLicenseValidity = _FluidCacheLicenseValidity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 4),
    _FluidCacheLicenseValidity_Type()
)
fluidCacheLicenseValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseValidity.setStatus("mandatory")
_FluidCacheLicenseEntitlementID_Type = OctetString
_FluidCacheLicenseEntitlementID_Object = MibTableColumn
fluidCacheLicenseEntitlementID = _FluidCacheLicenseEntitlementID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 5),
    _FluidCacheLicenseEntitlementID_Type()
)
fluidCacheLicenseEntitlementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseEntitlementID.setStatus("mandatory")
_FluidCacheLicenseDuration_Type = OctetString
_FluidCacheLicenseDuration_Object = MibTableColumn
fluidCacheLicenseDuration = _FluidCacheLicenseDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 6),
    _FluidCacheLicenseDuration_Type()
)
fluidCacheLicenseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseDuration.setStatus("mandatory")
_FluidCacheLicenseCapacity_Type = OctetString
_FluidCacheLicenseCapacity_Object = MibTableColumn
fluidCacheLicenseCapacity = _FluidCacheLicenseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 7),
    _FluidCacheLicenseCapacity_Type()
)
fluidCacheLicenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseCapacity.setStatus("mandatory")
_FluidCacheLicenseRemaining_Type = OctetString
_FluidCacheLicenseRemaining_Object = MibTableColumn
fluidCacheLicenseRemaining = _FluidCacheLicenseRemaining_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 8),
    _FluidCacheLicenseRemaining_Type()
)
fluidCacheLicenseRemaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fluidCacheLicenseRemaining.setStatus("mandatory")
_FluidCacheLicenseType_Type = OctetString
_FluidCacheLicenseType_Object = MibTableColumn
fluidCacheLicenseType = _FluidCacheLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 9),
    _FluidCacheLicenseType_Type()
)
fluidCacheLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseType.setStatus("mandatory")
_FluidCacheLicenseVendor_Type = OctetString
_FluidCacheLicenseVendor_Object = MibTableColumn
fluidCacheLicenseVendor = _FluidCacheLicenseVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 10),
    _FluidCacheLicenseVendor_Type()
)
fluidCacheLicenseVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseVendor.setStatus("mandatory")
_FluidCacheLicenseProductId_Type = OctetString
_FluidCacheLicenseProductId_Object = MibTableColumn
fluidCacheLicenseProductId = _FluidCacheLicenseProductId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 11),
    _FluidCacheLicenseProductId_Type()
)
fluidCacheLicenseProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseProductId.setStatus("mandatory")
_FluidCacheLicenseDateSold_Type = OctetString
_FluidCacheLicenseDateSold_Object = MibTableColumn
fluidCacheLicenseDateSold = _FluidCacheLicenseDateSold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 12),
    _FluidCacheLicenseDateSold_Type()
)
fluidCacheLicenseDateSold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseDateSold.setStatus("mandatory")
_FluidCacheLicenseGeneration_Type = OctetString
_FluidCacheLicenseGeneration_Object = MibTableColumn
fluidCacheLicenseGeneration = _FluidCacheLicenseGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 13),
    _FluidCacheLicenseGeneration_Type()
)
fluidCacheLicenseGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseGeneration.setStatus("mandatory")
_FluidCacheLicenseFeatureID_Type = OctetString
_FluidCacheLicenseFeatureID_Object = MibTableColumn
fluidCacheLicenseFeatureID = _FluidCacheLicenseFeatureID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 14),
    _FluidCacheLicenseFeatureID_Type()
)
fluidCacheLicenseFeatureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseFeatureID.setStatus("mandatory")
_FluidCacheLicenseFeatureDescription_Type = OctetString
_FluidCacheLicenseFeatureDescription_Object = MibTableColumn
fluidCacheLicenseFeatureDescription = _FluidCacheLicenseFeatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 15),
    _FluidCacheLicenseFeatureDescription_Type()
)
fluidCacheLicenseFeatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheLicenseFeatureDescription.setStatus("mandatory")
_FluidCacheNexus_Type = OctetString
_FluidCacheNexus_Object = MibTableColumn
fluidCacheNexus = _FluidCacheNexus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 4, 1, 16),
    _FluidCacheNexus_Type()
)
fluidCacheNexus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheNexus.setStatus("mandatory")
_FluidCacheDiskTable_Object = MibTable
fluidCacheDiskTable = _FluidCacheDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5)
)
if mibBuilder.loadTexts:
    fluidCacheDiskTable.setStatus("mandatory")
_FluidCacheDiskEntry_Object = MibTableRow
fluidCacheDiskEntry = _FluidCacheDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1)
)
fluidCacheDiskEntry.setIndexNames(
    (0, "StorageManagement-MIB", "fluidCacheDiskNumber"),
)
if mibBuilder.loadTexts:
    fluidCacheDiskEntry.setStatus("mandatory")


class _FluidCacheDiskNumber_Type(Integer32):
    """Custom type fluidCacheDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FluidCacheDiskNumber_Type.__name__ = "Integer32"
_FluidCacheDiskNumber_Object = MibTableColumn
fluidCacheDiskNumber = _FluidCacheDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 1),
    _FluidCacheDiskNumber_Type()
)
fluidCacheDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskNumber.setStatus("mandatory")
_FluidCacheDiskName_Type = OctetString
_FluidCacheDiskName_Object = MibTableColumn
fluidCacheDiskName = _FluidCacheDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 2),
    _FluidCacheDiskName_Type()
)
fluidCacheDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskName.setStatus("mandatory")
_FluidCacheDiskState_Type = Integer32
_FluidCacheDiskState_Object = MibTableColumn
fluidCacheDiskState = _FluidCacheDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 3),
    _FluidCacheDiskState_Type()
)
fluidCacheDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskState.setStatus("mandatory")
_FluidCacheDiskBackendDeviceType_Type = Integer32
_FluidCacheDiskBackendDeviceType_Object = MibTableColumn
fluidCacheDiskBackendDeviceType = _FluidCacheDiskBackendDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 4),
    _FluidCacheDiskBackendDeviceType_Type()
)
fluidCacheDiskBackendDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskBackendDeviceType.setStatus("mandatory")
_FluidCacheDiskBackendDeviceName_Type = OctetString
_FluidCacheDiskBackendDeviceName_Object = MibTableColumn
fluidCacheDiskBackendDeviceName = _FluidCacheDiskBackendDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 5),
    _FluidCacheDiskBackendDeviceName_Type()
)
fluidCacheDiskBackendDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskBackendDeviceName.setStatus("mandatory")
_FluidCacheDiskBackendDeviceSize_Type = Integer32
_FluidCacheDiskBackendDeviceSize_Object = MibTableColumn
fluidCacheDiskBackendDeviceSize = _FluidCacheDiskBackendDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 6),
    _FluidCacheDiskBackendDeviceSize_Type()
)
fluidCacheDiskBackendDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskBackendDeviceSize.setStatus("mandatory")
_FluidCacheDiskOperatingMode_Type = Integer32
_FluidCacheDiskOperatingMode_Object = MibTableColumn
fluidCacheDiskOperatingMode = _FluidCacheDiskOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 7),
    _FluidCacheDiskOperatingMode_Type()
)
fluidCacheDiskOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskOperatingMode.setStatus("mandatory")
_FluidCacheDiskConfiguredMode_Type = Integer32
_FluidCacheDiskConfiguredMode_Object = MibTableColumn
fluidCacheDiskConfiguredMode = _FluidCacheDiskConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 8),
    _FluidCacheDiskConfiguredMode_Type()
)
fluidCacheDiskConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskConfiguredMode.setStatus("mandatory")
_FluidCacheDiskNexus_Type = OctetString
_FluidCacheDiskNexus_Object = MibTableColumn
fluidCacheDiskNexus = _FluidCacheDiskNexus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 9),
    _FluidCacheDiskNexus_Type()
)
fluidCacheDiskNexus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fluidCacheDiskNexus.setStatus("mandatory")
_FluidCacheDiskStatus_Type = Integer32
_FluidCacheDiskStatus_Object = MibTableColumn
fluidCacheDiskStatus = _FluidCacheDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 5, 1, 10),
    _FluidCacheDiskStatus_Type()
)
fluidCacheDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCacheDiskStatus.setStatus("mandatory")
_FluidCachePoolTable_Object = MibTable
fluidCachePoolTable = _FluidCachePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6)
)
if mibBuilder.loadTexts:
    fluidCachePoolTable.setStatus("mandatory")
_FluidCachePoolEntry_Object = MibTableRow
fluidCachePoolEntry = _FluidCachePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1)
)
fluidCachePoolEntry.setIndexNames(
    (0, "StorageManagement-MIB", "fluidCachePoolNumber"),
)
if mibBuilder.loadTexts:
    fluidCachePoolEntry.setStatus("mandatory")


class _FluidCachePoolNumber_Type(Integer32):
    """Custom type fluidCachePoolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FluidCachePoolNumber_Type.__name__ = "Integer32"
_FluidCachePoolNumber_Object = MibTableColumn
fluidCachePoolNumber = _FluidCachePoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1, 1),
    _FluidCachePoolNumber_Type()
)
fluidCachePoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCachePoolNumber.setStatus("mandatory")
_FluidCachePoolStoreCount_Type = Integer32
_FluidCachePoolStoreCount_Object = MibTableColumn
fluidCachePoolStoreCount = _FluidCachePoolStoreCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1, 2),
    _FluidCachePoolStoreCount_Type()
)
fluidCachePoolStoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCachePoolStoreCount.setStatus("mandatory")
_FluidCachePoolUUID_Type = OctetString
_FluidCachePoolUUID_Object = MibTableColumn
fluidCachePoolUUID = _FluidCachePoolUUID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1, 3),
    _FluidCachePoolUUID_Type()
)
fluidCachePoolUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCachePoolUUID.setStatus("mandatory")
_FluidCachePoolLicenseState_Type = DisplayString
_FluidCachePoolLicenseState_Object = MibTableColumn
fluidCachePoolLicenseState = _FluidCachePoolLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1, 4),
    _FluidCachePoolLicenseState_Type()
)
fluidCachePoolLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCachePoolLicenseState.setStatus("mandatory")
_FluidCachePoolSize_Type = Integer32
_FluidCachePoolSize_Object = MibTableColumn
fluidCachePoolSize = _FluidCachePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1, 5),
    _FluidCachePoolSize_Type()
)
fluidCachePoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCachePoolSize.setStatus("mandatory")
_FluidCachePoolHighAvailabilityState_Type = OctetString
_FluidCachePoolHighAvailabilityState_Object = MibTableColumn
fluidCachePoolHighAvailabilityState = _FluidCachePoolHighAvailabilityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1, 6),
    _FluidCachePoolHighAvailabilityState_Type()
)
fluidCachePoolHighAvailabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCachePoolHighAvailabilityState.setStatus("mandatory")
_FluidCachePoolNexus_Type = OctetString
_FluidCachePoolNexus_Object = MibTableColumn
fluidCachePoolNexus = _FluidCachePoolNexus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1, 7),
    _FluidCachePoolNexus_Type()
)
fluidCachePoolNexus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCachePoolNexus.setStatus("mandatory")
_FluidCachePoolStatus_Type = Integer32
_FluidCachePoolStatus_Object = MibTableColumn
fluidCachePoolStatus = _FluidCachePoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 140, 6, 1, 8),
    _FluidCachePoolStatus_Type()
)
fluidCachePoolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidCachePoolStatus.setStatus("mandatory")
_StorageManagementEvent_ObjectIdentity = ObjectIdentity
storageManagementEvent = _StorageManagementEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200)
)
_MessageIDEvent_Type = Integer32
_MessageIDEvent_Object = MibScalar
messageIDEvent = _MessageIDEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 1),
    _MessageIDEvent_Type()
)
messageIDEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageIDEvent.setStatus("mandatory")


class _DescriptionEvent_Type(DisplayString):
    """Custom type descriptionEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DescriptionEvent_Type.__name__ = "DisplayString"
_DescriptionEvent_Object = MibScalar
descriptionEvent = _DescriptionEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 2),
    _DescriptionEvent_Type()
)
descriptionEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    descriptionEvent.setStatus("mandatory")
_LocationEvent_Type = DisplayString
_LocationEvent_Object = MibScalar
locationEvent = _LocationEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 3),
    _LocationEvent_Type()
)
locationEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locationEvent.setStatus("mandatory")
_ObjectNameEvent_Type = DisplayString
_ObjectNameEvent_Object = MibScalar
objectNameEvent = _ObjectNameEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 4),
    _ObjectNameEvent_Type()
)
objectNameEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectNameEvent.setStatus("mandatory")


class _ObjectOIDEvent_Type(DisplayString):
    """Custom type objectOIDEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ObjectOIDEvent_Type.__name__ = "DisplayString"
_ObjectOIDEvent_Object = MibScalar
objectOIDEvent = _ObjectOIDEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 5),
    _ObjectOIDEvent_Type()
)
objectOIDEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectOIDEvent.setStatus("mandatory")


class _ObjectNexusEvent_Type(DisplayString):
    """Custom type objectNexusEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ObjectNexusEvent_Type.__name__ = "DisplayString"
_ObjectNexusEvent_Object = MibScalar
objectNexusEvent = _ObjectNexusEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 6),
    _ObjectNexusEvent_Type()
)
objectNexusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectNexusEvent.setStatus("mandatory")
_CurrentStatusEvent_Type = DellStatus
_CurrentStatusEvent_Object = MibScalar
currentStatusEvent = _CurrentStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 7),
    _CurrentStatusEvent_Type()
)
currentStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentStatusEvent.setStatus("mandatory")
_PreviousStatusEvent_Type = DellStatus
_PreviousStatusEvent_Object = MibScalar
previousStatusEvent = _PreviousStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 8),
    _PreviousStatusEvent_Type()
)
previousStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    previousStatusEvent.setStatus("mandatory")
_EnhancedMessageIDEvent_Type = DisplayString
_EnhancedMessageIDEvent_Object = MibScalar
enhancedMessageIDEvent = _EnhancedMessageIDEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 9),
    _EnhancedMessageIDEvent_Type()
)
enhancedMessageIDEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enhancedMessageIDEvent.setStatus("mandatory")
_SystemFQDNEvent_Type = DisplayString
_SystemFQDNEvent_Object = MibScalar
systemFQDNEvent = _SystemFQDNEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 10),
    _SystemFQDNEvent_Type()
)
systemFQDNEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFQDNEvent.setStatus("mandatory")
_ServiceTagEvent_Type = DisplayString
_ServiceTagEvent_Object = MibScalar
serviceTagEvent = _ServiceTagEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 11),
    _ServiceTagEvent_Type()
)
serviceTagEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceTagEvent.setStatus("mandatory")
_ChassisServiceTagEvent_Type = DisplayString
_ChassisServiceTagEvent_Object = MibScalar
chassisServiceTagEvent = _ChassisServiceTagEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 12),
    _ChassisServiceTagEvent_Type()
)
chassisServiceTagEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisServiceTagEvent.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alertStorageManagementInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 101)
)
alertStorageManagementInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"))
)
if mibBuilder.loadTexts:
    alertStorageManagementInformation.setStatus(
        ""
    )

alertStorageManagementNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 102)
)
alertStorageManagementNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"))
)
if mibBuilder.loadTexts:
    alertStorageManagementNormal.setStatus(
        ""
    )

alertStorageManagementWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 103)
)
alertStorageManagementWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"))
)
if mibBuilder.loadTexts:
    alertStorageManagementWarning.setStatus(
        ""
    )

alertStorageManagementFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 104)
)
alertStorageManagementFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"))
)
if mibBuilder.loadTexts:
    alertStorageManagementFailure.setStatus(
        ""
    )

alertStorageManagementNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 105)
)
alertStorageManagementNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"))
)
if mibBuilder.loadTexts:
    alertStorageManagementNonRecoverable.setStatus(
        ""
    )

alertControllerInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 751)
)
alertControllerInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertControllerInformation.setStatus(
        ""
    )

alertControllerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 752)
)
alertControllerNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertControllerNormal.setStatus(
        ""
    )

alertControllerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 753)
)
alertControllerWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertControllerWarning.setStatus(
        ""
    )

alertControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 754)
)
alertControllerFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertControllerFailure.setStatus(
        ""
    )

alertControllerNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 755)
)
alertControllerNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertControllerNonRecoverable.setStatus(
        ""
    )

alertChannelInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 801)
)
alertChannelInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertChannelInformation.setStatus(
        ""
    )

alertChannelNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 802)
)
alertChannelNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertChannelNormal.setStatus(
        ""
    )

alertChannelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 803)
)
alertChannelWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertChannelWarning.setStatus(
        ""
    )

alertChannelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 804)
)
alertChannelFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertChannelFailure.setStatus(
        ""
    )

alertChannelNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 805)
)
alertChannelNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertChannelNonRecoverable.setStatus(
        ""
    )

alertEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 851)
)
alertEnclosureInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEnclosureInformation.setStatus(
        ""
    )

alertEnclosureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 852)
)
alertEnclosureNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEnclosureNormal.setStatus(
        ""
    )

alertEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 853)
)
alertEnclosureWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEnclosureWarning.setStatus(
        ""
    )

alertEnclosureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 854)
)
alertEnclosureFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEnclosureFailure.setStatus(
        ""
    )

alertEnclosureNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 855)
)
alertEnclosureNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEnclosureNonRecoverable.setStatus(
        ""
    )

alertArrayDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 901)
)
alertArrayDiskInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertArrayDiskInformation.setStatus(
        ""
    )

alertArrayDiskNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 902)
)
alertArrayDiskNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertArrayDiskNormal.setStatus(
        ""
    )

alertArrayDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 903)
)
alertArrayDiskWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertArrayDiskWarning.setStatus(
        ""
    )

alertArrayDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 904)
)
alertArrayDiskFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertArrayDiskFailure.setStatus(
        ""
    )

alertArrayDiskNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 905)
)
alertArrayDiskNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertArrayDiskNonRecoverable.setStatus(
        ""
    )

alertEMMInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 951)
)
alertEMMInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEMMInformation.setStatus(
        ""
    )

alertEMMNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 952)
)
alertEMMNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEMMNormal.setStatus(
        ""
    )

alertEMMWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 953)
)
alertEMMWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEMMWarning.setStatus(
        ""
    )

alertEMMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 954)
)
alertEMMFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEMMFailure.setStatus(
        ""
    )

alertEMMNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 955)
)
alertEMMNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertEMMNonRecoverable.setStatus(
        ""
    )

alertPowerSupplyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1001)
)
alertPowerSupplyInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyInformation.setStatus(
        ""
    )

alertPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1002)
)
alertPowerSupplyNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyNormal.setStatus(
        ""
    )

alertPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1003)
)
alertPowerSupplyWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyWarning.setStatus(
        ""
    )

alertPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1004)
)
alertPowerSupplyFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyFailure.setStatus(
        ""
    )

alertPowerSupplyNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1005)
)
alertPowerSupplyNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyNonRecoverable.setStatus(
        ""
    )

alertTemperatureProbeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1051)
)
alertTemperatureProbeInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeInformation.setStatus(
        ""
    )

alertTemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1052)
)
alertTemperatureProbeNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeNormal.setStatus(
        ""
    )

alertTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1053)
)
alertTemperatureProbeWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeWarning.setStatus(
        ""
    )

alertTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1054)
)
alertTemperatureProbeFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeFailure.setStatus(
        ""
    )

alertTemperatureProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1055)
)
alertTemperatureProbeNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeNonRecoverable.setStatus(
        ""
    )

alertFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1101)
)
alertFanInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFanInformation.setStatus(
        ""
    )

alertFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1102)
)
alertFanNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFanNormal.setStatus(
        ""
    )

alertFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1103)
)
alertFanWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFanWarning.setStatus(
        ""
    )

alertFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1104)
)
alertFanFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFanFailure.setStatus(
        ""
    )

alertFanNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1105)
)
alertFanNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFanNonRecoverable.setStatus(
        ""
    )

alertBatteryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1151)
)
alertBatteryInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertBatteryInformation.setStatus(
        ""
    )

alertBatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1152)
)
alertBatteryNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertBatteryNormal.setStatus(
        ""
    )

alertBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1153)
)
alertBatteryWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertBatteryWarning.setStatus(
        ""
    )

alertBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1154)
)
alertBatteryFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertBatteryFailure.setStatus(
        ""
    )

alertBatteryNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1155)
)
alertBatteryNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertBatteryNonRecoverable.setStatus(
        ""
    )

alertVirtualDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1201)
)
alertVirtualDiskInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskInformation.setStatus(
        ""
    )

alertVirtualDiskNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1202)
)
alertVirtualDiskNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskNormal.setStatus(
        ""
    )

alertVirtualDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1203)
)
alertVirtualDiskWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskWarning.setStatus(
        ""
    )

alertVirtualDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1204)
)
alertVirtualDiskFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskFailure.setStatus(
        ""
    )

alertVirtualDiskNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1205)
)
alertVirtualDiskNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskNonRecoverable.setStatus(
        ""
    )

alertRedundancyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1304)
)
alertRedundancyNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertRedundancyNormal.setStatus(
        ""
    )

alertRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1305)
)
alertRedundancyDegraded.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertRedundancyDegraded.setStatus(
        ""
    )

alertRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1306)
)
alertRedundancyLost.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertRedundancyLost.setStatus(
        ""
    )

alertFluidCacheDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1401)
)
alertFluidCacheDiskInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFluidCacheDiskInformation.setStatus(
        ""
    )

alertfluidCacheDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1403)
)
alertfluidCacheDiskWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertfluidCacheDiskWarning.setStatus(
        ""
    )

alertFluidCacheDisklFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1404)
)
alertFluidCacheDisklFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFluidCacheDisklFailure.setStatus(
        ""
    )

alertVirtualDiskPartitionInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1501)
)
alertVirtualDiskPartitionInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskPartitionInformation.setStatus(
        ""
    )

alertVirtualDiskPartitionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1503)
)
alertVirtualDiskPartitionWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskPartitionWarning.setStatus(
        ""
    )

alertVirtualDiskPartitionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1504)
)
alertVirtualDiskPartitionFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskPartitionFailure.setStatus(
        ""
    )

alertFluidCacheInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1601)
)
alertFluidCacheInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFluidCacheInformation.setStatus(
        ""
    )

alertfluidCacheWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1603)
)
alertfluidCacheWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertfluidCacheWarning.setStatus(
        ""
    )

alertFluidCacheFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1604)
)
alertFluidCacheFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFluidCacheFailure.setStatus(
        ""
    )

alertFluidCachePoolInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1701)
)
alertFluidCachePoolInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFluidCachePoolInformation.setStatus(
        ""
    )

alertfluidCachePoolWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1703)
)
alertfluidCachePoolWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertfluidCachePoolWarning.setStatus(
        ""
    )

alertFluidCachePoolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 1704)
)
alertFluidCachePoolFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"))
)
if mibBuilder.loadTexts:
    alertFluidCachePoolFailure.setStatus(
        ""
    )

alertEEMIStorageManagementInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 10100)
)
alertEEMIStorageManagementInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIStorageManagementInformation.setStatus(
        ""
    )

alertEEMIStorageManagementNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 10200)
)
alertEEMIStorageManagementNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIStorageManagementNormal.setStatus(
        ""
    )

alertEEMIStorageManagementWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 10300)
)
alertEEMIStorageManagementWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIStorageManagementWarning.setStatus(
        ""
    )

alertEEMIStorageManagementFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 10400)
)
alertEEMIStorageManagementFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIStorageManagementFailure.setStatus(
        ""
    )

alertEEMIStorageManagementNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 10500)
)
alertEEMIStorageManagementNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIStorageManagementNonRecoverable.setStatus(
        ""
    )

alertEEMIControllerInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 75100)
)
alertEEMIControllerInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIControllerInformation.setStatus(
        ""
    )

alertEEMIControllerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 75200)
)
alertEEMIControllerNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIControllerNormal.setStatus(
        ""
    )

alertEEMIControllerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 75300)
)
alertEEMIControllerWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIControllerWarning.setStatus(
        ""
    )

alertEEMIControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 75400)
)
alertEEMIControllerFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIControllerFailure.setStatus(
        ""
    )

alertEEMIControllerNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 75500)
)
alertEEMIControllerNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIControllerNonRecoverable.setStatus(
        ""
    )

alertEEMIChannelInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 80100)
)
alertEEMIChannelInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIChannelInformation.setStatus(
        ""
    )

alertEEMIChannelNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 80200)
)
alertEEMIChannelNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIChannelNormal.setStatus(
        ""
    )

alertEEMIChannelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 80300)
)
alertEEMIChannelWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIChannelWarning.setStatus(
        ""
    )

alertEEMIChannelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 80400)
)
alertEEMIChannelFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIChannelFailure.setStatus(
        ""
    )

alertEEMIChannelNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 80500)
)
alertEEMIChannelNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIChannelNonRecoverable.setStatus(
        ""
    )

alertEEMIEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 85100)
)
alertEEMIEnclosureInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEnclosureInformation.setStatus(
        ""
    )

alertEEMIEnclosureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 85200)
)
alertEEMIEnclosureNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEnclosureNormal.setStatus(
        ""
    )

alertEEMIEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 85300)
)
alertEEMIEnclosureWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEnclosureWarning.setStatus(
        ""
    )

alertEEMIEnclosureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 85400)
)
alertEEMIEnclosureFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEnclosureFailure.setStatus(
        ""
    )

alertEEMIEnclosureNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 85500)
)
alertEEMIEnclosureNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEnclosureNonRecoverable.setStatus(
        ""
    )

alertEEMIArrayDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 90100)
)
alertEEMIArrayDiskInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIArrayDiskInformation.setStatus(
        ""
    )

alertEEMIArrayDiskNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 90200)
)
alertEEMIArrayDiskNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIArrayDiskNormal.setStatus(
        ""
    )

alertEEMIArrayDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 90300)
)
alertEEMIArrayDiskWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIArrayDiskWarning.setStatus(
        ""
    )

alertEEMIArrayDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 90400)
)
alertEEMIArrayDiskFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIArrayDiskFailure.setStatus(
        ""
    )

alertEEMIArrayDiskNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 90500)
)
alertEEMIArrayDiskNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIArrayDiskNonRecoverable.setStatus(
        ""
    )

alertEMMEMMInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 95100)
)
alertEMMEMMInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEMMEMMInformation.setStatus(
        ""
    )

alertEEMIEMMNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 95200)
)
alertEEMIEMMNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEMMNormal.setStatus(
        ""
    )

alertEEMIEMMWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 95300)
)
alertEEMIEMMWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEMMWarning.setStatus(
        ""
    )

alertEEMIEMMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 95400)
)
alertEEMIEMMFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEMMFailure.setStatus(
        ""
    )

alertEEMIEMMNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 95500)
)
alertEEMIEMMNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIEMMNonRecoverable.setStatus(
        ""
    )

alertEEMIPowerSupplyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 100100)
)
alertEEMIPowerSupplyInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIPowerSupplyInformation.setStatus(
        ""
    )

alertEEMIPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 100200)
)
alertEEMIPowerSupplyNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIPowerSupplyNormal.setStatus(
        ""
    )

alertEEMIPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 100300)
)
alertEEMIPowerSupplyWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIPowerSupplyWarning.setStatus(
        ""
    )

alertEEMIPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 100400)
)
alertEEMIPowerSupplyFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIPowerSupplyFailure.setStatus(
        ""
    )

alertEEMIPowerSupplyNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 100500)
)
alertEEMIPowerSupplyNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIPowerSupplyNonRecoverable.setStatus(
        ""
    )

alertEEMITemperatureProbeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 105100)
)
alertEEMITemperatureProbeInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMITemperatureProbeInformation.setStatus(
        ""
    )

alertEEMITemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 105200)
)
alertEEMITemperatureProbeNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMITemperatureProbeNormal.setStatus(
        ""
    )

alertEEMITemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 105300)
)
alertEEMITemperatureProbeWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMITemperatureProbeWarning.setStatus(
        ""
    )

alertEEMITemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 105400)
)
alertEEMITemperatureProbeFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMITemperatureProbeFailure.setStatus(
        ""
    )

alertEEMITemperatureProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 105500)
)
alertEEMITemperatureProbeNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMITemperatureProbeNonRecoverable.setStatus(
        ""
    )

alertEEMIFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 110100)
)
alertEEMIFanInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFanInformation.setStatus(
        ""
    )

alertEEMIFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 110200)
)
alertEEMIFanNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFanNormal.setStatus(
        ""
    )

alertEEMIFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 110300)
)
alertEEMIFanWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFanWarning.setStatus(
        ""
    )

alertEEMIFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 110400)
)
alertEEMIFanFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFanFailure.setStatus(
        ""
    )

alertEEMIFanNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 110500)
)
alertEEMIFanNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFanNonRecoverable.setStatus(
        ""
    )

alertEEMIBatteryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 115100)
)
alertEEMIBatteryInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIBatteryInformation.setStatus(
        ""
    )

alertEEMIBatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 115200)
)
alertEEMIBatteryNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIBatteryNormal.setStatus(
        ""
    )

alertEEMIBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 115300)
)
alertEEMIBatteryWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIBatteryWarning.setStatus(
        ""
    )

alertEEMIBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 115400)
)
alertEEMIBatteryFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIBatteryFailure.setStatus(
        ""
    )

alertEEMIBatteryNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 115500)
)
alertEEMIBatteryNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIBatteryNonRecoverable.setStatus(
        ""
    )

alertEEMIVirtualDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 120100)
)
alertEEMIVirtualDiskInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIVirtualDiskInformation.setStatus(
        ""
    )

alertEEMIVirtualDiskNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 120200)
)
alertEEMIVirtualDiskNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIVirtualDiskNormal.setStatus(
        ""
    )

alertEEMIVirtualDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 120300)
)
alertEEMIVirtualDiskWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIVirtualDiskWarning.setStatus(
        ""
    )

alertEEMIVirtualDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 120400)
)
alertEEMIVirtualDiskFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIVirtualDiskFailure.setStatus(
        ""
    )

alertEEMIVirtualDiskNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 120500)
)
alertEEMIVirtualDiskNonRecoverable.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIVirtualDiskNonRecoverable.setStatus(
        ""
    )

alertEEMIRedundancyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 130400)
)
alertEEMIRedundancyNormal.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIRedundancyNormal.setStatus(
        ""
    )

alertEEMIRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 130500)
)
alertEEMIRedundancyDegraded.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIRedundancyDegraded.setStatus(
        ""
    )

alertEEMIRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 130600)
)
alertEEMIRedundancyLost.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIRedundancyLost.setStatus(
        ""
    )

alertEEMIFluidCacheDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 140100)
)
alertEEMIFluidCacheDiskInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFluidCacheDiskInformation.setStatus(
        ""
    )

alertEEMIfluidCacheDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 140300)
)
alertEEMIfluidCacheDiskWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIfluidCacheDiskWarning.setStatus(
        ""
    )

alertEEMIFluidCacheDisklFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 140400)
)
alertEEMIFluidCacheDisklFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFluidCacheDisklFailure.setStatus(
        ""
    )

alertEEMIVirtualDiskPartitionInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 150100)
)
alertEEMIVirtualDiskPartitionInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIVirtualDiskPartitionInformation.setStatus(
        ""
    )

alertEEMIVirtualDiskPartitionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 150300)
)
alertEEMIVirtualDiskPartitionWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIVirtualDiskPartitionWarning.setStatus(
        ""
    )

alertEEMIVirtualDiskPartitionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 150400)
)
alertEEMIVirtualDiskPartitionFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIVirtualDiskPartitionFailure.setStatus(
        ""
    )

alertEEMIFluidCacheInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 160100)
)
alertEEMIFluidCacheInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFluidCacheInformation.setStatus(
        ""
    )

alertEEMIfluidCacheWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 160300)
)
alertEEMIfluidCacheWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIfluidCacheWarning.setStatus(
        ""
    )

alertEEMIFluidCacheFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 160400)
)
alertEEMIFluidCacheFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFluidCacheFailure.setStatus(
        ""
    )

alertEEMIFluidCachePoolInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 170100)
)
alertEEMIFluidCachePoolInformation.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFluidCachePoolInformation.setStatus(
        ""
    )

alertEEMIfluidCachePoolWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 170300)
)
alertEEMIfluidCachePoolWarning.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIfluidCachePoolWarning.setStatus(
        ""
    )

alertEEMIFluidCachePoolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 20, 200, 0, 170400)
)
alertEEMIFluidCachePoolFailure.setObjects(
      *(("StorageManagement-MIB", "messageIDEvent"),
        ("StorageManagement-MIB", "descriptionEvent"),
        ("StorageManagement-MIB", "locationEvent"),
        ("StorageManagement-MIB", "objectNameEvent"),
        ("StorageManagement-MIB", "objectOIDEvent"),
        ("StorageManagement-MIB", "objectNexusEvent"),
        ("StorageManagement-MIB", "currentStatusEvent"),
        ("StorageManagement-MIB", "previousStatusEvent"),
        ("StorageManagement-MIB", "enhancedMessageIDEvent"),
        ("StorageManagement-MIB", "systemFQDNEvent"),
        ("StorageManagement-MIB", "serviceTagEvent"),
        ("StorageManagement-MIB", "chassisServiceTagEvent"))
)
if mibBuilder.loadTexts:
    alertEEMIFluidCachePoolFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "StorageManagement-MIB",
    **{"DellStatus": DellStatus,
       "dell": dell,
       "storage": storage,
       "software": software,
       "storageManagement": storageManagement,
       "softwareVersion": softwareVersion,
       "globalStatus": globalStatus,
       "softwareManufacturer": softwareManufacturer,
       "softwareProduct": softwareProduct,
       "softwareDescription": softwareDescription,
       "storageManagementInfo": storageManagementInfo,
       "displayName": displayName,
       "description": description,
       "agentVendor": agentVendor,
       "agentVersion": agentVersion,
       "globalData": globalData,
       "agentSystemGlobalStatus": agentSystemGlobalStatus,
       "agentLastGlobalStatus": agentLastGlobalStatus,
       "agentTimeStamp": agentTimeStamp,
       "agentGetTimeout": agentGetTimeout,
       "agentModifiers": agentModifiers,
       "agentRefreshRate": agentRefreshRate,
       "agentHostname": agentHostname,
       "agentIPAddress": agentIPAddress,
       "agentSoftwareStatus": agentSoftwareStatus,
       "agentSnmpVersion": agentSnmpVersion,
       "agentMibVersion": agentMibVersion,
       "agentManagementSoftwareURLName": agentManagementSoftwareURLName,
       "agentGlobalSystemStatus": agentGlobalSystemStatus,
       "agentLastGlobalSystemStatus": agentLastGlobalSystemStatus,
       "agentSmartThermalShutdown": agentSmartThermalShutdown,
       "physicalDevices": physicalDevices,
       "controllerTable": controllerTable,
       "controllerEntry": controllerEntry,
       "controllerNumber": controllerNumber,
       "controllerName": controllerName,
       "controllerVendor": controllerVendor,
       "controllerType": controllerType,
       "controllerState": controllerState,
       "controllerSeverity": controllerSeverity,
       "controllerRebuildRateInPercent": controllerRebuildRateInPercent,
       "controllerFWVersion": controllerFWVersion,
       "controllerCacheSizeInMB": controllerCacheSizeInMB,
       "controllerCacheSizeInBytes": controllerCacheSizeInBytes,
       "controllerPhysicalDeviceCount": controllerPhysicalDeviceCount,
       "controllerLogicalDeviceCount": controllerLogicalDeviceCount,
       "controllerPartnerStatus": controllerPartnerStatus,
       "controllerHostPortCount": controllerHostPortCount,
       "controllerMemorySizeInMB": controllerMemorySizeInMB,
       "controllerMemorySizeInBytes": controllerMemorySizeInBytes,
       "controllerDriveChannelCount": controllerDriveChannelCount,
       "controllerFaultTolerant": controllerFaultTolerant,
       "controllerC0Port0WWN": controllerC0Port0WWN,
       "controllerC0Port0Name": controllerC0Port0Name,
       "controllerC0Port0ID": controllerC0Port0ID,
       "controllerC0Target": controllerC0Target,
       "controllerC0Channel": controllerC0Channel,
       "controllerC0OSController": controllerC0OSController,
       "controllerC0BatteryState": controllerC0BatteryState,
       "controllerC1Port0WWN": controllerC1Port0WWN,
       "controllerC1Port0Name": controllerC1Port0Name,
       "controllerC1Port0ID": controllerC1Port0ID,
       "controllerC1Target": controllerC1Target,
       "controllerC1Channel": controllerC1Channel,
       "controllerC1OSController": controllerC1OSController,
       "controllerC1BatteryState": controllerC1BatteryState,
       "controllerNodeWWN": controllerNodeWWN,
       "controllerC0Port1WWN": controllerC0Port1WWN,
       "controllerC1Port1WWN": controllerC1Port1WWN,
       "controllerBatteryChargeCount": controllerBatteryChargeCount,
       "controllerRollUpStatus": controllerRollUpStatus,
       "controllerComponentStatus": controllerComponentStatus,
       "controllerNexusID": controllerNexusID,
       "controllerAlarmState": controllerAlarmState,
       "controllerDriverVersion": controllerDriverVersion,
       "controllerPCISlot": controllerPCISlot,
       "controllerClusterMode": controllerClusterMode,
       "controllerMinFWVersion": controllerMinFWVersion,
       "controllerMinDriverVersion": controllerMinDriverVersion,
       "controllerSCSIInitiatorID": controllerSCSIInitiatorID,
       "controllerChannelCount": controllerChannelCount,
       "controllerReconstructRate": controllerReconstructRate,
       "controllerPatrolReadRate": controllerPatrolReadRate,
       "controllerBGIRate": controllerBGIRate,
       "controllerCheckConsistencyRate": controllerCheckConsistencyRate,
       "controllerPatrolReadMode": controllerPatrolReadMode,
       "controllerPatrolReadState": controllerPatrolReadState,
       "controllerPatrolReadIterations": controllerPatrolReadIterations,
       "controllerStorportDriverVersion": controllerStorportDriverVersion,
       "controllerMinRequiredStorportVer": controllerMinRequiredStorportVer,
       "controllerEncryptionCapable": controllerEncryptionCapable,
       "controllerEncryptionKeyPresent": controllerEncryptionKeyPresent,
       "controllerPersistentHotSpare": controllerPersistentHotSpare,
       "controllerSpinDownUnconfiguredDrives": controllerSpinDownUnconfiguredDrives,
       "controllerSpinDownHotSpareDrives": controllerSpinDownHotSpareDrives,
       "controllerSpinDownTimeInterval": controllerSpinDownTimeInterval,
       "controllerEncryptionMode": controllerEncryptionMode,
       "controllerCacheCade": controllerCacheCade,
       "controllerSpinDownConfiguredDrives": controllerSpinDownConfiguredDrives,
       "controllerAutomaticPowerSaving": controllerAutomaticPowerSaving,
       "controllerConfiguredDrivesSpinUpTime": controllerConfiguredDrivesSpinUpTime,
       "controllerConfiguredDrivesSpinUpTimeInterval": controllerConfiguredDrivesSpinUpTimeInterval,
       "controllerPreservedCache": controllerPreservedCache,
       "controllerPIEnable": controllerPIEnable,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channelNumber": channelNumber,
       "channelName": channelName,
       "channelState": channelState,
       "channelSeverity": channelSeverity,
       "channelTermination": channelTermination,
       "channelSCSIID": channelSCSIID,
       "channelRollUpStatus": channelRollUpStatus,
       "channelComponentStatus": channelComponentStatus,
       "channelNexusID": channelNexusID,
       "channelDataRate": channelDataRate,
       "channelBusType": channelBusType,
       "enclosureTable": enclosureTable,
       "enclosureEntry": enclosureEntry,
       "enclosureNumber": enclosureNumber,
       "enclosureName": enclosureName,
       "enclosureVendor": enclosureVendor,
       "enclosureState": enclosureState,
       "enclosureSeverity": enclosureSeverity,
       "enclosureID": enclosureID,
       "enclosureProcessorVersion": enclosureProcessorVersion,
       "enclosureServiceTag": enclosureServiceTag,
       "enclosureAssetTag": enclosureAssetTag,
       "enclosureAssetName": enclosureAssetName,
       "enclosureSplitBusPartNumber": enclosureSplitBusPartNumber,
       "enclosureProductID": enclosureProductID,
       "enclosureKernelVersion": enclosureKernelVersion,
       "enclosureESM1PartNumber": enclosureESM1PartNumber,
       "enclosureESM2PartNumber": enclosureESM2PartNumber,
       "enclosureType": enclosureType,
       "enclosureProcessor2Version": enclosureProcessor2Version,
       "enclosureConfig": enclosureConfig,
       "enclosureChannelNumber": enclosureChannelNumber,
       "enclosureAlarm": enclosureAlarm,
       "enclosureBackplanePartNumber": enclosureBackplanePartNumber,
       "enclosureSCSIID": enclosureSCSIID,
       "enclosureRollUpStatus": enclosureRollUpStatus,
       "enclosureComponentStatus": enclosureComponentStatus,
       "enclosureNexusID": enclosureNexusID,
       "enclosureFirmwareVersion": enclosureFirmwareVersion,
       "enclosureSCSIRate": enclosureSCSIRate,
       "enclosurePartNumber": enclosurePartNumber,
       "enclosureSerialNumber": enclosureSerialNumber,
       "enclosureSASAddress": enclosureSASAddress,
       "enclosureOccupiedSlotCount": enclosureOccupiedSlotCount,
       "enclosureTotalSlots": enclosureTotalSlots,
       "enclosureEmptySlotCount": enclosureEmptySlotCount,
       "enclosureExpressServiceCode": enclosureExpressServiceCode,
       "arrayDiskTable": arrayDiskTable,
       "arrayDiskEntry": arrayDiskEntry,
       "arrayDiskNumber": arrayDiskNumber,
       "arrayDiskName": arrayDiskName,
       "arrayDiskVendor": arrayDiskVendor,
       "arrayDiskState": arrayDiskState,
       "arrayDiskSeverity": arrayDiskSeverity,
       "arrayDiskProductID": arrayDiskProductID,
       "arrayDiskSerialNo": arrayDiskSerialNo,
       "arrayDiskRevision": arrayDiskRevision,
       "arrayDiskEnclosureID": arrayDiskEnclosureID,
       "arrayDiskChannel": arrayDiskChannel,
       "arrayDiskLengthInMB": arrayDiskLengthInMB,
       "arrayDiskLengthInBytes": arrayDiskLengthInBytes,
       "arrayDiskLargestContiguousFreeSpaceInMB": arrayDiskLargestContiguousFreeSpaceInMB,
       "arrayDiskLargestContiguousFreeSpaceInBytes": arrayDiskLargestContiguousFreeSpaceInBytes,
       "arrayDiskTargetID": arrayDiskTargetID,
       "arrayDiskLunID": arrayDiskLunID,
       "arrayDiskUsedSpaceInMB": arrayDiskUsedSpaceInMB,
       "arrayDiskUsedSpaceInBytes": arrayDiskUsedSpaceInBytes,
       "arrayDiskFreeSpaceInMB": arrayDiskFreeSpaceInMB,
       "arrayDiskFreeSpaceInBytes": arrayDiskFreeSpaceInBytes,
       "arrayDiskBusType": arrayDiskBusType,
       "arrayDiskSpareState": arrayDiskSpareState,
       "arrayDiskRollUpStatus": arrayDiskRollUpStatus,
       "arrayDiskComponentStatus": arrayDiskComponentStatus,
       "arrayDiskDeviceName": arrayDiskDeviceName,
       "arrayDiskNexusID": arrayDiskNexusID,
       "arrayDiskPartNumber": arrayDiskPartNumber,
       "arrayDiskSASAddress": arrayDiskSASAddress,
       "arrayDiskNegotiatedSpeed": arrayDiskNegotiatedSpeed,
       "arrayDiskCapableSpeed": arrayDiskCapableSpeed,
       "arrayDiskSmartAlertIndication": arrayDiskSmartAlertIndication,
       "arrayDiskManufactureDay": arrayDiskManufactureDay,
       "arrayDiskManufactureWeek": arrayDiskManufactureWeek,
       "arrayDiskManufactureYear": arrayDiskManufactureYear,
       "arrayDiskMediaType": arrayDiskMediaType,
       "arrayDiskDellCertified": arrayDiskDellCertified,
       "arrayDiskAltaVendorId": arrayDiskAltaVendorId,
       "arrayDiskAltaProductId": arrayDiskAltaProductId,
       "arrayDiskAltaRevisionId": arrayDiskAltaRevisionId,
       "arrayDiskEncryptionCapable": arrayDiskEncryptionCapable,
       "arrayDiskEncrypted": arrayDiskEncrypted,
       "arrayDiskPowerState": arrayDiskPowerState,
       "arrayDiskDriveWriteCache": arrayDiskDriveWriteCache,
       "arrayDiskModelNumber": arrayDiskModelNumber,
       "arrayDiskLifeRemaining": arrayDiskLifeRemaining,
       "arrayDiskDriverVersion": arrayDiskDriverVersion,
       "arrayDiskDeviceLifeStatus": arrayDiskDeviceLifeStatus,
       "arrayDiskReadOnly": arrayDiskReadOnly,
       "arrayDiskRemainingRatedWriteEndurance": arrayDiskRemainingRatedWriteEndurance,
       "arrayDiskSectorSize": arrayDiskSectorSize,
       "arrayDiskPICapable": arrayDiskPICapable,
       "arrayDiskMaxLinkWidth": arrayDiskMaxLinkWidth,
       "arrayDiskNegotiatedLinkWidth": arrayDiskNegotiatedLinkWidth,
       "arrayDiskEnclosureConnectionTable": arrayDiskEnclosureConnectionTable,
       "arrayDiskEnclosureConnectionEntry": arrayDiskEnclosureConnectionEntry,
       "arrayDiskEnclosureConnectionNumber": arrayDiskEnclosureConnectionNumber,
       "arrayDiskEnclosureConnectionArrayDiskName": arrayDiskEnclosureConnectionArrayDiskName,
       "arrayDiskEnclosureConnectionArrayDiskNumber": arrayDiskEnclosureConnectionArrayDiskNumber,
       "arrayDiskEnclosureConnectionEnclosureName": arrayDiskEnclosureConnectionEnclosureName,
       "arrayDiskEnclosureConnectionEnclosureNumber": arrayDiskEnclosureConnectionEnclosureNumber,
       "arrayDiskEnclosureConnectionControllerName": arrayDiskEnclosureConnectionControllerName,
       "arrayDiskEnclosureConnectionControllerNumber": arrayDiskEnclosureConnectionControllerNumber,
       "arrayDiskChannelConnectionTable": arrayDiskChannelConnectionTable,
       "arrayDiskChannelConnectionEntry": arrayDiskChannelConnectionEntry,
       "arrayDiskChannelConnectionNumber": arrayDiskChannelConnectionNumber,
       "arrayDiskChannelConnectionArrayDiskName": arrayDiskChannelConnectionArrayDiskName,
       "arrayDiskChannelConnectionArrayDiskNumber": arrayDiskChannelConnectionArrayDiskNumber,
       "arrayDiskChannelConnectionChannelName": arrayDiskChannelConnectionChannelName,
       "arrayDiskChannelConnectionChannelNumber": arrayDiskChannelConnectionChannelNumber,
       "arrayDiskChannelConnectionControllerName": arrayDiskChannelConnectionControllerName,
       "arrayDiskChannelConnectionControllerNumber": arrayDiskChannelConnectionControllerNumber,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanNumber": fanNumber,
       "fanName": fanName,
       "fanVendor": fanVendor,
       "fanState": fanState,
       "fanSeverity": fanSeverity,
       "fanProbeUnit": fanProbeUnit,
       "fanProbeMinWarning": fanProbeMinWarning,
       "fanProbeMinCritical": fanProbeMinCritical,
       "fanProbeMaxWarning": fanProbeMaxWarning,
       "fanProbeMaxCritical": fanProbeMaxCritical,
       "fanProbeCurrValue": fanProbeCurrValue,
       "fan1PartNumber": fan1PartNumber,
       "fan2PartNumber": fan2PartNumber,
       "fanRollUpStatus": fanRollUpStatus,
       "fanComponentStatus": fanComponentStatus,
       "fanNexusID": fanNexusID,
       "fanRevision": fanRevision,
       "fanConnectionTable": fanConnectionTable,
       "fanConnectionEntry": fanConnectionEntry,
       "fanConnectionNumber": fanConnectionNumber,
       "fanConnectionFanName": fanConnectionFanName,
       "fanConnectionFanNumber": fanConnectionFanNumber,
       "fanConnectionEnclosureName": fanConnectionEnclosureName,
       "fanConnectionEnclosureNumber": fanConnectionEnclosureNumber,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyNumber": powerSupplyNumber,
       "powerSupplyName": powerSupplyName,
       "powerSupplyVendor": powerSupplyVendor,
       "powerSupplyState": powerSupplyState,
       "powerSupplySeverity": powerSupplySeverity,
       "powerSupply1PartNumber": powerSupply1PartNumber,
       "powerSupply2PartNumber": powerSupply2PartNumber,
       "powerSupplyRollUpStatus": powerSupplyRollUpStatus,
       "powerSupplyComponentStatus": powerSupplyComponentStatus,
       "powerSupplyNexusID": powerSupplyNexusID,
       "powerSupplyRevision": powerSupplyRevision,
       "powerSupplyConnectionTable": powerSupplyConnectionTable,
       "powerSupplyConnectionEntry": powerSupplyConnectionEntry,
       "powerSupplyConnectionNumber": powerSupplyConnectionNumber,
       "powerSupplyConnectionPowersupplyName": powerSupplyConnectionPowersupplyName,
       "powerSupplyConnectionPowersupplyNumber": powerSupplyConnectionPowersupplyNumber,
       "powerSupplyConnectionEnclosureName": powerSupplyConnectionEnclosureName,
       "powerSupplyConnectionEnclosureNumber": powerSupplyConnectionEnclosureNumber,
       "powerSupplyConnectionFirmwareVersion": powerSupplyConnectionFirmwareVersion,
       "temperatureProbeTable": temperatureProbeTable,
       "temperatureProbeEntry": temperatureProbeEntry,
       "temperatureProbeNumber": temperatureProbeNumber,
       "temperatureProbeName": temperatureProbeName,
       "temperatureProbeVendor": temperatureProbeVendor,
       "temperatureProbeState": temperatureProbeState,
       "temperatureProbeSeverity": temperatureProbeSeverity,
       "temperatureProbeUnit": temperatureProbeUnit,
       "temperatureProbeMinWarning": temperatureProbeMinWarning,
       "temperatureProbeMinCritical": temperatureProbeMinCritical,
       "temperatureProbeMaxWarning": temperatureProbeMaxWarning,
       "temperatureProbeMaxCritical": temperatureProbeMaxCritical,
       "temperatureProbeCurValue": temperatureProbeCurValue,
       "temperatureProbeRollUpStatus": temperatureProbeRollUpStatus,
       "temperatureProbeComponentStatus": temperatureProbeComponentStatus,
       "temperatureProbeNexusID": temperatureProbeNexusID,
       "temperatureConnectionTable": temperatureConnectionTable,
       "temperatureConnectionEntry": temperatureConnectionEntry,
       "temperatureConnectionNumber": temperatureConnectionNumber,
       "temperatureConnectionTemperatureName": temperatureConnectionTemperatureName,
       "temperatureConnectionTemperatureNumber": temperatureConnectionTemperatureNumber,
       "temperatureConnectionEnclosureName": temperatureConnectionEnclosureName,
       "temperatureConnectionEnclosureNumber": temperatureConnectionEnclosureNumber,
       "enclosureManagementModuleTable": enclosureManagementModuleTable,
       "enclosureManagementModuleEntry": enclosureManagementModuleEntry,
       "enclosureManagementModuleNumber": enclosureManagementModuleNumber,
       "enclosureManagementModuleName": enclosureManagementModuleName,
       "enclosureManagementModuleVendor": enclosureManagementModuleVendor,
       "enclosureManagementModuleState": enclosureManagementModuleState,
       "enclosureManagementModuleSeverity": enclosureManagementModuleSeverity,
       "enclosureManagementModulePartNumber": enclosureManagementModulePartNumber,
       "enclosureManagementModuleType": enclosureManagementModuleType,
       "enclosureManagementModuleFWVersion": enclosureManagementModuleFWVersion,
       "enclosureManagementModuleMaxSpeed": enclosureManagementModuleMaxSpeed,
       "enclosureManagementModuleRollUpStatus": enclosureManagementModuleRollUpStatus,
       "enclosureManagementModuleComponentStatus": enclosureManagementModuleComponentStatus,
       "enclosureManagementModuleNexusID": enclosureManagementModuleNexusID,
       "enclosureManagementModuleRevision": enclosureManagementModuleRevision,
       "enclosureManagementModuleConnectionTable": enclosureManagementModuleConnectionTable,
       "enclosureManagementModuleConnectionEntry": enclosureManagementModuleConnectionEntry,
       "enclosureManagementModuleConnectionNumber": enclosureManagementModuleConnectionNumber,
       "enclosureManagementModuleConnectionEMMName": enclosureManagementModuleConnectionEMMName,
       "enclosureManagementModuleConnectionEMMNumber": enclosureManagementModuleConnectionEMMNumber,
       "enclosureManagementModuleConnectionEnclosureName": enclosureManagementModuleConnectionEnclosureName,
       "enclosureManagementModuleConnectionEnclosureNumber": enclosureManagementModuleConnectionEnclosureNumber,
       "batteryTable": batteryTable,
       "batteryEntry": batteryEntry,
       "batteryNumber": batteryNumber,
       "batteryName": batteryName,
       "batteryVendor": batteryVendor,
       "batteryState": batteryState,
       "batteryRollUpStatus": batteryRollUpStatus,
       "batteryComponentStatus": batteryComponentStatus,
       "batteryChargeCount": batteryChargeCount,
       "batteryMaxChargeCount": batteryMaxChargeCount,
       "batteryNexusID": batteryNexusID,
       "batteryPredictedCapacity": batteryPredictedCapacity,
       "batteryNextLearnTime": batteryNextLearnTime,
       "batteryLearnState": batteryLearnState,
       "batteryID": batteryID,
       "batteryMaxLearnDelay": batteryMaxLearnDelay,
       "batteryLearnMode": batteryLearnMode,
       "batteryConnectionTable": batteryConnectionTable,
       "batteryConnectionEntry": batteryConnectionEntry,
       "batteryConnectionNumber": batteryConnectionNumber,
       "batteryConnectionBatteryName": batteryConnectionBatteryName,
       "batteryConnectionBatteryNumber": batteryConnectionBatteryNumber,
       "batteryConnectionControllerName": batteryConnectionControllerName,
       "batteryConnectionControllerNumber": batteryConnectionControllerNumber,
       "tapeDriveTable": tapeDriveTable,
       "tapeDriveEntry": tapeDriveEntry,
       "tapeDriveNumber": tapeDriveNumber,
       "tapeDriveName": tapeDriveName,
       "tapeDriveVendor": tapeDriveVendor,
       "tapeDriveProductID": tapeDriveProductID,
       "tapeDriveNexusID": tapeDriveNexusID,
       "tapeDriveBusType": tapeDriveBusType,
       "tapeDriveSASAddress": tapeDriveSASAddress,
       "tapeDriveMediaType": tapeDriveMediaType,
       "logicalDevices": logicalDevices,
       "virtualDiskTable": virtualDiskTable,
       "virtualDiskEntry": virtualDiskEntry,
       "virtualDiskNumber": virtualDiskNumber,
       "virtualDiskName": virtualDiskName,
       "virtualDiskDeviceName": virtualDiskDeviceName,
       "virtualDiskState": virtualDiskState,
       "virtualDiskSeverity": virtualDiskSeverity,
       "virtualDiskLengthInMB": virtualDiskLengthInMB,
       "virtualDiskLengthInBytes": virtualDiskLengthInBytes,
       "virtualDiskFreeSpaceInMB": virtualDiskFreeSpaceInMB,
       "virtualDiskFreeSpaceInBytes": virtualDiskFreeSpaceInBytes,
       "virtualDiskWritePolicy": virtualDiskWritePolicy,
       "virtualDiskReadPolicy": virtualDiskReadPolicy,
       "virtualDiskCachePolicy": virtualDiskCachePolicy,
       "virtualDiskLayout": virtualDiskLayout,
       "virtualDiskCurStripeSizeInMB": virtualDiskCurStripeSizeInMB,
       "virtualDiskCurStripeSizeInBytes": virtualDiskCurStripeSizeInBytes,
       "virtualDiskChannel": virtualDiskChannel,
       "virtualDiskTargetID": virtualDiskTargetID,
       "virtualDiskLunID": virtualDiskLunID,
       "virtualDiskRollUpStatus": virtualDiskRollUpStatus,
       "virtualDiskComponentStatus": virtualDiskComponentStatus,
       "virtualDiskNexusID": virtualDiskNexusID,
       "virtualDiskArrayDiskType": virtualDiskArrayDiskType,
       "virtualDiskBadBlocksDetected": virtualDiskBadBlocksDetected,
       "virtualDiskEncrypted": virtualDiskEncrypted,
       "virtualDiskIsCacheCade": virtualDiskIsCacheCade,
       "virtualDiskDiskCachePolicy": virtualDiskDiskCachePolicy,
       "virtualDiskAssociatedFluidCacheStatus": virtualDiskAssociatedFluidCacheStatus,
       "virtualDiskPIEnable": virtualDiskPIEnable,
       "virtualDiskPartitionTable": virtualDiskPartitionTable,
       "virtualDiskPartitionEntry": virtualDiskPartitionEntry,
       "virtualDiskPartitionNumber": virtualDiskPartitionNumber,
       "virtualDiskPartitionDeviceName": virtualDiskPartitionDeviceName,
       "virtualDiskPartitionState": virtualDiskPartitionState,
       "virtualDiskPartitionSize": virtualDiskPartitionSize,
       "virtualDiskPartitionFluidCacheStatus": virtualDiskPartitionFluidCacheStatus,
       "virtualDiskPartitionNexusID": virtualDiskPartitionNexusID,
       "arrayDiskLogicalConnectionTable": arrayDiskLogicalConnectionTable,
       "arrayDiskLogicalConnectionEntry": arrayDiskLogicalConnectionEntry,
       "arrayDiskLogicalConnectionNumber": arrayDiskLogicalConnectionNumber,
       "arrayDiskLogicalConnectionArrayDiskName": arrayDiskLogicalConnectionArrayDiskName,
       "arrayDiskLogicalConnectionArrayDiskNumber": arrayDiskLogicalConnectionArrayDiskNumber,
       "arrayDiskLogicalConnectionVirtualDiskName": arrayDiskLogicalConnectionVirtualDiskName,
       "arrayDiskLogicalConnectionVirtualDiskNumber": arrayDiskLogicalConnectionVirtualDiskNumber,
       "arrayDiskLogicalConnectionDiskName": arrayDiskLogicalConnectionDiskName,
       "arrayDiskLogicalConnectionDiskNumber": arrayDiskLogicalConnectionDiskNumber,
       "fluidCacheTable": fluidCacheTable,
       "fluidCacheEntry": fluidCacheEntry,
       "fluidCacheNumber": fluidCacheNumber,
       "fluidCacheName": fluidCacheName,
       "fluidCacheLicenseState": fluidCacheLicenseState,
       "fluidCacheLicenseValidity": fluidCacheLicenseValidity,
       "fluidCacheLicenseEntitlementID": fluidCacheLicenseEntitlementID,
       "fluidCacheLicenseDuration": fluidCacheLicenseDuration,
       "fluidCacheLicenseCapacity": fluidCacheLicenseCapacity,
       "fluidCacheLicenseRemaining": fluidCacheLicenseRemaining,
       "fluidCacheLicenseType": fluidCacheLicenseType,
       "fluidCacheLicenseVendor": fluidCacheLicenseVendor,
       "fluidCacheLicenseProductId": fluidCacheLicenseProductId,
       "fluidCacheLicenseDateSold": fluidCacheLicenseDateSold,
       "fluidCacheLicenseGeneration": fluidCacheLicenseGeneration,
       "fluidCacheLicenseFeatureID": fluidCacheLicenseFeatureID,
       "fluidCacheLicenseFeatureDescription": fluidCacheLicenseFeatureDescription,
       "fluidCacheNexus": fluidCacheNexus,
       "fluidCacheDiskTable": fluidCacheDiskTable,
       "fluidCacheDiskEntry": fluidCacheDiskEntry,
       "fluidCacheDiskNumber": fluidCacheDiskNumber,
       "fluidCacheDiskName": fluidCacheDiskName,
       "fluidCacheDiskState": fluidCacheDiskState,
       "fluidCacheDiskBackendDeviceType": fluidCacheDiskBackendDeviceType,
       "fluidCacheDiskBackendDeviceName": fluidCacheDiskBackendDeviceName,
       "fluidCacheDiskBackendDeviceSize": fluidCacheDiskBackendDeviceSize,
       "fluidCacheDiskOperatingMode": fluidCacheDiskOperatingMode,
       "fluidCacheDiskConfiguredMode": fluidCacheDiskConfiguredMode,
       "fluidCacheDiskNexus": fluidCacheDiskNexus,
       "fluidCacheDiskStatus": fluidCacheDiskStatus,
       "fluidCachePoolTable": fluidCachePoolTable,
       "fluidCachePoolEntry": fluidCachePoolEntry,
       "fluidCachePoolNumber": fluidCachePoolNumber,
       "fluidCachePoolStoreCount": fluidCachePoolStoreCount,
       "fluidCachePoolUUID": fluidCachePoolUUID,
       "fluidCachePoolLicenseState": fluidCachePoolLicenseState,
       "fluidCachePoolSize": fluidCachePoolSize,
       "fluidCachePoolHighAvailabilityState": fluidCachePoolHighAvailabilityState,
       "fluidCachePoolNexus": fluidCachePoolNexus,
       "fluidCachePoolStatus": fluidCachePoolStatus,
       "storageManagementEvent": storageManagementEvent,
       "alertStorageManagementInformation": alertStorageManagementInformation,
       "alertStorageManagementNormal": alertStorageManagementNormal,
       "alertStorageManagementWarning": alertStorageManagementWarning,
       "alertStorageManagementFailure": alertStorageManagementFailure,
       "alertStorageManagementNonRecoverable": alertStorageManagementNonRecoverable,
       "alertControllerInformation": alertControllerInformation,
       "alertControllerNormal": alertControllerNormal,
       "alertControllerWarning": alertControllerWarning,
       "alertControllerFailure": alertControllerFailure,
       "alertControllerNonRecoverable": alertControllerNonRecoverable,
       "alertChannelInformation": alertChannelInformation,
       "alertChannelNormal": alertChannelNormal,
       "alertChannelWarning": alertChannelWarning,
       "alertChannelFailure": alertChannelFailure,
       "alertChannelNonRecoverable": alertChannelNonRecoverable,
       "alertEnclosureInformation": alertEnclosureInformation,
       "alertEnclosureNormal": alertEnclosureNormal,
       "alertEnclosureWarning": alertEnclosureWarning,
       "alertEnclosureFailure": alertEnclosureFailure,
       "alertEnclosureNonRecoverable": alertEnclosureNonRecoverable,
       "alertArrayDiskInformation": alertArrayDiskInformation,
       "alertArrayDiskNormal": alertArrayDiskNormal,
       "alertArrayDiskWarning": alertArrayDiskWarning,
       "alertArrayDiskFailure": alertArrayDiskFailure,
       "alertArrayDiskNonRecoverable": alertArrayDiskNonRecoverable,
       "alertEMMInformation": alertEMMInformation,
       "alertEMMNormal": alertEMMNormal,
       "alertEMMWarning": alertEMMWarning,
       "alertEMMFailure": alertEMMFailure,
       "alertEMMNonRecoverable": alertEMMNonRecoverable,
       "alertPowerSupplyInformation": alertPowerSupplyInformation,
       "alertPowerSupplyNormal": alertPowerSupplyNormal,
       "alertPowerSupplyWarning": alertPowerSupplyWarning,
       "alertPowerSupplyFailure": alertPowerSupplyFailure,
       "alertPowerSupplyNonRecoverable": alertPowerSupplyNonRecoverable,
       "alertTemperatureProbeInformation": alertTemperatureProbeInformation,
       "alertTemperatureProbeNormal": alertTemperatureProbeNormal,
       "alertTemperatureProbeWarning": alertTemperatureProbeWarning,
       "alertTemperatureProbeFailure": alertTemperatureProbeFailure,
       "alertTemperatureProbeNonRecoverable": alertTemperatureProbeNonRecoverable,
       "alertFanInformation": alertFanInformation,
       "alertFanNormal": alertFanNormal,
       "alertFanWarning": alertFanWarning,
       "alertFanFailure": alertFanFailure,
       "alertFanNonRecoverable": alertFanNonRecoverable,
       "alertBatteryInformation": alertBatteryInformation,
       "alertBatteryNormal": alertBatteryNormal,
       "alertBatteryWarning": alertBatteryWarning,
       "alertBatteryFailure": alertBatteryFailure,
       "alertBatteryNonRecoverable": alertBatteryNonRecoverable,
       "alertVirtualDiskInformation": alertVirtualDiskInformation,
       "alertVirtualDiskNormal": alertVirtualDiskNormal,
       "alertVirtualDiskWarning": alertVirtualDiskWarning,
       "alertVirtualDiskFailure": alertVirtualDiskFailure,
       "alertVirtualDiskNonRecoverable": alertVirtualDiskNonRecoverable,
       "alertRedundancyNormal": alertRedundancyNormal,
       "alertRedundancyDegraded": alertRedundancyDegraded,
       "alertRedundancyLost": alertRedundancyLost,
       "alertFluidCacheDiskInformation": alertFluidCacheDiskInformation,
       "alertfluidCacheDiskWarning": alertfluidCacheDiskWarning,
       "alertFluidCacheDisklFailure": alertFluidCacheDisklFailure,
       "alertVirtualDiskPartitionInformation": alertVirtualDiskPartitionInformation,
       "alertVirtualDiskPartitionWarning": alertVirtualDiskPartitionWarning,
       "alertVirtualDiskPartitionFailure": alertVirtualDiskPartitionFailure,
       "alertFluidCacheInformation": alertFluidCacheInformation,
       "alertfluidCacheWarning": alertfluidCacheWarning,
       "alertFluidCacheFailure": alertFluidCacheFailure,
       "alertFluidCachePoolInformation": alertFluidCachePoolInformation,
       "alertfluidCachePoolWarning": alertfluidCachePoolWarning,
       "alertFluidCachePoolFailure": alertFluidCachePoolFailure,
       "alertEEMIStorageManagementInformation": alertEEMIStorageManagementInformation,
       "alertEEMIStorageManagementNormal": alertEEMIStorageManagementNormal,
       "alertEEMIStorageManagementWarning": alertEEMIStorageManagementWarning,
       "alertEEMIStorageManagementFailure": alertEEMIStorageManagementFailure,
       "alertEEMIStorageManagementNonRecoverable": alertEEMIStorageManagementNonRecoverable,
       "alertEEMIControllerInformation": alertEEMIControllerInformation,
       "alertEEMIControllerNormal": alertEEMIControllerNormal,
       "alertEEMIControllerWarning": alertEEMIControllerWarning,
       "alertEEMIControllerFailure": alertEEMIControllerFailure,
       "alertEEMIControllerNonRecoverable": alertEEMIControllerNonRecoverable,
       "alertEEMIChannelInformation": alertEEMIChannelInformation,
       "alertEEMIChannelNormal": alertEEMIChannelNormal,
       "alertEEMIChannelWarning": alertEEMIChannelWarning,
       "alertEEMIChannelFailure": alertEEMIChannelFailure,
       "alertEEMIChannelNonRecoverable": alertEEMIChannelNonRecoverable,
       "alertEEMIEnclosureInformation": alertEEMIEnclosureInformation,
       "alertEEMIEnclosureNormal": alertEEMIEnclosureNormal,
       "alertEEMIEnclosureWarning": alertEEMIEnclosureWarning,
       "alertEEMIEnclosureFailure": alertEEMIEnclosureFailure,
       "alertEEMIEnclosureNonRecoverable": alertEEMIEnclosureNonRecoverable,
       "alertEEMIArrayDiskInformation": alertEEMIArrayDiskInformation,
       "alertEEMIArrayDiskNormal": alertEEMIArrayDiskNormal,
       "alertEEMIArrayDiskWarning": alertEEMIArrayDiskWarning,
       "alertEEMIArrayDiskFailure": alertEEMIArrayDiskFailure,
       "alertEEMIArrayDiskNonRecoverable": alertEEMIArrayDiskNonRecoverable,
       "alertEMMEMMInformation": alertEMMEMMInformation,
       "alertEEMIEMMNormal": alertEEMIEMMNormal,
       "alertEEMIEMMWarning": alertEEMIEMMWarning,
       "alertEEMIEMMFailure": alertEEMIEMMFailure,
       "alertEEMIEMMNonRecoverable": alertEEMIEMMNonRecoverable,
       "alertEEMIPowerSupplyInformation": alertEEMIPowerSupplyInformation,
       "alertEEMIPowerSupplyNormal": alertEEMIPowerSupplyNormal,
       "alertEEMIPowerSupplyWarning": alertEEMIPowerSupplyWarning,
       "alertEEMIPowerSupplyFailure": alertEEMIPowerSupplyFailure,
       "alertEEMIPowerSupplyNonRecoverable": alertEEMIPowerSupplyNonRecoverable,
       "alertEEMITemperatureProbeInformation": alertEEMITemperatureProbeInformation,
       "alertEEMITemperatureProbeNormal": alertEEMITemperatureProbeNormal,
       "alertEEMITemperatureProbeWarning": alertEEMITemperatureProbeWarning,
       "alertEEMITemperatureProbeFailure": alertEEMITemperatureProbeFailure,
       "alertEEMITemperatureProbeNonRecoverable": alertEEMITemperatureProbeNonRecoverable,
       "alertEEMIFanInformation": alertEEMIFanInformation,
       "alertEEMIFanNormal": alertEEMIFanNormal,
       "alertEEMIFanWarning": alertEEMIFanWarning,
       "alertEEMIFanFailure": alertEEMIFanFailure,
       "alertEEMIFanNonRecoverable": alertEEMIFanNonRecoverable,
       "alertEEMIBatteryInformation": alertEEMIBatteryInformation,
       "alertEEMIBatteryNormal": alertEEMIBatteryNormal,
       "alertEEMIBatteryWarning": alertEEMIBatteryWarning,
       "alertEEMIBatteryFailure": alertEEMIBatteryFailure,
       "alertEEMIBatteryNonRecoverable": alertEEMIBatteryNonRecoverable,
       "alertEEMIVirtualDiskInformation": alertEEMIVirtualDiskInformation,
       "alertEEMIVirtualDiskNormal": alertEEMIVirtualDiskNormal,
       "alertEEMIVirtualDiskWarning": alertEEMIVirtualDiskWarning,
       "alertEEMIVirtualDiskFailure": alertEEMIVirtualDiskFailure,
       "alertEEMIVirtualDiskNonRecoverable": alertEEMIVirtualDiskNonRecoverable,
       "alertEEMIRedundancyNormal": alertEEMIRedundancyNormal,
       "alertEEMIRedundancyDegraded": alertEEMIRedundancyDegraded,
       "alertEEMIRedundancyLost": alertEEMIRedundancyLost,
       "alertEEMIFluidCacheDiskInformation": alertEEMIFluidCacheDiskInformation,
       "alertEEMIfluidCacheDiskWarning": alertEEMIfluidCacheDiskWarning,
       "alertEEMIFluidCacheDisklFailure": alertEEMIFluidCacheDisklFailure,
       "alertEEMIVirtualDiskPartitionInformation": alertEEMIVirtualDiskPartitionInformation,
       "alertEEMIVirtualDiskPartitionWarning": alertEEMIVirtualDiskPartitionWarning,
       "alertEEMIVirtualDiskPartitionFailure": alertEEMIVirtualDiskPartitionFailure,
       "alertEEMIFluidCacheInformation": alertEEMIFluidCacheInformation,
       "alertEEMIfluidCacheWarning": alertEEMIfluidCacheWarning,
       "alertEEMIFluidCacheFailure": alertEEMIFluidCacheFailure,
       "alertEEMIFluidCachePoolInformation": alertEEMIFluidCachePoolInformation,
       "alertEEMIfluidCachePoolWarning": alertEEMIfluidCachePoolWarning,
       "alertEEMIFluidCachePoolFailure": alertEEMIFluidCachePoolFailure,
       "messageIDEvent": messageIDEvent,
       "descriptionEvent": descriptionEvent,
       "locationEvent": locationEvent,
       "objectNameEvent": objectNameEvent,
       "objectOIDEvent": objectOIDEvent,
       "objectNexusEvent": objectNexusEvent,
       "currentStatusEvent": currentStatusEvent,
       "previousStatusEvent": previousStatusEvent,
       "enhancedMessageIDEvent": enhancedMessageIDEvent,
       "systemFQDNEvent": systemFQDNEvent,
       "serviceTagEvent": serviceTagEvent,
       "chassisServiceTagEvent": chassisServiceTagEvent}
)
