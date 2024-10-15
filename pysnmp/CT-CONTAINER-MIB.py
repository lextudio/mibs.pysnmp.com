# SNMP MIB module (CT-CONTAINER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-CONTAINER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:02 2024
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

(ctChassis2,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctChassis2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ContType_ObjectIdentity = ObjectIdentity
contType = _ContType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1)
)
_ContTypeDevice_Type = ObjectIdentifier
_ContTypeDevice_Object = MibScalar
contTypeDevice = _ContTypeDevice_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 1),
    _ContTypeDevice_Type()
)
contTypeDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypeDevice.setStatus("mandatory")
_ContTypePhysicalEntries_Type = Integer32
_ContTypePhysicalEntries_Object = MibScalar
contTypePhysicalEntries = _ContTypePhysicalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 2),
    _ContTypePhysicalEntries_Type()
)
contTypePhysicalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypePhysicalEntries.setStatus("mandatory")
_ContTypePhysicalChanges_Type = Counter32
_ContTypePhysicalChanges_Object = MibScalar
contTypePhysicalChanges = _ContTypePhysicalChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 3),
    _ContTypePhysicalChanges_Type()
)
contTypePhysicalChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypePhysicalChanges.setStatus("mandatory")
_ContTypeLogicalChanges_Type = Counter32
_ContTypeLogicalChanges_Object = MibScalar
contTypeLogicalChanges = _ContTypeLogicalChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 4),
    _ContTypeLogicalChanges_Type()
)
contTypeLogicalChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypeLogicalChanges.setStatus("mandatory")
_ContTypeSerialNumber_Type = DisplayString
_ContTypeSerialNumber_Object = MibScalar
contTypeSerialNumber = _ContTypeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 5),
    _ContTypeSerialNumber_Type()
)
contTypeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypeSerialNumber.setStatus("mandatory")
_ContTypeContainingDevice_Type = ObjectIdentifier
_ContTypeContainingDevice_Object = MibScalar
contTypeContainingDevice = _ContTypeContainingDevice_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 6),
    _ContTypeContainingDevice_Type()
)
contTypeContainingDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypeContainingDevice.setStatus("mandatory")
_ContTypeContainingPhysicalEntries_Type = Integer32
_ContTypeContainingPhysicalEntries_Object = MibScalar
contTypeContainingPhysicalEntries = _ContTypeContainingPhysicalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 7),
    _ContTypeContainingPhysicalEntries_Type()
)
contTypeContainingPhysicalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypeContainingPhysicalEntries.setStatus("mandatory")
_ContTypeContainingPhysicalEntryID_Type = Integer32
_ContTypeContainingPhysicalEntryID_Object = MibScalar
contTypeContainingPhysicalEntryID = _ContTypeContainingPhysicalEntryID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 8),
    _ContTypeContainingPhysicalEntryID_Type()
)
contTypeContainingPhysicalEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypeContainingPhysicalEntryID.setStatus("mandatory")
_ContTypeContainingSerialNumber_Type = DisplayString
_ContTypeContainingSerialNumber_Object = MibScalar
contTypeContainingSerialNumber = _ContTypeContainingSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 1, 9),
    _ContTypeContainingSerialNumber_Type()
)
contTypeContainingSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contTypeContainingSerialNumber.setStatus("mandatory")
_ContLogical_ObjectIdentity = ObjectIdentity
contLogical = _ContLogical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2)
)
_ContLogicalEntryTable_Object = MibTable
contLogicalEntryTable = _ContLogicalEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    contLogicalEntryTable.setStatus("mandatory")
_ContLogicalEntry_Object = MibTableRow
contLogicalEntry = _ContLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1)
)
contLogicalEntry.setIndexNames(
    (0, "CT-CONTAINER-MIB", "contLogicalEntryID"),
)
if mibBuilder.loadTexts:
    contLogicalEntry.setStatus("mandatory")
_ContLogicalEntryID_Type = Integer32
_ContLogicalEntryID_Object = MibTableColumn
contLogicalEntryID = _ContLogicalEntryID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 1),
    _ContLogicalEntryID_Type()
)
contLogicalEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntryID.setStatus("mandatory")
_ContLogicalEntryType_Type = ObjectIdentifier
_ContLogicalEntryType_Object = MibTableColumn
contLogicalEntryType = _ContLogicalEntryType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 2),
    _ContLogicalEntryType_Type()
)
contLogicalEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntryType.setStatus("mandatory")


class _ContLogicalEntryName_Type(DisplayString):
    """Custom type contLogicalEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ContLogicalEntryName_Type.__name__ = "DisplayString"
_ContLogicalEntryName_Object = MibTableColumn
contLogicalEntryName = _ContLogicalEntryName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 3),
    _ContLogicalEntryName_Type()
)
contLogicalEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntryName.setStatus("mandatory")


class _ContLogicalEntryVersion_Type(DisplayString):
    """Custom type contLogicalEntryVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ContLogicalEntryVersion_Type.__name__ = "DisplayString"
_ContLogicalEntryVersion_Object = MibTableColumn
contLogicalEntryVersion = _ContLogicalEntryVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 4),
    _ContLogicalEntryVersion_Type()
)
contLogicalEntryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntryVersion.setStatus("mandatory")
_ContLogicalEntryROCommStr_Type = OctetString
_ContLogicalEntryROCommStr_Object = MibTableColumn
contLogicalEntryROCommStr = _ContLogicalEntryROCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 5),
    _ContLogicalEntryROCommStr_Type()
)
contLogicalEntryROCommStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntryROCommStr.setStatus("mandatory")
_ContLogicalEntryRWCommStr_Type = OctetString
_ContLogicalEntryRWCommStr_Object = MibTableColumn
contLogicalEntryRWCommStr = _ContLogicalEntryRWCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 6),
    _ContLogicalEntryRWCommStr_Type()
)
contLogicalEntryRWCommStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntryRWCommStr.setStatus("mandatory")
_ContLogicalEntrySUCommStr_Type = OctetString
_ContLogicalEntrySUCommStr_Object = MibTableColumn
contLogicalEntrySUCommStr = _ContLogicalEntrySUCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 7),
    _ContLogicalEntrySUCommStr_Type()
)
contLogicalEntrySUCommStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntrySUCommStr.setStatus("mandatory")


class _ContLogicalEntryAdminStatus_Type(Integer32):
    """Custom type contLogicalEntryAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 7),
          ("enable", 3),
          ("reset", 9))
    )


_ContLogicalEntryAdminStatus_Type.__name__ = "Integer32"
_ContLogicalEntryAdminStatus_Object = MibTableColumn
contLogicalEntryAdminStatus = _ContLogicalEntryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 8),
    _ContLogicalEntryAdminStatus_Type()
)
contLogicalEntryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contLogicalEntryAdminStatus.setStatus("mandatory")


class _ContLogicalEntryOperStatus_Type(Integer32):
    """Custom type contLogicalEntryOperStatus based on Integer32"""
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
        *(("delete", 8),
          ("disabled", 7),
          ("enabled", 3),
          ("error", 6),
          ("invalid", 2),
          ("operational", 5),
          ("testing", 4),
          ("unknown", 1))
    )


_ContLogicalEntryOperStatus_Type.__name__ = "Integer32"
_ContLogicalEntryOperStatus_Object = MibTableColumn
contLogicalEntryOperStatus = _ContLogicalEntryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 2, 1, 1, 9),
    _ContLogicalEntryOperStatus_Type()
)
contLogicalEntryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntryOperStatus.setStatus("mandatory")
_ContPhysical_ObjectIdentity = ObjectIdentity
contPhysical = _ContPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3)
)
_ContPhysicalEntryTable_Object = MibTable
contPhysicalEntryTable = _ContPhysicalEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    contPhysicalEntryTable.setStatus("mandatory")
_ContPhysicalEntry_Object = MibTableRow
contPhysicalEntry = _ContPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 1, 1)
)
contPhysicalEntry.setIndexNames(
    (0, "CT-CONTAINER-MIB", "contPhysicalEntryID"),
)
if mibBuilder.loadTexts:
    contPhysicalEntry.setStatus("mandatory")
_ContPhysicalEntryID_Type = Integer32
_ContPhysicalEntryID_Object = MibTableColumn
contPhysicalEntryID = _ContPhysicalEntryID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 1, 1, 1),
    _ContPhysicalEntryID_Type()
)
contPhysicalEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contPhysicalEntryID.setStatus("mandatory")
_ContPhysicalEntries_Type = Integer32
_ContPhysicalEntries_Object = MibTableColumn
contPhysicalEntries = _ContPhysicalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 1, 1, 2),
    _ContPhysicalEntries_Type()
)
contPhysicalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contPhysicalEntries.setStatus("mandatory")
_ContPhysicalEntryClass_Type = ObjectIdentifier
_ContPhysicalEntryClass_Object = MibTableColumn
contPhysicalEntryClass = _ContPhysicalEntryClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 1, 1, 3),
    _ContPhysicalEntryClass_Type()
)
contPhysicalEntryClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contPhysicalEntryClass.setStatus("mandatory")
_ContPhysicalEntryType_Type = ObjectIdentifier
_ContPhysicalEntryType_Object = MibTableColumn
contPhysicalEntryType = _ContPhysicalEntryType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 1, 1, 4),
    _ContPhysicalEntryType_Type()
)
contPhysicalEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contPhysicalEntryType.setStatus("mandatory")
_ContPhysicalEntryTimeStamp_Type = TimeTicks
_ContPhysicalEntryTimeStamp_Object = MibTableColumn
contPhysicalEntryTimeStamp = _ContPhysicalEntryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 1, 1, 5),
    _ContPhysicalEntryTimeStamp_Type()
)
contPhysicalEntryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contPhysicalEntryTimeStamp.setStatus("mandatory")


class _ContPhysicalEntryStatus_Type(Integer32):
    """Custom type contPhysicalEntryStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("booting", 11),
          ("busy", 3),
          ("crippled", 4),
          ("error", 6),
          ("operational", 5),
          ("powerOff", 2),
          ("reset", 1),
          ("testing", 7))
    )


_ContPhysicalEntryStatus_Type.__name__ = "Integer32"
_ContPhysicalEntryStatus_Object = MibTableColumn
contPhysicalEntryStatus = _ContPhysicalEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 1, 1, 6),
    _ContPhysicalEntryStatus_Type()
)
contPhysicalEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contPhysicalEntryStatus.setStatus("mandatory")
_ContLogicalToPhysicalMapTable_Object = MibTable
contLogicalToPhysicalMapTable = _ContLogicalToPhysicalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    contLogicalToPhysicalMapTable.setStatus("mandatory")
_ContLogicalToPhysicalMapEntry_Object = MibTableRow
contLogicalToPhysicalMapEntry = _ContLogicalToPhysicalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 2, 1)
)
contLogicalToPhysicalMapEntry.setIndexNames(
    (0, "CT-CONTAINER-MIB", "contPhysicalEntryID"),
    (0, "CT-CONTAINER-MIB", "contLogicalEntryID"),
)
if mibBuilder.loadTexts:
    contLogicalToPhysicalMapEntry.setStatus("mandatory")
_ContPhysicalEntryMapID_Type = Integer32
_ContPhysicalEntryMapID_Object = MibTableColumn
contPhysicalEntryMapID = _ContPhysicalEntryMapID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 2, 1, 1),
    _ContPhysicalEntryMapID_Type()
)
contPhysicalEntryMapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contPhysicalEntryMapID.setStatus("mandatory")
_ContLogicalEntryMapID_Type = Integer32
_ContLogicalEntryMapID_Object = MibTableColumn
contLogicalEntryMapID = _ContLogicalEntryMapID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 3, 2, 1, 2),
    _ContLogicalEntryMapID_Type()
)
contLogicalEntryMapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contLogicalEntryMapID.setStatus("mandatory")
_ContResource_ObjectIdentity = ObjectIdentity
contResource = _ContResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 4)
)
_ContResourceTable_Object = MibTable
contResourceTable = _ContResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    contResourceTable.setStatus("mandatory")
_ContResourceEntry_Object = MibTableRow
contResourceEntry = _ContResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 4, 1, 1)
)
contResourceEntry.setIndexNames(
    (0, "CT-CONTAINER-MIB", "contResourceID"),
)
if mibBuilder.loadTexts:
    contResourceEntry.setStatus("mandatory")
_ContResourceID_Type = Integer32
_ContResourceID_Object = MibTableColumn
contResourceID = _ContResourceID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 4, 1, 1, 1),
    _ContResourceID_Type()
)
contResourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contResourceID.setStatus("mandatory")
_ContResourceType_Type = ObjectIdentifier
_ContResourceType_Object = MibTableColumn
contResourceType = _ContResourceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 4, 1, 1, 2),
    _ContResourceType_Type()
)
contResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contResourceType.setStatus("mandatory")
_ContResourceMibPointer_Type = ObjectIdentifier
_ContResourceMibPointer_Object = MibTableColumn
contResourceMibPointer = _ContResourceMibPointer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 4, 1, 1, 3),
    _ContResourceMibPointer_Type()
)
contResourceMibPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contResourceMibPointer.setStatus("mandatory")
_ContCommStr_ObjectIdentity = ObjectIdentity
contCommStr = _ContCommStr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 5)
)
_ContROCommStr_Type = OctetString
_ContROCommStr_Object = MibScalar
contROCommStr = _ContROCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 5, 1),
    _ContROCommStr_Type()
)
contROCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contROCommStr.setStatus("mandatory")
_ContRWCommStr_Type = OctetString
_ContRWCommStr_Object = MibScalar
contRWCommStr = _ContRWCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 5, 2),
    _ContRWCommStr_Type()
)
contRWCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contRWCommStr.setStatus("mandatory")
_ContSUCommStr_Type = OctetString
_ContSUCommStr_Object = MibScalar
contSUCommStr = _ContSUCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 5, 3),
    _ContSUCommStr_Type()
)
contSUCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contSUCommStr.setStatus("mandatory")
_ContAddress_ObjectIdentity = ObjectIdentity
contAddress = _ContAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 6)
)
_ContNetAddressTable_Object = MibTable
contNetAddressTable = _ContNetAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 6, 1)
)
if mibBuilder.loadTexts:
    contNetAddressTable.setStatus("mandatory")
_ContNetAddressEntry_Object = MibTableRow
contNetAddressEntry = _ContNetAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 6, 1, 1)
)
contNetAddressEntry.setIndexNames(
    (0, "CT-CONTAINER-MIB", "contNetAddressIndex"),
)
if mibBuilder.loadTexts:
    contNetAddressEntry.setStatus("mandatory")
_ContNetAddressIndex_Type = Integer32
_ContNetAddressIndex_Object = MibTableColumn
contNetAddressIndex = _ContNetAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 6, 1, 1, 1),
    _ContNetAddressIndex_Type()
)
contNetAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contNetAddressIndex.setStatus("mandatory")
_ContNetAddressNetworkType_Type = ObjectIdentifier
_ContNetAddressNetworkType_Object = MibTableColumn
contNetAddressNetworkType = _ContNetAddressNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 6, 1, 1, 2),
    _ContNetAddressNetworkType_Type()
)
contNetAddressNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contNetAddressNetworkType.setStatus("mandatory")
_ContNetAddress_Type = IpAddress
_ContNetAddress_Object = MibTableColumn
contNetAddress = _ContNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 6, 1, 1, 3),
    _ContNetAddress_Type()
)
contNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contNetAddress.setStatus("mandatory")
_ContNetAddressMask_Type = IpAddress
_ContNetAddressMask_Object = MibTableColumn
contNetAddressMask = _ContNetAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 6, 1, 1, 4),
    _ContNetAddressMask_Type()
)
contNetAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contNetAddressMask.setStatus("mandatory")
_ContTypeID_ObjectIdentity = ObjectIdentity
contTypeID = _ContTypeID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 7)
)
_ContUnknownTypeID_ObjectIdentity = ObjectIdentity
contUnknownTypeID = _ContUnknownTypeID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9, 7, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-CONTAINER-MIB",
    **{"contType": contType,
       "contTypeDevice": contTypeDevice,
       "contTypePhysicalEntries": contTypePhysicalEntries,
       "contTypePhysicalChanges": contTypePhysicalChanges,
       "contTypeLogicalChanges": contTypeLogicalChanges,
       "contTypeSerialNumber": contTypeSerialNumber,
       "contTypeContainingDevice": contTypeContainingDevice,
       "contTypeContainingPhysicalEntries": contTypeContainingPhysicalEntries,
       "contTypeContainingPhysicalEntryID": contTypeContainingPhysicalEntryID,
       "contTypeContainingSerialNumber": contTypeContainingSerialNumber,
       "contLogical": contLogical,
       "contLogicalEntryTable": contLogicalEntryTable,
       "contLogicalEntry": contLogicalEntry,
       "contLogicalEntryID": contLogicalEntryID,
       "contLogicalEntryType": contLogicalEntryType,
       "contLogicalEntryName": contLogicalEntryName,
       "contLogicalEntryVersion": contLogicalEntryVersion,
       "contLogicalEntryROCommStr": contLogicalEntryROCommStr,
       "contLogicalEntryRWCommStr": contLogicalEntryRWCommStr,
       "contLogicalEntrySUCommStr": contLogicalEntrySUCommStr,
       "contLogicalEntryAdminStatus": contLogicalEntryAdminStatus,
       "contLogicalEntryOperStatus": contLogicalEntryOperStatus,
       "contPhysical": contPhysical,
       "contPhysicalEntryTable": contPhysicalEntryTable,
       "contPhysicalEntry": contPhysicalEntry,
       "contPhysicalEntryID": contPhysicalEntryID,
       "contPhysicalEntries": contPhysicalEntries,
       "contPhysicalEntryClass": contPhysicalEntryClass,
       "contPhysicalEntryType": contPhysicalEntryType,
       "contPhysicalEntryTimeStamp": contPhysicalEntryTimeStamp,
       "contPhysicalEntryStatus": contPhysicalEntryStatus,
       "contLogicalToPhysicalMapTable": contLogicalToPhysicalMapTable,
       "contLogicalToPhysicalMapEntry": contLogicalToPhysicalMapEntry,
       "contPhysicalEntryMapID": contPhysicalEntryMapID,
       "contLogicalEntryMapID": contLogicalEntryMapID,
       "contResource": contResource,
       "contResourceTable": contResourceTable,
       "contResourceEntry": contResourceEntry,
       "contResourceID": contResourceID,
       "contResourceType": contResourceType,
       "contResourceMibPointer": contResourceMibPointer,
       "contCommStr": contCommStr,
       "contROCommStr": contROCommStr,
       "contRWCommStr": contRWCommStr,
       "contSUCommStr": contSUCommStr,
       "contAddress": contAddress,
       "contNetAddressTable": contNetAddressTable,
       "contNetAddressEntry": contNetAddressEntry,
       "contNetAddressIndex": contNetAddressIndex,
       "contNetAddressNetworkType": contNetAddressNetworkType,
       "contNetAddress": contNetAddress,
       "contNetAddressMask": contNetAddressMask,
       "contTypeID": contTypeID,
       "contUnknownTypeID": contUnknownTypeID}
)
