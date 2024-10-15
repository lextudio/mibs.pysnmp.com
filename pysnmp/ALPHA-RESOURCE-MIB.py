# SNMP MIB module (ALPHA-RESOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALPHA-RESOURCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:44 2024
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

alpha = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309)
)
alpha.setRevisions(
        ("2015-10-19 00:00",
         "2015-07-28 00:00",
         "2015-06-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScaledNumber(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-3"


# MIB Managed Objects in the order of their OIDs

_Controller_ObjectIdentity = ObjectIdentity
controller = _Controller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5)
)
_ControllerInfo_ObjectIdentity = ObjectIdentity
controllerInfo = _ControllerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1)
)


class _ControllerInfoName_Type(OctetString):
    """Custom type controllerInfoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ControllerInfoName_Type.__name__ = "OctetString"
_ControllerInfoName_Object = MibScalar
controllerInfoName = _ControllerInfoName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 1),
    _ControllerInfoName_Type()
)
controllerInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerInfoName.setStatus("current")


class _ControllerInfoDescription_Type(OctetString):
    """Custom type controllerInfoDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ControllerInfoDescription_Type.__name__ = "OctetString"
_ControllerInfoDescription_Object = MibScalar
controllerInfoDescription = _ControllerInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 2),
    _ControllerInfoDescription_Type()
)
controllerInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerInfoDescription.setStatus("current")


class _ControllerInfoSoftwareVersion_Type(OctetString):
    """Custom type controllerInfoSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ControllerInfoSoftwareVersion_Type.__name__ = "OctetString"
_ControllerInfoSoftwareVersion_Object = MibScalar
controllerInfoSoftwareVersion = _ControllerInfoSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 3),
    _ControllerInfoSoftwareVersion_Type()
)
controllerInfoSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerInfoSoftwareVersion.setStatus("current")
_ControllerInfoOperatingSystemVersion_Type = OctetString
_ControllerInfoOperatingSystemVersion_Object = MibScalar
controllerInfoOperatingSystemVersion = _ControllerInfoOperatingSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 4),
    _ControllerInfoOperatingSystemVersion_Type()
)
controllerInfoOperatingSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerInfoOperatingSystemVersion.setStatus("current")
_ControllerInfoHardwareVersion_Type = OctetString
_ControllerInfoHardwareVersion_Object = MibScalar
controllerInfoHardwareVersion = _ControllerInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 5),
    _ControllerInfoHardwareVersion_Type()
)
controllerInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerInfoHardwareVersion.setStatus("current")
_ControllerExtInfoTable_Object = MibTable
controllerExtInfoTable = _ControllerExtInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 100)
)
if mibBuilder.loadTexts:
    controllerExtInfoTable.setStatus("current")
_ControllerExtInfoEntry_Object = MibTableRow
controllerExtInfoEntry = _ControllerExtInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1)
)
controllerExtInfoEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "controllerExtInfoIndex"),
)
if mibBuilder.loadTexts:
    controllerExtInfoEntry.setStatus("current")


class _ControllerExtInfoIndex_Type(Unsigned32):
    """Custom type controllerExtInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ControllerExtInfoIndex_Type.__name__ = "Unsigned32"
_ControllerExtInfoIndex_Object = MibTableColumn
controllerExtInfoIndex = _ControllerExtInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 1),
    _ControllerExtInfoIndex_Type()
)
controllerExtInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controllerExtInfoIndex.setStatus("current")
_ControllerExtInfoName_Type = OctetString
_ControllerExtInfoName_Object = MibTableColumn
controllerExtInfoName = _ControllerExtInfoName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 2),
    _ControllerExtInfoName_Type()
)
controllerExtInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerExtInfoName.setStatus("current")


class _ControllerExtInfoStringValue_Type(OctetString):
    """Custom type controllerExtInfoStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ControllerExtInfoStringValue_Type.__name__ = "OctetString"
_ControllerExtInfoStringValue_Object = MibTableColumn
controllerExtInfoStringValue = _ControllerExtInfoStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 3),
    _ControllerExtInfoStringValue_Type()
)
controllerExtInfoStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerExtInfoStringValue.setStatus("current")


class _ControllerExtInfoUnit_Type(OctetString):
    """Custom type controllerExtInfoUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ControllerExtInfoUnit_Type.__name__ = "OctetString"
_ControllerExtInfoUnit_Object = MibTableColumn
controllerExtInfoUnit = _ControllerExtInfoUnit_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 4),
    _ControllerExtInfoUnit_Type()
)
controllerExtInfoUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerExtInfoUnit.setStatus("current")
_ControllerExtInfoNumberValue_Type = ScaledNumber
_ControllerExtInfoNumberValue_Object = MibTableColumn
controllerExtInfoNumberValue = _ControllerExtInfoNumberValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 5),
    _ControllerExtInfoNumberValue_Type()
)
controllerExtInfoNumberValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerExtInfoNumberValue.setStatus("current")
_Resource_ObjectIdentity = ObjectIdentity
resource = _Resource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2)
)
_ComponentList_ObjectIdentity = ObjectIdentity
componentList = _ComponentList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1)
)
_ComponentListCount_Type = Integer32
_ComponentListCount_Object = MibScalar
componentListCount = _ComponentListCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 1),
    _ComponentListCount_Type()
)
componentListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentListCount.setStatus("current")
_ComponentListTable_Object = MibTable
componentListTable = _ComponentListTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    componentListTable.setStatus("current")
_ComponentListEntry_Object = MibTableRow
componentListEntry = _ComponentListEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1)
)
componentListEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "componentListReference"),
)
if mibBuilder.loadTexts:
    componentListEntry.setStatus("current")


class _ComponentListReference_Type(Unsigned32):
    """Custom type componentListReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ComponentListReference_Type.__name__ = "Unsigned32"
_ComponentListReference_Object = MibTableColumn
componentListReference = _ComponentListReference_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 1),
    _ComponentListReference_Type()
)
componentListReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentListReference.setStatus("current")
_ComponentListStaticName_Type = OctetString
_ComponentListStaticName_Object = MibTableColumn
componentListStaticName = _ComponentListStaticName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 2),
    _ComponentListStaticName_Type()
)
componentListStaticName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentListStaticName.setStatus("current")


class _ComponentListConfiguredName_Type(OctetString):
    """Custom type componentListConfiguredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ComponentListConfiguredName_Type.__name__ = "OctetString"
_ComponentListConfiguredName_Object = MibTableColumn
componentListConfiguredName = _ComponentListConfiguredName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 3),
    _ComponentListConfiguredName_Type()
)
componentListConfiguredName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    componentListConfiguredName.setStatus("current")


class _ComponentListType_Type(Unsigned32):
    """Custom type componentListType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ComponentListType_Type.__name__ = "Unsigned32"
_ComponentListType_Object = MibTableColumn
componentListType = _ComponentListType_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 4),
    _ComponentListType_Type()
)
componentListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentListType.setStatus("current")


class _ComponentListModelNumber_Type(OctetString):
    """Custom type componentListModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ComponentListModelNumber_Type.__name__ = "OctetString"
_ComponentListModelNumber_Object = MibTableColumn
componentListModelNumber = _ComponentListModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 5),
    _ComponentListModelNumber_Type()
)
componentListModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentListModelNumber.setStatus("current")


class _ComponentListSerialNumber_Type(OctetString):
    """Custom type componentListSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ComponentListSerialNumber_Type.__name__ = "OctetString"
_ComponentListSerialNumber_Object = MibTableColumn
componentListSerialNumber = _ComponentListSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 6),
    _ComponentListSerialNumber_Type()
)
componentListSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentListSerialNumber.setStatus("current")
_ComponentListSystemPointer_Type = ObjectIdentifier
_ComponentListSystemPointer_Object = MibTableColumn
componentListSystemPointer = _ComponentListSystemPointer_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 7),
    _ComponentListSystemPointer_Type()
)
componentListSystemPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentListSystemPointer.setStatus("current")
_DataList_ObjectIdentity = ObjectIdentity
dataList = _DataList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 2)
)
_DataListCount_Type = Integer32
_DataListCount_Object = MibScalar
dataListCount = _DataListCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 1),
    _DataListCount_Type()
)
dataListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataListCount.setStatus("current")
_DataListTable_Object = MibTable
dataListTable = _DataListTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dataListTable.setStatus("current")
_DataListEntry_Object = MibTableRow
dataListEntry = _DataListEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1)
)
dataListEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "dataListReference"),
)
if mibBuilder.loadTexts:
    dataListEntry.setStatus("current")


class _DataListReference_Type(Unsigned32):
    """Custom type dataListReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DataListReference_Type.__name__ = "Unsigned32"
_DataListReference_Object = MibTableColumn
dataListReference = _DataListReference_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1, 1),
    _DataListReference_Type()
)
dataListReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataListReference.setStatus("current")


class _DataListName_Type(OctetString):
    """Custom type dataListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DataListName_Type.__name__ = "OctetString"
_DataListName_Object = MibTableColumn
dataListName = _DataListName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1, 2),
    _DataListName_Type()
)
dataListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataListName.setStatus("current")


class _DataListType_Type(Unsigned32):
    """Custom type dataListType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DataListType_Type.__name__ = "Unsigned32"
_DataListType_Object = MibTableColumn
dataListType = _DataListType_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1, 3),
    _DataListType_Type()
)
dataListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataListType.setStatus("current")
_DataListUnit_Type = OctetString
_DataListUnit_Object = MibTableColumn
dataListUnit = _DataListUnit_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1, 4),
    _DataListUnit_Type()
)
dataListUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataListUnit.setStatus("current")
_Data_ObjectIdentity = ObjectIdentity
data = _Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 3)
)
_DataCount_Type = Integer32
_DataCount_Object = MibScalar
dataCount = _DataCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 1),
    _DataCount_Type()
)
dataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCount.setStatus("current")
_DataTable_Object = MibTable
dataTable = _DataTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dataTable.setStatus("current")
_DataEntry_Object = MibTableRow
dataEntry = _DataEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2, 1)
)
dataEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "dataListReference"),
    (0, "ALPHA-RESOURCE-MIB", "componentListReference"),
)
if mibBuilder.loadTexts:
    dataEntry.setStatus("current")


class _DataReference_Type(Unsigned32):
    """Custom type dataReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DataReference_Type.__name__ = "Unsigned32"
_DataReference_Object = MibTableColumn
dataReference = _DataReference_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2, 1, 1),
    _DataReference_Type()
)
dataReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataReference.setStatus("current")
_DataNumberValue_Type = ScaledNumber
_DataNumberValue_Object = MibTableColumn
dataNumberValue = _DataNumberValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2, 1, 2),
    _DataNumberValue_Type()
)
dataNumberValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataNumberValue.setStatus("current")


class _DataStringValue_Type(OctetString):
    """Custom type dataStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DataStringValue_Type.__name__ = "OctetString"
_DataStringValue_Object = MibTableColumn
dataStringValue = _DataStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2, 1, 3),
    _DataStringValue_Type()
)
dataStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataStringValue.setStatus("current")
_ConfigurationList_ObjectIdentity = ObjectIdentity
configurationList = _ConfigurationList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 4)
)
_ConfigurationListCount_Type = Integer32
_ConfigurationListCount_Object = MibScalar
configurationListCount = _ConfigurationListCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 1),
    _ConfigurationListCount_Type()
)
configurationListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationListCount.setStatus("current")
_ConfigurationListTable_Object = MibTable
configurationListTable = _ConfigurationListTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2)
)
if mibBuilder.loadTexts:
    configurationListTable.setStatus("current")
_ConfigurationListEntry_Object = MibTableRow
configurationListEntry = _ConfigurationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1)
)
configurationListEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "configurationListReference"),
)
if mibBuilder.loadTexts:
    configurationListEntry.setStatus("current")


class _ConfigurationListReference_Type(Unsigned32):
    """Custom type configurationListReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ConfigurationListReference_Type.__name__ = "Unsigned32"
_ConfigurationListReference_Object = MibTableColumn
configurationListReference = _ConfigurationListReference_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1, 1),
    _ConfigurationListReference_Type()
)
configurationListReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configurationListReference.setStatus("current")


class _ConfigurationListName_Type(OctetString):
    """Custom type configurationListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConfigurationListName_Type.__name__ = "OctetString"
_ConfigurationListName_Object = MibTableColumn
configurationListName = _ConfigurationListName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1, 2),
    _ConfigurationListName_Type()
)
configurationListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationListName.setStatus("current")
_ConfigurationListType_Type = Integer32
_ConfigurationListType_Object = MibTableColumn
configurationListType = _ConfigurationListType_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1, 3),
    _ConfigurationListType_Type()
)
configurationListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationListType.setStatus("current")


class _ConfigurationListUnit_Type(OctetString):
    """Custom type configurationListUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ConfigurationListUnit_Type.__name__ = "OctetString"
_ConfigurationListUnit_Object = MibTableColumn
configurationListUnit = _ConfigurationListUnit_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1, 4),
    _ConfigurationListUnit_Type()
)
configurationListUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationListUnit.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 5)
)
_ConfigurationCount_Type = Integer32
_ConfigurationCount_Object = MibScalar
configurationCount = _ConfigurationCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 1),
    _ConfigurationCount_Type()
)
configurationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationCount.setStatus("current")
_ConfigurationTable_Object = MibTable
configurationTable = _ConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    configurationTable.setStatus("current")
_ConfigurationEntry_Object = MibTableRow
configurationEntry = _ConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2, 1)
)
configurationEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "configurationListReference"),
    (0, "ALPHA-RESOURCE-MIB", "componentListReference"),
)
if mibBuilder.loadTexts:
    configurationEntry.setStatus("current")


class _ConfigurationReference_Type(Unsigned32):
    """Custom type configurationReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ConfigurationReference_Type.__name__ = "Unsigned32"
_ConfigurationReference_Object = MibTableColumn
configurationReference = _ConfigurationReference_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2, 1, 1),
    _ConfigurationReference_Type()
)
configurationReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configurationReference.setStatus("current")
_ConfigurationNumberValue_Type = ScaledNumber
_ConfigurationNumberValue_Object = MibTableColumn
configurationNumberValue = _ConfigurationNumberValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2, 1, 2),
    _ConfigurationNumberValue_Type()
)
configurationNumberValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationNumberValue.setStatus("current")


class _ConfigurationStringValue_Type(OctetString):
    """Custom type configurationStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ConfigurationStringValue_Type.__name__ = "OctetString"
_ConfigurationStringValue_Object = MibTableColumn
configurationStringValue = _ConfigurationStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2, 1, 3),
    _ConfigurationStringValue_Type()
)
configurationStringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationStringValue.setStatus("current")
_CommandList_ObjectIdentity = ObjectIdentity
commandList = _CommandList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 6)
)
_CommandListCount_Type = Integer32
_CommandListCount_Object = MibScalar
commandListCount = _CommandListCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 1),
    _CommandListCount_Type()
)
commandListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandListCount.setStatus("current")
_CommandListTable_Object = MibTable
commandListTable = _CommandListTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 2)
)
if mibBuilder.loadTexts:
    commandListTable.setStatus("current")
_CommandListEntry_Object = MibTableRow
commandListEntry = _CommandListEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 2, 1)
)
commandListEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "commandListReference"),
)
if mibBuilder.loadTexts:
    commandListEntry.setStatus("current")


class _CommandListReference_Type(Unsigned32):
    """Custom type commandListReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CommandListReference_Type.__name__ = "Unsigned32"
_CommandListReference_Object = MibTableColumn
commandListReference = _CommandListReference_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 2, 1, 1),
    _CommandListReference_Type()
)
commandListReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    commandListReference.setStatus("current")


class _CommandListName_Type(OctetString):
    """Custom type commandListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CommandListName_Type.__name__ = "OctetString"
_CommandListName_Object = MibTableColumn
commandListName = _CommandListName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 2, 1, 2),
    _CommandListName_Type()
)
commandListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandListName.setStatus("current")
_Command_ObjectIdentity = ObjectIdentity
command = _Command_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 7)
)
_CommandCount_Type = Integer32
_CommandCount_Object = MibScalar
commandCount = _CommandCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 1),
    _CommandCount_Type()
)
commandCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandCount.setStatus("current")
_CommandTable_Object = MibTable
commandTable = _CommandTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 2)
)
if mibBuilder.loadTexts:
    commandTable.setStatus("current")
_CommandEntry_Object = MibTableRow
commandEntry = _CommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 2, 1)
)
commandEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "commandListReference"),
    (0, "ALPHA-RESOURCE-MIB", "componentListReference"),
)
if mibBuilder.loadTexts:
    commandEntry.setStatus("current")


class _CommandReference_Type(Unsigned32):
    """Custom type commandReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CommandReference_Type.__name__ = "Unsigned32"
_CommandReference_Object = MibTableColumn
commandReference = _CommandReference_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 2, 1, 1),
    _CommandReference_Type()
)
commandReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    commandReference.setStatus("current")
_CommandTrigger_Type = Integer32
_CommandTrigger_Object = MibTableColumn
commandTrigger = _CommandTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 2, 1, 2),
    _CommandTrigger_Type()
)
commandTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandTrigger.setStatus("current")
_AlarmType_ObjectIdentity = ObjectIdentity
alarmType = _AlarmType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 8)
)
_AlarmTypeCount_Type = Integer32
_AlarmTypeCount_Object = MibScalar
alarmTypeCount = _AlarmTypeCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 1),
    _AlarmTypeCount_Type()
)
alarmTypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTypeCount.setStatus("current")
_AlarmTypeTable_Object = MibTable
alarmTypeTable = _AlarmTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 2)
)
if mibBuilder.loadTexts:
    alarmTypeTable.setStatus("current")
_AlarmTypeEntry_Object = MibTableRow
alarmTypeEntry = _AlarmTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 2, 1)
)
alarmTypeEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "alarmTypeReference"),
)
if mibBuilder.loadTexts:
    alarmTypeEntry.setStatus("current")


class _AlarmTypeReference_Type(Unsigned32):
    """Custom type alarmTypeReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlarmTypeReference_Type.__name__ = "Unsigned32"
_AlarmTypeReference_Object = MibTableColumn
alarmTypeReference = _AlarmTypeReference_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 2, 1, 1),
    _AlarmTypeReference_Type()
)
alarmTypeReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmTypeReference.setStatus("current")


class _AlarmTypeName_Type(OctetString):
    """Custom type alarmTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AlarmTypeName_Type.__name__ = "OctetString"
_AlarmTypeName_Object = MibTableColumn
alarmTypeName = _AlarmTypeName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 2, 1, 2),
    _AlarmTypeName_Type()
)
alarmTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTypeName.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 9)
)
_AlarmCount_Type = Integer32
_AlarmCount_Object = MibScalar
alarmCount = _AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 9, 1),
    _AlarmCount_Type()
)
alarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCount.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 9, 2)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 9, 2, 1)
)
alarmEntry.setIndexNames(
    (0, "ALPHA-RESOURCE-MIB", "componentListType"),
    (0, "ALPHA-RESOURCE-MIB", "alarmTypeReference"),
    (0, "ALPHA-RESOURCE-MIB", "componentListReference"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmState_Type(Unsigned32):
    """Custom type alarmState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlarmState_Type.__name__ = "Unsigned32"
_AlarmState_Object = MibTableColumn
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 9, 2, 1, 1),
    _AlarmState_Type()
)
alarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmState.setStatus("current")
_ResourceConformance_ObjectIdentity = ObjectIdentity
resourceConformance = _ResourceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100)
)
_ResourceCompliances_ObjectIdentity = ObjectIdentity
resourceCompliances = _ResourceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1)
)
_ResourceGroups_ObjectIdentity = ObjectIdentity
resourceGroups = _ResourceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2)
)
_Simple_ObjectIdentity = ObjectIdentity
simple = _Simple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3)
)

# Managed Objects groups

alphaControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 1)
)
alphaControllerGroup.setObjects(
      *(("ALPHA-RESOURCE-MIB", "controllerInfoName"),
        ("ALPHA-RESOURCE-MIB", "controllerInfoDescription"),
        ("ALPHA-RESOURCE-MIB", "controllerInfoSoftwareVersion"),
        ("ALPHA-RESOURCE-MIB", "controllerInfoOperatingSystemVersion"),
        ("ALPHA-RESOURCE-MIB", "controllerInfoHardwareVersion"),
        ("ALPHA-RESOURCE-MIB", "controllerExtInfoName"),
        ("ALPHA-RESOURCE-MIB", "controllerExtInfoStringValue"),
        ("ALPHA-RESOURCE-MIB", "controllerExtInfoUnit"),
        ("ALPHA-RESOURCE-MIB", "controllerExtInfoNumberValue"))
)
if mibBuilder.loadTexts:
    alphaControllerGroup.setStatus("current")

alphaComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 2)
)
alphaComponentGroup.setObjects(
      *(("ALPHA-RESOURCE-MIB", "componentListCount"),
        ("ALPHA-RESOURCE-MIB", "componentListStaticName"),
        ("ALPHA-RESOURCE-MIB", "componentListConfiguredName"),
        ("ALPHA-RESOURCE-MIB", "componentListModelNumber"),
        ("ALPHA-RESOURCE-MIB", "componentListSerialNumber"),
        ("ALPHA-RESOURCE-MIB", "componentListSystemPointer"))
)
if mibBuilder.loadTexts:
    alphaComponentGroup.setStatus("current")

alphaDataTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 3)
)
alphaDataTypeGroup.setObjects(
      *(("ALPHA-RESOURCE-MIB", "dataListCount"),
        ("ALPHA-RESOURCE-MIB", "dataListName"),
        ("ALPHA-RESOURCE-MIB", "dataListUnit"))
)
if mibBuilder.loadTexts:
    alphaDataTypeGroup.setStatus("current")

alphaDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 4)
)
alphaDataGroup.setObjects(
      *(("ALPHA-RESOURCE-MIB", "dataCount"),
        ("ALPHA-RESOURCE-MIB", "dataNumberValue"),
        ("ALPHA-RESOURCE-MIB", "dataStringValue"))
)
if mibBuilder.loadTexts:
    alphaDataGroup.setStatus("current")

alphaConfigurationTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 5)
)
alphaConfigurationTypeGroup.setObjects(
      *(("ALPHA-RESOURCE-MIB", "configurationListCount"),
        ("ALPHA-RESOURCE-MIB", "configurationListName"),
        ("ALPHA-RESOURCE-MIB", "configurationListType"),
        ("ALPHA-RESOURCE-MIB", "configurationListUnit"))
)
if mibBuilder.loadTexts:
    alphaConfigurationTypeGroup.setStatus("current")

alphaConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 6)
)
alphaConfigurationGroup.setObjects(
      *(("ALPHA-RESOURCE-MIB", "configurationCount"),
        ("ALPHA-RESOURCE-MIB", "configurationStringValue"),
        ("ALPHA-RESOURCE-MIB", "configurationNumberValue"))
)
if mibBuilder.loadTexts:
    alphaConfigurationGroup.setStatus("current")

alphaCommandTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 7)
)
alphaCommandTypeGroup.setObjects(
      *(("ALPHA-RESOURCE-MIB", "commandListCount"),
        ("ALPHA-RESOURCE-MIB", "commandListName"))
)
if mibBuilder.loadTexts:
    alphaCommandTypeGroup.setStatus("current")

alphaCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 8)
)
alphaCommandGroup.setObjects(
      *(("ALPHA-RESOURCE-MIB", "commandCount"),
        ("ALPHA-RESOURCE-MIB", "commandTrigger"))
)
if mibBuilder.loadTexts:
    alphaCommandGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

resourceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 1)
)
if mibBuilder.loadTexts:
    resourceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPHA-RESOURCE-MIB",
    **{"ScaledNumber": ScaledNumber,
       "alpha": alpha,
       "controller": controller,
       "controllerInfo": controllerInfo,
       "controllerInfoName": controllerInfoName,
       "controllerInfoDescription": controllerInfoDescription,
       "controllerInfoSoftwareVersion": controllerInfoSoftwareVersion,
       "controllerInfoOperatingSystemVersion": controllerInfoOperatingSystemVersion,
       "controllerInfoHardwareVersion": controllerInfoHardwareVersion,
       "controllerExtInfoTable": controllerExtInfoTable,
       "controllerExtInfoEntry": controllerExtInfoEntry,
       "controllerExtInfoIndex": controllerExtInfoIndex,
       "controllerExtInfoName": controllerExtInfoName,
       "controllerExtInfoStringValue": controllerExtInfoStringValue,
       "controllerExtInfoUnit": controllerExtInfoUnit,
       "controllerExtInfoNumberValue": controllerExtInfoNumberValue,
       "resource": resource,
       "componentList": componentList,
       "componentListCount": componentListCount,
       "componentListTable": componentListTable,
       "componentListEntry": componentListEntry,
       "componentListReference": componentListReference,
       "componentListStaticName": componentListStaticName,
       "componentListConfiguredName": componentListConfiguredName,
       "componentListType": componentListType,
       "componentListModelNumber": componentListModelNumber,
       "componentListSerialNumber": componentListSerialNumber,
       "componentListSystemPointer": componentListSystemPointer,
       "dataList": dataList,
       "dataListCount": dataListCount,
       "dataListTable": dataListTable,
       "dataListEntry": dataListEntry,
       "dataListReference": dataListReference,
       "dataListName": dataListName,
       "dataListType": dataListType,
       "dataListUnit": dataListUnit,
       "data": data,
       "dataCount": dataCount,
       "dataTable": dataTable,
       "dataEntry": dataEntry,
       "dataReference": dataReference,
       "dataNumberValue": dataNumberValue,
       "dataStringValue": dataStringValue,
       "configurationList": configurationList,
       "configurationListCount": configurationListCount,
       "configurationListTable": configurationListTable,
       "configurationListEntry": configurationListEntry,
       "configurationListReference": configurationListReference,
       "configurationListName": configurationListName,
       "configurationListType": configurationListType,
       "configurationListUnit": configurationListUnit,
       "configuration": configuration,
       "configurationCount": configurationCount,
       "configurationTable": configurationTable,
       "configurationEntry": configurationEntry,
       "configurationReference": configurationReference,
       "configurationNumberValue": configurationNumberValue,
       "configurationStringValue": configurationStringValue,
       "commandList": commandList,
       "commandListCount": commandListCount,
       "commandListTable": commandListTable,
       "commandListEntry": commandListEntry,
       "commandListReference": commandListReference,
       "commandListName": commandListName,
       "command": command,
       "commandCount": commandCount,
       "commandTable": commandTable,
       "commandEntry": commandEntry,
       "commandReference": commandReference,
       "commandTrigger": commandTrigger,
       "alarmType": alarmType,
       "alarmTypeCount": alarmTypeCount,
       "alarmTypeTable": alarmTypeTable,
       "alarmTypeEntry": alarmTypeEntry,
       "alarmTypeReference": alarmTypeReference,
       "alarmTypeName": alarmTypeName,
       "alarm": alarm,
       "alarmCount": alarmCount,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmState": alarmState,
       "resourceConformance": resourceConformance,
       "resourceCompliances": resourceCompliances,
       "resourceCompliance": resourceCompliance,
       "resourceGroups": resourceGroups,
       "alphaControllerGroup": alphaControllerGroup,
       "alphaComponentGroup": alphaComponentGroup,
       "alphaDataTypeGroup": alphaDataTypeGroup,
       "alphaDataGroup": alphaDataGroup,
       "alphaConfigurationTypeGroup": alphaConfigurationTypeGroup,
       "alphaConfigurationGroup": alphaConfigurationGroup,
       "alphaCommandTypeGroup": alphaCommandTypeGroup,
       "alphaCommandGroup": alphaCommandGroup,
       "simple": simple}
)
