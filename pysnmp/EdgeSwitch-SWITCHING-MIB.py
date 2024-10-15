# SNMP MIB module (EdgeSwitch-SWITCHING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-SWITCHING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:09 2024
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

(AgentLogSeverity,) = mibBuilder.importSymbols(
    "EdgeSwitch-LOGGING-MIB",
    "AgentLogSeverity")

(AgentPortMask,
 fastPath) = mibBuilder.importSymbols(
    "EdgeSwitch-REF-MIB",
    "AgentPortMask",
    "fastPath")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,
 VlanIndex,
 dot1qFdbId,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIndex",
    "dot1qFdbId",
    "dot1qVlanIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathSwitching = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1)
)
fastPathSwitching.setRevisions(
        ("2014-04-09 00:00",
         "2013-11-08 00:00",
         "2013-10-15 00:00",
         "2013-09-10 00:00",
         "2013-07-05 00:00",
         "2013-01-29 00:00",
         "2013-01-07 00:00",
         "2013-01-04 00:00",
         "2011-09-19 00:00",
         "2010-12-19 00:00",
         "2009-11-19 00:00",
         "2010-01-14 00:00",
         "2009-07-23 00:00",
         "2009-07-07 00:00",
         "2009-02-11 00:00",
         "2007-05-23 00:00",
         "2003-11-21 00:00",
         "2003-02-06 18:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


class VlanList(OctetString, TextualConvention):
    status = "current"


class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class Ipv6AddressPrefix(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class Ipv6AddressIfIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class Ipv6IfIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class Ipv6IfIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class PortId(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_FastPathSwitchingTraps_ObjectIdentity = ObjectIdentity
fastPathSwitchingTraps = _FastPathSwitchingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0)
)
_AgentInfoGroup_ObjectIdentity = ObjectIdentity
agentInfoGroup = _AgentInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1)
)
_AgentInventoryGroup_ObjectIdentity = ObjectIdentity
agentInventoryGroup = _AgentInventoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1)
)
_AgentInventorySysDescription_Type = DisplayString
_AgentInventorySysDescription_Object = MibScalar
agentInventorySysDescription = _AgentInventorySysDescription_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 1),
    _AgentInventorySysDescription_Type()
)
agentInventorySysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySysDescription.setStatus("current")
_AgentInventoryMachineType_Type = DisplayString
_AgentInventoryMachineType_Object = MibScalar
agentInventoryMachineType = _AgentInventoryMachineType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 2),
    _AgentInventoryMachineType_Type()
)
agentInventoryMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryMachineType.setStatus("current")
_AgentInventoryMachineModel_Type = DisplayString
_AgentInventoryMachineModel_Object = MibScalar
agentInventoryMachineModel = _AgentInventoryMachineModel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 3),
    _AgentInventoryMachineModel_Type()
)
agentInventoryMachineModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryMachineModel.setStatus("current")
_AgentInventorySerialNumber_Type = DisplayString
_AgentInventorySerialNumber_Object = MibScalar
agentInventorySerialNumber = _AgentInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 4),
    _AgentInventorySerialNumber_Type()
)
agentInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySerialNumber.setStatus("current")
_AgentInventoryFRUNumber_Type = DisplayString
_AgentInventoryFRUNumber_Object = MibScalar
agentInventoryFRUNumber = _AgentInventoryFRUNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 5),
    _AgentInventoryFRUNumber_Type()
)
agentInventoryFRUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryFRUNumber.setStatus("current")
_AgentInventoryMaintenanceLevel_Type = DisplayString
_AgentInventoryMaintenanceLevel_Object = MibScalar
agentInventoryMaintenanceLevel = _AgentInventoryMaintenanceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 6),
    _AgentInventoryMaintenanceLevel_Type()
)
agentInventoryMaintenanceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryMaintenanceLevel.setStatus("current")
_AgentInventoryPartNumber_Type = DisplayString
_AgentInventoryPartNumber_Object = MibScalar
agentInventoryPartNumber = _AgentInventoryPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 7),
    _AgentInventoryPartNumber_Type()
)
agentInventoryPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryPartNumber.setStatus("current")
_AgentInventoryManufacturer_Type = DisplayString
_AgentInventoryManufacturer_Object = MibScalar
agentInventoryManufacturer = _AgentInventoryManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 8),
    _AgentInventoryManufacturer_Type()
)
agentInventoryManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryManufacturer.setStatus("current")
_AgentInventoryBurnedInMacAddress_Type = PhysAddress
_AgentInventoryBurnedInMacAddress_Object = MibScalar
agentInventoryBurnedInMacAddress = _AgentInventoryBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 9),
    _AgentInventoryBurnedInMacAddress_Type()
)
agentInventoryBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryBurnedInMacAddress.setStatus("current")
_AgentInventoryOperatingSystem_Type = DisplayString
_AgentInventoryOperatingSystem_Object = MibScalar
agentInventoryOperatingSystem = _AgentInventoryOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 10),
    _AgentInventoryOperatingSystem_Type()
)
agentInventoryOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryOperatingSystem.setStatus("current")
_AgentInventoryNetworkProcessingDevice_Type = DisplayString
_AgentInventoryNetworkProcessingDevice_Object = MibScalar
agentInventoryNetworkProcessingDevice = _AgentInventoryNetworkProcessingDevice_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 11),
    _AgentInventoryNetworkProcessingDevice_Type()
)
agentInventoryNetworkProcessingDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryNetworkProcessingDevice.setStatus("current")
_AgentInventoryAdditionalPackages_Type = DisplayString
_AgentInventoryAdditionalPackages_Object = MibScalar
agentInventoryAdditionalPackages = _AgentInventoryAdditionalPackages_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 12),
    _AgentInventoryAdditionalPackages_Type()
)
agentInventoryAdditionalPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryAdditionalPackages.setStatus("current")
_AgentInventorySoftwareVersion_Type = DisplayString
_AgentInventorySoftwareVersion_Object = MibScalar
agentInventorySoftwareVersion = _AgentInventorySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 13),
    _AgentInventorySoftwareVersion_Type()
)
agentInventorySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySoftwareVersion.setStatus("current")
_AgentInventoryHardwareVersion_Type = DisplayString
_AgentInventoryHardwareVersion_Object = MibScalar
agentInventoryHardwareVersion = _AgentInventoryHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 1, 14),
    _AgentInventoryHardwareVersion_Type()
)
agentInventoryHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryHardwareVersion.setStatus("current")
_AgentTrapLogGroup_ObjectIdentity = ObjectIdentity
agentTrapLogGroup = _AgentTrapLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 2)
)
_AgentTrapLogTotal_Type = Integer32
_AgentTrapLogTotal_Object = MibScalar
agentTrapLogTotal = _AgentTrapLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 2, 1),
    _AgentTrapLogTotal_Type()
)
agentTrapLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTotal.setStatus("current")
_AgentTrapLogTotalSinceLastViewed_Type = Integer32
_AgentTrapLogTotalSinceLastViewed_Object = MibScalar
agentTrapLogTotalSinceLastViewed = _AgentTrapLogTotalSinceLastViewed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 2, 3),
    _AgentTrapLogTotalSinceLastViewed_Type()
)
agentTrapLogTotalSinceLastViewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTotalSinceLastViewed.setStatus("current")
_AgentTrapLogTable_Object = MibTable
agentTrapLogTable = _AgentTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    agentTrapLogTable.setStatus("current")
_AgentTrapLogEntry_Object = MibTableRow
agentTrapLogEntry = _AgentTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 2, 4, 1)
)
agentTrapLogEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentTrapLogIndex"),
)
if mibBuilder.loadTexts:
    agentTrapLogEntry.setStatus("current")


class _AgentTrapLogIndex_Type(Integer32):
    """Custom type agentTrapLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentTrapLogIndex_Type.__name__ = "Integer32"
_AgentTrapLogIndex_Object = MibTableColumn
agentTrapLogIndex = _AgentTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 2, 4, 1, 1),
    _AgentTrapLogIndex_Type()
)
agentTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogIndex.setStatus("current")
_AgentTrapLogSystemTime_Type = DisplayString
_AgentTrapLogSystemTime_Object = MibTableColumn
agentTrapLogSystemTime = _AgentTrapLogSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 2, 4, 1, 2),
    _AgentTrapLogSystemTime_Type()
)
agentTrapLogSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogSystemTime.setStatus("current")


class _AgentTrapLogTrap_Type(DisplayString):
    """Custom type agentTrapLogTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AgentTrapLogTrap_Type.__name__ = "DisplayString"
_AgentTrapLogTrap_Object = MibTableColumn
agentTrapLogTrap = _AgentTrapLogTrap_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 2, 4, 1, 3),
    _AgentTrapLogTrap_Type()
)
agentTrapLogTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTrap.setStatus("current")
_AgentSupportedMibTable_Object = MibTable
agentSupportedMibTable = _AgentSupportedMibTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    agentSupportedMibTable.setStatus("current")
_AgentSupportedMibEntry_Object = MibTableRow
agentSupportedMibEntry = _AgentSupportedMibEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 3, 1)
)
agentSupportedMibEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSupportedMibIndex"),
)
if mibBuilder.loadTexts:
    agentSupportedMibEntry.setStatus("current")


class _AgentSupportedMibIndex_Type(Integer32):
    """Custom type agentSupportedMibIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSupportedMibIndex_Type.__name__ = "Integer32"
_AgentSupportedMibIndex_Object = MibTableColumn
agentSupportedMibIndex = _AgentSupportedMibIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 3, 1, 1),
    _AgentSupportedMibIndex_Type()
)
agentSupportedMibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSupportedMibIndex.setStatus("current")
_AgentSupportedMibName_Type = DisplayString
_AgentSupportedMibName_Object = MibTableColumn
agentSupportedMibName = _AgentSupportedMibName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 3, 1, 2),
    _AgentSupportedMibName_Type()
)
agentSupportedMibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSupportedMibName.setStatus("current")


class _AgentSupportedMibDescription_Type(DisplayString):
    """Custom type agentSupportedMibDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AgentSupportedMibDescription_Type.__name__ = "DisplayString"
_AgentSupportedMibDescription_Object = MibTableColumn
agentSupportedMibDescription = _AgentSupportedMibDescription_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 3, 1, 3),
    _AgentSupportedMibDescription_Type()
)
agentSupportedMibDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSupportedMibDescription.setStatus("current")
_AgentSwitchCpuProcessGroup_ObjectIdentity = ObjectIdentity
agentSwitchCpuProcessGroup = _AgentSwitchCpuProcessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4)
)
_AgentSwitchCpuProcessMemFree_Type = Integer32
_AgentSwitchCpuProcessMemFree_Object = MibScalar
agentSwitchCpuProcessMemFree = _AgentSwitchCpuProcessMemFree_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 1),
    _AgentSwitchCpuProcessMemFree_Type()
)
agentSwitchCpuProcessMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemFree.setStatus("current")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemFree.setUnits("KBytes")


class _AgentSwitchCpuProcessMemAvailable_Type(Integer32):
    """Custom type agentSwitchCpuProcessMemAvailable based on Integer32"""
    defaultValue = 2


_AgentSwitchCpuProcessMemAvailable_Object = MibScalar
agentSwitchCpuProcessMemAvailable = _AgentSwitchCpuProcessMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 2),
    _AgentSwitchCpuProcessMemAvailable_Type()
)
agentSwitchCpuProcessMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemAvailable.setStatus("current")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemAvailable.setUnits("KBytes")


class _AgentSwitchCpuProcessRisingThreshold_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessRisingThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentSwitchCpuProcessRisingThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessRisingThreshold_Object = MibScalar
agentSwitchCpuProcessRisingThreshold = _AgentSwitchCpuProcessRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 3),
    _AgentSwitchCpuProcessRisingThreshold_Type()
)
agentSwitchCpuProcessRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessRisingThreshold.setStatus("current")


class _AgentSwitchCpuProcessRisingThresholdInterval_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessRisingThresholdInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 86400),
    )


_AgentSwitchCpuProcessRisingThresholdInterval_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessRisingThresholdInterval_Object = MibScalar
agentSwitchCpuProcessRisingThresholdInterval = _AgentSwitchCpuProcessRisingThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 4),
    _AgentSwitchCpuProcessRisingThresholdInterval_Type()
)
agentSwitchCpuProcessRisingThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessRisingThresholdInterval.setStatus("current")


class _AgentSwitchCpuProcessFallingThreshold_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessFallingThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentSwitchCpuProcessFallingThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessFallingThreshold_Object = MibScalar
agentSwitchCpuProcessFallingThreshold = _AgentSwitchCpuProcessFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 5),
    _AgentSwitchCpuProcessFallingThreshold_Type()
)
agentSwitchCpuProcessFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessFallingThreshold.setStatus("current")


class _AgentSwitchCpuProcessFallingThresholdInterval_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessFallingThresholdInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 86400),
    )


_AgentSwitchCpuProcessFallingThresholdInterval_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessFallingThresholdInterval_Object = MibScalar
agentSwitchCpuProcessFallingThresholdInterval = _AgentSwitchCpuProcessFallingThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 6),
    _AgentSwitchCpuProcessFallingThresholdInterval_Type()
)
agentSwitchCpuProcessFallingThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessFallingThresholdInterval.setStatus("current")


class _AgentSwitchCpuProcessFreeMemoryThreshold_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessFreeMemoryThreshold based on Unsigned32"""
    defaultValue = 0


_AgentSwitchCpuProcessFreeMemoryThreshold_Object = MibScalar
agentSwitchCpuProcessFreeMemoryThreshold = _AgentSwitchCpuProcessFreeMemoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 7),
    _AgentSwitchCpuProcessFreeMemoryThreshold_Type()
)
agentSwitchCpuProcessFreeMemoryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessFreeMemoryThreshold.setStatus("current")
_AgentSwitchCpuProcessTable_Object = MibTable
agentSwitchCpuProcessTable = _AgentSwitchCpuProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    agentSwitchCpuProcessTable.setStatus("current")
_AgentSwitchCpuProcessEntry_Object = MibTableRow
agentSwitchCpuProcessEntry = _AgentSwitchCpuProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 8, 1)
)
agentSwitchCpuProcessEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchCpuProcessIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchCpuProcessEntry.setStatus("current")


class _AgentSwitchCpuProcessIndex_Type(Integer32):
    """Custom type agentSwitchCpuProcessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchCpuProcessIndex_Type.__name__ = "Integer32"
_AgentSwitchCpuProcessIndex_Object = MibTableColumn
agentSwitchCpuProcessIndex = _AgentSwitchCpuProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 8, 1, 1),
    _AgentSwitchCpuProcessIndex_Type()
)
agentSwitchCpuProcessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessIndex.setStatus("current")
_AgentSwitchCpuProcessName_Type = DisplayString
_AgentSwitchCpuProcessName_Object = MibTableColumn
agentSwitchCpuProcessName = _AgentSwitchCpuProcessName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 8, 1, 2),
    _AgentSwitchCpuProcessName_Type()
)
agentSwitchCpuProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessName.setStatus("current")
_AgentSwitchCpuProcessPercentageUtilization_Type = DisplayString
_AgentSwitchCpuProcessPercentageUtilization_Object = MibTableColumn
agentSwitchCpuProcessPercentageUtilization = _AgentSwitchCpuProcessPercentageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 8, 1, 3),
    _AgentSwitchCpuProcessPercentageUtilization_Type()
)
agentSwitchCpuProcessPercentageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessPercentageUtilization.setStatus("current")
_AgentSwitchCpuProcessId_Type = DisplayString
_AgentSwitchCpuProcessId_Object = MibTableColumn
agentSwitchCpuProcessId = _AgentSwitchCpuProcessId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 8, 1, 4),
    _AgentSwitchCpuProcessId_Type()
)
agentSwitchCpuProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessId.setStatus("current")
_AgentSwitchCpuProcessTotalUtilization_Type = DisplayString
_AgentSwitchCpuProcessTotalUtilization_Object = MibScalar
agentSwitchCpuProcessTotalUtilization = _AgentSwitchCpuProcessTotalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 4, 9),
    _AgentSwitchCpuProcessTotalUtilization_Type()
)
agentSwitchCpuProcessTotalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessTotalUtilization.setStatus("current")
_AgentSwitchCpuCosQDropGroup_ObjectIdentity = ObjectIdentity
agentSwitchCpuCosQDropGroup = _AgentSwitchCpuCosQDropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 6)
)
_AgentSwitchCpuCosQDropTable_Object = MibTable
agentSwitchCpuCosQDropTable = _AgentSwitchCpuCosQDropTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    agentSwitchCpuCosQDropTable.setStatus("current")
_AgentSwitchCpuCosQDropEntry_Object = MibTableRow
agentSwitchCpuCosQDropEntry = _AgentSwitchCpuCosQDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 6, 1, 1)
)
agentSwitchCpuCosQDropEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchCpuCosQIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchCpuCosQDropEntry.setStatus("current")
_AgentSwitchCpuCosQIndex_Type = Unsigned32
_AgentSwitchCpuCosQIndex_Object = MibTableColumn
agentSwitchCpuCosQIndex = _AgentSwitchCpuCosQIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 6, 1, 1, 1),
    _AgentSwitchCpuCosQIndex_Type()
)
agentSwitchCpuCosQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchCpuCosQIndex.setStatus("current")
_AgentSwitchCpuCosQDrops_Type = Counter32
_AgentSwitchCpuCosQDrops_Object = MibTableColumn
agentSwitchCpuCosQDrops = _AgentSwitchCpuCosQDrops_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 6, 1, 1, 2),
    _AgentSwitchCpuCosQDrops_Type()
)
agentSwitchCpuCosQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuCosQDrops.setStatus("current")
_AgentSwitchMbufGroup_ObjectIdentity = ObjectIdentity
agentSwitchMbufGroup = _AgentSwitchMbufGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7)
)
_AgentSwitchMbufsFree_Type = Gauge32
_AgentSwitchMbufsFree_Object = MibScalar
agentSwitchMbufsFree = _AgentSwitchMbufsFree_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 1),
    _AgentSwitchMbufsFree_Type()
)
agentSwitchMbufsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMbufsFree.setStatus("current")
_AgentSwitchMbufTable_Object = MibTable
agentSwitchMbufTable = _AgentSwitchMbufTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    agentSwitchMbufTable.setStatus("current")
_AgentSwitchMbufEntry_Object = MibTableRow
agentSwitchMbufEntry = _AgentSwitchMbufEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 2, 1)
)
agentSwitchMbufEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufPrio"),
)
if mibBuilder.loadTexts:
    agentSwitchMbufEntry.setStatus("current")
_AgentSwitchMbufPrio_Type = Unsigned32
_AgentSwitchMbufPrio_Object = MibTableColumn
agentSwitchMbufPrio = _AgentSwitchMbufPrio_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 2, 1, 1),
    _AgentSwitchMbufPrio_Type()
)
agentSwitchMbufPrio.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchMbufPrio.setStatus("current")
_AgentSwitchMbufClassName_Type = DisplayString
_AgentSwitchMbufClassName_Object = MibTableColumn
agentSwitchMbufClassName = _AgentSwitchMbufClassName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 2, 1, 2),
    _AgentSwitchMbufClassName_Type()
)
agentSwitchMbufClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMbufClassName.setStatus("current")
_AgentSwitchMbufAllocAttempts_Type = Counter32
_AgentSwitchMbufAllocAttempts_Object = MibTableColumn
agentSwitchMbufAllocAttempts = _AgentSwitchMbufAllocAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 2, 1, 3),
    _AgentSwitchMbufAllocAttempts_Type()
)
agentSwitchMbufAllocAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMbufAllocAttempts.setStatus("current")
_AgentSwitchMbufAllocFails_Type = Counter32
_AgentSwitchMbufAllocFails_Object = MibTableColumn
agentSwitchMbufAllocFails = _AgentSwitchMbufAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 2, 1, 4),
    _AgentSwitchMbufAllocFails_Type()
)
agentSwitchMbufAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMbufAllocFails.setStatus("current")
_AgentSwitchMbufsTotal_Type = Counter32
_AgentSwitchMbufsTotal_Object = MibScalar
agentSwitchMbufsTotal = _AgentSwitchMbufsTotal_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 3),
    _AgentSwitchMbufsTotal_Type()
)
agentSwitchMbufsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMbufsTotal.setStatus("current")
_AgentSwitchMbufsUsed_Type = Counter32
_AgentSwitchMbufsUsed_Object = MibScalar
agentSwitchMbufsUsed = _AgentSwitchMbufsUsed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 1, 7, 4),
    _AgentSwitchMbufsUsed_Type()
)
agentSwitchMbufsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMbufsUsed.setStatus("current")
_AgentConfigGroup_ObjectIdentity = ObjectIdentity
agentConfigGroup = _AgentConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2)
)
_AgentCLIConfigGroup_ObjectIdentity = ObjectIdentity
agentCLIConfigGroup = _AgentCLIConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1)
)
_AgentLoginSessionTable_Object = MibTable
agentLoginSessionTable = _AgentLoginSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    agentLoginSessionTable.setStatus("current")
_AgentLoginSessionEntry_Object = MibTableRow
agentLoginSessionEntry = _AgentLoginSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1)
)
agentLoginSessionEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentLoginSessionIndex"),
)
if mibBuilder.loadTexts:
    agentLoginSessionEntry.setStatus("current")


class _AgentLoginSessionIndex_Type(Integer32):
    """Custom type agentLoginSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentLoginSessionIndex_Type.__name__ = "Integer32"
_AgentLoginSessionIndex_Object = MibTableColumn
agentLoginSessionIndex = _AgentLoginSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 1),
    _AgentLoginSessionIndex_Type()
)
agentLoginSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIndex.setStatus("current")
_AgentLoginSessionUserName_Type = DisplayString
_AgentLoginSessionUserName_Object = MibTableColumn
agentLoginSessionUserName = _AgentLoginSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 2),
    _AgentLoginSessionUserName_Type()
)
agentLoginSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionUserName.setStatus("current")
_AgentLoginSessionIPAddress_Type = IpAddress
_AgentLoginSessionIPAddress_Object = MibTableColumn
agentLoginSessionIPAddress = _AgentLoginSessionIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 3),
    _AgentLoginSessionIPAddress_Type()
)
agentLoginSessionIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIPAddress.setStatus("obsolete")


class _AgentLoginSessionConnectionType_Type(Integer32):
    """Custom type agentLoginSessionConnectionType based on Integer32"""
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
        *(("http", 4),
          ("https", 5),
          ("serial", 1),
          ("ssh", 3),
          ("telnet", 2))
    )


_AgentLoginSessionConnectionType_Type.__name__ = "Integer32"
_AgentLoginSessionConnectionType_Object = MibTableColumn
agentLoginSessionConnectionType = _AgentLoginSessionConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 4),
    _AgentLoginSessionConnectionType_Type()
)
agentLoginSessionConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionConnectionType.setStatus("current")
_AgentLoginSessionIdleTime_Type = TimeTicks
_AgentLoginSessionIdleTime_Object = MibTableColumn
agentLoginSessionIdleTime = _AgentLoginSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 5),
    _AgentLoginSessionIdleTime_Type()
)
agentLoginSessionIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIdleTime.setStatus("current")
_AgentLoginSessionSessionTime_Type = TimeTicks
_AgentLoginSessionSessionTime_Object = MibTableColumn
agentLoginSessionSessionTime = _AgentLoginSessionSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 6),
    _AgentLoginSessionSessionTime_Type()
)
agentLoginSessionSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionSessionTime.setStatus("current")
_AgentLoginSessionStatus_Type = RowStatus
_AgentLoginSessionStatus_Object = MibTableColumn
agentLoginSessionStatus = _AgentLoginSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 7),
    _AgentLoginSessionStatus_Type()
)
agentLoginSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLoginSessionStatus.setStatus("current")
_AgentLoginSessionInetAddressType_Type = InetAddressType
_AgentLoginSessionInetAddressType_Object = MibTableColumn
agentLoginSessionInetAddressType = _AgentLoginSessionInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 8),
    _AgentLoginSessionInetAddressType_Type()
)
agentLoginSessionInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionInetAddressType.setStatus("current")
_AgentLoginSessionInetAddress_Type = InetAddress
_AgentLoginSessionInetAddress_Object = MibTableColumn
agentLoginSessionInetAddress = _AgentLoginSessionInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 1, 1, 9),
    _AgentLoginSessionInetAddress_Type()
)
agentLoginSessionInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionInetAddress.setStatus("current")
_AgentTelnetConfigGroup_ObjectIdentity = ObjectIdentity
agentTelnetConfigGroup = _AgentTelnetConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 2)
)


class _AgentTelnetLoginTimeout_Type(Integer32):
    """Custom type agentTelnetLoginTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_AgentTelnetLoginTimeout_Type.__name__ = "Integer32"
_AgentTelnetLoginTimeout_Object = MibScalar
agentTelnetLoginTimeout = _AgentTelnetLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 2, 1),
    _AgentTelnetLoginTimeout_Type()
)
agentTelnetLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetLoginTimeout.setStatus("current")
_AgentTelnetMaxSessions_Type = Integer32
_AgentTelnetMaxSessions_Object = MibScalar
agentTelnetMaxSessions = _AgentTelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 2, 2),
    _AgentTelnetMaxSessions_Type()
)
agentTelnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetMaxSessions.setStatus("current")


class _AgentTelnetAllowNewMode_Type(Integer32):
    """Custom type agentTelnetAllowNewMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentTelnetAllowNewMode_Type.__name__ = "Integer32"
_AgentTelnetAllowNewMode_Object = MibScalar
agentTelnetAllowNewMode = _AgentTelnetAllowNewMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 2, 3),
    _AgentTelnetAllowNewMode_Type()
)
agentTelnetAllowNewMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetAllowNewMode.setStatus("current")


class _AgentTelnetMgmtPortNum_Type(Integer32):
    """Custom type agentTelnetMgmtPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentTelnetMgmtPortNum_Type.__name__ = "Integer32"
_AgentTelnetMgmtPortNum_Object = MibScalar
agentTelnetMgmtPortNum = _AgentTelnetMgmtPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 2, 4),
    _AgentTelnetMgmtPortNum_Type()
)
agentTelnetMgmtPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetMgmtPortNum.setStatus("current")
_AgentUserConfigGroup_ObjectIdentity = ObjectIdentity
agentUserConfigGroup = _AgentUserConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3)
)


class _AgentUserConfigCreate_Type(DisplayString):
    """Custom type agentUserConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentUserConfigCreate_Type.__name__ = "DisplayString"
_AgentUserConfigCreate_Object = MibScalar
agentUserConfigCreate = _AgentUserConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 1),
    _AgentUserConfigCreate_Type()
)
agentUserConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserConfigCreate.setStatus("current")
_AgentUserConfigTable_Object = MibTable
agentUserConfigTable = _AgentUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    agentUserConfigTable.setStatus("current")
_AgentUserConfigEntry_Object = MibTableRow
agentUserConfigEntry = _AgentUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1)
)
agentUserConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentUserIndex"),
)
if mibBuilder.loadTexts:
    agentUserConfigEntry.setStatus("current")


class _AgentUserIndex_Type(Integer32):
    """Custom type agentUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentUserIndex_Type.__name__ = "Integer32"
_AgentUserIndex_Object = MibTableColumn
agentUserIndex = _AgentUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 1),
    _AgentUserIndex_Type()
)
agentUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentUserIndex.setStatus("current")


class _AgentUserName_Type(DisplayString):
    """Custom type agentUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentUserName_Type.__name__ = "DisplayString"
_AgentUserName_Object = MibTableColumn
agentUserName = _AgentUserName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 2),
    _AgentUserName_Type()
)
agentUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserName.setStatus("current")


class _AgentUserPassword_Type(DisplayString):
    """Custom type agentUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentUserPassword_Type.__name__ = "DisplayString"
_AgentUserPassword_Object = MibTableColumn
agentUserPassword = _AgentUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 3),
    _AgentUserPassword_Type()
)
agentUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserPassword.setStatus("current")


class _AgentUserAccessMode_Type(Integer32):
    """Custom type agentUserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("suspended", 3),
          ("write", 2))
    )


_AgentUserAccessMode_Type.__name__ = "Integer32"
_AgentUserAccessMode_Object = MibTableColumn
agentUserAccessMode = _AgentUserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 4),
    _AgentUserAccessMode_Type()
)
agentUserAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserAccessMode.setStatus("deprecated")
_AgentUserStatus_Type = RowStatus
_AgentUserStatus_Object = MibTableColumn
agentUserStatus = _AgentUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 5),
    _AgentUserStatus_Type()
)
agentUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserStatus.setStatus("current")


class _AgentUserAuthenticationType_Type(Integer32):
    """Custom type agentUserAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hmacmd5", 2),
          ("hmacsha", 3),
          ("none", 1))
    )


_AgentUserAuthenticationType_Type.__name__ = "Integer32"
_AgentUserAuthenticationType_Object = MibTableColumn
agentUserAuthenticationType = _AgentUserAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 6),
    _AgentUserAuthenticationType_Type()
)
agentUserAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserAuthenticationType.setStatus("current")


class _AgentUserEncryptionType_Type(Integer32):
    """Custom type agentUserEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("none", 1))
    )


_AgentUserEncryptionType_Type.__name__ = "Integer32"
_AgentUserEncryptionType_Object = MibTableColumn
agentUserEncryptionType = _AgentUserEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 7),
    _AgentUserEncryptionType_Type()
)
agentUserEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserEncryptionType.setStatus("current")


class _AgentUserEncryptionPassword_Type(DisplayString):
    """Custom type agentUserEncryptionPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_AgentUserEncryptionPassword_Type.__name__ = "DisplayString"
_AgentUserEncryptionPassword_Object = MibTableColumn
agentUserEncryptionPassword = _AgentUserEncryptionPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 8),
    _AgentUserEncryptionPassword_Type()
)
agentUserEncryptionPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserEncryptionPassword.setStatus("current")


class _AgentUserLockoutStatus_Type(Integer32):
    """Custom type agentUserLockoutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentUserLockoutStatus_Type.__name__ = "Integer32"
_AgentUserLockoutStatus_Object = MibTableColumn
agentUserLockoutStatus = _AgentUserLockoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 9),
    _AgentUserLockoutStatus_Type()
)
agentUserLockoutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUserLockoutStatus.setStatus("current")
_AgentUserPasswordExpireTime_Type = DateAndTime
_AgentUserPasswordExpireTime_Object = MibTableColumn
agentUserPasswordExpireTime = _AgentUserPasswordExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 10),
    _AgentUserPasswordExpireTime_Type()
)
agentUserPasswordExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUserPasswordExpireTime.setStatus("current")


class _AgentUserAccessLevel_Type(Integer32):
    """Custom type agentUserAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AgentUserAccessLevel_Type.__name__ = "Integer32"
_AgentUserAccessLevel_Object = MibTableColumn
agentUserAccessLevel = _AgentUserAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 3, 2, 1, 11),
    _AgentUserAccessLevel_Type()
)
agentUserAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserAccessLevel.setStatus("current")
_AgentSerialGroup_ObjectIdentity = ObjectIdentity
agentSerialGroup = _AgentSerialGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 5)
)


class _AgentSerialTimeout_Type(Integer32):
    """Custom type agentSerialTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_AgentSerialTimeout_Type.__name__ = "Integer32"
_AgentSerialTimeout_Object = MibScalar
agentSerialTimeout = _AgentSerialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 5, 1),
    _AgentSerialTimeout_Type()
)
agentSerialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialTimeout.setStatus("current")


class _AgentSerialBaudrate_Type(Integer32):
    """Custom type agentSerialBaudrate based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("baud-115200", 8),
          ("baud-1200", 1),
          ("baud-19200", 5),
          ("baud-2400", 2),
          ("baud-38400", 6),
          ("baud-4800", 3),
          ("baud-57600", 7),
          ("baud-9600", 4))
    )


_AgentSerialBaudrate_Type.__name__ = "Integer32"
_AgentSerialBaudrate_Object = MibScalar
agentSerialBaudrate = _AgentSerialBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 5, 2),
    _AgentSerialBaudrate_Type()
)
agentSerialBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialBaudrate.setStatus("current")
_AgentSerialCharacterSize_Type = Integer32
_AgentSerialCharacterSize_Object = MibScalar
agentSerialCharacterSize = _AgentSerialCharacterSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 5, 3),
    _AgentSerialCharacterSize_Type()
)
agentSerialCharacterSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialCharacterSize.setStatus("current")


class _AgentSerialHWFlowControlMode_Type(Integer32):
    """Custom type agentSerialHWFlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSerialHWFlowControlMode_Type.__name__ = "Integer32"
_AgentSerialHWFlowControlMode_Object = MibScalar
agentSerialHWFlowControlMode = _AgentSerialHWFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 5, 4),
    _AgentSerialHWFlowControlMode_Type()
)
agentSerialHWFlowControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialHWFlowControlMode.setStatus("current")
_AgentSerialStopBits_Type = Integer32
_AgentSerialStopBits_Object = MibScalar
agentSerialStopBits = _AgentSerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 5, 5),
    _AgentSerialStopBits_Type()
)
agentSerialStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialStopBits.setStatus("current")


class _AgentSerialParityType_Type(Integer32):
    """Custom type agentSerialParityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("none", 3),
          ("odd", 2))
    )


_AgentSerialParityType_Type.__name__ = "Integer32"
_AgentSerialParityType_Object = MibScalar
agentSerialParityType = _AgentSerialParityType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 5, 6),
    _AgentSerialParityType_Type()
)
agentSerialParityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialParityType.setStatus("current")
_AgentPasswordManagementConfigGroup_ObjectIdentity = ObjectIdentity
agentPasswordManagementConfigGroup = _AgentPasswordManagementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6)
)


class _AgentPasswordManagementMinLength_Type(Integer32):
    """Custom type agentPasswordManagementMinLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 64),
    )


_AgentPasswordManagementMinLength_Type.__name__ = "Integer32"
_AgentPasswordManagementMinLength_Object = MibScalar
agentPasswordManagementMinLength = _AgentPasswordManagementMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 1),
    _AgentPasswordManagementMinLength_Type()
)
agentPasswordManagementMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementMinLength.setStatus("current")


class _AgentPasswordManagementHistory_Type(Integer32):
    """Custom type agentPasswordManagementHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AgentPasswordManagementHistory_Type.__name__ = "Integer32"
_AgentPasswordManagementHistory_Object = MibScalar
agentPasswordManagementHistory = _AgentPasswordManagementHistory_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 2),
    _AgentPasswordManagementHistory_Type()
)
agentPasswordManagementHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementHistory.setStatus("current")


class _AgentPasswordManagementAging_Type(Integer32):
    """Custom type agentPasswordManagementAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_AgentPasswordManagementAging_Type.__name__ = "Integer32"
_AgentPasswordManagementAging_Object = MibScalar
agentPasswordManagementAging = _AgentPasswordManagementAging_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 3),
    _AgentPasswordManagementAging_Type()
)
agentPasswordManagementAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementAging.setStatus("current")


class _AgentPasswordManagementLockAttempts_Type(Integer32):
    """Custom type agentPasswordManagementLockAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentPasswordManagementLockAttempts_Type.__name__ = "Integer32"
_AgentPasswordManagementLockAttempts_Object = MibScalar
agentPasswordManagementLockAttempts = _AgentPasswordManagementLockAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 4),
    _AgentPasswordManagementLockAttempts_Type()
)
agentPasswordManagementLockAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementLockAttempts.setStatus("current")


class _AgentPasswordManagementPasswordStrengthCheck_Type(Integer32):
    """Custom type agentPasswordManagementPasswordStrengthCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPasswordManagementPasswordStrengthCheck_Type.__name__ = "Integer32"
_AgentPasswordManagementPasswordStrengthCheck_Object = MibScalar
agentPasswordManagementPasswordStrengthCheck = _AgentPasswordManagementPasswordStrengthCheck_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 5),
    _AgentPasswordManagementPasswordStrengthCheck_Type()
)
agentPasswordManagementPasswordStrengthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementPasswordStrengthCheck.setStatus("current")


class _AgentPasswordManagementStrengthMinUpperCase_Type(Integer32):
    """Custom type agentPasswordManagementStrengthMinUpperCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AgentPasswordManagementStrengthMinUpperCase_Type.__name__ = "Integer32"
_AgentPasswordManagementStrengthMinUpperCase_Object = MibScalar
agentPasswordManagementStrengthMinUpperCase = _AgentPasswordManagementStrengthMinUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 6),
    _AgentPasswordManagementStrengthMinUpperCase_Type()
)
agentPasswordManagementStrengthMinUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthMinUpperCase.setStatus("current")


class _AgentPasswordManagementStrengthMinLowerCase_Type(Integer32):
    """Custom type agentPasswordManagementStrengthMinLowerCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AgentPasswordManagementStrengthMinLowerCase_Type.__name__ = "Integer32"
_AgentPasswordManagementStrengthMinLowerCase_Object = MibScalar
agentPasswordManagementStrengthMinLowerCase = _AgentPasswordManagementStrengthMinLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 7),
    _AgentPasswordManagementStrengthMinLowerCase_Type()
)
agentPasswordManagementStrengthMinLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthMinLowerCase.setStatus("current")


class _AgentPasswordManagementStrengthMinNumericNumbers_Type(Integer32):
    """Custom type agentPasswordManagementStrengthMinNumericNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AgentPasswordManagementStrengthMinNumericNumbers_Type.__name__ = "Integer32"
_AgentPasswordManagementStrengthMinNumericNumbers_Object = MibScalar
agentPasswordManagementStrengthMinNumericNumbers = _AgentPasswordManagementStrengthMinNumericNumbers_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 8),
    _AgentPasswordManagementStrengthMinNumericNumbers_Type()
)
agentPasswordManagementStrengthMinNumericNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthMinNumericNumbers.setStatus("current")


class _AgentPasswordManagementStrengthMinSpecialCharacters_Type(Integer32):
    """Custom type agentPasswordManagementStrengthMinSpecialCharacters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AgentPasswordManagementStrengthMinSpecialCharacters_Type.__name__ = "Integer32"
_AgentPasswordManagementStrengthMinSpecialCharacters_Object = MibScalar
agentPasswordManagementStrengthMinSpecialCharacters = _AgentPasswordManagementStrengthMinSpecialCharacters_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 9),
    _AgentPasswordManagementStrengthMinSpecialCharacters_Type()
)
agentPasswordManagementStrengthMinSpecialCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthMinSpecialCharacters.setStatus("current")


class _AgentPasswordManagementStrengthMaxConsecutiveCharacters_Type(Integer32):
    """Custom type agentPasswordManagementStrengthMaxConsecutiveCharacters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AgentPasswordManagementStrengthMaxConsecutiveCharacters_Type.__name__ = "Integer32"
_AgentPasswordManagementStrengthMaxConsecutiveCharacters_Object = MibScalar
agentPasswordManagementStrengthMaxConsecutiveCharacters = _AgentPasswordManagementStrengthMaxConsecutiveCharacters_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 10),
    _AgentPasswordManagementStrengthMaxConsecutiveCharacters_Type()
)
agentPasswordManagementStrengthMaxConsecutiveCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthMaxConsecutiveCharacters.setStatus("current")


class _AgentPasswordManagementStrengthMaxRepeatedCharacters_Type(Integer32):
    """Custom type agentPasswordManagementStrengthMaxRepeatedCharacters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AgentPasswordManagementStrengthMaxRepeatedCharacters_Type.__name__ = "Integer32"
_AgentPasswordManagementStrengthMaxRepeatedCharacters_Object = MibScalar
agentPasswordManagementStrengthMaxRepeatedCharacters = _AgentPasswordManagementStrengthMaxRepeatedCharacters_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 11),
    _AgentPasswordManagementStrengthMaxRepeatedCharacters_Type()
)
agentPasswordManagementStrengthMaxRepeatedCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthMaxRepeatedCharacters.setStatus("current")


class _AgentPasswordManagementStrengthMinCharacterClasses_Type(Integer32):
    """Custom type agentPasswordManagementStrengthMinCharacterClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AgentPasswordManagementStrengthMinCharacterClasses_Type.__name__ = "Integer32"
_AgentPasswordManagementStrengthMinCharacterClasses_Object = MibScalar
agentPasswordManagementStrengthMinCharacterClasses = _AgentPasswordManagementStrengthMinCharacterClasses_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 12),
    _AgentPasswordManagementStrengthMinCharacterClasses_Type()
)
agentPasswordManagementStrengthMinCharacterClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthMinCharacterClasses.setStatus("current")
_AgentPasswordMgmtLastPasswordSetResult_Type = DisplayString
_AgentPasswordMgmtLastPasswordSetResult_Object = MibScalar
agentPasswordMgmtLastPasswordSetResult = _AgentPasswordMgmtLastPasswordSetResult_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 14),
    _AgentPasswordMgmtLastPasswordSetResult_Type()
)
agentPasswordMgmtLastPasswordSetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPasswordMgmtLastPasswordSetResult.setStatus("current")
_AgentPasswordManagementStrengthExcludeKeywordTable_Object = MibTable
agentPasswordManagementStrengthExcludeKeywordTable = _AgentPasswordManagementStrengthExcludeKeywordTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 15)
)
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthExcludeKeywordTable.setStatus("current")
_AgentPasswordManagementStrengthExcludeKeywordEntry_Object = MibTableRow
agentPasswordManagementStrengthExcludeKeywordEntry = _AgentPasswordManagementStrengthExcludeKeywordEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 15, 1)
)
agentPasswordManagementStrengthExcludeKeywordEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPasswordMgmtStrengthExcludeKeyword"),
)
if mibBuilder.loadTexts:
    agentPasswordManagementStrengthExcludeKeywordEntry.setStatus("current")
_AgentPasswordMgmtStrengthExcludeKeyword_Type = DisplayString
_AgentPasswordMgmtStrengthExcludeKeyword_Object = MibTableColumn
agentPasswordMgmtStrengthExcludeKeyword = _AgentPasswordMgmtStrengthExcludeKeyword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 15, 1, 1),
    _AgentPasswordMgmtStrengthExcludeKeyword_Type()
)
agentPasswordMgmtStrengthExcludeKeyword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPasswordMgmtStrengthExcludeKeyword.setStatus("current")
_AgentPasswordMgmtStrengthExcludeKeywordStatus_Type = RowStatus
_AgentPasswordMgmtStrengthExcludeKeywordStatus_Object = MibTableColumn
agentPasswordMgmtStrengthExcludeKeywordStatus = _AgentPasswordMgmtStrengthExcludeKeywordStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 6, 15, 1, 2),
    _AgentPasswordMgmtStrengthExcludeKeywordStatus_Type()
)
agentPasswordMgmtStrengthExcludeKeywordStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentPasswordMgmtStrengthExcludeKeywordStatus.setStatus("current")
_AgentIASUserConfigGroup_ObjectIdentity = ObjectIdentity
agentIASUserConfigGroup = _AgentIASUserConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 7)
)


class _AgentIASUserConfigCreate_Type(DisplayString):
    """Custom type agentIASUserConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentIASUserConfigCreate_Type.__name__ = "DisplayString"
_AgentIASUserConfigCreate_Object = MibScalar
agentIASUserConfigCreate = _AgentIASUserConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 7, 1),
    _AgentIASUserConfigCreate_Type()
)
agentIASUserConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIASUserConfigCreate.setStatus("current")
_AgentIASUserConfigTable_Object = MibTable
agentIASUserConfigTable = _AgentIASUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    agentIASUserConfigTable.setStatus("current")
_AgentIASUserConfigEntry_Object = MibTableRow
agentIASUserConfigEntry = _AgentIASUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 7, 2, 1)
)
agentIASUserConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentIASUserIndex"),
)
if mibBuilder.loadTexts:
    agentIASUserConfigEntry.setStatus("current")


class _AgentIASUserIndex_Type(Integer32):
    """Custom type agentIASUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AgentIASUserIndex_Type.__name__ = "Integer32"
_AgentIASUserIndex_Object = MibTableColumn
agentIASUserIndex = _AgentIASUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 7, 2, 1, 1),
    _AgentIASUserIndex_Type()
)
agentIASUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIASUserIndex.setStatus("current")


class _AgentIASUserName_Type(DisplayString):
    """Custom type agentIASUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentIASUserName_Type.__name__ = "DisplayString"
_AgentIASUserName_Object = MibTableColumn
agentIASUserName = _AgentIASUserName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 7, 2, 1, 2),
    _AgentIASUserName_Type()
)
agentIASUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIASUserName.setStatus("current")


class _AgentIASUserPassword_Type(DisplayString):
    """Custom type agentIASUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentIASUserPassword_Type.__name__ = "DisplayString"
_AgentIASUserPassword_Object = MibTableColumn
agentIASUserPassword = _AgentIASUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 7, 2, 1, 3),
    _AgentIASUserPassword_Type()
)
agentIASUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIASUserPassword.setStatus("current")
_AgentIASUserStatus_Type = RowStatus
_AgentIASUserStatus_Object = MibTableColumn
agentIASUserStatus = _AgentIASUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 7, 2, 1, 4),
    _AgentIASUserStatus_Type()
)
agentIASUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIASUserStatus.setStatus("current")
_AgentCLIBannerMsgConfigGroup_ObjectIdentity = ObjectIdentity
agentCLIBannerMsgConfigGroup = _AgentCLIBannerMsgConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 8)
)
_AgentCLIBannerMessage_Type = OctetString
_AgentCLIBannerMessage_Object = MibScalar
agentCLIBannerMessage = _AgentCLIBannerMessage_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 1, 8, 1),
    _AgentCLIBannerMessage_Type()
)
agentCLIBannerMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCLIBannerMessage.setStatus("current")
_AgentLagConfigGroup_ObjectIdentity = ObjectIdentity
agentLagConfigGroup = _AgentLagConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2)
)


class _AgentLagConfigCreate_Type(DisplayString):
    """Custom type agentLagConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 15),
    )


_AgentLagConfigCreate_Type.__name__ = "DisplayString"
_AgentLagConfigCreate_Object = MibScalar
agentLagConfigCreate = _AgentLagConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 1),
    _AgentLagConfigCreate_Type()
)
agentLagConfigCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagConfigCreate.setStatus("current")
_AgentLagSummaryConfigTable_Object = MibTable
agentLagSummaryConfigTable = _AgentLagSummaryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    agentLagSummaryConfigTable.setStatus("current")
_AgentLagSummaryConfigEntry_Object = MibTableRow
agentLagSummaryConfigEntry = _AgentLagSummaryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1)
)
agentLagSummaryConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentLagSummaryLagIndex"),
)
if mibBuilder.loadTexts:
    agentLagSummaryConfigEntry.setStatus("current")


class _AgentLagSummaryLagIndex_Type(Integer32):
    """Custom type agentLagSummaryLagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentLagSummaryLagIndex_Type.__name__ = "Integer32"
_AgentLagSummaryLagIndex_Object = MibTableColumn
agentLagSummaryLagIndex = _AgentLagSummaryLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 1),
    _AgentLagSummaryLagIndex_Type()
)
agentLagSummaryLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagSummaryLagIndex.setStatus("current")


class _AgentLagSummaryName_Type(DisplayString):
    """Custom type agentLagSummaryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentLagSummaryName_Type.__name__ = "DisplayString"
_AgentLagSummaryName_Object = MibTableColumn
agentLagSummaryName = _AgentLagSummaryName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 2),
    _AgentLagSummaryName_Type()
)
agentLagSummaryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryName.setStatus("current")
_AgentLagSummaryFlushTimer_Type = Integer32
_AgentLagSummaryFlushTimer_Object = MibTableColumn
agentLagSummaryFlushTimer = _AgentLagSummaryFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 3),
    _AgentLagSummaryFlushTimer_Type()
)
agentLagSummaryFlushTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryFlushTimer.setStatus("obsolete")


class _AgentLagSummaryLinkTrap_Type(Integer32):
    """Custom type agentLagSummaryLinkTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLagSummaryLinkTrap_Type.__name__ = "Integer32"
_AgentLagSummaryLinkTrap_Object = MibTableColumn
agentLagSummaryLinkTrap = _AgentLagSummaryLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 4),
    _AgentLagSummaryLinkTrap_Type()
)
agentLagSummaryLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryLinkTrap.setStatus("current")


class _AgentLagSummaryAdminMode_Type(Integer32):
    """Custom type agentLagSummaryAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLagSummaryAdminMode_Type.__name__ = "Integer32"
_AgentLagSummaryAdminMode_Object = MibTableColumn
agentLagSummaryAdminMode = _AgentLagSummaryAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 5),
    _AgentLagSummaryAdminMode_Type()
)
agentLagSummaryAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryAdminMode.setStatus("current")


class _AgentLagSummaryStpMode_Type(Integer32):
    """Custom type agentLagSummaryStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLagSummaryStpMode_Type.__name__ = "Integer32"
_AgentLagSummaryStpMode_Object = MibTableColumn
agentLagSummaryStpMode = _AgentLagSummaryStpMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 6),
    _AgentLagSummaryStpMode_Type()
)
agentLagSummaryStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryStpMode.setStatus("current")
_AgentLagSummaryAddPort_Type = Integer32
_AgentLagSummaryAddPort_Object = MibTableColumn
agentLagSummaryAddPort = _AgentLagSummaryAddPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 7),
    _AgentLagSummaryAddPort_Type()
)
agentLagSummaryAddPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryAddPort.setStatus("current")
_AgentLagSummaryDeletePort_Type = Integer32
_AgentLagSummaryDeletePort_Object = MibTableColumn
agentLagSummaryDeletePort = _AgentLagSummaryDeletePort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 8),
    _AgentLagSummaryDeletePort_Type()
)
agentLagSummaryDeletePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryDeletePort.setStatus("current")
_AgentLagSummaryStatus_Type = RowStatus
_AgentLagSummaryStatus_Object = MibTableColumn
agentLagSummaryStatus = _AgentLagSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 9),
    _AgentLagSummaryStatus_Type()
)
agentLagSummaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryStatus.setStatus("current")


class _AgentLagSummaryType_Type(Integer32):
    """Custom type agentLagSummaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_AgentLagSummaryType_Type.__name__ = "Integer32"
_AgentLagSummaryType_Object = MibTableColumn
agentLagSummaryType = _AgentLagSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 10),
    _AgentLagSummaryType_Type()
)
agentLagSummaryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagSummaryType.setStatus("current")


class _AgentLagSummaryStaticCapability_Type(Integer32):
    """Custom type agentLagSummaryStaticCapability based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLagSummaryStaticCapability_Type.__name__ = "Integer32"
_AgentLagSummaryStaticCapability_Object = MibTableColumn
agentLagSummaryStaticCapability = _AgentLagSummaryStaticCapability_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 11),
    _AgentLagSummaryStaticCapability_Type()
)
agentLagSummaryStaticCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryStaticCapability.setStatus("current")


class _AgentLagSummaryHashOption_Type(Integer32):
    """Custom type agentLagSummaryHashOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AgentLagSummaryHashOption_Type.__name__ = "Integer32"
_AgentLagSummaryHashOption_Object = MibTableColumn
agentLagSummaryHashOption = _AgentLagSummaryHashOption_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 12),
    _AgentLagSummaryHashOption_Type()
)
agentLagSummaryHashOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryHashOption.setStatus("current")


class _AgentLagSummaryMinimumActiveLinks_Type(Integer32):
    """Custom type agentLagSummaryMinimumActiveLinks based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AgentLagSummaryMinimumActiveLinks_Type.__name__ = "Integer32"
_AgentLagSummaryMinimumActiveLinks_Object = MibTableColumn
agentLagSummaryMinimumActiveLinks = _AgentLagSummaryMinimumActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 13),
    _AgentLagSummaryMinimumActiveLinks_Type()
)
agentLagSummaryMinimumActiveLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryMinimumActiveLinks.setStatus("current")


class _AgentLagSummaryLocalPreferenceMode_Type(Integer32):
    """Custom type agentLagSummaryLocalPreferenceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLagSummaryLocalPreferenceMode_Type.__name__ = "Integer32"
_AgentLagSummaryLocalPreferenceMode_Object = MibTableColumn
agentLagSummaryLocalPreferenceMode = _AgentLagSummaryLocalPreferenceMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 14),
    _AgentLagSummaryLocalPreferenceMode_Type()
)
agentLagSummaryLocalPreferenceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryLocalPreferenceMode.setStatus("current")


class _AgentLagSummaryMtuValue_Type(Unsigned32):
    """Custom type agentLagSummaryMtuValue based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 12288),
    )


_AgentLagSummaryMtuValue_Type.__name__ = "Unsigned32"
_AgentLagSummaryMtuValue_Object = MibTableColumn
agentLagSummaryMtuValue = _AgentLagSummaryMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 15),
    _AgentLagSummaryMtuValue_Type()
)
agentLagSummaryMtuValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagSummaryMtuValue.setStatus("current")


class _AgentLagSummaryPortCounter_Type(Integer32):
    """Custom type agentLagSummaryPortCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentLagSummaryPortCounter_Type.__name__ = "Integer32"
_AgentLagSummaryPortCounter_Object = MibTableColumn
agentLagSummaryPortCounter = _AgentLagSummaryPortCounter_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 2, 1, 17),
    _AgentLagSummaryPortCounter_Type()
)
agentLagSummaryPortCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagSummaryPortCounter.setStatus("current")
_AgentLagDetailedConfigTable_Object = MibTable
agentLagDetailedConfigTable = _AgentLagDetailedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    agentLagDetailedConfigTable.setStatus("current")
_AgentLagDetailedConfigEntry_Object = MibTableRow
agentLagDetailedConfigEntry = _AgentLagDetailedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 3, 1)
)
agentLagDetailedConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentLagDetailedLagIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentLagDetailedIfIndex"),
)
if mibBuilder.loadTexts:
    agentLagDetailedConfigEntry.setStatus("current")


class _AgentLagDetailedLagIndex_Type(Integer32):
    """Custom type agentLagDetailedLagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentLagDetailedLagIndex_Type.__name__ = "Integer32"
_AgentLagDetailedLagIndex_Object = MibTableColumn
agentLagDetailedLagIndex = _AgentLagDetailedLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 3, 1, 1),
    _AgentLagDetailedLagIndex_Type()
)
agentLagDetailedLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedLagIndex.setStatus("current")


class _AgentLagDetailedIfIndex_Type(Integer32):
    """Custom type agentLagDetailedIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentLagDetailedIfIndex_Type.__name__ = "Integer32"
_AgentLagDetailedIfIndex_Object = MibTableColumn
agentLagDetailedIfIndex = _AgentLagDetailedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 3, 1, 2),
    _AgentLagDetailedIfIndex_Type()
)
agentLagDetailedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedIfIndex.setStatus("current")
_AgentLagDetailedPortSpeed_Type = ObjectIdentifier
_AgentLagDetailedPortSpeed_Object = MibTableColumn
agentLagDetailedPortSpeed = _AgentLagDetailedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 3, 1, 3),
    _AgentLagDetailedPortSpeed_Type()
)
agentLagDetailedPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedPortSpeed.setStatus("current")


class _AgentLagDetailedPortStatus_Type(Integer32):
    """Custom type agentLagDetailedPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AgentLagDetailedPortStatus_Type.__name__ = "Integer32"
_AgentLagDetailedPortStatus_Object = MibTableColumn
agentLagDetailedPortStatus = _AgentLagDetailedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 3, 1, 4),
    _AgentLagDetailedPortStatus_Type()
)
agentLagDetailedPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedPortStatus.setStatus("current")


class _AgentLagDetailedPortCounter_Type(Integer32):
    """Custom type agentLagDetailedPortCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentLagDetailedPortCounter_Type.__name__ = "Integer32"
_AgentLagDetailedPortCounter_Object = MibTableColumn
agentLagDetailedPortCounter = _AgentLagDetailedPortCounter_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 3, 1, 5),
    _AgentLagDetailedPortCounter_Type()
)
agentLagDetailedPortCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedPortCounter.setStatus("current")


class _AgentLagConfigStaticCapability_Type(Integer32):
    """Custom type agentLagConfigStaticCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLagConfigStaticCapability_Type.__name__ = "Integer32"
_AgentLagConfigStaticCapability_Object = MibScalar
agentLagConfigStaticCapability = _AgentLagConfigStaticCapability_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 4),
    _AgentLagConfigStaticCapability_Type()
)
agentLagConfigStaticCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagConfigStaticCapability.setStatus("obsolete")


class _AgentLagConfigGroupHashOption_Type(Integer32):
    """Custom type agentLagConfigGroupHashOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AgentLagConfigGroupHashOption_Type.__name__ = "Integer32"
_AgentLagConfigGroupHashOption_Object = MibScalar
agentLagConfigGroupHashOption = _AgentLagConfigGroupHashOption_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 5),
    _AgentLagConfigGroupHashOption_Type()
)
agentLagConfigGroupHashOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagConfigGroupHashOption.setStatus("current")


class _AgentLagClearCounters_Type(Integer32):
    """Custom type agentLagClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("normalOperation", 0))
    )


_AgentLagClearCounters_Type.__name__ = "Integer32"
_AgentLagClearCounters_Object = MibScalar
agentLagClearCounters = _AgentLagClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 2, 6),
    _AgentLagClearCounters_Type()
)
agentLagClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagClearCounters.setStatus("current")
_AgentNetworkConfigGroup_ObjectIdentity = ObjectIdentity
agentNetworkConfigGroup = _AgentNetworkConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3)
)
_AgentNetworkIPAddress_Type = IpAddress
_AgentNetworkIPAddress_Object = MibScalar
agentNetworkIPAddress = _AgentNetworkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 1),
    _AgentNetworkIPAddress_Type()
)
agentNetworkIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkIPAddress.setStatus("current")
_AgentNetworkSubnetMask_Type = IpAddress
_AgentNetworkSubnetMask_Object = MibScalar
agentNetworkSubnetMask = _AgentNetworkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 2),
    _AgentNetworkSubnetMask_Type()
)
agentNetworkSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkSubnetMask.setStatus("current")
_AgentNetworkDefaultGateway_Type = IpAddress
_AgentNetworkDefaultGateway_Object = MibScalar
agentNetworkDefaultGateway = _AgentNetworkDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 3),
    _AgentNetworkDefaultGateway_Type()
)
agentNetworkDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDefaultGateway.setStatus("current")
_AgentNetworkBurnedInMacAddress_Type = PhysAddress
_AgentNetworkBurnedInMacAddress_Object = MibScalar
agentNetworkBurnedInMacAddress = _AgentNetworkBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 4),
    _AgentNetworkBurnedInMacAddress_Type()
)
agentNetworkBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkBurnedInMacAddress.setStatus("current")
_AgentNetworkLocalAdminMacAddress_Type = PhysAddress
_AgentNetworkLocalAdminMacAddress_Object = MibScalar
agentNetworkLocalAdminMacAddress = _AgentNetworkLocalAdminMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 5),
    _AgentNetworkLocalAdminMacAddress_Type()
)
agentNetworkLocalAdminMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkLocalAdminMacAddress.setStatus("current")


class _AgentNetworkMacAddressType_Type(Integer32):
    """Custom type agentNetworkMacAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("burned-in", 1),
          ("local", 2))
    )


_AgentNetworkMacAddressType_Type.__name__ = "Integer32"
_AgentNetworkMacAddressType_Object = MibScalar
agentNetworkMacAddressType = _AgentNetworkMacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 6),
    _AgentNetworkMacAddressType_Type()
)
agentNetworkMacAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkMacAddressType.setStatus("current")


class _AgentNetworkConfigProtocol_Type(Integer32):
    """Custom type agentNetworkConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_AgentNetworkConfigProtocol_Type.__name__ = "Integer32"
_AgentNetworkConfigProtocol_Object = MibScalar
agentNetworkConfigProtocol = _AgentNetworkConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 7),
    _AgentNetworkConfigProtocol_Type()
)
agentNetworkConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkConfigProtocol.setStatus("current")


class _AgentNetworkConfigProtocolDhcpRenew_Type(Integer32):
    """Custom type agentNetworkConfigProtocolDhcpRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 0),
          ("renew", 1))
    )


_AgentNetworkConfigProtocolDhcpRenew_Type.__name__ = "Integer32"
_AgentNetworkConfigProtocolDhcpRenew_Object = MibScalar
agentNetworkConfigProtocolDhcpRenew = _AgentNetworkConfigProtocolDhcpRenew_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 8),
    _AgentNetworkConfigProtocolDhcpRenew_Type()
)
agentNetworkConfigProtocolDhcpRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkConfigProtocolDhcpRenew.setStatus("current")


class _AgentNetworkWebMode_Type(Integer32):
    """Custom type agentNetworkWebMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentNetworkWebMode_Type.__name__ = "Integer32"
_AgentNetworkWebMode_Object = MibScalar
agentNetworkWebMode = _AgentNetworkWebMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 9),
    _AgentNetworkWebMode_Type()
)
agentNetworkWebMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkWebMode.setStatus("obsolete")


class _AgentNetworkJavaMode_Type(Integer32):
    """Custom type agentNetworkJavaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentNetworkJavaMode_Type.__name__ = "Integer32"
_AgentNetworkJavaMode_Object = MibScalar
agentNetworkJavaMode = _AgentNetworkJavaMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 10),
    _AgentNetworkJavaMode_Type()
)
agentNetworkJavaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkJavaMode.setStatus("obsolete")


class _AgentNetworkMgmtVlan_Type(Integer32):
    """Custom type agentNetworkMgmtVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentNetworkMgmtVlan_Type.__name__ = "Integer32"
_AgentNetworkMgmtVlan_Object = MibScalar
agentNetworkMgmtVlan = _AgentNetworkMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 11),
    _AgentNetworkMgmtVlan_Type()
)
agentNetworkMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkMgmtVlan.setStatus("current")


class _AgentNetworkIpv6AdminMode_Type(Integer32):
    """Custom type agentNetworkIpv6AdminMode based on Integer32"""
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


_AgentNetworkIpv6AdminMode_Type.__name__ = "Integer32"
_AgentNetworkIpv6AdminMode_Object = MibScalar
agentNetworkIpv6AdminMode = _AgentNetworkIpv6AdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 12),
    _AgentNetworkIpv6AdminMode_Type()
)
agentNetworkIpv6AdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkIpv6AdminMode.setStatus("current")
_AgentNetworkIpv6Gateway_Type = Ipv6AddressPrefix
_AgentNetworkIpv6Gateway_Object = MibScalar
agentNetworkIpv6Gateway = _AgentNetworkIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 13),
    _AgentNetworkIpv6Gateway_Type()
)
agentNetworkIpv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkIpv6Gateway.setStatus("current")
_AgentNetworkIpv6AddrTable_Object = MibTable
agentNetworkIpv6AddrTable = _AgentNetworkIpv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 14)
)
if mibBuilder.loadTexts:
    agentNetworkIpv6AddrTable.setStatus("current")
_AgentNetworkIpv6AddrEntry_Object = MibTableRow
agentNetworkIpv6AddrEntry = _AgentNetworkIpv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 14, 1)
)
agentNetworkIpv6AddrEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentNetworkIpv6AddrPrefix"),
)
if mibBuilder.loadTexts:
    agentNetworkIpv6AddrEntry.setStatus("current")
_AgentNetworkIpv6AddrPrefix_Type = Ipv6AddressPrefix
_AgentNetworkIpv6AddrPrefix_Object = MibTableColumn
agentNetworkIpv6AddrPrefix = _AgentNetworkIpv6AddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 14, 1, 1),
    _AgentNetworkIpv6AddrPrefix_Type()
)
agentNetworkIpv6AddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentNetworkIpv6AddrPrefix.setStatus("current")


class _AgentNetworkIpv6AddrPrefixLength_Type(Integer32):
    """Custom type agentNetworkIpv6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentNetworkIpv6AddrPrefixLength_Type.__name__ = "Integer32"
_AgentNetworkIpv6AddrPrefixLength_Object = MibTableColumn
agentNetworkIpv6AddrPrefixLength = _AgentNetworkIpv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 14, 1, 2),
    _AgentNetworkIpv6AddrPrefixLength_Type()
)
agentNetworkIpv6AddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNetworkIpv6AddrPrefixLength.setStatus("current")


class _AgentNetworkIpv6AddrEuiFlag_Type(Integer32):
    """Custom type agentNetworkIpv6AddrEuiFlag based on Integer32"""
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


_AgentNetworkIpv6AddrEuiFlag_Type.__name__ = "Integer32"
_AgentNetworkIpv6AddrEuiFlag_Object = MibTableColumn
agentNetworkIpv6AddrEuiFlag = _AgentNetworkIpv6AddrEuiFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 14, 1, 3),
    _AgentNetworkIpv6AddrEuiFlag_Type()
)
agentNetworkIpv6AddrEuiFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNetworkIpv6AddrEuiFlag.setStatus("current")
_AgentNetworkIpv6AddrStatus_Type = RowStatus
_AgentNetworkIpv6AddrStatus_Object = MibTableColumn
agentNetworkIpv6AddrStatus = _AgentNetworkIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 14, 1, 4),
    _AgentNetworkIpv6AddrStatus_Type()
)
agentNetworkIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNetworkIpv6AddrStatus.setStatus("current")


class _AgentNetworkIpv6AddressAutoConfig_Type(Integer32):
    """Custom type agentNetworkIpv6AddressAutoConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentNetworkIpv6AddressAutoConfig_Type.__name__ = "Integer32"
_AgentNetworkIpv6AddressAutoConfig_Object = MibScalar
agentNetworkIpv6AddressAutoConfig = _AgentNetworkIpv6AddressAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 15),
    _AgentNetworkIpv6AddressAutoConfig_Type()
)
agentNetworkIpv6AddressAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkIpv6AddressAutoConfig.setStatus("current")


class _AgentNetworkIpv6ConfigProtocol_Type(Integer32):
    """Custom type agentNetworkIpv6ConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("none", 1))
    )


_AgentNetworkIpv6ConfigProtocol_Type.__name__ = "Integer32"
_AgentNetworkIpv6ConfigProtocol_Object = MibScalar
agentNetworkIpv6ConfigProtocol = _AgentNetworkIpv6ConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 16),
    _AgentNetworkIpv6ConfigProtocol_Type()
)
agentNetworkIpv6ConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkIpv6ConfigProtocol.setStatus("current")


class _AgentNetworkDhcp6ClientDuid_Type(DisplayString):
    """Custom type agentNetworkDhcp6ClientDuid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AgentNetworkDhcp6ClientDuid_Type.__name__ = "DisplayString"
_AgentNetworkDhcp6ClientDuid_Object = MibScalar
agentNetworkDhcp6ClientDuid = _AgentNetworkDhcp6ClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 17),
    _AgentNetworkDhcp6ClientDuid_Type()
)
agentNetworkDhcp6ClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6ClientDuid.setStatus("current")
_AgentNetworkStatsGroup_ObjectIdentity = ObjectIdentity
agentNetworkStatsGroup = _AgentNetworkStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18)
)
_AgentNetworkDhcp6ADVERTISEMessagesReceived_Type = Counter32
_AgentNetworkDhcp6ADVERTISEMessagesReceived_Object = MibScalar
agentNetworkDhcp6ADVERTISEMessagesReceived = _AgentNetworkDhcp6ADVERTISEMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 1),
    _AgentNetworkDhcp6ADVERTISEMessagesReceived_Type()
)
agentNetworkDhcp6ADVERTISEMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6ADVERTISEMessagesReceived.setStatus("current")
_AgentNetworkDhcp6REPLYMessagesReceived_Type = Counter32
_AgentNetworkDhcp6REPLYMessagesReceived_Object = MibScalar
agentNetworkDhcp6REPLYMessagesReceived = _AgentNetworkDhcp6REPLYMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 2),
    _AgentNetworkDhcp6REPLYMessagesReceived_Type()
)
agentNetworkDhcp6REPLYMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6REPLYMessagesReceived.setStatus("current")
_AgentNetworkDhcp6ADVERTISEMessagesDiscarded_Type = Counter32
_AgentNetworkDhcp6ADVERTISEMessagesDiscarded_Object = MibScalar
agentNetworkDhcp6ADVERTISEMessagesDiscarded = _AgentNetworkDhcp6ADVERTISEMessagesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 3),
    _AgentNetworkDhcp6ADVERTISEMessagesDiscarded_Type()
)
agentNetworkDhcp6ADVERTISEMessagesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6ADVERTISEMessagesDiscarded.setStatus("current")
_AgentNetworkDhcp6REPLYMessagesDiscarded_Type = Counter32
_AgentNetworkDhcp6REPLYMessagesDiscarded_Object = MibScalar
agentNetworkDhcp6REPLYMessagesDiscarded = _AgentNetworkDhcp6REPLYMessagesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 4),
    _AgentNetworkDhcp6REPLYMessagesDiscarded_Type()
)
agentNetworkDhcp6REPLYMessagesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6REPLYMessagesDiscarded.setStatus("current")
_AgentNetworkDhcp6MalformedMessagesReceived_Type = Counter32
_AgentNetworkDhcp6MalformedMessagesReceived_Object = MibScalar
agentNetworkDhcp6MalformedMessagesReceived = _AgentNetworkDhcp6MalformedMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 5),
    _AgentNetworkDhcp6MalformedMessagesReceived_Type()
)
agentNetworkDhcp6MalformedMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6MalformedMessagesReceived.setStatus("current")
_AgentNetworkDhcp6SOLICITMessagesSent_Type = Counter32
_AgentNetworkDhcp6SOLICITMessagesSent_Object = MibScalar
agentNetworkDhcp6SOLICITMessagesSent = _AgentNetworkDhcp6SOLICITMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 6),
    _AgentNetworkDhcp6SOLICITMessagesSent_Type()
)
agentNetworkDhcp6SOLICITMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6SOLICITMessagesSent.setStatus("current")
_AgentNetworkDhcp6REQUESTMessagesSent_Type = Counter32
_AgentNetworkDhcp6REQUESTMessagesSent_Object = MibScalar
agentNetworkDhcp6REQUESTMessagesSent = _AgentNetworkDhcp6REQUESTMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 7),
    _AgentNetworkDhcp6REQUESTMessagesSent_Type()
)
agentNetworkDhcp6REQUESTMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6REQUESTMessagesSent.setStatus("current")
_AgentNetworkDhcp6RENEWMessagesSent_Type = Counter32
_AgentNetworkDhcp6RENEWMessagesSent_Object = MibScalar
agentNetworkDhcp6RENEWMessagesSent = _AgentNetworkDhcp6RENEWMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 8),
    _AgentNetworkDhcp6RENEWMessagesSent_Type()
)
agentNetworkDhcp6RENEWMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6RENEWMessagesSent.setStatus("current")
_AgentNetworkDhcp6REBINDMessagesSent_Type = Counter32
_AgentNetworkDhcp6REBINDMessagesSent_Object = MibScalar
agentNetworkDhcp6REBINDMessagesSent = _AgentNetworkDhcp6REBINDMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 9),
    _AgentNetworkDhcp6REBINDMessagesSent_Type()
)
agentNetworkDhcp6REBINDMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6REBINDMessagesSent.setStatus("current")
_AgentNetworkDhcp6RELEASEMessagesSent_Type = Counter32
_AgentNetworkDhcp6RELEASEMessagesSent_Object = MibScalar
agentNetworkDhcp6RELEASEMessagesSent = _AgentNetworkDhcp6RELEASEMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 10),
    _AgentNetworkDhcp6RELEASEMessagesSent_Type()
)
agentNetworkDhcp6RELEASEMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkDhcp6RELEASEMessagesSent.setStatus("current")


class _AgentNetworkDhcp6StatsReset_Type(Integer32):
    """Custom type agentNetworkDhcp6StatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentNetworkDhcp6StatsReset_Type.__name__ = "Integer32"
_AgentNetworkDhcp6StatsReset_Object = MibScalar
agentNetworkDhcp6StatsReset = _AgentNetworkDhcp6StatsReset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 3, 18, 11),
    _AgentNetworkDhcp6StatsReset_Type()
)
agentNetworkDhcp6StatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDhcp6StatsReset.setStatus("current")
_AgentServicePortConfigGroup_ObjectIdentity = ObjectIdentity
agentServicePortConfigGroup = _AgentServicePortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4)
)
_AgentServicePortIPAddress_Type = IpAddress
_AgentServicePortIPAddress_Object = MibScalar
agentServicePortIPAddress = _AgentServicePortIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 1),
    _AgentServicePortIPAddress_Type()
)
agentServicePortIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortIPAddress.setStatus("current")
_AgentServicePortSubnetMask_Type = IpAddress
_AgentServicePortSubnetMask_Object = MibScalar
agentServicePortSubnetMask = _AgentServicePortSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 2),
    _AgentServicePortSubnetMask_Type()
)
agentServicePortSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortSubnetMask.setStatus("current")
_AgentServicePortDefaultGateway_Type = IpAddress
_AgentServicePortDefaultGateway_Object = MibScalar
agentServicePortDefaultGateway = _AgentServicePortDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 3),
    _AgentServicePortDefaultGateway_Type()
)
agentServicePortDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDefaultGateway.setStatus("current")
_AgentServicePortBurnedInMacAddress_Type = PhysAddress
_AgentServicePortBurnedInMacAddress_Object = MibScalar
agentServicePortBurnedInMacAddress = _AgentServicePortBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 4),
    _AgentServicePortBurnedInMacAddress_Type()
)
agentServicePortBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortBurnedInMacAddress.setStatus("current")


class _AgentServicePortConfigProtocol_Type(Integer32):
    """Custom type agentServicePortConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_AgentServicePortConfigProtocol_Type.__name__ = "Integer32"
_AgentServicePortConfigProtocol_Object = MibScalar
agentServicePortConfigProtocol = _AgentServicePortConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 5),
    _AgentServicePortConfigProtocol_Type()
)
agentServicePortConfigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortConfigProtocol.setStatus("current")


class _AgentServicePortProtocolDhcpRenew_Type(Integer32):
    """Custom type agentServicePortProtocolDhcpRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 0),
          ("renew", 1))
    )


_AgentServicePortProtocolDhcpRenew_Type.__name__ = "Integer32"
_AgentServicePortProtocolDhcpRenew_Object = MibScalar
agentServicePortProtocolDhcpRenew = _AgentServicePortProtocolDhcpRenew_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 6),
    _AgentServicePortProtocolDhcpRenew_Type()
)
agentServicePortProtocolDhcpRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortProtocolDhcpRenew.setStatus("current")


class _AgentServicePortIpv6AdminMode_Type(Integer32):
    """Custom type agentServicePortIpv6AdminMode based on Integer32"""
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


_AgentServicePortIpv6AdminMode_Type.__name__ = "Integer32"
_AgentServicePortIpv6AdminMode_Object = MibScalar
agentServicePortIpv6AdminMode = _AgentServicePortIpv6AdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 7),
    _AgentServicePortIpv6AdminMode_Type()
)
agentServicePortIpv6AdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortIpv6AdminMode.setStatus("current")
_AgentServicePortIpv6Gateway_Type = Ipv6AddressPrefix
_AgentServicePortIpv6Gateway_Object = MibScalar
agentServicePortIpv6Gateway = _AgentServicePortIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 8),
    _AgentServicePortIpv6Gateway_Type()
)
agentServicePortIpv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortIpv6Gateway.setStatus("current")
_AgentServicePortIpv6AddrTable_Object = MibTable
agentServicePortIpv6AddrTable = _AgentServicePortIpv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 9)
)
if mibBuilder.loadTexts:
    agentServicePortIpv6AddrTable.setStatus("current")
_AgentServicePortIpv6AddrEntry_Object = MibTableRow
agentServicePortIpv6AddrEntry = _AgentServicePortIpv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 9, 1)
)
agentServicePortIpv6AddrEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentServicePortIpv6AddrPrefix"),
)
if mibBuilder.loadTexts:
    agentServicePortIpv6AddrEntry.setStatus("current")
_AgentServicePortIpv6AddrPrefix_Type = Ipv6AddressPrefix
_AgentServicePortIpv6AddrPrefix_Object = MibTableColumn
agentServicePortIpv6AddrPrefix = _AgentServicePortIpv6AddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 9, 1, 1),
    _AgentServicePortIpv6AddrPrefix_Type()
)
agentServicePortIpv6AddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentServicePortIpv6AddrPrefix.setStatus("current")


class _AgentServicePortIpv6AddrPrefixLength_Type(Integer32):
    """Custom type agentServicePortIpv6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentServicePortIpv6AddrPrefixLength_Type.__name__ = "Integer32"
_AgentServicePortIpv6AddrPrefixLength_Object = MibTableColumn
agentServicePortIpv6AddrPrefixLength = _AgentServicePortIpv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 9, 1, 2),
    _AgentServicePortIpv6AddrPrefixLength_Type()
)
agentServicePortIpv6AddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortIpv6AddrPrefixLength.setStatus("current")


class _AgentServicePortIpv6AddrEuiFlag_Type(Integer32):
    """Custom type agentServicePortIpv6AddrEuiFlag based on Integer32"""
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


_AgentServicePortIpv6AddrEuiFlag_Type.__name__ = "Integer32"
_AgentServicePortIpv6AddrEuiFlag_Object = MibTableColumn
agentServicePortIpv6AddrEuiFlag = _AgentServicePortIpv6AddrEuiFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 9, 1, 3),
    _AgentServicePortIpv6AddrEuiFlag_Type()
)
agentServicePortIpv6AddrEuiFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortIpv6AddrEuiFlag.setStatus("current")
_AgentServicePortIpv6AddrStatus_Type = RowStatus
_AgentServicePortIpv6AddrStatus_Object = MibTableColumn
agentServicePortIpv6AddrStatus = _AgentServicePortIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 9, 1, 4),
    _AgentServicePortIpv6AddrStatus_Type()
)
agentServicePortIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortIpv6AddrStatus.setStatus("current")


class _AgentServicePortIpv6AddressAutoConfig_Type(Integer32):
    """Custom type agentServicePortIpv6AddressAutoConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentServicePortIpv6AddressAutoConfig_Type.__name__ = "Integer32"
_AgentServicePortIpv6AddressAutoConfig_Object = MibScalar
agentServicePortIpv6AddressAutoConfig = _AgentServicePortIpv6AddressAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 10),
    _AgentServicePortIpv6AddressAutoConfig_Type()
)
agentServicePortIpv6AddressAutoConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortIpv6AddressAutoConfig.setStatus("current")


class _AgentServicePortIpv6ConfigProtocol_Type(Integer32):
    """Custom type agentServicePortIpv6ConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("none", 1))
    )


_AgentServicePortIpv6ConfigProtocol_Type.__name__ = "Integer32"
_AgentServicePortIpv6ConfigProtocol_Object = MibScalar
agentServicePortIpv6ConfigProtocol = _AgentServicePortIpv6ConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 11),
    _AgentServicePortIpv6ConfigProtocol_Type()
)
agentServicePortIpv6ConfigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortIpv6ConfigProtocol.setStatus("current")


class _AgentServicePortDhcp6ClientDuid_Type(DisplayString):
    """Custom type agentServicePortDhcp6ClientDuid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AgentServicePortDhcp6ClientDuid_Type.__name__ = "DisplayString"
_AgentServicePortDhcp6ClientDuid_Object = MibScalar
agentServicePortDhcp6ClientDuid = _AgentServicePortDhcp6ClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 12),
    _AgentServicePortDhcp6ClientDuid_Type()
)
agentServicePortDhcp6ClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6ClientDuid.setStatus("current")
_AgentServicePortStatsGroup_ObjectIdentity = ObjectIdentity
agentServicePortStatsGroup = _AgentServicePortStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13)
)
_AgentServicePortDhcp6ADVERTISEMessagesReceived_Type = Counter32
_AgentServicePortDhcp6ADVERTISEMessagesReceived_Object = MibScalar
agentServicePortDhcp6ADVERTISEMessagesReceived = _AgentServicePortDhcp6ADVERTISEMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 1),
    _AgentServicePortDhcp6ADVERTISEMessagesReceived_Type()
)
agentServicePortDhcp6ADVERTISEMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6ADVERTISEMessagesReceived.setStatus("current")
_AgentServicePortDhcp6REPLYMessagesReceived_Type = Counter32
_AgentServicePortDhcp6REPLYMessagesReceived_Object = MibScalar
agentServicePortDhcp6REPLYMessagesReceived = _AgentServicePortDhcp6REPLYMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 2),
    _AgentServicePortDhcp6REPLYMessagesReceived_Type()
)
agentServicePortDhcp6REPLYMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6REPLYMessagesReceived.setStatus("current")
_AgentServicePortDhcp6ADVERTISEMessagesDiscarded_Type = Counter32
_AgentServicePortDhcp6ADVERTISEMessagesDiscarded_Object = MibScalar
agentServicePortDhcp6ADVERTISEMessagesDiscarded = _AgentServicePortDhcp6ADVERTISEMessagesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 3),
    _AgentServicePortDhcp6ADVERTISEMessagesDiscarded_Type()
)
agentServicePortDhcp6ADVERTISEMessagesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6ADVERTISEMessagesDiscarded.setStatus("current")
_AgentServicePortDhcp6REPLYMessagesDiscarded_Type = Counter32
_AgentServicePortDhcp6REPLYMessagesDiscarded_Object = MibScalar
agentServicePortDhcp6REPLYMessagesDiscarded = _AgentServicePortDhcp6REPLYMessagesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 4),
    _AgentServicePortDhcp6REPLYMessagesDiscarded_Type()
)
agentServicePortDhcp6REPLYMessagesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6REPLYMessagesDiscarded.setStatus("current")
_AgentServicePortDhcp6MalformedMessagesReceived_Type = Counter32
_AgentServicePortDhcp6MalformedMessagesReceived_Object = MibScalar
agentServicePortDhcp6MalformedMessagesReceived = _AgentServicePortDhcp6MalformedMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 5),
    _AgentServicePortDhcp6MalformedMessagesReceived_Type()
)
agentServicePortDhcp6MalformedMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6MalformedMessagesReceived.setStatus("current")
_AgentServicePortDhcp6SOLICITMessagesSent_Type = Counter32
_AgentServicePortDhcp6SOLICITMessagesSent_Object = MibScalar
agentServicePortDhcp6SOLICITMessagesSent = _AgentServicePortDhcp6SOLICITMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 6),
    _AgentServicePortDhcp6SOLICITMessagesSent_Type()
)
agentServicePortDhcp6SOLICITMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6SOLICITMessagesSent.setStatus("current")
_AgentServicePortDhcp6REQUESTMessagesSent_Type = Counter32
_AgentServicePortDhcp6REQUESTMessagesSent_Object = MibScalar
agentServicePortDhcp6REQUESTMessagesSent = _AgentServicePortDhcp6REQUESTMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 7),
    _AgentServicePortDhcp6REQUESTMessagesSent_Type()
)
agentServicePortDhcp6REQUESTMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6REQUESTMessagesSent.setStatus("current")
_AgentServicePortDhcp6RENEWMessagesSent_Type = Counter32
_AgentServicePortDhcp6RENEWMessagesSent_Object = MibScalar
agentServicePortDhcp6RENEWMessagesSent = _AgentServicePortDhcp6RENEWMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 8),
    _AgentServicePortDhcp6RENEWMessagesSent_Type()
)
agentServicePortDhcp6RENEWMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6RENEWMessagesSent.setStatus("current")
_AgentServicePortDhcp6REBINDMessagesSent_Type = Counter32
_AgentServicePortDhcp6REBINDMessagesSent_Object = MibScalar
agentServicePortDhcp6REBINDMessagesSent = _AgentServicePortDhcp6REBINDMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 9),
    _AgentServicePortDhcp6REBINDMessagesSent_Type()
)
agentServicePortDhcp6REBINDMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6REBINDMessagesSent.setStatus("current")
_AgentServicePortDhcp6RELEASEMessagesSent_Type = Counter32
_AgentServicePortDhcp6RELEASEMessagesSent_Object = MibScalar
agentServicePortDhcp6RELEASEMessagesSent = _AgentServicePortDhcp6RELEASEMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 10),
    _AgentServicePortDhcp6RELEASEMessagesSent_Type()
)
agentServicePortDhcp6RELEASEMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortDhcp6RELEASEMessagesSent.setStatus("current")


class _AgentServicePortDhcp6StatsReset_Type(Integer32):
    """Custom type agentServicePortDhcp6StatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentServicePortDhcp6StatsReset_Type.__name__ = "Integer32"
_AgentServicePortDhcp6StatsReset_Object = MibScalar
agentServicePortDhcp6StatsReset = _AgentServicePortDhcp6StatsReset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 4, 13, 11),
    _AgentServicePortDhcp6StatsReset_Type()
)
agentServicePortDhcp6StatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortDhcp6StatsReset.setStatus("current")
_AgentDhcpClientOptionsConfigGroup_ObjectIdentity = ObjectIdentity
agentDhcpClientOptionsConfigGroup = _AgentDhcpClientOptionsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 5)
)
_AgentVendorClassOptionConfigGroup_ObjectIdentity = ObjectIdentity
agentVendorClassOptionConfigGroup = _AgentVendorClassOptionConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 5, 1)
)


class _AgentDhcpClientVendorClassIdMode_Type(TruthValue):
    """Custom type agentDhcpClientVendorClassIdMode based on TruthValue"""


_AgentDhcpClientVendorClassIdMode_Object = MibScalar
agentDhcpClientVendorClassIdMode = _AgentDhcpClientVendorClassIdMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 5, 1, 1),
    _AgentDhcpClientVendorClassIdMode_Type()
)
agentDhcpClientVendorClassIdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpClientVendorClassIdMode.setStatus("current")


class _AgentDhcpClientVendorClassIdString_Type(DisplayString):
    """Custom type agentDhcpClientVendorClassIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentDhcpClientVendorClassIdString_Type.__name__ = "DisplayString"
_AgentDhcpClientVendorClassIdString_Object = MibScalar
agentDhcpClientVendorClassIdString = _AgentDhcpClientVendorClassIdString_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 5, 1, 2),
    _AgentDhcpClientVendorClassIdString_Type()
)
agentDhcpClientVendorClassIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpClientVendorClassIdString.setStatus("current")
_AgentSnmpConfigGroup_ObjectIdentity = ObjectIdentity
agentSnmpConfigGroup = _AgentSnmpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6)
)


class _AgentSnmpCommunityCreate_Type(DisplayString):
    """Custom type agentSnmpCommunityCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpCommunityCreate_Type.__name__ = "DisplayString"
_AgentSnmpCommunityCreate_Object = MibScalar
agentSnmpCommunityCreate = _AgentSnmpCommunityCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 1),
    _AgentSnmpCommunityCreate_Type()
)
agentSnmpCommunityCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityCreate.setStatus("current")
_AgentSnmpCommunityConfigTable_Object = MibTable
agentSnmpCommunityConfigTable = _AgentSnmpCommunityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    agentSnmpCommunityConfigTable.setStatus("current")
_AgentSnmpCommunityConfigEntry_Object = MibTableRow
agentSnmpCommunityConfigEntry = _AgentSnmpCommunityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 2, 1)
)
agentSnmpCommunityConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSnmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    agentSnmpCommunityConfigEntry.setStatus("current")


class _AgentSnmpCommunityIndex_Type(Integer32):
    """Custom type agentSnmpCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSnmpCommunityIndex_Type.__name__ = "Integer32"
_AgentSnmpCommunityIndex_Object = MibTableColumn
agentSnmpCommunityIndex = _AgentSnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 2, 1, 1),
    _AgentSnmpCommunityIndex_Type()
)
agentSnmpCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSnmpCommunityIndex.setStatus("current")


class _AgentSnmpCommunityName_Type(DisplayString):
    """Custom type agentSnmpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpCommunityName_Type.__name__ = "DisplayString"
_AgentSnmpCommunityName_Object = MibTableColumn
agentSnmpCommunityName = _AgentSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 2, 1, 2),
    _AgentSnmpCommunityName_Type()
)
agentSnmpCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityName.setStatus("current")
_AgentSnmpCommunityIPAddress_Type = IpAddress
_AgentSnmpCommunityIPAddress_Object = MibTableColumn
agentSnmpCommunityIPAddress = _AgentSnmpCommunityIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 2, 1, 3),
    _AgentSnmpCommunityIPAddress_Type()
)
agentSnmpCommunityIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityIPAddress.setStatus("current")
_AgentSnmpCommunityIPMask_Type = IpAddress
_AgentSnmpCommunityIPMask_Object = MibTableColumn
agentSnmpCommunityIPMask = _AgentSnmpCommunityIPMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 2, 1, 4),
    _AgentSnmpCommunityIPMask_Type()
)
agentSnmpCommunityIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityIPMask.setStatus("current")


class _AgentSnmpCommunityAccessMode_Type(Integer32):
    """Custom type agentSnmpCommunityAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_AgentSnmpCommunityAccessMode_Type.__name__ = "Integer32"
_AgentSnmpCommunityAccessMode_Object = MibTableColumn
agentSnmpCommunityAccessMode = _AgentSnmpCommunityAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 2, 1, 5),
    _AgentSnmpCommunityAccessMode_Type()
)
agentSnmpCommunityAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityAccessMode.setStatus("current")


class _AgentSnmpCommunityStatus_Type(Integer32):
    """Custom type agentSnmpCommunityStatus based on Integer32"""
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
          ("config", 3),
          ("destroy", 4),
          ("notInService", 2))
    )


_AgentSnmpCommunityStatus_Type.__name__ = "Integer32"
_AgentSnmpCommunityStatus_Object = MibTableColumn
agentSnmpCommunityStatus = _AgentSnmpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 2, 1, 6),
    _AgentSnmpCommunityStatus_Type()
)
agentSnmpCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpCommunityStatus.setStatus("current")


class _AgentSnmpTrapReceiverCreate_Type(DisplayString):
    """Custom type agentSnmpTrapReceiverCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpTrapReceiverCreate_Type.__name__ = "DisplayString"
_AgentSnmpTrapReceiverCreate_Object = MibScalar
agentSnmpTrapReceiverCreate = _AgentSnmpTrapReceiverCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 3),
    _AgentSnmpTrapReceiverCreate_Type()
)
agentSnmpTrapReceiverCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverCreate.setStatus("current")
_AgentSnmpTrapReceiverConfigTable_Object = MibTable
agentSnmpTrapReceiverConfigTable = _AgentSnmpTrapReceiverConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverConfigTable.setStatus("current")
_AgentSnmpTrapReceiverConfigEntry_Object = MibTableRow
agentSnmpTrapReceiverConfigEntry = _AgentSnmpTrapReceiverConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1)
)
agentSnmpTrapReceiverConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSnmpTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverConfigEntry.setStatus("current")


class _AgentSnmpTrapReceiverIndex_Type(Integer32):
    """Custom type agentSnmpTrapReceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSnmpTrapReceiverIndex_Type.__name__ = "Integer32"
_AgentSnmpTrapReceiverIndex_Object = MibTableColumn
agentSnmpTrapReceiverIndex = _AgentSnmpTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1, 1),
    _AgentSnmpTrapReceiverIndex_Type()
)
agentSnmpTrapReceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverIndex.setStatus("current")


class _AgentSnmpTrapReceiverCommunityName_Type(DisplayString):
    """Custom type agentSnmpTrapReceiverCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpTrapReceiverCommunityName_Type.__name__ = "DisplayString"
_AgentSnmpTrapReceiverCommunityName_Object = MibTableColumn
agentSnmpTrapReceiverCommunityName = _AgentSnmpTrapReceiverCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1, 2),
    _AgentSnmpTrapReceiverCommunityName_Type()
)
agentSnmpTrapReceiverCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverCommunityName.setStatus("current")
_AgentSnmpTrapReceiverIPAddress_Type = IpAddress
_AgentSnmpTrapReceiverIPAddress_Object = MibTableColumn
agentSnmpTrapReceiverIPAddress = _AgentSnmpTrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1, 3),
    _AgentSnmpTrapReceiverIPAddress_Type()
)
agentSnmpTrapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverIPAddress.setStatus("obsolete")


class _AgentSnmpTrapReceiverStatus_Type(Integer32):
    """Custom type agentSnmpTrapReceiverStatus based on Integer32"""
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
          ("config", 3),
          ("destroy", 4),
          ("notInService", 2))
    )


_AgentSnmpTrapReceiverStatus_Type.__name__ = "Integer32"
_AgentSnmpTrapReceiverStatus_Object = MibTableColumn
agentSnmpTrapReceiverStatus = _AgentSnmpTrapReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1, 4),
    _AgentSnmpTrapReceiverStatus_Type()
)
agentSnmpTrapReceiverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverStatus.setStatus("current")


class _AgentSnmpTrapReceiverVersion_Type(Integer32):
    """Custom type agentSnmpTrapReceiverVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2))
    )


_AgentSnmpTrapReceiverVersion_Type.__name__ = "Integer32"
_AgentSnmpTrapReceiverVersion_Object = MibTableColumn
agentSnmpTrapReceiverVersion = _AgentSnmpTrapReceiverVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1, 5),
    _AgentSnmpTrapReceiverVersion_Type()
)
agentSnmpTrapReceiverVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverVersion.setStatus("current")
_AgentSnmpTrapReceiverIpv6Address_Type = Ipv6AddressPrefix
_AgentSnmpTrapReceiverIpv6Address_Object = MibTableColumn
agentSnmpTrapReceiverIpv6Address = _AgentSnmpTrapReceiverIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1, 6),
    _AgentSnmpTrapReceiverIpv6Address_Type()
)
agentSnmpTrapReceiverIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverIpv6Address.setStatus("obsolete")


class _AgentSnmpTrapReceiverAddressType_Type(Integer32):
    """Custom type agentSnmpTrapReceiverAddressType based on Integer32"""
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
        *(("dns-v4", 3),
          ("dns-v6", 4),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_AgentSnmpTrapReceiverAddressType_Type.__name__ = "Integer32"
_AgentSnmpTrapReceiverAddressType_Object = MibTableColumn
agentSnmpTrapReceiverAddressType = _AgentSnmpTrapReceiverAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1, 7),
    _AgentSnmpTrapReceiverAddressType_Type()
)
agentSnmpTrapReceiverAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverAddressType.setStatus("current")
_AgentSnmpTrapReceiverAddress_Type = DisplayString
_AgentSnmpTrapReceiverAddress_Object = MibTableColumn
agentSnmpTrapReceiverAddress = _AgentSnmpTrapReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 4, 1, 8),
    _AgentSnmpTrapReceiverAddress_Type()
)
agentSnmpTrapReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverAddress.setStatus("current")
_AgentSnmpTrapFlagsConfigGroup_ObjectIdentity = ObjectIdentity
agentSnmpTrapFlagsConfigGroup = _AgentSnmpTrapFlagsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 5)
)


class _AgentSnmpAuthenticationTrapFlag_Type(Integer32):
    """Custom type agentSnmpAuthenticationTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpAuthenticationTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpAuthenticationTrapFlag_Object = MibScalar
agentSnmpAuthenticationTrapFlag = _AgentSnmpAuthenticationTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 5, 1),
    _AgentSnmpAuthenticationTrapFlag_Type()
)
agentSnmpAuthenticationTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpAuthenticationTrapFlag.setStatus("current")


class _AgentSnmpLinkUpDownTrapFlag_Type(Integer32):
    """Custom type agentSnmpLinkUpDownTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpLinkUpDownTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpLinkUpDownTrapFlag_Object = MibScalar
agentSnmpLinkUpDownTrapFlag = _AgentSnmpLinkUpDownTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 5, 2),
    _AgentSnmpLinkUpDownTrapFlag_Type()
)
agentSnmpLinkUpDownTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpLinkUpDownTrapFlag.setStatus("current")


class _AgentSnmpMultipleUsersTrapFlag_Type(Integer32):
    """Custom type agentSnmpMultipleUsersTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpMultipleUsersTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpMultipleUsersTrapFlag_Object = MibScalar
agentSnmpMultipleUsersTrapFlag = _AgentSnmpMultipleUsersTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 5, 3),
    _AgentSnmpMultipleUsersTrapFlag_Type()
)
agentSnmpMultipleUsersTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpMultipleUsersTrapFlag.setStatus("current")


class _AgentSnmpSpanningTreeTrapFlag_Type(Integer32):
    """Custom type agentSnmpSpanningTreeTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpSpanningTreeTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpSpanningTreeTrapFlag_Object = MibScalar
agentSnmpSpanningTreeTrapFlag = _AgentSnmpSpanningTreeTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 5, 4),
    _AgentSnmpSpanningTreeTrapFlag_Type()
)
agentSnmpSpanningTreeTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpSpanningTreeTrapFlag.setStatus("current")


class _AgentSnmpBroadcastStormTrapFlag_Type(Integer32):
    """Custom type agentSnmpBroadcastStormTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpBroadcastStormTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpBroadcastStormTrapFlag_Object = MibScalar
agentSnmpBroadcastStormTrapFlag = _AgentSnmpBroadcastStormTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 5, 5),
    _AgentSnmpBroadcastStormTrapFlag_Type()
)
agentSnmpBroadcastStormTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpBroadcastStormTrapFlag.setStatus("obsolete")
_AgentSnmpTrapSourceInterface_Type = InterfaceIndexOrZero
_AgentSnmpTrapSourceInterface_Object = MibScalar
agentSnmpTrapSourceInterface = _AgentSnmpTrapSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 6),
    _AgentSnmpTrapSourceInterface_Type()
)
agentSnmpTrapSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapSourceInterface.setStatus("current")


class _AgentSnmpServerPortNum_Type(Integer32):
    """Custom type agentSnmpServerPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(1025, 65535),
    )


_AgentSnmpServerPortNum_Type.__name__ = "Integer32"
_AgentSnmpServerPortNum_Object = MibScalar
agentSnmpServerPortNum = _AgentSnmpServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 6, 7),
    _AgentSnmpServerPortNum_Type()
)
agentSnmpServerPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpServerPortNum.setStatus("current")
_AgentSpanningTreeConfigGroup_ObjectIdentity = ObjectIdentity
agentSpanningTreeConfigGroup = _AgentSpanningTreeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 7)
)


class _AgentSpanningTreeMode_Type(Integer32):
    """Custom type agentSpanningTreeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSpanningTreeMode_Type.__name__ = "Integer32"
_AgentSpanningTreeMode_Object = MibScalar
agentSpanningTreeMode = _AgentSpanningTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 7, 1),
    _AgentSpanningTreeMode_Type()
)
agentSpanningTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSpanningTreeMode.setStatus("obsolete")
_AgentSwitchConfigGroup_ObjectIdentity = ObjectIdentity
agentSwitchConfigGroup = _AgentSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8)
)


class _AgentSwitchFdbAddressAgingTimeout_Type(Integer32):
    """Custom type agentSwitchFdbAddressAgingTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AgentSwitchFdbAddressAgingTimeout_Type.__name__ = "Integer32"
_AgentSwitchFdbAddressAgingTimeout_Object = MibScalar
agentSwitchFdbAddressAgingTimeout = _AgentSwitchFdbAddressAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 3),
    _AgentSwitchFdbAddressAgingTimeout_Type()
)
agentSwitchFdbAddressAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchFdbAddressAgingTimeout.setStatus("current")
_AgentSwitchAddressAgingTimeoutTable_Object = MibTable
agentSwitchAddressAgingTimeoutTable = _AgentSwitchAddressAgingTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeoutTable.setStatus("deprecated")
_AgentSwitchAddressAgingTimeoutEntry_Object = MibTableRow
agentSwitchAddressAgingTimeoutEntry = _AgentSwitchAddressAgingTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 4, 1)
)
agentSwitchAddressAgingTimeoutEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeoutEntry.setStatus("deprecated")


class _AgentSwitchAddressAgingTimeout_Type(Integer32):
    """Custom type agentSwitchAddressAgingTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AgentSwitchAddressAgingTimeout_Type.__name__ = "Integer32"
_AgentSwitchAddressAgingTimeout_Object = MibTableColumn
agentSwitchAddressAgingTimeout = _AgentSwitchAddressAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 4, 1, 1),
    _AgentSwitchAddressAgingTimeout_Type()
)
agentSwitchAddressAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeout.setStatus("deprecated")
_AgentSwitchStaticMacFilteringTable_Object = MibTable
agentSwitchStaticMacFilteringTable = _AgentSwitchStaticMacFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    agentSwitchStaticMacFilteringTable.setStatus("current")
_AgentSwitchStaticMacFilteringEntry_Object = MibTableRow
agentSwitchStaticMacFilteringEntry = _AgentSwitchStaticMacFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 5, 1)
)
agentSwitchStaticMacFilteringEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchStaticMacFilteringVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchStaticMacFilteringAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchStaticMacFilteringEntry.setStatus("current")


class _AgentSwitchStaticMacFilteringVlanId_Type(Integer32):
    """Custom type agentSwitchStaticMacFilteringVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchStaticMacFilteringVlanId_Type.__name__ = "Integer32"
_AgentSwitchStaticMacFilteringVlanId_Object = MibTableColumn
agentSwitchStaticMacFilteringVlanId = _AgentSwitchStaticMacFilteringVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 5, 1, 1),
    _AgentSwitchStaticMacFilteringVlanId_Type()
)
agentSwitchStaticMacFilteringVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchStaticMacFilteringVlanId.setStatus("current")
_AgentSwitchStaticMacFilteringAddress_Type = MacAddress
_AgentSwitchStaticMacFilteringAddress_Object = MibTableColumn
agentSwitchStaticMacFilteringAddress = _AgentSwitchStaticMacFilteringAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 5, 1, 2),
    _AgentSwitchStaticMacFilteringAddress_Type()
)
agentSwitchStaticMacFilteringAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchStaticMacFilteringAddress.setStatus("current")
_AgentSwitchStaticMacFilteringSourcePortMask_Type = AgentPortMask
_AgentSwitchStaticMacFilteringSourcePortMask_Object = MibTableColumn
agentSwitchStaticMacFilteringSourcePortMask = _AgentSwitchStaticMacFilteringSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 5, 1, 3),
    _AgentSwitchStaticMacFilteringSourcePortMask_Type()
)
agentSwitchStaticMacFilteringSourcePortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchStaticMacFilteringSourcePortMask.setStatus("current")
_AgentSwitchStaticMacFilteringDestPortMask_Type = AgentPortMask
_AgentSwitchStaticMacFilteringDestPortMask_Object = MibTableColumn
agentSwitchStaticMacFilteringDestPortMask = _AgentSwitchStaticMacFilteringDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 5, 1, 4),
    _AgentSwitchStaticMacFilteringDestPortMask_Type()
)
agentSwitchStaticMacFilteringDestPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchStaticMacFilteringDestPortMask.setStatus("current")
_AgentSwitchStaticMacFilteringStatus_Type = RowStatus
_AgentSwitchStaticMacFilteringStatus_Object = MibTableColumn
agentSwitchStaticMacFilteringStatus = _AgentSwitchStaticMacFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 5, 1, 5),
    _AgentSwitchStaticMacFilteringStatus_Type()
)
agentSwitchStaticMacFilteringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchStaticMacFilteringStatus.setStatus("current")
_AgentSwitchSnoopingGroup_ObjectIdentity = ObjectIdentity
agentSwitchSnoopingGroup = _AgentSwitchSnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 6)
)
_AgentSwitchSnoopingCfgTable_Object = MibTable
agentSwitchSnoopingCfgTable = _AgentSwitchSnoopingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 6, 1)
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingCfgTable.setStatus("current")
_AgentSwitchSnoopingCfgEntry_Object = MibTableRow
agentSwitchSnoopingCfgEntry = _AgentSwitchSnoopingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 6, 1, 1)
)
agentSwitchSnoopingCfgEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingCfgEntry.setStatus("current")
_AgentSwitchSnoopingProtocol_Type = InetAddressType
_AgentSwitchSnoopingProtocol_Object = MibTableColumn
agentSwitchSnoopingProtocol = _AgentSwitchSnoopingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 6, 1, 1, 1),
    _AgentSwitchSnoopingProtocol_Type()
)
agentSwitchSnoopingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingProtocol.setStatus("current")


class _AgentSwitchSnoopingAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchSnoopingAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingAdminMode_Object = MibTableColumn
agentSwitchSnoopingAdminMode = _AgentSwitchSnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 6, 1, 1, 2),
    _AgentSwitchSnoopingAdminMode_Type()
)
agentSwitchSnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingAdminMode.setStatus("current")


class _AgentSwitchSnoopingPortMask_Type(AgentPortMask):
    """Custom type agentSwitchSnoopingPortMask based on AgentPortMask"""
    defaultHexValue = "000000000000"


_AgentSwitchSnoopingPortMask_Object = MibTableColumn
agentSwitchSnoopingPortMask = _AgentSwitchSnoopingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 6, 1, 1, 3),
    _AgentSwitchSnoopingPortMask_Type()
)
agentSwitchSnoopingPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingPortMask.setStatus("current")
_AgentSwitchSnoopingMulticastControlFramesProcessed_Type = Counter32
_AgentSwitchSnoopingMulticastControlFramesProcessed_Object = MibTableColumn
agentSwitchSnoopingMulticastControlFramesProcessed = _AgentSwitchSnoopingMulticastControlFramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 6, 1, 1, 4),
    _AgentSwitchSnoopingMulticastControlFramesProcessed_Type()
)
agentSwitchSnoopingMulticastControlFramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingMulticastControlFramesProcessed.setStatus("current")


class _AgentSwitchSnoopingProxyQuerierAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingProxyQuerierAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchSnoopingProxyQuerierAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingProxyQuerierAdminMode_Object = MibTableColumn
agentSwitchSnoopingProxyQuerierAdminMode = _AgentSwitchSnoopingProxyQuerierAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 6, 1, 1, 5),
    _AgentSwitchSnoopingProxyQuerierAdminMode_Type()
)
agentSwitchSnoopingProxyQuerierAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingProxyQuerierAdminMode.setStatus("current")
_AgentSwitchSnoopingIntfGroup_ObjectIdentity = ObjectIdentity
agentSwitchSnoopingIntfGroup = _AgentSwitchSnoopingIntfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7)
)
_AgentSwitchSnoopingIntfTable_Object = MibTable
agentSwitchSnoopingIntfTable = _AgentSwitchSnoopingIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1)
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfTable.setStatus("current")
_AgentSwitchSnoopingIntfEntry_Object = MibTableRow
agentSwitchSnoopingIntfEntry = _AgentSwitchSnoopingIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1)
)
agentSwitchSnoopingIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfEntry.setStatus("current")


class _AgentSwitchSnoopingIntfIndex_Type(Unsigned32):
    """Custom type agentSwitchSnoopingIntfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSwitchSnoopingIntfIndex_Type.__name__ = "Unsigned32"
_AgentSwitchSnoopingIntfIndex_Object = MibTableColumn
agentSwitchSnoopingIntfIndex = _AgentSwitchSnoopingIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 1),
    _AgentSwitchSnoopingIntfIndex_Type()
)
agentSwitchSnoopingIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfIndex.setStatus("current")


class _AgentSwitchSnoopingIntfAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingIntfAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchSnoopingIntfAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingIntfAdminMode_Object = MibTableColumn
agentSwitchSnoopingIntfAdminMode = _AgentSwitchSnoopingIntfAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 2),
    _AgentSwitchSnoopingIntfAdminMode_Type()
)
agentSwitchSnoopingIntfAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfAdminMode.setStatus("current")


class _AgentSwitchSnoopingIntfGroupMembershipInterval_Type(Integer32):
    """Custom type agentSwitchSnoopingIntfGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_AgentSwitchSnoopingIntfGroupMembershipInterval_Type.__name__ = "Integer32"
_AgentSwitchSnoopingIntfGroupMembershipInterval_Object = MibTableColumn
agentSwitchSnoopingIntfGroupMembershipInterval = _AgentSwitchSnoopingIntfGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 3),
    _AgentSwitchSnoopingIntfGroupMembershipInterval_Type()
)
agentSwitchSnoopingIntfGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfGroupMembershipInterval.setStatus("current")


class _AgentSwitchSnoopingIntfMaxResponseTime_Type(Integer32):
    """Custom type agentSwitchSnoopingIntfMaxResponseTime based on Integer32"""
    defaultValue = 10


_AgentSwitchSnoopingIntfMaxResponseTime_Object = MibTableColumn
agentSwitchSnoopingIntfMaxResponseTime = _AgentSwitchSnoopingIntfMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 4),
    _AgentSwitchSnoopingIntfMaxResponseTime_Type()
)
agentSwitchSnoopingIntfMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfMaxResponseTime.setStatus("current")


class _AgentSwitchSnoopingIntfMRPExpirationTime_Type(Integer32):
    """Custom type agentSwitchSnoopingIntfMRPExpirationTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AgentSwitchSnoopingIntfMRPExpirationTime_Type.__name__ = "Integer32"
_AgentSwitchSnoopingIntfMRPExpirationTime_Object = MibTableColumn
agentSwitchSnoopingIntfMRPExpirationTime = _AgentSwitchSnoopingIntfMRPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 5),
    _AgentSwitchSnoopingIntfMRPExpirationTime_Type()
)
agentSwitchSnoopingIntfMRPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfMRPExpirationTime.setStatus("current")


class _AgentSwitchSnoopingIntfFastLeaveAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingIntfFastLeaveAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchSnoopingIntfFastLeaveAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingIntfFastLeaveAdminMode_Object = MibTableColumn
agentSwitchSnoopingIntfFastLeaveAdminMode = _AgentSwitchSnoopingIntfFastLeaveAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 6),
    _AgentSwitchSnoopingIntfFastLeaveAdminMode_Type()
)
agentSwitchSnoopingIntfFastLeaveAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfFastLeaveAdminMode.setStatus("current")


class _AgentSwitchSnoopingIntfMulticastRouterMode_Type(Integer32):
    """Custom type agentSwitchSnoopingIntfMulticastRouterMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchSnoopingIntfMulticastRouterMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingIntfMulticastRouterMode_Object = MibTableColumn
agentSwitchSnoopingIntfMulticastRouterMode = _AgentSwitchSnoopingIntfMulticastRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 7),
    _AgentSwitchSnoopingIntfMulticastRouterMode_Type()
)
agentSwitchSnoopingIntfMulticastRouterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfMulticastRouterMode.setStatus("current")
_AgentSwitchSnoopingIntfVlanIDs_Type = VlanList
_AgentSwitchSnoopingIntfVlanIDs_Object = MibTableColumn
agentSwitchSnoopingIntfVlanIDs = _AgentSwitchSnoopingIntfVlanIDs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 8),
    _AgentSwitchSnoopingIntfVlanIDs_Type()
)
agentSwitchSnoopingIntfVlanIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfVlanIDs.setStatus("current")


class _AgentSwitchSnoopingIntfProxyQuerierAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingIntfProxyQuerierAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchSnoopingIntfProxyQuerierAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingIntfProxyQuerierAdminMode_Object = MibTableColumn
agentSwitchSnoopingIntfProxyQuerierAdminMode = _AgentSwitchSnoopingIntfProxyQuerierAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 7, 1, 1, 9),
    _AgentSwitchSnoopingIntfProxyQuerierAdminMode_Type()
)
agentSwitchSnoopingIntfProxyQuerierAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingIntfProxyQuerierAdminMode.setStatus("current")
_AgentSwitchSnoopingVlanGroup_ObjectIdentity = ObjectIdentity
agentSwitchSnoopingVlanGroup = _AgentSwitchSnoopingVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8)
)
_AgentSwitchSnoopingVlanTable_Object = MibTable
agentSwitchSnoopingVlanTable = _AgentSwitchSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1)
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanTable.setStatus("current")
_AgentSwitchSnoopingVlanEntry_Object = MibTableRow
agentSwitchSnoopingVlanEntry = _AgentSwitchSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1, 1)
)
agentSwitchSnoopingVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanEntry.setStatus("current")


class _AgentSwitchSnoopingVlanAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingVlanAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSwitchSnoopingVlanAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingVlanAdminMode_Object = MibTableColumn
agentSwitchSnoopingVlanAdminMode = _AgentSwitchSnoopingVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1, 1, 1),
    _AgentSwitchSnoopingVlanAdminMode_Type()
)
agentSwitchSnoopingVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanAdminMode.setStatus("current")


class _AgentSwitchSnoopingVlanGroupMembershipInterval_Type(Integer32):
    """Custom type agentSwitchSnoopingVlanGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_AgentSwitchSnoopingVlanGroupMembershipInterval_Type.__name__ = "Integer32"
_AgentSwitchSnoopingVlanGroupMembershipInterval_Object = MibTableColumn
agentSwitchSnoopingVlanGroupMembershipInterval = _AgentSwitchSnoopingVlanGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1, 1, 2),
    _AgentSwitchSnoopingVlanGroupMembershipInterval_Type()
)
agentSwitchSnoopingVlanGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanGroupMembershipInterval.setStatus("current")


class _AgentSwitchSnoopingVlanMaxResponseTime_Type(Integer32):
    """Custom type agentSwitchSnoopingVlanMaxResponseTime based on Integer32"""
    defaultValue = 10


_AgentSwitchSnoopingVlanMaxResponseTime_Object = MibTableColumn
agentSwitchSnoopingVlanMaxResponseTime = _AgentSwitchSnoopingVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1, 1, 3),
    _AgentSwitchSnoopingVlanMaxResponseTime_Type()
)
agentSwitchSnoopingVlanMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanMaxResponseTime.setStatus("current")


class _AgentSwitchSnoopingVlanFastLeaveAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingVlanFastLeaveAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSwitchSnoopingVlanFastLeaveAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingVlanFastLeaveAdminMode_Object = MibTableColumn
agentSwitchSnoopingVlanFastLeaveAdminMode = _AgentSwitchSnoopingVlanFastLeaveAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1, 1, 4),
    _AgentSwitchSnoopingVlanFastLeaveAdminMode_Type()
)
agentSwitchSnoopingVlanFastLeaveAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanFastLeaveAdminMode.setStatus("current")


class _AgentSwitchSnoopingVlanMRPExpirationTime_Type(Integer32):
    """Custom type agentSwitchSnoopingVlanMRPExpirationTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AgentSwitchSnoopingVlanMRPExpirationTime_Type.__name__ = "Integer32"
_AgentSwitchSnoopingVlanMRPExpirationTime_Object = MibTableColumn
agentSwitchSnoopingVlanMRPExpirationTime = _AgentSwitchSnoopingVlanMRPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1, 1, 5),
    _AgentSwitchSnoopingVlanMRPExpirationTime_Type()
)
agentSwitchSnoopingVlanMRPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanMRPExpirationTime.setStatus("current")


class _AgentSwitchSnoopingVlanReportSuppMode_Type(Integer32):
    """Custom type agentSwitchSnoopingVlanReportSuppMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSwitchSnoopingVlanReportSuppMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingVlanReportSuppMode_Object = MibTableColumn
agentSwitchSnoopingVlanReportSuppMode = _AgentSwitchSnoopingVlanReportSuppMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1, 1, 6),
    _AgentSwitchSnoopingVlanReportSuppMode_Type()
)
agentSwitchSnoopingVlanReportSuppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanReportSuppMode.setStatus("current")


class _AgentSwitchSnoopingVlanProxyQuerierAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingVlanProxyQuerierAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSwitchSnoopingVlanProxyQuerierAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingVlanProxyQuerierAdminMode_Object = MibTableColumn
agentSwitchSnoopingVlanProxyQuerierAdminMode = _AgentSwitchSnoopingVlanProxyQuerierAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 8, 1, 1, 7),
    _AgentSwitchSnoopingVlanProxyQuerierAdminMode_Type()
)
agentSwitchSnoopingVlanProxyQuerierAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingVlanProxyQuerierAdminMode.setStatus("current")
_AgentSwitchVlanStaticMrouterGroup_ObjectIdentity = ObjectIdentity
agentSwitchVlanStaticMrouterGroup = _AgentSwitchVlanStaticMrouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 9)
)
_AgentSwitchVlanStaticMrouterTable_Object = MibTable
agentSwitchVlanStaticMrouterTable = _AgentSwitchVlanStaticMrouterTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 9, 1)
)
if mibBuilder.loadTexts:
    agentSwitchVlanStaticMrouterTable.setStatus("current")
_AgentSwitchVlanStaticMrouterEntry_Object = MibTableRow
agentSwitchVlanStaticMrouterEntry = _AgentSwitchVlanStaticMrouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 9, 1, 1)
)
agentSwitchVlanStaticMrouterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    agentSwitchVlanStaticMrouterEntry.setStatus("current")


class _AgentSwitchVlanStaticMrouterAdminMode_Type(Integer32):
    """Custom type agentSwitchVlanStaticMrouterAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSwitchVlanStaticMrouterAdminMode_Type.__name__ = "Integer32"
_AgentSwitchVlanStaticMrouterAdminMode_Object = MibTableColumn
agentSwitchVlanStaticMrouterAdminMode = _AgentSwitchVlanStaticMrouterAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 9, 1, 1, 1),
    _AgentSwitchVlanStaticMrouterAdminMode_Type()
)
agentSwitchVlanStaticMrouterAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchVlanStaticMrouterAdminMode.setStatus("current")
_AgentSwitchMFDBGroup_ObjectIdentity = ObjectIdentity
agentSwitchMFDBGroup = _AgentSwitchMFDBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10)
)
_AgentSwitchMFDBTable_Object = MibTable
agentSwitchMFDBTable = _AgentSwitchMFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1)
)
if mibBuilder.loadTexts:
    agentSwitchMFDBTable.setStatus("current")
_AgentSwitchMFDBEntry_Object = MibTableRow
agentSwitchMFDBEntry = _AgentSwitchMFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1, 1)
)
agentSwitchMFDBEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchMFDBVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchMFDBMacAddress"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchMFDBProtocolType"),
)
if mibBuilder.loadTexts:
    agentSwitchMFDBEntry.setStatus("current")
_AgentSwitchMFDBVlanId_Type = VlanIndex
_AgentSwitchMFDBVlanId_Object = MibTableColumn
agentSwitchMFDBVlanId = _AgentSwitchMFDBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1, 1, 1),
    _AgentSwitchMFDBVlanId_Type()
)
agentSwitchMFDBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBVlanId.setStatus("current")
_AgentSwitchMFDBMacAddress_Type = MacAddress
_AgentSwitchMFDBMacAddress_Object = MibTableColumn
agentSwitchMFDBMacAddress = _AgentSwitchMFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1, 1, 2),
    _AgentSwitchMFDBMacAddress_Type()
)
agentSwitchMFDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBMacAddress.setStatus("current")


class _AgentSwitchMFDBProtocolType_Type(Integer32):
    """Custom type agentSwitchMFDBProtocolType based on Integer32"""
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
        *(("gmrp", 2),
          ("igmp", 3),
          ("mld", 4),
          ("static", 1))
    )


_AgentSwitchMFDBProtocolType_Type.__name__ = "Integer32"
_AgentSwitchMFDBProtocolType_Object = MibTableColumn
agentSwitchMFDBProtocolType = _AgentSwitchMFDBProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1, 1, 3),
    _AgentSwitchMFDBProtocolType_Type()
)
agentSwitchMFDBProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBProtocolType.setStatus("current")


class _AgentSwitchMFDBType_Type(Integer32):
    """Custom type agentSwitchMFDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_AgentSwitchMFDBType_Type.__name__ = "Integer32"
_AgentSwitchMFDBType_Object = MibTableColumn
agentSwitchMFDBType = _AgentSwitchMFDBType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1, 1, 4),
    _AgentSwitchMFDBType_Type()
)
agentSwitchMFDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBType.setStatus("current")
_AgentSwitchMFDBDescription_Type = DisplayString
_AgentSwitchMFDBDescription_Object = MibTableColumn
agentSwitchMFDBDescription = _AgentSwitchMFDBDescription_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1, 1, 5),
    _AgentSwitchMFDBDescription_Type()
)
agentSwitchMFDBDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBDescription.setStatus("current")
_AgentSwitchMFDBForwardingPortMask_Type = AgentPortMask
_AgentSwitchMFDBForwardingPortMask_Object = MibTableColumn
agentSwitchMFDBForwardingPortMask = _AgentSwitchMFDBForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1, 1, 6),
    _AgentSwitchMFDBForwardingPortMask_Type()
)
agentSwitchMFDBForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBForwardingPortMask.setStatus("current")
_AgentSwitchMFDBFilteringPortMask_Type = AgentPortMask
_AgentSwitchMFDBFilteringPortMask_Object = MibTableColumn
agentSwitchMFDBFilteringPortMask = _AgentSwitchMFDBFilteringPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 1, 1, 7),
    _AgentSwitchMFDBFilteringPortMask_Type()
)
agentSwitchMFDBFilteringPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBFilteringPortMask.setStatus("current")
_AgentSwitchMFDBSummaryTable_Object = MibTable
agentSwitchMFDBSummaryTable = _AgentSwitchMFDBSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 2)
)
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryTable.setStatus("current")
_AgentSwitchMFDBSummaryEntry_Object = MibTableRow
agentSwitchMFDBSummaryEntry = _AgentSwitchMFDBSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 2, 1)
)
agentSwitchMFDBSummaryEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchMFDBSummaryVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchMFDBSummaryMacAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryEntry.setStatus("current")
_AgentSwitchMFDBSummaryVlanId_Type = VlanIndex
_AgentSwitchMFDBSummaryVlanId_Object = MibTableColumn
agentSwitchMFDBSummaryVlanId = _AgentSwitchMFDBSummaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 2, 1, 1),
    _AgentSwitchMFDBSummaryVlanId_Type()
)
agentSwitchMFDBSummaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryVlanId.setStatus("current")
_AgentSwitchMFDBSummaryMacAddress_Type = MacAddress
_AgentSwitchMFDBSummaryMacAddress_Object = MibTableColumn
agentSwitchMFDBSummaryMacAddress = _AgentSwitchMFDBSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 2, 1, 2),
    _AgentSwitchMFDBSummaryMacAddress_Type()
)
agentSwitchMFDBSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryMacAddress.setStatus("current")
_AgentSwitchMFDBSummaryForwardingPortMask_Type = AgentPortMask
_AgentSwitchMFDBSummaryForwardingPortMask_Object = MibTableColumn
agentSwitchMFDBSummaryForwardingPortMask = _AgentSwitchMFDBSummaryForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 2, 1, 3),
    _AgentSwitchMFDBSummaryForwardingPortMask_Type()
)
agentSwitchMFDBSummaryForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBSummaryForwardingPortMask.setStatus("current")
_AgentSwitchMFDBMaxTableEntries_Type = Gauge32
_AgentSwitchMFDBMaxTableEntries_Object = MibScalar
agentSwitchMFDBMaxTableEntries = _AgentSwitchMFDBMaxTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 3),
    _AgentSwitchMFDBMaxTableEntries_Type()
)
agentSwitchMFDBMaxTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBMaxTableEntries.setStatus("current")
_AgentSwitchMFDBMostEntriesUsed_Type = Gauge32
_AgentSwitchMFDBMostEntriesUsed_Object = MibScalar
agentSwitchMFDBMostEntriesUsed = _AgentSwitchMFDBMostEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 4),
    _AgentSwitchMFDBMostEntriesUsed_Type()
)
agentSwitchMFDBMostEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBMostEntriesUsed.setStatus("current")
_AgentSwitchMFDBCurrentEntries_Type = Gauge32
_AgentSwitchMFDBCurrentEntries_Object = MibScalar
agentSwitchMFDBCurrentEntries = _AgentSwitchMFDBCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 10, 5),
    _AgentSwitchMFDBCurrentEntries_Type()
)
agentSwitchMFDBCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMFDBCurrentEntries.setStatus("current")
_AgentSwitchDVlanTagGroup_ObjectIdentity = ObjectIdentity
agentSwitchDVlanTagGroup = _AgentSwitchDVlanTagGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11)
)


class _AgentSwitchDVlanTagEthertype_Type(Integer32):
    """Custom type agentSwitchDVlanTagEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSwitchDVlanTagEthertype_Type.__name__ = "Integer32"
_AgentSwitchDVlanTagEthertype_Object = MibScalar
agentSwitchDVlanTagEthertype = _AgentSwitchDVlanTagEthertype_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 1),
    _AgentSwitchDVlanTagEthertype_Type()
)
agentSwitchDVlanTagEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDVlanTagEthertype.setStatus("current")
_AgentSwitchDVlanTagTable_Object = MibTable
agentSwitchDVlanTagTable = _AgentSwitchDVlanTagTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 2)
)
if mibBuilder.loadTexts:
    agentSwitchDVlanTagTable.setStatus("current")
_AgentSwitchDVlanTagEntry_Object = MibTableRow
agentSwitchDVlanTagEntry = _AgentSwitchDVlanTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 2, 1)
)
agentSwitchDVlanTagEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchDVlanTagTPid"),
)
if mibBuilder.loadTexts:
    agentSwitchDVlanTagEntry.setStatus("current")


class _AgentSwitchDVlanTagTPid_Type(Integer32):
    """Custom type agentSwitchDVlanTagTPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSwitchDVlanTagTPid_Type.__name__ = "Integer32"
_AgentSwitchDVlanTagTPid_Object = MibTableColumn
agentSwitchDVlanTagTPid = _AgentSwitchDVlanTagTPid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 2, 1, 1),
    _AgentSwitchDVlanTagTPid_Type()
)
agentSwitchDVlanTagTPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchDVlanTagTPid.setStatus("current")


class _AgentSwitchDVlanTagPrimaryTPid_Type(Integer32):
    """Custom type agentSwitchDVlanTagPrimaryTPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentSwitchDVlanTagPrimaryTPid_Type.__name__ = "Integer32"
_AgentSwitchDVlanTagPrimaryTPid_Object = MibTableColumn
agentSwitchDVlanTagPrimaryTPid = _AgentSwitchDVlanTagPrimaryTPid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 2, 1, 2),
    _AgentSwitchDVlanTagPrimaryTPid_Type()
)
agentSwitchDVlanTagPrimaryTPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchDVlanTagPrimaryTPid.setStatus("current")
_AgentSwitchDVlanTagRowStatus_Type = RowStatus
_AgentSwitchDVlanTagRowStatus_Object = MibTableColumn
agentSwitchDVlanTagRowStatus = _AgentSwitchDVlanTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 2, 1, 3),
    _AgentSwitchDVlanTagRowStatus_Type()
)
agentSwitchDVlanTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchDVlanTagRowStatus.setStatus("current")
_AgentSwitchPortDVlanTagTable_Object = MibTable
agentSwitchPortDVlanTagTable = _AgentSwitchPortDVlanTagTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 3)
)
if mibBuilder.loadTexts:
    agentSwitchPortDVlanTagTable.setStatus("current")
_AgentSwitchPortDVlanTagEntry_Object = MibTableRow
agentSwitchPortDVlanTagEntry = _AgentSwitchPortDVlanTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 3, 1)
)
agentSwitchPortDVlanTagEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchPortDVlanTagInterfaceIfIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchPortDVlanTagTPid"),
)
if mibBuilder.loadTexts:
    agentSwitchPortDVlanTagEntry.setStatus("current")


class _AgentSwitchPortDVlanTagInterfaceIfIndex_Type(Integer32):
    """Custom type agentSwitchPortDVlanTagInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchPortDVlanTagInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentSwitchPortDVlanTagInterfaceIfIndex_Object = MibTableColumn
agentSwitchPortDVlanTagInterfaceIfIndex = _AgentSwitchPortDVlanTagInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 3, 1, 1),
    _AgentSwitchPortDVlanTagInterfaceIfIndex_Type()
)
agentSwitchPortDVlanTagInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchPortDVlanTagInterfaceIfIndex.setStatus("current")


class _AgentSwitchPortDVlanTagTPid_Type(Integer32):
    """Custom type agentSwitchPortDVlanTagTPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSwitchPortDVlanTagTPid_Type.__name__ = "Integer32"
_AgentSwitchPortDVlanTagTPid_Object = MibTableColumn
agentSwitchPortDVlanTagTPid = _AgentSwitchPortDVlanTagTPid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 3, 1, 2),
    _AgentSwitchPortDVlanTagTPid_Type()
)
agentSwitchPortDVlanTagTPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchPortDVlanTagTPid.setStatus("current")


class _AgentSwitchPortDVlanTagMode_Type(Integer32):
    """Custom type agentSwitchPortDVlanTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchPortDVlanTagMode_Type.__name__ = "Integer32"
_AgentSwitchPortDVlanTagMode_Object = MibTableColumn
agentSwitchPortDVlanTagMode = _AgentSwitchPortDVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 3, 1, 3),
    _AgentSwitchPortDVlanTagMode_Type()
)
agentSwitchPortDVlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchPortDVlanTagMode.setStatus("current")
_AgentSwitchPortDVlanTagCustomerId_Type = Integer32
_AgentSwitchPortDVlanTagCustomerId_Object = MibTableColumn
agentSwitchPortDVlanTagCustomerId = _AgentSwitchPortDVlanTagCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 3, 1, 4),
    _AgentSwitchPortDVlanTagCustomerId_Type()
)
agentSwitchPortDVlanTagCustomerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchPortDVlanTagCustomerId.setStatus("current")
_AgentSwitchPortDVlanTagRowStatus_Type = RowStatus
_AgentSwitchPortDVlanTagRowStatus_Object = MibTableColumn
agentSwitchPortDVlanTagRowStatus = _AgentSwitchPortDVlanTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 11, 3, 1, 5),
    _AgentSwitchPortDVlanTagRowStatus_Type()
)
agentSwitchPortDVlanTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchPortDVlanTagRowStatus.setStatus("current")
_AgentSwitchStormControlGroup_ObjectIdentity = ObjectIdentity
agentSwitchStormControlGroup = _AgentSwitchStormControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12)
)


class _AgentSwitchDot3FlowControlMode_Type(Integer32):
    """Custom type agentSwitchDot3FlowControlMode based on Integer32"""
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
        *(("asymmetric", 2),
          ("disable", 3),
          ("symmetric", 1))
    )


_AgentSwitchDot3FlowControlMode_Type.__name__ = "Integer32"
_AgentSwitchDot3FlowControlMode_Object = MibScalar
agentSwitchDot3FlowControlMode = _AgentSwitchDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 1),
    _AgentSwitchDot3FlowControlMode_Type()
)
agentSwitchDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDot3FlowControlMode.setStatus("current")


class _AgentSwitchBroadcastControlMode_Type(Integer32):
    """Custom type agentSwitchBroadcastControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchBroadcastControlMode_Type.__name__ = "Integer32"
_AgentSwitchBroadcastControlMode_Object = MibScalar
agentSwitchBroadcastControlMode = _AgentSwitchBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 4),
    _AgentSwitchBroadcastControlMode_Type()
)
agentSwitchBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchBroadcastControlMode.setStatus("current")


class _AgentSwitchBroadcastControlThreshold_Type(Unsigned32):
    """Custom type agentSwitchBroadcastControlThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_AgentSwitchBroadcastControlThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchBroadcastControlThreshold_Object = MibScalar
agentSwitchBroadcastControlThreshold = _AgentSwitchBroadcastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 5),
    _AgentSwitchBroadcastControlThreshold_Type()
)
agentSwitchBroadcastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchBroadcastControlThreshold.setStatus("current")


class _AgentSwitchMulticastControlMode_Type(Integer32):
    """Custom type agentSwitchMulticastControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchMulticastControlMode_Type.__name__ = "Integer32"
_AgentSwitchMulticastControlMode_Object = MibScalar
agentSwitchMulticastControlMode = _AgentSwitchMulticastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 6),
    _AgentSwitchMulticastControlMode_Type()
)
agentSwitchMulticastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMulticastControlMode.setStatus("current")


class _AgentSwitchMulticastControlThreshold_Type(Unsigned32):
    """Custom type agentSwitchMulticastControlThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_AgentSwitchMulticastControlThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchMulticastControlThreshold_Object = MibScalar
agentSwitchMulticastControlThreshold = _AgentSwitchMulticastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 7),
    _AgentSwitchMulticastControlThreshold_Type()
)
agentSwitchMulticastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMulticastControlThreshold.setStatus("current")


class _AgentSwitchUnicastControlMode_Type(Integer32):
    """Custom type agentSwitchUnicastControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchUnicastControlMode_Type.__name__ = "Integer32"
_AgentSwitchUnicastControlMode_Object = MibScalar
agentSwitchUnicastControlMode = _AgentSwitchUnicastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 8),
    _AgentSwitchUnicastControlMode_Type()
)
agentSwitchUnicastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchUnicastControlMode.setStatus("current")


class _AgentSwitchUnicastControlThreshold_Type(Unsigned32):
    """Custom type agentSwitchUnicastControlThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_AgentSwitchUnicastControlThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchUnicastControlThreshold_Object = MibScalar
agentSwitchUnicastControlThreshold = _AgentSwitchUnicastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 9),
    _AgentSwitchUnicastControlThreshold_Type()
)
agentSwitchUnicastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchUnicastControlThreshold.setStatus("current")


class _AgentSwitchBroadcastControlThresholdUnit_Type(Integer32):
    """Custom type agentSwitchBroadcastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_AgentSwitchBroadcastControlThresholdUnit_Type.__name__ = "Integer32"
_AgentSwitchBroadcastControlThresholdUnit_Object = MibScalar
agentSwitchBroadcastControlThresholdUnit = _AgentSwitchBroadcastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 10),
    _AgentSwitchBroadcastControlThresholdUnit_Type()
)
agentSwitchBroadcastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchBroadcastControlThresholdUnit.setStatus("current")


class _AgentSwitchMulticastControlThresholdUnit_Type(Integer32):
    """Custom type agentSwitchMulticastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_AgentSwitchMulticastControlThresholdUnit_Type.__name__ = "Integer32"
_AgentSwitchMulticastControlThresholdUnit_Object = MibScalar
agentSwitchMulticastControlThresholdUnit = _AgentSwitchMulticastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 11),
    _AgentSwitchMulticastControlThresholdUnit_Type()
)
agentSwitchMulticastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMulticastControlThresholdUnit.setStatus("current")


class _AgentSwitchUnicastControlThresholdUnit_Type(Integer32):
    """Custom type agentSwitchUnicastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_AgentSwitchUnicastControlThresholdUnit_Type.__name__ = "Integer32"
_AgentSwitchUnicastControlThresholdUnit_Object = MibScalar
agentSwitchUnicastControlThresholdUnit = _AgentSwitchUnicastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 12, 12),
    _AgentSwitchUnicastControlThresholdUnit_Type()
)
agentSwitchUnicastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchUnicastControlThresholdUnit.setStatus("current")
_AgentSwitchVlanMacAssociationGroup_ObjectIdentity = ObjectIdentity
agentSwitchVlanMacAssociationGroup = _AgentSwitchVlanMacAssociationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 17)
)
_AgentSwitchVlanMacAssociationTable_Object = MibTable
agentSwitchVlanMacAssociationTable = _AgentSwitchVlanMacAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 17, 1)
)
if mibBuilder.loadTexts:
    agentSwitchVlanMacAssociationTable.setStatus("current")
_AgentSwitchVlanMacAssociationEntry_Object = MibTableRow
agentSwitchVlanMacAssociationEntry = _AgentSwitchVlanMacAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 17, 1, 1)
)
agentSwitchVlanMacAssociationEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchVlanMacAssociationMacAddress"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchVlanMacAssociationVlanId"),
)
if mibBuilder.loadTexts:
    agentSwitchVlanMacAssociationEntry.setStatus("current")
_AgentSwitchVlanMacAssociationMacAddress_Type = MacAddress
_AgentSwitchVlanMacAssociationMacAddress_Object = MibTableColumn
agentSwitchVlanMacAssociationMacAddress = _AgentSwitchVlanMacAssociationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 17, 1, 1, 1),
    _AgentSwitchVlanMacAssociationMacAddress_Type()
)
agentSwitchVlanMacAssociationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchVlanMacAssociationMacAddress.setStatus("current")
_AgentSwitchVlanMacAssociationVlanId_Type = VlanIndex
_AgentSwitchVlanMacAssociationVlanId_Object = MibTableColumn
agentSwitchVlanMacAssociationVlanId = _AgentSwitchVlanMacAssociationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 17, 1, 1, 2),
    _AgentSwitchVlanMacAssociationVlanId_Type()
)
agentSwitchVlanMacAssociationVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchVlanMacAssociationVlanId.setStatus("current")
_AgentSwitchVlanMacAssociationRowStatus_Type = RowStatus
_AgentSwitchVlanMacAssociationRowStatus_Object = MibTableColumn
agentSwitchVlanMacAssociationRowStatus = _AgentSwitchVlanMacAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 17, 1, 1, 3),
    _AgentSwitchVlanMacAssociationRowStatus_Type()
)
agentSwitchVlanMacAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchVlanMacAssociationRowStatus.setStatus("current")
_AgentSwitchProtectedPortConfigGroup_ObjectIdentity = ObjectIdentity
agentSwitchProtectedPortConfigGroup = _AgentSwitchProtectedPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 18)
)
_AgentSwitchProtectedPortTable_Object = MibTable
agentSwitchProtectedPortTable = _AgentSwitchProtectedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 18, 1)
)
if mibBuilder.loadTexts:
    agentSwitchProtectedPortTable.setStatus("current")
_AgentSwitchProtectedPortEntry_Object = MibTableRow
agentSwitchProtectedPortEntry = _AgentSwitchProtectedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 18, 1, 1)
)
agentSwitchProtectedPortEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchProtectedPortGroupId"),
)
if mibBuilder.loadTexts:
    agentSwitchProtectedPortEntry.setStatus("current")


class _AgentSwitchProtectedPortGroupId_Type(Integer32):
    """Custom type agentSwitchProtectedPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchProtectedPortGroupId_Type.__name__ = "Integer32"
_AgentSwitchProtectedPortGroupId_Object = MibTableColumn
agentSwitchProtectedPortGroupId = _AgentSwitchProtectedPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 18, 1, 1, 1),
    _AgentSwitchProtectedPortGroupId_Type()
)
agentSwitchProtectedPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchProtectedPortGroupId.setStatus("current")


class _AgentSwitchProtectedPortGroupName_Type(DisplayString):
    """Custom type agentSwitchProtectedPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentSwitchProtectedPortGroupName_Type.__name__ = "DisplayString"
_AgentSwitchProtectedPortGroupName_Object = MibTableColumn
agentSwitchProtectedPortGroupName = _AgentSwitchProtectedPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 18, 1, 1, 2),
    _AgentSwitchProtectedPortGroupName_Type()
)
agentSwitchProtectedPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchProtectedPortGroupName.setStatus("current")
_AgentSwitchProtectedPortPortList_Type = PortList
_AgentSwitchProtectedPortPortList_Object = MibTableColumn
agentSwitchProtectedPortPortList = _AgentSwitchProtectedPortPortList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 18, 1, 1, 3),
    _AgentSwitchProtectedPortPortList_Type()
)
agentSwitchProtectedPortPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchProtectedPortPortList.setStatus("current")
_AgentSwitchVlanSubnetAssociationGroup_ObjectIdentity = ObjectIdentity
agentSwitchVlanSubnetAssociationGroup = _AgentSwitchVlanSubnetAssociationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 19)
)
_AgentSwitchVlanSubnetAssociationTable_Object = MibTable
agentSwitchVlanSubnetAssociationTable = _AgentSwitchVlanSubnetAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 19, 1)
)
if mibBuilder.loadTexts:
    agentSwitchVlanSubnetAssociationTable.setStatus("current")
_AgentSwitchVlanSubnetAssociationEntry_Object = MibTableRow
agentSwitchVlanSubnetAssociationEntry = _AgentSwitchVlanSubnetAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 19, 1, 1)
)
agentSwitchVlanSubnetAssociationEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchVlanSubnetAssociationIPAddress"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchVlanSubnetAssociationSubnetMask"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchVlanSubnetAssociationVlanId"),
)
if mibBuilder.loadTexts:
    agentSwitchVlanSubnetAssociationEntry.setStatus("current")
_AgentSwitchVlanSubnetAssociationIPAddress_Type = IpAddress
_AgentSwitchVlanSubnetAssociationIPAddress_Object = MibTableColumn
agentSwitchVlanSubnetAssociationIPAddress = _AgentSwitchVlanSubnetAssociationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 19, 1, 1, 1),
    _AgentSwitchVlanSubnetAssociationIPAddress_Type()
)
agentSwitchVlanSubnetAssociationIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchVlanSubnetAssociationIPAddress.setStatus("current")
_AgentSwitchVlanSubnetAssociationSubnetMask_Type = IpAddress
_AgentSwitchVlanSubnetAssociationSubnetMask_Object = MibTableColumn
agentSwitchVlanSubnetAssociationSubnetMask = _AgentSwitchVlanSubnetAssociationSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 19, 1, 1, 2),
    _AgentSwitchVlanSubnetAssociationSubnetMask_Type()
)
agentSwitchVlanSubnetAssociationSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchVlanSubnetAssociationSubnetMask.setStatus("current")
_AgentSwitchVlanSubnetAssociationVlanId_Type = VlanIndex
_AgentSwitchVlanSubnetAssociationVlanId_Object = MibTableColumn
agentSwitchVlanSubnetAssociationVlanId = _AgentSwitchVlanSubnetAssociationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 19, 1, 1, 3),
    _AgentSwitchVlanSubnetAssociationVlanId_Type()
)
agentSwitchVlanSubnetAssociationVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchVlanSubnetAssociationVlanId.setStatus("current")
_AgentSwitchVlanSubnetAssociationRowStatus_Type = RowStatus
_AgentSwitchVlanSubnetAssociationRowStatus_Object = MibTableColumn
agentSwitchVlanSubnetAssociationRowStatus = _AgentSwitchVlanSubnetAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 19, 1, 1, 4),
    _AgentSwitchVlanSubnetAssociationRowStatus_Type()
)
agentSwitchVlanSubnetAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchVlanSubnetAssociationRowStatus.setStatus("current")
_AgentSwitchSnoopingQuerierGroup_ObjectIdentity = ObjectIdentity
agentSwitchSnoopingQuerierGroup = _AgentSwitchSnoopingQuerierGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20)
)
_AgentSwitchSnoopingQuerierCfgTable_Object = MibTable
agentSwitchSnoopingQuerierCfgTable = _AgentSwitchSnoopingQuerierCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 1)
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierCfgTable.setStatus("current")
_AgentSwitchSnoopingQuerierCfgEntry_Object = MibTableRow
agentSwitchSnoopingQuerierCfgEntry = _AgentSwitchSnoopingQuerierCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 1, 1)
)
agentSwitchSnoopingQuerierCfgEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierCfgEntry.setStatus("current")


class _AgentSwitchSnoopingQuerierAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingQuerierAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchSnoopingQuerierAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingQuerierAdminMode_Object = MibTableColumn
agentSwitchSnoopingQuerierAdminMode = _AgentSwitchSnoopingQuerierAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 1, 1, 1),
    _AgentSwitchSnoopingQuerierAdminMode_Type()
)
agentSwitchSnoopingQuerierAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierAdminMode.setStatus("current")
_AgentSwitchSnoopingQuerierVersion_Type = Integer32
_AgentSwitchSnoopingQuerierVersion_Object = MibTableColumn
agentSwitchSnoopingQuerierVersion = _AgentSwitchSnoopingQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 1, 1, 2),
    _AgentSwitchSnoopingQuerierVersion_Type()
)
agentSwitchSnoopingQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierVersion.setStatus("current")
_AgentSwitchSnoopingQuerierAddress_Type = InetAddress
_AgentSwitchSnoopingQuerierAddress_Object = MibTableColumn
agentSwitchSnoopingQuerierAddress = _AgentSwitchSnoopingQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 1, 1, 3),
    _AgentSwitchSnoopingQuerierAddress_Type()
)
agentSwitchSnoopingQuerierAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierAddress.setStatus("current")


class _AgentSwitchSnoopingQuerierQueryInterval_Type(Integer32):
    """Custom type agentSwitchSnoopingQuerierQueryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_AgentSwitchSnoopingQuerierQueryInterval_Type.__name__ = "Integer32"
_AgentSwitchSnoopingQuerierQueryInterval_Object = MibTableColumn
agentSwitchSnoopingQuerierQueryInterval = _AgentSwitchSnoopingQuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 1, 1, 4),
    _AgentSwitchSnoopingQuerierQueryInterval_Type()
)
agentSwitchSnoopingQuerierQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierQueryInterval.setStatus("current")


class _AgentSwitchSnoopingQuerierExpiryInterval_Type(Integer32):
    """Custom type agentSwitchSnoopingQuerierExpiryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_AgentSwitchSnoopingQuerierExpiryInterval_Type.__name__ = "Integer32"
_AgentSwitchSnoopingQuerierExpiryInterval_Object = MibTableColumn
agentSwitchSnoopingQuerierExpiryInterval = _AgentSwitchSnoopingQuerierExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 1, 1, 5),
    _AgentSwitchSnoopingQuerierExpiryInterval_Type()
)
agentSwitchSnoopingQuerierExpiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierExpiryInterval.setStatus("current")
_AgentSwitchSnoopingQuerierVlanTable_Object = MibTable
agentSwitchSnoopingQuerierVlanTable = _AgentSwitchSnoopingQuerierVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2)
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierVlanTable.setStatus("current")
_AgentSwitchSnoopingQuerierVlanEntry_Object = MibTableRow
agentSwitchSnoopingQuerierVlanEntry = _AgentSwitchSnoopingQuerierVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1)
)
agentSwitchSnoopingQuerierVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierVlanEntry.setStatus("current")


class _AgentSwitchSnoopingQuerierVlanAdminMode_Type(Integer32):
    """Custom type agentSwitchSnoopingQuerierVlanAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSwitchSnoopingQuerierVlanAdminMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingQuerierVlanAdminMode_Object = MibTableColumn
agentSwitchSnoopingQuerierVlanAdminMode = _AgentSwitchSnoopingQuerierVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1, 1),
    _AgentSwitchSnoopingQuerierVlanAdminMode_Type()
)
agentSwitchSnoopingQuerierVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierVlanAdminMode.setStatus("current")


class _AgentSwitchSnoopingQuerierVlanOperMode_Type(Integer32):
    """Custom type agentSwitchSnoopingQuerierVlanOperMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("non-querier", 2),
          ("querier", 1))
    )


_AgentSwitchSnoopingQuerierVlanOperMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingQuerierVlanOperMode_Object = MibTableColumn
agentSwitchSnoopingQuerierVlanOperMode = _AgentSwitchSnoopingQuerierVlanOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1, 2),
    _AgentSwitchSnoopingQuerierVlanOperMode_Type()
)
agentSwitchSnoopingQuerierVlanOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierVlanOperMode.setStatus("current")


class _AgentSwitchSnoopingQuerierElectionParticipateMode_Type(Integer32):
    """Custom type agentSwitchSnoopingQuerierElectionParticipateMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSwitchSnoopingQuerierElectionParticipateMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopingQuerierElectionParticipateMode_Object = MibTableColumn
agentSwitchSnoopingQuerierElectionParticipateMode = _AgentSwitchSnoopingQuerierElectionParticipateMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1, 3),
    _AgentSwitchSnoopingQuerierElectionParticipateMode_Type()
)
agentSwitchSnoopingQuerierElectionParticipateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierElectionParticipateMode.setStatus("current")
_AgentSwitchSnoopingQuerierVlanAddress_Type = InetAddress
_AgentSwitchSnoopingQuerierVlanAddress_Object = MibTableColumn
agentSwitchSnoopingQuerierVlanAddress = _AgentSwitchSnoopingQuerierVlanAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1, 4),
    _AgentSwitchSnoopingQuerierVlanAddress_Type()
)
agentSwitchSnoopingQuerierVlanAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierVlanAddress.setStatus("current")
_AgentSwitchSnoopingQuerierOperVersion_Type = Integer32
_AgentSwitchSnoopingQuerierOperVersion_Object = MibTableColumn
agentSwitchSnoopingQuerierOperVersion = _AgentSwitchSnoopingQuerierOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1, 5),
    _AgentSwitchSnoopingQuerierOperVersion_Type()
)
agentSwitchSnoopingQuerierOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierOperVersion.setStatus("current")


class _AgentSwitchSnoopingQuerierOperMaxResponseTime_Type(Integer32):
    """Custom type agentSwitchSnoopingQuerierOperMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchSnoopingQuerierOperMaxResponseTime_Type.__name__ = "Integer32"
_AgentSwitchSnoopingQuerierOperMaxResponseTime_Object = MibTableColumn
agentSwitchSnoopingQuerierOperMaxResponseTime = _AgentSwitchSnoopingQuerierOperMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1, 6),
    _AgentSwitchSnoopingQuerierOperMaxResponseTime_Type()
)
agentSwitchSnoopingQuerierOperMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierOperMaxResponseTime.setStatus("current")
_AgentSwitchSnoopingQuerierLastQuerierAddress_Type = InetAddress
_AgentSwitchSnoopingQuerierLastQuerierAddress_Object = MibTableColumn
agentSwitchSnoopingQuerierLastQuerierAddress = _AgentSwitchSnoopingQuerierLastQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1, 7),
    _AgentSwitchSnoopingQuerierLastQuerierAddress_Type()
)
agentSwitchSnoopingQuerierLastQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierLastQuerierAddress.setStatus("current")
_AgentSwitchSnoopingQuerierLastQuerierVersion_Type = Integer32
_AgentSwitchSnoopingQuerierLastQuerierVersion_Object = MibTableColumn
agentSwitchSnoopingQuerierLastQuerierVersion = _AgentSwitchSnoopingQuerierLastQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 20, 2, 1, 8),
    _AgentSwitchSnoopingQuerierLastQuerierVersion_Type()
)
agentSwitchSnoopingQuerierLastQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopingQuerierLastQuerierVersion.setStatus("current")
_AgentDaiConfigGroup_ObjectIdentity = ObjectIdentity
agentDaiConfigGroup = _AgentDaiConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21)
)


class _AgentDaiSrcMacValidate_Type(TruthValue):
    """Custom type agentDaiSrcMacValidate based on TruthValue"""


_AgentDaiSrcMacValidate_Object = MibScalar
agentDaiSrcMacValidate = _AgentDaiSrcMacValidate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 1),
    _AgentDaiSrcMacValidate_Type()
)
agentDaiSrcMacValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiSrcMacValidate.setStatus("current")


class _AgentDaiDstMacValidate_Type(TruthValue):
    """Custom type agentDaiDstMacValidate based on TruthValue"""


_AgentDaiDstMacValidate_Object = MibScalar
agentDaiDstMacValidate = _AgentDaiDstMacValidate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 2),
    _AgentDaiDstMacValidate_Type()
)
agentDaiDstMacValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiDstMacValidate.setStatus("current")


class _AgentDaiIPValidate_Type(TruthValue):
    """Custom type agentDaiIPValidate based on TruthValue"""


_AgentDaiIPValidate_Object = MibScalar
agentDaiIPValidate = _AgentDaiIPValidate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 3),
    _AgentDaiIPValidate_Type()
)
agentDaiIPValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiIPValidate.setStatus("current")
_AgentDaiVlanConfigTable_Object = MibTable
agentDaiVlanConfigTable = _AgentDaiVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 4)
)
if mibBuilder.loadTexts:
    agentDaiVlanConfigTable.setStatus("current")
_AgentDaiVlanConfigEntry_Object = MibTableRow
agentDaiVlanConfigEntry = _AgentDaiVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 4, 1)
)
agentDaiVlanConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDaiVlanIndex"),
)
if mibBuilder.loadTexts:
    agentDaiVlanConfigEntry.setStatus("current")
_AgentDaiVlanIndex_Type = VlanIndex
_AgentDaiVlanIndex_Object = MibTableColumn
agentDaiVlanIndex = _AgentDaiVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 4, 1, 1),
    _AgentDaiVlanIndex_Type()
)
agentDaiVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDaiVlanIndex.setStatus("current")


class _AgentDaiVlanDynArpInspEnable_Type(TruthValue):
    """Custom type agentDaiVlanDynArpInspEnable based on TruthValue"""


_AgentDaiVlanDynArpInspEnable_Object = MibTableColumn
agentDaiVlanDynArpInspEnable = _AgentDaiVlanDynArpInspEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 4, 1, 2),
    _AgentDaiVlanDynArpInspEnable_Type()
)
agentDaiVlanDynArpInspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiVlanDynArpInspEnable.setStatus("current")


class _AgentDaiVlanLoggingEnable_Type(TruthValue):
    """Custom type agentDaiVlanLoggingEnable based on TruthValue"""


_AgentDaiVlanLoggingEnable_Object = MibTableColumn
agentDaiVlanLoggingEnable = _AgentDaiVlanLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 4, 1, 3),
    _AgentDaiVlanLoggingEnable_Type()
)
agentDaiVlanLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiVlanLoggingEnable.setStatus("current")


class _AgentDaiVlanArpAclName_Type(DisplayString):
    """Custom type agentDaiVlanArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentDaiVlanArpAclName_Type.__name__ = "DisplayString"
_AgentDaiVlanArpAclName_Object = MibTableColumn
agentDaiVlanArpAclName = _AgentDaiVlanArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 4, 1, 4),
    _AgentDaiVlanArpAclName_Type()
)
agentDaiVlanArpAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiVlanArpAclName.setStatus("current")


class _AgentDaiVlanArpAclStaticFlag_Type(TruthValue):
    """Custom type agentDaiVlanArpAclStaticFlag based on TruthValue"""


_AgentDaiVlanArpAclStaticFlag_Object = MibTableColumn
agentDaiVlanArpAclStaticFlag = _AgentDaiVlanArpAclStaticFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 4, 1, 5),
    _AgentDaiVlanArpAclStaticFlag_Type()
)
agentDaiVlanArpAclStaticFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiVlanArpAclStaticFlag.setStatus("current")


class _AgentDaiStatsReset_Type(Integer32):
    """Custom type agentDaiStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentDaiStatsReset_Type.__name__ = "Integer32"
_AgentDaiStatsReset_Object = MibScalar
agentDaiStatsReset = _AgentDaiStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 5),
    _AgentDaiStatsReset_Type()
)
agentDaiStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiStatsReset.setStatus("current")
_AgentDaiVlanStatsTable_Object = MibTable
agentDaiVlanStatsTable = _AgentDaiVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6)
)
if mibBuilder.loadTexts:
    agentDaiVlanStatsTable.setStatus("current")
_AgentDaiVlanStatsEntry_Object = MibTableRow
agentDaiVlanStatsEntry = _AgentDaiVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1)
)
agentDaiVlanStatsEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDaiVlanStatsIndex"),
)
if mibBuilder.loadTexts:
    agentDaiVlanStatsEntry.setStatus("current")
_AgentDaiVlanStatsIndex_Type = VlanIndex
_AgentDaiVlanStatsIndex_Object = MibTableColumn
agentDaiVlanStatsIndex = _AgentDaiVlanStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 1),
    _AgentDaiVlanStatsIndex_Type()
)
agentDaiVlanStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDaiVlanStatsIndex.setStatus("current")
_AgentDaiVlanPktsForwarded_Type = Counter32
_AgentDaiVlanPktsForwarded_Object = MibTableColumn
agentDaiVlanPktsForwarded = _AgentDaiVlanPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 2),
    _AgentDaiVlanPktsForwarded_Type()
)
agentDaiVlanPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanPktsForwarded.setStatus("current")
_AgentDaiVlanPktsDropped_Type = Counter32
_AgentDaiVlanPktsDropped_Object = MibTableColumn
agentDaiVlanPktsDropped = _AgentDaiVlanPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 3),
    _AgentDaiVlanPktsDropped_Type()
)
agentDaiVlanPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanPktsDropped.setStatus("current")
_AgentDaiVlanDhcpDrops_Type = Counter32
_AgentDaiVlanDhcpDrops_Object = MibTableColumn
agentDaiVlanDhcpDrops = _AgentDaiVlanDhcpDrops_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 4),
    _AgentDaiVlanDhcpDrops_Type()
)
agentDaiVlanDhcpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanDhcpDrops.setStatus("current")
_AgentDaiVlanDhcpPermits_Type = Counter32
_AgentDaiVlanDhcpPermits_Object = MibTableColumn
agentDaiVlanDhcpPermits = _AgentDaiVlanDhcpPermits_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 5),
    _AgentDaiVlanDhcpPermits_Type()
)
agentDaiVlanDhcpPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanDhcpPermits.setStatus("current")
_AgentDaiVlanAclDrops_Type = Counter32
_AgentDaiVlanAclDrops_Object = MibTableColumn
agentDaiVlanAclDrops = _AgentDaiVlanAclDrops_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 6),
    _AgentDaiVlanAclDrops_Type()
)
agentDaiVlanAclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanAclDrops.setStatus("current")
_AgentDaiVlanAclPermits_Type = Counter32
_AgentDaiVlanAclPermits_Object = MibTableColumn
agentDaiVlanAclPermits = _AgentDaiVlanAclPermits_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 7),
    _AgentDaiVlanAclPermits_Type()
)
agentDaiVlanAclPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanAclPermits.setStatus("current")
_AgentDaiVlanSrcMacFailures_Type = Counter32
_AgentDaiVlanSrcMacFailures_Object = MibTableColumn
agentDaiVlanSrcMacFailures = _AgentDaiVlanSrcMacFailures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 8),
    _AgentDaiVlanSrcMacFailures_Type()
)
agentDaiVlanSrcMacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanSrcMacFailures.setStatus("current")
_AgentDaiVlanDstMacFailures_Type = Counter32
_AgentDaiVlanDstMacFailures_Object = MibTableColumn
agentDaiVlanDstMacFailures = _AgentDaiVlanDstMacFailures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 9),
    _AgentDaiVlanDstMacFailures_Type()
)
agentDaiVlanDstMacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanDstMacFailures.setStatus("current")
_AgentDaiVlanIpValidFailures_Type = Counter32
_AgentDaiVlanIpValidFailures_Object = MibTableColumn
agentDaiVlanIpValidFailures = _AgentDaiVlanIpValidFailures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 6, 1, 10),
    _AgentDaiVlanIpValidFailures_Type()
)
agentDaiVlanIpValidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDaiVlanIpValidFailures.setStatus("current")
_AgentDaiIfConfigTable_Object = MibTable
agentDaiIfConfigTable = _AgentDaiIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 7)
)
if mibBuilder.loadTexts:
    agentDaiIfConfigTable.setStatus("current")
_AgentDaiIfConfigEntry_Object = MibTableRow
agentDaiIfConfigEntry = _AgentDaiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 7, 1)
)
agentDaiIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDaiIfConfigEntry.setStatus("current")


class _AgentDaiIfTrustEnable_Type(TruthValue):
    """Custom type agentDaiIfTrustEnable based on TruthValue"""


_AgentDaiIfTrustEnable_Object = MibTableColumn
agentDaiIfTrustEnable = _AgentDaiIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 7, 1, 1),
    _AgentDaiIfTrustEnable_Type()
)
agentDaiIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiIfTrustEnable.setStatus("current")


class _AgentDaiIfRateLimit_Type(Integer32):
    """Custom type agentDaiIfRateLimit based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 300),
    )


_AgentDaiIfRateLimit_Type.__name__ = "Integer32"
_AgentDaiIfRateLimit_Object = MibTableColumn
agentDaiIfRateLimit = _AgentDaiIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 7, 1, 2),
    _AgentDaiIfRateLimit_Type()
)
agentDaiIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    agentDaiIfRateLimit.setUnits("packets per second")


class _AgentDaiIfBurstInterval_Type(Unsigned32):
    """Custom type agentDaiIfBurstInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AgentDaiIfBurstInterval_Type.__name__ = "Unsigned32"
_AgentDaiIfBurstInterval_Object = MibTableColumn
agentDaiIfBurstInterval = _AgentDaiIfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 21, 7, 1, 3),
    _AgentDaiIfBurstInterval_Type()
)
agentDaiIfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDaiIfBurstInterval.setStatus("current")
_AgentArpAclGroup_ObjectIdentity = ObjectIdentity
agentArpAclGroup = _AgentArpAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22)
)
_AgentArpAclTable_Object = MibTable
agentArpAclTable = _AgentArpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 1)
)
if mibBuilder.loadTexts:
    agentArpAclTable.setStatus("current")
_AgentArpAclEntry_Object = MibTableRow
agentArpAclEntry = _AgentArpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 1, 1)
)
agentArpAclEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentArpAclName"),
)
if mibBuilder.loadTexts:
    agentArpAclEntry.setStatus("current")


class _AgentArpAclName_Type(DisplayString):
    """Custom type agentArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AgentArpAclName_Type.__name__ = "DisplayString"
_AgentArpAclName_Object = MibTableColumn
agentArpAclName = _AgentArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 1, 1, 1),
    _AgentArpAclName_Type()
)
agentArpAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentArpAclName.setStatus("current")
_AgentArpAclRowStatus_Type = RowStatus
_AgentArpAclRowStatus_Object = MibTableColumn
agentArpAclRowStatus = _AgentArpAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 1, 1, 2),
    _AgentArpAclRowStatus_Type()
)
agentArpAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentArpAclRowStatus.setStatus("current")
_AgentArpAclRuleTable_Object = MibTable
agentArpAclRuleTable = _AgentArpAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 2)
)
if mibBuilder.loadTexts:
    agentArpAclRuleTable.setStatus("current")
_AgentArpAclRuleEntry_Object = MibTableRow
agentArpAclRuleEntry = _AgentArpAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 2, 1)
)
agentArpAclRuleEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentArpAclName"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentArpAclRuleMatchSenderIpAddr"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentArpAclRuleMatchSenderMacAddr"),
)
if mibBuilder.loadTexts:
    agentArpAclRuleEntry.setStatus("current")
_AgentArpAclRuleMatchSenderIpAddr_Type = IpAddress
_AgentArpAclRuleMatchSenderIpAddr_Object = MibTableColumn
agentArpAclRuleMatchSenderIpAddr = _AgentArpAclRuleMatchSenderIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 2, 1, 1),
    _AgentArpAclRuleMatchSenderIpAddr_Type()
)
agentArpAclRuleMatchSenderIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentArpAclRuleMatchSenderIpAddr.setStatus("current")
_AgentArpAclRuleMatchSenderMacAddr_Type = MacAddress
_AgentArpAclRuleMatchSenderMacAddr_Object = MibTableColumn
agentArpAclRuleMatchSenderMacAddr = _AgentArpAclRuleMatchSenderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 2, 1, 2),
    _AgentArpAclRuleMatchSenderMacAddr_Type()
)
agentArpAclRuleMatchSenderMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentArpAclRuleMatchSenderMacAddr.setStatus("current")
_AgentArpAclRuleRowStatus_Type = RowStatus
_AgentArpAclRuleRowStatus_Object = MibTableColumn
agentArpAclRuleRowStatus = _AgentArpAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 22, 2, 1, 3),
    _AgentArpAclRuleRowStatus_Type()
)
agentArpAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentArpAclRuleRowStatus.setStatus("current")
_AgentDhcpSnoopingConfigGroup_ObjectIdentity = ObjectIdentity
agentDhcpSnoopingConfigGroup = _AgentDhcpSnoopingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23)
)


class _AgentDhcpSnoopingAdminMode_Type(TruthValue):
    """Custom type agentDhcpSnoopingAdminMode based on TruthValue"""


_AgentDhcpSnoopingAdminMode_Object = MibScalar
agentDhcpSnoopingAdminMode = _AgentDhcpSnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 1),
    _AgentDhcpSnoopingAdminMode_Type()
)
agentDhcpSnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingAdminMode.setStatus("current")


class _AgentDhcpSnoopingVerifyMac_Type(TruthValue):
    """Custom type agentDhcpSnoopingVerifyMac based on TruthValue"""


_AgentDhcpSnoopingVerifyMac_Object = MibScalar
agentDhcpSnoopingVerifyMac = _AgentDhcpSnoopingVerifyMac_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 2),
    _AgentDhcpSnoopingVerifyMac_Type()
)
agentDhcpSnoopingVerifyMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingVerifyMac.setStatus("current")
_AgentDhcpSnoopingVlanConfigTable_Object = MibTable
agentDhcpSnoopingVlanConfigTable = _AgentDhcpSnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 3)
)
if mibBuilder.loadTexts:
    agentDhcpSnoopingVlanConfigTable.setStatus("current")
_AgentDhcpSnoopingVlanConfigEntry_Object = MibTableRow
agentDhcpSnoopingVlanConfigEntry = _AgentDhcpSnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 3, 1)
)
agentDhcpSnoopingVlanConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDhcpSnoopingVlanIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpSnoopingVlanConfigEntry.setStatus("current")
_AgentDhcpSnoopingVlanIndex_Type = VlanIndex
_AgentDhcpSnoopingVlanIndex_Object = MibTableColumn
agentDhcpSnoopingVlanIndex = _AgentDhcpSnoopingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 3, 1, 1),
    _AgentDhcpSnoopingVlanIndex_Type()
)
agentDhcpSnoopingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDhcpSnoopingVlanIndex.setStatus("current")


class _AgentDhcpSnoopingVlanEnable_Type(TruthValue):
    """Custom type agentDhcpSnoopingVlanEnable based on TruthValue"""


_AgentDhcpSnoopingVlanEnable_Object = MibTableColumn
agentDhcpSnoopingVlanEnable = _AgentDhcpSnoopingVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 3, 1, 2),
    _AgentDhcpSnoopingVlanEnable_Type()
)
agentDhcpSnoopingVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingVlanEnable.setStatus("current")
_AgentDhcpSnoopingIfConfigTable_Object = MibTable
agentDhcpSnoopingIfConfigTable = _AgentDhcpSnoopingIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 4)
)
if mibBuilder.loadTexts:
    agentDhcpSnoopingIfConfigTable.setStatus("current")
_AgentDhcpSnoopingIfConfigEntry_Object = MibTableRow
agentDhcpSnoopingIfConfigEntry = _AgentDhcpSnoopingIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 4, 1)
)
agentDhcpSnoopingIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpSnoopingIfConfigEntry.setStatus("current")


class _AgentDhcpSnoopingIfTrustEnable_Type(TruthValue):
    """Custom type agentDhcpSnoopingIfTrustEnable based on TruthValue"""


_AgentDhcpSnoopingIfTrustEnable_Object = MibTableColumn
agentDhcpSnoopingIfTrustEnable = _AgentDhcpSnoopingIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 4, 1, 1),
    _AgentDhcpSnoopingIfTrustEnable_Type()
)
agentDhcpSnoopingIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingIfTrustEnable.setStatus("current")


class _AgentDhcpSnoopingIfLogEnable_Type(TruthValue):
    """Custom type agentDhcpSnoopingIfLogEnable based on TruthValue"""


_AgentDhcpSnoopingIfLogEnable_Object = MibTableColumn
agentDhcpSnoopingIfLogEnable = _AgentDhcpSnoopingIfLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 4, 1, 2),
    _AgentDhcpSnoopingIfLogEnable_Type()
)
agentDhcpSnoopingIfLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingIfLogEnable.setStatus("current")


class _AgentDhcpSnoopingIfRateLimit_Type(Integer32):
    """Custom type agentDhcpSnoopingIfRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 300),
    )


_AgentDhcpSnoopingIfRateLimit_Type.__name__ = "Integer32"
_AgentDhcpSnoopingIfRateLimit_Object = MibTableColumn
agentDhcpSnoopingIfRateLimit = _AgentDhcpSnoopingIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 4, 1, 3),
    _AgentDhcpSnoopingIfRateLimit_Type()
)
agentDhcpSnoopingIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    agentDhcpSnoopingIfRateLimit.setUnits("packets per second")


class _AgentDhcpSnoopingIfBurstInterval_Type(Integer32):
    """Custom type agentDhcpSnoopingIfBurstInterval based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_AgentDhcpSnoopingIfBurstInterval_Type.__name__ = "Integer32"
_AgentDhcpSnoopingIfBurstInterval_Object = MibTableColumn
agentDhcpSnoopingIfBurstInterval = _AgentDhcpSnoopingIfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 4, 1, 4),
    _AgentDhcpSnoopingIfBurstInterval_Type()
)
agentDhcpSnoopingIfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingIfBurstInterval.setStatus("current")
_AgentIpsgIfConfigTable_Object = MibTable
agentIpsgIfConfigTable = _AgentIpsgIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 5)
)
if mibBuilder.loadTexts:
    agentIpsgIfConfigTable.setStatus("current")
_AgentIpsgIfConfigEntry_Object = MibTableRow
agentIpsgIfConfigEntry = _AgentIpsgIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 5, 1)
)
agentIpsgIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentIpsgIfConfigEntry.setStatus("current")


class _AgentIpsgIfVerifySource_Type(TruthValue):
    """Custom type agentIpsgIfVerifySource based on TruthValue"""


_AgentIpsgIfVerifySource_Object = MibTableColumn
agentIpsgIfVerifySource = _AgentIpsgIfVerifySource_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 5, 1, 1),
    _AgentIpsgIfVerifySource_Type()
)
agentIpsgIfVerifySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpsgIfVerifySource.setStatus("current")


class _AgentIpsgIfPortSecurity_Type(TruthValue):
    """Custom type agentIpsgIfPortSecurity based on TruthValue"""


_AgentIpsgIfPortSecurity_Object = MibTableColumn
agentIpsgIfPortSecurity = _AgentIpsgIfPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 5, 1, 2),
    _AgentIpsgIfPortSecurity_Type()
)
agentIpsgIfPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpsgIfPortSecurity.setStatus("current")


class _AgentDhcpSnoopingStatsReset_Type(Integer32):
    """Custom type agentDhcpSnoopingStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentDhcpSnoopingStatsReset_Type.__name__ = "Integer32"
_AgentDhcpSnoopingStatsReset_Object = MibScalar
agentDhcpSnoopingStatsReset = _AgentDhcpSnoopingStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 6),
    _AgentDhcpSnoopingStatsReset_Type()
)
agentDhcpSnoopingStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingStatsReset.setStatus("current")
_AgentDhcpSnoopingStatsTable_Object = MibTable
agentDhcpSnoopingStatsTable = _AgentDhcpSnoopingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 7)
)
if mibBuilder.loadTexts:
    agentDhcpSnoopingStatsTable.setStatus("current")
_AgentDhcpSnoopingStatsEntry_Object = MibTableRow
agentDhcpSnoopingStatsEntry = _AgentDhcpSnoopingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 7, 1)
)
agentDhcpSnoopingStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpSnoopingStatsEntry.setStatus("current")
_AgentDhcpSnoopingMacVerifyFailures_Type = Counter32
_AgentDhcpSnoopingMacVerifyFailures_Object = MibTableColumn
agentDhcpSnoopingMacVerifyFailures = _AgentDhcpSnoopingMacVerifyFailures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 7, 1, 1),
    _AgentDhcpSnoopingMacVerifyFailures_Type()
)
agentDhcpSnoopingMacVerifyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpSnoopingMacVerifyFailures.setStatus("current")
_AgentDhcpSnoopingInvalidClientMessages_Type = Counter32
_AgentDhcpSnoopingInvalidClientMessages_Object = MibTableColumn
agentDhcpSnoopingInvalidClientMessages = _AgentDhcpSnoopingInvalidClientMessages_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 7, 1, 2),
    _AgentDhcpSnoopingInvalidClientMessages_Type()
)
agentDhcpSnoopingInvalidClientMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpSnoopingInvalidClientMessages.setStatus("current")
_AgentDhcpSnoopingInvalidServerMessages_Type = Counter32
_AgentDhcpSnoopingInvalidServerMessages_Object = MibTableColumn
agentDhcpSnoopingInvalidServerMessages = _AgentDhcpSnoopingInvalidServerMessages_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 7, 1, 3),
    _AgentDhcpSnoopingInvalidServerMessages_Type()
)
agentDhcpSnoopingInvalidServerMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpSnoopingInvalidServerMessages.setStatus("current")
_AgentStaticIpsgBindingTable_Object = MibTable
agentStaticIpsgBindingTable = _AgentStaticIpsgBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 8)
)
if mibBuilder.loadTexts:
    agentStaticIpsgBindingTable.setStatus("current")
_AgentStaticIpsgBindingEntry_Object = MibTableRow
agentStaticIpsgBindingEntry = _AgentStaticIpsgBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 8, 1)
)
agentStaticIpsgBindingEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticIpsgBindingIfIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticIpsgBindingVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticIpsgBindingIpAddr"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticIpsgBindingMacAddr"),
)
if mibBuilder.loadTexts:
    agentStaticIpsgBindingEntry.setStatus("current")
_AgentStaticIpsgBindingIfIndex_Type = InterfaceIndex
_AgentStaticIpsgBindingIfIndex_Object = MibTableColumn
agentStaticIpsgBindingIfIndex = _AgentStaticIpsgBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 8, 1, 1),
    _AgentStaticIpsgBindingIfIndex_Type()
)
agentStaticIpsgBindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpsgBindingIfIndex.setStatus("current")
_AgentStaticIpsgBindingVlanId_Type = VlanIndex
_AgentStaticIpsgBindingVlanId_Object = MibTableColumn
agentStaticIpsgBindingVlanId = _AgentStaticIpsgBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 8, 1, 2),
    _AgentStaticIpsgBindingVlanId_Type()
)
agentStaticIpsgBindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpsgBindingVlanId.setStatus("current")
_AgentStaticIpsgBindingIpAddr_Type = IpAddress
_AgentStaticIpsgBindingIpAddr_Object = MibTableColumn
agentStaticIpsgBindingIpAddr = _AgentStaticIpsgBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 8, 1, 3),
    _AgentStaticIpsgBindingIpAddr_Type()
)
agentStaticIpsgBindingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpsgBindingIpAddr.setStatus("current")
_AgentStaticIpsgBindingMacAddr_Type = MacAddress
_AgentStaticIpsgBindingMacAddr_Object = MibTableColumn
agentStaticIpsgBindingMacAddr = _AgentStaticIpsgBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 8, 1, 4),
    _AgentStaticIpsgBindingMacAddr_Type()
)
agentStaticIpsgBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpsgBindingMacAddr.setStatus("current")
_AgentStaticIpsgBindingRowStatus_Type = RowStatus
_AgentStaticIpsgBindingRowStatus_Object = MibTableColumn
agentStaticIpsgBindingRowStatus = _AgentStaticIpsgBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 8, 1, 5),
    _AgentStaticIpsgBindingRowStatus_Type()
)
agentStaticIpsgBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpsgBindingRowStatus.setStatus("current")
_AgentDynamicIpsgBindingTable_Object = MibTable
agentDynamicIpsgBindingTable = _AgentDynamicIpsgBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 9)
)
if mibBuilder.loadTexts:
    agentDynamicIpsgBindingTable.setStatus("current")
_AgentDynamicIpsgBindingEntry_Object = MibTableRow
agentDynamicIpsgBindingEntry = _AgentDynamicIpsgBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 9, 1)
)
agentDynamicIpsgBindingEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicIpsgBindingIfIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicIpsgBindingVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicIpsgBindingIpAddr"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicIpsgBindingMacAddr"),
)
if mibBuilder.loadTexts:
    agentDynamicIpsgBindingEntry.setStatus("current")
_AgentDynamicIpsgBindingIfIndex_Type = InterfaceIndex
_AgentDynamicIpsgBindingIfIndex_Object = MibTableColumn
agentDynamicIpsgBindingIfIndex = _AgentDynamicIpsgBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 9, 1, 1),
    _AgentDynamicIpsgBindingIfIndex_Type()
)
agentDynamicIpsgBindingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicIpsgBindingIfIndex.setStatus("current")
_AgentDynamicIpsgBindingVlanId_Type = VlanIndex
_AgentDynamicIpsgBindingVlanId_Object = MibTableColumn
agentDynamicIpsgBindingVlanId = _AgentDynamicIpsgBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 9, 1, 2),
    _AgentDynamicIpsgBindingVlanId_Type()
)
agentDynamicIpsgBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicIpsgBindingVlanId.setStatus("current")
_AgentDynamicIpsgBindingIpAddr_Type = IpAddress
_AgentDynamicIpsgBindingIpAddr_Object = MibTableColumn
agentDynamicIpsgBindingIpAddr = _AgentDynamicIpsgBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 9, 1, 3),
    _AgentDynamicIpsgBindingIpAddr_Type()
)
agentDynamicIpsgBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicIpsgBindingIpAddr.setStatus("current")
_AgentDynamicIpsgBindingMacAddr_Type = MacAddress
_AgentDynamicIpsgBindingMacAddr_Object = MibTableColumn
agentDynamicIpsgBindingMacAddr = _AgentDynamicIpsgBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 9, 1, 4),
    _AgentDynamicIpsgBindingMacAddr_Type()
)
agentDynamicIpsgBindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicIpsgBindingMacAddr.setStatus("current")
_AgentStaticDsBindingTable_Object = MibTable
agentStaticDsBindingTable = _AgentStaticDsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 10)
)
if mibBuilder.loadTexts:
    agentStaticDsBindingTable.setStatus("current")
_AgentStaticDsBindingEntry_Object = MibTableRow
agentStaticDsBindingEntry = _AgentStaticDsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 10, 1)
)
agentStaticDsBindingEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticDsBindingMacAddr"),
)
if mibBuilder.loadTexts:
    agentStaticDsBindingEntry.setStatus("current")
_AgentStaticDsBindingIfIndex_Type = InterfaceIndex
_AgentStaticDsBindingIfIndex_Object = MibTableColumn
agentStaticDsBindingIfIndex = _AgentStaticDsBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 10, 1, 1),
    _AgentStaticDsBindingIfIndex_Type()
)
agentStaticDsBindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsBindingIfIndex.setStatus("current")
_AgentStaticDsBindingVlanId_Type = VlanId
_AgentStaticDsBindingVlanId_Object = MibTableColumn
agentStaticDsBindingVlanId = _AgentStaticDsBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 10, 1, 2),
    _AgentStaticDsBindingVlanId_Type()
)
agentStaticDsBindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsBindingVlanId.setStatus("current")
_AgentStaticDsBindingMacAddr_Type = MacAddress
_AgentStaticDsBindingMacAddr_Object = MibTableColumn
agentStaticDsBindingMacAddr = _AgentStaticDsBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 10, 1, 3),
    _AgentStaticDsBindingMacAddr_Type()
)
agentStaticDsBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsBindingMacAddr.setStatus("current")
_AgentStaticDsBindingIpAddr_Type = IpAddress
_AgentStaticDsBindingIpAddr_Object = MibTableColumn
agentStaticDsBindingIpAddr = _AgentStaticDsBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 10, 1, 4),
    _AgentStaticDsBindingIpAddr_Type()
)
agentStaticDsBindingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsBindingIpAddr.setStatus("current")
_AgentStaticDsBindingRowStatus_Type = RowStatus
_AgentStaticDsBindingRowStatus_Object = MibTableColumn
agentStaticDsBindingRowStatus = _AgentStaticDsBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 10, 1, 5),
    _AgentStaticDsBindingRowStatus_Type()
)
agentStaticDsBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsBindingRowStatus.setStatus("current")
_AgentDynamicDsBindingTable_Object = MibTable
agentDynamicDsBindingTable = _AgentDynamicDsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 11)
)
if mibBuilder.loadTexts:
    agentDynamicDsBindingTable.setStatus("current")
_AgentDynamicDsBindingEntry_Object = MibTableRow
agentDynamicDsBindingEntry = _AgentDynamicDsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 11, 1)
)
agentDynamicDsBindingEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicDsBindingMacAddr"),
)
if mibBuilder.loadTexts:
    agentDynamicDsBindingEntry.setStatus("current")
_AgentDynamicDsBindingIfIndex_Type = InterfaceIndex
_AgentDynamicDsBindingIfIndex_Object = MibTableColumn
agentDynamicDsBindingIfIndex = _AgentDynamicDsBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 11, 1, 1),
    _AgentDynamicDsBindingIfIndex_Type()
)
agentDynamicDsBindingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsBindingIfIndex.setStatus("current")
_AgentDynamicDsBindingVlanId_Type = VlanIndex
_AgentDynamicDsBindingVlanId_Object = MibTableColumn
agentDynamicDsBindingVlanId = _AgentDynamicDsBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 11, 1, 2),
    _AgentDynamicDsBindingVlanId_Type()
)
agentDynamicDsBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsBindingVlanId.setStatus("current")
_AgentDynamicDsBindingMacAddr_Type = MacAddress
_AgentDynamicDsBindingMacAddr_Object = MibTableColumn
agentDynamicDsBindingMacAddr = _AgentDynamicDsBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 11, 1, 3),
    _AgentDynamicDsBindingMacAddr_Type()
)
agentDynamicDsBindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsBindingMacAddr.setStatus("current")
_AgentDynamicDsBindingIpAddr_Type = IpAddress
_AgentDynamicDsBindingIpAddr_Object = MibTableColumn
agentDynamicDsBindingIpAddr = _AgentDynamicDsBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 11, 1, 4),
    _AgentDynamicDsBindingIpAddr_Type()
)
agentDynamicDsBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsBindingIpAddr.setStatus("current")
_AgentDynamicDsBindingLeaseRemainingTime_Type = TimeTicks
_AgentDynamicDsBindingLeaseRemainingTime_Object = MibTableColumn
agentDynamicDsBindingLeaseRemainingTime = _AgentDynamicDsBindingLeaseRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 11, 1, 5),
    _AgentDynamicDsBindingLeaseRemainingTime_Type()
)
agentDynamicDsBindingLeaseRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsBindingLeaseRemainingTime.setStatus("current")


class _AgentDhcpSnoopingRemoteFileName_Type(DisplayString):
    """Custom type agentDhcpSnoopingRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AgentDhcpSnoopingRemoteFileName_Type.__name__ = "DisplayString"
_AgentDhcpSnoopingRemoteFileName_Object = MibScalar
agentDhcpSnoopingRemoteFileName = _AgentDhcpSnoopingRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 12),
    _AgentDhcpSnoopingRemoteFileName_Type()
)
agentDhcpSnoopingRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingRemoteFileName.setStatus("current")
_AgentDhcpSnoopingRemoteIpAddr_Type = IpAddress
_AgentDhcpSnoopingRemoteIpAddr_Object = MibScalar
agentDhcpSnoopingRemoteIpAddr = _AgentDhcpSnoopingRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 13),
    _AgentDhcpSnoopingRemoteIpAddr_Type()
)
agentDhcpSnoopingRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingRemoteIpAddr.setStatus("current")
_AgentDhcpSnoopingStoreInterval_Type = Unsigned32
_AgentDhcpSnoopingStoreInterval_Object = MibScalar
agentDhcpSnoopingStoreInterval = _AgentDhcpSnoopingStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 23, 14),
    _AgentDhcpSnoopingStoreInterval_Type()
)
agentDhcpSnoopingStoreInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpSnoopingStoreInterval.setStatus("current")
_AgentDhcpL2RelayConfigGroup_ObjectIdentity = ObjectIdentity
agentDhcpL2RelayConfigGroup = _AgentDhcpL2RelayConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24)
)


class _AgentDhcpL2RelayAdminMode_Type(TruthValue):
    """Custom type agentDhcpL2RelayAdminMode based on TruthValue"""


_AgentDhcpL2RelayAdminMode_Object = MibScalar
agentDhcpL2RelayAdminMode = _AgentDhcpL2RelayAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 1),
    _AgentDhcpL2RelayAdminMode_Type()
)
agentDhcpL2RelayAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpL2RelayAdminMode.setStatus("current")
_AgentDhcpL2RelayIfConfigTable_Object = MibTable
agentDhcpL2RelayIfConfigTable = _AgentDhcpL2RelayIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 2)
)
if mibBuilder.loadTexts:
    agentDhcpL2RelayIfConfigTable.setStatus("current")
_AgentDhcpL2RelayIfConfigEntry_Object = MibTableRow
agentDhcpL2RelayIfConfigEntry = _AgentDhcpL2RelayIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 2, 1)
)
agentDhcpL2RelayIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpL2RelayIfConfigEntry.setStatus("current")


class _AgentDhcpL2RelayIfEnable_Type(TruthValue):
    """Custom type agentDhcpL2RelayIfEnable based on TruthValue"""


_AgentDhcpL2RelayIfEnable_Object = MibTableColumn
agentDhcpL2RelayIfEnable = _AgentDhcpL2RelayIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 2, 1, 1),
    _AgentDhcpL2RelayIfEnable_Type()
)
agentDhcpL2RelayIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpL2RelayIfEnable.setStatus("current")


class _AgentDhcpL2RelayIfTrustEnable_Type(TruthValue):
    """Custom type agentDhcpL2RelayIfTrustEnable based on TruthValue"""


_AgentDhcpL2RelayIfTrustEnable_Object = MibTableColumn
agentDhcpL2RelayIfTrustEnable = _AgentDhcpL2RelayIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 2, 1, 2),
    _AgentDhcpL2RelayIfTrustEnable_Type()
)
agentDhcpL2RelayIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpL2RelayIfTrustEnable.setStatus("current")
_AgentDhcpL2RelayVlanConfigTable_Object = MibTable
agentDhcpL2RelayVlanConfigTable = _AgentDhcpL2RelayVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 3)
)
if mibBuilder.loadTexts:
    agentDhcpL2RelayVlanConfigTable.setStatus("current")
_AgentDhcpL2RelayVlanConfigEntry_Object = MibTableRow
agentDhcpL2RelayVlanConfigEntry = _AgentDhcpL2RelayVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 3, 1)
)
agentDhcpL2RelayVlanConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDhcpL2RelayVlanIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpL2RelayVlanConfigEntry.setStatus("current")
_AgentDhcpL2RelayVlanIndex_Type = VlanIndex
_AgentDhcpL2RelayVlanIndex_Object = MibTableColumn
agentDhcpL2RelayVlanIndex = _AgentDhcpL2RelayVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 3, 1, 1),
    _AgentDhcpL2RelayVlanIndex_Type()
)
agentDhcpL2RelayVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDhcpL2RelayVlanIndex.setStatus("current")


class _AgentDhcpL2RelayVlanEnable_Type(TruthValue):
    """Custom type agentDhcpL2RelayVlanEnable based on TruthValue"""


_AgentDhcpL2RelayVlanEnable_Object = MibTableColumn
agentDhcpL2RelayVlanEnable = _AgentDhcpL2RelayVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 3, 1, 2),
    _AgentDhcpL2RelayVlanEnable_Type()
)
agentDhcpL2RelayVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpL2RelayVlanEnable.setStatus("current")


class _AgentDhcpL2RelayCircuitIdVlanEnable_Type(TruthValue):
    """Custom type agentDhcpL2RelayCircuitIdVlanEnable based on TruthValue"""


_AgentDhcpL2RelayCircuitIdVlanEnable_Object = MibTableColumn
agentDhcpL2RelayCircuitIdVlanEnable = _AgentDhcpL2RelayCircuitIdVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 3, 1, 3),
    _AgentDhcpL2RelayCircuitIdVlanEnable_Type()
)
agentDhcpL2RelayCircuitIdVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpL2RelayCircuitIdVlanEnable.setStatus("current")


class _AgentDhcpL2RelayRemoteIdVlanEnable_Type(DisplayString):
    """Custom type agentDhcpL2RelayRemoteIdVlanEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AgentDhcpL2RelayRemoteIdVlanEnable_Type.__name__ = "DisplayString"
_AgentDhcpL2RelayRemoteIdVlanEnable_Object = MibTableColumn
agentDhcpL2RelayRemoteIdVlanEnable = _AgentDhcpL2RelayRemoteIdVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 3, 1, 4),
    _AgentDhcpL2RelayRemoteIdVlanEnable_Type()
)
agentDhcpL2RelayRemoteIdVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpL2RelayRemoteIdVlanEnable.setStatus("current")


class _AgentDhcpL2RelayStatsReset_Type(Integer32):
    """Custom type agentDhcpL2RelayStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentDhcpL2RelayStatsReset_Type.__name__ = "Integer32"
_AgentDhcpL2RelayStatsReset_Object = MibScalar
agentDhcpL2RelayStatsReset = _AgentDhcpL2RelayStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 6),
    _AgentDhcpL2RelayStatsReset_Type()
)
agentDhcpL2RelayStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpL2RelayStatsReset.setStatus("current")
_AgentDhcpL2RelayStatsTable_Object = MibTable
agentDhcpL2RelayStatsTable = _AgentDhcpL2RelayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 7)
)
if mibBuilder.loadTexts:
    agentDhcpL2RelayStatsTable.setStatus("current")
_AgentDhcpL2RelayStatsEntry_Object = MibTableRow
agentDhcpL2RelayStatsEntry = _AgentDhcpL2RelayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 7, 1)
)
agentDhcpL2RelayStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpL2RelayStatsEntry.setStatus("current")
_AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82_Type = Counter32
_AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82_Object = MibTableColumn
agentDhcpL2RelayUntrustedSrvrMsgsWithOptn82 = _AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 7, 1, 1),
    _AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82_Type()
)
agentDhcpL2RelayUntrustedSrvrMsgsWithOptn82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpL2RelayUntrustedSrvrMsgsWithOptn82.setStatus("current")
_AgentDhcpL2RelayUntrustedClntMsgsWithOptn82_Type = Counter32
_AgentDhcpL2RelayUntrustedClntMsgsWithOptn82_Object = MibTableColumn
agentDhcpL2RelayUntrustedClntMsgsWithOptn82 = _AgentDhcpL2RelayUntrustedClntMsgsWithOptn82_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 7, 1, 2),
    _AgentDhcpL2RelayUntrustedClntMsgsWithOptn82_Type()
)
agentDhcpL2RelayUntrustedClntMsgsWithOptn82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpL2RelayUntrustedClntMsgsWithOptn82.setStatus("current")
_AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82_Type = Counter32
_AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82_Object = MibTableColumn
agentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82 = _AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 7, 1, 3),
    _AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82_Type()
)
agentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82.setStatus("current")
_AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82_Type = Counter32
_AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82_Object = MibTableColumn
agentDhcpL2RelayTrustedClntMsgsWithoutOptn82 = _AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 24, 7, 1, 4),
    _AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82_Type()
)
agentDhcpL2RelayTrustedClntMsgsWithoutOptn82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpL2RelayTrustedClntMsgsWithoutOptn82.setStatus("current")
_AgentSwitchVoiceVLANGroup_ObjectIdentity = ObjectIdentity
agentSwitchVoiceVLANGroup = _AgentSwitchVoiceVLANGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 25)
)


class _AgentSwitchVoiceVLANAdminMode_Type(Integer32):
    """Custom type agentSwitchVoiceVLANAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchVoiceVLANAdminMode_Type.__name__ = "Integer32"
_AgentSwitchVoiceVLANAdminMode_Object = MibScalar
agentSwitchVoiceVLANAdminMode = _AgentSwitchVoiceVLANAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 25, 1),
    _AgentSwitchVoiceVLANAdminMode_Type()
)
agentSwitchVoiceVLANAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchVoiceVLANAdminMode.setStatus("current")
_AgentSwitchVoiceVlanDeviceTable_Object = MibTable
agentSwitchVoiceVlanDeviceTable = _AgentSwitchVoiceVlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 25, 2)
)
if mibBuilder.loadTexts:
    agentSwitchVoiceVlanDeviceTable.setStatus("current")
_AgentSwitchVoiceVlanDeviceEntry_Object = MibTableRow
agentSwitchVoiceVlanDeviceEntry = _AgentSwitchVoiceVlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 25, 2, 1)
)
agentSwitchVoiceVlanDeviceEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchVoiceVlanInterfaceNum"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchVoiceVlanDeviceMacAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchVoiceVlanDeviceEntry.setStatus("current")


class _AgentSwitchVoiceVlanInterfaceNum_Type(Integer32):
    """Custom type agentSwitchVoiceVlanInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSwitchVoiceVlanInterfaceNum_Type.__name__ = "Integer32"
_AgentSwitchVoiceVlanInterfaceNum_Object = MibTableColumn
agentSwitchVoiceVlanInterfaceNum = _AgentSwitchVoiceVlanInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 25, 2, 1, 1),
    _AgentSwitchVoiceVlanInterfaceNum_Type()
)
agentSwitchVoiceVlanInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchVoiceVlanInterfaceNum.setStatus("current")
_AgentSwitchVoiceVlanDeviceMacAddress_Type = MacAddress
_AgentSwitchVoiceVlanDeviceMacAddress_Object = MibTableColumn
agentSwitchVoiceVlanDeviceMacAddress = _AgentSwitchVoiceVlanDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 25, 2, 1, 2),
    _AgentSwitchVoiceVlanDeviceMacAddress_Type()
)
agentSwitchVoiceVlanDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchVoiceVlanDeviceMacAddress.setStatus("current")
_AgentSwitchAddressConflictGroup_ObjectIdentity = ObjectIdentity
agentSwitchAddressConflictGroup = _AgentSwitchAddressConflictGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26)
)


class _AgentSwitchAddressConflictDetectionStatus_Type(Integer32):
    """Custom type agentSwitchAddressConflictDetectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentSwitchAddressConflictDetectionStatus_Type.__name__ = "Integer32"
_AgentSwitchAddressConflictDetectionStatus_Object = MibScalar
agentSwitchAddressConflictDetectionStatus = _AgentSwitchAddressConflictDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26, 1),
    _AgentSwitchAddressConflictDetectionStatus_Type()
)
agentSwitchAddressConflictDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchAddressConflictDetectionStatus.setStatus("current")


class _AgentSwitchAddressConflictDetectionStatusReset_Type(Integer32):
    """Custom type agentSwitchAddressConflictDetectionStatusReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentSwitchAddressConflictDetectionStatusReset_Type.__name__ = "Integer32"
_AgentSwitchAddressConflictDetectionStatusReset_Object = MibScalar
agentSwitchAddressConflictDetectionStatusReset = _AgentSwitchAddressConflictDetectionStatusReset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26, 2),
    _AgentSwitchAddressConflictDetectionStatusReset_Type()
)
agentSwitchAddressConflictDetectionStatusReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchAddressConflictDetectionStatusReset.setStatus("current")
_AgentSwitchLastConflictingIPAddr_Type = IpAddress
_AgentSwitchLastConflictingIPAddr_Object = MibScalar
agentSwitchLastConflictingIPAddr = _AgentSwitchLastConflictingIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26, 3),
    _AgentSwitchLastConflictingIPAddr_Type()
)
agentSwitchLastConflictingIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchLastConflictingIPAddr.setStatus("current")
_AgentSwitchLastConflictingMacAddr_Type = MacAddress
_AgentSwitchLastConflictingMacAddr_Object = MibScalar
agentSwitchLastConflictingMacAddr = _AgentSwitchLastConflictingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26, 4),
    _AgentSwitchLastConflictingMacAddr_Type()
)
agentSwitchLastConflictingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchLastConflictingMacAddr.setStatus("current")
_AgentSwitchLastConflictReportedTime_Type = TimeTicks
_AgentSwitchLastConflictReportedTime_Object = MibScalar
agentSwitchLastConflictReportedTime = _AgentSwitchLastConflictReportedTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26, 5),
    _AgentSwitchLastConflictReportedTime_Type()
)
agentSwitchLastConflictReportedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchLastConflictReportedTime.setStatus("current")
_AgentSwitchConflictIPAddr_Type = IpAddress
_AgentSwitchConflictIPAddr_Object = MibScalar
agentSwitchConflictIPAddr = _AgentSwitchConflictIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26, 6),
    _AgentSwitchConflictIPAddr_Type()
)
agentSwitchConflictIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentSwitchConflictIPAddr.setStatus("current")
_AgentSwitchConflictMacAddr_Type = MacAddress
_AgentSwitchConflictMacAddr_Object = MibScalar
agentSwitchConflictMacAddr = _AgentSwitchConflictMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26, 7),
    _AgentSwitchConflictMacAddr_Type()
)
agentSwitchConflictMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentSwitchConflictMacAddr.setStatus("current")


class _AgentSwitchAddressConflictDetectionRun_Type(Integer32):
    """Custom type agentSwitchAddressConflictDetectionRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("run", 1))
    )


_AgentSwitchAddressConflictDetectionRun_Type.__name__ = "Integer32"
_AgentSwitchAddressConflictDetectionRun_Object = MibScalar
agentSwitchAddressConflictDetectionRun = _AgentSwitchAddressConflictDetectionRun_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 26, 8),
    _AgentSwitchAddressConflictDetectionRun_Type()
)
agentSwitchAddressConflictDetectionRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchAddressConflictDetectionRun.setStatus("current")
_AgentSdmPreferConfigEntry_ObjectIdentity = ObjectIdentity
agentSdmPreferConfigEntry = _AgentSdmPreferConfigEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 27)
)


class _AgentSdmPreferCurrentTemplate_Type(Integer32):
    """Custom type agentSdmPreferCurrentTemplate based on Integer32"""
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
        *(("dualDataCenter", 5),
          ("dualIPv4andIPv6", 1),
          ("dualMplsDataCenter", 6),
          ("ipv4DataCenter", 3),
          ("ipv4DataCenterPlus", 4),
          ("ipv4RoutingDefault", 2))
    )


_AgentSdmPreferCurrentTemplate_Type.__name__ = "Integer32"
_AgentSdmPreferCurrentTemplate_Object = MibScalar
agentSdmPreferCurrentTemplate = _AgentSdmPreferCurrentTemplate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 27, 1),
    _AgentSdmPreferCurrentTemplate_Type()
)
agentSdmPreferCurrentTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSdmPreferCurrentTemplate.setStatus("current")


class _AgentSdmPreferNextTemplate_Type(Integer32):
    """Custom type agentSdmPreferNextTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("dualDataCenter", 5),
          ("dualIPv4andIPv6", 1),
          ("ipv4DataCenter", 3),
          ("ipv4DataCenterPlus", 4),
          ("ipv4RoutingDefault", 2))
    )


_AgentSdmPreferNextTemplate_Type.__name__ = "Integer32"
_AgentSdmPreferNextTemplate_Object = MibScalar
agentSdmPreferNextTemplate = _AgentSdmPreferNextTemplate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 27, 2),
    _AgentSdmPreferNextTemplate_Type()
)
agentSdmPreferNextTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSdmPreferNextTemplate.setStatus("current")
_AgentSdmTemplateSummaryTable_ObjectIdentity = ObjectIdentity
agentSdmTemplateSummaryTable = _AgentSdmTemplateSummaryTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28)
)
_AgentSdmTemplateTable_Object = MibTable
agentSdmTemplateTable = _AgentSdmTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1)
)
if mibBuilder.loadTexts:
    agentSdmTemplateTable.setStatus("current")
_AgentSdmTemplateEntry_Object = MibTableRow
agentSdmTemplateEntry = _AgentSdmTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1)
)
agentSdmTemplateEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSdmTemplateId"),
)
if mibBuilder.loadTexts:
    agentSdmTemplateEntry.setStatus("current")


class _AgentSdmTemplateId_Type(Integer32):
    """Custom type agentSdmTemplateId based on Integer32"""
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
        *(("dualDataCenter", 5),
          ("dualIPv4andIPv6", 1),
          ("ipv4DataCenter", 3),
          ("ipv4DataCenterPlus", 4),
          ("ipv4RoutingDefault", 2))
    )


_AgentSdmTemplateId_Type.__name__ = "Integer32"
_AgentSdmTemplateId_Object = MibTableColumn
agentSdmTemplateId = _AgentSdmTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1, 1),
    _AgentSdmTemplateId_Type()
)
agentSdmTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSdmTemplateId.setStatus("current")
_AgentArpEntries_Type = Integer32
_AgentArpEntries_Object = MibTableColumn
agentArpEntries = _AgentArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1, 2),
    _AgentArpEntries_Type()
)
agentArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentArpEntries.setStatus("current")
_AgentIPv4UnicastRoutes_Type = Integer32
_AgentIPv4UnicastRoutes_Object = MibTableColumn
agentIPv4UnicastRoutes = _AgentIPv4UnicastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1, 3),
    _AgentIPv4UnicastRoutes_Type()
)
agentIPv4UnicastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIPv4UnicastRoutes.setStatus("current")
_AgentIPv6NdpEntries_Type = Integer32
_AgentIPv6NdpEntries_Object = MibTableColumn
agentIPv6NdpEntries = _AgentIPv6NdpEntries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1, 4),
    _AgentIPv6NdpEntries_Type()
)
agentIPv6NdpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIPv6NdpEntries.setStatus("current")
_AgentIPv6UnicastRoutes_Type = Integer32
_AgentIPv6UnicastRoutes_Object = MibTableColumn
agentIPv6UnicastRoutes = _AgentIPv6UnicastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1, 5),
    _AgentIPv6UnicastRoutes_Type()
)
agentIPv6UnicastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIPv6UnicastRoutes.setStatus("current")
_AgentEcmpNextHops_Type = Integer32
_AgentEcmpNextHops_Object = MibTableColumn
agentEcmpNextHops = _AgentEcmpNextHops_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1, 6),
    _AgentEcmpNextHops_Type()
)
agentEcmpNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpNextHops.setStatus("current")
_AgentIPv4MulticastRoutes_Type = Integer32
_AgentIPv4MulticastRoutes_Object = MibTableColumn
agentIPv4MulticastRoutes = _AgentIPv4MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1, 7),
    _AgentIPv4MulticastRoutes_Type()
)
agentIPv4MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIPv4MulticastRoutes.setStatus("current")
_AgentIPv6MulticastRoutes_Type = Integer32
_AgentIPv6MulticastRoutes_Object = MibTableColumn
agentIPv6MulticastRoutes = _AgentIPv6MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 28, 1, 1, 8),
    _AgentIPv6MulticastRoutes_Type()
)
agentIPv6MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIPv6MulticastRoutes.setStatus("current")
_AgentSwitchCutThroughGroup_ObjectIdentity = ObjectIdentity
agentSwitchCutThroughGroup = _AgentSwitchCutThroughGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 29)
)


class _AgentSwitchCutThroughConfigMode_Type(Integer32):
    """Custom type agentSwitchCutThroughConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchCutThroughConfigMode_Type.__name__ = "Integer32"
_AgentSwitchCutThroughConfigMode_Object = MibScalar
agentSwitchCutThroughConfigMode = _AgentSwitchCutThroughConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 29, 1),
    _AgentSwitchCutThroughConfigMode_Type()
)
agentSwitchCutThroughConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCutThroughConfigMode.setStatus("current")


class _AgentSwitchCutThroughRunningModeStatus_Type(Integer32):
    """Custom type agentSwitchCutThroughRunningModeStatus based on Integer32"""
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
          ("not-supported", 3))
    )


_AgentSwitchCutThroughRunningModeStatus_Type.__name__ = "Integer32"
_AgentSwitchCutThroughRunningModeStatus_Object = MibScalar
agentSwitchCutThroughRunningModeStatus = _AgentSwitchCutThroughRunningModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 29, 2),
    _AgentSwitchCutThroughRunningModeStatus_Type()
)
agentSwitchCutThroughRunningModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCutThroughRunningModeStatus.setStatus("current")


class _AgentSwitchCutThroughConfiguredModeStatus_Type(Integer32):
    """Custom type agentSwitchCutThroughConfiguredModeStatus based on Integer32"""
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
          ("not-supported", 3))
    )


_AgentSwitchCutThroughConfiguredModeStatus_Type.__name__ = "Integer32"
_AgentSwitchCutThroughConfiguredModeStatus_Object = MibScalar
agentSwitchCutThroughConfiguredModeStatus = _AgentSwitchCutThroughConfiguredModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 29, 3),
    _AgentSwitchCutThroughConfiguredModeStatus_Type()
)
agentSwitchCutThroughConfiguredModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCutThroughConfiguredModeStatus.setStatus("current")
_AgentPortTypeGroup_ObjectIdentity = ObjectIdentity
agentPortTypeGroup = _AgentPortTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 30)
)
_AgentPortType40GigBaseX_ObjectIdentity = ObjectIdentity
agentPortType40GigBaseX = _AgentPortType40GigBaseX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 30, 1)
)
if mibBuilder.loadTexts:
    agentPortType40GigBaseX.setStatus("current")
_AgentPrivateVlanGroup_ObjectIdentity = ObjectIdentity
agentPrivateVlanGroup = _AgentPrivateVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31)
)
_AgentPrivateVlanTable_Object = MibTable
agentPrivateVlanTable = _AgentPrivateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 1)
)
if mibBuilder.loadTexts:
    agentPrivateVlanTable.setStatus("current")
_AgentPrivateVlanEntry_Object = MibTableRow
agentPrivateVlanEntry = _AgentPrivateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 1, 1)
)
agentPrivateVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    agentPrivateVlanEntry.setStatus("current")


class _AgentPrivateVlanType_Type(Integer32):
    """Custom type agentPrivateVlanType based on Integer32"""
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
        *(("community", 3),
          ("isolated", 2),
          ("primary", 1),
          ("unconfigured", 4))
    )


_AgentPrivateVlanType_Type.__name__ = "Integer32"
_AgentPrivateVlanType_Object = MibTableColumn
agentPrivateVlanType = _AgentPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 1, 1, 1),
    _AgentPrivateVlanType_Type()
)
agentPrivateVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPrivateVlanType.setStatus("current")
_AgentPrivateVlanAssociate_Type = VlanList
_AgentPrivateVlanAssociate_Object = MibTableColumn
agentPrivateVlanAssociate = _AgentPrivateVlanAssociate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 1, 1, 2),
    _AgentPrivateVlanAssociate_Type()
)
agentPrivateVlanAssociate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPrivateVlanAssociate.setStatus("current")
_AgentPrivateVlanIntfAssocTable_Object = MibTable
agentPrivateVlanIntfAssocTable = _AgentPrivateVlanIntfAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 2)
)
if mibBuilder.loadTexts:
    agentPrivateVlanIntfAssocTable.setStatus("current")
_AgentPrivateVlanIntfAssocEntry_Object = MibTableRow
agentPrivateVlanIntfAssocEntry = _AgentPrivateVlanIntfAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 2, 1)
)
agentPrivateVlanIntfAssocEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentPrivateVlanIntfAssocEntry.setStatus("current")


class _AgentPrivateVlanIntfAssocHostPrimary_Type(Integer32):
    """Custom type agentPrivateVlanIntfAssocHostPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentPrivateVlanIntfAssocHostPrimary_Type.__name__ = "Integer32"
_AgentPrivateVlanIntfAssocHostPrimary_Object = MibTableColumn
agentPrivateVlanIntfAssocHostPrimary = _AgentPrivateVlanIntfAssocHostPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 2, 1, 1),
    _AgentPrivateVlanIntfAssocHostPrimary_Type()
)
agentPrivateVlanIntfAssocHostPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPrivateVlanIntfAssocHostPrimary.setStatus("current")


class _AgentPrivateVlanIntfAssocHostSecondary_Type(Integer32):
    """Custom type agentPrivateVlanIntfAssocHostSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentPrivateVlanIntfAssocHostSecondary_Type.__name__ = "Integer32"
_AgentPrivateVlanIntfAssocHostSecondary_Object = MibTableColumn
agentPrivateVlanIntfAssocHostSecondary = _AgentPrivateVlanIntfAssocHostSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 2, 1, 2),
    _AgentPrivateVlanIntfAssocHostSecondary_Type()
)
agentPrivateVlanIntfAssocHostSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPrivateVlanIntfAssocHostSecondary.setStatus("current")


class _AgentPrivateVlanIntfAssocPromiscuousPrimary_Type(Integer32):
    """Custom type agentPrivateVlanIntfAssocPromiscuousPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentPrivateVlanIntfAssocPromiscuousPrimary_Type.__name__ = "Integer32"
_AgentPrivateVlanIntfAssocPromiscuousPrimary_Object = MibTableColumn
agentPrivateVlanIntfAssocPromiscuousPrimary = _AgentPrivateVlanIntfAssocPromiscuousPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 2, 1, 3),
    _AgentPrivateVlanIntfAssocPromiscuousPrimary_Type()
)
agentPrivateVlanIntfAssocPromiscuousPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPrivateVlanIntfAssocPromiscuousPrimary.setStatus("current")
_AgentPrivateVlanIntfAssocPromiscuousSecondary_Type = VlanList
_AgentPrivateVlanIntfAssocPromiscuousSecondary_Object = MibTableColumn
agentPrivateVlanIntfAssocPromiscuousSecondary = _AgentPrivateVlanIntfAssocPromiscuousSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 2, 1, 4),
    _AgentPrivateVlanIntfAssocPromiscuousSecondary_Type()
)
agentPrivateVlanIntfAssocPromiscuousSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPrivateVlanIntfAssocPromiscuousSecondary.setStatus("current")
_AgentPrivateVlanIntfAssocOperational_Type = VlanList
_AgentPrivateVlanIntfAssocOperational_Object = MibTableColumn
agentPrivateVlanIntfAssocOperational = _AgentPrivateVlanIntfAssocOperational_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 31, 2, 1, 5),
    _AgentPrivateVlanIntfAssocOperational_Type()
)
agentPrivateVlanIntfAssocOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPrivateVlanIntfAssocOperational.setStatus("current")
_AgentSwitchPrivateGroupConfigGroup_ObjectIdentity = ObjectIdentity
agentSwitchPrivateGroupConfigGroup = _AgentSwitchPrivateGroupConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32)
)
_AgentSwitchPrivateGroupTable_Object = MibTable
agentSwitchPrivateGroupTable = _AgentSwitchPrivateGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 1)
)
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupTable.setStatus("current")
_AgentSwitchPrivateGroupEntry_Object = MibTableRow
agentSwitchPrivateGroupEntry = _AgentSwitchPrivateGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 1, 1)
)
agentSwitchPrivateGroupEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchPrivateGroupId"),
)
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupEntry.setStatus("current")


class _AgentSwitchPrivateGroupId_Type(Integer32):
    """Custom type agentSwitchPrivateGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchPrivateGroupId_Type.__name__ = "Integer32"
_AgentSwitchPrivateGroupId_Object = MibTableColumn
agentSwitchPrivateGroupId = _AgentSwitchPrivateGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 1, 1, 1),
    _AgentSwitchPrivateGroupId_Type()
)
agentSwitchPrivateGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupId.setStatus("current")


class _AgentSwitchPrivateGroupName_Type(DisplayString):
    """Custom type agentSwitchPrivateGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AgentSwitchPrivateGroupName_Type.__name__ = "DisplayString"
_AgentSwitchPrivateGroupName_Object = MibTableColumn
agentSwitchPrivateGroupName = _AgentSwitchPrivateGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 1, 1, 2),
    _AgentSwitchPrivateGroupName_Type()
)
agentSwitchPrivateGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupName.setStatus("current")


class _AgentSwitchPrivateGroupMode_Type(Integer32):
    """Custom type agentSwitchPrivateGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("community", 2),
          ("isolated", 1))
    )


_AgentSwitchPrivateGroupMode_Type.__name__ = "Integer32"
_AgentSwitchPrivateGroupMode_Object = MibTableColumn
agentSwitchPrivateGroupMode = _AgentSwitchPrivateGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 1, 1, 3),
    _AgentSwitchPrivateGroupMode_Type()
)
agentSwitchPrivateGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupMode.setStatus("current")
_AgentSwitchPrivateGroupRowStatus_Type = RowStatus
_AgentSwitchPrivateGroupRowStatus_Object = MibTableColumn
agentSwitchPrivateGroupRowStatus = _AgentSwitchPrivateGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 1, 1, 4),
    _AgentSwitchPrivateGroupRowStatus_Type()
)
agentSwitchPrivateGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupRowStatus.setStatus("current")
_AgentSwitchPrivateGroupPortTable_Object = MibTable
agentSwitchPrivateGroupPortTable = _AgentSwitchPrivateGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 2)
)
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupPortTable.setStatus("current")
_AgentSwitchPrivateGroupPortEntry_Object = MibTableRow
agentSwitchPrivateGroupPortEntry = _AgentSwitchPrivateGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 2, 1)
)
agentSwitchPrivateGroupPortEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchPrivateGroupPortGroupId"),
)
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupPortEntry.setStatus("current")


class _AgentSwitchPrivateGroupPortGroupId_Type(Integer32):
    """Custom type agentSwitchPrivateGroupPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchPrivateGroupPortGroupId_Type.__name__ = "Integer32"
_AgentSwitchPrivateGroupPortGroupId_Object = MibTableColumn
agentSwitchPrivateGroupPortGroupId = _AgentSwitchPrivateGroupPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 2, 1, 1),
    _AgentSwitchPrivateGroupPortGroupId_Type()
)
agentSwitchPrivateGroupPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupPortGroupId.setStatus("current")


class _AgentSwitchPrivateGroupPortGroupName_Type(DisplayString):
    """Custom type agentSwitchPrivateGroupPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AgentSwitchPrivateGroupPortGroupName_Type.__name__ = "DisplayString"
_AgentSwitchPrivateGroupPortGroupName_Object = MibTableColumn
agentSwitchPrivateGroupPortGroupName = _AgentSwitchPrivateGroupPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 2, 1, 2),
    _AgentSwitchPrivateGroupPortGroupName_Type()
)
agentSwitchPrivateGroupPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupPortGroupName.setStatus("current")
_AgentSwitchPrivateGroupPortPortList_Type = PortList
_AgentSwitchPrivateGroupPortPortList_Object = MibTableColumn
agentSwitchPrivateGroupPortPortList = _AgentSwitchPrivateGroupPortPortList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 32, 2, 1, 3),
    _AgentSwitchPrivateGroupPortPortList_Type()
)
agentSwitchPrivateGroupPortPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchPrivateGroupPortPortList.setStatus("current")
_AgentDhcpv6SnoopingConfigGroup_ObjectIdentity = ObjectIdentity
agentDhcpv6SnoopingConfigGroup = _AgentDhcpv6SnoopingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33)
)


class _AgentDhcpv6SnoopingAdminMode_Type(TruthValue):
    """Custom type agentDhcpv6SnoopingAdminMode based on TruthValue"""


_AgentDhcpv6SnoopingAdminMode_Object = MibScalar
agentDhcpv6SnoopingAdminMode = _AgentDhcpv6SnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 1),
    _AgentDhcpv6SnoopingAdminMode_Type()
)
agentDhcpv6SnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingAdminMode.setStatus("current")


class _AgentDhcpv6SnoopingVerifyMac_Type(TruthValue):
    """Custom type agentDhcpv6SnoopingVerifyMac based on TruthValue"""


_AgentDhcpv6SnoopingVerifyMac_Object = MibScalar
agentDhcpv6SnoopingVerifyMac = _AgentDhcpv6SnoopingVerifyMac_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 2),
    _AgentDhcpv6SnoopingVerifyMac_Type()
)
agentDhcpv6SnoopingVerifyMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingVerifyMac.setStatus("current")
_AgentDhcpv6SnoopingVlanConfigTable_Object = MibTable
agentDhcpv6SnoopingVlanConfigTable = _AgentDhcpv6SnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 3)
)
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingVlanConfigTable.setStatus("current")
_AgentDhcpv6SnoopingVlanConfigEntry_Object = MibTableRow
agentDhcpv6SnoopingVlanConfigEntry = _AgentDhcpv6SnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 3, 1)
)
agentDhcpv6SnoopingVlanConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDhcpv6SnoopingVlanIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingVlanConfigEntry.setStatus("current")
_AgentDhcpv6SnoopingVlanIndex_Type = VlanIndex
_AgentDhcpv6SnoopingVlanIndex_Object = MibTableColumn
agentDhcpv6SnoopingVlanIndex = _AgentDhcpv6SnoopingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 3, 1, 1),
    _AgentDhcpv6SnoopingVlanIndex_Type()
)
agentDhcpv6SnoopingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingVlanIndex.setStatus("current")


class _AgentDhcpv6SnoopingVlanEnable_Type(TruthValue):
    """Custom type agentDhcpv6SnoopingVlanEnable based on TruthValue"""


_AgentDhcpv6SnoopingVlanEnable_Object = MibTableColumn
agentDhcpv6SnoopingVlanEnable = _AgentDhcpv6SnoopingVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 3, 1, 2),
    _AgentDhcpv6SnoopingVlanEnable_Type()
)
agentDhcpv6SnoopingVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingVlanEnable.setStatus("current")
_AgentDhcpv6SnoopingIfConfigTable_Object = MibTable
agentDhcpv6SnoopingIfConfigTable = _AgentDhcpv6SnoopingIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 4)
)
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingIfConfigTable.setStatus("current")
_AgentDhcpv6SnoopingIfConfigEntry_Object = MibTableRow
agentDhcpv6SnoopingIfConfigEntry = _AgentDhcpv6SnoopingIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 4, 1)
)
agentDhcpv6SnoopingIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingIfConfigEntry.setStatus("current")


class _AgentDhcpv6SnoopingIfTrustEnable_Type(TruthValue):
    """Custom type agentDhcpv6SnoopingIfTrustEnable based on TruthValue"""


_AgentDhcpv6SnoopingIfTrustEnable_Object = MibTableColumn
agentDhcpv6SnoopingIfTrustEnable = _AgentDhcpv6SnoopingIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 4, 1, 1),
    _AgentDhcpv6SnoopingIfTrustEnable_Type()
)
agentDhcpv6SnoopingIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingIfTrustEnable.setStatus("current")


class _AgentDhcpv6SnoopingIfLogEnable_Type(TruthValue):
    """Custom type agentDhcpv6SnoopingIfLogEnable based on TruthValue"""


_AgentDhcpv6SnoopingIfLogEnable_Object = MibTableColumn
agentDhcpv6SnoopingIfLogEnable = _AgentDhcpv6SnoopingIfLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 4, 1, 2),
    _AgentDhcpv6SnoopingIfLogEnable_Type()
)
agentDhcpv6SnoopingIfLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingIfLogEnable.setStatus("current")


class _AgentDhcpv6SnoopingIfRateLimit_Type(Integer32):
    """Custom type agentDhcpv6SnoopingIfRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 300),
    )


_AgentDhcpv6SnoopingIfRateLimit_Type.__name__ = "Integer32"
_AgentDhcpv6SnoopingIfRateLimit_Object = MibTableColumn
agentDhcpv6SnoopingIfRateLimit = _AgentDhcpv6SnoopingIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 4, 1, 3),
    _AgentDhcpv6SnoopingIfRateLimit_Type()
)
agentDhcpv6SnoopingIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingIfRateLimit.setUnits("packets per second")


class _AgentDhcpv6SnoopingIfBurstInterval_Type(Integer32):
    """Custom type agentDhcpv6SnoopingIfBurstInterval based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_AgentDhcpv6SnoopingIfBurstInterval_Type.__name__ = "Integer32"
_AgentDhcpv6SnoopingIfBurstInterval_Object = MibTableColumn
agentDhcpv6SnoopingIfBurstInterval = _AgentDhcpv6SnoopingIfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 4, 1, 4),
    _AgentDhcpv6SnoopingIfBurstInterval_Type()
)
agentDhcpv6SnoopingIfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingIfBurstInterval.setStatus("current")
_AgentIpv6sgIfConfigTable_Object = MibTable
agentIpv6sgIfConfigTable = _AgentIpv6sgIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 5)
)
if mibBuilder.loadTexts:
    agentIpv6sgIfConfigTable.setStatus("current")
_AgentIpv6sgIfConfigEntry_Object = MibTableRow
agentIpv6sgIfConfigEntry = _AgentIpv6sgIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 5, 1)
)
agentIpv6sgIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentIpv6sgIfConfigEntry.setStatus("current")


class _AgentIpv6sgIfVerifySource_Type(TruthValue):
    """Custom type agentIpv6sgIfVerifySource based on TruthValue"""


_AgentIpv6sgIfVerifySource_Object = MibTableColumn
agentIpv6sgIfVerifySource = _AgentIpv6sgIfVerifySource_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 5, 1, 1),
    _AgentIpv6sgIfVerifySource_Type()
)
agentIpv6sgIfVerifySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6sgIfVerifySource.setStatus("current")


class _AgentIpv6sgIfPortSecurity_Type(TruthValue):
    """Custom type agentIpv6sgIfPortSecurity based on TruthValue"""


_AgentIpv6sgIfPortSecurity_Object = MibTableColumn
agentIpv6sgIfPortSecurity = _AgentIpv6sgIfPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 5, 1, 2),
    _AgentIpv6sgIfPortSecurity_Type()
)
agentIpv6sgIfPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6sgIfPortSecurity.setStatus("current")


class _AgentDhcpv6SnoopingStatsReset_Type(Integer32):
    """Custom type agentDhcpv6SnoopingStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentDhcpv6SnoopingStatsReset_Type.__name__ = "Integer32"
_AgentDhcpv6SnoopingStatsReset_Object = MibScalar
agentDhcpv6SnoopingStatsReset = _AgentDhcpv6SnoopingStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 6),
    _AgentDhcpv6SnoopingStatsReset_Type()
)
agentDhcpv6SnoopingStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingStatsReset.setStatus("current")
_AgentDhcpv6SnoopingStatsTable_Object = MibTable
agentDhcpv6SnoopingStatsTable = _AgentDhcpv6SnoopingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 7)
)
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingStatsTable.setStatus("current")
_AgentDhcpv6SnoopingStatsEntry_Object = MibTableRow
agentDhcpv6SnoopingStatsEntry = _AgentDhcpv6SnoopingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 7, 1)
)
agentDhcpv6SnoopingStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingStatsEntry.setStatus("current")
_AgentDhcpv6SnoopingMacVerifyFailures_Type = Counter32
_AgentDhcpv6SnoopingMacVerifyFailures_Object = MibTableColumn
agentDhcpv6SnoopingMacVerifyFailures = _AgentDhcpv6SnoopingMacVerifyFailures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 7, 1, 1),
    _AgentDhcpv6SnoopingMacVerifyFailures_Type()
)
agentDhcpv6SnoopingMacVerifyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingMacVerifyFailures.setStatus("current")
_AgentDhcpv6SnoopingInvalidClientMessages_Type = Counter32
_AgentDhcpv6SnoopingInvalidClientMessages_Object = MibTableColumn
agentDhcpv6SnoopingInvalidClientMessages = _AgentDhcpv6SnoopingInvalidClientMessages_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 7, 1, 2),
    _AgentDhcpv6SnoopingInvalidClientMessages_Type()
)
agentDhcpv6SnoopingInvalidClientMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingInvalidClientMessages.setStatus("current")
_AgentDhcpv6SnoopingInvalidServerMessages_Type = Counter32
_AgentDhcpv6SnoopingInvalidServerMessages_Object = MibTableColumn
agentDhcpv6SnoopingInvalidServerMessages = _AgentDhcpv6SnoopingInvalidServerMessages_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 7, 1, 3),
    _AgentDhcpv6SnoopingInvalidServerMessages_Type()
)
agentDhcpv6SnoopingInvalidServerMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingInvalidServerMessages.setStatus("current")
_AgentStaticIpv6sgBindingTable_Object = MibTable
agentStaticIpv6sgBindingTable = _AgentStaticIpv6sgBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 8)
)
if mibBuilder.loadTexts:
    agentStaticIpv6sgBindingTable.setStatus("current")
_AgentStaticIpv6sgBindingEntry_Object = MibTableRow
agentStaticIpv6sgBindingEntry = _AgentStaticIpv6sgBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 8, 1)
)
agentStaticIpv6sgBindingEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticIpv6sgBindingIfIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticIpv6sgBindingVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticIpv6sgBindingIpAddr"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticIpv6sgBindingMacAddr"),
)
if mibBuilder.loadTexts:
    agentStaticIpv6sgBindingEntry.setStatus("current")
_AgentStaticIpv6sgBindingIfIndex_Type = InterfaceIndex
_AgentStaticIpv6sgBindingIfIndex_Object = MibTableColumn
agentStaticIpv6sgBindingIfIndex = _AgentStaticIpv6sgBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 8, 1, 1),
    _AgentStaticIpv6sgBindingIfIndex_Type()
)
agentStaticIpv6sgBindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpv6sgBindingIfIndex.setStatus("current")
_AgentStaticIpv6sgBindingVlanId_Type = VlanIndex
_AgentStaticIpv6sgBindingVlanId_Object = MibTableColumn
agentStaticIpv6sgBindingVlanId = _AgentStaticIpv6sgBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 8, 1, 2),
    _AgentStaticIpv6sgBindingVlanId_Type()
)
agentStaticIpv6sgBindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpv6sgBindingVlanId.setStatus("current")
_AgentStaticIpv6sgBindingIpAddr_Type = Ipv6Address
_AgentStaticIpv6sgBindingIpAddr_Object = MibTableColumn
agentStaticIpv6sgBindingIpAddr = _AgentStaticIpv6sgBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 8, 1, 3),
    _AgentStaticIpv6sgBindingIpAddr_Type()
)
agentStaticIpv6sgBindingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpv6sgBindingIpAddr.setStatus("current")
_AgentStaticIpv6sgBindingMacAddr_Type = MacAddress
_AgentStaticIpv6sgBindingMacAddr_Object = MibTableColumn
agentStaticIpv6sgBindingMacAddr = _AgentStaticIpv6sgBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 8, 1, 4),
    _AgentStaticIpv6sgBindingMacAddr_Type()
)
agentStaticIpv6sgBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpv6sgBindingMacAddr.setStatus("current")
_AgentStaticIpv6sgBindingRowStatus_Type = RowStatus
_AgentStaticIpv6sgBindingRowStatus_Object = MibTableColumn
agentStaticIpv6sgBindingRowStatus = _AgentStaticIpv6sgBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 8, 1, 5),
    _AgentStaticIpv6sgBindingRowStatus_Type()
)
agentStaticIpv6sgBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticIpv6sgBindingRowStatus.setStatus("current")
_AgentDynamicIpv6sgBindingTable_Object = MibTable
agentDynamicIpv6sgBindingTable = _AgentDynamicIpv6sgBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 9)
)
if mibBuilder.loadTexts:
    agentDynamicIpv6sgBindingTable.setStatus("current")
_AgentDynamicIpv6sgBindingEntry_Object = MibTableRow
agentDynamicIpv6sgBindingEntry = _AgentDynamicIpv6sgBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 9, 1)
)
agentDynamicIpv6sgBindingEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicIpv6sgBindingIfIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicIpv6sgBindingVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicIpv6sgBindingIpAddr"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicIpv6sgBindingMacAddr"),
)
if mibBuilder.loadTexts:
    agentDynamicIpv6sgBindingEntry.setStatus("current")
_AgentDynamicIpv6sgBindingIfIndex_Type = InterfaceIndex
_AgentDynamicIpv6sgBindingIfIndex_Object = MibTableColumn
agentDynamicIpv6sgBindingIfIndex = _AgentDynamicIpv6sgBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 9, 1, 1),
    _AgentDynamicIpv6sgBindingIfIndex_Type()
)
agentDynamicIpv6sgBindingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicIpv6sgBindingIfIndex.setStatus("current")
_AgentDynamicIpv6sgBindingVlanId_Type = VlanIndex
_AgentDynamicIpv6sgBindingVlanId_Object = MibTableColumn
agentDynamicIpv6sgBindingVlanId = _AgentDynamicIpv6sgBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 9, 1, 2),
    _AgentDynamicIpv6sgBindingVlanId_Type()
)
agentDynamicIpv6sgBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicIpv6sgBindingVlanId.setStatus("current")
_AgentDynamicIpv6sgBindingIpAddr_Type = Ipv6Address
_AgentDynamicIpv6sgBindingIpAddr_Object = MibTableColumn
agentDynamicIpv6sgBindingIpAddr = _AgentDynamicIpv6sgBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 9, 1, 3),
    _AgentDynamicIpv6sgBindingIpAddr_Type()
)
agentDynamicIpv6sgBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicIpv6sgBindingIpAddr.setStatus("current")
_AgentDynamicIpv6sgBindingMacAddr_Type = MacAddress
_AgentDynamicIpv6sgBindingMacAddr_Object = MibTableColumn
agentDynamicIpv6sgBindingMacAddr = _AgentDynamicIpv6sgBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 9, 1, 4),
    _AgentDynamicIpv6sgBindingMacAddr_Type()
)
agentDynamicIpv6sgBindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicIpv6sgBindingMacAddr.setStatus("current")
_AgentStaticDsv6BindingTable_Object = MibTable
agentStaticDsv6BindingTable = _AgentStaticDsv6BindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 10)
)
if mibBuilder.loadTexts:
    agentStaticDsv6BindingTable.setStatus("current")
_AgentStaticDsv6BindingEntry_Object = MibTableRow
agentStaticDsv6BindingEntry = _AgentStaticDsv6BindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 10, 1)
)
agentStaticDsv6BindingEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStaticDsv6BindingMacAddr"),
)
if mibBuilder.loadTexts:
    agentStaticDsv6BindingEntry.setStatus("current")
_AgentStaticDsv6BindingIfIndex_Type = InterfaceIndex
_AgentStaticDsv6BindingIfIndex_Object = MibTableColumn
agentStaticDsv6BindingIfIndex = _AgentStaticDsv6BindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 10, 1, 1),
    _AgentStaticDsv6BindingIfIndex_Type()
)
agentStaticDsv6BindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsv6BindingIfIndex.setStatus("current")
_AgentStaticDsv6BindingVlanId_Type = VlanId
_AgentStaticDsv6BindingVlanId_Object = MibTableColumn
agentStaticDsv6BindingVlanId = _AgentStaticDsv6BindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 10, 1, 2),
    _AgentStaticDsv6BindingVlanId_Type()
)
agentStaticDsv6BindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsv6BindingVlanId.setStatus("current")
_AgentStaticDsv6BindingMacAddr_Type = MacAddress
_AgentStaticDsv6BindingMacAddr_Object = MibTableColumn
agentStaticDsv6BindingMacAddr = _AgentStaticDsv6BindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 10, 1, 3),
    _AgentStaticDsv6BindingMacAddr_Type()
)
agentStaticDsv6BindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsv6BindingMacAddr.setStatus("current")
_AgentStaticDsv6BindingIpAddr_Type = Ipv6Address
_AgentStaticDsv6BindingIpAddr_Object = MibTableColumn
agentStaticDsv6BindingIpAddr = _AgentStaticDsv6BindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 10, 1, 4),
    _AgentStaticDsv6BindingIpAddr_Type()
)
agentStaticDsv6BindingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsv6BindingIpAddr.setStatus("current")
_AgentStaticDsv6BindingRowStatus_Type = RowStatus
_AgentStaticDsv6BindingRowStatus_Object = MibTableColumn
agentStaticDsv6BindingRowStatus = _AgentStaticDsv6BindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 10, 1, 5),
    _AgentStaticDsv6BindingRowStatus_Type()
)
agentStaticDsv6BindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStaticDsv6BindingRowStatus.setStatus("current")
_AgentDynamicDsv6BindingTable_Object = MibTable
agentDynamicDsv6BindingTable = _AgentDynamicDsv6BindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 11)
)
if mibBuilder.loadTexts:
    agentDynamicDsv6BindingTable.setStatus("current")
_AgentDynamicDsv6BindingEntry_Object = MibTableRow
agentDynamicDsv6BindingEntry = _AgentDynamicDsv6BindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 11, 1)
)
agentDynamicDsv6BindingEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDynamicDsv6BindingMacAddr"),
)
if mibBuilder.loadTexts:
    agentDynamicDsv6BindingEntry.setStatus("current")
_AgentDynamicDsv6BindingIfIndex_Type = InterfaceIndex
_AgentDynamicDsv6BindingIfIndex_Object = MibTableColumn
agentDynamicDsv6BindingIfIndex = _AgentDynamicDsv6BindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 11, 1, 1),
    _AgentDynamicDsv6BindingIfIndex_Type()
)
agentDynamicDsv6BindingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsv6BindingIfIndex.setStatus("current")
_AgentDynamicDsv6BindingVlanId_Type = VlanIndex
_AgentDynamicDsv6BindingVlanId_Object = MibTableColumn
agentDynamicDsv6BindingVlanId = _AgentDynamicDsv6BindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 11, 1, 2),
    _AgentDynamicDsv6BindingVlanId_Type()
)
agentDynamicDsv6BindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsv6BindingVlanId.setStatus("current")
_AgentDynamicDsv6BindingMacAddr_Type = MacAddress
_AgentDynamicDsv6BindingMacAddr_Object = MibTableColumn
agentDynamicDsv6BindingMacAddr = _AgentDynamicDsv6BindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 11, 1, 3),
    _AgentDynamicDsv6BindingMacAddr_Type()
)
agentDynamicDsv6BindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsv6BindingMacAddr.setStatus("current")
_AgentDynamicDsv6BindingIpAddr_Type = Ipv6Address
_AgentDynamicDsv6BindingIpAddr_Object = MibTableColumn
agentDynamicDsv6BindingIpAddr = _AgentDynamicDsv6BindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 11, 1, 4),
    _AgentDynamicDsv6BindingIpAddr_Type()
)
agentDynamicDsv6BindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsv6BindingIpAddr.setStatus("current")
_AgentDynamicDsv6BindingLeaseRemainingTime_Type = TimeTicks
_AgentDynamicDsv6BindingLeaseRemainingTime_Object = MibTableColumn
agentDynamicDsv6BindingLeaseRemainingTime = _AgentDynamicDsv6BindingLeaseRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 11, 1, 5),
    _AgentDynamicDsv6BindingLeaseRemainingTime_Type()
)
agentDynamicDsv6BindingLeaseRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDynamicDsv6BindingLeaseRemainingTime.setStatus("current")


class _AgentDhcpv6SnoopingRemoteFileName_Type(DisplayString):
    """Custom type agentDhcpv6SnoopingRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AgentDhcpv6SnoopingRemoteFileName_Type.__name__ = "DisplayString"
_AgentDhcpv6SnoopingRemoteFileName_Object = MibScalar
agentDhcpv6SnoopingRemoteFileName = _AgentDhcpv6SnoopingRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 12),
    _AgentDhcpv6SnoopingRemoteFileName_Type()
)
agentDhcpv6SnoopingRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingRemoteFileName.setStatus("current")
_AgentDhcpv6SnoopingRemoteIpAddr_Type = IpAddress
_AgentDhcpv6SnoopingRemoteIpAddr_Object = MibScalar
agentDhcpv6SnoopingRemoteIpAddr = _AgentDhcpv6SnoopingRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 13),
    _AgentDhcpv6SnoopingRemoteIpAddr_Type()
)
agentDhcpv6SnoopingRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingRemoteIpAddr.setStatus("current")
_AgentDhcpv6SnoopingStoreInterval_Type = Unsigned32
_AgentDhcpv6SnoopingStoreInterval_Object = MibScalar
agentDhcpv6SnoopingStoreInterval = _AgentDhcpv6SnoopingStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 33, 14),
    _AgentDhcpv6SnoopingStoreInterval_Type()
)
agentDhcpv6SnoopingStoreInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpv6SnoopingStoreInterval.setStatus("current")
_AgentSwitchSnoopSSMGroupTable_Object = MibTable
agentSwitchSnoopSSMGroupTable = _AgentSwitchSnoopSSMGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 34)
)
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMGroupTable.setStatus("current")
_AgentSwitchSnoopSSMGroupEntry_Object = MibTableRow
agentSwitchSnoopSSMGroupEntry = _AgentSwitchSnoopSSMGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 34, 1)
)
agentSwitchSnoopSSMGroupEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMGroupAddressType"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMGroupIfIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMGroupVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMGroupAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMGroupEntry.setStatus("current")
_AgentSwitchSnoopSSMGroupAddressType_Type = InetAddressType
_AgentSwitchSnoopSSMGroupAddressType_Object = MibTableColumn
agentSwitchSnoopSSMGroupAddressType = _AgentSwitchSnoopSSMGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 34, 1, 1),
    _AgentSwitchSnoopSSMGroupAddressType_Type()
)
agentSwitchSnoopSSMGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMGroupAddressType.setStatus("current")


class _AgentSwitchSnoopSSMGroupAddress_Type(InetAddress):
    """Custom type agentSwitchSnoopSSMGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AgentSwitchSnoopSSMGroupAddress_Type.__name__ = "InetAddress"
_AgentSwitchSnoopSSMGroupAddress_Object = MibTableColumn
agentSwitchSnoopSSMGroupAddress = _AgentSwitchSnoopSSMGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 34, 1, 2),
    _AgentSwitchSnoopSSMGroupAddress_Type()
)
agentSwitchSnoopSSMGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMGroupAddress.setStatus("current")
_AgentSwitchSnoopSSMGroupIfIndex_Type = InterfaceIndex
_AgentSwitchSnoopSSMGroupIfIndex_Object = MibTableColumn
agentSwitchSnoopSSMGroupIfIndex = _AgentSwitchSnoopSSMGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 34, 1, 3),
    _AgentSwitchSnoopSSMGroupIfIndex_Type()
)
agentSwitchSnoopSSMGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMGroupIfIndex.setStatus("current")
_AgentSwitchSnoopSSMGroupVlanId_Type = VlanIndex
_AgentSwitchSnoopSSMGroupVlanId_Object = MibTableColumn
agentSwitchSnoopSSMGroupVlanId = _AgentSwitchSnoopSSMGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 34, 1, 4),
    _AgentSwitchSnoopSSMGroupVlanId_Type()
)
agentSwitchSnoopSSMGroupVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMGroupVlanId.setStatus("current")
_AgentSwitchSnoopSSMGroupLastReporter_Type = InetAddress
_AgentSwitchSnoopSSMGroupLastReporter_Object = MibTableColumn
agentSwitchSnoopSSMGroupLastReporter = _AgentSwitchSnoopSSMGroupLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 34, 1, 5),
    _AgentSwitchSnoopSSMGroupLastReporter_Type()
)
agentSwitchSnoopSSMGroupLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMGroupLastReporter.setStatus("current")


class _AgentSwitchSnoopSSMGroupSourceFilterMode_Type(Integer32):
    """Custom type agentSwitchSnoopSSMGroupSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_AgentSwitchSnoopSSMGroupSourceFilterMode_Type.__name__ = "Integer32"
_AgentSwitchSnoopSSMGroupSourceFilterMode_Object = MibTableColumn
agentSwitchSnoopSSMGroupSourceFilterMode = _AgentSwitchSnoopSSMGroupSourceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 34, 1, 6),
    _AgentSwitchSnoopSSMGroupSourceFilterMode_Type()
)
agentSwitchSnoopSSMGroupSourceFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMGroupSourceFilterMode.setStatus("current")
_AgentSwitchSnoopSSMSrcListTable_Object = MibTable
agentSwitchSnoopSSMSrcListTable = _AgentSwitchSnoopSSMSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 35)
)
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMSrcListTable.setStatus("current")
_AgentSwitchSnoopSSMSrcListEntry_Object = MibTableRow
agentSwitchSnoopSSMSrcListEntry = _AgentSwitchSnoopSSMSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 35, 1)
)
agentSwitchSnoopSSMSrcListEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMSrcListAddressType"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMSrcListIfIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMSrcListVlanId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMSrcListHostAddress"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMSrcListAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMSrcListEntry.setStatus("current")
_AgentSwitchSnoopSSMSrcListAddressType_Type = InetAddressType
_AgentSwitchSnoopSSMSrcListAddressType_Object = MibTableColumn
agentSwitchSnoopSSMSrcListAddressType = _AgentSwitchSnoopSSMSrcListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 35, 1, 1),
    _AgentSwitchSnoopSSMSrcListAddressType_Type()
)
agentSwitchSnoopSSMSrcListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMSrcListAddressType.setStatus("current")


class _AgentSwitchSnoopSSMSrcListAddress_Type(InetAddress):
    """Custom type agentSwitchSnoopSSMSrcListAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AgentSwitchSnoopSSMSrcListAddress_Type.__name__ = "InetAddress"
_AgentSwitchSnoopSSMSrcListAddress_Object = MibTableColumn
agentSwitchSnoopSSMSrcListAddress = _AgentSwitchSnoopSSMSrcListAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 35, 1, 2),
    _AgentSwitchSnoopSSMSrcListAddress_Type()
)
agentSwitchSnoopSSMSrcListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMSrcListAddress.setStatus("current")
_AgentSwitchSnoopSSMSrcListIfIndex_Type = InterfaceIndex
_AgentSwitchSnoopSSMSrcListIfIndex_Object = MibTableColumn
agentSwitchSnoopSSMSrcListIfIndex = _AgentSwitchSnoopSSMSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 35, 1, 3),
    _AgentSwitchSnoopSSMSrcListIfIndex_Type()
)
agentSwitchSnoopSSMSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMSrcListIfIndex.setStatus("current")
_AgentSwitchSnoopSSMSrcListVlanId_Type = VlanIndex
_AgentSwitchSnoopSSMSrcListVlanId_Object = MibTableColumn
agentSwitchSnoopSSMSrcListVlanId = _AgentSwitchSnoopSSMSrcListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 35, 1, 4),
    _AgentSwitchSnoopSSMSrcListVlanId_Type()
)
agentSwitchSnoopSSMSrcListVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMSrcListVlanId.setStatus("current")


class _AgentSwitchSnoopSSMSrcListHostAddress_Type(InetAddress):
    """Custom type agentSwitchSnoopSSMSrcListHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AgentSwitchSnoopSSMSrcListHostAddress_Type.__name__ = "InetAddress"
_AgentSwitchSnoopSSMSrcListHostAddress_Object = MibTableColumn
agentSwitchSnoopSSMSrcListHostAddress = _AgentSwitchSnoopSSMSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 35, 1, 5),
    _AgentSwitchSnoopSSMSrcListHostAddress_Type()
)
agentSwitchSnoopSSMSrcListHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMSrcListHostAddress.setStatus("current")
_AgentSwitchSnoopSSMFDBTable_Object = MibTable
agentSwitchSnoopSSMFDBTable = _AgentSwitchSnoopSSMFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 36)
)
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMFDBTable.setStatus("current")
_AgentSwitchSnoopSSMFDBEntry_Object = MibTableRow
agentSwitchSnoopSSMFDBEntry = _AgentSwitchSnoopSSMFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 36, 1)
)
agentSwitchSnoopSSMFDBEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMFDBGroupAddressType"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMFDBGroupAddress"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMFDBSourceAddress"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchSnoopSSMFDBVlanIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMFDBEntry.setStatus("current")
_AgentSwitchSnoopSSMFDBVlanIndex_Type = VlanIndex
_AgentSwitchSnoopSSMFDBVlanIndex_Object = MibTableColumn
agentSwitchSnoopSSMFDBVlanIndex = _AgentSwitchSnoopSSMFDBVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 36, 1, 1),
    _AgentSwitchSnoopSSMFDBVlanIndex_Type()
)
agentSwitchSnoopSSMFDBVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMFDBVlanIndex.setStatus("current")
_AgentSwitchSnoopSSMFDBGroupAddressType_Type = InetAddressType
_AgentSwitchSnoopSSMFDBGroupAddressType_Object = MibTableColumn
agentSwitchSnoopSSMFDBGroupAddressType = _AgentSwitchSnoopSSMFDBGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 36, 1, 2),
    _AgentSwitchSnoopSSMFDBGroupAddressType_Type()
)
agentSwitchSnoopSSMFDBGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMFDBGroupAddressType.setStatus("current")
_AgentSwitchSnoopSSMFDBGroupAddress_Type = InetAddress
_AgentSwitchSnoopSSMFDBGroupAddress_Object = MibTableColumn
agentSwitchSnoopSSMFDBGroupAddress = _AgentSwitchSnoopSSMFDBGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 36, 1, 3),
    _AgentSwitchSnoopSSMFDBGroupAddress_Type()
)
agentSwitchSnoopSSMFDBGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMFDBGroupAddress.setStatus("current")
_AgentSwitchSnoopSSMFDBSourceAddress_Type = InetAddress
_AgentSwitchSnoopSSMFDBSourceAddress_Object = MibTableColumn
agentSwitchSnoopSSMFDBSourceAddress = _AgentSwitchSnoopSSMFDBSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 36, 1, 4),
    _AgentSwitchSnoopSSMFDBSourceAddress_Type()
)
agentSwitchSnoopSSMFDBSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMFDBSourceAddress.setStatus("current")
_AgentSwitchSnoopSSMFDBIncludePortList_Type = AgentPortMask
_AgentSwitchSnoopSSMFDBIncludePortList_Object = MibTableColumn
agentSwitchSnoopSSMFDBIncludePortList = _AgentSwitchSnoopSSMFDBIncludePortList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 36, 1, 5),
    _AgentSwitchSnoopSSMFDBIncludePortList_Type()
)
agentSwitchSnoopSSMFDBIncludePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMFDBIncludePortList.setStatus("current")
_AgentSwitchSnoopSSMFDBExcludePortList_Type = AgentPortMask
_AgentSwitchSnoopSSMFDBExcludePortList_Object = MibTableColumn
agentSwitchSnoopSSMFDBExcludePortList = _AgentSwitchSnoopSSMFDBExcludePortList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 36, 1, 6),
    _AgentSwitchSnoopSSMFDBExcludePortList_Type()
)
agentSwitchSnoopSSMFDBExcludePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchSnoopSSMFDBExcludePortList.setStatus("current")
_AgentSwitchportConfigTable_Object = MibTable
agentSwitchportConfigTable = _AgentSwitchportConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37)
)
if mibBuilder.loadTexts:
    agentSwitchportConfigTable.setStatus("current")
_AgentSwitchportConfigEntry_Object = MibTableRow
agentSwitchportConfigEntry = _AgentSwitchportConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1)
)
agentSwitchportConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentSwitchportIntfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchportConfigEntry.setStatus("current")


class _AgentSwitchportIntfIndex_Type(Integer32):
    """Custom type agentSwitchportIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSwitchportIntfIndex_Type.__name__ = "Integer32"
_AgentSwitchportIntfIndex_Object = MibTableColumn
agentSwitchportIntfIndex = _AgentSwitchportIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 1),
    _AgentSwitchportIntfIndex_Type()
)
agentSwitchportIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchportIntfIndex.setStatus("current")


class _AgentSwitchportMode_Type(Integer32):
    """Custom type agentSwitchportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("general", 3),
          ("trunk", 2))
    )


_AgentSwitchportMode_Type.__name__ = "Integer32"
_AgentSwitchportMode_Object = MibTableColumn
agentSwitchportMode = _AgentSwitchportMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 2),
    _AgentSwitchportMode_Type()
)
agentSwitchportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchportMode.setStatus("current")
_AgentSwitchportAccessVlanID_Type = VlanIndex
_AgentSwitchportAccessVlanID_Object = MibTableColumn
agentSwitchportAccessVlanID = _AgentSwitchportAccessVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 3),
    _AgentSwitchportAccessVlanID_Type()
)
agentSwitchportAccessVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchportAccessVlanID.setStatus("current")
_AgentSwitchportTrunkNativeVlanID_Type = VlanIndex
_AgentSwitchportTrunkNativeVlanID_Object = MibTableColumn
agentSwitchportTrunkNativeVlanID = _AgentSwitchportTrunkNativeVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 4),
    _AgentSwitchportTrunkNativeVlanID_Type()
)
agentSwitchportTrunkNativeVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchportTrunkNativeVlanID.setStatus("current")


class _AgentSwitchportTrunkNativeVlanTagging_Type(Integer32):
    """Custom type agentSwitchportTrunkNativeVlanTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchportTrunkNativeVlanTagging_Type.__name__ = "Integer32"
_AgentSwitchportTrunkNativeVlanTagging_Object = MibTableColumn
agentSwitchportTrunkNativeVlanTagging = _AgentSwitchportTrunkNativeVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 5),
    _AgentSwitchportTrunkNativeVlanTagging_Type()
)
agentSwitchportTrunkNativeVlanTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchportTrunkNativeVlanTagging.setStatus("current")
_AgentSwitchportTrunkAllowedVlanList_Type = VlanList
_AgentSwitchportTrunkAllowedVlanList_Object = MibTableColumn
agentSwitchportTrunkAllowedVlanList = _AgentSwitchportTrunkAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 6),
    _AgentSwitchportTrunkAllowedVlanList_Type()
)
agentSwitchportTrunkAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchportTrunkAllowedVlanList.setStatus("current")
_AgentSwitchportGeneralUntaggedVlanList_Type = VlanList
_AgentSwitchportGeneralUntaggedVlanList_Object = MibTableColumn
agentSwitchportGeneralUntaggedVlanList = _AgentSwitchportGeneralUntaggedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 7),
    _AgentSwitchportGeneralUntaggedVlanList_Type()
)
agentSwitchportGeneralUntaggedVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchportGeneralUntaggedVlanList.setStatus("current")
_AgentSwitchportGeneralTaggedVlanList_Type = VlanList
_AgentSwitchportGeneralTaggedVlanList_Object = MibTableColumn
agentSwitchportGeneralTaggedVlanList = _AgentSwitchportGeneralTaggedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 8),
    _AgentSwitchportGeneralTaggedVlanList_Type()
)
agentSwitchportGeneralTaggedVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchportGeneralTaggedVlanList.setStatus("current")
_AgentSwitchportGeneralForbiddenVlanList_Type = VlanList
_AgentSwitchportGeneralForbiddenVlanList_Object = MibTableColumn
agentSwitchportGeneralForbiddenVlanList = _AgentSwitchportGeneralForbiddenVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 9),
    _AgentSwitchportGeneralForbiddenVlanList_Type()
)
agentSwitchportGeneralForbiddenVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchportGeneralForbiddenVlanList.setStatus("current")
_AgentSwitchportGeneralDynamicallyAddedVlanList_Type = VlanList
_AgentSwitchportGeneralDynamicallyAddedVlanList_Object = MibTableColumn
agentSwitchportGeneralDynamicallyAddedVlanList = _AgentSwitchportGeneralDynamicallyAddedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 8, 37, 1, 10),
    _AgentSwitchportGeneralDynamicallyAddedVlanList_Type()
)
agentSwitchportGeneralDynamicallyAddedVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchportGeneralDynamicallyAddedVlanList.setStatus("current")
_AgentTransferConfigGroup_ObjectIdentity = ObjectIdentity
agentTransferConfigGroup = _AgentTransferConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9)
)
_AgentTransferUploadGroup_ObjectIdentity = ObjectIdentity
agentTransferUploadGroup = _AgentTransferUploadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1)
)


class _AgentTransferUploadMode_Type(Integer32):
    """Custom type agentTransferUploadMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 8),
          ("scp", 6),
          ("sftp", 5),
          ("tftp", 1),
          ("usb", 7),
          ("xmodem", 2),
          ("ymodem", 3),
          ("zmodem", 4))
    )


_AgentTransferUploadMode_Type.__name__ = "Integer32"
_AgentTransferUploadMode_Object = MibScalar
agentTransferUploadMode = _AgentTransferUploadMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 1),
    _AgentTransferUploadMode_Type()
)
agentTransferUploadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadMode.setStatus("current")
_AgentTransferUploadServerIP_Type = IpAddress
_AgentTransferUploadServerIP_Object = MibScalar
agentTransferUploadServerIP = _AgentTransferUploadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 2),
    _AgentTransferUploadServerIP_Type()
)
agentTransferUploadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadServerIP.setStatus("deprecated")


class _AgentTransferUploadPath_Type(DisplayString):
    """Custom type agentTransferUploadPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferUploadPath_Type.__name__ = "DisplayString"
_AgentTransferUploadPath_Object = MibScalar
agentTransferUploadPath = _AgentTransferUploadPath_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 3),
    _AgentTransferUploadPath_Type()
)
agentTransferUploadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadPath.setStatus("current")


class _AgentTransferUploadFilename_Type(DisplayString):
    """Custom type agentTransferUploadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferUploadFilename_Type.__name__ = "DisplayString"
_AgentTransferUploadFilename_Object = MibScalar
agentTransferUploadFilename = _AgentTransferUploadFilename_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 4),
    _AgentTransferUploadFilename_Type()
)
agentTransferUploadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadFilename.setStatus("current")


class _AgentTransferUploadDataType_Type(Integer32):
    """Custom type agentTransferUploadDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("backup-config", 11),
          ("clibanner", 6),
          ("code", 7),
          ("config", 2),
          ("config-script", 13),
          ("cpuPktCapture", 9),
          ("crash-log", 16),
          ("errorlog", 3),
          ("factory-default-config", 12),
          ("lang-pack", 8),
          ("messagelog", 4),
          ("operationallog", 15),
          ("startup-config", 10),
          ("startuplog", 14),
          ("tech-support", 17),
          ("traplog", 5))
    )


_AgentTransferUploadDataType_Type.__name__ = "Integer32"
_AgentTransferUploadDataType_Object = MibScalar
agentTransferUploadDataType = _AgentTransferUploadDataType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 5),
    _AgentTransferUploadDataType_Type()
)
agentTransferUploadDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadDataType.setStatus("current")


class _AgentTransferUploadStart_Type(Integer32):
    """Custom type agentTransferUploadStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentTransferUploadStart_Type.__name__ = "Integer32"
_AgentTransferUploadStart_Object = MibScalar
agentTransferUploadStart = _AgentTransferUploadStart_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 6),
    _AgentTransferUploadStart_Type()
)
agentTransferUploadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadStart.setStatus("current")


class _AgentTransferUploadStatus_Type(Integer32):
    """Custom type agentTransferUploadStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_AgentTransferUploadStatus_Type.__name__ = "Integer32"
_AgentTransferUploadStatus_Object = MibScalar
agentTransferUploadStatus = _AgentTransferUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 7),
    _AgentTransferUploadStatus_Type()
)
agentTransferUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTransferUploadStatus.setStatus("current")
_AgentTransferUploadServerAddressType_Type = InetAddressType
_AgentTransferUploadServerAddressType_Object = MibScalar
agentTransferUploadServerAddressType = _AgentTransferUploadServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 8),
    _AgentTransferUploadServerAddressType_Type()
)
agentTransferUploadServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadServerAddressType.setStatus("current")
_AgentTransferUploadServerAddress_Type = InetAddress
_AgentTransferUploadServerAddress_Object = MibScalar
agentTransferUploadServerAddress = _AgentTransferUploadServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 9),
    _AgentTransferUploadServerAddress_Type()
)
agentTransferUploadServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadServerAddress.setStatus("current")


class _AgentTransferUploadImagename_Type(Integer32):
    """Custom type agentTransferUploadImagename based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3),
          ("unknown", 1))
    )


_AgentTransferUploadImagename_Type.__name__ = "Integer32"
_AgentTransferUploadImagename_Object = MibScalar
agentTransferUploadImagename = _AgentTransferUploadImagename_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 10),
    _AgentTransferUploadImagename_Type()
)
agentTransferUploadImagename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadImagename.setStatus("current")


class _AgentTransferUploadUsername_Type(DisplayString):
    """Custom type agentTransferUploadUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentTransferUploadUsername_Type.__name__ = "DisplayString"
_AgentTransferUploadUsername_Object = MibScalar
agentTransferUploadUsername = _AgentTransferUploadUsername_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 11),
    _AgentTransferUploadUsername_Type()
)
agentTransferUploadUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadUsername.setStatus("current")


class _AgentTransferUploadPassword_Type(DisplayString):
    """Custom type agentTransferUploadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentTransferUploadPassword_Type.__name__ = "DisplayString"
_AgentTransferUploadPassword_Object = MibScalar
agentTransferUploadPassword = _AgentTransferUploadPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 12),
    _AgentTransferUploadPassword_Type()
)
agentTransferUploadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadPassword.setStatus("current")


class _AgentTransferUploadRemoteFilename_Type(DisplayString):
    """Custom type agentTransferUploadRemoteFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferUploadRemoteFilename_Type.__name__ = "DisplayString"
_AgentTransferUploadRemoteFilename_Object = MibScalar
agentTransferUploadRemoteFilename = _AgentTransferUploadRemoteFilename_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 1, 14),
    _AgentTransferUploadRemoteFilename_Type()
)
agentTransferUploadRemoteFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadRemoteFilename.setStatus("current")
_AgentTransferDownloadGroup_ObjectIdentity = ObjectIdentity
agentTransferDownloadGroup = _AgentTransferDownloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2)
)


class _AgentTransferDownloadMode_Type(Integer32):
    """Custom type agentTransferDownloadMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 8),
          ("scp", 6),
          ("sftp", 5),
          ("tftp", 1),
          ("usb", 7),
          ("xmodem", 2),
          ("ymodem", 3),
          ("zmodem", 4))
    )


_AgentTransferDownloadMode_Type.__name__ = "Integer32"
_AgentTransferDownloadMode_Object = MibScalar
agentTransferDownloadMode = _AgentTransferDownloadMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 1),
    _AgentTransferDownloadMode_Type()
)
agentTransferDownloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadMode.setStatus("current")
_AgentTransferDownloadServerIP_Type = IpAddress
_AgentTransferDownloadServerIP_Object = MibScalar
agentTransferDownloadServerIP = _AgentTransferDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 2),
    _AgentTransferDownloadServerIP_Type()
)
agentTransferDownloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadServerIP.setStatus("deprecated")


class _AgentTransferDownloadPath_Type(DisplayString):
    """Custom type agentTransferDownloadPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_AgentTransferDownloadPath_Type.__name__ = "DisplayString"
_AgentTransferDownloadPath_Object = MibScalar
agentTransferDownloadPath = _AgentTransferDownloadPath_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 3),
    _AgentTransferDownloadPath_Type()
)
agentTransferDownloadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadPath.setStatus("current")


class _AgentTransferDownloadFilename_Type(DisplayString):
    """Custom type agentTransferDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferDownloadFilename_Type.__name__ = "DisplayString"
_AgentTransferDownloadFilename_Object = MibScalar
agentTransferDownloadFilename = _AgentTransferDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 4),
    _AgentTransferDownloadFilename_Type()
)
agentTransferDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadFilename.setStatus("current")


class _AgentTransferDownloadDataType_Type(Integer32):
    """Custom type agentTransferDownloadDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("backup-config", 19),
          ("clibanner", 11),
          ("code", 2),
          ("config", 3),
          ("config-script", 21),
          ("factory-default-config", 20),
          ("ias-users", 17),
          ("kernel", 12),
          ("lang-pack", 16),
          ("publickey-image", 22),
          ("publickey-script", 23),
          ("sshkey-dsa", 6),
          ("sshkey-rsa1", 4),
          ("sshkey-rsa2", 5),
          ("sslpem-dhstrong", 10),
          ("sslpem-dhweak", 9),
          ("sslpem-root", 7),
          ("sslpem-server", 8),
          ("startup-config", 18),
          ("tr069-acs-sslpem-root", 13),
          ("tr069-client-ssl-cert", 15),
          ("tr069-client-ssl-private-key", 14))
    )


_AgentTransferDownloadDataType_Type.__name__ = "Integer32"
_AgentTransferDownloadDataType_Object = MibScalar
agentTransferDownloadDataType = _AgentTransferDownloadDataType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 5),
    _AgentTransferDownloadDataType_Type()
)
agentTransferDownloadDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadDataType.setStatus("current")


class _AgentTransferDownloadStart_Type(Integer32):
    """Custom type agentTransferDownloadStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentTransferDownloadStart_Type.__name__ = "Integer32"
_AgentTransferDownloadStart_Object = MibScalar
agentTransferDownloadStart = _AgentTransferDownloadStart_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 6),
    _AgentTransferDownloadStart_Type()
)
agentTransferDownloadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadStart.setStatus("current")


class _AgentTransferDownloadStatus_Type(Integer32):
    """Custom type agentTransferDownloadStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_AgentTransferDownloadStatus_Type.__name__ = "Integer32"
_AgentTransferDownloadStatus_Object = MibScalar
agentTransferDownloadStatus = _AgentTransferDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 7),
    _AgentTransferDownloadStatus_Type()
)
agentTransferDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTransferDownloadStatus.setStatus("current")
_AgentTransferDownloadServerAddressType_Type = InetAddressType
_AgentTransferDownloadServerAddressType_Object = MibScalar
agentTransferDownloadServerAddressType = _AgentTransferDownloadServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 8),
    _AgentTransferDownloadServerAddressType_Type()
)
agentTransferDownloadServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadServerAddressType.setStatus("current")
_AgentTransferDownloadServerAddress_Type = InetAddress
_AgentTransferDownloadServerAddress_Object = MibScalar
agentTransferDownloadServerAddress = _AgentTransferDownloadServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 9),
    _AgentTransferDownloadServerAddress_Type()
)
agentTransferDownloadServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadServerAddress.setStatus("current")


class _AgentTransferDownloadImagename_Type(Integer32):
    """Custom type agentTransferDownloadImagename based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3),
          ("unknown", 1))
    )


_AgentTransferDownloadImagename_Type.__name__ = "Integer32"
_AgentTransferDownloadImagename_Object = MibScalar
agentTransferDownloadImagename = _AgentTransferDownloadImagename_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 10),
    _AgentTransferDownloadImagename_Type()
)
agentTransferDownloadImagename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadImagename.setStatus("current")


class _AgentTransferDownloadUsername_Type(DisplayString):
    """Custom type agentTransferDownloadUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentTransferDownloadUsername_Type.__name__ = "DisplayString"
_AgentTransferDownloadUsername_Object = MibScalar
agentTransferDownloadUsername = _AgentTransferDownloadUsername_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 11),
    _AgentTransferDownloadUsername_Type()
)
agentTransferDownloadUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadUsername.setStatus("current")


class _AgentTransferDownloadPassword_Type(DisplayString):
    """Custom type agentTransferDownloadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentTransferDownloadPassword_Type.__name__ = "DisplayString"
_AgentTransferDownloadPassword_Object = MibScalar
agentTransferDownloadPassword = _AgentTransferDownloadPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 12),
    _AgentTransferDownloadPassword_Type()
)
agentTransferDownloadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadPassword.setStatus("current")


class _AgentTransferDownloadRemoteFilename_Type(DisplayString):
    """Custom type agentTransferDownloadRemoteFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTransferDownloadRemoteFilename_Type.__name__ = "DisplayString"
_AgentTransferDownloadRemoteFilename_Object = MibScalar
agentTransferDownloadRemoteFilename = _AgentTransferDownloadRemoteFilename_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 13),
    _AgentTransferDownloadRemoteFilename_Type()
)
agentTransferDownloadRemoteFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadRemoteFilename.setStatus("current")


class _AgentTransferDownloadDigitalSignatureVerifySelect_Type(Integer32):
    """Custom type agentTransferDownloadDigitalSignatureVerifySelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("noverify", 2),
          ("verify", 1))
    )


_AgentTransferDownloadDigitalSignatureVerifySelect_Type.__name__ = "Integer32"
_AgentTransferDownloadDigitalSignatureVerifySelect_Object = MibScalar
agentTransferDownloadDigitalSignatureVerifySelect = _AgentTransferDownloadDigitalSignatureVerifySelect_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 2, 14),
    _AgentTransferDownloadDigitalSignatureVerifySelect_Type()
)
agentTransferDownloadDigitalSignatureVerifySelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadDigitalSignatureVerifySelect.setStatus("current")
_AgentImageConfigGroup_ObjectIdentity = ObjectIdentity
agentImageConfigGroup = _AgentImageConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 3)
)


class _AgentImage1_Type(DisplayString):
    """Custom type agentImage1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentImage1_Type.__name__ = "DisplayString"
_AgentImage1_Object = MibScalar
agentImage1 = _AgentImage1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 3, 1),
    _AgentImage1_Type()
)
agentImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentImage1.setStatus("current")


class _AgentImage2_Type(DisplayString):
    """Custom type agentImage2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentImage2_Type.__name__ = "DisplayString"
_AgentImage2_Object = MibScalar
agentImage2 = _AgentImage2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 3, 2),
    _AgentImage2_Type()
)
agentImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentImage2.setStatus("current")


class _AgentActiveImage_Type(DisplayString):
    """Custom type agentActiveImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentActiveImage_Type.__name__ = "DisplayString"
_AgentActiveImage_Object = MibScalar
agentActiveImage = _AgentActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 3, 3),
    _AgentActiveImage_Type()
)
agentActiveImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentActiveImage.setStatus("current")


class _AgentNextActiveImage_Type(DisplayString):
    """Custom type agentNextActiveImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentNextActiveImage_Type.__name__ = "DisplayString"
_AgentNextActiveImage_Object = MibScalar
agentNextActiveImage = _AgentNextActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 9, 3, 4),
    _AgentNextActiveImage_Type()
)
agentNextActiveImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNextActiveImage.setStatus("obsolete")
_AgentPortMirroringGroup_ObjectIdentity = ObjectIdentity
agentPortMirroringGroup = _AgentPortMirroringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10)
)


class _AgentMirroredPortIfIndex_Type(Integer32):
    """Custom type agentMirroredPortIfIndex based on Integer32"""
    defaultValue = 0


_AgentMirroredPortIfIndex_Object = MibScalar
agentMirroredPortIfIndex = _AgentMirroredPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 1),
    _AgentMirroredPortIfIndex_Type()
)
agentMirroredPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMirroredPortIfIndex.setStatus("obsolete")


class _AgentProbePortIfIndex_Type(Integer32):
    """Custom type agentProbePortIfIndex based on Integer32"""
    defaultValue = 0


_AgentProbePortIfIndex_Object = MibScalar
agentProbePortIfIndex = _AgentProbePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 2),
    _AgentProbePortIfIndex_Type()
)
agentProbePortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProbePortIfIndex.setStatus("obsolete")


class _AgentPortMirroringMode_Type(Integer32):
    """Custom type agentPortMirroringMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_AgentPortMirroringMode_Type.__name__ = "Integer32"
_AgentPortMirroringMode_Object = MibScalar
agentPortMirroringMode = _AgentPortMirroringMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 3),
    _AgentPortMirroringMode_Type()
)
agentPortMirroringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirroringMode.setStatus("obsolete")
_AgentPortMirrorTable_Object = MibTable
agentPortMirrorTable = _AgentPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    agentPortMirrorTable.setStatus("current")
_AgentPortMirrorEntry_Object = MibTableRow
agentPortMirrorEntry = _AgentPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1)
)
agentPortMirrorEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPortMirrorSessionNum"),
)
if mibBuilder.loadTexts:
    agentPortMirrorEntry.setStatus("current")
_AgentPortMirrorSessionNum_Type = Unsigned32
_AgentPortMirrorSessionNum_Object = MibTableColumn
agentPortMirrorSessionNum = _AgentPortMirrorSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 1),
    _AgentPortMirrorSessionNum_Type()
)
agentPortMirrorSessionNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPortMirrorSessionNum.setStatus("current")
_AgentPortMirrorDestinationPort_Type = Unsigned32
_AgentPortMirrorDestinationPort_Object = MibTableColumn
agentPortMirrorDestinationPort = _AgentPortMirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 2),
    _AgentPortMirrorDestinationPort_Type()
)
agentPortMirrorDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorDestinationPort.setStatus("current")
_AgentPortMirrorSourcePortMask_Type = AgentPortMask
_AgentPortMirrorSourcePortMask_Object = MibTableColumn
agentPortMirrorSourcePortMask = _AgentPortMirrorSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 3),
    _AgentPortMirrorSourcePortMask_Type()
)
agentPortMirrorSourcePortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorSourcePortMask.setStatus("current")


class _AgentPortMirrorAdminMode_Type(Integer32):
    """Custom type agentPortMirrorAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_AgentPortMirrorAdminMode_Type.__name__ = "Integer32"
_AgentPortMirrorAdminMode_Object = MibTableColumn
agentPortMirrorAdminMode = _AgentPortMirrorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 4),
    _AgentPortMirrorAdminMode_Type()
)
agentPortMirrorAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorAdminMode.setStatus("current")


class _AgentPortMirrorSourceVlan_Type(Unsigned32):
    """Custom type agentPortMirrorSourceVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4093),
    )


_AgentPortMirrorSourceVlan_Type.__name__ = "Unsigned32"
_AgentPortMirrorSourceVlan_Object = MibTableColumn
agentPortMirrorSourceVlan = _AgentPortMirrorSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 5),
    _AgentPortMirrorSourceVlan_Type()
)
agentPortMirrorSourceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorSourceVlan.setStatus("current")


class _AgentPortMirrorRemoteSourceVlan_Type(Unsigned32):
    """Custom type agentPortMirrorRemoteSourceVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4093),
    )


_AgentPortMirrorRemoteSourceVlan_Type.__name__ = "Unsigned32"
_AgentPortMirrorRemoteSourceVlan_Object = MibTableColumn
agentPortMirrorRemoteSourceVlan = _AgentPortMirrorRemoteSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 6),
    _AgentPortMirrorRemoteSourceVlan_Type()
)
agentPortMirrorRemoteSourceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorRemoteSourceVlan.setStatus("current")


class _AgentPortMirrorRemoteDestinationVlan_Type(Unsigned32):
    """Custom type agentPortMirrorRemoteDestinationVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4093),
    )


_AgentPortMirrorRemoteDestinationVlan_Type.__name__ = "Unsigned32"
_AgentPortMirrorRemoteDestinationVlan_Object = MibTableColumn
agentPortMirrorRemoteDestinationVlan = _AgentPortMirrorRemoteDestinationVlan_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 7),
    _AgentPortMirrorRemoteDestinationVlan_Type()
)
agentPortMirrorRemoteDestinationVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorRemoteDestinationVlan.setStatus("current")
_AgentPortMirrorReflectorPort_Type = Unsigned32
_AgentPortMirrorReflectorPort_Object = MibTableColumn
agentPortMirrorReflectorPort = _AgentPortMirrorReflectorPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 8),
    _AgentPortMirrorReflectorPort_Type()
)
agentPortMirrorReflectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorReflectorPort.setStatus("current")
_AgentPortMirrorIpAccessListNumber_Type = Unsigned32
_AgentPortMirrorIpAccessListNumber_Object = MibTableColumn
agentPortMirrorIpAccessListNumber = _AgentPortMirrorIpAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 10),
    _AgentPortMirrorIpAccessListNumber_Type()
)
agentPortMirrorIpAccessListNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorIpAccessListNumber.setStatus("current")
_AgentPortMirrorMacAccessListNumber_Type = Unsigned32
_AgentPortMirrorMacAccessListNumber_Object = MibTableColumn
agentPortMirrorMacAccessListNumber = _AgentPortMirrorMacAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 4, 1, 11),
    _AgentPortMirrorMacAccessListNumber_Type()
)
agentPortMirrorMacAccessListNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorMacAccessListNumber.setStatus("current")
_AgentPortMirrorTypeTable_Object = MibTable
agentPortMirrorTypeTable = _AgentPortMirrorTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 5)
)
if mibBuilder.loadTexts:
    agentPortMirrorTypeTable.setStatus("current")
_AgentPortMirrorTypeEntry_Object = MibTableRow
agentPortMirrorTypeEntry = _AgentPortMirrorTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 5, 1)
)
agentPortMirrorTypeEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPortMirrorSessionNum"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPortMirrorTypeSourcePort"),
)
if mibBuilder.loadTexts:
    agentPortMirrorTypeEntry.setStatus("current")
_AgentPortMirrorTypeSourcePort_Type = Unsigned32
_AgentPortMirrorTypeSourcePort_Object = MibTableColumn
agentPortMirrorTypeSourcePort = _AgentPortMirrorTypeSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 5, 1, 1),
    _AgentPortMirrorTypeSourcePort_Type()
)
agentPortMirrorTypeSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPortMirrorTypeSourcePort.setStatus("current")


class _AgentPortMirrorTypeType_Type(Integer32):
    """Custom type agentPortMirrorTypeType based on Integer32"""
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
        *(("rx", 2),
          ("tx", 1),
          ("txrx", 3))
    )


_AgentPortMirrorTypeType_Type.__name__ = "Integer32"
_AgentPortMirrorTypeType_Object = MibTableColumn
agentPortMirrorTypeType = _AgentPortMirrorTypeType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 5, 1, 2),
    _AgentPortMirrorTypeType_Type()
)
agentPortMirrorTypeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorTypeType.setStatus("current")
_AgentPortMirrorRemoteVlan_Type = Unsigned32
_AgentPortMirrorRemoteVlan_Object = MibScalar
agentPortMirrorRemoteVlan = _AgentPortMirrorRemoteVlan_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 6),
    _AgentPortMirrorRemoteVlan_Type()
)
agentPortMirrorRemoteVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorRemoteVlan.setStatus("obsolete")
_AgentPortMirrorRemoteVlanTable_Object = MibTable
agentPortMirrorRemoteVlanTable = _AgentPortMirrorRemoteVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 7)
)
if mibBuilder.loadTexts:
    agentPortMirrorRemoteVlanTable.setStatus("current")
_AgentPortMirrorRemoteVlanEntry_Object = MibTableRow
agentPortMirrorRemoteVlanEntry = _AgentPortMirrorRemoteVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 7, 1)
)
agentPortMirrorRemoteVlanEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPortMirrorRemoteVlanIndex"),
)
if mibBuilder.loadTexts:
    agentPortMirrorRemoteVlanEntry.setStatus("current")
_AgentPortMirrorRemoteVlanIndex_Type = VlanIndex
_AgentPortMirrorRemoteVlanIndex_Object = MibTableColumn
agentPortMirrorRemoteVlanIndex = _AgentPortMirrorRemoteVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 7, 1, 1),
    _AgentPortMirrorRemoteVlanIndex_Type()
)
agentPortMirrorRemoteVlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentPortMirrorRemoteVlanIndex.setStatus("current")
_AgentPortMirrorRemoteVlanRowStatus_Type = RowStatus
_AgentPortMirrorRemoteVlanRowStatus_Object = MibTableColumn
agentPortMirrorRemoteVlanRowStatus = _AgentPortMirrorRemoteVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 10, 7, 1, 2),
    _AgentPortMirrorRemoteVlanRowStatus_Type()
)
agentPortMirrorRemoteVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentPortMirrorRemoteVlanRowStatus.setStatus("current")
_AgentDot3adAggPortTable_Object = MibTable
agentDot3adAggPortTable = _AgentDot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    agentDot3adAggPortTable.setStatus("current")
_AgentDot3adAggPortEntry_Object = MibTableRow
agentDot3adAggPortEntry = _AgentDot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 12, 1)
)
agentDot3adAggPortEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentDot3adAggPort"),
)
if mibBuilder.loadTexts:
    agentDot3adAggPortEntry.setStatus("current")


class _AgentDot3adAggPort_Type(Integer32):
    """Custom type agentDot3adAggPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentDot3adAggPort_Type.__name__ = "Integer32"
_AgentDot3adAggPort_Object = MibTableColumn
agentDot3adAggPort = _AgentDot3adAggPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 12, 1, 1),
    _AgentDot3adAggPort_Type()
)
agentDot3adAggPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot3adAggPort.setStatus("current")


class _AgentDot3adAggPortLACPMode_Type(Integer32):
    """Custom type agentDot3adAggPortLACPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentDot3adAggPortLACPMode_Type.__name__ = "Integer32"
_AgentDot3adAggPortLACPMode_Object = MibTableColumn
agentDot3adAggPortLACPMode = _AgentDot3adAggPortLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 12, 1, 2),
    _AgentDot3adAggPortLACPMode_Type()
)
agentDot3adAggPortLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot3adAggPortLACPMode.setStatus("current")
_AgentPortConfigTable_Object = MibTable
agentPortConfigTable = _AgentPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    agentPortConfigTable.setStatus("current")
_AgentPortConfigEntry_Object = MibTableRow
agentPortConfigEntry = _AgentPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1)
)
agentPortConfigEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPortDot1dBasePort"),
)
if mibBuilder.loadTexts:
    agentPortConfigEntry.setStatus("current")


class _AgentPortDot1dBasePort_Type(Integer32):
    """Custom type agentPortDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentPortDot1dBasePort_Type.__name__ = "Integer32"
_AgentPortDot1dBasePort_Object = MibTableColumn
agentPortDot1dBasePort = _AgentPortDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 1),
    _AgentPortDot1dBasePort_Type()
)
agentPortDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortDot1dBasePort.setStatus("current")
_AgentPortIfIndex_Type = Integer32
_AgentPortIfIndex_Object = MibTableColumn
agentPortIfIndex = _AgentPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 2),
    _AgentPortIfIndex_Type()
)
agentPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortIfIndex.setStatus("current")
_AgentPortIanaType_Type = IANAifType
_AgentPortIanaType_Object = MibTableColumn
agentPortIanaType = _AgentPortIanaType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 3),
    _AgentPortIanaType_Type()
)
agentPortIanaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortIanaType.setStatus("current")


class _AgentPortSTPMode_Type(Integer32):
    """Custom type agentPortSTPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("fast", 2),
          ("off", 3))
    )


_AgentPortSTPMode_Type.__name__ = "Integer32"
_AgentPortSTPMode_Object = MibTableColumn
agentPortSTPMode = _AgentPortSTPMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 4),
    _AgentPortSTPMode_Type()
)
agentPortSTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSTPMode.setStatus("obsolete")


class _AgentPortSTPState_Type(Integer32):
    """Custom type agentPortSTPState based on Integer32"""
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
        *(("blocking", 1),
          ("disabled", 5),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2))
    )


_AgentPortSTPState_Type.__name__ = "Integer32"
_AgentPortSTPState_Object = MibTableColumn
agentPortSTPState = _AgentPortSTPState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 5),
    _AgentPortSTPState_Type()
)
agentPortSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortSTPState.setStatus("obsolete")


class _AgentPortAdminMode_Type(Integer32):
    """Custom type agentPortAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortAdminMode_Type.__name__ = "Integer32"
_AgentPortAdminMode_Object = MibTableColumn
agentPortAdminMode = _AgentPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 6),
    _AgentPortAdminMode_Type()
)
agentPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortAdminMode.setStatus("current")


class _AgentPortPhysicalMode_Type(Integer32):
    """Custom type agentPortPhysicalMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("full-10", 3),
          ("full-100", 5),
          ("full-1000sx", 8),
          ("full-100fx", 7),
          ("full-10gsx", 9),
          ("half-10", 2),
          ("half-100", 4),
          ("half-100fx", 6))
    )


_AgentPortPhysicalMode_Type.__name__ = "Integer32"
_AgentPortPhysicalMode_Object = MibTableColumn
agentPortPhysicalMode = _AgentPortPhysicalMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 7),
    _AgentPortPhysicalMode_Type()
)
agentPortPhysicalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortPhysicalMode.setStatus("obsolete")


class _AgentPortPhysicalStatus_Type(Integer32):
    """Custom type agentPortPhysicalStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("full-10", 3),
          ("full-100", 5),
          ("full-1000sx", 8),
          ("full-100fx", 7),
          ("full-10gsx", 9),
          ("half-10", 2),
          ("half-100", 4),
          ("half-100fx", 6))
    )


_AgentPortPhysicalStatus_Type.__name__ = "Integer32"
_AgentPortPhysicalStatus_Object = MibTableColumn
agentPortPhysicalStatus = _AgentPortPhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 8),
    _AgentPortPhysicalStatus_Type()
)
agentPortPhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortPhysicalStatus.setStatus("obsolete")


class _AgentPortLinkTrapMode_Type(Integer32):
    """Custom type agentPortLinkTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortLinkTrapMode_Type.__name__ = "Integer32"
_AgentPortLinkTrapMode_Object = MibTableColumn
agentPortLinkTrapMode = _AgentPortLinkTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 9),
    _AgentPortLinkTrapMode_Type()
)
agentPortLinkTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortLinkTrapMode.setStatus("current")


class _AgentPortClearStats_Type(Integer32):
    """Custom type agentPortClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortClearStats_Type.__name__ = "Integer32"
_AgentPortClearStats_Object = MibTableColumn
agentPortClearStats = _AgentPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 10),
    _AgentPortClearStats_Type()
)
agentPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortClearStats.setStatus("current")
_AgentPortDefaultType_Type = ObjectIdentifier
_AgentPortDefaultType_Object = MibTableColumn
agentPortDefaultType = _AgentPortDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 11),
    _AgentPortDefaultType_Type()
)
agentPortDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDefaultType.setStatus("current")
_AgentPortType_Type = ObjectIdentifier
_AgentPortType_Object = MibTableColumn
agentPortType = _AgentPortType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 12),
    _AgentPortType_Type()
)
agentPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortType.setStatus("current")


class _AgentPortAutoNegAdminStatus_Type(Integer32):
    """Custom type agentPortAutoNegAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortAutoNegAdminStatus_Type.__name__ = "Integer32"
_AgentPortAutoNegAdminStatus_Object = MibTableColumn
agentPortAutoNegAdminStatus = _AgentPortAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 13),
    _AgentPortAutoNegAdminStatus_Type()
)
agentPortAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortAutoNegAdminStatus.setStatus("current")


class _AgentPortDot3FlowControlMode_Type(Integer32):
    """Custom type agentPortDot3FlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 2),
          ("disable", 3),
          ("symmetric", 1))
    )


_AgentPortDot3FlowControlMode_Type.__name__ = "Integer32"
_AgentPortDot3FlowControlMode_Object = MibTableColumn
agentPortDot3FlowControlMode = _AgentPortDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 14),
    _AgentPortDot3FlowControlMode_Type()
)
agentPortDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDot3FlowControlMode.setStatus("current")


class _AgentPortDVlanTagMode_Type(Integer32):
    """Custom type agentPortDVlanTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortDVlanTagMode_Type.__name__ = "Integer32"
_AgentPortDVlanTagMode_Object = MibTableColumn
agentPortDVlanTagMode = _AgentPortDVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 15),
    _AgentPortDVlanTagMode_Type()
)
agentPortDVlanTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDVlanTagMode.setStatus("current")


class _AgentPortDVlanTagEthertype_Type(Integer32):
    """Custom type agentPortDVlanTagEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentPortDVlanTagEthertype_Type.__name__ = "Integer32"
_AgentPortDVlanTagEthertype_Object = MibTableColumn
agentPortDVlanTagEthertype = _AgentPortDVlanTagEthertype_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 16),
    _AgentPortDVlanTagEthertype_Type()
)
agentPortDVlanTagEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDVlanTagEthertype.setStatus("current")
_AgentPortDVlanTagCustomerId_Type = Integer32
_AgentPortDVlanTagCustomerId_Object = MibTableColumn
agentPortDVlanTagCustomerId = _AgentPortDVlanTagCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 17),
    _AgentPortDVlanTagCustomerId_Type()
)
agentPortDVlanTagCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDVlanTagCustomerId.setStatus("current")
_AgentPortMaxFrameSizeLimit_Type = Integer32
_AgentPortMaxFrameSizeLimit_Object = MibTableColumn
agentPortMaxFrameSizeLimit = _AgentPortMaxFrameSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 18),
    _AgentPortMaxFrameSizeLimit_Type()
)
agentPortMaxFrameSizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortMaxFrameSizeLimit.setStatus("current")
_AgentPortMaxFrameSize_Type = Integer32
_AgentPortMaxFrameSize_Object = MibTableColumn
agentPortMaxFrameSize = _AgentPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 19),
    _AgentPortMaxFrameSize_Type()
)
agentPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMaxFrameSize.setStatus("current")


class _AgentPortBroadcastControlMode_Type(Integer32):
    """Custom type agentPortBroadcastControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortBroadcastControlMode_Type.__name__ = "Integer32"
_AgentPortBroadcastControlMode_Object = MibTableColumn
agentPortBroadcastControlMode = _AgentPortBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 20),
    _AgentPortBroadcastControlMode_Type()
)
agentPortBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortBroadcastControlMode.setStatus("current")


class _AgentPortBroadcastControlThreshold_Type(Integer32):
    """Custom type agentPortBroadcastControlThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_AgentPortBroadcastControlThreshold_Type.__name__ = "Integer32"
_AgentPortBroadcastControlThreshold_Object = MibTableColumn
agentPortBroadcastControlThreshold = _AgentPortBroadcastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 21),
    _AgentPortBroadcastControlThreshold_Type()
)
agentPortBroadcastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortBroadcastControlThreshold.setStatus("current")


class _AgentPortMulticastControlMode_Type(Integer32):
    """Custom type agentPortMulticastControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortMulticastControlMode_Type.__name__ = "Integer32"
_AgentPortMulticastControlMode_Object = MibTableColumn
agentPortMulticastControlMode = _AgentPortMulticastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 22),
    _AgentPortMulticastControlMode_Type()
)
agentPortMulticastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMulticastControlMode.setStatus("current")


class _AgentPortMulticastControlThreshold_Type(Integer32):
    """Custom type agentPortMulticastControlThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_AgentPortMulticastControlThreshold_Type.__name__ = "Integer32"
_AgentPortMulticastControlThreshold_Object = MibTableColumn
agentPortMulticastControlThreshold = _AgentPortMulticastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 23),
    _AgentPortMulticastControlThreshold_Type()
)
agentPortMulticastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMulticastControlThreshold.setStatus("current")


class _AgentPortUnicastControlMode_Type(Integer32):
    """Custom type agentPortUnicastControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortUnicastControlMode_Type.__name__ = "Integer32"
_AgentPortUnicastControlMode_Object = MibTableColumn
agentPortUnicastControlMode = _AgentPortUnicastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 24),
    _AgentPortUnicastControlMode_Type()
)
agentPortUnicastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortUnicastControlMode.setStatus("current")


class _AgentPortUnicastControlThreshold_Type(Integer32):
    """Custom type agentPortUnicastControlThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_AgentPortUnicastControlThreshold_Type.__name__ = "Integer32"
_AgentPortUnicastControlThreshold_Object = MibTableColumn
agentPortUnicastControlThreshold = _AgentPortUnicastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 25),
    _AgentPortUnicastControlThreshold_Type()
)
agentPortUnicastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortUnicastControlThreshold.setStatus("current")


class _AgentPortBroadcastControlThresholdUnit_Type(Integer32):
    """Custom type agentPortBroadcastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_AgentPortBroadcastControlThresholdUnit_Type.__name__ = "Integer32"
_AgentPortBroadcastControlThresholdUnit_Object = MibTableColumn
agentPortBroadcastControlThresholdUnit = _AgentPortBroadcastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 26),
    _AgentPortBroadcastControlThresholdUnit_Type()
)
agentPortBroadcastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortBroadcastControlThresholdUnit.setStatus("current")


class _AgentPortMulticastControlThresholdUnit_Type(Integer32):
    """Custom type agentPortMulticastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_AgentPortMulticastControlThresholdUnit_Type.__name__ = "Integer32"
_AgentPortMulticastControlThresholdUnit_Object = MibTableColumn
agentPortMulticastControlThresholdUnit = _AgentPortMulticastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 27),
    _AgentPortMulticastControlThresholdUnit_Type()
)
agentPortMulticastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMulticastControlThresholdUnit.setStatus("current")


class _AgentPortUnicastControlThresholdUnit_Type(Integer32):
    """Custom type agentPortUnicastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_AgentPortUnicastControlThresholdUnit_Type.__name__ = "Integer32"
_AgentPortUnicastControlThresholdUnit_Object = MibTableColumn
agentPortUnicastControlThresholdUnit = _AgentPortUnicastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 28),
    _AgentPortUnicastControlThresholdUnit_Type()
)
agentPortUnicastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortUnicastControlThresholdUnit.setStatus("current")


class _AgentPortVoiceVlanMode_Type(Integer32):
    """Custom type agentPortVoiceVlanMode based on Integer32"""
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
        *(("disable", 5),
          ("dot1p", 3),
          ("none", 1),
          ("untagged", 4),
          ("vlanid", 2))
    )


_AgentPortVoiceVlanMode_Type.__name__ = "Integer32"
_AgentPortVoiceVlanMode_Object = MibTableColumn
agentPortVoiceVlanMode = _AgentPortVoiceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 29),
    _AgentPortVoiceVlanMode_Type()
)
agentPortVoiceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortVoiceVlanMode.setStatus("current")


class _AgentPortVoiceVlanID_Type(Integer32):
    """Custom type agentPortVoiceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AgentPortVoiceVlanID_Type.__name__ = "Integer32"
_AgentPortVoiceVlanID_Object = MibTableColumn
agentPortVoiceVlanID = _AgentPortVoiceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 30),
    _AgentPortVoiceVlanID_Type()
)
agentPortVoiceVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortVoiceVlanID.setStatus("current")


class _AgentPortVoiceVlanPriority_Type(Integer32):
    """Custom type agentPortVoiceVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_AgentPortVoiceVlanPriority_Type.__name__ = "Integer32"
_AgentPortVoiceVlanPriority_Object = MibTableColumn
agentPortVoiceVlanPriority = _AgentPortVoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 31),
    _AgentPortVoiceVlanPriority_Type()
)
agentPortVoiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortVoiceVlanPriority.setStatus("current")


class _AgentPortVoiceVlanDataPriorityMode_Type(Integer32):
    """Custom type agentPortVoiceVlanDataPriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_AgentPortVoiceVlanDataPriorityMode_Type.__name__ = "Integer32"
_AgentPortVoiceVlanDataPriorityMode_Object = MibTableColumn
agentPortVoiceVlanDataPriorityMode = _AgentPortVoiceVlanDataPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 32),
    _AgentPortVoiceVlanDataPriorityMode_Type()
)
agentPortVoiceVlanDataPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortVoiceVlanDataPriorityMode.setStatus("current")


class _AgentPortVoiceVlanOperationalStatus_Type(Integer32):
    """Custom type agentPortVoiceVlanOperationalStatus based on Integer32"""
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


_AgentPortVoiceVlanOperationalStatus_Type.__name__ = "Integer32"
_AgentPortVoiceVlanOperationalStatus_Object = MibTableColumn
agentPortVoiceVlanOperationalStatus = _AgentPortVoiceVlanOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 33),
    _AgentPortVoiceVlanOperationalStatus_Type()
)
agentPortVoiceVlanOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortVoiceVlanOperationalStatus.setStatus("current")


class _AgentPortVoiceVlanUntagged_Type(Integer32):
    """Custom type agentPortVoiceVlanUntagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentPortVoiceVlanUntagged_Type.__name__ = "Integer32"
_AgentPortVoiceVlanUntagged_Object = MibTableColumn
agentPortVoiceVlanUntagged = _AgentPortVoiceVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 34),
    _AgentPortVoiceVlanUntagged_Type()
)
agentPortVoiceVlanUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortVoiceVlanUntagged.setStatus("current")


class _AgentPortVoiceVlanNoneMode_Type(Integer32):
    """Custom type agentPortVoiceVlanNoneMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentPortVoiceVlanNoneMode_Type.__name__ = "Integer32"
_AgentPortVoiceVlanNoneMode_Object = MibTableColumn
agentPortVoiceVlanNoneMode = _AgentPortVoiceVlanNoneMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 35),
    _AgentPortVoiceVlanNoneMode_Type()
)
agentPortVoiceVlanNoneMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortVoiceVlanNoneMode.setStatus("current")
_AgentPortVoiceVlanDSCP_Type = Integer32
_AgentPortVoiceVlanDSCP_Object = MibTableColumn
agentPortVoiceVlanDSCP = _AgentPortVoiceVlanDSCP_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 36),
    _AgentPortVoiceVlanDSCP_Type()
)
agentPortVoiceVlanDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortVoiceVlanDSCP.setStatus("current")


class _AgentPortVoiceVlanAuthMode_Type(Integer32):
    """Custom type agentPortVoiceVlanAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortVoiceVlanAuthMode_Type.__name__ = "Integer32"
_AgentPortVoiceVlanAuthMode_Object = MibTableColumn
agentPortVoiceVlanAuthMode = _AgentPortVoiceVlanAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 37),
    _AgentPortVoiceVlanAuthMode_Type()
)
agentPortVoiceVlanAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortVoiceVlanAuthMode.setStatus("current")


class _AgentPortDot3FlowControlOperStatus_Type(Integer32):
    """Custom type agentPortDot3FlowControlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AgentPortDot3FlowControlOperStatus_Type.__name__ = "Integer32"
_AgentPortDot3FlowControlOperStatus_Object = MibTableColumn
agentPortDot3FlowControlOperStatus = _AgentPortDot3FlowControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 38),
    _AgentPortDot3FlowControlOperStatus_Type()
)
agentPortDot3FlowControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortDot3FlowControlOperStatus.setStatus("current")


class _AgentPortSwitchportMode_Type(Integer32):
    """Custom type agentPortSwitchportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("general", 3),
          ("host", 4),
          ("promiscuous", 5))
    )


_AgentPortSwitchportMode_Type.__name__ = "Integer32"
_AgentPortSwitchportMode_Object = MibTableColumn
agentPortSwitchportMode = _AgentPortSwitchportMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 13, 1, 45),
    _AgentPortSwitchportMode_Type()
)
agentPortSwitchportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSwitchportMode.setStatus("current")
_AgentProtocolConfigGroup_ObjectIdentity = ObjectIdentity
agentProtocolConfigGroup = _AgentProtocolConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14)
)


class _AgentProtocolGroupCreate_Type(DisplayString):
    """Custom type agentProtocolGroupCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 16),
    )


_AgentProtocolGroupCreate_Type.__name__ = "DisplayString"
_AgentProtocolGroupCreate_Object = MibScalar
agentProtocolGroupCreate = _AgentProtocolGroupCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 1),
    _AgentProtocolGroupCreate_Type()
)
agentProtocolGroupCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupCreate.setStatus("obsolete")
_AgentProtocolGroupTable_Object = MibTable
agentProtocolGroupTable = _AgentProtocolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    agentProtocolGroupTable.setStatus("current")
_AgentProtocolGroupEntry_Object = MibTableRow
agentProtocolGroupEntry = _AgentProtocolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2, 1)
)
agentProtocolGroupEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentProtocolGroupId"),
)
if mibBuilder.loadTexts:
    agentProtocolGroupEntry.setStatus("current")


class _AgentProtocolGroupId_Type(Integer32):
    """Custom type agentProtocolGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentProtocolGroupId_Type.__name__ = "Integer32"
_AgentProtocolGroupId_Object = MibTableColumn
agentProtocolGroupId = _AgentProtocolGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2, 1, 1),
    _AgentProtocolGroupId_Type()
)
agentProtocolGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentProtocolGroupId.setStatus("current")


class _AgentProtocolGroupName_Type(DisplayString):
    """Custom type agentProtocolGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 16),
    )


_AgentProtocolGroupName_Type.__name__ = "DisplayString"
_AgentProtocolGroupName_Object = MibTableColumn
agentProtocolGroupName = _AgentProtocolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2, 1, 2),
    _AgentProtocolGroupName_Type()
)
agentProtocolGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupName.setStatus("current")


class _AgentProtocolGroupVlanId_Type(Integer32):
    """Custom type agentProtocolGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_AgentProtocolGroupVlanId_Type.__name__ = "Integer32"
_AgentProtocolGroupVlanId_Object = MibTableColumn
agentProtocolGroupVlanId = _AgentProtocolGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2, 1, 3),
    _AgentProtocolGroupVlanId_Type()
)
agentProtocolGroupVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupVlanId.setStatus("current")


class _AgentProtocolGroupProtocolIP_Type(Integer32):
    """Custom type agentProtocolGroupProtocolIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentProtocolGroupProtocolIP_Type.__name__ = "Integer32"
_AgentProtocolGroupProtocolIP_Object = MibTableColumn
agentProtocolGroupProtocolIP = _AgentProtocolGroupProtocolIP_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2, 1, 4),
    _AgentProtocolGroupProtocolIP_Type()
)
agentProtocolGroupProtocolIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolIP.setStatus("obsolete")


class _AgentProtocolGroupProtocolARP_Type(Integer32):
    """Custom type agentProtocolGroupProtocolARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentProtocolGroupProtocolARP_Type.__name__ = "Integer32"
_AgentProtocolGroupProtocolARP_Object = MibTableColumn
agentProtocolGroupProtocolARP = _AgentProtocolGroupProtocolARP_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2, 1, 5),
    _AgentProtocolGroupProtocolARP_Type()
)
agentProtocolGroupProtocolARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolARP.setStatus("obsolete")


class _AgentProtocolGroupProtocolIPX_Type(Integer32):
    """Custom type agentProtocolGroupProtocolIPX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentProtocolGroupProtocolIPX_Type.__name__ = "Integer32"
_AgentProtocolGroupProtocolIPX_Object = MibTableColumn
agentProtocolGroupProtocolIPX = _AgentProtocolGroupProtocolIPX_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2, 1, 6),
    _AgentProtocolGroupProtocolIPX_Type()
)
agentProtocolGroupProtocolIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolIPX.setStatus("obsolete")
_AgentProtocolGroupStatus_Type = RowStatus
_AgentProtocolGroupStatus_Object = MibTableColumn
agentProtocolGroupStatus = _AgentProtocolGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 2, 1, 7),
    _AgentProtocolGroupStatus_Type()
)
agentProtocolGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentProtocolGroupStatus.setStatus("current")
_AgentProtocolGroupPortTable_Object = MibTable
agentProtocolGroupPortTable = _AgentProtocolGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 3)
)
if mibBuilder.loadTexts:
    agentProtocolGroupPortTable.setStatus("current")
_AgentProtocolGroupPortEntry_Object = MibTableRow
agentProtocolGroupPortEntry = _AgentProtocolGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 3, 1)
)
agentProtocolGroupPortEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentProtocolGroupId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentProtocolGroupPortIfIndex"),
)
if mibBuilder.loadTexts:
    agentProtocolGroupPortEntry.setStatus("current")


class _AgentProtocolGroupPortIfIndex_Type(Integer32):
    """Custom type agentProtocolGroupPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentProtocolGroupPortIfIndex_Type.__name__ = "Integer32"
_AgentProtocolGroupPortIfIndex_Object = MibTableColumn
agentProtocolGroupPortIfIndex = _AgentProtocolGroupPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 3, 1, 1),
    _AgentProtocolGroupPortIfIndex_Type()
)
agentProtocolGroupPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentProtocolGroupPortIfIndex.setStatus("current")
_AgentProtocolGroupPortStatus_Type = RowStatus
_AgentProtocolGroupPortStatus_Object = MibTableColumn
agentProtocolGroupPortStatus = _AgentProtocolGroupPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 3, 1, 2),
    _AgentProtocolGroupPortStatus_Type()
)
agentProtocolGroupPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentProtocolGroupPortStatus.setStatus("current")
_AgentProtocolGroupProtocolTable_Object = MibTable
agentProtocolGroupProtocolTable = _AgentProtocolGroupProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 4)
)
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolTable.setStatus("current")
_AgentProtocolGroupProtocolEntry_Object = MibTableRow
agentProtocolGroupProtocolEntry = _AgentProtocolGroupProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 4, 1)
)
agentProtocolGroupProtocolEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentProtocolGroupId"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentProtocolGroupProtocolID"),
)
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolEntry.setStatus("current")


class _AgentProtocolGroupProtocolID_Type(Integer32):
    """Custom type agentProtocolGroupProtocolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_AgentProtocolGroupProtocolID_Type.__name__ = "Integer32"
_AgentProtocolGroupProtocolID_Object = MibTableColumn
agentProtocolGroupProtocolID = _AgentProtocolGroupProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 4, 1, 1),
    _AgentProtocolGroupProtocolID_Type()
)
agentProtocolGroupProtocolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolID.setStatus("current")
_AgentProtocolGroupProtocolStatus_Type = RowStatus
_AgentProtocolGroupProtocolStatus_Object = MibTableColumn
agentProtocolGroupProtocolStatus = _AgentProtocolGroupProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 14, 4, 1, 2),
    _AgentProtocolGroupProtocolStatus_Type()
)
agentProtocolGroupProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentProtocolGroupProtocolStatus.setStatus("current")
_AgentStpSwitchConfigGroup_ObjectIdentity = ObjectIdentity
agentStpSwitchConfigGroup = _AgentStpSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15)
)


class _AgentStpConfigDigestKey_Type(OctetString):
    """Custom type agentStpConfigDigestKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AgentStpConfigDigestKey_Type.__name__ = "OctetString"
_AgentStpConfigDigestKey_Object = MibScalar
agentStpConfigDigestKey = _AgentStpConfigDigestKey_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 1),
    _AgentStpConfigDigestKey_Type()
)
agentStpConfigDigestKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpConfigDigestKey.setStatus("current")


class _AgentStpConfigFormatSelector_Type(Unsigned32):
    """Custom type agentStpConfigFormatSelector based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentStpConfigFormatSelector_Type.__name__ = "Unsigned32"
_AgentStpConfigFormatSelector_Object = MibScalar
agentStpConfigFormatSelector = _AgentStpConfigFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 2),
    _AgentStpConfigFormatSelector_Type()
)
agentStpConfigFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpConfigFormatSelector.setStatus("current")


class _AgentStpConfigName_Type(DisplayString):
    """Custom type agentStpConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentStpConfigName_Type.__name__ = "DisplayString"
_AgentStpConfigName_Object = MibScalar
agentStpConfigName = _AgentStpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 3),
    _AgentStpConfigName_Type()
)
agentStpConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpConfigName.setStatus("current")


class _AgentStpConfigRevision_Type(Unsigned32):
    """Custom type agentStpConfigRevision based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentStpConfigRevision_Type.__name__ = "Unsigned32"
_AgentStpConfigRevision_Object = MibScalar
agentStpConfigRevision = _AgentStpConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 4),
    _AgentStpConfigRevision_Type()
)
agentStpConfigRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpConfigRevision.setStatus("current")


class _AgentStpForceVersion_Type(Integer32):
    """Custom type agentStpForceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("dot1s", 3),
          ("dot1w", 2))
    )


_AgentStpForceVersion_Type.__name__ = "Integer32"
_AgentStpForceVersion_Object = MibScalar
agentStpForceVersion = _AgentStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 5),
    _AgentStpForceVersion_Type()
)
agentStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpForceVersion.setStatus("current")


class _AgentStpAdminMode_Type(Integer32):
    """Custom type agentStpAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpAdminMode_Type.__name__ = "Integer32"
_AgentStpAdminMode_Object = MibScalar
agentStpAdminMode = _AgentStpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 6),
    _AgentStpAdminMode_Type()
)
agentStpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpAdminMode.setStatus("current")
_AgentStpPortTable_Object = MibTable
agentStpPortTable = _AgentStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7)
)
if mibBuilder.loadTexts:
    agentStpPortTable.setStatus("current")
_AgentStpPortEntry_Object = MibTableRow
agentStpPortEntry = _AgentStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1)
)
agentStpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentStpPortEntry.setStatus("current")


class _AgentStpPortState_Type(Integer32):
    """Custom type agentStpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpPortState_Type.__name__ = "Integer32"
_AgentStpPortState_Object = MibTableColumn
agentStpPortState = _AgentStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 1),
    _AgentStpPortState_Type()
)
agentStpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpPortState.setStatus("current")
_AgentStpPortStatsMstpBpduRx_Type = Counter32
_AgentStpPortStatsMstpBpduRx_Object = MibTableColumn
agentStpPortStatsMstpBpduRx = _AgentStpPortStatsMstpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 2),
    _AgentStpPortStatsMstpBpduRx_Type()
)
agentStpPortStatsMstpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsMstpBpduRx.setStatus("current")
_AgentStpPortStatsMstpBpduTx_Type = Counter32
_AgentStpPortStatsMstpBpduTx_Object = MibTableColumn
agentStpPortStatsMstpBpduTx = _AgentStpPortStatsMstpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 3),
    _AgentStpPortStatsMstpBpduTx_Type()
)
agentStpPortStatsMstpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsMstpBpduTx.setStatus("current")
_AgentStpPortStatsRstpBpduRx_Type = Counter32
_AgentStpPortStatsRstpBpduRx_Object = MibTableColumn
agentStpPortStatsRstpBpduRx = _AgentStpPortStatsRstpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 4),
    _AgentStpPortStatsRstpBpduRx_Type()
)
agentStpPortStatsRstpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsRstpBpduRx.setStatus("current")
_AgentStpPortStatsRstpBpduTx_Type = Counter32
_AgentStpPortStatsRstpBpduTx_Object = MibTableColumn
agentStpPortStatsRstpBpduTx = _AgentStpPortStatsRstpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 5),
    _AgentStpPortStatsRstpBpduTx_Type()
)
agentStpPortStatsRstpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsRstpBpduTx.setStatus("current")
_AgentStpPortStatsStpBpduRx_Type = Counter32
_AgentStpPortStatsStpBpduRx_Object = MibTableColumn
agentStpPortStatsStpBpduRx = _AgentStpPortStatsStpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 6),
    _AgentStpPortStatsStpBpduRx_Type()
)
agentStpPortStatsStpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsStpBpduRx.setStatus("current")
_AgentStpPortStatsStpBpduTx_Type = Counter32
_AgentStpPortStatsStpBpduTx_Object = MibTableColumn
agentStpPortStatsStpBpduTx = _AgentStpPortStatsStpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 7),
    _AgentStpPortStatsStpBpduTx_Type()
)
agentStpPortStatsStpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortStatsStpBpduTx.setStatus("current")
_AgentStpPortUpTime_Type = TimeTicks
_AgentStpPortUpTime_Object = MibTableColumn
agentStpPortUpTime = _AgentStpPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 8),
    _AgentStpPortUpTime_Type()
)
agentStpPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpPortUpTime.setStatus("current")


class _AgentStpPortMigrationCheck_Type(Integer32):
    """Custom type agentStpPortMigrationCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentStpPortMigrationCheck_Type.__name__ = "Integer32"
_AgentStpPortMigrationCheck_Object = MibTableColumn
agentStpPortMigrationCheck = _AgentStpPortMigrationCheck_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 7, 1, 9),
    _AgentStpPortMigrationCheck_Type()
)
agentStpPortMigrationCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpPortMigrationCheck.setStatus("current")
_AgentStpCstConfigGroup_ObjectIdentity = ObjectIdentity
agentStpCstConfigGroup = _AgentStpCstConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8)
)
_AgentStpCstHelloTime_Type = Unsigned32
_AgentStpCstHelloTime_Object = MibScalar
agentStpCstHelloTime = _AgentStpCstHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 1),
    _AgentStpCstHelloTime_Type()
)
agentStpCstHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstHelloTime.setStatus("current")
_AgentStpCstMaxAge_Type = Unsigned32
_AgentStpCstMaxAge_Object = MibScalar
agentStpCstMaxAge = _AgentStpCstMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 2),
    _AgentStpCstMaxAge_Type()
)
agentStpCstMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstMaxAge.setStatus("current")


class _AgentStpCstRegionalRootId_Type(OctetString):
    """Custom type agentStpCstRegionalRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpCstRegionalRootId_Type.__name__ = "OctetString"
_AgentStpCstRegionalRootId_Object = MibScalar
agentStpCstRegionalRootId = _AgentStpCstRegionalRootId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 3),
    _AgentStpCstRegionalRootId_Type()
)
agentStpCstRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstRegionalRootId.setStatus("current")
_AgentStpCstRegionalRootPathCost_Type = Unsigned32
_AgentStpCstRegionalRootPathCost_Object = MibScalar
agentStpCstRegionalRootPathCost = _AgentStpCstRegionalRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 4),
    _AgentStpCstRegionalRootPathCost_Type()
)
agentStpCstRegionalRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstRegionalRootPathCost.setStatus("current")
_AgentStpCstRootFwdDelay_Type = Unsigned32
_AgentStpCstRootFwdDelay_Object = MibScalar
agentStpCstRootFwdDelay = _AgentStpCstRootFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 5),
    _AgentStpCstRootFwdDelay_Type()
)
agentStpCstRootFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstRootFwdDelay.setStatus("current")


class _AgentStpCstBridgeFwdDelay_Type(Unsigned32):
    """Custom type agentStpCstBridgeFwdDelay based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_AgentStpCstBridgeFwdDelay_Type.__name__ = "Unsigned32"
_AgentStpCstBridgeFwdDelay_Object = MibScalar
agentStpCstBridgeFwdDelay = _AgentStpCstBridgeFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 6),
    _AgentStpCstBridgeFwdDelay_Type()
)
agentStpCstBridgeFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstBridgeFwdDelay.setStatus("current")


class _AgentStpCstBridgeHelloTime_Type(Unsigned32):
    """Custom type agentStpCstBridgeHelloTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentStpCstBridgeHelloTime_Type.__name__ = "Unsigned32"
_AgentStpCstBridgeHelloTime_Object = MibScalar
agentStpCstBridgeHelloTime = _AgentStpCstBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 7),
    _AgentStpCstBridgeHelloTime_Type()
)
agentStpCstBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstBridgeHelloTime.setStatus("current")
_AgentStpCstBridgeHoldTime_Type = Unsigned32
_AgentStpCstBridgeHoldTime_Object = MibScalar
agentStpCstBridgeHoldTime = _AgentStpCstBridgeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 8),
    _AgentStpCstBridgeHoldTime_Type()
)
agentStpCstBridgeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstBridgeHoldTime.setStatus("current")


class _AgentStpCstBridgeMaxAge_Type(Unsigned32):
    """Custom type agentStpCstBridgeMaxAge based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_AgentStpCstBridgeMaxAge_Type.__name__ = "Unsigned32"
_AgentStpCstBridgeMaxAge_Object = MibScalar
agentStpCstBridgeMaxAge = _AgentStpCstBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 9),
    _AgentStpCstBridgeMaxAge_Type()
)
agentStpCstBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstBridgeMaxAge.setStatus("current")


class _AgentStpCstBridgeMaxHops_Type(Unsigned32):
    """Custom type agentStpCstBridgeMaxHops based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_AgentStpCstBridgeMaxHops_Type.__name__ = "Unsigned32"
_AgentStpCstBridgeMaxHops_Object = MibScalar
agentStpCstBridgeMaxHops = _AgentStpCstBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 10),
    _AgentStpCstBridgeMaxHops_Type()
)
agentStpCstBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstBridgeMaxHops.setStatus("current")


class _AgentStpCstBridgePriority_Type(Unsigned32):
    """Custom type agentStpCstBridgePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_AgentStpCstBridgePriority_Type.__name__ = "Unsigned32"
_AgentStpCstBridgePriority_Object = MibScalar
agentStpCstBridgePriority = _AgentStpCstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 11),
    _AgentStpCstBridgePriority_Type()
)
agentStpCstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstBridgePriority.setStatus("current")


class _AgentStpCstBridgeHoldCount_Type(Unsigned32):
    """Custom type agentStpCstBridgeHoldCount based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentStpCstBridgeHoldCount_Type.__name__ = "Unsigned32"
_AgentStpCstBridgeHoldCount_Object = MibScalar
agentStpCstBridgeHoldCount = _AgentStpCstBridgeHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 8, 12),
    _AgentStpCstBridgeHoldCount_Type()
)
agentStpCstBridgeHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstBridgeHoldCount.setStatus("current")
_AgentStpCstPortTable_Object = MibTable
agentStpCstPortTable = _AgentStpCstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9)
)
if mibBuilder.loadTexts:
    agentStpCstPortTable.setStatus("current")
_AgentStpCstPortEntry_Object = MibTableRow
agentStpCstPortEntry = _AgentStpCstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1)
)
agentStpCstPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentStpCstPortEntry.setStatus("current")


class _AgentStpCstPortOperEdge_Type(Integer32):
    """Custom type agentStpCstPortOperEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortOperEdge_Type.__name__ = "Integer32"
_AgentStpCstPortOperEdge_Object = MibTableColumn
agentStpCstPortOperEdge = _AgentStpCstPortOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 1),
    _AgentStpCstPortOperEdge_Type()
)
agentStpCstPortOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortOperEdge.setStatus("current")


class _AgentStpCstPortOperPointToPoint_Type(Integer32):
    """Custom type agentStpCstPortOperPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentStpCstPortOperPointToPoint_Type.__name__ = "Integer32"
_AgentStpCstPortOperPointToPoint_Object = MibTableColumn
agentStpCstPortOperPointToPoint = _AgentStpCstPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 2),
    _AgentStpCstPortOperPointToPoint_Type()
)
agentStpCstPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortOperPointToPoint.setStatus("current")


class _AgentStpCstPortTopologyChangeAck_Type(Integer32):
    """Custom type agentStpCstPortTopologyChangeAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentStpCstPortTopologyChangeAck_Type.__name__ = "Integer32"
_AgentStpCstPortTopologyChangeAck_Object = MibTableColumn
agentStpCstPortTopologyChangeAck = _AgentStpCstPortTopologyChangeAck_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 3),
    _AgentStpCstPortTopologyChangeAck_Type()
)
agentStpCstPortTopologyChangeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortTopologyChangeAck.setStatus("current")


class _AgentStpCstPortEdge_Type(Integer32):
    """Custom type agentStpCstPortEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortEdge_Type.__name__ = "Integer32"
_AgentStpCstPortEdge_Object = MibTableColumn
agentStpCstPortEdge = _AgentStpCstPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 4),
    _AgentStpCstPortEdge_Type()
)
agentStpCstPortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortEdge.setStatus("current")


class _AgentStpCstPortForwardingState_Type(Integer32):
    """Custom type agentStpCstPortForwardingState based on Integer32"""
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
        *(("disabled", 4),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("manualFwd", 5),
          ("notParticipate", 6))
    )


_AgentStpCstPortForwardingState_Type.__name__ = "Integer32"
_AgentStpCstPortForwardingState_Object = MibTableColumn
agentStpCstPortForwardingState = _AgentStpCstPortForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 5),
    _AgentStpCstPortForwardingState_Type()
)
agentStpCstPortForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortForwardingState.setStatus("current")
_AgentStpCstPortId_Type = PortId
_AgentStpCstPortId_Object = MibTableColumn
agentStpCstPortId = _AgentStpCstPortId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 6),
    _AgentStpCstPortId_Type()
)
agentStpCstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortId.setStatus("current")


class _AgentStpCstPortPathCost_Type(Unsigned32):
    """Custom type agentStpCstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_AgentStpCstPortPathCost_Type.__name__ = "Unsigned32"
_AgentStpCstPortPathCost_Object = MibTableColumn
agentStpCstPortPathCost = _AgentStpCstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 7),
    _AgentStpCstPortPathCost_Type()
)
agentStpCstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortPathCost.setStatus("current")


class _AgentStpCstPortPriority_Type(Unsigned32):
    """Custom type agentStpCstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_AgentStpCstPortPriority_Type.__name__ = "Unsigned32"
_AgentStpCstPortPriority_Object = MibTableColumn
agentStpCstPortPriority = _AgentStpCstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 8),
    _AgentStpCstPortPriority_Type()
)
agentStpCstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortPriority.setStatus("current")


class _AgentStpCstDesignatedBridgeId_Type(OctetString):
    """Custom type agentStpCstDesignatedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpCstDesignatedBridgeId_Type.__name__ = "OctetString"
_AgentStpCstDesignatedBridgeId_Object = MibTableColumn
agentStpCstDesignatedBridgeId = _AgentStpCstDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 9),
    _AgentStpCstDesignatedBridgeId_Type()
)
agentStpCstDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstDesignatedBridgeId.setStatus("current")
_AgentStpCstDesignatedCost_Type = Unsigned32
_AgentStpCstDesignatedCost_Object = MibTableColumn
agentStpCstDesignatedCost = _AgentStpCstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 10),
    _AgentStpCstDesignatedCost_Type()
)
agentStpCstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstDesignatedCost.setStatus("current")
_AgentStpCstDesignatedPortId_Type = PortId
_AgentStpCstDesignatedPortId_Object = MibTableColumn
agentStpCstDesignatedPortId = _AgentStpCstDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 11),
    _AgentStpCstDesignatedPortId_Type()
)
agentStpCstDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstDesignatedPortId.setStatus("current")


class _AgentStpCstExtPortPathCost_Type(Unsigned32):
    """Custom type agentStpCstExtPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_AgentStpCstExtPortPathCost_Type.__name__ = "Unsigned32"
_AgentStpCstExtPortPathCost_Object = MibTableColumn
agentStpCstExtPortPathCost = _AgentStpCstExtPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 12),
    _AgentStpCstExtPortPathCost_Type()
)
agentStpCstExtPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstExtPortPathCost.setStatus("current")


class _AgentStpCstPortBpduGuardEffect_Type(Integer32):
    """Custom type agentStpCstPortBpduGuardEffect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortBpduGuardEffect_Type.__name__ = "Integer32"
_AgentStpCstPortBpduGuardEffect_Object = MibTableColumn
agentStpCstPortBpduGuardEffect = _AgentStpCstPortBpduGuardEffect_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 13),
    _AgentStpCstPortBpduGuardEffect_Type()
)
agentStpCstPortBpduGuardEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpCstPortBpduGuardEffect.setStatus("current")


class _AgentStpCstPortBpduFilter_Type(Integer32):
    """Custom type agentStpCstPortBpduFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortBpduFilter_Type.__name__ = "Integer32"
_AgentStpCstPortBpduFilter_Object = MibTableColumn
agentStpCstPortBpduFilter = _AgentStpCstPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 14),
    _AgentStpCstPortBpduFilter_Type()
)
agentStpCstPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortBpduFilter.setStatus("current")


class _AgentStpCstPortBpduFlood_Type(Integer32):
    """Custom type agentStpCstPortBpduFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortBpduFlood_Type.__name__ = "Integer32"
_AgentStpCstPortBpduFlood_Object = MibTableColumn
agentStpCstPortBpduFlood = _AgentStpCstPortBpduFlood_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 15),
    _AgentStpCstPortBpduFlood_Type()
)
agentStpCstPortBpduFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortBpduFlood.setStatus("current")


class _AgentStpCstPortAutoEdge_Type(Integer32):
    """Custom type agentStpCstPortAutoEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortAutoEdge_Type.__name__ = "Integer32"
_AgentStpCstPortAutoEdge_Object = MibTableColumn
agentStpCstPortAutoEdge = _AgentStpCstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 16),
    _AgentStpCstPortAutoEdge_Type()
)
agentStpCstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortAutoEdge.setStatus("current")


class _AgentStpCstPortRootGuard_Type(Integer32):
    """Custom type agentStpCstPortRootGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortRootGuard_Type.__name__ = "Integer32"
_AgentStpCstPortRootGuard_Object = MibTableColumn
agentStpCstPortRootGuard = _AgentStpCstPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 17),
    _AgentStpCstPortRootGuard_Type()
)
agentStpCstPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortRootGuard.setStatus("current")


class _AgentStpCstPortTCNGuard_Type(Integer32):
    """Custom type agentStpCstPortTCNGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortTCNGuard_Type.__name__ = "Integer32"
_AgentStpCstPortTCNGuard_Object = MibTableColumn
agentStpCstPortTCNGuard = _AgentStpCstPortTCNGuard_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 18),
    _AgentStpCstPortTCNGuard_Type()
)
agentStpCstPortTCNGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortTCNGuard.setStatus("current")


class _AgentStpCstPortLoopGuard_Type(Integer32):
    """Custom type agentStpCstPortLoopGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpCstPortLoopGuard_Type.__name__ = "Integer32"
_AgentStpCstPortLoopGuard_Object = MibTableColumn
agentStpCstPortLoopGuard = _AgentStpCstPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 9, 1, 19),
    _AgentStpCstPortLoopGuard_Type()
)
agentStpCstPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpCstPortLoopGuard.setStatus("current")
_AgentStpMstTable_Object = MibTable
agentStpMstTable = _AgentStpMstTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10)
)
if mibBuilder.loadTexts:
    agentStpMstTable.setStatus("current")
_AgentStpMstEntry_Object = MibTableRow
agentStpMstEntry = _AgentStpMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1)
)
agentStpMstEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStpMstId"),
)
if mibBuilder.loadTexts:
    agentStpMstEntry.setStatus("current")
_AgentStpMstId_Type = Unsigned32
_AgentStpMstId_Object = MibTableColumn
agentStpMstId = _AgentStpMstId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 1),
    _AgentStpMstId_Type()
)
agentStpMstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstId.setStatus("current")


class _AgentStpMstBridgePriority_Type(Unsigned32):
    """Custom type agentStpMstBridgePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_AgentStpMstBridgePriority_Type.__name__ = "Unsigned32"
_AgentStpMstBridgePriority_Object = MibTableColumn
agentStpMstBridgePriority = _AgentStpMstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 2),
    _AgentStpMstBridgePriority_Type()
)
agentStpMstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpMstBridgePriority.setStatus("current")


class _AgentStpMstBridgeIdentifier_Type(OctetString):
    """Custom type agentStpMstBridgeIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpMstBridgeIdentifier_Type.__name__ = "OctetString"
_AgentStpMstBridgeIdentifier_Object = MibTableColumn
agentStpMstBridgeIdentifier = _AgentStpMstBridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 3),
    _AgentStpMstBridgeIdentifier_Type()
)
agentStpMstBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstBridgeIdentifier.setStatus("current")


class _AgentStpMstDesignatedRootId_Type(OctetString):
    """Custom type agentStpMstDesignatedRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpMstDesignatedRootId_Type.__name__ = "OctetString"
_AgentStpMstDesignatedRootId_Object = MibTableColumn
agentStpMstDesignatedRootId = _AgentStpMstDesignatedRootId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 4),
    _AgentStpMstDesignatedRootId_Type()
)
agentStpMstDesignatedRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstDesignatedRootId.setStatus("current")
_AgentStpMstRootPathCost_Type = Unsigned32
_AgentStpMstRootPathCost_Object = MibTableColumn
agentStpMstRootPathCost = _AgentStpMstRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 5),
    _AgentStpMstRootPathCost_Type()
)
agentStpMstRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstRootPathCost.setStatus("current")


class _AgentStpMstRootPortId_Type(OctetString):
    """Custom type agentStpMstRootPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpMstRootPortId_Type.__name__ = "OctetString"
_AgentStpMstRootPortId_Object = MibTableColumn
agentStpMstRootPortId = _AgentStpMstRootPortId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 6),
    _AgentStpMstRootPortId_Type()
)
agentStpMstRootPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstRootPortId.setStatus("current")
_AgentStpMstTimeSinceTopologyChange_Type = TimeTicks
_AgentStpMstTimeSinceTopologyChange_Object = MibTableColumn
agentStpMstTimeSinceTopologyChange = _AgentStpMstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 7),
    _AgentStpMstTimeSinceTopologyChange_Type()
)
agentStpMstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstTimeSinceTopologyChange.setStatus("current")
_AgentStpMstTopologyChangeCount_Type = Counter32
_AgentStpMstTopologyChangeCount_Object = MibTableColumn
agentStpMstTopologyChangeCount = _AgentStpMstTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 8),
    _AgentStpMstTopologyChangeCount_Type()
)
agentStpMstTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstTopologyChangeCount.setStatus("current")


class _AgentStpMstTopologyChangeParm_Type(Integer32):
    """Custom type agentStpMstTopologyChangeParm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentStpMstTopologyChangeParm_Type.__name__ = "Integer32"
_AgentStpMstTopologyChangeParm_Object = MibTableColumn
agentStpMstTopologyChangeParm = _AgentStpMstTopologyChangeParm_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 9),
    _AgentStpMstTopologyChangeParm_Type()
)
agentStpMstTopologyChangeParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstTopologyChangeParm.setStatus("current")
_AgentStpMstRowStatus_Type = RowStatus
_AgentStpMstRowStatus_Object = MibTableColumn
agentStpMstRowStatus = _AgentStpMstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 10, 1, 10),
    _AgentStpMstRowStatus_Type()
)
agentStpMstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStpMstRowStatus.setStatus("current")
_AgentStpMstPortTable_Object = MibTable
agentStpMstPortTable = _AgentStpMstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11)
)
if mibBuilder.loadTexts:
    agentStpMstPortTable.setStatus("current")
_AgentStpMstPortEntry_Object = MibTableRow
agentStpMstPortEntry = _AgentStpMstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1)
)
agentStpMstPortEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStpMstId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentStpMstPortEntry.setStatus("current")


class _AgentStpMstPortForwardingState_Type(Integer32):
    """Custom type agentStpMstPortForwardingState based on Integer32"""
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
        *(("disabled", 4),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("manualFwd", 5),
          ("notParticipate", 6))
    )


_AgentStpMstPortForwardingState_Type.__name__ = "Integer32"
_AgentStpMstPortForwardingState_Object = MibTableColumn
agentStpMstPortForwardingState = _AgentStpMstPortForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 1),
    _AgentStpMstPortForwardingState_Type()
)
agentStpMstPortForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstPortForwardingState.setStatus("current")


class _AgentStpMstPortId_Type(OctetString):
    """Custom type agentStpMstPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AgentStpMstPortId_Type.__name__ = "OctetString"
_AgentStpMstPortId_Object = MibTableColumn
agentStpMstPortId = _AgentStpMstPortId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 2),
    _AgentStpMstPortId_Type()
)
agentStpMstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstPortId.setStatus("current")


class _AgentStpMstPortPathCost_Type(Unsigned32):
    """Custom type agentStpMstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_AgentStpMstPortPathCost_Type.__name__ = "Unsigned32"
_AgentStpMstPortPathCost_Object = MibTableColumn
agentStpMstPortPathCost = _AgentStpMstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 3),
    _AgentStpMstPortPathCost_Type()
)
agentStpMstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpMstPortPathCost.setStatus("current")


class _AgentStpMstPortPriority_Type(Unsigned32):
    """Custom type agentStpMstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_AgentStpMstPortPriority_Type.__name__ = "Unsigned32"
_AgentStpMstPortPriority_Object = MibTableColumn
agentStpMstPortPriority = _AgentStpMstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 4),
    _AgentStpMstPortPriority_Type()
)
agentStpMstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpMstPortPriority.setStatus("current")


class _AgentStpMstDesignatedBridgeId_Type(OctetString):
    """Custom type agentStpMstDesignatedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentStpMstDesignatedBridgeId_Type.__name__ = "OctetString"
_AgentStpMstDesignatedBridgeId_Object = MibTableColumn
agentStpMstDesignatedBridgeId = _AgentStpMstDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 5),
    _AgentStpMstDesignatedBridgeId_Type()
)
agentStpMstDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstDesignatedBridgeId.setStatus("current")
_AgentStpMstDesignatedCost_Type = Unsigned32
_AgentStpMstDesignatedCost_Object = MibTableColumn
agentStpMstDesignatedCost = _AgentStpMstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 6),
    _AgentStpMstDesignatedCost_Type()
)
agentStpMstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstDesignatedCost.setStatus("current")
_AgentStpMstDesignatedPortId_Type = PortId
_AgentStpMstDesignatedPortId_Object = MibTableColumn
agentStpMstDesignatedPortId = _AgentStpMstDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 7),
    _AgentStpMstDesignatedPortId_Type()
)
agentStpMstDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstDesignatedPortId.setStatus("current")


class _AgentStpMstPortLoopInconsistentState_Type(Integer32):
    """Custom type agentStpMstPortLoopInconsistentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentStpMstPortLoopInconsistentState_Type.__name__ = "Integer32"
_AgentStpMstPortLoopInconsistentState_Object = MibTableColumn
agentStpMstPortLoopInconsistentState = _AgentStpMstPortLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 8),
    _AgentStpMstPortLoopInconsistentState_Type()
)
agentStpMstPortLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstPortLoopInconsistentState.setStatus("current")
_AgentStpMstPortTransitionsIntoLoopInconsistentState_Type = Counter32
_AgentStpMstPortTransitionsIntoLoopInconsistentState_Object = MibTableColumn
agentStpMstPortTransitionsIntoLoopInconsistentState = _AgentStpMstPortTransitionsIntoLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 9),
    _AgentStpMstPortTransitionsIntoLoopInconsistentState_Type()
)
agentStpMstPortTransitionsIntoLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstPortTransitionsIntoLoopInconsistentState.setStatus("current")
_AgentStpMstPortTransitionsOutOfLoopInconsistentState_Type = Counter32
_AgentStpMstPortTransitionsOutOfLoopInconsistentState_Object = MibTableColumn
agentStpMstPortTransitionsOutOfLoopInconsistentState = _AgentStpMstPortTransitionsOutOfLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 11, 1, 10),
    _AgentStpMstPortTransitionsOutOfLoopInconsistentState_Type()
)
agentStpMstPortTransitionsOutOfLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStpMstPortTransitionsOutOfLoopInconsistentState.setStatus("current")
_AgentStpMstVlanTable_Object = MibTable
agentStpMstVlanTable = _AgentStpMstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 12)
)
if mibBuilder.loadTexts:
    agentStpMstVlanTable.setStatus("current")
_AgentStpMstVlanEntry_Object = MibTableRow
agentStpMstVlanEntry = _AgentStpMstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 12, 1)
)
agentStpMstVlanEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentStpMstId"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    agentStpMstVlanEntry.setStatus("current")
_AgentStpMstVlanRowStatus_Type = RowStatus
_AgentStpMstVlanRowStatus_Object = MibTableColumn
agentStpMstVlanRowStatus = _AgentStpMstVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 12, 1, 1),
    _AgentStpMstVlanRowStatus_Type()
)
agentStpMstVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentStpMstVlanRowStatus.setStatus("current")


class _AgentStpBpduGuardMode_Type(Integer32):
    """Custom type agentStpBpduGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpBpduGuardMode_Type.__name__ = "Integer32"
_AgentStpBpduGuardMode_Object = MibScalar
agentStpBpduGuardMode = _AgentStpBpduGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 13),
    _AgentStpBpduGuardMode_Type()
)
agentStpBpduGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpBpduGuardMode.setStatus("current")


class _AgentStpBpduFilterDefault_Type(Integer32):
    """Custom type agentStpBpduFilterDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentStpBpduFilterDefault_Type.__name__ = "Integer32"
_AgentStpBpduFilterDefault_Object = MibScalar
agentStpBpduFilterDefault = _AgentStpBpduFilterDefault_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 14),
    _AgentStpBpduFilterDefault_Type()
)
agentStpBpduFilterDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStpBpduFilterDefault.setStatus("current")
_AgentPvrstpSwitchConfigGroup_ObjectIdentity = ObjectIdentity
agentPvrstpSwitchConfigGroup = _AgentPvrstpSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15)
)


class _AgentPvstpAdminMode_Type(Integer32):
    """Custom type agentPvstpAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPvstpAdminMode_Type.__name__ = "Integer32"
_AgentPvstpAdminMode_Object = MibScalar
agentPvstpAdminMode = _AgentPvstpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 1),
    _AgentPvstpAdminMode_Type()
)
agentPvstpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvstpAdminMode.setStatus("current")


class _AgentPvrstpAdminMode_Type(Integer32):
    """Custom type agentPvrstpAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPvrstpAdminMode_Type.__name__ = "Integer32"
_AgentPvrstpAdminMode_Object = MibScalar
agentPvrstpAdminMode = _AgentPvrstpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 2),
    _AgentPvrstpAdminMode_Type()
)
agentPvrstpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpAdminMode.setStatus("current")


class _AgentPvrstpUplinkFast_Type(Integer32):
    """Custom type agentPvrstpUplinkFast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPvrstpUplinkFast_Type.__name__ = "Integer32"
_AgentPvrstpUplinkFast_Object = MibScalar
agentPvrstpUplinkFast = _AgentPvrstpUplinkFast_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 3),
    _AgentPvrstpUplinkFast_Type()
)
agentPvrstpUplinkFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpUplinkFast.setStatus("current")


class _AgentPvrstpBackboneFast_Type(Integer32):
    """Custom type agentPvrstpBackboneFast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPvrstpBackboneFast_Type.__name__ = "Integer32"
_AgentPvrstpBackboneFast_Object = MibScalar
agentPvrstpBackboneFast = _AgentPvrstpBackboneFast_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 4),
    _AgentPvrstpBackboneFast_Type()
)
agentPvrstpBackboneFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpBackboneFast.setStatus("current")
_AgentPvrstpVlanTable_Object = MibTable
agentPvrstpVlanTable = _AgentPvrstpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 5)
)
if mibBuilder.loadTexts:
    agentPvrstpVlanTable.setStatus("current")
_AgentPvrstpVlanEntry_Object = MibTableRow
agentPvrstpVlanEntry = _AgentPvrstpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 5, 1)
)
agentPvrstpVlanEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPvrstpVlanTableIndex"),
)
if mibBuilder.loadTexts:
    agentPvrstpVlanEntry.setStatus("current")
_AgentPvrstpVlanTableIndex_Type = VlanId
_AgentPvrstpVlanTableIndex_Object = MibTableColumn
agentPvrstpVlanTableIndex = _AgentPvrstpVlanTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 5, 1, 1),
    _AgentPvrstpVlanTableIndex_Type()
)
agentPvrstpVlanTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPvrstpVlanTableIndex.setStatus("current")


class _AgentPvrstpVlanRootPriSec_Type(Integer32):
    """Custom type agentPvrstpVlanRootPriSec based on Integer32"""
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
          ("primary", 1),
          ("secondary", 2))
    )


_AgentPvrstpVlanRootPriSec_Type.__name__ = "Integer32"
_AgentPvrstpVlanRootPriSec_Object = MibTableColumn
agentPvrstpVlanRootPriSec = _AgentPvrstpVlanRootPriSec_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 5, 1, 2),
    _AgentPvrstpVlanRootPriSec_Type()
)
agentPvrstpVlanRootPriSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpVlanRootPriSec.setStatus("current")


class _AgentPvrstpVlanHelloTime_Type(Integer32):
    """Custom type agentPvrstpVlanHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentPvrstpVlanHelloTime_Type.__name__ = "Integer32"
_AgentPvrstpVlanHelloTime_Object = MibTableColumn
agentPvrstpVlanHelloTime = _AgentPvrstpVlanHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 5, 1, 3),
    _AgentPvrstpVlanHelloTime_Type()
)
agentPvrstpVlanHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpVlanHelloTime.setStatus("current")


class _AgentPvrstpVlanFwdDelayTime_Type(Integer32):
    """Custom type agentPvrstpVlanFwdDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_AgentPvrstpVlanFwdDelayTime_Type.__name__ = "Integer32"
_AgentPvrstpVlanFwdDelayTime_Object = MibTableColumn
agentPvrstpVlanFwdDelayTime = _AgentPvrstpVlanFwdDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 5, 1, 4),
    _AgentPvrstpVlanFwdDelayTime_Type()
)
agentPvrstpVlanFwdDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpVlanFwdDelayTime.setStatus("current")


class _AgentPvrstpVlanMaxAgeTime_Type(Integer32):
    """Custom type agentPvrstpVlanMaxAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_AgentPvrstpVlanMaxAgeTime_Type.__name__ = "Integer32"
_AgentPvrstpVlanMaxAgeTime_Object = MibTableColumn
agentPvrstpVlanMaxAgeTime = _AgentPvrstpVlanMaxAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 5, 1, 5),
    _AgentPvrstpVlanMaxAgeTime_Type()
)
agentPvrstpVlanMaxAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpVlanMaxAgeTime.setStatus("current")
_AgentPvrstpPortVlanTable_Object = MibTable
agentPvrstpPortVlanTable = _AgentPvrstpPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 6)
)
if mibBuilder.loadTexts:
    agentPvrstpPortVlanTable.setStatus("current")
_AgentPvrstpPortVlanEntry_Object = MibTableRow
agentPvrstpPortVlanEntry = _AgentPvrstpPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 6, 1)
)
agentPvrstpPortVlanEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPvrstpPortIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentPvrstpVlanIndex"),
)
if mibBuilder.loadTexts:
    agentPvrstpPortVlanEntry.setStatus("current")
_AgentPvrstpPortIndex_Type = Unsigned32
_AgentPvrstpPortIndex_Object = MibTableColumn
agentPvrstpPortIndex = _AgentPvrstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 6, 1, 1),
    _AgentPvrstpPortIndex_Type()
)
agentPvrstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPvrstpPortIndex.setStatus("current")
_AgentPvrstpVlanIndex_Type = Unsigned32
_AgentPvrstpVlanIndex_Object = MibTableColumn
agentPvrstpVlanIndex = _AgentPvrstpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 6, 1, 2),
    _AgentPvrstpVlanIndex_Type()
)
agentPvrstpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPvrstpVlanIndex.setStatus("current")


class _AgentPvrstpPortVlanPriority_Type(Unsigned32):
    """Custom type agentPvrstpPortVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentPvrstpPortVlanPriority_Type.__name__ = "Unsigned32"
_AgentPvrstpPortVlanPriority_Object = MibTableColumn
agentPvrstpPortVlanPriority = _AgentPvrstpPortVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 6, 1, 3),
    _AgentPvrstpPortVlanPriority_Type()
)
agentPvrstpPortVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpPortVlanPriority.setStatus("current")


class _AgentPvrstpVlanCost_Type(Unsigned32):
    """Custom type agentPvrstpVlanCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_AgentPvrstpVlanCost_Type.__name__ = "Unsigned32"
_AgentPvrstpVlanCost_Object = MibTableColumn
agentPvrstpVlanCost = _AgentPvrstpVlanCost_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 15, 15, 6, 1, 4),
    _AgentPvrstpVlanCost_Type()
)
agentPvrstpVlanCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPvrstpVlanCost.setStatus("current")
_AgentAuthenticationGroup_ObjectIdentity = ObjectIdentity
agentAuthenticationGroup = _AgentAuthenticationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16)
)


class _AgentAuthenticationListCreate_Type(DisplayString):
    """Custom type agentAuthenticationListCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 15),
    )


_AgentAuthenticationListCreate_Type.__name__ = "DisplayString"
_AgentAuthenticationListCreate_Object = MibScalar
agentAuthenticationListCreate = _AgentAuthenticationListCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 1),
    _AgentAuthenticationListCreate_Type()
)
agentAuthenticationListCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListCreate.setStatus("current")
_AgentAuthenticationListTable_Object = MibTable
agentAuthenticationListTable = _AgentAuthenticationListTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2)
)
if mibBuilder.loadTexts:
    agentAuthenticationListTable.setStatus("current")
_AgentAuthenticationListEntry_Object = MibTableRow
agentAuthenticationListEntry = _AgentAuthenticationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1)
)
agentAuthenticationListEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentAuthenticationListIndex"),
)
if mibBuilder.loadTexts:
    agentAuthenticationListEntry.setStatus("current")
_AgentAuthenticationListIndex_Type = Unsigned32
_AgentAuthenticationListIndex_Object = MibTableColumn
agentAuthenticationListIndex = _AgentAuthenticationListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1, 1),
    _AgentAuthenticationListIndex_Type()
)
agentAuthenticationListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAuthenticationListIndex.setStatus("current")


class _AgentAuthenticationListName_Type(DisplayString):
    """Custom type agentAuthenticationListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentAuthenticationListName_Type.__name__ = "DisplayString"
_AgentAuthenticationListName_Object = MibTableColumn
agentAuthenticationListName = _AgentAuthenticationListName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1, 2),
    _AgentAuthenticationListName_Type()
)
agentAuthenticationListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAuthenticationListName.setStatus("current")


class _AgentAuthenticationListMethod1_Type(Integer32):
    """Custom type agentAuthenticationListMethod1 based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("ias", 7),
          ("line", 2),
          ("local", 3),
          ("none", 4),
          ("radius", 5),
          ("tacacs", 6),
          ("undefined", 0))
    )


_AgentAuthenticationListMethod1_Type.__name__ = "Integer32"
_AgentAuthenticationListMethod1_Object = MibTableColumn
agentAuthenticationListMethod1 = _AgentAuthenticationListMethod1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1, 3),
    _AgentAuthenticationListMethod1_Type()
)
agentAuthenticationListMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListMethod1.setStatus("current")


class _AgentAuthenticationListMethod2_Type(Integer32):
    """Custom type agentAuthenticationListMethod2 based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("ias", 7),
          ("line", 2),
          ("local", 3),
          ("none", 4),
          ("radius", 5),
          ("tacacs", 6),
          ("undefined", 0))
    )


_AgentAuthenticationListMethod2_Type.__name__ = "Integer32"
_AgentAuthenticationListMethod2_Object = MibTableColumn
agentAuthenticationListMethod2 = _AgentAuthenticationListMethod2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1, 4),
    _AgentAuthenticationListMethod2_Type()
)
agentAuthenticationListMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListMethod2.setStatus("current")


class _AgentAuthenticationListMethod3_Type(Integer32):
    """Custom type agentAuthenticationListMethod3 based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("ias", 7),
          ("line", 2),
          ("local", 3),
          ("none", 4),
          ("radius", 5),
          ("tacacs", 6),
          ("undefined", 0))
    )


_AgentAuthenticationListMethod3_Type.__name__ = "Integer32"
_AgentAuthenticationListMethod3_Object = MibTableColumn
agentAuthenticationListMethod3 = _AgentAuthenticationListMethod3_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1, 5),
    _AgentAuthenticationListMethod3_Type()
)
agentAuthenticationListMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListMethod3.setStatus("current")
_AgentAuthenticationListStatus_Type = RowStatus
_AgentAuthenticationListStatus_Object = MibTableColumn
agentAuthenticationListStatus = _AgentAuthenticationListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1, 6),
    _AgentAuthenticationListStatus_Type()
)
agentAuthenticationListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListStatus.setStatus("current")


class _AgentAuthenticationListMethod4_Type(Integer32):
    """Custom type agentAuthenticationListMethod4 based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("ias", 7),
          ("line", 2),
          ("local", 3),
          ("none", 4),
          ("radius", 5),
          ("tacacs", 6),
          ("undefined", 0))
    )


_AgentAuthenticationListMethod4_Type.__name__ = "Integer32"
_AgentAuthenticationListMethod4_Object = MibTableColumn
agentAuthenticationListMethod4 = _AgentAuthenticationListMethod4_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1, 7),
    _AgentAuthenticationListMethod4_Type()
)
agentAuthenticationListMethod4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListMethod4.setStatus("current")


class _AgentAuthenticationListMethod5_Type(Integer32):
    """Custom type agentAuthenticationListMethod5 based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("ias", 7),
          ("line", 2),
          ("local", 3),
          ("none", 4),
          ("radius", 5),
          ("tacacs", 6),
          ("undefined", 0))
    )


_AgentAuthenticationListMethod5_Type.__name__ = "Integer32"
_AgentAuthenticationListMethod5_Object = MibTableColumn
agentAuthenticationListMethod5 = _AgentAuthenticationListMethod5_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 2, 1, 8),
    _AgentAuthenticationListMethod5_Type()
)
agentAuthenticationListMethod5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthenticationListMethod5.setStatus("current")


class _AgentUserConfigDefaultAuthenticationList_Type(DisplayString):
    """Custom type agentUserConfigDefaultAuthenticationList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentUserConfigDefaultAuthenticationList_Type.__name__ = "DisplayString"
_AgentUserConfigDefaultAuthenticationList_Object = MibScalar
agentUserConfigDefaultAuthenticationList = _AgentUserConfigDefaultAuthenticationList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 3),
    _AgentUserConfigDefaultAuthenticationList_Type()
)
agentUserConfigDefaultAuthenticationList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserConfigDefaultAuthenticationList.setStatus("current")
_AgentUserAuthenticationConfigTable_Object = MibTable
agentUserAuthenticationConfigTable = _AgentUserAuthenticationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 4)
)
if mibBuilder.loadTexts:
    agentUserAuthenticationConfigTable.setStatus("current")
_AgentUserAuthenticationConfigEntry_Object = MibTableRow
agentUserAuthenticationConfigEntry = _AgentUserAuthenticationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 4, 1)
)
if mibBuilder.loadTexts:
    agentUserAuthenticationConfigEntry.setStatus("current")


class _AgentUserAuthenticationList_Type(DisplayString):
    """Custom type agentUserAuthenticationList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentUserAuthenticationList_Type.__name__ = "DisplayString"
_AgentUserAuthenticationList_Object = MibTableColumn
agentUserAuthenticationList = _AgentUserAuthenticationList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 4, 1, 1),
    _AgentUserAuthenticationList_Type()
)
agentUserAuthenticationList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserAuthenticationList.setStatus("current")
_AgentUserPortConfigTable_Object = MibTable
agentUserPortConfigTable = _AgentUserPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 5)
)
if mibBuilder.loadTexts:
    agentUserPortConfigTable.setStatus("current")
_AgentUserPortConfigEntry_Object = MibTableRow
agentUserPortConfigEntry = _AgentUserPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 5, 1)
)
if mibBuilder.loadTexts:
    agentUserPortConfigEntry.setStatus("current")
_AgentUserPortSecurity_Type = AgentPortMask
_AgentUserPortSecurity_Object = MibTableColumn
agentUserPortSecurity = _AgentUserPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 16, 5, 1, 1),
    _AgentUserPortSecurity_Type()
)
agentUserPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUserPortSecurity.setStatus("current")
_AgentClassOfServiceGroup_ObjectIdentity = ObjectIdentity
agentClassOfServiceGroup = _AgentClassOfServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 17)
)
_AgentClassOfServicePortTable_Object = MibTable
agentClassOfServicePortTable = _AgentClassOfServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    agentClassOfServicePortTable.setStatus("current")
_AgentClassOfServicePortEntry_Object = MibTableRow
agentClassOfServicePortEntry = _AgentClassOfServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 17, 1, 1)
)
agentClassOfServicePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EdgeSwitch-SWITCHING-MIB", "agentClassOfServicePortPriority"),
)
if mibBuilder.loadTexts:
    agentClassOfServicePortEntry.setStatus("current")


class _AgentClassOfServicePortPriority_Type(Integer32):
    """Custom type agentClassOfServicePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentClassOfServicePortPriority_Type.__name__ = "Integer32"
_AgentClassOfServicePortPriority_Object = MibTableColumn
agentClassOfServicePortPriority = _AgentClassOfServicePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 17, 1, 1, 1),
    _AgentClassOfServicePortPriority_Type()
)
agentClassOfServicePortPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentClassOfServicePortPriority.setStatus("current")


class _AgentClassOfServicePortClass_Type(Integer32):
    """Custom type agentClassOfServicePortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentClassOfServicePortClass_Type.__name__ = "Integer32"
_AgentClassOfServicePortClass_Object = MibTableColumn
agentClassOfServicePortClass = _AgentClassOfServicePortClass_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 17, 1, 1, 2),
    _AgentClassOfServicePortClass_Type()
)
agentClassOfServicePortClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClassOfServicePortClass.setStatus("current")
_AgentHTTPConfigGroup_ObjectIdentity = ObjectIdentity
agentHTTPConfigGroup = _AgentHTTPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 18)
)


class _AgentHTTPWebMode_Type(Integer32):
    """Custom type agentHTTPWebMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentHTTPWebMode_Type.__name__ = "Integer32"
_AgentHTTPWebMode_Object = MibScalar
agentHTTPWebMode = _AgentHTTPWebMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 18, 1),
    _AgentHTTPWebMode_Type()
)
agentHTTPWebMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentHTTPWebMode.setStatus("current")


class _AgentHTTPJavaMode_Type(Integer32):
    """Custom type agentHTTPJavaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentHTTPJavaMode_Type.__name__ = "Integer32"
_AgentHTTPJavaMode_Object = MibScalar
agentHTTPJavaMode = _AgentHTTPJavaMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 18, 2),
    _AgentHTTPJavaMode_Type()
)
agentHTTPJavaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentHTTPJavaMode.setStatus("current")


class _AgentHTTPMaxSessions_Type(Integer32):
    """Custom type agentHTTPMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AgentHTTPMaxSessions_Type.__name__ = "Integer32"
_AgentHTTPMaxSessions_Object = MibScalar
agentHTTPMaxSessions = _AgentHTTPMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 18, 3),
    _AgentHTTPMaxSessions_Type()
)
agentHTTPMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentHTTPMaxSessions.setStatus("current")


class _AgentHTTPHardTimeout_Type(Integer32):
    """Custom type agentHTTPHardTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_AgentHTTPHardTimeout_Type.__name__ = "Integer32"
_AgentHTTPHardTimeout_Object = MibScalar
agentHTTPHardTimeout = _AgentHTTPHardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 18, 4),
    _AgentHTTPHardTimeout_Type()
)
agentHTTPHardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentHTTPHardTimeout.setStatus("current")


class _AgentHTTPSoftTimeout_Type(Integer32):
    """Custom type agentHTTPSoftTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AgentHTTPSoftTimeout_Type.__name__ = "Integer32"
_AgentHTTPSoftTimeout_Object = MibScalar
agentHTTPSoftTimeout = _AgentHTTPSoftTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 18, 5),
    _AgentHTTPSoftTimeout_Type()
)
agentHTTPSoftTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentHTTPSoftTimeout.setStatus("current")


class _AgentHTTPWebMgmtPortNum_Type(Integer32):
    """Custom type agentHTTPWebMgmtPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(1025, 65535),
    )


_AgentHTTPWebMgmtPortNum_Type.__name__ = "Integer32"
_AgentHTTPWebMgmtPortNum_Object = MibScalar
agentHTTPWebMgmtPortNum = _AgentHTTPWebMgmtPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 18, 6),
    _AgentHTTPWebMgmtPortNum_Type()
)
agentHTTPWebMgmtPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentHTTPWebMgmtPortNum.setStatus("current")
_AgentAutoInstallConfigGroup_ObjectIdentity = ObjectIdentity
agentAutoInstallConfigGroup = _AgentAutoInstallConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 19)
)


class _AgentAutoinstallMode_Type(Integer32):
    """Custom type agentAutoinstallMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentAutoinstallMode_Type.__name__ = "Integer32"
_AgentAutoinstallMode_Object = MibScalar
agentAutoinstallMode = _AgentAutoinstallMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 19, 1),
    _AgentAutoinstallMode_Type()
)
agentAutoinstallMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoinstallMode.setStatus("current")


class _AgentAutoinstallAutosaveMode_Type(Integer32):
    """Custom type agentAutoinstallAutosaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentAutoinstallAutosaveMode_Type.__name__ = "Integer32"
_AgentAutoinstallAutosaveMode_Object = MibScalar
agentAutoinstallAutosaveMode = _AgentAutoinstallAutosaveMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 19, 2),
    _AgentAutoinstallAutosaveMode_Type()
)
agentAutoinstallAutosaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoinstallAutosaveMode.setStatus("current")


class _AgentAutoinstallUnicastRetryCount_Type(Integer32):
    """Custom type agentAutoinstallUnicastRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AgentAutoinstallUnicastRetryCount_Type.__name__ = "Integer32"
_AgentAutoinstallUnicastRetryCount_Object = MibScalar
agentAutoinstallUnicastRetryCount = _AgentAutoinstallUnicastRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 19, 3),
    _AgentAutoinstallUnicastRetryCount_Type()
)
agentAutoinstallUnicastRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoinstallUnicastRetryCount.setStatus("current")
_AgentAutoinstallStatus_Type = DisplayString
_AgentAutoinstallStatus_Object = MibScalar
agentAutoinstallStatus = _AgentAutoinstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 19, 4),
    _AgentAutoinstallStatus_Type()
)
agentAutoinstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoinstallStatus.setStatus("current")


class _AgentAutoinstallAutoRebootMode_Type(Integer32):
    """Custom type agentAutoinstallAutoRebootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentAutoinstallAutoRebootMode_Type.__name__ = "Integer32"
_AgentAutoinstallAutoRebootMode_Object = MibScalar
agentAutoinstallAutoRebootMode = _AgentAutoinstallAutoRebootMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 19, 5),
    _AgentAutoinstallAutoRebootMode_Type()
)
agentAutoinstallAutoRebootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoinstallAutoRebootMode.setStatus("current")


class _AgentAutoinstallOperationalMode_Type(Integer32):
    """Custom type agentAutoinstallOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentAutoinstallOperationalMode_Type.__name__ = "Integer32"
_AgentAutoinstallOperationalMode_Object = MibScalar
agentAutoinstallOperationalMode = _AgentAutoinstallOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 19, 6),
    _AgentAutoinstallOperationalMode_Type()
)
agentAutoinstallOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoinstallOperationalMode.setStatus("current")
_AgentExecAccountingGroup_ObjectIdentity = ObjectIdentity
agentExecAccountingGroup = _AgentExecAccountingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20)
)


class _AgentExecAccountingListCreate_Type(DisplayString):
    """Custom type agentExecAccountingListCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 15),
    )


_AgentExecAccountingListCreate_Type.__name__ = "DisplayString"
_AgentExecAccountingListCreate_Object = MibScalar
agentExecAccountingListCreate = _AgentExecAccountingListCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 1),
    _AgentExecAccountingListCreate_Type()
)
agentExecAccountingListCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAccountingListCreate.setStatus("current")
_AgentExecAccountingListTable_Object = MibTable
agentExecAccountingListTable = _AgentExecAccountingListTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    agentExecAccountingListTable.setStatus("current")
_AgentExecAccountingListEntry_Object = MibTableRow
agentExecAccountingListEntry = _AgentExecAccountingListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 2, 1)
)
agentExecAccountingListEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentExecAccountingListIndex"),
)
if mibBuilder.loadTexts:
    agentExecAccountingListEntry.setStatus("current")
_AgentExecAccountingListIndex_Type = Unsigned32
_AgentExecAccountingListIndex_Object = MibTableColumn
agentExecAccountingListIndex = _AgentExecAccountingListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 2, 1, 1),
    _AgentExecAccountingListIndex_Type()
)
agentExecAccountingListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentExecAccountingListIndex.setStatus("current")


class _AgentExecAccountingListName_Type(DisplayString):
    """Custom type agentExecAccountingListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentExecAccountingListName_Type.__name__ = "DisplayString"
_AgentExecAccountingListName_Object = MibTableColumn
agentExecAccountingListName = _AgentExecAccountingListName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 2, 1, 2),
    _AgentExecAccountingListName_Type()
)
agentExecAccountingListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentExecAccountingListName.setStatus("current")


class _AgentExecAccountingMethodType_Type(Integer32):
    """Custom type agentExecAccountingMethodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("start-stop", 1),
          ("stop-only", 2),
          ("undefined", 0))
    )


_AgentExecAccountingMethodType_Type.__name__ = "Integer32"
_AgentExecAccountingMethodType_Object = MibTableColumn
agentExecAccountingMethodType = _AgentExecAccountingMethodType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 2, 1, 3),
    _AgentExecAccountingMethodType_Type()
)
agentExecAccountingMethodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAccountingMethodType.setStatus("current")


class _AgentExecAccountingListMethod1_Type(Integer32):
    """Custom type agentExecAccountingListMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentExecAccountingListMethod1_Type.__name__ = "Integer32"
_AgentExecAccountingListMethod1_Object = MibTableColumn
agentExecAccountingListMethod1 = _AgentExecAccountingListMethod1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 2, 1, 4),
    _AgentExecAccountingListMethod1_Type()
)
agentExecAccountingListMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAccountingListMethod1.setStatus("current")


class _AgentExecAccountingListMethod2_Type(Integer32):
    """Custom type agentExecAccountingListMethod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentExecAccountingListMethod2_Type.__name__ = "Integer32"
_AgentExecAccountingListMethod2_Object = MibTableColumn
agentExecAccountingListMethod2 = _AgentExecAccountingListMethod2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 2, 1, 5),
    _AgentExecAccountingListMethod2_Type()
)
agentExecAccountingListMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAccountingListMethod2.setStatus("current")
_AgentExecAccountingListStatus_Type = RowStatus
_AgentExecAccountingListStatus_Object = MibTableColumn
agentExecAccountingListStatus = _AgentExecAccountingListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 20, 2, 1, 6),
    _AgentExecAccountingListStatus_Type()
)
agentExecAccountingListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAccountingListStatus.setStatus("current")
_AgentCmdsAccountingGroup_ObjectIdentity = ObjectIdentity
agentCmdsAccountingGroup = _AgentCmdsAccountingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21)
)


class _AgentCmdsAccountingListCreate_Type(DisplayString):
    """Custom type agentCmdsAccountingListCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 15),
    )


_AgentCmdsAccountingListCreate_Type.__name__ = "DisplayString"
_AgentCmdsAccountingListCreate_Object = MibScalar
agentCmdsAccountingListCreate = _AgentCmdsAccountingListCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21, 1),
    _AgentCmdsAccountingListCreate_Type()
)
agentCmdsAccountingListCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAccountingListCreate.setStatus("current")
_AgentCmdsAccountingListTable_Object = MibTable
agentCmdsAccountingListTable = _AgentCmdsAccountingListTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    agentCmdsAccountingListTable.setStatus("current")
_AgentCmdsAccountingListEntry_Object = MibTableRow
agentCmdsAccountingListEntry = _AgentCmdsAccountingListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21, 2, 1)
)
agentCmdsAccountingListEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentCmdsAccountingListIndex"),
)
if mibBuilder.loadTexts:
    agentCmdsAccountingListEntry.setStatus("current")
_AgentCmdsAccountingListIndex_Type = Unsigned32
_AgentCmdsAccountingListIndex_Object = MibTableColumn
agentCmdsAccountingListIndex = _AgentCmdsAccountingListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21, 2, 1, 1),
    _AgentCmdsAccountingListIndex_Type()
)
agentCmdsAccountingListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCmdsAccountingListIndex.setStatus("current")


class _AgentCmdsAccountingListName_Type(DisplayString):
    """Custom type agentCmdsAccountingListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentCmdsAccountingListName_Type.__name__ = "DisplayString"
_AgentCmdsAccountingListName_Object = MibTableColumn
agentCmdsAccountingListName = _AgentCmdsAccountingListName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21, 2, 1, 2),
    _AgentCmdsAccountingListName_Type()
)
agentCmdsAccountingListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCmdsAccountingListName.setStatus("current")


class _AgentCmdsAccountingMethodType_Type(Integer32):
    """Custom type agentCmdsAccountingMethodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("start-stop", 1),
          ("stop-only", 2),
          ("undefined", 0))
    )


_AgentCmdsAccountingMethodType_Type.__name__ = "Integer32"
_AgentCmdsAccountingMethodType_Object = MibTableColumn
agentCmdsAccountingMethodType = _AgentCmdsAccountingMethodType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21, 2, 1, 3),
    _AgentCmdsAccountingMethodType_Type()
)
agentCmdsAccountingMethodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAccountingMethodType.setStatus("current")


class _AgentCmdsAccountingListMethod1_Type(Integer32):
    """Custom type agentCmdsAccountingListMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tacacs", 1),
          ("undefined", 0))
    )


_AgentCmdsAccountingListMethod1_Type.__name__ = "Integer32"
_AgentCmdsAccountingListMethod1_Object = MibTableColumn
agentCmdsAccountingListMethod1 = _AgentCmdsAccountingListMethod1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21, 2, 1, 4),
    _AgentCmdsAccountingListMethod1_Type()
)
agentCmdsAccountingListMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAccountingListMethod1.setStatus("current")
_AgentCmdsAccountingListStatus_Type = RowStatus
_AgentCmdsAccountingListStatus_Object = MibTableColumn
agentCmdsAccountingListStatus = _AgentCmdsAccountingListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 21, 2, 1, 5),
    _AgentCmdsAccountingListStatus_Type()
)
agentCmdsAccountingListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAccountingListStatus.setStatus("current")
_AgentCmdsAuthorizationGroup_ObjectIdentity = ObjectIdentity
agentCmdsAuthorizationGroup = _AgentCmdsAuthorizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23)
)


class _AgentCmdsAuthorizationListCreate_Type(DisplayString):
    """Custom type agentCmdsAuthorizationListCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 20),
    )


_AgentCmdsAuthorizationListCreate_Type.__name__ = "DisplayString"
_AgentCmdsAuthorizationListCreate_Object = MibScalar
agentCmdsAuthorizationListCreate = _AgentCmdsAuthorizationListCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 1),
    _AgentCmdsAuthorizationListCreate_Type()
)
agentCmdsAuthorizationListCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListCreate.setStatus("current")
_AgentCmdsAuthorizationListTable_Object = MibTable
agentCmdsAuthorizationListTable = _AgentCmdsAuthorizationListTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 2)
)
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListTable.setStatus("current")
_AgentCmdsAuthorizationListEntry_Object = MibTableRow
agentCmdsAuthorizationListEntry = _AgentCmdsAuthorizationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 2, 1)
)
agentCmdsAuthorizationListEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentCmdsAuthorizationListIndex"),
)
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListEntry.setStatus("current")
_AgentCmdsAuthorizationListIndex_Type = Unsigned32
_AgentCmdsAuthorizationListIndex_Object = MibTableColumn
agentCmdsAuthorizationListIndex = _AgentCmdsAuthorizationListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 2, 1, 1),
    _AgentCmdsAuthorizationListIndex_Type()
)
agentCmdsAuthorizationListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListIndex.setStatus("current")


class _AgentCmdsAuthorizationListName_Type(DisplayString):
    """Custom type agentCmdsAuthorizationListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AgentCmdsAuthorizationListName_Type.__name__ = "DisplayString"
_AgentCmdsAuthorizationListName_Object = MibTableColumn
agentCmdsAuthorizationListName = _AgentCmdsAuthorizationListName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 2, 1, 2),
    _AgentCmdsAuthorizationListName_Type()
)
agentCmdsAuthorizationListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListName.setStatus("current")
_AgentCmdsAuthorizationListStatus_Type = RowStatus
_AgentCmdsAuthorizationListStatus_Object = MibTableColumn
agentCmdsAuthorizationListStatus = _AgentCmdsAuthorizationListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 2, 1, 3),
    _AgentCmdsAuthorizationListStatus_Type()
)
agentCmdsAuthorizationListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListStatus.setStatus("current")


class _AgentCmdsAuthorizationListMethod1_Type(Integer32):
    """Custom type agentCmdsAuthorizationListMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("none", 4),
          ("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentCmdsAuthorizationListMethod1_Type.__name__ = "Integer32"
_AgentCmdsAuthorizationListMethod1_Object = MibTableColumn
agentCmdsAuthorizationListMethod1 = _AgentCmdsAuthorizationListMethod1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 2, 1, 4),
    _AgentCmdsAuthorizationListMethod1_Type()
)
agentCmdsAuthorizationListMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListMethod1.setStatus("current")


class _AgentCmdsAuthorizationListMethod2_Type(Integer32):
    """Custom type agentCmdsAuthorizationListMethod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("none", 4),
          ("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentCmdsAuthorizationListMethod2_Type.__name__ = "Integer32"
_AgentCmdsAuthorizationListMethod2_Object = MibTableColumn
agentCmdsAuthorizationListMethod2 = _AgentCmdsAuthorizationListMethod2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 2, 1, 5),
    _AgentCmdsAuthorizationListMethod2_Type()
)
agentCmdsAuthorizationListMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListMethod2.setStatus("current")


class _AgentCmdsAuthorizationListMethod3_Type(Integer32):
    """Custom type agentCmdsAuthorizationListMethod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("none", 4),
          ("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentCmdsAuthorizationListMethod3_Type.__name__ = "Integer32"
_AgentCmdsAuthorizationListMethod3_Object = MibTableColumn
agentCmdsAuthorizationListMethod3 = _AgentCmdsAuthorizationListMethod3_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 23, 2, 1, 6),
    _AgentCmdsAuthorizationListMethod3_Type()
)
agentCmdsAuthorizationListMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCmdsAuthorizationListMethod3.setStatus("current")
_AgentExecAuthorizationGroup_ObjectIdentity = ObjectIdentity
agentExecAuthorizationGroup = _AgentExecAuthorizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24)
)


class _AgentExecAuthorizationListCreate_Type(DisplayString):
    """Custom type agentExecAuthorizationListCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 20),
    )


_AgentExecAuthorizationListCreate_Type.__name__ = "DisplayString"
_AgentExecAuthorizationListCreate_Object = MibScalar
agentExecAuthorizationListCreate = _AgentExecAuthorizationListCreate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 1),
    _AgentExecAuthorizationListCreate_Type()
)
agentExecAuthorizationListCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAuthorizationListCreate.setStatus("current")
_AgentExecAuthorizationListTable_Object = MibTable
agentExecAuthorizationListTable = _AgentExecAuthorizationListTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2)
)
if mibBuilder.loadTexts:
    agentExecAuthorizationListTable.setStatus("current")
_AgentExecAuthorizationListEntry_Object = MibTableRow
agentExecAuthorizationListEntry = _AgentExecAuthorizationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2, 1)
)
agentExecAuthorizationListEntry.setIndexNames(
    (0, "EdgeSwitch-SWITCHING-MIB", "agentExecAuthorizationListIndex"),
)
if mibBuilder.loadTexts:
    agentExecAuthorizationListEntry.setStatus("current")
_AgentExecAuthorizationListIndex_Type = Unsigned32
_AgentExecAuthorizationListIndex_Object = MibTableColumn
agentExecAuthorizationListIndex = _AgentExecAuthorizationListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2, 1, 1),
    _AgentExecAuthorizationListIndex_Type()
)
agentExecAuthorizationListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentExecAuthorizationListIndex.setStatus("current")


class _AgentExecAuthorizationListName_Type(DisplayString):
    """Custom type agentExecAuthorizationListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AgentExecAuthorizationListName_Type.__name__ = "DisplayString"
_AgentExecAuthorizationListName_Object = MibTableColumn
agentExecAuthorizationListName = _AgentExecAuthorizationListName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2, 1, 2),
    _AgentExecAuthorizationListName_Type()
)
agentExecAuthorizationListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentExecAuthorizationListName.setStatus("current")
_AgentExecAuthorizationListStatus_Type = RowStatus
_AgentExecAuthorizationListStatus_Object = MibTableColumn
agentExecAuthorizationListStatus = _AgentExecAuthorizationListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2, 1, 3),
    _AgentExecAuthorizationListStatus_Type()
)
agentExecAuthorizationListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAuthorizationListStatus.setStatus("current")


class _AgentExecAuthorizationListMethod1_Type(Integer32):
    """Custom type agentExecAuthorizationListMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("none", 4),
          ("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentExecAuthorizationListMethod1_Type.__name__ = "Integer32"
_AgentExecAuthorizationListMethod1_Object = MibTableColumn
agentExecAuthorizationListMethod1 = _AgentExecAuthorizationListMethod1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2, 1, 4),
    _AgentExecAuthorizationListMethod1_Type()
)
agentExecAuthorizationListMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAuthorizationListMethod1.setStatus("current")


class _AgentExecAuthorizationListMethod2_Type(Integer32):
    """Custom type agentExecAuthorizationListMethod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("none", 4),
          ("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentExecAuthorizationListMethod2_Type.__name__ = "Integer32"
_AgentExecAuthorizationListMethod2_Object = MibTableColumn
agentExecAuthorizationListMethod2 = _AgentExecAuthorizationListMethod2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2, 1, 5),
    _AgentExecAuthorizationListMethod2_Type()
)
agentExecAuthorizationListMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAuthorizationListMethod2.setStatus("current")


class _AgentExecAuthorizationListMethod3_Type(Integer32):
    """Custom type agentExecAuthorizationListMethod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("none", 4),
          ("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentExecAuthorizationListMethod3_Type.__name__ = "Integer32"
_AgentExecAuthorizationListMethod3_Object = MibTableColumn
agentExecAuthorizationListMethod3 = _AgentExecAuthorizationListMethod3_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2, 1, 6),
    _AgentExecAuthorizationListMethod3_Type()
)
agentExecAuthorizationListMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAuthorizationListMethod3.setStatus("current")


class _AgentExecAuthorizationListMethod4_Type(Integer32):
    """Custom type agentExecAuthorizationListMethod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("none", 4),
          ("radius", 2),
          ("tacacs", 1),
          ("undefined", 0))
    )


_AgentExecAuthorizationListMethod4_Type.__name__ = "Integer32"
_AgentExecAuthorizationListMethod4_Object = MibTableColumn
agentExecAuthorizationListMethod4 = _AgentExecAuthorizationListMethod4_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 24, 2, 1, 7),
    _AgentExecAuthorizationListMethod4_Type()
)
agentExecAuthorizationListMethod4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentExecAuthorizationListMethod4.setStatus("current")
_AgentSwitchMbufConfigGroup_ObjectIdentity = ObjectIdentity
agentSwitchMbufConfigGroup = _AgentSwitchMbufConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 25)
)


class _AgentSwitchMbufRisingThreshold_Type(Unsigned32):
    """Custom type agentSwitchMbufRisingThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentSwitchMbufRisingThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchMbufRisingThreshold_Object = MibScalar
agentSwitchMbufRisingThreshold = _AgentSwitchMbufRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 25, 1),
    _AgentSwitchMbufRisingThreshold_Type()
)
agentSwitchMbufRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMbufRisingThreshold.setStatus("current")


class _AgentSwitchMbufFallingThreshold_Type(Unsigned32):
    """Custom type agentSwitchMbufFallingThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentSwitchMbufFallingThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchMbufFallingThreshold_Object = MibScalar
agentSwitchMbufFallingThreshold = _AgentSwitchMbufFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 25, 2),
    _AgentSwitchMbufFallingThreshold_Type()
)
agentSwitchMbufFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMbufFallingThreshold.setStatus("current")
_AgentSwitchMbufNotificationSeverity_Type = AgentLogSeverity
_AgentSwitchMbufNotificationSeverity_Object = MibScalar
agentSwitchMbufNotificationSeverity = _AgentSwitchMbufNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 25, 3),
    _AgentSwitchMbufNotificationSeverity_Type()
)
agentSwitchMbufNotificationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMbufNotificationSeverity.setStatus("current")
_AgentDigitalSignatureConfigGroup_ObjectIdentity = ObjectIdentity
agentDigitalSignatureConfigGroup = _AgentDigitalSignatureConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 26)
)


class _AgentDigitalSignatureVerifyMode_Type(Integer32):
    """Custom type agentDigitalSignatureVerifyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("config", 2),
          ("image", 1),
          ("noverify", 0))
    )


_AgentDigitalSignatureVerifyMode_Type.__name__ = "Integer32"
_AgentDigitalSignatureVerifyMode_Object = MibScalar
agentDigitalSignatureVerifyMode = _AgentDigitalSignatureVerifyMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 2, 26, 1),
    _AgentDigitalSignatureVerifyMode_Type()
)
agentDigitalSignatureVerifyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDigitalSignatureVerifyMode.setStatus("current")
_AgentSystemGroup_ObjectIdentity = ObjectIdentity
agentSystemGroup = _AgentSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3)
)


class _AgentSaveConfig_Type(Integer32):
    """Custom type agentSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSaveConfig_Type.__name__ = "Integer32"
_AgentSaveConfig_Object = MibScalar
agentSaveConfig = _AgentSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 1),
    _AgentSaveConfig_Type()
)
agentSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSaveConfig.setStatus("current")


class _AgentClearConfig_Type(Integer32):
    """Custom type agentClearConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearConfig_Type.__name__ = "Integer32"
_AgentClearConfig_Object = MibScalar
agentClearConfig = _AgentClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 2),
    _AgentClearConfig_Type()
)
agentClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearConfig.setStatus("current")


class _AgentClearLoginSessions_Type(Integer32):
    """Custom type agentClearLoginSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearLoginSessions_Type.__name__ = "Integer32"
_AgentClearLoginSessions_Object = MibScalar
agentClearLoginSessions = _AgentClearLoginSessions_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 4),
    _AgentClearLoginSessions_Type()
)
agentClearLoginSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearLoginSessions.setStatus("current")


class _AgentClearPasswords_Type(Integer32):
    """Custom type agentClearPasswords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearPasswords_Type.__name__ = "Integer32"
_AgentClearPasswords_Object = MibScalar
agentClearPasswords = _AgentClearPasswords_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 5),
    _AgentClearPasswords_Type()
)
agentClearPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearPasswords.setStatus("current")


class _AgentClearPortStats_Type(Integer32):
    """Custom type agentClearPortStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearPortStats_Type.__name__ = "Integer32"
_AgentClearPortStats_Object = MibScalar
agentClearPortStats = _AgentClearPortStats_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 6),
    _AgentClearPortStats_Type()
)
agentClearPortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearPortStats.setStatus("current")


class _AgentClearSwitchStats_Type(Integer32):
    """Custom type agentClearSwitchStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearSwitchStats_Type.__name__ = "Integer32"
_AgentClearSwitchStats_Object = MibScalar
agentClearSwitchStats = _AgentClearSwitchStats_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 7),
    _AgentClearSwitchStats_Type()
)
agentClearSwitchStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearSwitchStats.setStatus("current")


class _AgentClearTrapLog_Type(Integer32):
    """Custom type agentClearTrapLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearTrapLog_Type.__name__ = "Integer32"
_AgentClearTrapLog_Object = MibScalar
agentClearTrapLog = _AgentClearTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 8),
    _AgentClearTrapLog_Type()
)
agentClearTrapLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearTrapLog.setStatus("current")


class _AgentClearVlan_Type(Integer32):
    """Custom type agentClearVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearVlan_Type.__name__ = "Integer32"
_AgentClearVlan_Object = MibScalar
agentClearVlan = _AgentClearVlan_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 9),
    _AgentClearVlan_Type()
)
agentClearVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearVlan.setStatus("current")


class _AgentResetSystem_Type(Integer32):
    """Custom type agentResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentResetSystem_Type.__name__ = "Integer32"
_AgentResetSystem_Object = MibScalar
agentResetSystem = _AgentResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 10),
    _AgentResetSystem_Type()
)
agentResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResetSystem.setStatus("current")


class _AgentSaveConfigStatus_Type(Integer32):
    """Custom type agentSaveConfigStatus based on Integer32"""
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
        *(("notInitiated", 1),
          ("savingComplete", 3),
          ("savingFailed", 4),
          ("savingInProcess", 2))
    )


_AgentSaveConfigStatus_Type.__name__ = "Integer32"
_AgentSaveConfigStatus_Object = MibScalar
agentSaveConfigStatus = _AgentSaveConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 11),
    _AgentSaveConfigStatus_Type()
)
agentSaveConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSaveConfigStatus.setStatus("current")


class _AgentStartupConfigErase_Type(Integer32):
    """Custom type agentStartupConfigErase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("erase", 1)
    )


_AgentStartupConfigErase_Type.__name__ = "Integer32"
_AgentStartupConfigErase_Object = MibScalar
agentStartupConfigErase = _AgentStartupConfigErase_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 12),
    _AgentStartupConfigErase_Type()
)
agentStartupConfigErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStartupConfigErase.setStatus("current")


class _AgentFactoryDefaultsErase_Type(Integer32):
    """Custom type agentFactoryDefaultsErase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("erase", 1)
    )


_AgentFactoryDefaultsErase_Type.__name__ = "Integer32"
_AgentFactoryDefaultsErase_Object = MibScalar
agentFactoryDefaultsErase = _AgentFactoryDefaultsErase_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 3, 13),
    _AgentFactoryDefaultsErase_Type()
)
agentFactoryDefaultsErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFactoryDefaultsErase.setStatus("current")
_AgentCableTesterGroup_ObjectIdentity = ObjectIdentity
agentCableTesterGroup = _AgentCableTesterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 4)
)


class _AgentCableTesterStatus_Type(Integer32):
    """Custom type agentCableTesterStatus based on Integer32"""
    defaultValue = 4

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
          ("failure", 3),
          ("success", 2),
          ("uninitialized", 4))
    )


_AgentCableTesterStatus_Type.__name__ = "Integer32"
_AgentCableTesterStatus_Object = MibScalar
agentCableTesterStatus = _AgentCableTesterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 4, 1),
    _AgentCableTesterStatus_Type()
)
agentCableTesterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCableTesterStatus.setStatus("current")


class _AgentCableTesterIfIndex_Type(Unsigned32):
    """Custom type agentCableTesterIfIndex based on Unsigned32"""
    defaultValue = 0


_AgentCableTesterIfIndex_Object = MibScalar
agentCableTesterIfIndex = _AgentCableTesterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 4, 2),
    _AgentCableTesterIfIndex_Type()
)
agentCableTesterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCableTesterIfIndex.setStatus("current")


class _AgentCableTesterCableStatus_Type(Integer32):
    """Custom type agentCableTesterCableStatus based on Integer32"""
    defaultValue = 4

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
        *(("normal", 1),
          ("open", 2),
          ("short", 3),
          ("unknown", 4))
    )


_AgentCableTesterCableStatus_Type.__name__ = "Integer32"
_AgentCableTesterCableStatus_Object = MibScalar
agentCableTesterCableStatus = _AgentCableTesterCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 4, 3),
    _AgentCableTesterCableStatus_Type()
)
agentCableTesterCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCableTesterCableStatus.setStatus("current")


class _AgentCableTesterMinimumCableLength_Type(Unsigned32):
    """Custom type agentCableTesterMinimumCableLength based on Unsigned32"""
    defaultValue = 0


_AgentCableTesterMinimumCableLength_Object = MibScalar
agentCableTesterMinimumCableLength = _AgentCableTesterMinimumCableLength_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 4, 4),
    _AgentCableTesterMinimumCableLength_Type()
)
agentCableTesterMinimumCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCableTesterMinimumCableLength.setStatus("current")


class _AgentCableTesterMaximumCableLength_Type(Unsigned32):
    """Custom type agentCableTesterMaximumCableLength based on Unsigned32"""
    defaultValue = 0


_AgentCableTesterMaximumCableLength_Object = MibScalar
agentCableTesterMaximumCableLength = _AgentCableTesterMaximumCableLength_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 4, 5),
    _AgentCableTesterMaximumCableLength_Type()
)
agentCableTesterMaximumCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCableTesterMaximumCableLength.setStatus("current")


class _AgentCableTesterCableFailureLocation_Type(Unsigned32):
    """Custom type agentCableTesterCableFailureLocation based on Unsigned32"""
    defaultValue = 0


_AgentCableTesterCableFailureLocation_Object = MibScalar
agentCableTesterCableFailureLocation = _AgentCableTesterCableFailureLocation_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 4, 6),
    _AgentCableTesterCableFailureLocation_Type()
)
agentCableTesterCableFailureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCableTesterCableFailureLocation.setStatus("current")
agentUserConfigEntry.registerAugmentions(
    ("EdgeSwitch-SWITCHING-MIB",
     "agentUserAuthenticationConfigEntry")
)
agentUserAuthenticationConfigEntry.setIndexNames(*agentUserConfigEntry.getIndexNames())
agentUserConfigEntry.registerAugmentions(
    ("EdgeSwitch-SWITCHING-MIB",
     "agentUserPortConfigEntry")
)
agentUserPortConfigEntry.setIndexNames(*agentUserConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

multipleUsersTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    multipleUsersTrap.setStatus(
        "current"
    )

broadcastStormStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 2)
)
if mibBuilder.loadTexts:
    broadcastStormStartTrap.setStatus(
        "obsolete"
    )

broadcastStormEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 3)
)
if mibBuilder.loadTexts:
    broadcastStormEndTrap.setStatus(
        "obsolete"
    )

linkFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 4)
)
if mibBuilder.loadTexts:
    linkFailureTrap.setStatus(
        "obsolete"
    )

vlanRequestFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 5)
)
vlanRequestFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanRequestFailureTrap.setStatus(
        "obsolete"
    )

vlanDeleteLastTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 6)
)
vlanDeleteLastTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanDeleteLastTrap.setStatus(
        "current"
    )

vlanDefaultCfgFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 7)
)
vlanDefaultCfgFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanDefaultCfgFailureTrap.setStatus(
        "current"
    )

vlanRestoreFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 8)
)
vlanRestoreFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanRestoreFailureTrap.setStatus(
        "obsolete"
    )

fanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 9)
)
if mibBuilder.loadTexts:
    fanFailureTrap.setStatus(
        "obsolete"
    )

stpInstanceNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 10)
)
stpInstanceNewRootTrap.setObjects(
    ("EdgeSwitch-SWITCHING-MIB", "agentStpMstId")
)
if mibBuilder.loadTexts:
    stpInstanceNewRootTrap.setStatus(
        "current"
    )

stpInstanceTopologyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 11)
)
stpInstanceTopologyChangeTrap.setObjects(
    ("EdgeSwitch-SWITCHING-MIB", "agentStpMstId")
)
if mibBuilder.loadTexts:
    stpInstanceTopologyChangeTrap.setStatus(
        "current"
    )

powerSupplyStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 12)
)
if mibBuilder.loadTexts:
    powerSupplyStatusChangeTrap.setStatus(
        "obsolete"
    )

failedUserLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 13)
)
if mibBuilder.loadTexts:
    failedUserLoginTrap.setStatus(
        "current"
    )

userLockoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 14)
)
if mibBuilder.loadTexts:
    userLockoutTrap.setStatus(
        "current"
    )

daiIntfErrorDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 15)
)
daiIntfErrorDisabledTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    daiIntfErrorDisabledTrap.setStatus(
        "current"
    )

stpInstanceLoopInconsistentStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 16)
)
stpInstanceLoopInconsistentStartTrap.setObjects(
      *(("EdgeSwitch-SWITCHING-MIB", "agentStpMstId"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    stpInstanceLoopInconsistentStartTrap.setStatus(
        "current"
    )

stpInstanceLoopInconsistentEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 17)
)
stpInstanceLoopInconsistentEndTrap.setObjects(
      *(("EdgeSwitch-SWITCHING-MIB", "agentStpMstId"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    stpInstanceLoopInconsistentEndTrap.setStatus(
        "current"
    )

dhcpSnoopingIntfErrorDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 18)
)
dhcpSnoopingIntfErrorDisabledTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    dhcpSnoopingIntfErrorDisabledTrap.setStatus(
        "current"
    )

noStartupConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 19)
)
if mibBuilder.loadTexts:
    noStartupConfigTrap.setStatus(
        "current"
    )

agentSwitchIpAddressConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 20)
)
agentSwitchIpAddressConflictTrap.setObjects(
      *(("EdgeSwitch-SWITCHING-MIB", "agentSwitchConflictIPAddr"),
        ("EdgeSwitch-SWITCHING-MIB", "agentSwitchConflictMacAddr"))
)
if mibBuilder.loadTexts:
    agentSwitchIpAddressConflictTrap.setStatus(
        "current"
    )

agentSwitchCpuRisingThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 21)
)
agentSwitchCpuRisingThresholdTrap.setObjects(
      *(("EdgeSwitch-SWITCHING-MIB", "agentSwitchCpuProcessRisingThreshold"),
        ("EdgeSwitch-SWITCHING-MIB", "agentSwitchCpuProcessName"))
)
if mibBuilder.loadTexts:
    agentSwitchCpuRisingThresholdTrap.setStatus(
        "current"
    )

agentSwitchCpuFallingThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 22)
)
agentSwitchCpuFallingThresholdTrap.setObjects(
    ("EdgeSwitch-SWITCHING-MIB", "agentSwitchCpuProcessFallingThreshold")
)
if mibBuilder.loadTexts:
    agentSwitchCpuFallingThresholdTrap.setStatus(
        "current"
    )

agentSwitchCpuFreeMemBelowThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 23)
)
agentSwitchCpuFreeMemBelowThresholdTrap.setObjects(
    ("EdgeSwitch-SWITCHING-MIB", "agentSwitchCpuProcessFreeMemoryThreshold")
)
if mibBuilder.loadTexts:
    agentSwitchCpuFreeMemBelowThresholdTrap.setStatus(
        "current"
    )

agentSwitchCpuFreeMemAboveThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 24)
)
agentSwitchCpuFreeMemAboveThresholdTrap.setObjects(
    ("EdgeSwitch-SWITCHING-MIB", "agentSwitchCpuProcessFreeMemoryThreshold")
)
if mibBuilder.loadTexts:
    agentSwitchCpuFreeMemAboveThresholdTrap.setStatus(
        "current"
    )

topologyChangeInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 25)
)
topologyChangeInitiatedTrap.setObjects(
      *(("EdgeSwitch-SWITCHING-MIB", "agentStpMstId"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    topologyChangeInitiatedTrap.setStatus(
        "current"
    )

loopDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 26)
)
loopDetectedTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    loopDetectedTrap.setStatus(
        "current"
    )

agentSwitchMbufRisingThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 27)
)
agentSwitchMbufRisingThresholdTrap.setObjects(
      *(("EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufRisingThreshold"),
        ("EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufsTotal"),
        ("EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufsUsed"),
        ("EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufsFree"))
)
if mibBuilder.loadTexts:
    agentSwitchMbufRisingThresholdTrap.setStatus(
        "current"
    )

agentSwitchMbufFallingThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 1, 0, 28)
)
agentSwitchMbufFallingThresholdTrap.setObjects(
      *(("EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufFallingThreshold"),
        ("EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufsTotal"),
        ("EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufsUsed"),
        ("EdgeSwitch-SWITCHING-MIB", "agentSwitchMbufsFree"))
)
if mibBuilder.loadTexts:
    agentSwitchMbufFallingThresholdTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-SWITCHING-MIB",
    **{"PortList": PortList,
       "VlanList": VlanList,
       "Ipv6Address": Ipv6Address,
       "Ipv6AddressPrefix": Ipv6AddressPrefix,
       "Ipv6AddressIfIdentifier": Ipv6AddressIfIdentifier,
       "Ipv6IfIndex": Ipv6IfIndex,
       "Ipv6IfIndexOrZero": Ipv6IfIndexOrZero,
       "PortId": PortId,
       "fastPathSwitching": fastPathSwitching,
       "fastPathSwitchingTraps": fastPathSwitchingTraps,
       "multipleUsersTrap": multipleUsersTrap,
       "broadcastStormStartTrap": broadcastStormStartTrap,
       "broadcastStormEndTrap": broadcastStormEndTrap,
       "linkFailureTrap": linkFailureTrap,
       "vlanRequestFailureTrap": vlanRequestFailureTrap,
       "vlanDeleteLastTrap": vlanDeleteLastTrap,
       "vlanDefaultCfgFailureTrap": vlanDefaultCfgFailureTrap,
       "vlanRestoreFailureTrap": vlanRestoreFailureTrap,
       "fanFailureTrap": fanFailureTrap,
       "stpInstanceNewRootTrap": stpInstanceNewRootTrap,
       "stpInstanceTopologyChangeTrap": stpInstanceTopologyChangeTrap,
       "powerSupplyStatusChangeTrap": powerSupplyStatusChangeTrap,
       "failedUserLoginTrap": failedUserLoginTrap,
       "userLockoutTrap": userLockoutTrap,
       "daiIntfErrorDisabledTrap": daiIntfErrorDisabledTrap,
       "stpInstanceLoopInconsistentStartTrap": stpInstanceLoopInconsistentStartTrap,
       "stpInstanceLoopInconsistentEndTrap": stpInstanceLoopInconsistentEndTrap,
       "dhcpSnoopingIntfErrorDisabledTrap": dhcpSnoopingIntfErrorDisabledTrap,
       "noStartupConfigTrap": noStartupConfigTrap,
       "agentSwitchIpAddressConflictTrap": agentSwitchIpAddressConflictTrap,
       "agentSwitchCpuRisingThresholdTrap": agentSwitchCpuRisingThresholdTrap,
       "agentSwitchCpuFallingThresholdTrap": agentSwitchCpuFallingThresholdTrap,
       "agentSwitchCpuFreeMemBelowThresholdTrap": agentSwitchCpuFreeMemBelowThresholdTrap,
       "agentSwitchCpuFreeMemAboveThresholdTrap": agentSwitchCpuFreeMemAboveThresholdTrap,
       "topologyChangeInitiatedTrap": topologyChangeInitiatedTrap,
       "loopDetectedTrap": loopDetectedTrap,
       "agentSwitchMbufRisingThresholdTrap": agentSwitchMbufRisingThresholdTrap,
       "agentSwitchMbufFallingThresholdTrap": agentSwitchMbufFallingThresholdTrap,
       "agentInfoGroup": agentInfoGroup,
       "agentInventoryGroup": agentInventoryGroup,
       "agentInventorySysDescription": agentInventorySysDescription,
       "agentInventoryMachineType": agentInventoryMachineType,
       "agentInventoryMachineModel": agentInventoryMachineModel,
       "agentInventorySerialNumber": agentInventorySerialNumber,
       "agentInventoryFRUNumber": agentInventoryFRUNumber,
       "agentInventoryMaintenanceLevel": agentInventoryMaintenanceLevel,
       "agentInventoryPartNumber": agentInventoryPartNumber,
       "agentInventoryManufacturer": agentInventoryManufacturer,
       "agentInventoryBurnedInMacAddress": agentInventoryBurnedInMacAddress,
       "agentInventoryOperatingSystem": agentInventoryOperatingSystem,
       "agentInventoryNetworkProcessingDevice": agentInventoryNetworkProcessingDevice,
       "agentInventoryAdditionalPackages": agentInventoryAdditionalPackages,
       "agentInventorySoftwareVersion": agentInventorySoftwareVersion,
       "agentInventoryHardwareVersion": agentInventoryHardwareVersion,
       "agentTrapLogGroup": agentTrapLogGroup,
       "agentTrapLogTotal": agentTrapLogTotal,
       "agentTrapLogTotalSinceLastViewed": agentTrapLogTotalSinceLastViewed,
       "agentTrapLogTable": agentTrapLogTable,
       "agentTrapLogEntry": agentTrapLogEntry,
       "agentTrapLogIndex": agentTrapLogIndex,
       "agentTrapLogSystemTime": agentTrapLogSystemTime,
       "agentTrapLogTrap": agentTrapLogTrap,
       "agentSupportedMibTable": agentSupportedMibTable,
       "agentSupportedMibEntry": agentSupportedMibEntry,
       "agentSupportedMibIndex": agentSupportedMibIndex,
       "agentSupportedMibName": agentSupportedMibName,
       "agentSupportedMibDescription": agentSupportedMibDescription,
       "agentSwitchCpuProcessGroup": agentSwitchCpuProcessGroup,
       "agentSwitchCpuProcessMemFree": agentSwitchCpuProcessMemFree,
       "agentSwitchCpuProcessMemAvailable": agentSwitchCpuProcessMemAvailable,
       "agentSwitchCpuProcessRisingThreshold": agentSwitchCpuProcessRisingThreshold,
       "agentSwitchCpuProcessRisingThresholdInterval": agentSwitchCpuProcessRisingThresholdInterval,
       "agentSwitchCpuProcessFallingThreshold": agentSwitchCpuProcessFallingThreshold,
       "agentSwitchCpuProcessFallingThresholdInterval": agentSwitchCpuProcessFallingThresholdInterval,
       "agentSwitchCpuProcessFreeMemoryThreshold": agentSwitchCpuProcessFreeMemoryThreshold,
       "agentSwitchCpuProcessTable": agentSwitchCpuProcessTable,
       "agentSwitchCpuProcessEntry": agentSwitchCpuProcessEntry,
       "agentSwitchCpuProcessIndex": agentSwitchCpuProcessIndex,
       "agentSwitchCpuProcessName": agentSwitchCpuProcessName,
       "agentSwitchCpuProcessPercentageUtilization": agentSwitchCpuProcessPercentageUtilization,
       "agentSwitchCpuProcessId": agentSwitchCpuProcessId,
       "agentSwitchCpuProcessTotalUtilization": agentSwitchCpuProcessTotalUtilization,
       "agentSwitchCpuCosQDropGroup": agentSwitchCpuCosQDropGroup,
       "agentSwitchCpuCosQDropTable": agentSwitchCpuCosQDropTable,
       "agentSwitchCpuCosQDropEntry": agentSwitchCpuCosQDropEntry,
       "agentSwitchCpuCosQIndex": agentSwitchCpuCosQIndex,
       "agentSwitchCpuCosQDrops": agentSwitchCpuCosQDrops,
       "agentSwitchMbufGroup": agentSwitchMbufGroup,
       "agentSwitchMbufsFree": agentSwitchMbufsFree,
       "agentSwitchMbufTable": agentSwitchMbufTable,
       "agentSwitchMbufEntry": agentSwitchMbufEntry,
       "agentSwitchMbufPrio": agentSwitchMbufPrio,
       "agentSwitchMbufClassName": agentSwitchMbufClassName,
       "agentSwitchMbufAllocAttempts": agentSwitchMbufAllocAttempts,
       "agentSwitchMbufAllocFails": agentSwitchMbufAllocFails,
       "agentSwitchMbufsTotal": agentSwitchMbufsTotal,
       "agentSwitchMbufsUsed": agentSwitchMbufsUsed,
       "agentConfigGroup": agentConfigGroup,
       "agentCLIConfigGroup": agentCLIConfigGroup,
       "agentLoginSessionTable": agentLoginSessionTable,
       "agentLoginSessionEntry": agentLoginSessionEntry,
       "agentLoginSessionIndex": agentLoginSessionIndex,
       "agentLoginSessionUserName": agentLoginSessionUserName,
       "agentLoginSessionIPAddress": agentLoginSessionIPAddress,
       "agentLoginSessionConnectionType": agentLoginSessionConnectionType,
       "agentLoginSessionIdleTime": agentLoginSessionIdleTime,
       "agentLoginSessionSessionTime": agentLoginSessionSessionTime,
       "agentLoginSessionStatus": agentLoginSessionStatus,
       "agentLoginSessionInetAddressType": agentLoginSessionInetAddressType,
       "agentLoginSessionInetAddress": agentLoginSessionInetAddress,
       "agentTelnetConfigGroup": agentTelnetConfigGroup,
       "agentTelnetLoginTimeout": agentTelnetLoginTimeout,
       "agentTelnetMaxSessions": agentTelnetMaxSessions,
       "agentTelnetAllowNewMode": agentTelnetAllowNewMode,
       "agentTelnetMgmtPortNum": agentTelnetMgmtPortNum,
       "agentUserConfigGroup": agentUserConfigGroup,
       "agentUserConfigCreate": agentUserConfigCreate,
       "agentUserConfigTable": agentUserConfigTable,
       "agentUserConfigEntry": agentUserConfigEntry,
       "agentUserIndex": agentUserIndex,
       "agentUserName": agentUserName,
       "agentUserPassword": agentUserPassword,
       "agentUserAccessMode": agentUserAccessMode,
       "agentUserStatus": agentUserStatus,
       "agentUserAuthenticationType": agentUserAuthenticationType,
       "agentUserEncryptionType": agentUserEncryptionType,
       "agentUserEncryptionPassword": agentUserEncryptionPassword,
       "agentUserLockoutStatus": agentUserLockoutStatus,
       "agentUserPasswordExpireTime": agentUserPasswordExpireTime,
       "agentUserAccessLevel": agentUserAccessLevel,
       "agentSerialGroup": agentSerialGroup,
       "agentSerialTimeout": agentSerialTimeout,
       "agentSerialBaudrate": agentSerialBaudrate,
       "agentSerialCharacterSize": agentSerialCharacterSize,
       "agentSerialHWFlowControlMode": agentSerialHWFlowControlMode,
       "agentSerialStopBits": agentSerialStopBits,
       "agentSerialParityType": agentSerialParityType,
       "agentPasswordManagementConfigGroup": agentPasswordManagementConfigGroup,
       "agentPasswordManagementMinLength": agentPasswordManagementMinLength,
       "agentPasswordManagementHistory": agentPasswordManagementHistory,
       "agentPasswordManagementAging": agentPasswordManagementAging,
       "agentPasswordManagementLockAttempts": agentPasswordManagementLockAttempts,
       "agentPasswordManagementPasswordStrengthCheck": agentPasswordManagementPasswordStrengthCheck,
       "agentPasswordManagementStrengthMinUpperCase": agentPasswordManagementStrengthMinUpperCase,
       "agentPasswordManagementStrengthMinLowerCase": agentPasswordManagementStrengthMinLowerCase,
       "agentPasswordManagementStrengthMinNumericNumbers": agentPasswordManagementStrengthMinNumericNumbers,
       "agentPasswordManagementStrengthMinSpecialCharacters": agentPasswordManagementStrengthMinSpecialCharacters,
       "agentPasswordManagementStrengthMaxConsecutiveCharacters": agentPasswordManagementStrengthMaxConsecutiveCharacters,
       "agentPasswordManagementStrengthMaxRepeatedCharacters": agentPasswordManagementStrengthMaxRepeatedCharacters,
       "agentPasswordManagementStrengthMinCharacterClasses": agentPasswordManagementStrengthMinCharacterClasses,
       "agentPasswordMgmtLastPasswordSetResult": agentPasswordMgmtLastPasswordSetResult,
       "agentPasswordManagementStrengthExcludeKeywordTable": agentPasswordManagementStrengthExcludeKeywordTable,
       "agentPasswordManagementStrengthExcludeKeywordEntry": agentPasswordManagementStrengthExcludeKeywordEntry,
       "agentPasswordMgmtStrengthExcludeKeyword": agentPasswordMgmtStrengthExcludeKeyword,
       "agentPasswordMgmtStrengthExcludeKeywordStatus": agentPasswordMgmtStrengthExcludeKeywordStatus,
       "agentIASUserConfigGroup": agentIASUserConfigGroup,
       "agentIASUserConfigCreate": agentIASUserConfigCreate,
       "agentIASUserConfigTable": agentIASUserConfigTable,
       "agentIASUserConfigEntry": agentIASUserConfigEntry,
       "agentIASUserIndex": agentIASUserIndex,
       "agentIASUserName": agentIASUserName,
       "agentIASUserPassword": agentIASUserPassword,
       "agentIASUserStatus": agentIASUserStatus,
       "agentCLIBannerMsgConfigGroup": agentCLIBannerMsgConfigGroup,
       "agentCLIBannerMessage": agentCLIBannerMessage,
       "agentLagConfigGroup": agentLagConfigGroup,
       "agentLagConfigCreate": agentLagConfigCreate,
       "agentLagSummaryConfigTable": agentLagSummaryConfigTable,
       "agentLagSummaryConfigEntry": agentLagSummaryConfigEntry,
       "agentLagSummaryLagIndex": agentLagSummaryLagIndex,
       "agentLagSummaryName": agentLagSummaryName,
       "agentLagSummaryFlushTimer": agentLagSummaryFlushTimer,
       "agentLagSummaryLinkTrap": agentLagSummaryLinkTrap,
       "agentLagSummaryAdminMode": agentLagSummaryAdminMode,
       "agentLagSummaryStpMode": agentLagSummaryStpMode,
       "agentLagSummaryAddPort": agentLagSummaryAddPort,
       "agentLagSummaryDeletePort": agentLagSummaryDeletePort,
       "agentLagSummaryStatus": agentLagSummaryStatus,
       "agentLagSummaryType": agentLagSummaryType,
       "agentLagSummaryStaticCapability": agentLagSummaryStaticCapability,
       "agentLagSummaryHashOption": agentLagSummaryHashOption,
       "agentLagSummaryMinimumActiveLinks": agentLagSummaryMinimumActiveLinks,
       "agentLagSummaryLocalPreferenceMode": agentLagSummaryLocalPreferenceMode,
       "agentLagSummaryMtuValue": agentLagSummaryMtuValue,
       "agentLagSummaryPortCounter": agentLagSummaryPortCounter,
       "agentLagDetailedConfigTable": agentLagDetailedConfigTable,
       "agentLagDetailedConfigEntry": agentLagDetailedConfigEntry,
       "agentLagDetailedLagIndex": agentLagDetailedLagIndex,
       "agentLagDetailedIfIndex": agentLagDetailedIfIndex,
       "agentLagDetailedPortSpeed": agentLagDetailedPortSpeed,
       "agentLagDetailedPortStatus": agentLagDetailedPortStatus,
       "agentLagDetailedPortCounter": agentLagDetailedPortCounter,
       "agentLagConfigStaticCapability": agentLagConfigStaticCapability,
       "agentLagConfigGroupHashOption": agentLagConfigGroupHashOption,
       "agentLagClearCounters": agentLagClearCounters,
       "agentNetworkConfigGroup": agentNetworkConfigGroup,
       "agentNetworkIPAddress": agentNetworkIPAddress,
       "agentNetworkSubnetMask": agentNetworkSubnetMask,
       "agentNetworkDefaultGateway": agentNetworkDefaultGateway,
       "agentNetworkBurnedInMacAddress": agentNetworkBurnedInMacAddress,
       "agentNetworkLocalAdminMacAddress": agentNetworkLocalAdminMacAddress,
       "agentNetworkMacAddressType": agentNetworkMacAddressType,
       "agentNetworkConfigProtocol": agentNetworkConfigProtocol,
       "agentNetworkConfigProtocolDhcpRenew": agentNetworkConfigProtocolDhcpRenew,
       "agentNetworkWebMode": agentNetworkWebMode,
       "agentNetworkJavaMode": agentNetworkJavaMode,
       "agentNetworkMgmtVlan": agentNetworkMgmtVlan,
       "agentNetworkIpv6AdminMode": agentNetworkIpv6AdminMode,
       "agentNetworkIpv6Gateway": agentNetworkIpv6Gateway,
       "agentNetworkIpv6AddrTable": agentNetworkIpv6AddrTable,
       "agentNetworkIpv6AddrEntry": agentNetworkIpv6AddrEntry,
       "agentNetworkIpv6AddrPrefix": agentNetworkIpv6AddrPrefix,
       "agentNetworkIpv6AddrPrefixLength": agentNetworkIpv6AddrPrefixLength,
       "agentNetworkIpv6AddrEuiFlag": agentNetworkIpv6AddrEuiFlag,
       "agentNetworkIpv6AddrStatus": agentNetworkIpv6AddrStatus,
       "agentNetworkIpv6AddressAutoConfig": agentNetworkIpv6AddressAutoConfig,
       "agentNetworkIpv6ConfigProtocol": agentNetworkIpv6ConfigProtocol,
       "agentNetworkDhcp6ClientDuid": agentNetworkDhcp6ClientDuid,
       "agentNetworkStatsGroup": agentNetworkStatsGroup,
       "agentNetworkDhcp6ADVERTISEMessagesReceived": agentNetworkDhcp6ADVERTISEMessagesReceived,
       "agentNetworkDhcp6REPLYMessagesReceived": agentNetworkDhcp6REPLYMessagesReceived,
       "agentNetworkDhcp6ADVERTISEMessagesDiscarded": agentNetworkDhcp6ADVERTISEMessagesDiscarded,
       "agentNetworkDhcp6REPLYMessagesDiscarded": agentNetworkDhcp6REPLYMessagesDiscarded,
       "agentNetworkDhcp6MalformedMessagesReceived": agentNetworkDhcp6MalformedMessagesReceived,
       "agentNetworkDhcp6SOLICITMessagesSent": agentNetworkDhcp6SOLICITMessagesSent,
       "agentNetworkDhcp6REQUESTMessagesSent": agentNetworkDhcp6REQUESTMessagesSent,
       "agentNetworkDhcp6RENEWMessagesSent": agentNetworkDhcp6RENEWMessagesSent,
       "agentNetworkDhcp6REBINDMessagesSent": agentNetworkDhcp6REBINDMessagesSent,
       "agentNetworkDhcp6RELEASEMessagesSent": agentNetworkDhcp6RELEASEMessagesSent,
       "agentNetworkDhcp6StatsReset": agentNetworkDhcp6StatsReset,
       "agentServicePortConfigGroup": agentServicePortConfigGroup,
       "agentServicePortIPAddress": agentServicePortIPAddress,
       "agentServicePortSubnetMask": agentServicePortSubnetMask,
       "agentServicePortDefaultGateway": agentServicePortDefaultGateway,
       "agentServicePortBurnedInMacAddress": agentServicePortBurnedInMacAddress,
       "agentServicePortConfigProtocol": agentServicePortConfigProtocol,
       "agentServicePortProtocolDhcpRenew": agentServicePortProtocolDhcpRenew,
       "agentServicePortIpv6AdminMode": agentServicePortIpv6AdminMode,
       "agentServicePortIpv6Gateway": agentServicePortIpv6Gateway,
       "agentServicePortIpv6AddrTable": agentServicePortIpv6AddrTable,
       "agentServicePortIpv6AddrEntry": agentServicePortIpv6AddrEntry,
       "agentServicePortIpv6AddrPrefix": agentServicePortIpv6AddrPrefix,
       "agentServicePortIpv6AddrPrefixLength": agentServicePortIpv6AddrPrefixLength,
       "agentServicePortIpv6AddrEuiFlag": agentServicePortIpv6AddrEuiFlag,
       "agentServicePortIpv6AddrStatus": agentServicePortIpv6AddrStatus,
       "agentServicePortIpv6AddressAutoConfig": agentServicePortIpv6AddressAutoConfig,
       "agentServicePortIpv6ConfigProtocol": agentServicePortIpv6ConfigProtocol,
       "agentServicePortDhcp6ClientDuid": agentServicePortDhcp6ClientDuid,
       "agentServicePortStatsGroup": agentServicePortStatsGroup,
       "agentServicePortDhcp6ADVERTISEMessagesReceived": agentServicePortDhcp6ADVERTISEMessagesReceived,
       "agentServicePortDhcp6REPLYMessagesReceived": agentServicePortDhcp6REPLYMessagesReceived,
       "agentServicePortDhcp6ADVERTISEMessagesDiscarded": agentServicePortDhcp6ADVERTISEMessagesDiscarded,
       "agentServicePortDhcp6REPLYMessagesDiscarded": agentServicePortDhcp6REPLYMessagesDiscarded,
       "agentServicePortDhcp6MalformedMessagesReceived": agentServicePortDhcp6MalformedMessagesReceived,
       "agentServicePortDhcp6SOLICITMessagesSent": agentServicePortDhcp6SOLICITMessagesSent,
       "agentServicePortDhcp6REQUESTMessagesSent": agentServicePortDhcp6REQUESTMessagesSent,
       "agentServicePortDhcp6RENEWMessagesSent": agentServicePortDhcp6RENEWMessagesSent,
       "agentServicePortDhcp6REBINDMessagesSent": agentServicePortDhcp6REBINDMessagesSent,
       "agentServicePortDhcp6RELEASEMessagesSent": agentServicePortDhcp6RELEASEMessagesSent,
       "agentServicePortDhcp6StatsReset": agentServicePortDhcp6StatsReset,
       "agentDhcpClientOptionsConfigGroup": agentDhcpClientOptionsConfigGroup,
       "agentVendorClassOptionConfigGroup": agentVendorClassOptionConfigGroup,
       "agentDhcpClientVendorClassIdMode": agentDhcpClientVendorClassIdMode,
       "agentDhcpClientVendorClassIdString": agentDhcpClientVendorClassIdString,
       "agentSnmpConfigGroup": agentSnmpConfigGroup,
       "agentSnmpCommunityCreate": agentSnmpCommunityCreate,
       "agentSnmpCommunityConfigTable": agentSnmpCommunityConfigTable,
       "agentSnmpCommunityConfigEntry": agentSnmpCommunityConfigEntry,
       "agentSnmpCommunityIndex": agentSnmpCommunityIndex,
       "agentSnmpCommunityName": agentSnmpCommunityName,
       "agentSnmpCommunityIPAddress": agentSnmpCommunityIPAddress,
       "agentSnmpCommunityIPMask": agentSnmpCommunityIPMask,
       "agentSnmpCommunityAccessMode": agentSnmpCommunityAccessMode,
       "agentSnmpCommunityStatus": agentSnmpCommunityStatus,
       "agentSnmpTrapReceiverCreate": agentSnmpTrapReceiverCreate,
       "agentSnmpTrapReceiverConfigTable": agentSnmpTrapReceiverConfigTable,
       "agentSnmpTrapReceiverConfigEntry": agentSnmpTrapReceiverConfigEntry,
       "agentSnmpTrapReceiverIndex": agentSnmpTrapReceiverIndex,
       "agentSnmpTrapReceiverCommunityName": agentSnmpTrapReceiverCommunityName,
       "agentSnmpTrapReceiverIPAddress": agentSnmpTrapReceiverIPAddress,
       "agentSnmpTrapReceiverStatus": agentSnmpTrapReceiverStatus,
       "agentSnmpTrapReceiverVersion": agentSnmpTrapReceiverVersion,
       "agentSnmpTrapReceiverIpv6Address": agentSnmpTrapReceiverIpv6Address,
       "agentSnmpTrapReceiverAddressType": agentSnmpTrapReceiverAddressType,
       "agentSnmpTrapReceiverAddress": agentSnmpTrapReceiverAddress,
       "agentSnmpTrapFlagsConfigGroup": agentSnmpTrapFlagsConfigGroup,
       "agentSnmpAuthenticationTrapFlag": agentSnmpAuthenticationTrapFlag,
       "agentSnmpLinkUpDownTrapFlag": agentSnmpLinkUpDownTrapFlag,
       "agentSnmpMultipleUsersTrapFlag": agentSnmpMultipleUsersTrapFlag,
       "agentSnmpSpanningTreeTrapFlag": agentSnmpSpanningTreeTrapFlag,
       "agentSnmpBroadcastStormTrapFlag": agentSnmpBroadcastStormTrapFlag,
       "agentSnmpTrapSourceInterface": agentSnmpTrapSourceInterface,
       "agentSnmpServerPortNum": agentSnmpServerPortNum,
       "agentSpanningTreeConfigGroup": agentSpanningTreeConfigGroup,
       "agentSpanningTreeMode": agentSpanningTreeMode,
       "agentSwitchConfigGroup": agentSwitchConfigGroup,
       "agentSwitchFdbAddressAgingTimeout": agentSwitchFdbAddressAgingTimeout,
       "agentSwitchAddressAgingTimeoutTable": agentSwitchAddressAgingTimeoutTable,
       "agentSwitchAddressAgingTimeoutEntry": agentSwitchAddressAgingTimeoutEntry,
       "agentSwitchAddressAgingTimeout": agentSwitchAddressAgingTimeout,
       "agentSwitchStaticMacFilteringTable": agentSwitchStaticMacFilteringTable,
       "agentSwitchStaticMacFilteringEntry": agentSwitchStaticMacFilteringEntry,
       "agentSwitchStaticMacFilteringVlanId": agentSwitchStaticMacFilteringVlanId,
       "agentSwitchStaticMacFilteringAddress": agentSwitchStaticMacFilteringAddress,
       "agentSwitchStaticMacFilteringSourcePortMask": agentSwitchStaticMacFilteringSourcePortMask,
       "agentSwitchStaticMacFilteringDestPortMask": agentSwitchStaticMacFilteringDestPortMask,
       "agentSwitchStaticMacFilteringStatus": agentSwitchStaticMacFilteringStatus,
       "agentSwitchSnoopingGroup": agentSwitchSnoopingGroup,
       "agentSwitchSnoopingCfgTable": agentSwitchSnoopingCfgTable,
       "agentSwitchSnoopingCfgEntry": agentSwitchSnoopingCfgEntry,
       "agentSwitchSnoopingProtocol": agentSwitchSnoopingProtocol,
       "agentSwitchSnoopingAdminMode": agentSwitchSnoopingAdminMode,
       "agentSwitchSnoopingPortMask": agentSwitchSnoopingPortMask,
       "agentSwitchSnoopingMulticastControlFramesProcessed": agentSwitchSnoopingMulticastControlFramesProcessed,
       "agentSwitchSnoopingProxyQuerierAdminMode": agentSwitchSnoopingProxyQuerierAdminMode,
       "agentSwitchSnoopingIntfGroup": agentSwitchSnoopingIntfGroup,
       "agentSwitchSnoopingIntfTable": agentSwitchSnoopingIntfTable,
       "agentSwitchSnoopingIntfEntry": agentSwitchSnoopingIntfEntry,
       "agentSwitchSnoopingIntfIndex": agentSwitchSnoopingIntfIndex,
       "agentSwitchSnoopingIntfAdminMode": agentSwitchSnoopingIntfAdminMode,
       "agentSwitchSnoopingIntfGroupMembershipInterval": agentSwitchSnoopingIntfGroupMembershipInterval,
       "agentSwitchSnoopingIntfMaxResponseTime": agentSwitchSnoopingIntfMaxResponseTime,
       "agentSwitchSnoopingIntfMRPExpirationTime": agentSwitchSnoopingIntfMRPExpirationTime,
       "agentSwitchSnoopingIntfFastLeaveAdminMode": agentSwitchSnoopingIntfFastLeaveAdminMode,
       "agentSwitchSnoopingIntfMulticastRouterMode": agentSwitchSnoopingIntfMulticastRouterMode,
       "agentSwitchSnoopingIntfVlanIDs": agentSwitchSnoopingIntfVlanIDs,
       "agentSwitchSnoopingIntfProxyQuerierAdminMode": agentSwitchSnoopingIntfProxyQuerierAdminMode,
       "agentSwitchSnoopingVlanGroup": agentSwitchSnoopingVlanGroup,
       "agentSwitchSnoopingVlanTable": agentSwitchSnoopingVlanTable,
       "agentSwitchSnoopingVlanEntry": agentSwitchSnoopingVlanEntry,
       "agentSwitchSnoopingVlanAdminMode": agentSwitchSnoopingVlanAdminMode,
       "agentSwitchSnoopingVlanGroupMembershipInterval": agentSwitchSnoopingVlanGroupMembershipInterval,
       "agentSwitchSnoopingVlanMaxResponseTime": agentSwitchSnoopingVlanMaxResponseTime,
       "agentSwitchSnoopingVlanFastLeaveAdminMode": agentSwitchSnoopingVlanFastLeaveAdminMode,
       "agentSwitchSnoopingVlanMRPExpirationTime": agentSwitchSnoopingVlanMRPExpirationTime,
       "agentSwitchSnoopingVlanReportSuppMode": agentSwitchSnoopingVlanReportSuppMode,
       "agentSwitchSnoopingVlanProxyQuerierAdminMode": agentSwitchSnoopingVlanProxyQuerierAdminMode,
       "agentSwitchVlanStaticMrouterGroup": agentSwitchVlanStaticMrouterGroup,
       "agentSwitchVlanStaticMrouterTable": agentSwitchVlanStaticMrouterTable,
       "agentSwitchVlanStaticMrouterEntry": agentSwitchVlanStaticMrouterEntry,
       "agentSwitchVlanStaticMrouterAdminMode": agentSwitchVlanStaticMrouterAdminMode,
       "agentSwitchMFDBGroup": agentSwitchMFDBGroup,
       "agentSwitchMFDBTable": agentSwitchMFDBTable,
       "agentSwitchMFDBEntry": agentSwitchMFDBEntry,
       "agentSwitchMFDBVlanId": agentSwitchMFDBVlanId,
       "agentSwitchMFDBMacAddress": agentSwitchMFDBMacAddress,
       "agentSwitchMFDBProtocolType": agentSwitchMFDBProtocolType,
       "agentSwitchMFDBType": agentSwitchMFDBType,
       "agentSwitchMFDBDescription": agentSwitchMFDBDescription,
       "agentSwitchMFDBForwardingPortMask": agentSwitchMFDBForwardingPortMask,
       "agentSwitchMFDBFilteringPortMask": agentSwitchMFDBFilteringPortMask,
       "agentSwitchMFDBSummaryTable": agentSwitchMFDBSummaryTable,
       "agentSwitchMFDBSummaryEntry": agentSwitchMFDBSummaryEntry,
       "agentSwitchMFDBSummaryVlanId": agentSwitchMFDBSummaryVlanId,
       "agentSwitchMFDBSummaryMacAddress": agentSwitchMFDBSummaryMacAddress,
       "agentSwitchMFDBSummaryForwardingPortMask": agentSwitchMFDBSummaryForwardingPortMask,
       "agentSwitchMFDBMaxTableEntries": agentSwitchMFDBMaxTableEntries,
       "agentSwitchMFDBMostEntriesUsed": agentSwitchMFDBMostEntriesUsed,
       "agentSwitchMFDBCurrentEntries": agentSwitchMFDBCurrentEntries,
       "agentSwitchDVlanTagGroup": agentSwitchDVlanTagGroup,
       "agentSwitchDVlanTagEthertype": agentSwitchDVlanTagEthertype,
       "agentSwitchDVlanTagTable": agentSwitchDVlanTagTable,
       "agentSwitchDVlanTagEntry": agentSwitchDVlanTagEntry,
       "agentSwitchDVlanTagTPid": agentSwitchDVlanTagTPid,
       "agentSwitchDVlanTagPrimaryTPid": agentSwitchDVlanTagPrimaryTPid,
       "agentSwitchDVlanTagRowStatus": agentSwitchDVlanTagRowStatus,
       "agentSwitchPortDVlanTagTable": agentSwitchPortDVlanTagTable,
       "agentSwitchPortDVlanTagEntry": agentSwitchPortDVlanTagEntry,
       "agentSwitchPortDVlanTagInterfaceIfIndex": agentSwitchPortDVlanTagInterfaceIfIndex,
       "agentSwitchPortDVlanTagTPid": agentSwitchPortDVlanTagTPid,
       "agentSwitchPortDVlanTagMode": agentSwitchPortDVlanTagMode,
       "agentSwitchPortDVlanTagCustomerId": agentSwitchPortDVlanTagCustomerId,
       "agentSwitchPortDVlanTagRowStatus": agentSwitchPortDVlanTagRowStatus,
       "agentSwitchStormControlGroup": agentSwitchStormControlGroup,
       "agentSwitchDot3FlowControlMode": agentSwitchDot3FlowControlMode,
       "agentSwitchBroadcastControlMode": agentSwitchBroadcastControlMode,
       "agentSwitchBroadcastControlThreshold": agentSwitchBroadcastControlThreshold,
       "agentSwitchMulticastControlMode": agentSwitchMulticastControlMode,
       "agentSwitchMulticastControlThreshold": agentSwitchMulticastControlThreshold,
       "agentSwitchUnicastControlMode": agentSwitchUnicastControlMode,
       "agentSwitchUnicastControlThreshold": agentSwitchUnicastControlThreshold,
       "agentSwitchBroadcastControlThresholdUnit": agentSwitchBroadcastControlThresholdUnit,
       "agentSwitchMulticastControlThresholdUnit": agentSwitchMulticastControlThresholdUnit,
       "agentSwitchUnicastControlThresholdUnit": agentSwitchUnicastControlThresholdUnit,
       "agentSwitchVlanMacAssociationGroup": agentSwitchVlanMacAssociationGroup,
       "agentSwitchVlanMacAssociationTable": agentSwitchVlanMacAssociationTable,
       "agentSwitchVlanMacAssociationEntry": agentSwitchVlanMacAssociationEntry,
       "agentSwitchVlanMacAssociationMacAddress": agentSwitchVlanMacAssociationMacAddress,
       "agentSwitchVlanMacAssociationVlanId": agentSwitchVlanMacAssociationVlanId,
       "agentSwitchVlanMacAssociationRowStatus": agentSwitchVlanMacAssociationRowStatus,
       "agentSwitchProtectedPortConfigGroup": agentSwitchProtectedPortConfigGroup,
       "agentSwitchProtectedPortTable": agentSwitchProtectedPortTable,
       "agentSwitchProtectedPortEntry": agentSwitchProtectedPortEntry,
       "agentSwitchProtectedPortGroupId": agentSwitchProtectedPortGroupId,
       "agentSwitchProtectedPortGroupName": agentSwitchProtectedPortGroupName,
       "agentSwitchProtectedPortPortList": agentSwitchProtectedPortPortList,
       "agentSwitchVlanSubnetAssociationGroup": agentSwitchVlanSubnetAssociationGroup,
       "agentSwitchVlanSubnetAssociationTable": agentSwitchVlanSubnetAssociationTable,
       "agentSwitchVlanSubnetAssociationEntry": agentSwitchVlanSubnetAssociationEntry,
       "agentSwitchVlanSubnetAssociationIPAddress": agentSwitchVlanSubnetAssociationIPAddress,
       "agentSwitchVlanSubnetAssociationSubnetMask": agentSwitchVlanSubnetAssociationSubnetMask,
       "agentSwitchVlanSubnetAssociationVlanId": agentSwitchVlanSubnetAssociationVlanId,
       "agentSwitchVlanSubnetAssociationRowStatus": agentSwitchVlanSubnetAssociationRowStatus,
       "agentSwitchSnoopingQuerierGroup": agentSwitchSnoopingQuerierGroup,
       "agentSwitchSnoopingQuerierCfgTable": agentSwitchSnoopingQuerierCfgTable,
       "agentSwitchSnoopingQuerierCfgEntry": agentSwitchSnoopingQuerierCfgEntry,
       "agentSwitchSnoopingQuerierAdminMode": agentSwitchSnoopingQuerierAdminMode,
       "agentSwitchSnoopingQuerierVersion": agentSwitchSnoopingQuerierVersion,
       "agentSwitchSnoopingQuerierAddress": agentSwitchSnoopingQuerierAddress,
       "agentSwitchSnoopingQuerierQueryInterval": agentSwitchSnoopingQuerierQueryInterval,
       "agentSwitchSnoopingQuerierExpiryInterval": agentSwitchSnoopingQuerierExpiryInterval,
       "agentSwitchSnoopingQuerierVlanTable": agentSwitchSnoopingQuerierVlanTable,
       "agentSwitchSnoopingQuerierVlanEntry": agentSwitchSnoopingQuerierVlanEntry,
       "agentSwitchSnoopingQuerierVlanAdminMode": agentSwitchSnoopingQuerierVlanAdminMode,
       "agentSwitchSnoopingQuerierVlanOperMode": agentSwitchSnoopingQuerierVlanOperMode,
       "agentSwitchSnoopingQuerierElectionParticipateMode": agentSwitchSnoopingQuerierElectionParticipateMode,
       "agentSwitchSnoopingQuerierVlanAddress": agentSwitchSnoopingQuerierVlanAddress,
       "agentSwitchSnoopingQuerierOperVersion": agentSwitchSnoopingQuerierOperVersion,
       "agentSwitchSnoopingQuerierOperMaxResponseTime": agentSwitchSnoopingQuerierOperMaxResponseTime,
       "agentSwitchSnoopingQuerierLastQuerierAddress": agentSwitchSnoopingQuerierLastQuerierAddress,
       "agentSwitchSnoopingQuerierLastQuerierVersion": agentSwitchSnoopingQuerierLastQuerierVersion,
       "agentDaiConfigGroup": agentDaiConfigGroup,
       "agentDaiSrcMacValidate": agentDaiSrcMacValidate,
       "agentDaiDstMacValidate": agentDaiDstMacValidate,
       "agentDaiIPValidate": agentDaiIPValidate,
       "agentDaiVlanConfigTable": agentDaiVlanConfigTable,
       "agentDaiVlanConfigEntry": agentDaiVlanConfigEntry,
       "agentDaiVlanIndex": agentDaiVlanIndex,
       "agentDaiVlanDynArpInspEnable": agentDaiVlanDynArpInspEnable,
       "agentDaiVlanLoggingEnable": agentDaiVlanLoggingEnable,
       "agentDaiVlanArpAclName": agentDaiVlanArpAclName,
       "agentDaiVlanArpAclStaticFlag": agentDaiVlanArpAclStaticFlag,
       "agentDaiStatsReset": agentDaiStatsReset,
       "agentDaiVlanStatsTable": agentDaiVlanStatsTable,
       "agentDaiVlanStatsEntry": agentDaiVlanStatsEntry,
       "agentDaiVlanStatsIndex": agentDaiVlanStatsIndex,
       "agentDaiVlanPktsForwarded": agentDaiVlanPktsForwarded,
       "agentDaiVlanPktsDropped": agentDaiVlanPktsDropped,
       "agentDaiVlanDhcpDrops": agentDaiVlanDhcpDrops,
       "agentDaiVlanDhcpPermits": agentDaiVlanDhcpPermits,
       "agentDaiVlanAclDrops": agentDaiVlanAclDrops,
       "agentDaiVlanAclPermits": agentDaiVlanAclPermits,
       "agentDaiVlanSrcMacFailures": agentDaiVlanSrcMacFailures,
       "agentDaiVlanDstMacFailures": agentDaiVlanDstMacFailures,
       "agentDaiVlanIpValidFailures": agentDaiVlanIpValidFailures,
       "agentDaiIfConfigTable": agentDaiIfConfigTable,
       "agentDaiIfConfigEntry": agentDaiIfConfigEntry,
       "agentDaiIfTrustEnable": agentDaiIfTrustEnable,
       "agentDaiIfRateLimit": agentDaiIfRateLimit,
       "agentDaiIfBurstInterval": agentDaiIfBurstInterval,
       "agentArpAclGroup": agentArpAclGroup,
       "agentArpAclTable": agentArpAclTable,
       "agentArpAclEntry": agentArpAclEntry,
       "agentArpAclName": agentArpAclName,
       "agentArpAclRowStatus": agentArpAclRowStatus,
       "agentArpAclRuleTable": agentArpAclRuleTable,
       "agentArpAclRuleEntry": agentArpAclRuleEntry,
       "agentArpAclRuleMatchSenderIpAddr": agentArpAclRuleMatchSenderIpAddr,
       "agentArpAclRuleMatchSenderMacAddr": agentArpAclRuleMatchSenderMacAddr,
       "agentArpAclRuleRowStatus": agentArpAclRuleRowStatus,
       "agentDhcpSnoopingConfigGroup": agentDhcpSnoopingConfigGroup,
       "agentDhcpSnoopingAdminMode": agentDhcpSnoopingAdminMode,
       "agentDhcpSnoopingVerifyMac": agentDhcpSnoopingVerifyMac,
       "agentDhcpSnoopingVlanConfigTable": agentDhcpSnoopingVlanConfigTable,
       "agentDhcpSnoopingVlanConfigEntry": agentDhcpSnoopingVlanConfigEntry,
       "agentDhcpSnoopingVlanIndex": agentDhcpSnoopingVlanIndex,
       "agentDhcpSnoopingVlanEnable": agentDhcpSnoopingVlanEnable,
       "agentDhcpSnoopingIfConfigTable": agentDhcpSnoopingIfConfigTable,
       "agentDhcpSnoopingIfConfigEntry": agentDhcpSnoopingIfConfigEntry,
       "agentDhcpSnoopingIfTrustEnable": agentDhcpSnoopingIfTrustEnable,
       "agentDhcpSnoopingIfLogEnable": agentDhcpSnoopingIfLogEnable,
       "agentDhcpSnoopingIfRateLimit": agentDhcpSnoopingIfRateLimit,
       "agentDhcpSnoopingIfBurstInterval": agentDhcpSnoopingIfBurstInterval,
       "agentIpsgIfConfigTable": agentIpsgIfConfigTable,
       "agentIpsgIfConfigEntry": agentIpsgIfConfigEntry,
       "agentIpsgIfVerifySource": agentIpsgIfVerifySource,
       "agentIpsgIfPortSecurity": agentIpsgIfPortSecurity,
       "agentDhcpSnoopingStatsReset": agentDhcpSnoopingStatsReset,
       "agentDhcpSnoopingStatsTable": agentDhcpSnoopingStatsTable,
       "agentDhcpSnoopingStatsEntry": agentDhcpSnoopingStatsEntry,
       "agentDhcpSnoopingMacVerifyFailures": agentDhcpSnoopingMacVerifyFailures,
       "agentDhcpSnoopingInvalidClientMessages": agentDhcpSnoopingInvalidClientMessages,
       "agentDhcpSnoopingInvalidServerMessages": agentDhcpSnoopingInvalidServerMessages,
       "agentStaticIpsgBindingTable": agentStaticIpsgBindingTable,
       "agentStaticIpsgBindingEntry": agentStaticIpsgBindingEntry,
       "agentStaticIpsgBindingIfIndex": agentStaticIpsgBindingIfIndex,
       "agentStaticIpsgBindingVlanId": agentStaticIpsgBindingVlanId,
       "agentStaticIpsgBindingIpAddr": agentStaticIpsgBindingIpAddr,
       "agentStaticIpsgBindingMacAddr": agentStaticIpsgBindingMacAddr,
       "agentStaticIpsgBindingRowStatus": agentStaticIpsgBindingRowStatus,
       "agentDynamicIpsgBindingTable": agentDynamicIpsgBindingTable,
       "agentDynamicIpsgBindingEntry": agentDynamicIpsgBindingEntry,
       "agentDynamicIpsgBindingIfIndex": agentDynamicIpsgBindingIfIndex,
       "agentDynamicIpsgBindingVlanId": agentDynamicIpsgBindingVlanId,
       "agentDynamicIpsgBindingIpAddr": agentDynamicIpsgBindingIpAddr,
       "agentDynamicIpsgBindingMacAddr": agentDynamicIpsgBindingMacAddr,
       "agentStaticDsBindingTable": agentStaticDsBindingTable,
       "agentStaticDsBindingEntry": agentStaticDsBindingEntry,
       "agentStaticDsBindingIfIndex": agentStaticDsBindingIfIndex,
       "agentStaticDsBindingVlanId": agentStaticDsBindingVlanId,
       "agentStaticDsBindingMacAddr": agentStaticDsBindingMacAddr,
       "agentStaticDsBindingIpAddr": agentStaticDsBindingIpAddr,
       "agentStaticDsBindingRowStatus": agentStaticDsBindingRowStatus,
       "agentDynamicDsBindingTable": agentDynamicDsBindingTable,
       "agentDynamicDsBindingEntry": agentDynamicDsBindingEntry,
       "agentDynamicDsBindingIfIndex": agentDynamicDsBindingIfIndex,
       "agentDynamicDsBindingVlanId": agentDynamicDsBindingVlanId,
       "agentDynamicDsBindingMacAddr": agentDynamicDsBindingMacAddr,
       "agentDynamicDsBindingIpAddr": agentDynamicDsBindingIpAddr,
       "agentDynamicDsBindingLeaseRemainingTime": agentDynamicDsBindingLeaseRemainingTime,
       "agentDhcpSnoopingRemoteFileName": agentDhcpSnoopingRemoteFileName,
       "agentDhcpSnoopingRemoteIpAddr": agentDhcpSnoopingRemoteIpAddr,
       "agentDhcpSnoopingStoreInterval": agentDhcpSnoopingStoreInterval,
       "agentDhcpL2RelayConfigGroup": agentDhcpL2RelayConfigGroup,
       "agentDhcpL2RelayAdminMode": agentDhcpL2RelayAdminMode,
       "agentDhcpL2RelayIfConfigTable": agentDhcpL2RelayIfConfigTable,
       "agentDhcpL2RelayIfConfigEntry": agentDhcpL2RelayIfConfigEntry,
       "agentDhcpL2RelayIfEnable": agentDhcpL2RelayIfEnable,
       "agentDhcpL2RelayIfTrustEnable": agentDhcpL2RelayIfTrustEnable,
       "agentDhcpL2RelayVlanConfigTable": agentDhcpL2RelayVlanConfigTable,
       "agentDhcpL2RelayVlanConfigEntry": agentDhcpL2RelayVlanConfigEntry,
       "agentDhcpL2RelayVlanIndex": agentDhcpL2RelayVlanIndex,
       "agentDhcpL2RelayVlanEnable": agentDhcpL2RelayVlanEnable,
       "agentDhcpL2RelayCircuitIdVlanEnable": agentDhcpL2RelayCircuitIdVlanEnable,
       "agentDhcpL2RelayRemoteIdVlanEnable": agentDhcpL2RelayRemoteIdVlanEnable,
       "agentDhcpL2RelayStatsReset": agentDhcpL2RelayStatsReset,
       "agentDhcpL2RelayStatsTable": agentDhcpL2RelayStatsTable,
       "agentDhcpL2RelayStatsEntry": agentDhcpL2RelayStatsEntry,
       "agentDhcpL2RelayUntrustedSrvrMsgsWithOptn82": agentDhcpL2RelayUntrustedSrvrMsgsWithOptn82,
       "agentDhcpL2RelayUntrustedClntMsgsWithOptn82": agentDhcpL2RelayUntrustedClntMsgsWithOptn82,
       "agentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82": agentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82,
       "agentDhcpL2RelayTrustedClntMsgsWithoutOptn82": agentDhcpL2RelayTrustedClntMsgsWithoutOptn82,
       "agentSwitchVoiceVLANGroup": agentSwitchVoiceVLANGroup,
       "agentSwitchVoiceVLANAdminMode": agentSwitchVoiceVLANAdminMode,
       "agentSwitchVoiceVlanDeviceTable": agentSwitchVoiceVlanDeviceTable,
       "agentSwitchVoiceVlanDeviceEntry": agentSwitchVoiceVlanDeviceEntry,
       "agentSwitchVoiceVlanInterfaceNum": agentSwitchVoiceVlanInterfaceNum,
       "agentSwitchVoiceVlanDeviceMacAddress": agentSwitchVoiceVlanDeviceMacAddress,
       "agentSwitchAddressConflictGroup": agentSwitchAddressConflictGroup,
       "agentSwitchAddressConflictDetectionStatus": agentSwitchAddressConflictDetectionStatus,
       "agentSwitchAddressConflictDetectionStatusReset": agentSwitchAddressConflictDetectionStatusReset,
       "agentSwitchLastConflictingIPAddr": agentSwitchLastConflictingIPAddr,
       "agentSwitchLastConflictingMacAddr": agentSwitchLastConflictingMacAddr,
       "agentSwitchLastConflictReportedTime": agentSwitchLastConflictReportedTime,
       "agentSwitchConflictIPAddr": agentSwitchConflictIPAddr,
       "agentSwitchConflictMacAddr": agentSwitchConflictMacAddr,
       "agentSwitchAddressConflictDetectionRun": agentSwitchAddressConflictDetectionRun,
       "agentSdmPreferConfigEntry": agentSdmPreferConfigEntry,
       "agentSdmPreferCurrentTemplate": agentSdmPreferCurrentTemplate,
       "agentSdmPreferNextTemplate": agentSdmPreferNextTemplate,
       "agentSdmTemplateSummaryTable": agentSdmTemplateSummaryTable,
       "agentSdmTemplateTable": agentSdmTemplateTable,
       "agentSdmTemplateEntry": agentSdmTemplateEntry,
       "agentSdmTemplateId": agentSdmTemplateId,
       "agentArpEntries": agentArpEntries,
       "agentIPv4UnicastRoutes": agentIPv4UnicastRoutes,
       "agentIPv6NdpEntries": agentIPv6NdpEntries,
       "agentIPv6UnicastRoutes": agentIPv6UnicastRoutes,
       "agentEcmpNextHops": agentEcmpNextHops,
       "agentIPv4MulticastRoutes": agentIPv4MulticastRoutes,
       "agentIPv6MulticastRoutes": agentIPv6MulticastRoutes,
       "agentSwitchCutThroughGroup": agentSwitchCutThroughGroup,
       "agentSwitchCutThroughConfigMode": agentSwitchCutThroughConfigMode,
       "agentSwitchCutThroughRunningModeStatus": agentSwitchCutThroughRunningModeStatus,
       "agentSwitchCutThroughConfiguredModeStatus": agentSwitchCutThroughConfiguredModeStatus,
       "agentPortTypeGroup": agentPortTypeGroup,
       "agentPortType40GigBaseX": agentPortType40GigBaseX,
       "agentPrivateVlanGroup": agentPrivateVlanGroup,
       "agentPrivateVlanTable": agentPrivateVlanTable,
       "agentPrivateVlanEntry": agentPrivateVlanEntry,
       "agentPrivateVlanType": agentPrivateVlanType,
       "agentPrivateVlanAssociate": agentPrivateVlanAssociate,
       "agentPrivateVlanIntfAssocTable": agentPrivateVlanIntfAssocTable,
       "agentPrivateVlanIntfAssocEntry": agentPrivateVlanIntfAssocEntry,
       "agentPrivateVlanIntfAssocHostPrimary": agentPrivateVlanIntfAssocHostPrimary,
       "agentPrivateVlanIntfAssocHostSecondary": agentPrivateVlanIntfAssocHostSecondary,
       "agentPrivateVlanIntfAssocPromiscuousPrimary": agentPrivateVlanIntfAssocPromiscuousPrimary,
       "agentPrivateVlanIntfAssocPromiscuousSecondary": agentPrivateVlanIntfAssocPromiscuousSecondary,
       "agentPrivateVlanIntfAssocOperational": agentPrivateVlanIntfAssocOperational,
       "agentSwitchPrivateGroupConfigGroup": agentSwitchPrivateGroupConfigGroup,
       "agentSwitchPrivateGroupTable": agentSwitchPrivateGroupTable,
       "agentSwitchPrivateGroupEntry": agentSwitchPrivateGroupEntry,
       "agentSwitchPrivateGroupId": agentSwitchPrivateGroupId,
       "agentSwitchPrivateGroupName": agentSwitchPrivateGroupName,
       "agentSwitchPrivateGroupMode": agentSwitchPrivateGroupMode,
       "agentSwitchPrivateGroupRowStatus": agentSwitchPrivateGroupRowStatus,
       "agentSwitchPrivateGroupPortTable": agentSwitchPrivateGroupPortTable,
       "agentSwitchPrivateGroupPortEntry": agentSwitchPrivateGroupPortEntry,
       "agentSwitchPrivateGroupPortGroupId": agentSwitchPrivateGroupPortGroupId,
       "agentSwitchPrivateGroupPortGroupName": agentSwitchPrivateGroupPortGroupName,
       "agentSwitchPrivateGroupPortPortList": agentSwitchPrivateGroupPortPortList,
       "agentDhcpv6SnoopingConfigGroup": agentDhcpv6SnoopingConfigGroup,
       "agentDhcpv6SnoopingAdminMode": agentDhcpv6SnoopingAdminMode,
       "agentDhcpv6SnoopingVerifyMac": agentDhcpv6SnoopingVerifyMac,
       "agentDhcpv6SnoopingVlanConfigTable": agentDhcpv6SnoopingVlanConfigTable,
       "agentDhcpv6SnoopingVlanConfigEntry": agentDhcpv6SnoopingVlanConfigEntry,
       "agentDhcpv6SnoopingVlanIndex": agentDhcpv6SnoopingVlanIndex,
       "agentDhcpv6SnoopingVlanEnable": agentDhcpv6SnoopingVlanEnable,
       "agentDhcpv6SnoopingIfConfigTable": agentDhcpv6SnoopingIfConfigTable,
       "agentDhcpv6SnoopingIfConfigEntry": agentDhcpv6SnoopingIfConfigEntry,
       "agentDhcpv6SnoopingIfTrustEnable": agentDhcpv6SnoopingIfTrustEnable,
       "agentDhcpv6SnoopingIfLogEnable": agentDhcpv6SnoopingIfLogEnable,
       "agentDhcpv6SnoopingIfRateLimit": agentDhcpv6SnoopingIfRateLimit,
       "agentDhcpv6SnoopingIfBurstInterval": agentDhcpv6SnoopingIfBurstInterval,
       "agentIpv6sgIfConfigTable": agentIpv6sgIfConfigTable,
       "agentIpv6sgIfConfigEntry": agentIpv6sgIfConfigEntry,
       "agentIpv6sgIfVerifySource": agentIpv6sgIfVerifySource,
       "agentIpv6sgIfPortSecurity": agentIpv6sgIfPortSecurity,
       "agentDhcpv6SnoopingStatsReset": agentDhcpv6SnoopingStatsReset,
       "agentDhcpv6SnoopingStatsTable": agentDhcpv6SnoopingStatsTable,
       "agentDhcpv6SnoopingStatsEntry": agentDhcpv6SnoopingStatsEntry,
       "agentDhcpv6SnoopingMacVerifyFailures": agentDhcpv6SnoopingMacVerifyFailures,
       "agentDhcpv6SnoopingInvalidClientMessages": agentDhcpv6SnoopingInvalidClientMessages,
       "agentDhcpv6SnoopingInvalidServerMessages": agentDhcpv6SnoopingInvalidServerMessages,
       "agentStaticIpv6sgBindingTable": agentStaticIpv6sgBindingTable,
       "agentStaticIpv6sgBindingEntry": agentStaticIpv6sgBindingEntry,
       "agentStaticIpv6sgBindingIfIndex": agentStaticIpv6sgBindingIfIndex,
       "agentStaticIpv6sgBindingVlanId": agentStaticIpv6sgBindingVlanId,
       "agentStaticIpv6sgBindingIpAddr": agentStaticIpv6sgBindingIpAddr,
       "agentStaticIpv6sgBindingMacAddr": agentStaticIpv6sgBindingMacAddr,
       "agentStaticIpv6sgBindingRowStatus": agentStaticIpv6sgBindingRowStatus,
       "agentDynamicIpv6sgBindingTable": agentDynamicIpv6sgBindingTable,
       "agentDynamicIpv6sgBindingEntry": agentDynamicIpv6sgBindingEntry,
       "agentDynamicIpv6sgBindingIfIndex": agentDynamicIpv6sgBindingIfIndex,
       "agentDynamicIpv6sgBindingVlanId": agentDynamicIpv6sgBindingVlanId,
       "agentDynamicIpv6sgBindingIpAddr": agentDynamicIpv6sgBindingIpAddr,
       "agentDynamicIpv6sgBindingMacAddr": agentDynamicIpv6sgBindingMacAddr,
       "agentStaticDsv6BindingTable": agentStaticDsv6BindingTable,
       "agentStaticDsv6BindingEntry": agentStaticDsv6BindingEntry,
       "agentStaticDsv6BindingIfIndex": agentStaticDsv6BindingIfIndex,
       "agentStaticDsv6BindingVlanId": agentStaticDsv6BindingVlanId,
       "agentStaticDsv6BindingMacAddr": agentStaticDsv6BindingMacAddr,
       "agentStaticDsv6BindingIpAddr": agentStaticDsv6BindingIpAddr,
       "agentStaticDsv6BindingRowStatus": agentStaticDsv6BindingRowStatus,
       "agentDynamicDsv6BindingTable": agentDynamicDsv6BindingTable,
       "agentDynamicDsv6BindingEntry": agentDynamicDsv6BindingEntry,
       "agentDynamicDsv6BindingIfIndex": agentDynamicDsv6BindingIfIndex,
       "agentDynamicDsv6BindingVlanId": agentDynamicDsv6BindingVlanId,
       "agentDynamicDsv6BindingMacAddr": agentDynamicDsv6BindingMacAddr,
       "agentDynamicDsv6BindingIpAddr": agentDynamicDsv6BindingIpAddr,
       "agentDynamicDsv6BindingLeaseRemainingTime": agentDynamicDsv6BindingLeaseRemainingTime,
       "agentDhcpv6SnoopingRemoteFileName": agentDhcpv6SnoopingRemoteFileName,
       "agentDhcpv6SnoopingRemoteIpAddr": agentDhcpv6SnoopingRemoteIpAddr,
       "agentDhcpv6SnoopingStoreInterval": agentDhcpv6SnoopingStoreInterval,
       "agentSwitchSnoopSSMGroupTable": agentSwitchSnoopSSMGroupTable,
       "agentSwitchSnoopSSMGroupEntry": agentSwitchSnoopSSMGroupEntry,
       "agentSwitchSnoopSSMGroupAddressType": agentSwitchSnoopSSMGroupAddressType,
       "agentSwitchSnoopSSMGroupAddress": agentSwitchSnoopSSMGroupAddress,
       "agentSwitchSnoopSSMGroupIfIndex": agentSwitchSnoopSSMGroupIfIndex,
       "agentSwitchSnoopSSMGroupVlanId": agentSwitchSnoopSSMGroupVlanId,
       "agentSwitchSnoopSSMGroupLastReporter": agentSwitchSnoopSSMGroupLastReporter,
       "agentSwitchSnoopSSMGroupSourceFilterMode": agentSwitchSnoopSSMGroupSourceFilterMode,
       "agentSwitchSnoopSSMSrcListTable": agentSwitchSnoopSSMSrcListTable,
       "agentSwitchSnoopSSMSrcListEntry": agentSwitchSnoopSSMSrcListEntry,
       "agentSwitchSnoopSSMSrcListAddressType": agentSwitchSnoopSSMSrcListAddressType,
       "agentSwitchSnoopSSMSrcListAddress": agentSwitchSnoopSSMSrcListAddress,
       "agentSwitchSnoopSSMSrcListIfIndex": agentSwitchSnoopSSMSrcListIfIndex,
       "agentSwitchSnoopSSMSrcListVlanId": agentSwitchSnoopSSMSrcListVlanId,
       "agentSwitchSnoopSSMSrcListHostAddress": agentSwitchSnoopSSMSrcListHostAddress,
       "agentSwitchSnoopSSMFDBTable": agentSwitchSnoopSSMFDBTable,
       "agentSwitchSnoopSSMFDBEntry": agentSwitchSnoopSSMFDBEntry,
       "agentSwitchSnoopSSMFDBVlanIndex": agentSwitchSnoopSSMFDBVlanIndex,
       "agentSwitchSnoopSSMFDBGroupAddressType": agentSwitchSnoopSSMFDBGroupAddressType,
       "agentSwitchSnoopSSMFDBGroupAddress": agentSwitchSnoopSSMFDBGroupAddress,
       "agentSwitchSnoopSSMFDBSourceAddress": agentSwitchSnoopSSMFDBSourceAddress,
       "agentSwitchSnoopSSMFDBIncludePortList": agentSwitchSnoopSSMFDBIncludePortList,
       "agentSwitchSnoopSSMFDBExcludePortList": agentSwitchSnoopSSMFDBExcludePortList,
       "agentSwitchportConfigTable": agentSwitchportConfigTable,
       "agentSwitchportConfigEntry": agentSwitchportConfigEntry,
       "agentSwitchportIntfIndex": agentSwitchportIntfIndex,
       "agentSwitchportMode": agentSwitchportMode,
       "agentSwitchportAccessVlanID": agentSwitchportAccessVlanID,
       "agentSwitchportTrunkNativeVlanID": agentSwitchportTrunkNativeVlanID,
       "agentSwitchportTrunkNativeVlanTagging": agentSwitchportTrunkNativeVlanTagging,
       "agentSwitchportTrunkAllowedVlanList": agentSwitchportTrunkAllowedVlanList,
       "agentSwitchportGeneralUntaggedVlanList": agentSwitchportGeneralUntaggedVlanList,
       "agentSwitchportGeneralTaggedVlanList": agentSwitchportGeneralTaggedVlanList,
       "agentSwitchportGeneralForbiddenVlanList": agentSwitchportGeneralForbiddenVlanList,
       "agentSwitchportGeneralDynamicallyAddedVlanList": agentSwitchportGeneralDynamicallyAddedVlanList,
       "agentTransferConfigGroup": agentTransferConfigGroup,
       "agentTransferUploadGroup": agentTransferUploadGroup,
       "agentTransferUploadMode": agentTransferUploadMode,
       "agentTransferUploadServerIP": agentTransferUploadServerIP,
       "agentTransferUploadPath": agentTransferUploadPath,
       "agentTransferUploadFilename": agentTransferUploadFilename,
       "agentTransferUploadDataType": agentTransferUploadDataType,
       "agentTransferUploadStart": agentTransferUploadStart,
       "agentTransferUploadStatus": agentTransferUploadStatus,
       "agentTransferUploadServerAddressType": agentTransferUploadServerAddressType,
       "agentTransferUploadServerAddress": agentTransferUploadServerAddress,
       "agentTransferUploadImagename": agentTransferUploadImagename,
       "agentTransferUploadUsername": agentTransferUploadUsername,
       "agentTransferUploadPassword": agentTransferUploadPassword,
       "agentTransferUploadRemoteFilename": agentTransferUploadRemoteFilename,
       "agentTransferDownloadGroup": agentTransferDownloadGroup,
       "agentTransferDownloadMode": agentTransferDownloadMode,
       "agentTransferDownloadServerIP": agentTransferDownloadServerIP,
       "agentTransferDownloadPath": agentTransferDownloadPath,
       "agentTransferDownloadFilename": agentTransferDownloadFilename,
       "agentTransferDownloadDataType": agentTransferDownloadDataType,
       "agentTransferDownloadStart": agentTransferDownloadStart,
       "agentTransferDownloadStatus": agentTransferDownloadStatus,
       "agentTransferDownloadServerAddressType": agentTransferDownloadServerAddressType,
       "agentTransferDownloadServerAddress": agentTransferDownloadServerAddress,
       "agentTransferDownloadImagename": agentTransferDownloadImagename,
       "agentTransferDownloadUsername": agentTransferDownloadUsername,
       "agentTransferDownloadPassword": agentTransferDownloadPassword,
       "agentTransferDownloadRemoteFilename": agentTransferDownloadRemoteFilename,
       "agentTransferDownloadDigitalSignatureVerifySelect": agentTransferDownloadDigitalSignatureVerifySelect,
       "agentImageConfigGroup": agentImageConfigGroup,
       "agentImage1": agentImage1,
       "agentImage2": agentImage2,
       "agentActiveImage": agentActiveImage,
       "agentNextActiveImage": agentNextActiveImage,
       "agentPortMirroringGroup": agentPortMirroringGroup,
       "agentMirroredPortIfIndex": agentMirroredPortIfIndex,
       "agentProbePortIfIndex": agentProbePortIfIndex,
       "agentPortMirroringMode": agentPortMirroringMode,
       "agentPortMirrorTable": agentPortMirrorTable,
       "agentPortMirrorEntry": agentPortMirrorEntry,
       "agentPortMirrorSessionNum": agentPortMirrorSessionNum,
       "agentPortMirrorDestinationPort": agentPortMirrorDestinationPort,
       "agentPortMirrorSourcePortMask": agentPortMirrorSourcePortMask,
       "agentPortMirrorAdminMode": agentPortMirrorAdminMode,
       "agentPortMirrorSourceVlan": agentPortMirrorSourceVlan,
       "agentPortMirrorRemoteSourceVlan": agentPortMirrorRemoteSourceVlan,
       "agentPortMirrorRemoteDestinationVlan": agentPortMirrorRemoteDestinationVlan,
       "agentPortMirrorReflectorPort": agentPortMirrorReflectorPort,
       "agentPortMirrorIpAccessListNumber": agentPortMirrorIpAccessListNumber,
       "agentPortMirrorMacAccessListNumber": agentPortMirrorMacAccessListNumber,
       "agentPortMirrorTypeTable": agentPortMirrorTypeTable,
       "agentPortMirrorTypeEntry": agentPortMirrorTypeEntry,
       "agentPortMirrorTypeSourcePort": agentPortMirrorTypeSourcePort,
       "agentPortMirrorTypeType": agentPortMirrorTypeType,
       "agentPortMirrorRemoteVlan": agentPortMirrorRemoteVlan,
       "agentPortMirrorRemoteVlanTable": agentPortMirrorRemoteVlanTable,
       "agentPortMirrorRemoteVlanEntry": agentPortMirrorRemoteVlanEntry,
       "agentPortMirrorRemoteVlanIndex": agentPortMirrorRemoteVlanIndex,
       "agentPortMirrorRemoteVlanRowStatus": agentPortMirrorRemoteVlanRowStatus,
       "agentDot3adAggPortTable": agentDot3adAggPortTable,
       "agentDot3adAggPortEntry": agentDot3adAggPortEntry,
       "agentDot3adAggPort": agentDot3adAggPort,
       "agentDot3adAggPortLACPMode": agentDot3adAggPortLACPMode,
       "agentPortConfigTable": agentPortConfigTable,
       "agentPortConfigEntry": agentPortConfigEntry,
       "agentPortDot1dBasePort": agentPortDot1dBasePort,
       "agentPortIfIndex": agentPortIfIndex,
       "agentPortIanaType": agentPortIanaType,
       "agentPortSTPMode": agentPortSTPMode,
       "agentPortSTPState": agentPortSTPState,
       "agentPortAdminMode": agentPortAdminMode,
       "agentPortPhysicalMode": agentPortPhysicalMode,
       "agentPortPhysicalStatus": agentPortPhysicalStatus,
       "agentPortLinkTrapMode": agentPortLinkTrapMode,
       "agentPortClearStats": agentPortClearStats,
       "agentPortDefaultType": agentPortDefaultType,
       "agentPortType": agentPortType,
       "agentPortAutoNegAdminStatus": agentPortAutoNegAdminStatus,
       "agentPortDot3FlowControlMode": agentPortDot3FlowControlMode,
       "agentPortDVlanTagMode": agentPortDVlanTagMode,
       "agentPortDVlanTagEthertype": agentPortDVlanTagEthertype,
       "agentPortDVlanTagCustomerId": agentPortDVlanTagCustomerId,
       "agentPortMaxFrameSizeLimit": agentPortMaxFrameSizeLimit,
       "agentPortMaxFrameSize": agentPortMaxFrameSize,
       "agentPortBroadcastControlMode": agentPortBroadcastControlMode,
       "agentPortBroadcastControlThreshold": agentPortBroadcastControlThreshold,
       "agentPortMulticastControlMode": agentPortMulticastControlMode,
       "agentPortMulticastControlThreshold": agentPortMulticastControlThreshold,
       "agentPortUnicastControlMode": agentPortUnicastControlMode,
       "agentPortUnicastControlThreshold": agentPortUnicastControlThreshold,
       "agentPortBroadcastControlThresholdUnit": agentPortBroadcastControlThresholdUnit,
       "agentPortMulticastControlThresholdUnit": agentPortMulticastControlThresholdUnit,
       "agentPortUnicastControlThresholdUnit": agentPortUnicastControlThresholdUnit,
       "agentPortVoiceVlanMode": agentPortVoiceVlanMode,
       "agentPortVoiceVlanID": agentPortVoiceVlanID,
       "agentPortVoiceVlanPriority": agentPortVoiceVlanPriority,
       "agentPortVoiceVlanDataPriorityMode": agentPortVoiceVlanDataPriorityMode,
       "agentPortVoiceVlanOperationalStatus": agentPortVoiceVlanOperationalStatus,
       "agentPortVoiceVlanUntagged": agentPortVoiceVlanUntagged,
       "agentPortVoiceVlanNoneMode": agentPortVoiceVlanNoneMode,
       "agentPortVoiceVlanDSCP": agentPortVoiceVlanDSCP,
       "agentPortVoiceVlanAuthMode": agentPortVoiceVlanAuthMode,
       "agentPortDot3FlowControlOperStatus": agentPortDot3FlowControlOperStatus,
       "agentPortSwitchportMode": agentPortSwitchportMode,
       "agentProtocolConfigGroup": agentProtocolConfigGroup,
       "agentProtocolGroupCreate": agentProtocolGroupCreate,
       "agentProtocolGroupTable": agentProtocolGroupTable,
       "agentProtocolGroupEntry": agentProtocolGroupEntry,
       "agentProtocolGroupId": agentProtocolGroupId,
       "agentProtocolGroupName": agentProtocolGroupName,
       "agentProtocolGroupVlanId": agentProtocolGroupVlanId,
       "agentProtocolGroupProtocolIP": agentProtocolGroupProtocolIP,
       "agentProtocolGroupProtocolARP": agentProtocolGroupProtocolARP,
       "agentProtocolGroupProtocolIPX": agentProtocolGroupProtocolIPX,
       "agentProtocolGroupStatus": agentProtocolGroupStatus,
       "agentProtocolGroupPortTable": agentProtocolGroupPortTable,
       "agentProtocolGroupPortEntry": agentProtocolGroupPortEntry,
       "agentProtocolGroupPortIfIndex": agentProtocolGroupPortIfIndex,
       "agentProtocolGroupPortStatus": agentProtocolGroupPortStatus,
       "agentProtocolGroupProtocolTable": agentProtocolGroupProtocolTable,
       "agentProtocolGroupProtocolEntry": agentProtocolGroupProtocolEntry,
       "agentProtocolGroupProtocolID": agentProtocolGroupProtocolID,
       "agentProtocolGroupProtocolStatus": agentProtocolGroupProtocolStatus,
       "agentStpSwitchConfigGroup": agentStpSwitchConfigGroup,
       "agentStpConfigDigestKey": agentStpConfigDigestKey,
       "agentStpConfigFormatSelector": agentStpConfigFormatSelector,
       "agentStpConfigName": agentStpConfigName,
       "agentStpConfigRevision": agentStpConfigRevision,
       "agentStpForceVersion": agentStpForceVersion,
       "agentStpAdminMode": agentStpAdminMode,
       "agentStpPortTable": agentStpPortTable,
       "agentStpPortEntry": agentStpPortEntry,
       "agentStpPortState": agentStpPortState,
       "agentStpPortStatsMstpBpduRx": agentStpPortStatsMstpBpduRx,
       "agentStpPortStatsMstpBpduTx": agentStpPortStatsMstpBpduTx,
       "agentStpPortStatsRstpBpduRx": agentStpPortStatsRstpBpduRx,
       "agentStpPortStatsRstpBpduTx": agentStpPortStatsRstpBpduTx,
       "agentStpPortStatsStpBpduRx": agentStpPortStatsStpBpduRx,
       "agentStpPortStatsStpBpduTx": agentStpPortStatsStpBpduTx,
       "agentStpPortUpTime": agentStpPortUpTime,
       "agentStpPortMigrationCheck": agentStpPortMigrationCheck,
       "agentStpCstConfigGroup": agentStpCstConfigGroup,
       "agentStpCstHelloTime": agentStpCstHelloTime,
       "agentStpCstMaxAge": agentStpCstMaxAge,
       "agentStpCstRegionalRootId": agentStpCstRegionalRootId,
       "agentStpCstRegionalRootPathCost": agentStpCstRegionalRootPathCost,
       "agentStpCstRootFwdDelay": agentStpCstRootFwdDelay,
       "agentStpCstBridgeFwdDelay": agentStpCstBridgeFwdDelay,
       "agentStpCstBridgeHelloTime": agentStpCstBridgeHelloTime,
       "agentStpCstBridgeHoldTime": agentStpCstBridgeHoldTime,
       "agentStpCstBridgeMaxAge": agentStpCstBridgeMaxAge,
       "agentStpCstBridgeMaxHops": agentStpCstBridgeMaxHops,
       "agentStpCstBridgePriority": agentStpCstBridgePriority,
       "agentStpCstBridgeHoldCount": agentStpCstBridgeHoldCount,
       "agentStpCstPortTable": agentStpCstPortTable,
       "agentStpCstPortEntry": agentStpCstPortEntry,
       "agentStpCstPortOperEdge": agentStpCstPortOperEdge,
       "agentStpCstPortOperPointToPoint": agentStpCstPortOperPointToPoint,
       "agentStpCstPortTopologyChangeAck": agentStpCstPortTopologyChangeAck,
       "agentStpCstPortEdge": agentStpCstPortEdge,
       "agentStpCstPortForwardingState": agentStpCstPortForwardingState,
       "agentStpCstPortId": agentStpCstPortId,
       "agentStpCstPortPathCost": agentStpCstPortPathCost,
       "agentStpCstPortPriority": agentStpCstPortPriority,
       "agentStpCstDesignatedBridgeId": agentStpCstDesignatedBridgeId,
       "agentStpCstDesignatedCost": agentStpCstDesignatedCost,
       "agentStpCstDesignatedPortId": agentStpCstDesignatedPortId,
       "agentStpCstExtPortPathCost": agentStpCstExtPortPathCost,
       "agentStpCstPortBpduGuardEffect": agentStpCstPortBpduGuardEffect,
       "agentStpCstPortBpduFilter": agentStpCstPortBpduFilter,
       "agentStpCstPortBpduFlood": agentStpCstPortBpduFlood,
       "agentStpCstPortAutoEdge": agentStpCstPortAutoEdge,
       "agentStpCstPortRootGuard": agentStpCstPortRootGuard,
       "agentStpCstPortTCNGuard": agentStpCstPortTCNGuard,
       "agentStpCstPortLoopGuard": agentStpCstPortLoopGuard,
       "agentStpMstTable": agentStpMstTable,
       "agentStpMstEntry": agentStpMstEntry,
       "agentStpMstId": agentStpMstId,
       "agentStpMstBridgePriority": agentStpMstBridgePriority,
       "agentStpMstBridgeIdentifier": agentStpMstBridgeIdentifier,
       "agentStpMstDesignatedRootId": agentStpMstDesignatedRootId,
       "agentStpMstRootPathCost": agentStpMstRootPathCost,
       "agentStpMstRootPortId": agentStpMstRootPortId,
       "agentStpMstTimeSinceTopologyChange": agentStpMstTimeSinceTopologyChange,
       "agentStpMstTopologyChangeCount": agentStpMstTopologyChangeCount,
       "agentStpMstTopologyChangeParm": agentStpMstTopologyChangeParm,
       "agentStpMstRowStatus": agentStpMstRowStatus,
       "agentStpMstPortTable": agentStpMstPortTable,
       "agentStpMstPortEntry": agentStpMstPortEntry,
       "agentStpMstPortForwardingState": agentStpMstPortForwardingState,
       "agentStpMstPortId": agentStpMstPortId,
       "agentStpMstPortPathCost": agentStpMstPortPathCost,
       "agentStpMstPortPriority": agentStpMstPortPriority,
       "agentStpMstDesignatedBridgeId": agentStpMstDesignatedBridgeId,
       "agentStpMstDesignatedCost": agentStpMstDesignatedCost,
       "agentStpMstDesignatedPortId": agentStpMstDesignatedPortId,
       "agentStpMstPortLoopInconsistentState": agentStpMstPortLoopInconsistentState,
       "agentStpMstPortTransitionsIntoLoopInconsistentState": agentStpMstPortTransitionsIntoLoopInconsistentState,
       "agentStpMstPortTransitionsOutOfLoopInconsistentState": agentStpMstPortTransitionsOutOfLoopInconsistentState,
       "agentStpMstVlanTable": agentStpMstVlanTable,
       "agentStpMstVlanEntry": agentStpMstVlanEntry,
       "agentStpMstVlanRowStatus": agentStpMstVlanRowStatus,
       "agentStpBpduGuardMode": agentStpBpduGuardMode,
       "agentStpBpduFilterDefault": agentStpBpduFilterDefault,
       "agentPvrstpSwitchConfigGroup": agentPvrstpSwitchConfigGroup,
       "agentPvstpAdminMode": agentPvstpAdminMode,
       "agentPvrstpAdminMode": agentPvrstpAdminMode,
       "agentPvrstpUplinkFast": agentPvrstpUplinkFast,
       "agentPvrstpBackboneFast": agentPvrstpBackboneFast,
       "agentPvrstpVlanTable": agentPvrstpVlanTable,
       "agentPvrstpVlanEntry": agentPvrstpVlanEntry,
       "agentPvrstpVlanTableIndex": agentPvrstpVlanTableIndex,
       "agentPvrstpVlanRootPriSec": agentPvrstpVlanRootPriSec,
       "agentPvrstpVlanHelloTime": agentPvrstpVlanHelloTime,
       "agentPvrstpVlanFwdDelayTime": agentPvrstpVlanFwdDelayTime,
       "agentPvrstpVlanMaxAgeTime": agentPvrstpVlanMaxAgeTime,
       "agentPvrstpPortVlanTable": agentPvrstpPortVlanTable,
       "agentPvrstpPortVlanEntry": agentPvrstpPortVlanEntry,
       "agentPvrstpPortIndex": agentPvrstpPortIndex,
       "agentPvrstpVlanIndex": agentPvrstpVlanIndex,
       "agentPvrstpPortVlanPriority": agentPvrstpPortVlanPriority,
       "agentPvrstpVlanCost": agentPvrstpVlanCost,
       "agentAuthenticationGroup": agentAuthenticationGroup,
       "agentAuthenticationListCreate": agentAuthenticationListCreate,
       "agentAuthenticationListTable": agentAuthenticationListTable,
       "agentAuthenticationListEntry": agentAuthenticationListEntry,
       "agentAuthenticationListIndex": agentAuthenticationListIndex,
       "agentAuthenticationListName": agentAuthenticationListName,
       "agentAuthenticationListMethod1": agentAuthenticationListMethod1,
       "agentAuthenticationListMethod2": agentAuthenticationListMethod2,
       "agentAuthenticationListMethod3": agentAuthenticationListMethod3,
       "agentAuthenticationListStatus": agentAuthenticationListStatus,
       "agentAuthenticationListMethod4": agentAuthenticationListMethod4,
       "agentAuthenticationListMethod5": agentAuthenticationListMethod5,
       "agentUserConfigDefaultAuthenticationList": agentUserConfigDefaultAuthenticationList,
       "agentUserAuthenticationConfigTable": agentUserAuthenticationConfigTable,
       "agentUserAuthenticationConfigEntry": agentUserAuthenticationConfigEntry,
       "agentUserAuthenticationList": agentUserAuthenticationList,
       "agentUserPortConfigTable": agentUserPortConfigTable,
       "agentUserPortConfigEntry": agentUserPortConfigEntry,
       "agentUserPortSecurity": agentUserPortSecurity,
       "agentClassOfServiceGroup": agentClassOfServiceGroup,
       "agentClassOfServicePortTable": agentClassOfServicePortTable,
       "agentClassOfServicePortEntry": agentClassOfServicePortEntry,
       "agentClassOfServicePortPriority": agentClassOfServicePortPriority,
       "agentClassOfServicePortClass": agentClassOfServicePortClass,
       "agentHTTPConfigGroup": agentHTTPConfigGroup,
       "agentHTTPWebMode": agentHTTPWebMode,
       "agentHTTPJavaMode": agentHTTPJavaMode,
       "agentHTTPMaxSessions": agentHTTPMaxSessions,
       "agentHTTPHardTimeout": agentHTTPHardTimeout,
       "agentHTTPSoftTimeout": agentHTTPSoftTimeout,
       "agentHTTPWebMgmtPortNum": agentHTTPWebMgmtPortNum,
       "agentAutoInstallConfigGroup": agentAutoInstallConfigGroup,
       "agentAutoinstallMode": agentAutoinstallMode,
       "agentAutoinstallAutosaveMode": agentAutoinstallAutosaveMode,
       "agentAutoinstallUnicastRetryCount": agentAutoinstallUnicastRetryCount,
       "agentAutoinstallStatus": agentAutoinstallStatus,
       "agentAutoinstallAutoRebootMode": agentAutoinstallAutoRebootMode,
       "agentAutoinstallOperationalMode": agentAutoinstallOperationalMode,
       "agentExecAccountingGroup": agentExecAccountingGroup,
       "agentExecAccountingListCreate": agentExecAccountingListCreate,
       "agentExecAccountingListTable": agentExecAccountingListTable,
       "agentExecAccountingListEntry": agentExecAccountingListEntry,
       "agentExecAccountingListIndex": agentExecAccountingListIndex,
       "agentExecAccountingListName": agentExecAccountingListName,
       "agentExecAccountingMethodType": agentExecAccountingMethodType,
       "agentExecAccountingListMethod1": agentExecAccountingListMethod1,
       "agentExecAccountingListMethod2": agentExecAccountingListMethod2,
       "agentExecAccountingListStatus": agentExecAccountingListStatus,
       "agentCmdsAccountingGroup": agentCmdsAccountingGroup,
       "agentCmdsAccountingListCreate": agentCmdsAccountingListCreate,
       "agentCmdsAccountingListTable": agentCmdsAccountingListTable,
       "agentCmdsAccountingListEntry": agentCmdsAccountingListEntry,
       "agentCmdsAccountingListIndex": agentCmdsAccountingListIndex,
       "agentCmdsAccountingListName": agentCmdsAccountingListName,
       "agentCmdsAccountingMethodType": agentCmdsAccountingMethodType,
       "agentCmdsAccountingListMethod1": agentCmdsAccountingListMethod1,
       "agentCmdsAccountingListStatus": agentCmdsAccountingListStatus,
       "agentCmdsAuthorizationGroup": agentCmdsAuthorizationGroup,
       "agentCmdsAuthorizationListCreate": agentCmdsAuthorizationListCreate,
       "agentCmdsAuthorizationListTable": agentCmdsAuthorizationListTable,
       "agentCmdsAuthorizationListEntry": agentCmdsAuthorizationListEntry,
       "agentCmdsAuthorizationListIndex": agentCmdsAuthorizationListIndex,
       "agentCmdsAuthorizationListName": agentCmdsAuthorizationListName,
       "agentCmdsAuthorizationListStatus": agentCmdsAuthorizationListStatus,
       "agentCmdsAuthorizationListMethod1": agentCmdsAuthorizationListMethod1,
       "agentCmdsAuthorizationListMethod2": agentCmdsAuthorizationListMethod2,
       "agentCmdsAuthorizationListMethod3": agentCmdsAuthorizationListMethod3,
       "agentExecAuthorizationGroup": agentExecAuthorizationGroup,
       "agentExecAuthorizationListCreate": agentExecAuthorizationListCreate,
       "agentExecAuthorizationListTable": agentExecAuthorizationListTable,
       "agentExecAuthorizationListEntry": agentExecAuthorizationListEntry,
       "agentExecAuthorizationListIndex": agentExecAuthorizationListIndex,
       "agentExecAuthorizationListName": agentExecAuthorizationListName,
       "agentExecAuthorizationListStatus": agentExecAuthorizationListStatus,
       "agentExecAuthorizationListMethod1": agentExecAuthorizationListMethod1,
       "agentExecAuthorizationListMethod2": agentExecAuthorizationListMethod2,
       "agentExecAuthorizationListMethod3": agentExecAuthorizationListMethod3,
       "agentExecAuthorizationListMethod4": agentExecAuthorizationListMethod4,
       "agentSwitchMbufConfigGroup": agentSwitchMbufConfigGroup,
       "agentSwitchMbufRisingThreshold": agentSwitchMbufRisingThreshold,
       "agentSwitchMbufFallingThreshold": agentSwitchMbufFallingThreshold,
       "agentSwitchMbufNotificationSeverity": agentSwitchMbufNotificationSeverity,
       "agentDigitalSignatureConfigGroup": agentDigitalSignatureConfigGroup,
       "agentDigitalSignatureVerifyMode": agentDigitalSignatureVerifyMode,
       "agentSystemGroup": agentSystemGroup,
       "agentSaveConfig": agentSaveConfig,
       "agentClearConfig": agentClearConfig,
       "agentClearLoginSessions": agentClearLoginSessions,
       "agentClearPasswords": agentClearPasswords,
       "agentClearPortStats": agentClearPortStats,
       "agentClearSwitchStats": agentClearSwitchStats,
       "agentClearTrapLog": agentClearTrapLog,
       "agentClearVlan": agentClearVlan,
       "agentResetSystem": agentResetSystem,
       "agentSaveConfigStatus": agentSaveConfigStatus,
       "agentStartupConfigErase": agentStartupConfigErase,
       "agentFactoryDefaultsErase": agentFactoryDefaultsErase,
       "agentCableTesterGroup": agentCableTesterGroup,
       "agentCableTesterStatus": agentCableTesterStatus,
       "agentCableTesterIfIndex": agentCableTesterIfIndex,
       "agentCableTesterCableStatus": agentCableTesterCableStatus,
       "agentCableTesterMinimumCableLength": agentCableTesterMinimumCableLength,
       "agentCableTesterMaximumCableLength": agentCableTesterMaximumCableLength,
       "agentCableTesterCableFailureLocation": agentCableTesterCableFailureLocation}
)
