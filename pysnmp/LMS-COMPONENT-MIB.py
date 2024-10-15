# SNMP MIB module (LMS-COMPONENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LMS-COMPONENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:16 2024
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



class TimeInterval(Integer32):
    """Custom type TimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class UInteger32(Integer32):
    """Custom type UInteger32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lotus_ObjectIdentity = ObjectIdentity
lotus = _Lotus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334)
)
_Notes_ObjectIdentity = ObjectIdentity
notes = _Notes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 1)
)
_Lcs_ObjectIdentity = ObjectIdentity
lcs = _Lcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 2)
)
_Softswitch_ObjectIdentity = ObjectIdentity
softswitch = _Softswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3)
)
_Common_mibs_ObjectIdentity = ObjectIdentity
common_mibs = _Common_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 1)
)
_Lms_ObjectIdentity = ObjectIdentity
lms = _Lms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2)
)
_LmsComponent_ObjectIdentity = ObjectIdentity
lmsComponent = _LmsComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1)
)
_LmsSwitch_ObjectIdentity = ObjectIdentity
lmsSwitch = _LmsSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1)
)
_LmsSwitchID_Type = DisplayString
_LmsSwitchID_Object = MibScalar
lmsSwitchID = _LmsSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 1),
    _LmsSwitchID_Type()
)
lmsSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSwitchID.setStatus("mandatory")
_LmsSwitchName_Type = DisplayString
_LmsSwitchName_Object = MibScalar
lmsSwitchName = _LmsSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 2),
    _LmsSwitchName_Type()
)
lmsSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmsSwitchName.setStatus("mandatory")
_LmsSwitchVersion_Type = DisplayString
_LmsSwitchVersion_Object = MibScalar
lmsSwitchVersion = _LmsSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 3),
    _LmsSwitchVersion_Type()
)
lmsSwitchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSwitchVersion.setStatus("mandatory")
_LmsSwitchUpTime_Type = TimeTicks
_LmsSwitchUpTime_Object = MibScalar
lmsSwitchUpTime = _LmsSwitchUpTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 4),
    _LmsSwitchUpTime_Type()
)
lmsSwitchUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSwitchUpTime.setStatus("mandatory")


class _LmsSwitchOperStatus_Type(Integer32):
    """Custom type lmsSwitchOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("configurable", 5),
          ("running", 6),
          ("shutdown", 4),
          ("starting", 3),
          ("stopped", 2),
          ("stopping", 7),
          ("unknown", 1))
    )


_LmsSwitchOperStatus_Type.__name__ = "Integer32"
_LmsSwitchOperStatus_Object = MibScalar
lmsSwitchOperStatus = _LmsSwitchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 5),
    _LmsSwitchOperStatus_Type()
)
lmsSwitchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSwitchOperStatus.setStatus("mandatory")
_LmsSwitchLastChange_Type = TimeTicks
_LmsSwitchLastChange_Object = MibScalar
lmsSwitchLastChange = _LmsSwitchLastChange_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 6),
    _LmsSwitchLastChange_Type()
)
lmsSwitchLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsSwitchLastChange.setStatus("mandatory")


class _LmsSwitchDesiredOperStatus_Type(Integer32):
    """Custom type lmsSwitchDesiredOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("configurable", 3),
          ("running", 4),
          ("shutdown", 2),
          ("stopped", 1))
    )


_LmsSwitchDesiredOperStatus_Type.__name__ = "Integer32"
_LmsSwitchDesiredOperStatus_Object = MibScalar
lmsSwitchDesiredOperStatus = _LmsSwitchDesiredOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 7),
    _LmsSwitchDesiredOperStatus_Type()
)
lmsSwitchDesiredOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmsSwitchDesiredOperStatus.setStatus("mandatory")
_LmsSwitchDescr_Type = DisplayString
_LmsSwitchDescr_Object = MibScalar
lmsSwitchDescr = _LmsSwitchDescr_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 8),
    _LmsSwitchDescr_Type()
)
lmsSwitchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmsSwitchDescr.setStatus("mandatory")
_LmsSwitchContact_Type = DisplayString
_LmsSwitchContact_Object = MibScalar
lmsSwitchContact = _LmsSwitchContact_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 1, 9),
    _LmsSwitchContact_Type()
)
lmsSwitchContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmsSwitchContact.setStatus("mandatory")
_LmsSystem_ObjectIdentity = ObjectIdentity
lmsSystem = _LmsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 2)
)
_LmsMsgStore_ObjectIdentity = ObjectIdentity
lmsMsgStore = _LmsMsgStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 3)
)


class _LmsMsgStoreDatabaseUtilization_Type(Integer32):
    """Custom type lmsMsgStoreDatabaseUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LmsMsgStoreDatabaseUtilization_Type.__name__ = "Integer32"
_LmsMsgStoreDatabaseUtilization_Object = MibScalar
lmsMsgStoreDatabaseUtilization = _LmsMsgStoreDatabaseUtilization_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 3, 1),
    _LmsMsgStoreDatabaseUtilization_Type()
)
lmsMsgStoreDatabaseUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsMsgStoreDatabaseUtilization.setStatus("mandatory")


class _LmsMsgStoreFileSystemUtilization_Type(Integer32):
    """Custom type lmsMsgStoreFileSystemUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LmsMsgStoreFileSystemUtilization_Type.__name__ = "Integer32"
_LmsMsgStoreFileSystemUtilization_Object = MibScalar
lmsMsgStoreFileSystemUtilization = _LmsMsgStoreFileSystemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 3, 2),
    _LmsMsgStoreFileSystemUtilization_Type()
)
lmsMsgStoreFileSystemUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsMsgStoreFileSystemUtilization.setStatus("mandatory")
_LmsTransports_ObjectIdentity = ObjectIdentity
lmsTransports = _LmsTransports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 4)
)


class _SnaState_Type(Integer32):
    """Custom type snaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("congested", 4),
          ("down", 2),
          ("halted", 3),
          ("quiescing", 6),
          ("restarting", 5),
          ("unknown", 7),
          ("up", 1))
    )


_SnaState_Type.__name__ = "Integer32"
_SnaState_Object = MibScalar
snaState = _SnaState_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 4, 1),
    _SnaState_Type()
)
snaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaState.setStatus("mandatory")


class _OsiState_Type(Integer32):
    """Custom type osiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("congested", 4),
          ("down", 2),
          ("halted", 3),
          ("quiescing", 6),
          ("restarting", 5),
          ("unknown", 7),
          ("up", 1))
    )


_OsiState_Type.__name__ = "Integer32"
_OsiState_Object = MibScalar
osiState = _OsiState_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 4, 2),
    _OsiState_Type()
)
osiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osiState.setStatus("mandatory")


class _TcpIpState_Type(Integer32):
    """Custom type tcpIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("congested", 4),
          ("down", 2),
          ("halted", 3),
          ("quiescing", 6),
          ("restarting", 5),
          ("unknown", 7),
          ("up", 1))
    )


_TcpIpState_Type.__name__ = "Integer32"
_TcpIpState_Object = MibScalar
tcpIpState = _TcpIpState_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 4, 3),
    _TcpIpState_Type()
)
tcpIpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIpState.setStatus("mandatory")
_TransportLastUpdate_Type = TimeTicks
_TransportLastUpdate_Object = MibScalar
transportLastUpdate = _TransportLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 4, 4),
    _TransportLastUpdate_Type()
)
transportLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transportLastUpdate.setStatus("mandatory")
_LmsIPC_ObjectIdentity = ObjectIdentity
lmsIPC = _LmsIPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5)
)


class _IpcOperStatus_Type(Integer32):
    """Custom type ipcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("congested", 4),
          ("down", 2),
          ("halted", 3),
          ("quiescing", 6),
          ("restarting", 5),
          ("unknown", 7),
          ("up", 1))
    )


_IpcOperStatus_Type.__name__ = "Integer32"
_IpcOperStatus_Object = MibScalar
ipcOperStatus = _IpcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 1),
    _IpcOperStatus_Type()
)
ipcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcOperStatus.setStatus("mandatory")
_SemaphoreMaxUsers_Type = UInteger32
_SemaphoreMaxUsers_Object = MibScalar
semaphoreMaxUsers = _SemaphoreMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 2),
    _SemaphoreMaxUsers_Type()
)
semaphoreMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semaphoreMaxUsers.setStatus("mandatory")
_SemaphoreCurrUsers_Type = Gauge32
_SemaphoreCurrUsers_Object = MibScalar
semaphoreCurrUsers = _SemaphoreCurrUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 3),
    _SemaphoreCurrUsers_Type()
)
semaphoreCurrUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semaphoreCurrUsers.setStatus("mandatory")
_SemaphoreMaxSemaphores_Type = UInteger32
_SemaphoreMaxSemaphores_Object = MibScalar
semaphoreMaxSemaphores = _SemaphoreMaxSemaphores_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 4),
    _SemaphoreMaxSemaphores_Type()
)
semaphoreMaxSemaphores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semaphoreMaxSemaphores.setStatus("mandatory")
_SemaphoreCurrSemaphores_Type = Gauge32
_SemaphoreCurrSemaphores_Object = MibScalar
semaphoreCurrSemaphores = _SemaphoreCurrSemaphores_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 5),
    _SemaphoreCurrSemaphores_Type()
)
semaphoreCurrSemaphores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semaphoreCurrSemaphores.setStatus("mandatory")
_SemaphoreMaxNodes_Type = UInteger32
_SemaphoreMaxNodes_Object = MibScalar
semaphoreMaxNodes = _SemaphoreMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 6),
    _SemaphoreMaxNodes_Type()
)
semaphoreMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semaphoreMaxNodes.setStatus("mandatory")
_SemaphoreCurrNodes_Type = Gauge32
_SemaphoreCurrNodes_Object = MibScalar
semaphoreCurrNodes = _SemaphoreCurrNodes_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 7),
    _SemaphoreCurrNodes_Type()
)
semaphoreCurrNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semaphoreCurrNodes.setStatus("mandatory")
_SharedmemMaxUsers_Type = UInteger32
_SharedmemMaxUsers_Object = MibScalar
sharedmemMaxUsers = _SharedmemMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 8),
    _SharedmemMaxUsers_Type()
)
sharedmemMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedmemMaxUsers.setStatus("mandatory")
_SharedmemCurrUsers_Type = Gauge32
_SharedmemCurrUsers_Object = MibScalar
sharedmemCurrUsers = _SharedmemCurrUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 9),
    _SharedmemCurrUsers_Type()
)
sharedmemCurrUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedmemCurrUsers.setStatus("mandatory")
_SharedmemMaxSeqments_Type = UInteger32
_SharedmemMaxSeqments_Object = MibScalar
sharedmemMaxSeqments = _SharedmemMaxSeqments_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 10),
    _SharedmemMaxSeqments_Type()
)
sharedmemMaxSeqments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedmemMaxSeqments.setStatus("mandatory")
_SharedmemCurrSegments_Type = Gauge32
_SharedmemCurrSegments_Object = MibScalar
sharedmemCurrSegments = _SharedmemCurrSegments_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 11),
    _SharedmemCurrSegments_Type()
)
sharedmemCurrSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedmemCurrSegments.setStatus("mandatory")
_SharedmemMaxNodes_Type = UInteger32
_SharedmemMaxNodes_Object = MibScalar
sharedmemMaxNodes = _SharedmemMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 12),
    _SharedmemMaxNodes_Type()
)
sharedmemMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedmemMaxNodes.setStatus("mandatory")
_SharedmemCurrNodes_Type = Gauge32
_SharedmemCurrNodes_Object = MibScalar
sharedmemCurrNodes = _SharedmemCurrNodes_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 13),
    _SharedmemCurrNodes_Type()
)
sharedmemCurrNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedmemCurrNodes.setStatus("mandatory")
_SharedmemMaxMempool_Type = UInteger32
_SharedmemMaxMempool_Object = MibScalar
sharedmemMaxMempool = _SharedmemMaxMempool_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 14),
    _SharedmemMaxMempool_Type()
)
sharedmemMaxMempool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedmemMaxMempool.setStatus("mandatory")
_SharedmemCurrMempool_Type = Gauge32
_SharedmemCurrMempool_Object = MibScalar
sharedmemCurrMempool = _SharedmemCurrMempool_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 15),
    _SharedmemCurrMempool_Type()
)
sharedmemCurrMempool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedmemCurrMempool.setStatus("mandatory")
_MsgqueueMaxUsers_Type = UInteger32
_MsgqueueMaxUsers_Object = MibScalar
msgqueueMaxUsers = _MsgqueueMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 16),
    _MsgqueueMaxUsers_Type()
)
msgqueueMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgqueueMaxUsers.setStatus("mandatory")
_MsgqueueCurrUsers_Type = Gauge32
_MsgqueueCurrUsers_Object = MibScalar
msgqueueCurrUsers = _MsgqueueCurrUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 17),
    _MsgqueueCurrUsers_Type()
)
msgqueueCurrUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgqueueCurrUsers.setStatus("mandatory")
_MsgqueueMaxQueues_Type = UInteger32
_MsgqueueMaxQueues_Object = MibScalar
msgqueueMaxQueues = _MsgqueueMaxQueues_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 18),
    _MsgqueueMaxQueues_Type()
)
msgqueueMaxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgqueueMaxQueues.setStatus("mandatory")
_MsgqueueCurrQueues_Type = Gauge32
_MsgqueueCurrQueues_Object = MibScalar
msgqueueCurrQueues = _MsgqueueCurrQueues_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 19),
    _MsgqueueCurrQueues_Type()
)
msgqueueCurrQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgqueueCurrQueues.setStatus("mandatory")
_MsgqueueMaxNodes_Type = UInteger32
_MsgqueueMaxNodes_Object = MibScalar
msgqueueMaxNodes = _MsgqueueMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 20),
    _MsgqueueMaxNodes_Type()
)
msgqueueMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgqueueMaxNodes.setStatus("mandatory")
_MsgqueueCurrNodes_Type = Gauge32
_MsgqueueCurrNodes_Object = MibScalar
msgqueueCurrNodes = _MsgqueueCurrNodes_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 21),
    _MsgqueueCurrNodes_Type()
)
msgqueueCurrNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgqueueCurrNodes.setStatus("mandatory")
_MsgqueueMaxMempool_Type = UInteger32
_MsgqueueMaxMempool_Object = MibScalar
msgqueueMaxMempool = _MsgqueueMaxMempool_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 22),
    _MsgqueueMaxMempool_Type()
)
msgqueueMaxMempool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgqueueMaxMempool.setStatus("mandatory")
_MsgqueueCurrMempool_Type = Gauge32
_MsgqueueCurrMempool_Object = MibScalar
msgqueueCurrMempool = _MsgqueueCurrMempool_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 5, 23),
    _MsgqueueCurrMempool_Type()
)
msgqueueCurrMempool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgqueueCurrMempool.setStatus("mandatory")
_LmsDatabase_ObjectIdentity = ObjectIdentity
lmsDatabase = _LmsDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 6)
)


class _DbConfigSpaceUtilization_Type(Integer32):
    """Custom type dbConfigSpaceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DbConfigSpaceUtilization_Type.__name__ = "Integer32"
_DbConfigSpaceUtilization_Object = MibScalar
dbConfigSpaceUtilization = _DbConfigSpaceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 6, 1),
    _DbConfigSpaceUtilization_Type()
)
dbConfigSpaceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbConfigSpaceUtilization.setStatus("mandatory")


class _DbNameSpaceUtilization_Type(Integer32):
    """Custom type dbNameSpaceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DbNameSpaceUtilization_Type.__name__ = "Integer32"
_DbNameSpaceUtilization_Object = MibScalar
dbNameSpaceUtilization = _DbNameSpaceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 6, 2),
    _DbNameSpaceUtilization_Type()
)
dbNameSpaceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbNameSpaceUtilization.setStatus("mandatory")


class _DbDistribSpaceUtilization_Type(Integer32):
    """Custom type dbDistribSpaceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DbDistribSpaceUtilization_Type.__name__ = "Integer32"
_DbDistribSpaceUtilization_Object = MibScalar
dbDistribSpaceUtilization = _DbDistribSpaceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 6, 3),
    _DbDistribSpaceUtilization_Type()
)
dbDistribSpaceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbDistribSpaceUtilization.setStatus("mandatory")


class _DbSystemSpaceUtilization_Type(Integer32):
    """Custom type dbSystemSpaceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DbSystemSpaceUtilization_Type.__name__ = "Integer32"
_DbSystemSpaceUtilization_Object = MibScalar
dbSystemSpaceUtilization = _DbSystemSpaceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 6, 4),
    _DbSystemSpaceUtilization_Type()
)
dbSystemSpaceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbSystemSpaceUtilization.setStatus("mandatory")
_DbLastUpdate_Type = TimeTicks
_DbLastUpdate_Object = MibScalar
dbLastUpdate = _DbLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 1, 6, 5),
    _DbLastUpdate_Type()
)
dbLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbLastUpdate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LMS-COMPONENT-MIB",
    **{"TimeInterval": TimeInterval,
       "UInteger32": UInteger32,
       "lotus": lotus,
       "notes": notes,
       "lcs": lcs,
       "softswitch": softswitch,
       "common-mibs": common_mibs,
       "lms": lms,
       "lmsComponent": lmsComponent,
       "lmsSwitch": lmsSwitch,
       "lmsSwitchID": lmsSwitchID,
       "lmsSwitchName": lmsSwitchName,
       "lmsSwitchVersion": lmsSwitchVersion,
       "lmsSwitchUpTime": lmsSwitchUpTime,
       "lmsSwitchOperStatus": lmsSwitchOperStatus,
       "lmsSwitchLastChange": lmsSwitchLastChange,
       "lmsSwitchDesiredOperStatus": lmsSwitchDesiredOperStatus,
       "lmsSwitchDescr": lmsSwitchDescr,
       "lmsSwitchContact": lmsSwitchContact,
       "lmsSystem": lmsSystem,
       "lmsMsgStore": lmsMsgStore,
       "lmsMsgStoreDatabaseUtilization": lmsMsgStoreDatabaseUtilization,
       "lmsMsgStoreFileSystemUtilization": lmsMsgStoreFileSystemUtilization,
       "lmsTransports": lmsTransports,
       "snaState": snaState,
       "osiState": osiState,
       "tcpIpState": tcpIpState,
       "transportLastUpdate": transportLastUpdate,
       "lmsIPC": lmsIPC,
       "ipcOperStatus": ipcOperStatus,
       "semaphoreMaxUsers": semaphoreMaxUsers,
       "semaphoreCurrUsers": semaphoreCurrUsers,
       "semaphoreMaxSemaphores": semaphoreMaxSemaphores,
       "semaphoreCurrSemaphores": semaphoreCurrSemaphores,
       "semaphoreMaxNodes": semaphoreMaxNodes,
       "semaphoreCurrNodes": semaphoreCurrNodes,
       "sharedmemMaxUsers": sharedmemMaxUsers,
       "sharedmemCurrUsers": sharedmemCurrUsers,
       "sharedmemMaxSeqments": sharedmemMaxSeqments,
       "sharedmemCurrSegments": sharedmemCurrSegments,
       "sharedmemMaxNodes": sharedmemMaxNodes,
       "sharedmemCurrNodes": sharedmemCurrNodes,
       "sharedmemMaxMempool": sharedmemMaxMempool,
       "sharedmemCurrMempool": sharedmemCurrMempool,
       "msgqueueMaxUsers": msgqueueMaxUsers,
       "msgqueueCurrUsers": msgqueueCurrUsers,
       "msgqueueMaxQueues": msgqueueMaxQueues,
       "msgqueueCurrQueues": msgqueueCurrQueues,
       "msgqueueMaxNodes": msgqueueMaxNodes,
       "msgqueueCurrNodes": msgqueueCurrNodes,
       "msgqueueMaxMempool": msgqueueMaxMempool,
       "msgqueueCurrMempool": msgqueueCurrMempool,
       "lmsDatabase": lmsDatabase,
       "dbConfigSpaceUtilization": dbConfigSpaceUtilization,
       "dbNameSpaceUtilization": dbNameSpaceUtilization,
       "dbDistribSpaceUtilization": dbDistribSpaceUtilization,
       "dbSystemSpaceUtilization": dbSystemSpaceUtilization,
       "dbLastUpdate": dbLastUpdate}
)
