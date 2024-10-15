# SNMP MIB module (Nortel-MsCarrier-MscPassport-TimeMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-TimeMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:09 2024
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
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(EnterpriseDateAndTime,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
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

_MscTime_ObjectIdentity = ObjectIdentity
mscTime = _MscTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19)
)
_MscTimeRowStatusTable_Object = MibTable
mscTimeRowStatusTable = _MscTimeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1)
)
if mibBuilder.loadTexts:
    mscTimeRowStatusTable.setStatus("mandatory")
_MscTimeRowStatusEntry_Object = MibTableRow
mscTimeRowStatusEntry = _MscTimeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1)
)
mscTimeRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"),
)
if mibBuilder.loadTexts:
    mscTimeRowStatusEntry.setStatus("mandatory")
_MscTimeRowStatus_Type = RowStatus
_MscTimeRowStatus_Object = MibTableColumn
mscTimeRowStatus = _MscTimeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1, 1),
    _MscTimeRowStatus_Type()
)
mscTimeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeRowStatus.setStatus("mandatory")
_MscTimeComponentName_Type = DisplayString
_MscTimeComponentName_Object = MibTableColumn
mscTimeComponentName = _MscTimeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1, 2),
    _MscTimeComponentName_Type()
)
mscTimeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeComponentName.setStatus("mandatory")
_MscTimeStorageType_Type = StorageType
_MscTimeStorageType_Object = MibTableColumn
mscTimeStorageType = _MscTimeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1, 4),
    _MscTimeStorageType_Type()
)
mscTimeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeStorageType.setStatus("mandatory")
_MscTimeIndex_Type = NonReplicated
_MscTimeIndex_Object = MibTableColumn
mscTimeIndex = _MscTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 1, 1, 10),
    _MscTimeIndex_Type()
)
mscTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTimeIndex.setStatus("mandatory")
_MscTimeServer_ObjectIdentity = ObjectIdentity
mscTimeServer = _MscTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3)
)
_MscTimeServerRowStatusTable_Object = MibTable
mscTimeServerRowStatusTable = _MscTimeServerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1)
)
if mibBuilder.loadTexts:
    mscTimeServerRowStatusTable.setStatus("mandatory")
_MscTimeServerRowStatusEntry_Object = MibTableRow
mscTimeServerRowStatusEntry = _MscTimeServerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1)
)
mscTimeServerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeServerIndex"),
)
if mibBuilder.loadTexts:
    mscTimeServerRowStatusEntry.setStatus("mandatory")
_MscTimeServerRowStatus_Type = RowStatus
_MscTimeServerRowStatus_Object = MibTableColumn
mscTimeServerRowStatus = _MscTimeServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1, 1),
    _MscTimeServerRowStatus_Type()
)
mscTimeServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTimeServerRowStatus.setStatus("mandatory")
_MscTimeServerComponentName_Type = DisplayString
_MscTimeServerComponentName_Object = MibTableColumn
mscTimeServerComponentName = _MscTimeServerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1, 2),
    _MscTimeServerComponentName_Type()
)
mscTimeServerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerComponentName.setStatus("mandatory")
_MscTimeServerStorageType_Type = StorageType
_MscTimeServerStorageType_Object = MibTableColumn
mscTimeServerStorageType = _MscTimeServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1, 4),
    _MscTimeServerStorageType_Type()
)
mscTimeServerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerStorageType.setStatus("mandatory")


class _MscTimeServerIndex_Type(Integer32):
    """Custom type mscTimeServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscTimeServerIndex_Type.__name__ = "Integer32"
_MscTimeServerIndex_Object = MibTableColumn
mscTimeServerIndex = _MscTimeServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 1, 1, 10),
    _MscTimeServerIndex_Type()
)
mscTimeServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTimeServerIndex.setStatus("mandatory")
_MscTimeServerProvTable_Object = MibTable
mscTimeServerProvTable = _MscTimeServerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 11)
)
if mibBuilder.loadTexts:
    mscTimeServerProvTable.setStatus("mandatory")
_MscTimeServerProvEntry_Object = MibTableRow
mscTimeServerProvEntry = _MscTimeServerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 11, 1)
)
mscTimeServerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeServerIndex"),
)
if mibBuilder.loadTexts:
    mscTimeServerProvEntry.setStatus("mandatory")
_MscTimeServerIpAddress_Type = IpAddress
_MscTimeServerIpAddress_Object = MibTableColumn
mscTimeServerIpAddress = _MscTimeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 11, 1, 1),
    _MscTimeServerIpAddress_Type()
)
mscTimeServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTimeServerIpAddress.setStatus("mandatory")


class _MscTimeServerIpStack_Type(Integer32):
    """Custom type mscTimeServerIpStack based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipiFrIpiVc", 1),
          ("vrIp", 2))
    )


_MscTimeServerIpStack_Type.__name__ = "Integer32"
_MscTimeServerIpStack_Object = MibTableColumn
mscTimeServerIpStack = _MscTimeServerIpStack_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 11, 1, 2),
    _MscTimeServerIpStack_Type()
)
mscTimeServerIpStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTimeServerIpStack.setStatus("mandatory")
_MscTimeServerStateTable_Object = MibTable
mscTimeServerStateTable = _MscTimeServerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12)
)
if mibBuilder.loadTexts:
    mscTimeServerStateTable.setStatus("mandatory")
_MscTimeServerStateEntry_Object = MibTableRow
mscTimeServerStateEntry = _MscTimeServerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12, 1)
)
mscTimeServerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeServerIndex"),
)
if mibBuilder.loadTexts:
    mscTimeServerStateEntry.setStatus("mandatory")


class _MscTimeServerAdminState_Type(Integer32):
    """Custom type mscTimeServerAdminState based on Integer32"""
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


_MscTimeServerAdminState_Type.__name__ = "Integer32"
_MscTimeServerAdminState_Object = MibTableColumn
mscTimeServerAdminState = _MscTimeServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12, 1, 1),
    _MscTimeServerAdminState_Type()
)
mscTimeServerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerAdminState.setStatus("mandatory")


class _MscTimeServerOperationalState_Type(Integer32):
    """Custom type mscTimeServerOperationalState based on Integer32"""
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


_MscTimeServerOperationalState_Type.__name__ = "Integer32"
_MscTimeServerOperationalState_Object = MibTableColumn
mscTimeServerOperationalState = _MscTimeServerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12, 1, 2),
    _MscTimeServerOperationalState_Type()
)
mscTimeServerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerOperationalState.setStatus("mandatory")


class _MscTimeServerUsageState_Type(Integer32):
    """Custom type mscTimeServerUsageState based on Integer32"""
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


_MscTimeServerUsageState_Type.__name__ = "Integer32"
_MscTimeServerUsageState_Object = MibTableColumn
mscTimeServerUsageState = _MscTimeServerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 12, 1, 3),
    _MscTimeServerUsageState_Type()
)
mscTimeServerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerUsageState.setStatus("mandatory")
_MscTimeServerOperTable_Object = MibTable
mscTimeServerOperTable = _MscTimeServerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13)
)
if mibBuilder.loadTexts:
    mscTimeServerOperTable.setStatus("mandatory")
_MscTimeServerOperEntry_Object = MibTableRow
mscTimeServerOperEntry = _MscTimeServerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1)
)
mscTimeServerOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeServerIndex"),
)
if mibBuilder.loadTexts:
    mscTimeServerOperEntry.setStatus("mandatory")


class _MscTimeServerXntpVersion_Type(Unsigned32):
    """Custom type mscTimeServerXntpVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscTimeServerXntpVersion_Type.__name__ = "Unsigned32"
_MscTimeServerXntpVersion_Object = MibTableColumn
mscTimeServerXntpVersion = _MscTimeServerXntpVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 1),
    _MscTimeServerXntpVersion_Type()
)
mscTimeServerXntpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerXntpVersion.setStatus("mandatory")


class _MscTimeServerStratum_Type(Unsigned32):
    """Custom type mscTimeServerStratum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MscTimeServerStratum_Type.__name__ = "Unsigned32"
_MscTimeServerStratum_Object = MibTableColumn
mscTimeServerStratum = _MscTimeServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 2),
    _MscTimeServerStratum_Type()
)
mscTimeServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerStratum.setStatus("mandatory")


class _MscTimeServerPoll_Type(Unsigned32):
    """Custom type mscTimeServerPoll based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscTimeServerPoll_Type.__name__ = "Unsigned32"
_MscTimeServerPoll_Object = MibTableColumn
mscTimeServerPoll = _MscTimeServerPoll_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 3),
    _MscTimeServerPoll_Type()
)
mscTimeServerPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerPoll.setStatus("mandatory")
_MscTimeServerPktSent_Type = Counter32
_MscTimeServerPktSent_Object = MibTableColumn
mscTimeServerPktSent = _MscTimeServerPktSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 4),
    _MscTimeServerPktSent_Type()
)
mscTimeServerPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerPktSent.setStatus("mandatory")
_MscTimeServerPktRecv_Type = Counter32
_MscTimeServerPktRecv_Object = MibTableColumn
mscTimeServerPktRecv = _MscTimeServerPktRecv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 5),
    _MscTimeServerPktRecv_Type()
)
mscTimeServerPktRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerPktRecv.setStatus("mandatory")
_MscTimeServerPktValid_Type = Counter32
_MscTimeServerPktValid_Object = MibTableColumn
mscTimeServerPktValid = _MscTimeServerPktValid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 6),
    _MscTimeServerPktValid_Type()
)
mscTimeServerPktValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerPktValid.setStatus("mandatory")


class _MscTimeServerStatus_Type(OctetString):
    """Custom type mscTimeServerStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscTimeServerStatus_Type.__name__ = "OctetString"
_MscTimeServerStatus_Object = MibTableColumn
mscTimeServerStatus = _MscTimeServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 3, 13, 1, 392),
    _MscTimeServerStatus_Type()
)
mscTimeServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeServerStatus.setStatus("mandatory")
_MscTimeOperTable_Object = MibTable
mscTimeOperTable = _MscTimeOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10)
)
if mibBuilder.loadTexts:
    mscTimeOperTable.setStatus("mandatory")
_MscTimeOperEntry_Object = MibTableRow
mscTimeOperEntry = _MscTimeOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1)
)
mscTimeOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"),
)
if mibBuilder.loadTexts:
    mscTimeOperEntry.setStatus("mandatory")


class _MscTimeNetworkTime_Type(EnterpriseDateAndTime):
    """Custom type mscTimeNetworkTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscTimeNetworkTime_Type.__name__ = "EnterpriseDateAndTime"
_MscTimeNetworkTime_Object = MibTableColumn
mscTimeNetworkTime = _MscTimeNetworkTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 1),
    _MscTimeNetworkTime_Type()
)
mscTimeNetworkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTimeNetworkTime.setStatus("obsolete")


class _MscTimeSyncStatus_Type(Integer32):
    """Custom type mscTimeSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("synchronized", 0),
          ("synchronizing", 4),
          ("unspecified", 5),
          ("unsynchronized", 1))
    )


_MscTimeSyncStatus_Type.__name__ = "Integer32"
_MscTimeSyncStatus_Object = MibTableColumn
mscTimeSyncStatus = _MscTimeSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 2),
    _MscTimeSyncStatus_Type()
)
mscTimeSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeSyncStatus.setStatus("mandatory")
_MscTimeSyncSource_Type = IpAddress
_MscTimeSyncSource_Object = MibTableColumn
mscTimeSyncSource = _MscTimeSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 3),
    _MscTimeSyncSource_Type()
)
mscTimeSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeSyncSource.setStatus("obsolete")


class _MscTimeTimeOffset_Type(Unsigned32):
    """Custom type mscTimeTimeOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_MscTimeTimeOffset_Type.__name__ = "Unsigned32"
_MscTimeTimeOffset_Object = MibTableColumn
mscTimeTimeOffset = _MscTimeTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 4),
    _MscTimeTimeOffset_Type()
)
mscTimeTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTimeTimeOffset.setStatus("obsolete")


class _MscTimeModuleTime_Type(EnterpriseDateAndTime):
    """Custom type mscTimeModuleTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscTimeModuleTime_Type.__name__ = "EnterpriseDateAndTime"
_MscTimeModuleTime_Object = MibTableColumn
mscTimeModuleTime = _MscTimeModuleTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 5),
    _MscTimeModuleTime_Type()
)
mscTimeModuleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTimeModuleTime.setStatus("mandatory")


class _MscTimeOffset_Type(Integer32):
    """Custom type mscTimeOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 1440),
    )


_MscTimeOffset_Type.__name__ = "Integer32"
_MscTimeOffset_Object = MibTableColumn
mscTimeOffset = _MscTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 6),
    _MscTimeOffset_Type()
)
mscTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTimeOffset.setStatus("mandatory")
_MscTimeMainServer_Type = IpAddress
_MscTimeMainServer_Object = MibTableColumn
mscTimeMainServer = _MscTimeMainServer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 7),
    _MscTimeMainServer_Type()
)
mscTimeMainServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeMainServer.setStatus("mandatory")


class _MscTimeXntpVersion_Type(Unsigned32):
    """Custom type mscTimeXntpVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscTimeXntpVersion_Type.__name__ = "Unsigned32"
_MscTimeXntpVersion_Object = MibTableColumn
mscTimeXntpVersion = _MscTimeXntpVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 10, 1, 8),
    _MscTimeXntpVersion_Type()
)
mscTimeXntpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeXntpVersion.setStatus("mandatory")
_MscTimeSyncSourcesTable_Object = MibTable
mscTimeSyncSourcesTable = _MscTimeSyncSourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 391)
)
if mibBuilder.loadTexts:
    mscTimeSyncSourcesTable.setStatus("mandatory")
_MscTimeSyncSourcesEntry_Object = MibTableRow
mscTimeSyncSourcesEntry = _MscTimeSyncSourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 391, 1)
)
mscTimeSyncSourcesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscTimeSyncSourcesValue"),
)
if mibBuilder.loadTexts:
    mscTimeSyncSourcesEntry.setStatus("mandatory")
_MscTimeSyncSourcesValue_Type = IpAddress
_MscTimeSyncSourcesValue_Object = MibTableColumn
mscTimeSyncSourcesValue = _MscTimeSyncSourcesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 19, 391, 1, 1),
    _MscTimeSyncSourcesValue_Type()
)
mscTimeSyncSourcesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeSyncSourcesValue.setStatus("mandatory")
_MscNS_ObjectIdentity = ObjectIdentity
mscNS = _MscNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20)
)
_MscNSRowStatusTable_Object = MibTable
mscNSRowStatusTable = _MscNSRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1)
)
if mibBuilder.loadTexts:
    mscNSRowStatusTable.setStatus("mandatory")
_MscNSRowStatusEntry_Object = MibTableRow
mscNSRowStatusEntry = _MscNSRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1)
)
mscNSRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscNSIndex"),
)
if mibBuilder.loadTexts:
    mscNSRowStatusEntry.setStatus("mandatory")
_MscNSRowStatus_Type = RowStatus
_MscNSRowStatus_Object = MibTableColumn
mscNSRowStatus = _MscNSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1, 1),
    _MscNSRowStatus_Type()
)
mscNSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNSRowStatus.setStatus("mandatory")
_MscNSComponentName_Type = DisplayString
_MscNSComponentName_Object = MibTableColumn
mscNSComponentName = _MscNSComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1, 2),
    _MscNSComponentName_Type()
)
mscNSComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNSComponentName.setStatus("mandatory")
_MscNSStorageType_Type = StorageType
_MscNSStorageType_Object = MibTableColumn
mscNSStorageType = _MscNSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1, 4),
    _MscNSStorageType_Type()
)
mscNSStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNSStorageType.setStatus("mandatory")
_MscNSIndex_Type = NonReplicated
_MscNSIndex_Object = MibTableColumn
mscNSIndex = _MscNSIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 1, 1, 10),
    _MscNSIndex_Type()
)
mscNSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNSIndex.setStatus("mandatory")
_MscNSProvTable_Object = MibTable
mscNSProvTable = _MscNSProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10)
)
if mibBuilder.loadTexts:
    mscNSProvTable.setStatus("mandatory")
_MscNSProvEntry_Object = MibTableRow
mscNSProvEntry = _MscNSProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10, 1)
)
mscNSProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscNSIndex"),
)
if mibBuilder.loadTexts:
    mscNSProvEntry.setStatus("mandatory")
_MscNSPrimaryReference_Type = RowPointer
_MscNSPrimaryReference_Object = MibTableColumn
mscNSPrimaryReference = _MscNSPrimaryReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10, 1, 1),
    _MscNSPrimaryReference_Type()
)
mscNSPrimaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNSPrimaryReference.setStatus("mandatory")
_MscNSSecondaryReference_Type = RowPointer
_MscNSSecondaryReference_Object = MibTableColumn
mscNSSecondaryReference = _MscNSSecondaryReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10, 1, 2),
    _MscNSSecondaryReference_Type()
)
mscNSSecondaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNSSecondaryReference.setStatus("mandatory")
_MscNSTertiaryReference_Type = RowPointer
_MscNSTertiaryReference_Object = MibTableColumn
mscNSTertiaryReference = _MscNSTertiaryReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 10, 1, 3),
    _MscNSTertiaryReference_Type()
)
mscNSTertiaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNSTertiaryReference.setStatus("mandatory")
_MscNSStateTable_Object = MibTable
mscNSStateTable = _MscNSStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11)
)
if mibBuilder.loadTexts:
    mscNSStateTable.setStatus("mandatory")
_MscNSStateEntry_Object = MibTableRow
mscNSStateEntry = _MscNSStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11, 1)
)
mscNSStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscNSIndex"),
)
if mibBuilder.loadTexts:
    mscNSStateEntry.setStatus("mandatory")


class _MscNSAdminState_Type(Integer32):
    """Custom type mscNSAdminState based on Integer32"""
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


_MscNSAdminState_Type.__name__ = "Integer32"
_MscNSAdminState_Object = MibTableColumn
mscNSAdminState = _MscNSAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11, 1, 1),
    _MscNSAdminState_Type()
)
mscNSAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNSAdminState.setStatus("mandatory")


class _MscNSOperationalState_Type(Integer32):
    """Custom type mscNSOperationalState based on Integer32"""
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


_MscNSOperationalState_Type.__name__ = "Integer32"
_MscNSOperationalState_Object = MibTableColumn
mscNSOperationalState = _MscNSOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11, 1, 2),
    _MscNSOperationalState_Type()
)
mscNSOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNSOperationalState.setStatus("mandatory")


class _MscNSUsageState_Type(Integer32):
    """Custom type mscNSUsageState based on Integer32"""
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


_MscNSUsageState_Type.__name__ = "Integer32"
_MscNSUsageState_Object = MibTableColumn
mscNSUsageState = _MscNSUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 11, 1, 3),
    _MscNSUsageState_Type()
)
mscNSUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNSUsageState.setStatus("mandatory")
_MscNSOperTable_Object = MibTable
mscNSOperTable = _MscNSOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12)
)
if mibBuilder.loadTexts:
    mscNSOperTable.setStatus("mandatory")
_MscNSOperEntry_Object = MibTableRow
mscNSOperEntry = _MscNSOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12, 1)
)
mscNSOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TimeMIB", "mscNSIndex"),
)
if mibBuilder.loadTexts:
    mscNSOperEntry.setStatus("mandatory")


class _MscNSClockSyncState_Type(Integer32):
    """Custom type mscNSClockSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freeRun", 0),
          ("synchronized", 3),
          ("synchronizing", 1))
    )


_MscNSClockSyncState_Type.__name__ = "Integer32"
_MscNSClockSyncState_Object = MibTableColumn
mscNSClockSyncState = _MscNSClockSyncState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12, 1, 1),
    _MscNSClockSyncState_Type()
)
mscNSClockSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNSClockSyncState.setStatus("mandatory")
_MscNSActiveReference_Type = RowPointer
_MscNSActiveReference_Object = MibTableColumn
mscNSActiveReference = _MscNSActiveReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12, 1, 2),
    _MscNSActiveReference_Type()
)
mscNSActiveReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNSActiveReference.setStatus("mandatory")
_MscNSStandbyReference_Type = RowPointer
_MscNSStandbyReference_Object = MibTableColumn
mscNSStandbyReference = _MscNSStandbyReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 20, 12, 1, 3),
    _MscNSStandbyReference_Type()
)
mscNSStandbyReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNSStandbyReference.setStatus("mandatory")
_TimeMIB_ObjectIdentity = ObjectIdentity
timeMIB = _TimeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13)
)
_TimeGroup_ObjectIdentity = ObjectIdentity
timeGroup = _TimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 1)
)
_TimeGroupCA_ObjectIdentity = ObjectIdentity
timeGroupCA = _TimeGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 1, 1)
)
_TimeGroupCA02_ObjectIdentity = ObjectIdentity
timeGroupCA02 = _TimeGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 1, 1, 3)
)
_TimeGroupCA02A_ObjectIdentity = ObjectIdentity
timeGroupCA02A = _TimeGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 1, 1, 3, 2)
)
_TimeCapabilities_ObjectIdentity = ObjectIdentity
timeCapabilities = _TimeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 3)
)
_TimeCapabilitiesCA_ObjectIdentity = ObjectIdentity
timeCapabilitiesCA = _TimeCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 3, 1)
)
_TimeCapabilitiesCA02_ObjectIdentity = ObjectIdentity
timeCapabilitiesCA02 = _TimeCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 3, 1, 3)
)
_TimeCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
timeCapabilitiesCA02A = _TimeCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 13, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-TimeMIB",
    **{"mscTime": mscTime,
       "mscTimeRowStatusTable": mscTimeRowStatusTable,
       "mscTimeRowStatusEntry": mscTimeRowStatusEntry,
       "mscTimeRowStatus": mscTimeRowStatus,
       "mscTimeComponentName": mscTimeComponentName,
       "mscTimeStorageType": mscTimeStorageType,
       "mscTimeIndex": mscTimeIndex,
       "mscTimeServer": mscTimeServer,
       "mscTimeServerRowStatusTable": mscTimeServerRowStatusTable,
       "mscTimeServerRowStatusEntry": mscTimeServerRowStatusEntry,
       "mscTimeServerRowStatus": mscTimeServerRowStatus,
       "mscTimeServerComponentName": mscTimeServerComponentName,
       "mscTimeServerStorageType": mscTimeServerStorageType,
       "mscTimeServerIndex": mscTimeServerIndex,
       "mscTimeServerProvTable": mscTimeServerProvTable,
       "mscTimeServerProvEntry": mscTimeServerProvEntry,
       "mscTimeServerIpAddress": mscTimeServerIpAddress,
       "mscTimeServerIpStack": mscTimeServerIpStack,
       "mscTimeServerStateTable": mscTimeServerStateTable,
       "mscTimeServerStateEntry": mscTimeServerStateEntry,
       "mscTimeServerAdminState": mscTimeServerAdminState,
       "mscTimeServerOperationalState": mscTimeServerOperationalState,
       "mscTimeServerUsageState": mscTimeServerUsageState,
       "mscTimeServerOperTable": mscTimeServerOperTable,
       "mscTimeServerOperEntry": mscTimeServerOperEntry,
       "mscTimeServerXntpVersion": mscTimeServerXntpVersion,
       "mscTimeServerStratum": mscTimeServerStratum,
       "mscTimeServerPoll": mscTimeServerPoll,
       "mscTimeServerPktSent": mscTimeServerPktSent,
       "mscTimeServerPktRecv": mscTimeServerPktRecv,
       "mscTimeServerPktValid": mscTimeServerPktValid,
       "mscTimeServerStatus": mscTimeServerStatus,
       "mscTimeOperTable": mscTimeOperTable,
       "mscTimeOperEntry": mscTimeOperEntry,
       "mscTimeNetworkTime": mscTimeNetworkTime,
       "mscTimeSyncStatus": mscTimeSyncStatus,
       "mscTimeSyncSource": mscTimeSyncSource,
       "mscTimeTimeOffset": mscTimeTimeOffset,
       "mscTimeModuleTime": mscTimeModuleTime,
       "mscTimeOffset": mscTimeOffset,
       "mscTimeMainServer": mscTimeMainServer,
       "mscTimeXntpVersion": mscTimeXntpVersion,
       "mscTimeSyncSourcesTable": mscTimeSyncSourcesTable,
       "mscTimeSyncSourcesEntry": mscTimeSyncSourcesEntry,
       "mscTimeSyncSourcesValue": mscTimeSyncSourcesValue,
       "mscNS": mscNS,
       "mscNSRowStatusTable": mscNSRowStatusTable,
       "mscNSRowStatusEntry": mscNSRowStatusEntry,
       "mscNSRowStatus": mscNSRowStatus,
       "mscNSComponentName": mscNSComponentName,
       "mscNSStorageType": mscNSStorageType,
       "mscNSIndex": mscNSIndex,
       "mscNSProvTable": mscNSProvTable,
       "mscNSProvEntry": mscNSProvEntry,
       "mscNSPrimaryReference": mscNSPrimaryReference,
       "mscNSSecondaryReference": mscNSSecondaryReference,
       "mscNSTertiaryReference": mscNSTertiaryReference,
       "mscNSStateTable": mscNSStateTable,
       "mscNSStateEntry": mscNSStateEntry,
       "mscNSAdminState": mscNSAdminState,
       "mscNSOperationalState": mscNSOperationalState,
       "mscNSUsageState": mscNSUsageState,
       "mscNSOperTable": mscNSOperTable,
       "mscNSOperEntry": mscNSOperEntry,
       "mscNSClockSyncState": mscNSClockSyncState,
       "mscNSActiveReference": mscNSActiveReference,
       "mscNSStandbyReference": mscNSStandbyReference,
       "timeMIB": timeMIB,
       "timeGroup": timeGroup,
       "timeGroupCA": timeGroupCA,
       "timeGroupCA02": timeGroupCA02,
       "timeGroupCA02A": timeGroupCA02A,
       "timeCapabilities": timeCapabilities,
       "timeCapabilitiesCA": timeCapabilitiesCA,
       "timeCapabilitiesCA02": timeCapabilitiesCA02,
       "timeCapabilitiesCA02A": timeCapabilitiesCA02A}
)
