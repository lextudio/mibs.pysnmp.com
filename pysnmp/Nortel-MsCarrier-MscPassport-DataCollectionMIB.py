# SNMP MIB module (Nortel-MsCarrier-MscPassport-DataCollectionMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DataCollectionMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:08 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscCol_ObjectIdentity = ObjectIdentity
mscCol = _MscCol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21)
)
_MscColRowStatusTable_Object = MibTable
mscColRowStatusTable = _MscColRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    mscColRowStatusTable.setStatus("mandatory")
_MscColRowStatusEntry_Object = MibTableRow
mscColRowStatusEntry = _MscColRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1)
)
mscColRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
)
if mibBuilder.loadTexts:
    mscColRowStatusEntry.setStatus("mandatory")
_MscColRowStatus_Type = RowStatus
_MscColRowStatus_Object = MibTableColumn
mscColRowStatus = _MscColRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1, 1),
    _MscColRowStatus_Type()
)
mscColRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscColRowStatus.setStatus("mandatory")
_MscColComponentName_Type = DisplayString
_MscColComponentName_Object = MibTableColumn
mscColComponentName = _MscColComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1, 2),
    _MscColComponentName_Type()
)
mscColComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColComponentName.setStatus("mandatory")
_MscColStorageType_Type = StorageType
_MscColStorageType_Object = MibTableColumn
mscColStorageType = _MscColStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1, 4),
    _MscColStorageType_Type()
)
mscColStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColStorageType.setStatus("mandatory")


class _MscColIndex_Type(Integer32):
    """Custom type mscColIndex based on Integer32"""
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


_MscColIndex_Type.__name__ = "Integer32"
_MscColIndex_Object = MibTableColumn
mscColIndex = _MscColIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1, 10),
    _MscColIndex_Type()
)
mscColIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscColIndex.setStatus("mandatory")
_MscColSp_ObjectIdentity = ObjectIdentity
mscColSp = _MscColSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2)
)
_MscColSpRowStatusTable_Object = MibTable
mscColSpRowStatusTable = _MscColSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1)
)
if mibBuilder.loadTexts:
    mscColSpRowStatusTable.setStatus("mandatory")
_MscColSpRowStatusEntry_Object = MibTableRow
mscColSpRowStatusEntry = _MscColSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1)
)
mscColSpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"),
)
if mibBuilder.loadTexts:
    mscColSpRowStatusEntry.setStatus("mandatory")
_MscColSpRowStatus_Type = RowStatus
_MscColSpRowStatus_Object = MibTableColumn
mscColSpRowStatus = _MscColSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1, 1),
    _MscColSpRowStatus_Type()
)
mscColSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpRowStatus.setStatus("mandatory")
_MscColSpComponentName_Type = DisplayString
_MscColSpComponentName_Object = MibTableColumn
mscColSpComponentName = _MscColSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1, 2),
    _MscColSpComponentName_Type()
)
mscColSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpComponentName.setStatus("mandatory")
_MscColSpStorageType_Type = StorageType
_MscColSpStorageType_Object = MibTableColumn
mscColSpStorageType = _MscColSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1, 4),
    _MscColSpStorageType_Type()
)
mscColSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpStorageType.setStatus("mandatory")
_MscColSpIndex_Type = NonReplicated
_MscColSpIndex_Object = MibTableColumn
mscColSpIndex = _MscColSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1, 10),
    _MscColSpIndex_Type()
)
mscColSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscColSpIndex.setStatus("mandatory")
_MscColSpProvTable_Object = MibTable
mscColSpProvTable = _MscColSpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 10)
)
if mibBuilder.loadTexts:
    mscColSpProvTable.setStatus("mandatory")
_MscColSpProvEntry_Object = MibTableRow
mscColSpProvEntry = _MscColSpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 10, 1)
)
mscColSpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"),
)
if mibBuilder.loadTexts:
    mscColSpProvEntry.setStatus("mandatory")


class _MscColSpSpooling_Type(Integer32):
    """Custom type mscColSpSpooling based on Integer32"""
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


_MscColSpSpooling_Type.__name__ = "Integer32"
_MscColSpSpooling_Object = MibTableColumn
mscColSpSpooling = _MscColSpSpooling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 10, 1, 1),
    _MscColSpSpooling_Type()
)
mscColSpSpooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscColSpSpooling.setStatus("mandatory")


class _MscColSpMaximumNumberOfFiles_Type(Unsigned32):
    """Custom type mscColSpMaximumNumberOfFiles based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MscColSpMaximumNumberOfFiles_Type.__name__ = "Unsigned32"
_MscColSpMaximumNumberOfFiles_Object = MibTableColumn
mscColSpMaximumNumberOfFiles = _MscColSpMaximumNumberOfFiles_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 10, 1, 2),
    _MscColSpMaximumNumberOfFiles_Type()
)
mscColSpMaximumNumberOfFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscColSpMaximumNumberOfFiles.setStatus("mandatory")
_MscColSpStateTable_Object = MibTable
mscColSpStateTable = _MscColSpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11)
)
if mibBuilder.loadTexts:
    mscColSpStateTable.setStatus("mandatory")
_MscColSpStateEntry_Object = MibTableRow
mscColSpStateEntry = _MscColSpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1)
)
mscColSpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"),
)
if mibBuilder.loadTexts:
    mscColSpStateEntry.setStatus("mandatory")


class _MscColSpAdminState_Type(Integer32):
    """Custom type mscColSpAdminState based on Integer32"""
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


_MscColSpAdminState_Type.__name__ = "Integer32"
_MscColSpAdminState_Object = MibTableColumn
mscColSpAdminState = _MscColSpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 1),
    _MscColSpAdminState_Type()
)
mscColSpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpAdminState.setStatus("mandatory")


class _MscColSpOperationalState_Type(Integer32):
    """Custom type mscColSpOperationalState based on Integer32"""
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


_MscColSpOperationalState_Type.__name__ = "Integer32"
_MscColSpOperationalState_Object = MibTableColumn
mscColSpOperationalState = _MscColSpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 2),
    _MscColSpOperationalState_Type()
)
mscColSpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpOperationalState.setStatus("mandatory")


class _MscColSpUsageState_Type(Integer32):
    """Custom type mscColSpUsageState based on Integer32"""
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


_MscColSpUsageState_Type.__name__ = "Integer32"
_MscColSpUsageState_Object = MibTableColumn
mscColSpUsageState = _MscColSpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 3),
    _MscColSpUsageState_Type()
)
mscColSpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpUsageState.setStatus("mandatory")


class _MscColSpAvailabilityStatus_Type(OctetString):
    """Custom type mscColSpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscColSpAvailabilityStatus_Type.__name__ = "OctetString"
_MscColSpAvailabilityStatus_Object = MibTableColumn
mscColSpAvailabilityStatus = _MscColSpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 4),
    _MscColSpAvailabilityStatus_Type()
)
mscColSpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpAvailabilityStatus.setStatus("mandatory")


class _MscColSpProceduralStatus_Type(OctetString):
    """Custom type mscColSpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscColSpProceduralStatus_Type.__name__ = "OctetString"
_MscColSpProceduralStatus_Object = MibTableColumn
mscColSpProceduralStatus = _MscColSpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 5),
    _MscColSpProceduralStatus_Type()
)
mscColSpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpProceduralStatus.setStatus("mandatory")


class _MscColSpControlStatus_Type(OctetString):
    """Custom type mscColSpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscColSpControlStatus_Type.__name__ = "OctetString"
_MscColSpControlStatus_Object = MibTableColumn
mscColSpControlStatus = _MscColSpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 6),
    _MscColSpControlStatus_Type()
)
mscColSpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpControlStatus.setStatus("mandatory")


class _MscColSpAlarmStatus_Type(OctetString):
    """Custom type mscColSpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscColSpAlarmStatus_Type.__name__ = "OctetString"
_MscColSpAlarmStatus_Object = MibTableColumn
mscColSpAlarmStatus = _MscColSpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 7),
    _MscColSpAlarmStatus_Type()
)
mscColSpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpAlarmStatus.setStatus("mandatory")


class _MscColSpStandbyStatus_Type(Integer32):
    """Custom type mscColSpStandbyStatus based on Integer32"""
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


_MscColSpStandbyStatus_Type.__name__ = "Integer32"
_MscColSpStandbyStatus_Object = MibTableColumn
mscColSpStandbyStatus = _MscColSpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 8),
    _MscColSpStandbyStatus_Type()
)
mscColSpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpStandbyStatus.setStatus("mandatory")


class _MscColSpUnknownStatus_Type(Integer32):
    """Custom type mscColSpUnknownStatus based on Integer32"""
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


_MscColSpUnknownStatus_Type.__name__ = "Integer32"
_MscColSpUnknownStatus_Object = MibTableColumn
mscColSpUnknownStatus = _MscColSpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 9),
    _MscColSpUnknownStatus_Type()
)
mscColSpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpUnknownStatus.setStatus("mandatory")
_MscColSpOperTable_Object = MibTable
mscColSpOperTable = _MscColSpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 12)
)
if mibBuilder.loadTexts:
    mscColSpOperTable.setStatus("mandatory")
_MscColSpOperEntry_Object = MibTableRow
mscColSpOperEntry = _MscColSpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 12, 1)
)
mscColSpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"),
)
if mibBuilder.loadTexts:
    mscColSpOperEntry.setStatus("mandatory")


class _MscColSpSpoolingFileName_Type(AsciiString):
    """Custom type mscColSpSpoolingFileName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscColSpSpoolingFileName_Type.__name__ = "AsciiString"
_MscColSpSpoolingFileName_Object = MibTableColumn
mscColSpSpoolingFileName = _MscColSpSpoolingFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 12, 1, 1),
    _MscColSpSpoolingFileName_Type()
)
mscColSpSpoolingFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpSpoolingFileName.setStatus("mandatory")
_MscColSpStatsTable_Object = MibTable
mscColSpStatsTable = _MscColSpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13)
)
if mibBuilder.loadTexts:
    mscColSpStatsTable.setStatus("mandatory")
_MscColSpStatsEntry_Object = MibTableRow
mscColSpStatsEntry = _MscColSpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13, 1)
)
mscColSpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"),
)
if mibBuilder.loadTexts:
    mscColSpStatsEntry.setStatus("mandatory")


class _MscColSpCurrentQueueSize_Type(Gauge32):
    """Custom type mscColSpCurrentQueueSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscColSpCurrentQueueSize_Type.__name__ = "Gauge32"
_MscColSpCurrentQueueSize_Object = MibTableColumn
mscColSpCurrentQueueSize = _MscColSpCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13, 1, 1),
    _MscColSpCurrentQueueSize_Type()
)
mscColSpCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpCurrentQueueSize.setStatus("mandatory")
_MscColSpRecordsRx_Type = Counter32
_MscColSpRecordsRx_Object = MibTableColumn
mscColSpRecordsRx = _MscColSpRecordsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13, 1, 2),
    _MscColSpRecordsRx_Type()
)
mscColSpRecordsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpRecordsRx.setStatus("mandatory")
_MscColSpRecordsDiscarded_Type = Counter32
_MscColSpRecordsDiscarded_Object = MibTableColumn
mscColSpRecordsDiscarded = _MscColSpRecordsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13, 1, 3),
    _MscColSpRecordsDiscarded_Type()
)
mscColSpRecordsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColSpRecordsDiscarded.setStatus("mandatory")
_MscColAg_ObjectIdentity = ObjectIdentity
mscColAg = _MscColAg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3)
)
_MscColAgRowStatusTable_Object = MibTable
mscColAgRowStatusTable = _MscColAgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1)
)
if mibBuilder.loadTexts:
    mscColAgRowStatusTable.setStatus("mandatory")
_MscColAgRowStatusEntry_Object = MibTableRow
mscColAgRowStatusEntry = _MscColAgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1)
)
mscColAgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColAgIndex"),
)
if mibBuilder.loadTexts:
    mscColAgRowStatusEntry.setStatus("mandatory")
_MscColAgRowStatus_Type = RowStatus
_MscColAgRowStatus_Object = MibTableColumn
mscColAgRowStatus = _MscColAgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1, 1),
    _MscColAgRowStatus_Type()
)
mscColAgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColAgRowStatus.setStatus("mandatory")
_MscColAgComponentName_Type = DisplayString
_MscColAgComponentName_Object = MibTableColumn
mscColAgComponentName = _MscColAgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1, 2),
    _MscColAgComponentName_Type()
)
mscColAgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColAgComponentName.setStatus("mandatory")
_MscColAgStorageType_Type = StorageType
_MscColAgStorageType_Object = MibTableColumn
mscColAgStorageType = _MscColAgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1, 4),
    _MscColAgStorageType_Type()
)
mscColAgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColAgStorageType.setStatus("mandatory")


class _MscColAgIndex_Type(Integer32):
    """Custom type mscColAgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscColAgIndex_Type.__name__ = "Integer32"
_MscColAgIndex_Object = MibTableColumn
mscColAgIndex = _MscColAgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1, 10),
    _MscColAgIndex_Type()
)
mscColAgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscColAgIndex.setStatus("mandatory")
_MscColAgStatsTable_Object = MibTable
mscColAgStatsTable = _MscColAgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10)
)
if mibBuilder.loadTexts:
    mscColAgStatsTable.setStatus("mandatory")
_MscColAgStatsEntry_Object = MibTableRow
mscColAgStatsEntry = _MscColAgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10, 1)
)
mscColAgStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColAgIndex"),
)
if mibBuilder.loadTexts:
    mscColAgStatsEntry.setStatus("mandatory")


class _MscColAgCurrentQueueSize_Type(Gauge32):
    """Custom type mscColAgCurrentQueueSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscColAgCurrentQueueSize_Type.__name__ = "Gauge32"
_MscColAgCurrentQueueSize_Object = MibTableColumn
mscColAgCurrentQueueSize = _MscColAgCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10, 1, 1),
    _MscColAgCurrentQueueSize_Type()
)
mscColAgCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColAgCurrentQueueSize.setStatus("mandatory")
_MscColAgRecordsRx_Type = Counter32
_MscColAgRecordsRx_Object = MibTableColumn
mscColAgRecordsRx = _MscColAgRecordsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10, 1, 2),
    _MscColAgRecordsRx_Type()
)
mscColAgRecordsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColAgRecordsRx.setStatus("mandatory")
_MscColAgRecordsDiscarded_Type = Counter32
_MscColAgRecordsDiscarded_Object = MibTableColumn
mscColAgRecordsDiscarded = _MscColAgRecordsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10, 1, 3),
    _MscColAgRecordsDiscarded_Type()
)
mscColAgRecordsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColAgRecordsDiscarded.setStatus("mandatory")
_MscColAgAgentStatsTable_Object = MibTable
mscColAgAgentStatsTable = _MscColAgAgentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 11)
)
if mibBuilder.loadTexts:
    mscColAgAgentStatsTable.setStatus("mandatory")
_MscColAgAgentStatsEntry_Object = MibTableRow
mscColAgAgentStatsEntry = _MscColAgAgentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 11, 1)
)
mscColAgAgentStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColAgIndex"),
)
if mibBuilder.loadTexts:
    mscColAgAgentStatsEntry.setStatus("mandatory")
_MscColAgRecordsNotGenerated_Type = Counter32
_MscColAgRecordsNotGenerated_Object = MibTableColumn
mscColAgRecordsNotGenerated = _MscColAgRecordsNotGenerated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 11, 1, 1),
    _MscColAgRecordsNotGenerated_Type()
)
mscColAgRecordsNotGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColAgRecordsNotGenerated.setStatus("mandatory")
_MscColProvTable_Object = MibTable
mscColProvTable = _MscColProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 10)
)
if mibBuilder.loadTexts:
    mscColProvTable.setStatus("mandatory")
_MscColProvEntry_Object = MibTableRow
mscColProvEntry = _MscColProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 10, 1)
)
mscColProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
)
if mibBuilder.loadTexts:
    mscColProvEntry.setStatus("mandatory")


class _MscColAgentQueueSize_Type(Unsigned32):
    """Custom type mscColAgentQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 10000),
    )


_MscColAgentQueueSize_Type.__name__ = "Unsigned32"
_MscColAgentQueueSize_Object = MibTableColumn
mscColAgentQueueSize = _MscColAgentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 10, 1, 1),
    _MscColAgentQueueSize_Type()
)
mscColAgentQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscColAgentQueueSize.setStatus("obsolete")
_MscColStatsTable_Object = MibTable
mscColStatsTable = _MscColStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11)
)
if mibBuilder.loadTexts:
    mscColStatsTable.setStatus("mandatory")
_MscColStatsEntry_Object = MibTableRow
mscColStatsEntry = _MscColStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11, 1)
)
mscColStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
)
if mibBuilder.loadTexts:
    mscColStatsEntry.setStatus("mandatory")


class _MscColCurrentQueueSize_Type(Gauge32):
    """Custom type mscColCurrentQueueSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscColCurrentQueueSize_Type.__name__ = "Gauge32"
_MscColCurrentQueueSize_Object = MibTableColumn
mscColCurrentQueueSize = _MscColCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11, 1, 1),
    _MscColCurrentQueueSize_Type()
)
mscColCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColCurrentQueueSize.setStatus("mandatory")
_MscColRecordsRx_Type = Counter32
_MscColRecordsRx_Object = MibTableColumn
mscColRecordsRx = _MscColRecordsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11, 1, 2),
    _MscColRecordsRx_Type()
)
mscColRecordsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColRecordsRx.setStatus("mandatory")
_MscColRecordsDiscarded_Type = Counter32
_MscColRecordsDiscarded_Object = MibTableColumn
mscColRecordsDiscarded = _MscColRecordsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11, 1, 3),
    _MscColRecordsDiscarded_Type()
)
mscColRecordsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColRecordsDiscarded.setStatus("mandatory")
_MscColTimesTable_Object = MibTable
mscColTimesTable = _MscColTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 266)
)
if mibBuilder.loadTexts:
    mscColTimesTable.setStatus("mandatory")
_MscColTimesEntry_Object = MibTableRow
mscColTimesEntry = _MscColTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 266, 1)
)
mscColTimesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColTimesValue"),
)
if mibBuilder.loadTexts:
    mscColTimesEntry.setStatus("mandatory")


class _MscColTimesValue_Type(EnterpriseDateAndTime):
    """Custom type mscColTimesValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_MscColTimesValue_Type.__name__ = "EnterpriseDateAndTime"
_MscColTimesValue_Object = MibTableColumn
mscColTimesValue = _MscColTimesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 266, 1, 1),
    _MscColTimesValue_Type()
)
mscColTimesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscColTimesValue.setStatus("mandatory")
_MscColTimesRowStatus_Type = RowStatus
_MscColTimesRowStatus_Object = MibTableColumn
mscColTimesRowStatus = _MscColTimesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 266, 1, 2),
    _MscColTimesRowStatus_Type()
)
mscColTimesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscColTimesRowStatus.setStatus("mandatory")
_MscColLastTable_Object = MibTable
mscColLastTable = _MscColLastTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 275)
)
if mibBuilder.loadTexts:
    mscColLastTable.setStatus("obsolete")
_MscColLastEntry_Object = MibTableRow
mscColLastEntry = _MscColLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 275, 1)
)
mscColLastEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColLastValue"),
)
if mibBuilder.loadTexts:
    mscColLastEntry.setStatus("obsolete")


class _MscColLastValue_Type(EnterpriseDateAndTime):
    """Custom type mscColLastValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_MscColLastValue_Type.__name__ = "EnterpriseDateAndTime"
_MscColLastValue_Object = MibTableColumn
mscColLastValue = _MscColLastValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 275, 1, 1),
    _MscColLastValue_Type()
)
mscColLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscColLastValue.setStatus("obsolete")
_MscColPeakTable_Object = MibTable
mscColPeakTable = _MscColPeakTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 279)
)
if mibBuilder.loadTexts:
    mscColPeakTable.setStatus("mandatory")
_MscColPeakEntry_Object = MibTableRow
mscColPeakEntry = _MscColPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 279, 1)
)
mscColPeakEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColPeakValue"),
)
if mibBuilder.loadTexts:
    mscColPeakEntry.setStatus("mandatory")


class _MscColPeakValue_Type(Integer32):
    """Custom type mscColPeakValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscColPeakValue_Type.__name__ = "Integer32"
_MscColPeakValue_Object = MibTableColumn
mscColPeakValue = _MscColPeakValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 279, 1, 1),
    _MscColPeakValue_Type()
)
mscColPeakValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscColPeakValue.setStatus("mandatory")
_MscColPeakRowStatus_Type = RowStatus
_MscColPeakRowStatus_Object = MibTableColumn
mscColPeakRowStatus = _MscColPeakRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 279, 1, 2),
    _MscColPeakRowStatus_Type()
)
mscColPeakRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscColPeakRowStatus.setStatus("mandatory")
_DataCollectionMIB_ObjectIdentity = ObjectIdentity
dataCollectionMIB = _DataCollectionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14)
)
_DataCollectionGroup_ObjectIdentity = ObjectIdentity
dataCollectionGroup = _DataCollectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 1)
)
_DataCollectionGroupCA_ObjectIdentity = ObjectIdentity
dataCollectionGroupCA = _DataCollectionGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 1, 1)
)
_DataCollectionGroupCA02_ObjectIdentity = ObjectIdentity
dataCollectionGroupCA02 = _DataCollectionGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 1, 1, 3)
)
_DataCollectionGroupCA02A_ObjectIdentity = ObjectIdentity
dataCollectionGroupCA02A = _DataCollectionGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 1, 1, 3, 2)
)
_DataCollectionCapabilities_ObjectIdentity = ObjectIdentity
dataCollectionCapabilities = _DataCollectionCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 3)
)
_DataCollectionCapabilitiesCA_ObjectIdentity = ObjectIdentity
dataCollectionCapabilitiesCA = _DataCollectionCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 3, 1)
)
_DataCollectionCapabilitiesCA02_ObjectIdentity = ObjectIdentity
dataCollectionCapabilitiesCA02 = _DataCollectionCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 3, 1, 3)
)
_DataCollectionCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
dataCollectionCapabilitiesCA02A = _DataCollectionCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DataCollectionMIB",
    **{"mscCol": mscCol,
       "mscColRowStatusTable": mscColRowStatusTable,
       "mscColRowStatusEntry": mscColRowStatusEntry,
       "mscColRowStatus": mscColRowStatus,
       "mscColComponentName": mscColComponentName,
       "mscColStorageType": mscColStorageType,
       "mscColIndex": mscColIndex,
       "mscColSp": mscColSp,
       "mscColSpRowStatusTable": mscColSpRowStatusTable,
       "mscColSpRowStatusEntry": mscColSpRowStatusEntry,
       "mscColSpRowStatus": mscColSpRowStatus,
       "mscColSpComponentName": mscColSpComponentName,
       "mscColSpStorageType": mscColSpStorageType,
       "mscColSpIndex": mscColSpIndex,
       "mscColSpProvTable": mscColSpProvTable,
       "mscColSpProvEntry": mscColSpProvEntry,
       "mscColSpSpooling": mscColSpSpooling,
       "mscColSpMaximumNumberOfFiles": mscColSpMaximumNumberOfFiles,
       "mscColSpStateTable": mscColSpStateTable,
       "mscColSpStateEntry": mscColSpStateEntry,
       "mscColSpAdminState": mscColSpAdminState,
       "mscColSpOperationalState": mscColSpOperationalState,
       "mscColSpUsageState": mscColSpUsageState,
       "mscColSpAvailabilityStatus": mscColSpAvailabilityStatus,
       "mscColSpProceduralStatus": mscColSpProceduralStatus,
       "mscColSpControlStatus": mscColSpControlStatus,
       "mscColSpAlarmStatus": mscColSpAlarmStatus,
       "mscColSpStandbyStatus": mscColSpStandbyStatus,
       "mscColSpUnknownStatus": mscColSpUnknownStatus,
       "mscColSpOperTable": mscColSpOperTable,
       "mscColSpOperEntry": mscColSpOperEntry,
       "mscColSpSpoolingFileName": mscColSpSpoolingFileName,
       "mscColSpStatsTable": mscColSpStatsTable,
       "mscColSpStatsEntry": mscColSpStatsEntry,
       "mscColSpCurrentQueueSize": mscColSpCurrentQueueSize,
       "mscColSpRecordsRx": mscColSpRecordsRx,
       "mscColSpRecordsDiscarded": mscColSpRecordsDiscarded,
       "mscColAg": mscColAg,
       "mscColAgRowStatusTable": mscColAgRowStatusTable,
       "mscColAgRowStatusEntry": mscColAgRowStatusEntry,
       "mscColAgRowStatus": mscColAgRowStatus,
       "mscColAgComponentName": mscColAgComponentName,
       "mscColAgStorageType": mscColAgStorageType,
       "mscColAgIndex": mscColAgIndex,
       "mscColAgStatsTable": mscColAgStatsTable,
       "mscColAgStatsEntry": mscColAgStatsEntry,
       "mscColAgCurrentQueueSize": mscColAgCurrentQueueSize,
       "mscColAgRecordsRx": mscColAgRecordsRx,
       "mscColAgRecordsDiscarded": mscColAgRecordsDiscarded,
       "mscColAgAgentStatsTable": mscColAgAgentStatsTable,
       "mscColAgAgentStatsEntry": mscColAgAgentStatsEntry,
       "mscColAgRecordsNotGenerated": mscColAgRecordsNotGenerated,
       "mscColProvTable": mscColProvTable,
       "mscColProvEntry": mscColProvEntry,
       "mscColAgentQueueSize": mscColAgentQueueSize,
       "mscColStatsTable": mscColStatsTable,
       "mscColStatsEntry": mscColStatsEntry,
       "mscColCurrentQueueSize": mscColCurrentQueueSize,
       "mscColRecordsRx": mscColRecordsRx,
       "mscColRecordsDiscarded": mscColRecordsDiscarded,
       "mscColTimesTable": mscColTimesTable,
       "mscColTimesEntry": mscColTimesEntry,
       "mscColTimesValue": mscColTimesValue,
       "mscColTimesRowStatus": mscColTimesRowStatus,
       "mscColLastTable": mscColLastTable,
       "mscColLastEntry": mscColLastEntry,
       "mscColLastValue": mscColLastValue,
       "mscColPeakTable": mscColPeakTable,
       "mscColPeakEntry": mscColPeakEntry,
       "mscColPeakValue": mscColPeakValue,
       "mscColPeakRowStatus": mscColPeakRowStatus,
       "dataCollectionMIB": dataCollectionMIB,
       "dataCollectionGroup": dataCollectionGroup,
       "dataCollectionGroupCA": dataCollectionGroupCA,
       "dataCollectionGroupCA02": dataCollectionGroupCA02,
       "dataCollectionGroupCA02A": dataCollectionGroupCA02A,
       "dataCollectionCapabilities": dataCollectionCapabilities,
       "dataCollectionCapabilitiesCA": dataCollectionCapabilitiesCA,
       "dataCollectionCapabilitiesCA02": dataCollectionCapabilitiesCA02,
       "dataCollectionCapabilitiesCA02A": dataCollectionCapabilitiesCA02A}
)
