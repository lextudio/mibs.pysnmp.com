# SNMP MIB module (ENTERASYS-POWER-ETHERNET-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-POWER-ETHERNET-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:23 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(pethMainPseEntry,
 pethPsePortEntry) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseEntry",
    "pethPsePortEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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

etsysPowerEthernetMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50)
)
etsysPowerEthernetMibExtMIB.setRevisions(
        ("2009-08-27 20:31",
         "2005-01-10 16:30",
         "2004-08-17 22:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysPowerEthernetObjects_ObjectIdentity = ObjectIdentity
etsysPowerEthernetObjects = _EtsysPowerEthernetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1)
)
_EtsysPsePowerNotification_ObjectIdentity = ObjectIdentity
etsysPsePowerNotification = _EtsysPsePowerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0)
)
_EtsysPseChassisPowerAllocation_ObjectIdentity = ObjectIdentity
etsysPseChassisPowerAllocation = _EtsysPseChassisPowerAllocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1)
)


class _EtsysPseChassisPowerAllocationMode_Type(Integer32):
    """Custom type etsysPseChassisPowerAllocationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_EtsysPseChassisPowerAllocationMode_Type.__name__ = "Integer32"
_EtsysPseChassisPowerAllocationMode_Object = MibScalar
etsysPseChassisPowerAllocationMode = _EtsysPseChassisPowerAllocationMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 1),
    _EtsysPseChassisPowerAllocationMode_Type()
)
etsysPseChassisPowerAllocationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPseChassisPowerAllocationMode.setStatus("current")
_EtsysPseChassisPowerSnmpNotification_Type = EnabledStatus
_EtsysPseChassisPowerSnmpNotification_Object = MibScalar
etsysPseChassisPowerSnmpNotification = _EtsysPseChassisPowerSnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 2),
    _EtsysPseChassisPowerSnmpNotification_Type()
)
etsysPseChassisPowerSnmpNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPseChassisPowerSnmpNotification.setStatus("current")


class _EtsysPseChassisPowerAvailableMaximum_Type(Unsigned32):
    """Custom type etsysPseChassisPowerAvailableMaximum based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EtsysPseChassisPowerAvailableMaximum_Type.__name__ = "Unsigned32"
_EtsysPseChassisPowerAvailableMaximum_Object = MibScalar
etsysPseChassisPowerAvailableMaximum = _EtsysPseChassisPowerAvailableMaximum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 3),
    _EtsysPseChassisPowerAvailableMaximum_Type()
)
etsysPseChassisPowerAvailableMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPseChassisPowerAvailableMaximum.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseChassisPowerAvailableMaximum.setUnits("percent")
_EtsysPseSlotPowerAllocation_ObjectIdentity = ObjectIdentity
etsysPseSlotPowerAllocation = _EtsysPseSlotPowerAllocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2)
)
_EtsysPseSlotPowerAllocationTable_Object = MibTable
etsysPseSlotPowerAllocationTable = _EtsysPseSlotPowerAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysPseSlotPowerAllocationTable.setStatus("current")
_EtsysPseSlotPowerAllocationEntry_Object = MibTableRow
etsysPseSlotPowerAllocationEntry = _EtsysPseSlotPowerAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1)
)
etsysPseSlotPowerAllocationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    etsysPseSlotPowerAllocationEntry.setStatus("current")
_EtsysPseSlotPowerMaximum_Type = Unsigned32
_EtsysPseSlotPowerMaximum_Object = MibTableColumn
etsysPseSlotPowerMaximum = _EtsysPseSlotPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1, 1),
    _EtsysPseSlotPowerMaximum_Type()
)
etsysPseSlotPowerMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPseSlotPowerMaximum.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseSlotPowerMaximum.setUnits("Watts")


class _EtsysPseSlotPowerAssigned_Type(Unsigned32):
    """Custom type etsysPseSlotPowerAssigned based on Unsigned32"""
    defaultValue = 0


_EtsysPseSlotPowerAssigned_Object = MibTableColumn
etsysPseSlotPowerAssigned = _EtsysPseSlotPowerAssigned_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1, 2),
    _EtsysPseSlotPowerAssigned_Type()
)
etsysPseSlotPowerAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPseSlotPowerAssigned.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseSlotPowerAssigned.setUnits("Watts")
_EtsysPseChassisPowerStatus_ObjectIdentity = ObjectIdentity
etsysPseChassisPowerStatus = _EtsysPseChassisPowerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3)
)
_EtsysPseChassisPowerDetected_Type = Gauge32
_EtsysPseChassisPowerDetected_Object = MibScalar
etsysPseChassisPowerDetected = _EtsysPseChassisPowerDetected_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 1),
    _EtsysPseChassisPowerDetected_Type()
)
etsysPseChassisPowerDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPseChassisPowerDetected.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseChassisPowerDetected.setUnits("Watts")
_EtsysPseChassisPowerAvailable_Type = Gauge32
_EtsysPseChassisPowerAvailable_Object = MibScalar
etsysPseChassisPowerAvailable = _EtsysPseChassisPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 2),
    _EtsysPseChassisPowerAvailable_Type()
)
etsysPseChassisPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPseChassisPowerAvailable.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseChassisPowerAvailable.setUnits("Watts")
_EtsysPseChassisPowerConsumable_Type = Gauge32
_EtsysPseChassisPowerConsumable_Object = MibScalar
etsysPseChassisPowerConsumable = _EtsysPseChassisPowerConsumable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 3),
    _EtsysPseChassisPowerConsumable_Type()
)
etsysPseChassisPowerConsumable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPseChassisPowerConsumable.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseChassisPowerConsumable.setUnits("Watts")
_EtsysPseChassisPowerAssigned_Type = Unsigned32
_EtsysPseChassisPowerAssigned_Object = MibScalar
etsysPseChassisPowerAssigned = _EtsysPseChassisPowerAssigned_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 4),
    _EtsysPseChassisPowerAssigned_Type()
)
etsysPseChassisPowerAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPseChassisPowerAssigned.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseChassisPowerAssigned.setUnits("Watts")


class _EtsysPseChassisPowerRedundancy_Type(Integer32):
    """Custom type etsysPseChassisPowerRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundant", 2),
          ("notSupported", 3),
          ("redundant", 1))
    )


_EtsysPseChassisPowerRedundancy_Type.__name__ = "Integer32"
_EtsysPseChassisPowerRedundancy_Object = MibScalar
etsysPseChassisPowerRedundancy = _EtsysPseChassisPowerRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 5),
    _EtsysPseChassisPowerRedundancy_Type()
)
etsysPseChassisPowerRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPseChassisPowerRedundancy.setStatus("current")
_EtsysPsePowerSupplyStatusTable_Object = MibTable
etsysPsePowerSupplyStatusTable = _EtsysPsePowerSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6)
)
if mibBuilder.loadTexts:
    etsysPsePowerSupplyStatusTable.setStatus("current")
_EtsysPsePowerSupplyStatusEntry_Object = MibTableRow
etsysPsePowerSupplyStatusEntry = _EtsysPsePowerSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1)
)
etsysPsePowerSupplyStatusEntry.setIndexNames(
    (0, "ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleNumber"),
)
if mibBuilder.loadTexts:
    etsysPsePowerSupplyStatusEntry.setStatus("current")
_EtsysPsePowerSupplyModuleNumber_Type = Unsigned32
_EtsysPsePowerSupplyModuleNumber_Object = MibTableColumn
etsysPsePowerSupplyModuleNumber = _EtsysPsePowerSupplyModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1, 1),
    _EtsysPsePowerSupplyModuleNumber_Type()
)
etsysPsePowerSupplyModuleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPsePowerSupplyModuleNumber.setStatus("current")


class _EtsysPsePowerSupplyModuleStatus_Type(Integer32):
    """Custom type etsysPsePowerSupplyModuleStatus based on Integer32"""
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
        *(("infoNotAvailable", 1),
          ("installedAndNotOperating", 4),
          ("installedAndOperating", 3),
          ("notInstalled", 2))
    )


_EtsysPsePowerSupplyModuleStatus_Type.__name__ = "Integer32"
_EtsysPsePowerSupplyModuleStatus_Object = MibTableColumn
etsysPsePowerSupplyModuleStatus = _EtsysPsePowerSupplyModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1, 2),
    _EtsysPsePowerSupplyModuleStatus_Type()
)
etsysPsePowerSupplyModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPsePowerSupplyModuleStatus.setStatus("current")
_EtsysPseSlotPowerManagement_ObjectIdentity = ObjectIdentity
etsysPseSlotPowerManagement = _EtsysPseSlotPowerManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4)
)
_EtsysPseModulePowerManagementTable_Object = MibTable
etsysPseModulePowerManagementTable = _EtsysPseModulePowerManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysPseModulePowerManagementTable.setStatus("current")
_EtsysPseModulePowerManagementEntry_Object = MibTableRow
etsysPseModulePowerManagementEntry = _EtsysPseModulePowerManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    etsysPseModulePowerManagementEntry.setStatus("current")


class _EtsysPseModulePowerMode_Type(Integer32):
    """Custom type etsysPseModulePowerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("class", 2),
          ("realtime", 1))
    )


_EtsysPseModulePowerMode_Type.__name__ = "Integer32"
_EtsysPseModulePowerMode_Object = MibTableColumn
etsysPseModulePowerMode = _EtsysPseModulePowerMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 1),
    _EtsysPseModulePowerMode_Type()
)
etsysPseModulePowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPseModulePowerMode.setStatus("current")
_EtsysPseModulePowerClassBudget_Type = Gauge32
_EtsysPseModulePowerClassBudget_Object = MibTableColumn
etsysPseModulePowerClassBudget = _EtsysPseModulePowerClassBudget_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 2),
    _EtsysPseModulePowerClassBudget_Type()
)
etsysPseModulePowerClassBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPseModulePowerClassBudget.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseModulePowerClassBudget.setUnits("Watts")


class _EtsysPseModulePowerUsage_Type(Integer32):
    """Custom type etsysPseModulePowerUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EtsysPseModulePowerUsage_Type.__name__ = "Integer32"
_EtsysPseModulePowerUsage_Object = MibTableColumn
etsysPseModulePowerUsage = _EtsysPseModulePowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 3),
    _EtsysPseModulePowerUsage_Type()
)
etsysPseModulePowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPseModulePowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    etsysPseModulePowerUsage.setUnits("%")
_EtsysPsePortPowerManagement_ObjectIdentity = ObjectIdentity
etsysPsePortPowerManagement = _EtsysPsePortPowerManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5)
)
_EtsysPsePortPowerManagementTable_Object = MibTable
etsysPsePortPowerManagementTable = _EtsysPsePortPowerManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1)
)
if mibBuilder.loadTexts:
    etsysPsePortPowerManagementTable.setStatus("current")
_EtsysPsePortPowerManagementEntry_Object = MibTableRow
etsysPsePortPowerManagementEntry = _EtsysPsePortPowerManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    etsysPsePortPowerManagementEntry.setStatus("current")


class _EtsysPsePortPowerLimit_Type(Integer32):
    """Custom type etsysPsePortPowerLimit based on Integer32"""
    defaultValue = 15400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34000),
    )


_EtsysPsePortPowerLimit_Type.__name__ = "Integer32"
_EtsysPsePortPowerLimit_Object = MibTableColumn
etsysPsePortPowerLimit = _EtsysPsePortPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 1),
    _EtsysPsePortPowerLimit_Type()
)
etsysPsePortPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPsePortPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    etsysPsePortPowerLimit.setUnits("milliwatts")
_EtsysPsePortPowerUsage_Type = Gauge32
_EtsysPsePortPowerUsage_Object = MibTableColumn
etsysPsePortPowerUsage = _EtsysPsePortPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 2),
    _EtsysPsePortPowerUsage_Type()
)
etsysPsePortPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPsePortPowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    etsysPsePortPowerUsage.setUnits("milliwatts")


class _EtsysPsePortPDType_Type(Integer32):
    """Custom type etsysPsePortPDType based on Integer32"""
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
        *(("ieee8023", 4),
          ("ieee8023af", 2),
          ("ieee8023at", 5),
          ("legacy", 1),
          ("other", 3))
    )


_EtsysPsePortPDType_Type.__name__ = "Integer32"
_EtsysPsePortPDType_Object = MibTableColumn
etsysPsePortPDType = _EtsysPsePortPDType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 3),
    _EtsysPsePortPDType_Type()
)
etsysPsePortPDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPsePortPDType.setStatus("current")


class _EtsysPsePortCapability_Type(Bits):
    """Custom type etsysPsePortCapability based on Bits"""
    namedValues = NamedValues(
        *(("ieee8023afCapable", 1),
          ("ieee8023atCapable", 2),
          ("other", 0))
    )

_EtsysPsePortCapability_Type.__name__ = "Bits"
_EtsysPsePortCapability_Object = MibTableColumn
etsysPsePortCapability = _EtsysPsePortCapability_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 4),
    _EtsysPsePortCapability_Type()
)
etsysPsePortCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPsePortCapability.setStatus("current")


class _EtsysPsePortCapabilitySelect_Type(Integer32):
    """Custom type etsysPsePortCapabilitySelect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8023af", 1),
          ("ieee8023at", 2))
    )


_EtsysPsePortCapabilitySelect_Type.__name__ = "Integer32"
_EtsysPsePortCapabilitySelect_Object = MibTableColumn
etsysPsePortCapabilitySelect = _EtsysPsePortCapabilitySelect_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 5),
    _EtsysPsePortCapabilitySelect_Type()
)
etsysPsePortCapabilitySelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPsePortCapabilitySelect.setStatus("current")


class _EtsysPsePortDetectionStatus_Type(Integer32):
    """Custom type etsysPsePortDetectionStatus based on Integer32"""
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
        *(("deliveringPower", 3),
          ("disabled", 1),
          ("fault", 4),
          ("otherFault", 6),
          ("requestingPower", 7),
          ("searching", 2),
          ("test", 5))
    )


_EtsysPsePortDetectionStatus_Type.__name__ = "Integer32"
_EtsysPsePortDetectionStatus_Object = MibTableColumn
etsysPsePortDetectionStatus = _EtsysPsePortDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 6),
    _EtsysPsePortDetectionStatus_Type()
)
etsysPsePortDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPsePortDetectionStatus.setStatus("current")
_EtsysPsePowerAllocationConformance_ObjectIdentity = ObjectIdentity
etsysPsePowerAllocationConformance = _EtsysPsePowerAllocationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2)
)
_EtsysPsePowerAllocationGroups_ObjectIdentity = ObjectIdentity
etsysPsePowerAllocationGroups = _EtsysPsePowerAllocationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1)
)
_EtsysPsePowerAllocationCompliances_ObjectIdentity = ObjectIdentity
etsysPsePowerAllocationCompliances = _EtsysPsePowerAllocationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2)
)
pethMainPseEntry.registerAugmentions(
    ("ENTERASYS-POWER-ETHERNET-EXT-MIB",
     "etsysPseModulePowerManagementEntry")
)
etsysPseModulePowerManagementEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethPsePortEntry.registerAugmentions(
    ("ENTERASYS-POWER-ETHERNET-EXT-MIB",
     "etsysPsePortPowerManagementEntry")
)
etsysPsePortPowerManagementEntry.setIndexNames(*pethPsePortEntry.getIndexNames())

# Managed Objects groups

etsysPsePowerAllocationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 1)
)
etsysPsePowerAllocationControlGroup.setObjects(
      *(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAllocationMode"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerSnmpNotification"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAvailableMaximum"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseSlotPowerMaximum"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseSlotPowerAssigned"))
)
if mibBuilder.loadTexts:
    etsysPsePowerAllocationControlGroup.setStatus("current")

etsysPseChassisPowerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 2)
)
etsysPseChassisPowerStatusGroup.setObjects(
      *(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAvailable"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerConsumable"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAssigned"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerRedundancy"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatus"))
)
if mibBuilder.loadTexts:
    etsysPseChassisPowerStatusGroup.setStatus("current")

etsysPseModulePowerManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 4)
)
etsysPseModulePowerManagementGroup.setObjects(
      *(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerMode"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerClassBudget"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerUsage"))
)
if mibBuilder.loadTexts:
    etsysPseModulePowerManagementGroup.setStatus("current")

etsysPsePortPowerManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 5)
)
etsysPsePortPowerManagementGroup.setObjects(
      *(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerLimit"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerUsage"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPDType"))
)
if mibBuilder.loadTexts:
    etsysPsePortPowerManagementGroup.setStatus("deprecated")

etsysPsePortPowerManagementGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 6)
)
etsysPsePortPowerManagementGroupRev2.setObjects(
      *(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerLimit"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerUsage"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPDType"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortCapability"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortCapabilitySelect"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortDetectionStatus"))
)
if mibBuilder.loadTexts:
    etsysPsePortPowerManagementGroupRev2.setStatus("current")


# Notification objects

etsysPseChassisPowerRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 1)
)
etsysPseChassisPowerRedundant.setObjects(
    ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected")
)
if mibBuilder.loadTexts:
    etsysPseChassisPowerRedundant.setStatus(
        "current"
    )

etsysPseChassisPowerNonRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 2)
)
etsysPseChassisPowerNonRedundant.setObjects(
    ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected")
)
if mibBuilder.loadTexts:
    etsysPseChassisPowerNonRedundant.setStatus(
        "current"
    )

etsysPsePowerSupplyModuleStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 3)
)
etsysPsePowerSupplyModuleStatusChange.setObjects(
    ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatus")
)
if mibBuilder.loadTexts:
    etsysPsePowerSupplyModuleStatusChange.setStatus(
        "current"
    )


# Notifications groups

etsysPsePowerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 3)
)
etsysPsePowerNotificationGroup.setObjects(
      *(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerRedundant"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerNonRedundant"),
        ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatusChange"))
)
if mibBuilder.loadTexts:
    etsysPsePowerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysPsePowerAllocationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysPsePowerAllocationCompliance.setStatus(
        "current"
    )

etsysPsePowerAllocationCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysPsePowerAllocationCompliance2.setStatus(
        "deprecated"
    )

etsysPsePowerAllocationCompliance2Rev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 3)
)
if mibBuilder.loadTexts:
    etsysPsePowerAllocationCompliance2Rev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-POWER-ETHERNET-EXT-MIB",
    **{"etsysPowerEthernetMibExtMIB": etsysPowerEthernetMibExtMIB,
       "etsysPowerEthernetObjects": etsysPowerEthernetObjects,
       "etsysPsePowerNotification": etsysPsePowerNotification,
       "etsysPseChassisPowerRedundant": etsysPseChassisPowerRedundant,
       "etsysPseChassisPowerNonRedundant": etsysPseChassisPowerNonRedundant,
       "etsysPsePowerSupplyModuleStatusChange": etsysPsePowerSupplyModuleStatusChange,
       "etsysPseChassisPowerAllocation": etsysPseChassisPowerAllocation,
       "etsysPseChassisPowerAllocationMode": etsysPseChassisPowerAllocationMode,
       "etsysPseChassisPowerSnmpNotification": etsysPseChassisPowerSnmpNotification,
       "etsysPseChassisPowerAvailableMaximum": etsysPseChassisPowerAvailableMaximum,
       "etsysPseSlotPowerAllocation": etsysPseSlotPowerAllocation,
       "etsysPseSlotPowerAllocationTable": etsysPseSlotPowerAllocationTable,
       "etsysPseSlotPowerAllocationEntry": etsysPseSlotPowerAllocationEntry,
       "etsysPseSlotPowerMaximum": etsysPseSlotPowerMaximum,
       "etsysPseSlotPowerAssigned": etsysPseSlotPowerAssigned,
       "etsysPseChassisPowerStatus": etsysPseChassisPowerStatus,
       "etsysPseChassisPowerDetected": etsysPseChassisPowerDetected,
       "etsysPseChassisPowerAvailable": etsysPseChassisPowerAvailable,
       "etsysPseChassisPowerConsumable": etsysPseChassisPowerConsumable,
       "etsysPseChassisPowerAssigned": etsysPseChassisPowerAssigned,
       "etsysPseChassisPowerRedundancy": etsysPseChassisPowerRedundancy,
       "etsysPsePowerSupplyStatusTable": etsysPsePowerSupplyStatusTable,
       "etsysPsePowerSupplyStatusEntry": etsysPsePowerSupplyStatusEntry,
       "etsysPsePowerSupplyModuleNumber": etsysPsePowerSupplyModuleNumber,
       "etsysPsePowerSupplyModuleStatus": etsysPsePowerSupplyModuleStatus,
       "etsysPseSlotPowerManagement": etsysPseSlotPowerManagement,
       "etsysPseModulePowerManagementTable": etsysPseModulePowerManagementTable,
       "etsysPseModulePowerManagementEntry": etsysPseModulePowerManagementEntry,
       "etsysPseModulePowerMode": etsysPseModulePowerMode,
       "etsysPseModulePowerClassBudget": etsysPseModulePowerClassBudget,
       "etsysPseModulePowerUsage": etsysPseModulePowerUsage,
       "etsysPsePortPowerManagement": etsysPsePortPowerManagement,
       "etsysPsePortPowerManagementTable": etsysPsePortPowerManagementTable,
       "etsysPsePortPowerManagementEntry": etsysPsePortPowerManagementEntry,
       "etsysPsePortPowerLimit": etsysPsePortPowerLimit,
       "etsysPsePortPowerUsage": etsysPsePortPowerUsage,
       "etsysPsePortPDType": etsysPsePortPDType,
       "etsysPsePortCapability": etsysPsePortCapability,
       "etsysPsePortCapabilitySelect": etsysPsePortCapabilitySelect,
       "etsysPsePortDetectionStatus": etsysPsePortDetectionStatus,
       "etsysPsePowerAllocationConformance": etsysPsePowerAllocationConformance,
       "etsysPsePowerAllocationGroups": etsysPsePowerAllocationGroups,
       "etsysPsePowerAllocationControlGroup": etsysPsePowerAllocationControlGroup,
       "etsysPseChassisPowerStatusGroup": etsysPseChassisPowerStatusGroup,
       "etsysPsePowerNotificationGroup": etsysPsePowerNotificationGroup,
       "etsysPseModulePowerManagementGroup": etsysPseModulePowerManagementGroup,
       "etsysPsePortPowerManagementGroup": etsysPsePortPowerManagementGroup,
       "etsysPsePortPowerManagementGroupRev2": etsysPsePortPowerManagementGroupRev2,
       "etsysPsePowerAllocationCompliances": etsysPsePowerAllocationCompliances,
       "etsysPsePowerAllocationCompliance": etsysPsePowerAllocationCompliance,
       "etsysPsePowerAllocationCompliance2": etsysPsePowerAllocationCompliance2,
       "etsysPsePowerAllocationCompliance2Rev2": etsysPsePowerAllocationCompliance2Rev2}
)
