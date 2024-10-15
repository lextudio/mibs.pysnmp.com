# SNMP MIB module (Nortel-Magellan-Passport-TimeMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-TimeMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:28 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(EnterpriseDateAndTime,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
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

_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19)
)
_TimeRowStatusTable_Object = MibTable
timeRowStatusTable = _TimeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 1)
)
if mibBuilder.loadTexts:
    timeRowStatusTable.setStatus("mandatory")
_TimeRowStatusEntry_Object = MibTableRow
timeRowStatusEntry = _TimeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 1, 1)
)
timeRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeIndex"),
)
if mibBuilder.loadTexts:
    timeRowStatusEntry.setStatus("mandatory")
_TimeRowStatus_Type = RowStatus
_TimeRowStatus_Object = MibTableColumn
timeRowStatus = _TimeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 1, 1, 1),
    _TimeRowStatus_Type()
)
timeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRowStatus.setStatus("mandatory")
_TimeComponentName_Type = DisplayString
_TimeComponentName_Object = MibTableColumn
timeComponentName = _TimeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 1, 1, 2),
    _TimeComponentName_Type()
)
timeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeComponentName.setStatus("mandatory")
_TimeStorageType_Type = StorageType
_TimeStorageType_Object = MibTableColumn
timeStorageType = _TimeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 1, 1, 4),
    _TimeStorageType_Type()
)
timeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeStorageType.setStatus("mandatory")
_TimeIndex_Type = NonReplicated
_TimeIndex_Object = MibTableColumn
timeIndex = _TimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 1, 1, 10),
    _TimeIndex_Type()
)
timeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeIndex.setStatus("mandatory")
_TimeServer_ObjectIdentity = ObjectIdentity
timeServer = _TimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3)
)
_TimeServerRowStatusTable_Object = MibTable
timeServerRowStatusTable = _TimeServerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 1)
)
if mibBuilder.loadTexts:
    timeServerRowStatusTable.setStatus("mandatory")
_TimeServerRowStatusEntry_Object = MibTableRow
timeServerRowStatusEntry = _TimeServerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 1, 1)
)
timeServerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeIndex"),
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeServerIndex"),
)
if mibBuilder.loadTexts:
    timeServerRowStatusEntry.setStatus("mandatory")
_TimeServerRowStatus_Type = RowStatus
_TimeServerRowStatus_Object = MibTableColumn
timeServerRowStatus = _TimeServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 1, 1, 1),
    _TimeServerRowStatus_Type()
)
timeServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerRowStatus.setStatus("mandatory")
_TimeServerComponentName_Type = DisplayString
_TimeServerComponentName_Object = MibTableColumn
timeServerComponentName = _TimeServerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 1, 1, 2),
    _TimeServerComponentName_Type()
)
timeServerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerComponentName.setStatus("mandatory")
_TimeServerStorageType_Type = StorageType
_TimeServerStorageType_Object = MibTableColumn
timeServerStorageType = _TimeServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 1, 1, 4),
    _TimeServerStorageType_Type()
)
timeServerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerStorageType.setStatus("mandatory")


class _TimeServerIndex_Type(Integer32):
    """Custom type timeServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TimeServerIndex_Type.__name__ = "Integer32"
_TimeServerIndex_Object = MibTableColumn
timeServerIndex = _TimeServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 1, 1, 10),
    _TimeServerIndex_Type()
)
timeServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeServerIndex.setStatus("mandatory")
_TimeServerProvTable_Object = MibTable
timeServerProvTable = _TimeServerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 11)
)
if mibBuilder.loadTexts:
    timeServerProvTable.setStatus("mandatory")
_TimeServerProvEntry_Object = MibTableRow
timeServerProvEntry = _TimeServerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 11, 1)
)
timeServerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeIndex"),
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeServerIndex"),
)
if mibBuilder.loadTexts:
    timeServerProvEntry.setStatus("mandatory")
_TimeServerIpAddress_Type = IpAddress
_TimeServerIpAddress_Object = MibTableColumn
timeServerIpAddress = _TimeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 11, 1, 1),
    _TimeServerIpAddress_Type()
)
timeServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerIpAddress.setStatus("mandatory")


class _TimeServerIpStack_Type(Integer32):
    """Custom type timeServerIpStack based on Integer32"""
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


_TimeServerIpStack_Type.__name__ = "Integer32"
_TimeServerIpStack_Object = MibTableColumn
timeServerIpStack = _TimeServerIpStack_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 11, 1, 2),
    _TimeServerIpStack_Type()
)
timeServerIpStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServerIpStack.setStatus("mandatory")
_TimeServerStateTable_Object = MibTable
timeServerStateTable = _TimeServerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 12)
)
if mibBuilder.loadTexts:
    timeServerStateTable.setStatus("mandatory")
_TimeServerStateEntry_Object = MibTableRow
timeServerStateEntry = _TimeServerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 12, 1)
)
timeServerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeIndex"),
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeServerIndex"),
)
if mibBuilder.loadTexts:
    timeServerStateEntry.setStatus("mandatory")


class _TimeServerAdminState_Type(Integer32):
    """Custom type timeServerAdminState based on Integer32"""
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


_TimeServerAdminState_Type.__name__ = "Integer32"
_TimeServerAdminState_Object = MibTableColumn
timeServerAdminState = _TimeServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 12, 1, 1),
    _TimeServerAdminState_Type()
)
timeServerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerAdminState.setStatus("mandatory")


class _TimeServerOperationalState_Type(Integer32):
    """Custom type timeServerOperationalState based on Integer32"""
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


_TimeServerOperationalState_Type.__name__ = "Integer32"
_TimeServerOperationalState_Object = MibTableColumn
timeServerOperationalState = _TimeServerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 12, 1, 2),
    _TimeServerOperationalState_Type()
)
timeServerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerOperationalState.setStatus("mandatory")


class _TimeServerUsageState_Type(Integer32):
    """Custom type timeServerUsageState based on Integer32"""
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


_TimeServerUsageState_Type.__name__ = "Integer32"
_TimeServerUsageState_Object = MibTableColumn
timeServerUsageState = _TimeServerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 12, 1, 3),
    _TimeServerUsageState_Type()
)
timeServerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerUsageState.setStatus("mandatory")
_TimeServerOperTable_Object = MibTable
timeServerOperTable = _TimeServerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13)
)
if mibBuilder.loadTexts:
    timeServerOperTable.setStatus("mandatory")
_TimeServerOperEntry_Object = MibTableRow
timeServerOperEntry = _TimeServerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13, 1)
)
timeServerOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeIndex"),
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeServerIndex"),
)
if mibBuilder.loadTexts:
    timeServerOperEntry.setStatus("mandatory")


class _TimeServerXntpVersion_Type(Unsigned32):
    """Custom type timeServerXntpVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TimeServerXntpVersion_Type.__name__ = "Unsigned32"
_TimeServerXntpVersion_Object = MibTableColumn
timeServerXntpVersion = _TimeServerXntpVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13, 1, 1),
    _TimeServerXntpVersion_Type()
)
timeServerXntpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerXntpVersion.setStatus("mandatory")


class _TimeServerStratum_Type(Unsigned32):
    """Custom type timeServerStratum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TimeServerStratum_Type.__name__ = "Unsigned32"
_TimeServerStratum_Object = MibTableColumn
timeServerStratum = _TimeServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13, 1, 2),
    _TimeServerStratum_Type()
)
timeServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerStratum.setStatus("mandatory")


class _TimeServerPoll_Type(Unsigned32):
    """Custom type timeServerPoll based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TimeServerPoll_Type.__name__ = "Unsigned32"
_TimeServerPoll_Object = MibTableColumn
timeServerPoll = _TimeServerPoll_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13, 1, 3),
    _TimeServerPoll_Type()
)
timeServerPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerPoll.setStatus("mandatory")
_TimeServerPktSent_Type = Counter32
_TimeServerPktSent_Object = MibTableColumn
timeServerPktSent = _TimeServerPktSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13, 1, 4),
    _TimeServerPktSent_Type()
)
timeServerPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerPktSent.setStatus("mandatory")
_TimeServerPktRecv_Type = Counter32
_TimeServerPktRecv_Object = MibTableColumn
timeServerPktRecv = _TimeServerPktRecv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13, 1, 5),
    _TimeServerPktRecv_Type()
)
timeServerPktRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerPktRecv.setStatus("mandatory")
_TimeServerPktValid_Type = Counter32
_TimeServerPktValid_Object = MibTableColumn
timeServerPktValid = _TimeServerPktValid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13, 1, 6),
    _TimeServerPktValid_Type()
)
timeServerPktValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerPktValid.setStatus("mandatory")


class _TimeServerStatus_Type(OctetString):
    """Custom type timeServerStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TimeServerStatus_Type.__name__ = "OctetString"
_TimeServerStatus_Object = MibTableColumn
timeServerStatus = _TimeServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 3, 13, 1, 392),
    _TimeServerStatus_Type()
)
timeServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServerStatus.setStatus("mandatory")
_TimeOperTable_Object = MibTable
timeOperTable = _TimeOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10)
)
if mibBuilder.loadTexts:
    timeOperTable.setStatus("mandatory")
_TimeOperEntry_Object = MibTableRow
timeOperEntry = _TimeOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1)
)
timeOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeIndex"),
)
if mibBuilder.loadTexts:
    timeOperEntry.setStatus("mandatory")


class _TimeNetworkTime_Type(EnterpriseDateAndTime):
    """Custom type timeNetworkTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_TimeNetworkTime_Type.__name__ = "EnterpriseDateAndTime"
_TimeNetworkTime_Object = MibTableColumn
timeNetworkTime = _TimeNetworkTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1, 1),
    _TimeNetworkTime_Type()
)
timeNetworkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNetworkTime.setStatus("obsolete")


class _TimeSyncStatus_Type(Integer32):
    """Custom type timeSyncStatus based on Integer32"""
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


_TimeSyncStatus_Type.__name__ = "Integer32"
_TimeSyncStatus_Object = MibTableColumn
timeSyncStatus = _TimeSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1, 2),
    _TimeSyncStatus_Type()
)
timeSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSyncStatus.setStatus("mandatory")
_TimeSyncSource_Type = IpAddress
_TimeSyncSource_Object = MibTableColumn
timeSyncSource = _TimeSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1, 3),
    _TimeSyncSource_Type()
)
timeSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSyncSource.setStatus("obsolete")


class _TimeTimeOffset_Type(Unsigned32):
    """Custom type timeTimeOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_TimeTimeOffset_Type.__name__ = "Unsigned32"
_TimeTimeOffset_Object = MibTableColumn
timeTimeOffset = _TimeTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1, 4),
    _TimeTimeOffset_Type()
)
timeTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeTimeOffset.setStatus("obsolete")


class _TimeModuleTime_Type(EnterpriseDateAndTime):
    """Custom type timeModuleTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_TimeModuleTime_Type.__name__ = "EnterpriseDateAndTime"
_TimeModuleTime_Object = MibTableColumn
timeModuleTime = _TimeModuleTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1, 5),
    _TimeModuleTime_Type()
)
timeModuleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeModuleTime.setStatus("mandatory")


class _TimeOffset_Type(Integer32):
    """Custom type timeOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 1440),
    )


_TimeOffset_Type.__name__ = "Integer32"
_TimeOffset_Object = MibTableColumn
timeOffset = _TimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1, 6),
    _TimeOffset_Type()
)
timeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeOffset.setStatus("mandatory")
_TimeMainServer_Type = IpAddress
_TimeMainServer_Object = MibTableColumn
timeMainServer = _TimeMainServer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1, 7),
    _TimeMainServer_Type()
)
timeMainServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeMainServer.setStatus("mandatory")


class _TimeXntpVersion_Type(Unsigned32):
    """Custom type timeXntpVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TimeXntpVersion_Type.__name__ = "Unsigned32"
_TimeXntpVersion_Object = MibTableColumn
timeXntpVersion = _TimeXntpVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 10, 1, 8),
    _TimeXntpVersion_Type()
)
timeXntpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeXntpVersion.setStatus("mandatory")
_TimeSyncSourcesTable_Object = MibTable
timeSyncSourcesTable = _TimeSyncSourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 391)
)
if mibBuilder.loadTexts:
    timeSyncSourcesTable.setStatus("mandatory")
_TimeSyncSourcesEntry_Object = MibTableRow
timeSyncSourcesEntry = _TimeSyncSourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 391, 1)
)
timeSyncSourcesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeIndex"),
    (0, "Nortel-Magellan-Passport-TimeMIB", "timeSyncSourcesValue"),
)
if mibBuilder.loadTexts:
    timeSyncSourcesEntry.setStatus("mandatory")
_TimeSyncSourcesValue_Type = IpAddress
_TimeSyncSourcesValue_Object = MibTableColumn
timeSyncSourcesValue = _TimeSyncSourcesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 19, 391, 1, 1),
    _TimeSyncSourcesValue_Type()
)
timeSyncSourcesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSyncSourcesValue.setStatus("mandatory")
_NS_ObjectIdentity = ObjectIdentity
nS = _NS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20)
)
_NSRowStatusTable_Object = MibTable
nSRowStatusTable = _NSRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 1)
)
if mibBuilder.loadTexts:
    nSRowStatusTable.setStatus("mandatory")
_NSRowStatusEntry_Object = MibTableRow
nSRowStatusEntry = _NSRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 1, 1)
)
nSRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "nSIndex"),
)
if mibBuilder.loadTexts:
    nSRowStatusEntry.setStatus("mandatory")
_NSRowStatus_Type = RowStatus
_NSRowStatus_Object = MibTableColumn
nSRowStatus = _NSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 1, 1, 1),
    _NSRowStatus_Type()
)
nSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nSRowStatus.setStatus("mandatory")
_NSComponentName_Type = DisplayString
_NSComponentName_Object = MibTableColumn
nSComponentName = _NSComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 1, 1, 2),
    _NSComponentName_Type()
)
nSComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSComponentName.setStatus("mandatory")
_NSStorageType_Type = StorageType
_NSStorageType_Object = MibTableColumn
nSStorageType = _NSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 1, 1, 4),
    _NSStorageType_Type()
)
nSStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSStorageType.setStatus("mandatory")
_NSIndex_Type = NonReplicated
_NSIndex_Object = MibTableColumn
nSIndex = _NSIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 1, 1, 10),
    _NSIndex_Type()
)
nSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nSIndex.setStatus("mandatory")
_NSProvTable_Object = MibTable
nSProvTable = _NSProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 10)
)
if mibBuilder.loadTexts:
    nSProvTable.setStatus("mandatory")
_NSProvEntry_Object = MibTableRow
nSProvEntry = _NSProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 10, 1)
)
nSProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "nSIndex"),
)
if mibBuilder.loadTexts:
    nSProvEntry.setStatus("mandatory")
_NSPrimaryReference_Type = RowPointer
_NSPrimaryReference_Object = MibTableColumn
nSPrimaryReference = _NSPrimaryReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 10, 1, 1),
    _NSPrimaryReference_Type()
)
nSPrimaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nSPrimaryReference.setStatus("mandatory")
_NSSecondaryReference_Type = RowPointer
_NSSecondaryReference_Object = MibTableColumn
nSSecondaryReference = _NSSecondaryReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 10, 1, 2),
    _NSSecondaryReference_Type()
)
nSSecondaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nSSecondaryReference.setStatus("mandatory")
_NSTertiaryReference_Type = RowPointer
_NSTertiaryReference_Object = MibTableColumn
nSTertiaryReference = _NSTertiaryReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 10, 1, 3),
    _NSTertiaryReference_Type()
)
nSTertiaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nSTertiaryReference.setStatus("mandatory")
_NSStateTable_Object = MibTable
nSStateTable = _NSStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 11)
)
if mibBuilder.loadTexts:
    nSStateTable.setStatus("mandatory")
_NSStateEntry_Object = MibTableRow
nSStateEntry = _NSStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 11, 1)
)
nSStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "nSIndex"),
)
if mibBuilder.loadTexts:
    nSStateEntry.setStatus("mandatory")


class _NSAdminState_Type(Integer32):
    """Custom type nSAdminState based on Integer32"""
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


_NSAdminState_Type.__name__ = "Integer32"
_NSAdminState_Object = MibTableColumn
nSAdminState = _NSAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 11, 1, 1),
    _NSAdminState_Type()
)
nSAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSAdminState.setStatus("mandatory")


class _NSOperationalState_Type(Integer32):
    """Custom type nSOperationalState based on Integer32"""
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


_NSOperationalState_Type.__name__ = "Integer32"
_NSOperationalState_Object = MibTableColumn
nSOperationalState = _NSOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 11, 1, 2),
    _NSOperationalState_Type()
)
nSOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSOperationalState.setStatus("mandatory")


class _NSUsageState_Type(Integer32):
    """Custom type nSUsageState based on Integer32"""
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


_NSUsageState_Type.__name__ = "Integer32"
_NSUsageState_Object = MibTableColumn
nSUsageState = _NSUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 11, 1, 3),
    _NSUsageState_Type()
)
nSUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSUsageState.setStatus("mandatory")
_NSOperTable_Object = MibTable
nSOperTable = _NSOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 12)
)
if mibBuilder.loadTexts:
    nSOperTable.setStatus("mandatory")
_NSOperEntry_Object = MibTableRow
nSOperEntry = _NSOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 12, 1)
)
nSOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TimeMIB", "nSIndex"),
)
if mibBuilder.loadTexts:
    nSOperEntry.setStatus("mandatory")


class _NSClockSyncState_Type(Integer32):
    """Custom type nSClockSyncState based on Integer32"""
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


_NSClockSyncState_Type.__name__ = "Integer32"
_NSClockSyncState_Object = MibTableColumn
nSClockSyncState = _NSClockSyncState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 12, 1, 1),
    _NSClockSyncState_Type()
)
nSClockSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSClockSyncState.setStatus("mandatory")
_NSActiveReference_Type = RowPointer
_NSActiveReference_Object = MibTableColumn
nSActiveReference = _NSActiveReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 12, 1, 2),
    _NSActiveReference_Type()
)
nSActiveReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSActiveReference.setStatus("mandatory")
_NSStandbyReference_Type = RowPointer
_NSStandbyReference_Object = MibTableColumn
nSStandbyReference = _NSStandbyReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 20, 12, 1, 3),
    _NSStandbyReference_Type()
)
nSStandbyReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSStandbyReference.setStatus("mandatory")
_TimeMIB_ObjectIdentity = ObjectIdentity
timeMIB = _TimeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13)
)
_TimeGroup_ObjectIdentity = ObjectIdentity
timeGroup = _TimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13, 1)
)
_TimeGroupBE_ObjectIdentity = ObjectIdentity
timeGroupBE = _TimeGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13, 1, 5)
)
_TimeGroupBE01_ObjectIdentity = ObjectIdentity
timeGroupBE01 = _TimeGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13, 1, 5, 2)
)
_TimeGroupBE01A_ObjectIdentity = ObjectIdentity
timeGroupBE01A = _TimeGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13, 1, 5, 2, 2)
)
_TimeCapabilities_ObjectIdentity = ObjectIdentity
timeCapabilities = _TimeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13, 3)
)
_TimeCapabilitiesBE_ObjectIdentity = ObjectIdentity
timeCapabilitiesBE = _TimeCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13, 3, 5)
)
_TimeCapabilitiesBE01_ObjectIdentity = ObjectIdentity
timeCapabilitiesBE01 = _TimeCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13, 3, 5, 2)
)
_TimeCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
timeCapabilitiesBE01A = _TimeCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 13, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-TimeMIB",
    **{"time": time,
       "timeRowStatusTable": timeRowStatusTable,
       "timeRowStatusEntry": timeRowStatusEntry,
       "timeRowStatus": timeRowStatus,
       "timeComponentName": timeComponentName,
       "timeStorageType": timeStorageType,
       "timeIndex": timeIndex,
       "timeServer": timeServer,
       "timeServerRowStatusTable": timeServerRowStatusTable,
       "timeServerRowStatusEntry": timeServerRowStatusEntry,
       "timeServerRowStatus": timeServerRowStatus,
       "timeServerComponentName": timeServerComponentName,
       "timeServerStorageType": timeServerStorageType,
       "timeServerIndex": timeServerIndex,
       "timeServerProvTable": timeServerProvTable,
       "timeServerProvEntry": timeServerProvEntry,
       "timeServerIpAddress": timeServerIpAddress,
       "timeServerIpStack": timeServerIpStack,
       "timeServerStateTable": timeServerStateTable,
       "timeServerStateEntry": timeServerStateEntry,
       "timeServerAdminState": timeServerAdminState,
       "timeServerOperationalState": timeServerOperationalState,
       "timeServerUsageState": timeServerUsageState,
       "timeServerOperTable": timeServerOperTable,
       "timeServerOperEntry": timeServerOperEntry,
       "timeServerXntpVersion": timeServerXntpVersion,
       "timeServerStratum": timeServerStratum,
       "timeServerPoll": timeServerPoll,
       "timeServerPktSent": timeServerPktSent,
       "timeServerPktRecv": timeServerPktRecv,
       "timeServerPktValid": timeServerPktValid,
       "timeServerStatus": timeServerStatus,
       "timeOperTable": timeOperTable,
       "timeOperEntry": timeOperEntry,
       "timeNetworkTime": timeNetworkTime,
       "timeSyncStatus": timeSyncStatus,
       "timeSyncSource": timeSyncSource,
       "timeTimeOffset": timeTimeOffset,
       "timeModuleTime": timeModuleTime,
       "timeOffset": timeOffset,
       "timeMainServer": timeMainServer,
       "timeXntpVersion": timeXntpVersion,
       "timeSyncSourcesTable": timeSyncSourcesTable,
       "timeSyncSourcesEntry": timeSyncSourcesEntry,
       "timeSyncSourcesValue": timeSyncSourcesValue,
       "nS": nS,
       "nSRowStatusTable": nSRowStatusTable,
       "nSRowStatusEntry": nSRowStatusEntry,
       "nSRowStatus": nSRowStatus,
       "nSComponentName": nSComponentName,
       "nSStorageType": nSStorageType,
       "nSIndex": nSIndex,
       "nSProvTable": nSProvTable,
       "nSProvEntry": nSProvEntry,
       "nSPrimaryReference": nSPrimaryReference,
       "nSSecondaryReference": nSSecondaryReference,
       "nSTertiaryReference": nSTertiaryReference,
       "nSStateTable": nSStateTable,
       "nSStateEntry": nSStateEntry,
       "nSAdminState": nSAdminState,
       "nSOperationalState": nSOperationalState,
       "nSUsageState": nSUsageState,
       "nSOperTable": nSOperTable,
       "nSOperEntry": nSOperEntry,
       "nSClockSyncState": nSClockSyncState,
       "nSActiveReference": nSActiveReference,
       "nSStandbyReference": nSStandbyReference,
       "timeMIB": timeMIB,
       "timeGroup": timeGroup,
       "timeGroupBE": timeGroupBE,
       "timeGroupBE01": timeGroupBE01,
       "timeGroupBE01A": timeGroupBE01A,
       "timeCapabilities": timeCapabilities,
       "timeCapabilitiesBE": timeCapabilitiesBE,
       "timeCapabilitiesBE01": timeCapabilitiesBE01,
       "timeCapabilitiesBE01A": timeCapabilitiesBE01A}
)
