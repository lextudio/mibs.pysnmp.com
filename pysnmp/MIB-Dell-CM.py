# SNMP MIB module (MIB-Dell-CM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIB-Dell-CM
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:26 2024
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


# Types definitions



class SystemID(OctetString):
    """Custom type SystemID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )





class Unsigned16BitRange(Integer32):
    """Custom type Unsigned16BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Cm_ObjectIdentity = ObjectIdentity
cm = _Cm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10899)
)
_InventoryGroup_ObjectIdentity = ObjectIdentity
inventoryGroup = _InventoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1)
)
_InventoryLocale_Type = DisplayString
_InventoryLocale_Object = MibScalar
inventoryLocale = _InventoryLocale_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 1),
    _InventoryLocale_Type()
)
inventoryLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryLocale.setStatus("mandatory")
_InventorySchemaVersion_Type = DisplayString
_InventorySchemaVersion_Object = MibScalar
inventorySchemaVersion = _InventorySchemaVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 2),
    _InventorySchemaVersion_Type()
)
inventorySchemaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySchemaVersion.setStatus("mandatory")
_InventorySystemID_Type = SystemID
_InventorySystemID_Object = MibScalar
inventorySystemID = _InventorySystemID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 3),
    _InventorySystemID_Type()
)
inventorySystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySystemID.setStatus("mandatory")
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("mandatory")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1)
)
deviceEntry.setIndexNames(
    (0, "MIB-Dell-CM", "deviceIndex"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("mandatory")
_DeviceIndex_Type = Unsigned16BitRange
_DeviceIndex_Object = MibTableColumn
deviceIndex = _DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 1),
    _DeviceIndex_Type()
)
deviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIndex.setStatus("mandatory")
_DeviceComponentID_Type = Integer32
_DeviceComponentID_Object = MibTableColumn
deviceComponentID = _DeviceComponentID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 2),
    _DeviceComponentID_Type()
)
deviceComponentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceComponentID.setStatus("mandatory")
_DeviceDisplayString_Type = DisplayString
_DeviceDisplayString_Object = MibTableColumn
deviceDisplayString = _DeviceDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 3),
    _DeviceDisplayString_Type()
)
deviceDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDisplayString.setStatus("mandatory")
_DeviceVendorID_Type = OctetString
_DeviceVendorID_Object = MibTableColumn
deviceVendorID = _DeviceVendorID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 4),
    _DeviceVendorID_Type()
)
deviceVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVendorID.setStatus("mandatory")
_DeviceDeviceID_Type = OctetString
_DeviceDeviceID_Object = MibTableColumn
deviceDeviceID = _DeviceDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 5),
    _DeviceDeviceID_Type()
)
deviceDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDeviceID.setStatus("mandatory")
_DeviceSubID_Type = OctetString
_DeviceSubID_Object = MibTableColumn
deviceSubID = _DeviceSubID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 6),
    _DeviceSubID_Type()
)
deviceSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSubID.setStatus("mandatory")
_DeviceSubVendorID_Type = OctetString
_DeviceSubVendorID_Object = MibTableColumn
deviceSubVendorID = _DeviceSubVendorID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 7),
    _DeviceSubVendorID_Type()
)
deviceSubVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSubVendorID.setStatus("mandatory")
_ApplicationTable_Object = MibTable
applicationTable = _ApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 6)
)
if mibBuilder.loadTexts:
    applicationTable.setStatus("mandatory")
_ApplicationEntry_Object = MibTableRow
applicationEntry = _ApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1)
)
applicationEntry.setIndexNames(
    (0, "MIB-Dell-CM", "applicationIndex"),
)
if mibBuilder.loadTexts:
    applicationEntry.setStatus("mandatory")
_ApplicationIndex_Type = Unsigned16BitRange
_ApplicationIndex_Object = MibTableColumn
applicationIndex = _ApplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 1),
    _ApplicationIndex_Type()
)
applicationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationIndex.setStatus("mandatory")
_ApplicationDeviceIndex_Type = Unsigned16BitRange
_ApplicationDeviceIndex_Object = MibTableColumn
applicationDeviceIndex = _ApplicationDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 2),
    _ApplicationDeviceIndex_Type()
)
applicationDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationDeviceIndex.setStatus("mandatory")
_ApplicationComponentType_Type = DisplayString
_ApplicationComponentType_Object = MibTableColumn
applicationComponentType = _ApplicationComponentType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 3),
    _ApplicationComponentType_Type()
)
applicationComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationComponentType.setStatus("mandatory")
_ApplicationVersion_Type = DisplayString
_ApplicationVersion_Object = MibTableColumn
applicationVersion = _ApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 4),
    _ApplicationVersion_Type()
)
applicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationVersion.setStatus("mandatory")
_ApplicationDisplayString_Type = DisplayString
_ApplicationDisplayString_Object = MibTableColumn
applicationDisplayString = _ApplicationDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 5),
    _ApplicationDisplayString_Type()
)
applicationDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationDisplayString.setStatus("mandatory")
_ApplicationSubComponentID_Type = DisplayString
_ApplicationSubComponentID_Object = MibTableColumn
applicationSubComponentID = _ApplicationSubComponentID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 6),
    _ApplicationSubComponentID_Type()
)
applicationSubComponentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationSubComponentID.setStatus("mandatory")
_OperatingSystemGroup_ObjectIdentity = ObjectIdentity
operatingSystemGroup = _OperatingSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10899, 2)
)
_OperatingSystemVendor_Type = DisplayString
_OperatingSystemVendor_Object = MibScalar
operatingSystemVendor = _OperatingSystemVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 2, 1),
    _OperatingSystemVendor_Type()
)
operatingSystemVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemVendor.setStatus("mandatory")
_OperatingSystemMajorVersion_Type = DisplayString
_OperatingSystemMajorVersion_Object = MibScalar
operatingSystemMajorVersion = _OperatingSystemMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 2, 2),
    _OperatingSystemMajorVersion_Type()
)
operatingSystemMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMajorVersion.setStatus("mandatory")
_OperatingSystemMinorVersion_Type = DisplayString
_OperatingSystemMinorVersion_Object = MibScalar
operatingSystemMinorVersion = _OperatingSystemMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 2, 3),
    _OperatingSystemMinorVersion_Type()
)
operatingSystemMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMinorVersion.setStatus("mandatory")
_OperatingSystemSPMajorVersion_Type = DisplayString
_OperatingSystemSPMajorVersion_Object = MibScalar
operatingSystemSPMajorVersion = _OperatingSystemSPMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 2, 5),
    _OperatingSystemSPMajorVersion_Type()
)
operatingSystemSPMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemSPMajorVersion.setStatus("mandatory")
_OperatingSystemSPMinorVersion_Type = DisplayString
_OperatingSystemSPMinorVersion_Object = MibScalar
operatingSystemSPMinorVersion = _OperatingSystemSPMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 2, 6),
    _OperatingSystemSPMinorVersion_Type()
)
operatingSystemSPMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemSPMinorVersion.setStatus("mandatory")
_OperatingSystemArchitecture_Type = DisplayString
_OperatingSystemArchitecture_Object = MibScalar
operatingSystemArchitecture = _OperatingSystemArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 2, 7),
    _OperatingSystemArchitecture_Type()
)
operatingSystemArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemArchitecture.setStatus("mandatory")
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10899, 100)
)
_ProductIDDisplayName_Type = DisplayString
_ProductIDDisplayName_Object = MibScalar
productIDDisplayName = _ProductIDDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 100, 1),
    _ProductIDDisplayName_Type()
)
productIDDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDDisplayName.setStatus("mandatory")
_ProductIDDescription_Type = DisplayString
_ProductIDDescription_Object = MibScalar
productIDDescription = _ProductIDDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 100, 2),
    _ProductIDDescription_Type()
)
productIDDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDDescription.setStatus("mandatory")
_ProductIDVendor_Type = DisplayString
_ProductIDVendor_Object = MibScalar
productIDVendor = _ProductIDVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 100, 3),
    _ProductIDVendor_Type()
)
productIDVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDVendor.setStatus("mandatory")
_ProductIDVersion_Type = DisplayString
_ProductIDVersion_Object = MibScalar
productIDVersion = _ProductIDVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 100, 4),
    _ProductIDVersion_Type()
)
productIDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDVersion.setStatus("mandatory")
_ProductIDBuildNumber_Type = DisplayString
_ProductIDBuildNumber_Object = MibScalar
productIDBuildNumber = _ProductIDBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10899, 100, 5),
    _ProductIDBuildNumber_Type()
)
productIDBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDBuildNumber.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-Dell-CM",
    **{"SystemID": SystemID,
       "Unsigned16BitRange": Unsigned16BitRange,
       "dell": dell,
       "cm": cm,
       "inventoryGroup": inventoryGroup,
       "inventoryLocale": inventoryLocale,
       "inventorySchemaVersion": inventorySchemaVersion,
       "inventorySystemID": inventorySystemID,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "deviceIndex": deviceIndex,
       "deviceComponentID": deviceComponentID,
       "deviceDisplayString": deviceDisplayString,
       "deviceVendorID": deviceVendorID,
       "deviceDeviceID": deviceDeviceID,
       "deviceSubID": deviceSubID,
       "deviceSubVendorID": deviceSubVendorID,
       "applicationTable": applicationTable,
       "applicationEntry": applicationEntry,
       "applicationIndex": applicationIndex,
       "applicationDeviceIndex": applicationDeviceIndex,
       "applicationComponentType": applicationComponentType,
       "applicationVersion": applicationVersion,
       "applicationDisplayString": applicationDisplayString,
       "applicationSubComponentID": applicationSubComponentID,
       "operatingSystemGroup": operatingSystemGroup,
       "operatingSystemVendor": operatingSystemVendor,
       "operatingSystemMajorVersion": operatingSystemMajorVersion,
       "operatingSystemMinorVersion": operatingSystemMinorVersion,
       "operatingSystemSPMajorVersion": operatingSystemSPMajorVersion,
       "operatingSystemSPMinorVersion": operatingSystemSPMinorVersion,
       "operatingSystemArchitecture": operatingSystemArchitecture,
       "productID": productID,
       "productIDDisplayName": productIDDisplayName,
       "productIDDescription": productIDDescription,
       "productIDVendor": productIDVendor,
       "productIDVersion": productIDVersion,
       "productIDBuildNumber": productIDBuildNumber}
)
