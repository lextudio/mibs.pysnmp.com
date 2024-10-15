# SNMP MIB module (MELLANOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MELLANOX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:55 2024
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

mellanox = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049)
)
mellanox.setRevisions(
        ("2011-01-31 00:00",
         "2010-12-12 00:00",
         "2010-02-01 00:00",
         "2010-01-01 00:00",
         "2009-10-03 00:00",
         "2009-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IbGuid(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_MellanoxProducts_ObjectIdentity = ObjectIdentity
mellanoxProducts = _MellanoxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 1)
)
_MellanoxMgmt_ObjectIdentity = ObjectIdentity
mellanoxMgmt = _MellanoxMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2)
)
_GeneralMgmt_ObjectIdentity = ObjectIdentity
generalMgmt = _GeneralMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1)
)
_GmVariables_ObjectIdentity = ObjectIdentity
gmVariables = _GmVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1)
)
_GmSystem_ObjectIdentity = ObjectIdentity
gmSystem = _GmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 1)
)
_Type_Type = OctetString
_Type_Object = MibScalar
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 1, 1),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_SwVersion_Type = OctetString
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 1, 3),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")
_BuildInfo_Type = OctetString
_BuildInfo_Object = MibScalar
buildInfo = _BuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 1, 4),
    _BuildInfo_Type()
)
buildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildInfo.setStatus("current")
_NodeName_Type = OctetString
_NodeName_Object = MibScalar
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 1, 5),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeName.setStatus("current")
_Procmgr_ObjectIdentity = ObjectIdentity
procmgr = _Procmgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 2)
)
_ProcTable_Object = MibTable
procTable = _ProcTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    procTable.setStatus("current")
_ProcEntry_Object = MibTableRow
procEntry = _ProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 2, 1, 1)
)
procEntry.setIndexNames(
    (0, "MELLANOX-MIB", "procIndex"),
)
if mibBuilder.loadTexts:
    procEntry.setStatus("current")
_ProcIndex_Type = Unsigned32
_ProcIndex_Object = MibTableColumn
procIndex = _ProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 2, 1, 1, 1),
    _ProcIndex_Type()
)
procIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    procIndex.setStatus("current")
_ProcName_Type = OctetString
_ProcName_Object = MibTableColumn
procName = _ProcName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 2, 1, 1, 2),
    _ProcName_Type()
)
procName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procName.setStatus("current")
_ProcStatus_Type = OctetString
_ProcStatus_Object = MibTableColumn
procStatus = _ProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 2, 1, 1, 3),
    _ProcStatus_Type()
)
procStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStatus.setStatus("current")
_ProcNumFailures_Type = Unsigned32
_ProcNumFailures_Object = MibTableColumn
procNumFailures = _ProcNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 2, 1, 1, 4),
    _ProcNumFailures_Type()
)
procNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procNumFailures.setStatus("current")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3)
)
_FsTable_Object = MibTable
fsTable = _FsTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsTable.setStatus("current")
_FsEntry_Object = MibTableRow
fsEntry = _FsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3, 1, 1)
)
fsEntry.setIndexNames(
    (0, "MELLANOX-MIB", "fsIndex"),
)
if mibBuilder.loadTexts:
    fsEntry.setStatus("current")
_FsIndex_Type = Unsigned32
_FsIndex_Object = MibTableColumn
fsIndex = _FsIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3, 1, 1, 1),
    _FsIndex_Type()
)
fsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIndex.setStatus("current")
_FsMountPoint_Type = OctetString
_FsMountPoint_Object = MibTableColumn
fsMountPoint = _FsMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3, 1, 1, 2),
    _FsMountPoint_Type()
)
fsMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMountPoint.setStatus("current")
_FsSpaceTotal_Type = Counter64
_FsSpaceTotal_Object = MibTableColumn
fsSpaceTotal = _FsSpaceTotal_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3, 1, 1, 3),
    _FsSpaceTotal_Type()
)
fsSpaceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSpaceTotal.setStatus("current")
_FsSpaceUsed_Type = Counter64
_FsSpaceUsed_Object = MibTableColumn
fsSpaceUsed = _FsSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3, 1, 1, 4),
    _FsSpaceUsed_Type()
)
fsSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSpaceUsed.setStatus("current")
_FsSpaceFree_Type = Counter64
_FsSpaceFree_Object = MibTableColumn
fsSpaceFree = _FsSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3, 1, 1, 5),
    _FsSpaceFree_Type()
)
fsSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSpaceFree.setStatus("current")
_FsSpaceAvail_Type = Counter64
_FsSpaceAvail_Object = MibTableColumn
fsSpaceAvail = _FsSpaceAvail_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 3, 1, 1, 6),
    _FsSpaceAvail_Type()
)
fsSpaceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSpaceAvail.setStatus("current")
_Cpus_ObjectIdentity = ObjectIdentity
cpus = _Cpus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 4)
)
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("current")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 4, 1, 1)
)
cpuEntry.setIndexNames(
    (0, "MELLANOX-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("current")
_CpuIndex_Type = Unsigned32
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 4, 1, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")
_IdleTime_Type = TimeTicks
_IdleTime_Object = MibTableColumn
idleTime = _IdleTime_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 4, 1, 1, 2),
    _IdleTime_Type()
)
idleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idleTime.setStatus("current")
_SystemTime_Type = TimeTicks
_SystemTime_Object = MibTableColumn
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 4, 1, 1, 3),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_UserTime_Type = TimeTicks
_UserTime_Object = MibTableColumn
userTime = _UserTime_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 1, 4, 1, 1, 4),
    _UserTime_Type()
)
userTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTime.setStatus("current")
_GmNotifications_ObjectIdentity = ObjectIdentity
gmNotifications = _GmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2)
)
_IbSwitch_ObjectIdentity = ObjectIdentity
ibSwitch = _IbSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2)
)
_IbVariables_ObjectIdentity = ObjectIdentity
ibVariables = _IbVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1)
)
_IbInventory_ObjectIdentity = ObjectIdentity
ibInventory = _IbInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1)
)
_InvTable_Object = MibTable
invTable = _InvTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    invTable.setStatus("current")
_InvEntry_Object = MibTableRow
invEntry = _InvEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1, 1)
)
invEntry.setIndexNames(
    (0, "MELLANOX-MIB", "invIndex"),
)
if mibBuilder.loadTexts:
    invEntry.setStatus("current")
_InvIndex_Type = Unsigned32
_InvIndex_Object = MibTableColumn
invIndex = _InvIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1, 1, 1),
    _InvIndex_Type()
)
invIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invIndex.setStatus("current")
_InvName_Type = OctetString
_InvName_Object = MibTableColumn
invName = _InvName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1, 1, 2),
    _InvName_Type()
)
invName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invName.setStatus("current")
_InvType_Type = OctetString
_InvType_Object = MibTableColumn
invType = _InvType_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1, 1, 3),
    _InvType_Type()
)
invType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invType.setStatus("current")
_InvPartNum_Type = OctetString
_InvPartNum_Object = MibTableColumn
invPartNum = _InvPartNum_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1, 1, 4),
    _InvPartNum_Type()
)
invPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPartNum.setStatus("current")
_InvSerialNum_Type = OctetString
_InvSerialNum_Object = MibTableColumn
invSerialNum = _InvSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1, 1, 5),
    _InvSerialNum_Type()
)
invSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSerialNum.setStatus("current")
_InvFirmware_Type = OctetString
_InvFirmware_Object = MibTableColumn
invFirmware = _InvFirmware_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1, 1, 6),
    _InvFirmware_Type()
)
invFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invFirmware.setStatus("current")
_InvHealthStatus_Type = OctetString
_InvHealthStatus_Object = MibTableColumn
invHealthStatus = _InvHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 1, 1, 1, 7),
    _InvHealthStatus_Type()
)
invHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invHealthStatus.setStatus("current")
_IbPorts_ObjectIdentity = ObjectIdentity
ibPorts = _IbPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2)
)
_CntTable_Object = MibTable
cntTable = _CntTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cntTable.setStatus("current")
_CntEntry_Object = MibTableRow
cntEntry = _CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1)
)
cntEntry.setIndexNames(
    (0, "MELLANOX-MIB", "cntIndex"),
)
if mibBuilder.loadTexts:
    cntEntry.setStatus("current")
_CntIndex_Type = Unsigned32
_CntIndex_Object = MibTableColumn
cntIndex = _CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 1),
    _CntIndex_Type()
)
cntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIndex.setStatus("current")
_CntName_Type = OctetString
_CntName_Object = MibTableColumn
cntName = _CntName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 2),
    _CntName_Type()
)
cntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntName.setStatus("current")
_CntPort_Type = Unsigned32
_CntPort_Object = MibTableColumn
cntPort = _CntPort_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 3),
    _CntPort_Type()
)
cntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPort.setStatus("current")
_CntPhyState_Type = OctetString
_CntPhyState_Object = MibTableColumn
cntPhyState = _CntPhyState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 4),
    _CntPhyState_Type()
)
cntPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPhyState.setStatus("current")
_CntLogState_Type = OctetString
_CntLogState_Object = MibTableColumn
cntLogState = _CntLogState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 5),
    _CntLogState_Type()
)
cntLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntLogState.setStatus("current")
_CntRate_Type = OctetString
_CntRate_Object = MibTableColumn
cntRate = _CntRate_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 6),
    _CntRate_Type()
)
cntRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRate.setStatus("current")
_CntMTU_Type = OctetString
_CntMTU_Object = MibTableColumn
cntMTU = _CntMTU_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 7),
    _CntMTU_Type()
)
cntMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMTU.setStatus("current")
_CntRcvData_Type = Counter64
_CntRcvData_Object = MibTableColumn
cntRcvData = _CntRcvData_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 8),
    _CntRcvData_Type()
)
cntRcvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvData.setStatus("current")
_CntRcvPkts_Type = Counter64
_CntRcvPkts_Object = MibTableColumn
cntRcvPkts = _CntRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 9),
    _CntRcvPkts_Type()
)
cntRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvPkts.setStatus("current")
_CntXmitData_Type = Counter64
_CntXmitData_Object = MibTableColumn
cntXmitData = _CntXmitData_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 10),
    _CntXmitData_Type()
)
cntXmitData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntXmitData.setStatus("current")
_CntXmitPkts_Type = Counter64
_CntXmitPkts_Object = MibTableColumn
cntXmitPkts = _CntXmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 11),
    _CntXmitPkts_Type()
)
cntXmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntXmitPkts.setStatus("current")
_CntRcvErr_Type = Counter64
_CntRcvErr_Object = MibTableColumn
cntRcvErr = _CntRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 12),
    _CntRcvErr_Type()
)
cntRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRcvErr.setStatus("current")
_CntXmitDiscard_Type = Counter64
_CntXmitDiscard_Object = MibTableColumn
cntXmitDiscard = _CntXmitDiscard_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 13),
    _CntXmitDiscard_Type()
)
cntXmitDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntXmitDiscard.setStatus("current")
_CntXmitWait_Type = Counter64
_CntXmitWait_Object = MibTableColumn
cntXmitWait = _CntXmitWait_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 14),
    _CntXmitWait_Type()
)
cntXmitWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntXmitWait.setStatus("current")
_CntSymErr_Type = Counter64
_CntSymErr_Object = MibTableColumn
cntSymErr = _CntSymErr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 15),
    _CntSymErr_Type()
)
cntSymErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSymErr.setStatus("current")
_CntVL15Drop_Type = Counter64
_CntVL15Drop_Object = MibTableColumn
cntVL15Drop = _CntVL15Drop_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 16),
    _CntVL15Drop_Type()
)
cntVL15Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntVL15Drop.setStatus("current")
_CntSpeed_Type = OctetString
_CntSpeed_Object = MibTableColumn
cntSpeed = _CntSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 17),
    _CntSpeed_Type()
)
cntSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSpeed.setStatus("current")
_CntWidth_Type = OctetString
_CntWidth_Object = MibTableColumn
cntWidth = _CntWidth_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 18),
    _CntWidth_Type()
)
cntWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntWidth.setStatus("current")
_CntOperationalVLs_Type = OctetString
_CntOperationalVLs_Object = MibTableColumn
cntOperationalVLs = _CntOperationalVLs_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 19),
    _CntOperationalVLs_Type()
)
cntOperationalVLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntOperationalVLs.setStatus("current")
_CntSupportedSpeeds_Type = OctetString
_CntSupportedSpeeds_Object = MibTableColumn
cntSupportedSpeeds = _CntSupportedSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 20),
    _CntSupportedSpeeds_Type()
)
cntSupportedSpeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSupportedSpeeds.setStatus("current")
_CntSupportedWidths_Type = OctetString
_CntSupportedWidths_Object = MibTableColumn
cntSupportedWidths = _CntSupportedWidths_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 21),
    _CntSupportedWidths_Type()
)
cntSupportedWidths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSupportedWidths.setStatus("current")
_CntMaxSupportedMTUs_Type = OctetString
_CntMaxSupportedMTUs_Object = MibTableColumn
cntMaxSupportedMTUs = _CntMaxSupportedMTUs_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 22),
    _CntMaxSupportedMTUs_Type()
)
cntMaxSupportedMTUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMaxSupportedMTUs.setStatus("current")
_CntVLCapabilities_Type = OctetString
_CntVLCapabilities_Object = MibTableColumn
cntVLCapabilities = _CntVLCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 23),
    _CntVLCapabilities_Type()
)
cntVLCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntVLCapabilities.setStatus("current")
_CntGUID_Type = OctetString
_CntGUID_Object = MibTableColumn
cntGUID = _CntGUID_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 24),
    _CntGUID_Type()
)
cntGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntGUID.setStatus("current")
_CntLID_Type = OctetString
_CntLID_Object = MibTableColumn
cntLID = _CntLID_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 1, 2, 1, 1, 25),
    _CntLID_Type()
)
cntLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntLID.setStatus("current")
_IbNotifications_ObjectIdentity = ObjectIdentity
ibNotifications = _IbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 2)
)
_SubnetMngr_ObjectIdentity = ObjectIdentity
subnetMngr = _SubnetMngr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 3)
)
_SmVariables_ObjectIdentity = ObjectIdentity
smVariables = _SmVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 3, 1)
)
_SmNotifications_ObjectIdentity = ObjectIdentity
smNotifications = _SmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 3, 2)
)
_BxBridge_ObjectIdentity = ObjectIdentity
bxBridge = _BxBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4)
)
_BxVariables_ObjectIdentity = ObjectIdentity
bxVariables = _BxVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1)
)
_BxInventory_ObjectIdentity = ObjectIdentity
bxInventory = _BxInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1)
)
_BxInvTable_Object = MibTable
bxInvTable = _BxInvTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bxInvTable.setStatus("current")
_BxInvEntry_Object = MibTableRow
bxInvEntry = _BxInvEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1, 1, 1)
)
bxInvEntry.setIndexNames(
    (0, "MELLANOX-MIB", "bxInvIndex"),
)
if mibBuilder.loadTexts:
    bxInvEntry.setStatus("current")
_BxInvIndex_Type = Unsigned32
_BxInvIndex_Object = MibTableColumn
bxInvIndex = _BxInvIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1, 1, 1, 1),
    _BxInvIndex_Type()
)
bxInvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bxInvIndex.setStatus("current")
_BxInvName_Type = OctetString
_BxInvName_Object = MibTableColumn
bxInvName = _BxInvName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1, 1, 1, 2),
    _BxInvName_Type()
)
bxInvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxInvName.setStatus("current")
_BxInvType_Type = OctetString
_BxInvType_Object = MibTableColumn
bxInvType = _BxInvType_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1, 1, 1, 3),
    _BxInvType_Type()
)
bxInvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxInvType.setStatus("current")
_BxInvPartNum_Type = OctetString
_BxInvPartNum_Object = MibTableColumn
bxInvPartNum = _BxInvPartNum_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1, 1, 1, 4),
    _BxInvPartNum_Type()
)
bxInvPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxInvPartNum.setStatus("current")
_BxInvSerialNum_Type = OctetString
_BxInvSerialNum_Object = MibTableColumn
bxInvSerialNum = _BxInvSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1, 1, 1, 5),
    _BxInvSerialNum_Type()
)
bxInvSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxInvSerialNum.setStatus("current")
_BxInvFirmware_Type = OctetString
_BxInvFirmware_Object = MibTableColumn
bxInvFirmware = _BxInvFirmware_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 1, 1, 1, 6),
    _BxInvFirmware_Type()
)
bxInvFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxInvFirmware.setStatus("current")
_BxIbPorts_ObjectIdentity = ObjectIdentity
bxIbPorts = _BxIbPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2)
)
_BxIbCntTable_Object = MibTable
bxIbCntTable = _BxIbCntTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bxIbCntTable.setStatus("current")
_BxIbCntEntry_Object = MibTableRow
bxIbCntEntry = _BxIbCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1)
)
bxIbCntEntry.setIndexNames(
    (0, "MELLANOX-MIB", "bxIbCntIndex"),
)
if mibBuilder.loadTexts:
    bxIbCntEntry.setStatus("current")
_BxIbCntIndex_Type = Unsigned32
_BxIbCntIndex_Object = MibTableColumn
bxIbCntIndex = _BxIbCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 1),
    _BxIbCntIndex_Type()
)
bxIbCntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bxIbCntIndex.setStatus("current")
_BxIbCntName_Type = OctetString
_BxIbCntName_Object = MibTableColumn
bxIbCntName = _BxIbCntName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 2),
    _BxIbCntName_Type()
)
bxIbCntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntName.setStatus("current")
_BxIbCntPort_Type = Unsigned32
_BxIbCntPort_Object = MibTableColumn
bxIbCntPort = _BxIbCntPort_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 3),
    _BxIbCntPort_Type()
)
bxIbCntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntPort.setStatus("current")
_BxIbCntLogState_Type = OctetString
_BxIbCntLogState_Object = MibTableColumn
bxIbCntLogState = _BxIbCntLogState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 4),
    _BxIbCntLogState_Type()
)
bxIbCntLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntLogState.setStatus("current")
_BxIbCntPhyState_Type = OctetString
_BxIbCntPhyState_Object = MibTableColumn
bxIbCntPhyState = _BxIbCntPhyState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 5),
    _BxIbCntPhyState_Type()
)
bxIbCntPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntPhyState.setStatus("current")
_BxIbCntRate_Type = OctetString
_BxIbCntRate_Object = MibTableColumn
bxIbCntRate = _BxIbCntRate_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 6),
    _BxIbCntRate_Type()
)
bxIbCntRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntRate.setStatus("current")
_BxIbCntSupportedSpeeds_Type = OctetString
_BxIbCntSupportedSpeeds_Object = MibTableColumn
bxIbCntSupportedSpeeds = _BxIbCntSupportedSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 7),
    _BxIbCntSupportedSpeeds_Type()
)
bxIbCntSupportedSpeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntSupportedSpeeds.setStatus("current")
_BxIbCntSpeed_Type = OctetString
_BxIbCntSpeed_Object = MibTableColumn
bxIbCntSpeed = _BxIbCntSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 8),
    _BxIbCntSpeed_Type()
)
bxIbCntSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntSpeed.setStatus("current")
_BxIbCntSupportedWidths_Type = OctetString
_BxIbCntSupportedWidths_Object = MibTableColumn
bxIbCntSupportedWidths = _BxIbCntSupportedWidths_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 9),
    _BxIbCntSupportedWidths_Type()
)
bxIbCntSupportedWidths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntSupportedWidths.setStatus("current")
_BxIbCntWidth_Type = OctetString
_BxIbCntWidth_Object = MibTableColumn
bxIbCntWidth = _BxIbCntWidth_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 10),
    _BxIbCntWidth_Type()
)
bxIbCntWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntWidth.setStatus("current")
_BxIbCntMaxSupportedMTUs_Type = OctetString
_BxIbCntMaxSupportedMTUs_Object = MibTableColumn
bxIbCntMaxSupportedMTUs = _BxIbCntMaxSupportedMTUs_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 11),
    _BxIbCntMaxSupportedMTUs_Type()
)
bxIbCntMaxSupportedMTUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntMaxSupportedMTUs.setStatus("current")
_BxIbCntMTU_Type = OctetString
_BxIbCntMTU_Object = MibTableColumn
bxIbCntMTU = _BxIbCntMTU_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 12),
    _BxIbCntMTU_Type()
)
bxIbCntMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntMTU.setStatus("current")
_BxIbCntVLCapabilities_Type = OctetString
_BxIbCntVLCapabilities_Object = MibTableColumn
bxIbCntVLCapabilities = _BxIbCntVLCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 13),
    _BxIbCntVLCapabilities_Type()
)
bxIbCntVLCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntVLCapabilities.setStatus("current")
_BxIbCntOperationalVLs_Type = OctetString
_BxIbCntOperationalVLs_Object = MibTableColumn
bxIbCntOperationalVLs = _BxIbCntOperationalVLs_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 14),
    _BxIbCntOperationalVLs_Type()
)
bxIbCntOperationalVLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntOperationalVLs.setStatus("current")
_BxIbCntGUID_Type = OctetString
_BxIbCntGUID_Object = MibTableColumn
bxIbCntGUID = _BxIbCntGUID_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 15),
    _BxIbCntGUID_Type()
)
bxIbCntGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntGUID.setStatus("current")
_BxIbCntLID_Type = OctetString
_BxIbCntLID_Object = MibTableColumn
bxIbCntLID = _BxIbCntLID_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 16),
    _BxIbCntLID_Type()
)
bxIbCntLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntLID.setStatus("current")
_BxIbCntRcvPkts_Type = Counter64
_BxIbCntRcvPkts_Object = MibTableColumn
bxIbCntRcvPkts = _BxIbCntRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 17),
    _BxIbCntRcvPkts_Type()
)
bxIbCntRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntRcvPkts.setStatus("current")
_BxIbCntRcvData_Type = Counter64
_BxIbCntRcvData_Object = MibTableColumn
bxIbCntRcvData = _BxIbCntRcvData_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 18),
    _BxIbCntRcvData_Type()
)
bxIbCntRcvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntRcvData.setStatus("current")
_BxIbCntRcvErr_Type = Counter64
_BxIbCntRcvErr_Object = MibTableColumn
bxIbCntRcvErr = _BxIbCntRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 19),
    _BxIbCntRcvErr_Type()
)
bxIbCntRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntRcvErr.setStatus("current")
_BxIbCntSymErr_Type = Counter64
_BxIbCntSymErr_Object = MibTableColumn
bxIbCntSymErr = _BxIbCntSymErr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 20),
    _BxIbCntSymErr_Type()
)
bxIbCntSymErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntSymErr.setStatus("current")
_BxIbCntVL15Drop_Type = Counter64
_BxIbCntVL15Drop_Object = MibTableColumn
bxIbCntVL15Drop = _BxIbCntVL15Drop_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 21),
    _BxIbCntVL15Drop_Type()
)
bxIbCntVL15Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntVL15Drop.setStatus("current")
_BxIbCntXmitPkts_Type = Counter64
_BxIbCntXmitPkts_Object = MibTableColumn
bxIbCntXmitPkts = _BxIbCntXmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 22),
    _BxIbCntXmitPkts_Type()
)
bxIbCntXmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntXmitPkts.setStatus("current")
_BxIbCntXmitData_Type = Counter64
_BxIbCntXmitData_Object = MibTableColumn
bxIbCntXmitData = _BxIbCntXmitData_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 23),
    _BxIbCntXmitData_Type()
)
bxIbCntXmitData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntXmitData.setStatus("current")
_BxIbCntXmitWaits_Type = Counter64
_BxIbCntXmitWaits_Object = MibTableColumn
bxIbCntXmitWaits = _BxIbCntXmitWaits_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 24),
    _BxIbCntXmitWaits_Type()
)
bxIbCntXmitWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntXmitWaits.setStatus("current")
_BxIbCntXmitDiscards_Type = Counter64
_BxIbCntXmitDiscards_Object = MibTableColumn
bxIbCntXmitDiscards = _BxIbCntXmitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 2, 1, 1, 25),
    _BxIbCntXmitDiscards_Type()
)
bxIbCntXmitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxIbCntXmitDiscards.setStatus("current")
_BxEthPorts_ObjectIdentity = ObjectIdentity
bxEthPorts = _BxEthPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3)
)
_BxEthCntTable_Object = MibTable
bxEthCntTable = _BxEthCntTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bxEthCntTable.setStatus("current")
_BxEthCntEntry_Object = MibTableRow
bxEthCntEntry = _BxEthCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1)
)
bxEthCntEntry.setIndexNames(
    (0, "MELLANOX-MIB", "bxEthCntIndex"),
)
if mibBuilder.loadTexts:
    bxEthCntEntry.setStatus("current")
_BxEthCntIndex_Type = Unsigned32
_BxEthCntIndex_Object = MibTableColumn
bxEthCntIndex = _BxEthCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 1),
    _BxEthCntIndex_Type()
)
bxEthCntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bxEthCntIndex.setStatus("current")
_BxEthCntName_Type = OctetString
_BxEthCntName_Object = MibTableColumn
bxEthCntName = _BxEthCntName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 2),
    _BxEthCntName_Type()
)
bxEthCntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntName.setStatus("current")
_BxEthCntAdminMode_Type = OctetString
_BxEthCntAdminMode_Object = MibTableColumn
bxEthCntAdminMode = _BxEthCntAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 3),
    _BxEthCntAdminMode_Type()
)
bxEthCntAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntAdminMode.setStatus("current")
_BxEthCntStatus_Type = OctetString
_BxEthCntStatus_Object = MibTableColumn
bxEthCntStatus = _BxEthCntStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 4),
    _BxEthCntStatus_Type()
)
bxEthCntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntStatus.setStatus("current")
_BxEthCntSupportedSpeeds_Type = OctetString
_BxEthCntSupportedSpeeds_Object = MibTableColumn
bxEthCntSupportedSpeeds = _BxEthCntSupportedSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 5),
    _BxEthCntSupportedSpeeds_Type()
)
bxEthCntSupportedSpeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntSupportedSpeeds.setStatus("current")
_BxEthCntSpeed_Type = OctetString
_BxEthCntSpeed_Object = MibTableColumn
bxEthCntSpeed = _BxEthCntSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 6),
    _BxEthCntSpeed_Type()
)
bxEthCntSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntSpeed.setStatus("current")
_BxEthCntDuplex_Type = OctetString
_BxEthCntDuplex_Object = MibTableColumn
bxEthCntDuplex = _BxEthCntDuplex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 7),
    _BxEthCntDuplex_Type()
)
bxEthCntDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntDuplex.setStatus("current")
_BxEthCntMTU_Type = OctetString
_BxEthCntMTU_Object = MibTableColumn
bxEthCntMTU = _BxEthCntMTU_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 8),
    _BxEthCntMTU_Type()
)
bxEthCntMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntMTU.setStatus("current")
_BxEthCntFlowcontrolStatus_Type = OctetString
_BxEthCntFlowcontrolStatus_Object = MibTableColumn
bxEthCntFlowcontrolStatus = _BxEthCntFlowcontrolStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 9),
    _BxEthCntFlowcontrolStatus_Type()
)
bxEthCntFlowcontrolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntFlowcontrolStatus.setStatus("current")
_BxEthCntFlowcontrolMode_Type = OctetString
_BxEthCntFlowcontrolMode_Object = MibTableColumn
bxEthCntFlowcontrolMode = _BxEthCntFlowcontrolMode_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 10),
    _BxEthCntFlowcontrolMode_Type()
)
bxEthCntFlowcontrolMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntFlowcontrolMode.setStatus("current")
_BxEthCntFlowcontrolPriorities_Type = OctetString
_BxEthCntFlowcontrolPriorities_Object = MibTableColumn
bxEthCntFlowcontrolPriorities = _BxEthCntFlowcontrolPriorities_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 11),
    _BxEthCntFlowcontrolPriorities_Type()
)
bxEthCntFlowcontrolPriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntFlowcontrolPriorities.setStatus("current")
_BxEthCntRcvPkts_Type = Counter64
_BxEthCntRcvPkts_Object = MibTableColumn
bxEthCntRcvPkts = _BxEthCntRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 12),
    _BxEthCntRcvPkts_Type()
)
bxEthCntRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvPkts.setStatus("current")
_BxEthCntRcvUcastPkts_Type = Counter64
_BxEthCntRcvUcastPkts_Object = MibTableColumn
bxEthCntRcvUcastPkts = _BxEthCntRcvUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 13),
    _BxEthCntRcvUcastPkts_Type()
)
bxEthCntRcvUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvUcastPkts.setStatus("current")
_BxEthCntRcvMcatsPkts_Type = Counter64
_BxEthCntRcvMcatsPkts_Object = MibTableColumn
bxEthCntRcvMcatsPkts = _BxEthCntRcvMcatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 14),
    _BxEthCntRcvMcatsPkts_Type()
)
bxEthCntRcvMcatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvMcatsPkts.setStatus("current")
_BxEthCntRcvBcastPkts_Type = Counter64
_BxEthCntRcvBcastPkts_Object = MibTableColumn
bxEthCntRcvBcastPkts = _BxEthCntRcvBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 15),
    _BxEthCntRcvBcastPkts_Type()
)
bxEthCntRcvBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvBcastPkts.setStatus("current")
_BxEthCntRcvJumboPkts_Type = Counter64
_BxEthCntRcvJumboPkts_Object = MibTableColumn
bxEthCntRcvJumboPkts = _BxEthCntRcvJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 16),
    _BxEthCntRcvJumboPkts_Type()
)
bxEthCntRcvJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvJumboPkts.setStatus("current")
_BxEthCntRcvData_Type = Counter64
_BxEthCntRcvData_Object = MibTableColumn
bxEthCntRcvData = _BxEthCntRcvData_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 17),
    _BxEthCntRcvData_Type()
)
bxEthCntRcvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvData.setStatus("current")
_BxEthCntRcvErr_Type = Counter64
_BxEthCntRcvErr_Object = MibTableColumn
bxEthCntRcvErr = _BxEthCntRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 18),
    _BxEthCntRcvErr_Type()
)
bxEthCntRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvErr.setStatus("current")
_BxEthCntRcvNoBuffer_Type = Counter64
_BxEthCntRcvNoBuffer_Object = MibTableColumn
bxEthCntRcvNoBuffer = _BxEthCntRcvNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 19),
    _BxEthCntRcvNoBuffer_Type()
)
bxEthCntRcvNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvNoBuffer.setStatus("current")
_BxEthCntRcvRunt_Type = Counter64
_BxEthCntRcvRunt_Object = MibTableColumn
bxEthCntRcvRunt = _BxEthCntRcvRunt_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 20),
    _BxEthCntRcvRunt_Type()
)
bxEthCntRcvRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvRunt.setStatus("current")
_BxEthCntRcvCRC_Type = Counter64
_BxEthCntRcvCRC_Object = MibTableColumn
bxEthCntRcvCRC = _BxEthCntRcvCRC_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 21),
    _BxEthCntRcvCRC_Type()
)
bxEthCntRcvCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntRcvCRC.setStatus("current")
_BxEthCntXmitPkts_Type = Counter64
_BxEthCntXmitPkts_Object = MibTableColumn
bxEthCntXmitPkts = _BxEthCntXmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 22),
    _BxEthCntXmitPkts_Type()
)
bxEthCntXmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntXmitPkts.setStatus("current")
_BxEthCntXmitUcastPkts_Type = Counter64
_BxEthCntXmitUcastPkts_Object = MibTableColumn
bxEthCntXmitUcastPkts = _BxEthCntXmitUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 23),
    _BxEthCntXmitUcastPkts_Type()
)
bxEthCntXmitUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntXmitUcastPkts.setStatus("current")
_BxEthCntXmitMcastPkts_Type = Counter64
_BxEthCntXmitMcastPkts_Object = MibTableColumn
bxEthCntXmitMcastPkts = _BxEthCntXmitMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 24),
    _BxEthCntXmitMcastPkts_Type()
)
bxEthCntXmitMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntXmitMcastPkts.setStatus("current")
_BxEthCntXmitBcastPkts_Type = Counter64
_BxEthCntXmitBcastPkts_Object = MibTableColumn
bxEthCntXmitBcastPkts = _BxEthCntXmitBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 25),
    _BxEthCntXmitBcastPkts_Type()
)
bxEthCntXmitBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntXmitBcastPkts.setStatus("current")
_BxEthCntXmitJumboPkts_Type = Counter64
_BxEthCntXmitJumboPkts_Object = MibTableColumn
bxEthCntXmitJumboPkts = _BxEthCntXmitJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 26),
    _BxEthCntXmitJumboPkts_Type()
)
bxEthCntXmitJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntXmitJumboPkts.setStatus("current")
_BxEthCntXmitData_Type = Counter64
_BxEthCntXmitData_Object = MibTableColumn
bxEthCntXmitData = _BxEthCntXmitData_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 27),
    _BxEthCntXmitData_Type()
)
bxEthCntXmitData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntXmitData.setStatus("current")
_BxEthCntXmitErr_Type = Counter64
_BxEthCntXmitErr_Object = MibTableColumn
bxEthCntXmitErr = _BxEthCntXmitErr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 3, 1, 1, 28),
    _BxEthCntXmitErr_Type()
)
bxEthCntXmitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxEthCntXmitErr.setStatus("current")
_BxFcPorts_ObjectIdentity = ObjectIdentity
bxFcPorts = _BxFcPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4)
)
_BxFcCntTable_Object = MibTable
bxFcCntTable = _BxFcCntTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bxFcCntTable.setStatus("current")
_BxFcCntEntry_Object = MibTableRow
bxFcCntEntry = _BxFcCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1)
)
bxFcCntEntry.setIndexNames(
    (0, "MELLANOX-MIB", "bxFcCntIndex"),
)
if mibBuilder.loadTexts:
    bxFcCntEntry.setStatus("current")
_BxFcCntIndex_Type = Unsigned32
_BxFcCntIndex_Object = MibTableColumn
bxFcCntIndex = _BxFcCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 1),
    _BxFcCntIndex_Type()
)
bxFcCntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bxFcCntIndex.setStatus("current")
_BxFcCntName_Type = OctetString
_BxFcCntName_Object = MibTableColumn
bxFcCntName = _BxFcCntName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 2),
    _BxFcCntName_Type()
)
bxFcCntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntName.setStatus("current")
_BxFcCntAdminMode_Type = OctetString
_BxFcCntAdminMode_Object = MibTableColumn
bxFcCntAdminMode = _BxFcCntAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 3),
    _BxFcCntAdminMode_Type()
)
bxFcCntAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntAdminMode.setStatus("current")
_BxFcCntStatus_Type = OctetString
_BxFcCntStatus_Object = MibTableColumn
bxFcCntStatus = _BxFcCntStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 4),
    _BxFcCntStatus_Type()
)
bxFcCntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntStatus.setStatus("current")
_BxFcCntSupportedSpeeds_Type = OctetString
_BxFcCntSupportedSpeeds_Object = MibTableColumn
bxFcCntSupportedSpeeds = _BxFcCntSupportedSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 5),
    _BxFcCntSupportedSpeeds_Type()
)
bxFcCntSupportedSpeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntSupportedSpeeds.setStatus("current")
_BxFcCntSpeed_Type = OctetString
_BxFcCntSpeed_Object = MibTableColumn
bxFcCntSpeed = _BxFcCntSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 6),
    _BxFcCntSpeed_Type()
)
bxFcCntSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntSpeed.setStatus("current")
_BxFcCntWWPN_Type = OctetString
_BxFcCntWWPN_Object = MibTableColumn
bxFcCntWWPN = _BxFcCntWWPN_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 7),
    _BxFcCntWWPN_Type()
)
bxFcCntWWPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntWWPN.setStatus("current")
_BxFcCntFCID_Type = OctetString
_BxFcCntFCID_Object = MibTableColumn
bxFcCntFCID = _BxFcCntFCID_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 8),
    _BxFcCntFCID_Type()
)
bxFcCntFCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntFCID.setStatus("current")
_BxFcCntRcvCreditsAlloc_Type = OctetString
_BxFcCntRcvCreditsAlloc_Object = MibTableColumn
bxFcCntRcvCreditsAlloc = _BxFcCntRcvCreditsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 9),
    _BxFcCntRcvCreditsAlloc_Type()
)
bxFcCntRcvCreditsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvCreditsAlloc.setStatus("current")
_BxFcCntXmitCreditsAlloc_Type = OctetString
_BxFcCntXmitCreditsAlloc_Object = MibTableColumn
bxFcCntXmitCreditsAlloc = _BxFcCntXmitCreditsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 10),
    _BxFcCntXmitCreditsAlloc_Type()
)
bxFcCntXmitCreditsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitCreditsAlloc.setStatus("current")
_BxFcCntRcvPkts_Type = Counter64
_BxFcCntRcvPkts_Object = MibTableColumn
bxFcCntRcvPkts = _BxFcCntRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 11),
    _BxFcCntRcvPkts_Type()
)
bxFcCntRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvPkts.setStatus("current")
_BxFcCntRcvData_Type = Counter64
_BxFcCntRcvData_Object = MibTableColumn
bxFcCntRcvData = _BxFcCntRcvData_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 12),
    _BxFcCntRcvData_Type()
)
bxFcCntRcvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvData.setStatus("current")
_BxFcCntRcvDiscards_Type = Counter64
_BxFcCntRcvDiscards_Object = MibTableColumn
bxFcCntRcvDiscards = _BxFcCntRcvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 13),
    _BxFcCntRcvDiscards_Type()
)
bxFcCntRcvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvDiscards.setStatus("current")
_BxFcCntRcvErr_Type = Counter64
_BxFcCntRcvErr_Object = MibTableColumn
bxFcCntRcvErr = _BxFcCntRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 14),
    _BxFcCntRcvErr_Type()
)
bxFcCntRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvErr.setStatus("current")
_BxFcCntRcvCRC_Type = Counter64
_BxFcCntRcvCRC_Object = MibTableColumn
bxFcCntRcvCRC = _BxFcCntRcvCRC_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 15),
    _BxFcCntRcvCRC_Type()
)
bxFcCntRcvCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvCRC.setStatus("current")
_BxFcCntRcvUnknown_Type = Counter64
_BxFcCntRcvUnknown_Object = MibTableColumn
bxFcCntRcvUnknown = _BxFcCntRcvUnknown_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 16),
    _BxFcCntRcvUnknown_Type()
)
bxFcCntRcvUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvUnknown.setStatus("current")
_BxFcCntRcvLong_Type = Counter64
_BxFcCntRcvLong_Object = MibTableColumn
bxFcCntRcvLong = _BxFcCntRcvLong_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 17),
    _BxFcCntRcvLong_Type()
)
bxFcCntRcvLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvLong.setStatus("current")
_BxFcCntRcvShort_Type = Counter64
_BxFcCntRcvShort_Object = MibTableColumn
bxFcCntRcvShort = _BxFcCntRcvShort_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 18),
    _BxFcCntRcvShort_Type()
)
bxFcCntRcvShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvShort.setStatus("current")
_BxFcCntRcvOffline_Type = Counter64
_BxFcCntRcvOffline_Object = MibTableColumn
bxFcCntRcvOffline = _BxFcCntRcvOffline_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 19),
    _BxFcCntRcvOffline_Type()
)
bxFcCntRcvOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvOffline.setStatus("current")
_BxFcCntRcvLinkReset_Type = Counter64
_BxFcCntRcvLinkReset_Object = MibTableColumn
bxFcCntRcvLinkReset = _BxFcCntRcvLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 20),
    _BxFcCntRcvLinkReset_Type()
)
bxFcCntRcvLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvLinkReset.setStatus("current")
_BxFcCntRcvNonOperational_Type = Counter64
_BxFcCntRcvNonOperational_Object = MibTableColumn
bxFcCntRcvNonOperational = _BxFcCntRcvNonOperational_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 21),
    _BxFcCntRcvNonOperational_Type()
)
bxFcCntRcvNonOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvNonOperational.setStatus("current")
_BxFcCntRcvRemainCredits_Type = Counter64
_BxFcCntRcvRemainCredits_Object = MibTableColumn
bxFcCntRcvRemainCredits = _BxFcCntRcvRemainCredits_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 22),
    _BxFcCntRcvRemainCredits_Type()
)
bxFcCntRcvRemainCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntRcvRemainCredits.setStatus("current")
_BxFcCntXmitPkts_Type = Counter64
_BxFcCntXmitPkts_Object = MibTableColumn
bxFcCntXmitPkts = _BxFcCntXmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 23),
    _BxFcCntXmitPkts_Type()
)
bxFcCntXmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitPkts.setStatus("current")
_BxFcCntXmitData_Type = Counter64
_BxFcCntXmitData_Object = MibTableColumn
bxFcCntXmitData = _BxFcCntXmitData_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 24),
    _BxFcCntXmitData_Type()
)
bxFcCntXmitData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitData.setStatus("current")
_BxFcCntXmitDiscards_Type = Counter64
_BxFcCntXmitDiscards_Object = MibTableColumn
bxFcCntXmitDiscards = _BxFcCntXmitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 25),
    _BxFcCntXmitDiscards_Type()
)
bxFcCntXmitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitDiscards.setStatus("current")
_BxFcCntXmitErr_Type = Counter64
_BxFcCntXmitErr_Object = MibTableColumn
bxFcCntXmitErr = _BxFcCntXmitErr_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 26),
    _BxFcCntXmitErr_Type()
)
bxFcCntXmitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitErr.setStatus("current")
_BxFcCntXmitOffline_Type = Counter64
_BxFcCntXmitOffline_Object = MibTableColumn
bxFcCntXmitOffline = _BxFcCntXmitOffline_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 27),
    _BxFcCntXmitOffline_Type()
)
bxFcCntXmitOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitOffline.setStatus("current")
_BxFcCntXmitLinkReset_Type = Counter64
_BxFcCntXmitLinkReset_Object = MibTableColumn
bxFcCntXmitLinkReset = _BxFcCntXmitLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 28),
    _BxFcCntXmitLinkReset_Type()
)
bxFcCntXmitLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitLinkReset.setStatus("current")
_BxFcCntXmitNonOperational_Type = Counter64
_BxFcCntXmitNonOperational_Object = MibTableColumn
bxFcCntXmitNonOperational = _BxFcCntXmitNonOperational_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 29),
    _BxFcCntXmitNonOperational_Type()
)
bxFcCntXmitNonOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitNonOperational.setStatus("current")
_BxFcCntXmitRemainCredits_Type = Counter64
_BxFcCntXmitRemainCredits_Object = MibTableColumn
bxFcCntXmitRemainCredits = _BxFcCntXmitRemainCredits_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 1, 4, 1, 1, 30),
    _BxFcCntXmitRemainCredits_Type()
)
bxFcCntXmitRemainCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bxFcCntXmitRemainCredits.setStatus("current")
_BxNotifications_ObjectIdentity = ObjectIdentity
bxNotifications = _BxNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 2)
)
_MlxIBObjects_ObjectIdentity = ObjectIdentity
mlxIBObjects = _MlxIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5)
)
_MlxIBCAInfoGroup_ObjectIdentity = ObjectIdentity
mlxIBCAInfoGroup = _MlxIBCAInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1)
)
_MlxIBCAInfoTableNumCAs_Type = Unsigned32
_MlxIBCAInfoTableNumCAs_Object = MibScalar
mlxIBCAInfoTableNumCAs = _MlxIBCAInfoTableNumCAs_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 1),
    _MlxIBCAInfoTableNumCAs_Type()
)
mlxIBCAInfoTableNumCAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAInfoTableNumCAs.setStatus("current")
_MlxIBCAInfoTable_Object = MibTable
mlxIBCAInfoTable = _MlxIBCAInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    mlxIBCAInfoTable.setStatus("current")
_MlxIBCAInfoEntry_Object = MibTableRow
mlxIBCAInfoEntry = _MlxIBCAInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1)
)
mlxIBCAInfoEntry.setIndexNames(
    (0, "MELLANOX-MIB", "mlxIBCAIndex"),
)
if mibBuilder.loadTexts:
    mlxIBCAInfoEntry.setStatus("current")
_MlxIBCAIndex_Type = Unsigned32
_MlxIBCAIndex_Object = MibTableColumn
mlxIBCAIndex = _MlxIBCAIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 1),
    _MlxIBCAIndex_Type()
)
mlxIBCAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mlxIBCAIndex.setStatus("current")


class _MlxIBCADeviceName_Type(OctetString):
    """Custom type mlxIBCADeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MlxIBCADeviceName_Type.__name__ = "OctetString"
_MlxIBCADeviceName_Object = MibTableColumn
mlxIBCADeviceName = _MlxIBCADeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 2),
    _MlxIBCADeviceName_Type()
)
mlxIBCADeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCADeviceName.setStatus("current")
_MlxIBCAPCIDomain_Type = Unsigned32
_MlxIBCAPCIDomain_Object = MibTableColumn
mlxIBCAPCIDomain = _MlxIBCAPCIDomain_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 3),
    _MlxIBCAPCIDomain_Type()
)
mlxIBCAPCIDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAPCIDomain.setStatus("current")
_MlxIBCAPCIBus_Type = Unsigned32
_MlxIBCAPCIBus_Object = MibTableColumn
mlxIBCAPCIBus = _MlxIBCAPCIBus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 4),
    _MlxIBCAPCIBus_Type()
)
mlxIBCAPCIBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAPCIBus.setStatus("current")
_MlxIBCAPCISlot_Type = Unsigned32
_MlxIBCAPCISlot_Object = MibTableColumn
mlxIBCAPCISlot = _MlxIBCAPCISlot_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 5),
    _MlxIBCAPCISlot_Type()
)
mlxIBCAPCISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAPCISlot.setStatus("current")
_MlxIBCAPCIFunction_Type = Unsigned32
_MlxIBCAPCIFunction_Object = MibTableColumn
mlxIBCAPCIFunction = _MlxIBCAPCIFunction_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 6),
    _MlxIBCAPCIFunction_Type()
)
mlxIBCAPCIFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAPCIFunction.setStatus("current")
_MlxIBCAPCIPhysicalSlot_Type = Integer32
_MlxIBCAPCIPhysicalSlot_Object = MibTableColumn
mlxIBCAPCIPhysicalSlot = _MlxIBCAPCIPhysicalSlot_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 7),
    _MlxIBCAPCIPhysicalSlot_Type()
)
mlxIBCAPCIPhysicalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAPCIPhysicalSlot.setStatus("current")
_MlxIBCAIrq_Type = Unsigned32
_MlxIBCAIrq_Object = MibTableColumn
mlxIBCAIrq = _MlxIBCAIrq_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 8),
    _MlxIBCAIrq_Type()
)
mlxIBCAIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAIrq.setStatus("current")


class _MlxIBCAModelString_Type(OctetString):
    """Custom type mlxIBCAModelString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MlxIBCAModelString_Type.__name__ = "OctetString"
_MlxIBCAModelString_Object = MibTableColumn
mlxIBCAModelString = _MlxIBCAModelString_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 9),
    _MlxIBCAModelString_Type()
)
mlxIBCAModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAModelString.setStatus("current")


class _MlxIBCASerialNumber_Type(OctetString):
    """Custom type mlxIBCASerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MlxIBCASerialNumber_Type.__name__ = "OctetString"
_MlxIBCASerialNumber_Object = MibTableColumn
mlxIBCASerialNumber = _MlxIBCASerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 10),
    _MlxIBCASerialNumber_Type()
)
mlxIBCASerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCASerialNumber.setStatus("current")


class _MlxIBCAPartNumber_Type(OctetString):
    """Custom type mlxIBCAPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MlxIBCAPartNumber_Type.__name__ = "OctetString"
_MlxIBCAPartNumber_Object = MibTableColumn
mlxIBCAPartNumber = _MlxIBCAPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 11),
    _MlxIBCAPartNumber_Type()
)
mlxIBCAPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAPartNumber.setStatus("current")
_MlxIBCANodeGUID_Type = IbGuid
_MlxIBCANodeGUID_Object = MibTableColumn
mlxIBCANodeGUID = _MlxIBCANodeGUID_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 12),
    _MlxIBCANodeGUID_Type()
)
mlxIBCANodeGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCANodeGUID.setStatus("current")
_MlxIBCASystemImageGUID_Type = IbGuid
_MlxIBCASystemImageGUID_Object = MibTableColumn
mlxIBCASystemImageGUID = _MlxIBCASystemImageGUID_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 13),
    _MlxIBCASystemImageGUID_Type()
)
mlxIBCASystemImageGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCASystemImageGUID.setStatus("current")


class _MlxIBCAFirmwareVersion_Type(OctetString):
    """Custom type mlxIBCAFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MlxIBCAFirmwareVersion_Type.__name__ = "OctetString"
_MlxIBCAFirmwareVersion_Object = MibTableColumn
mlxIBCAFirmwareVersion = _MlxIBCAFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 14),
    _MlxIBCAFirmwareVersion_Type()
)
mlxIBCAFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAFirmwareVersion.setStatus("current")


class _MlxIBCAHardwareVersion_Type(OctetString):
    """Custom type mlxIBCAHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MlxIBCAHardwareVersion_Type.__name__ = "OctetString"
_MlxIBCAHardwareVersion_Object = MibTableColumn
mlxIBCAHardwareVersion = _MlxIBCAHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 15),
    _MlxIBCAHardwareVersion_Type()
)
mlxIBCAHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAHardwareVersion.setStatus("current")


class _MlxIBCAHealthStatus_Type(Integer32):
    """Custom type mlxIBCAHealthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("healthy", 1),
          ("unhealthy", 0))
    )


_MlxIBCAHealthStatus_Type.__name__ = "Integer32"
_MlxIBCAHealthStatus_Object = MibTableColumn
mlxIBCAHealthStatus = _MlxIBCAHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 16),
    _MlxIBCAHealthStatus_Type()
)
mlxIBCAHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAHealthStatus.setStatus("current")


class _MlxIBCANumPorts_Type(Unsigned32):
    """Custom type mlxIBCANumPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_MlxIBCANumPorts_Type.__name__ = "Unsigned32"
_MlxIBCANumPorts_Object = MibTableColumn
mlxIBCANumPorts = _MlxIBCANumPorts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 17),
    _MlxIBCANumPorts_Type()
)
mlxIBCANumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCANumPorts.setStatus("current")


class _MlxIBCAType_Type(Integer32):
    """Custom type mlxIBCAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hca", 2),
          ("tca", 3),
          ("unknown", 1))
    )


_MlxIBCAType_Type.__name__ = "Integer32"
_MlxIBCAType_Object = MibTableColumn
mlxIBCAType = _MlxIBCAType_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 1, 2, 1, 18),
    _MlxIBCAType_Type()
)
mlxIBCAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBCAType.setStatus("current")
_MlxIBSwitchInfoGroup_ObjectIdentity = ObjectIdentity
mlxIBSwitchInfoGroup = _MlxIBSwitchInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 2)
)
_MlxIBSwitchInfoTableNumSwitches_Type = Unsigned32
_MlxIBSwitchInfoTableNumSwitches_Object = MibScalar
mlxIBSwitchInfoTableNumSwitches = _MlxIBSwitchInfoTableNumSwitches_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 2, 1),
    _MlxIBSwitchInfoTableNumSwitches_Type()
)
mlxIBSwitchInfoTableNumSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBSwitchInfoTableNumSwitches.setStatus("current")
_MlxIBSwitchInfoTable_Object = MibTable
mlxIBSwitchInfoTable = _MlxIBSwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    mlxIBSwitchInfoTable.setStatus("current")
_MlxIBSwitchInfoEntry_Object = MibTableRow
mlxIBSwitchInfoEntry = _MlxIBSwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 2, 2, 1)
)
mlxIBSwitchInfoEntry.setIndexNames(
    (0, "MELLANOX-MIB", "mlxIBSwitchIndex"),
)
if mibBuilder.loadTexts:
    mlxIBSwitchInfoEntry.setStatus("current")
_MlxIBSwitchIndex_Type = Unsigned32
_MlxIBSwitchIndex_Object = MibTableColumn
mlxIBSwitchIndex = _MlxIBSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 2, 2, 1, 1),
    _MlxIBSwitchIndex_Type()
)
mlxIBSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mlxIBSwitchIndex.setStatus("current")
_MlxIBRouterInfoGroup_ObjectIdentity = ObjectIdentity
mlxIBRouterInfoGroup = _MlxIBRouterInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 3)
)
_MlxIBRouterInfoTableNumRouters_Type = Unsigned32
_MlxIBRouterInfoTableNumRouters_Object = MibScalar
mlxIBRouterInfoTableNumRouters = _MlxIBRouterInfoTableNumRouters_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 3, 1),
    _MlxIBRouterInfoTableNumRouters_Type()
)
mlxIBRouterInfoTableNumRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBRouterInfoTableNumRouters.setStatus("current")
_MlxIBRouterInfoTable_Object = MibTable
mlxIBRouterInfoTable = _MlxIBRouterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    mlxIBRouterInfoTable.setStatus("current")
_MlxIBRouterInfoEntry_Object = MibTableRow
mlxIBRouterInfoEntry = _MlxIBRouterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 3, 2, 1)
)
mlxIBRouterInfoEntry.setIndexNames(
    (0, "MELLANOX-MIB", "mlxIBRouterIndex"),
)
if mibBuilder.loadTexts:
    mlxIBRouterInfoEntry.setStatus("current")
_MlxIBRouterIndex_Type = Unsigned32
_MlxIBRouterIndex_Object = MibTableColumn
mlxIBRouterIndex = _MlxIBRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 3, 2, 1, 1),
    _MlxIBRouterIndex_Type()
)
mlxIBRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mlxIBRouterIndex.setStatus("current")
_MlxIBPortInfoGroup_ObjectIdentity = ObjectIdentity
mlxIBPortInfoGroup = _MlxIBPortInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4)
)
_MlxIBPortInfoTableNumPorts_Type = Unsigned32
_MlxIBPortInfoTableNumPorts_Object = MibScalar
mlxIBPortInfoTableNumPorts = _MlxIBPortInfoTableNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 1),
    _MlxIBPortInfoTableNumPorts_Type()
)
mlxIBPortInfoTableNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBPortInfoTableNumPorts.setStatus("current")
_MlxIBPortInfoTable_Object = MibTable
mlxIBPortInfoTable = _MlxIBPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2)
)
if mibBuilder.loadTexts:
    mlxIBPortInfoTable.setStatus("current")
_MlxIBPortInfoEntry_Object = MibTableRow
mlxIBPortInfoEntry = _MlxIBPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2, 1)
)
mlxIBPortInfoEntry.setIndexNames(
    (0, "MELLANOX-MIB", "mlxIBPortIndex"),
)
if mibBuilder.loadTexts:
    mlxIBPortInfoEntry.setStatus("current")
_MlxIBPortIndex_Type = Unsigned32
_MlxIBPortIndex_Object = MibTableColumn
mlxIBPortIndex = _MlxIBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2, 1, 1),
    _MlxIBPortIndex_Type()
)
mlxIBPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mlxIBPortIndex.setStatus("current")


class _MlxIBPortLocalPortNumber_Type(Unsigned32):
    """Custom type mlxIBPortLocalPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MlxIBPortLocalPortNumber_Type.__name__ = "Unsigned32"
_MlxIBPortLocalPortNumber_Object = MibTableColumn
mlxIBPortLocalPortNumber = _MlxIBPortLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2, 1, 2),
    _MlxIBPortLocalPortNumber_Type()
)
mlxIBPortLocalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBPortLocalPortNumber.setStatus("current")


class _MlxIBPortState_Type(Integer32):
    """Custom type mlxIBPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("armed", 3),
          ("down", 1),
          ("init", 2),
          ("other", 5))
    )


_MlxIBPortState_Type.__name__ = "Integer32"
_MlxIBPortState_Object = MibTableColumn
mlxIBPortState = _MlxIBPortState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2, 1, 3),
    _MlxIBPortState_Type()
)
mlxIBPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBPortState.setStatus("current")


class _MlxIBPortPhysicalState_Type(Integer32):
    """Custom type mlxIBPortPhysicalState based on Integer32"""
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
        *(("disabled", 3),
          ("linkErrorRecovery", 6),
          ("linkUp", 5),
          ("other", 8),
          ("phyTest", 7),
          ("polling", 2),
          ("portConfigTraining", 4),
          ("sleep", 1))
    )


_MlxIBPortPhysicalState_Type.__name__ = "Integer32"
_MlxIBPortPhysicalState_Object = MibTableColumn
mlxIBPortPhysicalState = _MlxIBPortPhysicalState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2, 1, 4),
    _MlxIBPortPhysicalState_Type()
)
mlxIBPortPhysicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBPortPhysicalState.setStatus("current")
_MlxIBPortGUID_Type = IbGuid
_MlxIBPortGUID_Object = MibTableColumn
mlxIBPortGUID = _MlxIBPortGUID_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2, 1, 5),
    _MlxIBPortGUID_Type()
)
mlxIBPortGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBPortGUID.setStatus("current")


class _MlxIBPortNodeType_Type(Integer32):
    """Custom type mlxIBPortNodeType based on Integer32"""
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
        *(("channelAdapter", 1),
          ("other", 4),
          ("router", 3),
          ("switch", 2))
    )


_MlxIBPortNodeType_Type.__name__ = "Integer32"
_MlxIBPortNodeType_Object = MibTableColumn
mlxIBPortNodeType = _MlxIBPortNodeType_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2, 1, 6),
    _MlxIBPortNodeType_Type()
)
mlxIBPortNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBPortNodeType.setStatus("current")
_MlxIBPortNodeIndex_Type = Unsigned32
_MlxIBPortNodeIndex_Object = MibTableColumn
mlxIBPortNodeIndex = _MlxIBPortNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 4, 2, 1, 7),
    _MlxIBPortNodeIndex_Type()
)
mlxIBPortNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlxIBPortNodeIndex.setStatus("current")
_MlxIBNotifications_ObjectIdentity = ObjectIdentity
mlxIBNotifications = _MlxIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5)
)

# Managed Objects groups


# Notification objects

internalBusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    internalBusError.setStatus(
        "current"
    )

procCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    procCrash.setStatus(
        "current"
    )

cpuUtilHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cpuUtilHigh.setStatus(
        "current"
    )

procUnexpectedExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    procUnexpectedExit.setStatus(
        "current"
    )

unexpectedShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    unexpectedShutdown.setStatus(
        "current"
    )

diskSpaceLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    diskSpaceLow.setStatus(
        "current"
    )

systemHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    systemHealthStatus.setStatus(
        "current"
    )

lowPowerRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    lowPowerRecover.setStatus(
        "current"
    )

insufficientFans = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    insufficientFans.setStatus(
        "current"
    )

insufficientFansRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    insufficientFansRecover.setStatus(
        "current"
    )

asicChipDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    asicChipDown.setStatus(
        "current"
    )

asicOverTempReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    asicOverTempReset.setStatus(
        "current"
    )

asicOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    asicOverTemp.setStatus(
        "current"
    )

lowPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    lowPower.setStatus(
        "current"
    )

ibSMup = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ibSMup.setStatus(
        "current"
    )

ibSMdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ibSMdown.setStatus(
        "current"
    )

ibSMrestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ibSMrestart.setStatus(
        "current"
    )

bxAsicChipDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    bxAsicChipDown.setStatus(
        "current"
    )

bxAsicOverTempReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    bxAsicOverTempReset.setStatus(
        "current"
    )

bxAsicOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    bxAsicOverTemp.setStatus(
        "current"
    )

mlxIBCAHealthStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 1)
)
mlxIBCAHealthStatusChange.setObjects(
      *(("MELLANOX-MIB", "mlxIBCAIndex"),
        ("MELLANOX-MIB", "mlxIBCAHealthStatus"),
        ("MELLANOX-MIB", "mlxIBCADeviceName"))
)
if mibBuilder.loadTexts:
    mlxIBCAHealthStatusChange.setStatus(
        "current"
    )

mlxIBCAInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 2)
)
mlxIBCAInsertion.setObjects(
    ("MELLANOX-MIB", "mlxIBCAIndex")
)
if mibBuilder.loadTexts:
    mlxIBCAInsertion.setStatus(
        "current"
    )

mlxIBCARemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 3)
)
mlxIBCARemoval.setObjects(
    ("MELLANOX-MIB", "mlxIBCAIndex")
)
if mibBuilder.loadTexts:
    mlxIBCARemoval.setStatus(
        "current"
    )

mlxIBSwitchInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 4)
)
mlxIBSwitchInsertion.setObjects(
    ("MELLANOX-MIB", "mlxIBSwitchIndex")
)
if mibBuilder.loadTexts:
    mlxIBSwitchInsertion.setStatus(
        "current"
    )

mlxIBSwitchRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 5)
)
mlxIBSwitchRemoval.setObjects(
    ("MELLANOX-MIB", "mlxIBSwitchIndex")
)
if mibBuilder.loadTexts:
    mlxIBSwitchRemoval.setStatus(
        "current"
    )

mlxIBRouterInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 6)
)
mlxIBRouterInsertion.setObjects(
    ("MELLANOX-MIB", "mlxIBRouterIndex")
)
if mibBuilder.loadTexts:
    mlxIBRouterInsertion.setStatus(
        "current"
    )

mlxIBRouterRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 7)
)
mlxIBRouterRemoval.setObjects(
    ("MELLANOX-MIB", "mlxIBRouterIndex")
)
if mibBuilder.loadTexts:
    mlxIBRouterRemoval.setStatus(
        "current"
    )

mlxIBPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 8)
)
mlxIBPortStateChange.setObjects(
      *(("MELLANOX-MIB", "mlxIBPortIndex"),
        ("MELLANOX-MIB", "mlxIBPortState"),
        ("MELLANOX-MIB", "mlxIBPortGUID"),
        ("MELLANOX-MIB", "mlxIBPortNodeType"),
        ("MELLANOX-MIB", "mlxIBPortNodeIndex"))
)
if mibBuilder.loadTexts:
    mlxIBPortStateChange.setStatus(
        "current"
    )

mlxIBPortPhysicalStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 9)
)
mlxIBPortPhysicalStateChange.setObjects(
      *(("MELLANOX-MIB", "mlxIBPortIndex"),
        ("MELLANOX-MIB", "mlxIBPortPhysicalState"),
        ("MELLANOX-MIB", "mlxIBPortGUID"),
        ("MELLANOX-MIB", "mlxIBPortNodeType"),
        ("MELLANOX-MIB", "mlxIBPortNodeIndex"))
)
if mibBuilder.loadTexts:
    mlxIBPortPhysicalStateChange.setStatus(
        "current"
    )

mlxIBPortInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 10)
)
mlxIBPortInsertion.setObjects(
    ("MELLANOX-MIB", "mlxIBPortIndex")
)
if mibBuilder.loadTexts:
    mlxIBPortInsertion.setStatus(
        "current"
    )

mlxIBPortRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 2, 5, 5, 11)
)
mlxIBPortRemoval.setObjects(
    ("MELLANOX-MIB", "mlxIBPortIndex")
)
if mibBuilder.loadTexts:
    mlxIBPortRemoval.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-MIB",
    **{"IbGuid": IbGuid,
       "mellanox": mellanox,
       "mellanoxProducts": mellanoxProducts,
       "mellanoxMgmt": mellanoxMgmt,
       "generalMgmt": generalMgmt,
       "gmVariables": gmVariables,
       "gmSystem": gmSystem,
       "type": type,
       "serialNumber": serialNumber,
       "swVersion": swVersion,
       "buildInfo": buildInfo,
       "nodeName": nodeName,
       "procmgr": procmgr,
       "procTable": procTable,
       "procEntry": procEntry,
       "procIndex": procIndex,
       "procName": procName,
       "procStatus": procStatus,
       "procNumFailures": procNumFailures,
       "storage": storage,
       "fsTable": fsTable,
       "fsEntry": fsEntry,
       "fsIndex": fsIndex,
       "fsMountPoint": fsMountPoint,
       "fsSpaceTotal": fsSpaceTotal,
       "fsSpaceUsed": fsSpaceUsed,
       "fsSpaceFree": fsSpaceFree,
       "fsSpaceAvail": fsSpaceAvail,
       "cpus": cpus,
       "cpuTable": cpuTable,
       "cpuEntry": cpuEntry,
       "cpuIndex": cpuIndex,
       "idleTime": idleTime,
       "systemTime": systemTime,
       "userTime": userTime,
       "gmNotifications": gmNotifications,
       "internalBusError": internalBusError,
       "procCrash": procCrash,
       "cpuUtilHigh": cpuUtilHigh,
       "procUnexpectedExit": procUnexpectedExit,
       "unexpectedShutdown": unexpectedShutdown,
       "diskSpaceLow": diskSpaceLow,
       "systemHealthStatus": systemHealthStatus,
       "lowPowerRecover": lowPowerRecover,
       "insufficientFans": insufficientFans,
       "insufficientFansRecover": insufficientFansRecover,
       "ibSwitch": ibSwitch,
       "ibVariables": ibVariables,
       "ibInventory": ibInventory,
       "invTable": invTable,
       "invEntry": invEntry,
       "invIndex": invIndex,
       "invName": invName,
       "invType": invType,
       "invPartNum": invPartNum,
       "invSerialNum": invSerialNum,
       "invFirmware": invFirmware,
       "invHealthStatus": invHealthStatus,
       "ibPorts": ibPorts,
       "cntTable": cntTable,
       "cntEntry": cntEntry,
       "cntIndex": cntIndex,
       "cntName": cntName,
       "cntPort": cntPort,
       "cntPhyState": cntPhyState,
       "cntLogState": cntLogState,
       "cntRate": cntRate,
       "cntMTU": cntMTU,
       "cntRcvData": cntRcvData,
       "cntRcvPkts": cntRcvPkts,
       "cntXmitData": cntXmitData,
       "cntXmitPkts": cntXmitPkts,
       "cntRcvErr": cntRcvErr,
       "cntXmitDiscard": cntXmitDiscard,
       "cntXmitWait": cntXmitWait,
       "cntSymErr": cntSymErr,
       "cntVL15Drop": cntVL15Drop,
       "cntSpeed": cntSpeed,
       "cntWidth": cntWidth,
       "cntOperationalVLs": cntOperationalVLs,
       "cntSupportedSpeeds": cntSupportedSpeeds,
       "cntSupportedWidths": cntSupportedWidths,
       "cntMaxSupportedMTUs": cntMaxSupportedMTUs,
       "cntVLCapabilities": cntVLCapabilities,
       "cntGUID": cntGUID,
       "cntLID": cntLID,
       "ibNotifications": ibNotifications,
       "asicChipDown": asicChipDown,
       "asicOverTempReset": asicOverTempReset,
       "asicOverTemp": asicOverTemp,
       "lowPower": lowPower,
       "subnetMngr": subnetMngr,
       "smVariables": smVariables,
       "smNotifications": smNotifications,
       "ibSMup": ibSMup,
       "ibSMdown": ibSMdown,
       "ibSMrestart": ibSMrestart,
       "bxBridge": bxBridge,
       "bxVariables": bxVariables,
       "bxInventory": bxInventory,
       "bxInvTable": bxInvTable,
       "bxInvEntry": bxInvEntry,
       "bxInvIndex": bxInvIndex,
       "bxInvName": bxInvName,
       "bxInvType": bxInvType,
       "bxInvPartNum": bxInvPartNum,
       "bxInvSerialNum": bxInvSerialNum,
       "bxInvFirmware": bxInvFirmware,
       "bxIbPorts": bxIbPorts,
       "bxIbCntTable": bxIbCntTable,
       "bxIbCntEntry": bxIbCntEntry,
       "bxIbCntIndex": bxIbCntIndex,
       "bxIbCntName": bxIbCntName,
       "bxIbCntPort": bxIbCntPort,
       "bxIbCntLogState": bxIbCntLogState,
       "bxIbCntPhyState": bxIbCntPhyState,
       "bxIbCntRate": bxIbCntRate,
       "bxIbCntSupportedSpeeds": bxIbCntSupportedSpeeds,
       "bxIbCntSpeed": bxIbCntSpeed,
       "bxIbCntSupportedWidths": bxIbCntSupportedWidths,
       "bxIbCntWidth": bxIbCntWidth,
       "bxIbCntMaxSupportedMTUs": bxIbCntMaxSupportedMTUs,
       "bxIbCntMTU": bxIbCntMTU,
       "bxIbCntVLCapabilities": bxIbCntVLCapabilities,
       "bxIbCntOperationalVLs": bxIbCntOperationalVLs,
       "bxIbCntGUID": bxIbCntGUID,
       "bxIbCntLID": bxIbCntLID,
       "bxIbCntRcvPkts": bxIbCntRcvPkts,
       "bxIbCntRcvData": bxIbCntRcvData,
       "bxIbCntRcvErr": bxIbCntRcvErr,
       "bxIbCntSymErr": bxIbCntSymErr,
       "bxIbCntVL15Drop": bxIbCntVL15Drop,
       "bxIbCntXmitPkts": bxIbCntXmitPkts,
       "bxIbCntXmitData": bxIbCntXmitData,
       "bxIbCntXmitWaits": bxIbCntXmitWaits,
       "bxIbCntXmitDiscards": bxIbCntXmitDiscards,
       "bxEthPorts": bxEthPorts,
       "bxEthCntTable": bxEthCntTable,
       "bxEthCntEntry": bxEthCntEntry,
       "bxEthCntIndex": bxEthCntIndex,
       "bxEthCntName": bxEthCntName,
       "bxEthCntAdminMode": bxEthCntAdminMode,
       "bxEthCntStatus": bxEthCntStatus,
       "bxEthCntSupportedSpeeds": bxEthCntSupportedSpeeds,
       "bxEthCntSpeed": bxEthCntSpeed,
       "bxEthCntDuplex": bxEthCntDuplex,
       "bxEthCntMTU": bxEthCntMTU,
       "bxEthCntFlowcontrolStatus": bxEthCntFlowcontrolStatus,
       "bxEthCntFlowcontrolMode": bxEthCntFlowcontrolMode,
       "bxEthCntFlowcontrolPriorities": bxEthCntFlowcontrolPriorities,
       "bxEthCntRcvPkts": bxEthCntRcvPkts,
       "bxEthCntRcvUcastPkts": bxEthCntRcvUcastPkts,
       "bxEthCntRcvMcatsPkts": bxEthCntRcvMcatsPkts,
       "bxEthCntRcvBcastPkts": bxEthCntRcvBcastPkts,
       "bxEthCntRcvJumboPkts": bxEthCntRcvJumboPkts,
       "bxEthCntRcvData": bxEthCntRcvData,
       "bxEthCntRcvErr": bxEthCntRcvErr,
       "bxEthCntRcvNoBuffer": bxEthCntRcvNoBuffer,
       "bxEthCntRcvRunt": bxEthCntRcvRunt,
       "bxEthCntRcvCRC": bxEthCntRcvCRC,
       "bxEthCntXmitPkts": bxEthCntXmitPkts,
       "bxEthCntXmitUcastPkts": bxEthCntXmitUcastPkts,
       "bxEthCntXmitMcastPkts": bxEthCntXmitMcastPkts,
       "bxEthCntXmitBcastPkts": bxEthCntXmitBcastPkts,
       "bxEthCntXmitJumboPkts": bxEthCntXmitJumboPkts,
       "bxEthCntXmitData": bxEthCntXmitData,
       "bxEthCntXmitErr": bxEthCntXmitErr,
       "bxFcPorts": bxFcPorts,
       "bxFcCntTable": bxFcCntTable,
       "bxFcCntEntry": bxFcCntEntry,
       "bxFcCntIndex": bxFcCntIndex,
       "bxFcCntName": bxFcCntName,
       "bxFcCntAdminMode": bxFcCntAdminMode,
       "bxFcCntStatus": bxFcCntStatus,
       "bxFcCntSupportedSpeeds": bxFcCntSupportedSpeeds,
       "bxFcCntSpeed": bxFcCntSpeed,
       "bxFcCntWWPN": bxFcCntWWPN,
       "bxFcCntFCID": bxFcCntFCID,
       "bxFcCntRcvCreditsAlloc": bxFcCntRcvCreditsAlloc,
       "bxFcCntXmitCreditsAlloc": bxFcCntXmitCreditsAlloc,
       "bxFcCntRcvPkts": bxFcCntRcvPkts,
       "bxFcCntRcvData": bxFcCntRcvData,
       "bxFcCntRcvDiscards": bxFcCntRcvDiscards,
       "bxFcCntRcvErr": bxFcCntRcvErr,
       "bxFcCntRcvCRC": bxFcCntRcvCRC,
       "bxFcCntRcvUnknown": bxFcCntRcvUnknown,
       "bxFcCntRcvLong": bxFcCntRcvLong,
       "bxFcCntRcvShort": bxFcCntRcvShort,
       "bxFcCntRcvOffline": bxFcCntRcvOffline,
       "bxFcCntRcvLinkReset": bxFcCntRcvLinkReset,
       "bxFcCntRcvNonOperational": bxFcCntRcvNonOperational,
       "bxFcCntRcvRemainCredits": bxFcCntRcvRemainCredits,
       "bxFcCntXmitPkts": bxFcCntXmitPkts,
       "bxFcCntXmitData": bxFcCntXmitData,
       "bxFcCntXmitDiscards": bxFcCntXmitDiscards,
       "bxFcCntXmitErr": bxFcCntXmitErr,
       "bxFcCntXmitOffline": bxFcCntXmitOffline,
       "bxFcCntXmitLinkReset": bxFcCntXmitLinkReset,
       "bxFcCntXmitNonOperational": bxFcCntXmitNonOperational,
       "bxFcCntXmitRemainCredits": bxFcCntXmitRemainCredits,
       "bxNotifications": bxNotifications,
       "bxAsicChipDown": bxAsicChipDown,
       "bxAsicOverTempReset": bxAsicOverTempReset,
       "bxAsicOverTemp": bxAsicOverTemp,
       "mlxIBObjects": mlxIBObjects,
       "mlxIBCAInfoGroup": mlxIBCAInfoGroup,
       "mlxIBCAInfoTableNumCAs": mlxIBCAInfoTableNumCAs,
       "mlxIBCAInfoTable": mlxIBCAInfoTable,
       "mlxIBCAInfoEntry": mlxIBCAInfoEntry,
       "mlxIBCAIndex": mlxIBCAIndex,
       "mlxIBCADeviceName": mlxIBCADeviceName,
       "mlxIBCAPCIDomain": mlxIBCAPCIDomain,
       "mlxIBCAPCIBus": mlxIBCAPCIBus,
       "mlxIBCAPCISlot": mlxIBCAPCISlot,
       "mlxIBCAPCIFunction": mlxIBCAPCIFunction,
       "mlxIBCAPCIPhysicalSlot": mlxIBCAPCIPhysicalSlot,
       "mlxIBCAIrq": mlxIBCAIrq,
       "mlxIBCAModelString": mlxIBCAModelString,
       "mlxIBCASerialNumber": mlxIBCASerialNumber,
       "mlxIBCAPartNumber": mlxIBCAPartNumber,
       "mlxIBCANodeGUID": mlxIBCANodeGUID,
       "mlxIBCASystemImageGUID": mlxIBCASystemImageGUID,
       "mlxIBCAFirmwareVersion": mlxIBCAFirmwareVersion,
       "mlxIBCAHardwareVersion": mlxIBCAHardwareVersion,
       "mlxIBCAHealthStatus": mlxIBCAHealthStatus,
       "mlxIBCANumPorts": mlxIBCANumPorts,
       "mlxIBCAType": mlxIBCAType,
       "mlxIBSwitchInfoGroup": mlxIBSwitchInfoGroup,
       "mlxIBSwitchInfoTableNumSwitches": mlxIBSwitchInfoTableNumSwitches,
       "mlxIBSwitchInfoTable": mlxIBSwitchInfoTable,
       "mlxIBSwitchInfoEntry": mlxIBSwitchInfoEntry,
       "mlxIBSwitchIndex": mlxIBSwitchIndex,
       "mlxIBRouterInfoGroup": mlxIBRouterInfoGroup,
       "mlxIBRouterInfoTableNumRouters": mlxIBRouterInfoTableNumRouters,
       "mlxIBRouterInfoTable": mlxIBRouterInfoTable,
       "mlxIBRouterInfoEntry": mlxIBRouterInfoEntry,
       "mlxIBRouterIndex": mlxIBRouterIndex,
       "mlxIBPortInfoGroup": mlxIBPortInfoGroup,
       "mlxIBPortInfoTableNumPorts": mlxIBPortInfoTableNumPorts,
       "mlxIBPortInfoTable": mlxIBPortInfoTable,
       "mlxIBPortInfoEntry": mlxIBPortInfoEntry,
       "mlxIBPortIndex": mlxIBPortIndex,
       "mlxIBPortLocalPortNumber": mlxIBPortLocalPortNumber,
       "mlxIBPortState": mlxIBPortState,
       "mlxIBPortPhysicalState": mlxIBPortPhysicalState,
       "mlxIBPortGUID": mlxIBPortGUID,
       "mlxIBPortNodeType": mlxIBPortNodeType,
       "mlxIBPortNodeIndex": mlxIBPortNodeIndex,
       "mlxIBNotifications": mlxIBNotifications,
       "mlxIBCAHealthStatusChange": mlxIBCAHealthStatusChange,
       "mlxIBCAInsertion": mlxIBCAInsertion,
       "mlxIBCARemoval": mlxIBCARemoval,
       "mlxIBSwitchInsertion": mlxIBSwitchInsertion,
       "mlxIBSwitchRemoval": mlxIBSwitchRemoval,
       "mlxIBRouterInsertion": mlxIBRouterInsertion,
       "mlxIBRouterRemoval": mlxIBRouterRemoval,
       "mlxIBPortStateChange": mlxIBPortStateChange,
       "mlxIBPortPhysicalStateChange": mlxIBPortPhysicalStateChange,
       "mlxIBPortInsertion": mlxIBPortInsertion,
       "mlxIBPortRemoval": mlxIBPortRemoval}
)
