# SNMP MIB module (Nortel-Magellan-Passport-DataCollectionMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DataCollectionMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:32 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_Col_ObjectIdentity = ObjectIdentity
col = _Col_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21)
)
_ColRowStatusTable_Object = MibTable
colRowStatusTable = _ColRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 1)
)
if mibBuilder.loadTexts:
    colRowStatusTable.setStatus("mandatory")
_ColRowStatusEntry_Object = MibTableRow
colRowStatusEntry = _ColRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 1, 1)
)
colRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
)
if mibBuilder.loadTexts:
    colRowStatusEntry.setStatus("mandatory")
_ColRowStatus_Type = RowStatus
_ColRowStatus_Object = MibTableColumn
colRowStatus = _ColRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 1, 1, 1),
    _ColRowStatus_Type()
)
colRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colRowStatus.setStatus("mandatory")
_ColComponentName_Type = DisplayString
_ColComponentName_Object = MibTableColumn
colComponentName = _ColComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 1, 1, 2),
    _ColComponentName_Type()
)
colComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colComponentName.setStatus("mandatory")
_ColStorageType_Type = StorageType
_ColStorageType_Object = MibTableColumn
colStorageType = _ColStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 1, 1, 4),
    _ColStorageType_Type()
)
colStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colStorageType.setStatus("mandatory")


class _ColIndex_Type(Integer32):
    """Custom type colIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 0),
          ("alarm", 1),
          ("debug", 3),
          ("log", 2),
          ("scn", 4),
          ("stats", 6),
          ("trap", 5))
    )


_ColIndex_Type.__name__ = "Integer32"
_ColIndex_Object = MibTableColumn
colIndex = _ColIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 1, 1, 10),
    _ColIndex_Type()
)
colIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    colIndex.setStatus("mandatory")
_ColSp_ObjectIdentity = ObjectIdentity
colSp = _ColSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2)
)
_ColSpRowStatusTable_Object = MibTable
colSpRowStatusTable = _ColSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 1)
)
if mibBuilder.loadTexts:
    colSpRowStatusTable.setStatus("mandatory")
_ColSpRowStatusEntry_Object = MibTableRow
colSpRowStatusEntry = _ColSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 1, 1)
)
colSpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colSpIndex"),
)
if mibBuilder.loadTexts:
    colSpRowStatusEntry.setStatus("mandatory")
_ColSpRowStatus_Type = RowStatus
_ColSpRowStatus_Object = MibTableColumn
colSpRowStatus = _ColSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 1, 1, 1),
    _ColSpRowStatus_Type()
)
colSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpRowStatus.setStatus("mandatory")
_ColSpComponentName_Type = DisplayString
_ColSpComponentName_Object = MibTableColumn
colSpComponentName = _ColSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 1, 1, 2),
    _ColSpComponentName_Type()
)
colSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpComponentName.setStatus("mandatory")
_ColSpStorageType_Type = StorageType
_ColSpStorageType_Object = MibTableColumn
colSpStorageType = _ColSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 1, 1, 4),
    _ColSpStorageType_Type()
)
colSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpStorageType.setStatus("mandatory")
_ColSpIndex_Type = NonReplicated
_ColSpIndex_Object = MibTableColumn
colSpIndex = _ColSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 1, 1, 10),
    _ColSpIndex_Type()
)
colSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    colSpIndex.setStatus("mandatory")
_ColSpProvTable_Object = MibTable
colSpProvTable = _ColSpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 10)
)
if mibBuilder.loadTexts:
    colSpProvTable.setStatus("mandatory")
_ColSpProvEntry_Object = MibTableRow
colSpProvEntry = _ColSpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 10, 1)
)
colSpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colSpIndex"),
)
if mibBuilder.loadTexts:
    colSpProvEntry.setStatus("mandatory")


class _ColSpSpooling_Type(Integer32):
    """Custom type colSpSpooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ColSpSpooling_Type.__name__ = "Integer32"
_ColSpSpooling_Object = MibTableColumn
colSpSpooling = _ColSpSpooling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 10, 1, 1),
    _ColSpSpooling_Type()
)
colSpSpooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colSpSpooling.setStatus("mandatory")


class _ColSpMaximumNumberOfFiles_Type(Unsigned32):
    """Custom type colSpMaximumNumberOfFiles based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ColSpMaximumNumberOfFiles_Type.__name__ = "Unsigned32"
_ColSpMaximumNumberOfFiles_Object = MibTableColumn
colSpMaximumNumberOfFiles = _ColSpMaximumNumberOfFiles_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 10, 1, 2),
    _ColSpMaximumNumberOfFiles_Type()
)
colSpMaximumNumberOfFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colSpMaximumNumberOfFiles.setStatus("mandatory")
_ColSpStateTable_Object = MibTable
colSpStateTable = _ColSpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11)
)
if mibBuilder.loadTexts:
    colSpStateTable.setStatus("mandatory")
_ColSpStateEntry_Object = MibTableRow
colSpStateEntry = _ColSpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1)
)
colSpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colSpIndex"),
)
if mibBuilder.loadTexts:
    colSpStateEntry.setStatus("mandatory")


class _ColSpAdminState_Type(Integer32):
    """Custom type colSpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_ColSpAdminState_Type.__name__ = "Integer32"
_ColSpAdminState_Object = MibTableColumn
colSpAdminState = _ColSpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 1),
    _ColSpAdminState_Type()
)
colSpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpAdminState.setStatus("mandatory")


class _ColSpOperationalState_Type(Integer32):
    """Custom type colSpOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ColSpOperationalState_Type.__name__ = "Integer32"
_ColSpOperationalState_Object = MibTableColumn
colSpOperationalState = _ColSpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 2),
    _ColSpOperationalState_Type()
)
colSpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpOperationalState.setStatus("mandatory")


class _ColSpUsageState_Type(Integer32):
    """Custom type colSpUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_ColSpUsageState_Type.__name__ = "Integer32"
_ColSpUsageState_Object = MibTableColumn
colSpUsageState = _ColSpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 3),
    _ColSpUsageState_Type()
)
colSpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpUsageState.setStatus("mandatory")


class _ColSpAvailabilityStatus_Type(OctetString):
    """Custom type colSpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ColSpAvailabilityStatus_Type.__name__ = "OctetString"
_ColSpAvailabilityStatus_Object = MibTableColumn
colSpAvailabilityStatus = _ColSpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 4),
    _ColSpAvailabilityStatus_Type()
)
colSpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpAvailabilityStatus.setStatus("mandatory")


class _ColSpProceduralStatus_Type(OctetString):
    """Custom type colSpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ColSpProceduralStatus_Type.__name__ = "OctetString"
_ColSpProceduralStatus_Object = MibTableColumn
colSpProceduralStatus = _ColSpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 5),
    _ColSpProceduralStatus_Type()
)
colSpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpProceduralStatus.setStatus("mandatory")


class _ColSpControlStatus_Type(OctetString):
    """Custom type colSpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ColSpControlStatus_Type.__name__ = "OctetString"
_ColSpControlStatus_Object = MibTableColumn
colSpControlStatus = _ColSpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 6),
    _ColSpControlStatus_Type()
)
colSpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpControlStatus.setStatus("mandatory")


class _ColSpAlarmStatus_Type(OctetString):
    """Custom type colSpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ColSpAlarmStatus_Type.__name__ = "OctetString"
_ColSpAlarmStatus_Object = MibTableColumn
colSpAlarmStatus = _ColSpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 7),
    _ColSpAlarmStatus_Type()
)
colSpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpAlarmStatus.setStatus("mandatory")


class _ColSpStandbyStatus_Type(Integer32):
    """Custom type colSpStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_ColSpStandbyStatus_Type.__name__ = "Integer32"
_ColSpStandbyStatus_Object = MibTableColumn
colSpStandbyStatus = _ColSpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 8),
    _ColSpStandbyStatus_Type()
)
colSpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpStandbyStatus.setStatus("mandatory")


class _ColSpUnknownStatus_Type(Integer32):
    """Custom type colSpUnknownStatus based on Integer32"""
    defaultValue = 0

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


_ColSpUnknownStatus_Type.__name__ = "Integer32"
_ColSpUnknownStatus_Object = MibTableColumn
colSpUnknownStatus = _ColSpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 11, 1, 9),
    _ColSpUnknownStatus_Type()
)
colSpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpUnknownStatus.setStatus("mandatory")
_ColSpOperTable_Object = MibTable
colSpOperTable = _ColSpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 12)
)
if mibBuilder.loadTexts:
    colSpOperTable.setStatus("mandatory")
_ColSpOperEntry_Object = MibTableRow
colSpOperEntry = _ColSpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 12, 1)
)
colSpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colSpIndex"),
)
if mibBuilder.loadTexts:
    colSpOperEntry.setStatus("mandatory")


class _ColSpSpoolingFileName_Type(AsciiString):
    """Custom type colSpSpoolingFileName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ColSpSpoolingFileName_Type.__name__ = "AsciiString"
_ColSpSpoolingFileName_Object = MibTableColumn
colSpSpoolingFileName = _ColSpSpoolingFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 12, 1, 1),
    _ColSpSpoolingFileName_Type()
)
colSpSpoolingFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpSpoolingFileName.setStatus("mandatory")
_ColSpStatsTable_Object = MibTable
colSpStatsTable = _ColSpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 13)
)
if mibBuilder.loadTexts:
    colSpStatsTable.setStatus("mandatory")
_ColSpStatsEntry_Object = MibTableRow
colSpStatsEntry = _ColSpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 13, 1)
)
colSpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colSpIndex"),
)
if mibBuilder.loadTexts:
    colSpStatsEntry.setStatus("mandatory")


class _ColSpCurrentQueueSize_Type(Gauge32):
    """Custom type colSpCurrentQueueSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ColSpCurrentQueueSize_Type.__name__ = "Gauge32"
_ColSpCurrentQueueSize_Object = MibTableColumn
colSpCurrentQueueSize = _ColSpCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 13, 1, 1),
    _ColSpCurrentQueueSize_Type()
)
colSpCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpCurrentQueueSize.setStatus("mandatory")
_ColSpRecordsRx_Type = Counter32
_ColSpRecordsRx_Object = MibTableColumn
colSpRecordsRx = _ColSpRecordsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 13, 1, 2),
    _ColSpRecordsRx_Type()
)
colSpRecordsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpRecordsRx.setStatus("mandatory")
_ColSpRecordsDiscarded_Type = Counter32
_ColSpRecordsDiscarded_Object = MibTableColumn
colSpRecordsDiscarded = _ColSpRecordsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 2, 13, 1, 3),
    _ColSpRecordsDiscarded_Type()
)
colSpRecordsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colSpRecordsDiscarded.setStatus("mandatory")
_ColAg_ObjectIdentity = ObjectIdentity
colAg = _ColAg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3)
)
_ColAgRowStatusTable_Object = MibTable
colAgRowStatusTable = _ColAgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 1)
)
if mibBuilder.loadTexts:
    colAgRowStatusTable.setStatus("mandatory")
_ColAgRowStatusEntry_Object = MibTableRow
colAgRowStatusEntry = _ColAgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 1, 1)
)
colAgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colAgIndex"),
)
if mibBuilder.loadTexts:
    colAgRowStatusEntry.setStatus("mandatory")
_ColAgRowStatus_Type = RowStatus
_ColAgRowStatus_Object = MibTableColumn
colAgRowStatus = _ColAgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 1, 1, 1),
    _ColAgRowStatus_Type()
)
colAgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colAgRowStatus.setStatus("mandatory")
_ColAgComponentName_Type = DisplayString
_ColAgComponentName_Object = MibTableColumn
colAgComponentName = _ColAgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 1, 1, 2),
    _ColAgComponentName_Type()
)
colAgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colAgComponentName.setStatus("mandatory")
_ColAgStorageType_Type = StorageType
_ColAgStorageType_Object = MibTableColumn
colAgStorageType = _ColAgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 1, 1, 4),
    _ColAgStorageType_Type()
)
colAgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colAgStorageType.setStatus("mandatory")


class _ColAgIndex_Type(Integer32):
    """Custom type colAgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ColAgIndex_Type.__name__ = "Integer32"
_ColAgIndex_Object = MibTableColumn
colAgIndex = _ColAgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 1, 1, 10),
    _ColAgIndex_Type()
)
colAgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    colAgIndex.setStatus("mandatory")
_ColAgStatsTable_Object = MibTable
colAgStatsTable = _ColAgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 10)
)
if mibBuilder.loadTexts:
    colAgStatsTable.setStatus("mandatory")
_ColAgStatsEntry_Object = MibTableRow
colAgStatsEntry = _ColAgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 10, 1)
)
colAgStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colAgIndex"),
)
if mibBuilder.loadTexts:
    colAgStatsEntry.setStatus("mandatory")


class _ColAgCurrentQueueSize_Type(Gauge32):
    """Custom type colAgCurrentQueueSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ColAgCurrentQueueSize_Type.__name__ = "Gauge32"
_ColAgCurrentQueueSize_Object = MibTableColumn
colAgCurrentQueueSize = _ColAgCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 10, 1, 1),
    _ColAgCurrentQueueSize_Type()
)
colAgCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colAgCurrentQueueSize.setStatus("mandatory")
_ColAgRecordsRx_Type = Counter32
_ColAgRecordsRx_Object = MibTableColumn
colAgRecordsRx = _ColAgRecordsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 10, 1, 2),
    _ColAgRecordsRx_Type()
)
colAgRecordsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colAgRecordsRx.setStatus("mandatory")
_ColAgRecordsDiscarded_Type = Counter32
_ColAgRecordsDiscarded_Object = MibTableColumn
colAgRecordsDiscarded = _ColAgRecordsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 10, 1, 3),
    _ColAgRecordsDiscarded_Type()
)
colAgRecordsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colAgRecordsDiscarded.setStatus("mandatory")
_ColAgAgentStatsTable_Object = MibTable
colAgAgentStatsTable = _ColAgAgentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 11)
)
if mibBuilder.loadTexts:
    colAgAgentStatsTable.setStatus("mandatory")
_ColAgAgentStatsEntry_Object = MibTableRow
colAgAgentStatsEntry = _ColAgAgentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 11, 1)
)
colAgAgentStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colAgIndex"),
)
if mibBuilder.loadTexts:
    colAgAgentStatsEntry.setStatus("mandatory")
_ColAgRecordsNotGenerated_Type = Counter32
_ColAgRecordsNotGenerated_Object = MibTableColumn
colAgRecordsNotGenerated = _ColAgRecordsNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 3, 11, 1, 1),
    _ColAgRecordsNotGenerated_Type()
)
colAgRecordsNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colAgRecordsNotGenerated.setStatus("mandatory")
_ColProvTable_Object = MibTable
colProvTable = _ColProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 10)
)
if mibBuilder.loadTexts:
    colProvTable.setStatus("mandatory")
_ColProvEntry_Object = MibTableRow
colProvEntry = _ColProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 10, 1)
)
colProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
)
if mibBuilder.loadTexts:
    colProvEntry.setStatus("mandatory")


class _ColAgentQueueSize_Type(Unsigned32):
    """Custom type colAgentQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 10000),
    )


_ColAgentQueueSize_Type.__name__ = "Unsigned32"
_ColAgentQueueSize_Object = MibTableColumn
colAgentQueueSize = _ColAgentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 10, 1, 1),
    _ColAgentQueueSize_Type()
)
colAgentQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colAgentQueueSize.setStatus("obsolete")
_ColStatsTable_Object = MibTable
colStatsTable = _ColStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 11)
)
if mibBuilder.loadTexts:
    colStatsTable.setStatus("mandatory")
_ColStatsEntry_Object = MibTableRow
colStatsEntry = _ColStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 11, 1)
)
colStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
)
if mibBuilder.loadTexts:
    colStatsEntry.setStatus("mandatory")


class _ColCurrentQueueSize_Type(Gauge32):
    """Custom type colCurrentQueueSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ColCurrentQueueSize_Type.__name__ = "Gauge32"
_ColCurrentQueueSize_Object = MibTableColumn
colCurrentQueueSize = _ColCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 11, 1, 1),
    _ColCurrentQueueSize_Type()
)
colCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colCurrentQueueSize.setStatus("mandatory")
_ColRecordsRx_Type = Counter32
_ColRecordsRx_Object = MibTableColumn
colRecordsRx = _ColRecordsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 11, 1, 2),
    _ColRecordsRx_Type()
)
colRecordsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colRecordsRx.setStatus("mandatory")
_ColRecordsDiscarded_Type = Counter32
_ColRecordsDiscarded_Object = MibTableColumn
colRecordsDiscarded = _ColRecordsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 11, 1, 3),
    _ColRecordsDiscarded_Type()
)
colRecordsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colRecordsDiscarded.setStatus("mandatory")
_ColTimesTable_Object = MibTable
colTimesTable = _ColTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 266)
)
if mibBuilder.loadTexts:
    colTimesTable.setStatus("mandatory")
_ColTimesEntry_Object = MibTableRow
colTimesEntry = _ColTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 266, 1)
)
colTimesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colTimesValue"),
)
if mibBuilder.loadTexts:
    colTimesEntry.setStatus("mandatory")


class _ColTimesValue_Type(EnterpriseDateAndTime):
    """Custom type colTimesValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_ColTimesValue_Type.__name__ = "EnterpriseDateAndTime"
_ColTimesValue_Object = MibTableColumn
colTimesValue = _ColTimesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 266, 1, 1),
    _ColTimesValue_Type()
)
colTimesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colTimesValue.setStatus("mandatory")
_ColTimesRowStatus_Type = RowStatus
_ColTimesRowStatus_Object = MibTableColumn
colTimesRowStatus = _ColTimesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 266, 1, 2),
    _ColTimesRowStatus_Type()
)
colTimesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    colTimesRowStatus.setStatus("mandatory")
_ColLastTable_Object = MibTable
colLastTable = _ColLastTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 275)
)
if mibBuilder.loadTexts:
    colLastTable.setStatus("obsolete")
_ColLastEntry_Object = MibTableRow
colLastEntry = _ColLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 275, 1)
)
colLastEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colLastValue"),
)
if mibBuilder.loadTexts:
    colLastEntry.setStatus("obsolete")


class _ColLastValue_Type(EnterpriseDateAndTime):
    """Custom type colLastValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_ColLastValue_Type.__name__ = "EnterpriseDateAndTime"
_ColLastValue_Object = MibTableColumn
colLastValue = _ColLastValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 275, 1, 1),
    _ColLastValue_Type()
)
colLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colLastValue.setStatus("obsolete")
_ColPeakTable_Object = MibTable
colPeakTable = _ColPeakTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 279)
)
if mibBuilder.loadTexts:
    colPeakTable.setStatus("mandatory")
_ColPeakEntry_Object = MibTableRow
colPeakEntry = _ColPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 279, 1)
)
colPeakEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colIndex"),
    (0, "Nortel-Magellan-Passport-DataCollectionMIB", "colPeakValue"),
)
if mibBuilder.loadTexts:
    colPeakEntry.setStatus("mandatory")


class _ColPeakValue_Type(Integer32):
    """Custom type colPeakValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ColPeakValue_Type.__name__ = "Integer32"
_ColPeakValue_Object = MibTableColumn
colPeakValue = _ColPeakValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 279, 1, 1),
    _ColPeakValue_Type()
)
colPeakValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colPeakValue.setStatus("mandatory")
_ColPeakRowStatus_Type = RowStatus
_ColPeakRowStatus_Object = MibTableColumn
colPeakRowStatus = _ColPeakRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 21, 279, 1, 2),
    _ColPeakRowStatus_Type()
)
colPeakRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    colPeakRowStatus.setStatus("mandatory")
_DataCollectionMIB_ObjectIdentity = ObjectIdentity
dataCollectionMIB = _DataCollectionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14)
)
_DataCollectionGroup_ObjectIdentity = ObjectIdentity
dataCollectionGroup = _DataCollectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14, 1)
)
_DataCollectionGroupBE_ObjectIdentity = ObjectIdentity
dataCollectionGroupBE = _DataCollectionGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14, 1, 5)
)
_DataCollectionGroupBE00_ObjectIdentity = ObjectIdentity
dataCollectionGroupBE00 = _DataCollectionGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14, 1, 5, 1)
)
_DataCollectionGroupBE00A_ObjectIdentity = ObjectIdentity
dataCollectionGroupBE00A = _DataCollectionGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14, 1, 5, 1, 2)
)
_DataCollectionCapabilities_ObjectIdentity = ObjectIdentity
dataCollectionCapabilities = _DataCollectionCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14, 3)
)
_DataCollectionCapabilitiesBE_ObjectIdentity = ObjectIdentity
dataCollectionCapabilitiesBE = _DataCollectionCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14, 3, 5)
)
_DataCollectionCapabilitiesBE00_ObjectIdentity = ObjectIdentity
dataCollectionCapabilitiesBE00 = _DataCollectionCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14, 3, 5, 1)
)
_DataCollectionCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
dataCollectionCapabilitiesBE00A = _DataCollectionCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 14, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DataCollectionMIB",
    **{"col": col,
       "colRowStatusTable": colRowStatusTable,
       "colRowStatusEntry": colRowStatusEntry,
       "colRowStatus": colRowStatus,
       "colComponentName": colComponentName,
       "colStorageType": colStorageType,
       "colIndex": colIndex,
       "colSp": colSp,
       "colSpRowStatusTable": colSpRowStatusTable,
       "colSpRowStatusEntry": colSpRowStatusEntry,
       "colSpRowStatus": colSpRowStatus,
       "colSpComponentName": colSpComponentName,
       "colSpStorageType": colSpStorageType,
       "colSpIndex": colSpIndex,
       "colSpProvTable": colSpProvTable,
       "colSpProvEntry": colSpProvEntry,
       "colSpSpooling": colSpSpooling,
       "colSpMaximumNumberOfFiles": colSpMaximumNumberOfFiles,
       "colSpStateTable": colSpStateTable,
       "colSpStateEntry": colSpStateEntry,
       "colSpAdminState": colSpAdminState,
       "colSpOperationalState": colSpOperationalState,
       "colSpUsageState": colSpUsageState,
       "colSpAvailabilityStatus": colSpAvailabilityStatus,
       "colSpProceduralStatus": colSpProceduralStatus,
       "colSpControlStatus": colSpControlStatus,
       "colSpAlarmStatus": colSpAlarmStatus,
       "colSpStandbyStatus": colSpStandbyStatus,
       "colSpUnknownStatus": colSpUnknownStatus,
       "colSpOperTable": colSpOperTable,
       "colSpOperEntry": colSpOperEntry,
       "colSpSpoolingFileName": colSpSpoolingFileName,
       "colSpStatsTable": colSpStatsTable,
       "colSpStatsEntry": colSpStatsEntry,
       "colSpCurrentQueueSize": colSpCurrentQueueSize,
       "colSpRecordsRx": colSpRecordsRx,
       "colSpRecordsDiscarded": colSpRecordsDiscarded,
       "colAg": colAg,
       "colAgRowStatusTable": colAgRowStatusTable,
       "colAgRowStatusEntry": colAgRowStatusEntry,
       "colAgRowStatus": colAgRowStatus,
       "colAgComponentName": colAgComponentName,
       "colAgStorageType": colAgStorageType,
       "colAgIndex": colAgIndex,
       "colAgStatsTable": colAgStatsTable,
       "colAgStatsEntry": colAgStatsEntry,
       "colAgCurrentQueueSize": colAgCurrentQueueSize,
       "colAgRecordsRx": colAgRecordsRx,
       "colAgRecordsDiscarded": colAgRecordsDiscarded,
       "colAgAgentStatsTable": colAgAgentStatsTable,
       "colAgAgentStatsEntry": colAgAgentStatsEntry,
       "colAgRecordsNotGenerated": colAgRecordsNotGenerated,
       "colProvTable": colProvTable,
       "colProvEntry": colProvEntry,
       "colAgentQueueSize": colAgentQueueSize,
       "colStatsTable": colStatsTable,
       "colStatsEntry": colStatsEntry,
       "colCurrentQueueSize": colCurrentQueueSize,
       "colRecordsRx": colRecordsRx,
       "colRecordsDiscarded": colRecordsDiscarded,
       "colTimesTable": colTimesTable,
       "colTimesEntry": colTimesEntry,
       "colTimesValue": colTimesValue,
       "colTimesRowStatus": colTimesRowStatus,
       "colLastTable": colLastTable,
       "colLastEntry": colLastEntry,
       "colLastValue": colLastValue,
       "colPeakTable": colPeakTable,
       "colPeakEntry": colPeakEntry,
       "colPeakValue": colPeakValue,
       "colPeakRowStatus": colPeakRowStatus,
       "dataCollectionMIB": dataCollectionMIB,
       "dataCollectionGroup": dataCollectionGroup,
       "dataCollectionGroupBE": dataCollectionGroupBE,
       "dataCollectionGroupBE00": dataCollectionGroupBE00,
       "dataCollectionGroupBE00A": dataCollectionGroupBE00A,
       "dataCollectionCapabilities": dataCollectionCapabilities,
       "dataCollectionCapabilitiesBE": dataCollectionCapabilitiesBE,
       "dataCollectionCapabilitiesBE00": dataCollectionCapabilitiesBE00,
       "dataCollectionCapabilitiesBE00A": dataCollectionCapabilitiesBE00A}
)
