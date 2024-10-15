# SNMP MIB module (AdaptecArrayController-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AdaptecArrayController-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:04 2024
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

_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3)
)
_AdaptecArrayController_ObjectIdentity = ObjectIdentity
adaptecArrayController = _AdaptecArrayController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3, 5)
)
_AdaptecArrayControllerSoftwareVersion_Type = DisplayString
_AdaptecArrayControllerSoftwareVersion_Object = MibScalar
adaptecArrayControllerSoftwareVersion = _AdaptecArrayControllerSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 1),
    _AdaptecArrayControllerSoftwareVersion_Type()
)
adaptecArrayControllerSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerSoftwareVersion.setStatus("mandatory")
_AdaptecArrayControllerAdapterNumber_Type = Integer32
_AdaptecArrayControllerAdapterNumber_Object = MibScalar
adaptecArrayControllerAdapterNumber = _AdaptecArrayControllerAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 2),
    _AdaptecArrayControllerAdapterNumber_Type()
)
adaptecArrayControllerAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterNumber.setStatus("mandatory")
_AdaptecArrayControllerAdapterTable_Object = MibTable
adaptecArrayControllerAdapterTable = _AdaptecArrayControllerAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterTable.setStatus("mandatory")
_AdaptecArrayControllerAdapterEntry_Object = MibTableRow
adaptecArrayControllerAdapterEntry = _AdaptecArrayControllerAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1)
)
adaptecArrayControllerAdapterEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerAdapterIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterEntry.setStatus("mandatory")
_AdaptecArrayControllerAdapterIndex_Type = Integer32
_AdaptecArrayControllerAdapterIndex_Object = MibTableColumn
adaptecArrayControllerAdapterIndex = _AdaptecArrayControllerAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 1),
    _AdaptecArrayControllerAdapterIndex_Type()
)
adaptecArrayControllerAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterIndex.setStatus("mandatory")
_AdaptecArrayControllerAdapterDescription_Type = DisplayString
_AdaptecArrayControllerAdapterDescription_Object = MibTableColumn
adaptecArrayControllerAdapterDescription = _AdaptecArrayControllerAdapterDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 2),
    _AdaptecArrayControllerAdapterDescription_Type()
)
adaptecArrayControllerAdapterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterDescription.setStatus("mandatory")
_AdaptecArrayControllerAdapterType_Type = DisplayString
_AdaptecArrayControllerAdapterType_Object = MibTableColumn
adaptecArrayControllerAdapterType = _AdaptecArrayControllerAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 3),
    _AdaptecArrayControllerAdapterType_Type()
)
adaptecArrayControllerAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterType.setStatus("mandatory")
_AdaptecArrayControllerAdapterVersion_Type = DisplayString
_AdaptecArrayControllerAdapterVersion_Object = MibTableColumn
adaptecArrayControllerAdapterVersion = _AdaptecArrayControllerAdapterVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 4),
    _AdaptecArrayControllerAdapterVersion_Type()
)
adaptecArrayControllerAdapterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterVersion.setStatus("mandatory")
_AdaptecArrayControllerAdapterChannelCount_Type = Integer32
_AdaptecArrayControllerAdapterChannelCount_Object = MibTableColumn
adaptecArrayControllerAdapterChannelCount = _AdaptecArrayControllerAdapterChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 5),
    _AdaptecArrayControllerAdapterChannelCount_Type()
)
adaptecArrayControllerAdapterChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterChannelCount.setStatus("mandatory")


class _AdaptecArrayControllerAdapterStatus_Type(Integer32):
    """Custom type adaptecArrayControllerAdapterStatus based on Integer32"""
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


_AdaptecArrayControllerAdapterStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerAdapterStatus_Object = MibTableColumn
adaptecArrayControllerAdapterStatus = _AdaptecArrayControllerAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 6),
    _AdaptecArrayControllerAdapterStatus_Type()
)
adaptecArrayControllerAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterStatus.setStatus("mandatory")
_AdaptecArrayControllerAdapterBiosVersion_Type = DisplayString
_AdaptecArrayControllerAdapterBiosVersion_Object = MibTableColumn
adaptecArrayControllerAdapterBiosVersion = _AdaptecArrayControllerAdapterBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 7),
    _AdaptecArrayControllerAdapterBiosVersion_Type()
)
adaptecArrayControllerAdapterBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterBiosVersion.setStatus("mandatory")
_AdaptecArrayControllerAdapterKernelVersion_Type = DisplayString
_AdaptecArrayControllerAdapterKernelVersion_Object = MibTableColumn
adaptecArrayControllerAdapterKernelVersion = _AdaptecArrayControllerAdapterKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 8),
    _AdaptecArrayControllerAdapterKernelVersion_Type()
)
adaptecArrayControllerAdapterKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterKernelVersion.setStatus("mandatory")
_AdaptecArrayControllerAdapterMonitorVersion_Type = DisplayString
_AdaptecArrayControllerAdapterMonitorVersion_Object = MibTableColumn
adaptecArrayControllerAdapterMonitorVersion = _AdaptecArrayControllerAdapterMonitorVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 9),
    _AdaptecArrayControllerAdapterMonitorVersion_Type()
)
adaptecArrayControllerAdapterMonitorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterMonitorVersion.setStatus("mandatory")
_AdaptecArrayControllerAdapterHardwareVersion_Type = DisplayString
_AdaptecArrayControllerAdapterHardwareVersion_Object = MibTableColumn
adaptecArrayControllerAdapterHardwareVersion = _AdaptecArrayControllerAdapterHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 10),
    _AdaptecArrayControllerAdapterHardwareVersion_Type()
)
adaptecArrayControllerAdapterHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterHardwareVersion.setStatus("mandatory")
_AdaptecArrayControllerAdapterTotalMemory_Type = Integer32
_AdaptecArrayControllerAdapterTotalMemory_Object = MibTableColumn
adaptecArrayControllerAdapterTotalMemory = _AdaptecArrayControllerAdapterTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 11),
    _AdaptecArrayControllerAdapterTotalMemory_Type()
)
adaptecArrayControllerAdapterTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterTotalMemory.setStatus("mandatory")
_AdaptecArrayControllerAdapterProgramMemory_Type = Integer32
_AdaptecArrayControllerAdapterProgramMemory_Object = MibTableColumn
adaptecArrayControllerAdapterProgramMemory = _AdaptecArrayControllerAdapterProgramMemory_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 12),
    _AdaptecArrayControllerAdapterProgramMemory_Type()
)
adaptecArrayControllerAdapterProgramMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterProgramMemory.setStatus("mandatory")
_AdaptecArrayControllerAdapterBufferMemory_Type = Integer32
_AdaptecArrayControllerAdapterBufferMemory_Object = MibTableColumn
adaptecArrayControllerAdapterBufferMemory = _AdaptecArrayControllerAdapterBufferMemory_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 13),
    _AdaptecArrayControllerAdapterBufferMemory_Type()
)
adaptecArrayControllerAdapterBufferMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterBufferMemory.setStatus("mandatory")
_AdaptecArrayControllerContainerTable_Object = MibTable
adaptecArrayControllerContainerTable = _AdaptecArrayControllerContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerContainerTable.setStatus("mandatory")
_AdaptecArrayControllerContainerEntry_Object = MibTableRow
adaptecArrayControllerContainerEntry = _AdaptecArrayControllerContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1)
)
adaptecArrayControllerContainerEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerContIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerContainerEntry.setStatus("mandatory")
_AdaptecArrayControllerContIndex_Type = Integer32
_AdaptecArrayControllerContIndex_Object = MibTableColumn
adaptecArrayControllerContIndex = _AdaptecArrayControllerContIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 1),
    _AdaptecArrayControllerContIndex_Type()
)
adaptecArrayControllerContIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContIndex.setStatus("mandatory")
_AdaptecArrayControllerContAdapterIndex_Type = Integer32
_AdaptecArrayControllerContAdapterIndex_Object = MibTableColumn
adaptecArrayControllerContAdapterIndex = _AdaptecArrayControllerContAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 2),
    _AdaptecArrayControllerContAdapterIndex_Type()
)
adaptecArrayControllerContAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContAdapterIndex.setStatus("mandatory")
_AdaptecArrayControllerContNumber_Type = Integer32
_AdaptecArrayControllerContNumber_Object = MibTableColumn
adaptecArrayControllerContNumber = _AdaptecArrayControllerContNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 3),
    _AdaptecArrayControllerContNumber_Type()
)
adaptecArrayControllerContNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContNumber.setStatus("mandatory")
_AdaptecArrayControllerContSize_Type = Integer32
_AdaptecArrayControllerContSize_Object = MibTableColumn
adaptecArrayControllerContSize = _AdaptecArrayControllerContSize_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 4),
    _AdaptecArrayControllerContSize_Type()
)
adaptecArrayControllerContSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContSize.setStatus("mandatory")
_AdaptecArrayControllerContMountPoint_Type = DisplayString
_AdaptecArrayControllerContMountPoint_Object = MibTableColumn
adaptecArrayControllerContMountPoint = _AdaptecArrayControllerContMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 5),
    _AdaptecArrayControllerContMountPoint_Type()
)
adaptecArrayControllerContMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContMountPoint.setStatus("mandatory")
_AdaptecArrayControllerContType_Type = DisplayString
_AdaptecArrayControllerContType_Object = MibTableColumn
adaptecArrayControllerContType = _AdaptecArrayControllerContType_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 6),
    _AdaptecArrayControllerContType_Type()
)
adaptecArrayControllerContType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContType.setStatus("mandatory")
_AdaptecArrayControllerContUsage_Type = DisplayString
_AdaptecArrayControllerContUsage_Object = MibTableColumn
adaptecArrayControllerContUsage = _AdaptecArrayControllerContUsage_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 7),
    _AdaptecArrayControllerContUsage_Type()
)
adaptecArrayControllerContUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContUsage.setStatus("mandatory")


class _AdaptecArrayControllerContStatus_Type(Integer32):
    """Custom type adaptecArrayControllerContStatus based on Integer32"""
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


_AdaptecArrayControllerContStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerContStatus_Object = MibTableColumn
adaptecArrayControllerContStatus = _AdaptecArrayControllerContStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 8),
    _AdaptecArrayControllerContStatus_Type()
)
adaptecArrayControllerContStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContStatus.setStatus("mandatory")
_AdaptecArrayControllerContStripeSize_Type = Integer32
_AdaptecArrayControllerContStripeSize_Object = MibTableColumn
adaptecArrayControllerContStripeSize = _AdaptecArrayControllerContStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 9),
    _AdaptecArrayControllerContStripeSize_Type()
)
adaptecArrayControllerContStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContStripeSize.setStatus("mandatory")
_AdaptecArrayControllerDeviceTable_Object = MibTable
adaptecArrayControllerDeviceTable = _AdaptecArrayControllerDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerDeviceTable.setStatus("mandatory")
_AdaptecArrayControllerDeviceEntry_Object = MibTableRow
adaptecArrayControllerDeviceEntry = _AdaptecArrayControllerDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1)
)
adaptecArrayControllerDeviceEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerDevIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerDeviceEntry.setStatus("mandatory")
_AdaptecArrayControllerDevIndex_Type = Integer32
_AdaptecArrayControllerDevIndex_Object = MibTableColumn
adaptecArrayControllerDevIndex = _AdaptecArrayControllerDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 1),
    _AdaptecArrayControllerDevIndex_Type()
)
adaptecArrayControllerDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevIndex.setStatus("mandatory")
_AdaptecArrayControllerDevAdapterIndex_Type = Integer32
_AdaptecArrayControllerDevAdapterIndex_Object = MibTableColumn
adaptecArrayControllerDevAdapterIndex = _AdaptecArrayControllerDevAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 2),
    _AdaptecArrayControllerDevAdapterIndex_Type()
)
adaptecArrayControllerDevAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevAdapterIndex.setStatus("mandatory")
_AdaptecArrayControllerDevChannelId_Type = Integer32
_AdaptecArrayControllerDevChannelId_Object = MibTableColumn
adaptecArrayControllerDevChannelId = _AdaptecArrayControllerDevChannelId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 3),
    _AdaptecArrayControllerDevChannelId_Type()
)
adaptecArrayControllerDevChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevChannelId.setStatus("mandatory")
_AdaptecArrayControllerDevId_Type = Integer32
_AdaptecArrayControllerDevId_Object = MibTableColumn
adaptecArrayControllerDevId = _AdaptecArrayControllerDevId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 4),
    _AdaptecArrayControllerDevId_Type()
)
adaptecArrayControllerDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevId.setStatus("mandatory")
_AdaptecArrayControllerDevLogicalNumber_Type = Integer32
_AdaptecArrayControllerDevLogicalNumber_Object = MibTableColumn
adaptecArrayControllerDevLogicalNumber = _AdaptecArrayControllerDevLogicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 5),
    _AdaptecArrayControllerDevLogicalNumber_Type()
)
adaptecArrayControllerDevLogicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevLogicalNumber.setStatus("mandatory")
_AdaptecArrayControllerDevType_Type = Integer32
_AdaptecArrayControllerDevType_Object = MibTableColumn
adaptecArrayControllerDevType = _AdaptecArrayControllerDevType_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 6),
    _AdaptecArrayControllerDevType_Type()
)
adaptecArrayControllerDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevType.setStatus("mandatory")
_AdaptecArrayControllerDevVendor_Type = DisplayString
_AdaptecArrayControllerDevVendor_Object = MibTableColumn
adaptecArrayControllerDevVendor = _AdaptecArrayControllerDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 7),
    _AdaptecArrayControllerDevVendor_Type()
)
adaptecArrayControllerDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevVendor.setStatus("mandatory")
_AdaptecArrayControllerDevProduct_Type = DisplayString
_AdaptecArrayControllerDevProduct_Object = MibTableColumn
adaptecArrayControllerDevProduct = _AdaptecArrayControllerDevProduct_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 8),
    _AdaptecArrayControllerDevProduct_Type()
)
adaptecArrayControllerDevProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevProduct.setStatus("mandatory")
_AdaptecArrayControllerDevRevision_Type = DisplayString
_AdaptecArrayControllerDevRevision_Object = MibTableColumn
adaptecArrayControllerDevRevision = _AdaptecArrayControllerDevRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 9),
    _AdaptecArrayControllerDevRevision_Type()
)
adaptecArrayControllerDevRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevRevision.setStatus("mandatory")
_AdaptecArrayControllerDevBlocks_Type = Integer32
_AdaptecArrayControllerDevBlocks_Object = MibTableColumn
adaptecArrayControllerDevBlocks = _AdaptecArrayControllerDevBlocks_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 10),
    _AdaptecArrayControllerDevBlocks_Type()
)
adaptecArrayControllerDevBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevBlocks.setStatus("mandatory")
_AdaptecArrayControllerDevBytesPerBlock_Type = Integer32
_AdaptecArrayControllerDevBytesPerBlock_Object = MibTableColumn
adaptecArrayControllerDevBytesPerBlock = _AdaptecArrayControllerDevBytesPerBlock_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 11),
    _AdaptecArrayControllerDevBytesPerBlock_Type()
)
adaptecArrayControllerDevBytesPerBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevBytesPerBlock.setStatus("mandatory")
_AdaptecArrayControllerDevUsage_Type = DisplayString
_AdaptecArrayControllerDevUsage_Object = MibTableColumn
adaptecArrayControllerDevUsage = _AdaptecArrayControllerDevUsage_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 12),
    _AdaptecArrayControllerDevUsage_Type()
)
adaptecArrayControllerDevUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevUsage.setStatus("mandatory")


class _AdaptecArrayControllerDevStatus_Type(Integer32):
    """Custom type adaptecArrayControllerDevStatus based on Integer32"""
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


_AdaptecArrayControllerDevStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerDevStatus_Object = MibTableColumn
adaptecArrayControllerDevStatus = _AdaptecArrayControllerDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 13),
    _AdaptecArrayControllerDevStatus_Type()
)
adaptecArrayControllerDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevStatus.setStatus("mandatory")
_AdaptecArrayControllerContainerToDeviceTable_Object = MibTable
adaptecArrayControllerContainerToDeviceTable = _AdaptecArrayControllerContainerToDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerContainerToDeviceTable.setStatus("mandatory")
_AdaptecArrayControllerContainerToDeviceEntry_Object = MibTableRow
adaptecArrayControllerContainerToDeviceEntry = _AdaptecArrayControllerContainerToDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1)
)
adaptecArrayControllerContainerToDeviceEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerContainerToDeviceIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerContainerToDeviceEntry.setStatus("mandatory")
_AdaptecArrayControllerContainerToDeviceIndex_Type = Integer32
_AdaptecArrayControllerContainerToDeviceIndex_Object = MibTableColumn
adaptecArrayControllerContainerToDeviceIndex = _AdaptecArrayControllerContainerToDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1, 1),
    _AdaptecArrayControllerContainerToDeviceIndex_Type()
)
adaptecArrayControllerContainerToDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContainerToDeviceIndex.setStatus("mandatory")
_AdaptecArrayControllerCDAdapterIndex_Type = Integer32
_AdaptecArrayControllerCDAdapterIndex_Object = MibTableColumn
adaptecArrayControllerCDAdapterIndex = _AdaptecArrayControllerCDAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1, 2),
    _AdaptecArrayControllerCDAdapterIndex_Type()
)
adaptecArrayControllerCDAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerCDAdapterIndex.setStatus("mandatory")
_AdaptecArrayControllerContainerIndex_Type = Integer32
_AdaptecArrayControllerContainerIndex_Object = MibTableColumn
adaptecArrayControllerContainerIndex = _AdaptecArrayControllerContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1, 3),
    _AdaptecArrayControllerContainerIndex_Type()
)
adaptecArrayControllerContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContainerIndex.setStatus("mandatory")
_AdaptecArrayControllerDeviceIndex_Type = Integer32
_AdaptecArrayControllerDeviceIndex_Object = MibTableColumn
adaptecArrayControllerDeviceIndex = _AdaptecArrayControllerDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1, 4),
    _AdaptecArrayControllerDeviceIndex_Type()
)
adaptecArrayControllerDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDeviceIndex.setStatus("mandatory")
_AdaptecArrayControllerPartitionOffsetLSW_Type = Integer32
_AdaptecArrayControllerPartitionOffsetLSW_Object = MibTableColumn
adaptecArrayControllerPartitionOffsetLSW = _AdaptecArrayControllerPartitionOffsetLSW_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1, 5),
    _AdaptecArrayControllerPartitionOffsetLSW_Type()
)
adaptecArrayControllerPartitionOffsetLSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerPartitionOffsetLSW.setStatus("mandatory")
_AdaptecArrayControllerPartitionOffsetMSW_Type = Integer32
_AdaptecArrayControllerPartitionOffsetMSW_Object = MibTableColumn
adaptecArrayControllerPartitionOffsetMSW = _AdaptecArrayControllerPartitionOffsetMSW_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1, 6),
    _AdaptecArrayControllerPartitionOffsetMSW_Type()
)
adaptecArrayControllerPartitionOffsetMSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerPartitionOffsetMSW.setStatus("mandatory")
_AdaptecArrayControllerPartitionSizeLSW_Type = Integer32
_AdaptecArrayControllerPartitionSizeLSW_Object = MibTableColumn
adaptecArrayControllerPartitionSizeLSW = _AdaptecArrayControllerPartitionSizeLSW_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1, 7),
    _AdaptecArrayControllerPartitionSizeLSW_Type()
)
adaptecArrayControllerPartitionSizeLSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerPartitionSizeLSW.setStatus("mandatory")
_AdaptecArrayControllerPartitionSizeMSW_Type = Integer32
_AdaptecArrayControllerPartitionSizeMSW_Object = MibTableColumn
adaptecArrayControllerPartitionSizeMSW = _AdaptecArrayControllerPartitionSizeMSW_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 6, 1, 8),
    _AdaptecArrayControllerPartitionSizeMSW_Type()
)
adaptecArrayControllerPartitionSizeMSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerPartitionSizeMSW.setStatus("mandatory")
_AdaptecArrayControllerEnclosureTable_Object = MibTable
adaptecArrayControllerEnclosureTable = _AdaptecArrayControllerEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureTable.setStatus("mandatory")
_AdaptecArrayControllerEnclosureEntry_Object = MibTableRow
adaptecArrayControllerEnclosureEntry = _AdaptecArrayControllerEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1)
)
adaptecArrayControllerEnclosureEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerEnclosureIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureEntry.setStatus("mandatory")
_AdaptecArrayControllerEnclosureIndex_Type = Integer32
_AdaptecArrayControllerEnclosureIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureIndex = _AdaptecArrayControllerEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 1),
    _AdaptecArrayControllerEnclosureIndex_Type()
)
adaptecArrayControllerEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureAdapterIndex_Type = Integer32
_AdaptecArrayControllerEnclosureAdapterIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureAdapterIndex = _AdaptecArrayControllerEnclosureAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 2),
    _AdaptecArrayControllerEnclosureAdapterIndex_Type()
)
adaptecArrayControllerEnclosureAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureAdapterIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureProcessorId_Type = Integer32
_AdaptecArrayControllerEnclosureProcessorId_Object = MibTableColumn
adaptecArrayControllerEnclosureProcessorId = _AdaptecArrayControllerEnclosureProcessorId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 3),
    _AdaptecArrayControllerEnclosureProcessorId_Type()
)
adaptecArrayControllerEnclosureProcessorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureProcessorId.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureType_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureType based on Integer32"""
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
        *(("aemi", 6),
          ("decFault", 3),
          ("other", 1),
          ("saf-te", 4),
          ("ses", 5),
          ("unknown", 2))
    )


_AdaptecArrayControllerEnclosureType_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureType_Object = MibTableColumn
adaptecArrayControllerEnclosureType = _AdaptecArrayControllerEnclosureType_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 4),
    _AdaptecArrayControllerEnclosureType_Type()
)
adaptecArrayControllerEnclosureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureType.setStatus("mandatory")
_AdaptecArrayControllerEnclosureNumberFans_Type = Integer32
_AdaptecArrayControllerEnclosureNumberFans_Object = MibTableColumn
adaptecArrayControllerEnclosureNumberFans = _AdaptecArrayControllerEnclosureNumberFans_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 5),
    _AdaptecArrayControllerEnclosureNumberFans_Type()
)
adaptecArrayControllerEnclosureNumberFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureNumberFans.setStatus("mandatory")
_AdaptecArrayControllerEnclosureNumberPowerSupplies_Type = Integer32
_AdaptecArrayControllerEnclosureNumberPowerSupplies_Object = MibTableColumn
adaptecArrayControllerEnclosureNumberPowerSupplies = _AdaptecArrayControllerEnclosureNumberPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 6),
    _AdaptecArrayControllerEnclosureNumberPowerSupplies_Type()
)
adaptecArrayControllerEnclosureNumberPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureNumberPowerSupplies.setStatus("mandatory")
_AdaptecArrayControllerEnclosureNumberSlots_Type = Integer32
_AdaptecArrayControllerEnclosureNumberSlots_Object = MibTableColumn
adaptecArrayControllerEnclosureNumberSlots = _AdaptecArrayControllerEnclosureNumberSlots_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 7),
    _AdaptecArrayControllerEnclosureNumberSlots_Type()
)
adaptecArrayControllerEnclosureNumberSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureNumberSlots.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureDoorLock_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureDoorLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AdaptecArrayControllerEnclosureDoorLock_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureDoorLock_Object = MibTableColumn
adaptecArrayControllerEnclosureDoorLock = _AdaptecArrayControllerEnclosureDoorLock_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 8),
    _AdaptecArrayControllerEnclosureDoorLock_Type()
)
adaptecArrayControllerEnclosureDoorLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDoorLock.setStatus("mandatory")
_AdaptecArrayControllerEnclosureNumberTemperatureSensors_Type = Integer32
_AdaptecArrayControllerEnclosureNumberTemperatureSensors_Object = MibTableColumn
adaptecArrayControllerEnclosureNumberTemperatureSensors = _AdaptecArrayControllerEnclosureNumberTemperatureSensors_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 9),
    _AdaptecArrayControllerEnclosureNumberTemperatureSensors_Type()
)
adaptecArrayControllerEnclosureNumberTemperatureSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureNumberTemperatureSensors.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureSpeaker_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureSpeaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AdaptecArrayControllerEnclosureSpeaker_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureSpeaker_Object = MibTableColumn
adaptecArrayControllerEnclosureSpeaker = _AdaptecArrayControllerEnclosureSpeaker_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 10),
    _AdaptecArrayControllerEnclosureSpeaker_Type()
)
adaptecArrayControllerEnclosureSpeaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureSpeaker.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureBootTimeDiagnostic_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureBootTimeDiagnostic based on Integer32"""
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


_AdaptecArrayControllerEnclosureBootTimeDiagnostic_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureBootTimeDiagnostic_Object = MibTableColumn
adaptecArrayControllerEnclosureBootTimeDiagnostic = _AdaptecArrayControllerEnclosureBootTimeDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 11),
    _AdaptecArrayControllerEnclosureBootTimeDiagnostic_Type()
)
adaptecArrayControllerEnclosureBootTimeDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureBootTimeDiagnostic.setStatus("mandatory")
_AdaptecArrayControllerEnclosureVendor_Type = DisplayString
_AdaptecArrayControllerEnclosureVendor_Object = MibTableColumn
adaptecArrayControllerEnclosureVendor = _AdaptecArrayControllerEnclosureVendor_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 12),
    _AdaptecArrayControllerEnclosureVendor_Type()
)
adaptecArrayControllerEnclosureVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureVendor.setStatus("mandatory")
_AdaptecArrayControllerEnclosureProduct_Type = DisplayString
_AdaptecArrayControllerEnclosureProduct_Object = MibTableColumn
adaptecArrayControllerEnclosureProduct = _AdaptecArrayControllerEnclosureProduct_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 13),
    _AdaptecArrayControllerEnclosureProduct_Type()
)
adaptecArrayControllerEnclosureProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureProduct.setStatus("mandatory")
_AdaptecArrayControllerEnclosureRevision_Type = DisplayString
_AdaptecArrayControllerEnclosureRevision_Object = MibTableColumn
adaptecArrayControllerEnclosureRevision = _AdaptecArrayControllerEnclosureRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 14),
    _AdaptecArrayControllerEnclosureRevision_Type()
)
adaptecArrayControllerEnclosureRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureRevision.setStatus("mandatory")
_AdaptecArrayControllerEnclosureIdLow_Type = Integer32
_AdaptecArrayControllerEnclosureIdLow_Object = MibTableColumn
adaptecArrayControllerEnclosureIdLow = _AdaptecArrayControllerEnclosureIdLow_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 15),
    _AdaptecArrayControllerEnclosureIdLow_Type()
)
adaptecArrayControllerEnclosureIdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureIdLow.setStatus("mandatory")
_AdaptecArrayControllerEnclosureIdHigh_Type = Integer32
_AdaptecArrayControllerEnclosureIdHigh_Object = MibTableColumn
adaptecArrayControllerEnclosureIdHigh = _AdaptecArrayControllerEnclosureIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 16),
    _AdaptecArrayControllerEnclosureIdHigh_Type()
)
adaptecArrayControllerEnclosureIdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureIdHigh.setStatus("mandatory")
_AdaptecArrayControllerEnclosureStandardRevision_Type = DisplayString
_AdaptecArrayControllerEnclosureStandardRevision_Object = MibTableColumn
adaptecArrayControllerEnclosureStandardRevision = _AdaptecArrayControllerEnclosureStandardRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 17),
    _AdaptecArrayControllerEnclosureStandardRevision_Type()
)
adaptecArrayControllerEnclosureStandardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureStandardRevision.setStatus("mandatory")
_AdaptecArrayControllerEnclosurePowerOnTime_Type = Integer32
_AdaptecArrayControllerEnclosurePowerOnTime_Object = MibTableColumn
adaptecArrayControllerEnclosurePowerOnTime = _AdaptecArrayControllerEnclosurePowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 18),
    _AdaptecArrayControllerEnclosurePowerOnTime_Type()
)
adaptecArrayControllerEnclosurePowerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosurePowerOnTime.setStatus("mandatory")
_AdaptecArrayControllerEnclosurePowerCycles_Type = Integer32
_AdaptecArrayControllerEnclosurePowerCycles_Object = MibTableColumn
adaptecArrayControllerEnclosurePowerCycles = _AdaptecArrayControllerEnclosurePowerCycles_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 19),
    _AdaptecArrayControllerEnclosurePowerCycles_Type()
)
adaptecArrayControllerEnclosurePowerCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosurePowerCycles.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureSpeakerStatus_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureSpeakerStatus based on Integer32"""
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


_AdaptecArrayControllerEnclosureSpeakerStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureSpeakerStatus_Object = MibTableColumn
adaptecArrayControllerEnclosureSpeakerStatus = _AdaptecArrayControllerEnclosureSpeakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 20),
    _AdaptecArrayControllerEnclosureSpeakerStatus_Type()
)
adaptecArrayControllerEnclosureSpeakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureSpeakerStatus.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureOverTemperature_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureOverTemperature based on Integer32"""
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


_AdaptecArrayControllerEnclosureOverTemperature_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureOverTemperature_Object = MibTableColumn
adaptecArrayControllerEnclosureOverTemperature = _AdaptecArrayControllerEnclosureOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 20, 1, 21),
    _AdaptecArrayControllerEnclosureOverTemperature_Type()
)
adaptecArrayControllerEnclosureOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureOverTemperature.setStatus("mandatory")
_AdaptecArrayControllerEnclosureFanTable_Object = MibTable
adaptecArrayControllerEnclosureFanTable = _AdaptecArrayControllerEnclosureFanTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 21)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureFanTable.setStatus("mandatory")
_AdaptecArrayControllerEnclosureFanEntry_Object = MibTableRow
adaptecArrayControllerEnclosureFanEntry = _AdaptecArrayControllerEnclosureFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 21, 1)
)
adaptecArrayControllerEnclosureFanEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerEnclosureFanIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureFanEntry.setStatus("mandatory")
_AdaptecArrayControllerEnclosureFanIndex_Type = Integer32
_AdaptecArrayControllerEnclosureFanIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureFanIndex = _AdaptecArrayControllerEnclosureFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 21, 1, 1),
    _AdaptecArrayControllerEnclosureFanIndex_Type()
)
adaptecArrayControllerEnclosureFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureFanIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureFanEnclosureIndex_Type = Integer32
_AdaptecArrayControllerEnclosureFanEnclosureIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureFanEnclosureIndex = _AdaptecArrayControllerEnclosureFanEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 21, 1, 2),
    _AdaptecArrayControllerEnclosureFanEnclosureIndex_Type()
)
adaptecArrayControllerEnclosureFanEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureFanEnclosureIndex.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureFanStatus_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureFanStatus based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("notInstalled", 7),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_AdaptecArrayControllerEnclosureFanStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureFanStatus_Object = MibTableColumn
adaptecArrayControllerEnclosureFanStatus = _AdaptecArrayControllerEnclosureFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 21, 1, 3),
    _AdaptecArrayControllerEnclosureFanStatus_Type()
)
adaptecArrayControllerEnclosureFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureFanStatus.setStatus("mandatory")
_AdaptecArrayControllerEnclosurePowerSupplyTable_Object = MibTable
adaptecArrayControllerEnclosurePowerSupplyTable = _AdaptecArrayControllerEnclosurePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 22)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosurePowerSupplyTable.setStatus("mandatory")
_AdaptecArrayControllerEnclosurePowerSupplyEntry_Object = MibTableRow
adaptecArrayControllerEnclosurePowerSupplyEntry = _AdaptecArrayControllerEnclosurePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 22, 1)
)
adaptecArrayControllerEnclosurePowerSupplyEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerEnclosurePowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosurePowerSupplyEntry.setStatus("mandatory")
_AdaptecArrayControllerEnclosurePowerSupplyIndex_Type = Integer32
_AdaptecArrayControllerEnclosurePowerSupplyIndex_Object = MibTableColumn
adaptecArrayControllerEnclosurePowerSupplyIndex = _AdaptecArrayControllerEnclosurePowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 22, 1, 1),
    _AdaptecArrayControllerEnclosurePowerSupplyIndex_Type()
)
adaptecArrayControllerEnclosurePowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosurePowerSupplyIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosurePowerSupplyEnclosureIndex_Type = Integer32
_AdaptecArrayControllerEnclosurePowerSupplyEnclosureIndex_Object = MibTableColumn
adaptecArrayControllerEnclosurePowerSupplyEnclosureIndex = _AdaptecArrayControllerEnclosurePowerSupplyEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 22, 1, 2),
    _AdaptecArrayControllerEnclosurePowerSupplyEnclosureIndex_Type()
)
adaptecArrayControllerEnclosurePowerSupplyEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosurePowerSupplyEnclosureIndex.setStatus("mandatory")


class _AdaptecArrayControllerEnclosurePowerSupplyStatus_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosurePowerSupplyStatus based on Integer32"""
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
        *(("installed", 6),
          ("notInstalled", 7),
          ("offAndMalfunctioning", 5),
          ("onAndMalfunctioning", 4),
          ("operationalAndOff", 3),
          ("operationalAndOn", 2),
          ("unknown", 1))
    )


_AdaptecArrayControllerEnclosurePowerSupplyStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosurePowerSupplyStatus_Object = MibTableColumn
adaptecArrayControllerEnclosurePowerSupplyStatus = _AdaptecArrayControllerEnclosurePowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 22, 1, 3),
    _AdaptecArrayControllerEnclosurePowerSupplyStatus_Type()
)
adaptecArrayControllerEnclosurePowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosurePowerSupplyStatus.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDoorLockTable_Object = MibTable
adaptecArrayControllerEnclosureDoorLockTable = _AdaptecArrayControllerEnclosureDoorLockTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 23)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDoorLockTable.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDoorLockEntry_Object = MibTableRow
adaptecArrayControllerEnclosureDoorLockEntry = _AdaptecArrayControllerEnclosureDoorLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 23, 1)
)
adaptecArrayControllerEnclosureDoorLockEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerEnclosureDoorLockIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDoorLockEntry.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDoorLockIndex_Type = Integer32
_AdaptecArrayControllerEnclosureDoorLockIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureDoorLockIndex = _AdaptecArrayControllerEnclosureDoorLockIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 23, 1, 1),
    _AdaptecArrayControllerEnclosureDoorLockIndex_Type()
)
adaptecArrayControllerEnclosureDoorLockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDoorLockIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDoorLockEnclosureIndex_Type = Integer32
_AdaptecArrayControllerEnclosureDoorLockEnclosureIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureDoorLockEnclosureIndex = _AdaptecArrayControllerEnclosureDoorLockEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 23, 1, 2),
    _AdaptecArrayControllerEnclosureDoorLockEnclosureIndex_Type()
)
adaptecArrayControllerEnclosureDoorLockEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDoorLockEnclosureIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDoorLockSlot_Type = Integer32
_AdaptecArrayControllerEnclosureDoorLockSlot_Object = MibTableColumn
adaptecArrayControllerEnclosureDoorLockSlot = _AdaptecArrayControllerEnclosureDoorLockSlot_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 23, 1, 3),
    _AdaptecArrayControllerEnclosureDoorLockSlot_Type()
)
adaptecArrayControllerEnclosureDoorLockSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDoorLockSlot.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureDoorLockStatus_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureDoorLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unknown", 1),
          ("unlocked", 3))
    )


_AdaptecArrayControllerEnclosureDoorLockStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureDoorLockStatus_Object = MibTableColumn
adaptecArrayControllerEnclosureDoorLockStatus = _AdaptecArrayControllerEnclosureDoorLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 23, 1, 4),
    _AdaptecArrayControllerEnclosureDoorLockStatus_Type()
)
adaptecArrayControllerEnclosureDoorLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDoorLockStatus.setStatus("mandatory")
_AdaptecArrayControllerEnclosureTemperatureSensorTable_Object = MibTable
adaptecArrayControllerEnclosureTemperatureSensorTable = _AdaptecArrayControllerEnclosureTemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 24)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureTemperatureSensorTable.setStatus("mandatory")
_AdaptecArrayControllerEnclosureTemperatureSensorEntry_Object = MibTableRow
adaptecArrayControllerEnclosureTemperatureSensorEntry = _AdaptecArrayControllerEnclosureTemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 24, 1)
)
adaptecArrayControllerEnclosureTemperatureSensorEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerEnclosureTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureTemperatureSensorEntry.setStatus("mandatory")
_AdaptecArrayControllerEnclosureTemperatureSensorIndex_Type = Integer32
_AdaptecArrayControllerEnclosureTemperatureSensorIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureTemperatureSensorIndex = _AdaptecArrayControllerEnclosureTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 24, 1, 1),
    _AdaptecArrayControllerEnclosureTemperatureSensorIndex_Type()
)
adaptecArrayControllerEnclosureTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureTemperatureSensorIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex_Type = Integer32
_AdaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex = _AdaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 24, 1, 2),
    _AdaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex_Type()
)
adaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex.setStatus("mandatory")


class _AdaptecArrayControllerEnclosureTemperatureSensorOverTemperature_Type(Integer32):
    """Custom type adaptecArrayControllerEnclosureTemperatureSensorOverTemperature based on Integer32"""
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


_AdaptecArrayControllerEnclosureTemperatureSensorOverTemperature_Type.__name__ = "Integer32"
_AdaptecArrayControllerEnclosureTemperatureSensorOverTemperature_Object = MibTableColumn
adaptecArrayControllerEnclosureTemperatureSensorOverTemperature = _AdaptecArrayControllerEnclosureTemperatureSensorOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 24, 1, 3),
    _AdaptecArrayControllerEnclosureTemperatureSensorOverTemperature_Type()
)
adaptecArrayControllerEnclosureTemperatureSensorOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureTemperatureSensorOverTemperature.setStatus("mandatory")
_AdaptecArrayControllerEnclosureTemperatureSensorDegrees_Type = Integer32
_AdaptecArrayControllerEnclosureTemperatureSensorDegrees_Object = MibTableColumn
adaptecArrayControllerEnclosureTemperatureSensorDegrees = _AdaptecArrayControllerEnclosureTemperatureSensorDegrees_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 24, 1, 4),
    _AdaptecArrayControllerEnclosureTemperatureSensorDegrees_Type()
)
adaptecArrayControllerEnclosureTemperatureSensorDegrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureTemperatureSensorDegrees.setStatus("mandatory")
_AdaptecArrayControllerEnclosureScsiIdTable_Object = MibTable
adaptecArrayControllerEnclosureScsiIdTable = _AdaptecArrayControllerEnclosureScsiIdTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 25)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureScsiIdTable.setStatus("mandatory")
_AdaptecArrayControllerEnclosureScsiIdEntry_Object = MibTableRow
adaptecArrayControllerEnclosureScsiIdEntry = _AdaptecArrayControllerEnclosureScsiIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 25, 1)
)
adaptecArrayControllerEnclosureScsiIdEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerEnclosureScsiIdIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureScsiIdEntry.setStatus("mandatory")
_AdaptecArrayControllerEnclosureScsiIdIndex_Type = Integer32
_AdaptecArrayControllerEnclosureScsiIdIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureScsiIdIndex = _AdaptecArrayControllerEnclosureScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 25, 1, 1),
    _AdaptecArrayControllerEnclosureScsiIdIndex_Type()
)
adaptecArrayControllerEnclosureScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureScsiIdIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureScsiIdEnclosureIndex_Type = Integer32
_AdaptecArrayControllerEnclosureScsiIdEnclosureIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureScsiIdEnclosureIndex = _AdaptecArrayControllerEnclosureScsiIdEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 25, 1, 2),
    _AdaptecArrayControllerEnclosureScsiIdEnclosureIndex_Type()
)
adaptecArrayControllerEnclosureScsiIdEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureScsiIdEnclosureIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureScsiIdSlot_Type = Integer32
_AdaptecArrayControllerEnclosureScsiIdSlot_Object = MibTableColumn
adaptecArrayControllerEnclosureScsiIdSlot = _AdaptecArrayControllerEnclosureScsiIdSlot_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 25, 1, 3),
    _AdaptecArrayControllerEnclosureScsiIdSlot_Type()
)
adaptecArrayControllerEnclosureScsiIdSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureScsiIdSlot.setStatus("mandatory")
_AdaptecArrayControllerEnclosureChannelId_Type = Integer32
_AdaptecArrayControllerEnclosureChannelId_Object = MibTableColumn
adaptecArrayControllerEnclosureChannelId = _AdaptecArrayControllerEnclosureChannelId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 25, 1, 4),
    _AdaptecArrayControllerEnclosureChannelId_Type()
)
adaptecArrayControllerEnclosureChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureChannelId.setStatus("mandatory")
_AdaptecArrayControllerEnclosureScsiId_Type = Integer32
_AdaptecArrayControllerEnclosureScsiId_Object = MibTableColumn
adaptecArrayControllerEnclosureScsiId = _AdaptecArrayControllerEnclosureScsiId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 25, 1, 5),
    _AdaptecArrayControllerEnclosureScsiId_Type()
)
adaptecArrayControllerEnclosureScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureScsiId.setStatus("mandatory")
_AdaptecArrayControllerEnclosureLunId_Type = Integer32
_AdaptecArrayControllerEnclosureLunId_Object = MibTableColumn
adaptecArrayControllerEnclosureLunId = _AdaptecArrayControllerEnclosureLunId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 25, 1, 6),
    _AdaptecArrayControllerEnclosureLunId_Type()
)
adaptecArrayControllerEnclosureLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureLunId.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDeviceInsertionTable_Object = MibTable
adaptecArrayControllerEnclosureDeviceInsertionTable = _AdaptecArrayControllerEnclosureDeviceInsertionTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 26)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDeviceInsertionTable.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDeviceInsertionEntry_Object = MibTableRow
adaptecArrayControllerEnclosureDeviceInsertionEntry = _AdaptecArrayControllerEnclosureDeviceInsertionEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 26, 1)
)
adaptecArrayControllerEnclosureDeviceInsertionEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerEnclosureDeviceInsertionIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDeviceInsertionEntry.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDeviceInsertionIndex_Type = Integer32
_AdaptecArrayControllerEnclosureDeviceInsertionIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureDeviceInsertionIndex = _AdaptecArrayControllerEnclosureDeviceInsertionIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 26, 1, 1),
    _AdaptecArrayControllerEnclosureDeviceInsertionIndex_Type()
)
adaptecArrayControllerEnclosureDeviceInsertionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDeviceInsertionIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex_Type = Integer32
_AdaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex = _AdaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 26, 1, 2),
    _AdaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex_Type()
)
adaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDeviceInsertionSlot_Type = Integer32
_AdaptecArrayControllerEnclosureDeviceInsertionSlot_Object = MibTableColumn
adaptecArrayControllerEnclosureDeviceInsertionSlot = _AdaptecArrayControllerEnclosureDeviceInsertionSlot_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 26, 1, 3),
    _AdaptecArrayControllerEnclosureDeviceInsertionSlot_Type()
)
adaptecArrayControllerEnclosureDeviceInsertionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDeviceInsertionSlot.setStatus("mandatory")
_AdaptecArrayControllerEnclosureDeviceInsertions_Type = Integer32
_AdaptecArrayControllerEnclosureDeviceInsertions_Object = MibTableColumn
adaptecArrayControllerEnclosureDeviceInsertions = _AdaptecArrayControllerEnclosureDeviceInsertions_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 26, 1, 4),
    _AdaptecArrayControllerEnclosureDeviceInsertions_Type()
)
adaptecArrayControllerEnclosureDeviceInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureDeviceInsertions.setStatus("mandatory")
_AdaptecArrayControllerEnclosureSlotStatusTable_Object = MibTable
adaptecArrayControllerEnclosureSlotStatusTable = _AdaptecArrayControllerEnclosureSlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 27)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureSlotStatusTable.setStatus("mandatory")
_AdaptecArrayControllerEnclosureSlotStatusEntry_Object = MibTableRow
adaptecArrayControllerEnclosureSlotStatusEntry = _AdaptecArrayControllerEnclosureSlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 27, 1)
)
adaptecArrayControllerEnclosureSlotStatusEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerEnclosureSlotStatusIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureSlotStatusEntry.setStatus("mandatory")
_AdaptecArrayControllerEnclosureSlotStatusIndex_Type = Integer32
_AdaptecArrayControllerEnclosureSlotStatusIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureSlotStatusIndex = _AdaptecArrayControllerEnclosureSlotStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 27, 1, 1),
    _AdaptecArrayControllerEnclosureSlotStatusIndex_Type()
)
adaptecArrayControllerEnclosureSlotStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureSlotStatusIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureSlotStatusEnclosureIndex_Type = Integer32
_AdaptecArrayControllerEnclosureSlotStatusEnclosureIndex_Object = MibTableColumn
adaptecArrayControllerEnclosureSlotStatusEnclosureIndex = _AdaptecArrayControllerEnclosureSlotStatusEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 27, 1, 2),
    _AdaptecArrayControllerEnclosureSlotStatusEnclosureIndex_Type()
)
adaptecArrayControllerEnclosureSlotStatusEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureSlotStatusEnclosureIndex.setStatus("mandatory")
_AdaptecArrayControllerEnclosureSlotStatusSlot_Type = Integer32
_AdaptecArrayControllerEnclosureSlotStatusSlot_Object = MibTableColumn
adaptecArrayControllerEnclosureSlotStatusSlot = _AdaptecArrayControllerEnclosureSlotStatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 27, 1, 3),
    _AdaptecArrayControllerEnclosureSlotStatusSlot_Type()
)
adaptecArrayControllerEnclosureSlotStatusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureSlotStatusSlot.setStatus("mandatory")
_AdaptecArrayControllerEnclosureSlotStatus_Type = Integer32
_AdaptecArrayControllerEnclosureSlotStatus_Object = MibTableColumn
adaptecArrayControllerEnclosureSlotStatus = _AdaptecArrayControllerEnclosureSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 27, 1, 4),
    _AdaptecArrayControllerEnclosureSlotStatus_Type()
)
adaptecArrayControllerEnclosureSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerEnclosureSlotStatus.setStatus("mandatory")
_AdaptecArrayControllerTraps_ObjectIdentity = ObjectIdentity
adaptecArrayControllerTraps = _AdaptecArrayControllerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 9000)
)
_AacControllerId_Type = DisplayString
_AacControllerId_Object = MibScalar
aacControllerId = _AacControllerId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 9000, 1),
    _AacControllerId_Type()
)
aacControllerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aacControllerId.setStatus("mandatory")
_AacContainerId_Type = Integer32
_AacContainerId_Object = MibScalar
aacContainerId = _AacContainerId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 9000, 2),
    _AacContainerId_Type()
)
aacContainerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aacContainerId.setStatus("mandatory")
_AacBusId_Type = Integer32
_AacBusId_Object = MibScalar
aacBusId = _AacBusId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 9000, 3),
    _AacBusId_Type()
)
aacBusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aacBusId.setStatus("mandatory")
_AacScsiId_Type = Integer32
_AacScsiId_Object = MibScalar
aacScsiId = _AacScsiId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 9000, 4),
    _AacScsiId_Type()
)
aacScsiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aacScsiId.setStatus("mandatory")
_AacLunId_Type = Integer32
_AacLunId_Object = MibScalar
aacLunId = _AacLunId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 9000, 5),
    _AacLunId_Type()
)
aacLunId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aacLunId.setStatus("mandatory")
_AacEnclosureProcessorId_Type = Integer32
_AacEnclosureProcessorId_Object = MibScalar
aacEnclosureProcessorId = _AacEnclosureProcessorId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 9000, 6),
    _AacEnclosureProcessorId_Type()
)
aacEnclosureProcessorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aacEnclosureProcessorId.setStatus("mandatory")
_AacComponentUnitId_Type = Integer32
_AacComponentUnitId_Object = MibScalar
aacComponentUnitId = _AacComponentUnitId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 9000, 7),
    _AacComponentUnitId_Type()
)
aacComponentUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aacComponentUnitId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

aacDriveLetterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 1)
)
aacDriveLetterChange.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacDriveLetterChange.setStatus(
        ""
    )

aacFailoverChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 2)
)
aacFailoverChange.setObjects(
    ("AdaptecArrayController-MIB", "aacControllerId")
)
if mibBuilder.loadTexts:
    aacFailoverChange.setStatus(
        ""
    )

aacContainerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 3)
)
aacContainerStateChange.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacContainerStateChange.setStatus(
        ""
    )

aacFileSystemChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 4)
)
aacFileSystemChange.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacFileSystemChange.setStatus(
        ""
    )

aacGeneralContainerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 6)
)
aacGeneralContainerFailure.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacGeneralContainerFailure.setStatus(
        ""
    )

aacMirrorNotMirroring = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 7)
)
aacMirrorNotMirroring.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacMirrorNotMirroring.setStatus(
        ""
    )

aacMirrorFailureNoSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 8)
)
aacMirrorFailureNoSpace.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacMirrorFailureNoSpace.setStatus(
        ""
    )

aacMirrorFailureNoUnmirror = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 9)
)
aacMirrorFailureNoUnmirror.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacMirrorFailureNoUnmirror.setStatus(
        ""
    )

aacMirrorFailoverStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 10)
)
aacMirrorFailoverStarted.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacMirrorFailoverStarted.setStatus(
        ""
    )

aacMirrorFailoverFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 11)
)
aacMirrorFailoverFailed.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacMirrorFailoverFailed.setStatus(
        ""
    )

aacMirrorNoFailoverAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 12)
)
aacMirrorNoFailoverAssigned.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacMirrorNoFailoverAssigned.setStatus(
        ""
    )

aacMirrorDriveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 13)
)
aacMirrorDriveFailure.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacMirrorDriveFailure.setStatus(
        ""
    )

aacRaidRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 14)
)
aacRaidRebuildStart.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacRaidRebuildStart.setStatus(
        ""
    )

aacRaidRebuildRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 15)
)
aacRaidRebuildRestart.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacRaidRebuildRestart.setStatus(
        ""
    )

aacRaidDriveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 16)
)
aacRaidDriveFailure.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacRaidDriveFailure.setStatus(
        ""
    )

aacRaidNoFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 17)
)
aacRaidNoFailover.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacRaidNoFailover.setStatus(
        ""
    )

aacRaidNoSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 18)
)
aacRaidNoSpace.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacRaidNoSpace.setStatus(
        ""
    )

aacSnapshotContainerAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 19)
)
aacSnapshotContainerAlmostFull.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacSnapshotContainerAlmostFull.setStatus(
        ""
    )

aacSnapshotContainerFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 20)
)
aacSnapshotContainerFull.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacSnapshotContainerFull.setStatus(
        ""
    )

aacRaidRebuildComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 21)
)
aacRaidRebuildComplete.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacRaidRebuildComplete.setStatus(
        ""
    )

aacDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 22)
)
aacDeviceFailure.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacBusId"),
        ("AdaptecArrayController-MIB", "aacScsiId"),
        ("AdaptecArrayController-MIB", "aacLunId"))
)
if mibBuilder.loadTexts:
    aacDeviceFailure.setStatus(
        ""
    )

aacControllerResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 23)
)
aacControllerResume.setObjects(
    ("AdaptecArrayController-MIB", "aacControllerId")
)
if mibBuilder.loadTexts:
    aacControllerResume.setStatus(
        ""
    )

aacInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 24)
)
if mibBuilder.loadTexts:
    aacInterfaceUp.setStatus(
        ""
    )

aacBatteryReconditionRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 25)
)
aacBatteryReconditionRequired.setObjects(
    ("AdaptecArrayController-MIB", "aacControllerId")
)
if mibBuilder.loadTexts:
    aacBatteryReconditionRequired.setStatus(
        ""
    )

aacEnclosureGeneralError = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 26)
)
aacEnclosureGeneralError.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacEnclosureProcessorId"),
        ("AdaptecArrayController-MIB", "aacComponentUnitId"))
)
if mibBuilder.loadTexts:
    aacEnclosureGeneralError.setStatus(
        ""
    )

aacEnclosureFanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 27)
)
aacEnclosureFanError.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacEnclosureProcessorId"),
        ("AdaptecArrayController-MIB", "aacComponentUnitId"))
)
if mibBuilder.loadTexts:
    aacEnclosureFanError.setStatus(
        ""
    )

aacEnclosurePowerSupplyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 28)
)
aacEnclosurePowerSupplyError.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacEnclosureProcessorId"),
        ("AdaptecArrayController-MIB", "aacComponentUnitId"))
)
if mibBuilder.loadTexts:
    aacEnclosurePowerSupplyError.setStatus(
        ""
    )

aacEnclosureTempAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 29)
)
aacEnclosureTempAbnormal.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacEnclosureProcessorId"),
        ("AdaptecArrayController-MIB", "aacComponentUnitId"))
)
if mibBuilder.loadTexts:
    aacEnclosureTempAbnormal.setStatus(
        ""
    )

aacEnclosureTempOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 30)
)
aacEnclosureTempOver.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacEnclosureProcessorId"),
        ("AdaptecArrayController-MIB", "aacComponentUnitId"))
)
if mibBuilder.loadTexts:
    aacEnclosureTempOver.setStatus(
        ""
    )

aacBatteryDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 31)
)
aacBatteryDead.setObjects(
    ("AdaptecArrayController-MIB", "aacControllerId")
)
if mibBuilder.loadTexts:
    aacBatteryDead.setStatus(
        ""
    )

aacBatteryImproving = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 32)
)
aacBatteryImproving.setObjects(
    ("AdaptecArrayController-MIB", "aacControllerId")
)
if mibBuilder.loadTexts:
    aacBatteryImproving.setStatus(
        ""
    )

aacBatteryDegrading = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 33)
)
aacBatteryDegrading.setObjects(
    ("AdaptecArrayController-MIB", "aacControllerId")
)
if mibBuilder.loadTexts:
    aacBatteryDegrading.setStatus(
        ""
    )

aacBatteryGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 34)
)
aacBatteryGood.setObjects(
    ("AdaptecArrayController-MIB", "aacControllerId")
)
if mibBuilder.loadTexts:
    aacBatteryGood.setStatus(
        ""
    )

aacControllerPaused = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 35)
)
aacControllerPaused.setObjects(
    ("AdaptecArrayController-MIB", "aacControllerId")
)
if mibBuilder.loadTexts:
    aacControllerPaused.setStatus(
        ""
    )

aacContainerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 36)
)
aacContainerCreated.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacContainerCreated.setStatus(
        ""
    )

aacContainerDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 37)
)
aacContainerDeleted.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacContainerId"))
)
if mibBuilder.loadTexts:
    aacContainerDeleted.setStatus(
        ""
    )

aacDeviceFailurePredictionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 38)
)
aacDeviceFailurePredictionThresholdExceeded.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacBusId"),
        ("AdaptecArrayController-MIB", "aacScsiId"),
        ("AdaptecArrayController-MIB", "aacLunId"))
)
if mibBuilder.loadTexts:
    aacDeviceFailurePredictionThresholdExceeded.setStatus(
        ""
    )

aacDeviceFailurePredictionTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 39)
)
aacDeviceFailurePredictionTest.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacBusId"),
        ("AdaptecArrayController-MIB", "aacScsiId"),
        ("AdaptecArrayController-MIB", "aacLunId"))
)
if mibBuilder.loadTexts:
    aacDeviceFailurePredictionTest.setStatus(
        ""
    )

aacDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 40)
)
aacDeviceWarning.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacBusId"),
        ("AdaptecArrayController-MIB", "aacScsiId"),
        ("AdaptecArrayController-MIB", "aacLunId"))
)
if mibBuilder.loadTexts:
    aacDeviceWarning.setStatus(
        ""
    )

aacDeviceTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 41)
)
aacDeviceTemperatureWarning.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacBusId"),
        ("AdaptecArrayController-MIB", "aacScsiId"),
        ("AdaptecArrayController-MIB", "aacLunId"))
)
if mibBuilder.loadTexts:
    aacDeviceTemperatureWarning.setStatus(
        ""
    )

aacDeviceDegradedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 42)
)
aacDeviceDegradedWarning.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacBusId"),
        ("AdaptecArrayController-MIB", "aacScsiId"),
        ("AdaptecArrayController-MIB", "aacLunId"))
)
if mibBuilder.loadTexts:
    aacDeviceDegradedWarning.setStatus(
        ""
    )

aacDeviceFailurePredictionConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 0, 43)
)
aacDeviceFailurePredictionConfigurationChanged.setObjects(
      *(("AdaptecArrayController-MIB", "aacControllerId"),
        ("AdaptecArrayController-MIB", "aacBusId"),
        ("AdaptecArrayController-MIB", "aacScsiId"),
        ("AdaptecArrayController-MIB", "aacLunId"))
)
if mibBuilder.loadTexts:
    aacDeviceFailurePredictionConfigurationChanged.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AdaptecArrayController-MIB",
    **{"adaptec": adaptec,
       "products": products,
       "adaptecArrayController": adaptecArrayController,
       "aacDriveLetterChange": aacDriveLetterChange,
       "aacFailoverChange": aacFailoverChange,
       "aacContainerStateChange": aacContainerStateChange,
       "aacFileSystemChange": aacFileSystemChange,
       "aacGeneralContainerFailure": aacGeneralContainerFailure,
       "aacMirrorNotMirroring": aacMirrorNotMirroring,
       "aacMirrorFailureNoSpace": aacMirrorFailureNoSpace,
       "aacMirrorFailureNoUnmirror": aacMirrorFailureNoUnmirror,
       "aacMirrorFailoverStarted": aacMirrorFailoverStarted,
       "aacMirrorFailoverFailed": aacMirrorFailoverFailed,
       "aacMirrorNoFailoverAssigned": aacMirrorNoFailoverAssigned,
       "aacMirrorDriveFailure": aacMirrorDriveFailure,
       "aacRaidRebuildStart": aacRaidRebuildStart,
       "aacRaidRebuildRestart": aacRaidRebuildRestart,
       "aacRaidDriveFailure": aacRaidDriveFailure,
       "aacRaidNoFailover": aacRaidNoFailover,
       "aacRaidNoSpace": aacRaidNoSpace,
       "aacSnapshotContainerAlmostFull": aacSnapshotContainerAlmostFull,
       "aacSnapshotContainerFull": aacSnapshotContainerFull,
       "aacRaidRebuildComplete": aacRaidRebuildComplete,
       "aacDeviceFailure": aacDeviceFailure,
       "aacControllerResume": aacControllerResume,
       "aacInterfaceUp": aacInterfaceUp,
       "aacBatteryReconditionRequired": aacBatteryReconditionRequired,
       "aacEnclosureGeneralError": aacEnclosureGeneralError,
       "aacEnclosureFanError": aacEnclosureFanError,
       "aacEnclosurePowerSupplyError": aacEnclosurePowerSupplyError,
       "aacEnclosureTempAbnormal": aacEnclosureTempAbnormal,
       "aacEnclosureTempOver": aacEnclosureTempOver,
       "aacBatteryDead": aacBatteryDead,
       "aacBatteryImproving": aacBatteryImproving,
       "aacBatteryDegrading": aacBatteryDegrading,
       "aacBatteryGood": aacBatteryGood,
       "aacControllerPaused": aacControllerPaused,
       "aacContainerCreated": aacContainerCreated,
       "aacContainerDeleted": aacContainerDeleted,
       "aacDeviceFailurePredictionThresholdExceeded": aacDeviceFailurePredictionThresholdExceeded,
       "aacDeviceFailurePredictionTest": aacDeviceFailurePredictionTest,
       "aacDeviceWarning": aacDeviceWarning,
       "aacDeviceTemperatureWarning": aacDeviceTemperatureWarning,
       "aacDeviceDegradedWarning": aacDeviceDegradedWarning,
       "aacDeviceFailurePredictionConfigurationChanged": aacDeviceFailurePredictionConfigurationChanged,
       "adaptecArrayControllerSoftwareVersion": adaptecArrayControllerSoftwareVersion,
       "adaptecArrayControllerAdapterNumber": adaptecArrayControllerAdapterNumber,
       "adaptecArrayControllerAdapterTable": adaptecArrayControllerAdapterTable,
       "adaptecArrayControllerAdapterEntry": adaptecArrayControllerAdapterEntry,
       "adaptecArrayControllerAdapterIndex": adaptecArrayControllerAdapterIndex,
       "adaptecArrayControllerAdapterDescription": adaptecArrayControllerAdapterDescription,
       "adaptecArrayControllerAdapterType": adaptecArrayControllerAdapterType,
       "adaptecArrayControllerAdapterVersion": adaptecArrayControllerAdapterVersion,
       "adaptecArrayControllerAdapterChannelCount": adaptecArrayControllerAdapterChannelCount,
       "adaptecArrayControllerAdapterStatus": adaptecArrayControllerAdapterStatus,
       "adaptecArrayControllerAdapterBiosVersion": adaptecArrayControllerAdapterBiosVersion,
       "adaptecArrayControllerAdapterKernelVersion": adaptecArrayControllerAdapterKernelVersion,
       "adaptecArrayControllerAdapterMonitorVersion": adaptecArrayControllerAdapterMonitorVersion,
       "adaptecArrayControllerAdapterHardwareVersion": adaptecArrayControllerAdapterHardwareVersion,
       "adaptecArrayControllerAdapterTotalMemory": adaptecArrayControllerAdapterTotalMemory,
       "adaptecArrayControllerAdapterProgramMemory": adaptecArrayControllerAdapterProgramMemory,
       "adaptecArrayControllerAdapterBufferMemory": adaptecArrayControllerAdapterBufferMemory,
       "adaptecArrayControllerContainerTable": adaptecArrayControllerContainerTable,
       "adaptecArrayControllerContainerEntry": adaptecArrayControllerContainerEntry,
       "adaptecArrayControllerContIndex": adaptecArrayControllerContIndex,
       "adaptecArrayControllerContAdapterIndex": adaptecArrayControllerContAdapterIndex,
       "adaptecArrayControllerContNumber": adaptecArrayControllerContNumber,
       "adaptecArrayControllerContSize": adaptecArrayControllerContSize,
       "adaptecArrayControllerContMountPoint": adaptecArrayControllerContMountPoint,
       "adaptecArrayControllerContType": adaptecArrayControllerContType,
       "adaptecArrayControllerContUsage": adaptecArrayControllerContUsage,
       "adaptecArrayControllerContStatus": adaptecArrayControllerContStatus,
       "adaptecArrayControllerContStripeSize": adaptecArrayControllerContStripeSize,
       "adaptecArrayControllerDeviceTable": adaptecArrayControllerDeviceTable,
       "adaptecArrayControllerDeviceEntry": adaptecArrayControllerDeviceEntry,
       "adaptecArrayControllerDevIndex": adaptecArrayControllerDevIndex,
       "adaptecArrayControllerDevAdapterIndex": adaptecArrayControllerDevAdapterIndex,
       "adaptecArrayControllerDevChannelId": adaptecArrayControllerDevChannelId,
       "adaptecArrayControllerDevId": adaptecArrayControllerDevId,
       "adaptecArrayControllerDevLogicalNumber": adaptecArrayControllerDevLogicalNumber,
       "adaptecArrayControllerDevType": adaptecArrayControllerDevType,
       "adaptecArrayControllerDevVendor": adaptecArrayControllerDevVendor,
       "adaptecArrayControllerDevProduct": adaptecArrayControllerDevProduct,
       "adaptecArrayControllerDevRevision": adaptecArrayControllerDevRevision,
       "adaptecArrayControllerDevBlocks": adaptecArrayControllerDevBlocks,
       "adaptecArrayControllerDevBytesPerBlock": adaptecArrayControllerDevBytesPerBlock,
       "adaptecArrayControllerDevUsage": adaptecArrayControllerDevUsage,
       "adaptecArrayControllerDevStatus": adaptecArrayControllerDevStatus,
       "adaptecArrayControllerContainerToDeviceTable": adaptecArrayControllerContainerToDeviceTable,
       "adaptecArrayControllerContainerToDeviceEntry": adaptecArrayControllerContainerToDeviceEntry,
       "adaptecArrayControllerContainerToDeviceIndex": adaptecArrayControllerContainerToDeviceIndex,
       "adaptecArrayControllerCDAdapterIndex": adaptecArrayControllerCDAdapterIndex,
       "adaptecArrayControllerContainerIndex": adaptecArrayControllerContainerIndex,
       "adaptecArrayControllerDeviceIndex": adaptecArrayControllerDeviceIndex,
       "adaptecArrayControllerPartitionOffsetLSW": adaptecArrayControllerPartitionOffsetLSW,
       "adaptecArrayControllerPartitionOffsetMSW": adaptecArrayControllerPartitionOffsetMSW,
       "adaptecArrayControllerPartitionSizeLSW": adaptecArrayControllerPartitionSizeLSW,
       "adaptecArrayControllerPartitionSizeMSW": adaptecArrayControllerPartitionSizeMSW,
       "adaptecArrayControllerEnclosureTable": adaptecArrayControllerEnclosureTable,
       "adaptecArrayControllerEnclosureEntry": adaptecArrayControllerEnclosureEntry,
       "adaptecArrayControllerEnclosureIndex": adaptecArrayControllerEnclosureIndex,
       "adaptecArrayControllerEnclosureAdapterIndex": adaptecArrayControllerEnclosureAdapterIndex,
       "adaptecArrayControllerEnclosureProcessorId": adaptecArrayControllerEnclosureProcessorId,
       "adaptecArrayControllerEnclosureType": adaptecArrayControllerEnclosureType,
       "adaptecArrayControllerEnclosureNumberFans": adaptecArrayControllerEnclosureNumberFans,
       "adaptecArrayControllerEnclosureNumberPowerSupplies": adaptecArrayControllerEnclosureNumberPowerSupplies,
       "adaptecArrayControllerEnclosureNumberSlots": adaptecArrayControllerEnclosureNumberSlots,
       "adaptecArrayControllerEnclosureDoorLock": adaptecArrayControllerEnclosureDoorLock,
       "adaptecArrayControllerEnclosureNumberTemperatureSensors": adaptecArrayControllerEnclosureNumberTemperatureSensors,
       "adaptecArrayControllerEnclosureSpeaker": adaptecArrayControllerEnclosureSpeaker,
       "adaptecArrayControllerEnclosureBootTimeDiagnostic": adaptecArrayControllerEnclosureBootTimeDiagnostic,
       "adaptecArrayControllerEnclosureVendor": adaptecArrayControllerEnclosureVendor,
       "adaptecArrayControllerEnclosureProduct": adaptecArrayControllerEnclosureProduct,
       "adaptecArrayControllerEnclosureRevision": adaptecArrayControllerEnclosureRevision,
       "adaptecArrayControllerEnclosureIdLow": adaptecArrayControllerEnclosureIdLow,
       "adaptecArrayControllerEnclosureIdHigh": adaptecArrayControllerEnclosureIdHigh,
       "adaptecArrayControllerEnclosureStandardRevision": adaptecArrayControllerEnclosureStandardRevision,
       "adaptecArrayControllerEnclosurePowerOnTime": adaptecArrayControllerEnclosurePowerOnTime,
       "adaptecArrayControllerEnclosurePowerCycles": adaptecArrayControllerEnclosurePowerCycles,
       "adaptecArrayControllerEnclosureSpeakerStatus": adaptecArrayControllerEnclosureSpeakerStatus,
       "adaptecArrayControllerEnclosureOverTemperature": adaptecArrayControllerEnclosureOverTemperature,
       "adaptecArrayControllerEnclosureFanTable": adaptecArrayControllerEnclosureFanTable,
       "adaptecArrayControllerEnclosureFanEntry": adaptecArrayControllerEnclosureFanEntry,
       "adaptecArrayControllerEnclosureFanIndex": adaptecArrayControllerEnclosureFanIndex,
       "adaptecArrayControllerEnclosureFanEnclosureIndex": adaptecArrayControllerEnclosureFanEnclosureIndex,
       "adaptecArrayControllerEnclosureFanStatus": adaptecArrayControllerEnclosureFanStatus,
       "adaptecArrayControllerEnclosurePowerSupplyTable": adaptecArrayControllerEnclosurePowerSupplyTable,
       "adaptecArrayControllerEnclosurePowerSupplyEntry": adaptecArrayControllerEnclosurePowerSupplyEntry,
       "adaptecArrayControllerEnclosurePowerSupplyIndex": adaptecArrayControllerEnclosurePowerSupplyIndex,
       "adaptecArrayControllerEnclosurePowerSupplyEnclosureIndex": adaptecArrayControllerEnclosurePowerSupplyEnclosureIndex,
       "adaptecArrayControllerEnclosurePowerSupplyStatus": adaptecArrayControllerEnclosurePowerSupplyStatus,
       "adaptecArrayControllerEnclosureDoorLockTable": adaptecArrayControllerEnclosureDoorLockTable,
       "adaptecArrayControllerEnclosureDoorLockEntry": adaptecArrayControllerEnclosureDoorLockEntry,
       "adaptecArrayControllerEnclosureDoorLockIndex": adaptecArrayControllerEnclosureDoorLockIndex,
       "adaptecArrayControllerEnclosureDoorLockEnclosureIndex": adaptecArrayControllerEnclosureDoorLockEnclosureIndex,
       "adaptecArrayControllerEnclosureDoorLockSlot": adaptecArrayControllerEnclosureDoorLockSlot,
       "adaptecArrayControllerEnclosureDoorLockStatus": adaptecArrayControllerEnclosureDoorLockStatus,
       "adaptecArrayControllerEnclosureTemperatureSensorTable": adaptecArrayControllerEnclosureTemperatureSensorTable,
       "adaptecArrayControllerEnclosureTemperatureSensorEntry": adaptecArrayControllerEnclosureTemperatureSensorEntry,
       "adaptecArrayControllerEnclosureTemperatureSensorIndex": adaptecArrayControllerEnclosureTemperatureSensorIndex,
       "adaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex": adaptecArrayControllerEnclosureTemperatureSensorEnclosureIndex,
       "adaptecArrayControllerEnclosureTemperatureSensorOverTemperature": adaptecArrayControllerEnclosureTemperatureSensorOverTemperature,
       "adaptecArrayControllerEnclosureTemperatureSensorDegrees": adaptecArrayControllerEnclosureTemperatureSensorDegrees,
       "adaptecArrayControllerEnclosureScsiIdTable": adaptecArrayControllerEnclosureScsiIdTable,
       "adaptecArrayControllerEnclosureScsiIdEntry": adaptecArrayControllerEnclosureScsiIdEntry,
       "adaptecArrayControllerEnclosureScsiIdIndex": adaptecArrayControllerEnclosureScsiIdIndex,
       "adaptecArrayControllerEnclosureScsiIdEnclosureIndex": adaptecArrayControllerEnclosureScsiIdEnclosureIndex,
       "adaptecArrayControllerEnclosureScsiIdSlot": adaptecArrayControllerEnclosureScsiIdSlot,
       "adaptecArrayControllerEnclosureChannelId": adaptecArrayControllerEnclosureChannelId,
       "adaptecArrayControllerEnclosureScsiId": adaptecArrayControllerEnclosureScsiId,
       "adaptecArrayControllerEnclosureLunId": adaptecArrayControllerEnclosureLunId,
       "adaptecArrayControllerEnclosureDeviceInsertionTable": adaptecArrayControllerEnclosureDeviceInsertionTable,
       "adaptecArrayControllerEnclosureDeviceInsertionEntry": adaptecArrayControllerEnclosureDeviceInsertionEntry,
       "adaptecArrayControllerEnclosureDeviceInsertionIndex": adaptecArrayControllerEnclosureDeviceInsertionIndex,
       "adaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex": adaptecArrayControllerEnclosureDeviceInsertionEnclosureIndex,
       "adaptecArrayControllerEnclosureDeviceInsertionSlot": adaptecArrayControllerEnclosureDeviceInsertionSlot,
       "adaptecArrayControllerEnclosureDeviceInsertions": adaptecArrayControllerEnclosureDeviceInsertions,
       "adaptecArrayControllerEnclosureSlotStatusTable": adaptecArrayControllerEnclosureSlotStatusTable,
       "adaptecArrayControllerEnclosureSlotStatusEntry": adaptecArrayControllerEnclosureSlotStatusEntry,
       "adaptecArrayControllerEnclosureSlotStatusIndex": adaptecArrayControllerEnclosureSlotStatusIndex,
       "adaptecArrayControllerEnclosureSlotStatusEnclosureIndex": adaptecArrayControllerEnclosureSlotStatusEnclosureIndex,
       "adaptecArrayControllerEnclosureSlotStatusSlot": adaptecArrayControllerEnclosureSlotStatusSlot,
       "adaptecArrayControllerEnclosureSlotStatus": adaptecArrayControllerEnclosureSlotStatus,
       "adaptecArrayControllerTraps": adaptecArrayControllerTraps,
       "aacControllerId": aacControllerId,
       "aacContainerId": aacContainerId,
       "aacBusId": aacBusId,
       "aacScsiId": aacScsiId,
       "aacLunId": aacLunId,
       "aacEnclosureProcessorId": aacEnclosureProcessorId,
       "aacComponentUnitId": aacComponentUnitId}
)
