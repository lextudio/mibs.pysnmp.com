# SNMP MIB module (TIME-AGGREGATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIME-AGGREGATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:47 2024
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

tAggrMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 124)
)
tAggrMIB.setRevisions(
        ("2006-04-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TAggrMOErrorStatus(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class TimeAggrMOValue(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class CompressedTimeAggrMOValue(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_TAggrCtlTable_Object = MibTable
tAggrCtlTable = _TAggrCtlTable_Object(
    (1, 3, 6, 1, 3, 124, 1)
)
if mibBuilder.loadTexts:
    tAggrCtlTable.setStatus("current")
_TAggrCtlEntry_Object = MibTableRow
tAggrCtlEntry = _TAggrCtlEntry_Object(
    (1, 3, 6, 1, 3, 124, 1, 1)
)
tAggrCtlEntry.setIndexNames(
    (0, "TIME-AGGREGATE-MIB", "tAggrCtlEntryID"),
)
if mibBuilder.loadTexts:
    tAggrCtlEntry.setStatus("current")


class _TAggrCtlEntryID_Type(SnmpAdminString):
    """Custom type tAggrCtlEntryID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TAggrCtlEntryID_Type.__name__ = "SnmpAdminString"
_TAggrCtlEntryID_Object = MibTableColumn
tAggrCtlEntryID = _TAggrCtlEntryID_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 1),
    _TAggrCtlEntryID_Type()
)
tAggrCtlEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAggrCtlEntryID.setStatus("current")
_TAggrCtlMOInstance_Type = ObjectIdentifier
_TAggrCtlMOInstance_Object = MibTableColumn
tAggrCtlMOInstance = _TAggrCtlMOInstance_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 2),
    _TAggrCtlMOInstance_Type()
)
tAggrCtlMOInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAggrCtlMOInstance.setStatus("current")


class _TAggrCtlAgMODescr_Type(SnmpAdminString):
    """Custom type tAggrCtlAgMODescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TAggrCtlAgMODescr_Type.__name__ = "SnmpAdminString"
_TAggrCtlAgMODescr_Object = MibTableColumn
tAggrCtlAgMODescr = _TAggrCtlAgMODescr_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 3),
    _TAggrCtlAgMODescr_Type()
)
tAggrCtlAgMODescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAggrCtlAgMODescr.setStatus("current")
_TAggrCtlInterval_Type = Integer32
_TAggrCtlInterval_Object = MibTableColumn
tAggrCtlInterval = _TAggrCtlInterval_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 4),
    _TAggrCtlInterval_Type()
)
tAggrCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAggrCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tAggrCtlInterval.setUnits("micro seconds")
_TAggrCtlSamples_Type = Integer32
_TAggrCtlSamples_Object = MibTableColumn
tAggrCtlSamples = _TAggrCtlSamples_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 5),
    _TAggrCtlSamples_Type()
)
tAggrCtlSamples.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAggrCtlSamples.setStatus("current")


class _TAggrCtlCompressionAlgorithm_Type(Integer32):
    """Custom type tAggrCtlCompressionAlgorithm based on Integer32"""
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


_TAggrCtlCompressionAlgorithm_Type.__name__ = "Integer32"
_TAggrCtlCompressionAlgorithm_Object = MibTableColumn
tAggrCtlCompressionAlgorithm = _TAggrCtlCompressionAlgorithm_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 6),
    _TAggrCtlCompressionAlgorithm_Type()
)
tAggrCtlCompressionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAggrCtlCompressionAlgorithm.setStatus("current")
_TAggrCtlEntryOwner_Type = OwnerString
_TAggrCtlEntryOwner_Object = MibTableColumn
tAggrCtlEntryOwner = _TAggrCtlEntryOwner_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 7),
    _TAggrCtlEntryOwner_Type()
)
tAggrCtlEntryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAggrCtlEntryOwner.setStatus("current")
_TAggrCtlEntryStorageType_Type = StorageType
_TAggrCtlEntryStorageType_Object = MibTableColumn
tAggrCtlEntryStorageType = _TAggrCtlEntryStorageType_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 8),
    _TAggrCtlEntryStorageType_Type()
)
tAggrCtlEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAggrCtlEntryStorageType.setStatus("current")
_TAggrCtlEntryStatus_Type = RowStatus
_TAggrCtlEntryStatus_Object = MibTableColumn
tAggrCtlEntryStatus = _TAggrCtlEntryStatus_Object(
    (1, 3, 6, 1, 3, 124, 1, 1, 9),
    _TAggrCtlEntryStatus_Type()
)
tAggrCtlEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAggrCtlEntryStatus.setStatus("current")
_TAggrDataTable_Object = MibTable
tAggrDataTable = _TAggrDataTable_Object(
    (1, 3, 6, 1, 3, 124, 2)
)
if mibBuilder.loadTexts:
    tAggrDataTable.setStatus("current")
_TAggrDataEntry_Object = MibTableRow
tAggrDataEntry = _TAggrDataEntry_Object(
    (1, 3, 6, 1, 3, 124, 2, 1)
)
tAggrDataEntry.setIndexNames(
    (0, "TIME-AGGREGATE-MIB", "tAggrCtlEntryID"),
)
if mibBuilder.loadTexts:
    tAggrDataEntry.setStatus("current")
_TAggrDataRecord_Type = TimeAggrMOValue
_TAggrDataRecord_Object = MibTableColumn
tAggrDataRecord = _TAggrDataRecord_Object(
    (1, 3, 6, 1, 3, 124, 2, 1, 1),
    _TAggrDataRecord_Type()
)
tAggrDataRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAggrDataRecord.setStatus("current")
_TAggrDataRecordCompressed_Type = CompressedTimeAggrMOValue
_TAggrDataRecordCompressed_Object = MibTableColumn
tAggrDataRecordCompressed = _TAggrDataRecordCompressed_Object(
    (1, 3, 6, 1, 3, 124, 2, 1, 2),
    _TAggrDataRecordCompressed_Type()
)
tAggrDataRecordCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAggrDataRecordCompressed.setStatus("current")
_TAggrDataErrorRecord_Type = TAggrMOErrorStatus
_TAggrDataErrorRecord_Object = MibTableColumn
tAggrDataErrorRecord = _TAggrDataErrorRecord_Object(
    (1, 3, 6, 1, 3, 124, 2, 1, 3),
    _TAggrDataErrorRecord_Type()
)
tAggrDataErrorRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAggrDataErrorRecord.setStatus("current")
_TAggrConformance_ObjectIdentity = ObjectIdentity
tAggrConformance = _TAggrConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 124, 3)
)
_TAggrGroups_ObjectIdentity = ObjectIdentity
tAggrGroups = _TAggrGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 124, 3, 1)
)
_TAggrCompliances_ObjectIdentity = ObjectIdentity
tAggrCompliances = _TAggrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 124, 3, 2)
)

# Managed Objects groups

tAggrMibBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 124, 3, 1, 1)
)
tAggrMibBasicGroup.setObjects(
      *(("TIME-AGGREGATE-MIB", "tAggrCtlMOInstance"),
        ("TIME-AGGREGATE-MIB", "tAggrCtlAgMODescr"),
        ("TIME-AGGREGATE-MIB", "tAggrCtlInterval"),
        ("TIME-AGGREGATE-MIB", "tAggrCtlSamples"),
        ("TIME-AGGREGATE-MIB", "tAggrCtlCompressionAlgorithm"),
        ("TIME-AGGREGATE-MIB", "tAggrCtlEntryOwner"),
        ("TIME-AGGREGATE-MIB", "tAggrCtlEntryStorageType"),
        ("TIME-AGGREGATE-MIB", "tAggrCtlEntryStatus"),
        ("TIME-AGGREGATE-MIB", "tAggrDataRecord"),
        ("TIME-AGGREGATE-MIB", "tAggrDataRecordCompressed"),
        ("TIME-AGGREGATE-MIB", "tAggrDataErrorRecord"))
)
if mibBuilder.loadTexts:
    tAggrMibBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tAggrMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 124, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tAggrMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIME-AGGREGATE-MIB",
    **{"TAggrMOErrorStatus": TAggrMOErrorStatus,
       "TimeAggrMOValue": TimeAggrMOValue,
       "CompressedTimeAggrMOValue": CompressedTimeAggrMOValue,
       "tAggrMIB": tAggrMIB,
       "tAggrCtlTable": tAggrCtlTable,
       "tAggrCtlEntry": tAggrCtlEntry,
       "tAggrCtlEntryID": tAggrCtlEntryID,
       "tAggrCtlMOInstance": tAggrCtlMOInstance,
       "tAggrCtlAgMODescr": tAggrCtlAgMODescr,
       "tAggrCtlInterval": tAggrCtlInterval,
       "tAggrCtlSamples": tAggrCtlSamples,
       "tAggrCtlCompressionAlgorithm": tAggrCtlCompressionAlgorithm,
       "tAggrCtlEntryOwner": tAggrCtlEntryOwner,
       "tAggrCtlEntryStorageType": tAggrCtlEntryStorageType,
       "tAggrCtlEntryStatus": tAggrCtlEntryStatus,
       "tAggrDataTable": tAggrDataTable,
       "tAggrDataEntry": tAggrDataEntry,
       "tAggrDataRecord": tAggrDataRecord,
       "tAggrDataRecordCompressed": tAggrDataRecordCompressed,
       "tAggrDataErrorRecord": tAggrDataErrorRecord,
       "tAggrConformance": tAggrConformance,
       "tAggrGroups": tAggrGroups,
       "tAggrMibBasicGroup": tAggrMibBasicGroup,
       "tAggrCompliances": tAggrCompliances,
       "tAggrMibCompliance": tAggrMibCompliance}
)
