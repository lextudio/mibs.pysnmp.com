# SNMP MIB module (VRTS-SNMP-MIBv1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VRTS-SNMP-MIBv1
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:20 2024
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



class OpEnum(Integer32):
    """Custom type OpEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("startMm", 4),
          ("startNbu", 2),
          ("stopMm", 5),
          ("stopNbu", 3),
          ("userDef0", 20),
          ("userDef1", 21),
          ("userDef2", 22),
          ("userDef3", 23),
          ("userDef4", 24),
          ("userDef5", 25),
          ("userDef6", 26),
          ("userDef7", 27),
          ("userDef8", 28),
          ("userDef9", 29))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Veritas_ObjectIdentity = ObjectIdentity
veritas = _Veritas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035)
)
_Netbackup_ObjectIdentity = ObjectIdentity
netbackup = _Netbackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1)
)
_Job_ObjectIdentity = ObjectIdentity
job = _Job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1)
)
_JobTable_Object = MibTable
jobTable = _JobTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jobTable.setStatus("mandatory")
_JobEntry_Object = MibTableRow
jobEntry = _JobEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1)
)
jobEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "jobIndex"),
)
if mibBuilder.loadTexts:
    jobEntry.setStatus("mandatory")


class _JobIndex_Type(Integer32):
    """Custom type jobIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JobIndex_Type.__name__ = "Integer32"
_JobIndex_Object = MibTableColumn
jobIndex = _JobIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 1),
    _JobIndex_Type()
)
jobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobIndex.setStatus("mandatory")
_JobType_Type = DisplayString
_JobType_Object = MibTableColumn
jobType = _JobType_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 2),
    _JobType_Type()
)
jobType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobType.setStatus("mandatory")
_JobState_Type = DisplayString
_JobState_Object = MibTableColumn
jobState = _JobState_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 3),
    _JobState_Type()
)
jobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobState.setStatus("mandatory")
_JobClass_Type = DisplayString
_JobClass_Object = MibTableColumn
jobClass = _JobClass_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 4),
    _JobClass_Type()
)
jobClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobClass.setStatus("mandatory")
_JobClient_Type = DisplayString
_JobClient_Object = MibTableColumn
jobClient = _JobClient_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 5),
    _JobClient_Type()
)
jobClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobClient.setStatus("mandatory")
_JobSched_Type = DisplayString
_JobSched_Object = MibTableColumn
jobSched = _JobSched_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 6),
    _JobSched_Type()
)
jobSched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobSched.setStatus("mandatory")
_JobSchedType_Type = DisplayString
_JobSchedType_Object = MibTableColumn
jobSchedType = _JobSchedType_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 7),
    _JobSchedType_Type()
)
jobSchedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobSchedType.setStatus("mandatory")
_JobStu_Type = DisplayString
_JobStu_Object = MibTableColumn
jobStu = _JobStu_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 8),
    _JobStu_Type()
)
jobStu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobStu.setStatus("mandatory")
_JobVolpool_Type = DisplayString
_JobVolpool_Object = MibTableColumn
jobVolpool = _JobVolpool_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 9),
    _JobVolpool_Type()
)
jobVolpool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobVolpool.setStatus("mandatory")


class _JobKbytes_Type(Integer32):
    """Custom type jobKbytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JobKbytes_Type.__name__ = "Integer32"
_JobKbytes_Object = MibTableColumn
jobKbytes = _JobKbytes_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 10),
    _JobKbytes_Type()
)
jobKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobKbytes.setStatus("mandatory")
_JobMaster_Type = DisplayString
_JobMaster_Object = MibTableColumn
jobMaster = _JobMaster_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 11),
    _JobMaster_Type()
)
jobMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobMaster.setStatus("mandatory")
_JobErrExpl_Type = DisplayString
_JobErrExpl_Object = MibTableColumn
jobErrExpl = _JobErrExpl_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 12),
    _JobErrExpl_Type()
)
jobErrExpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobErrExpl.setStatus("mandatory")
_JobErrReco_Type = DisplayString
_JobErrReco_Object = MibTableColumn
jobErrReco = _JobErrReco_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 13),
    _JobErrReco_Type()
)
jobErrReco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobErrReco.setStatus("mandatory")


class _JobId_Type(Integer32):
    """Custom type jobId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JobId_Type.__name__ = "Integer32"
_JobId_Object = MibTableColumn
jobId = _JobId_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 14),
    _JobId_Type()
)
jobId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobId.setStatus("mandatory")


class _JobErrCode_Type(Integer32):
    """Custom type jobErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JobErrCode_Type.__name__ = "Integer32"
_JobErrCode_Object = MibTableColumn
jobErrCode = _JobErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 100),
    _JobErrCode_Type()
)
jobErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobErrCode.setStatus("mandatory")
_JobErrMsg_Type = DisplayString
_JobErrMsg_Object = MibTableColumn
jobErrMsg = _JobErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 101),
    _JobErrMsg_Type()
)
jobErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobErrMsg.setStatus("mandatory")


class _JobErrFix_Type(Integer32):
    """Custom type jobErrFix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JobErrFix_Type.__name__ = "Integer32"
_JobErrFix_Object = MibTableColumn
jobErrFix = _JobErrFix_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 102),
    _JobErrFix_Type()
)
jobErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jobErrFix.setStatus("mandatory")
_JobErrFixCmd_Type = DisplayString
_JobErrFixCmd_Object = MibTableColumn
jobErrFixCmd = _JobErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 1, 1, 103),
    _JobErrFixCmd_Type()
)
jobErrFixCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jobErrFixCmd.setStatus("mandatory")
_VrtsNbuJobEvent_ObjectIdentity = ObjectIdentity
vrtsNbuJobEvent = _VrtsNbuJobEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 251)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2)
)
__pysmi_class_ObjectIdentity = ObjectIdentity
_pysmi_class = __pysmi_class_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 2)
)
_ClassTable_Object = MibTable
classTable = _ClassTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    classTable.setStatus("mandatory")
_ClassEntry_Object = MibTableRow
classEntry = _ClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 2, 1, 1)
)
classEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "classIndex"),
)
if mibBuilder.loadTexts:
    classEntry.setStatus("mandatory")


class _ClassIndex_Type(Integer32):
    """Custom type classIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClassIndex_Type.__name__ = "Integer32"
_ClassIndex_Object = MibTableColumn
classIndex = _ClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 2, 1, 1, 1),
    _ClassIndex_Type()
)
classIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classIndex.setStatus("mandatory")
_ClassName_Type = DisplayString
_ClassName_Object = MibTableColumn
className = _ClassName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 2, 1, 1, 2),
    _ClassName_Type()
)
className.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    className.setStatus("mandatory")
_Client_ObjectIdentity = ObjectIdentity
client = _Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 4)
)
_ClientTable_Object = MibTable
clientTable = _ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    clientTable.setStatus("mandatory")
_ClientEntry_Object = MibTableRow
clientEntry = _ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 4, 1, 1)
)
clientEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "clientIndex"),
)
if mibBuilder.loadTexts:
    clientEntry.setStatus("mandatory")


class _ClientIndex_Type(Integer32):
    """Custom type clientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClientIndex_Type.__name__ = "Integer32"
_ClientIndex_Object = MibTableColumn
clientIndex = _ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 4, 1, 1, 1),
    _ClientIndex_Type()
)
clientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIndex.setStatus("mandatory")
_ClientName_Type = DisplayString
_ClientName_Object = MibTableColumn
clientName = _ClientName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 4, 1, 1, 2),
    _ClientName_Type()
)
clientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientName.setStatus("mandatory")
_Sched_ObjectIdentity = ObjectIdentity
sched = _Sched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 6)
)
_SchedTable_Object = MibTable
schedTable = _SchedTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    schedTable.setStatus("mandatory")
_SchedEntry_Object = MibTableRow
schedEntry = _SchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 6, 1, 1)
)
schedEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "schedIndex"),
)
if mibBuilder.loadTexts:
    schedEntry.setStatus("mandatory")


class _SchedIndex_Type(Integer32):
    """Custom type schedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SchedIndex_Type.__name__ = "Integer32"
_SchedIndex_Object = MibTableColumn
schedIndex = _SchedIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 6, 1, 1, 1),
    _SchedIndex_Type()
)
schedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedIndex.setStatus("mandatory")
_SchedName_Type = DisplayString
_SchedName_Object = MibTableColumn
schedName = _SchedName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 6, 1, 1, 2),
    _SchedName_Type()
)
schedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedName.setStatus("mandatory")
_Stu_ObjectIdentity = ObjectIdentity
stu = _Stu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 8)
)
_StuTable_Object = MibTable
stuTable = _StuTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    stuTable.setStatus("mandatory")
_StuEntry_Object = MibTableRow
stuEntry = _StuEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 8, 1, 1)
)
stuEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "stuIndex"),
)
if mibBuilder.loadTexts:
    stuEntry.setStatus("mandatory")


class _StuIndex_Type(Integer32):
    """Custom type stuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StuIndex_Type.__name__ = "Integer32"
_StuIndex_Object = MibTableColumn
stuIndex = _StuIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 8, 1, 1, 1),
    _StuIndex_Type()
)
stuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuIndex.setStatus("mandatory")
_StuName_Type = DisplayString
_StuName_Object = MibTableColumn
stuName = _StuName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 2, 8, 1, 1, 2),
    _StuName_Type()
)
stuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuName.setStatus("mandatory")
_Media_ObjectIdentity = ObjectIdentity
media = _Media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4)
)
_MediaTable_Object = MibTable
mediaTable = _MediaTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mediaTable.setStatus("mandatory")
_MediaEntry_Object = MibTableRow
mediaEntry = _MediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1)
)
mediaEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "mediaIndex"),
)
if mibBuilder.loadTexts:
    mediaEntry.setStatus("mandatory")


class _MediaIndex_Type(Integer32):
    """Custom type mediaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MediaIndex_Type.__name__ = "Integer32"
_MediaIndex_Object = MibTableColumn
mediaIndex = _MediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 1),
    _MediaIndex_Type()
)
mediaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndex.setStatus("mandatory")
_MediaPool_Type = DisplayString
_MediaPool_Object = MibTableColumn
mediaPool = _MediaPool_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 2),
    _MediaPool_Type()
)
mediaPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaPool.setStatus("mandatory")
_MediaId_Type = DisplayString
_MediaId_Object = MibTableColumn
mediaId = _MediaId_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 3),
    _MediaId_Type()
)
mediaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaId.setStatus("mandatory")
_MediaType_Type = DisplayString
_MediaType_Object = MibTableColumn
mediaType = _MediaType_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 4),
    _MediaType_Type()
)
mediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaType.setStatus("mandatory")
_MediaRobotType_Type = DisplayString
_MediaRobotType_Object = MibTableColumn
mediaRobotType = _MediaRobotType_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 5),
    _MediaRobotType_Type()
)
mediaRobotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaRobotType.setStatus("mandatory")


class _MediaRobotNum_Type(Integer32):
    """Custom type mediaRobotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MediaRobotNum_Type.__name__ = "Integer32"
_MediaRobotNum_Object = MibTableColumn
mediaRobotNum = _MediaRobotNum_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 6),
    _MediaRobotNum_Type()
)
mediaRobotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaRobotNum.setStatus("mandatory")


class _MediaRobotSlot_Type(Integer32):
    """Custom type mediaRobotSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MediaRobotSlot_Type.__name__ = "Integer32"
_MediaRobotSlot_Object = MibTableColumn
mediaRobotSlot = _MediaRobotSlot_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 7),
    _MediaRobotSlot_Type()
)
mediaRobotSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaRobotSlot.setStatus("mandatory")
_MediaSideFace_Type = DisplayString
_MediaSideFace_Object = MibTableColumn
mediaSideFace = _MediaSideFace_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 8),
    _MediaSideFace_Type()
)
mediaSideFace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaSideFace.setStatus("mandatory")
_MediaRetLevel_Type = Integer32
_MediaRetLevel_Object = MibTableColumn
mediaRetLevel = _MediaRetLevel_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 9),
    _MediaRetLevel_Type()
)
mediaRetLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaRetLevel.setStatus("mandatory")
_MediaSize_Type = Integer32
_MediaSize_Object = MibTableColumn
mediaSize = _MediaSize_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 10),
    _MediaSize_Type()
)
mediaSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaSize.setStatus("mandatory")
_MediaStatus_Type = DisplayString
_MediaStatus_Object = MibTableColumn
mediaStatus = _MediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 1, 1, 11),
    _MediaStatus_Type()
)
mediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatus.setStatus("mandatory")
_Volpool_ObjectIdentity = ObjectIdentity
volpool = _Volpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 2)
)
_VolpoolTable_Object = MibTable
volpoolTable = _VolpoolTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    volpoolTable.setStatus("mandatory")
_VolpoolEntry_Object = MibTableRow
volpoolEntry = _VolpoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 2, 1, 1)
)
volpoolEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "volpoolIndex"),
)
if mibBuilder.loadTexts:
    volpoolEntry.setStatus("mandatory")


class _VolpoolIndex_Type(Integer32):
    """Custom type volpoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VolpoolIndex_Type.__name__ = "Integer32"
_VolpoolIndex_Object = MibTableColumn
volpoolIndex = _VolpoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 2, 1, 1, 1),
    _VolpoolIndex_Type()
)
volpoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volpoolIndex.setStatus("mandatory")
_VolpoolName_Type = DisplayString
_VolpoolName_Object = MibTableColumn
volpoolName = _VolpoolName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 2, 1, 1, 2),
    _VolpoolName_Type()
)
volpoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volpoolName.setStatus("mandatory")
_Robot_ObjectIdentity = ObjectIdentity
robot = _Robot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 4)
)
_RobotTable_Object = MibTable
robotTable = _RobotTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    robotTable.setStatus("mandatory")
_RobotEntry_Object = MibTableRow
robotEntry = _RobotEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 4, 1, 1)
)
robotEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "robotIndex"),
)
if mibBuilder.loadTexts:
    robotEntry.setStatus("mandatory")


class _RobotIndex_Type(Integer32):
    """Custom type robotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RobotIndex_Type.__name__ = "Integer32"
_RobotIndex_Object = MibTableColumn
robotIndex = _RobotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 4, 1, 1, 1),
    _RobotIndex_Type()
)
robotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    robotIndex.setStatus("mandatory")
_RobotName_Type = DisplayString
_RobotName_Object = MibTableColumn
robotName = _RobotName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 4, 1, 1, 2),
    _RobotName_Type()
)
robotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    robotName.setStatus("mandatory")
_Drive_ObjectIdentity = ObjectIdentity
drive = _Drive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 6)
)
_DriveTable_Object = MibTable
driveTable = _DriveTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    driveTable.setStatus("mandatory")
_DriveEntry_Object = MibTableRow
driveEntry = _DriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 6, 1, 1)
)
driveEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "driveIndex"),
)
if mibBuilder.loadTexts:
    driveEntry.setStatus("mandatory")


class _DriveIndex_Type(Integer32):
    """Custom type driveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DriveIndex_Type.__name__ = "Integer32"
_DriveIndex_Object = MibTableColumn
driveIndex = _DriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 6, 1, 1, 1),
    _DriveIndex_Type()
)
driveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveIndex.setStatus("mandatory")
_DriveName_Type = DisplayString
_DriveName_Object = MibTableColumn
driveName = _DriveName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 6, 1, 1, 2),
    _DriveName_Type()
)
driveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveName.setStatus("mandatory")
_Tape_ObjectIdentity = ObjectIdentity
tape = _Tape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 8)
)
_TapeTable_Object = MibTable
tapeTable = _TapeTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    tapeTable.setStatus("mandatory")
_TapeEntry_Object = MibTableRow
tapeEntry = _TapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 8, 1, 1)
)
tapeEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "tapeIndex"),
)
if mibBuilder.loadTexts:
    tapeEntry.setStatus("mandatory")


class _TapeIndex_Type(Integer32):
    """Custom type tapeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TapeIndex_Type.__name__ = "Integer32"
_TapeIndex_Object = MibTableColumn
tapeIndex = _TapeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 8, 1, 1, 1),
    _TapeIndex_Type()
)
tapeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeIndex.setStatus("mandatory")
_TapeName_Type = DisplayString
_TapeName_Object = MibTableColumn
tapeName = _TapeName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 4, 8, 1, 1, 2),
    _TapeName_Type()
)
tapeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeName.setStatus("mandatory")
_Dr_ObjectIdentity = ObjectIdentity
dr = _Dr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 6)
)
_Vault_ObjectIdentity = ObjectIdentity
vault = _Vault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 6, 2)
)
_VaultTable_Object = MibTable
vaultTable = _VaultTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vaultTable.setStatus("mandatory")
_VaultEntry_Object = MibTableRow
vaultEntry = _VaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 6, 2, 1, 1)
)
vaultEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "vaultIndex"),
)
if mibBuilder.loadTexts:
    vaultEntry.setStatus("mandatory")


class _VaultIndex_Type(Integer32):
    """Custom type vaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VaultIndex_Type.__name__ = "Integer32"
_VaultIndex_Object = MibTableColumn
vaultIndex = _VaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 6, 2, 1, 1, 1),
    _VaultIndex_Type()
)
vaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaultIndex.setStatus("mandatory")
_VaultName_Type = DisplayString
_VaultName_Object = MibTableColumn
vaultName = _VaultName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 6, 2, 1, 1, 2),
    _VaultName_Type()
)
vaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaultName.setStatus("mandatory")
_NbuExtTable_Object = MibTable
nbuExtTable = _NbuExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100)
)
if mibBuilder.loadTexts:
    nbuExtTable.setStatus("mandatory")
_NbuEntry_Object = MibTableRow
nbuEntry = _NbuEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1)
)
nbuEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "nbuIndex"),
)
if mibBuilder.loadTexts:
    nbuEntry.setStatus("mandatory")
_NbuIndex_Type = OpEnum
_NbuIndex_Object = MibTableColumn
nbuIndex = _NbuIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 1),
    _NbuIndex_Type()
)
nbuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuIndex.setStatus("mandatory")
_NbuNames_Type = DisplayString
_NbuNames_Object = MibTableColumn
nbuNames = _NbuNames_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 2),
    _NbuNames_Type()
)
nbuNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbuNames.setStatus("mandatory")
_NbuCommand_Type = DisplayString
_NbuCommand_Object = MibTableColumn
nbuCommand = _NbuCommand_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 3),
    _NbuCommand_Type()
)
nbuCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbuCommand.setStatus("mandatory")
_NbuCtlFlag_Type = Integer32
_NbuCtlFlag_Object = MibTableColumn
nbuCtlFlag = _NbuCtlFlag_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 4),
    _NbuCtlFlag_Type()
)
nbuCtlFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbuCtlFlag.setStatus("mandatory")
_NbuResFile_Type = DisplayString
_NbuResFile_Object = MibTableColumn
nbuResFile = _NbuResFile_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 5),
    _NbuResFile_Type()
)
nbuResFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuResFile.setStatus("mandatory")
_NbuLockFile_Type = DisplayString
_NbuLockFile_Object = MibTableColumn
nbuLockFile = _NbuLockFile_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 6),
    _NbuLockFile_Type()
)
nbuLockFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuLockFile.setStatus("mandatory")
_NbuTimeout_Type = Integer32
_NbuTimeout_Object = MibTableColumn
nbuTimeout = _NbuTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 7),
    _NbuTimeout_Type()
)
nbuTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuTimeout.setStatus("mandatory")
_NbuFreq_Type = Integer32
_NbuFreq_Object = MibTableColumn
nbuFreq = _NbuFreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 8),
    _NbuFreq_Type()
)
nbuFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuFreq.setStatus("mandatory")
_NbuResult_Type = Integer32
_NbuResult_Object = MibTableColumn
nbuResult = _NbuResult_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 100),
    _NbuResult_Type()
)
nbuResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuResult.setStatus("mandatory")
_NbuOutput_Type = DisplayString
_NbuOutput_Object = MibTableColumn
nbuOutput = _NbuOutput_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 101),
    _NbuOutput_Type()
)
nbuOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuOutput.setStatus("mandatory")
_NbuErrFix_Type = Integer32
_NbuErrFix_Object = MibTableColumn
nbuErrFix = _NbuErrFix_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 102),
    _NbuErrFix_Type()
)
nbuErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbuErrFix.setStatus("mandatory")
_NbuErrFixCmd_Type = DisplayString
_NbuErrFixCmd_Object = MibTableColumn
nbuErrFixCmd = _NbuErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 100, 1, 103),
    _NbuErrFixCmd_Type()
)
nbuErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuErrFixCmd.setStatus("mandatory")
_VrtsNbuExtEvent_ObjectIdentity = ObjectIdentity
vrtsNbuExtEvent = _VrtsNbuExtEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 101)
)
_NbuTrapVars_ObjectIdentity = ObjectIdentity
nbuTrapVars = _NbuTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 250)
)
_NbuHost_Type = DisplayString
_NbuHost_Object = MibScalar
nbuHost = _NbuHost_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 250, 1),
    _NbuHost_Type()
)
nbuHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuHost.setStatus("mandatory")
_NbuErrcode_Type = Integer32
_NbuErrcode_Object = MibScalar
nbuErrcode = _NbuErrcode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 250, 100),
    _NbuErrcode_Type()
)
nbuErrcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuErrcode.setStatus("mandatory")
_NbuErrmsg_Type = DisplayString
_NbuErrmsg_Object = MibScalar
nbuErrmsg = _NbuErrmsg_Object(
    (1, 3, 6, 1, 4, 1, 1035, 1, 250, 101),
    _NbuErrmsg_Type()
)
nbuErrmsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbuErrmsg.setStatus("mandatory")
_VrtsNbuEvents_ObjectIdentity = ObjectIdentity
vrtsNbuEvents = _VrtsNbuEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251)
)
_Vxvm_ObjectIdentity = ObjectIdentity
vxvm = _Vxvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 2)
)
_VmExtTable_Object = MibTable
vmExtTable = _VmExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100)
)
if mibBuilder.loadTexts:
    vmExtTable.setStatus("mandatory")
_VmEntry_Object = MibTableRow
vmEntry = _VmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1)
)
vmEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "vmIndex"),
)
if mibBuilder.loadTexts:
    vmEntry.setStatus("mandatory")


class _VmIndex_Type(Integer32):
    """Custom type vmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmIndex_Type.__name__ = "Integer32"
_VmIndex_Object = MibTableColumn
vmIndex = _VmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1, 1),
    _VmIndex_Type()
)
vmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIndex.setStatus("mandatory")
_VmNames_Type = DisplayString
_VmNames_Object = MibTableColumn
vmNames = _VmNames_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1, 2),
    _VmNames_Type()
)
vmNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmNames.setStatus("mandatory")
_VmCommand_Type = DisplayString
_VmCommand_Object = MibTableColumn
vmCommand = _VmCommand_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1, 3),
    _VmCommand_Type()
)
vmCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmCommand.setStatus("mandatory")
_VmCtlFlag_Type = Integer32
_VmCtlFlag_Object = MibTableColumn
vmCtlFlag = _VmCtlFlag_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1, 4),
    _VmCtlFlag_Type()
)
vmCtlFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmCtlFlag.setStatus("mandatory")
_VmResult_Type = Integer32
_VmResult_Object = MibTableColumn
vmResult = _VmResult_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1, 100),
    _VmResult_Type()
)
vmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmResult.setStatus("mandatory")
_VmOutput_Type = DisplayString
_VmOutput_Object = MibTableColumn
vmOutput = _VmOutput_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1, 101),
    _VmOutput_Type()
)
vmOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmOutput.setStatus("mandatory")
_VmErrFix_Type = Integer32
_VmErrFix_Object = MibTableColumn
vmErrFix = _VmErrFix_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1, 102),
    _VmErrFix_Type()
)
vmErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmErrFix.setStatus("mandatory")
_VmErrFixCmd_Type = DisplayString
_VmErrFixCmd_Object = MibTableColumn
vmErrFixCmd = _VmErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 100, 1, 103),
    _VmErrFixCmd_Type()
)
vmErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmErrFixCmd.setStatus("mandatory")
_VxvmEventAttrs_ObjectIdentity = ObjectIdentity
vxvmEventAttrs = _VxvmEventAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 2, 250)
)
_VxvmHost_Type = DisplayString
_VxvmHost_Object = MibScalar
vxvmHost = _VxvmHost_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 250, 1),
    _VxvmHost_Type()
)
vxvmHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxvmHost.setStatus("mandatory")
_VxvmType_Type = DisplayString
_VxvmType_Object = MibScalar
vxvmType = _VxvmType_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 250, 2),
    _VxvmType_Type()
)
vxvmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxvmType.setStatus("mandatory")
_VxvmSeverity_Type = DisplayString
_VxvmSeverity_Object = MibScalar
vxvmSeverity = _VxvmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 250, 3),
    _VxvmSeverity_Type()
)
vxvmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxvmSeverity.setStatus("mandatory")
_VxvmErrExpl_Type = DisplayString
_VxvmErrExpl_Object = MibScalar
vxvmErrExpl = _VxvmErrExpl_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 250, 98),
    _VxvmErrExpl_Type()
)
vxvmErrExpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxvmErrExpl.setStatus("mandatory")
_VxvmErrReco_Type = DisplayString
_VxvmErrReco_Object = MibScalar
vxvmErrReco = _VxvmErrReco_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 250, 99),
    _VxvmErrReco_Type()
)
vxvmErrReco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxvmErrReco.setStatus("mandatory")
_VxvmErrCode_Type = Integer32
_VxvmErrCode_Object = MibScalar
vxvmErrCode = _VxvmErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 250, 100),
    _VxvmErrCode_Type()
)
vxvmErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxvmErrCode.setStatus("mandatory")
_VxvmErrMsg_Type = DisplayString
_VxvmErrMsg_Object = MibScalar
vxvmErrMsg = _VxvmErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 1035, 2, 250, 101),
    _VxvmErrMsg_Type()
)
vxvmErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxvmErrMsg.setStatus("mandatory")
_VrtsVxvmEvent_ObjectIdentity = ObjectIdentity
vrtsVxvmEvent = _VrtsVxvmEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 2, 251)
)
_Vxfs_ObjectIdentity = ObjectIdentity
vxfs = _Vxfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 3)
)
_FsExtTable_Object = MibTable
fsExtTable = _FsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100)
)
if mibBuilder.loadTexts:
    fsExtTable.setStatus("mandatory")
_FsEntry_Object = MibTableRow
fsEntry = _FsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1)
)
fsEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "fsIndex"),
)
if mibBuilder.loadTexts:
    fsEntry.setStatus("mandatory")


class _FsIndex_Type(Integer32):
    """Custom type fsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsIndex_Type.__name__ = "Integer32"
_FsIndex_Object = MibTableColumn
fsIndex = _FsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1, 1),
    _FsIndex_Type()
)
fsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIndex.setStatus("mandatory")
_FsNames_Type = DisplayString
_FsNames_Object = MibTableColumn
fsNames = _FsNames_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1, 2),
    _FsNames_Type()
)
fsNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNames.setStatus("mandatory")
_FsCommand_Type = DisplayString
_FsCommand_Object = MibTableColumn
fsCommand = _FsCommand_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1, 3),
    _FsCommand_Type()
)
fsCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCommand.setStatus("mandatory")
_FsCtlFlag_Type = Integer32
_FsCtlFlag_Object = MibTableColumn
fsCtlFlag = _FsCtlFlag_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1, 4),
    _FsCtlFlag_Type()
)
fsCtlFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCtlFlag.setStatus("mandatory")
_FsResult_Type = Integer32
_FsResult_Object = MibTableColumn
fsResult = _FsResult_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1, 100),
    _FsResult_Type()
)
fsResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsResult.setStatus("mandatory")
_FsOutput_Type = DisplayString
_FsOutput_Object = MibTableColumn
fsOutput = _FsOutput_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1, 101),
    _FsOutput_Type()
)
fsOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutput.setStatus("mandatory")
_FsErrFix_Type = Integer32
_FsErrFix_Object = MibTableColumn
fsErrFix = _FsErrFix_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1, 102),
    _FsErrFix_Type()
)
fsErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErrFix.setStatus("mandatory")
_FsErrFixCmd_Type = DisplayString
_FsErrFixCmd_Object = MibTableColumn
fsErrFixCmd = _FsErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 100, 1, 103),
    _FsErrFixCmd_Type()
)
fsErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErrFixCmd.setStatus("mandatory")
_VxfsEventAttrs_ObjectIdentity = ObjectIdentity
vxfsEventAttrs = _VxfsEventAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 3, 250)
)
_VxfsHost_Type = DisplayString
_VxfsHost_Object = MibScalar
vxfsHost = _VxfsHost_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 250, 1),
    _VxfsHost_Type()
)
vxfsHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxfsHost.setStatus("mandatory")
_VxfsMsgcnt_Type = Integer32
_VxfsMsgcnt_Object = MibScalar
vxfsMsgcnt = _VxfsMsgcnt_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 250, 2),
    _VxfsMsgcnt_Type()
)
vxfsMsgcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxfsMsgcnt.setStatus("mandatory")
_VxfsSeverity_Type = DisplayString
_VxfsSeverity_Object = MibScalar
vxfsSeverity = _VxfsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 250, 3),
    _VxfsSeverity_Type()
)
vxfsSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxfsSeverity.setStatus("mandatory")
_VxfsErrExpl_Type = DisplayString
_VxfsErrExpl_Object = MibScalar
vxfsErrExpl = _VxfsErrExpl_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 250, 98),
    _VxfsErrExpl_Type()
)
vxfsErrExpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxfsErrExpl.setStatus("mandatory")
_VxfsErrReco_Type = DisplayString
_VxfsErrReco_Object = MibScalar
vxfsErrReco = _VxfsErrReco_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 250, 99),
    _VxfsErrReco_Type()
)
vxfsErrReco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxfsErrReco.setStatus("mandatory")
_VxfsErrCode_Type = Integer32
_VxfsErrCode_Object = MibScalar
vxfsErrCode = _VxfsErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 250, 100),
    _VxfsErrCode_Type()
)
vxfsErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxfsErrCode.setStatus("mandatory")
_VxfsErrMsg_Type = DisplayString
_VxfsErrMsg_Object = MibScalar
vxfsErrMsg = _VxfsErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 1035, 3, 250, 101),
    _VxfsErrMsg_Type()
)
vxfsErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxfsErrMsg.setStatus("mandatory")
_VrtsVxfsEvent_ObjectIdentity = ObjectIdentity
vrtsVxfsEvent = _VrtsVxfsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 3, 251)
)
_Vcs_ObjectIdentity = ObjectIdentity
vcs = _Vcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 7)
)
_VcsExtTable_Object = MibTable
vcsExtTable = _VcsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100)
)
if mibBuilder.loadTexts:
    vcsExtTable.setStatus("mandatory")
_VcsEntry_Object = MibTableRow
vcsEntry = _VcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1)
)
vcsEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "vcsIndex"),
)
if mibBuilder.loadTexts:
    vcsEntry.setStatus("mandatory")


class _VcsIndex_Type(Integer32):
    """Custom type vcsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VcsIndex_Type.__name__ = "Integer32"
_VcsIndex_Object = MibTableColumn
vcsIndex = _VcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1, 1),
    _VcsIndex_Type()
)
vcsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsIndex.setStatus("mandatory")
_VcsNames_Type = DisplayString
_VcsNames_Object = MibTableColumn
vcsNames = _VcsNames_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1, 2),
    _VcsNames_Type()
)
vcsNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsNames.setStatus("mandatory")
_VcsCommand_Type = DisplayString
_VcsCommand_Object = MibTableColumn
vcsCommand = _VcsCommand_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1, 3),
    _VcsCommand_Type()
)
vcsCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsCommand.setStatus("mandatory")
_VcsCtlFlag_Type = Integer32
_VcsCtlFlag_Object = MibTableColumn
vcsCtlFlag = _VcsCtlFlag_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1, 4),
    _VcsCtlFlag_Type()
)
vcsCtlFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcsCtlFlag.setStatus("mandatory")
_VcsResult_Type = Integer32
_VcsResult_Object = MibTableColumn
vcsResult = _VcsResult_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1, 100),
    _VcsResult_Type()
)
vcsResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsResult.setStatus("mandatory")
_VcsOutput_Type = DisplayString
_VcsOutput_Object = MibTableColumn
vcsOutput = _VcsOutput_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1, 101),
    _VcsOutput_Type()
)
vcsOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsOutput.setStatus("mandatory")
_VcsErrFix_Type = Integer32
_VcsErrFix_Object = MibTableColumn
vcsErrFix = _VcsErrFix_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1, 102),
    _VcsErrFix_Type()
)
vcsErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcsErrFix.setStatus("mandatory")
_VcsErrFixCmd_Type = DisplayString
_VcsErrFixCmd_Object = MibTableColumn
vcsErrFixCmd = _VcsErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 100, 1, 103),
    _VcsErrFixCmd_Type()
)
vcsErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsErrFixCmd.setStatus("mandatory")
_VcsEventAttrs_ObjectIdentity = ObjectIdentity
vcsEventAttrs = _VcsEventAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250)
)
_VcsTag_Type = DisplayString
_VcsTag_Object = MibScalar
vcsTag = _VcsTag_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 1),
    _VcsTag_Type()
)
vcsTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsTag.setStatus("mandatory")
_VcsHost_Type = DisplayString
_VcsHost_Object = MibScalar
vcsHost = _VcsHost_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 2),
    _VcsHost_Type()
)
vcsHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsHost.setStatus("mandatory")
_VcsRes_Type = DisplayString
_VcsRes_Object = MibScalar
vcsRes = _VcsRes_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 3),
    _VcsRes_Type()
)
vcsRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsRes.setStatus("mandatory")
_VcsResStat_Type = DisplayString
_VcsResStat_Object = MibScalar
vcsResStat = _VcsResStat_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 4),
    _VcsResStat_Type()
)
vcsResStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsResStat.setStatus("mandatory")
_VcsAgent_Type = DisplayString
_VcsAgent_Object = MibScalar
vcsAgent = _VcsAgent_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 5),
    _VcsAgent_Type()
)
vcsAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsAgent.setStatus("mandatory")
_VcsNode_Type = DisplayString
_VcsNode_Object = MibScalar
vcsNode = _VcsNode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 6),
    _VcsNode_Type()
)
vcsNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsNode.setStatus("mandatory")
_VcsDate_Type = DisplayString
_VcsDate_Object = MibScalar
vcsDate = _VcsDate_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 7),
    _VcsDate_Type()
)
vcsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsDate.setStatus("mandatory")
_VcsTime_Type = DisplayString
_VcsTime_Object = MibScalar
vcsTime = _VcsTime_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 8),
    _VcsTime_Type()
)
vcsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsTime.setStatus("mandatory")
_VcsErrExpl_Type = DisplayString
_VcsErrExpl_Object = MibScalar
vcsErrExpl = _VcsErrExpl_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 98),
    _VcsErrExpl_Type()
)
vcsErrExpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsErrExpl.setStatus("mandatory")
_VcsErrReco_Type = DisplayString
_VcsErrReco_Object = MibScalar
vcsErrReco = _VcsErrReco_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 99),
    _VcsErrReco_Type()
)
vcsErrReco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsErrReco.setStatus("mandatory")
_VcsErrCode_Type = Integer32
_VcsErrCode_Object = MibScalar
vcsErrCode = _VcsErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 100),
    _VcsErrCode_Type()
)
vcsErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsErrCode.setStatus("mandatory")
_VcsErrMsg_Type = DisplayString
_VcsErrMsg_Object = MibScalar
vcsErrMsg = _VcsErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 1035, 7, 250, 101),
    _VcsErrMsg_Type()
)
vcsErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsErrMsg.setStatus("mandatory")
_VrtsVcsEvent_ObjectIdentity = ObjectIdentity
vrtsVcsEvent = _VrtsVcsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 7, 251)
)
_CommonObjects_ObjectIdentity = ObjectIdentity
commonObjects = _CommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301)
)
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1)
)
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1)
)
if mibBuilder.loadTexts:
    logTable.setStatus("mandatory")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1)
)
logEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("mandatory")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")
_LogHost_Type = DisplayString
_LogHost_Object = MibTableColumn
logHost = _LogHost_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 2),
    _LogHost_Type()
)
logHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logHost.setStatus("mandatory")
_LogPrdCode_Type = Integer32
_LogPrdCode_Object = MibTableColumn
logPrdCode = _LogPrdCode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 3),
    _LogPrdCode_Type()
)
logPrdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logPrdCode.setStatus("mandatory")
_LogPrdName_Type = DisplayString
_LogPrdName_Object = MibTableColumn
logPrdName = _LogPrdName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 4),
    _LogPrdName_Type()
)
logPrdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logPrdName.setStatus("mandatory")
_LogObjName_Type = DisplayString
_LogObjName_Object = MibTableColumn
logObjName = _LogObjName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 5),
    _LogObjName_Type()
)
logObjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logObjName.setStatus("mandatory")
_LogAttrName_Type = DisplayString
_LogAttrName_Object = MibTableColumn
logAttrName = _LogAttrName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 6),
    _LogAttrName_Type()
)
logAttrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAttrName.setStatus("mandatory")
_LogFile_Type = DisplayString
_LogFile_Object = MibTableColumn
logFile = _LogFile_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 7),
    _LogFile_Type()
)
logFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFile.setStatus("mandatory")
_LogErrStrs_Type = DisplayString
_LogErrStrs_Object = MibTableColumn
logErrStrs = _LogErrStrs_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 8),
    _LogErrStrs_Type()
)
logErrStrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logErrStrs.setStatus("mandatory")
_LogDesc_Type = DisplayString
_LogDesc_Object = MibTableColumn
logDesc = _LogDesc_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 9),
    _LogDesc_Type()
)
logDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDesc.setStatus("mandatory")
_LogResolution_Type = DisplayString
_LogResolution_Object = MibTableColumn
logResolution = _LogResolution_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 10),
    _LogResolution_Type()
)
logResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logResolution.setStatus("mandatory")
_LogErrFlag_Type = Integer32
_LogErrFlag_Object = MibTableColumn
logErrFlag = _LogErrFlag_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 99),
    _LogErrFlag_Type()
)
logErrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logErrFlag.setStatus("mandatory")
_LogErrcode_Type = Integer32
_LogErrcode_Object = MibTableColumn
logErrcode = _LogErrcode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 100),
    _LogErrcode_Type()
)
logErrcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logErrcode.setStatus("mandatory")
_LogErrmsg_Type = DisplayString
_LogErrmsg_Object = MibTableColumn
logErrmsg = _LogErrmsg_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 101),
    _LogErrmsg_Type()
)
logErrmsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logErrmsg.setStatus("mandatory")


class _LogErrFix_Type(Integer32):
    """Custom type logErrFix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LogErrFix_Type.__name__ = "Integer32"
_LogErrFix_Object = MibTableColumn
logErrFix = _LogErrFix_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 102),
    _LogErrFix_Type()
)
logErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logErrFix.setStatus("mandatory")
_LogErrFixCmd_Type = DisplayString
_LogErrFixCmd_Object = MibTableColumn
logErrFixCmd = _LogErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 1, 1, 103),
    _LogErrFixCmd_Type()
)
logErrFixCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logErrFixCmd.setStatus("mandatory")
_VrtsLogMonitor_ObjectIdentity = ObjectIdentity
vrtsLogMonitor = _VrtsLogMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 251)
)
_Process_ObjectIdentity = ObjectIdentity
process = _Process_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2)
)
_PsTable_Object = MibTable
psTable = _PsTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1)
)
if mibBuilder.loadTexts:
    psTable.setStatus("mandatory")
_PsEntry_Object = MibTableRow
psEntry = _PsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1)
)
psEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "psIndex"),
)
if mibBuilder.loadTexts:
    psEntry.setStatus("mandatory")


class _PsIndex_Type(Integer32):
    """Custom type psIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsIndex_Type.__name__ = "Integer32"
_PsIndex_Object = MibTableColumn
psIndex = _PsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 1),
    _PsIndex_Type()
)
psIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIndex.setStatus("mandatory")


class _PsId_Type(Integer32):
    """Custom type psId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsId_Type.__name__ = "Integer32"
_PsId_Object = MibTableColumn
psId = _PsId_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 2),
    _PsId_Type()
)
psId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psId.setStatus("mandatory")
_PsName_Type = DisplayString
_PsName_Object = MibTableColumn
psName = _PsName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 3),
    _PsName_Type()
)
psName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psName.setStatus("mandatory")
_PsAttr_Type = DisplayString
_PsAttr_Object = MibTableColumn
psAttr = _PsAttr_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 4),
    _PsAttr_Type()
)
psAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAttr.setStatus("mandatory")
_PsMin_Type = Integer32
_PsMin_Object = MibTableColumn
psMin = _PsMin_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 5),
    _PsMin_Type()
)
psMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMin.setStatus("mandatory")
_PsMax_Type = Integer32
_PsMax_Object = MibTableColumn
psMax = _PsMax_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 6),
    _PsMax_Type()
)
psMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMax.setStatus("mandatory")
_PsCount_Type = Integer32
_PsCount_Object = MibTableColumn
psCount = _PsCount_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 7),
    _PsCount_Type()
)
psCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psCount.setStatus("mandatory")
_PsCpuPct_Type = DisplayString
_PsCpuPct_Object = MibTableColumn
psCpuPct = _PsCpuPct_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 8),
    _PsCpuPct_Type()
)
psCpuPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psCpuPct.setStatus("mandatory")
_PsBytesIO_Type = Integer32
_PsBytesIO_Object = MibTableColumn
psBytesIO = _PsBytesIO_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 9),
    _PsBytesIO_Type()
)
psBytesIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBytesIO.setStatus("mandatory")
_PsSlpMax_Type = Integer32
_PsSlpMax_Object = MibTableColumn
psSlpMax = _PsSlpMax_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 10),
    _PsSlpMax_Type()
)
psSlpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSlpMax.setStatus("mandatory")
_PsHost_Type = DisplayString
_PsHost_Object = MibTableColumn
psHost = _PsHost_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 11),
    _PsHost_Type()
)
psHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psHost.setStatus("mandatory")
_PsErrFlag_Type = Integer32
_PsErrFlag_Object = MibTableColumn
psErrFlag = _PsErrFlag_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 99),
    _PsErrFlag_Type()
)
psErrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psErrFlag.setStatus("mandatory")
_PsErrcode_Type = Integer32
_PsErrcode_Object = MibTableColumn
psErrcode = _PsErrcode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 100),
    _PsErrcode_Type()
)
psErrcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psErrcode.setStatus("mandatory")
_PsErrmsg_Type = DisplayString
_PsErrmsg_Object = MibTableColumn
psErrmsg = _PsErrmsg_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 101),
    _PsErrmsg_Type()
)
psErrmsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psErrmsg.setStatus("mandatory")
_PsErrFix_Type = Integer32
_PsErrFix_Object = MibTableColumn
psErrFix = _PsErrFix_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 102),
    _PsErrFix_Type()
)
psErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psErrFix.setStatus("mandatory")
_PsErrFixCmd_Type = DisplayString
_PsErrFixCmd_Object = MibTableColumn
psErrFixCmd = _PsErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 1, 1, 103),
    _PsErrFixCmd_Type()
)
psErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psErrFixCmd.setStatus("mandatory")
_VrtsProcessMonitor_ObjectIdentity = ObjectIdentity
vrtsProcessMonitor = _VrtsProcessMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 251)
)
_Collector_ObjectIdentity = ObjectIdentity
collector = _Collector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4)
)
_ClTable_Object = MibTable
clTable = _ClTable_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1)
)
if mibBuilder.loadTexts:
    clTable.setStatus("mandatory")
_ClEntry_Object = MibTableRow
clEntry = _ClEntry_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1)
)
clEntry.setIndexNames(
    (0, "VRTS-SNMP-MIBv1", "clIndex"),
)
if mibBuilder.loadTexts:
    clEntry.setStatus("mandatory")


class _ClIndex_Type(Integer32):
    """Custom type clIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClIndex_Type.__name__ = "Integer32"
_ClIndex_Object = MibTableColumn
clIndex = _ClIndex_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 1),
    _ClIndex_Type()
)
clIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIndex.setStatus("mandatory")
_ClName_Type = DisplayString
_ClName_Object = MibTableColumn
clName = _ClName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 2),
    _ClName_Type()
)
clName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clName.setStatus("mandatory")
_ClHost_Type = DisplayString
_ClHost_Object = MibTableColumn
clHost = _ClHost_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 3),
    _ClHost_Type()
)
clHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clHost.setStatus("mandatory")
_ClScript_Type = DisplayString
_ClScript_Object = MibTableColumn
clScript = _ClScript_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 4),
    _ClScript_Type()
)
clScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clScript.setStatus("mandatory")
_ClSampFreq_Type = Integer32
_ClSampFreq_Object = MibTableColumn
clSampFreq = _ClSampFreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 5),
    _ClSampFreq_Type()
)
clSampFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clSampFreq.setStatus("mandatory")
_ClFreq_Type = Integer32
_ClFreq_Object = MibTableColumn
clFreq = _ClFreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 6),
    _ClFreq_Type()
)
clFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clFreq.setStatus("mandatory")
_ClTimeout_Type = Integer32
_ClTimeout_Object = MibTableColumn
clTimeout = _ClTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 7),
    _ClTimeout_Type()
)
clTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clTimeout.setStatus("mandatory")
_ClPrdCode_Type = Integer32
_ClPrdCode_Object = MibTableColumn
clPrdCode = _ClPrdCode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 8),
    _ClPrdCode_Type()
)
clPrdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPrdCode.setStatus("mandatory")
_ClPrdName_Type = DisplayString
_ClPrdName_Object = MibTableColumn
clPrdName = _ClPrdName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 9),
    _ClPrdName_Type()
)
clPrdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPrdName.setStatus("mandatory")
_ClObjName_Type = DisplayString
_ClObjName_Object = MibTableColumn
clObjName = _ClObjName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 10),
    _ClObjName_Type()
)
clObjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clObjName.setStatus("mandatory")
_ClAttrName_Type = DisplayString
_ClAttrName_Object = MibTableColumn
clAttrName = _ClAttrName_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 11),
    _ClAttrName_Type()
)
clAttrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clAttrName.setStatus("mandatory")
_ClLow_Type = Integer32
_ClLow_Object = MibTableColumn
clLow = _ClLow_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 12),
    _ClLow_Type()
)
clLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clLow.setStatus("mandatory")
_ClHigh_Type = Integer32
_ClHigh_Object = MibTableColumn
clHigh = _ClHigh_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 13),
    _ClHigh_Type()
)
clHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clHigh.setStatus("mandatory")
_ClCount_Type = Integer32
_ClCount_Object = MibTableColumn
clCount = _ClCount_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 14),
    _ClCount_Type()
)
clCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCount.setStatus("mandatory")
_ClObjNames_Type = DisplayString
_ClObjNames_Object = MibTableColumn
clObjNames = _ClObjNames_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 15),
    _ClObjNames_Type()
)
clObjNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clObjNames.setStatus("mandatory")
_ClResolution_Type = DisplayString
_ClResolution_Object = MibTableColumn
clResolution = _ClResolution_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 16),
    _ClResolution_Type()
)
clResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clResolution.setStatus("mandatory")
_ClErrFlag_Type = Integer32
_ClErrFlag_Object = MibTableColumn
clErrFlag = _ClErrFlag_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 99),
    _ClErrFlag_Type()
)
clErrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clErrFlag.setStatus("mandatory")
_ClErrcode_Type = Integer32
_ClErrcode_Object = MibTableColumn
clErrcode = _ClErrcode_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 100),
    _ClErrcode_Type()
)
clErrcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clErrcode.setStatus("mandatory")
_ClErrmsg_Type = DisplayString
_ClErrmsg_Object = MibTableColumn
clErrmsg = _ClErrmsg_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 101),
    _ClErrmsg_Type()
)
clErrmsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clErrmsg.setStatus("mandatory")
_ClErrFix_Type = Integer32
_ClErrFix_Object = MibTableColumn
clErrFix = _ClErrFix_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 102),
    _ClErrFix_Type()
)
clErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clErrFix.setStatus("mandatory")
_ClErrFixCmd_Type = DisplayString
_ClErrFixCmd_Object = MibTableColumn
clErrFixCmd = _ClErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 1, 1, 103),
    _ClErrFixCmd_Type()
)
clErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clErrFixCmd.setStatus("mandatory")
_VrtsCollectorMonitor_ObjectIdentity = ObjectIdentity
vrtsCollectorMonitor = _VrtsCollectorMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 251)
)
_Frequency_ObjectIdentity = ObjectIdentity
frequency = _Frequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8)
)
_Messagefreq_Type = Integer32
_Messagefreq_Object = MibScalar
messagefreq = _Messagefreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8, 1),
    _Messagefreq_Type()
)
messagefreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagefreq.setStatus("mandatory")
_Processfreq_Type = Integer32
_Processfreq_Object = MibScalar
processfreq = _Processfreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8, 2),
    _Processfreq_Type()
)
processfreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processfreq.setStatus("mandatory")
_VxvmSamplefreq_Type = Integer32
_VxvmSamplefreq_Object = MibScalar
vxvmSamplefreq = _VxvmSamplefreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8, 11),
    _VxvmSamplefreq_Type()
)
vxvmSamplefreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxvmSamplefreq.setStatus("mandatory")
_VxvmCheckfreq_Type = Integer32
_VxvmCheckfreq_Object = MibScalar
vxvmCheckfreq = _VxvmCheckfreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8, 12),
    _VxvmCheckfreq_Type()
)
vxvmCheckfreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxvmCheckfreq.setStatus("mandatory")
_VxvmTimeout_Type = Integer32
_VxvmTimeout_Object = MibScalar
vxvmTimeout = _VxvmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8, 13),
    _VxvmTimeout_Type()
)
vxvmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxvmTimeout.setStatus("mandatory")
_VxfsSamplefreq_Type = Integer32
_VxfsSamplefreq_Object = MibScalar
vxfsSamplefreq = _VxfsSamplefreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8, 21),
    _VxfsSamplefreq_Type()
)
vxfsSamplefreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxfsSamplefreq.setStatus("mandatory")
_VxfsCheckfreq_Type = Integer32
_VxfsCheckfreq_Object = MibScalar
vxfsCheckfreq = _VxfsCheckfreq_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8, 22),
    _VxfsCheckfreq_Type()
)
vxfsCheckfreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxfsCheckfreq.setStatus("mandatory")
_VxfsTimeout_Type = Integer32
_VxfsTimeout_Object = MibScalar
vxfsTimeout = _VxfsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1035, 301, 8, 23),
    _VxfsTimeout_Type()
)
vxfsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxfsTimeout.setStatus("mandatory")
_VrtsEneMonitor_ObjectIdentity = ObjectIdentity
vrtsEneMonitor = _VrtsEneMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1035, 301, 251)
)

# Managed Objects groups


# Notification objects

abnormalJobEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 251, 0, 1)
)
abnormalJobEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "jobId"),
        ("VRTS-SNMP-MIBv1", "jobClass"),
        ("VRTS-SNMP-MIBv1", "jobClient"),
        ("VRTS-SNMP-MIBv1", "jobSched"),
        ("VRTS-SNMP-MIBv1", "jobSchedType"),
        ("VRTS-SNMP-MIBv1", "jobStu"),
        ("VRTS-SNMP-MIBv1", "jobVolpool"),
        ("VRTS-SNMP-MIBv1", "jobErrCode"),
        ("VRTS-SNMP-MIBv1", "jobErrMsg"),
        ("VRTS-SNMP-MIBv1", "jobMaster"),
        ("VRTS-SNMP-MIBv1", "jobErrExpl"),
        ("VRTS-SNMP-MIBv1", "jobErrReco"))
)
if mibBuilder.loadTexts:
    abnormalJobEvent.setStatus(
        ""
    )

normalJobEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 1, 251, 0, 2)
)
normalJobEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "jobId"),
        ("VRTS-SNMP-MIBv1", "jobClass"),
        ("VRTS-SNMP-MIBv1", "jobClient"),
        ("VRTS-SNMP-MIBv1", "jobSched"),
        ("VRTS-SNMP-MIBv1", "jobSchedType"),
        ("VRTS-SNMP-MIBv1", "jobStu"),
        ("VRTS-SNMP-MIBv1", "jobVolpool"),
        ("VRTS-SNMP-MIBv1", "jobErrCode"),
        ("VRTS-SNMP-MIBv1", "jobErrMsg"),
        ("VRTS-SNMP-MIBv1", "jobMaster"),
        ("VRTS-SNMP-MIBv1", "jobErrExpl"),
        ("VRTS-SNMP-MIBv1", "jobErrReco"))
)
if mibBuilder.loadTexts:
    normalJobEvent.setStatus(
        ""
    )

nbuExtEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 101, 0, 1)
)
nbuExtEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuIndex"),
        ("VRTS-SNMP-MIBv1", "nbuNames"),
        ("VRTS-SNMP-MIBv1", "nbuCommand"),
        ("VRTS-SNMP-MIBv1", "nbuResult"),
        ("VRTS-SNMP-MIBv1", "nbuOutput"))
)
if mibBuilder.loadTexts:
    nbuExtEvent.setStatus(
        ""
    )

dbBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 300)
)
dbBackupFailed.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    dbBackupFailed.setStatus(
        ""
    )

dbBackupIsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 301)
)
dbBackupIsDisabled.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    dbBackupIsDisabled.setStatus(
        ""
    )

freezingMedia = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 302)
)
freezingMedia.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    freezingMedia.setStatus(
        ""
    )

suspendingMedia = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 303)
)
suspendingMedia.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    suspendingMedia.setStatus(
        ""
    )

mediaRequiredForRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 304)
)
mediaRequiredForRestore.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    mediaRequiredForRestore.setStatus(
        ""
    )

downedDrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 305)
)
downedDrive.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    downedDrive.setStatus(
        ""
    )

exceededCleaningFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 306)
)
exceededCleaningFrequency.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    exceededCleaningFrequency.setStatus(
        ""
    )

exceededMaxMounts = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 307)
)
exceededMaxMounts.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    exceededMaxMounts.setStatus(
        ""
    )

mountRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 308)
)
mountRequest.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    mountRequest.setStatus(
        ""
    )

noCleaningTape = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 309)
)
noCleaningTape.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    noCleaningTape.setStatus(
        ""
    )

zeroCleaningsLeft = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 1, 251, 0, 310)
)
zeroCleaningsLeft.setObjects(
      *(("VRTS-SNMP-MIBv1", "nbuHost"),
        ("VRTS-SNMP-MIBv1", "nbuErrcode"),
        ("VRTS-SNMP-MIBv1", "nbuErrmsg"))
)
if mibBuilder.loadTexts:
    zeroCleaningsLeft.setStatus(
        ""
    )

errorVxvmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 2, 251, 0, 1)
)
errorVxvmEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "vxvmHost"),
        ("VRTS-SNMP-MIBv1", "vxvmType"),
        ("VRTS-SNMP-MIBv1", "vxvmSeverity"),
        ("VRTS-SNMP-MIBv1", "vxvmErrMsg"))
)
if mibBuilder.loadTexts:
    errorVxvmEvent.setStatus(
        ""
    )

normalVxvmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 2, 251, 0, 2)
)
normalVxvmEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "vxvmHost"),
        ("VRTS-SNMP-MIBv1", "vxvmType"),
        ("VRTS-SNMP-MIBv1", "vxvmSeverity"),
        ("VRTS-SNMP-MIBv1", "vxvmErrMsg"))
)
if mibBuilder.loadTexts:
    normalVxvmEvent.setStatus(
        ""
    )

errorVxfsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 3, 251, 0, 1)
)
errorVxfsEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "vxfsHost"),
        ("VRTS-SNMP-MIBv1", "vxfsMsgcnt"),
        ("VRTS-SNMP-MIBv1", "vxfsSeverity"),
        ("VRTS-SNMP-MIBv1", "vxfsErrCode"),
        ("VRTS-SNMP-MIBv1", "vxfsErrMsg"))
)
if mibBuilder.loadTexts:
    errorVxfsEvent.setStatus(
        ""
    )

normalVxfsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 3, 251, 0, 2)
)
normalVxfsEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "vxfsHost"),
        ("VRTS-SNMP-MIBv1", "vxfsMsgcnt"),
        ("VRTS-SNMP-MIBv1", "vxfsSeverity"),
        ("VRTS-SNMP-MIBv1", "vxfsErrCode"),
        ("VRTS-SNMP-MIBv1", "vxfsErrMsg"))
)
if mibBuilder.loadTexts:
    normalVxfsEvent.setStatus(
        ""
    )

errorVcsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 7, 251, 0, 1)
)
errorVcsEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "vcsTag"),
        ("VRTS-SNMP-MIBv1", "vcsDate"),
        ("VRTS-SNMP-MIBv1", "vcsTime"),
        ("VRTS-SNMP-MIBv1", "vcsErrMsg"),
        ("VRTS-SNMP-MIBv1", "vcsErrCode"),
        ("VRTS-SNMP-MIBv1", "vcsHost"),
        ("VRTS-SNMP-MIBv1", "vcsRes"),
        ("VRTS-SNMP-MIBv1", "vcsAgent"),
        ("VRTS-SNMP-MIBv1", "vcsNode"))
)
if mibBuilder.loadTexts:
    errorVcsEvent.setStatus(
        ""
    )

normalVcsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 7, 251, 0, 2)
)
normalVcsEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "vcsTag"),
        ("VRTS-SNMP-MIBv1", "vcsDate"),
        ("VRTS-SNMP-MIBv1", "vcsTime"),
        ("VRTS-SNMP-MIBv1", "vcsErrMsg"),
        ("VRTS-SNMP-MIBv1", "vcsErrCode"),
        ("VRTS-SNMP-MIBv1", "vcsHost"),
        ("VRTS-SNMP-MIBv1", "vcsRes"),
        ("VRTS-SNMP-MIBv1", "vcsAgent"),
        ("VRTS-SNMP-MIBv1", "vcsNode"))
)
if mibBuilder.loadTexts:
    normalVcsEvent.setStatus(
        ""
    )

logEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 301, 1, 251, 0, 1)
)
logEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "logHost"),
        ("VRTS-SNMP-MIBv1", "logObjName"),
        ("VRTS-SNMP-MIBv1", "logFile"),
        ("VRTS-SNMP-MIBv1", "logErrStrs"),
        ("VRTS-SNMP-MIBv1", "logDesc"),
        ("VRTS-SNMP-MIBv1", "logResolution"),
        ("VRTS-SNMP-MIBv1", "logErrcode"),
        ("VRTS-SNMP-MIBv1", "logErrmsg"))
)
if mibBuilder.loadTexts:
    logEvent.setStatus(
        ""
    )

processEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 301, 2, 251, 0, 1)
)
processEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "psHost"),
        ("VRTS-SNMP-MIBv1", "psId"),
        ("VRTS-SNMP-MIBv1", "psName"),
        ("VRTS-SNMP-MIBv1", "psAttr"),
        ("VRTS-SNMP-MIBv1", "psErrcode"),
        ("VRTS-SNMP-MIBv1", "psErrmsg"))
)
if mibBuilder.loadTexts:
    processEvent.setStatus(
        ""
    )

collectorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 301, 4, 251, 0, 1)
)
collectorEvent.setObjects(
      *(("VRTS-SNMP-MIBv1", "clName"),
        ("VRTS-SNMP-MIBv1", "clHost"),
        ("VRTS-SNMP-MIBv1", "clPrdName"),
        ("VRTS-SNMP-MIBv1", "clObjName"),
        ("VRTS-SNMP-MIBv1", "clAttrName"),
        ("VRTS-SNMP-MIBv1", "clErrcode"),
        ("VRTS-SNMP-MIBv1", "clErrmsg"),
        ("VRTS-SNMP-MIBv1", "clResolution"))
)
if mibBuilder.loadTexts:
    collectorEvent.setStatus(
        ""
    )

coldStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 301, 251, 0, 1)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

heartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 301, 251, 0, 3)
)
if mibBuilder.loadTexts:
    heartBeat.setStatus(
        ""
    )

shutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1035, 301, 251, 0, 5)
)
if mibBuilder.loadTexts:
    shutDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VRTS-SNMP-MIBv1",
    **{"OpEnum": OpEnum,
       "veritas": veritas,
       "netbackup": netbackup,
       "job": job,
       "jobTable": jobTable,
       "jobEntry": jobEntry,
       "jobIndex": jobIndex,
       "jobType": jobType,
       "jobState": jobState,
       "jobClass": jobClass,
       "jobClient": jobClient,
       "jobSched": jobSched,
       "jobSchedType": jobSchedType,
       "jobStu": jobStu,
       "jobVolpool": jobVolpool,
       "jobKbytes": jobKbytes,
       "jobMaster": jobMaster,
       "jobErrExpl": jobErrExpl,
       "jobErrReco": jobErrReco,
       "jobId": jobId,
       "jobErrCode": jobErrCode,
       "jobErrMsg": jobErrMsg,
       "jobErrFix": jobErrFix,
       "jobErrFixCmd": jobErrFixCmd,
       "vrtsNbuJobEvent": vrtsNbuJobEvent,
       "abnormalJobEvent": abnormalJobEvent,
       "normalJobEvent": normalJobEvent,
       "config": config,
       "class": _pysmi_class,
       "classTable": classTable,
       "classEntry": classEntry,
       "classIndex": classIndex,
       "className": className,
       "client": client,
       "clientTable": clientTable,
       "clientEntry": clientEntry,
       "clientIndex": clientIndex,
       "clientName": clientName,
       "sched": sched,
       "schedTable": schedTable,
       "schedEntry": schedEntry,
       "schedIndex": schedIndex,
       "schedName": schedName,
       "stu": stu,
       "stuTable": stuTable,
       "stuEntry": stuEntry,
       "stuIndex": stuIndex,
       "stuName": stuName,
       "media": media,
       "mediaTable": mediaTable,
       "mediaEntry": mediaEntry,
       "mediaIndex": mediaIndex,
       "mediaPool": mediaPool,
       "mediaId": mediaId,
       "mediaType": mediaType,
       "mediaRobotType": mediaRobotType,
       "mediaRobotNum": mediaRobotNum,
       "mediaRobotSlot": mediaRobotSlot,
       "mediaSideFace": mediaSideFace,
       "mediaRetLevel": mediaRetLevel,
       "mediaSize": mediaSize,
       "mediaStatus": mediaStatus,
       "volpool": volpool,
       "volpoolTable": volpoolTable,
       "volpoolEntry": volpoolEntry,
       "volpoolIndex": volpoolIndex,
       "volpoolName": volpoolName,
       "robot": robot,
       "robotTable": robotTable,
       "robotEntry": robotEntry,
       "robotIndex": robotIndex,
       "robotName": robotName,
       "drive": drive,
       "driveTable": driveTable,
       "driveEntry": driveEntry,
       "driveIndex": driveIndex,
       "driveName": driveName,
       "tape": tape,
       "tapeTable": tapeTable,
       "tapeEntry": tapeEntry,
       "tapeIndex": tapeIndex,
       "tapeName": tapeName,
       "dr": dr,
       "vault": vault,
       "vaultTable": vaultTable,
       "vaultEntry": vaultEntry,
       "vaultIndex": vaultIndex,
       "vaultName": vaultName,
       "nbuExtTable": nbuExtTable,
       "nbuEntry": nbuEntry,
       "nbuIndex": nbuIndex,
       "nbuNames": nbuNames,
       "nbuCommand": nbuCommand,
       "nbuCtlFlag": nbuCtlFlag,
       "nbuResFile": nbuResFile,
       "nbuLockFile": nbuLockFile,
       "nbuTimeout": nbuTimeout,
       "nbuFreq": nbuFreq,
       "nbuResult": nbuResult,
       "nbuOutput": nbuOutput,
       "nbuErrFix": nbuErrFix,
       "nbuErrFixCmd": nbuErrFixCmd,
       "vrtsNbuExtEvent": vrtsNbuExtEvent,
       "nbuExtEvent": nbuExtEvent,
       "nbuTrapVars": nbuTrapVars,
       "nbuHost": nbuHost,
       "nbuErrcode": nbuErrcode,
       "nbuErrmsg": nbuErrmsg,
       "vrtsNbuEvents": vrtsNbuEvents,
       "dbBackupFailed": dbBackupFailed,
       "dbBackupIsDisabled": dbBackupIsDisabled,
       "freezingMedia": freezingMedia,
       "suspendingMedia": suspendingMedia,
       "mediaRequiredForRestore": mediaRequiredForRestore,
       "downedDrive": downedDrive,
       "exceededCleaningFrequency": exceededCleaningFrequency,
       "exceededMaxMounts": exceededMaxMounts,
       "mountRequest": mountRequest,
       "noCleaningTape": noCleaningTape,
       "zeroCleaningsLeft": zeroCleaningsLeft,
       "vxvm": vxvm,
       "vmExtTable": vmExtTable,
       "vmEntry": vmEntry,
       "vmIndex": vmIndex,
       "vmNames": vmNames,
       "vmCommand": vmCommand,
       "vmCtlFlag": vmCtlFlag,
       "vmResult": vmResult,
       "vmOutput": vmOutput,
       "vmErrFix": vmErrFix,
       "vmErrFixCmd": vmErrFixCmd,
       "vxvmEventAttrs": vxvmEventAttrs,
       "vxvmHost": vxvmHost,
       "vxvmType": vxvmType,
       "vxvmSeverity": vxvmSeverity,
       "vxvmErrExpl": vxvmErrExpl,
       "vxvmErrReco": vxvmErrReco,
       "vxvmErrCode": vxvmErrCode,
       "vxvmErrMsg": vxvmErrMsg,
       "vrtsVxvmEvent": vrtsVxvmEvent,
       "errorVxvmEvent": errorVxvmEvent,
       "normalVxvmEvent": normalVxvmEvent,
       "vxfs": vxfs,
       "fsExtTable": fsExtTable,
       "fsEntry": fsEntry,
       "fsIndex": fsIndex,
       "fsNames": fsNames,
       "fsCommand": fsCommand,
       "fsCtlFlag": fsCtlFlag,
       "fsResult": fsResult,
       "fsOutput": fsOutput,
       "fsErrFix": fsErrFix,
       "fsErrFixCmd": fsErrFixCmd,
       "vxfsEventAttrs": vxfsEventAttrs,
       "vxfsHost": vxfsHost,
       "vxfsMsgcnt": vxfsMsgcnt,
       "vxfsSeverity": vxfsSeverity,
       "vxfsErrExpl": vxfsErrExpl,
       "vxfsErrReco": vxfsErrReco,
       "vxfsErrCode": vxfsErrCode,
       "vxfsErrMsg": vxfsErrMsg,
       "vrtsVxfsEvent": vrtsVxfsEvent,
       "errorVxfsEvent": errorVxfsEvent,
       "normalVxfsEvent": normalVxfsEvent,
       "vcs": vcs,
       "vcsExtTable": vcsExtTable,
       "vcsEntry": vcsEntry,
       "vcsIndex": vcsIndex,
       "vcsNames": vcsNames,
       "vcsCommand": vcsCommand,
       "vcsCtlFlag": vcsCtlFlag,
       "vcsResult": vcsResult,
       "vcsOutput": vcsOutput,
       "vcsErrFix": vcsErrFix,
       "vcsErrFixCmd": vcsErrFixCmd,
       "vcsEventAttrs": vcsEventAttrs,
       "vcsTag": vcsTag,
       "vcsHost": vcsHost,
       "vcsRes": vcsRes,
       "vcsResStat": vcsResStat,
       "vcsAgent": vcsAgent,
       "vcsNode": vcsNode,
       "vcsDate": vcsDate,
       "vcsTime": vcsTime,
       "vcsErrExpl": vcsErrExpl,
       "vcsErrReco": vcsErrReco,
       "vcsErrCode": vcsErrCode,
       "vcsErrMsg": vcsErrMsg,
       "vrtsVcsEvent": vrtsVcsEvent,
       "errorVcsEvent": errorVcsEvent,
       "normalVcsEvent": normalVcsEvent,
       "commonObjects": commonObjects,
       "log": log,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "logHost": logHost,
       "logPrdCode": logPrdCode,
       "logPrdName": logPrdName,
       "logObjName": logObjName,
       "logAttrName": logAttrName,
       "logFile": logFile,
       "logErrStrs": logErrStrs,
       "logDesc": logDesc,
       "logResolution": logResolution,
       "logErrFlag": logErrFlag,
       "logErrcode": logErrcode,
       "logErrmsg": logErrmsg,
       "logErrFix": logErrFix,
       "logErrFixCmd": logErrFixCmd,
       "vrtsLogMonitor": vrtsLogMonitor,
       "logEvent": logEvent,
       "process": process,
       "psTable": psTable,
       "psEntry": psEntry,
       "psIndex": psIndex,
       "psId": psId,
       "psName": psName,
       "psAttr": psAttr,
       "psMin": psMin,
       "psMax": psMax,
       "psCount": psCount,
       "psCpuPct": psCpuPct,
       "psBytesIO": psBytesIO,
       "psSlpMax": psSlpMax,
       "psHost": psHost,
       "psErrFlag": psErrFlag,
       "psErrcode": psErrcode,
       "psErrmsg": psErrmsg,
       "psErrFix": psErrFix,
       "psErrFixCmd": psErrFixCmd,
       "vrtsProcessMonitor": vrtsProcessMonitor,
       "processEvent": processEvent,
       "collector": collector,
       "clTable": clTable,
       "clEntry": clEntry,
       "clIndex": clIndex,
       "clName": clName,
       "clHost": clHost,
       "clScript": clScript,
       "clSampFreq": clSampFreq,
       "clFreq": clFreq,
       "clTimeout": clTimeout,
       "clPrdCode": clPrdCode,
       "clPrdName": clPrdName,
       "clObjName": clObjName,
       "clAttrName": clAttrName,
       "clLow": clLow,
       "clHigh": clHigh,
       "clCount": clCount,
       "clObjNames": clObjNames,
       "clResolution": clResolution,
       "clErrFlag": clErrFlag,
       "clErrcode": clErrcode,
       "clErrmsg": clErrmsg,
       "clErrFix": clErrFix,
       "clErrFixCmd": clErrFixCmd,
       "vrtsCollectorMonitor": vrtsCollectorMonitor,
       "collectorEvent": collectorEvent,
       "frequency": frequency,
       "messagefreq": messagefreq,
       "processfreq": processfreq,
       "vxvmSamplefreq": vxvmSamplefreq,
       "vxvmCheckfreq": vxvmCheckfreq,
       "vxvmTimeout": vxvmTimeout,
       "vxfsSamplefreq": vxfsSamplefreq,
       "vxfsCheckfreq": vxfsCheckfreq,
       "vxfsTimeout": vxfsTimeout,
       "vrtsEneMonitor": vrtsEneMonitor,
       "coldStart": coldStart,
       "heartBeat": heartBeat,
       "shutDown": shutDown}
)
