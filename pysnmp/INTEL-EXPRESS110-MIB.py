# SNMP MIB module (INTEL-EXPRESS110-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-EXPRESS110-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:40 2024
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

(hub_products,) = mibBuilder.importSymbols(
    "Intel-Common-MIB",
    "hub-products")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Express110_ObjectIdentity = ObjectIdentity
express110 = _Express110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1)
)
_HubNumberofStackedChassis_Type = Integer32
_HubNumberofStackedChassis_Object = MibScalar
hubNumberofStackedChassis = _HubNumberofStackedChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 1),
    _HubNumberofStackedChassis_Type()
)
hubNumberofStackedChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubNumberofStackedChassis.setStatus("mandatory")


class _HubDescriptionString_Type(OctetString):
    """Custom type hubDescriptionString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 33),
    )


_HubDescriptionString_Type.__name__ = "OctetString"
_HubDescriptionString_Object = MibScalar
hubDescriptionString = _HubDescriptionString_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 2),
    _HubDescriptionString_Type()
)
hubDescriptionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubDescriptionString.setStatus("mandatory")


class _HubStackReset_Type(Integer32):
    """Custom type hubStackReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 2),
          ("reset", 1))
    )


_HubStackReset_Type.__name__ = "Integer32"
_HubStackReset_Object = MibScalar
hubStackReset = _HubStackReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 3),
    _HubStackReset_Type()
)
hubStackReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubStackReset.setStatus("mandatory")


class _HubLCDModeVariable_Type(Integer32):
    """Custom type hubLCDModeVariable based on Integer32"""
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
        *(("ipaddress", 6),
          ("lcdSleepText", 7),
          ("notSupported", 8),
          ("sysContact", 3),
          ("sysLocation", 2),
          ("sysName", 1),
          ("traps", 4),
          ("utilization", 5))
    )


_HubLCDModeVariable_Type.__name__ = "Integer32"
_HubLCDModeVariable_Object = MibScalar
hubLCDModeVariable = _HubLCDModeVariable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 4),
    _HubLCDModeVariable_Type()
)
hubLCDModeVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubLCDModeVariable.setStatus("mandatory")


class _HubLCDSleepText_Type(DisplayString):
    """Custom type hubLCDSleepText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HubLCDSleepText_Type.__name__ = "DisplayString"
_HubLCDSleepText_Object = MibScalar
hubLCDSleepText = _HubLCDSleepText_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 5),
    _HubLCDSleepText_Type()
)
hubLCDSleepText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubLCDSleepText.setStatus("mandatory")


class _HubLCDSleepTime_Type(Integer32):
    """Custom type hubLCDSleepTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HubLCDSleepTime_Type.__name__ = "Integer32"
_HubLCDSleepTime_Object = MibScalar
hubLCDSleepTime = _HubLCDSleepTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 6),
    _HubLCDSleepTime_Type()
)
hubLCDSleepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubLCDSleepTime.setStatus("mandatory")


class _HubRFC1516Segment_Type(Integer32):
    """Custom type hubRFC1516Segment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allsegments", 3),
          ("segment1", 1),
          ("segment2", 2))
    )


_HubRFC1516Segment_Type.__name__ = "Integer32"
_HubRFC1516Segment_Object = MibScalar
hubRFC1516Segment = _HubRFC1516Segment_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 7),
    _HubRFC1516Segment_Type()
)
hubRFC1516Segment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubRFC1516Segment.setStatus("mandatory")
_ChassisConfigTable_Object = MibTable
chassisConfigTable = _ChassisConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    chassisConfigTable.setStatus("mandatory")
_ChassisConfigEntry_Object = MibTableRow
chassisConfigEntry = _ChassisConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 8, 1)
)
chassisConfigEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "chassisConfigTableIndex"),
)
if mibBuilder.loadTexts:
    chassisConfigEntry.setStatus("mandatory")
_ChassisConfigTableIndex_Type = Integer32
_ChassisConfigTableIndex_Object = MibTableColumn
chassisConfigTableIndex = _ChassisConfigTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 8, 1, 1),
    _ChassisConfigTableIndex_Type()
)
chassisConfigTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisConfigTableIndex.setStatus("mandatory")


class _ChassisSegmentMode_Type(Integer32):
    """Custom type chassisSegmentMode based on Integer32"""
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
        *(("auto", 3),
          ("mixed", 4),
          ("segment1", 1),
          ("segment2", 2))
    )


_ChassisSegmentMode_Type.__name__ = "Integer32"
_ChassisSegmentMode_Object = MibTableColumn
chassisSegmentMode = _ChassisSegmentMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 8, 1, 2),
    _ChassisSegmentMode_Type()
)
chassisSegmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSegmentMode.setStatus("mandatory")


class _ChassisReset_Type(Integer32):
    """Custom type chassisReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 2),
          ("reset", 1))
    )


_ChassisReset_Type.__name__ = "Integer32"
_ChassisReset_Object = MibTableColumn
chassisReset = _ChassisReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 8, 1, 3),
    _ChassisReset_Type()
)
chassisReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisReset.setStatus("mandatory")


class _ChassisRPSState_Type(Integer32):
    """Custom type chassisRPSState based on Integer32"""
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
        *(("active", 3),
          ("notPresent", 1),
          ("notSupported", 4),
          ("standby", 2))
    )


_ChassisRPSState_Type.__name__ = "Integer32"
_ChassisRPSState_Object = MibTableColumn
chassisRPSState = _ChassisRPSState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 8, 1, 4),
    _ChassisRPSState_Type()
)
chassisRPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisRPSState.setStatus("mandatory")


class _ChassisIsolate_Type(Integer32):
    """Custom type chassisIsolate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isolate", 1),
          ("notSupported", 3),
          ("unisolate", 2))
    )


_ChassisIsolate_Type.__name__ = "Integer32"
_ChassisIsolate_Object = MibTableColumn
chassisIsolate = _ChassisIsolate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 8, 1, 5),
    _ChassisIsolate_Type()
)
chassisIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIsolate.setStatus("mandatory")
_ModuleConfigStatusTable_Object = MibTable
moduleConfigStatusTable = _ModuleConfigStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9)
)
if mibBuilder.loadTexts:
    moduleConfigStatusTable.setStatus("mandatory")
_ModuleConfigStatusEntry_Object = MibTableRow
moduleConfigStatusEntry = _ModuleConfigStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1)
)
moduleConfigStatusEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "moduleChassisIndex"),
    (0, "INTEL-EXPRESS110-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleConfigStatusEntry.setStatus("mandatory")
_ModuleChassisIndex_Type = Integer32
_ModuleChassisIndex_Object = MibTableColumn
moduleChassisIndex = _ModuleChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 1),
    _ModuleChassisIndex_Type()
)
moduleChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleChassisIndex.setStatus("mandatory")
_ModuleIndex_Type = Integer32
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 2),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("mandatory")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 6),
          ("express330TXports16", 13),
          ("express330TXports24", 14),
          ("fxUplink", 15),
          ("hubTXports12", 2),
          ("hubTXports24", 3),
          ("hubcrTXports12", 9),
          ("hubcrTXports24", 10),
          ("hubppTXports12", 11),
          ("hubppTXports24", 12),
          ("management", 5),
          ("managementWithRMON", 7),
          ("none", 1),
          ("reserved4", 4),
          ("reserved8", 8),
          ("txUplink", 16))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 3),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("mandatory")


class _ModuleUserAssignedType_Type(DisplayString):
    """Custom type moduleUserAssignedType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_ModuleUserAssignedType_Type.__name__ = "DisplayString"
_ModuleUserAssignedType_Object = MibTableColumn
moduleUserAssignedType = _ModuleUserAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 4),
    _ModuleUserAssignedType_Type()
)
moduleUserAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleUserAssignedType.setStatus("mandatory")


class _ModuleUserAssignedNumber_Type(DisplayString):
    """Custom type moduleUserAssignedNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_ModuleUserAssignedNumber_Type.__name__ = "DisplayString"
_ModuleUserAssignedNumber_Object = MibTableColumn
moduleUserAssignedNumber = _ModuleUserAssignedNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 5),
    _ModuleUserAssignedNumber_Type()
)
moduleUserAssignedNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleUserAssignedNumber.setStatus("mandatory")


class _ModuleUserAssignedName_Type(DisplayString):
    """Custom type moduleUserAssignedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_ModuleUserAssignedName_Type.__name__ = "DisplayString"
_ModuleUserAssignedName_Object = MibTableColumn
moduleUserAssignedName = _ModuleUserAssignedName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 6),
    _ModuleUserAssignedName_Type()
)
moduleUserAssignedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleUserAssignedName.setStatus("mandatory")
_ModuleSizeofROM_Type = Integer32
_ModuleSizeofROM_Object = MibTableColumn
moduleSizeofROM = _ModuleSizeofROM_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 7),
    _ModuleSizeofROM_Type()
)
moduleSizeofROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSizeofROM.setStatus("mandatory")
_ModuleSizeofRAM_Type = Integer32
_ModuleSizeofRAM_Object = MibTableColumn
moduleSizeofRAM = _ModuleSizeofRAM_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 8),
    _ModuleSizeofRAM_Type()
)
moduleSizeofRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSizeofRAM.setStatus("mandatory")


class _ModuleHWDescription_Type(DisplayString):
    """Custom type moduleHWDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_ModuleHWDescription_Type.__name__ = "DisplayString"
_ModuleHWDescription_Object = MibTableColumn
moduleHWDescription = _ModuleHWDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 9),
    _ModuleHWDescription_Type()
)
moduleHWDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHWDescription.setStatus("mandatory")


class _ModuleAgentSWVersion_Type(DisplayString):
    """Custom type moduleAgentSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_ModuleAgentSWVersion_Type.__name__ = "DisplayString"
_ModuleAgentSWVersion_Object = MibTableColumn
moduleAgentSWVersion = _ModuleAgentSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 10),
    _ModuleAgentSWVersion_Type()
)
moduleAgentSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAgentSWVersion.setStatus("mandatory")


class _ModuleBootSWVersion_Type(DisplayString):
    """Custom type moduleBootSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_ModuleBootSWVersion_Type.__name__ = "DisplayString"
_ModuleBootSWVersion_Object = MibTableColumn
moduleBootSWVersion = _ModuleBootSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 11),
    _ModuleBootSWVersion_Type()
)
moduleBootSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBootSWVersion.setStatus("mandatory")


class _ModuleManufacturingInfo_Type(DisplayString):
    """Custom type moduleManufacturingInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_ModuleManufacturingInfo_Type.__name__ = "DisplayString"
_ModuleManufacturingInfo_Object = MibTableColumn
moduleManufacturingInfo = _ModuleManufacturingInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 12),
    _ModuleManufacturingInfo_Type()
)
moduleManufacturingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleManufacturingInfo.setStatus("mandatory")
_ModuleTotalPortCount_Type = Integer32
_ModuleTotalPortCount_Object = MibTableColumn
moduleTotalPortCount = _ModuleTotalPortCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 13),
    _ModuleTotalPortCount_Type()
)
moduleTotalPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTotalPortCount.setStatus("mandatory")
_ModuleExternalPortCount_Type = Integer32
_ModuleExternalPortCount_Object = MibTableColumn
moduleExternalPortCount = _ModuleExternalPortCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 14),
    _ModuleExternalPortCount_Type()
)
moduleExternalPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleExternalPortCount.setStatus("mandatory")


class _ModuleSegmentLockout_Type(Integer32):
    """Custom type moduleSegmentLockout based on Integer32"""
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
        *(("nButtonnMgmt", 4),
          ("nButtonyMgmt", 2),
          ("yButtonnMgmt", 3),
          ("yButtonyMgmt", 1))
    )


_ModuleSegmentLockout_Type.__name__ = "Integer32"
_ModuleSegmentLockout_Object = MibTableColumn
moduleSegmentLockout = _ModuleSegmentLockout_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 15),
    _ModuleSegmentLockout_Type()
)
moduleSegmentLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSegmentLockout.setStatus("mandatory")


class _ModuleLEDInfo_Type(OctetString):
    """Custom type moduleLEDInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ModuleLEDInfo_Type.__name__ = "OctetString"
_ModuleLEDInfo_Object = MibTableColumn
moduleLEDInfo = _ModuleLEDInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 16),
    _ModuleLEDInfo_Type()
)
moduleLEDInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleLEDInfo.setStatus("mandatory")
_ModuleLastErrorID_Type = Integer32
_ModuleLastErrorID_Object = MibTableColumn
moduleLastErrorID = _ModuleLastErrorID_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 17),
    _ModuleLastErrorID_Type()
)
moduleLastErrorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleLastErrorID.setStatus("mandatory")


class _ModuleMediaDevicesReset_Type(Integer32):
    """Custom type moduleMediaDevicesReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("notreset", 2),
          ("reset", 1))
    )


_ModuleMediaDevicesReset_Type.__name__ = "Integer32"
_ModuleMediaDevicesReset_Object = MibTableColumn
moduleMediaDevicesReset = _ModuleMediaDevicesReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 18),
    _ModuleMediaDevicesReset_Type()
)
moduleMediaDevicesReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleMediaDevicesReset.setStatus("mandatory")
_ModuleImageFileSource_Type = IpAddress
_ModuleImageFileSource_Object = MibTableColumn
moduleImageFileSource = _ModuleImageFileSource_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 19),
    _ModuleImageFileSource_Type()
)
moduleImageFileSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleImageFileSource.setStatus("mandatory")


class _ModuleImageFileName_Type(DisplayString):
    """Custom type moduleImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_ModuleImageFileName_Type.__name__ = "DisplayString"
_ModuleImageFileName_Object = MibTableColumn
moduleImageFileName = _ModuleImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 20),
    _ModuleImageFileName_Type()
)
moduleImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleImageFileName.setStatus("mandatory")


class _ModuleImageDownloadControl_Type(Integer32):
    """Custom type moduleImageDownloadControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("start", 1),
          ("stop", 2))
    )


_ModuleImageDownloadControl_Type.__name__ = "Integer32"
_ModuleImageDownloadControl_Object = MibTableColumn
moduleImageDownloadControl = _ModuleImageDownloadControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 21),
    _ModuleImageDownloadControl_Type()
)
moduleImageDownloadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleImageDownloadControl.setStatus("mandatory")


class _ModuleImageDownloadStatus_Type(Integer32):
    """Custom type moduleImageDownloadStatus based on Integer32"""
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
        *(("completed", 3),
          ("error", 4),
          ("notSupported", 5),
          ("started", 1),
          ("stopping", 2))
    )


_ModuleImageDownloadStatus_Type.__name__ = "Integer32"
_ModuleImageDownloadStatus_Object = MibTableColumn
moduleImageDownloadStatus = _ModuleImageDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 22),
    _ModuleImageDownloadStatus_Type()
)
moduleImageDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleImageDownloadStatus.setStatus("mandatory")


class _ModuleOperationalStatus_Type(Integer32):
    """Custom type moduleOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notoperational", 2),
          ("notpresent", 3),
          ("operational", 1))
    )


_ModuleOperationalStatus_Type.__name__ = "Integer32"
_ModuleOperationalStatus_Object = MibTableColumn
moduleOperationalStatus = _ModuleOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 23),
    _ModuleOperationalStatus_Type()
)
moduleOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleOperationalStatus.setStatus("mandatory")
_ModuleUptime_Type = TimeTicks
_ModuleUptime_Object = MibTableColumn
moduleUptime = _ModuleUptime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 24),
    _ModuleUptime_Type()
)
moduleUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleUptime.setStatus("mandatory")


class _ModuleReset_Type(Integer32):
    """Custom type moduleReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("notreset", 2),
          ("reset", 1))
    )


_ModuleReset_Type.__name__ = "Integer32"
_ModuleReset_Object = MibTableColumn
moduleReset = _ModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 25),
    _ModuleReset_Type()
)
moduleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleReset.setStatus("mandatory")
_ModuleAllPortLEDInfo_Type = OctetString
_ModuleAllPortLEDInfo_Object = MibTableColumn
moduleAllPortLEDInfo = _ModuleAllPortLEDInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 26),
    _ModuleAllPortLEDInfo_Type()
)
moduleAllPortLEDInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortLEDInfo.setStatus("mandatory")
_ModuleAllPortAdminStatus_Type = OctetString
_ModuleAllPortAdminStatus_Object = MibTableColumn
moduleAllPortAdminStatus = _ModuleAllPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 27),
    _ModuleAllPortAdminStatus_Type()
)
moduleAllPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleAllPortAdminStatus.setStatus("mandatory")
_ModuleAllPortOperStatus_Type = OctetString
_ModuleAllPortOperStatus_Object = MibTableColumn
moduleAllPortOperStatus = _ModuleAllPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 28),
    _ModuleAllPortOperStatus_Type()
)
moduleAllPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortOperStatus.setStatus("mandatory")
_ModuleAllPortSpeed_Type = OctetString
_ModuleAllPortSpeed_Object = MibTableColumn
moduleAllPortSpeed = _ModuleAllPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 29),
    _ModuleAllPortSpeed_Type()
)
moduleAllPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortSpeed.setStatus("mandatory")
_ModuleAllPortSpeedInfo_Type = OctetString
_ModuleAllPortSpeedInfo_Object = MibTableColumn
moduleAllPortSpeedInfo = _ModuleAllPortSpeedInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 30),
    _ModuleAllPortSpeedInfo_Type()
)
moduleAllPortSpeedInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortSpeedInfo.setStatus("mandatory")


class _ModuleSegmentMode_Type(Integer32):
    """Custom type moduleSegmentMode based on Integer32"""
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
        *(("auto", 3),
          ("mixed", 4),
          ("segment1", 1),
          ("segment2", 2))
    )


_ModuleSegmentMode_Type.__name__ = "Integer32"
_ModuleSegmentMode_Object = MibTableColumn
moduleSegmentMode = _ModuleSegmentMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 31),
    _ModuleSegmentMode_Type()
)
moduleSegmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSegmentMode.setStatus("mandatory")
_ModuleAllPortLinkPartnerInfo_Type = OctetString
_ModuleAllPortLinkPartnerInfo_Object = MibTableColumn
moduleAllPortLinkPartnerInfo = _ModuleAllPortLinkPartnerInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 32),
    _ModuleAllPortLinkPartnerInfo_Type()
)
moduleAllPortLinkPartnerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortLinkPartnerInfo.setStatus("mandatory")


class _ModuleAllPortCounterReset_Type(Integer32):
    """Custom type moduleAllPortCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 2),
          ("reset", 1))
    )


_ModuleAllPortCounterReset_Type.__name__ = "Integer32"
_ModuleAllPortCounterReset_Object = MibTableColumn
moduleAllPortCounterReset = _ModuleAllPortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 33),
    _ModuleAllPortCounterReset_Type()
)
moduleAllPortCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleAllPortCounterReset.setStatus("mandatory")
_ModuleAllPortTimeSinceLinkChange_Type = OctetString
_ModuleAllPortTimeSinceLinkChange_Object = MibTableColumn
moduleAllPortTimeSinceLinkChange = _ModuleAllPortTimeSinceLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 34),
    _ModuleAllPortTimeSinceLinkChange_Type()
)
moduleAllPortTimeSinceLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortTimeSinceLinkChange.setStatus("mandatory")


class _ModulePersistentMemoryReset_Type(Integer32):
    """Custom type modulePersistentMemoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("notreset", 2),
          ("reset", 1))
    )


_ModulePersistentMemoryReset_Type.__name__ = "Integer32"
_ModulePersistentMemoryReset_Object = MibTableColumn
modulePersistentMemoryReset = _ModulePersistentMemoryReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 9, 1, 35),
    _ModulePersistentMemoryReset_Type()
)
modulePersistentMemoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePersistentMemoryReset.setStatus("mandatory")
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("mandatory")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1)
)
portConfigEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "portChassisIndex"),
    (0, "INTEL-EXPRESS110-MIB", "portModuleIndex"),
    (0, "INTEL-EXPRESS110-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("mandatory")
_PortChassisIndex_Type = Integer32
_PortChassisIndex_Object = MibTableColumn
portChassisIndex = _PortChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 1),
    _PortChassisIndex_Type()
)
portChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChassisIndex.setStatus("mandatory")
_PortModuleIndex_Type = Integer32
_PortModuleIndex_Object = MibTableColumn
portModuleIndex = _PortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 2),
    _PortModuleIndex_Type()
)
portModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleIndex.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 3),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("fiberMultimode", 3),
          ("fiberSinglemode", 4),
          ("internalHalfDuplex", 5),
          ("twistedPairFullDuplex", 2),
          ("twistedPairHalfDuplex", 1))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 4),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")


class _PortAdminStatus_Type(Integer32):
    """Custom type portAdminStatus based on Integer32"""
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


_PortAdminStatus_Type.__name__ = "Integer32"
_PortAdminStatus_Object = MibTableColumn
portAdminStatus = _PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 5),
    _PortAdminStatus_Type()
)
portAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminStatus.setStatus("mandatory")


class _PortOperStatus_Type(Integer32):
    """Custom type portOperStatus based on Integer32"""
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
        *(("notoperational", 2),
          ("notpresent", 3),
          ("operational", 1),
          ("violated", 4))
    )


_PortOperStatus_Type.__name__ = "Integer32"
_PortOperStatus_Object = MibTableColumn
portOperStatus = _PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 6),
    _PortOperStatus_Type()
)
portOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperStatus.setStatus("mandatory")


class _PortJabber_Type(Integer32):
    """Custom type portJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("ok", 1))
    )


_PortJabber_Type.__name__ = "Integer32"
_PortJabber_Object = MibTableColumn
portJabber = _PortJabber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 7),
    _PortJabber_Type()
)
portJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portJabber.setStatus("mandatory")


class _PortLinkPartnerInfo_Type(OctetString):
    """Custom type portLinkPartnerInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PortLinkPartnerInfo_Type.__name__ = "OctetString"
_PortLinkPartnerInfo_Object = MibTableColumn
portLinkPartnerInfo = _PortLinkPartnerInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 8),
    _PortLinkPartnerInfo_Type()
)
portLinkPartnerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkPartnerInfo.setStatus("mandatory")


class _PortLEDInfo_Type(OctetString):
    """Custom type portLEDInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PortLEDInfo_Type.__name__ = "OctetString"
_PortLEDInfo_Object = MibTableColumn
portLEDInfo = _PortLEDInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 9),
    _PortLEDInfo_Type()
)
portLEDInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLEDInfo.setStatus("mandatory")
_PortTimeSinceLastLinkChange_Type = TimeTicks
_PortTimeSinceLastLinkChange_Object = MibTableColumn
portTimeSinceLastLinkChange = _PortTimeSinceLastLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 10),
    _PortTimeSinceLastLinkChange_Type()
)
portTimeSinceLastLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTimeSinceLastLinkChange.setStatus("mandatory")


class _PortAllCountersReset_Type(Integer32):
    """Custom type portAllCountersReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 2),
          ("reset", 1))
    )


_PortAllCountersReset_Type.__name__ = "Integer32"
_PortAllCountersReset_Object = MibTableColumn
portAllCountersReset = _PortAllCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 11),
    _PortAllCountersReset_Type()
)
portAllCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAllCountersReset.setStatus("mandatory")


class _PortReset_Type(Integer32):
    """Custom type portReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("notreset", 2),
          ("reset", 1))
    )


_PortReset_Type.__name__ = "Integer32"
_PortReset_Object = MibTableColumn
portReset = _PortReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 12),
    _PortReset_Type()
)
portReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReset.setStatus("mandatory")


class _PortLastErrorID_Type(Integer32):
    """Custom type portLastErrorID based on Integer32"""
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
        *(("badPhy", 2),
          ("jabberSeen", 5),
          ("noError", 1),
          ("partition", 6),
          ("polarity", 3),
          ("reserved1", 7),
          ("reserved2", 8),
          ("wrongSpeedLP", 4))
    )


_PortLastErrorID_Type.__name__ = "Integer32"
_PortLastErrorID_Object = MibTableColumn
portLastErrorID = _PortLastErrorID_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 13),
    _PortLastErrorID_Type()
)
portLastErrorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastErrorID.setStatus("mandatory")


class _PortSegmentAdminMode_Type(Integer32):
    """Custom type portSegmentAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("segment1", 1),
          ("segment2", 2))
    )


_PortSegmentAdminMode_Type.__name__ = "Integer32"
_PortSegmentAdminMode_Object = MibTableColumn
portSegmentAdminMode = _PortSegmentAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 14),
    _PortSegmentAdminMode_Type()
)
portSegmentAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSegmentAdminMode.setStatus("mandatory")


class _PortSegmentOperStatus_Type(Integer32):
    """Custom type portSegmentOperStatus based on Integer32"""
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
          ("segment1", 1),
          ("segment2", 2))
    )


_PortSegmentOperStatus_Type.__name__ = "Integer32"
_PortSegmentOperStatus_Object = MibTableColumn
portSegmentOperStatus = _PortSegmentOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 15),
    _PortSegmentOperStatus_Type()
)
portSegmentOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSegmentOperStatus.setStatus("mandatory")


class _PortLinkSpeed_Type(Integer32):
    """Custom type portLinkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mb10", 2),
          ("mb100", 3),
          ("none", 1))
    )


_PortLinkSpeed_Type.__name__ = "Integer32"
_PortLinkSpeed_Object = MibTableColumn
portLinkSpeed = _PortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 16),
    _PortLinkSpeed_Type()
)
portLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkSpeed.setStatus("mandatory")


class _PortSecureAdminMode_Type(Integer32):
    """Custom type portSecureAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portSecurityOff", 1),
          ("portSecurityOn", 2))
    )


_PortSecureAdminMode_Type.__name__ = "Integer32"
_PortSecureAdminMode_Object = MibTableColumn
portSecureAdminMode = _PortSecureAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 17),
    _PortSecureAdminMode_Type()
)
portSecureAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecureAdminMode.setStatus("mandatory")


class _PortSecureMAC_Type(OctetString):
    """Custom type portSecureMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortSecureMAC_Type.__name__ = "OctetString"
_PortSecureMAC_Object = MibTableColumn
portSecureMAC = _PortSecureMAC_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 18),
    _PortSecureMAC_Type()
)
portSecureMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecureMAC.setStatus("mandatory")


class _PortLinkTestState_Type(Integer32):
    """Custom type portLinkTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 3))
    )


_PortLinkTestState_Type.__name__ = "Integer32"
_PortLinkTestState_Object = MibTableColumn
portLinkTestState = _PortLinkTestState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 19),
    _PortLinkTestState_Type()
)
portLinkTestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLinkTestState.setStatus("mandatory")


class _PortLinkTestStatusTrapCtrl_Type(Integer32):
    """Custom type portLinkTestStatusTrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 3))
    )


_PortLinkTestStatusTrapCtrl_Type.__name__ = "Integer32"
_PortLinkTestStatusTrapCtrl_Object = MibTableColumn
portLinkTestStatusTrapCtrl = _PortLinkTestStatusTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 20),
    _PortLinkTestStatusTrapCtrl_Type()
)
portLinkTestStatusTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLinkTestStatusTrapCtrl.setStatus("mandatory")


class _PortSpeedStatusTrapCtrl_Type(Integer32):
    """Custom type portSpeedStatusTrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 3))
    )


_PortSpeedStatusTrapCtrl_Type.__name__ = "Integer32"
_PortSpeedStatusTrapCtrl_Object = MibTableColumn
portSpeedStatusTrapCtrl = _PortSpeedStatusTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 21),
    _PortSpeedStatusTrapCtrl_Type()
)
portSpeedStatusTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedStatusTrapCtrl.setStatus("mandatory")


class _PortPolarityStatus_Type(Integer32):
    """Custom type portPolarityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reversed", 2),
          ("unknown", 3))
    )


_PortPolarityStatus_Type.__name__ = "Integer32"
_PortPolarityStatus_Object = MibTableColumn
portPolarityStatus = _PortPolarityStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 10, 1, 22),
    _PortPolarityStatus_Type()
)
portPolarityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPolarityStatus.setStatus("mandatory")
_RptrSegmentConfigTable_Object = MibTable
rptrSegmentConfigTable = _RptrSegmentConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11)
)
if mibBuilder.loadTexts:
    rptrSegmentConfigTable.setStatus("mandatory")
_RptrSegmentConfigEntry_Object = MibTableRow
rptrSegmentConfigEntry = _RptrSegmentConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1)
)
rptrSegmentConfigEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "rptrSegmentConfigIndex"),
)
if mibBuilder.loadTexts:
    rptrSegmentConfigEntry.setStatus("mandatory")


class _RptrSegmentConfigIndex_Type(Integer32):
    """Custom type rptrSegmentConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("segment1", 1),
          ("segment2", 2))
    )


_RptrSegmentConfigIndex_Type.__name__ = "Integer32"
_RptrSegmentConfigIndex_Object = MibTableColumn
rptrSegmentConfigIndex = _RptrSegmentConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 1),
    _RptrSegmentConfigIndex_Type()
)
rptrSegmentConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentConfigIndex.setStatus("mandatory")


class _RptrSegmentOperationalStatus_Type(Integer32):
    """Custom type rptrSegmentOperationalStatus based on Integer32"""
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
        *(("generalFailure", 6),
          ("groupFailure", 4),
          ("holdInReset", 7),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5),
          ("rptrFailure", 3))
    )


_RptrSegmentOperationalStatus_Type.__name__ = "Integer32"
_RptrSegmentOperationalStatus_Object = MibTableColumn
rptrSegmentOperationalStatus = _RptrSegmentOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 2),
    _RptrSegmentOperationalStatus_Type()
)
rptrSegmentOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentOperationalStatus.setStatus("mandatory")


class _RptrSegmentZeroCounters_Type(Integer32):
    """Custom type rptrSegmentZeroCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 2),
          ("reset", 1))
    )


_RptrSegmentZeroCounters_Type.__name__ = "Integer32"
_RptrSegmentZeroCounters_Object = MibTableColumn
rptrSegmentZeroCounters = _RptrSegmentZeroCounters_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 3),
    _RptrSegmentZeroCounters_Type()
)
rptrSegmentZeroCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentZeroCounters.setStatus("mandatory")


class _RptrSegmentReset_Type(Integer32):
    """Custom type rptrSegmentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("notreset", 2),
          ("reset", 1))
    )


_RptrSegmentReset_Type.__name__ = "Integer32"
_RptrSegmentReset_Object = MibTableColumn
rptrSegmentReset = _RptrSegmentReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 4),
    _RptrSegmentReset_Type()
)
rptrSegmentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentReset.setStatus("mandatory")


class _RptrSegmentResetMedia_Type(Integer32):
    """Custom type rptrSegmentResetMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("notreset", 2),
          ("reset", 1))
    )


_RptrSegmentResetMedia_Type.__name__ = "Integer32"
_RptrSegmentResetMedia_Object = MibTableColumn
rptrSegmentResetMedia = _RptrSegmentResetMedia_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 5),
    _RptrSegmentResetMedia_Type()
)
rptrSegmentResetMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentResetMedia.setStatus("mandatory")


class _RptrSegmentPartitionThreshold_Type(Integer32):
    """Custom type rptrSegmentPartitionThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("collisions128", 2),
          ("collisions32", 3),
          ("collisions64", 1))
    )


_RptrSegmentPartitionThreshold_Type.__name__ = "Integer32"
_RptrSegmentPartitionThreshold_Object = MibTableColumn
rptrSegmentPartitionThreshold = _RptrSegmentPartitionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 6),
    _RptrSegmentPartitionThreshold_Type()
)
rptrSegmentPartitionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentPartitionThreshold.setStatus("mandatory")


class _RptrSegmentNonDisruptTest_Type(Integer32):
    """Custom type rptrSegmentNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("notSupported", 3),
          ("selfTest", 2))
    )


_RptrSegmentNonDisruptTest_Type.__name__ = "Integer32"
_RptrSegmentNonDisruptTest_Object = MibTableColumn
rptrSegmentNonDisruptTest = _RptrSegmentNonDisruptTest_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 7),
    _RptrSegmentNonDisruptTest_Type()
)
rptrSegmentNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentNonDisruptTest.setStatus("mandatory")
_RptrSegmentUtilizationTrapThreshold_Type = Gauge32
_RptrSegmentUtilizationTrapThreshold_Object = MibTableColumn
rptrSegmentUtilizationTrapThreshold = _RptrSegmentUtilizationTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 8),
    _RptrSegmentUtilizationTrapThreshold_Type()
)
rptrSegmentUtilizationTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentUtilizationTrapThreshold.setStatus("mandatory")
_RptrSegmentCollisionTrapThreshold_Type = Counter32
_RptrSegmentCollisionTrapThreshold_Object = MibTableColumn
rptrSegmentCollisionTrapThreshold = _RptrSegmentCollisionTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 9),
    _RptrSegmentCollisionTrapThreshold_Type()
)
rptrSegmentCollisionTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentCollisionTrapThreshold.setStatus("mandatory")


class _RptrSegmentUtilizationTrapPeriod_Type(Integer32):
    """Custom type rptrSegmentUtilizationTrapPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_RptrSegmentUtilizationTrapPeriod_Type.__name__ = "Integer32"
_RptrSegmentUtilizationTrapPeriod_Object = MibTableColumn
rptrSegmentUtilizationTrapPeriod = _RptrSegmentUtilizationTrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 10),
    _RptrSegmentUtilizationTrapPeriod_Type()
)
rptrSegmentUtilizationTrapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentUtilizationTrapPeriod.setStatus("mandatory")


class _RptrSegmentCollisionTrapPeriod_Type(Integer32):
    """Custom type rptrSegmentCollisionTrapPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_RptrSegmentCollisionTrapPeriod_Type.__name__ = "Integer32"
_RptrSegmentCollisionTrapPeriod_Object = MibTableColumn
rptrSegmentCollisionTrapPeriod = _RptrSegmentCollisionTrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 11),
    _RptrSegmentCollisionTrapPeriod_Type()
)
rptrSegmentCollisionTrapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSegmentCollisionTrapPeriod.setStatus("mandatory")


class _RptrSegmentSpeed_Type(Integer32):
    """Custom type rptrSegmentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mb10", 1),
          ("mb100", 2))
    )


_RptrSegmentSpeed_Type.__name__ = "Integer32"
_RptrSegmentSpeed_Object = MibTableColumn
rptrSegmentSpeed = _RptrSegmentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 11, 1, 12),
    _RptrSegmentSpeed_Type()
)
rptrSegmentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentSpeed.setStatus("mandatory")
_RptrSegmentStatTable_Object = MibTable
rptrSegmentStatTable = _RptrSegmentStatTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12)
)
if mibBuilder.loadTexts:
    rptrSegmentStatTable.setStatus("mandatory")
_RptrSegmentStatEntry_Object = MibTableRow
rptrSegmentStatEntry = _RptrSegmentStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1)
)
rptrSegmentStatEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "rptrSegmentStatIndex"),
)
if mibBuilder.loadTexts:
    rptrSegmentStatEntry.setStatus("mandatory")


class _RptrSegmentStatIndex_Type(Integer32):
    """Custom type rptrSegmentStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("segment1", 1),
          ("segment2", 2))
    )


_RptrSegmentStatIndex_Type.__name__ = "Integer32"
_RptrSegmentStatIndex_Object = MibTableColumn
rptrSegmentStatIndex = _RptrSegmentStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1, 1),
    _RptrSegmentStatIndex_Type()
)
rptrSegmentStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentStatIndex.setStatus("mandatory")
_RptrSegmentTotalFrames_Type = Counter32
_RptrSegmentTotalFrames_Object = MibTableColumn
rptrSegmentTotalFrames = _RptrSegmentTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1, 2),
    _RptrSegmentTotalFrames_Type()
)
rptrSegmentTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentTotalFrames.setStatus("mandatory")
_RptrSegmentTotalOctets_Type = Counter32
_RptrSegmentTotalOctets_Object = MibTableColumn
rptrSegmentTotalOctets = _RptrSegmentTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1, 3),
    _RptrSegmentTotalOctets_Type()
)
rptrSegmentTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentTotalOctets.setStatus("mandatory")
_RptrSegmentTotalErrors_Type = Counter32
_RptrSegmentTotalErrors_Object = MibTableColumn
rptrSegmentTotalErrors = _RptrSegmentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1, 4),
    _RptrSegmentTotalErrors_Type()
)
rptrSegmentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentTotalErrors.setStatus("mandatory")
_RptrSegmentTotalCollisions_Type = Counter32
_RptrSegmentTotalCollisions_Object = MibTableColumn
rptrSegmentTotalCollisions = _RptrSegmentTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1, 5),
    _RptrSegmentTotalCollisions_Type()
)
rptrSegmentTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentTotalCollisions.setStatus("mandatory")
_RptrSegmentPartitionedPorts_Type = Gauge32
_RptrSegmentPartitionedPorts_Object = MibTableColumn
rptrSegmentPartitionedPorts = _RptrSegmentPartitionedPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1, 6),
    _RptrSegmentPartitionedPorts_Type()
)
rptrSegmentPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentPartitionedPorts.setStatus("mandatory")
_RptrSegmentHealthText_Type = DisplayString
_RptrSegmentHealthText_Object = MibTableColumn
rptrSegmentHealthText = _RptrSegmentHealthText_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1, 7),
    _RptrSegmentHealthText_Type()
)
rptrSegmentHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentHealthText.setStatus("mandatory")
_RptrSegmentUtilization_Type = Gauge32
_RptrSegmentUtilization_Object = MibTableColumn
rptrSegmentUtilization = _RptrSegmentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 12, 1, 8),
    _RptrSegmentUtilization_Type()
)
rptrSegmentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSegmentUtilization.setStatus("mandatory")
_RptrModuleStatTable_Object = MibTable
rptrModuleStatTable = _RptrModuleStatTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13)
)
if mibBuilder.loadTexts:
    rptrModuleStatTable.setStatus("mandatory")
_RptrModuleStatEntry_Object = MibTableRow
rptrModuleStatEntry = _RptrModuleStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1)
)
rptrModuleStatEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "rptrModuleIndex"),
)
if mibBuilder.loadTexts:
    rptrModuleStatEntry.setStatus("mandatory")
_RptrModuleIndex_Type = Integer32
_RptrModuleIndex_Object = MibTableColumn
rptrModuleIndex = _RptrModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 1),
    _RptrModuleIndex_Type()
)
rptrModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleIndex.setStatus("mandatory")
_RptrModuleTotalFrames_Type = Counter32
_RptrModuleTotalFrames_Object = MibTableColumn
rptrModuleTotalFrames = _RptrModuleTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 2),
    _RptrModuleTotalFrames_Type()
)
rptrModuleTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleTotalFrames.setStatus("mandatory")
_RptrModuleTotalOctets_Type = Counter32
_RptrModuleTotalOctets_Object = MibTableColumn
rptrModuleTotalOctets = _RptrModuleTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 3),
    _RptrModuleTotalOctets_Type()
)
rptrModuleTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleTotalOctets.setStatus("mandatory")
_RptrModuleTotalErrors_Type = Counter32
_RptrModuleTotalErrors_Object = MibTableColumn
rptrModuleTotalErrors = _RptrModuleTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 4),
    _RptrModuleTotalErrors_Type()
)
rptrModuleTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleTotalErrors.setStatus("mandatory")
_RptrModuleFCSErrors_Type = Counter32
_RptrModuleFCSErrors_Object = MibTableColumn
rptrModuleFCSErrors = _RptrModuleFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 5),
    _RptrModuleFCSErrors_Type()
)
rptrModuleFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleFCSErrors.setStatus("mandatory")
_RptrModuleAlignmentErrors_Type = Counter32
_RptrModuleAlignmentErrors_Object = MibTableColumn
rptrModuleAlignmentErrors = _RptrModuleAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 6),
    _RptrModuleAlignmentErrors_Type()
)
rptrModuleAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleAlignmentErrors.setStatus("mandatory")
_RptrModuleFrameTooLongs_Type = Counter32
_RptrModuleFrameTooLongs_Object = MibTableColumn
rptrModuleFrameTooLongs = _RptrModuleFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 7),
    _RptrModuleFrameTooLongs_Type()
)
rptrModuleFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleFrameTooLongs.setStatus("mandatory")
_RptrModuleShortEvents_Type = Counter32
_RptrModuleShortEvents_Object = MibTableColumn
rptrModuleShortEvents = _RptrModuleShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 8),
    _RptrModuleShortEvents_Type()
)
rptrModuleShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleShortEvents.setStatus("mandatory")
_RptrModuleRunts_Type = Counter32
_RptrModuleRunts_Object = MibTableColumn
rptrModuleRunts = _RptrModuleRunts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 9),
    _RptrModuleRunts_Type()
)
rptrModuleRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleRunts.setStatus("mandatory")
_RptrModuleCollisions_Type = Counter32
_RptrModuleCollisions_Object = MibTableColumn
rptrModuleCollisions = _RptrModuleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 10),
    _RptrModuleCollisions_Type()
)
rptrModuleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleCollisions.setStatus("mandatory")
_RptrModuleLateEvents_Type = Counter32
_RptrModuleLateEvents_Object = MibTableColumn
rptrModuleLateEvents = _RptrModuleLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 11),
    _RptrModuleLateEvents_Type()
)
rptrModuleLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleLateEvents.setStatus("mandatory")
_RptrModuleVeryLongEvents_Type = Counter32
_RptrModuleVeryLongEvents_Object = MibTableColumn
rptrModuleVeryLongEvents = _RptrModuleVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 12),
    _RptrModuleVeryLongEvents_Type()
)
rptrModuleVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleVeryLongEvents.setStatus("mandatory")
_RptrModuleDataRateMismatches_Type = Counter32
_RptrModuleDataRateMismatches_Object = MibTableColumn
rptrModuleDataRateMismatches = _RptrModuleDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 13),
    _RptrModuleDataRateMismatches_Type()
)
rptrModuleDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleDataRateMismatches.setStatus("mandatory")
_RptrModuleAutoPartitions_Type = Counter32
_RptrModuleAutoPartitions_Object = MibTableColumn
rptrModuleAutoPartitions = _RptrModuleAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 13, 1, 14),
    _RptrModuleAutoPartitions_Type()
)
rptrModuleAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrModuleAutoPartitions.setStatus("mandatory")
_RptrPortStatTable_Object = MibTable
rptrPortStatTable = _RptrPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14)
)
if mibBuilder.loadTexts:
    rptrPortStatTable.setStatus("mandatory")
_RptrPortStatEntry_Object = MibTableRow
rptrPortStatEntry = _RptrPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1)
)
rptrPortStatEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "rptrPortChassisIndex"),
    (0, "INTEL-EXPRESS110-MIB", "rptrPortIndex"),
)
if mibBuilder.loadTexts:
    rptrPortStatEntry.setStatus("mandatory")
_RptrPortChassisIndex_Type = Integer32
_RptrPortChassisIndex_Object = MibTableColumn
rptrPortChassisIndex = _RptrPortChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 1),
    _RptrPortChassisIndex_Type()
)
rptrPortChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortChassisIndex.setStatus("mandatory")
_RptrPortIndex_Type = Integer32
_RptrPortIndex_Object = MibTableColumn
rptrPortIndex = _RptrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 2),
    _RptrPortIndex_Type()
)
rptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortIndex.setStatus("mandatory")


class _RptrPortPartitionState_Type(Integer32):
    """Custom type rptrPortPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartition", 1),
          ("notAutoPartition", 2))
    )


_RptrPortPartitionState_Type.__name__ = "Integer32"
_RptrPortPartitionState_Object = MibTableColumn
rptrPortPartitionState = _RptrPortPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 3),
    _RptrPortPartitionState_Type()
)
rptrPortPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPartitionState.setStatus("mandatory")
_RptrPortReadableFrames_Type = Counter32
_RptrPortReadableFrames_Object = MibTableColumn
rptrPortReadableFrames = _RptrPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 4),
    _RptrPortReadableFrames_Type()
)
rptrPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortReadableFrames.setStatus("mandatory")
_RptrPortReadableOctets_Type = Counter32
_RptrPortReadableOctets_Object = MibTableColumn
rptrPortReadableOctets = _RptrPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 5),
    _RptrPortReadableOctets_Type()
)
rptrPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortReadableOctets.setStatus("mandatory")
_RptrPortFcsErrors_Type = Counter32
_RptrPortFcsErrors_Object = MibTableColumn
rptrPortFcsErrors = _RptrPortFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 6),
    _RptrPortFcsErrors_Type()
)
rptrPortFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFcsErrors.setStatus("mandatory")
_RptrPortAlignmentErrors_Type = Counter32
_RptrPortAlignmentErrors_Object = MibTableColumn
rptrPortAlignmentErrors = _RptrPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 7),
    _RptrPortAlignmentErrors_Type()
)
rptrPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAlignmentErrors.setStatus("mandatory")
_RptrPortFrameTooLongs_Type = Counter32
_RptrPortFrameTooLongs_Object = MibTableColumn
rptrPortFrameTooLongs = _RptrPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 8),
    _RptrPortFrameTooLongs_Type()
)
rptrPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameTooLongs.setStatus("mandatory")
_RptrPortShortEvents_Type = Counter32
_RptrPortShortEvents_Object = MibTableColumn
rptrPortShortEvents = _RptrPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 9),
    _RptrPortShortEvents_Type()
)
rptrPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortShortEvents.setStatus("mandatory")
_RptrPortRunts_Type = Counter32
_RptrPortRunts_Object = MibTableColumn
rptrPortRunts = _RptrPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 10),
    _RptrPortRunts_Type()
)
rptrPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortRunts.setStatus("mandatory")
_RptrPortCollisions_Type = Counter32
_RptrPortCollisions_Object = MibTableColumn
rptrPortCollisions = _RptrPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 11),
    _RptrPortCollisions_Type()
)
rptrPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortCollisions.setStatus("mandatory")
_RptrPortLateEvents_Type = Counter32
_RptrPortLateEvents_Object = MibTableColumn
rptrPortLateEvents = _RptrPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 12),
    _RptrPortLateEvents_Type()
)
rptrPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortLateEvents.setStatus("mandatory")
_RptrPortVeryLongEvents_Type = Counter32
_RptrPortVeryLongEvents_Object = MibTableColumn
rptrPortVeryLongEvents = _RptrPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 13),
    _RptrPortVeryLongEvents_Type()
)
rptrPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortVeryLongEvents.setStatus("mandatory")
_RptrPortDataRateMismatches_Type = Counter32
_RptrPortDataRateMismatches_Object = MibTableColumn
rptrPortDataRateMismatches = _RptrPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 14),
    _RptrPortDataRateMismatches_Type()
)
rptrPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortDataRateMismatches.setStatus("mandatory")
_RptrPortAutoPartitions_Type = Counter32
_RptrPortAutoPartitions_Object = MibTableColumn
rptrPortAutoPartitions = _RptrPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 15),
    _RptrPortAutoPartitions_Type()
)
rptrPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAutoPartitions.setStatus("mandatory")
_RptrPortTotalErrors_Type = Counter32
_RptrPortTotalErrors_Object = MibTableColumn
rptrPortTotalErrors = _RptrPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 16),
    _RptrPortTotalErrors_Type()
)
rptrPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortTotalErrors.setStatus("mandatory")
_RptrPortLastMACAddress_Type = DisplayString
_RptrPortLastMACAddress_Object = MibTableColumn
rptrPortLastMACAddress = _RptrPortLastMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 17),
    _RptrPortLastMACAddress_Type()
)
rptrPortLastMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortLastMACAddress.setStatus("mandatory")
_RptrPortNumberofMACAddressChanges_Type = Counter32
_RptrPortNumberofMACAddressChanges_Object = MibTableColumn
rptrPortNumberofMACAddressChanges = _RptrPortNumberofMACAddressChanges_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 18),
    _RptrPortNumberofMACAddressChanges_Type()
)
rptrPortNumberofMACAddressChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortNumberofMACAddressChanges.setStatus("mandatory")
_RptrPortSymbolErrors_Type = Counter32
_RptrPortSymbolErrors_Object = MibTableColumn
rptrPortSymbolErrors = _RptrPortSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 14, 1, 19),
    _RptrPortSymbolErrors_Type()
)
rptrPortSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSymbolErrors.setStatus("mandatory")
_RptrChassisSegmentStatTable_Object = MibTable
rptrChassisSegmentStatTable = _RptrChassisSegmentStatTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15)
)
if mibBuilder.loadTexts:
    rptrChassisSegmentStatTable.setStatus("mandatory")
_RptrChassisSegmentStatEntry_Object = MibTableRow
rptrChassisSegmentStatEntry = _RptrChassisSegmentStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1)
)
rptrChassisSegmentStatEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "rptrChassisIndex"),
    (0, "INTEL-EXPRESS110-MIB", "rptrChassisSegmentIndex"),
)
if mibBuilder.loadTexts:
    rptrChassisSegmentStatEntry.setStatus("mandatory")
_RptrChassisIndex_Type = Integer32
_RptrChassisIndex_Object = MibTableColumn
rptrChassisIndex = _RptrChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 1),
    _RptrChassisIndex_Type()
)
rptrChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisIndex.setStatus("mandatory")
_RptrChassisSegmentIndex_Type = Integer32
_RptrChassisSegmentIndex_Object = MibTableColumn
rptrChassisSegmentIndex = _RptrChassisSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 2),
    _RptrChassisSegmentIndex_Type()
)
rptrChassisSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentIndex.setStatus("mandatory")
_RptrChassisSegmentTotalFrames_Type = Counter32
_RptrChassisSegmentTotalFrames_Object = MibTableColumn
rptrChassisSegmentTotalFrames = _RptrChassisSegmentTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 3),
    _RptrChassisSegmentTotalFrames_Type()
)
rptrChassisSegmentTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentTotalFrames.setStatus("mandatory")
_RptrChassisSegmentTotalOctets_Type = Counter32
_RptrChassisSegmentTotalOctets_Object = MibTableColumn
rptrChassisSegmentTotalOctets = _RptrChassisSegmentTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 4),
    _RptrChassisSegmentTotalOctets_Type()
)
rptrChassisSegmentTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentTotalOctets.setStatus("mandatory")
_RptrChassisSegmentTotalErrors_Type = Counter32
_RptrChassisSegmentTotalErrors_Object = MibTableColumn
rptrChassisSegmentTotalErrors = _RptrChassisSegmentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 5),
    _RptrChassisSegmentTotalErrors_Type()
)
rptrChassisSegmentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentTotalErrors.setStatus("mandatory")
_RptrChassisSegmentFCSErrors_Type = Counter32
_RptrChassisSegmentFCSErrors_Object = MibTableColumn
rptrChassisSegmentFCSErrors = _RptrChassisSegmentFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 6),
    _RptrChassisSegmentFCSErrors_Type()
)
rptrChassisSegmentFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentFCSErrors.setStatus("mandatory")
_RptrChassisSegmentAlignmentErrors_Type = Counter32
_RptrChassisSegmentAlignmentErrors_Object = MibTableColumn
rptrChassisSegmentAlignmentErrors = _RptrChassisSegmentAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 7),
    _RptrChassisSegmentAlignmentErrors_Type()
)
rptrChassisSegmentAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentAlignmentErrors.setStatus("mandatory")
_RptrChassisSegmentFrameTooLongs_Type = Counter32
_RptrChassisSegmentFrameTooLongs_Object = MibTableColumn
rptrChassisSegmentFrameTooLongs = _RptrChassisSegmentFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 8),
    _RptrChassisSegmentFrameTooLongs_Type()
)
rptrChassisSegmentFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentFrameTooLongs.setStatus("mandatory")
_RptrChassisSegmentShortEvents_Type = Counter32
_RptrChassisSegmentShortEvents_Object = MibTableColumn
rptrChassisSegmentShortEvents = _RptrChassisSegmentShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 9),
    _RptrChassisSegmentShortEvents_Type()
)
rptrChassisSegmentShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentShortEvents.setStatus("mandatory")
_RptrChassisSegmentRunts_Type = Counter32
_RptrChassisSegmentRunts_Object = MibTableColumn
rptrChassisSegmentRunts = _RptrChassisSegmentRunts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 10),
    _RptrChassisSegmentRunts_Type()
)
rptrChassisSegmentRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentRunts.setStatus("mandatory")
_RptrChassisSegmentCollisions_Type = Counter32
_RptrChassisSegmentCollisions_Object = MibTableColumn
rptrChassisSegmentCollisions = _RptrChassisSegmentCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 11),
    _RptrChassisSegmentCollisions_Type()
)
rptrChassisSegmentCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentCollisions.setStatus("mandatory")
_RptrChassisSegmentLateEvents_Type = Counter32
_RptrChassisSegmentLateEvents_Object = MibTableColumn
rptrChassisSegmentLateEvents = _RptrChassisSegmentLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 12),
    _RptrChassisSegmentLateEvents_Type()
)
rptrChassisSegmentLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentLateEvents.setStatus("mandatory")
_RptrChassisSegmentVeryLongEvents_Type = Counter32
_RptrChassisSegmentVeryLongEvents_Object = MibTableColumn
rptrChassisSegmentVeryLongEvents = _RptrChassisSegmentVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 13),
    _RptrChassisSegmentVeryLongEvents_Type()
)
rptrChassisSegmentVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentVeryLongEvents.setStatus("mandatory")
_RptrChassisSegmentDataRateMismatches_Type = Counter32
_RptrChassisSegmentDataRateMismatches_Object = MibTableColumn
rptrChassisSegmentDataRateMismatches = _RptrChassisSegmentDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 14),
    _RptrChassisSegmentDataRateMismatches_Type()
)
rptrChassisSegmentDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentDataRateMismatches.setStatus("mandatory")
_RptrChassisSegmentAutoPartitions_Type = Counter32
_RptrChassisSegmentAutoPartitions_Object = MibTableColumn
rptrChassisSegmentAutoPartitions = _RptrChassisSegmentAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 15),
    _RptrChassisSegmentAutoPartitions_Type()
)
rptrChassisSegmentAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentAutoPartitions.setStatus("mandatory")
_RptrChassisSegmentSymbolErrors_Type = Counter32
_RptrChassisSegmentSymbolErrors_Object = MibTableColumn
rptrChassisSegmentSymbolErrors = _RptrChassisSegmentSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 15, 1, 16),
    _RptrChassisSegmentSymbolErrors_Type()
)
rptrChassisSegmentSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrChassisSegmentSymbolErrors.setStatus("mandatory")
_TBrdgAdminTable_Object = MibTable
tBrdgAdminTable = _TBrdgAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16)
)
if mibBuilder.loadTexts:
    tBrdgAdminTable.setStatus("mandatory")
_TBrdgAdminEntry_Object = MibTableRow
tBrdgAdminEntry = _TBrdgAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1)
)
tBrdgAdminEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "tBrdgAdminSpanIndex"),
)
if mibBuilder.loadTexts:
    tBrdgAdminEntry.setStatus("mandatory")
_TBrdgAdminSpanIndex_Type = Integer32
_TBrdgAdminSpanIndex_Object = MibTableColumn
tBrdgAdminSpanIndex = _TBrdgAdminSpanIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1, 1),
    _TBrdgAdminSpanIndex_Type()
)
tBrdgAdminSpanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBrdgAdminSpanIndex.setStatus("mandatory")


class _TBrdgAdminState_Type(Integer32):
    """Custom type tBrdgAdminState based on Integer32"""
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


_TBrdgAdminState_Type.__name__ = "Integer32"
_TBrdgAdminState_Object = MibTableColumn
tBrdgAdminState = _TBrdgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1, 2),
    _TBrdgAdminState_Type()
)
tBrdgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tBrdgAdminState.setStatus("mandatory")


class _TBrdgReset_Type(Integer32):
    """Custom type tBrdgReset based on Integer32"""
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
        *(("notSupported", 4),
          ("notreset", 3),
          ("reset", 1),
          ("resetCounters", 2))
    )


_TBrdgReset_Type.__name__ = "Integer32"
_TBrdgReset_Object = MibTableColumn
tBrdgReset = _TBrdgReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1, 3),
    _TBrdgReset_Type()
)
tBrdgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tBrdgReset.setStatus("mandatory")
_TBrdgThrshld_Type = Integer32
_TBrdgThrshld_Object = MibTableColumn
tBrdgThrshld = _TBrdgThrshld_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1, 4),
    _TBrdgThrshld_Type()
)
tBrdgThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tBrdgThrshld.setStatus("mandatory")
_TBrdgPeriod_Type = Integer32
_TBrdgPeriod_Object = MibTableColumn
tBrdgPeriod = _TBrdgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1, 5),
    _TBrdgPeriod_Type()
)
tBrdgPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tBrdgPeriod.setStatus("mandatory")


class _TBrdgLockout_Type(Integer32):
    """Custom type tBrdgLockout based on Integer32"""
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
        *(("nButtonnMgmt", 4),
          ("nButtonyMgmt", 2),
          ("yButtonnMgmt", 3),
          ("yButtonyMgmt", 1))
    )


_TBrdgLockout_Type.__name__ = "Integer32"
_TBrdgLockout_Object = MibTableColumn
tBrdgLockout = _TBrdgLockout_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1, 6),
    _TBrdgLockout_Type()
)
tBrdgLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tBrdgLockout.setStatus("mandatory")
_TBrdgHubId_Type = Integer32
_TBrdgHubId_Object = MibTableColumn
tBrdgHubId = _TBrdgHubId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1, 7),
    _TBrdgHubId_Type()
)
tBrdgHubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBrdgHubId.setStatus("mandatory")
_TBrdgSegments_Type = OctetString
_TBrdgSegments_Object = MibTableColumn
tBrdgSegments = _TBrdgSegments_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 16, 1, 8),
    _TBrdgSegments_Type()
)
tBrdgSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBrdgSegments.setStatus("mandatory")
_TBrdgStatsTable_Object = MibTable
tBrdgStatsTable = _TBrdgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 17)
)
if mibBuilder.loadTexts:
    tBrdgStatsTable.setStatus("mandatory")
_TBrdgStatsEntry_Object = MibTableRow
tBrdgStatsEntry = _TBrdgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 17, 1)
)
tBrdgStatsEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "tBrdgStatsSpan"),
    (0, "INTEL-EXPRESS110-MIB", "tBrdgStatsSegment"),
)
if mibBuilder.loadTexts:
    tBrdgStatsEntry.setStatus("mandatory")
_TBrdgStatsSpan_Type = Integer32
_TBrdgStatsSpan_Object = MibTableColumn
tBrdgStatsSpan = _TBrdgStatsSpan_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 17, 1, 1),
    _TBrdgStatsSpan_Type()
)
tBrdgStatsSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBrdgStatsSpan.setStatus("mandatory")
_TBrdgStatsSegment_Type = Integer32
_TBrdgStatsSegment_Object = MibTableColumn
tBrdgStatsSegment = _TBrdgStatsSegment_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 17, 1, 2),
    _TBrdgStatsSegment_Type()
)
tBrdgStatsSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBrdgStatsSegment.setStatus("mandatory")
_TBrdgUtilIn_Type = Integer32
_TBrdgUtilIn_Object = MibTableColumn
tBrdgUtilIn = _TBrdgUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 17, 1, 3),
    _TBrdgUtilIn_Type()
)
tBrdgUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBrdgUtilIn.setStatus("mandatory")
_TBrdgUtilOut_Type = Integer32
_TBrdgUtilOut_Object = MibTableColumn
tBrdgUtilOut = _TBrdgUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 17, 1, 4),
    _TBrdgUtilOut_Type()
)
tBrdgUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBrdgUtilOut.setStatus("mandatory")
_TBrdgBufferFullCount_Type = Integer32
_TBrdgBufferFullCount_Object = MibTableColumn
tBrdgBufferFullCount = _TBrdgBufferFullCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 17, 1, 5),
    _TBrdgBufferFullCount_Type()
)
tBrdgBufferFullCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBrdgBufferFullCount.setStatus("mandatory")
_StackConfigExtensions_ObjectIdentity = ObjectIdentity
stackConfigExtensions = _StackConfigExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 18)
)


class _StackClearPortSecurity_Type(Integer32):
    """Custom type stackClearPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_StackClearPortSecurity_Type.__name__ = "Integer32"
_StackClearPortSecurity_Object = MibScalar
stackClearPortSecurity = _StackClearPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 18, 1),
    _StackClearPortSecurity_Type()
)
stackClearPortSecurity.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    stackClearPortSecurity.setStatus("mandatory")
_Express_snmp_agents_ObjectIdentity = ObjectIdentity
express_snmp_agents = _Express_snmp_agents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19)
)
_E300agentConfiguration_ObjectIdentity = ObjectIdentity
e300agentConfiguration = _E300agentConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1)
)


class _E300agentVendorName_Type(DisplayString):
    """Custom type e300agentVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_E300agentVendorName_Type.__name__ = "DisplayString"
_E300agentVendorName_Object = MibScalar
e300agentVendorName = _E300agentVendorName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 1),
    _E300agentVendorName_Type()
)
e300agentVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentVendorName.setStatus("mandatory")


class _E300agentProductName_Type(DisplayString):
    """Custom type e300agentProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_E300agentProductName_Type.__name__ = "DisplayString"
_E300agentProductName_Object = MibScalar
e300agentProductName = _E300agentProductName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 2),
    _E300agentProductName_Type()
)
e300agentProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentProductName.setStatus("mandatory")
_E300agentChassisIndex_Type = Integer32
_E300agentChassisIndex_Object = MibScalar
e300agentChassisIndex = _E300agentChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 3),
    _E300agentChassisIndex_Type()
)
e300agentChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentChassisIndex.setStatus("mandatory")
_E300agentModuleIndex_Type = Integer32
_E300agentModuleIndex_Object = MibScalar
e300agentModuleIndex = _E300agentModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 4),
    _E300agentModuleIndex_Type()
)
e300agentModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentModuleIndex.setStatus("mandatory")


class _E300mibversion_Type(DisplayString):
    """Custom type e300mibversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_E300mibversion_Type.__name__ = "DisplayString"
_E300mibversion_Object = MibScalar
e300mibversion = _E300mibversion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 5),
    _E300mibversion_Type()
)
e300mibversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300mibversion.setStatus("mandatory")


class _E300resetAgent_Type(Integer32):
    """Custom type e300resetAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 2),
          ("reset", 1))
    )


_E300resetAgent_Type.__name__ = "Integer32"
_E300resetAgent_Object = MibScalar
e300resetAgent = _E300resetAgent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 6),
    _E300resetAgent_Type()
)
e300resetAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300resetAgent.setStatus("mandatory")


class _E300agentRole_Type(Integer32):
    """Custom type e300agentRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupAgent", 3),
          ("other", 1),
          ("primaryAgent", 2))
    )


_E300agentRole_Type.__name__ = "Integer32"
_E300agentRole_Object = MibScalar
e300agentRole = _E300agentRole_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 7),
    _E300agentRole_Type()
)
e300agentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentRole.setStatus("mandatory")
_E300agentIpBootServerAddr_Type = IpAddress
_E300agentIpBootServerAddr_Object = MibScalar
e300agentIpBootServerAddr = _E300agentIpBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 8),
    _E300agentIpBootServerAddr_Type()
)
e300agentIpBootServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300agentIpBootServerAddr.setStatus("mandatory")
_E300agentIpUnauthAddr_Type = IpAddress
_E300agentIpUnauthAddr_Object = MibScalar
e300agentIpUnauthAddr = _E300agentIpUnauthAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 9),
    _E300agentIpUnauthAddr_Type()
)
e300agentIpUnauthAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentIpUnauthAddr.setStatus("mandatory")


class _E300agentIpUnauthComm_Type(DisplayString):
    """Custom type e300agentIpUnauthComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_E300agentIpUnauthComm_Type.__name__ = "DisplayString"
_E300agentIpUnauthComm_Object = MibScalar
e300agentIpUnauthComm = _E300agentIpUnauthComm_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 10),
    _E300agentIpUnauthComm_Type()
)
e300agentIpUnauthComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentIpUnauthComm.setStatus("mandatory")
_E300agentIpLastBootServerAddr_Type = IpAddress
_E300agentIpLastBootServerAddr_Object = MibScalar
e300agentIpLastBootServerAddr = _E300agentIpLastBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 11),
    _E300agentIpLastBootServerAddr_Type()
)
e300agentIpLastBootServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentIpLastBootServerAddr.setStatus("mandatory")
_E300agentIpLastIpAddr_Type = IpAddress
_E300agentIpLastIpAddr_Object = MibScalar
e300agentIpLastIpAddr = _E300agentIpLastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 1, 12),
    _E300agentIpLastIpAddr_Type()
)
e300agentIpLastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300agentIpLastIpAddr.setStatus("mandatory")
_E300ipConfiguration_ObjectIdentity = ObjectIdentity
e300ipConfiguration = _E300ipConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2)
)


class _E300ipAddressMethodInUse_Type(Integer32):
    """Custom type e300ipAddressMethodInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("fixed", 1))
    )


_E300ipAddressMethodInUse_Type.__name__ = "Integer32"
_E300ipAddressMethodInUse_Object = MibScalar
e300ipAddressMethodInUse = _E300ipAddressMethodInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 1),
    _E300ipAddressMethodInUse_Type()
)
e300ipAddressMethodInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300ipAddressMethodInUse.setStatus("mandatory")
_E300ipAddressInUse_Type = IpAddress
_E300ipAddressInUse_Object = MibScalar
e300ipAddressInUse = _E300ipAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 2),
    _E300ipAddressInUse_Type()
)
e300ipAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300ipAddressInUse.setStatus("mandatory")
_E300gatewayorRouterAddrInUse_Type = IpAddress
_E300gatewayorRouterAddrInUse_Object = MibScalar
e300gatewayorRouterAddrInUse = _E300gatewayorRouterAddrInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 3),
    _E300gatewayorRouterAddrInUse_Type()
)
e300gatewayorRouterAddrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300gatewayorRouterAddrInUse.setStatus("mandatory")
_E300networkMaskInUse_Type = IpAddress
_E300networkMaskInUse_Object = MibScalar
e300networkMaskInUse = _E300networkMaskInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 4),
    _E300networkMaskInUse_Type()
)
e300networkMaskInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300networkMaskInUse.setStatus("mandatory")
_E300broadcastAddressInUse_Type = IpAddress
_E300broadcastAddressInUse_Object = MibScalar
e300broadcastAddressInUse = _E300broadcastAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 5),
    _E300broadcastAddressInUse_Type()
)
e300broadcastAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300broadcastAddressInUse.setStatus("mandatory")


class _E300ipAddressMethodNextReset_Type(Integer32):
    """Custom type e300ipAddressMethodNextReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("fixed", 1))
    )


_E300ipAddressMethodNextReset_Type.__name__ = "Integer32"
_E300ipAddressMethodNextReset_Object = MibScalar
e300ipAddressMethodNextReset = _E300ipAddressMethodNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 6),
    _E300ipAddressMethodNextReset_Type()
)
e300ipAddressMethodNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300ipAddressMethodNextReset.setStatus("mandatory")
_E300ipAddressNextReset_Type = IpAddress
_E300ipAddressNextReset_Object = MibScalar
e300ipAddressNextReset = _E300ipAddressNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 7),
    _E300ipAddressNextReset_Type()
)
e300ipAddressNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300ipAddressNextReset.setStatus("mandatory")
_E300gatewayorRouterAddrNextReset_Type = IpAddress
_E300gatewayorRouterAddrNextReset_Object = MibScalar
e300gatewayorRouterAddrNextReset = _E300gatewayorRouterAddrNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 8),
    _E300gatewayorRouterAddrNextReset_Type()
)
e300gatewayorRouterAddrNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300gatewayorRouterAddrNextReset.setStatus("mandatory")
_E300networkMaskNextReset_Type = IpAddress
_E300networkMaskNextReset_Object = MibScalar
e300networkMaskNextReset = _E300networkMaskNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 2, 9),
    _E300networkMaskNextReset_Type()
)
e300networkMaskNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300networkMaskNextReset.setStatus("mandatory")
_E300snmpConfiguration_ObjectIdentity = ObjectIdentity
e300snmpConfiguration = _E300snmpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3)
)


class _E300snmpReadCommunityString_Type(DisplayString):
    """Custom type e300snmpReadCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_E300snmpReadCommunityString_Type.__name__ = "DisplayString"
_E300snmpReadCommunityString_Object = MibScalar
e300snmpReadCommunityString = _E300snmpReadCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 1),
    _E300snmpReadCommunityString_Type()
)
e300snmpReadCommunityString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    e300snmpReadCommunityString.setStatus("mandatory")


class _E300snmpWriteCommunityString_Type(DisplayString):
    """Custom type e300snmpWriteCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_E300snmpWriteCommunityString_Type.__name__ = "DisplayString"
_E300snmpWriteCommunityString_Object = MibScalar
e300snmpWriteCommunityString = _E300snmpWriteCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 2),
    _E300snmpWriteCommunityString_Type()
)
e300snmpWriteCommunityString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    e300snmpWriteCommunityString.setStatus("mandatory")
_E300snmpTrapReceiverMAX_Type = Integer32
_E300snmpTrapReceiverMAX_Object = MibScalar
e300snmpTrapReceiverMAX = _E300snmpTrapReceiverMAX_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 3),
    _E300snmpTrapReceiverMAX_Type()
)
e300snmpTrapReceiverMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300snmpTrapReceiverMAX.setStatus("mandatory")
_E300snmpTrapReceiverNumber_Type = Integer32
_E300snmpTrapReceiverNumber_Object = MibScalar
e300snmpTrapReceiverNumber = _E300snmpTrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 4),
    _E300snmpTrapReceiverNumber_Type()
)
e300snmpTrapReceiverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300snmpTrapReceiverNumber.setStatus("mandatory")
_E300snmpTrapAddressTable_Object = MibTable
e300snmpTrapAddressTable = _E300snmpTrapAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 5)
)
if mibBuilder.loadTexts:
    e300snmpTrapAddressTable.setStatus("mandatory")
_E300snmpTrapAddressEntry_Object = MibTableRow
e300snmpTrapAddressEntry = _E300snmpTrapAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 5, 1)
)
e300snmpTrapAddressEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "e300trapAddrIndex"),
)
if mibBuilder.loadTexts:
    e300snmpTrapAddressEntry.setStatus("mandatory")
_E300trapAddrIndex_Type = Integer32
_E300trapAddrIndex_Object = MibTableColumn
e300trapAddrIndex = _E300trapAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 5, 1, 1),
    _E300trapAddrIndex_Type()
)
e300trapAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300trapAddrIndex.setStatus("mandatory")
_E300trapIPAddr_Type = IpAddress
_E300trapIPAddr_Object = MibTableColumn
e300trapIPAddr = _E300trapIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 5, 1, 2),
    _E300trapIPAddr_Type()
)
e300trapIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300trapIPAddr.setStatus("mandatory")


class _E300trapCommunityString_Type(DisplayString):
    """Custom type e300trapCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_E300trapCommunityString_Type.__name__ = "DisplayString"
_E300trapCommunityString_Object = MibTableColumn
e300trapCommunityString = _E300trapCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 5, 1, 3),
    _E300trapCommunityString_Type()
)
e300trapCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300trapCommunityString.setStatus("mandatory")


class _E300trapStatus_Type(Integer32):
    """Custom type e300trapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("ignore", 2))
    )


_E300trapStatus_Type.__name__ = "Integer32"
_E300trapStatus_Object = MibTableColumn
e300trapStatus = _E300trapStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 3, 5, 1, 4),
    _E300trapStatus_Type()
)
e300trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300trapStatus.setStatus("mandatory")
_E300agentExtConfiguration_ObjectIdentity = ObjectIdentity
e300agentExtConfiguration = _E300agentExtConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 4)
)


class _E300agentSwUpdateMode_Type(Integer32):
    """Custom type e300agentSwUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network-load", 2),
          ("other", 1),
          ("out-of-band-load", 3))
    )


_E300agentSwUpdateMode_Type.__name__ = "Integer32"
_E300agentSwUpdateMode_Object = MibScalar
e300agentSwUpdateMode = _E300agentSwUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 4, 1),
    _E300agentSwUpdateMode_Type()
)
e300agentSwUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300agentSwUpdateMode.setStatus("mandatory")


class _E300agentConfigUpdateCtrl_Type(Integer32):
    """Custom type e300agentConfigUpdateCtrl based on Integer32"""
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


_E300agentConfigUpdateCtrl_Type.__name__ = "Integer32"
_E300agentConfigUpdateCtrl_Object = MibScalar
e300agentConfigUpdateCtrl = _E300agentConfigUpdateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 4, 2),
    _E300agentConfigUpdateCtrl_Type()
)
e300agentConfigUpdateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300agentConfigUpdateCtrl.setStatus("mandatory")


class _E300agentConfigFilename_Type(DisplayString):
    """Custom type e300agentConfigFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_E300agentConfigFilename_Type.__name__ = "DisplayString"
_E300agentConfigFilename_Object = MibScalar
e300agentConfigFilename = _E300agentConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 4, 3),
    _E300agentConfigFilename_Type()
)
e300agentConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300agentConfigFilename.setStatus("mandatory")


class _E300agentImageUpdateCtrl_Type(Integer32):
    """Custom type e300agentImageUpdateCtrl based on Integer32"""
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


_E300agentImageUpdateCtrl_Type.__name__ = "Integer32"
_E300agentImageUpdateCtrl_Object = MibScalar
e300agentImageUpdateCtrl = _E300agentImageUpdateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 4, 4),
    _E300agentImageUpdateCtrl_Type()
)
e300agentImageUpdateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300agentImageUpdateCtrl.setStatus("mandatory")


class _E300agentImageFilename_Type(DisplayString):
    """Custom type e300agentImageFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_E300agentImageFilename_Type.__name__ = "DisplayString"
_E300agentImageFilename_Object = MibScalar
e300agentImageFilename = _E300agentImageFilename_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 4, 5),
    _E300agentImageFilename_Type()
)
e300agentImageFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300agentImageFilename.setStatus("mandatory")


class _E300agentRs232PortConfig_Type(Integer32):
    """Custom type e300agentRs232PortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 2),
          ("other", 1),
          ("out-of-band", 3))
    )


_E300agentRs232PortConfig_Type.__name__ = "Integer32"
_E300agentRs232PortConfig_Object = MibScalar
e300agentRs232PortConfig = _E300agentRs232PortConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 4, 6),
    _E300agentRs232PortConfig_Type()
)
e300agentRs232PortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300agentRs232PortConfig.setStatus("mandatory")


class _E300agentOutOfBandBaudRateConfig_Type(Integer32):
    """Custom type e300agentOutOfBandBaudRateConfig based on Integer32"""
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
        *(("baudRate-1200", 2),
          ("baudRate-19200", 5),
          ("baudRate-2400", 3),
          ("baudRate-9600", 4),
          ("other", 1))
    )


_E300agentOutOfBandBaudRateConfig_Type.__name__ = "Integer32"
_E300agentOutOfBandBaudRateConfig_Object = MibScalar
e300agentOutOfBandBaudRateConfig = _E300agentOutOfBandBaudRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 4, 7),
    _E300agentOutOfBandBaudRateConfig_Type()
)
e300agentOutOfBandBaudRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300agentOutOfBandBaudRateConfig.setStatus("mandatory")
_E300slipConfiguration_ObjectIdentity = ObjectIdentity
e300slipConfiguration = _E300slipConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 5)
)
_E300slipAddressInUse_Type = IpAddress
_E300slipAddressInUse_Object = MibScalar
e300slipAddressInUse = _E300slipAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 5, 1),
    _E300slipAddressInUse_Type()
)
e300slipAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300slipAddressInUse.setStatus("mandatory")
_E300slipGatewayorRouterAddrInUse_Type = IpAddress
_E300slipGatewayorRouterAddrInUse_Object = MibScalar
e300slipGatewayorRouterAddrInUse = _E300slipGatewayorRouterAddrInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 5, 2),
    _E300slipGatewayorRouterAddrInUse_Type()
)
e300slipGatewayorRouterAddrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300slipGatewayorRouterAddrInUse.setStatus("mandatory")
_E300slipNetworkMaskInUse_Type = IpAddress
_E300slipNetworkMaskInUse_Object = MibScalar
e300slipNetworkMaskInUse = _E300slipNetworkMaskInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 5, 3),
    _E300slipNetworkMaskInUse_Type()
)
e300slipNetworkMaskInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300slipNetworkMaskInUse.setStatus("mandatory")
_E300slipBroadcastAddressInUse_Type = IpAddress
_E300slipBroadcastAddressInUse_Object = MibScalar
e300slipBroadcastAddressInUse = _E300slipBroadcastAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 5, 4),
    _E300slipBroadcastAddressInUse_Type()
)
e300slipBroadcastAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300slipBroadcastAddressInUse.setStatus("mandatory")
_E300slipAddressNextReset_Type = IpAddress
_E300slipAddressNextReset_Object = MibScalar
e300slipAddressNextReset = _E300slipAddressNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 5, 5),
    _E300slipAddressNextReset_Type()
)
e300slipAddressNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300slipAddressNextReset.setStatus("mandatory")
_E300slipGatewayorRouterAddrNextReset_Type = IpAddress
_E300slipGatewayorRouterAddrNextReset_Object = MibScalar
e300slipGatewayorRouterAddrNextReset = _E300slipGatewayorRouterAddrNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 5, 6),
    _E300slipGatewayorRouterAddrNextReset_Type()
)
e300slipGatewayorRouterAddrNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300slipGatewayorRouterAddrNextReset.setStatus("mandatory")
_E300slipNetworkMaskNextReset_Type = IpAddress
_E300slipNetworkMaskNextReset_Object = MibScalar
e300slipNetworkMaskNextReset = _E300slipNetworkMaskNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 5, 7),
    _E300slipNetworkMaskNextReset_Type()
)
e300slipNetworkMaskNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e300slipNetworkMaskNextReset.setStatus("mandatory")
_E300mgmtBasicInfoTable_Object = MibTable
e300mgmtBasicInfoTable = _E300mgmtBasicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 6)
)
if mibBuilder.loadTexts:
    e300mgmtBasicInfoTable.setStatus("mandatory")
_E300mgmtBasicInfoEntry_Object = MibTableRow
e300mgmtBasicInfoEntry = _E300mgmtBasicInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 6, 1)
)
e300mgmtBasicInfoEntry.setIndexNames(
    (0, "INTEL-EXPRESS110-MIB", "e300mgmtChassisIndex"),
)
if mibBuilder.loadTexts:
    e300mgmtBasicInfoEntry.setStatus("mandatory")
_E300mgmtChassisIndex_Type = Integer32
_E300mgmtChassisIndex_Object = MibTableColumn
e300mgmtChassisIndex = _E300mgmtChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 6, 1, 1),
    _E300mgmtChassisIndex_Type()
)
e300mgmtChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300mgmtChassisIndex.setStatus("mandatory")
_E300mgmtIPAddress_Type = IpAddress
_E300mgmtIPAddress_Object = MibTableColumn
e300mgmtIPAddress = _E300mgmtIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 6, 1, 2),
    _E300mgmtIPAddress_Type()
)
e300mgmtIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300mgmtIPAddress.setStatus("mandatory")
_E300mgmtPhysicalAddress_Type = PhysAddress
_E300mgmtPhysicalAddress_Object = MibTableColumn
e300mgmtPhysicalAddress = _E300mgmtPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 6, 1, 3),
    _E300mgmtPhysicalAddress_Type()
)
e300mgmtPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300mgmtPhysicalAddress.setStatus("mandatory")


class _E300mgmtRole_Type(Integer32):
    """Custom type e300mgmtRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupAgent", 3),
          ("other", 1),
          ("primaryAgent", 2))
    )


_E300mgmtRole_Type.__name__ = "Integer32"
_E300mgmtRole_Object = MibTableColumn
e300mgmtRole = _E300mgmtRole_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 19, 6, 1, 4),
    _E300mgmtRole_Type()
)
e300mgmtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e300mgmtRole.setStatus("mandatory")

# Managed Objects groups


# Notification objects

utilizationThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 0)
)
utilizationThresholdExceeded.setObjects(
    ("INTEL-EXPRESS110-MIB", "rptrSegmentStatIndex")
)
if mibBuilder.loadTexts:
    utilizationThresholdExceeded.setStatus(
        ""
    )

collisionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 1)
)
collisionThresholdExceeded.setObjects(
    ("INTEL-EXPRESS110-MIB", "rptrSegmentStatIndex")
)
if mibBuilder.loadTexts:
    collisionThresholdExceeded.setStatus(
        ""
    )

configurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 2)
)
configurationChange.setObjects(
    ("INTEL-EXPRESS110-MIB", "hubDescriptionString")
)
if mibBuilder.loadTexts:
    configurationChange.setStatus(
        ""
    )

tBrdgBufferFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 3)
)
if mibBuilder.loadTexts:
    tBrdgBufferFull.setStatus(
        ""
    )

chassisRPSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 4)
)
chassisRPSActive.setObjects(
    ("INTEL-EXPRESS110-MIB", "chassisConfigTableIndex")
)
if mibBuilder.loadTexts:
    chassisRPSActive.setStatus(
        ""
    )

portSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 5)
)
portSecurityViolation.setObjects(
      *(("INTEL-EXPRESS110-MIB", "chassisConfigTableIndex"),
        ("INTEL-EXPRESS110-MIB", "portIndex"))
)
if mibBuilder.loadTexts:
    portSecurityViolation.setStatus(
        ""
    )

mgmtSwitchedToBackupMgmt = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 6)
)
mgmtSwitchedToBackupMgmt.setObjects(
    ("INTEL-EXPRESS110-MIB", "chassisConfigTableIndex")
)
if mibBuilder.loadTexts:
    mgmtSwitchedToBackupMgmt.setStatus(
        ""
    )

bridgeConfigChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 7)
)
bridgeConfigChangeEvent.setObjects(
    ("INTEL-EXPRESS110-MIB", "tBrdgHubId")
)
if mibBuilder.loadTexts:
    bridgeConfigChangeEvent.setStatus(
        ""
    )

bridgeConfigNoBridgeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 8)
)
if mibBuilder.loadTexts:
    bridgeConfigNoBridgeEvent.setStatus(
        ""
    )

portlinkChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 9)
)
portlinkChangeEvent.setObjects(
      *(("INTEL-EXPRESS110-MIB", "portChassisIndex"),
        ("INTEL-EXPRESS110-MIB", "portModuleIndex"),
        ("INTEL-EXPRESS110-MIB", "portIndex"),
        ("INTEL-EXPRESS110-MIB", "portType"),
        ("INTEL-EXPRESS110-MIB", "portOperStatus"),
        ("INTEL-EXPRESS110-MIB", "portLinkTestStatusTrapCtrl"))
)
if mibBuilder.loadTexts:
    portlinkChangeEvent.setStatus(
        ""
    )

portSpeedChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1, 0, 10)
)
portSpeedChangeEvent.setObjects(
      *(("INTEL-EXPRESS110-MIB", "portChassisIndex"),
        ("INTEL-EXPRESS110-MIB", "portModuleIndex"),
        ("INTEL-EXPRESS110-MIB", "portIndex"),
        ("INTEL-EXPRESS110-MIB", "portType"),
        ("INTEL-EXPRESS110-MIB", "portLinkSpeed"),
        ("INTEL-EXPRESS110-MIB", "portSpeedStatusTrapCtrl"))
)
if mibBuilder.loadTexts:
    portSpeedChangeEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-EXPRESS110-MIB",
    **{"express110": express110,
       "utilizationThresholdExceeded": utilizationThresholdExceeded,
       "collisionThresholdExceeded": collisionThresholdExceeded,
       "configurationChange": configurationChange,
       "tBrdgBufferFull": tBrdgBufferFull,
       "chassisRPSActive": chassisRPSActive,
       "portSecurityViolation": portSecurityViolation,
       "mgmtSwitchedToBackupMgmt": mgmtSwitchedToBackupMgmt,
       "bridgeConfigChangeEvent": bridgeConfigChangeEvent,
       "bridgeConfigNoBridgeEvent": bridgeConfigNoBridgeEvent,
       "portlinkChangeEvent": portlinkChangeEvent,
       "portSpeedChangeEvent": portSpeedChangeEvent,
       "hubNumberofStackedChassis": hubNumberofStackedChassis,
       "hubDescriptionString": hubDescriptionString,
       "hubStackReset": hubStackReset,
       "hubLCDModeVariable": hubLCDModeVariable,
       "hubLCDSleepText": hubLCDSleepText,
       "hubLCDSleepTime": hubLCDSleepTime,
       "hubRFC1516Segment": hubRFC1516Segment,
       "chassisConfigTable": chassisConfigTable,
       "chassisConfigEntry": chassisConfigEntry,
       "chassisConfigTableIndex": chassisConfigTableIndex,
       "chassisSegmentMode": chassisSegmentMode,
       "chassisReset": chassisReset,
       "chassisRPSState": chassisRPSState,
       "chassisIsolate": chassisIsolate,
       "moduleConfigStatusTable": moduleConfigStatusTable,
       "moduleConfigStatusEntry": moduleConfigStatusEntry,
       "moduleChassisIndex": moduleChassisIndex,
       "moduleIndex": moduleIndex,
       "moduleType": moduleType,
       "moduleUserAssignedType": moduleUserAssignedType,
       "moduleUserAssignedNumber": moduleUserAssignedNumber,
       "moduleUserAssignedName": moduleUserAssignedName,
       "moduleSizeofROM": moduleSizeofROM,
       "moduleSizeofRAM": moduleSizeofRAM,
       "moduleHWDescription": moduleHWDescription,
       "moduleAgentSWVersion": moduleAgentSWVersion,
       "moduleBootSWVersion": moduleBootSWVersion,
       "moduleManufacturingInfo": moduleManufacturingInfo,
       "moduleTotalPortCount": moduleTotalPortCount,
       "moduleExternalPortCount": moduleExternalPortCount,
       "moduleSegmentLockout": moduleSegmentLockout,
       "moduleLEDInfo": moduleLEDInfo,
       "moduleLastErrorID": moduleLastErrorID,
       "moduleMediaDevicesReset": moduleMediaDevicesReset,
       "moduleImageFileSource": moduleImageFileSource,
       "moduleImageFileName": moduleImageFileName,
       "moduleImageDownloadControl": moduleImageDownloadControl,
       "moduleImageDownloadStatus": moduleImageDownloadStatus,
       "moduleOperationalStatus": moduleOperationalStatus,
       "moduleUptime": moduleUptime,
       "moduleReset": moduleReset,
       "moduleAllPortLEDInfo": moduleAllPortLEDInfo,
       "moduleAllPortAdminStatus": moduleAllPortAdminStatus,
       "moduleAllPortOperStatus": moduleAllPortOperStatus,
       "moduleAllPortSpeed": moduleAllPortSpeed,
       "moduleAllPortSpeedInfo": moduleAllPortSpeedInfo,
       "moduleSegmentMode": moduleSegmentMode,
       "moduleAllPortLinkPartnerInfo": moduleAllPortLinkPartnerInfo,
       "moduleAllPortCounterReset": moduleAllPortCounterReset,
       "moduleAllPortTimeSinceLinkChange": moduleAllPortTimeSinceLinkChange,
       "modulePersistentMemoryReset": modulePersistentMemoryReset,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portChassisIndex": portChassisIndex,
       "portModuleIndex": portModuleIndex,
       "portIndex": portIndex,
       "portType": portType,
       "portAdminStatus": portAdminStatus,
       "portOperStatus": portOperStatus,
       "portJabber": portJabber,
       "portLinkPartnerInfo": portLinkPartnerInfo,
       "portLEDInfo": portLEDInfo,
       "portTimeSinceLastLinkChange": portTimeSinceLastLinkChange,
       "portAllCountersReset": portAllCountersReset,
       "portReset": portReset,
       "portLastErrorID": portLastErrorID,
       "portSegmentAdminMode": portSegmentAdminMode,
       "portSegmentOperStatus": portSegmentOperStatus,
       "portLinkSpeed": portLinkSpeed,
       "portSecureAdminMode": portSecureAdminMode,
       "portSecureMAC": portSecureMAC,
       "portLinkTestState": portLinkTestState,
       "portLinkTestStatusTrapCtrl": portLinkTestStatusTrapCtrl,
       "portSpeedStatusTrapCtrl": portSpeedStatusTrapCtrl,
       "portPolarityStatus": portPolarityStatus,
       "rptrSegmentConfigTable": rptrSegmentConfigTable,
       "rptrSegmentConfigEntry": rptrSegmentConfigEntry,
       "rptrSegmentConfigIndex": rptrSegmentConfigIndex,
       "rptrSegmentOperationalStatus": rptrSegmentOperationalStatus,
       "rptrSegmentZeroCounters": rptrSegmentZeroCounters,
       "rptrSegmentReset": rptrSegmentReset,
       "rptrSegmentResetMedia": rptrSegmentResetMedia,
       "rptrSegmentPartitionThreshold": rptrSegmentPartitionThreshold,
       "rptrSegmentNonDisruptTest": rptrSegmentNonDisruptTest,
       "rptrSegmentUtilizationTrapThreshold": rptrSegmentUtilizationTrapThreshold,
       "rptrSegmentCollisionTrapThreshold": rptrSegmentCollisionTrapThreshold,
       "rptrSegmentUtilizationTrapPeriod": rptrSegmentUtilizationTrapPeriod,
       "rptrSegmentCollisionTrapPeriod": rptrSegmentCollisionTrapPeriod,
       "rptrSegmentSpeed": rptrSegmentSpeed,
       "rptrSegmentStatTable": rptrSegmentStatTable,
       "rptrSegmentStatEntry": rptrSegmentStatEntry,
       "rptrSegmentStatIndex": rptrSegmentStatIndex,
       "rptrSegmentTotalFrames": rptrSegmentTotalFrames,
       "rptrSegmentTotalOctets": rptrSegmentTotalOctets,
       "rptrSegmentTotalErrors": rptrSegmentTotalErrors,
       "rptrSegmentTotalCollisions": rptrSegmentTotalCollisions,
       "rptrSegmentPartitionedPorts": rptrSegmentPartitionedPorts,
       "rptrSegmentHealthText": rptrSegmentHealthText,
       "rptrSegmentUtilization": rptrSegmentUtilization,
       "rptrModuleStatTable": rptrModuleStatTable,
       "rptrModuleStatEntry": rptrModuleStatEntry,
       "rptrModuleIndex": rptrModuleIndex,
       "rptrModuleTotalFrames": rptrModuleTotalFrames,
       "rptrModuleTotalOctets": rptrModuleTotalOctets,
       "rptrModuleTotalErrors": rptrModuleTotalErrors,
       "rptrModuleFCSErrors": rptrModuleFCSErrors,
       "rptrModuleAlignmentErrors": rptrModuleAlignmentErrors,
       "rptrModuleFrameTooLongs": rptrModuleFrameTooLongs,
       "rptrModuleShortEvents": rptrModuleShortEvents,
       "rptrModuleRunts": rptrModuleRunts,
       "rptrModuleCollisions": rptrModuleCollisions,
       "rptrModuleLateEvents": rptrModuleLateEvents,
       "rptrModuleVeryLongEvents": rptrModuleVeryLongEvents,
       "rptrModuleDataRateMismatches": rptrModuleDataRateMismatches,
       "rptrModuleAutoPartitions": rptrModuleAutoPartitions,
       "rptrPortStatTable": rptrPortStatTable,
       "rptrPortStatEntry": rptrPortStatEntry,
       "rptrPortChassisIndex": rptrPortChassisIndex,
       "rptrPortIndex": rptrPortIndex,
       "rptrPortPartitionState": rptrPortPartitionState,
       "rptrPortReadableFrames": rptrPortReadableFrames,
       "rptrPortReadableOctets": rptrPortReadableOctets,
       "rptrPortFcsErrors": rptrPortFcsErrors,
       "rptrPortAlignmentErrors": rptrPortAlignmentErrors,
       "rptrPortFrameTooLongs": rptrPortFrameTooLongs,
       "rptrPortShortEvents": rptrPortShortEvents,
       "rptrPortRunts": rptrPortRunts,
       "rptrPortCollisions": rptrPortCollisions,
       "rptrPortLateEvents": rptrPortLateEvents,
       "rptrPortVeryLongEvents": rptrPortVeryLongEvents,
       "rptrPortDataRateMismatches": rptrPortDataRateMismatches,
       "rptrPortAutoPartitions": rptrPortAutoPartitions,
       "rptrPortTotalErrors": rptrPortTotalErrors,
       "rptrPortLastMACAddress": rptrPortLastMACAddress,
       "rptrPortNumberofMACAddressChanges": rptrPortNumberofMACAddressChanges,
       "rptrPortSymbolErrors": rptrPortSymbolErrors,
       "rptrChassisSegmentStatTable": rptrChassisSegmentStatTable,
       "rptrChassisSegmentStatEntry": rptrChassisSegmentStatEntry,
       "rptrChassisIndex": rptrChassisIndex,
       "rptrChassisSegmentIndex": rptrChassisSegmentIndex,
       "rptrChassisSegmentTotalFrames": rptrChassisSegmentTotalFrames,
       "rptrChassisSegmentTotalOctets": rptrChassisSegmentTotalOctets,
       "rptrChassisSegmentTotalErrors": rptrChassisSegmentTotalErrors,
       "rptrChassisSegmentFCSErrors": rptrChassisSegmentFCSErrors,
       "rptrChassisSegmentAlignmentErrors": rptrChassisSegmentAlignmentErrors,
       "rptrChassisSegmentFrameTooLongs": rptrChassisSegmentFrameTooLongs,
       "rptrChassisSegmentShortEvents": rptrChassisSegmentShortEvents,
       "rptrChassisSegmentRunts": rptrChassisSegmentRunts,
       "rptrChassisSegmentCollisions": rptrChassisSegmentCollisions,
       "rptrChassisSegmentLateEvents": rptrChassisSegmentLateEvents,
       "rptrChassisSegmentVeryLongEvents": rptrChassisSegmentVeryLongEvents,
       "rptrChassisSegmentDataRateMismatches": rptrChassisSegmentDataRateMismatches,
       "rptrChassisSegmentAutoPartitions": rptrChassisSegmentAutoPartitions,
       "rptrChassisSegmentSymbolErrors": rptrChassisSegmentSymbolErrors,
       "tBrdgAdminTable": tBrdgAdminTable,
       "tBrdgAdminEntry": tBrdgAdminEntry,
       "tBrdgAdminSpanIndex": tBrdgAdminSpanIndex,
       "tBrdgAdminState": tBrdgAdminState,
       "tBrdgReset": tBrdgReset,
       "tBrdgThrshld": tBrdgThrshld,
       "tBrdgPeriod": tBrdgPeriod,
       "tBrdgLockout": tBrdgLockout,
       "tBrdgHubId": tBrdgHubId,
       "tBrdgSegments": tBrdgSegments,
       "tBrdgStatsTable": tBrdgStatsTable,
       "tBrdgStatsEntry": tBrdgStatsEntry,
       "tBrdgStatsSpan": tBrdgStatsSpan,
       "tBrdgStatsSegment": tBrdgStatsSegment,
       "tBrdgUtilIn": tBrdgUtilIn,
       "tBrdgUtilOut": tBrdgUtilOut,
       "tBrdgBufferFullCount": tBrdgBufferFullCount,
       "stackConfigExtensions": stackConfigExtensions,
       "stackClearPortSecurity": stackClearPortSecurity,
       "express-snmp-agents": express_snmp_agents,
       "e300agentConfiguration": e300agentConfiguration,
       "e300agentVendorName": e300agentVendorName,
       "e300agentProductName": e300agentProductName,
       "e300agentChassisIndex": e300agentChassisIndex,
       "e300agentModuleIndex": e300agentModuleIndex,
       "e300mibversion": e300mibversion,
       "e300resetAgent": e300resetAgent,
       "e300agentRole": e300agentRole,
       "e300agentIpBootServerAddr": e300agentIpBootServerAddr,
       "e300agentIpUnauthAddr": e300agentIpUnauthAddr,
       "e300agentIpUnauthComm": e300agentIpUnauthComm,
       "e300agentIpLastBootServerAddr": e300agentIpLastBootServerAddr,
       "e300agentIpLastIpAddr": e300agentIpLastIpAddr,
       "e300ipConfiguration": e300ipConfiguration,
       "e300ipAddressMethodInUse": e300ipAddressMethodInUse,
       "e300ipAddressInUse": e300ipAddressInUse,
       "e300gatewayorRouterAddrInUse": e300gatewayorRouterAddrInUse,
       "e300networkMaskInUse": e300networkMaskInUse,
       "e300broadcastAddressInUse": e300broadcastAddressInUse,
       "e300ipAddressMethodNextReset": e300ipAddressMethodNextReset,
       "e300ipAddressNextReset": e300ipAddressNextReset,
       "e300gatewayorRouterAddrNextReset": e300gatewayorRouterAddrNextReset,
       "e300networkMaskNextReset": e300networkMaskNextReset,
       "e300snmpConfiguration": e300snmpConfiguration,
       "e300snmpReadCommunityString": e300snmpReadCommunityString,
       "e300snmpWriteCommunityString": e300snmpWriteCommunityString,
       "e300snmpTrapReceiverMAX": e300snmpTrapReceiverMAX,
       "e300snmpTrapReceiverNumber": e300snmpTrapReceiverNumber,
       "e300snmpTrapAddressTable": e300snmpTrapAddressTable,
       "e300snmpTrapAddressEntry": e300snmpTrapAddressEntry,
       "e300trapAddrIndex": e300trapAddrIndex,
       "e300trapIPAddr": e300trapIPAddr,
       "e300trapCommunityString": e300trapCommunityString,
       "e300trapStatus": e300trapStatus,
       "e300agentExtConfiguration": e300agentExtConfiguration,
       "e300agentSwUpdateMode": e300agentSwUpdateMode,
       "e300agentConfigUpdateCtrl": e300agentConfigUpdateCtrl,
       "e300agentConfigFilename": e300agentConfigFilename,
       "e300agentImageUpdateCtrl": e300agentImageUpdateCtrl,
       "e300agentImageFilename": e300agentImageFilename,
       "e300agentRs232PortConfig": e300agentRs232PortConfig,
       "e300agentOutOfBandBaudRateConfig": e300agentOutOfBandBaudRateConfig,
       "e300slipConfiguration": e300slipConfiguration,
       "e300slipAddressInUse": e300slipAddressInUse,
       "e300slipGatewayorRouterAddrInUse": e300slipGatewayorRouterAddrInUse,
       "e300slipNetworkMaskInUse": e300slipNetworkMaskInUse,
       "e300slipBroadcastAddressInUse": e300slipBroadcastAddressInUse,
       "e300slipAddressNextReset": e300slipAddressNextReset,
       "e300slipGatewayorRouterAddrNextReset": e300slipGatewayorRouterAddrNextReset,
       "e300slipNetworkMaskNextReset": e300slipNetworkMaskNextReset,
       "e300mgmtBasicInfoTable": e300mgmtBasicInfoTable,
       "e300mgmtBasicInfoEntry": e300mgmtBasicInfoEntry,
       "e300mgmtChassisIndex": e300mgmtChassisIndex,
       "e300mgmtIPAddress": e300mgmtIPAddress,
       "e300mgmtPhysicalAddress": e300mgmtPhysicalAddress,
       "e300mgmtRole": e300mgmtRole}
)
