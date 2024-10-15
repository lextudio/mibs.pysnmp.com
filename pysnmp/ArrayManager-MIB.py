# SNMP MIB module (ArrayManager-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ArrayManager-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:08 2024
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
_ArrayManager_ObjectIdentity = ObjectIdentity
arrayManager = _ArrayManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1)
)


class _ArrayMgrSoftwareVersion_Type(DisplayString):
    """Custom type arrayMgrSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArrayMgrSoftwareVersion_Type.__name__ = "DisplayString"
_ArrayMgrSoftwareVersion_Object = MibScalar
arrayMgrSoftwareVersion = _ArrayMgrSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 1),
    _ArrayMgrSoftwareVersion_Type()
)
arrayMgrSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrSoftwareVersion.setStatus("mandatory")


class _ArrayMgrGlobalStatus_Type(Integer32):
    """Custom type arrayMgrGlobalStatus based on Integer32"""
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


_ArrayMgrGlobalStatus_Type.__name__ = "Integer32"
_ArrayMgrGlobalStatus_Object = MibScalar
arrayMgrGlobalStatus = _ArrayMgrGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 2),
    _ArrayMgrGlobalStatus_Type()
)
arrayMgrGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrGlobalStatus.setStatus("mandatory")


class _ArrayMgrSoftwareManufacturer_Type(DisplayString):
    """Custom type arrayMgrSoftwareManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArrayMgrSoftwareManufacturer_Type.__name__ = "DisplayString"
_ArrayMgrSoftwareManufacturer_Object = MibScalar
arrayMgrSoftwareManufacturer = _ArrayMgrSoftwareManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 3),
    _ArrayMgrSoftwareManufacturer_Type()
)
arrayMgrSoftwareManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrSoftwareManufacturer.setStatus("mandatory")


class _ArrayMgrSoftwareProduct_Type(DisplayString):
    """Custom type arrayMgrSoftwareProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ArrayMgrSoftwareProduct_Type.__name__ = "DisplayString"
_ArrayMgrSoftwareProduct_Object = MibScalar
arrayMgrSoftwareProduct = _ArrayMgrSoftwareProduct_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 4),
    _ArrayMgrSoftwareProduct_Type()
)
arrayMgrSoftwareProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrSoftwareProduct.setStatus("mandatory")


class _ArrayMgrSoftwareDescription_Type(DisplayString):
    """Custom type arrayMgrSoftwareDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ArrayMgrSoftwareDescription_Type.__name__ = "DisplayString"
_ArrayMgrSoftwareDescription_Object = MibScalar
arrayMgrSoftwareDescription = _ArrayMgrSoftwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 5),
    _ArrayMgrSoftwareDescription_Type()
)
arrayMgrSoftwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrSoftwareDescription.setStatus("mandatory")
_ArrayMgrInfo_ObjectIdentity = ObjectIdentity
arrayMgrInfo = _ArrayMgrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 100)
)
_ArrayMgrDisplayName_Type = DisplayString
_ArrayMgrDisplayName_Object = MibScalar
arrayMgrDisplayName = _ArrayMgrDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 100, 1),
    _ArrayMgrDisplayName_Type()
)
arrayMgrDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrDisplayName.setStatus("mandatory")
_ArrayMgrDescription_Type = DisplayString
_ArrayMgrDescription_Object = MibScalar
arrayMgrDescription = _ArrayMgrDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 100, 2),
    _ArrayMgrDescription_Type()
)
arrayMgrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrDescription.setStatus("mandatory")
_ArrayMgrAgentVendor_Type = DisplayString
_ArrayMgrAgentVendor_Object = MibScalar
arrayMgrAgentVendor = _ArrayMgrAgentVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 100, 3),
    _ArrayMgrAgentVendor_Type()
)
arrayMgrAgentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrAgentVendor.setStatus("mandatory")
_ArrayMgrAgentVersion_Type = DisplayString
_ArrayMgrAgentVersion_Object = MibScalar
arrayMgrAgentVersion = _ArrayMgrAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 100, 4),
    _ArrayMgrAgentVersion_Type()
)
arrayMgrAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMgrAgentVersion.setStatus("mandatory")
_GlobalData_ObjectIdentity = ObjectIdentity
globalData = _GlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110)
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 1),
    _AgentSystemGlobalStatus_Type()
)
agentSystemGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSystemGlobalStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 2),
    _AgentLastGlobalStatus_Type()
)
agentLastGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLastGlobalStatus.setStatus("mandatory")
_AgentTimeStamp_Type = Integer32
_AgentTimeStamp_Object = MibScalar
agentTimeStamp = _AgentTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 5),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 6),
    _AgentRefreshRate_Type()
)
agentRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRefreshRate.setStatus("mandatory")
_AgentHostname_Type = DisplayString
_AgentHostname_Object = MibScalar
agentHostname = _AgentHostname_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 7),
    _AgentHostname_Type()
)
agentHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentHostname.setStatus("mandatory")
_AgentIPAddress_Type = DisplayString
_AgentIPAddress_Object = MibScalar
agentIPAddress = _AgentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 8),
    _AgentIPAddress_Type()
)
agentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIPAddress.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 9),
    _AgentSoftwareStatus_Type()
)
agentSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSoftwareStatus.setStatus("mandatory")
_AgentAmSnmpVersion_Type = DisplayString
_AgentAmSnmpVersion_Object = MibScalar
agentAmSnmpVersion = _AgentAmSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 10),
    _AgentAmSnmpVersion_Type()
)
agentAmSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAmSnmpVersion.setStatus("mandatory")
_AgentAmMibVersion_Type = DisplayString
_AgentAmMibVersion_Object = MibScalar
agentAmMibVersion = _AgentAmMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 110, 11),
    _AgentAmMibVersion_Type()
)
agentAmMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAmMibVersion.setStatus("mandatory")
_ProviderData_ObjectIdentity = ObjectIdentity
providerData = _ProviderData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 120)
)
_ProviderTable_Object = MibTable
providerTable = _ProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 120, 1)
)
if mibBuilder.loadTexts:
    providerTable.setStatus("mandatory")
_ProviderEntry_Object = MibTableRow
providerEntry = _ProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 120, 1, 1)
)
providerEntry.setIndexNames(
    (0, "ArrayManager-MIB", "providerNumber"),
)
if mibBuilder.loadTexts:
    providerEntry.setStatus("mandatory")


class _ProviderNumber_Type(Integer32):
    """Custom type providerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ProviderNumber_Type.__name__ = "Integer32"
_ProviderNumber_Object = MibTableColumn
providerNumber = _ProviderNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 120, 1, 1, 1),
    _ProviderNumber_Type()
)
providerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    providerNumber.setStatus("mandatory")
_ProviderName_Type = DisplayString
_ProviderName_Object = MibTableColumn
providerName = _ProviderName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 120, 1, 1, 2),
    _ProviderName_Type()
)
providerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    providerName.setStatus("mandatory")


class _ProviderStatus_Type(Integer32):
    """Custom type providerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("loaded", 1),
          ("unknown", 3))
    )


_ProviderStatus_Type.__name__ = "Integer32"
_ProviderStatus_Object = MibTableColumn
providerStatus = _ProviderStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 120, 1, 1, 3),
    _ProviderStatus_Type()
)
providerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    providerStatus.setStatus("mandatory")
_ProviderVersion_Type = DisplayString
_ProviderVersion_Object = MibTableColumn
providerVersion = _ProviderVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 120, 1, 1, 4),
    _ProviderVersion_Type()
)
providerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    providerVersion.setStatus("mandatory")
_PhysicalDevices_ObjectIdentity = ObjectIdentity
physicalDevices = _PhysicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130)
)
_ControllerTable_Object = MibTable
controllerTable = _ControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1)
)
if mibBuilder.loadTexts:
    controllerTable.setStatus("mandatory")
_ControllerEntry_Object = MibTableRow
controllerEntry = _ControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1)
)
controllerEntry.setIndexNames(
    (0, "ArrayManager-MIB", "controllerNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 1),
    _ControllerNumber_Type()
)
controllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNumber.setStatus("mandatory")
_ControllerName_Type = DisplayString
_ControllerName_Object = MibTableColumn
controllerName = _ControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 2),
    _ControllerName_Type()
)
controllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerName.setStatus("mandatory")
_ControllerVendor_Type = DisplayString
_ControllerVendor_Object = MibTableColumn
controllerVendor = _ControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 3),
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("ide", 4),
          ("pv660F", 2),
          ("pv662F", 3),
          ("scsi", 1))
    )


_ControllerType_Type.__name__ = "Integer32"
_ControllerType_Object = MibTableColumn
controllerType = _ControllerType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 6),
    _ControllerSeverity_Type()
)
controllerSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSeverity.setStatus("mandatory")


class _ControllerRebuildRateInPercent_Type(Integer32):
    """Custom type controllerRebuildRateInPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerRebuildRateInPercent_Type.__name__ = "Integer32"
_ControllerRebuildRateInPercent_Object = MibTableColumn
controllerRebuildRateInPercent = _ControllerRebuildRateInPercent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 7),
    _ControllerRebuildRateInPercent_Type()
)
controllerRebuildRateInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRebuildRateInPercent.setStatus("mandatory")
_ControllerFWVersion_Type = DisplayString
_ControllerFWVersion_Object = MibTableColumn
controllerFWVersion = _ControllerFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 8),
    _ControllerFWVersion_Type()
)
controllerFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerFWVersion.setStatus("mandatory")
_ControllerCacheSizeInMB_Type = Integer32
_ControllerCacheSizeInMB_Object = MibTableColumn
controllerCacheSizeInMB = _ControllerCacheSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 9),
    _ControllerCacheSizeInMB_Type()
)
controllerCacheSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCacheSizeInMB.setStatus("mandatory")
_ControllerCacheSizeInBytes_Type = Integer32
_ControllerCacheSizeInBytes_Object = MibTableColumn
controllerCacheSizeInBytes = _ControllerCacheSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 10),
    _ControllerCacheSizeInBytes_Type()
)
controllerCacheSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCacheSizeInBytes.setStatus("mandatory")
_ControllerPhysicalDeviceCount_Type = Integer32
_ControllerPhysicalDeviceCount_Object = MibTableColumn
controllerPhysicalDeviceCount = _ControllerPhysicalDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 11),
    _ControllerPhysicalDeviceCount_Type()
)
controllerPhysicalDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPhysicalDeviceCount.setStatus("mandatory")
_ControllerLogicalDeviceCount_Type = Integer32
_ControllerLogicalDeviceCount_Object = MibTableColumn
controllerLogicalDeviceCount = _ControllerLogicalDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 12),
    _ControllerLogicalDeviceCount_Type()
)
controllerLogicalDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerLogicalDeviceCount.setStatus("mandatory")
_ControllerPartnerStatus_Type = DisplayString
_ControllerPartnerStatus_Object = MibTableColumn
controllerPartnerStatus = _ControllerPartnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 13),
    _ControllerPartnerStatus_Type()
)
controllerPartnerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPartnerStatus.setStatus("mandatory")
_ControllerHostPortCount_Type = Integer32
_ControllerHostPortCount_Object = MibTableColumn
controllerHostPortCount = _ControllerHostPortCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 14),
    _ControllerHostPortCount_Type()
)
controllerHostPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerHostPortCount.setStatus("mandatory")
_ControllerMemorySizeInMB_Type = Integer32
_ControllerMemorySizeInMB_Object = MibTableColumn
controllerMemorySizeInMB = _ControllerMemorySizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 15),
    _ControllerMemorySizeInMB_Type()
)
controllerMemorySizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerMemorySizeInMB.setStatus("mandatory")
_ControllerMemorySizeInBytes_Type = Integer32
_ControllerMemorySizeInBytes_Object = MibTableColumn
controllerMemorySizeInBytes = _ControllerMemorySizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 17),
    _ControllerDriveChannelCount_Type()
)
controllerDriveChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerDriveChannelCount.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 18),
    _ControllerFaultTolerant_Type()
)
controllerFaultTolerant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerFaultTolerant.setStatus("mandatory")
_ControllerC0Port0WWN_Type = DisplayString
_ControllerC0Port0WWN_Object = MibTableColumn
controllerC0Port0WWN = _ControllerC0Port0WWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 19),
    _ControllerC0Port0WWN_Type()
)
controllerC0Port0WWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Port0WWN.setStatus("mandatory")
_ControllerC0Port0Name_Type = DisplayString
_ControllerC0Port0Name_Object = MibTableColumn
controllerC0Port0Name = _ControllerC0Port0Name_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 20),
    _ControllerC0Port0Name_Type()
)
controllerC0Port0Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Port0Name.setStatus("mandatory")
_ControllerC0Port0ID_Type = Integer32
_ControllerC0Port0ID_Object = MibTableColumn
controllerC0Port0ID = _ControllerC0Port0ID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 21),
    _ControllerC0Port0ID_Type()
)
controllerC0Port0ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Port0ID.setStatus("mandatory")
_ControllerC0Target_Type = Integer32
_ControllerC0Target_Object = MibTableColumn
controllerC0Target = _ControllerC0Target_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 22),
    _ControllerC0Target_Type()
)
controllerC0Target.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Target.setStatus("mandatory")
_ControllerC0Channel_Type = Integer32
_ControllerC0Channel_Object = MibTableColumn
controllerC0Channel = _ControllerC0Channel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 23),
    _ControllerC0Channel_Type()
)
controllerC0Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Channel.setStatus("mandatory")
_ControllerC0OSController_Type = DisplayString
_ControllerC0OSController_Object = MibTableColumn
controllerC0OSController = _ControllerC0OSController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 24),
    _ControllerC0OSController_Type()
)
controllerC0OSController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0OSController.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 25),
    _ControllerC0BatteryState_Type()
)
controllerC0BatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0BatteryState.setStatus("mandatory")
_ControllerC1Port0WWN_Type = DisplayString
_ControllerC1Port0WWN_Object = MibTableColumn
controllerC1Port0WWN = _ControllerC1Port0WWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 26),
    _ControllerC1Port0WWN_Type()
)
controllerC1Port0WWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Port0WWN.setStatus("mandatory")
_ControllerC1Port0Name_Type = DisplayString
_ControllerC1Port0Name_Object = MibTableColumn
controllerC1Port0Name = _ControllerC1Port0Name_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 27),
    _ControllerC1Port0Name_Type()
)
controllerC1Port0Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Port0Name.setStatus("mandatory")
_ControllerC1Port0ID_Type = Integer32
_ControllerC1Port0ID_Object = MibTableColumn
controllerC1Port0ID = _ControllerC1Port0ID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 28),
    _ControllerC1Port0ID_Type()
)
controllerC1Port0ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Port0ID.setStatus("mandatory")
_ControllerC1Target_Type = Integer32
_ControllerC1Target_Object = MibTableColumn
controllerC1Target = _ControllerC1Target_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 29),
    _ControllerC1Target_Type()
)
controllerC1Target.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Target.setStatus("mandatory")
_ControllerC1Channel_Type = Integer32
_ControllerC1Channel_Object = MibTableColumn
controllerC1Channel = _ControllerC1Channel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 30),
    _ControllerC1Channel_Type()
)
controllerC1Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Channel.setStatus("mandatory")
_ControllerC1OSController_Type = Integer32
_ControllerC1OSController_Object = MibTableColumn
controllerC1OSController = _ControllerC1OSController_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 31),
    _ControllerC1OSController_Type()
)
controllerC1OSController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1OSController.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 32),
    _ControllerC1BatteryState_Type()
)
controllerC1BatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1BatteryState.setStatus("mandatory")
_ControllerNodeWWN_Type = DisplayString
_ControllerNodeWWN_Object = MibTableColumn
controllerNodeWWN = _ControllerNodeWWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 33),
    _ControllerNodeWWN_Type()
)
controllerNodeWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNodeWWN.setStatus("mandatory")
_ControllerC0Port1WWN_Type = DisplayString
_ControllerC0Port1WWN_Object = MibTableColumn
controllerC0Port1WWN = _ControllerC0Port1WWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 34),
    _ControllerC0Port1WWN_Type()
)
controllerC0Port1WWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC0Port1WWN.setStatus("mandatory")
_ControllerC1Port1WWN_Type = DisplayString
_ControllerC1Port1WWN_Object = MibTableColumn
controllerC1Port1WWN = _ControllerC1Port1WWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 35),
    _ControllerC1Port1WWN_Type()
)
controllerC1Port1WWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerC1Port1WWN.setStatus("mandatory")
_ControllerBatteryChargeCount_Type = Integer32
_ControllerBatteryChargeCount_Object = MibTableColumn
controllerBatteryChargeCount = _ControllerBatteryChargeCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 1, 1, 36),
    _ControllerBatteryChargeCount_Type()
)
controllerBatteryChargeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBatteryChargeCount.setStatus("mandatory")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 2)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("mandatory")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 2, 1)
)
channelEntry.setIndexNames(
    (0, "ArrayManager-MIB", "channelNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 2, 1, 1),
    _ChannelNumber_Type()
)
channelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumber.setStatus("mandatory")
_ChannelName_Type = DisplayString
_ChannelName_Object = MibTableColumn
channelName = _ChannelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 2, 1, 4),
    _ChannelSeverity_Type()
)
channelSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelSeverity.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 2, 1, 5),
    _ChannelTermination_Type()
)
channelTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelTermination.setStatus("mandatory")
_ChannelSCSIID_Type = Integer32
_ChannelSCSIID_Object = MibTableColumn
channelSCSIID = _ChannelSCSIID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 2, 1, 6),
    _ChannelSCSIID_Type()
)
channelSCSIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelSCSIID.setStatus("mandatory")
_EnclosureTable_Object = MibTable
enclosureTable = _EnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3)
)
if mibBuilder.loadTexts:
    enclosureTable.setStatus("mandatory")
_EnclosureEntry_Object = MibTableRow
enclosureEntry = _EnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1)
)
enclosureEntry.setIndexNames(
    (0, "ArrayManager-MIB", "enclosureNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 1),
    _EnclosureNumber_Type()
)
enclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNumber.setStatus("mandatory")
_EnclosureName_Type = DisplayString
_EnclosureName_Object = MibTableColumn
enclosureName = _EnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 2),
    _EnclosureName_Type()
)
enclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureName.setStatus("mandatory")
_EnclosureVendor_Type = DisplayString
_EnclosureVendor_Object = MibTableColumn
enclosureVendor = _EnclosureVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 3),
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
              6,
              55)
        )
    )
    namedValues = NamedValues(
        *(("commLost", 55),
          ("degraded", 6),
          ("failed", 2),
          ("offline", 4),
          ("online", 3),
          ("ready", 1))
    )


_EnclosureState_Type.__name__ = "Integer32"
_EnclosureState_Object = MibTableColumn
enclosureState = _EnclosureState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 4),
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
          ("warining", 1))
    )


_EnclosureSeverity_Type.__name__ = "Integer32"
_EnclosureSeverity_Object = MibTableColumn
enclosureSeverity = _EnclosureSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 5),
    _EnclosureSeverity_Type()
)
enclosureSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSeverity.setStatus("mandatory")
_EnclosureID_Type = Integer32
_EnclosureID_Object = MibTableColumn
enclosureID = _EnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 6),
    _EnclosureID_Type()
)
enclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureID.setStatus("mandatory")
_EnclosureProcessorVersion_Type = DisplayString
_EnclosureProcessorVersion_Object = MibTableColumn
enclosureProcessorVersion = _EnclosureProcessorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 7),
    _EnclosureProcessorVersion_Type()
)
enclosureProcessorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureProcessorVersion.setStatus("mandatory")
_EnclosureServiceTag_Type = DisplayString
_EnclosureServiceTag_Object = MibTableColumn
enclosureServiceTag = _EnclosureServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 8),
    _EnclosureServiceTag_Type()
)
enclosureServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureServiceTag.setStatus("mandatory")
_EnclosureAssetTag_Type = DisplayString
_EnclosureAssetTag_Object = MibTableColumn
enclosureAssetTag = _EnclosureAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 9),
    _EnclosureAssetTag_Type()
)
enclosureAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAssetTag.setStatus("mandatory")
_EnclosureAssetName_Type = DisplayString
_EnclosureAssetName_Object = MibTableColumn
enclosureAssetName = _EnclosureAssetName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 10),
    _EnclosureAssetName_Type()
)
enclosureAssetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAssetName.setStatus("mandatory")
_EnclosureSplitBusPartNumber_Type = DisplayString
_EnclosureSplitBusPartNumber_Object = MibTableColumn
enclosureSplitBusPartNumber = _EnclosureSplitBusPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 11),
    _EnclosureSplitBusPartNumber_Type()
)
enclosureSplitBusPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSplitBusPartNumber.setStatus("mandatory")
_EnclosureProductID_Type = DisplayString
_EnclosureProductID_Object = MibTableColumn
enclosureProductID = _EnclosureProductID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 12),
    _EnclosureProductID_Type()
)
enclosureProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureProductID.setStatus("mandatory")
_EnclosureKernelVersion_Type = DisplayString
_EnclosureKernelVersion_Object = MibTableColumn
enclosureKernelVersion = _EnclosureKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 13),
    _EnclosureKernelVersion_Type()
)
enclosureKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureKernelVersion.setStatus("mandatory")
_EnclosureESM1PartNumber_Type = DisplayString
_EnclosureESM1PartNumber_Object = MibTableColumn
enclosureESM1PartNumber = _EnclosureESM1PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 14),
    _EnclosureESM1PartNumber_Type()
)
enclosureESM1PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureESM1PartNumber.setStatus("mandatory")
_EnclosureESM2PartNumber_Type = DisplayString
_EnclosureESM2PartNumber_Object = MibTableColumn
enclosureESM2PartNumber = _EnclosureESM2PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 15),
    _EnclosureESM2PartNumber_Type()
)
enclosureESM2PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureESM2PartNumber.setStatus("mandatory")


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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dELLPV200SPV201S", 2),
          ("dELLPV210SPV211S", 3),
          ("dELLPV220SPV221S", 4),
          ("dELLPV224F", 6),
          ("dELLPV660F", 5),
          ("dELLPV660F224F", 7),
          ("internal", 1))
    )


_EnclosureType_Type.__name__ = "Integer32"
_EnclosureType_Object = MibTableColumn
enclosureType = _EnclosureType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 16),
    _EnclosureType_Type()
)
enclosureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureType.setStatus("mandatory")
_EnclosureProcessor2Version_Type = DisplayString
_EnclosureProcessor2Version_Object = MibTableColumn
enclosureProcessor2Version = _EnclosureProcessor2Version_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 17),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("clustered", 3),
          ("joined", 1),
          ("splitBus", 2))
    )


_EnclosureConfig_Type.__name__ = "Integer32"
_EnclosureConfig_Object = MibTableColumn
enclosureConfig = _EnclosureConfig_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 18),
    _EnclosureConfig_Type()
)
enclosureConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureConfig.setStatus("mandatory")
_EnclosureChannelNumber_Type = Integer32
_EnclosureChannelNumber_Object = MibTableColumn
enclosureChannelNumber = _EnclosureChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 19),
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
        *(("off", 1),
          ("on", 2))
    )


_EnclosureAlarm_Type.__name__ = "Integer32"
_EnclosureAlarm_Object = MibTableColumn
enclosureAlarm = _EnclosureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 20),
    _EnclosureAlarm_Type()
)
enclosureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAlarm.setStatus("mandatory")
_EnclosureBackplanePartNumber_Type = DisplayString
_EnclosureBackplanePartNumber_Object = MibTableColumn
enclosureBackplanePartNumber = _EnclosureBackplanePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 21),
    _EnclosureBackplanePartNumber_Type()
)
enclosureBackplanePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureBackplanePartNumber.setStatus("mandatory")
_EnclosureSCSIID_Type = Integer32
_EnclosureSCSIID_Object = MibTableColumn
enclosureSCSIID = _EnclosureSCSIID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 3, 1, 22),
    _EnclosureSCSIID_Type()
)
enclosureSCSIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSCSIID.setStatus("mandatory")
_ArrayDiskTable_Object = MibTable
arrayDiskTable = _ArrayDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4)
)
if mibBuilder.loadTexts:
    arrayDiskTable.setStatus("mandatory")
_ArrayDiskEntry_Object = MibTableRow
arrayDiskEntry = _ArrayDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1)
)
arrayDiskEntry.setIndexNames(
    (0, "ArrayManager-MIB", "arrayDiskNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 1),
    _ArrayDiskNumber_Type()
)
arrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskNumber.setStatus("mandatory")
_ArrayDiskName_Type = DisplayString
_ArrayDiskName_Object = MibTableColumn
arrayDiskName = _ArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 2),
    _ArrayDiskName_Type()
)
arrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskName.setStatus("mandatory")
_ArrayDiskVendor_Type = DisplayString
_ArrayDiskVendor_Object = MibTableColumn
arrayDiskVendor = _ArrayDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 3),
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
              15,
              24,
              25,
              26,
              28,
              35)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("diagnostics", 28),
          ("failed", 2),
          ("formatting", 26),
          ("initializing", 35),
          ("noMedia", 25),
          ("offline", 4),
          ("online", 3),
          ("ready", 1),
          ("rebuild", 24),
          ("recovering", 7),
          ("removed", 11),
          ("resynching", 15))
    )


_ArrayDiskState_Type.__name__ = "Integer32"
_ArrayDiskState_Object = MibTableColumn
arrayDiskState = _ArrayDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 5),
    _ArrayDiskSeverity_Type()
)
arrayDiskSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskSeverity.setStatus("mandatory")
_ArrayDiskProductID_Type = DisplayString
_ArrayDiskProductID_Object = MibTableColumn
arrayDiskProductID = _ArrayDiskProductID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 6),
    _ArrayDiskProductID_Type()
)
arrayDiskProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskProductID.setStatus("mandatory")
_ArrayDiskSerialNo_Type = DisplayString
_ArrayDiskSerialNo_Object = MibTableColumn
arrayDiskSerialNo = _ArrayDiskSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 7),
    _ArrayDiskSerialNo_Type()
)
arrayDiskSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskSerialNo.setStatus("mandatory")
_ArrayDiskRevision_Type = DisplayString
_ArrayDiskRevision_Object = MibTableColumn
arrayDiskRevision = _ArrayDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 8),
    _ArrayDiskRevision_Type()
)
arrayDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskRevision.setStatus("mandatory")
_ArrayDiskEnclosureID_Type = DisplayString
_ArrayDiskEnclosureID_Object = MibTableColumn
arrayDiskEnclosureID = _ArrayDiskEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 9),
    _ArrayDiskEnclosureID_Type()
)
arrayDiskEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureID.setStatus("mandatory")
_ArrayDiskChannel_Type = Integer32
_ArrayDiskChannel_Object = MibTableColumn
arrayDiskChannel = _ArrayDiskChannel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 10),
    _ArrayDiskChannel_Type()
)
arrayDiskChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannel.setStatus("mandatory")
_ArrayDiskLengthInMB_Type = Integer32
_ArrayDiskLengthInMB_Object = MibTableColumn
arrayDiskLengthInMB = _ArrayDiskLengthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 11),
    _ArrayDiskLengthInMB_Type()
)
arrayDiskLengthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLengthInMB.setStatus("mandatory")
_ArrayDiskLengthInBytes_Type = Integer32
_ArrayDiskLengthInBytes_Object = MibTableColumn
arrayDiskLengthInBytes = _ArrayDiskLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 12),
    _ArrayDiskLengthInBytes_Type()
)
arrayDiskLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLengthInBytes.setStatus("mandatory")
_ArrayDiskLargestContiguousFreeSpaceInMB_Type = Integer32
_ArrayDiskLargestContiguousFreeSpaceInMB_Object = MibTableColumn
arrayDiskLargestContiguousFreeSpaceInMB = _ArrayDiskLargestContiguousFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 13),
    _ArrayDiskLargestContiguousFreeSpaceInMB_Type()
)
arrayDiskLargestContiguousFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLargestContiguousFreeSpaceInMB.setStatus("mandatory")
_ArrayDiskLargestContiguousFreeSpaceInBytes_Type = Integer32
_ArrayDiskLargestContiguousFreeSpaceInBytes_Object = MibTableColumn
arrayDiskLargestContiguousFreeSpaceInBytes = _ArrayDiskLargestContiguousFreeSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 15),
    _ArrayDiskTargetID_Type()
)
arrayDiskTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskTargetID.setStatus("mandatory")
_ArrayDiskLunID_Type = Integer32
_ArrayDiskLunID_Object = MibTableColumn
arrayDiskLunID = _ArrayDiskLunID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 16),
    _ArrayDiskLunID_Type()
)
arrayDiskLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLunID.setStatus("mandatory")
_ArrayDiskUsedSpaceInMB_Type = Integer32
_ArrayDiskUsedSpaceInMB_Object = MibTableColumn
arrayDiskUsedSpaceInMB = _ArrayDiskUsedSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 17),
    _ArrayDiskUsedSpaceInMB_Type()
)
arrayDiskUsedSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskUsedSpaceInMB.setStatus("mandatory")
_ArrayDiskUsedSpaceInBytes_Type = Integer32
_ArrayDiskUsedSpaceInBytes_Object = MibTableColumn
arrayDiskUsedSpaceInBytes = _ArrayDiskUsedSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 18),
    _ArrayDiskUsedSpaceInBytes_Type()
)
arrayDiskUsedSpaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskUsedSpaceInBytes.setStatus("mandatory")
_ArrayDiskFreeSpaceInMB_Type = Integer32
_ArrayDiskFreeSpaceInMB_Object = MibTableColumn
arrayDiskFreeSpaceInMB = _ArrayDiskFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 19),
    _ArrayDiskFreeSpaceInMB_Type()
)
arrayDiskFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskFreeSpaceInMB.setStatus("mandatory")
_ArrayDiskFreeSpaceInBytes_Type = Integer32
_ArrayDiskFreeSpaceInBytes_Object = MibTableColumn
arrayDiskFreeSpaceInBytes = _ArrayDiskFreeSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 20),
    _ArrayDiskFreeSpaceInBytes_Type()
)
arrayDiskFreeSpaceInBytes.setMaxAccess("read-write")
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("fibre", 3),
          ("ide", 2),
          ("scsi", 1),
          ("ssa", 4),
          ("usb", 6))
    )


_ArrayDiskBusType_Type.__name__ = "Integer32"
_ArrayDiskBusType_Object = MibTableColumn
arrayDiskBusType = _ArrayDiskBusType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 21),
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("dedicatedHotSpare", 4),
          ("globalHotSpare", 3),
          ("memberDG", 2),
          ("memberVD", 1))
    )


_ArrayDiskSpareState_Type.__name__ = "Integer32"
_ArrayDiskSpareState_Object = MibTableColumn
arrayDiskSpareState = _ArrayDiskSpareState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 4, 1, 22),
    _ArrayDiskSpareState_Type()
)
arrayDiskSpareState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrayDiskSpareState.setStatus("mandatory")
_ArrayDiskEnclosureConnectionTable_Object = MibTable
arrayDiskEnclosureConnectionTable = _ArrayDiskEnclosureConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5)
)
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionTable.setStatus("mandatory")
_ArrayDiskEnclosureConnectionEntry_Object = MibTableRow
arrayDiskEnclosureConnectionEntry = _ArrayDiskEnclosureConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5, 1)
)
arrayDiskEnclosureConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "arrayDiskEnclosureConnectionNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5, 1, 1),
    _ArrayDiskEnclosureConnectionNumber_Type()
)
arrayDiskEnclosureConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionNumber.setStatus("mandatory")
_ArrayDiskEnclosureConnectionArrayDiskName_Type = DisplayString
_ArrayDiskEnclosureConnectionArrayDiskName_Object = MibTableColumn
arrayDiskEnclosureConnectionArrayDiskName = _ArrayDiskEnclosureConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5, 1, 2),
    _ArrayDiskEnclosureConnectionArrayDiskName_Type()
)
arrayDiskEnclosureConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionArrayDiskName.setStatus("mandatory")
_ArrayDiskEnclosureConnectionArrayDiskNumber_Type = Integer32
_ArrayDiskEnclosureConnectionArrayDiskNumber_Object = MibTableColumn
arrayDiskEnclosureConnectionArrayDiskNumber = _ArrayDiskEnclosureConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5, 1, 3),
    _ArrayDiskEnclosureConnectionArrayDiskNumber_Type()
)
arrayDiskEnclosureConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionArrayDiskNumber.setStatus("mandatory")
_ArrayDiskEnclosureConnectionEnclosureName_Type = DisplayString
_ArrayDiskEnclosureConnectionEnclosureName_Object = MibTableColumn
arrayDiskEnclosureConnectionEnclosureName = _ArrayDiskEnclosureConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5, 1, 4),
    _ArrayDiskEnclosureConnectionEnclosureName_Type()
)
arrayDiskEnclosureConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionEnclosureName.setStatus("mandatory")
_ArrayDiskEnclosureConnectionEnclosureNumber_Type = Integer32
_ArrayDiskEnclosureConnectionEnclosureNumber_Object = MibTableColumn
arrayDiskEnclosureConnectionEnclosureNumber = _ArrayDiskEnclosureConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5, 1, 5),
    _ArrayDiskEnclosureConnectionEnclosureNumber_Type()
)
arrayDiskEnclosureConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionEnclosureNumber.setStatus("mandatory")
_ArrayDiskEnclosureConnectionControllerName_Type = DisplayString
_ArrayDiskEnclosureConnectionControllerName_Object = MibTableColumn
arrayDiskEnclosureConnectionControllerName = _ArrayDiskEnclosureConnectionControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5, 1, 6),
    _ArrayDiskEnclosureConnectionControllerName_Type()
)
arrayDiskEnclosureConnectionControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionControllerName.setStatus("mandatory")
_ArrayDiskEnclosureConnectionControllerNumber_Type = Integer32
_ArrayDiskEnclosureConnectionControllerNumber_Object = MibTableColumn
arrayDiskEnclosureConnectionControllerNumber = _ArrayDiskEnclosureConnectionControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 5, 1, 7),
    _ArrayDiskEnclosureConnectionControllerNumber_Type()
)
arrayDiskEnclosureConnectionControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskEnclosureConnectionControllerNumber.setStatus("mandatory")
_ArrayDiskChannelConnectionTable_Object = MibTable
arrayDiskChannelConnectionTable = _ArrayDiskChannelConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6)
)
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionTable.setStatus("mandatory")
_ArrayDiskChannelConnectionEntry_Object = MibTableRow
arrayDiskChannelConnectionEntry = _ArrayDiskChannelConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6, 1)
)
arrayDiskChannelConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "arrayDiskChannelConnectionNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6, 1, 1),
    _ArrayDiskChannelConnectionNumber_Type()
)
arrayDiskChannelConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionNumber.setStatus("mandatory")
_ArrayDiskChannelConnectionArrayDiskName_Type = DisplayString
_ArrayDiskChannelConnectionArrayDiskName_Object = MibTableColumn
arrayDiskChannelConnectionArrayDiskName = _ArrayDiskChannelConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6, 1, 2),
    _ArrayDiskChannelConnectionArrayDiskName_Type()
)
arrayDiskChannelConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionArrayDiskName.setStatus("mandatory")
_ArrayDiskChannelConnectionArrayDiskNumber_Type = Integer32
_ArrayDiskChannelConnectionArrayDiskNumber_Object = MibTableColumn
arrayDiskChannelConnectionArrayDiskNumber = _ArrayDiskChannelConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6, 1, 3),
    _ArrayDiskChannelConnectionArrayDiskNumber_Type()
)
arrayDiskChannelConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionArrayDiskNumber.setStatus("mandatory")
_ArrayDiskChannelConnectionChannelName_Type = DisplayString
_ArrayDiskChannelConnectionChannelName_Object = MibTableColumn
arrayDiskChannelConnectionChannelName = _ArrayDiskChannelConnectionChannelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6, 1, 4),
    _ArrayDiskChannelConnectionChannelName_Type()
)
arrayDiskChannelConnectionChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionChannelName.setStatus("mandatory")
_ArrayDiskChannelConnectionChannelNumber_Type = Integer32
_ArrayDiskChannelConnectionChannelNumber_Object = MibTableColumn
arrayDiskChannelConnectionChannelNumber = _ArrayDiskChannelConnectionChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6, 1, 5),
    _ArrayDiskChannelConnectionChannelNumber_Type()
)
arrayDiskChannelConnectionChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionChannelNumber.setStatus("mandatory")
_ArrayDiskChannelConnectionControllerName_Type = DisplayString
_ArrayDiskChannelConnectionControllerName_Object = MibTableColumn
arrayDiskChannelConnectionControllerName = _ArrayDiskChannelConnectionControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6, 1, 6),
    _ArrayDiskChannelConnectionControllerName_Type()
)
arrayDiskChannelConnectionControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionControllerName.setStatus("mandatory")
_ArrayDiskChannelConnectionControllerNumber_Type = Integer32
_ArrayDiskChannelConnectionControllerNumber_Object = MibTableColumn
arrayDiskChannelConnectionControllerNumber = _ArrayDiskChannelConnectionControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 6, 1, 7),
    _ArrayDiskChannelConnectionControllerNumber_Type()
)
arrayDiskChannelConnectionControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskChannelConnectionControllerNumber.setStatus("mandatory")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("mandatory")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1)
)
fanEntry.setIndexNames(
    (0, "ArrayManager-MIB", "fanNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("mandatory")
_FanName_Type = DisplayString
_FanName_Object = MibTableColumn
fanName = _FanName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 2),
    _FanName_Type()
)
fanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanName.setStatus("mandatory")
_FanVendor_Type = DisplayString
_FanVendor_Object = MibTableColumn
fanVendor = _FanVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 3),
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
              55)
        )
    )
    namedValues = NamedValues(
        *(("commLost", 55),
          ("degraded", 6),
          ("failed", 2),
          ("ready", 1),
          ("removed", 11))
    )


_FanState_Type.__name__ = "Integer32"
_FanState_Object = MibTableColumn
fanState = _FanState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 5),
    _FanSeverity_Type()
)
fanSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSeverity.setStatus("mandatory")
_FanProbeUnit_Type = DisplayString
_FanProbeUnit_Object = MibTableColumn
fanProbeUnit = _FanProbeUnit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 6),
    _FanProbeUnit_Type()
)
fanProbeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeUnit.setStatus("mandatory")
_FanProbeMinWarning_Type = DisplayString
_FanProbeMinWarning_Object = MibTableColumn
fanProbeMinWarning = _FanProbeMinWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 7),
    _FanProbeMinWarning_Type()
)
fanProbeMinWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeMinWarning.setStatus("mandatory")
_FanProbeMinCritical_Type = DisplayString
_FanProbeMinCritical_Object = MibTableColumn
fanProbeMinCritical = _FanProbeMinCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 8),
    _FanProbeMinCritical_Type()
)
fanProbeMinCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeMinCritical.setStatus("mandatory")
_FanProbeMaxWarning_Type = DisplayString
_FanProbeMaxWarning_Object = MibTableColumn
fanProbeMaxWarning = _FanProbeMaxWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 9),
    _FanProbeMaxWarning_Type()
)
fanProbeMaxWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeMaxWarning.setStatus("mandatory")
_FanProbeMaxCritical_Type = DisplayString
_FanProbeMaxCritical_Object = MibTableColumn
fanProbeMaxCritical = _FanProbeMaxCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 10),
    _FanProbeMaxCritical_Type()
)
fanProbeMaxCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeMaxCritical.setStatus("mandatory")
_FanProbeCurrValue_Type = DisplayString
_FanProbeCurrValue_Object = MibTableColumn
fanProbeCurrValue = _FanProbeCurrValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 11),
    _FanProbeCurrValue_Type()
)
fanProbeCurrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanProbeCurrValue.setStatus("mandatory")
_Fan1PartNumber_Type = DisplayString
_Fan1PartNumber_Object = MibTableColumn
fan1PartNumber = _Fan1PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 12),
    _Fan1PartNumber_Type()
)
fan1PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1PartNumber.setStatus("mandatory")
_Fan2PartNumber_Type = DisplayString
_Fan2PartNumber_Object = MibTableColumn
fan2PartNumber = _Fan2PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 7, 1, 13),
    _Fan2PartNumber_Type()
)
fan2PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2PartNumber.setStatus("mandatory")
_FanConnectionTable_Object = MibTable
fanConnectionTable = _FanConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 8)
)
if mibBuilder.loadTexts:
    fanConnectionTable.setStatus("mandatory")
_FanConnectionEntry_Object = MibTableRow
fanConnectionEntry = _FanConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 8, 1)
)
fanConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "fanConnectionNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 8, 1, 1),
    _FanConnectionNumber_Type()
)
fanConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionNumber.setStatus("mandatory")
_FanConnectionFanName_Type = DisplayString
_FanConnectionFanName_Object = MibTableColumn
fanConnectionFanName = _FanConnectionFanName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 8, 1, 2),
    _FanConnectionFanName_Type()
)
fanConnectionFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionFanName.setStatus("mandatory")
_FanConnectionFanNumber_Type = Integer32
_FanConnectionFanNumber_Object = MibTableColumn
fanConnectionFanNumber = _FanConnectionFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 8, 1, 3),
    _FanConnectionFanNumber_Type()
)
fanConnectionFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionFanNumber.setStatus("mandatory")
_FanConnectionEnclosureName_Type = DisplayString
_FanConnectionEnclosureName_Object = MibTableColumn
fanConnectionEnclosureName = _FanConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 8, 1, 4),
    _FanConnectionEnclosureName_Type()
)
fanConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionEnclosureName.setStatus("mandatory")
_FanConnectionEnclosureNumber_Type = Integer32
_FanConnectionEnclosureNumber_Object = MibTableColumn
fanConnectionEnclosureNumber = _FanConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 8, 1, 5),
    _FanConnectionEnclosureNumber_Type()
)
fanConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanConnectionEnclosureNumber.setStatus("mandatory")
_PowersupplyTable_Object = MibTable
powersupplyTable = _PowersupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9)
)
if mibBuilder.loadTexts:
    powersupplyTable.setStatus("mandatory")
_PowersupplyEntry_Object = MibTableRow
powersupplyEntry = _PowersupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9, 1)
)
powersupplyEntry.setIndexNames(
    (0, "ArrayManager-MIB", "powersupplyNumber"),
)
if mibBuilder.loadTexts:
    powersupplyEntry.setStatus("mandatory")


class _PowersupplyNumber_Type(Integer32):
    """Custom type powersupplyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PowersupplyNumber_Type.__name__ = "Integer32"
_PowersupplyNumber_Object = MibTableColumn
powersupplyNumber = _PowersupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9, 1, 1),
    _PowersupplyNumber_Type()
)
powersupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplyNumber.setStatus("mandatory")
_PowersupplyName_Type = DisplayString
_PowersupplyName_Object = MibTableColumn
powersupplyName = _PowersupplyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9, 1, 2),
    _PowersupplyName_Type()
)
powersupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplyName.setStatus("mandatory")
_PowersupplyVendor_Type = DisplayString
_PowersupplyVendor_Object = MibTableColumn
powersupplyVendor = _PowersupplyVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9, 1, 3),
    _PowersupplyVendor_Type()
)
powersupplyVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplyVendor.setStatus("mandatory")


class _PowersupplyState_Type(Integer32):
    """Custom type powersupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              55)
        )
    )
    namedValues = NamedValues(
        *(("commLost", 55),
          ("failed", 2),
          ("ready", 1))
    )


_PowersupplyState_Type.__name__ = "Integer32"
_PowersupplyState_Object = MibTableColumn
powersupplyState = _PowersupplyState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9, 1, 4),
    _PowersupplyState_Type()
)
powersupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplyState.setStatus("mandatory")


class _PowersupplySeverity_Type(Integer32):
    """Custom type powersupplySeverity based on Integer32"""
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


_PowersupplySeverity_Type.__name__ = "Integer32"
_PowersupplySeverity_Object = MibTableColumn
powersupplySeverity = _PowersupplySeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9, 1, 5),
    _PowersupplySeverity_Type()
)
powersupplySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplySeverity.setStatus("mandatory")
_Powersupply1PartNumber_Type = DisplayString
_Powersupply1PartNumber_Object = MibTableColumn
powersupply1PartNumber = _Powersupply1PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9, 1, 6),
    _Powersupply1PartNumber_Type()
)
powersupply1PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupply1PartNumber.setStatus("mandatory")
_Powersupply2PartNumber_Type = DisplayString
_Powersupply2PartNumber_Object = MibTableColumn
powersupply2PartNumber = _Powersupply2PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 9, 1, 7),
    _Powersupply2PartNumber_Type()
)
powersupply2PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupply2PartNumber.setStatus("mandatory")
_PowersupplyConnectionTable_Object = MibTable
powersupplyConnectionTable = _PowersupplyConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 10)
)
if mibBuilder.loadTexts:
    powersupplyConnectionTable.setStatus("mandatory")
_PowersupplyConnectionEntry_Object = MibTableRow
powersupplyConnectionEntry = _PowersupplyConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 10, 1)
)
powersupplyConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "powersupplyConnectionNumber"),
)
if mibBuilder.loadTexts:
    powersupplyConnectionEntry.setStatus("mandatory")


class _PowersupplyConnectionNumber_Type(Integer32):
    """Custom type powersupplyConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PowersupplyConnectionNumber_Type.__name__ = "Integer32"
_PowersupplyConnectionNumber_Object = MibTableColumn
powersupplyConnectionNumber = _PowersupplyConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 10, 1, 1),
    _PowersupplyConnectionNumber_Type()
)
powersupplyConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplyConnectionNumber.setStatus("mandatory")
_PowersupplyConnectionPowersupplyName_Type = DisplayString
_PowersupplyConnectionPowersupplyName_Object = MibTableColumn
powersupplyConnectionPowersupplyName = _PowersupplyConnectionPowersupplyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 10, 1, 2),
    _PowersupplyConnectionPowersupplyName_Type()
)
powersupplyConnectionPowersupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplyConnectionPowersupplyName.setStatus("mandatory")
_PowersupplyConnectionPowersupplyNumber_Type = Integer32
_PowersupplyConnectionPowersupplyNumber_Object = MibTableColumn
powersupplyConnectionPowersupplyNumber = _PowersupplyConnectionPowersupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 10, 1, 3),
    _PowersupplyConnectionPowersupplyNumber_Type()
)
powersupplyConnectionPowersupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplyConnectionPowersupplyNumber.setStatus("mandatory")
_PowersupplyConnectionEnclosureName_Type = DisplayString
_PowersupplyConnectionEnclosureName_Object = MibTableColumn
powersupplyConnectionEnclosureName = _PowersupplyConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 10, 1, 4),
    _PowersupplyConnectionEnclosureName_Type()
)
powersupplyConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powersupplyConnectionEnclosureName.setStatus("mandatory")
_PowersupplyConnectionEnclosureNumber_Type = Integer32
_PowersupplyConnectionEnclosureNumber_Object = MibTableColumn
powersupplyConnectionEnclosureNumber = _PowersupplyConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 10, 1, 5),
    _PowersupplyConnectionEnclosureNumber_Type()
)
powersupplyConnectionEnclosureNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powersupplyConnectionEnclosureNumber.setStatus("mandatory")
_TemperatureTable_Object = MibTable
temperatureTable = _TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11)
)
if mibBuilder.loadTexts:
    temperatureTable.setStatus("mandatory")
_TemperatureEntry_Object = MibTableRow
temperatureEntry = _TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1)
)
temperatureEntry.setIndexNames(
    (0, "ArrayManager-MIB", "temperatureNumber"),
)
if mibBuilder.loadTexts:
    temperatureEntry.setStatus("mandatory")


class _TemperatureNumber_Type(Integer32):
    """Custom type temperatureNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TemperatureNumber_Type.__name__ = "Integer32"
_TemperatureNumber_Object = MibTableColumn
temperatureNumber = _TemperatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 1),
    _TemperatureNumber_Type()
)
temperatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureNumber.setStatus("mandatory")
_TemperatureName_Type = DisplayString
_TemperatureName_Object = MibTableColumn
temperatureName = _TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 2),
    _TemperatureName_Type()
)
temperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureName.setStatus("mandatory")
_TemperatureVendor_Type = DisplayString
_TemperatureVendor_Object = MibTableColumn
temperatureVendor = _TemperatureVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 3),
    _TemperatureVendor_Type()
)
temperatureVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureVendor.setStatus("mandatory")


class _TemperatureState_Type(Integer32):
    """Custom type temperatureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              55)
        )
    )
    namedValues = NamedValues(
        *(("commLost", 55),
          ("degraded", 6),
          ("failed", 2),
          ("offline", 4),
          ("ready", 1))
    )


_TemperatureState_Type.__name__ = "Integer32"
_TemperatureState_Object = MibTableColumn
temperatureState = _TemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 4),
    _TemperatureState_Type()
)
temperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureState.setStatus("mandatory")


class _TemperatureSeverity_Type(Integer32):
    """Custom type temperatureSeverity based on Integer32"""
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


_TemperatureSeverity_Type.__name__ = "Integer32"
_TemperatureSeverity_Object = MibTableColumn
temperatureSeverity = _TemperatureSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 5),
    _TemperatureSeverity_Type()
)
temperatureSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSeverity.setStatus("mandatory")
_TemperatureProbeUnit_Type = DisplayString
_TemperatureProbeUnit_Object = MibTableColumn
temperatureProbeUnit = _TemperatureProbeUnit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 6),
    _TemperatureProbeUnit_Type()
)
temperatureProbeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUnit.setStatus("mandatory")
_TemperatureProbeMinWarning_Type = Integer32
_TemperatureProbeMinWarning_Object = MibTableColumn
temperatureProbeMinWarning = _TemperatureProbeMinWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 7),
    _TemperatureProbeMinWarning_Type()
)
temperatureProbeMinWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMinWarning.setStatus("mandatory")
_TemperatureProbeMinCritical_Type = Integer32
_TemperatureProbeMinCritical_Object = MibTableColumn
temperatureProbeMinCritical = _TemperatureProbeMinCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 8),
    _TemperatureProbeMinCritical_Type()
)
temperatureProbeMinCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMinCritical.setStatus("mandatory")
_TemperatureProbeMaxWarning_Type = Integer32
_TemperatureProbeMaxWarning_Object = MibTableColumn
temperatureProbeMaxWarning = _TemperatureProbeMaxWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 9),
    _TemperatureProbeMaxWarning_Type()
)
temperatureProbeMaxWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMaxWarning.setStatus("mandatory")
_TemperatureProbeMaxCritical_Type = Integer32
_TemperatureProbeMaxCritical_Object = MibTableColumn
temperatureProbeMaxCritical = _TemperatureProbeMaxCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 10),
    _TemperatureProbeMaxCritical_Type()
)
temperatureProbeMaxCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMaxCritical.setStatus("mandatory")
_TemperatureProbeCurValue_Type = Integer32
_TemperatureProbeCurValue_Object = MibTableColumn
temperatureProbeCurValue = _TemperatureProbeCurValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 11, 1, 11),
    _TemperatureProbeCurValue_Type()
)
temperatureProbeCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeCurValue.setStatus("mandatory")
_TemperatureConnectionTable_Object = MibTable
temperatureConnectionTable = _TemperatureConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 12)
)
if mibBuilder.loadTexts:
    temperatureConnectionTable.setStatus("mandatory")
_TemperatureConnectionEntry_Object = MibTableRow
temperatureConnectionEntry = _TemperatureConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 12, 1)
)
temperatureConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "temperatureConnectionNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 12, 1, 1),
    _TemperatureConnectionNumber_Type()
)
temperatureConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionNumber.setStatus("mandatory")
_TemperatureConnectionTemperatureName_Type = DisplayString
_TemperatureConnectionTemperatureName_Object = MibTableColumn
temperatureConnectionTemperatureName = _TemperatureConnectionTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 12, 1, 2),
    _TemperatureConnectionTemperatureName_Type()
)
temperatureConnectionTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionTemperatureName.setStatus("mandatory")
_TemperatureConnectionTemperatureNumber_Type = Integer32
_TemperatureConnectionTemperatureNumber_Object = MibTableColumn
temperatureConnectionTemperatureNumber = _TemperatureConnectionTemperatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 12, 1, 3),
    _TemperatureConnectionTemperatureNumber_Type()
)
temperatureConnectionTemperatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionTemperatureNumber.setStatus("mandatory")
_TemperatureConnectionEnclosureName_Type = DisplayString
_TemperatureConnectionEnclosureName_Object = MibTableColumn
temperatureConnectionEnclosureName = _TemperatureConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 12, 1, 4),
    _TemperatureConnectionEnclosureName_Type()
)
temperatureConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionEnclosureName.setStatus("mandatory")
_TemperatureConnectionEnclosureNumber_Type = Integer32
_TemperatureConnectionEnclosureNumber_Object = MibTableColumn
temperatureConnectionEnclosureNumber = _TemperatureConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 12, 1, 5),
    _TemperatureConnectionEnclosureNumber_Type()
)
temperatureConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionEnclosureNumber.setStatus("mandatory")
_EnclosureManagementModuleTable_Object = MibTable
enclosureManagementModuleTable = _EnclosureManagementModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13)
)
if mibBuilder.loadTexts:
    enclosureManagementModuleTable.setStatus("mandatory")
_EnclosureManagementModuleEntry_Object = MibTableRow
enclosureManagementModuleEntry = _EnclosureManagementModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1)
)
enclosureManagementModuleEntry.setIndexNames(
    (0, "ArrayManager-MIB", "enclosureManagementModuleNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 1),
    _EnclosureManagementModuleNumber_Type()
)
enclosureManagementModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleNumber.setStatus("mandatory")
_EnclosureManagementModuleName_Type = DisplayString
_EnclosureManagementModuleName_Object = MibTableColumn
enclosureManagementModuleName = _EnclosureManagementModuleName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 2),
    _EnclosureManagementModuleName_Type()
)
enclosureManagementModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleName.setStatus("mandatory")
_EnclosureManagementModuleVendor_Type = DisplayString
_EnclosureManagementModuleVendor_Object = MibTableColumn
enclosureManagementModuleVendor = _EnclosureManagementModuleVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 3),
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
              6,
              55)
        )
    )
    namedValues = NamedValues(
        *(("commLost", 55),
          ("degraded", 6),
          ("failed", 2),
          ("offline", 4),
          ("online", 3),
          ("ready", 1))
    )


_EnclosureManagementModuleState_Type.__name__ = "Integer32"
_EnclosureManagementModuleState_Object = MibTableColumn
enclosureManagementModuleState = _EnclosureManagementModuleState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 4),
    _EnclosureManagementModuleState_Type()
)
enclosureManagementModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleState.setStatus("mandatory")
_EnclosureManagementModuleSeverity_Type = Integer32
_EnclosureManagementModuleSeverity_Object = MibTableColumn
enclosureManagementModuleSeverity = _EnclosureManagementModuleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 5),
    _EnclosureManagementModuleSeverity_Type()
)
enclosureManagementModuleSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleSeverity.setStatus("mandatory")
_EnclosureManagementModulePartNumber_Type = DisplayString
_EnclosureManagementModulePartNumber_Object = MibTableColumn
enclosureManagementModulePartNumber = _EnclosureManagementModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 7),
    _EnclosureManagementModuleType_Type()
)
enclosureManagementModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleType.setStatus("mandatory")
_EnclosureManagementModuleFWVersion_Type = DisplayString
_EnclosureManagementModuleFWVersion_Object = MibTableColumn
enclosureManagementModuleFWVersion = _EnclosureManagementModuleFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 8),
    _EnclosureManagementModuleFWVersion_Type()
)
enclosureManagementModuleFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleFWVersion.setStatus("mandatory")
_EnclosureManagementModuleMaxSpeed_Type = DisplayString
_EnclosureManagementModuleMaxSpeed_Object = MibTableColumn
enclosureManagementModuleMaxSpeed = _EnclosureManagementModuleMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 13, 1, 9),
    _EnclosureManagementModuleMaxSpeed_Type()
)
enclosureManagementModuleMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleMaxSpeed.setStatus("mandatory")
_EnclosureManagementModuleConnectionTable_Object = MibTable
enclosureManagementModuleConnectionTable = _EnclosureManagementModuleConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 14)
)
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionTable.setStatus("mandatory")
_EnclosureManagementModuleConnectionEntry_Object = MibTableRow
enclosureManagementModuleConnectionEntry = _EnclosureManagementModuleConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 14, 1)
)
enclosureManagementModuleConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "enclosureManagementModuleConnectionNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 14, 1, 1),
    _EnclosureManagementModuleConnectionNumber_Type()
)
enclosureManagementModuleConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionNumber.setStatus("mandatory")
_EnclosureManagementModuleConnectionEMMName_Type = DisplayString
_EnclosureManagementModuleConnectionEMMName_Object = MibTableColumn
enclosureManagementModuleConnectionEMMName = _EnclosureManagementModuleConnectionEMMName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 14, 1, 2),
    _EnclosureManagementModuleConnectionEMMName_Type()
)
enclosureManagementModuleConnectionEMMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEMMName.setStatus("mandatory")
_EnclosureManagementModuleConnectionEMMNumber_Type = Integer32
_EnclosureManagementModuleConnectionEMMNumber_Object = MibTableColumn
enclosureManagementModuleConnectionEMMNumber = _EnclosureManagementModuleConnectionEMMNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 14, 1, 3),
    _EnclosureManagementModuleConnectionEMMNumber_Type()
)
enclosureManagementModuleConnectionEMMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEMMNumber.setStatus("mandatory")
_EnclosureManagementModuleConnectionEnclosureName_Type = DisplayString
_EnclosureManagementModuleConnectionEnclosureName_Object = MibTableColumn
enclosureManagementModuleConnectionEnclosureName = _EnclosureManagementModuleConnectionEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 14, 1, 4),
    _EnclosureManagementModuleConnectionEnclosureName_Type()
)
enclosureManagementModuleConnectionEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEnclosureName.setStatus("mandatory")
_EnclosureManagementModuleConnectionEnclosureNumber_Type = Integer32
_EnclosureManagementModuleConnectionEnclosureNumber_Object = MibTableColumn
enclosureManagementModuleConnectionEnclosureNumber = _EnclosureManagementModuleConnectionEnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 130, 14, 1, 5),
    _EnclosureManagementModuleConnectionEnclosureNumber_Type()
)
enclosureManagementModuleConnectionEnclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleConnectionEnclosureNumber.setStatus("mandatory")
_LogicalDevices_ObjectIdentity = ObjectIdentity
logicalDevices = _LogicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140)
)
_VirtualDiskTable_Object = MibTable
virtualDiskTable = _VirtualDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1)
)
if mibBuilder.loadTexts:
    virtualDiskTable.setStatus("mandatory")
_VirtualDiskEntry_Object = MibTableRow
virtualDiskEntry = _VirtualDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1)
)
virtualDiskEntry.setIndexNames(
    (0, "ArrayManager-MIB", "virtualDiskNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 1),
    _VirtualDiskNumber_Type()
)
virtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskNumber.setStatus("mandatory")
_VirtualDiskName_Type = DisplayString
_VirtualDiskName_Object = MibTableColumn
virtualDiskName = _VirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 2),
    _VirtualDiskName_Type()
)
virtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskName.setStatus("mandatory")
_VirtualDiskDeviceName_Type = DisplayString
_VirtualDiskDeviceName_Object = MibTableColumn
virtualDiskDeviceName = _VirtualDiskDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 3),
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
              18,
              24,
              26,
              35)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("failedRedundancy", 18),
          ("formatting", 26),
          ("initializing", 35),
          ("offline", 4),
          ("online", 3),
          ("ready", 1),
          ("rebuilding", 24),
          ("resynching", 15),
          ("verifying", 7))
    )


_VirtualDiskState_Type.__name__ = "Integer32"
_VirtualDiskState_Object = MibTableColumn
virtualDiskState = _VirtualDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 5),
    _VirtualDiskSeverity_Type()
)
virtualDiskSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskSeverity.setStatus("mandatory")
_VirtualDiskLengthInMB_Type = Integer32
_VirtualDiskLengthInMB_Object = MibTableColumn
virtualDiskLengthInMB = _VirtualDiskLengthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 6),
    _VirtualDiskLengthInMB_Type()
)
virtualDiskLengthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLengthInMB.setStatus("mandatory")
_VirtualDiskLengthInBytes_Type = Integer32
_VirtualDiskLengthInBytes_Object = MibTableColumn
virtualDiskLengthInBytes = _VirtualDiskLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 7),
    _VirtualDiskLengthInBytes_Type()
)
virtualDiskLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLengthInBytes.setStatus("mandatory")
_VirtualDiskFreeSpaceInMB_Type = Integer32
_VirtualDiskFreeSpaceInMB_Object = MibTableColumn
virtualDiskFreeSpaceInMB = _VirtualDiskFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 8),
    _VirtualDiskFreeSpaceInMB_Type()
)
virtualDiskFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskFreeSpaceInMB.setStatus("mandatory")
_VirtualDiskFreeSpaceInBytes_Type = Integer32
_VirtualDiskFreeSpaceInBytes_Object = MibTableColumn
virtualDiskFreeSpaceInBytes = _VirtualDiskFreeSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 9),
    _VirtualDiskFreeSpaceInBytes_Type()
)
virtualDiskFreeSpaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskFreeSpaceInBytes.setStatus("mandatory")


class _VirtualDiskWritePolicy_Type(Integer32):
    """Custom type virtualDiskWritePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VirtualDiskWritePolicy_Type.__name__ = "Integer32"
_VirtualDiskWritePolicy_Object = MibTableColumn
virtualDiskWritePolicy = _VirtualDiskWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 10),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveReadAhead", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_VirtualDiskReadPolicy_Type.__name__ = "Integer32"
_VirtualDiskReadPolicy_Object = MibTableColumn
virtualDiskReadPolicy = _VirtualDiskReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 11),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("cachedIO", 2),
          ("directIO", 1))
    )


_VirtualDiskCachePolicy_Type.__name__ = "Integer32"
_VirtualDiskCachePolicy_Object = MibTableColumn
virtualDiskCachePolicy = _VirtualDiskCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 12),
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("addSpares", 13),
          ("concatenated", 1),
          ("deleteLogical", 14),
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
          ("raid-7", 9),
          ("transformLogical", 15))
    )


_VirtualDiskLayout_Type.__name__ = "Integer32"
_VirtualDiskLayout_Object = MibTableColumn
virtualDiskLayout = _VirtualDiskLayout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 13),
    _VirtualDiskLayout_Type()
)
virtualDiskLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLayout.setStatus("mandatory")
_VirtualDiskCurStripeSizeInMB_Type = Integer32
_VirtualDiskCurStripeSizeInMB_Object = MibTableColumn
virtualDiskCurStripeSizeInMB = _VirtualDiskCurStripeSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 14),
    _VirtualDiskCurStripeSizeInMB_Type()
)
virtualDiskCurStripeSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskCurStripeSizeInMB.setStatus("mandatory")
_VirtualDiskCurStripeSizeInBytes_Type = Integer32
_VirtualDiskCurStripeSizeInBytes_Object = MibTableColumn
virtualDiskCurStripeSizeInBytes = _VirtualDiskCurStripeSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 15),
    _VirtualDiskCurStripeSizeInBytes_Type()
)
virtualDiskCurStripeSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskCurStripeSizeInBytes.setStatus("mandatory")
_VirtualDiskChannel_Type = Integer32
_VirtualDiskChannel_Object = MibTableColumn
virtualDiskChannel = _VirtualDiskChannel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 16),
    _VirtualDiskChannel_Type()
)
virtualDiskChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskChannel.setStatus("mandatory")
_VirtualDiskTargetID_Type = Integer32
_VirtualDiskTargetID_Object = MibTableColumn
virtualDiskTargetID = _VirtualDiskTargetID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 17),
    _VirtualDiskTargetID_Type()
)
virtualDiskTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskTargetID.setStatus("mandatory")
_VirtualDiskLunID_Type = Integer32
_VirtualDiskLunID_Object = MibTableColumn
virtualDiskLunID = _VirtualDiskLunID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 1, 1, 18),
    _VirtualDiskLunID_Type()
)
virtualDiskLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLunID.setStatus("mandatory")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("mandatory")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1)
)
diskEntry.setIndexNames(
    (0, "ArrayManager-MIB", "diskNumber"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("mandatory")


class _DiskNumber_Type(Integer32):
    """Custom type diskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_DiskNumber_Type.__name__ = "Integer32"
_DiskNumber_Object = MibTableColumn
diskNumber = _DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 1),
    _DiskNumber_Type()
)
diskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumber.setStatus("mandatory")
_DiskName_Type = DisplayString
_DiskName_Object = MibTableColumn
diskName = _DiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 2),
    _DiskName_Type()
)
diskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskName.setStatus("mandatory")
_DiskVirtualDiskDeviceName_Type = DisplayString
_DiskVirtualDiskDeviceName_Object = MibTableColumn
diskVirtualDiskDeviceName = _DiskVirtualDiskDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 3),
    _DiskVirtualDiskDeviceName_Type()
)
diskVirtualDiskDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVirtualDiskDeviceName.setStatus("mandatory")


class _DiskState_Type(Integer32):
    """Custom type diskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              24,
              25,
              40)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("noMedia", 25),
          ("notReady", 40),
          ("offline", 4),
          ("online", 3),
          ("ready", 1),
          ("rebuild", 24))
    )


_DiskState_Type.__name__ = "Integer32"
_DiskState_Object = MibTableColumn
diskState = _DiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 4),
    _DiskState_Type()
)
diskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskState.setStatus("mandatory")


class _DiskSeverity_Type(Integer32):
    """Custom type diskSeverity based on Integer32"""
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


_DiskSeverity_Type.__name__ = "Integer32"
_DiskSeverity_Object = MibTableColumn
diskSeverity = _DiskSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 5),
    _DiskSeverity_Type()
)
diskSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSeverity.setStatus("mandatory")


class _DiskLdmDeviceType_Type(Integer32):
    """Custom type diskLdmDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("basic", 4),
          ("basicNoSignature", 5),
          ("cd-rom", 3),
          ("dvd", 7),
          ("dynamic", 1),
          ("oem", 6),
          ("removable", 2))
    )


_DiskLdmDeviceType_Type.__name__ = "Integer32"
_DiskLdmDeviceType_Object = MibTableColumn
diskLdmDeviceType = _DiskLdmDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 6),
    _DiskLdmDeviceType_Type()
)
diskLdmDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskLdmDeviceType.setStatus("mandatory")
_DiskDgName_Type = DisplayString
_DiskDgName_Object = MibTableColumn
diskDgName = _DiskDgName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 7),
    _DiskDgName_Type()
)
diskDgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDgName.setStatus("mandatory")
_DiskLengthInMB_Type = Integer32
_DiskLengthInMB_Object = MibTableColumn
diskLengthInMB = _DiskLengthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 8),
    _DiskLengthInMB_Type()
)
diskLengthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskLengthInMB.setStatus("mandatory")
_DiskLengthInBytes_Type = Integer32
_DiskLengthInBytes_Object = MibTableColumn
diskLengthInBytes = _DiskLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 9),
    _DiskLengthInBytes_Type()
)
diskLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskLengthInBytes.setStatus("mandatory")
_DiskFreeSpaceInMB_Type = Integer32
_DiskFreeSpaceInMB_Object = MibTableColumn
diskFreeSpaceInMB = _DiskFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 10),
    _DiskFreeSpaceInMB_Type()
)
diskFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFreeSpaceInMB.setStatus("mandatory")
_DiskFreeSpaceInBytes_Type = Integer32
_DiskFreeSpaceInBytes_Object = MibTableColumn
diskFreeSpaceInBytes = _DiskFreeSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 11),
    _DiskFreeSpaceInBytes_Type()
)
diskFreeSpaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFreeSpaceInBytes.setStatus("mandatory")
_DiskAdapter_Type = DisplayString
_DiskAdapter_Object = MibTableColumn
diskAdapter = _DiskAdapter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 12),
    _DiskAdapter_Type()
)
diskAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskAdapter.setStatus("mandatory")
_DiskPort_Type = Integer32
_DiskPort_Object = MibTableColumn
diskPort = _DiskPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 13),
    _DiskPort_Type()
)
diskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPort.setStatus("mandatory")
_DiskTargetID_Type = Integer32
_DiskTargetID_Object = MibTableColumn
diskTargetID = _DiskTargetID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 14),
    _DiskTargetID_Type()
)
diskTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTargetID.setStatus("mandatory")
_DiskLunID_Type = Integer32
_DiskLunID_Object = MibTableColumn
diskLunID = _DiskLunID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 15),
    _DiskLunID_Type()
)
diskLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskLunID.setStatus("mandatory")
_DiskVendor_Type = DisplayString
_DiskVendor_Object = MibTableColumn
diskVendor = _DiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 2, 1, 16),
    _DiskVendor_Type()
)
diskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVendor.setStatus("mandatory")
_ArrayDiskLogicalConnectionTable_Object = MibTable
arrayDiskLogicalConnectionTable = _ArrayDiskLogicalConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3)
)
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionTable.setStatus("mandatory")
_ArrayDiskLogicalConnectionEntry_Object = MibTableRow
arrayDiskLogicalConnectionEntry = _ArrayDiskLogicalConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3, 1)
)
arrayDiskLogicalConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "arrayDiskLogicalConnectionNumber"),
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
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3, 1, 1),
    _ArrayDiskLogicalConnectionNumber_Type()
)
arrayDiskLogicalConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionNumber.setStatus("mandatory")
_ArrayDiskLogicalConnectionArrayDiskName_Type = DisplayString
_ArrayDiskLogicalConnectionArrayDiskName_Object = MibTableColumn
arrayDiskLogicalConnectionArrayDiskName = _ArrayDiskLogicalConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3, 1, 2),
    _ArrayDiskLogicalConnectionArrayDiskName_Type()
)
arrayDiskLogicalConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionArrayDiskName.setStatus("mandatory")
_ArrayDiskLogicalConnectionArrayDiskNumber_Type = Integer32
_ArrayDiskLogicalConnectionArrayDiskNumber_Object = MibTableColumn
arrayDiskLogicalConnectionArrayDiskNumber = _ArrayDiskLogicalConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3, 1, 3),
    _ArrayDiskLogicalConnectionArrayDiskNumber_Type()
)
arrayDiskLogicalConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionArrayDiskNumber.setStatus("mandatory")
_ArrayDiskLogicalConnectionVirtualDiskName_Type = DisplayString
_ArrayDiskLogicalConnectionVirtualDiskName_Object = MibTableColumn
arrayDiskLogicalConnectionVirtualDiskName = _ArrayDiskLogicalConnectionVirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3, 1, 4),
    _ArrayDiskLogicalConnectionVirtualDiskName_Type()
)
arrayDiskLogicalConnectionVirtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionVirtualDiskName.setStatus("mandatory")
_ArrayDiskLogicalConnectionVirtualDiskNumber_Type = Integer32
_ArrayDiskLogicalConnectionVirtualDiskNumber_Object = MibTableColumn
arrayDiskLogicalConnectionVirtualDiskNumber = _ArrayDiskLogicalConnectionVirtualDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3, 1, 5),
    _ArrayDiskLogicalConnectionVirtualDiskNumber_Type()
)
arrayDiskLogicalConnectionVirtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionVirtualDiskNumber.setStatus("mandatory")
_ArrayDiskLogicalConnectionDiskName_Type = DisplayString
_ArrayDiskLogicalConnectionDiskName_Object = MibTableColumn
arrayDiskLogicalConnectionDiskName = _ArrayDiskLogicalConnectionDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3, 1, 6),
    _ArrayDiskLogicalConnectionDiskName_Type()
)
arrayDiskLogicalConnectionDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionDiskName.setStatus("mandatory")
_ArrayDiskLogicalConnectionDiskNumber_Type = Integer32
_ArrayDiskLogicalConnectionDiskNumber_Object = MibTableColumn
arrayDiskLogicalConnectionDiskNumber = _ArrayDiskLogicalConnectionDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 3, 1, 7),
    _ArrayDiskLogicalConnectionDiskNumber_Type()
)
arrayDiskLogicalConnectionDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskLogicalConnectionDiskNumber.setStatus("mandatory")
_SubDiskTable_Object = MibTable
subDiskTable = _SubDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 4)
)
if mibBuilder.loadTexts:
    subDiskTable.setStatus("mandatory")
_SubDiskEntry_Object = MibTableRow
subDiskEntry = _SubDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 4, 1)
)
subDiskEntry.setIndexNames(
    (0, "ArrayManager-MIB", "subDiskNumber"),
)
if mibBuilder.loadTexts:
    subDiskEntry.setStatus("mandatory")


class _SubDiskNumber_Type(Integer32):
    """Custom type subDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_SubDiskNumber_Type.__name__ = "Integer32"
_SubDiskNumber_Object = MibTableColumn
subDiskNumber = _SubDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 4, 1, 1),
    _SubDiskNumber_Type()
)
subDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDiskNumber.setStatus("mandatory")
_SubDiskName_Type = DisplayString
_SubDiskName_Object = MibTableColumn
subDiskName = _SubDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 4, 1, 2),
    _SubDiskName_Type()
)
subDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDiskName.setStatus("mandatory")


class _SubDiskState_Type(Integer32):
    """Custom type subDiskState based on Integer32"""
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


_SubDiskState_Type.__name__ = "Integer32"
_SubDiskState_Object = MibTableColumn
subDiskState = _SubDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 4, 1, 3),
    _SubDiskState_Type()
)
subDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDiskState.setStatus("mandatory")
_SubDiskSeverity_Type = Integer32
_SubDiskSeverity_Object = MibTableColumn
subDiskSeverity = _SubDiskSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 4, 1, 4),
    _SubDiskSeverity_Type()
)
subDiskSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDiskSeverity.setStatus("mandatory")
_SubDiskLengthInMB_Type = Integer32
_SubDiskLengthInMB_Object = MibTableColumn
subDiskLengthInMB = _SubDiskLengthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 4, 1, 5),
    _SubDiskLengthInMB_Type()
)
subDiskLengthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDiskLengthInMB.setStatus("mandatory")
_SubDiskLengthInBytes_Type = Integer32
_SubDiskLengthInBytes_Object = MibTableColumn
subDiskLengthInBytes = _SubDiskLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 4, 1, 6),
    _SubDiskLengthInBytes_Type()
)
subDiskLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDiskLengthInBytes.setStatus("mandatory")
_PartitionTable_Object = MibTable
partitionTable = _PartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5)
)
if mibBuilder.loadTexts:
    partitionTable.setStatus("mandatory")
_PartitionEntry_Object = MibTableRow
partitionEntry = _PartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5, 1)
)
partitionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "partitionNumber"),
)
if mibBuilder.loadTexts:
    partitionEntry.setStatus("mandatory")


class _PartitionNumber_Type(Integer32):
    """Custom type partitionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PartitionNumber_Type.__name__ = "Integer32"
_PartitionNumber_Object = MibTableColumn
partitionNumber = _PartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5, 1, 1),
    _PartitionNumber_Type()
)
partitionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionNumber.setStatus("mandatory")
_PartitionName_Type = DisplayString
_PartitionName_Object = MibTableColumn
partitionName = _PartitionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5, 1, 2),
    _PartitionName_Type()
)
partitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionName.setStatus("mandatory")


class _PartitionState_Type(Integer32):
    """Custom type partitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("online", 3),
          ("ready", 1))
    )


_PartitionState_Type.__name__ = "Integer32"
_PartitionState_Object = MibTableColumn
partitionState = _PartitionState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5, 1, 3),
    _PartitionState_Type()
)
partitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionState.setStatus("mandatory")


class _PartitionSeverity_Type(Integer32):
    """Custom type partitionSeverity based on Integer32"""
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


_PartitionSeverity_Type.__name__ = "Integer32"
_PartitionSeverity_Object = MibTableColumn
partitionSeverity = _PartitionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5, 1, 4),
    _PartitionSeverity_Type()
)
partitionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSeverity.setStatus("mandatory")
_PartitionLengthInMB_Type = Integer32
_PartitionLengthInMB_Object = MibTableColumn
partitionLengthInMB = _PartitionLengthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5, 1, 5),
    _PartitionLengthInMB_Type()
)
partitionLengthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionLengthInMB.setStatus("mandatory")
_PartitionLengthInBytes_Type = Integer32
_PartitionLengthInBytes_Object = MibTableColumn
partitionLengthInBytes = _PartitionLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5, 1, 6),
    _PartitionLengthInBytes_Type()
)
partitionLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionLengthInBytes.setStatus("mandatory")


class _PartitionLdmVolumeType_Type(Integer32):
    """Custom type partitionLdmVolumeType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("cdrom", 4),
          ("dynamic", 10),
          ("extended", 2),
          ("logical", 3),
          ("mirror", 7),
          ("raid5", 8),
          ("simple", 5),
          ("span", 9),
          ("stripe", 6))
    )


_PartitionLdmVolumeType_Type.__name__ = "Integer32"
_PartitionLdmVolumeType_Object = MibTableColumn
partitionLdmVolumeType = _PartitionLdmVolumeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 5, 1, 7),
    _PartitionLdmVolumeType_Type()
)
partitionLdmVolumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionLdmVolumeType.setStatus("mandatory")
_ExtendedPartitionTable_Object = MibTable
extendedPartitionTable = _ExtendedPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 6)
)
if mibBuilder.loadTexts:
    extendedPartitionTable.setStatus("mandatory")
_ExtendedPartitionEntry_Object = MibTableRow
extendedPartitionEntry = _ExtendedPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 6, 1)
)
extendedPartitionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "extendedPartitionNumber"),
)
if mibBuilder.loadTexts:
    extendedPartitionEntry.setStatus("mandatory")


class _ExtendedPartitionNumber_Type(Integer32):
    """Custom type extendedPartitionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_ExtendedPartitionNumber_Type.__name__ = "Integer32"
_ExtendedPartitionNumber_Object = MibTableColumn
extendedPartitionNumber = _ExtendedPartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 6, 1, 1),
    _ExtendedPartitionNumber_Type()
)
extendedPartitionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendedPartitionNumber.setStatus("mandatory")
_ExtendedPartitionName_Type = DisplayString
_ExtendedPartitionName_Object = MibTableColumn
extendedPartitionName = _ExtendedPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 6, 1, 2),
    _ExtendedPartitionName_Type()
)
extendedPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendedPartitionName.setStatus("mandatory")


class _ExtendedPartitionState_Type(Integer32):
    """Custom type extendedPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("online", 3),
          ("ready", 1))
    )


_ExtendedPartitionState_Type.__name__ = "Integer32"
_ExtendedPartitionState_Object = MibTableColumn
extendedPartitionState = _ExtendedPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 6, 1, 3),
    _ExtendedPartitionState_Type()
)
extendedPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendedPartitionState.setStatus("mandatory")


class _ExtendedPartitionSeverity_Type(Integer32):
    """Custom type extendedPartitionSeverity based on Integer32"""
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


_ExtendedPartitionSeverity_Type.__name__ = "Integer32"
_ExtendedPartitionSeverity_Object = MibTableColumn
extendedPartitionSeverity = _ExtendedPartitionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 6, 1, 4),
    _ExtendedPartitionSeverity_Type()
)
extendedPartitionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendedPartitionSeverity.setStatus("mandatory")
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("mandatory")
_VolumeEntry_Object = MibTableRow
volumeEntry = _VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1)
)
volumeEntry.setIndexNames(
    (0, "ArrayManager-MIB", "volumeNumber"),
)
if mibBuilder.loadTexts:
    volumeEntry.setStatus("mandatory")


class _VolumeNumber_Type(Integer32):
    """Custom type volumeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VolumeNumber_Type.__name__ = "Integer32"
_VolumeNumber_Object = MibTableColumn
volumeNumber = _VolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 1),
    _VolumeNumber_Type()
)
volumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNumber.setStatus("mandatory")


class _VolumeDriveLetter_Type(DisplayString):
    """Custom type volumeDriveLetter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_VolumeDriveLetter_Type.__name__ = "DisplayString"
_VolumeDriveLetter_Object = MibTableColumn
volumeDriveLetter = _VolumeDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 2),
    _VolumeDriveLetter_Type()
)
volumeDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeDriveLetter.setStatus("mandatory")


class _VolumeState_Type(Integer32):
    """Custom type volumeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              18,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 6),
          ("failed", 2),
          ("failedRedundancy", 18),
          ("formatting", 26),
          ("noMedia", 25),
          ("offline", 4),
          ("online", 3),
          ("ready", 1))
    )


_VolumeState_Type.__name__ = "Integer32"
_VolumeState_Object = MibTableColumn
volumeState = _VolumeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 3),
    _VolumeState_Type()
)
volumeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeState.setStatus("mandatory")


class _VolumeSeverity_Type(Integer32):
    """Custom type volumeSeverity based on Integer32"""
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
          ("failrue", 3),
          ("warning", 1))
    )


_VolumeSeverity_Type.__name__ = "Integer32"
_VolumeSeverity_Object = MibTableColumn
volumeSeverity = _VolumeSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 4),
    _VolumeSeverity_Type()
)
volumeSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeSeverity.setStatus("mandatory")


class _VolumeLdmVolumeType_Type(Integer32):
    """Custom type volumeLdmVolumeType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("cd-rom", 4),
          ("dynamic", 10),
          ("extended", 2),
          ("logical", 3),
          ("mirrror", 7),
          ("raid5", 8),
          ("simple", 5),
          ("span", 9),
          ("stripe", 6))
    )


_VolumeLdmVolumeType_Type.__name__ = "Integer32"
_VolumeLdmVolumeType_Object = MibTableColumn
volumeLdmVolumeType = _VolumeLdmVolumeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 5),
    _VolumeLdmVolumeType_Type()
)
volumeLdmVolumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeLdmVolumeType.setStatus("mandatory")
_VolumeLabel_Type = DisplayString
_VolumeLabel_Object = MibTableColumn
volumeLabel = _VolumeLabel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 6),
    _VolumeLabel_Type()
)
volumeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeLabel.setStatus("mandatory")
_VolumeFSType_Type = DisplayString
_VolumeFSType_Object = MibTableColumn
volumeFSType = _VolumeFSType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 7),
    _VolumeFSType_Type()
)
volumeFSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFSType.setStatus("mandatory")
_VolumeLengthInMB_Type = Integer32
_VolumeLengthInMB_Object = MibTableColumn
volumeLengthInMB = _VolumeLengthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 8),
    _VolumeLengthInMB_Type()
)
volumeLengthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeLengthInMB.setStatus("mandatory")
_VolumeLengthInBytes_Type = Integer32
_VolumeLengthInBytes_Object = MibTableColumn
volumeLengthInBytes = _VolumeLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 9),
    _VolumeLengthInBytes_Type()
)
volumeLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeLengthInBytes.setStatus("mandatory")
_VolumeFreeSpaceInMB_Type = Integer32
_VolumeFreeSpaceInMB_Object = MibTableColumn
volumeFreeSpaceInMB = _VolumeFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 10),
    _VolumeFreeSpaceInMB_Type()
)
volumeFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFreeSpaceInMB.setStatus("mandatory")
_VolumeFreeSpaceInBytes_Type = Integer32
_VolumeFreeSpaceInBytes_Object = MibTableColumn
volumeFreeSpaceInBytes = _VolumeFreeSpaceInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 7, 1, 11),
    _VolumeFreeSpaceInBytes_Type()
)
volumeFreeSpaceInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFreeSpaceInBytes.setStatus("mandatory")
_PlexTable_Object = MibTable
plexTable = _PlexTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 8)
)
if mibBuilder.loadTexts:
    plexTable.setStatus("mandatory")
_PlexEntry_Object = MibTableRow
plexEntry = _PlexEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 8, 1)
)
plexEntry.setIndexNames(
    (0, "ArrayManager-MIB", "plexNumber"),
)
if mibBuilder.loadTexts:
    plexEntry.setStatus("mandatory")


class _PlexNumber_Type(Integer32):
    """Custom type plexNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PlexNumber_Type.__name__ = "Integer32"
_PlexNumber_Object = MibTableColumn
plexNumber = _PlexNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 8, 1, 1),
    _PlexNumber_Type()
)
plexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexNumber.setStatus("mandatory")
_PlexName_Type = DisplayString
_PlexName_Object = MibTableColumn
plexName = _PlexName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 8, 1, 2),
    _PlexName_Type()
)
plexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexName.setStatus("mandatory")
_PlexStripeWidthInMB_Type = Integer32
_PlexStripeWidthInMB_Object = MibTableColumn
plexStripeWidthInMB = _PlexStripeWidthInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 8, 1, 3),
    _PlexStripeWidthInMB_Type()
)
plexStripeWidthInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexStripeWidthInMB.setStatus("mandatory")
_PlexStripeWidthInBytes_Type = Integer32
_PlexStripeWidthInBytes_Object = MibTableColumn
plexStripeWidthInBytes = _PlexStripeWidthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 8, 1, 4),
    _PlexStripeWidthInBytes_Type()
)
plexStripeWidthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexStripeWidthInBytes.setStatus("mandatory")
_PlexColumns_Type = Integer32
_PlexColumns_Object = MibTableColumn
plexColumns = _PlexColumns_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 8, 1, 5),
    _PlexColumns_Type()
)
plexColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexColumns.setStatus("mandatory")


class _PlexLayout_Type(Integer32):
    """Custom type plexLayout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concatenatedSubdisks", 2),
          ("raidLayout", 3),
          ("stripedSubdisks", 1))
    )


_PlexLayout_Type.__name__ = "Integer32"
_PlexLayout_Object = MibTableColumn
plexLayout = _PlexLayout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 8, 1, 6),
    _PlexLayout_Type()
)
plexLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexLayout.setStatus("mandatory")
_BasicDiskExtendedConnectionTable_Object = MibTable
basicDiskExtendedConnectionTable = _BasicDiskExtendedConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9)
)
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionTable.setStatus("mandatory")
_BasicDiskExtendedConnectionEntry_Object = MibTableRow
basicDiskExtendedConnectionEntry = _BasicDiskExtendedConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1)
)
basicDiskExtendedConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "basicDiskExtendedConnectionNumber"),
)
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionEntry.setStatus("mandatory")


class _BasicDiskExtendedConnectionNumber_Type(Integer32):
    """Custom type basicDiskExtendedConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_BasicDiskExtendedConnectionNumber_Type.__name__ = "Integer32"
_BasicDiskExtendedConnectionNumber_Object = MibTableColumn
basicDiskExtendedConnectionNumber = _BasicDiskExtendedConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 1),
    _BasicDiskExtendedConnectionNumber_Type()
)
basicDiskExtendedConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionNumber.setStatus("mandatory")
_BasicDiskExtendedConnectionArrayDiskName_Type = DisplayString
_BasicDiskExtendedConnectionArrayDiskName_Object = MibTableColumn
basicDiskExtendedConnectionArrayDiskName = _BasicDiskExtendedConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 2),
    _BasicDiskExtendedConnectionArrayDiskName_Type()
)
basicDiskExtendedConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionArrayDiskName.setStatus("mandatory")
_BasicDiskExtendedConnectionArrayDiskNumber_Type = Integer32
_BasicDiskExtendedConnectionArrayDiskNumber_Object = MibTableColumn
basicDiskExtendedConnectionArrayDiskNumber = _BasicDiskExtendedConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 3),
    _BasicDiskExtendedConnectionArrayDiskNumber_Type()
)
basicDiskExtendedConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionArrayDiskNumber.setStatus("mandatory")
_BasicDiskExtendedConnectionVirtualDiskName_Type = DisplayString
_BasicDiskExtendedConnectionVirtualDiskName_Object = MibTableColumn
basicDiskExtendedConnectionVirtualDiskName = _BasicDiskExtendedConnectionVirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 4),
    _BasicDiskExtendedConnectionVirtualDiskName_Type()
)
basicDiskExtendedConnectionVirtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionVirtualDiskName.setStatus("mandatory")
_BasicDiskExtendedConnectionVirtualDiskNumber_Type = Integer32
_BasicDiskExtendedConnectionVirtualDiskNumber_Object = MibTableColumn
basicDiskExtendedConnectionVirtualDiskNumber = _BasicDiskExtendedConnectionVirtualDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 5),
    _BasicDiskExtendedConnectionVirtualDiskNumber_Type()
)
basicDiskExtendedConnectionVirtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionVirtualDiskNumber.setStatus("mandatory")
_BasicDiskExtendedConnectionDiskName_Type = DisplayString
_BasicDiskExtendedConnectionDiskName_Object = MibTableColumn
basicDiskExtendedConnectionDiskName = _BasicDiskExtendedConnectionDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 6),
    _BasicDiskExtendedConnectionDiskName_Type()
)
basicDiskExtendedConnectionDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionDiskName.setStatus("mandatory")
_BasicDiskExtendedConnectionDiskNumber_Type = Integer32
_BasicDiskExtendedConnectionDiskNumber_Object = MibTableColumn
basicDiskExtendedConnectionDiskNumber = _BasicDiskExtendedConnectionDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 7),
    _BasicDiskExtendedConnectionDiskNumber_Type()
)
basicDiskExtendedConnectionDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionDiskNumber.setStatus("mandatory")
_BasicDiskExtendedConnectionExtendedPartitionName_Type = DisplayString
_BasicDiskExtendedConnectionExtendedPartitionName_Object = MibTableColumn
basicDiskExtendedConnectionExtendedPartitionName = _BasicDiskExtendedConnectionExtendedPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 8),
    _BasicDiskExtendedConnectionExtendedPartitionName_Type()
)
basicDiskExtendedConnectionExtendedPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionExtendedPartitionName.setStatus("mandatory")
_BasicDiskExtendedConnectionExtendedPartitionNumber_Type = Integer32
_BasicDiskExtendedConnectionExtendedPartitionNumber_Object = MibTableColumn
basicDiskExtendedConnectionExtendedPartitionNumber = _BasicDiskExtendedConnectionExtendedPartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 9),
    _BasicDiskExtendedConnectionExtendedPartitionNumber_Type()
)
basicDiskExtendedConnectionExtendedPartitionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionExtendedPartitionNumber.setStatus("mandatory")
_BasicDiskExtendedConnectionPartitionName_Type = DisplayString
_BasicDiskExtendedConnectionPartitionName_Object = MibTableColumn
basicDiskExtendedConnectionPartitionName = _BasicDiskExtendedConnectionPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 10),
    _BasicDiskExtendedConnectionPartitionName_Type()
)
basicDiskExtendedConnectionPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionPartitionName.setStatus("mandatory")
_BasicDiskExtendedConnectionPartitionNumber_Type = Integer32
_BasicDiskExtendedConnectionPartitionNumber_Object = MibTableColumn
basicDiskExtendedConnectionPartitionNumber = _BasicDiskExtendedConnectionPartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 11),
    _BasicDiskExtendedConnectionPartitionNumber_Type()
)
basicDiskExtendedConnectionPartitionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionPartitionNumber.setStatus("mandatory")
_BasicDiskExtendedConnectionVolumeDriveLetter_Type = DisplayString
_BasicDiskExtendedConnectionVolumeDriveLetter_Object = MibTableColumn
basicDiskExtendedConnectionVolumeDriveLetter = _BasicDiskExtendedConnectionVolumeDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 12),
    _BasicDiskExtendedConnectionVolumeDriveLetter_Type()
)
basicDiskExtendedConnectionVolumeDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionVolumeDriveLetter.setStatus("mandatory")
_BasicDiskExtendedConnectionVolumeNumber_Type = Integer32
_BasicDiskExtendedConnectionVolumeNumber_Object = MibTableColumn
basicDiskExtendedConnectionVolumeNumber = _BasicDiskExtendedConnectionVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 9, 1, 13),
    _BasicDiskExtendedConnectionVolumeNumber_Type()
)
basicDiskExtendedConnectionVolumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskExtendedConnectionVolumeNumber.setStatus("mandatory")
_BasicDiskNonExtendedConnectionTable_Object = MibTable
basicDiskNonExtendedConnectionTable = _BasicDiskNonExtendedConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10)
)
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionTable.setStatus("mandatory")
_BasicDiskNonExtendedConnectionEntry_Object = MibTableRow
basicDiskNonExtendedConnectionEntry = _BasicDiskNonExtendedConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1)
)
basicDiskNonExtendedConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "basicDiskNonExtendedConnectionNumber"),
)
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionEntry.setStatus("mandatory")


class _BasicDiskNonExtendedConnectionNumber_Type(Integer32):
    """Custom type basicDiskNonExtendedConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_BasicDiskNonExtendedConnectionNumber_Type.__name__ = "Integer32"
_BasicDiskNonExtendedConnectionNumber_Object = MibTableColumn
basicDiskNonExtendedConnectionNumber = _BasicDiskNonExtendedConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 1),
    _BasicDiskNonExtendedConnectionNumber_Type()
)
basicDiskNonExtendedConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionNumber.setStatus("mandatory")
_BasicDiskNonExtendedConnectionArrayDiskName_Type = DisplayString
_BasicDiskNonExtendedConnectionArrayDiskName_Object = MibTableColumn
basicDiskNonExtendedConnectionArrayDiskName = _BasicDiskNonExtendedConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 2),
    _BasicDiskNonExtendedConnectionArrayDiskName_Type()
)
basicDiskNonExtendedConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionArrayDiskName.setStatus("mandatory")
_BasicDiskNonExtendedConnectionArrayDiskNumber_Type = Integer32
_BasicDiskNonExtendedConnectionArrayDiskNumber_Object = MibTableColumn
basicDiskNonExtendedConnectionArrayDiskNumber = _BasicDiskNonExtendedConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 3),
    _BasicDiskNonExtendedConnectionArrayDiskNumber_Type()
)
basicDiskNonExtendedConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionArrayDiskNumber.setStatus("mandatory")
_BasicDiskNonExtendedConnectionVirtualDiskName_Type = DisplayString
_BasicDiskNonExtendedConnectionVirtualDiskName_Object = MibTableColumn
basicDiskNonExtendedConnectionVirtualDiskName = _BasicDiskNonExtendedConnectionVirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 4),
    _BasicDiskNonExtendedConnectionVirtualDiskName_Type()
)
basicDiskNonExtendedConnectionVirtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionVirtualDiskName.setStatus("mandatory")
_BasicDiskNonExtendedConnectionVirtualDiskNumber_Type = Integer32
_BasicDiskNonExtendedConnectionVirtualDiskNumber_Object = MibTableColumn
basicDiskNonExtendedConnectionVirtualDiskNumber = _BasicDiskNonExtendedConnectionVirtualDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 5),
    _BasicDiskNonExtendedConnectionVirtualDiskNumber_Type()
)
basicDiskNonExtendedConnectionVirtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionVirtualDiskNumber.setStatus("mandatory")
_BasicDiskNonExtendedConnectionDiskName_Type = DisplayString
_BasicDiskNonExtendedConnectionDiskName_Object = MibTableColumn
basicDiskNonExtendedConnectionDiskName = _BasicDiskNonExtendedConnectionDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 6),
    _BasicDiskNonExtendedConnectionDiskName_Type()
)
basicDiskNonExtendedConnectionDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionDiskName.setStatus("mandatory")
_BasicDiskNonExtendedConnectionDiskNumber_Type = Integer32
_BasicDiskNonExtendedConnectionDiskNumber_Object = MibTableColumn
basicDiskNonExtendedConnectionDiskNumber = _BasicDiskNonExtendedConnectionDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 7),
    _BasicDiskNonExtendedConnectionDiskNumber_Type()
)
basicDiskNonExtendedConnectionDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionDiskNumber.setStatus("mandatory")
_BasicDiskNonExtendedConnectionPartitionName_Type = DisplayString
_BasicDiskNonExtendedConnectionPartitionName_Object = MibTableColumn
basicDiskNonExtendedConnectionPartitionName = _BasicDiskNonExtendedConnectionPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 8),
    _BasicDiskNonExtendedConnectionPartitionName_Type()
)
basicDiskNonExtendedConnectionPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionPartitionName.setStatus("mandatory")
_BasicDiskNonExtendedConnectionPartitionNumber_Type = Integer32
_BasicDiskNonExtendedConnectionPartitionNumber_Object = MibTableColumn
basicDiskNonExtendedConnectionPartitionNumber = _BasicDiskNonExtendedConnectionPartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 9),
    _BasicDiskNonExtendedConnectionPartitionNumber_Type()
)
basicDiskNonExtendedConnectionPartitionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionPartitionNumber.setStatus("mandatory")
_BasicDiskNonExtendedConnectionVolumeDriveLetter_Type = DisplayString
_BasicDiskNonExtendedConnectionVolumeDriveLetter_Object = MibTableColumn
basicDiskNonExtendedConnectionVolumeDriveLetter = _BasicDiskNonExtendedConnectionVolumeDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 10),
    _BasicDiskNonExtendedConnectionVolumeDriveLetter_Type()
)
basicDiskNonExtendedConnectionVolumeDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionVolumeDriveLetter.setStatus("mandatory")
_BasicDiskNonExtendedConnectionVolumeNumber_Type = Integer32
_BasicDiskNonExtendedConnectionVolumeNumber_Object = MibTableColumn
basicDiskNonExtendedConnectionVolumeNumber = _BasicDiskNonExtendedConnectionVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 10, 1, 11),
    _BasicDiskNonExtendedConnectionVolumeNumber_Type()
)
basicDiskNonExtendedConnectionVolumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDiskNonExtendedConnectionVolumeNumber.setStatus("mandatory")
_DynamicDiskConnectionTable_Object = MibTable
dynamicDiskConnectionTable = _DynamicDiskConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11)
)
if mibBuilder.loadTexts:
    dynamicDiskConnectionTable.setStatus("mandatory")
_DynamicDiskConnectionEntry_Object = MibTableRow
dynamicDiskConnectionEntry = _DynamicDiskConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1)
)
dynamicDiskConnectionEntry.setIndexNames(
    (0, "ArrayManager-MIB", "dynamicDiskConnectionNumber"),
)
if mibBuilder.loadTexts:
    dynamicDiskConnectionEntry.setStatus("mandatory")


class _DynamicDiskConnectionNumber_Type(Integer32):
    """Custom type dynamicDiskConnectionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DynamicDiskConnectionNumber_Type.__name__ = "Integer32"
_DynamicDiskConnectionNumber_Object = MibTableColumn
dynamicDiskConnectionNumber = _DynamicDiskConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 1),
    _DynamicDiskConnectionNumber_Type()
)
dynamicDiskConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionNumber.setStatus("mandatory")
_DynamicDiskConnectionArrayDiskName_Type = DisplayString
_DynamicDiskConnectionArrayDiskName_Object = MibTableColumn
dynamicDiskConnectionArrayDiskName = _DynamicDiskConnectionArrayDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 2),
    _DynamicDiskConnectionArrayDiskName_Type()
)
dynamicDiskConnectionArrayDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionArrayDiskName.setStatus("mandatory")
_DynamicDiskConnectionArrayDiskNumber_Type = Integer32
_DynamicDiskConnectionArrayDiskNumber_Object = MibTableColumn
dynamicDiskConnectionArrayDiskNumber = _DynamicDiskConnectionArrayDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 3),
    _DynamicDiskConnectionArrayDiskNumber_Type()
)
dynamicDiskConnectionArrayDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionArrayDiskNumber.setStatus("mandatory")
_DynamicDiskConnectionVirtualDiskName_Type = DisplayString
_DynamicDiskConnectionVirtualDiskName_Object = MibTableColumn
dynamicDiskConnectionVirtualDiskName = _DynamicDiskConnectionVirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 4),
    _DynamicDiskConnectionVirtualDiskName_Type()
)
dynamicDiskConnectionVirtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionVirtualDiskName.setStatus("mandatory")
_DynamicDiskConnectionVirtualDiskNumber_Type = Integer32
_DynamicDiskConnectionVirtualDiskNumber_Object = MibTableColumn
dynamicDiskConnectionVirtualDiskNumber = _DynamicDiskConnectionVirtualDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 5),
    _DynamicDiskConnectionVirtualDiskNumber_Type()
)
dynamicDiskConnectionVirtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionVirtualDiskNumber.setStatus("mandatory")
_DynamicDiskConnectionDiskName_Type = DisplayString
_DynamicDiskConnectionDiskName_Object = MibTableColumn
dynamicDiskConnectionDiskName = _DynamicDiskConnectionDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 6),
    _DynamicDiskConnectionDiskName_Type()
)
dynamicDiskConnectionDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionDiskName.setStatus("mandatory")
_DynamicDiskConnectionDiskNumber_Type = Integer32
_DynamicDiskConnectionDiskNumber_Object = MibTableColumn
dynamicDiskConnectionDiskNumber = _DynamicDiskConnectionDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 7),
    _DynamicDiskConnectionDiskNumber_Type()
)
dynamicDiskConnectionDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionDiskNumber.setStatus("mandatory")
_DynamicDiskConnectionSubDiskName_Type = DisplayString
_DynamicDiskConnectionSubDiskName_Object = MibTableColumn
dynamicDiskConnectionSubDiskName = _DynamicDiskConnectionSubDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 8),
    _DynamicDiskConnectionSubDiskName_Type()
)
dynamicDiskConnectionSubDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionSubDiskName.setStatus("mandatory")
_DynamicDiskConnectionSubDiskNumber_Type = Integer32
_DynamicDiskConnectionSubDiskNumber_Object = MibTableColumn
dynamicDiskConnectionSubDiskNumber = _DynamicDiskConnectionSubDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 9),
    _DynamicDiskConnectionSubDiskNumber_Type()
)
dynamicDiskConnectionSubDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionSubDiskNumber.setStatus("mandatory")
_DynamicDiskConnectionPlexName_Type = DisplayString
_DynamicDiskConnectionPlexName_Object = MibTableColumn
dynamicDiskConnectionPlexName = _DynamicDiskConnectionPlexName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 10),
    _DynamicDiskConnectionPlexName_Type()
)
dynamicDiskConnectionPlexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionPlexName.setStatus("mandatory")
_DynamicDiskConnectionPlexNumber_Type = Integer32
_DynamicDiskConnectionPlexNumber_Object = MibTableColumn
dynamicDiskConnectionPlexNumber = _DynamicDiskConnectionPlexNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 11),
    _DynamicDiskConnectionPlexNumber_Type()
)
dynamicDiskConnectionPlexNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicDiskConnectionPlexNumber.setStatus("mandatory")
_DynamicDiskConnectionVolumeDriveLetter_Type = DisplayString
_DynamicDiskConnectionVolumeDriveLetter_Object = MibTableColumn
dynamicDiskConnectionVolumeDriveLetter = _DynamicDiskConnectionVolumeDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 12),
    _DynamicDiskConnectionVolumeDriveLetter_Type()
)
dynamicDiskConnectionVolumeDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionVolumeDriveLetter.setStatus("mandatory")
_DynamicDiskConnectionVolumeNumber_Type = Integer32
_DynamicDiskConnectionVolumeNumber_Object = MibTableColumn
dynamicDiskConnectionVolumeNumber = _DynamicDiskConnectionVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 140, 11, 1, 13),
    _DynamicDiskConnectionVolumeNumber_Type()
)
dynamicDiskConnectionVolumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicDiskConnectionVolumeNumber.setStatus("mandatory")
_AryMgrEvts_ObjectIdentity = ObjectIdentity
aryMgrEvts = _AryMgrEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200)
)


class _ControllerNameEv_Type(DisplayString):
    """Custom type controllerNameEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ControllerNameEv_Type.__name__ = "DisplayString"
_ControllerNameEv_Object = MibScalar
controllerNameEv = _ControllerNameEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 201),
    _ControllerNameEv_Type()
)
controllerNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNameEv.setStatus("mandatory")


class _ChannelNumberEv_Type(Integer32):
    """Custom type channelNumberEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ChannelNumberEv_Type.__name__ = "Integer32"
_ChannelNumberEv_Object = MibScalar
channelNumberEv = _ChannelNumberEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 202),
    _ChannelNumberEv_Type()
)
channelNumberEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumberEv.setStatus("mandatory")


class _TargetIDEv_Type(Integer32):
    """Custom type targetIDEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TargetIDEv_Type.__name__ = "Integer32"
_TargetIDEv_Object = MibScalar
targetIDEv = _TargetIDEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 203),
    _TargetIDEv_Type()
)
targetIDEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetIDEv.setStatus("mandatory")


class _VirtualDiskNameEv_Type(DisplayString):
    """Custom type virtualDiskNameEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VirtualDiskNameEv_Type.__name__ = "DisplayString"
_VirtualDiskNameEv_Object = MibScalar
virtualDiskNameEv = _VirtualDiskNameEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 204),
    _VirtualDiskNameEv_Type()
)
virtualDiskNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskNameEv.setStatus("mandatory")


class _ArrayDiskNameEv_Type(DisplayString):
    """Custom type arrayDiskNameEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ArrayDiskNameEv_Type.__name__ = "DisplayString"
_ArrayDiskNameEv_Object = MibScalar
arrayDiskNameEv = _ArrayDiskNameEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 205),
    _ArrayDiskNameEv_Type()
)
arrayDiskNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskNameEv.setStatus("mandatory")


class _OldVDConfigEv_Type(DisplayString):
    """Custom type oldVDConfigEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OldVDConfigEv_Type.__name__ = "DisplayString"
_OldVDConfigEv_Object = MibScalar
oldVDConfigEv = _OldVDConfigEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 206),
    _OldVDConfigEv_Type()
)
oldVDConfigEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldVDConfigEv.setStatus("mandatory")


class _NewVDConfigEv_Type(DisplayString):
    """Custom type newVDConfigEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_NewVDConfigEv_Type.__name__ = "DisplayString"
_NewVDConfigEv_Object = MibScalar
newVDConfigEv = _NewVDConfigEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 207),
    _NewVDConfigEv_Type()
)
newVDConfigEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newVDConfigEv.setStatus("mandatory")
_EnclosureNumberEv_Type = Integer32
_EnclosureNumberEv_Object = MibScalar
enclosureNumberEv = _EnclosureNumberEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 208),
    _EnclosureNumberEv_Type()
)
enclosureNumberEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNumberEv.setStatus("mandatory")
_UnitNumberEv_Type = Integer32
_UnitNumberEv_Object = MibScalar
unitNumberEv = _UnitNumberEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 209),
    _UnitNumberEv_Type()
)
unitNumberEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitNumberEv.setStatus("mandatory")
_EnclosureNameEv_Type = DisplayString
_EnclosureNameEv_Object = MibScalar
enclosureNameEv = _EnclosureNameEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 210),
    _EnclosureNameEv_Type()
)
enclosureNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNameEv.setStatus("mandatory")
_UnitNameEv_Type = DisplayString
_UnitNameEv_Object = MibScalar
unitNameEv = _UnitNameEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 211),
    _UnitNameEv_Type()
)
unitNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitNameEv.setStatus("mandatory")
_TimeEv_Type = Integer32
_TimeEv_Object = MibScalar
timeEv = _TimeEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 212),
    _TimeEv_Type()
)
timeEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeEv.setStatus("mandatory")
_VolumeNameEv_Type = DisplayString
_VolumeNameEv_Object = MibScalar
volumeNameEv = _VolumeNameEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 213),
    _VolumeNameEv_Type()
)
volumeNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNameEv.setStatus("mandatory")
_EnclosureUnitNamesEv_Type = DisplayString
_EnclosureUnitNamesEv_Object = MibScalar
enclosureUnitNamesEv = _EnclosureUnitNamesEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 214),
    _EnclosureUnitNamesEv_Type()
)
enclosureUnitNamesEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureUnitNamesEv.setStatus("mandatory")
_VirtualDiskNameNewEv_Type = DisplayString
_VirtualDiskNameNewEv_Object = MibScalar
virtualDiskNameNewEv = _VirtualDiskNameNewEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 215),
    _VirtualDiskNameNewEv_Type()
)
virtualDiskNameNewEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskNameNewEv.setStatus("mandatory")
_Device1NameEv_Type = DisplayString
_Device1NameEv_Object = MibScalar
device1NameEv = _Device1NameEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 216),
    _Device1NameEv_Type()
)
device1NameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device1NameEv.setStatus("mandatory")
_SenseKeyEv_Type = DisplayString
_SenseKeyEv_Object = MibScalar
senseKeyEv = _SenseKeyEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 217),
    _SenseKeyEv_Type()
)
senseKeyEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senseKeyEv.setStatus("mandatory")
_SenseCodeEv_Type = DisplayString
_SenseCodeEv_Object = MibScalar
senseCodeEv = _SenseCodeEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 218),
    _SenseCodeEv_Type()
)
senseCodeEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senseCodeEv.setStatus("mandatory")
_SenseQualifierEv_Type = DisplayString
_SenseQualifierEv_Object = MibScalar
senseQualifierEv = _SenseQualifierEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 219),
    _SenseQualifierEv_Type()
)
senseQualifierEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senseQualifierEv.setStatus("mandatory")
_EMMFWVersion0Ev_Type = DisplayString
_EMMFWVersion0Ev_Object = MibScalar
eMMFWVersion0Ev = _EMMFWVersion0Ev_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 220),
    _EMMFWVersion0Ev_Type()
)
eMMFWVersion0Ev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMMFWVersion0Ev.setStatus("mandatory")
_EMMFWVersion1Ev_Type = DisplayString
_EMMFWVersion1Ev_Object = MibScalar
eMMFWVersion1Ev = _EMMFWVersion1Ev_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 221),
    _EMMFWVersion1Ev_Type()
)
eMMFWVersion1Ev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMMFWVersion1Ev.setStatus("mandatory")
_RebuildRateEv_Type = DisplayString
_RebuildRateEv_Object = MibScalar
rebuildRateEv = _RebuildRateEv_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 222),
    _RebuildRateEv_Type()
)
rebuildRateEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rebuildRateEv.setStatus("mandatory")

# Managed Objects groups


# Notification objects

arrayDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 500)
)
arrayDiskFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    arrayDiskFailed.setStatus(
        ""
    )

arrayDiskRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 501)
)
arrayDiskRemoved.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    arrayDiskRemoved.setStatus(
        ""
    )

arrayDiskOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 502)
)
arrayDiskOffline.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    arrayDiskOffline.setStatus(
        ""
    )

arrayDiskDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 503)
)
arrayDiskDegraded.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    arrayDiskDegraded.setStatus(
        ""
    )

arrayDiskInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 504)
)
arrayDiskInserted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    arrayDiskInserted.setStatus(
        ""
    )

virtualDiskCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 505)
)
virtualDiskCreated.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    virtualDiskCreated.setStatus(
        ""
    )

virtualDiskDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 506)
)
virtualDiskDeleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    virtualDiskDeleted.setStatus(
        ""
    )

virtualDiskConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 507)
)
virtualDiskConfigChanged.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"),
        ("ArrayManager-MIB", "oldVDConfigEv"),
        ("ArrayManager-MIB", "newVDConfigEv"))
)
if mibBuilder.loadTexts:
    virtualDiskConfigChanged.setStatus(
        ""
    )

virtualDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 508)
)
virtualDiskFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    virtualDiskFailed.setStatus(
        ""
    )

virtualDiskDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 509)
)
virtualDiskDegraded.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    virtualDiskDegraded.setStatus(
        ""
    )

vdFailedRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 510)
)
vdFailedRedundancy.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdFailedRedundancy.setStatus(
        ""
    )

checkConsistencyStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 520)
)
checkConsistencyStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    checkConsistencyStarted.setStatus(
        ""
    )

vdFormatStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 521)
)
vdFormatStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdFormatStarted.setStatus(
        ""
    )

adFormatStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 522)
)
adFormatStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adFormatStarted.setStatus(
        ""
    )

vdInitializeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 523)
)
vdInitializeStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdInitializeStarted.setStatus(
        ""
    )

adInitializeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 524)
)
adInitializeStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adInitializeStarted.setStatus(
        ""
    )

vdReconfigStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 525)
)
vdReconfigStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"),
        ("ArrayManager-MIB", "oldVDConfigEv"),
        ("ArrayManager-MIB", "newVDConfigEv"))
)
if mibBuilder.loadTexts:
    vdReconfigStarted.setStatus(
        ""
    )

vdRebuildStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 526)
)
vdRebuildStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdRebuildStarted.setStatus(
        ""
    )

adRebuildStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 527)
)
adRebuildStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adRebuildStarted.setStatus(
        ""
    )

adDiagStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 528)
)
adDiagStarted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adDiagStarted.setStatus(
        ""
    )

checkConsistencyCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 529)
)
checkConsistencyCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    checkConsistencyCancelled.setStatus(
        ""
    )

vdFormatCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 530)
)
vdFormatCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdFormatCancelled.setStatus(
        ""
    )

adFormatCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 531)
)
adFormatCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adFormatCancelled.setStatus(
        ""
    )

vdInitializeCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 532)
)
vdInitializeCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdInitializeCancelled.setStatus(
        ""
    )

adInitializeCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 533)
)
adInitializeCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adInitializeCancelled.setStatus(
        ""
    )

vdReconfigCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 534)
)
vdReconfigCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdReconfigCancelled.setStatus(
        ""
    )

vdRebuildCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 535)
)
vdRebuildCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdRebuildCancelled.setStatus(
        ""
    )

adRebuildCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 536)
)
adRebuildCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adRebuildCancelled.setStatus(
        ""
    )

adDiagCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 537)
)
adDiagCancelled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adDiagCancelled.setStatus(
        ""
    )

checkConsistencyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 538)
)
checkConsistencyFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    checkConsistencyFailed.setStatus(
        ""
    )

vdFormatFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 539)
)
vdFormatFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdFormatFailed.setStatus(
        ""
    )

adFormatFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 540)
)
adFormatFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adFormatFailed.setStatus(
        ""
    )

vdInitializeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 541)
)
vdInitializeFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdInitializeFailed.setStatus(
        ""
    )

adInitializeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 542)
)
adInitializeFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adInitializeFailed.setStatus(
        ""
    )

vdReconfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 543)
)
vdReconfigFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdReconfigFailed.setStatus(
        ""
    )

vdRebuildFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 544)
)
vdRebuildFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdRebuildFailed.setStatus(
        ""
    )

adRebuildFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 545)
)
adRebuildFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adRebuildFailed.setStatus(
        ""
    )

adDiagFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 546)
)
adDiagFailed.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adDiagFailed.setStatus(
        ""
    )

checkConsistencyCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 547)
)
checkConsistencyCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    checkConsistencyCompleted.setStatus(
        ""
    )

vdFormatCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 548)
)
vdFormatCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdFormatCompleted.setStatus(
        ""
    )

adFormatCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 549)
)
adFormatCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adFormatCompleted.setStatus(
        ""
    )

vdInitializeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 550)
)
vdInitializeCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdInitializeCompleted.setStatus(
        ""
    )

adInitializeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 551)
)
adInitializeCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adInitializeCompleted.setStatus(
        ""
    )

vdReconfigCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 552)
)
vdReconfigCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdReconfigCompleted.setStatus(
        ""
    )

vdRebuildCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 553)
)
vdRebuildCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    vdRebuildCompleted.setStatus(
        ""
    )

adRebuildCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 554)
)
adRebuildCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adRebuildCompleted.setStatus(
        ""
    )

adDiagCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 555)
)
adDiagCompleted.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    adDiagCompleted.setStatus(
        ""
    )

percPredictiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 570)
)
percPredictiveFailure.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    percPredictiveFailure.setStatus(
        ""
    )

percSCSISenseData = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 571)
)
percSCSISenseData.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    percSCSISenseData.setStatus(
        ""
    )

percPauseIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 572)
)
percPauseIO.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "timeEv"))
)
if mibBuilder.loadTexts:
    percPauseIO.setStatus(
        ""
    )

percResumeIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 573)
)
percResumeIO.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    percResumeIO.setStatus(
        ""
    )

percHotSpareAssign = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 574)
)
percHotSpareAssign.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    percHotSpareAssign.setStatus(
        ""
    )

percHotSpareUnAssign = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 575)
)
percHotSpareUnAssign.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    percHotSpareUnAssign.setStatus(
        ""
    )

cntrlBatteryNeedsReconditioning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 579)
)
cntrlBatteryNeedsReconditioning.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    cntrlBatteryNeedsReconditioning.setStatus(
        ""
    )

cntrlBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 580)
)
cntrlBatteryLow.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    cntrlBatteryLow.setStatus(
        ""
    )

cntrlBatteryRecondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 581)
)
cntrlBatteryRecondition.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    cntrlBatteryRecondition.setStatus(
        ""
    )

cntrlBatteryReconComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 582)
)
cntrlBatteryReconComplete.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    cntrlBatteryReconComplete.setStatus(
        ""
    )

cntrlPauseIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 583)
)
cntrlPauseIO.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    cntrlPauseIO.setStatus(
        ""
    )

cntrlResumeIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 584)
)
cntrlResumeIO.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    cntrlResumeIO.setStatus(
        ""
    )

perc2SmartFPTExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 585)
)
perc2SmartFPTExceeded.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    perc2SmartFPTExceeded.setStatus(
        ""
    )

perc2SmartConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 586)
)
perc2SmartConfigChange.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    perc2SmartConfigChange.setStatus(
        ""
    )

perc2SmartWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 587)
)
perc2SmartWarning.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    perc2SmartWarning.setStatus(
        ""
    )

perc2SmartWarningTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 588)
)
perc2SmartWarningTemp.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    perc2SmartWarningTemp.setStatus(
        ""
    )

perc2SmartWarningDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 589)
)
perc2SmartWarningDegraded.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    perc2SmartWarningDegraded.setStatus(
        ""
    )

perc2SmartFPTExceededTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 590)
)
perc2SmartFPTExceededTest.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    perc2SmartFPTExceededTest.setStatus(
        ""
    )

enclosureAlertTempWarnMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 591)
)
enclosureAlertTempWarnMax.setObjects(
      *(("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "unitNameEv"))
)
if mibBuilder.loadTexts:
    enclosureAlertTempWarnMax.setStatus(
        ""
    )

enclosureAlertTempWarnMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 592)
)
enclosureAlertTempWarnMin.setObjects(
      *(("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "unitNameEv"))
)
if mibBuilder.loadTexts:
    enclosureAlertTempWarnMin.setStatus(
        ""
    )

enclosureAlertTempErrMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 593)
)
enclosureAlertTempErrMax.setObjects(
      *(("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "unitNameEv"))
)
if mibBuilder.loadTexts:
    enclosureAlertTempErrMax.setStatus(
        ""
    )

enclosureAlertTempErrMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 594)
)
enclosureAlertTempErrMin.setObjects(
      *(("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "unitNameEv"))
)
if mibBuilder.loadTexts:
    enclosureAlertTempErrMin.setStatus(
        ""
    )

enclosureGenericFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 595)
)
enclosureGenericFailed.setObjects(
      *(("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "unitNameEv"))
)
if mibBuilder.loadTexts:
    enclosureGenericFailed.setStatus(
        ""
    )

enclosureGenericOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 596)
)
enclosureGenericOffline.setObjects(
      *(("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "unitNameEv"))
)
if mibBuilder.loadTexts:
    enclosureGenericOffline.setStatus(
        ""
    )

enclosureGenericUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 597)
)
enclosureGenericUnknown.setObjects(
      *(("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "unitNameEv"))
)
if mibBuilder.loadTexts:
    enclosureGenericUnknown.setStatus(
        ""
    )

enclosureGenericWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 598)
)
enclosureGenericWarning.setObjects(
      *(("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "unitNameEv"))
)
if mibBuilder.loadTexts:
    enclosureGenericWarning.setStatus(
        ""
    )

enclosureGenericDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 600)
)
enclosureGenericDegraded.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureUnitNamesEv"))
)
if mibBuilder.loadTexts:
    enclosureGenericDegraded.setStatus(
        ""
    )

alertShutdownEnclosure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 602)
)
alertShutdownEnclosure.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNameEv"))
)
if mibBuilder.loadTexts:
    alertShutdownEnclosure.setStatus(
        ""
    )

alertShutdownServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 603)
)
alertShutdownServer.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNameEv"))
)
if mibBuilder.loadTexts:
    alertShutdownServer.setStatus(
        ""
    )

alertPausedCheckConsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 604)
)
alertPausedCheckConsistency.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertPausedCheckConsistency.setStatus(
        ""
    )

alertResumedCheckConsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 605)
)
alertResumedCheckConsistency.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertResumedCheckConsistency.setStatus(
        ""
    )

alertVirtualDiskSplitMirror = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 606)
)
alertVirtualDiskSplitMirror.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskSplitMirror.setStatus(
        ""
    )

alertVirtualDiskUnmirror = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 607)
)
alertVirtualDiskUnmirror.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertVirtualDiskUnmirror.setStatus(
        ""
    )

alertRenameVirtualDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 608)
)
alertRenameVirtualDisk.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameNewEv"))
)
if mibBuilder.loadTexts:
    alertRenameVirtualDisk.setStatus(
        ""
    )

alertGenericReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 609)
)
alertGenericReady.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "device1NameEv"))
)
if mibBuilder.loadTexts:
    alertGenericReady.setStatus(
        ""
    )

alertCommTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 610)
)
alertCommTimeout.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "device1NameEv"))
)
if mibBuilder.loadTexts:
    alertCommTimeout.setStatus(
        ""
    )

alertCommFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 611)
)
alertCommFailure.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "device1NameEv"))
)
if mibBuilder.loadTexts:
    alertCommFailure.setStatus(
        ""
    )

alertCommRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 612)
)
alertCommRestored.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "device1NameEv"))
)
if mibBuilder.loadTexts:
    alertCommRestored.setStatus(
        ""
    )

genericEvent_DATABASE_UP = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 650)
)
if mibBuilder.loadTexts:
    genericEvent_DATABASE_UP.setStatus(
        ""
    )

genericEvent_DATABASE_DOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 651)
)
if mibBuilder.loadTexts:
    genericEvent_DATABASE_DOWN.setStatus(
        ""
    )

alertMegalibTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 668)
)
alertMegalibTimeout.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    alertMegalibTimeout.setStatus(
        ""
    )

alertScsiSenseFormatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 670)
)
alertScsiSenseFormatFail.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"),
        ("ArrayManager-MIB", "senseKeyEv"),
        ("ArrayManager-MIB", "senseCodeEv"),
        ("ArrayManager-MIB", "senseQualifierEv"))
)
if mibBuilder.loadTexts:
    alertScsiSenseFormatFail.setStatus(
        ""
    )

alertScsiSenseSectorReassign = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 671)
)
alertScsiSenseSectorReassign.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"),
        ("ArrayManager-MIB", "senseKeyEv"),
        ("ArrayManager-MIB", "senseCodeEv"),
        ("ArrayManager-MIB", "senseQualifierEv"))
)
if mibBuilder.loadTexts:
    alertScsiSenseSectorReassign.setStatus(
        ""
    )

alertEmmFwMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 672)
)
alertEmmFwMismatch.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "eMMFWVersion0Ev"),
        ("ArrayManager-MIB", "eMMFWVersion1Ev"))
)
if mibBuilder.loadTexts:
    alertEmmFwMismatch.setStatus(
        ""
    )

alertConserveCacheModeEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 673)
)
alertConserveCacheModeEnable.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNameEv"))
)
if mibBuilder.loadTexts:
    alertConserveCacheModeEnable.setStatus(
        ""
    )

alertConserveCacheModeDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 674)
)
alertConserveCacheModeDisable.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNameEv"))
)
if mibBuilder.loadTexts:
    alertConserveCacheModeDisable.setStatus(
        ""
    )

alertEnclosureFwDownload = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 675)
)
alertEnclosureFwDownload.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNameEv"),
        ("ArrayManager-MIB", "eMMFWVersion0Ev"))
)
if mibBuilder.loadTexts:
    alertEnclosureFwDownload.setStatus(
        ""
    )

alertEnclosureAlarmEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 676)
)
alertEnclosureAlarmEnable.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNameEv"))
)
if mibBuilder.loadTexts:
    alertEnclosureAlarmEnable.setStatus(
        ""
    )

alertEnclosureAlarmDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 677)
)
alertEnclosureAlarmDisable.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNameEv"))
)
if mibBuilder.loadTexts:
    alertEnclosureAlarmDisable.setStatus(
        ""
    )

alertControllerAlarmEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 678)
)
alertControllerAlarmEnable.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    alertControllerAlarmEnable.setStatus(
        ""
    )

alertControllerAlarmDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 679)
)
alertControllerAlarmDisable.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    alertControllerAlarmDisable.setStatus(
        ""
    )

alertControllerRebuildRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 680)
)
alertControllerRebuildRate.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "rebuildRateEv"))
)
if mibBuilder.loadTexts:
    alertControllerRebuildRate.setStatus(
        ""
    )

alertArrayDiskForcedOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 681)
)
alertArrayDiskForcedOnline.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertArrayDiskForcedOnline.setStatus(
        ""
    )

alertArrayDiskForcedOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 682)
)
alertArrayDiskForcedOffline.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "arrayDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertArrayDiskForcedOffline.setStatus(
        ""
    )

alertTaskBGI = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 683)
)
alertTaskBGI.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertTaskBGI.setStatus(
        ""
    )

alertCancelBGI = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 684)
)
alertCancelBGI.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertCancelBGI.setStatus(
        ""
    )

alertFailBGI = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 685)
)
alertFailBGI.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertFailBGI.setStatus(
        ""
    )

alertCompleteBGI = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 686)
)
alertCompleteBGI.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    alertCompleteBGI.setStatus(
        ""
    )

enclosureGenericNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 687)
)
enclosureGenericNotInstalled.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureUnitNamesEv"))
)
if mibBuilder.loadTexts:
    enclosureGenericNotInstalled.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_ONLINE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 700)
)
pv660fEvent_PHYSDEV_ONLINE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_ONLINE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_HOTSPARE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 701)
)
pv660fEvent_PHYSDEV_HOTSPARE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_HOTSPARE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_HARD_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 702)
)
pv660fEvent_PHYSDEV_HARD_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_HARD_ERROR.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_PFA = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 703)
)
pv660fEvent_PHYSDEV_PFA.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_PFA.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_AUTO_REBUILD_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 704)
)
pv660fEvent_PHYSDEV_AUTO_REBUILD_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_AUTO_REBUILD_START.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_MANUAL_REBUILD_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 705)
)
pv660fEvent_PHYSDEV_MANUAL_REBUILD_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_MANUAL_REBUILD_START.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REBUILD_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 706)
)
pv660fEvent_PHYSDEV_REBUILD_DONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REBUILD_DONE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REBUILD_CANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 707)
)
pv660fEvent_PHYSDEV_REBUILD_CANCELED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REBUILD_CANCELED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REBUILD_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 708)
)
pv660fEvent_PHYSDEV_REBUILD_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REBUILD_ERROR.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REBUILD_NEWDEV_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 709)
)
pv660fEvent_PHYSDEV_REBUILD_NEWDEV_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REBUILD_NEWDEV_FAILED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REBUILD_SYSDEV_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 710)
)
pv660fEvent_PHYSDEV_REBUILD_SYSDEV_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REBUILD_SYSDEV_FAILED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 711)
)
pv660fEvent_PHYSDEV_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_FOUND = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 712)
)
pv660fEvent_PHYSDEV_FOUND.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_FOUND.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_GONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 713)
)
pv660fEvent_PHYSDEV_GONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_GONE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_UNCONFIGURED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 714)
)
pv660fEvent_PHYSDEV_UNCONFIGURED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_UNCONFIGURED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_EXPANDCAPACITY_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 715)
)
pv660fEvent_PHYSDEV_EXPANDCAPACITY_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_EXPANDCAPACITY_START.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_EXPANDCAPACITY_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 716)
)
pv660fEvent_PHYSDEV_EXPANDCAPACITY_DONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_EXPANDCAPACITY_DONE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_EXPANDCAPACITY_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 717)
)
pv660fEvent_PHYSDEV_EXPANDCAPACITY_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_EXPANDCAPACITY_ERROR.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_COMMAND_TIMEOUT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 718)
)
pv660fEvent_PHYSDEV_COMMAND_TIMEOUT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_COMMAND_TIMEOUT.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_COMMAND_ABORT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 719)
)
pv660fEvent_PHYSDEV_COMMAND_ABORT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_COMMAND_ABORT.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_COMMAND_RETRIED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 720)
)
pv660fEvent_PHYSDEV_COMMAND_RETRIED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_COMMAND_RETRIED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_PARITY_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 721)
)
pv660fEvent_PHYSDEV_PARITY_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_PARITY_ERROR.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_SOFT_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 722)
)
pv660fEvent_PHYSDEV_SOFT_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_SOFT_ERROR.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_MISC_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 723)
)
pv660fEvent_PHYSDEV_MISC_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_MISC_ERROR.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_RESET = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 724)
)
pv660fEvent_PHYSDEV_RESET.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_RESET.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_ACTIVESPARE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 725)
)
pv660fEvent_PHYSDEV_ACTIVESPARE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_ACTIVESPARE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_WARMSPARE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 726)
)
pv660fEvent_PHYSDEV_WARMSPARE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_WARMSPARE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REQSENSE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 727)
)
pv660fEvent_PHYSDEV_REQSENSE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REQSENSE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_INIT_STARTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 728)
)
pv660fEvent_PHYSDEV_INIT_STARTED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_INIT_STARTED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_INIT_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 729)
)
pv660fEvent_PHYSDEV_INIT_DONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_INIT_DONE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_INIT_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 730)
)
pv660fEvent_PHYSDEV_INIT_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_INIT_FAILED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_INIT_CANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 731)
)
pv660fEvent_PHYSDEV_INIT_CANCELED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_INIT_CANCELED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_WRITEREC_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 732)
)
pv660fEvent_PHYSDEV_WRITEREC_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_WRITEREC_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_RESET_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 733)
)
pv660fEvent_PHYSDEV_RESET_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_RESET_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_DBLCC_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 734)
)
pv660fEvent_PHYSDEV_DBLCC_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_DBLCC_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REMOVED_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 735)
)
pv660fEvent_PHYSDEV_REMOVED_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REMOVED_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_GROSSERR_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 736)
)
pv660fEvent_PHYSDEV_GROSSERR_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_GROSSERR_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_BADTAG_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 737)
)
pv660fEvent_PHYSDEV_BADTAG_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_BADTAG_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_SCSITMO_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 738)
)
pv660fEvent_PHYSDEV_SCSITMO_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_SCSITMO_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_SYSRESET_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 739)
)
pv660fEvent_PHYSDEV_SYSRESET_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_SYSRESET_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_BSYPAR_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 740)
)
pv660fEvent_PHYSDEV_BSYPAR_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_BSYPAR_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_BYCMD_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 741)
)
pv660fEvent_PHYSDEV_BYCMD_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_BYCMD_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_SELTMO_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 742)
)
pv660fEvent_PHYSDEV_SELTMO_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_SELTMO_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_SEQERR_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 743)
)
pv660fEvent_PHYSDEV_SEQERR_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_SEQERR_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_UNKNOWNSTS_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 744)
)
pv660fEvent_PHYSDEV_UNKNOWNSTS_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_UNKNOWNSTS_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_NOTRDY_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 745)
)
pv660fEvent_PHYSDEV_NOTRDY_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_NOTRDY_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_MISSING_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 746)
)
pv660fEvent_PHYSDEV_MISSING_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_MISSING_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_CODWRFAIL_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 747)
)
pv660fEvent_PHYSDEV_CODWRFAIL_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_CODWRFAIL_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_BDTWRFAIL_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 748)
)
pv660fEvent_PHYSDEV_BDTWRFAIL_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_BDTWRFAIL_DEAD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_OFFLINE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 749)
)
pv660fEvent_PHYSDEV_OFFLINE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_OFFLINE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_STANDBY = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 750)
)
pv660fEvent_PHYSDEV_STANDBY.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_STANDBY.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REBUILD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 751)
)
pv660fEvent_PHYSDEV_REBUILD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REBUILD.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_ID_MISMATCH = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 752)
)
pv660fEvent_PHYSDEV_ID_MISMATCH.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_ID_MISMATCH.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_FAILED_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 753)
)
pv660fEvent_PHYSDEV_FAILED_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_FAILED_START.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_OFFSET_SET = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 754)
)
pv660fEvent_PHYSDEV_OFFSET_SET.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_OFFSET_SET.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_SET_BUS_WIDTH = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 755)
)
pv660fEvent_PHYSDEV_SET_BUS_WIDTH.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_SET_BUS_WIDTH.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_MISSING_ONSTARTUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 756)
)
pv660fEvent_PHYSDEV_MISSING_ONSTARTUP.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_MISSING_ONSTARTUP.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_REBUILD_START_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 757)
)
pv660fEvent_PHYSDEV_REBUILD_START_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_REBUILD_START_FAILED.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_MOVING_TO_OTHER_CHN = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 758)
)
pv660fEvent_PHYSDEV_MOVING_TO_OTHER_CHN.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_MOVING_TO_OTHER_CHN.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_OFFLINE_DEVICE_MADE_ONLINE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 759)
)
pv660fEvent_PHYSDEV_OFFLINE_DEVICE_MADE_ONLINE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_OFFLINE_DEVICE_MADE_ONLINE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_STANDBY_REBUILD_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 760)
)
pv660fEvent_PHYSDEV_STANDBY_REBUILD_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_STANDBY_REBUILD_START.setStatus(
        ""
    )

pv660fEvent_FIBREDEV_LOOPID_SOFTADDR_OCCURRED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 761)
)
pv660fEvent_FIBREDEV_LOOPID_SOFTADDR_OCCURRED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_FIBREDEV_LOOPID_SOFTADDR_OCCURRED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_CHECK_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 762)
)
pv660fEvent_SYSDEV_CHECK_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_CHECK_START.setStatus(
        ""
    )

pv660fEvent_SYSDEV_CHECK_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 763)
)
pv660fEvent_SYSDEV_CHECK_DONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_CHECK_DONE.setStatus(
        ""
    )

pv660fEvent_SYSDEV_CHECK_CANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 764)
)
pv660fEvent_SYSDEV_CHECK_CANCELED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_CHECK_CANCELED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_CHECK_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 765)
)
pv660fEvent_SYSDEV_CHECK_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_CHECK_ERROR.setStatus(
        ""
    )

pv660fEvent_SYSDEV_CHECK_SYSDEV_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 766)
)
pv660fEvent_SYSDEV_CHECK_SYSDEV_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_CHECK_SYSDEV_FAILED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_CHECK_PHYSDEV_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 767)
)
pv660fEvent_SYSDEV_CHECK_PHYSDEV_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_CHECK_PHYSDEV_FAILED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_OFFLINE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 768)
)
pv660fEvent_SYSDEV_OFFLINE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_OFFLINE.setStatus(
        ""
    )

pv660fEvent_SYSDEV_CRITICAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 769)
)
pv660fEvent_SYSDEV_CRITICAL.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_CRITICAL.setStatus(
        ""
    )

pv660fEvent_SYSDEV_ONLINE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 770)
)
pv660fEvent_SYSDEV_ONLINE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_ONLINE.setStatus(
        ""
    )

pv660fEvent_SYSDEV_AUTO_REBUILD_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 771)
)
pv660fEvent_SYSDEV_AUTO_REBUILD_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_AUTO_REBUILD_START.setStatus(
        ""
    )

pv660fEvent_SYSDEV_MANUAL_REBUILD_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 772)
)
pv660fEvent_SYSDEV_MANUAL_REBUILD_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_MANUAL_REBUILD_START.setStatus(
        ""
    )

pv660fEvent_SYSDEV_REBUILD_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 773)
)
pv660fEvent_SYSDEV_REBUILD_DONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_REBUILD_DONE.setStatus(
        ""
    )

pv660fEvent_SYSDEV_REBUILD_CANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 774)
)
pv660fEvent_SYSDEV_REBUILD_CANCELED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_REBUILD_CANCELED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_REBUILD_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 775)
)
pv660fEvent_SYSDEV_REBUILD_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_REBUILD_ERROR.setStatus(
        ""
    )

pv660fEvent_SYSDEV_REBUILD_NEWDEV_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 776)
)
pv660fEvent_SYSDEV_REBUILD_NEWDEV_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_REBUILD_NEWDEV_FAILED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_REBUILD_SYSDEV_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 777)
)
pv660fEvent_SYSDEV_REBUILD_SYSDEV_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_REBUILD_SYSDEV_FAILED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_INIT_STARTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 778)
)
pv660fEvent_SYSDEV_INIT_STARTED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_INIT_STARTED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_INIT_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 779)
)
pv660fEvent_SYSDEV_INIT_DONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_INIT_DONE.setStatus(
        ""
    )

pv660fEvent_SYSDEV_INIT_CANCELED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 780)
)
pv660fEvent_SYSDEV_INIT_CANCELED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_INIT_CANCELED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_INIT_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 781)
)
pv660fEvent_SYSDEV_INIT_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_INIT_FAILED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_FOUND = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 782)
)
pv660fEvent_SYSDEV_FOUND.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_FOUND.setStatus(
        ""
    )

pv660fEvent_SYSDEV_GONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 783)
)
pv660fEvent_SYSDEV_GONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_GONE.setStatus(
        ""
    )

pv660fEvent_SYSDEV_EXPANDCAPACITY_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 784)
)
pv660fEvent_SYSDEV_EXPANDCAPACITY_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_EXPANDCAPACITY_START.setStatus(
        ""
    )

pv660fEvent_SYSDEV_EXPANDCAPACITY_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 785)
)
pv660fEvent_SYSDEV_EXPANDCAPACITY_DONE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_EXPANDCAPACITY_DONE.setStatus(
        ""
    )

pv660fEvent_SYSDEV_EXPANDCAPACITY_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 786)
)
pv660fEvent_SYSDEV_EXPANDCAPACITY_ERROR.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_EXPANDCAPACITY_ERROR.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BADBLOCK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 787)
)
pv660fEvent_SYSDEV_BADBLOCK.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BADBLOCK.setStatus(
        ""
    )

pv660fEvent_SYSDEV_SIZECHANGED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 788)
)
pv660fEvent_SYSDEV_SIZECHANGED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_SIZECHANGED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_TYPECHANGED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 789)
)
pv660fEvent_SYSDEV_TYPECHANGED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_TYPECHANGED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BADDATABLOCK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 790)
)
pv660fEvent_SYSDEV_BADDATABLOCK.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BADDATABLOCK.setStatus(
        ""
    )

pv660fEvent_SYSDEV_WR_LUN_MAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 791)
)
pv660fEvent_SYSDEV_WR_LUN_MAP.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_WR_LUN_MAP.setStatus(
        ""
    )

pv660fEvent_SYSDEV_DATAREAD_FROM_BLOCK_IN_BDT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 792)
)
pv660fEvent_SYSDEV_DATAREAD_FROM_BLOCK_IN_BDT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_DATAREAD_FROM_BLOCK_IN_BDT.setStatus(
        ""
    )

pv660fEvent_SYSDEV_DATA_FOR_BLOCK_LOST = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 793)
)
pv660fEvent_SYSDEV_DATA_FOR_BLOCK_LOST.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_DATA_FOR_BLOCK_LOST.setStatus(
        ""
    )

pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE_WITH_DATALOSS = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 794)
)
pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE_WITH_DATALOSS.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE_WITH_DATALOSS.setStatus(
        ""
    )

pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 795)
)
pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE.setStatus(
        ""
    )

pv660fEvent_SYSDEV_STANDBY_REBUILD_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 796)
)
pv660fEvent_SYSDEV_STANDBY_REBUILD_START.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_STANDBY_REBUILD_START.setStatus(
        ""
    )

pv660fEvent_FMTFAN_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 797)
)
pv660fEvent_FMTFAN_FAILED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTFAN_FAILED.setStatus(
        ""
    )

pv660fEvent_FMTFAN_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 798)
)
pv660fEvent_FMTFAN_OK.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTFAN_OK.setStatus(
        ""
    )

pv660fEvent_AEMI_FAN_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 799)
)
pv660fEvent_AEMI_FAN_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_AEMI_FAN_FAILED.setStatus(
        ""
    )

pv660fEvent_FMTFAN_NOTPRESENT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 800)
)
pv660fEvent_FMTFAN_NOTPRESENT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTFAN_NOTPRESENT.setStatus(
        ""
    )

pv660fEvent_FMTPOWER_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 801)
)
pv660fEvent_FMTPOWER_FAILED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTPOWER_FAILED.setStatus(
        ""
    )

pv660fEvent_FMTPOWER_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 802)
)
pv660fEvent_FMTPOWER_OK.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTPOWER_OK.setStatus(
        ""
    )

pv660fEvent_AEMI_PWR_SUPPLY_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 803)
)
pv660fEvent_AEMI_PWR_SUPPLY_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_AEMI_PWR_SUPPLY_FAILED.setStatus(
        ""
    )

pv660fEvent_FMTPOWER_NOTPRESENT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 804)
)
pv660fEvent_FMTPOWER_NOTPRESENT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTPOWER_NOTPRESENT.setStatus(
        ""
    )

pv660fEvent_FMTHEAT_BAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 805)
)
pv660fEvent_FMTHEAT_BAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTHEAT_BAD.setStatus(
        ""
    )

pv660fEvent_FMTHEAT_CRITICAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 806)
)
pv660fEvent_FMTHEAT_CRITICAL.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTHEAT_CRITICAL.setStatus(
        ""
    )

pv660fEvent_FMTHEAT_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 807)
)
pv660fEvent_FMTHEAT_OK.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTHEAT_OK.setStatus(
        ""
    )

pv660fEvent_AEMI_OVER_TEMPERATURE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 808)
)
pv660fEvent_AEMI_OVER_TEMPERATURE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_AEMI_OVER_TEMPERATURE.setStatus(
        ""
    )

pv660fEvent_FMTHEAT_NOTPRESENT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 809)
)
pv660fEvent_FMTHEAT_NOTPRESENT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTHEAT_NOTPRESENT.setStatus(
        ""
    )

pv660fEvent_FMTSTWK_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 810)
)
pv660fEvent_FMTSTWK_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTSTWK_FAILED.setStatus(
        ""
    )

pv660fEvent_FMTSTWK_CRITICAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 811)
)
pv660fEvent_FMTSTWK_CRITICAL.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTSTWK_CRITICAL.setStatus(
        ""
    )

pv660fEvent_FMTSTWK_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 812)
)
pv660fEvent_FMTSTWK_OK.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_FMTSTWK_OK.setStatus(
        ""
    )

pv660fEvent_FMT_UPS_DISABLED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 813)
)
pv660fEvent_FMT_UPS_DISABLED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMT_UPS_DISABLED.setStatus(
        ""
    )

pv660fEvent_FMT_UPS_AC_FAIL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 814)
)
pv660fEvent_FMT_UPS_AC_FAIL.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMT_UPS_AC_FAIL.setStatus(
        ""
    )

pv660fEvent_FMT_UPS_BAT_LOW = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 815)
)
pv660fEvent_FMT_UPS_BAT_LOW.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMT_UPS_BAT_LOW.setStatus(
        ""
    )

pv660fEvent_FMT_UPS_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 816)
)
pv660fEvent_FMT_UPS_FAILED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMT_UPS_FAILED.setStatus(
        ""
    )

pv660fEvent_FMT_UPS_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 817)
)
pv660fEvent_FMT_UPS_OK.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_FMT_UPS_OK.setStatus(
        ""
    )

pv660fEvent_ENCLFAN_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 818)
)
pv660fEvent_ENCLFAN_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLFAN_FAILED.setStatus(
        ""
    )

pv660fEvent_ENCLFAN_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 819)
)
pv660fEvent_ENCLFAN_OK.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLFAN_OK.setStatus(
        ""
    )

pv660fEvent_ENCLFAN_NOTPRESENT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 820)
)
pv660fEvent_ENCLFAN_NOTPRESENT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLFAN_NOTPRESENT.setStatus(
        ""
    )

pv660fEvent_ENCLPOWER_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 821)
)
pv660fEvent_ENCLPOWER_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLPOWER_FAILED.setStatus(
        ""
    )

pv660fEvent_ENCLPOWER_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 822)
)
pv660fEvent_ENCLPOWER_OK.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLPOWER_OK.setStatus(
        ""
    )

pv660fEvent_ENCLPOWER_NOTPRESENT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 823)
)
pv660fEvent_ENCLPOWER_NOTPRESENT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLPOWER_NOTPRESENT.setStatus(
        ""
    )

pv660fEvent_ENCLHEAT_BAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 824)
)
pv660fEvent_ENCLHEAT_BAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLHEAT_BAD.setStatus(
        ""
    )

pv660fEvent_ENCLHEAT_CRITICAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 825)
)
pv660fEvent_ENCLHEAT_CRITICAL.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLHEAT_CRITICAL.setStatus(
        ""
    )

pv660fEvent_ENCLHEAT_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 826)
)
pv660fEvent_ENCLHEAT_OK.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLHEAT_OK.setStatus(
        ""
    )

pv660fEvent_ENCLHEAT_NOTPRESENT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 827)
)
pv660fEvent_ENCLHEAT_NOTPRESENT.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLHEAT_NOTPRESENT.setStatus(
        ""
    )

pv660fEvent_ENCLACCESS_CRITICAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 828)
)
pv660fEvent_ENCLACCESS_CRITICAL.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLACCESS_CRITICAL.setStatus(
        ""
    )

pv660fEvent_ENCLACCESS_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 829)
)
pv660fEvent_ENCLACCESS_OK.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLACCESS_OK.setStatus(
        ""
    )

pv660fEvent_ENCLACCESS_OFFLINE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 830)
)
pv660fEvent_ENCLACCESS_OFFLINE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLACCESS_OFFLINE.setStatus(
        ""
    )

pv660fEvent_ENCLSES_SOFTADDR_OCCURRED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 831)
)
pv660fEvent_ENCLSES_SOFTADDR_OCCURRED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLSES_SOFTADDR_OCCURRED.setStatus(
        ""
    )

pv660fEvent_ENCLACCESS_READY = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 832)
)
pv660fEvent_ENCLACCESS_READY.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLACCESS_READY.setStatus(
        ""
    )

pv660fEvent_ENCLHEAT_UNKNOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 833)
)
pv660fEvent_ENCLHEAT_UNKNOWN.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLHEAT_UNKNOWN.setStatus(
        ""
    )

pv660fEvent_ENCLPOWER_UNKNOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 834)
)
pv660fEvent_ENCLPOWER_UNKNOWN.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLPOWER_UNKNOWN.setStatus(
        ""
    )

pv660fEvent_ENCLFAN_UNKNOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 835)
)
pv660fEvent_ENCLFAN_UNKNOWN.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "enclosureNumberEv"),
        ("ArrayManager-MIB", "unitNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_ENCLFAN_UNKNOWN.setStatus(
        ""
    )

pv660fEvent_SYSTEM_STARTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 836)
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSTEM_STARTED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_WRITEBACK_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 837)
)
pv660fEvent_CTLDEV_WRITEBACK_ERROR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_WRITEBACK_ERROR.setStatus(
        ""
    )

pv660fEvent_CTLDEV_STATE_TABLE_FULL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 838)
)
pv660fEvent_CTLDEV_STATE_TABLE_FULL.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_STATE_TABLE_FULL.setStatus(
        ""
    )

pv660fEvent_CTLDEV_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 839)
)
pv660fEvent_CTLDEV_DEAD.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_DEAD.setStatus(
        ""
    )

pv660fEvent_CTLDEV_RESET = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 840)
)
pv660fEvent_CTLDEV_RESET.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_RESET.setStatus(
        ""
    )

pv660fEvent_CTLDEV_FOUND = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 841)
)
pv660fEvent_CTLDEV_FOUND.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_FOUND.setStatus(
        ""
    )

pv660fEvent_CTLDEV_GONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 842)
)
pv660fEvent_CTLDEV_GONE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_GONE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_FOUND = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 843)
)
pv660fEvent_CTLDEV_BBU_FOUND.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_FOUND.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_POWER_LOW = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 844)
)
pv660fEvent_CTLDEV_BBU_POWER_LOW.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_POWER_LOW.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_POWER_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 845)
)
pv660fEvent_CTLDEV_BBU_POWER_OK.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_POWER_OK.setStatus(
        ""
    )

pv660fEvent_CTLDEV_POWER_OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 846)
)
pv660fEvent_CTLDEV_POWER_OFF.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_POWER_OFF.setStatus(
        ""
    )

pv660fEvent_CTLDEV_POWER_ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 847)
)
pv660fEvent_CTLDEV_POWER_ON.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_POWER_ON.setStatus(
        ""
    )

pv660fEvent_CTLDEV_ONLINE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 848)
)
pv660fEvent_CTLDEV_ONLINE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_ONLINE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_OFFLINE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 849)
)
pv660fEvent_CTLDEV_OFFLINE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_OFFLINE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_CRITICAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 850)
)
pv660fEvent_CTLDEV_CRITICAL.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_CRITICAL.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_RECOND_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 851)
)
pv660fEvent_CTLDEV_BBU_RECOND_START.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_RECOND_START.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_RECOND_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 852)
)
pv660fEvent_CTLDEV_BBU_RECOND_DONE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_RECOND_DONE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_RECOND_ABORT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 853)
)
pv660fEvent_CTLDEV_BBU_RECOND_ABORT.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_RECOND_ABORT.setStatus(
        ""
    )

pv660fEvent_CTLDEV_INSTALLATION_ABORTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 854)
)
pv660fEvent_CTLDEV_INSTALLATION_ABORTED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_INSTALLATION_ABORTED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_FIRMWARE_MISMATCH = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 855)
)
pv660fEvent_CTLDEV_FIRMWARE_MISMATCH.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_FIRMWARE_MISMATCH.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_NORESPONSE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 856)
)
pv660fEvent_CTLDEV_BBU_NORESPONSE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_NORESPONSE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_WARM_BOOT_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 857)
)
pv660fEvent_CTLDEV_WARM_BOOT_ERROR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_WARM_BOOT_ERROR.setStatus(
        ""
    )

pv660fEvent_CTLDEV_CONSERV_CACHE_MODE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 858)
)
pv660fEvent_CTLDEV_CONSERV_CACHE_MODE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_CONSERV_CACHE_MODE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NORMAL_CACHE_MODE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 859)
)
pv660fEvent_CTLDEV_NORMAL_CACHE_MODE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NORMAL_CACHE_MODE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_DEV_START_CMPLT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 860)
)
pv660fEvent_CTLDEV_DEV_START_CMPLT.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_DEV_START_CMPLT.setStatus(
        ""
    )

pv660fEvent_CTLDEV_SOFT_ECC_CORRECTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 861)
)
pv660fEvent_CTLDEV_SOFT_ECC_CORRECTED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_SOFT_ECC_CORRECTED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_HARD_ECC_CORRECTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 862)
)
pv660fEvent_CTLDEV_HARD_ECC_CORRECTED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_HARD_ECC_CORRECTED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_RECOND_NEEDED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 863)
)
pv660fEvent_CTLDEV_BBU_RECOND_NEEDED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_RECOND_NEEDED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_REMOVED_PTNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 864)
)
pv660fEvent_CTLDEV_REMOVED_PTNR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_REMOVED_PTNR.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_OUT_OF_SERVICE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 865)
)
pv660fEvent_CTLDEV_BBU_OUT_OF_SERVICE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_OUT_OF_SERVICE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_UPDATE_PTNR_STATUS = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 866)
)
pv660fEvent_CTLDEV_UPDATE_PTNR_STATUS.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_UPDATE_PTNR_STATUS.setStatus(
        ""
    )

pv660fEvent_CTLDEV_RELINQUISH_PTNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 867)
)
pv660fEvent_CTLDEV_RELINQUISH_PTNR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_RELINQUISH_PTNR.setStatus(
        ""
    )

pv660fEvent_CTLDEV_INSERTED_PTNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 868)
)
pv660fEvent_CTLDEV_INSERTED_PTNR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_INSERTED_PTNR.setStatus(
        ""
    )

pv660fEvent_CTLDEV_DUAL_ENABLED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 869)
)
pv660fEvent_CTLDEV_DUAL_ENABLED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_DUAL_ENABLED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_KILL_PTNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 870)
)
pv660fEvent_CTLDEV_KILL_PTNR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_KILL_PTNR.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NEXUS = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 871)
)
pv660fEvent_CTLDEV_NEXUS.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NEXUS.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BAD_BOOTROM_IMAGE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 872)
)
pv660fEvent_CTLDEV_BAD_BOOTROM_IMAGE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BAD_BOOTROM_IMAGE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BAD_MAC_ADDRESS = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 873)
)
pv660fEvent_CTLDEV_BAD_MAC_ADDRESS.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BAD_MAC_ADDRESS.setStatus(
        ""
    )

pv660fEvent_CTLDEV_MIRROR_RACE_RECOVERY_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 874)
)
pv660fEvent_CTLDEV_MIRROR_RACE_RECOVERY_FAILED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_MIRROR_RACE_RECOVERY_FAILED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_MIRROR_CRITICAL_DRIVE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 875)
)
pv660fEvent_CTLDEV_MIRROR_CRITICAL_DRIVE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_MIRROR_CRITICAL_DRIVE.setStatus(
        ""
    )

pv660fEvent_SYSTEM_STARTED_NEW = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 876)
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSTEM_STARTED_NEW.setStatus(
        ""
    )

pv660fEvent_SYSTEM_SIZE_TABLE_FULL = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 877)
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSTEM_SIZE_TABLE_FULL.setStatus(
        ""
    )

pv660fEvent_SYSTEM_USER_LOGGED_IN = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 878)
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSTEM_USER_LOGGED_IN.setStatus(
        ""
    )

pv660fEvent_SYSTEM_USER_LOGGED_OUT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 879)
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSTEM_USER_LOGGED_OUT.setStatus(
        ""
    )

pv660fEvent_SYSTEM_ALIVE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 880)
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSTEM_ALIVE.setStatus(
        ""
    )

pv660fEvent_SYSTEM_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 881)
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSTEM_DEAD.setStatus(
        ""
    )

pv660fEvent_AUTOBOOT_CHANGED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 882)
)
pv660fEvent_AUTOBOOT_CHANGED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_AUTOBOOT_CHANGED.setStatus(
        ""
    )

pv660fEvent_CHANNEL_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 883)
)
pv660fEvent_CHANNEL_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CHANNEL_FAILED.setStatus(
        ""
    )

pv660fEvent_CHANNEL_OK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 884)
)
pv660fEvent_CHANNEL_OK.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CHANNEL_OK.setStatus(
        ""
    )

pv660fEvent_CHANNEL_SCSI_BUS_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 885)
)
pv660fEvent_CHANNEL_SCSI_BUS_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CHANNEL_SCSI_BUS_DEAD.setStatus(
        ""
    )

pv660fEvent_CHANNEL_SCSI_BUS_ALIVE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 886)
)
pv660fEvent_CHANNEL_SCSI_BUS_ALIVE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CHANNEL_SCSI_BUS_ALIVE.setStatus(
        ""
    )

pv660fEvent_CHANNEL_FIBER_DEAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 887)
)
pv660fEvent_CHANNEL_FIBER_DEAD.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CHANNEL_FIBER_DEAD.setStatus(
        ""
    )

pv660fEvent_CHANNEL_FIBER_ALIVE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 888)
)
pv660fEvent_CHANNEL_FIBER_ALIVE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CHANNEL_FIBER_ALIVE.setStatus(
        ""
    )

pv660fEvent_LOG_EMPTY = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 889)
)
pv660fEvent_LOG_EMPTY.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_LOG_EMPTY.setStatus(
        ""
    )

pv660fEvent_LOG_OUT_SYNC = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 890)
)
pv660fEvent_LOG_OUT_SYNC.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_LOG_OUT_SYNC.setStatus(
        ""
    )

pv660fEvent_LOG_REQUEST_SENSE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 891)
)
pv660fEvent_LOG_REQUEST_SENSE.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_LOG_REQUEST_SENSE.setStatus(
        ""
    )

pv660fEvent_LOG_SET_RTC = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 892)
)
pv660fEvent_LOG_SET_RTC.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_LOG_SET_RTC.setStatus(
        ""
    )

pv660fEvent_CFG_NEW = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 893)
)
pv660fEvent_CFG_NEW.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CFG_NEW.setStatus(
        ""
    )

pv660fEvent_CFG_CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 894)
)
pv660fEvent_CFG_CLEAR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CFG_CLEAR.setStatus(
        ""
    )

pv660fEvent_CFG_INVALID = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 895)
)
pv660fEvent_CFG_INVALID.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CFG_INVALID.setStatus(
        ""
    )

pv660fEvent_CFG_COD_ACCESS_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 896)
)
pv660fEvent_CFG_COD_ACCESS_ERROR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CFG_COD_ACCESS_ERROR.setStatus(
        ""
    )

pv660fEvent_CFG_COD_CONVERTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 897)
)
pv660fEvent_CFG_COD_CONVERTED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CFG_COD_CONVERTED.setStatus(
        ""
    )

pv660fEvent_CFG_COD_IMPORT_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 898)
)
pv660fEvent_CFG_COD_IMPORT_FAILED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CFG_COD_IMPORT_FAILED.setStatus(
        ""
    )

pv660fEvent_DEBUG_DUMP_GENERATED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 899)
)
pv660fEvent_DEBUG_DUMP_GENERATED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_DEBUG_DUMP_GENERATED.setStatus(
        ""
    )

pv660fEvent_DEBUG_DUMP_GENERATED_PARTNER = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 900)
)
pv660fEvent_DEBUG_DUMP_GENERATED_PARTNER.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_DEBUG_DUMP_GENERATED_PARTNER.setStatus(
        ""
    )

pv660fEvent_FATAL_HANG = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 901)
)
if mibBuilder.loadTexts:
    pv660fEvent_FATAL_HANG.setStatus(
        ""
    )

pv660fEvent_FATAL_BRKP = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 902)
)
if mibBuilder.loadTexts:
    pv660fEvent_FATAL_BRKP.setStatus(
        ""
    )

pv660fEvent_I960_HW_ERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 903)
)
if mibBuilder.loadTexts:
    pv660fEvent_I960_HW_ERR.setStatus(
        ""
    )

pv660fEvent_SARM_HW_ERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 904)
)
if mibBuilder.loadTexts:
    pv660fEvent_SARM_HW_ERR.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BG_INIT_STARTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 905)
)
pv660fEvent_SYSDEV_BG_INIT_STARTED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BG_INIT_STARTED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BG_INIT_STOPPED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 906)
)
pv660fEvent_SYSDEV_BG_INIT_STOPPED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BG_INIT_STOPPED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BG_INIT_PAUSED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 907)
)
pv660fEvent_SYSDEV_BG_INIT_PAUSED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BG_INIT_PAUSED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BG_INIT_RESTARTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 908)
)
pv660fEvent_SYSDEV_BG_INIT_RESTARTED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BG_INIT_RESTARTED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BG_INIT_FAILED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 909)
)
pv660fEvent_SYSDEV_BG_INIT_FAILED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BG_INIT_FAILED.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BG_INIT_COMPLETED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 910)
)
pv660fEvent_SYSDEV_BG_INIT_COMPLETED.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BG_INIT_COMPLETED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_CALIBRATE_START = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 911)
)
pv660fEvent_CTLDEV_BBU_CALIBRATE_START.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_CALIBRATE_START.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_CALIBRATE_DONE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 912)
)
pv660fEvent_CTLDEV_BBU_CALIBRATE_DONE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_CALIBRATE_DONE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_CALIBRATE_ABORT = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 913)
)
pv660fEvent_CTLDEV_BBU_CALIBRATE_ABORT.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_CALIBRATE_ABORT.setStatus(
        ""
    )

pv660fEvent_CTLDEV_BBU_NO_BATTERY = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 914)
)
pv660fEvent_CTLDEV_BBU_NO_BATTERY.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_BBU_NO_BATTERY.setStatus(
        ""
    )

pv660fEvent_SYSDEV_BBULOW_POSSIBLE_DATA_LOSS = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 915)
)
pv660fEvent_SYSDEV_BBULOW_POSSIBLE_DATA_LOSS.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_SYSDEV_BBULOW_POSSIBLE_DATA_LOSS.setStatus(
        ""
    )

pv660fEvent_CTLDEV_IN_CLUSTER = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 916)
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_IN_CLUSTER.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NOT_IN_CLUSTER = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 917)
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NOT_IN_CLUSTER.setStatus(
        ""
    )

pv660fEvent_CTLDEV_IMPROPERLY_SHUTDOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 918)
)
pv660fEvent_CTLDEV_IMPROPERLY_SHUTDOWN.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "virtualDiskNameEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_IMPROPERLY_SHUTDOWN.setStatus(
        ""
    )

pv660fEvent_CTLDEV_AUTOMATIC_FLASH_STARTED = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 919)
)
pv660fEvent_CTLDEV_AUTOMATIC_FLASH_STARTED.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_AUTOMATIC_FLASH_STARTED.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NEGOTIATION_FAILED_JUMPERS = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 920)
)
pv660fEvent_CTLDEV_NEGOTIATION_FAILED_JUMPERS.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NEGOTIATION_FAILED_JUMPERS.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NEGOTIATION_SAME_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 921)
)
pv660fEvent_CTLDEV_NEGOTIATION_SAME_ID.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NEGOTIATION_SAME_ID.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NEGOTIATION_BOARD_TYPE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 922)
)
pv660fEvent_CTLDEV_NEGOTIATION_BOARD_TYPE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NEGOTIATION_BOARD_TYPE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NEGOTIATION_DISK_CHANNELS = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 923)
)
pv660fEvent_CTLDEV_NEGOTIATION_DISK_CHANNELS.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NEGOTIATION_DISK_CHANNELS.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NEGOTIATION_HOST_CHANNELS = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 924)
)
pv660fEvent_CTLDEV_NEGOTIATION_HOST_CHANNELS.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NEGOTIATION_HOST_CHANNELS.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NEGOTIATION_MEMORY_SIZE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 925)
)
pv660fEvent_CTLDEV_NEGOTIATION_MEMORY_SIZE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NEGOTIATION_MEMORY_SIZE.setStatus(
        ""
    )

pv660fEvent_CTLDEV_NEGOTIATION_CACHE_SIZE = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 926)
)
pv660fEvent_CTLDEV_NEGOTIATION_CACHE_SIZE.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_CTLDEV_NEGOTIATION_CACHE_SIZE.setStatus(
        ""
    )

pv660fEvent_PHYSDEV_HOT_SPARE_SMALLER = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 927)
)
pv660fEvent_PHYSDEV_HOT_SPARE_SMALLER.setObjects(
      *(("ArrayManager-MIB", "controllerNameEv"),
        ("ArrayManager-MIB", "channelNumberEv"),
        ("ArrayManager-MIB", "targetIDEv"))
)
if mibBuilder.loadTexts:
    pv660fEvent_PHYSDEV_HOT_SPARE_SMALLER.setStatus(
        ""
    )

pv660fEvent_SES_ERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 980)
)
pv660fEvent_SES_ERR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_SES_ERR.setStatus(
        ""
    )

pv660fEvent_ENC_SES_ERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 981)
)
pv660fEvent_ENC_SES_ERR.setObjects(
    ("ArrayManager-MIB", "controllerNameEv")
)
if mibBuilder.loadTexts:
    pv660fEvent_ENC_SES_ERR.setStatus(
        ""
    )

fsysPro_DISK_CAPACITY_WARNING = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 10804)
)
fsysPro_DISK_CAPACITY_WARNING.setObjects(
    ("ArrayManager-MIB", "volumeNameEv")
)
if mibBuilder.loadTexts:
    fsysPro_DISK_CAPACITY_WARNING.setStatus(
        ""
    )

fsysPro_DISK_CAPACITY_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 1, 1, 200, 0, 10805)
)
fsysPro_DISK_CAPACITY_ERROR.setObjects(
    ("ArrayManager-MIB", "volumeNameEv")
)
if mibBuilder.loadTexts:
    fsysPro_DISK_CAPACITY_ERROR.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ArrayManager-MIB",
    **{"dell": dell,
       "storage": storage,
       "software": software,
       "arrayManager": arrayManager,
       "arrayMgrSoftwareVersion": arrayMgrSoftwareVersion,
       "arrayMgrGlobalStatus": arrayMgrGlobalStatus,
       "arrayMgrSoftwareManufacturer": arrayMgrSoftwareManufacturer,
       "arrayMgrSoftwareProduct": arrayMgrSoftwareProduct,
       "arrayMgrSoftwareDescription": arrayMgrSoftwareDescription,
       "arrayMgrInfo": arrayMgrInfo,
       "arrayMgrDisplayName": arrayMgrDisplayName,
       "arrayMgrDescription": arrayMgrDescription,
       "arrayMgrAgentVendor": arrayMgrAgentVendor,
       "arrayMgrAgentVersion": arrayMgrAgentVersion,
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
       "agentAmSnmpVersion": agentAmSnmpVersion,
       "agentAmMibVersion": agentAmMibVersion,
       "providerData": providerData,
       "providerTable": providerTable,
       "providerEntry": providerEntry,
       "providerNumber": providerNumber,
       "providerName": providerName,
       "providerStatus": providerStatus,
       "providerVersion": providerVersion,
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
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channelNumber": channelNumber,
       "channelName": channelName,
       "channelState": channelState,
       "channelSeverity": channelSeverity,
       "channelTermination": channelTermination,
       "channelSCSIID": channelSCSIID,
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
       "fanConnectionTable": fanConnectionTable,
       "fanConnectionEntry": fanConnectionEntry,
       "fanConnectionNumber": fanConnectionNumber,
       "fanConnectionFanName": fanConnectionFanName,
       "fanConnectionFanNumber": fanConnectionFanNumber,
       "fanConnectionEnclosureName": fanConnectionEnclosureName,
       "fanConnectionEnclosureNumber": fanConnectionEnclosureNumber,
       "powersupplyTable": powersupplyTable,
       "powersupplyEntry": powersupplyEntry,
       "powersupplyNumber": powersupplyNumber,
       "powersupplyName": powersupplyName,
       "powersupplyVendor": powersupplyVendor,
       "powersupplyState": powersupplyState,
       "powersupplySeverity": powersupplySeverity,
       "powersupply1PartNumber": powersupply1PartNumber,
       "powersupply2PartNumber": powersupply2PartNumber,
       "powersupplyConnectionTable": powersupplyConnectionTable,
       "powersupplyConnectionEntry": powersupplyConnectionEntry,
       "powersupplyConnectionNumber": powersupplyConnectionNumber,
       "powersupplyConnectionPowersupplyName": powersupplyConnectionPowersupplyName,
       "powersupplyConnectionPowersupplyNumber": powersupplyConnectionPowersupplyNumber,
       "powersupplyConnectionEnclosureName": powersupplyConnectionEnclosureName,
       "powersupplyConnectionEnclosureNumber": powersupplyConnectionEnclosureNumber,
       "temperatureTable": temperatureTable,
       "temperatureEntry": temperatureEntry,
       "temperatureNumber": temperatureNumber,
       "temperatureName": temperatureName,
       "temperatureVendor": temperatureVendor,
       "temperatureState": temperatureState,
       "temperatureSeverity": temperatureSeverity,
       "temperatureProbeUnit": temperatureProbeUnit,
       "temperatureProbeMinWarning": temperatureProbeMinWarning,
       "temperatureProbeMinCritical": temperatureProbeMinCritical,
       "temperatureProbeMaxWarning": temperatureProbeMaxWarning,
       "temperatureProbeMaxCritical": temperatureProbeMaxCritical,
       "temperatureProbeCurValue": temperatureProbeCurValue,
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
       "enclosureManagementModuleConnectionTable": enclosureManagementModuleConnectionTable,
       "enclosureManagementModuleConnectionEntry": enclosureManagementModuleConnectionEntry,
       "enclosureManagementModuleConnectionNumber": enclosureManagementModuleConnectionNumber,
       "enclosureManagementModuleConnectionEMMName": enclosureManagementModuleConnectionEMMName,
       "enclosureManagementModuleConnectionEMMNumber": enclosureManagementModuleConnectionEMMNumber,
       "enclosureManagementModuleConnectionEnclosureName": enclosureManagementModuleConnectionEnclosureName,
       "enclosureManagementModuleConnectionEnclosureNumber": enclosureManagementModuleConnectionEnclosureNumber,
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
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskNumber": diskNumber,
       "diskName": diskName,
       "diskVirtualDiskDeviceName": diskVirtualDiskDeviceName,
       "diskState": diskState,
       "diskSeverity": diskSeverity,
       "diskLdmDeviceType": diskLdmDeviceType,
       "diskDgName": diskDgName,
       "diskLengthInMB": diskLengthInMB,
       "diskLengthInBytes": diskLengthInBytes,
       "diskFreeSpaceInMB": diskFreeSpaceInMB,
       "diskFreeSpaceInBytes": diskFreeSpaceInBytes,
       "diskAdapter": diskAdapter,
       "diskPort": diskPort,
       "diskTargetID": diskTargetID,
       "diskLunID": diskLunID,
       "diskVendor": diskVendor,
       "arrayDiskLogicalConnectionTable": arrayDiskLogicalConnectionTable,
       "arrayDiskLogicalConnectionEntry": arrayDiskLogicalConnectionEntry,
       "arrayDiskLogicalConnectionNumber": arrayDiskLogicalConnectionNumber,
       "arrayDiskLogicalConnectionArrayDiskName": arrayDiskLogicalConnectionArrayDiskName,
       "arrayDiskLogicalConnectionArrayDiskNumber": arrayDiskLogicalConnectionArrayDiskNumber,
       "arrayDiskLogicalConnectionVirtualDiskName": arrayDiskLogicalConnectionVirtualDiskName,
       "arrayDiskLogicalConnectionVirtualDiskNumber": arrayDiskLogicalConnectionVirtualDiskNumber,
       "arrayDiskLogicalConnectionDiskName": arrayDiskLogicalConnectionDiskName,
       "arrayDiskLogicalConnectionDiskNumber": arrayDiskLogicalConnectionDiskNumber,
       "subDiskTable": subDiskTable,
       "subDiskEntry": subDiskEntry,
       "subDiskNumber": subDiskNumber,
       "subDiskName": subDiskName,
       "subDiskState": subDiskState,
       "subDiskSeverity": subDiskSeverity,
       "subDiskLengthInMB": subDiskLengthInMB,
       "subDiskLengthInBytes": subDiskLengthInBytes,
       "partitionTable": partitionTable,
       "partitionEntry": partitionEntry,
       "partitionNumber": partitionNumber,
       "partitionName": partitionName,
       "partitionState": partitionState,
       "partitionSeverity": partitionSeverity,
       "partitionLengthInMB": partitionLengthInMB,
       "partitionLengthInBytes": partitionLengthInBytes,
       "partitionLdmVolumeType": partitionLdmVolumeType,
       "extendedPartitionTable": extendedPartitionTable,
       "extendedPartitionEntry": extendedPartitionEntry,
       "extendedPartitionNumber": extendedPartitionNumber,
       "extendedPartitionName": extendedPartitionName,
       "extendedPartitionState": extendedPartitionState,
       "extendedPartitionSeverity": extendedPartitionSeverity,
       "volumeTable": volumeTable,
       "volumeEntry": volumeEntry,
       "volumeNumber": volumeNumber,
       "volumeDriveLetter": volumeDriveLetter,
       "volumeState": volumeState,
       "volumeSeverity": volumeSeverity,
       "volumeLdmVolumeType": volumeLdmVolumeType,
       "volumeLabel": volumeLabel,
       "volumeFSType": volumeFSType,
       "volumeLengthInMB": volumeLengthInMB,
       "volumeLengthInBytes": volumeLengthInBytes,
       "volumeFreeSpaceInMB": volumeFreeSpaceInMB,
       "volumeFreeSpaceInBytes": volumeFreeSpaceInBytes,
       "plexTable": plexTable,
       "plexEntry": plexEntry,
       "plexNumber": plexNumber,
       "plexName": plexName,
       "plexStripeWidthInMB": plexStripeWidthInMB,
       "plexStripeWidthInBytes": plexStripeWidthInBytes,
       "plexColumns": plexColumns,
       "plexLayout": plexLayout,
       "basicDiskExtendedConnectionTable": basicDiskExtendedConnectionTable,
       "basicDiskExtendedConnectionEntry": basicDiskExtendedConnectionEntry,
       "basicDiskExtendedConnectionNumber": basicDiskExtendedConnectionNumber,
       "basicDiskExtendedConnectionArrayDiskName": basicDiskExtendedConnectionArrayDiskName,
       "basicDiskExtendedConnectionArrayDiskNumber": basicDiskExtendedConnectionArrayDiskNumber,
       "basicDiskExtendedConnectionVirtualDiskName": basicDiskExtendedConnectionVirtualDiskName,
       "basicDiskExtendedConnectionVirtualDiskNumber": basicDiskExtendedConnectionVirtualDiskNumber,
       "basicDiskExtendedConnectionDiskName": basicDiskExtendedConnectionDiskName,
       "basicDiskExtendedConnectionDiskNumber": basicDiskExtendedConnectionDiskNumber,
       "basicDiskExtendedConnectionExtendedPartitionName": basicDiskExtendedConnectionExtendedPartitionName,
       "basicDiskExtendedConnectionExtendedPartitionNumber": basicDiskExtendedConnectionExtendedPartitionNumber,
       "basicDiskExtendedConnectionPartitionName": basicDiskExtendedConnectionPartitionName,
       "basicDiskExtendedConnectionPartitionNumber": basicDiskExtendedConnectionPartitionNumber,
       "basicDiskExtendedConnectionVolumeDriveLetter": basicDiskExtendedConnectionVolumeDriveLetter,
       "basicDiskExtendedConnectionVolumeNumber": basicDiskExtendedConnectionVolumeNumber,
       "basicDiskNonExtendedConnectionTable": basicDiskNonExtendedConnectionTable,
       "basicDiskNonExtendedConnectionEntry": basicDiskNonExtendedConnectionEntry,
       "basicDiskNonExtendedConnectionNumber": basicDiskNonExtendedConnectionNumber,
       "basicDiskNonExtendedConnectionArrayDiskName": basicDiskNonExtendedConnectionArrayDiskName,
       "basicDiskNonExtendedConnectionArrayDiskNumber": basicDiskNonExtendedConnectionArrayDiskNumber,
       "basicDiskNonExtendedConnectionVirtualDiskName": basicDiskNonExtendedConnectionVirtualDiskName,
       "basicDiskNonExtendedConnectionVirtualDiskNumber": basicDiskNonExtendedConnectionVirtualDiskNumber,
       "basicDiskNonExtendedConnectionDiskName": basicDiskNonExtendedConnectionDiskName,
       "basicDiskNonExtendedConnectionDiskNumber": basicDiskNonExtendedConnectionDiskNumber,
       "basicDiskNonExtendedConnectionPartitionName": basicDiskNonExtendedConnectionPartitionName,
       "basicDiskNonExtendedConnectionPartitionNumber": basicDiskNonExtendedConnectionPartitionNumber,
       "basicDiskNonExtendedConnectionVolumeDriveLetter": basicDiskNonExtendedConnectionVolumeDriveLetter,
       "basicDiskNonExtendedConnectionVolumeNumber": basicDiskNonExtendedConnectionVolumeNumber,
       "dynamicDiskConnectionTable": dynamicDiskConnectionTable,
       "dynamicDiskConnectionEntry": dynamicDiskConnectionEntry,
       "dynamicDiskConnectionNumber": dynamicDiskConnectionNumber,
       "dynamicDiskConnectionArrayDiskName": dynamicDiskConnectionArrayDiskName,
       "dynamicDiskConnectionArrayDiskNumber": dynamicDiskConnectionArrayDiskNumber,
       "dynamicDiskConnectionVirtualDiskName": dynamicDiskConnectionVirtualDiskName,
       "dynamicDiskConnectionVirtualDiskNumber": dynamicDiskConnectionVirtualDiskNumber,
       "dynamicDiskConnectionDiskName": dynamicDiskConnectionDiskName,
       "dynamicDiskConnectionDiskNumber": dynamicDiskConnectionDiskNumber,
       "dynamicDiskConnectionSubDiskName": dynamicDiskConnectionSubDiskName,
       "dynamicDiskConnectionSubDiskNumber": dynamicDiskConnectionSubDiskNumber,
       "dynamicDiskConnectionPlexName": dynamicDiskConnectionPlexName,
       "dynamicDiskConnectionPlexNumber": dynamicDiskConnectionPlexNumber,
       "dynamicDiskConnectionVolumeDriveLetter": dynamicDiskConnectionVolumeDriveLetter,
       "dynamicDiskConnectionVolumeNumber": dynamicDiskConnectionVolumeNumber,
       "aryMgrEvts": aryMgrEvts,
       "arrayDiskFailed": arrayDiskFailed,
       "arrayDiskRemoved": arrayDiskRemoved,
       "arrayDiskOffline": arrayDiskOffline,
       "arrayDiskDegraded": arrayDiskDegraded,
       "arrayDiskInserted": arrayDiskInserted,
       "virtualDiskCreated": virtualDiskCreated,
       "virtualDiskDeleted": virtualDiskDeleted,
       "virtualDiskConfigChanged": virtualDiskConfigChanged,
       "virtualDiskFailed": virtualDiskFailed,
       "virtualDiskDegraded": virtualDiskDegraded,
       "vdFailedRedundancy": vdFailedRedundancy,
       "checkConsistencyStarted": checkConsistencyStarted,
       "vdFormatStarted": vdFormatStarted,
       "adFormatStarted": adFormatStarted,
       "vdInitializeStarted": vdInitializeStarted,
       "adInitializeStarted": adInitializeStarted,
       "vdReconfigStarted": vdReconfigStarted,
       "vdRebuildStarted": vdRebuildStarted,
       "adRebuildStarted": adRebuildStarted,
       "adDiagStarted": adDiagStarted,
       "checkConsistencyCancelled": checkConsistencyCancelled,
       "vdFormatCancelled": vdFormatCancelled,
       "adFormatCancelled": adFormatCancelled,
       "vdInitializeCancelled": vdInitializeCancelled,
       "adInitializeCancelled": adInitializeCancelled,
       "vdReconfigCancelled": vdReconfigCancelled,
       "vdRebuildCancelled": vdRebuildCancelled,
       "adRebuildCancelled": adRebuildCancelled,
       "adDiagCancelled": adDiagCancelled,
       "checkConsistencyFailed": checkConsistencyFailed,
       "vdFormatFailed": vdFormatFailed,
       "adFormatFailed": adFormatFailed,
       "vdInitializeFailed": vdInitializeFailed,
       "adInitializeFailed": adInitializeFailed,
       "vdReconfigFailed": vdReconfigFailed,
       "vdRebuildFailed": vdRebuildFailed,
       "adRebuildFailed": adRebuildFailed,
       "adDiagFailed": adDiagFailed,
       "checkConsistencyCompleted": checkConsistencyCompleted,
       "vdFormatCompleted": vdFormatCompleted,
       "adFormatCompleted": adFormatCompleted,
       "vdInitializeCompleted": vdInitializeCompleted,
       "adInitializeCompleted": adInitializeCompleted,
       "vdReconfigCompleted": vdReconfigCompleted,
       "vdRebuildCompleted": vdRebuildCompleted,
       "adRebuildCompleted": adRebuildCompleted,
       "adDiagCompleted": adDiagCompleted,
       "percPredictiveFailure": percPredictiveFailure,
       "percSCSISenseData": percSCSISenseData,
       "percPauseIO": percPauseIO,
       "percResumeIO": percResumeIO,
       "percHotSpareAssign": percHotSpareAssign,
       "percHotSpareUnAssign": percHotSpareUnAssign,
       "cntrlBatteryNeedsReconditioning": cntrlBatteryNeedsReconditioning,
       "cntrlBatteryLow": cntrlBatteryLow,
       "cntrlBatteryRecondition": cntrlBatteryRecondition,
       "cntrlBatteryReconComplete": cntrlBatteryReconComplete,
       "cntrlPauseIO": cntrlPauseIO,
       "cntrlResumeIO": cntrlResumeIO,
       "perc2SmartFPTExceeded": perc2SmartFPTExceeded,
       "perc2SmartConfigChange": perc2SmartConfigChange,
       "perc2SmartWarning": perc2SmartWarning,
       "perc2SmartWarningTemp": perc2SmartWarningTemp,
       "perc2SmartWarningDegraded": perc2SmartWarningDegraded,
       "perc2SmartFPTExceededTest": perc2SmartFPTExceededTest,
       "enclosureAlertTempWarnMax": enclosureAlertTempWarnMax,
       "enclosureAlertTempWarnMin": enclosureAlertTempWarnMin,
       "enclosureAlertTempErrMax": enclosureAlertTempErrMax,
       "enclosureAlertTempErrMin": enclosureAlertTempErrMin,
       "enclosureGenericFailed": enclosureGenericFailed,
       "enclosureGenericOffline": enclosureGenericOffline,
       "enclosureGenericUnknown": enclosureGenericUnknown,
       "enclosureGenericWarning": enclosureGenericWarning,
       "enclosureGenericDegraded": enclosureGenericDegraded,
       "alertShutdownEnclosure": alertShutdownEnclosure,
       "alertShutdownServer": alertShutdownServer,
       "alertPausedCheckConsistency": alertPausedCheckConsistency,
       "alertResumedCheckConsistency": alertResumedCheckConsistency,
       "alertVirtualDiskSplitMirror": alertVirtualDiskSplitMirror,
       "alertVirtualDiskUnmirror": alertVirtualDiskUnmirror,
       "alertRenameVirtualDisk": alertRenameVirtualDisk,
       "alertGenericReady": alertGenericReady,
       "alertCommTimeout": alertCommTimeout,
       "alertCommFailure": alertCommFailure,
       "alertCommRestored": alertCommRestored,
       "genericEvent_DATABASE_UP": genericEvent_DATABASE_UP,
       "genericEvent_DATABASE_DOWN": genericEvent_DATABASE_DOWN,
       "alertMegalibTimeout": alertMegalibTimeout,
       "alertScsiSenseFormatFail": alertScsiSenseFormatFail,
       "alertScsiSenseSectorReassign": alertScsiSenseSectorReassign,
       "alertEmmFwMismatch": alertEmmFwMismatch,
       "alertConserveCacheModeEnable": alertConserveCacheModeEnable,
       "alertConserveCacheModeDisable": alertConserveCacheModeDisable,
       "alertEnclosureFwDownload": alertEnclosureFwDownload,
       "alertEnclosureAlarmEnable": alertEnclosureAlarmEnable,
       "alertEnclosureAlarmDisable": alertEnclosureAlarmDisable,
       "alertControllerAlarmEnable": alertControllerAlarmEnable,
       "alertControllerAlarmDisable": alertControllerAlarmDisable,
       "alertControllerRebuildRate": alertControllerRebuildRate,
       "alertArrayDiskForcedOnline": alertArrayDiskForcedOnline,
       "alertArrayDiskForcedOffline": alertArrayDiskForcedOffline,
       "alertTaskBGI": alertTaskBGI,
       "alertCancelBGI": alertCancelBGI,
       "alertFailBGI": alertFailBGI,
       "alertCompleteBGI": alertCompleteBGI,
       "enclosureGenericNotInstalled": enclosureGenericNotInstalled,
       "pv660fEvent_PHYSDEV_ONLINE": pv660fEvent_PHYSDEV_ONLINE,
       "pv660fEvent_PHYSDEV_HOTSPARE": pv660fEvent_PHYSDEV_HOTSPARE,
       "pv660fEvent_PHYSDEV_HARD_ERROR": pv660fEvent_PHYSDEV_HARD_ERROR,
       "pv660fEvent_PHYSDEV_PFA": pv660fEvent_PHYSDEV_PFA,
       "pv660fEvent_PHYSDEV_AUTO_REBUILD_START": pv660fEvent_PHYSDEV_AUTO_REBUILD_START,
       "pv660fEvent_PHYSDEV_MANUAL_REBUILD_START": pv660fEvent_PHYSDEV_MANUAL_REBUILD_START,
       "pv660fEvent_PHYSDEV_REBUILD_DONE": pv660fEvent_PHYSDEV_REBUILD_DONE,
       "pv660fEvent_PHYSDEV_REBUILD_CANCELED": pv660fEvent_PHYSDEV_REBUILD_CANCELED,
       "pv660fEvent_PHYSDEV_REBUILD_ERROR": pv660fEvent_PHYSDEV_REBUILD_ERROR,
       "pv660fEvent_PHYSDEV_REBUILD_NEWDEV_FAILED": pv660fEvent_PHYSDEV_REBUILD_NEWDEV_FAILED,
       "pv660fEvent_PHYSDEV_REBUILD_SYSDEV_FAILED": pv660fEvent_PHYSDEV_REBUILD_SYSDEV_FAILED,
       "pv660fEvent_PHYSDEV_DEAD": pv660fEvent_PHYSDEV_DEAD,
       "pv660fEvent_PHYSDEV_FOUND": pv660fEvent_PHYSDEV_FOUND,
       "pv660fEvent_PHYSDEV_GONE": pv660fEvent_PHYSDEV_GONE,
       "pv660fEvent_PHYSDEV_UNCONFIGURED": pv660fEvent_PHYSDEV_UNCONFIGURED,
       "pv660fEvent_PHYSDEV_EXPANDCAPACITY_START": pv660fEvent_PHYSDEV_EXPANDCAPACITY_START,
       "pv660fEvent_PHYSDEV_EXPANDCAPACITY_DONE": pv660fEvent_PHYSDEV_EXPANDCAPACITY_DONE,
       "pv660fEvent_PHYSDEV_EXPANDCAPACITY_ERROR": pv660fEvent_PHYSDEV_EXPANDCAPACITY_ERROR,
       "pv660fEvent_PHYSDEV_COMMAND_TIMEOUT": pv660fEvent_PHYSDEV_COMMAND_TIMEOUT,
       "pv660fEvent_PHYSDEV_COMMAND_ABORT": pv660fEvent_PHYSDEV_COMMAND_ABORT,
       "pv660fEvent_PHYSDEV_COMMAND_RETRIED": pv660fEvent_PHYSDEV_COMMAND_RETRIED,
       "pv660fEvent_PHYSDEV_PARITY_ERROR": pv660fEvent_PHYSDEV_PARITY_ERROR,
       "pv660fEvent_PHYSDEV_SOFT_ERROR": pv660fEvent_PHYSDEV_SOFT_ERROR,
       "pv660fEvent_PHYSDEV_MISC_ERROR": pv660fEvent_PHYSDEV_MISC_ERROR,
       "pv660fEvent_PHYSDEV_RESET": pv660fEvent_PHYSDEV_RESET,
       "pv660fEvent_PHYSDEV_ACTIVESPARE": pv660fEvent_PHYSDEV_ACTIVESPARE,
       "pv660fEvent_PHYSDEV_WARMSPARE": pv660fEvent_PHYSDEV_WARMSPARE,
       "pv660fEvent_PHYSDEV_REQSENSE": pv660fEvent_PHYSDEV_REQSENSE,
       "pv660fEvent_PHYSDEV_INIT_STARTED": pv660fEvent_PHYSDEV_INIT_STARTED,
       "pv660fEvent_PHYSDEV_INIT_DONE": pv660fEvent_PHYSDEV_INIT_DONE,
       "pv660fEvent_PHYSDEV_INIT_FAILED": pv660fEvent_PHYSDEV_INIT_FAILED,
       "pv660fEvent_PHYSDEV_INIT_CANCELED": pv660fEvent_PHYSDEV_INIT_CANCELED,
       "pv660fEvent_PHYSDEV_WRITEREC_DEAD": pv660fEvent_PHYSDEV_WRITEREC_DEAD,
       "pv660fEvent_PHYSDEV_RESET_DEAD": pv660fEvent_PHYSDEV_RESET_DEAD,
       "pv660fEvent_PHYSDEV_DBLCC_DEAD": pv660fEvent_PHYSDEV_DBLCC_DEAD,
       "pv660fEvent_PHYSDEV_REMOVED_DEAD": pv660fEvent_PHYSDEV_REMOVED_DEAD,
       "pv660fEvent_PHYSDEV_GROSSERR_DEAD": pv660fEvent_PHYSDEV_GROSSERR_DEAD,
       "pv660fEvent_PHYSDEV_BADTAG_DEAD": pv660fEvent_PHYSDEV_BADTAG_DEAD,
       "pv660fEvent_PHYSDEV_SCSITMO_DEAD": pv660fEvent_PHYSDEV_SCSITMO_DEAD,
       "pv660fEvent_PHYSDEV_SYSRESET_DEAD": pv660fEvent_PHYSDEV_SYSRESET_DEAD,
       "pv660fEvent_PHYSDEV_BSYPAR_DEAD": pv660fEvent_PHYSDEV_BSYPAR_DEAD,
       "pv660fEvent_PHYSDEV_BYCMD_DEAD": pv660fEvent_PHYSDEV_BYCMD_DEAD,
       "pv660fEvent_PHYSDEV_SELTMO_DEAD": pv660fEvent_PHYSDEV_SELTMO_DEAD,
       "pv660fEvent_PHYSDEV_SEQERR_DEAD": pv660fEvent_PHYSDEV_SEQERR_DEAD,
       "pv660fEvent_PHYSDEV_UNKNOWNSTS_DEAD": pv660fEvent_PHYSDEV_UNKNOWNSTS_DEAD,
       "pv660fEvent_PHYSDEV_NOTRDY_DEAD": pv660fEvent_PHYSDEV_NOTRDY_DEAD,
       "pv660fEvent_PHYSDEV_MISSING_DEAD": pv660fEvent_PHYSDEV_MISSING_DEAD,
       "pv660fEvent_PHYSDEV_CODWRFAIL_DEAD": pv660fEvent_PHYSDEV_CODWRFAIL_DEAD,
       "pv660fEvent_PHYSDEV_BDTWRFAIL_DEAD": pv660fEvent_PHYSDEV_BDTWRFAIL_DEAD,
       "pv660fEvent_PHYSDEV_OFFLINE": pv660fEvent_PHYSDEV_OFFLINE,
       "pv660fEvent_PHYSDEV_STANDBY": pv660fEvent_PHYSDEV_STANDBY,
       "pv660fEvent_PHYSDEV_REBUILD": pv660fEvent_PHYSDEV_REBUILD,
       "pv660fEvent_PHYSDEV_ID_MISMATCH": pv660fEvent_PHYSDEV_ID_MISMATCH,
       "pv660fEvent_PHYSDEV_FAILED_START": pv660fEvent_PHYSDEV_FAILED_START,
       "pv660fEvent_PHYSDEV_OFFSET_SET": pv660fEvent_PHYSDEV_OFFSET_SET,
       "pv660fEvent_PHYSDEV_SET_BUS_WIDTH": pv660fEvent_PHYSDEV_SET_BUS_WIDTH,
       "pv660fEvent_PHYSDEV_MISSING_ONSTARTUP": pv660fEvent_PHYSDEV_MISSING_ONSTARTUP,
       "pv660fEvent_PHYSDEV_REBUILD_START_FAILED": pv660fEvent_PHYSDEV_REBUILD_START_FAILED,
       "pv660fEvent_PHYSDEV_MOVING_TO_OTHER_CHN": pv660fEvent_PHYSDEV_MOVING_TO_OTHER_CHN,
       "pv660fEvent_PHYSDEV_OFFLINE_DEVICE_MADE_ONLINE": pv660fEvent_PHYSDEV_OFFLINE_DEVICE_MADE_ONLINE,
       "pv660fEvent_PHYSDEV_STANDBY_REBUILD_START": pv660fEvent_PHYSDEV_STANDBY_REBUILD_START,
       "pv660fEvent_FIBREDEV_LOOPID_SOFTADDR_OCCURRED": pv660fEvent_FIBREDEV_LOOPID_SOFTADDR_OCCURRED,
       "pv660fEvent_SYSDEV_CHECK_START": pv660fEvent_SYSDEV_CHECK_START,
       "pv660fEvent_SYSDEV_CHECK_DONE": pv660fEvent_SYSDEV_CHECK_DONE,
       "pv660fEvent_SYSDEV_CHECK_CANCELED": pv660fEvent_SYSDEV_CHECK_CANCELED,
       "pv660fEvent_SYSDEV_CHECK_ERROR": pv660fEvent_SYSDEV_CHECK_ERROR,
       "pv660fEvent_SYSDEV_CHECK_SYSDEV_FAILED": pv660fEvent_SYSDEV_CHECK_SYSDEV_FAILED,
       "pv660fEvent_SYSDEV_CHECK_PHYSDEV_FAILED": pv660fEvent_SYSDEV_CHECK_PHYSDEV_FAILED,
       "pv660fEvent_SYSDEV_OFFLINE": pv660fEvent_SYSDEV_OFFLINE,
       "pv660fEvent_SYSDEV_CRITICAL": pv660fEvent_SYSDEV_CRITICAL,
       "pv660fEvent_SYSDEV_ONLINE": pv660fEvent_SYSDEV_ONLINE,
       "pv660fEvent_SYSDEV_AUTO_REBUILD_START": pv660fEvent_SYSDEV_AUTO_REBUILD_START,
       "pv660fEvent_SYSDEV_MANUAL_REBUILD_START": pv660fEvent_SYSDEV_MANUAL_REBUILD_START,
       "pv660fEvent_SYSDEV_REBUILD_DONE": pv660fEvent_SYSDEV_REBUILD_DONE,
       "pv660fEvent_SYSDEV_REBUILD_CANCELED": pv660fEvent_SYSDEV_REBUILD_CANCELED,
       "pv660fEvent_SYSDEV_REBUILD_ERROR": pv660fEvent_SYSDEV_REBUILD_ERROR,
       "pv660fEvent_SYSDEV_REBUILD_NEWDEV_FAILED": pv660fEvent_SYSDEV_REBUILD_NEWDEV_FAILED,
       "pv660fEvent_SYSDEV_REBUILD_SYSDEV_FAILED": pv660fEvent_SYSDEV_REBUILD_SYSDEV_FAILED,
       "pv660fEvent_SYSDEV_INIT_STARTED": pv660fEvent_SYSDEV_INIT_STARTED,
       "pv660fEvent_SYSDEV_INIT_DONE": pv660fEvent_SYSDEV_INIT_DONE,
       "pv660fEvent_SYSDEV_INIT_CANCELED": pv660fEvent_SYSDEV_INIT_CANCELED,
       "pv660fEvent_SYSDEV_INIT_FAILED": pv660fEvent_SYSDEV_INIT_FAILED,
       "pv660fEvent_SYSDEV_FOUND": pv660fEvent_SYSDEV_FOUND,
       "pv660fEvent_SYSDEV_GONE": pv660fEvent_SYSDEV_GONE,
       "pv660fEvent_SYSDEV_EXPANDCAPACITY_START": pv660fEvent_SYSDEV_EXPANDCAPACITY_START,
       "pv660fEvent_SYSDEV_EXPANDCAPACITY_DONE": pv660fEvent_SYSDEV_EXPANDCAPACITY_DONE,
       "pv660fEvent_SYSDEV_EXPANDCAPACITY_ERROR": pv660fEvent_SYSDEV_EXPANDCAPACITY_ERROR,
       "pv660fEvent_SYSDEV_BADBLOCK": pv660fEvent_SYSDEV_BADBLOCK,
       "pv660fEvent_SYSDEV_SIZECHANGED": pv660fEvent_SYSDEV_SIZECHANGED,
       "pv660fEvent_SYSDEV_TYPECHANGED": pv660fEvent_SYSDEV_TYPECHANGED,
       "pv660fEvent_SYSDEV_BADDATABLOCK": pv660fEvent_SYSDEV_BADDATABLOCK,
       "pv660fEvent_SYSDEV_WR_LUN_MAP": pv660fEvent_SYSDEV_WR_LUN_MAP,
       "pv660fEvent_SYSDEV_DATAREAD_FROM_BLOCK_IN_BDT": pv660fEvent_SYSDEV_DATAREAD_FROM_BLOCK_IN_BDT,
       "pv660fEvent_SYSDEV_DATA_FOR_BLOCK_LOST": pv660fEvent_SYSDEV_DATA_FOR_BLOCK_LOST,
       "pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE_WITH_DATALOSS": pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE_WITH_DATALOSS,
       "pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE": pv660fEvent_SYSDEV_OFFLINE_DEVICE_MADE_AVAILABLE,
       "pv660fEvent_SYSDEV_STANDBY_REBUILD_START": pv660fEvent_SYSDEV_STANDBY_REBUILD_START,
       "pv660fEvent_FMTFAN_FAILED": pv660fEvent_FMTFAN_FAILED,
       "pv660fEvent_FMTFAN_OK": pv660fEvent_FMTFAN_OK,
       "pv660fEvent_AEMI_FAN_FAILED": pv660fEvent_AEMI_FAN_FAILED,
       "pv660fEvent_FMTFAN_NOTPRESENT": pv660fEvent_FMTFAN_NOTPRESENT,
       "pv660fEvent_FMTPOWER_FAILED": pv660fEvent_FMTPOWER_FAILED,
       "pv660fEvent_FMTPOWER_OK": pv660fEvent_FMTPOWER_OK,
       "pv660fEvent_AEMI_PWR_SUPPLY_FAILED": pv660fEvent_AEMI_PWR_SUPPLY_FAILED,
       "pv660fEvent_FMTPOWER_NOTPRESENT": pv660fEvent_FMTPOWER_NOTPRESENT,
       "pv660fEvent_FMTHEAT_BAD": pv660fEvent_FMTHEAT_BAD,
       "pv660fEvent_FMTHEAT_CRITICAL": pv660fEvent_FMTHEAT_CRITICAL,
       "pv660fEvent_FMTHEAT_OK": pv660fEvent_FMTHEAT_OK,
       "pv660fEvent_AEMI_OVER_TEMPERATURE": pv660fEvent_AEMI_OVER_TEMPERATURE,
       "pv660fEvent_FMTHEAT_NOTPRESENT": pv660fEvent_FMTHEAT_NOTPRESENT,
       "pv660fEvent_FMTSTWK_FAILED": pv660fEvent_FMTSTWK_FAILED,
       "pv660fEvent_FMTSTWK_CRITICAL": pv660fEvent_FMTSTWK_CRITICAL,
       "pv660fEvent_FMTSTWK_OK": pv660fEvent_FMTSTWK_OK,
       "pv660fEvent_FMT_UPS_DISABLED": pv660fEvent_FMT_UPS_DISABLED,
       "pv660fEvent_FMT_UPS_AC_FAIL": pv660fEvent_FMT_UPS_AC_FAIL,
       "pv660fEvent_FMT_UPS_BAT_LOW": pv660fEvent_FMT_UPS_BAT_LOW,
       "pv660fEvent_FMT_UPS_FAILED": pv660fEvent_FMT_UPS_FAILED,
       "pv660fEvent_FMT_UPS_OK": pv660fEvent_FMT_UPS_OK,
       "pv660fEvent_ENCLFAN_FAILED": pv660fEvent_ENCLFAN_FAILED,
       "pv660fEvent_ENCLFAN_OK": pv660fEvent_ENCLFAN_OK,
       "pv660fEvent_ENCLFAN_NOTPRESENT": pv660fEvent_ENCLFAN_NOTPRESENT,
       "pv660fEvent_ENCLPOWER_FAILED": pv660fEvent_ENCLPOWER_FAILED,
       "pv660fEvent_ENCLPOWER_OK": pv660fEvent_ENCLPOWER_OK,
       "pv660fEvent_ENCLPOWER_NOTPRESENT": pv660fEvent_ENCLPOWER_NOTPRESENT,
       "pv660fEvent_ENCLHEAT_BAD": pv660fEvent_ENCLHEAT_BAD,
       "pv660fEvent_ENCLHEAT_CRITICAL": pv660fEvent_ENCLHEAT_CRITICAL,
       "pv660fEvent_ENCLHEAT_OK": pv660fEvent_ENCLHEAT_OK,
       "pv660fEvent_ENCLHEAT_NOTPRESENT": pv660fEvent_ENCLHEAT_NOTPRESENT,
       "pv660fEvent_ENCLACCESS_CRITICAL": pv660fEvent_ENCLACCESS_CRITICAL,
       "pv660fEvent_ENCLACCESS_OK": pv660fEvent_ENCLACCESS_OK,
       "pv660fEvent_ENCLACCESS_OFFLINE": pv660fEvent_ENCLACCESS_OFFLINE,
       "pv660fEvent_ENCLSES_SOFTADDR_OCCURRED": pv660fEvent_ENCLSES_SOFTADDR_OCCURRED,
       "pv660fEvent_ENCLACCESS_READY": pv660fEvent_ENCLACCESS_READY,
       "pv660fEvent_ENCLHEAT_UNKNOWN": pv660fEvent_ENCLHEAT_UNKNOWN,
       "pv660fEvent_ENCLPOWER_UNKNOWN": pv660fEvent_ENCLPOWER_UNKNOWN,
       "pv660fEvent_ENCLFAN_UNKNOWN": pv660fEvent_ENCLFAN_UNKNOWN,
       "pv660fEvent_SYSTEM_STARTED": pv660fEvent_SYSTEM_STARTED,
       "pv660fEvent_CTLDEV_WRITEBACK_ERROR": pv660fEvent_CTLDEV_WRITEBACK_ERROR,
       "pv660fEvent_CTLDEV_STATE_TABLE_FULL": pv660fEvent_CTLDEV_STATE_TABLE_FULL,
       "pv660fEvent_CTLDEV_DEAD": pv660fEvent_CTLDEV_DEAD,
       "pv660fEvent_CTLDEV_RESET": pv660fEvent_CTLDEV_RESET,
       "pv660fEvent_CTLDEV_FOUND": pv660fEvent_CTLDEV_FOUND,
       "pv660fEvent_CTLDEV_GONE": pv660fEvent_CTLDEV_GONE,
       "pv660fEvent_CTLDEV_BBU_FOUND": pv660fEvent_CTLDEV_BBU_FOUND,
       "pv660fEvent_CTLDEV_BBU_POWER_LOW": pv660fEvent_CTLDEV_BBU_POWER_LOW,
       "pv660fEvent_CTLDEV_BBU_POWER_OK": pv660fEvent_CTLDEV_BBU_POWER_OK,
       "pv660fEvent_CTLDEV_POWER_OFF": pv660fEvent_CTLDEV_POWER_OFF,
       "pv660fEvent_CTLDEV_POWER_ON": pv660fEvent_CTLDEV_POWER_ON,
       "pv660fEvent_CTLDEV_ONLINE": pv660fEvent_CTLDEV_ONLINE,
       "pv660fEvent_CTLDEV_OFFLINE": pv660fEvent_CTLDEV_OFFLINE,
       "pv660fEvent_CTLDEV_CRITICAL": pv660fEvent_CTLDEV_CRITICAL,
       "pv660fEvent_CTLDEV_BBU_RECOND_START": pv660fEvent_CTLDEV_BBU_RECOND_START,
       "pv660fEvent_CTLDEV_BBU_RECOND_DONE": pv660fEvent_CTLDEV_BBU_RECOND_DONE,
       "pv660fEvent_CTLDEV_BBU_RECOND_ABORT": pv660fEvent_CTLDEV_BBU_RECOND_ABORT,
       "pv660fEvent_CTLDEV_INSTALLATION_ABORTED": pv660fEvent_CTLDEV_INSTALLATION_ABORTED,
       "pv660fEvent_CTLDEV_FIRMWARE_MISMATCH": pv660fEvent_CTLDEV_FIRMWARE_MISMATCH,
       "pv660fEvent_CTLDEV_BBU_NORESPONSE": pv660fEvent_CTLDEV_BBU_NORESPONSE,
       "pv660fEvent_CTLDEV_WARM_BOOT_ERROR": pv660fEvent_CTLDEV_WARM_BOOT_ERROR,
       "pv660fEvent_CTLDEV_CONSERV_CACHE_MODE": pv660fEvent_CTLDEV_CONSERV_CACHE_MODE,
       "pv660fEvent_CTLDEV_NORMAL_CACHE_MODE": pv660fEvent_CTLDEV_NORMAL_CACHE_MODE,
       "pv660fEvent_CTLDEV_DEV_START_CMPLT": pv660fEvent_CTLDEV_DEV_START_CMPLT,
       "pv660fEvent_CTLDEV_SOFT_ECC_CORRECTED": pv660fEvent_CTLDEV_SOFT_ECC_CORRECTED,
       "pv660fEvent_CTLDEV_HARD_ECC_CORRECTED": pv660fEvent_CTLDEV_HARD_ECC_CORRECTED,
       "pv660fEvent_CTLDEV_BBU_RECOND_NEEDED": pv660fEvent_CTLDEV_BBU_RECOND_NEEDED,
       "pv660fEvent_CTLDEV_REMOVED_PTNR": pv660fEvent_CTLDEV_REMOVED_PTNR,
       "pv660fEvent_CTLDEV_BBU_OUT_OF_SERVICE": pv660fEvent_CTLDEV_BBU_OUT_OF_SERVICE,
       "pv660fEvent_CTLDEV_UPDATE_PTNR_STATUS": pv660fEvent_CTLDEV_UPDATE_PTNR_STATUS,
       "pv660fEvent_CTLDEV_RELINQUISH_PTNR": pv660fEvent_CTLDEV_RELINQUISH_PTNR,
       "pv660fEvent_CTLDEV_INSERTED_PTNR": pv660fEvent_CTLDEV_INSERTED_PTNR,
       "pv660fEvent_CTLDEV_DUAL_ENABLED": pv660fEvent_CTLDEV_DUAL_ENABLED,
       "pv660fEvent_CTLDEV_KILL_PTNR": pv660fEvent_CTLDEV_KILL_PTNR,
       "pv660fEvent_CTLDEV_NEXUS": pv660fEvent_CTLDEV_NEXUS,
       "pv660fEvent_CTLDEV_BAD_BOOTROM_IMAGE": pv660fEvent_CTLDEV_BAD_BOOTROM_IMAGE,
       "pv660fEvent_CTLDEV_BAD_MAC_ADDRESS": pv660fEvent_CTLDEV_BAD_MAC_ADDRESS,
       "pv660fEvent_CTLDEV_MIRROR_RACE_RECOVERY_FAILED": pv660fEvent_CTLDEV_MIRROR_RACE_RECOVERY_FAILED,
       "pv660fEvent_CTLDEV_MIRROR_CRITICAL_DRIVE": pv660fEvent_CTLDEV_MIRROR_CRITICAL_DRIVE,
       "pv660fEvent_SYSTEM_STARTED_NEW": pv660fEvent_SYSTEM_STARTED_NEW,
       "pv660fEvent_SYSTEM_SIZE_TABLE_FULL": pv660fEvent_SYSTEM_SIZE_TABLE_FULL,
       "pv660fEvent_SYSTEM_USER_LOGGED_IN": pv660fEvent_SYSTEM_USER_LOGGED_IN,
       "pv660fEvent_SYSTEM_USER_LOGGED_OUT": pv660fEvent_SYSTEM_USER_LOGGED_OUT,
       "pv660fEvent_SYSTEM_ALIVE": pv660fEvent_SYSTEM_ALIVE,
       "pv660fEvent_SYSTEM_DEAD": pv660fEvent_SYSTEM_DEAD,
       "pv660fEvent_AUTOBOOT_CHANGED": pv660fEvent_AUTOBOOT_CHANGED,
       "pv660fEvent_CHANNEL_FAILED": pv660fEvent_CHANNEL_FAILED,
       "pv660fEvent_CHANNEL_OK": pv660fEvent_CHANNEL_OK,
       "pv660fEvent_CHANNEL_SCSI_BUS_DEAD": pv660fEvent_CHANNEL_SCSI_BUS_DEAD,
       "pv660fEvent_CHANNEL_SCSI_BUS_ALIVE": pv660fEvent_CHANNEL_SCSI_BUS_ALIVE,
       "pv660fEvent_CHANNEL_FIBER_DEAD": pv660fEvent_CHANNEL_FIBER_DEAD,
       "pv660fEvent_CHANNEL_FIBER_ALIVE": pv660fEvent_CHANNEL_FIBER_ALIVE,
       "pv660fEvent_LOG_EMPTY": pv660fEvent_LOG_EMPTY,
       "pv660fEvent_LOG_OUT_SYNC": pv660fEvent_LOG_OUT_SYNC,
       "pv660fEvent_LOG_REQUEST_SENSE": pv660fEvent_LOG_REQUEST_SENSE,
       "pv660fEvent_LOG_SET_RTC": pv660fEvent_LOG_SET_RTC,
       "pv660fEvent_CFG_NEW": pv660fEvent_CFG_NEW,
       "pv660fEvent_CFG_CLEAR": pv660fEvent_CFG_CLEAR,
       "pv660fEvent_CFG_INVALID": pv660fEvent_CFG_INVALID,
       "pv660fEvent_CFG_COD_ACCESS_ERROR": pv660fEvent_CFG_COD_ACCESS_ERROR,
       "pv660fEvent_CFG_COD_CONVERTED": pv660fEvent_CFG_COD_CONVERTED,
       "pv660fEvent_CFG_COD_IMPORT_FAILED": pv660fEvent_CFG_COD_IMPORT_FAILED,
       "pv660fEvent_DEBUG_DUMP_GENERATED": pv660fEvent_DEBUG_DUMP_GENERATED,
       "pv660fEvent_DEBUG_DUMP_GENERATED_PARTNER": pv660fEvent_DEBUG_DUMP_GENERATED_PARTNER,
       "pv660fEvent_FATAL_HANG": pv660fEvent_FATAL_HANG,
       "pv660fEvent_FATAL_BRKP": pv660fEvent_FATAL_BRKP,
       "pv660fEvent_I960_HW_ERR": pv660fEvent_I960_HW_ERR,
       "pv660fEvent_SARM_HW_ERR": pv660fEvent_SARM_HW_ERR,
       "pv660fEvent_SYSDEV_BG_INIT_STARTED": pv660fEvent_SYSDEV_BG_INIT_STARTED,
       "pv660fEvent_SYSDEV_BG_INIT_STOPPED": pv660fEvent_SYSDEV_BG_INIT_STOPPED,
       "pv660fEvent_SYSDEV_BG_INIT_PAUSED": pv660fEvent_SYSDEV_BG_INIT_PAUSED,
       "pv660fEvent_SYSDEV_BG_INIT_RESTARTED": pv660fEvent_SYSDEV_BG_INIT_RESTARTED,
       "pv660fEvent_SYSDEV_BG_INIT_FAILED": pv660fEvent_SYSDEV_BG_INIT_FAILED,
       "pv660fEvent_SYSDEV_BG_INIT_COMPLETED": pv660fEvent_SYSDEV_BG_INIT_COMPLETED,
       "pv660fEvent_CTLDEV_BBU_CALIBRATE_START": pv660fEvent_CTLDEV_BBU_CALIBRATE_START,
       "pv660fEvent_CTLDEV_BBU_CALIBRATE_DONE": pv660fEvent_CTLDEV_BBU_CALIBRATE_DONE,
       "pv660fEvent_CTLDEV_BBU_CALIBRATE_ABORT": pv660fEvent_CTLDEV_BBU_CALIBRATE_ABORT,
       "pv660fEvent_CTLDEV_BBU_NO_BATTERY": pv660fEvent_CTLDEV_BBU_NO_BATTERY,
       "pv660fEvent_SYSDEV_BBULOW_POSSIBLE_DATA_LOSS": pv660fEvent_SYSDEV_BBULOW_POSSIBLE_DATA_LOSS,
       "pv660fEvent_CTLDEV_IN_CLUSTER": pv660fEvent_CTLDEV_IN_CLUSTER,
       "pv660fEvent_CTLDEV_NOT_IN_CLUSTER": pv660fEvent_CTLDEV_NOT_IN_CLUSTER,
       "pv660fEvent_CTLDEV_IMPROPERLY_SHUTDOWN": pv660fEvent_CTLDEV_IMPROPERLY_SHUTDOWN,
       "pv660fEvent_CTLDEV_AUTOMATIC_FLASH_STARTED": pv660fEvent_CTLDEV_AUTOMATIC_FLASH_STARTED,
       "pv660fEvent_CTLDEV_NEGOTIATION_FAILED_JUMPERS": pv660fEvent_CTLDEV_NEGOTIATION_FAILED_JUMPERS,
       "pv660fEvent_CTLDEV_NEGOTIATION_SAME_ID": pv660fEvent_CTLDEV_NEGOTIATION_SAME_ID,
       "pv660fEvent_CTLDEV_NEGOTIATION_BOARD_TYPE": pv660fEvent_CTLDEV_NEGOTIATION_BOARD_TYPE,
       "pv660fEvent_CTLDEV_NEGOTIATION_DISK_CHANNELS": pv660fEvent_CTLDEV_NEGOTIATION_DISK_CHANNELS,
       "pv660fEvent_CTLDEV_NEGOTIATION_HOST_CHANNELS": pv660fEvent_CTLDEV_NEGOTIATION_HOST_CHANNELS,
       "pv660fEvent_CTLDEV_NEGOTIATION_MEMORY_SIZE": pv660fEvent_CTLDEV_NEGOTIATION_MEMORY_SIZE,
       "pv660fEvent_CTLDEV_NEGOTIATION_CACHE_SIZE": pv660fEvent_CTLDEV_NEGOTIATION_CACHE_SIZE,
       "pv660fEvent_PHYSDEV_HOT_SPARE_SMALLER": pv660fEvent_PHYSDEV_HOT_SPARE_SMALLER,
       "pv660fEvent_SES_ERR": pv660fEvent_SES_ERR,
       "pv660fEvent_ENC_SES_ERR": pv660fEvent_ENC_SES_ERR,
       "fsysPro_DISK_CAPACITY_WARNING": fsysPro_DISK_CAPACITY_WARNING,
       "fsysPro_DISK_CAPACITY_ERROR": fsysPro_DISK_CAPACITY_ERROR,
       "controllerNameEv": controllerNameEv,
       "channelNumberEv": channelNumberEv,
       "targetIDEv": targetIDEv,
       "virtualDiskNameEv": virtualDiskNameEv,
       "arrayDiskNameEv": arrayDiskNameEv,
       "oldVDConfigEv": oldVDConfigEv,
       "newVDConfigEv": newVDConfigEv,
       "enclosureNumberEv": enclosureNumberEv,
       "unitNumberEv": unitNumberEv,
       "enclosureNameEv": enclosureNameEv,
       "unitNameEv": unitNameEv,
       "timeEv": timeEv,
       "volumeNameEv": volumeNameEv,
       "enclosureUnitNamesEv": enclosureUnitNamesEv,
       "virtualDiskNameNewEv": virtualDiskNameNewEv,
       "device1NameEv": device1NameEv,
       "senseKeyEv": senseKeyEv,
       "senseCodeEv": senseCodeEv,
       "senseQualifierEv": senseQualifierEv,
       "eMMFWVersion0Ev": eMMFWVersion0Ev,
       "eMMFWVersion1Ev": eMMFWVersion1Ev,
       "rebuildRateEv": rebuildRateEv}
)
