# SNMP MIB module (GWPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWPOA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:27 2024
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

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Gwpoa_ObjectIdentity = ObjectIdentity
gwpoa = _Gwpoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 38)
)
_Poa_ObjectIdentity = ObjectIdentity
poa = _Poa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1)
)
_PoaTable_Object = MibTable
poaTable = _PoaTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1)
)
if mibBuilder.loadTexts:
    poaTable.setStatus("mandatory")
_PoaEntry_Object = MibTableRow
poaEntry = _PoaEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1)
)
poaEntry.setIndexNames(
    (0, "GWPOA-MIB", "poaIndex"),
)
if mibBuilder.loadTexts:
    poaEntry.setStatus("mandatory")
_PoaIndex_Type = Integer32
_PoaIndex_Object = MibTableColumn
poaIndex = _PoaIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 1),
    _PoaIndex_Type()
)
poaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poaIndex.setStatus("mandatory")


class _PoaPostOfficeName_Type(DisplayString):
    """Custom type poaPostOfficeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoaPostOfficeName_Type.__name__ = "DisplayString"
_PoaPostOfficeName_Object = MibTableColumn
poaPostOfficeName = _PoaPostOfficeName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 2),
    _PoaPostOfficeName_Type()
)
poaPostOfficeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaPostOfficeName.setStatus("mandatory")
_PoaTotalMsgs_Type = Counter32
_PoaTotalMsgs_Object = MibTableColumn
poaTotalMsgs = _PoaTotalMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 3),
    _PoaTotalMsgs_Type()
)
poaTotalMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaTotalMsgs.setStatus("mandatory")
_PoaProblemMsgs_Type = Counter32
_PoaProblemMsgs_Object = MibTableColumn
poaProblemMsgs = _PoaProblemMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 4),
    _PoaProblemMsgs_Type()
)
poaProblemMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaProblemMsgs.setStatus("mandatory")
_PoaStatuses_Type = Counter32
_PoaStatuses_Object = MibTableColumn
poaStatuses = _PoaStatuses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 5),
    _PoaStatuses_Type()
)
poaStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaStatuses.setStatus("mandatory")
_PoaDeliveredUsers_Type = Counter32
_PoaDeliveredUsers_Object = MibTableColumn
poaDeliveredUsers = _PoaDeliveredUsers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 6),
    _PoaDeliveredUsers_Type()
)
poaDeliveredUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaDeliveredUsers.setStatus("mandatory")
_PoaExecutedRules_Type = Counter32
_PoaExecutedRules_Object = MibTableColumn
poaExecutedRules = _PoaExecutedRules_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 7),
    _PoaExecutedRules_Type()
)
poaExecutedRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaExecutedRules.setStatus("mandatory")
_PoaUndeliverableMsgs_Type = Counter32
_PoaUndeliverableMsgs_Object = MibTableColumn
poaUndeliverableMsgs = _PoaUndeliverableMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 8),
    _PoaUndeliverableMsgs_Type()
)
poaUndeliverableMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaUndeliverableMsgs.setStatus("mandatory")
_PoaPriorityQueues_Type = Gauge32
_PoaPriorityQueues_Object = MibTableColumn
poaPriorityQueues = _PoaPriorityQueues_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 9),
    _PoaPriorityQueues_Type()
)
poaPriorityQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaPriorityQueues.setStatus("mandatory")
_PoaNormalQueues_Type = Gauge32
_PoaNormalQueues_Object = MibTableColumn
poaNormalQueues = _PoaNormalQueues_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 10),
    _PoaNormalQueues_Type()
)
poaNormalQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaNormalQueues.setStatus("mandatory")
_PoaUptime_Type = TimeTicks
_PoaUptime_Object = MibTableColumn
poaUptime = _PoaUptime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 11),
    _PoaUptime_Type()
)
poaUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaUptime.setStatus("mandatory")


class _PoaCurrentLogFile_Type(DisplayString):
    """Custom type poaCurrentLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoaCurrentLogFile_Type.__name__ = "DisplayString"
_PoaCurrentLogFile_Object = MibTableColumn
poaCurrentLogFile = _PoaCurrentLogFile_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 12),
    _PoaCurrentLogFile_Type()
)
poaCurrentLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaCurrentLogFile.setStatus("mandatory")


class _PoaLogLevel_Type(Integer32):
    """Custom type poaLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("verbose", 1))
    )


_PoaLogLevel_Type.__name__ = "Integer32"
_PoaLogLevel_Object = MibTableColumn
poaLogLevel = _PoaLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 13),
    _PoaLogLevel_Type()
)
poaLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poaLogLevel.setStatus("mandatory")


class _PoaFileLogging_Type(Integer32):
    """Custom type poaFileLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_PoaFileLogging_Type.__name__ = "Integer32"
_PoaFileLogging_Object = MibTableColumn
poaFileLogging = _PoaFileLogging_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 14),
    _PoaFileLogging_Type()
)
poaFileLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poaFileLogging.setStatus("mandatory")
_PoaMaxLogFileAge_Type = Integer32
_PoaMaxLogFileAge_Object = MibTableColumn
poaMaxLogFileAge = _PoaMaxLogFileAge_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 15),
    _PoaMaxLogFileAge_Type()
)
poaMaxLogFileAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poaMaxLogFileAge.setStatus("mandatory")
_PoaMaxLogDiskSpace_Type = Integer32
_PoaMaxLogDiskSpace_Object = MibTableColumn
poaMaxLogDiskSpace = _PoaMaxLogDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 16),
    _PoaMaxLogDiskSpace_Type()
)
poaMaxLogDiskSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poaMaxLogDiskSpace.setStatus("mandatory")
_PoaCSRequests_Type = Integer32
_PoaCSRequests_Object = MibTableColumn
poaCSRequests = _PoaCSRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 17),
    _PoaCSRequests_Type()
)
poaCSRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaCSRequests.setStatus("mandatory")
_PoaCSRequestsPending_Type = Integer32
_PoaCSRequestsPending_Object = MibTableColumn
poaCSRequestsPending = _PoaCSRequestsPending_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 18),
    _PoaCSRequestsPending_Type()
)
poaCSRequestsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaCSRequestsPending.setStatus("mandatory")
_PoaCSUserTimeouts_Type = Integer32
_PoaCSUserTimeouts_Object = MibTableColumn
poaCSUserTimeouts = _PoaCSUserTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 19),
    _PoaCSUserTimeouts_Type()
)
poaCSUserTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaCSUserTimeouts.setStatus("mandatory")
_PoaCSFileQueues_Type = Integer32
_PoaCSFileQueues_Object = MibTableColumn
poaCSFileQueues = _PoaCSFileQueues_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 20),
    _PoaCSFileQueues_Type()
)
poaCSFileQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaCSFileQueues.setStatus("mandatory")
_PoaCSUsersConnected_Type = Integer32
_PoaCSUsersConnected_Object = MibTableColumn
poaCSUsersConnected = _PoaCSUsersConnected_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 21),
    _PoaCSUsersConnected_Type()
)
poaCSUsersConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaCSUsersConnected.setStatus("mandatory")


class _PoaGUID_Type(DisplayString):
    """Custom type poaGUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_PoaGUID_Type.__name__ = "DisplayString"
_PoaGUID_Object = MibTableColumn
poaGUID = _PoaGUID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 22),
    _PoaGUID_Type()
)
poaGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaGUID.setStatus("mandatory")


class _PoaOS_Type(DisplayString):
    """Custom type poaOS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PoaOS_Type.__name__ = "DisplayString"
_PoaOS_Object = MibTableColumn
poaOS = _PoaOS_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 23),
    _PoaOS_Type()
)
poaOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaOS.setStatus("mandatory")


class _PoaVersion_Type(DisplayString):
    """Custom type poaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PoaVersion_Type.__name__ = "DisplayString"
_PoaVersion_Object = MibTableColumn
poaVersion = _PoaVersion_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 24),
    _PoaVersion_Type()
)
poaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaVersion.setStatus("mandatory")


class _PoaAdmThreadStatus_Type(DisplayString):
    """Custom type poaAdmThreadStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PoaAdmThreadStatus_Type.__name__ = "DisplayString"
_PoaAdmThreadStatus_Object = MibTableColumn
poaAdmThreadStatus = _PoaAdmThreadStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 25),
    _PoaAdmThreadStatus_Type()
)
poaAdmThreadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaAdmThreadStatus.setStatus("mandatory")
_PoaAdmCompletedMsgs_Type = Counter32
_PoaAdmCompletedMsgs_Object = MibTableColumn
poaAdmCompletedMsgs = _PoaAdmCompletedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 26),
    _PoaAdmCompletedMsgs_Type()
)
poaAdmCompletedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaAdmCompletedMsgs.setStatus("mandatory")
_PoaAdmErrorMsgs_Type = Counter32
_PoaAdmErrorMsgs_Object = MibTableColumn
poaAdmErrorMsgs = _PoaAdmErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 27),
    _PoaAdmErrorMsgs_Type()
)
poaAdmErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaAdmErrorMsgs.setStatus("mandatory")
_PoaAdmInQueueMsgs_Type = Gauge32
_PoaAdmInQueueMsgs_Object = MibTableColumn
poaAdmInQueueMsgs = _PoaAdmInQueueMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 28),
    _PoaAdmInQueueMsgs_Type()
)
poaAdmInQueueMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaAdmInQueueMsgs.setStatus("mandatory")


class _PoaAdmDBStatus_Type(DisplayString):
    """Custom type poaAdmDBStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PoaAdmDBStatus_Type.__name__ = "DisplayString"
_PoaAdmDBStatus_Object = MibTableColumn
poaAdmDBStatus = _PoaAdmDBStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 29),
    _PoaAdmDBStatus_Type()
)
poaAdmDBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaAdmDBStatus.setStatus("mandatory")


class _PoaAdmDBSortLang_Type(DisplayString):
    """Custom type poaAdmDBSortLang based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PoaAdmDBSortLang_Type.__name__ = "DisplayString"
_PoaAdmDBSortLang_Object = MibTableColumn
poaAdmDBSortLang = _PoaAdmDBSortLang_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 30),
    _PoaAdmDBSortLang_Type()
)
poaAdmDBSortLang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaAdmDBSortLang.setStatus("mandatory")
_PoaAdmDBRecoverCnt_Type = Counter32
_PoaAdmDBRecoverCnt_Object = MibTableColumn
poaAdmDBRecoverCnt = _PoaAdmDBRecoverCnt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 31),
    _PoaAdmDBRecoverCnt_Type()
)
poaAdmDBRecoverCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaAdmDBRecoverCnt.setStatus("mandatory")


class _PoaDN_Type(DisplayString):
    """Custom type poaDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoaDN_Type.__name__ = "DisplayString"
_PoaDN_Object = MibTableColumn
poaDN = _PoaDN_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 32),
    _PoaDN_Type()
)
poaDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaDN.setStatus("mandatory")
_PoaAvailDiskSpace_Type = Counter32
_PoaAvailDiskSpace_Object = MibTableColumn
poaAvailDiskSpace = _PoaAvailDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 33),
    _PoaAvailDiskSpace_Type()
)
poaAvailDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaAvailDiskSpace.setStatus("mandatory")
_PoaHTTPPort_Type = Integer32
_PoaHTTPPort_Object = MibTableColumn
poaHTTPPort = _PoaHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 34),
    _PoaHTTPPort_Type()
)
poaHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poaHTTPPort.setStatus("mandatory")


class _PoaAdmDBStatusNumber_Type(Integer32):
    """Custom type poaAdmDBStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("normal", 0),
          ("recovering", 2),
          ("unknown", 3))
    )


_PoaAdmDBStatusNumber_Type.__name__ = "Integer32"
_PoaAdmDBStatusNumber_Object = MibTableColumn
poaAdmDBStatusNumber = _PoaAdmDBStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 35),
    _PoaAdmDBStatusNumber_Type()
)
poaAdmDBStatusNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poaAdmDBStatusNumber.setStatus("mandatory")


class _PoaMTPStatus_Type(Integer32):
    """Custom type poaMTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2),
          ("receiveopen", 4),
          ("sendopen", 3),
          ("unknown", 0))
    )


_PoaMTPStatus_Type.__name__ = "Integer32"
_PoaMTPStatus_Object = MibTableColumn
poaMTPStatus = _PoaMTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 36),
    _PoaMTPStatus_Type()
)
poaMTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poaMTPStatus.setStatus("mandatory")
_PoaUptimeInSeconds_Type = Integer32
_PoaUptimeInSeconds_Object = MibTableColumn
poaUptimeInSeconds = _PoaUptimeInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 37),
    _PoaUptimeInSeconds_Type()
)
poaUptimeInSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poaUptimeInSeconds.setStatus("mandatory")
_PoaTrapInfo_ObjectIdentity = ObjectIdentity
poaTrapInfo = _PoaTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 2)
)
_PoaTrapTime_Type = Integer32
_PoaTrapTime_Object = MibScalar
poaTrapTime = _PoaTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 2, 1),
    _PoaTrapTime_Type()
)
poaTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poaTrapTime.setStatus("mandatory")
_PoaTraps_ObjectIdentity = ObjectIdentity
poaTraps = _PoaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 3)
)

# Managed Objects groups


# Notification objects

poaStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 3, 0, 1)
)
poaStartTrap.setObjects(
      *(("GWPOA-MIB", "poaTrapTime"),
        ("GWPOA-MIB", "poaPostOfficeName"),
        ("GWPOA-MIB", "poaGUID"))
)
if mibBuilder.loadTexts:
    poaStartTrap.setStatus(
        ""
    )

poaShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 38, 3, 0, 2)
)
poaShutdownTrap.setObjects(
      *(("GWPOA-MIB", "poaTrapTime"),
        ("GWPOA-MIB", "poaPostOfficeName"),
        ("GWPOA-MIB", "poaGUID"))
)
if mibBuilder.loadTexts:
    poaShutdownTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWPOA-MIB",
    **{"novell": novell,
       "mibDoc": mibDoc,
       "gwpoa": gwpoa,
       "poa": poa,
       "poaTable": poaTable,
       "poaEntry": poaEntry,
       "poaIndex": poaIndex,
       "poaPostOfficeName": poaPostOfficeName,
       "poaTotalMsgs": poaTotalMsgs,
       "poaProblemMsgs": poaProblemMsgs,
       "poaStatuses": poaStatuses,
       "poaDeliveredUsers": poaDeliveredUsers,
       "poaExecutedRules": poaExecutedRules,
       "poaUndeliverableMsgs": poaUndeliverableMsgs,
       "poaPriorityQueues": poaPriorityQueues,
       "poaNormalQueues": poaNormalQueues,
       "poaUptime": poaUptime,
       "poaCurrentLogFile": poaCurrentLogFile,
       "poaLogLevel": poaLogLevel,
       "poaFileLogging": poaFileLogging,
       "poaMaxLogFileAge": poaMaxLogFileAge,
       "poaMaxLogDiskSpace": poaMaxLogDiskSpace,
       "poaCSRequests": poaCSRequests,
       "poaCSRequestsPending": poaCSRequestsPending,
       "poaCSUserTimeouts": poaCSUserTimeouts,
       "poaCSFileQueues": poaCSFileQueues,
       "poaCSUsersConnected": poaCSUsersConnected,
       "poaGUID": poaGUID,
       "poaOS": poaOS,
       "poaVersion": poaVersion,
       "poaAdmThreadStatus": poaAdmThreadStatus,
       "poaAdmCompletedMsgs": poaAdmCompletedMsgs,
       "poaAdmErrorMsgs": poaAdmErrorMsgs,
       "poaAdmInQueueMsgs": poaAdmInQueueMsgs,
       "poaAdmDBStatus": poaAdmDBStatus,
       "poaAdmDBSortLang": poaAdmDBSortLang,
       "poaAdmDBRecoverCnt": poaAdmDBRecoverCnt,
       "poaDN": poaDN,
       "poaAvailDiskSpace": poaAvailDiskSpace,
       "poaHTTPPort": poaHTTPPort,
       "poaAdmDBStatusNumber": poaAdmDBStatusNumber,
       "poaMTPStatus": poaMTPStatus,
       "poaUptimeInSeconds": poaUptimeInSeconds,
       "poaTrapInfo": poaTrapInfo,
       "poaTrapTime": poaTrapTime,
       "poaTraps": poaTraps,
       "poaStartTrap": poaStartTrap,
       "poaShutdownTrap": poaShutdownTrap}
)
