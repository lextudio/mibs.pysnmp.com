# SNMP MIB module (AGGREGATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AGGREGATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:57 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

aggrMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 123)
)
aggrMIB.setRevisions(
        ("2006-04-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AggrMOErrorStatus(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class AggrMOValue(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class AggrMOCompressedValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_AggrCtlTable_Object = MibTable
aggrCtlTable = _AggrCtlTable_Object(
    (1, 3, 6, 1, 3, 123, 1)
)
if mibBuilder.loadTexts:
    aggrCtlTable.setStatus("current")
_AggrCtlEntry_Object = MibTableRow
aggrCtlEntry = _AggrCtlEntry_Object(
    (1, 3, 6, 1, 3, 123, 1, 1)
)
aggrCtlEntry.setIndexNames(
    (0, "AGGREGATE-MIB", "aggrCtlEntryID"),
)
if mibBuilder.loadTexts:
    aggrCtlEntry.setStatus("current")


class _AggrCtlEntryID_Type(SnmpAdminString):
    """Custom type aggrCtlEntryID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AggrCtlEntryID_Type.__name__ = "SnmpAdminString"
_AggrCtlEntryID_Object = MibTableColumn
aggrCtlEntryID = _AggrCtlEntryID_Object(
    (1, 3, 6, 1, 3, 123, 1, 1, 1),
    _AggrCtlEntryID_Type()
)
aggrCtlEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aggrCtlEntryID.setStatus("current")


class _AggrCtlMOIndex_Type(Unsigned32):
    """Custom type aggrCtlMOIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AggrCtlMOIndex_Type.__name__ = "Unsigned32"
_AggrCtlMOIndex_Object = MibTableColumn
aggrCtlMOIndex = _AggrCtlMOIndex_Object(
    (1, 3, 6, 1, 3, 123, 1, 1, 2),
    _AggrCtlMOIndex_Type()
)
aggrCtlMOIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrCtlMOIndex.setStatus("current")


class _AggrCtlMODescr_Type(SnmpAdminString):
    """Custom type aggrCtlMODescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AggrCtlMODescr_Type.__name__ = "SnmpAdminString"
_AggrCtlMODescr_Object = MibTableColumn
aggrCtlMODescr = _AggrCtlMODescr_Object(
    (1, 3, 6, 1, 3, 123, 1, 1, 3),
    _AggrCtlMODescr_Type()
)
aggrCtlMODescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrCtlMODescr.setStatus("current")


class _AggrCtlCompressionAlgorithm_Type(Integer32):
    """Custom type aggrCtlCompressionAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deflate", 2),
          ("none", 1))
    )


_AggrCtlCompressionAlgorithm_Type.__name__ = "Integer32"
_AggrCtlCompressionAlgorithm_Object = MibTableColumn
aggrCtlCompressionAlgorithm = _AggrCtlCompressionAlgorithm_Object(
    (1, 3, 6, 1, 3, 123, 1, 1, 4),
    _AggrCtlCompressionAlgorithm_Type()
)
aggrCtlCompressionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrCtlCompressionAlgorithm.setStatus("current")
_AggrCtlEntryOwner_Type = OwnerString
_AggrCtlEntryOwner_Object = MibTableColumn
aggrCtlEntryOwner = _AggrCtlEntryOwner_Object(
    (1, 3, 6, 1, 3, 123, 1, 1, 5),
    _AggrCtlEntryOwner_Type()
)
aggrCtlEntryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrCtlEntryOwner.setStatus("current")
_AggrCtlEntryStorageType_Type = StorageType
_AggrCtlEntryStorageType_Object = MibTableColumn
aggrCtlEntryStorageType = _AggrCtlEntryStorageType_Object(
    (1, 3, 6, 1, 3, 123, 1, 1, 6),
    _AggrCtlEntryStorageType_Type()
)
aggrCtlEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrCtlEntryStorageType.setStatus("current")
_AggrCtlEntryStatus_Type = RowStatus
_AggrCtlEntryStatus_Object = MibTableColumn
aggrCtlEntryStatus = _AggrCtlEntryStatus_Object(
    (1, 3, 6, 1, 3, 123, 1, 1, 7),
    _AggrCtlEntryStatus_Type()
)
aggrCtlEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrCtlEntryStatus.setStatus("current")
_AggrMOTable_Object = MibTable
aggrMOTable = _AggrMOTable_Object(
    (1, 3, 6, 1, 3, 123, 2)
)
if mibBuilder.loadTexts:
    aggrMOTable.setStatus("current")
_AggrMOEntry_Object = MibTableRow
aggrMOEntry = _AggrMOEntry_Object(
    (1, 3, 6, 1, 3, 123, 2, 1)
)
aggrMOEntry.setIndexNames(
    (0, "AGGREGATE-MIB", "aggrMOEntryID"),
    (0, "AGGREGATE-MIB", "aggrMOEntryMOID"),
)
if mibBuilder.loadTexts:
    aggrMOEntry.setStatus("current")


class _AggrMOEntryID_Type(Unsigned32):
    """Custom type aggrMOEntryID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AggrMOEntryID_Type.__name__ = "Unsigned32"
_AggrMOEntryID_Object = MibTableColumn
aggrMOEntryID = _AggrMOEntryID_Object(
    (1, 3, 6, 1, 3, 123, 2, 1, 1),
    _AggrMOEntryID_Type()
)
aggrMOEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aggrMOEntryID.setStatus("current")


class _AggrMOEntryMOID_Type(Unsigned32):
    """Custom type aggrMOEntryMOID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AggrMOEntryMOID_Type.__name__ = "Unsigned32"
_AggrMOEntryMOID_Object = MibTableColumn
aggrMOEntryMOID = _AggrMOEntryMOID_Object(
    (1, 3, 6, 1, 3, 123, 2, 1, 2),
    _AggrMOEntryMOID_Type()
)
aggrMOEntryMOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aggrMOEntryMOID.setStatus("current")
_AggrMOInstance_Type = ObjectIdentifier
_AggrMOInstance_Object = MibTableColumn
aggrMOInstance = _AggrMOInstance_Object(
    (1, 3, 6, 1, 3, 123, 2, 1, 3),
    _AggrMOInstance_Type()
)
aggrMOInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrMOInstance.setStatus("current")


class _AggrMODescr_Type(SnmpAdminString):
    """Custom type aggrMODescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AggrMODescr_Type.__name__ = "SnmpAdminString"
_AggrMODescr_Object = MibTableColumn
aggrMODescr = _AggrMODescr_Object(
    (1, 3, 6, 1, 3, 123, 2, 1, 4),
    _AggrMODescr_Type()
)
aggrMODescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrMODescr.setStatus("current")
_AggrMOEntryStorageType_Type = StorageType
_AggrMOEntryStorageType_Object = MibTableColumn
aggrMOEntryStorageType = _AggrMOEntryStorageType_Object(
    (1, 3, 6, 1, 3, 123, 2, 1, 5),
    _AggrMOEntryStorageType_Type()
)
aggrMOEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrMOEntryStorageType.setStatus("current")
_AggrMOEntryStatus_Type = RowStatus
_AggrMOEntryStatus_Object = MibTableColumn
aggrMOEntryStatus = _AggrMOEntryStatus_Object(
    (1, 3, 6, 1, 3, 123, 2, 1, 6),
    _AggrMOEntryStatus_Type()
)
aggrMOEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrMOEntryStatus.setStatus("current")
_AggrDataTable_Object = MibTable
aggrDataTable = _AggrDataTable_Object(
    (1, 3, 6, 1, 3, 123, 3)
)
if mibBuilder.loadTexts:
    aggrDataTable.setStatus("current")
_AggrDataEntry_Object = MibTableRow
aggrDataEntry = _AggrDataEntry_Object(
    (1, 3, 6, 1, 3, 123, 3, 1)
)
aggrDataEntry.setIndexNames(
    (0, "AGGREGATE-MIB", "aggrCtlEntryID"),
)
if mibBuilder.loadTexts:
    aggrDataEntry.setStatus("current")
_AggrDataRecord_Type = AggrMOValue
_AggrDataRecord_Object = MibTableColumn
aggrDataRecord = _AggrDataRecord_Object(
    (1, 3, 6, 1, 3, 123, 3, 1, 1),
    _AggrDataRecord_Type()
)
aggrDataRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrDataRecord.setStatus("current")
_AggrDataRecordCompressed_Type = AggrMOCompressedValue
_AggrDataRecordCompressed_Object = MibTableColumn
aggrDataRecordCompressed = _AggrDataRecordCompressed_Object(
    (1, 3, 6, 1, 3, 123, 3, 1, 2),
    _AggrDataRecordCompressed_Type()
)
aggrDataRecordCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrDataRecordCompressed.setStatus("current")
_AggrDataErrorRecord_Type = AggrMOErrorStatus
_AggrDataErrorRecord_Object = MibTableColumn
aggrDataErrorRecord = _AggrDataErrorRecord_Object(
    (1, 3, 6, 1, 3, 123, 3, 1, 3),
    _AggrDataErrorRecord_Type()
)
aggrDataErrorRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrDataErrorRecord.setStatus("current")
_AggrConformance_ObjectIdentity = ObjectIdentity
aggrConformance = _AggrConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 123, 4)
)
_AggrGroups_ObjectIdentity = ObjectIdentity
aggrGroups = _AggrGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 123, 4, 1)
)
_AggrCompliances_ObjectIdentity = ObjectIdentity
aggrCompliances = _AggrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 123, 4, 2)
)

# Managed Objects groups

aggrMibBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 123, 4, 1, 1)
)
aggrMibBasicGroup.setObjects(
      *(("AGGREGATE-MIB", "aggrCtlMOIndex"),
        ("AGGREGATE-MIB", "aggrCtlMODescr"),
        ("AGGREGATE-MIB", "aggrCtlCompressionAlgorithm"),
        ("AGGREGATE-MIB", "aggrCtlEntryOwner"),
        ("AGGREGATE-MIB", "aggrCtlEntryStorageType"),
        ("AGGREGATE-MIB", "aggrCtlEntryStatus"),
        ("AGGREGATE-MIB", "aggrMOInstance"),
        ("AGGREGATE-MIB", "aggrMODescr"),
        ("AGGREGATE-MIB", "aggrMOEntryStorageType"),
        ("AGGREGATE-MIB", "aggrMOEntryStatus"),
        ("AGGREGATE-MIB", "aggrDataRecord"),
        ("AGGREGATE-MIB", "aggrDataRecordCompressed"),
        ("AGGREGATE-MIB", "aggrDataErrorRecord"))
)
if mibBuilder.loadTexts:
    aggrMibBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aggrMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 123, 4, 2, 1)
)
if mibBuilder.loadTexts:
    aggrMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGGREGATE-MIB",
    **{"AggrMOErrorStatus": AggrMOErrorStatus,
       "AggrMOValue": AggrMOValue,
       "AggrMOCompressedValue": AggrMOCompressedValue,
       "aggrMIB": aggrMIB,
       "aggrCtlTable": aggrCtlTable,
       "aggrCtlEntry": aggrCtlEntry,
       "aggrCtlEntryID": aggrCtlEntryID,
       "aggrCtlMOIndex": aggrCtlMOIndex,
       "aggrCtlMODescr": aggrCtlMODescr,
       "aggrCtlCompressionAlgorithm": aggrCtlCompressionAlgorithm,
       "aggrCtlEntryOwner": aggrCtlEntryOwner,
       "aggrCtlEntryStorageType": aggrCtlEntryStorageType,
       "aggrCtlEntryStatus": aggrCtlEntryStatus,
       "aggrMOTable": aggrMOTable,
       "aggrMOEntry": aggrMOEntry,
       "aggrMOEntryID": aggrMOEntryID,
       "aggrMOEntryMOID": aggrMOEntryMOID,
       "aggrMOInstance": aggrMOInstance,
       "aggrMODescr": aggrMODescr,
       "aggrMOEntryStorageType": aggrMOEntryStorageType,
       "aggrMOEntryStatus": aggrMOEntryStatus,
       "aggrDataTable": aggrDataTable,
       "aggrDataEntry": aggrDataEntry,
       "aggrDataRecord": aggrDataRecord,
       "aggrDataRecordCompressed": aggrDataRecordCompressed,
       "aggrDataErrorRecord": aggrDataErrorRecord,
       "aggrConformance": aggrConformance,
       "aggrGroups": aggrGroups,
       "aggrMibBasicGroup": aggrMibBasicGroup,
       "aggrCompliances": aggrCompliances,
       "aggrMibCompliance": aggrMibCompliance}
)
