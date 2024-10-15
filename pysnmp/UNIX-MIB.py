# SNMP MIB module (UNIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UNIX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:35 2024
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
 TimeTicks,
 Unsigned32,
 experimental,
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
    "experimental",
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

_Host_ObjectIdentity = ObjectIdentity
host = _Host_ObjectIdentity(
    (1, 3, 6, 1, 3, 999)
)
_Machine_ObjectIdentity = ObjectIdentity
machine = _Machine_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 1)
)
_MachineOsType_Type = OctetString
_MachineOsType_Object = MibScalar
machineOsType = _MachineOsType_Object(
    (1, 3, 6, 1, 3, 999, 1, 1),
    _MachineOsType_Type()
)
machineOsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineOsType.setStatus("mandatory")
_MachineName_Type = OctetString
_MachineName_Object = MibScalar
machineName = _MachineName_Object(
    (1, 3, 6, 1, 3, 999, 1, 2),
    _MachineName_Type()
)
machineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineName.setStatus("mandatory")
_MachineTime_Type = OctetString
_MachineTime_Object = MibScalar
machineTime = _MachineTime_Object(
    (1, 3, 6, 1, 3, 999, 1, 3),
    _MachineTime_Type()
)
machineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineTime.setStatus("mandatory")
_MachineOsVersion_Type = OctetString
_MachineOsVersion_Object = MibScalar
machineOsVersion = _MachineOsVersion_Object(
    (1, 3, 6, 1, 3, 999, 1, 4),
    _MachineOsVersion_Type()
)
machineOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineOsVersion.setStatus("mandatory")
_MachineBootRoot_Type = OctetString
_MachineBootRoot_Object = MibScalar
machineBootRoot = _MachineBootRoot_Object(
    (1, 3, 6, 1, 3, 999, 1, 5),
    _MachineBootRoot_Type()
)
machineBootRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineBootRoot.setStatus("mandatory")
_MachineBootTime_Type = OctetString
_MachineBootTime_Object = MibScalar
machineBootTime = _MachineBootTime_Object(
    (1, 3, 6, 1, 3, 999, 1, 6),
    _MachineBootTime_Type()
)
machineBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineBootTime.setStatus("mandatory")
_MachineHwModel_Type = OctetString
_MachineHwModel_Object = MibScalar
machineHwModel = _MachineHwModel_Object(
    (1, 3, 6, 1, 3, 999, 1, 7),
    _MachineHwModel_Type()
)
machineHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineHwModel.setStatus("mandatory")
_MachineHwType_Type = OctetString
_MachineHwType_Object = MibScalar
machineHwType = _MachineHwType_Object(
    (1, 3, 6, 1, 3, 999, 1, 8),
    _MachineHwType_Type()
)
machineHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineHwType.setStatus("mandatory")
_MachineHwVersion_Type = OctetString
_MachineHwVersion_Object = MibScalar
machineHwVersion = _MachineHwVersion_Object(
    (1, 3, 6, 1, 3, 999, 1, 9),
    _MachineHwVersion_Type()
)
machineHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineHwVersion.setStatus("mandatory")
_MachineVendor_Type = OctetString
_MachineVendor_Object = MibScalar
machineVendor = _MachineVendor_Object(
    (1, 3, 6, 1, 3, 999, 1, 10),
    _MachineVendor_Type()
)
machineVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineVendor.setStatus("mandatory")
_MachineMemorySize_Type = Integer32
_MachineMemorySize_Object = MibScalar
machineMemorySize = _MachineMemorySize_Object(
    (1, 3, 6, 1, 3, 999, 1, 10),
    _MachineMemorySize_Type()
)
machineMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineMemorySize.setStatus("mandatory")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 2)
)
_NetworkTable_Object = MibTable
networkTable = _NetworkTable_Object(
    (1, 3, 6, 1, 3, 999, 2)
)
if mibBuilder.loadTexts:
    networkTable.setStatus("mandatory")
_NetworkEntry_Object = MibTableRow
networkEntry = _NetworkEntry_Object(
    (1, 3, 6, 1, 3, 999, 2, 1)
)
networkEntry.setIndexNames(
    (0, "UNIX-MIB", "networkIndex"),
)
if mibBuilder.loadTexts:
    networkEntry.setStatus("mandatory")
_NetworkIndex_Type = OctetString
_NetworkIndex_Object = MibTableColumn
networkIndex = _NetworkIndex_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 1),
    _NetworkIndex_Type()
)
networkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIndex.setStatus("mandatory")
_NetworkAddress_Type = OctetString
_NetworkAddress_Object = MibTableColumn
networkAddress = _NetworkAddress_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 2),
    _NetworkAddress_Type()
)
networkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAddress.setStatus("mandatory")
_NetworkNodeName_Type = OctetString
_NetworkNodeName_Object = MibTableColumn
networkNodeName = _NetworkNodeName_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 3),
    _NetworkNodeName_Type()
)
networkNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkNodeName.setStatus("mandatory")
_NetworkType_Type = OctetString
_NetworkType_Object = MibTableColumn
networkType = _NetworkType_Object(
    (1, 3, 6, 1, 3, 999, 2, 1, 4),
    _NetworkType_Type()
)
networkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkType.setStatus("mandatory")
_Processor_ObjectIdentity = ObjectIdentity
processor = _Processor_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 3)
)
_ProcessorTable_Object = MibTable
processorTable = _ProcessorTable_Object(
    (1, 3, 6, 1, 3, 999, 3)
)
if mibBuilder.loadTexts:
    processorTable.setStatus("mandatory")
_ProcessorEntry_Object = MibTableRow
processorEntry = _ProcessorEntry_Object(
    (1, 3, 6, 1, 3, 999, 3, 1)
)
processorEntry.setIndexNames(
    (0, "UNIX-MIB", "processorIndex"),
)
if mibBuilder.loadTexts:
    processorEntry.setStatus("mandatory")
_ProcessorIndex_Type = OctetString
_ProcessorIndex_Object = MibTableColumn
processorIndex = _ProcessorIndex_Object(
    (1, 3, 6, 1, 3, 999, 3, 1, 1),
    _ProcessorIndex_Type()
)
processorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorIndex.setStatus("mandatory")
_ProcessorActiveState_Type = Integer32
_ProcessorActiveState_Object = MibTableColumn
processorActiveState = _ProcessorActiveState_Object(
    (1, 3, 6, 1, 3, 999, 3, 1, 2),
    _ProcessorActiveState_Type()
)
processorActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorActiveState.setStatus("mandatory")
_ProcessorPrimary_Type = OctetString
_ProcessorPrimary_Object = MibTableColumn
processorPrimary = _ProcessorPrimary_Object(
    (1, 3, 6, 1, 3, 999, 3, 1, 3),
    _ProcessorPrimary_Type()
)
processorPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPrimary.setStatus("mandatory")
_Adapter_ObjectIdentity = ObjectIdentity
adapter = _Adapter_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 4)
)
_AdapterTable_Object = MibTable
adapterTable = _AdapterTable_Object(
    (1, 3, 6, 1, 3, 999, 4)
)
if mibBuilder.loadTexts:
    adapterTable.setStatus("mandatory")
_AdapterEntry_Object = MibTableRow
adapterEntry = _AdapterEntry_Object(
    (1, 3, 6, 1, 3, 999, 4, 1)
)
adapterEntry.setIndexNames(
    (0, "UNIX-MIB", "adapterIndex"),
)
if mibBuilder.loadTexts:
    adapterEntry.setStatus("mandatory")
_AdapterIndex_Type = Integer32
_AdapterIndex_Object = MibTableColumn
adapterIndex = _AdapterIndex_Object(
    (1, 3, 6, 1, 3, 999, 4, 1, 1),
    _AdapterIndex_Type()
)
adapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterIndex.setStatus("mandatory")
_AdapterName_Type = OctetString
_AdapterName_Object = MibTableColumn
adapterName = _AdapterName_Object(
    (1, 3, 6, 1, 3, 999, 4, 1, 2),
    _AdapterName_Type()
)
adapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterName.setStatus("mandatory")
_AdapterType_Type = OctetString
_AdapterType_Object = MibScalar
adapterType = _AdapterType_Object(
    (1, 3, 6, 1, 3, 999, 4, 1, 3),
    _AdapterType_Type()
)
adapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterType.setStatus("mandatory")
_AdapterUnitNumber_Type = Integer32
_AdapterUnitNumber_Object = MibTableColumn
adapterUnitNumber = _AdapterUnitNumber_Object(
    (1, 3, 6, 1, 3, 999, 4, 1, 4),
    _AdapterUnitNumber_Type()
)
adapterUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterUnitNumber.setStatus("mandatory")
_AdapterNexusNumber_Type = Integer32
_AdapterNexusNumber_Object = MibTableColumn
adapterNexusNumber = _AdapterNexusNumber_Object(
    (1, 3, 6, 1, 3, 999, 4, 1, 5),
    _AdapterNexusNumber_Type()
)
adapterNexusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNexusNumber.setStatus("mandatory")
_AdapterRevLevel_Type = OctetString
_AdapterRevLevel_Object = MibTableColumn
adapterRevLevel = _AdapterRevLevel_Object(
    (1, 3, 6, 1, 3, 999, 4, 1, 5),
    _AdapterRevLevel_Type()
)
adapterRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRevLevel.setStatus("mandatory")
_Controller_ObjectIdentity = ObjectIdentity
controller = _Controller_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 5)
)
_ControllerTable_Object = MibTable
controllerTable = _ControllerTable_Object(
    (1, 3, 6, 1, 3, 999, 5)
)
if mibBuilder.loadTexts:
    controllerTable.setStatus("mandatory")
_ControllerEntry_Object = MibTableRow
controllerEntry = _ControllerEntry_Object(
    (1, 3, 6, 1, 3, 999, 5, 1)
)
controllerEntry.setIndexNames(
    (0, "UNIX-MIB", "controllerIndex"),
)
if mibBuilder.loadTexts:
    controllerEntry.setStatus("mandatory")
_ControllerIndex_Type = Integer32
_ControllerIndex_Object = MibTableColumn
controllerIndex = _ControllerIndex_Object(
    (1, 3, 6, 1, 3, 999, 5, 1, 1),
    _ControllerIndex_Type()
)
controllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerIndex.setStatus("mandatory")
_ControllerName_Type = OctetString
_ControllerName_Object = MibTableColumn
controllerName = _ControllerName_Object(
    (1, 3, 6, 1, 3, 999, 5, 1, 2),
    _ControllerName_Type()
)
controllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerName.setStatus("mandatory")
_ControllerType_Type = OctetString
_ControllerType_Object = MibTableColumn
controllerType = _ControllerType_Object(
    (1, 3, 6, 1, 3, 999, 5, 1, 3),
    _ControllerType_Type()
)
controllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerType.setStatus("mandatory")
_ControllerUnitNumber_Type = Integer32
_ControllerUnitNumber_Object = MibTableColumn
controllerUnitNumber = _ControllerUnitNumber_Object(
    (1, 3, 6, 1, 3, 999, 5, 1, 4),
    _ControllerUnitNumber_Type()
)
controllerUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerUnitNumber.setStatus("mandatory")
_Printer_ObjectIdentity = ObjectIdentity
printer = _Printer_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 6)
)
_PrinterTable_Object = MibTable
printerTable = _PrinterTable_Object(
    (1, 3, 6, 1, 3, 999, 6)
)
if mibBuilder.loadTexts:
    printerTable.setStatus("mandatory")
_PrinterEntry_Object = MibTableRow
printerEntry = _PrinterEntry_Object(
    (1, 3, 6, 1, 3, 999, 6, 1)
)
printerEntry.setIndexNames(
    (0, "UNIX-MIB", "printerIndex"),
)
if mibBuilder.loadTexts:
    printerEntry.setStatus("mandatory")
_PrinterIndex_Type = Integer32
_PrinterIndex_Object = MibTableColumn
printerIndex = _PrinterIndex_Object(
    (1, 3, 6, 1, 3, 999, 6, 1, 1),
    _PrinterIndex_Type()
)
printerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printerIndex.setStatus("mandatory")
_PrinterName_Type = OctetString
_PrinterName_Object = MibTableColumn
printerName = _PrinterName_Object(
    (1, 3, 6, 1, 3, 999, 6, 1, 2),
    _PrinterName_Type()
)
printerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printerName.setStatus("mandatory")
_PrinterQueue_Type = OctetString
_PrinterQueue_Object = MibTableColumn
printerQueue = _PrinterQueue_Object(
    (1, 3, 6, 1, 3, 999, 6, 1, 3),
    _PrinterQueue_Type()
)
printerQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printerQueue.setStatus("mandatory")
_PrinterDeviceDriver_Type = OctetString
_PrinterDeviceDriver_Object = MibTableColumn
printerDeviceDriver = _PrinterDeviceDriver_Object(
    (1, 3, 6, 1, 3, 999, 6, 1, 4),
    _PrinterDeviceDriver_Type()
)
printerDeviceDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printerDeviceDriver.setStatus("mandatory")
_PrinterDeviceType_Type = OctetString
_PrinterDeviceType_Object = MibTableColumn
printerDeviceType = _PrinterDeviceType_Object(
    (1, 3, 6, 1, 3, 999, 6, 1, 5),
    _PrinterDeviceType_Type()
)
printerDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printerDeviceType.setStatus("mandatory")
_PrinterUnitNumber_Type = Integer32
_PrinterUnitNumber_Object = MibTableColumn
printerUnitNumber = _PrinterUnitNumber_Object(
    (1, 3, 6, 1, 3, 999, 6, 1, 6),
    _PrinterUnitNumber_Type()
)
printerUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printerUnitNumber.setStatus("mandatory")
_Disk_ObjectIdentity = ObjectIdentity
disk = _Disk_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 7)
)
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 3, 999, 7)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("mandatory")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 3, 999, 7, 1)
)
diskEntry.setIndexNames(
    (0, "UNIX-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("mandatory")
_DiskIndex_Type = Integer32
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 3, 999, 7, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIndex.setStatus("mandatory")
_DiskDeviceName_Type = OctetString
_DiskDeviceName_Object = MibTableColumn
diskDeviceName = _DiskDeviceName_Object(
    (1, 3, 6, 1, 3, 999, 7, 1, 2),
    _DiskDeviceName_Type()
)
diskDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDeviceName.setStatus("mandatory")
_DiskPrimaryHost_Type = OctetString
_DiskPrimaryHost_Object = MibTableColumn
diskPrimaryHost = _DiskPrimaryHost_Object(
    (1, 3, 6, 1, 3, 999, 7, 1, 3),
    _DiskPrimaryHost_Type()
)
diskPrimaryHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPrimaryHost.setStatus("mandatory")
_DiskUnitNumber_Type = Integer32
_DiskUnitNumber_Object = MibTableColumn
diskUnitNumber = _DiskUnitNumber_Object(
    (1, 3, 6, 1, 3, 999, 7, 1, 4),
    _DiskUnitNumber_Type()
)
diskUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskUnitNumber.setStatus("mandatory")
_DiskDeviceDriver_Type = OctetString
_DiskDeviceDriver_Object = MibTableColumn
diskDeviceDriver = _DiskDeviceDriver_Object(
    (1, 3, 6, 1, 3, 999, 7, 1, 5),
    _DiskDeviceDriver_Type()
)
diskDeviceDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDeviceDriver.setStatus("mandatory")
_DiskDeviceType_Type = OctetString
_DiskDeviceType_Object = MibTableColumn
diskDeviceType = _DiskDeviceType_Object(
    (1, 3, 6, 1, 3, 999, 7, 1, 6),
    _DiskDeviceType_Type()
)
diskDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDeviceType.setStatus("mandatory")
_DiskPhysicalCapacity_Type = Integer32
_DiskPhysicalCapacity_Object = MibTableColumn
diskPhysicalCapacity = _DiskPhysicalCapacity_Object(
    (1, 3, 6, 1, 3, 999, 7, 1, 7),
    _DiskPhysicalCapacity_Type()
)
diskPhysicalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPhysicalCapacity.setStatus("mandatory")
_DiskPartition_ObjectIdentity = ObjectIdentity
diskPartition = _DiskPartition_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 8)
)
_DiskPartitionTable_Object = MibTable
diskPartitionTable = _DiskPartitionTable_Object(
    (1, 3, 6, 1, 3, 999, 8)
)
if mibBuilder.loadTexts:
    diskPartitionTable.setStatus("mandatory")
_DiskPartitionEntry_Object = MibTableRow
diskPartitionEntry = _DiskPartitionEntry_Object(
    (1, 3, 6, 1, 3, 999, 8, 1)
)
diskPartitionEntry.setIndexNames(
    (0, "UNIX-MIB", "diskPartitionIndex"),
)
if mibBuilder.loadTexts:
    diskPartitionEntry.setStatus("mandatory")
_DiskPartitionIndex_Type = Integer32
_DiskPartitionIndex_Object = MibScalar
diskPartitionIndex = _DiskPartitionIndex_Object(
    (1, 3, 6, 1, 3, 999, 8, 1, 1),
    _DiskPartitionIndex_Type()
)
diskPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPartitionIndex.setStatus("mandatory")
_DiskPartitionName_Type = OctetString
_DiskPartitionName_Object = MibTableColumn
diskPartitionName = _DiskPartitionName_Object(
    (1, 3, 6, 1, 3, 999, 8, 1, 2),
    _DiskPartitionName_Type()
)
diskPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPartitionName.setStatus("mandatory")
_DiskPartitionPrimaryHost_Type = OctetString
_DiskPartitionPrimaryHost_Object = MibTableColumn
diskPartitionPrimaryHost = _DiskPartitionPrimaryHost_Object(
    (1, 3, 6, 1, 3, 999, 8, 1, 3),
    _DiskPartitionPrimaryHost_Type()
)
diskPartitionPrimaryHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPartitionPrimaryHost.setStatus("mandatory")
_DiskPartitionSize_Type = Integer32
_DiskPartitionSize_Object = MibScalar
diskPartitionSize = _DiskPartitionSize_Object(
    (1, 3, 6, 1, 3, 999, 8, 1, 4),
    _DiskPartitionSize_Type()
)
diskPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPartitionSize.setStatus("mandatory")
_DiskPartitionDeviceName_Type = OctetString
_DiskPartitionDeviceName_Object = MibScalar
diskPartitionDeviceName = _DiskPartitionDeviceName_Object(
    (1, 3, 6, 1, 3, 999, 8, 1, 5),
    _DiskPartitionDeviceName_Type()
)
diskPartitionDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPartitionDeviceName.setStatus("mandatory")
_DiskPartitionStartSector_Type = Integer32
_DiskPartitionStartSector_Object = MibTableColumn
diskPartitionStartSector = _DiskPartitionStartSector_Object(
    (1, 3, 6, 1, 3, 999, 8, 1, 6),
    _DiskPartitionStartSector_Type()
)
diskPartitionStartSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPartitionStartSector.setStatus("mandatory")
_DiskPartitionEndSector_Type = Integer32
_DiskPartitionEndSector_Object = MibTableColumn
diskPartitionEndSector = _DiskPartitionEndSector_Object(
    (1, 3, 6, 1, 3, 999, 8, 1, 7),
    _DiskPartitionEndSector_Type()
)
diskPartitionEndSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPartitionEndSector.setStatus("mandatory")
_Tape_ObjectIdentity = ObjectIdentity
tape = _Tape_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 9)
)
_TapeTable_Object = MibTable
tapeTable = _TapeTable_Object(
    (1, 3, 6, 1, 3, 999, 9)
)
if mibBuilder.loadTexts:
    tapeTable.setStatus("mandatory")
_TapeEntry_Object = MibTableRow
tapeEntry = _TapeEntry_Object(
    (1, 3, 6, 1, 3, 999, 9, 1)
)
tapeEntry.setIndexNames(
    (0, "UNIX-MIB", "tapeIndex"),
)
if mibBuilder.loadTexts:
    tapeEntry.setStatus("mandatory")
_TapeIndex_Type = OctetString
_TapeIndex_Object = MibTableColumn
tapeIndex = _TapeIndex_Object(
    (1, 3, 6, 1, 3, 999, 9, 1, 1),
    _TapeIndex_Type()
)
tapeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeIndex.setStatus("mandatory")
_TapeDeviceName_Type = OctetString
_TapeDeviceName_Object = MibTableColumn
tapeDeviceName = _TapeDeviceName_Object(
    (1, 3, 6, 1, 3, 999, 9, 1, 2),
    _TapeDeviceName_Type()
)
tapeDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDeviceName.setStatus("mandatory")
_TapeTapeUnitNumber_Type = Integer32
_TapeTapeUnitNumber_Object = MibScalar
tapeTapeUnitNumber = _TapeTapeUnitNumber_Object(
    (1, 3, 6, 1, 3, 999, 9, 1, 4),
    _TapeTapeUnitNumber_Type()
)
tapeTapeUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeTapeUnitNumber.setStatus("mandatory")
_TapeDeviceDriver_Type = OctetString
_TapeDeviceDriver_Object = MibTableColumn
tapeDeviceDriver = _TapeDeviceDriver_Object(
    (1, 3, 6, 1, 3, 999, 9, 1, 5),
    _TapeDeviceDriver_Type()
)
tapeDeviceDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDeviceDriver.setStatus("mandatory")
_TapeDeviceType_Type = OctetString
_TapeDeviceType_Object = MibTableColumn
tapeDeviceType = _TapeDeviceType_Object(
    (1, 3, 6, 1, 3, 999, 9, 1, 6),
    _TapeDeviceType_Type()
)
tapeDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeDeviceType.setStatus("mandatory")
_TapeMountPoint_Type = OctetString
_TapeMountPoint_Object = MibTableColumn
tapeMountPoint = _TapeMountPoint_Object(
    (1, 3, 6, 1, 3, 999, 9, 1, 7),
    _TapeMountPoint_Type()
)
tapeMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeMountPoint.setStatus("mandatory")
_Queue_ObjectIdentity = ObjectIdentity
queue = _Queue_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 10)
)
_QueueTable_Object = MibTable
queueTable = _QueueTable_Object(
    (1, 3, 6, 1, 3, 999, 10)
)
if mibBuilder.loadTexts:
    queueTable.setStatus("mandatory")
_QueueEntry_Object = MibTableRow
queueEntry = _QueueEntry_Object(
    (1, 3, 6, 1, 3, 999, 10, 1)
)
queueEntry.setIndexNames(
    (0, "UNIX-MIB", "queueIndex"),
)
if mibBuilder.loadTexts:
    queueEntry.setStatus("mandatory")
_QueueIndex_Type = Integer32
_QueueIndex_Object = MibTableColumn
queueIndex = _QueueIndex_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 1),
    _QueueIndex_Type()
)
queueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueIndex.setStatus("mandatory")
_QueueName_Type = OctetString
_QueueName_Object = MibTableColumn
queueName = _QueueName_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 2),
    _QueueName_Type()
)
queueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueName.setStatus("mandatory")
_QueueType_Type = OctetString
_QueueType_Object = MibTableColumn
queueType = _QueueType_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 3),
    _QueueType_Type()
)
queueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueType.setStatus("mandatory")
_QueueState_Type = Integer32
_QueueState_Object = MibTableColumn
queueState = _QueueState_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 4),
    _QueueState_Type()
)
queueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueState.setStatus("mandatory")
_QueueDestinationList_Type = OctetString
_QueueDestinationList_Object = MibTableColumn
queueDestinationList = _QueueDestinationList_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 5),
    _QueueDestinationList_Type()
)
queueDestinationList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueDestinationList.setStatus("mandatory")
_QueueCapacity_Type = OctetString
_QueueCapacity_Object = MibTableColumn
queueCapacity = _QueueCapacity_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 6),
    _QueueCapacity_Type()
)
queueCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueCapacity.setStatus("mandatory")
_QueuePriority_Type = OctetString
_QueuePriority_Object = MibTableColumn
queuePriority = _QueuePriority_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 7),
    _QueuePriority_Type()
)
queuePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePriority.setStatus("mandatory")
_QueueProtection_Type = Integer32
_QueueProtection_Object = MibTableColumn
queueProtection = _QueueProtection_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 8),
    _QueueProtection_Type()
)
queueProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueProtection.setStatus("mandatory")
_QueueUserComment_Type = OctetString
_QueueUserComment_Object = MibTableColumn
queueUserComment = _QueueUserComment_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 9),
    _QueueUserComment_Type()
)
queueUserComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueUserComment.setStatus("mandatory")
_QueuePrintServer_Type = OctetString
_QueuePrintServer_Object = MibTableColumn
queuePrintServer = _QueuePrintServer_Object(
    (1, 3, 6, 1, 3, 999, 10, 1, 10),
    _QueuePrintServer_Type()
)
queuePrintServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePrintServer.setStatus("mandatory")
_Group_ObjectIdentity = ObjectIdentity
group = _Group_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 11)
)
_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 3, 999, 11)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("mandatory")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 3, 999, 11, 1)
)
groupEntry.setIndexNames(
    (0, "UNIX-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("mandatory")
_GroupIndex_Type = OctetString
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 3, 999, 11, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupIndex.setStatus("mandatory")
_GroupId_Type = OctetString
_GroupId_Object = MibTableColumn
groupId = _GroupId_Object(
    (1, 3, 6, 1, 3, 999, 11, 1, 2),
    _GroupId_Type()
)
groupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupId.setStatus("mandatory")
_GroupName_Type = OctetString
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 3, 999, 11, 1, 3),
    _GroupName_Type()
)
groupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupName.setStatus("mandatory")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 12)
)
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 3, 999, 12)
)
if mibBuilder.loadTexts:
    userTable.setStatus("mandatory")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 3, 999, 12, 1)
)
userEntry.setIndexNames(
    (0, "UNIX-MIB", "userIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("mandatory")
_UserIndex_Type = Integer32
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 3, 999, 12, 1, 1),
    _UserIndex_Type()
)
userIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userIndex.setStatus("mandatory")
_UserName_Type = OctetString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 3, 999, 12, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")
_UserId_Type = OctetString
_UserId_Object = MibTableColumn
userId = _UserId_Object(
    (1, 3, 6, 1, 3, 999, 12, 1, 3),
    _UserId_Type()
)
userId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userId.setStatus("mandatory")
_UserFullName_Type = OctetString
_UserFullName_Object = MibTableColumn
userFullName = _UserFullName_Object(
    (1, 3, 6, 1, 3, 999, 12, 1, 4),
    _UserFullName_Type()
)
userFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userFullName.setStatus("mandatory")
_UserLoginShellCli_Type = OctetString
_UserLoginShellCli_Object = MibTableColumn
userLoginShellCli = _UserLoginShellCli_Object(
    (1, 3, 6, 1, 3, 999, 12, 1, 5),
    _UserLoginShellCli_Type()
)
userLoginShellCli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLoginShellCli.setStatus("mandatory")
_UserLoginDirectory_Type = OctetString
_UserLoginDirectory_Object = MibTableColumn
userLoginDirectory = _UserLoginDirectory_Object(
    (1, 3, 6, 1, 3, 999, 12, 1, 6),
    _UserLoginDirectory_Type()
)
userLoginDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLoginDirectory.setStatus("mandatory")
_Installedsw_ObjectIdentity = ObjectIdentity
installedsw = _Installedsw_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 13)
)
_InstalledSwTable_Object = MibTable
installedSwTable = _InstalledSwTable_Object(
    (1, 3, 6, 1, 3, 999, 13)
)
if mibBuilder.loadTexts:
    installedSwTable.setStatus("mandatory")
_InstalledSwEntry_Object = MibTableRow
installedSwEntry = _InstalledSwEntry_Object(
    (1, 3, 6, 1, 3, 999, 13, 1)
)
installedSwEntry.setIndexNames(
    (0, "UNIX-MIB", "installedSwIndex"),
)
if mibBuilder.loadTexts:
    installedSwEntry.setStatus("mandatory")
_InstalledSwIndex_Type = OctetString
_InstalledSwIndex_Object = MibTableColumn
installedSwIndex = _InstalledSwIndex_Object(
    (1, 3, 6, 1, 3, 999, 13, 1, 1),
    _InstalledSwIndex_Type()
)
installedSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedSwIndex.setStatus("mandatory")
_InstalledSwName_Type = OctetString
_InstalledSwName_Object = MibTableColumn
installedSwName = _InstalledSwName_Object(
    (1, 3, 6, 1, 3, 999, 13, 1, 2),
    _InstalledSwName_Type()
)
installedSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedSwName.setStatus("mandatory")
_InstalledSwVendorAuthor_Type = OctetString
_InstalledSwVendorAuthor_Object = MibTableColumn
installedSwVendorAuthor = _InstalledSwVendorAuthor_Object(
    (1, 3, 6, 1, 3, 999, 13, 1, 3),
    _InstalledSwVendorAuthor_Type()
)
installedSwVendorAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedSwVendorAuthor.setStatus("mandatory")
_InstalledSwVersion_Type = OctetString
_InstalledSwVersion_Object = MibTableColumn
installedSwVersion = _InstalledSwVersion_Object(
    (1, 3, 6, 1, 3, 999, 13, 1, 4),
    _InstalledSwVersion_Type()
)
installedSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedSwVersion.setStatus("mandatory")
_InstalledSwVendorPatches_Type = OctetString
_InstalledSwVendorPatches_Object = MibTableColumn
installedSwVendorPatches = _InstalledSwVendorPatches_Object(
    (1, 3, 6, 1, 3, 999, 13, 1, 5),
    _InstalledSwVendorPatches_Type()
)
installedSwVendorPatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedSwVendorPatches.setStatus("mandatory")
_InstalledSwUserPatches_Type = OctetString
_InstalledSwUserPatches_Object = MibTableColumn
installedSwUserPatches = _InstalledSwUserPatches_Object(
    (1, 3, 6, 1, 3, 999, 13, 1, 6),
    _InstalledSwUserPatches_Type()
)
installedSwUserPatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedSwUserPatches.setStatus("mandatory")
_InstalledSwLicInstalled_Type = OctetString
_InstalledSwLicInstalled_Object = MibTableColumn
installedSwLicInstalled = _InstalledSwLicInstalled_Object(
    (1, 3, 6, 1, 3, 999, 13, 1, 7),
    _InstalledSwLicInstalled_Type()
)
installedSwLicInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedSwLicInstalled.setStatus("mandatory")
_License_ObjectIdentity = ObjectIdentity
license = _License_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 14)
)
_LicenseTable_Object = MibTable
licenseTable = _LicenseTable_Object(
    (1, 3, 6, 1, 3, 999, 14)
)
if mibBuilder.loadTexts:
    licenseTable.setStatus("mandatory")
_LicenseEntry_Object = MibTableRow
licenseEntry = _LicenseEntry_Object(
    (1, 3, 6, 1, 3, 999, 14, 1)
)
licenseEntry.setIndexNames(
    (0, "UNIX-MIB", "licenseIndex"),
)
if mibBuilder.loadTexts:
    licenseEntry.setStatus("mandatory")
_LicenseIndex_Type = OctetString
_LicenseIndex_Object = MibTableColumn
licenseIndex = _LicenseIndex_Object(
    (1, 3, 6, 1, 3, 999, 14, 1, 1),
    _LicenseIndex_Type()
)
licenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIndex.setStatus("mandatory")
_LicenseProductName_Type = OctetString
_LicenseProductName_Object = MibScalar
licenseProductName = _LicenseProductName_Object(
    (1, 3, 6, 1, 3, 999, 14, 1, 2),
    _LicenseProductName_Type()
)
licenseProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseProductName.setStatus("mandatory")
_LicenseVendorAuthor_Type = OctetString
_LicenseVendorAuthor_Object = MibTableColumn
licenseVendorAuthor = _LicenseVendorAuthor_Object(
    (1, 3, 6, 1, 3, 999, 14, 1, 3),
    _LicenseVendorAuthor_Type()
)
licenseVendorAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseVendorAuthor.setStatus("mandatory")
_LicenseExpirationDate_Type = OctetString
_LicenseExpirationDate_Object = MibTableColumn
licenseExpirationDate = _LicenseExpirationDate_Object(
    (1, 3, 6, 1, 3, 999, 14, 1, 4),
    _LicenseExpirationDate_Type()
)
licenseExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpirationDate.setStatus("mandatory")
_LicenseVersion_Type = OctetString
_LicenseVersion_Object = MibTableColumn
licenseVersion = _LicenseVersion_Object(
    (1, 3, 6, 1, 3, 999, 14, 1, 5),
    _LicenseVersion_Type()
)
licenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseVersion.setStatus("mandatory")
_LicenseCapacity_Type = OctetString
_LicenseCapacity_Object = MibTableColumn
licenseCapacity = _LicenseCapacity_Object(
    (1, 3, 6, 1, 3, 999, 14, 1, 6),
    _LicenseCapacity_Type()
)
licenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseCapacity.setStatus("mandatory")
_LicenseAuthorization_Type = OctetString
_LicenseAuthorization_Object = MibTableColumn
licenseAuthorization = _LicenseAuthorization_Object(
    (1, 3, 6, 1, 3, 999, 14, 1, 7),
    _LicenseAuthorization_Type()
)
licenseAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseAuthorization.setStatus("mandatory")
_Filesystem_ObjectIdentity = ObjectIdentity
filesystem = _Filesystem_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 15)
)
_FilesystemTable_Object = MibTable
filesystemTable = _FilesystemTable_Object(
    (1, 3, 6, 1, 3, 999, 15)
)
if mibBuilder.loadTexts:
    filesystemTable.setStatus("mandatory")
_FilesystemEntry_Object = MibTableRow
filesystemEntry = _FilesystemEntry_Object(
    (1, 3, 6, 1, 3, 999, 15, 1)
)
filesystemEntry.setIndexNames(
    (0, "UNIX-MIB", "filesystemIndex"),
)
if mibBuilder.loadTexts:
    filesystemEntry.setStatus("mandatory")
_FilesystemIndex_Type = Integer32
_FilesystemIndex_Object = MibTableColumn
filesystemIndex = _FilesystemIndex_Object(
    (1, 3, 6, 1, 3, 999, 15, 1, 1),
    _FilesystemIndex_Type()
)
filesystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesystemIndex.setStatus("mandatory")
_FilesystemName_Type = OctetString
_FilesystemName_Object = MibTableColumn
filesystemName = _FilesystemName_Object(
    (1, 3, 6, 1, 3, 999, 15, 1, 2),
    _FilesystemName_Type()
)
filesystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesystemName.setStatus("mandatory")
_FilesystemFreeCapacity_Type = OctetString
_FilesystemFreeCapacity_Object = MibTableColumn
filesystemFreeCapacity = _FilesystemFreeCapacity_Object(
    (1, 3, 6, 1, 3, 999, 15, 1, 3),
    _FilesystemFreeCapacity_Type()
)
filesystemFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesystemFreeCapacity.setStatus("mandatory")
_FilesystemFormattedCap_Type = Integer32
_FilesystemFormattedCap_Object = MibTableColumn
filesystemFormattedCap = _FilesystemFormattedCap_Object(
    (1, 3, 6, 1, 3, 999, 15, 1, 4),
    _FilesystemFormattedCap_Type()
)
filesystemFormattedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesystemFormattedCap.setStatus("mandatory")
_Mountinfo_ObjectIdentity = ObjectIdentity
mountinfo = _Mountinfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 16)
)
_MountInfoTable_Object = MibTable
mountInfoTable = _MountInfoTable_Object(
    (1, 3, 6, 1, 3, 999, 16)
)
if mibBuilder.loadTexts:
    mountInfoTable.setStatus("mandatory")
_MountInfoEntry_Object = MibTableRow
mountInfoEntry = _MountInfoEntry_Object(
    (1, 3, 6, 1, 3, 999, 16, 1)
)
mountInfoEntry.setIndexNames(
    (0, "UNIX-MIB", "mountInfoIndex"),
)
if mibBuilder.loadTexts:
    mountInfoEntry.setStatus("mandatory")
_MountInfoIndex_Type = Integer32
_MountInfoIndex_Object = MibTableColumn
mountInfoIndex = _MountInfoIndex_Object(
    (1, 3, 6, 1, 3, 999, 16, 1, 1),
    _MountInfoIndex_Type()
)
mountInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInfoIndex.setStatus("mandatory")
_MountInfoFileSystemName_Type = OctetString
_MountInfoFileSystemName_Object = MibScalar
mountInfoFileSystemName = _MountInfoFileSystemName_Object(
    (1, 3, 6, 1, 3, 999, 16, 1, 2),
    _MountInfoFileSystemName_Type()
)
mountInfoFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInfoFileSystemName.setStatus("mandatory")
_MountInfoDeviceName_Type = OctetString
_MountInfoDeviceName_Object = MibTableColumn
mountInfoDeviceName = _MountInfoDeviceName_Object(
    (1, 3, 6, 1, 3, 999, 16, 1, 3),
    _MountInfoDeviceName_Type()
)
mountInfoDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInfoDeviceName.setStatus("mandatory")
_MountInfoMountPoint_Type = OctetString
_MountInfoMountPoint_Object = MibTableColumn
mountInfoMountPoint = _MountInfoMountPoint_Object(
    (1, 3, 6, 1, 3, 999, 16, 1, 4),
    _MountInfoMountPoint_Type()
)
mountInfoMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInfoMountPoint.setStatus("mandatory")
_MountInfoMountType_Type = OctetString
_MountInfoMountType_Object = MibTableColumn
mountInfoMountType = _MountInfoMountType_Object(
    (1, 3, 6, 1, 3, 999, 16, 1, 4),
    _MountInfoMountType_Type()
)
mountInfoMountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInfoMountType.setStatus("mandatory")
_MountInfoRelVolNum_Type = Integer32
_MountInfoRelVolNum_Object = MibTableColumn
mountInfoRelVolNum = _MountInfoRelVolNum_Object(
    (1, 3, 6, 1, 3, 999, 16, 1, 6),
    _MountInfoRelVolNum_Type()
)
mountInfoRelVolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInfoRelVolNum.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UNIX-MIB",
    **{"host": host,
       "machine": machine,
       "machineOsType": machineOsType,
       "machineName": machineName,
       "machineTime": machineTime,
       "machineOsVersion": machineOsVersion,
       "machineBootRoot": machineBootRoot,
       "machineBootTime": machineBootTime,
       "machineHwModel": machineHwModel,
       "machineHwType": machineHwType,
       "machineHwVersion": machineHwVersion,
       "machineVendor": machineVendor,
       "machineMemorySize": machineMemorySize,
       "network": network,
       "networkTable": networkTable,
       "networkEntry": networkEntry,
       "networkIndex": networkIndex,
       "networkAddress": networkAddress,
       "networkNodeName": networkNodeName,
       "networkType": networkType,
       "processor": processor,
       "processorTable": processorTable,
       "processorEntry": processorEntry,
       "processorIndex": processorIndex,
       "processorActiveState": processorActiveState,
       "processorPrimary": processorPrimary,
       "adapter": adapter,
       "adapterTable": adapterTable,
       "adapterEntry": adapterEntry,
       "adapterIndex": adapterIndex,
       "adapterName": adapterName,
       "adapterType": adapterType,
       "adapterUnitNumber": adapterUnitNumber,
       "adapterNexusNumber": adapterNexusNumber,
       "adapterRevLevel": adapterRevLevel,
       "controller": controller,
       "controllerTable": controllerTable,
       "controllerEntry": controllerEntry,
       "controllerIndex": controllerIndex,
       "controllerName": controllerName,
       "controllerType": controllerType,
       "controllerUnitNumber": controllerUnitNumber,
       "printer": printer,
       "printerTable": printerTable,
       "printerEntry": printerEntry,
       "printerIndex": printerIndex,
       "printerName": printerName,
       "printerQueue": printerQueue,
       "printerDeviceDriver": printerDeviceDriver,
       "printerDeviceType": printerDeviceType,
       "printerUnitNumber": printerUnitNumber,
       "disk": disk,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskIndex": diskIndex,
       "diskDeviceName": diskDeviceName,
       "diskPrimaryHost": diskPrimaryHost,
       "diskUnitNumber": diskUnitNumber,
       "diskDeviceDriver": diskDeviceDriver,
       "diskDeviceType": diskDeviceType,
       "diskPhysicalCapacity": diskPhysicalCapacity,
       "diskPartition": diskPartition,
       "diskPartitionTable": diskPartitionTable,
       "diskPartitionEntry": diskPartitionEntry,
       "diskPartitionIndex": diskPartitionIndex,
       "diskPartitionName": diskPartitionName,
       "diskPartitionPrimaryHost": diskPartitionPrimaryHost,
       "diskPartitionSize": diskPartitionSize,
       "diskPartitionDeviceName": diskPartitionDeviceName,
       "diskPartitionStartSector": diskPartitionStartSector,
       "diskPartitionEndSector": diskPartitionEndSector,
       "tape": tape,
       "tapeTable": tapeTable,
       "tapeEntry": tapeEntry,
       "tapeIndex": tapeIndex,
       "tapeDeviceName": tapeDeviceName,
       "tapeTapeUnitNumber": tapeTapeUnitNumber,
       "tapeDeviceDriver": tapeDeviceDriver,
       "tapeDeviceType": tapeDeviceType,
       "tapeMountPoint": tapeMountPoint,
       "queue": queue,
       "queueTable": queueTable,
       "queueEntry": queueEntry,
       "queueIndex": queueIndex,
       "queueName": queueName,
       "queueType": queueType,
       "queueState": queueState,
       "queueDestinationList": queueDestinationList,
       "queueCapacity": queueCapacity,
       "queuePriority": queuePriority,
       "queueProtection": queueProtection,
       "queueUserComment": queueUserComment,
       "queuePrintServer": queuePrintServer,
       "group": group,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupIndex": groupIndex,
       "groupId": groupId,
       "groupName": groupName,
       "user": user,
       "userTable": userTable,
       "userEntry": userEntry,
       "userIndex": userIndex,
       "userName": userName,
       "userId": userId,
       "userFullName": userFullName,
       "userLoginShellCli": userLoginShellCli,
       "userLoginDirectory": userLoginDirectory,
       "installedsw": installedsw,
       "installedSwTable": installedSwTable,
       "installedSwEntry": installedSwEntry,
       "installedSwIndex": installedSwIndex,
       "installedSwName": installedSwName,
       "installedSwVendorAuthor": installedSwVendorAuthor,
       "installedSwVersion": installedSwVersion,
       "installedSwVendorPatches": installedSwVendorPatches,
       "installedSwUserPatches": installedSwUserPatches,
       "installedSwLicInstalled": installedSwLicInstalled,
       "license": license,
       "licenseTable": licenseTable,
       "licenseEntry": licenseEntry,
       "licenseIndex": licenseIndex,
       "licenseProductName": licenseProductName,
       "licenseVendorAuthor": licenseVendorAuthor,
       "licenseExpirationDate": licenseExpirationDate,
       "licenseVersion": licenseVersion,
       "licenseCapacity": licenseCapacity,
       "licenseAuthorization": licenseAuthorization,
       "filesystem": filesystem,
       "filesystemTable": filesystemTable,
       "filesystemEntry": filesystemEntry,
       "filesystemIndex": filesystemIndex,
       "filesystemName": filesystemName,
       "filesystemFreeCapacity": filesystemFreeCapacity,
       "filesystemFormattedCap": filesystemFormattedCap,
       "mountinfo": mountinfo,
       "mountInfoTable": mountInfoTable,
       "mountInfoEntry": mountInfoEntry,
       "mountInfoIndex": mountInfoIndex,
       "mountInfoFileSystemName": mountInfoFileSystemName,
       "mountInfoDeviceName": mountInfoDeviceName,
       "mountInfoMountPoint": mountInfoMountPoint,
       "mountInfoMountType": mountInfoMountType,
       "mountInfoRelVolNum": mountInfoRelVolNum}
)
