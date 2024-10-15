# SNMP MIB module (EMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:23 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class UInt32(Gauge32):
    """Custom type UInt32 based on Gauge32"""




class StateValues(Integer32):
    """Custom type StateValues based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 0),
          ("mixed", 2),
          ("state-na", 3))
    )





class DirectorType(Integer32):
    """Custom type DirectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("channel-adapter", 3),
          ("disk-adapter", 2),
          ("escon-adapter", 5),
          ("fibre-channel", 0),
          ("memory-board", 4),
          ("rdf-adapter-bi", 8),
          ("rdf-adapter-r1", 6),
          ("rdf-adapter-r2", 7),
          ("scsi-adapter", 1))
    )





class DirectorStatus(Integer32):
    """Custom type DirectorStatus based on Integer32"""
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
        *(("dead", 2),
          ("offline", 1),
          ("online", 0),
          ("unknown", 3))
    )





class PortStatus(Integer32):
    """Custom type PortStatus based on Integer32"""
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
        *(("off", 2),
          ("on", 1),
          ("status-na", 0),
          ("wd", 3))
    )





class SCSIWidth(Integer32):
    """Custom type SCSIWidth based on Integer32"""
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
        *(("narrow", 1),
          ("not-applicable", 0),
          ("ultra", 3),
          ("wide", 2))
    )





class DeviceStatus(Integer32):
    """Custom type DeviceStatus based on Integer32"""
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
        *(("mixed", 4),
          ("not-applicable", 3),
          ("not-ready", 1),
          ("ready", 0),
          ("write-disabled", 2))
    )





class DeviceType(Integer32):
    """Custom type DeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              128)
        )
    )
    namedValues = NamedValues(
        *(("hot-spare", 128),
          ("local-data", 2),
          ("not-applicable", 1),
          ("raid-s", 4),
          ("raid-s-parity", 8),
          ("remote-r1-data", 16),
          ("remote-r2-data", 32))
    )





class DeviceEmulation(Integer32):
    """Custom type DeviceEmulation based on Integer32"""
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
        *(("as400", 2),
          ("ckd-3380", 5),
          ("ckd-3390", 6),
          ("emulation-na", 0),
          ("fba", 1),
          ("icl", 3),
          ("unisys-fba", 4))
    )





class SCSIMethod(Integer32):
    """Custom type SCSIMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 2),
          ("method-na", 0),
          ("synchronous", 1))
    )





class BCVState(Integer32):
    """Custom type BCVState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("in-progress", 1),
          ("invalid", 10),
          ("never-established", 0),
          ("restore-in-progress", 7),
          ("restored", 8),
          ("split", 5),
          ("split-before-restore", 9),
          ("split-before-sync", 4),
          ("split-in-progress", 3),
          ("split-no-incremental", 6),
          ("synchronous", 2))
    )





class RDFPairState(Integer32):
    """Custom type RDFPairState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110)
        )
    )
    namedValues = NamedValues(
        *(("failed-over", 105),
          ("invalid", 100),
          ("mixed", 109),
          ("partitioned", 106),
          ("r1-updated", 107),
          ("r1-updinprog", 108),
          ("split", 103),
          ("state-na", 110),
          ("suspended", 104),
          ("synchronized", 102),
          ("syncinprog", 101))
    )





class RDFType(Integer32):
    """Custom type RDFType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("r1", 0),
          ("r2", 1))
    )





class RDFMode(Integer32):
    """Custom type RDFMode based on Integer32"""
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
        *(("adaptive-copy", 2),
          ("mixed", 3),
          ("rdf-mode-na", 4),
          ("semi-synchronous", 1),
          ("synchronous", 0))
    )





class RDFAdaptiveCopy(Integer32):
    """Custom type RDFAdaptiveCopy based on Integer32"""
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
        *(("ac-na", 4),
          ("disabled", 0),
          ("disk-mode", 2),
          ("mixed", 3),
          ("wp-mode", 1))
    )





class RDFLinkConfig(Integer32):
    """Custom type RDFLinkConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("escon", 1),
          ("na", 3),
          ("t3", 2))
    )





class RDDFTransientState(Integer32):
    """Custom type RDDFTransientState based on Integer32"""
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
        *(("offline", 2),
          ("offline-pend", 3),
          ("online", 4),
          ("transient-state-na", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Emc_ObjectIdentity = ObjectIdentity
emc = _Emc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139)
)
_EmcSymmetrix_ObjectIdentity = ObjectIdentity
emcSymmetrix = _EmcSymmetrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1)
)
_EmcControlCenter_Object = MibTable
emcControlCenter = _EmcControlCenter_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1)
)
if mibBuilder.loadTexts:
    emcControlCenter.setStatus("obsolete")
_EsmVariables_Object = MibTableRow
esmVariables = _EsmVariables_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1)
)
esmVariables.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    esmVariables.setStatus("obsolete")
_EmcSymCnfg_Type = Opaque
_EmcSymCnfg_Object = MibTableColumn
emcSymCnfg = _EmcSymCnfg_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 1),
    _EmcSymCnfg_Type()
)
emcSymCnfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymCnfg.setStatus("obsolete")
_EmcSymDiskCfg_Type = Opaque
_EmcSymDiskCfg_Object = MibTableColumn
emcSymDiskCfg = _EmcSymDiskCfg_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 2),
    _EmcSymDiskCfg_Type()
)
emcSymDiskCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymDiskCfg.setStatus("obsolete")
_EmcSymMirrorDiskCfg_Type = Opaque
_EmcSymMirrorDiskCfg_Object = MibTableColumn
emcSymMirrorDiskCfg = _EmcSymMirrorDiskCfg_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 3),
    _EmcSymMirrorDiskCfg_Type()
)
emcSymMirrorDiskCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymMirrorDiskCfg.setStatus("obsolete")
_EmcSymMirror3DiskCfg_Type = Opaque
_EmcSymMirror3DiskCfg_Object = MibTableColumn
emcSymMirror3DiskCfg = _EmcSymMirror3DiskCfg_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 4),
    _EmcSymMirror3DiskCfg_Type()
)
emcSymMirror3DiskCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymMirror3DiskCfg.setStatus("obsolete")
_EmcSymMirror4DiskCfg_Type = Opaque
_EmcSymMirror4DiskCfg_Object = MibTableColumn
emcSymMirror4DiskCfg = _EmcSymMirror4DiskCfg_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 5),
    _EmcSymMirror4DiskCfg_Type()
)
emcSymMirror4DiskCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymMirror4DiskCfg.setStatus("obsolete")
_EmcSymStatistics_Type = Opaque
_EmcSymStatistics_Object = MibTableColumn
emcSymStatistics = _EmcSymStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 6),
    _EmcSymStatistics_Type()
)
emcSymStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymStatistics.setStatus("obsolete")
_EmcSymUtilA7_Type = DisplayString
_EmcSymUtilA7_Object = MibTableColumn
emcSymUtilA7 = _EmcSymUtilA7_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 7),
    _EmcSymUtilA7_Type()
)
emcSymUtilA7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymUtilA7.setStatus("obsolete")
_EmcSymRdfMaint_Type = Opaque
_EmcSymRdfMaint_Object = MibTableColumn
emcSymRdfMaint = _EmcSymRdfMaint_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 8),
    _EmcSymRdfMaint_Type()
)
emcSymRdfMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymRdfMaint.setStatus("obsolete")
_EmcSymWinConfig_Type = Opaque
_EmcSymWinConfig_Object = MibTableColumn
emcSymWinConfig = _EmcSymWinConfig_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 9),
    _EmcSymWinConfig_Type()
)
emcSymWinConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymWinConfig.setStatus("obsolete")
_EmcSymUtil99_Type = DisplayString
_EmcSymUtil99_Object = MibTableColumn
emcSymUtil99 = _EmcSymUtil99_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 10),
    _EmcSymUtil99_Type()
)
emcSymUtil99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymUtil99.setStatus("obsolete")
_EmcSymDir_Type = Opaque
_EmcSymDir_Object = MibTableColumn
emcSymDir = _EmcSymDir_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 11),
    _EmcSymDir_Type()
)
emcSymDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymDir.setStatus("obsolete")
_EmcSymDevStats_Type = Opaque
_EmcSymDevStats_Object = MibTableColumn
emcSymDevStats = _EmcSymDevStats_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 12),
    _EmcSymDevStats_Type()
)
emcSymDevStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymDevStats.setStatus("obsolete")
_EmcSymSumStatus_Type = Opaque
_EmcSymSumStatus_Object = MibTableColumn
emcSymSumStatus = _EmcSymSumStatus_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 13),
    _EmcSymSumStatus_Type()
)
emcSymSumStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymSumStatus.setStatus("obsolete")
_EmcRatiosOutofRange_Type = DisplayString
_EmcRatiosOutofRange_Object = MibTableColumn
emcRatiosOutofRange = _EmcRatiosOutofRange_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 14),
    _EmcRatiosOutofRange_Type()
)
emcRatiosOutofRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcRatiosOutofRange.setStatus("obsolete")
_EmcSymPortStats_Type = Opaque
_EmcSymPortStats_Object = MibTableColumn
emcSymPortStats = _EmcSymPortStats_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 15),
    _EmcSymPortStats_Type()
)
emcSymPortStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymPortStats.setStatus("obsolete")
_EmcSymBCVDevice_Type = Opaque
_EmcSymBCVDevice_Object = MibTableColumn
emcSymBCVDevice = _EmcSymBCVDevice_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 16),
    _EmcSymBCVDevice_Type()
)
emcSymBCVDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymBCVDevice.setStatus("obsolete")
_EmcSymSaitInfo_Type = Opaque
_EmcSymSaitInfo_Object = MibTableColumn
emcSymSaitInfo = _EmcSymSaitInfo_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 17),
    _EmcSymSaitInfo_Type()
)
emcSymSaitInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymSaitInfo.setStatus("obsolete")
_EmcSymTimefinderInfo_Type = Opaque
_EmcSymTimefinderInfo_Object = MibTableColumn
emcSymTimefinderInfo = _EmcSymTimefinderInfo_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 18),
    _EmcSymTimefinderInfo_Type()
)
emcSymTimefinderInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymTimefinderInfo.setStatus("obsolete")
_EmcSymSRDFInfo_Type = Opaque
_EmcSymSRDFInfo_Object = MibTableColumn
emcSymSRDFInfo = _EmcSymSRDFInfo_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 19),
    _EmcSymSRDFInfo_Type()
)
emcSymSRDFInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymSRDFInfo.setStatus("obsolete")
_EmcSymPhysDevStats_Type = Opaque
_EmcSymPhysDevStats_Object = MibTableColumn
emcSymPhysDevStats = _EmcSymPhysDevStats_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 20),
    _EmcSymPhysDevStats_Type()
)
emcSymPhysDevStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymPhysDevStats.setStatus("obsolete")
_EmcSymSumStatusErrorCodes_Type = DisplayString
_EmcSymSumStatusErrorCodes_Object = MibTableColumn
emcSymSumStatusErrorCodes = _EmcSymSumStatusErrorCodes_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 1, 1, 98),
    _EmcSymSumStatusErrorCodes_Type()
)
emcSymSumStatusErrorCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymSumStatusErrorCodes.setStatus("obsolete")
_SystemCalls_ObjectIdentity = ObjectIdentity
systemCalls = _SystemCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2)
)
_Informational_ObjectIdentity = ObjectIdentity
informational = _Informational_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1)
)
_SystemInformation_ObjectIdentity = ObjectIdentity
systemInformation = _SystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257)
)
_SystemInfoHeaderTable_Object = MibTable
systemInfoHeaderTable = _SystemInfoHeaderTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 1)
)
if mibBuilder.loadTexts:
    systemInfoHeaderTable.setStatus("obsolete")
_SystemInfoHeaderEntry_Object = MibTableRow
systemInfoHeaderEntry = _SystemInfoHeaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 1, 1)
)
systemInfoHeaderEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    systemInfoHeaderEntry.setStatus("obsolete")
_SysinfoBuffer_Type = Opaque
_SysinfoBuffer_Object = MibTableColumn
sysinfoBuffer = _SysinfoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 1, 1, 1),
    _SysinfoBuffer_Type()
)
sysinfoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBuffer.setStatus("obsolete")
_SysinfoNumberofRecords_Type = Integer32
_SysinfoNumberofRecords_Object = MibTableColumn
sysinfoNumberofRecords = _SysinfoNumberofRecords_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 1, 1, 2),
    _SysinfoNumberofRecords_Type()
)
sysinfoNumberofRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoNumberofRecords.setStatus("obsolete")
_SysinfoRecordSize_Type = Integer32
_SysinfoRecordSize_Object = MibTableColumn
sysinfoRecordSize = _SysinfoRecordSize_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 1, 1, 3),
    _SysinfoRecordSize_Type()
)
sysinfoRecordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoRecordSize.setStatus("obsolete")
_SysinfoFirstRecordNumber_Type = Integer32
_SysinfoFirstRecordNumber_Object = MibTableColumn
sysinfoFirstRecordNumber = _SysinfoFirstRecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 1, 1, 4),
    _SysinfoFirstRecordNumber_Type()
)
sysinfoFirstRecordNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoFirstRecordNumber.setStatus("obsolete")
_SysinfoMaxRecords_Type = Integer32
_SysinfoMaxRecords_Object = MibTableColumn
sysinfoMaxRecords = _SysinfoMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 1, 1, 5),
    _SysinfoMaxRecords_Type()
)
sysinfoMaxRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoMaxRecords.setStatus("obsolete")
_SysinfoRecordsTable_Object = MibTable
sysinfoRecordsTable = _SysinfoRecordsTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 2)
)
if mibBuilder.loadTexts:
    sysinfoRecordsTable.setStatus("obsolete")
_SysinfoRecordsEntry_Object = MibTableRow
sysinfoRecordsEntry = _SysinfoRecordsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 2, 1)
)
sysinfoRecordsEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    sysinfoRecordsEntry.setStatus("obsolete")


class _SysinfoSerialNumber_Type(DisplayString):
    """Custom type sysinfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SysinfoSerialNumber_Type.__name__ = "DisplayString"
_SysinfoSerialNumber_Object = MibTableColumn
sysinfoSerialNumber = _SysinfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 2, 1, 1),
    _SysinfoSerialNumber_Type()
)
sysinfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoSerialNumber.setStatus("obsolete")
_SysinfoNumberofDirectors_Type = Integer32
_SysinfoNumberofDirectors_Object = MibTableColumn
sysinfoNumberofDirectors = _SysinfoNumberofDirectors_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 2, 1, 19),
    _SysinfoNumberofDirectors_Type()
)
sysinfoNumberofDirectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoNumberofDirectors.setStatus("obsolete")
_SysinfoNumberofVolumes_Type = Integer32
_SysinfoNumberofVolumes_Object = MibTableColumn
sysinfoNumberofVolumes = _SysinfoNumberofVolumes_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 2, 1, 23),
    _SysinfoNumberofVolumes_Type()
)
sysinfoNumberofVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoNumberofVolumes.setStatus("obsolete")
_SysinfoMemorySize_Type = Opaque
_SysinfoMemorySize_Object = MibTableColumn
sysinfoMemorySize = _SysinfoMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 257, 2, 1, 25),
    _SysinfoMemorySize_Type()
)
sysinfoMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoMemorySize.setStatus("obsolete")
_SystemCodes_ObjectIdentity = ObjectIdentity
systemCodes = _SystemCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258)
)
_SystemCodesTable_Object = MibTable
systemCodesTable = _SystemCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 1)
)
if mibBuilder.loadTexts:
    systemCodesTable.setStatus("obsolete")
_SystemCodesEntry_Object = MibTableRow
systemCodesEntry = _SystemCodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 1, 1)
)
systemCodesEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    systemCodesEntry.setStatus("obsolete")
_SyscodesBuffer_Type = Opaque
_SyscodesBuffer_Object = MibTableColumn
syscodesBuffer = _SyscodesBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 1, 1, 1),
    _SyscodesBuffer_Type()
)
syscodesBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syscodesBuffer.setStatus("obsolete")
_SyscodesNumberofRecords_Type = Integer32
_SyscodesNumberofRecords_Object = MibTableColumn
syscodesNumberofRecords = _SyscodesNumberofRecords_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 1, 1, 2),
    _SyscodesNumberofRecords_Type()
)
syscodesNumberofRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syscodesNumberofRecords.setStatus("obsolete")
_SyscodesRecordSize_Type = Integer32
_SyscodesRecordSize_Object = MibTableColumn
syscodesRecordSize = _SyscodesRecordSize_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 1, 1, 3),
    _SyscodesRecordSize_Type()
)
syscodesRecordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syscodesRecordSize.setStatus("obsolete")
_SyscodesFirstRecordNumber_Type = Integer32
_SyscodesFirstRecordNumber_Object = MibTableColumn
syscodesFirstRecordNumber = _SyscodesFirstRecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 1, 1, 4),
    _SyscodesFirstRecordNumber_Type()
)
syscodesFirstRecordNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syscodesFirstRecordNumber.setStatus("obsolete")
_SyscodesMaxRecords_Type = Integer32
_SyscodesMaxRecords_Object = MibTableColumn
syscodesMaxRecords = _SyscodesMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 1, 1, 5),
    _SyscodesMaxRecords_Type()
)
syscodesMaxRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syscodesMaxRecords.setStatus("obsolete")
_SystemCodesRecordsTable_Object = MibTable
systemCodesRecordsTable = _SystemCodesRecordsTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2)
)
if mibBuilder.loadTexts:
    systemCodesRecordsTable.setStatus("obsolete")
_SystemCodesRecordsEntry_Object = MibTableRow
systemCodesRecordsEntry = _SystemCodesRecordsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1)
)
systemCodesRecordsEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "syscodesDirectorNum"),
)
if mibBuilder.loadTexts:
    systemCodesRecordsEntry.setStatus("obsolete")


class _SyscodesDirectorType_Type(Integer32):
    """Custom type syscodesDirectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disk-adapter", 4),
          ("escon-adapter", 2),
          ("fiber-adapter", 6),
          ("parallel-adapter", 1),
          ("remote-adapter", 5),
          ("scsi-adapter", 3))
    )


_SyscodesDirectorType_Type.__name__ = "Integer32"
_SyscodesDirectorType_Object = MibTableColumn
syscodesDirectorType = _SyscodesDirectorType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 1),
    _SyscodesDirectorType_Type()
)
syscodesDirectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syscodesDirectorType.setStatus("obsolete")
_SyscodesDirectorNum_Type = Integer32
_SyscodesDirectorNum_Object = MibTableColumn
syscodesDirectorNum = _SyscodesDirectorNum_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 2),
    _SyscodesDirectorNum_Type()
)
syscodesDirectorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syscodesDirectorNum.setStatus("obsolete")


class _EmulCodeType_Type(DisplayString):
    """Custom type emulCodeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_EmulCodeType_Type.__name__ = "DisplayString"
_EmulCodeType_Object = MibTableColumn
emulCodeType = _EmulCodeType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 5),
    _EmulCodeType_Type()
)
emulCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emulCodeType.setStatus("obsolete")
_EmulVersion_Type = Integer32
_EmulVersion_Object = MibTableColumn
emulVersion = _EmulVersion_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 6),
    _EmulVersion_Type()
)
emulVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emulVersion.setStatus("obsolete")
_EmulDate_Type = Opaque
_EmulDate_Object = MibTableColumn
emulDate = _EmulDate_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 7),
    _EmulDate_Type()
)
emulDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emulDate.setStatus("obsolete")
_EmulChecksum_Type = Integer32
_EmulChecksum_Object = MibTableColumn
emulChecksum = _EmulChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 8),
    _EmulChecksum_Type()
)
emulChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emulChecksum.setStatus("obsolete")
_EmulMTPF_Type = Integer32
_EmulMTPF_Object = MibTableColumn
emulMTPF = _EmulMTPF_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 9),
    _EmulMTPF_Type()
)
emulMTPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emulMTPF.setStatus("obsolete")
_EmulFileCount_Type = Integer32
_EmulFileCount_Object = MibTableColumn
emulFileCount = _EmulFileCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 10),
    _EmulFileCount_Type()
)
emulFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emulFileCount.setStatus("obsolete")


class _ImplCodeType_Type(DisplayString):
    """Custom type implCodeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ImplCodeType_Type.__name__ = "DisplayString"
_ImplCodeType_Object = MibTableColumn
implCodeType = _ImplCodeType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 11),
    _ImplCodeType_Type()
)
implCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    implCodeType.setStatus("obsolete")
_ImplVersion_Type = Integer32
_ImplVersion_Object = MibTableColumn
implVersion = _ImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 12),
    _ImplVersion_Type()
)
implVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    implVersion.setStatus("obsolete")
_ImplDate_Type = Opaque
_ImplDate_Object = MibTableColumn
implDate = _ImplDate_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 13),
    _ImplDate_Type()
)
implDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    implDate.setStatus("obsolete")
_ImplChecksum_Type = Integer32
_ImplChecksum_Object = MibTableColumn
implChecksum = _ImplChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 14),
    _ImplChecksum_Type()
)
implChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    implChecksum.setStatus("obsolete")
_ImplMTPF_Type = Integer32
_ImplMTPF_Object = MibTableColumn
implMTPF = _ImplMTPF_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 15),
    _ImplMTPF_Type()
)
implMTPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    implMTPF.setStatus("obsolete")
_ImplFileCount_Type = Integer32
_ImplFileCount_Object = MibTableColumn
implFileCount = _ImplFileCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 16),
    _ImplFileCount_Type()
)
implFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    implFileCount.setStatus("obsolete")


class _InitCodeType_Type(DisplayString):
    """Custom type initCodeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_InitCodeType_Type.__name__ = "DisplayString"
_InitCodeType_Object = MibTableColumn
initCodeType = _InitCodeType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 17),
    _InitCodeType_Type()
)
initCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initCodeType.setStatus("obsolete")
_InitVersion_Type = Integer32
_InitVersion_Object = MibTableColumn
initVersion = _InitVersion_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 18),
    _InitVersion_Type()
)
initVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initVersion.setStatus("obsolete")
_InitDate_Type = Opaque
_InitDate_Object = MibTableColumn
initDate = _InitDate_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 19),
    _InitDate_Type()
)
initDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initDate.setStatus("obsolete")
_InitChecksum_Type = Integer32
_InitChecksum_Object = MibTableColumn
initChecksum = _InitChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 20),
    _InitChecksum_Type()
)
initChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initChecksum.setStatus("obsolete")
_InitMTPF_Type = Integer32
_InitMTPF_Object = MibTableColumn
initMTPF = _InitMTPF_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 21),
    _InitMTPF_Type()
)
initMTPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initMTPF.setStatus("obsolete")
_InitFileCount_Type = Integer32
_InitFileCount_Object = MibTableColumn
initFileCount = _InitFileCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 22),
    _InitFileCount_Type()
)
initFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initFileCount.setStatus("obsolete")


class _EscnCodeType_Type(DisplayString):
    """Custom type escnCodeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_EscnCodeType_Type.__name__ = "DisplayString"
_EscnCodeType_Object = MibTableColumn
escnCodeType = _EscnCodeType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 23),
    _EscnCodeType_Type()
)
escnCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escnCodeType.setStatus("obsolete")
_EscnVersion_Type = Integer32
_EscnVersion_Object = MibTableColumn
escnVersion = _EscnVersion_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 24),
    _EscnVersion_Type()
)
escnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escnVersion.setStatus("obsolete")
_EscnDate_Type = Opaque
_EscnDate_Object = MibTableColumn
escnDate = _EscnDate_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 25),
    _EscnDate_Type()
)
escnDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escnDate.setStatus("obsolete")
_EscnChecksum_Type = Integer32
_EscnChecksum_Object = MibTableColumn
escnChecksum = _EscnChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 26),
    _EscnChecksum_Type()
)
escnChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escnChecksum.setStatus("obsolete")
_EscnMTPF_Type = Integer32
_EscnMTPF_Object = MibTableColumn
escnMTPF = _EscnMTPF_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 27),
    _EscnMTPF_Type()
)
escnMTPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escnMTPF.setStatus("obsolete")
_EscnFileCount_Type = Integer32
_EscnFileCount_Object = MibTableColumn
escnFileCount = _EscnFileCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 258, 2, 1, 28),
    _EscnFileCount_Type()
)
escnFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escnFileCount.setStatus("obsolete")
_DiskAdapterDeviceConfiguration_ObjectIdentity = ObjectIdentity
diskAdapterDeviceConfiguration = _DiskAdapterDeviceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273)
)
_DiskAdapterDeviceConfigurationTable_Object = MibTable
diskAdapterDeviceConfigurationTable = _DiskAdapterDeviceConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 1)
)
if mibBuilder.loadTexts:
    diskAdapterDeviceConfigurationTable.setStatus("obsolete")
_DiskAdapterDeviceConfigurationEntry_Object = MibTableRow
diskAdapterDeviceConfigurationEntry = _DiskAdapterDeviceConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 1, 1)
)
diskAdapterDeviceConfigurationEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    diskAdapterDeviceConfigurationEntry.setStatus("obsolete")
_DadcnfigBuffer_Type = Opaque
_DadcnfigBuffer_Object = MibTableColumn
dadcnfigBuffer = _DadcnfigBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 1, 1, 1),
    _DadcnfigBuffer_Type()
)
dadcnfigBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigBuffer.setStatus("obsolete")
_DadcnfigNumberofRecords_Type = Integer32
_DadcnfigNumberofRecords_Object = MibTableColumn
dadcnfigNumberofRecords = _DadcnfigNumberofRecords_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 1, 1, 2),
    _DadcnfigNumberofRecords_Type()
)
dadcnfigNumberofRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigNumberofRecords.setStatus("obsolete")
_DadcnfigRecordSize_Type = Integer32
_DadcnfigRecordSize_Object = MibTableColumn
dadcnfigRecordSize = _DadcnfigRecordSize_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 1, 1, 3),
    _DadcnfigRecordSize_Type()
)
dadcnfigRecordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigRecordSize.setStatus("obsolete")
_DadcnfigFirstRecordNumber_Type = Integer32
_DadcnfigFirstRecordNumber_Object = MibTableColumn
dadcnfigFirstRecordNumber = _DadcnfigFirstRecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 1, 1, 4),
    _DadcnfigFirstRecordNumber_Type()
)
dadcnfigFirstRecordNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigFirstRecordNumber.setStatus("obsolete")
_DadcnfigMaxRecords_Type = Integer32
_DadcnfigMaxRecords_Object = MibTableColumn
dadcnfigMaxRecords = _DadcnfigMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 1, 1, 5),
    _DadcnfigMaxRecords_Type()
)
dadcnfigMaxRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMaxRecords.setStatus("obsolete")
_DadcnfigDeviceRecordsTable_Object = MibTable
dadcnfigDeviceRecordsTable = _DadcnfigDeviceRecordsTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2)
)
if mibBuilder.loadTexts:
    dadcnfigDeviceRecordsTable.setStatus("obsolete")
_DadcnfigDeviceRecordsEntry_Object = MibTableRow
dadcnfigDeviceRecordsEntry = _DadcnfigDeviceRecordsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1)
)
dadcnfigDeviceRecordsEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "dadcnfigSymmNumber"),
)
if mibBuilder.loadTexts:
    dadcnfigDeviceRecordsEntry.setStatus("obsolete")
_DadcnfigSymmNumber_Type = Integer32
_DadcnfigSymmNumber_Object = MibTableColumn
dadcnfigSymmNumber = _DadcnfigSymmNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 1),
    _DadcnfigSymmNumber_Type()
)
dadcnfigSymmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigSymmNumber.setStatus("obsolete")
_DadcnfigMirrors_Type = Opaque
_DadcnfigMirrors_Object = MibTableColumn
dadcnfigMirrors = _DadcnfigMirrors_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 8),
    _DadcnfigMirrors_Type()
)
dadcnfigMirrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirrors.setStatus("obsolete")
_DadcnfigMirror1Director_Type = Integer32
_DadcnfigMirror1Director_Object = MibTableColumn
dadcnfigMirror1Director = _DadcnfigMirror1Director_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 9),
    _DadcnfigMirror1Director_Type()
)
dadcnfigMirror1Director.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirror1Director.setStatus("obsolete")
_DadcnfigMirror1Interface_Type = Integer32
_DadcnfigMirror1Interface_Object = MibTableColumn
dadcnfigMirror1Interface = _DadcnfigMirror1Interface_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 10),
    _DadcnfigMirror1Interface_Type()
)
dadcnfigMirror1Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirror1Interface.setStatus("obsolete")
_DadcnfigMirror2Director_Type = Integer32
_DadcnfigMirror2Director_Object = MibTableColumn
dadcnfigMirror2Director = _DadcnfigMirror2Director_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 11),
    _DadcnfigMirror2Director_Type()
)
dadcnfigMirror2Director.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirror2Director.setStatus("obsolete")
_DadcnfigMirror2Interface_Type = Integer32
_DadcnfigMirror2Interface_Object = MibTableColumn
dadcnfigMirror2Interface = _DadcnfigMirror2Interface_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 12),
    _DadcnfigMirror2Interface_Type()
)
dadcnfigMirror2Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirror2Interface.setStatus("obsolete")
_DadcnfigMirror3Director_Type = Integer32
_DadcnfigMirror3Director_Object = MibTableColumn
dadcnfigMirror3Director = _DadcnfigMirror3Director_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 13),
    _DadcnfigMirror3Director_Type()
)
dadcnfigMirror3Director.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirror3Director.setStatus("obsolete")
_DadcnfigMirror3Interface_Type = Integer32
_DadcnfigMirror3Interface_Object = MibTableColumn
dadcnfigMirror3Interface = _DadcnfigMirror3Interface_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 14),
    _DadcnfigMirror3Interface_Type()
)
dadcnfigMirror3Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirror3Interface.setStatus("obsolete")
_DadcnfigMirror4Director_Type = Integer32
_DadcnfigMirror4Director_Object = MibTableColumn
dadcnfigMirror4Director = _DadcnfigMirror4Director_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 15),
    _DadcnfigMirror4Director_Type()
)
dadcnfigMirror4Director.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirror4Director.setStatus("obsolete")
_DadcnfigMirror4Interface_Type = Integer32
_DadcnfigMirror4Interface_Object = MibTableColumn
dadcnfigMirror4Interface = _DadcnfigMirror4Interface_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 273, 2, 1, 16),
    _DadcnfigMirror4Interface_Type()
)
dadcnfigMirror4Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadcnfigMirror4Interface.setStatus("obsolete")
_DeviceHostAddressConfiguration_ObjectIdentity = ObjectIdentity
deviceHostAddressConfiguration = _DeviceHostAddressConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281)
)
_DeviceHostAddressConfigurationTable_Object = MibTable
deviceHostAddressConfigurationTable = _DeviceHostAddressConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 1)
)
if mibBuilder.loadTexts:
    deviceHostAddressConfigurationTable.setStatus("obsolete")
_DeviceHostAddressConfigurationEntry_Object = MibTableRow
deviceHostAddressConfigurationEntry = _DeviceHostAddressConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 1, 1)
)
deviceHostAddressConfigurationEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    deviceHostAddressConfigurationEntry.setStatus("obsolete")
_DvhoaddrBuffer_Type = Opaque
_DvhoaddrBuffer_Object = MibTableColumn
dvhoaddrBuffer = _DvhoaddrBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 1, 1, 1),
    _DvhoaddrBuffer_Type()
)
dvhoaddrBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrBuffer.setStatus("obsolete")
_DvhoaddrNumberofRecords_Type = Integer32
_DvhoaddrNumberofRecords_Object = MibTableColumn
dvhoaddrNumberofRecords = _DvhoaddrNumberofRecords_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 1, 1, 2),
    _DvhoaddrNumberofRecords_Type()
)
dvhoaddrNumberofRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrNumberofRecords.setStatus("obsolete")
_DvhoaddrRecordSize_Type = Integer32
_DvhoaddrRecordSize_Object = MibTableColumn
dvhoaddrRecordSize = _DvhoaddrRecordSize_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 1, 1, 3),
    _DvhoaddrRecordSize_Type()
)
dvhoaddrRecordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrRecordSize.setStatus("obsolete")
_DvhoaddrFirstRecordNumber_Type = Integer32
_DvhoaddrFirstRecordNumber_Object = MibTableColumn
dvhoaddrFirstRecordNumber = _DvhoaddrFirstRecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 1, 1, 4),
    _DvhoaddrFirstRecordNumber_Type()
)
dvhoaddrFirstRecordNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrFirstRecordNumber.setStatus("obsolete")
_DvhoaddrMaxRecords_Type = Integer32
_DvhoaddrMaxRecords_Object = MibTableColumn
dvhoaddrMaxRecords = _DvhoaddrMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 1, 1, 5),
    _DvhoaddrMaxRecords_Type()
)
dvhoaddrMaxRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrMaxRecords.setStatus("obsolete")
_DvhoaddrDeviceRecordsTable_Object = MibTable
dvhoaddrDeviceRecordsTable = _DvhoaddrDeviceRecordsTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2)
)
if mibBuilder.loadTexts:
    dvhoaddrDeviceRecordsTable.setStatus("obsolete")
_DvhoaddrDeviceRecordsEntry_Object = MibTableRow
dvhoaddrDeviceRecordsEntry = _DvhoaddrDeviceRecordsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1)
)
dvhoaddrDeviceRecordsEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "dvhoaddrSymmNumber"),
)
if mibBuilder.loadTexts:
    dvhoaddrDeviceRecordsEntry.setStatus("obsolete")
_DvhoaddrSymmNumber_Type = Integer32
_DvhoaddrSymmNumber_Object = MibTableColumn
dvhoaddrSymmNumber = _DvhoaddrSymmNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 1),
    _DvhoaddrSymmNumber_Type()
)
dvhoaddrSymmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrSymmNumber.setStatus("obsolete")
_DvhoaddrDirectorNumber_Type = Integer32
_DvhoaddrDirectorNumber_Object = MibTableColumn
dvhoaddrDirectorNumber = _DvhoaddrDirectorNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 2),
    _DvhoaddrDirectorNumber_Type()
)
dvhoaddrDirectorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrDirectorNumber.setStatus("obsolete")


class _DvhoaddrPortAType_Type(Integer32):
    """Custom type dvhoaddrPortAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("escon-ca", 2),
          ("fibre", 6),
          ("parallel-ca", 1),
          ("sa", 3))
    )


_DvhoaddrPortAType_Type.__name__ = "Integer32"
_DvhoaddrPortAType_Object = MibTableColumn
dvhoaddrPortAType = _DvhoaddrPortAType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 3),
    _DvhoaddrPortAType_Type()
)
dvhoaddrPortAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrPortAType.setStatus("obsolete")
_DvhoaddrPortADeviceAddress_Type = Opaque
_DvhoaddrPortADeviceAddress_Object = MibTableColumn
dvhoaddrPortADeviceAddress = _DvhoaddrPortADeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 4),
    _DvhoaddrPortADeviceAddress_Type()
)
dvhoaddrPortADeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrPortADeviceAddress.setStatus("obsolete")


class _DvhoaddrPortBType_Type(Integer32):
    """Custom type dvhoaddrPortBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("escon-ca", 2),
          ("fibre", 6),
          ("parallel-ca", 1),
          ("sa", 3))
    )


_DvhoaddrPortBType_Type.__name__ = "Integer32"
_DvhoaddrPortBType_Object = MibTableColumn
dvhoaddrPortBType = _DvhoaddrPortBType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 5),
    _DvhoaddrPortBType_Type()
)
dvhoaddrPortBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrPortBType.setStatus("obsolete")
_DvhoaddrPortBDeviceAddress_Type = Opaque
_DvhoaddrPortBDeviceAddress_Object = MibTableColumn
dvhoaddrPortBDeviceAddress = _DvhoaddrPortBDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 6),
    _DvhoaddrPortBDeviceAddress_Type()
)
dvhoaddrPortBDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrPortBDeviceAddress.setStatus("obsolete")


class _DvhoaddrPortCType_Type(Integer32):
    """Custom type dvhoaddrPortCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("escon-ca", 2),
          ("fibre", 6),
          ("parallel-ca", 1),
          ("sa", 3))
    )


_DvhoaddrPortCType_Type.__name__ = "Integer32"
_DvhoaddrPortCType_Object = MibTableColumn
dvhoaddrPortCType = _DvhoaddrPortCType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 7),
    _DvhoaddrPortCType_Type()
)
dvhoaddrPortCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrPortCType.setStatus("obsolete")
_DvhoaddrPortCDeviceAddress_Type = Opaque
_DvhoaddrPortCDeviceAddress_Object = MibTableColumn
dvhoaddrPortCDeviceAddress = _DvhoaddrPortCDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 8),
    _DvhoaddrPortCDeviceAddress_Type()
)
dvhoaddrPortCDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrPortCDeviceAddress.setStatus("obsolete")


class _DvhoaddrPortDType_Type(Integer32):
    """Custom type dvhoaddrPortDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("escon-ca", 2),
          ("fibre", 6),
          ("parallel-ca", 1),
          ("sa", 3))
    )


_DvhoaddrPortDType_Type.__name__ = "Integer32"
_DvhoaddrPortDType_Object = MibTableColumn
dvhoaddrPortDType = _DvhoaddrPortDType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 9),
    _DvhoaddrPortDType_Type()
)
dvhoaddrPortDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrPortDType.setStatus("obsolete")
_DvhoaddrPortDDeviceAddress_Type = Opaque
_DvhoaddrPortDDeviceAddress_Object = MibTableColumn
dvhoaddrPortDDeviceAddress = _DvhoaddrPortDDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 10),
    _DvhoaddrPortDDeviceAddress_Type()
)
dvhoaddrPortDDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrPortDDeviceAddress.setStatus("obsolete")
_DvhoaddrMetaFlags_Type = Opaque
_DvhoaddrMetaFlags_Object = MibTableColumn
dvhoaddrMetaFlags = _DvhoaddrMetaFlags_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 11),
    _DvhoaddrMetaFlags_Type()
)
dvhoaddrMetaFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrMetaFlags.setStatus("obsolete")
_DvhoaddrFiberChannelAddress_Type = Integer32
_DvhoaddrFiberChannelAddress_Object = MibTableColumn
dvhoaddrFiberChannelAddress = _DvhoaddrFiberChannelAddress_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 1, 281, 2, 1, 15),
    _DvhoaddrFiberChannelAddress_Type()
)
dvhoaddrFiberChannelAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvhoaddrFiberChannelAddress.setStatus("obsolete")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 2, 2)
)
_Discovery_ObjectIdentity = ObjectIdentity
discovery = _Discovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3)
)
_DiscoveryTableSize_Type = Integer32
_DiscoveryTableSize_Object = MibScalar
discoveryTableSize = _DiscoveryTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 1),
    _DiscoveryTableSize_Type()
)
discoveryTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discoveryTableSize.setStatus("mandatory")
_DiscoveryTable_Object = MibTable
discoveryTable = _DiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2)
)
if mibBuilder.loadTexts:
    discoveryTable.setStatus("mandatory")
_DiscoveryTbl_Object = MibTableRow
discoveryTbl = _DiscoveryTbl_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1)
)
discoveryTbl.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    discoveryTbl.setStatus("mandatory")
_DiscIndex_Type = Integer32
_DiscIndex_Object = MibTableColumn
discIndex = _DiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 1),
    _DiscIndex_Type()
)
discIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discIndex.setStatus("mandatory")
_DiscSerialNumber_Type = DisplayString
_DiscSerialNumber_Object = MibTableColumn
discSerialNumber = _DiscSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 2),
    _DiscSerialNumber_Type()
)
discSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discSerialNumber.setStatus("mandatory")
_DiscRawDevice_Type = DisplayString
_DiscRawDevice_Object = MibTableColumn
discRawDevice = _DiscRawDevice_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 3),
    _DiscRawDevice_Type()
)
discRawDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discRawDevice.setStatus("obsolete")
_DiscModel_Type = Integer32
_DiscModel_Object = MibTableColumn
discModel = _DiscModel_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 4),
    _DiscModel_Type()
)
discModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discModel.setStatus("mandatory")
_DiscCapacity_Type = Integer32
_DiscCapacity_Object = MibTableColumn
discCapacity = _DiscCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 5),
    _DiscCapacity_Type()
)
discCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discCapacity.setStatus("obsolete")
_DiscChecksum_Type = Integer32
_DiscChecksum_Object = MibTableColumn
discChecksum = _DiscChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 6),
    _DiscChecksum_Type()
)
discChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discChecksum.setStatus("mandatory")
_DiscConfigDate_Type = DisplayString
_DiscConfigDate_Object = MibTableColumn
discConfigDate = _DiscConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 7),
    _DiscConfigDate_Type()
)
discConfigDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discConfigDate.setStatus("mandatory")


class _DiscRDF_Type(Integer32):
    """Custom type discRDF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_DiscRDF_Type.__name__ = "Integer32"
_DiscRDF_Object = MibTableColumn
discRDF = _DiscRDF_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 8),
    _DiscRDF_Type()
)
discRDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discRDF.setStatus("mandatory")


class _DiscBCV_Type(Integer32):
    """Custom type discBCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_DiscBCV_Type.__name__ = "Integer32"
_DiscBCV_Object = MibTableColumn
discBCV = _DiscBCV_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 9),
    _DiscBCV_Type()
)
discBCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discBCV.setStatus("mandatory")


class _DiscState_Type(Integer32):
    """Custom type discState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 3),
          ("online", 2),
          ("unknown", 1))
    )


_DiscState_Type.__name__ = "Integer32"
_DiscState_Object = MibTableColumn
discState = _DiscState_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 10),
    _DiscState_Type()
)
discState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discState.setStatus("mandatory")


class _DiscStatus_Type(Integer32):
    """Custom type discStatus based on Integer32"""
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
        *(("failed", 5),
          ("ok", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_DiscStatus_Type.__name__ = "Integer32"
_DiscStatus_Object = MibTableColumn
discStatus = _DiscStatus_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 11),
    _DiscStatus_Type()
)
discStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discStatus.setStatus("mandatory")
_DiscMicrocodeVersion_Type = DisplayString
_DiscMicrocodeVersion_Object = MibTableColumn
discMicrocodeVersion = _DiscMicrocodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 12),
    _DiscMicrocodeVersion_Type()
)
discMicrocodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discMicrocodeVersion.setStatus("mandatory")
_DiscSymapisrv_IP_Type = IpAddress
_DiscSymapisrv_IP_Object = MibScalar
discSymapisrv_IP = _DiscSymapisrv_IP_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 13),
    _DiscSymapisrv_IP_Type()
)
discSymapisrv_IP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discSymapisrv_IP.setStatus("mandatory")
_DiscNumEvents_Type = Integer32
_DiscNumEvents_Object = MibTableColumn
discNumEvents = _DiscNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 14),
    _DiscNumEvents_Type()
)
discNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discNumEvents.setStatus("mandatory")
_DiscEventCurrID_Type = Integer32
_DiscEventCurrID_Object = MibTableColumn
discEventCurrID = _DiscEventCurrID_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 3, 2, 1, 15),
    _DiscEventCurrID_Type()
)
discEventCurrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discEventCurrID.setStatus("mandatory")
_AgentAdministration_ObjectIdentity = ObjectIdentity
agentAdministration = _AgentAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4)
)
_AgentRevision_Type = DisplayString
_AgentRevision_Object = MibScalar
agentRevision = _AgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1),
    _AgentRevision_Type()
)
agentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRevision.setStatus("mandatory")
_MibRevision_Type = DisplayString
_MibRevision_Object = MibScalar
mibRevision = _MibRevision_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 2),
    _MibRevision_Type()
)
mibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibRevision.setStatus("mandatory")


class _AgentType_Type(Integer32):
    """Custom type agentType based on Integer32"""
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
        *(("mainframe", 2),
          ("nt-host", 3),
          ("unix-host", 1),
          ("unknown", 0))
    )


_AgentType_Type.__name__ = "Integer32"
_AgentType_Object = MibScalar
agentType = _AgentType_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 3),
    _AgentType_Type()
)
agentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentType.setStatus("mandatory")
_PeriodicDiscoveryFrequency_Type = Integer32
_PeriodicDiscoveryFrequency_Object = MibScalar
periodicDiscoveryFrequency = _PeriodicDiscoveryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 4),
    _PeriodicDiscoveryFrequency_Type()
)
periodicDiscoveryFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    periodicDiscoveryFrequency.setStatus("mandatory")
_ChecksumTestFrequency_Type = Integer32
_ChecksumTestFrequency_Object = MibScalar
checksumTestFrequency = _ChecksumTestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 5),
    _ChecksumTestFrequency_Type()
)
checksumTestFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    checksumTestFrequency.setStatus("mandatory")
_StatusCheckFrequency_Type = Integer32
_StatusCheckFrequency_Object = MibScalar
statusCheckFrequency = _StatusCheckFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 6),
    _StatusCheckFrequency_Type()
)
statusCheckFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusCheckFrequency.setStatus("mandatory")
_DiscoveryChangeTime_Type = Integer32
_DiscoveryChangeTime_Object = MibScalar
discoveryChangeTime = _DiscoveryChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 302),
    _DiscoveryChangeTime_Type()
)
discoveryChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discoveryChangeTime.setStatus("mandatory")
_Analyzer_ObjectIdentity = ObjectIdentity
analyzer = _Analyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000)
)
_AnalyzerTopFileSavePolicy_Type = Integer32
_AnalyzerTopFileSavePolicy_Object = MibScalar
analyzerTopFileSavePolicy = _AnalyzerTopFileSavePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 1),
    _AnalyzerTopFileSavePolicy_Type()
)
analyzerTopFileSavePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analyzerTopFileSavePolicy.setStatus("obsolete")
_AnalyzerSpecialDurationLimit_Type = Integer32
_AnalyzerSpecialDurationLimit_Object = MibScalar
analyzerSpecialDurationLimit = _AnalyzerSpecialDurationLimit_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 2),
    _AnalyzerSpecialDurationLimit_Type()
)
analyzerSpecialDurationLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analyzerSpecialDurationLimit.setStatus("obsolete")
_AnalyzerFiles_ObjectIdentity = ObjectIdentity
analyzerFiles = _AnalyzerFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3)
)
_AnalyzerFilesCountTable_Object = MibTable
analyzerFilesCountTable = _AnalyzerFilesCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 1)
)
if mibBuilder.loadTexts:
    analyzerFilesCountTable.setStatus("obsolete")
_AnalyzerFileCountEntry_Object = MibTableRow
analyzerFileCountEntry = _AnalyzerFileCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 1, 1)
)
analyzerFileCountEntry.setIndexNames(
    (0, "EMC-MIB", "symListCount"),
)
if mibBuilder.loadTexts:
    analyzerFileCountEntry.setStatus("obsolete")
_AnalyzerFileCount_Type = Integer32
_AnalyzerFileCount_Object = MibTableColumn
analyzerFileCount = _AnalyzerFileCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 1, 1, 1),
    _AnalyzerFileCount_Type()
)
analyzerFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analyzerFileCount.setStatus("obsolete")
_AnalyzerFilesListTable_Object = MibTable
analyzerFilesListTable = _AnalyzerFilesListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 2)
)
if mibBuilder.loadTexts:
    analyzerFilesListTable.setStatus("obsolete")
_AnalyzerFilesListEntry_Object = MibTableRow
analyzerFilesListEntry = _AnalyzerFilesListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 2, 1)
)
analyzerFilesListEntry.setIndexNames(
    (0, "EMC-MIB", "symListCount"),
    (0, "EMC-MIB", "analyzerFileCount"),
)
if mibBuilder.loadTexts:
    analyzerFilesListEntry.setStatus("obsolete")
_AnalyzerFileName_Type = DisplayString
_AnalyzerFileName_Object = MibTableColumn
analyzerFileName = _AnalyzerFileName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 2, 1, 1),
    _AnalyzerFileName_Type()
)
analyzerFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analyzerFileName.setStatus("obsolete")
_AnalyzerFileSize_Type = Integer32
_AnalyzerFileSize_Object = MibTableColumn
analyzerFileSize = _AnalyzerFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 2, 1, 2),
    _AnalyzerFileSize_Type()
)
analyzerFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analyzerFileSize.setStatus("obsolete")
_AnalyzerFileCreation_Type = DisplayString
_AnalyzerFileCreation_Object = MibTableColumn
analyzerFileCreation = _AnalyzerFileCreation_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 2, 1, 3),
    _AnalyzerFileCreation_Type()
)
analyzerFileCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analyzerFileCreation.setStatus("obsolete")
_AnalyzerFileLastModified_Type = DisplayString
_AnalyzerFileLastModified_Object = MibTableColumn
analyzerFileLastModified = _AnalyzerFileLastModified_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 2, 1, 4),
    _AnalyzerFileLastModified_Type()
)
analyzerFileLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analyzerFileLastModified.setStatus("obsolete")


class _AnalyzerFileIsActive_Type(Integer32):
    """Custom type analyzerFileIsActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_AnalyzerFileIsActive_Type.__name__ = "Integer32"
_AnalyzerFileIsActive_Object = MibTableColumn
analyzerFileIsActive = _AnalyzerFileIsActive_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 2, 1, 5),
    _AnalyzerFileIsActive_Type()
)
analyzerFileIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analyzerFileIsActive.setStatus("obsolete")
_AnalyzerFileRuntime_Type = TimeTicks
_AnalyzerFileRuntime_Object = MibTableColumn
analyzerFileRuntime = _AnalyzerFileRuntime_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1000, 3, 2, 1, 6),
    _AnalyzerFileRuntime_Type()
)
analyzerFileRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analyzerFileRuntime.setStatus("obsolete")
_Clients_ObjectIdentity = ObjectIdentity
clients = _Clients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1001)
)
_ClientListMaintenanceFrequency_Type = Integer32
_ClientListMaintenanceFrequency_Object = MibScalar
clientListMaintenanceFrequency = _ClientListMaintenanceFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1001, 1),
    _ClientListMaintenanceFrequency_Type()
)
clientListMaintenanceFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientListMaintenanceFrequency.setStatus("obsolete")
_ClientListRequestExpiration_Type = Integer32
_ClientListRequestExpiration_Object = MibScalar
clientListRequestExpiration = _ClientListRequestExpiration_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1001, 2),
    _ClientListRequestExpiration_Type()
)
clientListRequestExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientListRequestExpiration.setStatus("obsolete")
_ClientListClientExpiration_Type = Integer32
_ClientListClientExpiration_Object = MibScalar
clientListClientExpiration = _ClientListClientExpiration_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1001, 3),
    _ClientListClientExpiration_Type()
)
clientListClientExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientListClientExpiration.setStatus("obsolete")
_TrapSetup_ObjectIdentity = ObjectIdentity
trapSetup = _TrapSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1002)
)
_DiscoveryTrapPort_Type = Integer32
_DiscoveryTrapPort_Object = MibScalar
discoveryTrapPort = _DiscoveryTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1002, 1),
    _DiscoveryTrapPort_Type()
)
discoveryTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discoveryTrapPort.setStatus("obsolete")
_TrapTestFrequency_Type = Integer32
_TrapTestFrequency_Object = MibScalar
trapTestFrequency = _TrapTestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1002, 2),
    _TrapTestFrequency_Type()
)
trapTestFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapTestFrequency.setStatus("obsolete")
_ActivePorts_ObjectIdentity = ObjectIdentity
activePorts = _ActivePorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1003)
)
_StandardSNMPRequestPort_Type = Integer32
_StandardSNMPRequestPort_Object = MibScalar
standardSNMPRequestPort = _StandardSNMPRequestPort_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1003, 1),
    _StandardSNMPRequestPort_Type()
)
standardSNMPRequestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standardSNMPRequestPort.setStatus("mandatory")
_EsmSNMPRequestPort_Type = Integer32
_EsmSNMPRequestPort_Object = MibScalar
esmSNMPRequestPort = _EsmSNMPRequestPort_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1003, 2),
    _EsmSNMPRequestPort_Type()
)
esmSNMPRequestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmSNMPRequestPort.setStatus("mandatory")
_CelerraTCPPort_Type = Integer32
_CelerraTCPPort_Object = MibScalar
celerraTCPPort = _CelerraTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1003, 3),
    _CelerraTCPPort_Type()
)
celerraTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celerraTCPPort.setStatus("obsolete")
_XdrTCPPort_Type = Integer32
_XdrTCPPort_Object = MibScalar
xdrTCPPort = _XdrTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1003, 4),
    _XdrTCPPort_Type()
)
xdrTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdrTCPPort.setStatus("obsolete")
_AgentConfiguration_ObjectIdentity = ObjectIdentity
agentConfiguration = _AgentConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1004)
)
_EsmVariablePacketSize_Type = Integer32
_EsmVariablePacketSize_Object = MibScalar
esmVariablePacketSize = _EsmVariablePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1004, 1),
    _EsmVariablePacketSize_Type()
)
esmVariablePacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmVariablePacketSize.setStatus("obsolete")
_DiscoveryFrequency_Type = Integer32
_DiscoveryFrequency_Object = MibScalar
discoveryFrequency = _DiscoveryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1004, 2),
    _DiscoveryFrequency_Type()
)
discoveryFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discoveryFrequency.setStatus("obsolete")


class _MasterTraceMessagesEnable_Type(Integer32):
    """Custom type masterTraceMessagesEnable based on Integer32"""
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


_MasterTraceMessagesEnable_Type.__name__ = "Integer32"
_MasterTraceMessagesEnable_Object = MibScalar
masterTraceMessagesEnable = _MasterTraceMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1004, 3),
    _MasterTraceMessagesEnable_Type()
)
masterTraceMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterTraceMessagesEnable.setStatus("obsolete")
_SubagentConfiguration_ObjectIdentity = ObjectIdentity
subagentConfiguration = _SubagentConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1005)
)
_SubagentInformation_Object = MibTable
subagentInformation = _SubagentInformation_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1005, 1)
)
if mibBuilder.loadTexts:
    subagentInformation.setStatus("obsolete")
_SubagentInfo_Object = MibTableRow
subagentInfo = _SubagentInfo_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1005, 1, 1)
)
subagentInfo.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    subagentInfo.setStatus("obsolete")
_SubagentSymmetrixSerialNumber_Type = DisplayString
_SubagentSymmetrixSerialNumber_Object = MibTableColumn
subagentSymmetrixSerialNumber = _SubagentSymmetrixSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1005, 1, 1, 1),
    _SubagentSymmetrixSerialNumber_Type()
)
subagentSymmetrixSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subagentSymmetrixSerialNumber.setStatus("obsolete")


class _SubagentProcessActive_Type(Integer32):
    """Custom type subagentProcessActive based on Integer32"""
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


_SubagentProcessActive_Type.__name__ = "Integer32"
_SubagentProcessActive_Object = MibTableColumn
subagentProcessActive = _SubagentProcessActive_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1005, 1, 1, 2),
    _SubagentProcessActive_Type()
)
subagentProcessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subagentProcessActive.setStatus("obsolete")


class _SubagentTraceMessagesEnable_Type(Integer32):
    """Custom type subagentTraceMessagesEnable based on Integer32"""
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


_SubagentTraceMessagesEnable_Type.__name__ = "Integer32"
_SubagentTraceMessagesEnable_Object = MibTableColumn
subagentTraceMessagesEnable = _SubagentTraceMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 4, 1005, 1, 1, 3),
    _SubagentTraceMessagesEnable_Type()
)
subagentTraceMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subagentTraceMessagesEnable.setStatus("obsolete")
_MainframeVariables_ObjectIdentity = ObjectIdentity
mainframeVariables = _MainframeVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5)
)
_MainframeDiskInformation_Object = MibTable
mainframeDiskInformation = _MainframeDiskInformation_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mainframeDiskInformation.setStatus("obsolete")
_MfDiskInformation_Object = MibTableRow
mfDiskInformation = _MfDiskInformation_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5, 1, 1)
)
mfDiskInformation.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    mfDiskInformation.setStatus("obsolete")
_EmcSymMvsVolume_Type = Opaque
_EmcSymMvsVolume_Object = MibTableColumn
emcSymMvsVolume = _EmcSymMvsVolume_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5, 1, 1, 1),
    _EmcSymMvsVolume_Type()
)
emcSymMvsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymMvsVolume.setStatus("obsolete")
_MainframeDataSetInformation_Object = MibTable
mainframeDataSetInformation = _MainframeDataSetInformation_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mainframeDataSetInformation.setStatus("obsolete")
_MfDataSetInformation_Object = MibTableRow
mfDataSetInformation = _MfDataSetInformation_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5, 2, 1)
)
mfDataSetInformation.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "emcSymMvsLUNNumber"),
)
if mibBuilder.loadTexts:
    mfDataSetInformation.setStatus("obsolete")
_EmcSymMvsLUNNumber_Type = Integer32
_EmcSymMvsLUNNumber_Object = MibTableColumn
emcSymMvsLUNNumber = _EmcSymMvsLUNNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5, 2, 1, 1),
    _EmcSymMvsLUNNumber_Type()
)
emcSymMvsLUNNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymMvsLUNNumber.setStatus("obsolete")
_EmcSymMvsDsname_Type = Opaque
_EmcSymMvsDsname_Object = MibTableColumn
emcSymMvsDsname = _EmcSymMvsDsname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5, 2, 1, 2),
    _EmcSymMvsDsname_Type()
)
emcSymMvsDsname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcSymMvsDsname.setStatus("obsolete")
_EmcSymMvsBuildStatus_Type = Integer32
_EmcSymMvsBuildStatus_Object = MibTableColumn
emcSymMvsBuildStatus = _EmcSymMvsBuildStatus_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 5, 2, 1, 3),
    _EmcSymMvsBuildStatus_Type()
)
emcSymMvsBuildStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emcSymMvsBuildStatus.setStatus("obsolete")
_SymAPI_ObjectIdentity = ObjectIdentity
symAPI = _SymAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6)
)
_SymAPIList_ObjectIdentity = ObjectIdentity
symAPIList = _SymAPIList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1)
)
_SymList_ObjectIdentity = ObjectIdentity
symList = _SymList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 1)
)
_SymListCount_Type = Integer32
_SymListCount_Object = MibScalar
symListCount = _SymListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 1, 1),
    _SymListCount_Type()
)
symListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symListCount.setStatus("obsolete")
_SymListTable_Object = MibTable
symListTable = _SymListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    symListTable.setStatus("obsolete")
_SymListEntry_Object = MibTableRow
symListEntry = _SymListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 1, 2, 1)
)
symListEntry.setIndexNames(
    (0, "EMC-MIB", "symListCount"),
)
if mibBuilder.loadTexts:
    symListEntry.setStatus("obsolete")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 1, 2, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("obsolete")
_SymRemoteList_ObjectIdentity = ObjectIdentity
symRemoteList = _SymRemoteList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 2)
)
_SymRemoteListCount_Type = Integer32
_SymRemoteListCount_Object = MibScalar
symRemoteListCount = _SymRemoteListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 2, 1),
    _SymRemoteListCount_Type()
)
symRemoteListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symRemoteListCount.setStatus("obsolete")
_SymRemoteListTable_Object = MibTable
symRemoteListTable = _SymRemoteListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    symRemoteListTable.setStatus("obsolete")
_SymRemoteListEntry_Object = MibTableRow
symRemoteListEntry = _SymRemoteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 2, 2, 2)
)
symRemoteListEntry.setIndexNames(
    (0, "EMC-MIB", "symRemoteListCount"),
)
if mibBuilder.loadTexts:
    symRemoteListEntry.setStatus("obsolete")
_RemoteSerialNumber_Type = DisplayString
_RemoteSerialNumber_Object = MibTableColumn
remoteSerialNumber = _RemoteSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 2, 2, 2, 1),
    _RemoteSerialNumber_Type()
)
remoteSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSerialNumber.setStatus("obsolete")
_SymDevList_ObjectIdentity = ObjectIdentity
symDevList = _SymDevList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 3)
)
_SymDevListCountTable_Object = MibTable
symDevListCountTable = _SymDevListCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    symDevListCountTable.setStatus("mandatory")
_SymDevListCountEntry_Object = MibTableRow
symDevListCountEntry = _SymDevListCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 3, 1, 1)
)
symDevListCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symDevListCountEntry.setStatus("mandatory")
_SymDevListCount_Type = Integer32
_SymDevListCount_Object = MibTableColumn
symDevListCount = _SymDevListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 3, 1, 1, 1),
    _SymDevListCount_Type()
)
symDevListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symDevListCount.setStatus("mandatory")
_SymDevListTable_Object = MibTable
symDevListTable = _SymDevListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    symDevListTable.setStatus("mandatory")
_SymDevListEntry_Object = MibTableRow
symDevListEntry = _SymDevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 3, 2, 1)
)
symDevListEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symDevListCount"),
)
if mibBuilder.loadTexts:
    symDevListEntry.setStatus("mandatory")
_SymDeviceName_Type = DisplayString
_SymDeviceName_Object = MibTableColumn
symDeviceName = _SymDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 3, 2, 1, 1),
    _SymDeviceName_Type()
)
symDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symDeviceName.setStatus("mandatory")
_SymPDevList_ObjectIdentity = ObjectIdentity
symPDevList = _SymPDevList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 4)
)
_SymPDevListCountTable_Object = MibTable
symPDevListCountTable = _SymPDevListCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    symPDevListCountTable.setStatus("mandatory")
_SymPDevListCountEntry_Object = MibTableRow
symPDevListCountEntry = _SymPDevListCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 4, 1, 1)
)
symPDevListCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symPDevListCountEntry.setStatus("mandatory")
_SymPDevListCount_Type = Integer32
_SymPDevListCount_Object = MibTableColumn
symPDevListCount = _SymPDevListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 4, 1, 1, 1),
    _SymPDevListCount_Type()
)
symPDevListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symPDevListCount.setStatus("mandatory")
_SymPDevListTable_Object = MibTable
symPDevListTable = _SymPDevListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    symPDevListTable.setStatus("mandatory")
_SymPDevListEntry_Object = MibTableRow
symPDevListEntry = _SymPDevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 4, 2, 1)
)
symPDevListEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symPDevListCount"),
)
if mibBuilder.loadTexts:
    symPDevListEntry.setStatus("mandatory")
_SymPDeviceName_Type = DisplayString
_SymPDeviceName_Object = MibTableColumn
symPDeviceName = _SymPDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 4, 2, 1, 1),
    _SymPDeviceName_Type()
)
symPDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symPDeviceName.setStatus("mandatory")
_SymPDevNoDgList_ObjectIdentity = ObjectIdentity
symPDevNoDgList = _SymPDevNoDgList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 5)
)
_SymPDevNoDgListCountTable_Object = MibTable
symPDevNoDgListCountTable = _SymPDevNoDgListCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    symPDevNoDgListCountTable.setStatus("mandatory")
_SymPDevNoDgListCountEntry_Object = MibTableRow
symPDevNoDgListCountEntry = _SymPDevNoDgListCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 5, 1, 1)
)
symPDevNoDgListCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symPDevNoDgListCountEntry.setStatus("mandatory")
_SymPDevNoDgListCount_Type = Integer32
_SymPDevNoDgListCount_Object = MibTableColumn
symPDevNoDgListCount = _SymPDevNoDgListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 5, 1, 1, 1),
    _SymPDevNoDgListCount_Type()
)
symPDevNoDgListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symPDevNoDgListCount.setStatus("mandatory")
_SymPDevNoDgListTable_Object = MibTable
symPDevNoDgListTable = _SymPDevNoDgListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 5, 2)
)
if mibBuilder.loadTexts:
    symPDevNoDgListTable.setStatus("mandatory")
_SymPDevNoDgListEntry_Object = MibTableRow
symPDevNoDgListEntry = _SymPDevNoDgListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 5, 2, 1)
)
symPDevNoDgListEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symPDevNoDgListCount"),
)
if mibBuilder.loadTexts:
    symPDevNoDgListEntry.setStatus("mandatory")
_SymPDevNoDgDeviceName_Type = DisplayString
_SymPDevNoDgDeviceName_Object = MibTableColumn
symPDevNoDgDeviceName = _SymPDevNoDgDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 5, 2, 1, 1),
    _SymPDevNoDgDeviceName_Type()
)
symPDevNoDgDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symPDevNoDgDeviceName.setStatus("mandatory")
_SymDevNoDgList_ObjectIdentity = ObjectIdentity
symDevNoDgList = _SymDevNoDgList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 6)
)
_SymDevNoDgListCountTable_Object = MibTable
symDevNoDgListCountTable = _SymDevNoDgListCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    symDevNoDgListCountTable.setStatus("mandatory")
_SymDevNoDgListCountEntry_Object = MibTableRow
symDevNoDgListCountEntry = _SymDevNoDgListCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 6, 1, 1)
)
symDevNoDgListCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symDevNoDgListCountEntry.setStatus("mandatory")
_SymDevNoDgListCount_Type = Integer32
_SymDevNoDgListCount_Object = MibTableColumn
symDevNoDgListCount = _SymDevNoDgListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 6, 1, 1, 1),
    _SymDevNoDgListCount_Type()
)
symDevNoDgListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symDevNoDgListCount.setStatus("mandatory")
_SymDevNoDgListTable_Object = MibTable
symDevNoDgListTable = _SymDevNoDgListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 6, 2)
)
if mibBuilder.loadTexts:
    symDevNoDgListTable.setStatus("mandatory")
_SymDevNoDgListEntry_Object = MibTableRow
symDevNoDgListEntry = _SymDevNoDgListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 6, 2, 1)
)
symDevNoDgListEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symDevNoDgListCount"),
)
if mibBuilder.loadTexts:
    symDevNoDgListEntry.setStatus("mandatory")
_SymDevNoDgDeviceName_Type = DisplayString
_SymDevNoDgDeviceName_Object = MibTableColumn
symDevNoDgDeviceName = _SymDevNoDgDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 6, 2, 1, 1),
    _SymDevNoDgDeviceName_Type()
)
symDevNoDgDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symDevNoDgDeviceName.setStatus("mandatory")
_SymDgList_ObjectIdentity = ObjectIdentity
symDgList = _SymDgList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 7)
)
_SymDgListCount_Type = Integer32
_SymDgListCount_Object = MibScalar
symDgListCount = _SymDgListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 7, 1),
    _SymDgListCount_Type()
)
symDgListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symDgListCount.setStatus("obsolete")
_SymDgListTable_Object = MibTable
symDgListTable = _SymDgListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 7, 2)
)
if mibBuilder.loadTexts:
    symDgListTable.setStatus("obsolete")
_SymDgListEntry_Object = MibTableRow
symDgListEntry = _SymDgListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 7, 2, 1)
)
symDgListEntry.setIndexNames(
    (0, "EMC-MIB", "symDgListCount"),
)
if mibBuilder.loadTexts:
    symDgListEntry.setStatus("obsolete")
_SymDevGroupName_Type = DisplayString
_SymDevGroupName_Object = MibTableColumn
symDevGroupName = _SymDevGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 7, 2, 1, 1),
    _SymDevGroupName_Type()
)
symDevGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symDevGroupName.setStatus("obsolete")
_SymLDevList_ObjectIdentity = ObjectIdentity
symLDevList = _SymLDevList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 8)
)
_SymLDevListCountTable_Object = MibTable
symLDevListCountTable = _SymLDevListCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 8, 1)
)
if mibBuilder.loadTexts:
    symLDevListCountTable.setStatus("obsolete")
_SymLDevListCountEntry_Object = MibTableRow
symLDevListCountEntry = _SymLDevListCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 8, 1, 1)
)
symLDevListCountEntry.setIndexNames(
    (0, "EMC-MIB", "symDgListCount"),
)
if mibBuilder.loadTexts:
    symLDevListCountEntry.setStatus("obsolete")
_SymLDevListCount_Type = Integer32
_SymLDevListCount_Object = MibTableColumn
symLDevListCount = _SymLDevListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 8, 1, 1, 1),
    _SymLDevListCount_Type()
)
symLDevListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symLDevListCount.setStatus("obsolete")
_SymLDevListTable_Object = MibTable
symLDevListTable = _SymLDevListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 8, 2)
)
if mibBuilder.loadTexts:
    symLDevListTable.setStatus("obsolete")
_SymLDevListEntry_Object = MibTableRow
symLDevListEntry = _SymLDevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 8, 2, 1)
)
symLDevListEntry.setIndexNames(
    (0, "EMC-MIB", "symDgListCount"),
    (0, "EMC-MIB", "symLDevListCount"),
)
if mibBuilder.loadTexts:
    symLDevListEntry.setStatus("obsolete")
_LDeviceName_Type = DisplayString
_LDeviceName_Object = MibTableColumn
lDeviceName = _LDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 8, 2, 1, 1),
    _LDeviceName_Type()
)
lDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDeviceName.setStatus("obsolete")
_SymGateList_ObjectIdentity = ObjectIdentity
symGateList = _SymGateList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 9)
)
_SymGateListCountTable_Object = MibTable
symGateListCountTable = _SymGateListCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 9, 1)
)
if mibBuilder.loadTexts:
    symGateListCountTable.setStatus("mandatory")
_SymGateListCountEntry_Object = MibTableRow
symGateListCountEntry = _SymGateListCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 9, 1, 1)
)
symGateListCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symGateListCountEntry.setStatus("mandatory")
_SymGateListCount_Type = Integer32
_SymGateListCount_Object = MibTableColumn
symGateListCount = _SymGateListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 9, 1, 1, 1),
    _SymGateListCount_Type()
)
symGateListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symGateListCount.setStatus("mandatory")
_SymGateListTable_Object = MibTable
symGateListTable = _SymGateListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 9, 2)
)
if mibBuilder.loadTexts:
    symGateListTable.setStatus("mandatory")
_SymGateListEntry_Object = MibTableRow
symGateListEntry = _SymGateListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 9, 2, 1)
)
symGateListEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symGateListCount"),
)
if mibBuilder.loadTexts:
    symGateListEntry.setStatus("mandatory")
_GatekeeperDeviceName_Type = DisplayString
_GatekeeperDeviceName_Object = MibTableColumn
gatekeeperDeviceName = _GatekeeperDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 9, 2, 1, 1),
    _GatekeeperDeviceName_Type()
)
gatekeeperDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatekeeperDeviceName.setStatus("mandatory")
_SymBcvDevList_ObjectIdentity = ObjectIdentity
symBcvDevList = _SymBcvDevList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 10)
)
_SymBcvDevListCountTable_Object = MibTable
symBcvDevListCountTable = _SymBcvDevListCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 10, 1)
)
if mibBuilder.loadTexts:
    symBcvDevListCountTable.setStatus("mandatory")
_SymBcvDevListCountEntry_Object = MibTableRow
symBcvDevListCountEntry = _SymBcvDevListCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 10, 1, 1)
)
symBcvDevListCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symBcvDevListCountEntry.setStatus("mandatory")
_SymBcvDevListCount_Type = Integer32
_SymBcvDevListCount_Object = MibTableColumn
symBcvDevListCount = _SymBcvDevListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 10, 1, 1, 1),
    _SymBcvDevListCount_Type()
)
symBcvDevListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symBcvDevListCount.setStatus("mandatory")
_SymBcvDevListTable_Object = MibTable
symBcvDevListTable = _SymBcvDevListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 10, 2)
)
if mibBuilder.loadTexts:
    symBcvDevListTable.setStatus("mandatory")
_SymBcvDevListEntry_Object = MibTableRow
symBcvDevListEntry = _SymBcvDevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 10, 2, 1)
)
symBcvDevListEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symBcvDevListCount"),
)
if mibBuilder.loadTexts:
    symBcvDevListEntry.setStatus("mandatory")
_BcvDeviceName_Type = DisplayString
_BcvDeviceName_Object = MibTableColumn
bcvDeviceName = _BcvDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 10, 2, 1, 1),
    _BcvDeviceName_Type()
)
bcvDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcvDeviceName.setStatus("mandatory")
_SymBcvPDevList_ObjectIdentity = ObjectIdentity
symBcvPDevList = _SymBcvPDevList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 11)
)
_SymBcvPDevListCountTable_Object = MibTable
symBcvPDevListCountTable = _SymBcvPDevListCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 11, 1)
)
if mibBuilder.loadTexts:
    symBcvPDevListCountTable.setStatus("mandatory")
_SymBcvPDevListCountEntry_Object = MibTableRow
symBcvPDevListCountEntry = _SymBcvPDevListCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 11, 1, 1)
)
symBcvPDevListCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symBcvPDevListCountEntry.setStatus("mandatory")
_SymBcvPDevListCount_Type = Integer32
_SymBcvPDevListCount_Object = MibTableColumn
symBcvPDevListCount = _SymBcvPDevListCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 11, 1, 1, 1),
    _SymBcvPDevListCount_Type()
)
symBcvPDevListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symBcvPDevListCount.setStatus("mandatory")
_SymBcvPDevListTable_Object = MibTable
symBcvPDevListTable = _SymBcvPDevListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 11, 2)
)
if mibBuilder.loadTexts:
    symBcvPDevListTable.setStatus("mandatory")
_SymBcvPDevListEntry_Object = MibTableRow
symBcvPDevListEntry = _SymBcvPDevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 11, 2, 1)
)
symBcvPDevListEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symBcvPDevListCount"),
)
if mibBuilder.loadTexts:
    symBcvPDevListEntry.setStatus("mandatory")
_SymBcvPDeviceName_Type = DisplayString
_SymBcvPDeviceName_Object = MibTableColumn
symBcvPDeviceName = _SymBcvPDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 1, 11, 2, 1, 1),
    _SymBcvPDeviceName_Type()
)
symBcvPDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symBcvPDeviceName.setStatus("mandatory")
_SymAPIShow_ObjectIdentity = ObjectIdentity
symAPIShow = _SymAPIShow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2)
)
_SymShow_ObjectIdentity = ObjectIdentity
symShow = _SymShow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1)
)
_SymShowConfiguration_Object = MibTable
symShowConfiguration = _SymShowConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    symShowConfiguration.setStatus("mandatory")
_SymShowEntry_Object = MibTableRow
symShowEntry = _SymShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1)
)
symShowEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symShowEntry.setStatus("mandatory")
_SymShowSymid_Type = DisplayString
_SymShowSymid_Object = MibTableColumn
symShowSymid = _SymShowSymid_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 1),
    _SymShowSymid_Type()
)
symShowSymid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowSymid.setStatus("mandatory")
_SymShowSymmetrix_ident_Type = DisplayString
_SymShowSymmetrix_ident_Object = MibScalar
symShowSymmetrix_ident = _SymShowSymmetrix_ident_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 2),
    _SymShowSymmetrix_ident_Type()
)
symShowSymmetrix_ident.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowSymmetrix_ident.setStatus("mandatory")
_SymShowSymmetrix_model_Type = DisplayString
_SymShowSymmetrix_model_Object = MibScalar
symShowSymmetrix_model = _SymShowSymmetrix_model_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 3),
    _SymShowSymmetrix_model_Type()
)
symShowSymmetrix_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowSymmetrix_model.setStatus("mandatory")
_SymShowMicrocode_version_Type = DisplayString
_SymShowMicrocode_version_Object = MibScalar
symShowMicrocode_version = _SymShowMicrocode_version_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 4),
    _SymShowMicrocode_version_Type()
)
symShowMicrocode_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowMicrocode_version.setStatus("mandatory")
_SymShowMicrocode_version_num_Type = DisplayString
_SymShowMicrocode_version_num_Object = MibScalar
symShowMicrocode_version_num = _SymShowMicrocode_version_num_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 5),
    _SymShowMicrocode_version_num_Type()
)
symShowMicrocode_version_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowMicrocode_version_num.setStatus("mandatory")
_SymShowMicrocode_date_Type = DisplayString
_SymShowMicrocode_date_Object = MibScalar
symShowMicrocode_date = _SymShowMicrocode_date_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 6),
    _SymShowMicrocode_date_Type()
)
symShowMicrocode_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowMicrocode_date.setStatus("mandatory")
_SymShowMicrocode_patch_level_Type = DisplayString
_SymShowMicrocode_patch_level_Object = MibScalar
symShowMicrocode_patch_level = _SymShowMicrocode_patch_level_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 7),
    _SymShowMicrocode_patch_level_Type()
)
symShowMicrocode_patch_level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowMicrocode_patch_level.setStatus("mandatory")
_SymShowMicrocode_patch_date_Type = DisplayString
_SymShowMicrocode_patch_date_Object = MibScalar
symShowMicrocode_patch_date = _SymShowMicrocode_patch_date_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 8),
    _SymShowMicrocode_patch_date_Type()
)
symShowMicrocode_patch_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowMicrocode_patch_date.setStatus("mandatory")
_SymShowSymmetrix_pwron_time_Type = TimeTicks
_SymShowSymmetrix_pwron_time_Object = MibScalar
symShowSymmetrix_pwron_time = _SymShowSymmetrix_pwron_time_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 9),
    _SymShowSymmetrix_pwron_time_Type()
)
symShowSymmetrix_pwron_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowSymmetrix_pwron_time.setStatus("mandatory")
_SymShowSymmetrix_uptime_Type = TimeTicks
_SymShowSymmetrix_uptime_Object = MibScalar
symShowSymmetrix_uptime = _SymShowSymmetrix_uptime_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 10),
    _SymShowSymmetrix_uptime_Type()
)
symShowSymmetrix_uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowSymmetrix_uptime.setStatus("mandatory")
_SymShowDb_sync_time_Type = TimeTicks
_SymShowDb_sync_time_Object = MibScalar
symShowDb_sync_time = _SymShowDb_sync_time_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 11),
    _SymShowDb_sync_time_Type()
)
symShowDb_sync_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowDb_sync_time.setStatus("mandatory")
_SymShowDb_sync_bcv_time_Type = TimeTicks
_SymShowDb_sync_bcv_time_Object = MibScalar
symShowDb_sync_bcv_time = _SymShowDb_sync_bcv_time_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 12),
    _SymShowDb_sync_bcv_time_Type()
)
symShowDb_sync_bcv_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowDb_sync_bcv_time.setStatus("mandatory")
_SymShowDb_sync_rdf_time_Type = TimeTicks
_SymShowDb_sync_rdf_time_Object = MibScalar
symShowDb_sync_rdf_time = _SymShowDb_sync_rdf_time_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 13),
    _SymShowDb_sync_rdf_time_Type()
)
symShowDb_sync_rdf_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowDb_sync_rdf_time.setStatus("mandatory")
_SymShowLast_ipl_time_Type = TimeTicks
_SymShowLast_ipl_time_Object = MibScalar
symShowLast_ipl_time = _SymShowLast_ipl_time_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 14),
    _SymShowLast_ipl_time_Type()
)
symShowLast_ipl_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowLast_ipl_time.setStatus("mandatory")
_SymShowLast_fast_ipl_time_Type = TimeTicks
_SymShowLast_fast_ipl_time_Object = MibScalar
symShowLast_fast_ipl_time = _SymShowLast_fast_ipl_time_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 15),
    _SymShowLast_fast_ipl_time_Type()
)
symShowLast_fast_ipl_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowLast_fast_ipl_time.setStatus("mandatory")
_SymShowReserved_Type = DisplayString
_SymShowReserved_Object = MibTableColumn
symShowReserved = _SymShowReserved_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 16),
    _SymShowReserved_Type()
)
symShowReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowReserved.setStatus("mandatory")
_SymShowCache_size_Type = UInt32
_SymShowCache_size_Object = MibScalar
symShowCache_size = _SymShowCache_size_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 17),
    _SymShowCache_size_Type()
)
symShowCache_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowCache_size.setStatus("mandatory")
_SymShowCache_slot_count_Type = UInt32
_SymShowCache_slot_count_Object = MibScalar
symShowCache_slot_count = _SymShowCache_slot_count_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 18),
    _SymShowCache_slot_count_Type()
)
symShowCache_slot_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowCache_slot_count.setStatus("mandatory")
_SymShowMax_wr_pend_slots_Type = UInt32
_SymShowMax_wr_pend_slots_Object = MibScalar
symShowMax_wr_pend_slots = _SymShowMax_wr_pend_slots_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 19),
    _SymShowMax_wr_pend_slots_Type()
)
symShowMax_wr_pend_slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowMax_wr_pend_slots.setStatus("mandatory")
_SymShowMax_da_wr_pend_slots_Type = UInt32
_SymShowMax_da_wr_pend_slots_Object = MibScalar
symShowMax_da_wr_pend_slots = _SymShowMax_da_wr_pend_slots_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 20),
    _SymShowMax_da_wr_pend_slots_Type()
)
symShowMax_da_wr_pend_slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowMax_da_wr_pend_slots.setStatus("mandatory")
_SymShowMax_dev_wr_pend_slots_Type = UInt32
_SymShowMax_dev_wr_pend_slots_Object = MibScalar
symShowMax_dev_wr_pend_slots = _SymShowMax_dev_wr_pend_slots_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 21),
    _SymShowMax_dev_wr_pend_slots_Type()
)
symShowMax_dev_wr_pend_slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowMax_dev_wr_pend_slots.setStatus("mandatory")
_SymShowPermacache_slot_count_Type = UInt32
_SymShowPermacache_slot_count_Object = MibScalar
symShowPermacache_slot_count = _SymShowPermacache_slot_count_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 22),
    _SymShowPermacache_slot_count_Type()
)
symShowPermacache_slot_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPermacache_slot_count.setStatus("mandatory")
_SymShowNum_disks_Type = UInt32
_SymShowNum_disks_Object = MibScalar
symShowNum_disks = _SymShowNum_disks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 23),
    _SymShowNum_disks_Type()
)
symShowNum_disks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowNum_disks.setStatus("mandatory")
_SymShowNum_symdevs_Type = UInt32
_SymShowNum_symdevs_Object = MibScalar
symShowNum_symdevs = _SymShowNum_symdevs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 24),
    _SymShowNum_symdevs_Type()
)
symShowNum_symdevs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowNum_symdevs.setStatus("mandatory")
_SymShowNum_pdevs_Type = UInt32
_SymShowNum_pdevs_Object = MibScalar
symShowNum_pdevs = _SymShowNum_pdevs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 25),
    _SymShowNum_pdevs_Type()
)
symShowNum_pdevs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowNum_pdevs.setStatus("mandatory")
_SymShowAPI_version_Type = DisplayString
_SymShowAPI_version_Object = MibScalar
symShowAPI_version = _SymShowAPI_version_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 26),
    _SymShowAPI_version_Type()
)
symShowAPI_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowAPI_version.setStatus("mandatory")
_SymShowSDDF_configuration_Type = StateValues
_SymShowSDDF_configuration_Object = MibScalar
symShowSDDF_configuration = _SymShowSDDF_configuration_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 27),
    _SymShowSDDF_configuration_Type()
)
symShowSDDF_configuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowSDDF_configuration.setStatus("mandatory")
_SymShowConfig_checksum_Type = UInt32
_SymShowConfig_checksum_Object = MibScalar
symShowConfig_checksum = _SymShowConfig_checksum_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 28),
    _SymShowConfig_checksum_Type()
)
symShowConfig_checksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowConfig_checksum.setStatus("mandatory")
_SymShowNum_powerpath_devs_Type = UInt32
_SymShowNum_powerpath_devs_Object = MibScalar
symShowNum_powerpath_devs = _SymShowNum_powerpath_devs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 1, 1, 29),
    _SymShowNum_powerpath_devs_Type()
)
symShowNum_powerpath_devs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowNum_powerpath_devs.setStatus("mandatory")
_SymShowPDevCountTable_Object = MibTable
symShowPDevCountTable = _SymShowPDevCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    symShowPDevCountTable.setStatus("mandatory")
_SymShowPDevCountEntry_Object = MibTableRow
symShowPDevCountEntry = _SymShowPDevCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 2, 1)
)
symShowPDevCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symShowPDevCountEntry.setStatus("mandatory")
_SymShowPDevCount_Type = Integer32
_SymShowPDevCount_Object = MibTableColumn
symShowPDevCount = _SymShowPDevCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 2, 1, 1),
    _SymShowPDevCount_Type()
)
symShowPDevCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPDevCount.setStatus("mandatory")
_SymShowPDevListTable_Object = MibTable
symShowPDevListTable = _SymShowPDevListTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    symShowPDevListTable.setStatus("mandatory")
_SymShowPDevListEntry_Object = MibTableRow
symShowPDevListEntry = _SymShowPDevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 3, 1)
)
symShowPDevListEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symShowPDevCount"),
)
if mibBuilder.loadTexts:
    symShowPDevListEntry.setStatus("mandatory")
_SymShowPDeviceName_Type = DisplayString
_SymShowPDeviceName_Object = MibTableColumn
symShowPDeviceName = _SymShowPDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 3, 1, 1),
    _SymShowPDeviceName_Type()
)
symShowPDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPDeviceName.setStatus("mandatory")
_SymShowDirectorCountTable_Object = MibTable
symShowDirectorCountTable = _SymShowDirectorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    symShowDirectorCountTable.setStatus("mandatory")
_SymShowDirectorCountEntry_Object = MibTableRow
symShowDirectorCountEntry = _SymShowDirectorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 4, 1)
)
symShowDirectorCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symShowDirectorCountEntry.setStatus("mandatory")
_SymShowDirectorCount_Type = Integer32
_SymShowDirectorCount_Object = MibTableColumn
symShowDirectorCount = _SymShowDirectorCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 4, 1, 1),
    _SymShowDirectorCount_Type()
)
symShowDirectorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowDirectorCount.setStatus("mandatory")
_SymShowDirectorConfigurationTable_Object = MibTable
symShowDirectorConfigurationTable = _SymShowDirectorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    symShowDirectorConfigurationTable.setStatus("mandatory")
_SymShowDirectorConfigurationEntry_Object = MibTableRow
symShowDirectorConfigurationEntry = _SymShowDirectorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1)
)
symShowDirectorConfigurationEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symShowDirectorCount"),
)
if mibBuilder.loadTexts:
    symShowDirectorConfigurationEntry.setStatus("mandatory")
_SymShowDirector_type_Type = DirectorType
_SymShowDirector_type_Object = MibScalar
symShowDirector_type = _SymShowDirector_type_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 1),
    _SymShowDirector_type_Type()
)
symShowDirector_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowDirector_type.setStatus("mandatory")
_SymShowDirector_num_Type = UInt32
_SymShowDirector_num_Object = MibScalar
symShowDirector_num = _SymShowDirector_num_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 2),
    _SymShowDirector_num_Type()
)
symShowDirector_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowDirector_num.setStatus("mandatory")
_SymShowSlot_num_Type = UInt32
_SymShowSlot_num_Object = MibScalar
symShowSlot_num = _SymShowSlot_num_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 3),
    _SymShowSlot_num_Type()
)
symShowSlot_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowSlot_num.setStatus("mandatory")
_SymShowDirector_ident_Type = DisplayString
_SymShowDirector_ident_Object = MibScalar
symShowDirector_ident = _SymShowDirector_ident_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 4),
    _SymShowDirector_ident_Type()
)
symShowDirector_ident.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowDirector_ident.setStatus("mandatory")
_SymShowDirector_status_Type = DirectorStatus
_SymShowDirector_status_Object = MibScalar
symShowDirector_status = _SymShowDirector_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 5),
    _SymShowDirector_status_Type()
)
symShowDirector_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowDirector_status.setStatus("mandatory")
_SymShowScsi_capability_Type = SCSIWidth
_SymShowScsi_capability_Object = MibScalar
symShowScsi_capability = _SymShowScsi_capability_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 6),
    _SymShowScsi_capability_Type()
)
symShowScsi_capability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowScsi_capability.setStatus("mandatory")
_SymShowNum_da_volumes_Type = UInt32
_SymShowNum_da_volumes_Object = MibScalar
symShowNum_da_volumes = _SymShowNum_da_volumes_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 7),
    _SymShowNum_da_volumes_Type()
)
symShowNum_da_volumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowNum_da_volumes.setStatus("mandatory")
_SymShowRemote_symid_Type = DisplayString
_SymShowRemote_symid_Object = MibScalar
symShowRemote_symid = _SymShowRemote_symid_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 8),
    _SymShowRemote_symid_Type()
)
symShowRemote_symid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowRemote_symid.setStatus("mandatory")
_SymShowRa_group_num_Type = UInt32
_SymShowRa_group_num_Object = MibScalar
symShowRa_group_num = _SymShowRa_group_num_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 9),
    _SymShowRa_group_num_Type()
)
symShowRa_group_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowRa_group_num.setStatus("mandatory")
_SymShowRemote_ra_group_num_Type = UInt32
_SymShowRemote_ra_group_num_Object = MibScalar
symShowRemote_ra_group_num = _SymShowRemote_ra_group_num_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 10),
    _SymShowRemote_ra_group_num_Type()
)
symShowRemote_ra_group_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowRemote_ra_group_num.setStatus("mandatory")
_SymShowPrevent_auto_link_recovery_Type = StateValues
_SymShowPrevent_auto_link_recovery_Object = MibScalar
symShowPrevent_auto_link_recovery = _SymShowPrevent_auto_link_recovery_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 11),
    _SymShowPrevent_auto_link_recovery_Type()
)
symShowPrevent_auto_link_recovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPrevent_auto_link_recovery.setStatus("mandatory")
_SymShowPrevent_ra_online_upon_pwron_Type = StateValues
_SymShowPrevent_ra_online_upon_pwron_Object = MibScalar
symShowPrevent_ra_online_upon_pwron = _SymShowPrevent_ra_online_upon_pwron_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 12),
    _SymShowPrevent_ra_online_upon_pwron_Type()
)
symShowPrevent_ra_online_upon_pwron.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPrevent_ra_online_upon_pwron.setStatus("mandatory")
_SymShowNum_ports_Type = UInt32
_SymShowNum_ports_Object = MibScalar
symShowNum_ports = _SymShowNum_ports_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 13),
    _SymShowNum_ports_Type()
)
symShowNum_ports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowNum_ports.setStatus("mandatory")
_SymShowPort0_status_Type = PortStatus
_SymShowPort0_status_Object = MibScalar
symShowPort0_status = _SymShowPort0_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 14),
    _SymShowPort0_status_Type()
)
symShowPort0_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPort0_status.setStatus("mandatory")
_SymShowPort1_status_Type = PortStatus
_SymShowPort1_status_Object = MibScalar
symShowPort1_status = _SymShowPort1_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 15),
    _SymShowPort1_status_Type()
)
symShowPort1_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPort1_status.setStatus("mandatory")
_SymShowPort2_status_Type = PortStatus
_SymShowPort2_status_Object = MibScalar
symShowPort2_status = _SymShowPort2_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 16),
    _SymShowPort2_status_Type()
)
symShowPort2_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPort2_status.setStatus("mandatory")
_SymShowPort3_status_Type = PortStatus
_SymShowPort3_status_Object = MibScalar
symShowPort3_status = _SymShowPort3_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 1, 5, 1, 17),
    _SymShowPort3_status_Type()
)
symShowPort3_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symShowPort3_status.setStatus("mandatory")
_SymDevShow_ObjectIdentity = ObjectIdentity
symDevShow = _SymDevShow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2)
)
_DevShowConfigurationTable_Object = MibTable
devShowConfigurationTable = _DevShowConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    devShowConfigurationTable.setStatus("mandatory")
_DevShowConfigurationEntry_Object = MibTableRow
devShowConfigurationEntry = _DevShowConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1)
)
devShowConfigurationEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symDevListCount"),
)
if mibBuilder.loadTexts:
    devShowConfigurationEntry.setStatus("mandatory")
_DevShowVendor_id_Type = DisplayString
_DevShowVendor_id_Object = MibScalar
devShowVendor_id = _DevShowVendor_id_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 1),
    _DevShowVendor_id_Type()
)
devShowVendor_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowVendor_id.setStatus("mandatory")
_DevShowProduct_id_Type = DisplayString
_DevShowProduct_id_Object = MibScalar
devShowProduct_id = _DevShowProduct_id_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 2),
    _DevShowProduct_id_Type()
)
devShowProduct_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowProduct_id.setStatus("mandatory")
_DevShowProduct_rev_Type = DisplayString
_DevShowProduct_rev_Object = MibScalar
devShowProduct_rev = _DevShowProduct_rev_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 3),
    _DevShowProduct_rev_Type()
)
devShowProduct_rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowProduct_rev.setStatus("mandatory")
_DevShowSymid_Type = DisplayString
_DevShowSymid_Object = MibTableColumn
devShowSymid = _DevShowSymid_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 4),
    _DevShowSymid_Type()
)
devShowSymid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowSymid.setStatus("mandatory")
_DevShowDevice_serial_id_Type = DisplayString
_DevShowDevice_serial_id_Object = MibScalar
devShowDevice_serial_id = _DevShowDevice_serial_id_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 5),
    _DevShowDevice_serial_id_Type()
)
devShowDevice_serial_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDevice_serial_id.setStatus("mandatory")
_DevShowSym_devname_Type = DisplayString
_DevShowSym_devname_Object = MibScalar
devShowSym_devname = _DevShowSym_devname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 6),
    _DevShowSym_devname_Type()
)
devShowSym_devname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowSym_devname.setStatus("mandatory")
_DevShowPdevname_Type = DisplayString
_DevShowPdevname_Object = MibTableColumn
devShowPdevname = _DevShowPdevname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 7),
    _DevShowPdevname_Type()
)
devShowPdevname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowPdevname.setStatus("mandatory")
_DevShowDgname_Type = DisplayString
_DevShowDgname_Object = MibTableColumn
devShowDgname = _DevShowDgname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 8),
    _DevShowDgname_Type()
)
devShowDgname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDgname.setStatus("mandatory")
_DevShowLdevname_Type = DisplayString
_DevShowLdevname_Object = MibTableColumn
devShowLdevname = _DevShowLdevname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 9),
    _DevShowLdevname_Type()
)
devShowLdevname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowLdevname.setStatus("mandatory")


class _DevShowDev_config_Type(Integer32):
    """Custom type devShowDev_config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bcv", 12),
          ("bcv-mirror-2", 14),
          ("bcv-rdf-r1", 15),
          ("bcv-rdf-r1-mirror", 16),
          ("hot-spare", 13),
          ("mirror-2", 1),
          ("mirror-3", 2),
          ("mirror-4", 3),
          ("raid-s", 4),
          ("raid-s-mirror", 5),
          ("rdf-r1", 6),
          ("rdf-r1-mirror", 10),
          ("rdf-r1-raid-s", 8),
          ("rdf-r2", 7),
          ("rdf-r2-mirror", 11),
          ("rdf-r2-raid-s", 9),
          ("unprotected", 0))
    )


_DevShowDev_config_Type.__name__ = "Integer32"
_DevShowDev_config_Object = MibScalar
devShowDev_config = _DevShowDev_config_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 10),
    _DevShowDev_config_Type()
)
devShowDev_config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_config.setStatus("mandatory")


class _DevShowDev_parameters_Type(Integer32):
    """Custom type devShowDev_parameters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("associated-device", 4),
          ("ckd-device", 1),
          ("gatekeeper-device", 2),
          ("meta-head-device", 16),
          ("meta-member-device", 32),
          ("multi-channel-device", 8))
    )


_DevShowDev_parameters_Type.__name__ = "Integer32"
_DevShowDev_parameters_Object = MibScalar
devShowDev_parameters = _DevShowDev_parameters_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 11),
    _DevShowDev_parameters_Type()
)
devShowDev_parameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_parameters.setStatus("mandatory")
_DevShowDev_status_Type = DeviceStatus
_DevShowDev_status_Object = MibScalar
devShowDev_status = _DevShowDev_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 12),
    _DevShowDev_status_Type()
)
devShowDev_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_status.setStatus("mandatory")
_DevShowDev_capacity_Type = UInt32
_DevShowDev_capacity_Object = MibScalar
devShowDev_capacity = _DevShowDev_capacity_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 13),
    _DevShowDev_capacity_Type()
)
devShowDev_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_capacity.setStatus("mandatory")
_DevShowTid_Type = UInt32
_DevShowTid_Object = MibTableColumn
devShowTid = _DevShowTid_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 14),
    _DevShowTid_Type()
)
devShowTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowTid.setStatus("mandatory")
_DevShowLun_Type = UInt32
_DevShowLun_Object = MibTableColumn
devShowLun = _DevShowLun_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 15),
    _DevShowLun_Type()
)
devShowLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowLun.setStatus("mandatory")
_DevShowDirector_num_Type = Integer32
_DevShowDirector_num_Object = MibScalar
devShowDirector_num = _DevShowDirector_num_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 16),
    _DevShowDirector_num_Type()
)
devShowDirector_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDirector_num.setStatus("mandatory")
_DevShowDirector_slot_num_Type = Integer32
_DevShowDirector_slot_num_Object = MibScalar
devShowDirector_slot_num = _DevShowDirector_slot_num_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 17),
    _DevShowDirector_slot_num_Type()
)
devShowDirector_slot_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDirector_slot_num.setStatus("mandatory")
_DevShowDirector_ident_Type = DisplayString
_DevShowDirector_ident_Object = MibScalar
devShowDirector_ident = _DevShowDirector_ident_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 18),
    _DevShowDirector_ident_Type()
)
devShowDirector_ident.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDirector_ident.setStatus("mandatory")
_DevShowDirector_port_num_Type = Integer32
_DevShowDirector_port_num_Object = MibScalar
devShowDirector_port_num = _DevShowDirector_port_num_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 19),
    _DevShowDirector_port_num_Type()
)
devShowDirector_port_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDirector_port_num.setStatus("mandatory")
_DevShowMset_M1_type_Type = DeviceType
_DevShowMset_M1_type_Object = MibScalar
devShowMset_M1_type = _DevShowMset_M1_type_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 20),
    _DevShowMset_M1_type_Type()
)
devShowMset_M1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M1_type.setStatus("mandatory")
_DevShowMset_M2_type_Type = DeviceType
_DevShowMset_M2_type_Object = MibScalar
devShowMset_M2_type = _DevShowMset_M2_type_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 21),
    _DevShowMset_M2_type_Type()
)
devShowMset_M2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M2_type.setStatus("mandatory")
_DevShowMset_M3_type_Type = DeviceType
_DevShowMset_M3_type_Object = MibScalar
devShowMset_M3_type = _DevShowMset_M3_type_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 22),
    _DevShowMset_M3_type_Type()
)
devShowMset_M3_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M3_type.setStatus("mandatory")
_DevShowMset_M4_type_Type = DeviceType
_DevShowMset_M4_type_Object = MibScalar
devShowMset_M4_type = _DevShowMset_M4_type_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 23),
    _DevShowMset_M4_type_Type()
)
devShowMset_M4_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M4_type.setStatus("mandatory")
_DevShowMset_M1_status_Type = DeviceStatus
_DevShowMset_M1_status_Object = MibScalar
devShowMset_M1_status = _DevShowMset_M1_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 24),
    _DevShowMset_M1_status_Type()
)
devShowMset_M1_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M1_status.setStatus("mandatory")
_DevShowMset_M2_status_Type = DeviceStatus
_DevShowMset_M2_status_Object = MibScalar
devShowMset_M2_status = _DevShowMset_M2_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 25),
    _DevShowMset_M2_status_Type()
)
devShowMset_M2_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M2_status.setStatus("mandatory")
_DevShowMset_M3_status_Type = DeviceStatus
_DevShowMset_M3_status_Object = MibScalar
devShowMset_M3_status = _DevShowMset_M3_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 26),
    _DevShowMset_M3_status_Type()
)
devShowMset_M3_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M3_status.setStatus("mandatory")
_DevShowMset_M4_status_Type = DeviceStatus
_DevShowMset_M4_status_Object = MibScalar
devShowMset_M4_status = _DevShowMset_M4_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 27),
    _DevShowMset_M4_status_Type()
)
devShowMset_M4_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M4_status.setStatus("mandatory")
_DevShowMset_M1_invalid_tracks_Type = Integer32
_DevShowMset_M1_invalid_tracks_Object = MibScalar
devShowMset_M1_invalid_tracks = _DevShowMset_M1_invalid_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 28),
    _DevShowMset_M1_invalid_tracks_Type()
)
devShowMset_M1_invalid_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M1_invalid_tracks.setStatus("mandatory")
_DevShowMset_M2_invalid_tracks_Type = Integer32
_DevShowMset_M2_invalid_tracks_Object = MibScalar
devShowMset_M2_invalid_tracks = _DevShowMset_M2_invalid_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 29),
    _DevShowMset_M2_invalid_tracks_Type()
)
devShowMset_M2_invalid_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M2_invalid_tracks.setStatus("mandatory")
_DevShowMset_M3_invalid_tracks_Type = Integer32
_DevShowMset_M3_invalid_tracks_Object = MibScalar
devShowMset_M3_invalid_tracks = _DevShowMset_M3_invalid_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 30),
    _DevShowMset_M3_invalid_tracks_Type()
)
devShowMset_M3_invalid_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M3_invalid_tracks.setStatus("mandatory")
_DevShowMset_M4_invalid_tracks_Type = Integer32
_DevShowMset_M4_invalid_tracks_Object = MibScalar
devShowMset_M4_invalid_tracks = _DevShowMset_M4_invalid_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 31),
    _DevShowMset_M4_invalid_tracks_Type()
)
devShowMset_M4_invalid_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowMset_M4_invalid_tracks.setStatus("mandatory")
_DevShowDirector_port_status_Type = DeviceStatus
_DevShowDirector_port_status_Object = MibScalar
devShowDirector_port_status = _DevShowDirector_port_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 48),
    _DevShowDirector_port_status_Type()
)
devShowDirector_port_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDirector_port_status.setStatus("mandatory")
_DevShowDev_sa_status_Type = DeviceStatus
_DevShowDev_sa_status_Object = MibScalar
devShowDev_sa_status = _DevShowDev_sa_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 49),
    _DevShowDev_sa_status_Type()
)
devShowDev_sa_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_sa_status.setStatus("mandatory")
_DevShowVbus_Type = Integer32
_DevShowVbus_Object = MibTableColumn
devShowVbus = _DevShowVbus_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 50),
    _DevShowVbus_Type()
)
devShowVbus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowVbus.setStatus("mandatory")
_DevShowEmulation_Type = DeviceEmulation
_DevShowEmulation_Object = MibTableColumn
devShowEmulation = _DevShowEmulation_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 51),
    _DevShowEmulation_Type()
)
devShowEmulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowEmulation.setStatus("mandatory")
_DevShowDev_block_size_Type = UInt32
_DevShowDev_block_size_Object = MibScalar
devShowDev_block_size = _DevShowDev_block_size_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 52),
    _DevShowDev_block_size_Type()
)
devShowDev_block_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_block_size.setStatus("mandatory")
_DevShowSCSI_negotiation_Type = SCSIWidth
_DevShowSCSI_negotiation_Object = MibScalar
devShowSCSI_negotiation = _DevShowSCSI_negotiation_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 53),
    _DevShowSCSI_negotiation_Type()
)
devShowSCSI_negotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowSCSI_negotiation.setStatus("mandatory")
_DevShowSCSI_method_Type = SCSIMethod
_DevShowSCSI_method_Object = MibScalar
devShowSCSI_method = _DevShowSCSI_method_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 54),
    _DevShowSCSI_method_Type()
)
devShowSCSI_method.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowSCSI_method.setStatus("mandatory")
_DevShowDev_cylinders_Type = UInt32
_DevShowDev_cylinders_Object = MibScalar
devShowDev_cylinders = _DevShowDev_cylinders_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 55),
    _DevShowDev_cylinders_Type()
)
devShowDev_cylinders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_cylinders.setStatus("mandatory")
_DevShowAttached_bcv_symdev_Type = DisplayString
_DevShowAttached_bcv_symdev_Object = MibScalar
devShowAttached_bcv_symdev = _DevShowAttached_bcv_symdev_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 1, 1, 56),
    _DevShowAttached_bcv_symdev_Type()
)
devShowAttached_bcv_symdev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowAttached_bcv_symdev.setStatus("mandatory")
_DevShowRDFInfoTable_Object = MibTable
devShowRDFInfoTable = _DevShowRDFInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    devShowRDFInfoTable.setStatus("mandatory")
_DevShowRDFInfoEntry_Object = MibTableRow
devShowRDFInfoEntry = _DevShowRDFInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1)
)
devShowRDFInfoEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symDevListCount"),
)
if mibBuilder.loadTexts:
    devShowRDFInfoEntry.setStatus("mandatory")
_DevShowRemote_symid_Type = DisplayString
_DevShowRemote_symid_Object = MibScalar
devShowRemote_symid = _DevShowRemote_symid_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 1),
    _DevShowRemote_symid_Type()
)
devShowRemote_symid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowRemote_symid.setStatus("mandatory")
_DevShowRemote_sym_devname_Type = DisplayString
_DevShowRemote_sym_devname_Object = MibScalar
devShowRemote_sym_devname = _DevShowRemote_sym_devname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 2),
    _DevShowRemote_sym_devname_Type()
)
devShowRemote_sym_devname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowRemote_sym_devname.setStatus("mandatory")
_DevShowRa_group_number_Type = Integer32
_DevShowRa_group_number_Object = MibScalar
devShowRa_group_number = _DevShowRa_group_number_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 3),
    _DevShowRa_group_number_Type()
)
devShowRa_group_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowRa_group_number.setStatus("mandatory")
_DevShowDev_rdf_type_Type = RDFType
_DevShowDev_rdf_type_Object = MibScalar
devShowDev_rdf_type = _DevShowDev_rdf_type_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 4),
    _DevShowDev_rdf_type_Type()
)
devShowDev_rdf_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_rdf_type.setStatus("mandatory")
_DevShowDev_ra_status_Type = DeviceStatus
_DevShowDev_ra_status_Object = MibScalar
devShowDev_ra_status = _DevShowDev_ra_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 5),
    _DevShowDev_ra_status_Type()
)
devShowDev_ra_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_ra_status.setStatus("mandatory")
_DevShowDev_link_status_Type = DeviceStatus
_DevShowDev_link_status_Object = MibScalar
devShowDev_link_status = _DevShowDev_link_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 6),
    _DevShowDev_link_status_Type()
)
devShowDev_link_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_link_status.setStatus("mandatory")
_DevShowRdf_mode_Type = RDFMode
_DevShowRdf_mode_Object = MibScalar
devShowRdf_mode = _DevShowRdf_mode_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 7),
    _DevShowRdf_mode_Type()
)
devShowRdf_mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowRdf_mode.setStatus("mandatory")
_DevShowRdf_pair_state_Type = RDFPairState
_DevShowRdf_pair_state_Object = MibScalar
devShowRdf_pair_state = _DevShowRdf_pair_state_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 8),
    _DevShowRdf_pair_state_Type()
)
devShowRdf_pair_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowRdf_pair_state.setStatus("mandatory")
_DevShowRdf_domino_Type = StateValues
_DevShowRdf_domino_Object = MibScalar
devShowRdf_domino = _DevShowRdf_domino_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 9),
    _DevShowRdf_domino_Type()
)
devShowRdf_domino.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowRdf_domino.setStatus("mandatory")
_DevShowAdaptive_copy_Type = RDFAdaptiveCopy
_DevShowAdaptive_copy_Object = MibScalar
devShowAdaptive_copy = _DevShowAdaptive_copy_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 10),
    _DevShowAdaptive_copy_Type()
)
devShowAdaptive_copy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowAdaptive_copy.setStatus("mandatory")
_DevShowAdaptive_copy_skew_Type = UInt32
_DevShowAdaptive_copy_skew_Object = MibScalar
devShowAdaptive_copy_skew = _DevShowAdaptive_copy_skew_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 11),
    _DevShowAdaptive_copy_skew_Type()
)
devShowAdaptive_copy_skew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowAdaptive_copy_skew.setStatus("mandatory")
_DevShowNum_r1_invalid_tracks_Type = UInt32
_DevShowNum_r1_invalid_tracks_Object = MibScalar
devShowNum_r1_invalid_tracks = _DevShowNum_r1_invalid_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 12),
    _DevShowNum_r1_invalid_tracks_Type()
)
devShowNum_r1_invalid_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowNum_r1_invalid_tracks.setStatus("mandatory")
_DevShowNum_r2_invalid_tracks_Type = UInt32
_DevShowNum_r2_invalid_tracks_Object = MibScalar
devShowNum_r2_invalid_tracks = _DevShowNum_r2_invalid_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 13),
    _DevShowNum_r2_invalid_tracks_Type()
)
devShowNum_r2_invalid_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowNum_r2_invalid_tracks.setStatus("mandatory")
_DevShowDev_rdf_state_Type = DeviceStatus
_DevShowDev_rdf_state_Object = MibScalar
devShowDev_rdf_state = _DevShowDev_rdf_state_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 14),
    _DevShowDev_rdf_state_Type()
)
devShowDev_rdf_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_rdf_state.setStatus("mandatory")
_DevShowRemote_dev_rdf_state_Type = DeviceStatus
_DevShowRemote_dev_rdf_state_Object = MibScalar
devShowRemote_dev_rdf_state = _DevShowRemote_dev_rdf_state_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 15),
    _DevShowRemote_dev_rdf_state_Type()
)
devShowRemote_dev_rdf_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowRemote_dev_rdf_state.setStatus("mandatory")
_DevShowRdf_status_Type = DeviceStatus
_DevShowRdf_status_Object = MibScalar
devShowRdf_status = _DevShowRdf_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 16),
    _DevShowRdf_status_Type()
)
devShowRdf_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowRdf_status.setStatus("mandatory")
_DevShowLink_domino_Type = StateValues
_DevShowLink_domino_Object = MibScalar
devShowLink_domino = _DevShowLink_domino_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 17),
    _DevShowLink_domino_Type()
)
devShowLink_domino.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowLink_domino.setStatus("mandatory")
_DevShowPrevent_auto_link_recovery_Type = StateValues
_DevShowPrevent_auto_link_recovery_Object = MibScalar
devShowPrevent_auto_link_recovery = _DevShowPrevent_auto_link_recovery_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 18),
    _DevShowPrevent_auto_link_recovery_Type()
)
devShowPrevent_auto_link_recovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowPrevent_auto_link_recovery.setStatus("mandatory")
_DevShowLink_config_Type = RDFLinkConfig
_DevShowLink_config_Object = MibScalar
devShowLink_config = _DevShowLink_config_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 19),
    _DevShowLink_config_Type()
)
devShowLink_config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowLink_config.setStatus("mandatory")
_DevShowSuspend_state_Type = RDDFTransientState
_DevShowSuspend_state_Object = MibScalar
devShowSuspend_state = _DevShowSuspend_state_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 20),
    _DevShowSuspend_state_Type()
)
devShowSuspend_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowSuspend_state.setStatus("mandatory")
_DevShowConsistency_state_Type = StateValues
_DevShowConsistency_state_Object = MibScalar
devShowConsistency_state = _DevShowConsistency_state_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 21),
    _DevShowConsistency_state_Type()
)
devShowConsistency_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowConsistency_state.setStatus("mandatory")
_DevShowAdaptive_copy_wp_state_Type = RDDFTransientState
_DevShowAdaptive_copy_wp_state_Object = MibScalar
devShowAdaptive_copy_wp_state = _DevShowAdaptive_copy_wp_state_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 22),
    _DevShowAdaptive_copy_wp_state_Type()
)
devShowAdaptive_copy_wp_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowAdaptive_copy_wp_state.setStatus("mandatory")
_DevShowPrevent_ra_online_upon_pwron_Type = StateValues
_DevShowPrevent_ra_online_upon_pwron_Object = MibScalar
devShowPrevent_ra_online_upon_pwron = _DevShowPrevent_ra_online_upon_pwron_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 2, 1, 23),
    _DevShowPrevent_ra_online_upon_pwron_Type()
)
devShowPrevent_ra_online_upon_pwron.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowPrevent_ra_online_upon_pwron.setStatus("mandatory")
_DevShowBCVInfoTable_Object = MibTable
devShowBCVInfoTable = _DevShowBCVInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3)
)
if mibBuilder.loadTexts:
    devShowBCVInfoTable.setStatus("mandatory")
_DevShowBCVInfoEntry_Object = MibTableRow
devShowBCVInfoEntry = _DevShowBCVInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1)
)
devShowBCVInfoEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symDevListCount"),
)
if mibBuilder.loadTexts:
    devShowBCVInfoEntry.setStatus("mandatory")
_DevShowDev_serial_id_Type = DisplayString
_DevShowDev_serial_id_Object = MibScalar
devShowDev_serial_id = _DevShowDev_serial_id_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 1),
    _DevShowDev_serial_id_Type()
)
devShowDev_serial_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_serial_id.setStatus("mandatory")
_DevShowDev_sym_devname_Type = DisplayString
_DevShowDev_sym_devname_Object = MibScalar
devShowDev_sym_devname = _DevShowDev_sym_devname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 2),
    _DevShowDev_sym_devname_Type()
)
devShowDev_sym_devname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_sym_devname.setStatus("mandatory")
_DevShowDev_dgname_Type = DisplayString
_DevShowDev_dgname_Object = MibScalar
devShowDev_dgname = _DevShowDev_dgname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 3),
    _DevShowDev_dgname_Type()
)
devShowDev_dgname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowDev_dgname.setStatus("mandatory")
_DevShowBcvdev_serial_id_Type = DisplayString
_DevShowBcvdev_serial_id_Object = MibScalar
devShowBcvdev_serial_id = _DevShowBcvdev_serial_id_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 4),
    _DevShowBcvdev_serial_id_Type()
)
devShowBcvdev_serial_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowBcvdev_serial_id.setStatus("mandatory")
_DevShowBcvdev_sym_devname_Type = DisplayString
_DevShowBcvdev_sym_devname_Object = MibScalar
devShowBcvdev_sym_devname = _DevShowBcvdev_sym_devname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 5),
    _DevShowBcvdev_sym_devname_Type()
)
devShowBcvdev_sym_devname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowBcvdev_sym_devname.setStatus("mandatory")
_DevShowBcvdev_dgname_Type = DisplayString
_DevShowBcvdev_dgname_Object = MibScalar
devShowBcvdev_dgname = _DevShowBcvdev_dgname_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 6),
    _DevShowBcvdev_dgname_Type()
)
devShowBcvdev_dgname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowBcvdev_dgname.setStatus("mandatory")
_DevShowBcv_pair_state_Type = BCVState
_DevShowBcv_pair_state_Object = MibScalar
devShowBcv_pair_state = _DevShowBcv_pair_state_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 7),
    _DevShowBcv_pair_state_Type()
)
devShowBcv_pair_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowBcv_pair_state.setStatus("mandatory")
_DevShowNum_dev_invalid_tracks_Type = UInt32
_DevShowNum_dev_invalid_tracks_Object = MibScalar
devShowNum_dev_invalid_tracks = _DevShowNum_dev_invalid_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 8),
    _DevShowNum_dev_invalid_tracks_Type()
)
devShowNum_dev_invalid_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowNum_dev_invalid_tracks.setStatus("mandatory")
_DevShowNum_bcvdev_invalid_tracks_Type = UInt32
_DevShowNum_bcvdev_invalid_tracks_Object = MibScalar
devShowNum_bcvdev_invalid_tracks = _DevShowNum_bcvdev_invalid_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 9),
    _DevShowNum_bcvdev_invalid_tracks_Type()
)
devShowNum_bcvdev_invalid_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowNum_bcvdev_invalid_tracks.setStatus("mandatory")
_DevShowBcvdev_status_Type = DeviceStatus
_DevShowBcvdev_status_Object = MibScalar
devShowBcvdev_status = _DevShowBcvdev_status_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 2, 2, 3, 1, 10),
    _DevShowBcvdev_status_Type()
)
devShowBcvdev_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devShowBcvdev_status.setStatus("mandatory")
_SymAPIStatistics_ObjectIdentity = ObjectIdentity
symAPIStatistics = _SymAPIStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3)
)
_SymStatTable_Object = MibTable
symStatTable = _SymStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    symStatTable.setStatus("mandatory")
_SymStatEntry_Object = MibTableRow
symStatEntry = _SymStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1)
)
symStatEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
)
if mibBuilder.loadTexts:
    symStatEntry.setStatus("mandatory")
_SymstatTime_stamp_Type = TimeTicks
_SymstatTime_stamp_Object = MibScalar
symstatTime_stamp = _SymstatTime_stamp_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 1),
    _SymstatTime_stamp_Type()
)
symstatTime_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatTime_stamp.setStatus("mandatory")
_SymstatNum_rw_reqs_Type = UInt32
_SymstatNum_rw_reqs_Object = MibScalar
symstatNum_rw_reqs = _SymstatNum_rw_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 2),
    _SymstatNum_rw_reqs_Type()
)
symstatNum_rw_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_rw_reqs.setStatus("mandatory")
_SymstatNum_read_reqs_Type = UInt32
_SymstatNum_read_reqs_Object = MibScalar
symstatNum_read_reqs = _SymstatNum_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 3),
    _SymstatNum_read_reqs_Type()
)
symstatNum_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_read_reqs.setStatus("mandatory")
_SymstatNum_write_reqs_Type = UInt32
_SymstatNum_write_reqs_Object = MibScalar
symstatNum_write_reqs = _SymstatNum_write_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 4),
    _SymstatNum_write_reqs_Type()
)
symstatNum_write_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_write_reqs.setStatus("mandatory")
_SymstatNum_rw_hits_Type = UInt32
_SymstatNum_rw_hits_Object = MibScalar
symstatNum_rw_hits = _SymstatNum_rw_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 5),
    _SymstatNum_rw_hits_Type()
)
symstatNum_rw_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_rw_hits.setStatus("mandatory")
_SymstatNum_read_hits_Type = UInt32
_SymstatNum_read_hits_Object = MibScalar
symstatNum_read_hits = _SymstatNum_read_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 6),
    _SymstatNum_read_hits_Type()
)
symstatNum_read_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_read_hits.setStatus("mandatory")
_SymstatNum_write_hits_Type = UInt32
_SymstatNum_write_hits_Object = MibScalar
symstatNum_write_hits = _SymstatNum_write_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 7),
    _SymstatNum_write_hits_Type()
)
symstatNum_write_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_write_hits.setStatus("mandatory")
_SymstatNum_blocks_read_Type = UInt32
_SymstatNum_blocks_read_Object = MibScalar
symstatNum_blocks_read = _SymstatNum_blocks_read_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 12),
    _SymstatNum_blocks_read_Type()
)
symstatNum_blocks_read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_blocks_read.setStatus("mandatory")
_SymstatNum_blocks_written_Type = UInt32
_SymstatNum_blocks_written_Object = MibScalar
symstatNum_blocks_written = _SymstatNum_blocks_written_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 17),
    _SymstatNum_blocks_written_Type()
)
symstatNum_blocks_written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_blocks_written.setStatus("mandatory")
_SymstatNum_seq_read_reqs_Type = UInt32
_SymstatNum_seq_read_reqs_Object = MibScalar
symstatNum_seq_read_reqs = _SymstatNum_seq_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 18),
    _SymstatNum_seq_read_reqs_Type()
)
symstatNum_seq_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_seq_read_reqs.setStatus("mandatory")
_SymstatNum_prefetched_tracks_Type = UInt32
_SymstatNum_prefetched_tracks_Object = MibScalar
symstatNum_prefetched_tracks = _SymstatNum_prefetched_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 19),
    _SymstatNum_prefetched_tracks_Type()
)
symstatNum_prefetched_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_prefetched_tracks.setStatus("mandatory")
_SymstatNum_destaged_tracks_Type = UInt32
_SymstatNum_destaged_tracks_Object = MibScalar
symstatNum_destaged_tracks = _SymstatNum_destaged_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 20),
    _SymstatNum_destaged_tracks_Type()
)
symstatNum_destaged_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_destaged_tracks.setStatus("mandatory")
_SymstatNum_deferred_writes_Type = UInt32
_SymstatNum_deferred_writes_Object = MibScalar
symstatNum_deferred_writes = _SymstatNum_deferred_writes_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 21),
    _SymstatNum_deferred_writes_Type()
)
symstatNum_deferred_writes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_deferred_writes.setStatus("mandatory")
_SymstatNum_delayed_dfw_Type = UInt32
_SymstatNum_delayed_dfw_Object = MibScalar
symstatNum_delayed_dfw = _SymstatNum_delayed_dfw_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 22),
    _SymstatNum_delayed_dfw_Type()
)
symstatNum_delayed_dfw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_delayed_dfw.setStatus("mandatory")
_SymstatNum_wr_pend_tracks_Type = UInt32
_SymstatNum_wr_pend_tracks_Object = MibScalar
symstatNum_wr_pend_tracks = _SymstatNum_wr_pend_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 23),
    _SymstatNum_wr_pend_tracks_Type()
)
symstatNum_wr_pend_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_wr_pend_tracks.setStatus("mandatory")
_SymstatNum_format_pend_tracks_Type = UInt32
_SymstatNum_format_pend_tracks_Object = MibScalar
symstatNum_format_pend_tracks = _SymstatNum_format_pend_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 24),
    _SymstatNum_format_pend_tracks_Type()
)
symstatNum_format_pend_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_format_pend_tracks.setStatus("mandatory")
_SymstatDevice_max_wp_limit_Type = UInt32
_SymstatDevice_max_wp_limit_Object = MibScalar
symstatDevice_max_wp_limit = _SymstatDevice_max_wp_limit_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 25),
    _SymstatDevice_max_wp_limit_Type()
)
symstatDevice_max_wp_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatDevice_max_wp_limit.setStatus("mandatory")
_SymstatNum_sa_cdb_reqs_Type = UInt32
_SymstatNum_sa_cdb_reqs_Object = MibScalar
symstatNum_sa_cdb_reqs = _SymstatNum_sa_cdb_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 26),
    _SymstatNum_sa_cdb_reqs_Type()
)
symstatNum_sa_cdb_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_sa_cdb_reqs.setStatus("mandatory")
_SymstatNum_sa_rw_reqs_Type = UInt32
_SymstatNum_sa_rw_reqs_Object = MibScalar
symstatNum_sa_rw_reqs = _SymstatNum_sa_rw_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 27),
    _SymstatNum_sa_rw_reqs_Type()
)
symstatNum_sa_rw_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_sa_rw_reqs.setStatus("mandatory")
_SymstatNum_sa_read_reqs_Type = UInt32
_SymstatNum_sa_read_reqs_Object = MibScalar
symstatNum_sa_read_reqs = _SymstatNum_sa_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 28),
    _SymstatNum_sa_read_reqs_Type()
)
symstatNum_sa_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_sa_read_reqs.setStatus("mandatory")
_SymstatNum_sa_write_reqs_Type = UInt32
_SymstatNum_sa_write_reqs_Object = MibScalar
symstatNum_sa_write_reqs = _SymstatNum_sa_write_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 29),
    _SymstatNum_sa_write_reqs_Type()
)
symstatNum_sa_write_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_sa_write_reqs.setStatus("mandatory")
_SymstatNum_sa_rw_hits_Type = UInt32
_SymstatNum_sa_rw_hits_Object = MibScalar
symstatNum_sa_rw_hits = _SymstatNum_sa_rw_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 30),
    _SymstatNum_sa_rw_hits_Type()
)
symstatNum_sa_rw_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_sa_rw_hits.setStatus("mandatory")
_SymstatNum_free_permacache_slots_Type = UInt32
_SymstatNum_free_permacache_slots_Object = MibScalar
symstatNum_free_permacache_slots = _SymstatNum_free_permacache_slots_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 31),
    _SymstatNum_free_permacache_slots_Type()
)
symstatNum_free_permacache_slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_free_permacache_slots.setStatus("mandatory")
_SymstatNum_used_permacache_slots_Type = UInt32
_SymstatNum_used_permacache_slots_Object = MibScalar
symstatNum_used_permacache_slots = _SymstatNum_used_permacache_slots_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 1, 1, 32),
    _SymstatNum_used_permacache_slots_Type()
)
symstatNum_used_permacache_slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symstatNum_used_permacache_slots.setStatus("mandatory")
_DevStatTable_Object = MibTable
devStatTable = _DevStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    devStatTable.setStatus("mandatory")
_DevStatEntry_Object = MibTableRow
devStatEntry = _DevStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1)
)
devStatEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symDevListCount"),
)
if mibBuilder.loadTexts:
    devStatEntry.setStatus("mandatory")
_DevstatTime_stamp_Type = TimeTicks
_DevstatTime_stamp_Object = MibScalar
devstatTime_stamp = _DevstatTime_stamp_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 1),
    _DevstatTime_stamp_Type()
)
devstatTime_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatTime_stamp.setStatus("mandatory")
_DevstatNum_sym_timeslices_Type = UInt32
_DevstatNum_sym_timeslices_Object = MibScalar
devstatNum_sym_timeslices = _DevstatNum_sym_timeslices_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 2),
    _DevstatNum_sym_timeslices_Type()
)
devstatNum_sym_timeslices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_sym_timeslices.setStatus("mandatory")
_DevstatNum_rw_reqs_Type = UInt32
_DevstatNum_rw_reqs_Object = MibScalar
devstatNum_rw_reqs = _DevstatNum_rw_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 3),
    _DevstatNum_rw_reqs_Type()
)
devstatNum_rw_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_rw_reqs.setStatus("mandatory")
_DevstatNum_read_reqs_Type = UInt32
_DevstatNum_read_reqs_Object = MibScalar
devstatNum_read_reqs = _DevstatNum_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 4),
    _DevstatNum_read_reqs_Type()
)
devstatNum_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_read_reqs.setStatus("mandatory")
_DevstatNum_write_reqs_Type = UInt32
_DevstatNum_write_reqs_Object = MibScalar
devstatNum_write_reqs = _DevstatNum_write_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 5),
    _DevstatNum_write_reqs_Type()
)
devstatNum_write_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_write_reqs.setStatus("mandatory")
_DevstatNum_rw_hits_Type = UInt32
_DevstatNum_rw_hits_Object = MibScalar
devstatNum_rw_hits = _DevstatNum_rw_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 6),
    _DevstatNum_rw_hits_Type()
)
devstatNum_rw_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_rw_hits.setStatus("mandatory")
_DevstatNum_read_hits_Type = UInt32
_DevstatNum_read_hits_Object = MibScalar
devstatNum_read_hits = _DevstatNum_read_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 7),
    _DevstatNum_read_hits_Type()
)
devstatNum_read_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_read_hits.setStatus("mandatory")
_DevstatNum_write_hits_Type = UInt32
_DevstatNum_write_hits_Object = MibScalar
devstatNum_write_hits = _DevstatNum_write_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 8),
    _DevstatNum_write_hits_Type()
)
devstatNum_write_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_write_hits.setStatus("mandatory")
_DevstatNum_blocks_read_Type = UInt32
_DevstatNum_blocks_read_Object = MibScalar
devstatNum_blocks_read = _DevstatNum_blocks_read_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 13),
    _DevstatNum_blocks_read_Type()
)
devstatNum_blocks_read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_blocks_read.setStatus("mandatory")
_DevstatNum_blocks_written_Type = UInt32
_DevstatNum_blocks_written_Object = MibScalar
devstatNum_blocks_written = _DevstatNum_blocks_written_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 18),
    _DevstatNum_blocks_written_Type()
)
devstatNum_blocks_written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_blocks_written.setStatus("mandatory")
_DevstatNum_seq_read_reqs_Type = UInt32
_DevstatNum_seq_read_reqs_Object = MibScalar
devstatNum_seq_read_reqs = _DevstatNum_seq_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 19),
    _DevstatNum_seq_read_reqs_Type()
)
devstatNum_seq_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_seq_read_reqs.setStatus("mandatory")
_DevstatNum_prefetched_tracks_Type = UInt32
_DevstatNum_prefetched_tracks_Object = MibScalar
devstatNum_prefetched_tracks = _DevstatNum_prefetched_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 20),
    _DevstatNum_prefetched_tracks_Type()
)
devstatNum_prefetched_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_prefetched_tracks.setStatus("mandatory")
_DevstatNum_destaged_tracks_Type = UInt32
_DevstatNum_destaged_tracks_Object = MibScalar
devstatNum_destaged_tracks = _DevstatNum_destaged_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 21),
    _DevstatNum_destaged_tracks_Type()
)
devstatNum_destaged_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_destaged_tracks.setStatus("mandatory")
_DevstatNum_deferred_writes_Type = UInt32
_DevstatNum_deferred_writes_Object = MibScalar
devstatNum_deferred_writes = _DevstatNum_deferred_writes_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 22),
    _DevstatNum_deferred_writes_Type()
)
devstatNum_deferred_writes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_deferred_writes.setStatus("mandatory")
_DevstatNum_delayed_dfw_Type = UInt32
_DevstatNum_delayed_dfw_Object = MibScalar
devstatNum_delayed_dfw = _DevstatNum_delayed_dfw_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 23),
    _DevstatNum_delayed_dfw_Type()
)
devstatNum_delayed_dfw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_delayed_dfw.setStatus("mandatory")
_DevstatNum_wp_tracks_Type = UInt32
_DevstatNum_wp_tracks_Object = MibScalar
devstatNum_wp_tracks = _DevstatNum_wp_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 24),
    _DevstatNum_wp_tracks_Type()
)
devstatNum_wp_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_wp_tracks.setStatus("mandatory")
_DevstatNum_format_pend_tracks_Type = UInt32
_DevstatNum_format_pend_tracks_Object = MibScalar
devstatNum_format_pend_tracks = _DevstatNum_format_pend_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 25),
    _DevstatNum_format_pend_tracks_Type()
)
devstatNum_format_pend_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatNum_format_pend_tracks.setStatus("mandatory")
_DevstatDevice_max_wp_limit_Type = UInt32
_DevstatDevice_max_wp_limit_Object = MibScalar
devstatDevice_max_wp_limit = _DevstatDevice_max_wp_limit_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 2, 1, 26),
    _DevstatDevice_max_wp_limit_Type()
)
devstatDevice_max_wp_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devstatDevice_max_wp_limit.setStatus("mandatory")
_PDevStatTable_Object = MibTable
pDevStatTable = _PDevStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    pDevStatTable.setStatus("mandatory")
_PDevStatEntry_Object = MibTableRow
pDevStatEntry = _PDevStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1)
)
pDevStatEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symPDevListCount"),
)
if mibBuilder.loadTexts:
    pDevStatEntry.setStatus("mandatory")
_PdevstatTime_stamp_Type = TimeTicks
_PdevstatTime_stamp_Object = MibScalar
pdevstatTime_stamp = _PdevstatTime_stamp_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 1),
    _PdevstatTime_stamp_Type()
)
pdevstatTime_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatTime_stamp.setStatus("mandatory")
_PdevstatNum_sym_timeslices_Type = UInt32
_PdevstatNum_sym_timeslices_Object = MibScalar
pdevstatNum_sym_timeslices = _PdevstatNum_sym_timeslices_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 2),
    _PdevstatNum_sym_timeslices_Type()
)
pdevstatNum_sym_timeslices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_sym_timeslices.setStatus("mandatory")
_PdevstatNum_rw_reqs_Type = UInt32
_PdevstatNum_rw_reqs_Object = MibScalar
pdevstatNum_rw_reqs = _PdevstatNum_rw_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 3),
    _PdevstatNum_rw_reqs_Type()
)
pdevstatNum_rw_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_rw_reqs.setStatus("mandatory")
_PdevstatNum_read_reqs_Type = UInt32
_PdevstatNum_read_reqs_Object = MibScalar
pdevstatNum_read_reqs = _PdevstatNum_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 4),
    _PdevstatNum_read_reqs_Type()
)
pdevstatNum_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_read_reqs.setStatus("mandatory")
_PdevstatNum_write_reqs_Type = UInt32
_PdevstatNum_write_reqs_Object = MibScalar
pdevstatNum_write_reqs = _PdevstatNum_write_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 5),
    _PdevstatNum_write_reqs_Type()
)
pdevstatNum_write_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_write_reqs.setStatus("mandatory")
_PdevstatNum_rw_hits_Type = UInt32
_PdevstatNum_rw_hits_Object = MibScalar
pdevstatNum_rw_hits = _PdevstatNum_rw_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 6),
    _PdevstatNum_rw_hits_Type()
)
pdevstatNum_rw_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_rw_hits.setStatus("mandatory")
_PdevstatNum_read_hits_Type = UInt32
_PdevstatNum_read_hits_Object = MibScalar
pdevstatNum_read_hits = _PdevstatNum_read_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 7),
    _PdevstatNum_read_hits_Type()
)
pdevstatNum_read_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_read_hits.setStatus("mandatory")
_PdevstatNum_write_hits_Type = UInt32
_PdevstatNum_write_hits_Object = MibScalar
pdevstatNum_write_hits = _PdevstatNum_write_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 8),
    _PdevstatNum_write_hits_Type()
)
pdevstatNum_write_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_write_hits.setStatus("mandatory")
_PdevstatNum_blocks_read_Type = UInt32
_PdevstatNum_blocks_read_Object = MibScalar
pdevstatNum_blocks_read = _PdevstatNum_blocks_read_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 13),
    _PdevstatNum_blocks_read_Type()
)
pdevstatNum_blocks_read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_blocks_read.setStatus("mandatory")
_PdevstatNum_blocks_written_Type = UInt32
_PdevstatNum_blocks_written_Object = MibScalar
pdevstatNum_blocks_written = _PdevstatNum_blocks_written_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 18),
    _PdevstatNum_blocks_written_Type()
)
pdevstatNum_blocks_written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_blocks_written.setStatus("mandatory")
_PdevstatNum_seq_read_reqs_Type = UInt32
_PdevstatNum_seq_read_reqs_Object = MibScalar
pdevstatNum_seq_read_reqs = _PdevstatNum_seq_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 19),
    _PdevstatNum_seq_read_reqs_Type()
)
pdevstatNum_seq_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_seq_read_reqs.setStatus("mandatory")
_PdevstatNum_prefetched_tracks_Type = UInt32
_PdevstatNum_prefetched_tracks_Object = MibScalar
pdevstatNum_prefetched_tracks = _PdevstatNum_prefetched_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 20),
    _PdevstatNum_prefetched_tracks_Type()
)
pdevstatNum_prefetched_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_prefetched_tracks.setStatus("mandatory")
_PdevstatNum_destaged_tracks_Type = UInt32
_PdevstatNum_destaged_tracks_Object = MibScalar
pdevstatNum_destaged_tracks = _PdevstatNum_destaged_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 21),
    _PdevstatNum_destaged_tracks_Type()
)
pdevstatNum_destaged_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_destaged_tracks.setStatus("mandatory")
_PdevstatNum_deferred_writes_Type = UInt32
_PdevstatNum_deferred_writes_Object = MibScalar
pdevstatNum_deferred_writes = _PdevstatNum_deferred_writes_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 22),
    _PdevstatNum_deferred_writes_Type()
)
pdevstatNum_deferred_writes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_deferred_writes.setStatus("mandatory")
_PdevstatNum_delayed_dfw_Type = UInt32
_PdevstatNum_delayed_dfw_Object = MibScalar
pdevstatNum_delayed_dfw = _PdevstatNum_delayed_dfw_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 23),
    _PdevstatNum_delayed_dfw_Type()
)
pdevstatNum_delayed_dfw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_delayed_dfw.setStatus("mandatory")
_PdevstatNum_wp_tracks_Type = UInt32
_PdevstatNum_wp_tracks_Object = MibScalar
pdevstatNum_wp_tracks = _PdevstatNum_wp_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 24),
    _PdevstatNum_wp_tracks_Type()
)
pdevstatNum_wp_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_wp_tracks.setStatus("mandatory")
_PdevstatNum_format_pend_tracks_Type = UInt32
_PdevstatNum_format_pend_tracks_Object = MibScalar
pdevstatNum_format_pend_tracks = _PdevstatNum_format_pend_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 25),
    _PdevstatNum_format_pend_tracks_Type()
)
pdevstatNum_format_pend_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatNum_format_pend_tracks.setStatus("mandatory")
_PdevstatDevice_max_wp_limit_Type = UInt32
_PdevstatDevice_max_wp_limit_Object = MibScalar
pdevstatDevice_max_wp_limit = _PdevstatDevice_max_wp_limit_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 3, 1, 26),
    _PdevstatDevice_max_wp_limit_Type()
)
pdevstatDevice_max_wp_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdevstatDevice_max_wp_limit.setStatus("mandatory")
_LDevStatTable_Object = MibTable
lDevStatTable = _LDevStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    lDevStatTable.setStatus("obsolete")
_LDevStatEntry_Object = MibTableRow
lDevStatEntry = _LDevStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1)
)
lDevStatEntry.setIndexNames(
    (0, "EMC-MIB", "symDgListCount"),
    (0, "EMC-MIB", "symLDevListCount"),
)
if mibBuilder.loadTexts:
    lDevStatEntry.setStatus("obsolete")
_LdevstatTime_stamp_Type = TimeTicks
_LdevstatTime_stamp_Object = MibScalar
ldevstatTime_stamp = _LdevstatTime_stamp_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 1),
    _LdevstatTime_stamp_Type()
)
ldevstatTime_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatTime_stamp.setStatus("obsolete")
_LdevstatNum_sym_timeslices_Type = UInt32
_LdevstatNum_sym_timeslices_Object = MibScalar
ldevstatNum_sym_timeslices = _LdevstatNum_sym_timeslices_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 2),
    _LdevstatNum_sym_timeslices_Type()
)
ldevstatNum_sym_timeslices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_sym_timeslices.setStatus("obsolete")
_LdevstatNum_rw_reqs_Type = UInt32
_LdevstatNum_rw_reqs_Object = MibScalar
ldevstatNum_rw_reqs = _LdevstatNum_rw_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 3),
    _LdevstatNum_rw_reqs_Type()
)
ldevstatNum_rw_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_rw_reqs.setStatus("obsolete")
_LdevstatNum_read_reqs_Type = UInt32
_LdevstatNum_read_reqs_Object = MibScalar
ldevstatNum_read_reqs = _LdevstatNum_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 4),
    _LdevstatNum_read_reqs_Type()
)
ldevstatNum_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_read_reqs.setStatus("obsolete")
_LdevstatNum_write_reqs_Type = UInt32
_LdevstatNum_write_reqs_Object = MibScalar
ldevstatNum_write_reqs = _LdevstatNum_write_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 5),
    _LdevstatNum_write_reqs_Type()
)
ldevstatNum_write_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_write_reqs.setStatus("obsolete")
_LdevstatNum_rw_hits_Type = UInt32
_LdevstatNum_rw_hits_Object = MibScalar
ldevstatNum_rw_hits = _LdevstatNum_rw_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 6),
    _LdevstatNum_rw_hits_Type()
)
ldevstatNum_rw_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_rw_hits.setStatus("obsolete")
_LdevstatNum_read_hits_Type = UInt32
_LdevstatNum_read_hits_Object = MibScalar
ldevstatNum_read_hits = _LdevstatNum_read_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 7),
    _LdevstatNum_read_hits_Type()
)
ldevstatNum_read_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_read_hits.setStatus("obsolete")
_LdevstatNum_write_hits_Type = UInt32
_LdevstatNum_write_hits_Object = MibScalar
ldevstatNum_write_hits = _LdevstatNum_write_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 8),
    _LdevstatNum_write_hits_Type()
)
ldevstatNum_write_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_write_hits.setStatus("obsolete")
_LdevstatNum_blocks_read_Type = UInt32
_LdevstatNum_blocks_read_Object = MibScalar
ldevstatNum_blocks_read = _LdevstatNum_blocks_read_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 13),
    _LdevstatNum_blocks_read_Type()
)
ldevstatNum_blocks_read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_blocks_read.setStatus("obsolete")
_LdevstatNum_blocks_written_Type = UInt32
_LdevstatNum_blocks_written_Object = MibScalar
ldevstatNum_blocks_written = _LdevstatNum_blocks_written_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 18),
    _LdevstatNum_blocks_written_Type()
)
ldevstatNum_blocks_written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_blocks_written.setStatus("obsolete")
_LdevstatNum_seq_read_reqs_Type = UInt32
_LdevstatNum_seq_read_reqs_Object = MibScalar
ldevstatNum_seq_read_reqs = _LdevstatNum_seq_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 19),
    _LdevstatNum_seq_read_reqs_Type()
)
ldevstatNum_seq_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_seq_read_reqs.setStatus("obsolete")
_LdevstatNum_prefetched_tracks_Type = UInt32
_LdevstatNum_prefetched_tracks_Object = MibScalar
ldevstatNum_prefetched_tracks = _LdevstatNum_prefetched_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 20),
    _LdevstatNum_prefetched_tracks_Type()
)
ldevstatNum_prefetched_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_prefetched_tracks.setStatus("obsolete")
_LdevstatNum_destaged_tracks_Type = UInt32
_LdevstatNum_destaged_tracks_Object = MibScalar
ldevstatNum_destaged_tracks = _LdevstatNum_destaged_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 21),
    _LdevstatNum_destaged_tracks_Type()
)
ldevstatNum_destaged_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_destaged_tracks.setStatus("obsolete")
_LdevstatNum_deferred_writes_Type = UInt32
_LdevstatNum_deferred_writes_Object = MibScalar
ldevstatNum_deferred_writes = _LdevstatNum_deferred_writes_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 22),
    _LdevstatNum_deferred_writes_Type()
)
ldevstatNum_deferred_writes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_deferred_writes.setStatus("obsolete")
_LdevstatNum_delayed_dfw_Type = UInt32
_LdevstatNum_delayed_dfw_Object = MibScalar
ldevstatNum_delayed_dfw = _LdevstatNum_delayed_dfw_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 23),
    _LdevstatNum_delayed_dfw_Type()
)
ldevstatNum_delayed_dfw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_delayed_dfw.setStatus("obsolete")
_LdevstatNum_wp_tracks_Type = UInt32
_LdevstatNum_wp_tracks_Object = MibScalar
ldevstatNum_wp_tracks = _LdevstatNum_wp_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 24),
    _LdevstatNum_wp_tracks_Type()
)
ldevstatNum_wp_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_wp_tracks.setStatus("obsolete")
_LdevstatNum_format_pend_tracks_Type = UInt32
_LdevstatNum_format_pend_tracks_Object = MibScalar
ldevstatNum_format_pend_tracks = _LdevstatNum_format_pend_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 25),
    _LdevstatNum_format_pend_tracks_Type()
)
ldevstatNum_format_pend_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatNum_format_pend_tracks.setStatus("obsolete")
_LdevstatDevice_max_wp_limit_Type = UInt32
_LdevstatDevice_max_wp_limit_Object = MibScalar
ldevstatDevice_max_wp_limit = _LdevstatDevice_max_wp_limit_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 4, 1, 26),
    _LdevstatDevice_max_wp_limit_Type()
)
ldevstatDevice_max_wp_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevstatDevice_max_wp_limit.setStatus("obsolete")
_DgStatTable_Object = MibTable
dgStatTable = _DgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5)
)
if mibBuilder.loadTexts:
    dgStatTable.setStatus("obsolete")
_DgStatEntry_Object = MibTableRow
dgStatEntry = _DgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1)
)
dgStatEntry.setIndexNames(
    (0, "EMC-MIB", "symDgListCount"),
)
if mibBuilder.loadTexts:
    dgStatEntry.setStatus("obsolete")
_DgstatTime_stamp_Type = TimeTicks
_DgstatTime_stamp_Object = MibScalar
dgstatTime_stamp = _DgstatTime_stamp_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 1),
    _DgstatTime_stamp_Type()
)
dgstatTime_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatTime_stamp.setStatus("obsolete")
_DgstatNum_sym_timeslices_Type = UInt32
_DgstatNum_sym_timeslices_Object = MibScalar
dgstatNum_sym_timeslices = _DgstatNum_sym_timeslices_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 2),
    _DgstatNum_sym_timeslices_Type()
)
dgstatNum_sym_timeslices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_sym_timeslices.setStatus("obsolete")
_DgstatNum_rw_reqs_Type = UInt32
_DgstatNum_rw_reqs_Object = MibScalar
dgstatNum_rw_reqs = _DgstatNum_rw_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 3),
    _DgstatNum_rw_reqs_Type()
)
dgstatNum_rw_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_rw_reqs.setStatus("obsolete")
_DgstatNum_read_reqs_Type = UInt32
_DgstatNum_read_reqs_Object = MibScalar
dgstatNum_read_reqs = _DgstatNum_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 4),
    _DgstatNum_read_reqs_Type()
)
dgstatNum_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_read_reqs.setStatus("obsolete")
_DgstatNum_write_reqs_Type = UInt32
_DgstatNum_write_reqs_Object = MibScalar
dgstatNum_write_reqs = _DgstatNum_write_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 5),
    _DgstatNum_write_reqs_Type()
)
dgstatNum_write_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_write_reqs.setStatus("obsolete")
_DgstatNum_rw_hits_Type = UInt32
_DgstatNum_rw_hits_Object = MibScalar
dgstatNum_rw_hits = _DgstatNum_rw_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 6),
    _DgstatNum_rw_hits_Type()
)
dgstatNum_rw_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_rw_hits.setStatus("obsolete")
_DgstatNum_read_hits_Type = UInt32
_DgstatNum_read_hits_Object = MibScalar
dgstatNum_read_hits = _DgstatNum_read_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 7),
    _DgstatNum_read_hits_Type()
)
dgstatNum_read_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_read_hits.setStatus("obsolete")
_DgstatNum_write_hits_Type = UInt32
_DgstatNum_write_hits_Object = MibScalar
dgstatNum_write_hits = _DgstatNum_write_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 8),
    _DgstatNum_write_hits_Type()
)
dgstatNum_write_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_write_hits.setStatus("obsolete")
_DgstatNum_blocks_read_Type = UInt32
_DgstatNum_blocks_read_Object = MibScalar
dgstatNum_blocks_read = _DgstatNum_blocks_read_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 13),
    _DgstatNum_blocks_read_Type()
)
dgstatNum_blocks_read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_blocks_read.setStatus("obsolete")
_DgstatNum_blocks_written_Type = UInt32
_DgstatNum_blocks_written_Object = MibScalar
dgstatNum_blocks_written = _DgstatNum_blocks_written_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 18),
    _DgstatNum_blocks_written_Type()
)
dgstatNum_blocks_written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_blocks_written.setStatus("obsolete")
_DgstatNum_seq_read_reqs_Type = UInt32
_DgstatNum_seq_read_reqs_Object = MibScalar
dgstatNum_seq_read_reqs = _DgstatNum_seq_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 19),
    _DgstatNum_seq_read_reqs_Type()
)
dgstatNum_seq_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_seq_read_reqs.setStatus("obsolete")
_DgstatNum_prefetched_tracks_Type = UInt32
_DgstatNum_prefetched_tracks_Object = MibScalar
dgstatNum_prefetched_tracks = _DgstatNum_prefetched_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 20),
    _DgstatNum_prefetched_tracks_Type()
)
dgstatNum_prefetched_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_prefetched_tracks.setStatus("obsolete")
_DgstatNum_destaged_tracks_Type = UInt32
_DgstatNum_destaged_tracks_Object = MibScalar
dgstatNum_destaged_tracks = _DgstatNum_destaged_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 21),
    _DgstatNum_destaged_tracks_Type()
)
dgstatNum_destaged_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_destaged_tracks.setStatus("obsolete")
_DgstatNum_deferred_writes_Type = UInt32
_DgstatNum_deferred_writes_Object = MibScalar
dgstatNum_deferred_writes = _DgstatNum_deferred_writes_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 22),
    _DgstatNum_deferred_writes_Type()
)
dgstatNum_deferred_writes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_deferred_writes.setStatus("obsolete")
_DgstatNum_delayed_dfw_Type = UInt32
_DgstatNum_delayed_dfw_Object = MibScalar
dgstatNum_delayed_dfw = _DgstatNum_delayed_dfw_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 23),
    _DgstatNum_delayed_dfw_Type()
)
dgstatNum_delayed_dfw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_delayed_dfw.setStatus("obsolete")
_DgstatNum_wp_tracks_Type = UInt32
_DgstatNum_wp_tracks_Object = MibScalar
dgstatNum_wp_tracks = _DgstatNum_wp_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 24),
    _DgstatNum_wp_tracks_Type()
)
dgstatNum_wp_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_wp_tracks.setStatus("obsolete")
_DgstatNum_format_pend_tracks_Type = UInt32
_DgstatNum_format_pend_tracks_Object = MibScalar
dgstatNum_format_pend_tracks = _DgstatNum_format_pend_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 25),
    _DgstatNum_format_pend_tracks_Type()
)
dgstatNum_format_pend_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatNum_format_pend_tracks.setStatus("obsolete")
_Dgstatdevice_max_wp_limit_Type = UInt32
_Dgstatdevice_max_wp_limit_Object = MibScalar
dgstatdevice_max_wp_limit = _Dgstatdevice_max_wp_limit_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 5, 1, 26),
    _Dgstatdevice_max_wp_limit_Type()
)
dgstatdevice_max_wp_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgstatdevice_max_wp_limit.setStatus("obsolete")
_DirectorStatTable_Object = MibTable
directorStatTable = _DirectorStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6)
)
if mibBuilder.loadTexts:
    directorStatTable.setStatus("mandatory")
_DirectorStatEntry_Object = MibTableRow
directorStatEntry = _DirectorStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1)
)
directorStatEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symShowDirectorCount"),
)
if mibBuilder.loadTexts:
    directorStatEntry.setStatus("mandatory")
_DirstatTime_stamp_Type = TimeTicks
_DirstatTime_stamp_Object = MibScalar
dirstatTime_stamp = _DirstatTime_stamp_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1, 1),
    _DirstatTime_stamp_Type()
)
dirstatTime_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatTime_stamp.setStatus("mandatory")
_DirstatNum_sym_timeslices_Type = UInt32
_DirstatNum_sym_timeslices_Object = MibScalar
dirstatNum_sym_timeslices = _DirstatNum_sym_timeslices_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1, 2),
    _DirstatNum_sym_timeslices_Type()
)
dirstatNum_sym_timeslices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatNum_sym_timeslices.setStatus("mandatory")
_DirstatNum_rw_reqs_Type = UInt32
_DirstatNum_rw_reqs_Object = MibScalar
dirstatNum_rw_reqs = _DirstatNum_rw_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1, 3),
    _DirstatNum_rw_reqs_Type()
)
dirstatNum_rw_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatNum_rw_reqs.setStatus("mandatory")
_DirstatNum_read_reqs_Type = UInt32
_DirstatNum_read_reqs_Object = MibScalar
dirstatNum_read_reqs = _DirstatNum_read_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1, 4),
    _DirstatNum_read_reqs_Type()
)
dirstatNum_read_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatNum_read_reqs.setStatus("mandatory")
_DirstatNum_write_reqs_Type = UInt32
_DirstatNum_write_reqs_Object = MibScalar
dirstatNum_write_reqs = _DirstatNum_write_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1, 5),
    _DirstatNum_write_reqs_Type()
)
dirstatNum_write_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatNum_write_reqs.setStatus("mandatory")
_DirstatNum_rw_hits_Type = UInt32
_DirstatNum_rw_hits_Object = MibScalar
dirstatNum_rw_hits = _DirstatNum_rw_hits_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1, 6),
    _DirstatNum_rw_hits_Type()
)
dirstatNum_rw_hits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatNum_rw_hits.setStatus("mandatory")
_DirstatNum_permacache_reqs_Type = UInt32
_DirstatNum_permacache_reqs_Object = MibScalar
dirstatNum_permacache_reqs = _DirstatNum_permacache_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1, 7),
    _DirstatNum_permacache_reqs_Type()
)
dirstatNum_permacache_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatNum_permacache_reqs.setStatus("mandatory")
_DirstatNum_ios_Type = UInt32
_DirstatNum_ios_Object = MibScalar
dirstatNum_ios = _DirstatNum_ios_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 6, 1, 8),
    _DirstatNum_ios_Type()
)
dirstatNum_ios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatNum_ios.setStatus("mandatory")
_SaDirStatTable_Object = MibTable
saDirStatTable = _SaDirStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 7)
)
if mibBuilder.loadTexts:
    saDirStatTable.setStatus("mandatory")
_SaDirStatEntry_Object = MibTableRow
saDirStatEntry = _SaDirStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 7, 1)
)
saDirStatEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symShowDirectorCount"),
)
if mibBuilder.loadTexts:
    saDirStatEntry.setStatus("mandatory")
_DirstatSANum_read_misses_Type = UInt32
_DirstatSANum_read_misses_Object = MibScalar
dirstatSANum_read_misses = _DirstatSANum_read_misses_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 7, 1, 1),
    _DirstatSANum_read_misses_Type()
)
dirstatSANum_read_misses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatSANum_read_misses.setStatus("mandatory")
_DirstatSANum_slot_collisions_Type = UInt32
_DirstatSANum_slot_collisions_Object = MibScalar
dirstatSANum_slot_collisions = _DirstatSANum_slot_collisions_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 7, 1, 2),
    _DirstatSANum_slot_collisions_Type()
)
dirstatSANum_slot_collisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatSANum_slot_collisions.setStatus("mandatory")
_DirstatSANum_system_wp_disconnects_Type = UInt32
_DirstatSANum_system_wp_disconnects_Object = MibScalar
dirstatSANum_system_wp_disconnects = _DirstatSANum_system_wp_disconnects_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 7, 1, 3),
    _DirstatSANum_system_wp_disconnects_Type()
)
dirstatSANum_system_wp_disconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatSANum_system_wp_disconnects.setStatus("mandatory")
_DirstatSANum_device_wp_disconnects_Type = UInt32
_DirstatSANum_device_wp_disconnects_Object = MibScalar
dirstatSANum_device_wp_disconnects = _DirstatSANum_device_wp_disconnects_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 7, 1, 4),
    _DirstatSANum_device_wp_disconnects_Type()
)
dirstatSANum_device_wp_disconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatSANum_device_wp_disconnects.setStatus("mandatory")
_DaDirStatTable_Object = MibTable
daDirStatTable = _DaDirStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8)
)
if mibBuilder.loadTexts:
    daDirStatTable.setStatus("mandatory")
_DaDirStatEntry_Object = MibTableRow
daDirStatEntry = _DaDirStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8, 1)
)
daDirStatEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symShowDirectorCount"),
)
if mibBuilder.loadTexts:
    daDirStatEntry.setStatus("mandatory")
_DirstatDANum_pf_tracks_Type = UInt32
_DirstatDANum_pf_tracks_Object = MibScalar
dirstatDANum_pf_tracks = _DirstatDANum_pf_tracks_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8, 1, 1),
    _DirstatDANum_pf_tracks_Type()
)
dirstatDANum_pf_tracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatDANum_pf_tracks.setStatus("mandatory")
_DirstatDANum_pf_tracks_used_Type = UInt32
_DirstatDANum_pf_tracks_used_Object = MibScalar
dirstatDANum_pf_tracks_used = _DirstatDANum_pf_tracks_used_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8, 1, 2),
    _DirstatDANum_pf_tracks_used_Type()
)
dirstatDANum_pf_tracks_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatDANum_pf_tracks_used.setStatus("mandatory")
_DirstatDANum_pf_tracks_unused_Type = UInt32
_DirstatDANum_pf_tracks_unused_Object = MibScalar
dirstatDANum_pf_tracks_unused = _DirstatDANum_pf_tracks_unused_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8, 1, 3),
    _DirstatDANum_pf_tracks_unused_Type()
)
dirstatDANum_pf_tracks_unused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatDANum_pf_tracks_unused.setStatus("mandatory")
_DirstatDANum_pf_short_misses_Type = UInt32
_DirstatDANum_pf_short_misses_Object = MibScalar
dirstatDANum_pf_short_misses = _DirstatDANum_pf_short_misses_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8, 1, 4),
    _DirstatDANum_pf_short_misses_Type()
)
dirstatDANum_pf_short_misses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatDANum_pf_short_misses.setStatus("mandatory")
_DirstatDANum_pf_long_misses_Type = UInt32
_DirstatDANum_pf_long_misses_Object = MibScalar
dirstatDANum_pf_long_misses = _DirstatDANum_pf_long_misses_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8, 1, 5),
    _DirstatDANum_pf_long_misses_Type()
)
dirstatDANum_pf_long_misses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatDANum_pf_long_misses.setStatus("mandatory")
_DirstatDANum_pf_restarts_Type = UInt32
_DirstatDANum_pf_restarts_Object = MibScalar
dirstatDANum_pf_restarts = _DirstatDANum_pf_restarts_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8, 1, 6),
    _DirstatDANum_pf_restarts_Type()
)
dirstatDANum_pf_restarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatDANum_pf_restarts.setStatus("mandatory")
_DirstatDANum_pf_mismatches_Type = UInt32
_DirstatDANum_pf_mismatches_Object = MibScalar
dirstatDANum_pf_mismatches = _DirstatDANum_pf_mismatches_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 8, 1, 7),
    _DirstatDANum_pf_mismatches_Type()
)
dirstatDANum_pf_mismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatDANum_pf_mismatches.setStatus("mandatory")
_RaDirStatTable_Object = MibTable
raDirStatTable = _RaDirStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 9)
)
if mibBuilder.loadTexts:
    raDirStatTable.setStatus("mandatory")
_RaDirStatEntry_Object = MibTableRow
raDirStatEntry = _RaDirStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 9, 1)
)
raDirStatEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symShowDirectorCount"),
)
if mibBuilder.loadTexts:
    raDirStatEntry.setStatus("mandatory")
_DirstatRANum_read_misses_Type = UInt32
_DirstatRANum_read_misses_Object = MibScalar
dirstatRANum_read_misses = _DirstatRANum_read_misses_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 9, 1, 1),
    _DirstatRANum_read_misses_Type()
)
dirstatRANum_read_misses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatRANum_read_misses.setStatus("mandatory")
_DirstatRANum_slot_collisions_Type = UInt32
_DirstatRANum_slot_collisions_Object = MibScalar
dirstatRANum_slot_collisions = _DirstatRANum_slot_collisions_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 9, 1, 2),
    _DirstatRANum_slot_collisions_Type()
)
dirstatRANum_slot_collisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatRANum_slot_collisions.setStatus("mandatory")
_DirstatRANum_system_wp_disconnects_Type = UInt32
_DirstatRANum_system_wp_disconnects_Object = MibScalar
dirstatRANum_system_wp_disconnects = _DirstatRANum_system_wp_disconnects_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 9, 1, 3),
    _DirstatRANum_system_wp_disconnects_Type()
)
dirstatRANum_system_wp_disconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatRANum_system_wp_disconnects.setStatus("mandatory")
_DirstatRANum_device_wp_disconnects_Type = UInt32
_DirstatRANum_device_wp_disconnects_Object = MibScalar
dirstatRANum_device_wp_disconnects = _DirstatRANum_device_wp_disconnects_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 9, 1, 4),
    _DirstatRANum_device_wp_disconnects_Type()
)
dirstatRANum_device_wp_disconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirstatRANum_device_wp_disconnects.setStatus("mandatory")
_DirPortStatistics_ObjectIdentity = ObjectIdentity
dirPortStatistics = _DirPortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10)
)
_DirStatPortCountTable_Object = MibTable
dirStatPortCountTable = _DirStatPortCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 1)
)
if mibBuilder.loadTexts:
    dirStatPortCountTable.setStatus("mandatory")
_DirStatPortCountEntry_Object = MibTableRow
dirStatPortCountEntry = _DirStatPortCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 1, 1)
)
dirStatPortCountEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symShowDirectorCount"),
)
if mibBuilder.loadTexts:
    dirStatPortCountEntry.setStatus("mandatory")
_DirPortStatPortCount_Type = Integer32
_DirPortStatPortCount_Object = MibTableColumn
dirPortStatPortCount = _DirPortStatPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 1, 1, 1),
    _DirPortStatPortCount_Type()
)
dirPortStatPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirPortStatPortCount.setStatus("mandatory")
_DirPortStatTable_Object = MibTable
dirPortStatTable = _DirPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 2)
)
if mibBuilder.loadTexts:
    dirPortStatTable.setStatus("mandatory")
_DirPortStatEntry_Object = MibTableRow
dirPortStatEntry = _DirPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 2, 1)
)
dirPortStatEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symShowDirectorCount"),
    (0, "EMC-MIB", "dirPortStatPortCount"),
)
if mibBuilder.loadTexts:
    dirPortStatEntry.setStatus("mandatory")
_PortstatTime_stamp_Type = TimeTicks
_PortstatTime_stamp_Object = MibScalar
portstatTime_stamp = _PortstatTime_stamp_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 2, 1, 1),
    _PortstatTime_stamp_Type()
)
portstatTime_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portstatTime_stamp.setStatus("mandatory")
_PortstatNum_sym_timeslices_Type = UInt32
_PortstatNum_sym_timeslices_Object = MibScalar
portstatNum_sym_timeslices = _PortstatNum_sym_timeslices_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 2, 1, 2),
    _PortstatNum_sym_timeslices_Type()
)
portstatNum_sym_timeslices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portstatNum_sym_timeslices.setStatus("mandatory")
_PortstatNum_rw_reqs_Type = UInt32
_PortstatNum_rw_reqs_Object = MibScalar
portstatNum_rw_reqs = _PortstatNum_rw_reqs_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 2, 1, 3),
    _PortstatNum_rw_reqs_Type()
)
portstatNum_rw_reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portstatNum_rw_reqs.setStatus("mandatory")
_PortstatNum_blocks_read_and_written_Type = UInt32
_PortstatNum_blocks_read_and_written_Object = MibScalar
portstatNum_blocks_read_and_written = _PortstatNum_blocks_read_and_written_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 6, 3, 10, 2, 1, 4),
    _PortstatNum_blocks_read_and_written_Type()
)
portstatNum_blocks_read_and_written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portstatNum_blocks_read_and_written.setStatus("mandatory")
_SymmEvent_ObjectIdentity = ObjectIdentity
symmEvent = _SymmEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 1, 7)
)
_SymmEventMaxEvents_Type = Integer32
_SymmEventMaxEvents_Object = MibScalar
symmEventMaxEvents = _SymmEventMaxEvents_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 7, 1),
    _SymmEventMaxEvents_Type()
)
symmEventMaxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symmEventMaxEvents.setStatus("mandatory")
_SymmEventTable_Object = MibTable
symmEventTable = _SymmEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 7, 2)
)
if mibBuilder.loadTexts:
    symmEventTable.setStatus("mandatory")
_SymmEventEntry_Object = MibTableRow
symmEventEntry = _SymmEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 7, 2, 1)
)
symmEventEntry.setIndexNames(
    (0, "EMC-MIB", "discIndex"),
    (0, "EMC-MIB", "symmEventIndex"),
)
if mibBuilder.loadTexts:
    symmEventEntry.setStatus("mandatory")


class _SymmEventIndex_Type(Integer32):
    """Custom type symmEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SymmEventIndex_Type.__name__ = "Integer32"
_SymmEventIndex_Object = MibTableColumn
symmEventIndex = _SymmEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 7, 2, 1, 1),
    _SymmEventIndex_Type()
)
symmEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symmEventIndex.setStatus("mandatory")
_SymmEventTime_Type = DisplayString
_SymmEventTime_Object = MibTableColumn
symmEventTime = _SymmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 7, 2, 1, 2),
    _SymmEventTime_Type()
)
symmEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symmEventTime.setStatus("mandatory")


class _SymmEventSeverity_Type(Integer32):
    """Custom type symmEventSeverity based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("alert", 3),
          ("critical", 4),
          ("debug", 9),
          ("emergency", 2),
          ("error", 5),
          ("info", 8),
          ("mark", 10),
          ("notify", 7),
          ("unknown", 1),
          ("warning", 6))
    )


_SymmEventSeverity_Type.__name__ = "Integer32"
_SymmEventSeverity_Object = MibTableColumn
symmEventSeverity = _SymmEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 7, 2, 1, 3),
    _SymmEventSeverity_Type()
)
symmEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symmEventSeverity.setStatus("mandatory")
_SymmEventDescr_Type = DisplayString
_SymmEventDescr_Object = MibTableColumn
symmEventDescr = _SymmEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 1139, 1, 7, 2, 1, 4),
    _SymmEventDescr_Type()
)
symmEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symmEventDescr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

emcDeviceStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 1, 0, 1)
)
emcDeviceStatusTrap.setObjects(
    ("EMC-MIB", "symmEventDescr")
)
if mibBuilder.loadTexts:
    emcDeviceStatusTrap.setStatus(
        ""
    )

emcSymmetrixStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 1, 0, 2)
)
emcSymmetrixStatusTrap.setObjects(
    ("EMC-MIB", "symmEventDescr")
)
if mibBuilder.loadTexts:
    emcSymmetrixStatusTrap.setStatus(
        ""
    )

emcRatiosOutofRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 1, 0, 3)
)
emcRatiosOutofRangeTrap.setObjects(
    ("EMC-MIB", "symmEventDescr")
)
if mibBuilder.loadTexts:
    emcRatiosOutofRangeTrap.setStatus(
        ""
    )

discoveryTableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 1, 0, 4)
)
discoveryTableChange.setObjects(
    ("EMC-MIB", "discoveryChangeTime")
)
if mibBuilder.loadTexts:
    discoveryTableChange.setStatus(
        ""
    )

emcSymmetrixEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 1, 0, 5)
)
emcSymmetrixEventTrap.setObjects(
    ("EMC-MIB", "symmEventDescr")
)
if mibBuilder.loadTexts:
    emcSymmetrixEventTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMC-MIB",
    **{"UInt32": UInt32,
       "StateValues": StateValues,
       "DirectorType": DirectorType,
       "DirectorStatus": DirectorStatus,
       "PortStatus": PortStatus,
       "SCSIWidth": SCSIWidth,
       "DeviceStatus": DeviceStatus,
       "DeviceType": DeviceType,
       "DeviceEmulation": DeviceEmulation,
       "SCSIMethod": SCSIMethod,
       "BCVState": BCVState,
       "RDFPairState": RDFPairState,
       "RDFType": RDFType,
       "RDFMode": RDFMode,
       "RDFAdaptiveCopy": RDFAdaptiveCopy,
       "RDFLinkConfig": RDFLinkConfig,
       "RDDFTransientState": RDDFTransientState,
       "emc": emc,
       "emcSymmetrix": emcSymmetrix,
       "emcDeviceStatusTrap": emcDeviceStatusTrap,
       "emcSymmetrixStatusTrap": emcSymmetrixStatusTrap,
       "emcRatiosOutofRangeTrap": emcRatiosOutofRangeTrap,
       "discoveryTableChange": discoveryTableChange,
       "emcSymmetrixEventTrap": emcSymmetrixEventTrap,
       "emcControlCenter": emcControlCenter,
       "esmVariables": esmVariables,
       "emcSymCnfg": emcSymCnfg,
       "emcSymDiskCfg": emcSymDiskCfg,
       "emcSymMirrorDiskCfg": emcSymMirrorDiskCfg,
       "emcSymMirror3DiskCfg": emcSymMirror3DiskCfg,
       "emcSymMirror4DiskCfg": emcSymMirror4DiskCfg,
       "emcSymStatistics": emcSymStatistics,
       "emcSymUtilA7": emcSymUtilA7,
       "emcSymRdfMaint": emcSymRdfMaint,
       "emcSymWinConfig": emcSymWinConfig,
       "emcSymUtil99": emcSymUtil99,
       "emcSymDir": emcSymDir,
       "emcSymDevStats": emcSymDevStats,
       "emcSymSumStatus": emcSymSumStatus,
       "emcRatiosOutofRange": emcRatiosOutofRange,
       "emcSymPortStats": emcSymPortStats,
       "emcSymBCVDevice": emcSymBCVDevice,
       "emcSymSaitInfo": emcSymSaitInfo,
       "emcSymTimefinderInfo": emcSymTimefinderInfo,
       "emcSymSRDFInfo": emcSymSRDFInfo,
       "emcSymPhysDevStats": emcSymPhysDevStats,
       "emcSymSumStatusErrorCodes": emcSymSumStatusErrorCodes,
       "systemCalls": systemCalls,
       "informational": informational,
       "systemInformation": systemInformation,
       "systemInfoHeaderTable": systemInfoHeaderTable,
       "systemInfoHeaderEntry": systemInfoHeaderEntry,
       "sysinfoBuffer": sysinfoBuffer,
       "sysinfoNumberofRecords": sysinfoNumberofRecords,
       "sysinfoRecordSize": sysinfoRecordSize,
       "sysinfoFirstRecordNumber": sysinfoFirstRecordNumber,
       "sysinfoMaxRecords": sysinfoMaxRecords,
       "sysinfoRecordsTable": sysinfoRecordsTable,
       "sysinfoRecordsEntry": sysinfoRecordsEntry,
       "sysinfoSerialNumber": sysinfoSerialNumber,
       "sysinfoNumberofDirectors": sysinfoNumberofDirectors,
       "sysinfoNumberofVolumes": sysinfoNumberofVolumes,
       "sysinfoMemorySize": sysinfoMemorySize,
       "systemCodes": systemCodes,
       "systemCodesTable": systemCodesTable,
       "systemCodesEntry": systemCodesEntry,
       "syscodesBuffer": syscodesBuffer,
       "syscodesNumberofRecords": syscodesNumberofRecords,
       "syscodesRecordSize": syscodesRecordSize,
       "syscodesFirstRecordNumber": syscodesFirstRecordNumber,
       "syscodesMaxRecords": syscodesMaxRecords,
       "systemCodesRecordsTable": systemCodesRecordsTable,
       "systemCodesRecordsEntry": systemCodesRecordsEntry,
       "syscodesDirectorType": syscodesDirectorType,
       "syscodesDirectorNum": syscodesDirectorNum,
       "emulCodeType": emulCodeType,
       "emulVersion": emulVersion,
       "emulDate": emulDate,
       "emulChecksum": emulChecksum,
       "emulMTPF": emulMTPF,
       "emulFileCount": emulFileCount,
       "implCodeType": implCodeType,
       "implVersion": implVersion,
       "implDate": implDate,
       "implChecksum": implChecksum,
       "implMTPF": implMTPF,
       "implFileCount": implFileCount,
       "initCodeType": initCodeType,
       "initVersion": initVersion,
       "initDate": initDate,
       "initChecksum": initChecksum,
       "initMTPF": initMTPF,
       "initFileCount": initFileCount,
       "escnCodeType": escnCodeType,
       "escnVersion": escnVersion,
       "escnDate": escnDate,
       "escnChecksum": escnChecksum,
       "escnMTPF": escnMTPF,
       "escnFileCount": escnFileCount,
       "diskAdapterDeviceConfiguration": diskAdapterDeviceConfiguration,
       "diskAdapterDeviceConfigurationTable": diskAdapterDeviceConfigurationTable,
       "diskAdapterDeviceConfigurationEntry": diskAdapterDeviceConfigurationEntry,
       "dadcnfigBuffer": dadcnfigBuffer,
       "dadcnfigNumberofRecords": dadcnfigNumberofRecords,
       "dadcnfigRecordSize": dadcnfigRecordSize,
       "dadcnfigFirstRecordNumber": dadcnfigFirstRecordNumber,
       "dadcnfigMaxRecords": dadcnfigMaxRecords,
       "dadcnfigDeviceRecordsTable": dadcnfigDeviceRecordsTable,
       "dadcnfigDeviceRecordsEntry": dadcnfigDeviceRecordsEntry,
       "dadcnfigSymmNumber": dadcnfigSymmNumber,
       "dadcnfigMirrors": dadcnfigMirrors,
       "dadcnfigMirror1Director": dadcnfigMirror1Director,
       "dadcnfigMirror1Interface": dadcnfigMirror1Interface,
       "dadcnfigMirror2Director": dadcnfigMirror2Director,
       "dadcnfigMirror2Interface": dadcnfigMirror2Interface,
       "dadcnfigMirror3Director": dadcnfigMirror3Director,
       "dadcnfigMirror3Interface": dadcnfigMirror3Interface,
       "dadcnfigMirror4Director": dadcnfigMirror4Director,
       "dadcnfigMirror4Interface": dadcnfigMirror4Interface,
       "deviceHostAddressConfiguration": deviceHostAddressConfiguration,
       "deviceHostAddressConfigurationTable": deviceHostAddressConfigurationTable,
       "deviceHostAddressConfigurationEntry": deviceHostAddressConfigurationEntry,
       "dvhoaddrBuffer": dvhoaddrBuffer,
       "dvhoaddrNumberofRecords": dvhoaddrNumberofRecords,
       "dvhoaddrRecordSize": dvhoaddrRecordSize,
       "dvhoaddrFirstRecordNumber": dvhoaddrFirstRecordNumber,
       "dvhoaddrMaxRecords": dvhoaddrMaxRecords,
       "dvhoaddrDeviceRecordsTable": dvhoaddrDeviceRecordsTable,
       "dvhoaddrDeviceRecordsEntry": dvhoaddrDeviceRecordsEntry,
       "dvhoaddrSymmNumber": dvhoaddrSymmNumber,
       "dvhoaddrDirectorNumber": dvhoaddrDirectorNumber,
       "dvhoaddrPortAType": dvhoaddrPortAType,
       "dvhoaddrPortADeviceAddress": dvhoaddrPortADeviceAddress,
       "dvhoaddrPortBType": dvhoaddrPortBType,
       "dvhoaddrPortBDeviceAddress": dvhoaddrPortBDeviceAddress,
       "dvhoaddrPortCType": dvhoaddrPortCType,
       "dvhoaddrPortCDeviceAddress": dvhoaddrPortCDeviceAddress,
       "dvhoaddrPortDType": dvhoaddrPortDType,
       "dvhoaddrPortDDeviceAddress": dvhoaddrPortDDeviceAddress,
       "dvhoaddrMetaFlags": dvhoaddrMetaFlags,
       "dvhoaddrFiberChannelAddress": dvhoaddrFiberChannelAddress,
       "control": control,
       "discovery": discovery,
       "discoveryTableSize": discoveryTableSize,
       "discoveryTable": discoveryTable,
       "discoveryTbl": discoveryTbl,
       "discIndex": discIndex,
       "discSerialNumber": discSerialNumber,
       "discRawDevice": discRawDevice,
       "discModel": discModel,
       "discCapacity": discCapacity,
       "discChecksum": discChecksum,
       "discConfigDate": discConfigDate,
       "discRDF": discRDF,
       "discBCV": discBCV,
       "discState": discState,
       "discStatus": discStatus,
       "discMicrocodeVersion": discMicrocodeVersion,
       "discSymapisrv-IP": discSymapisrv_IP,
       "discNumEvents": discNumEvents,
       "discEventCurrID": discEventCurrID,
       "agentAdministration": agentAdministration,
       "agentRevision": agentRevision,
       "mibRevision": mibRevision,
       "agentType": agentType,
       "periodicDiscoveryFrequency": periodicDiscoveryFrequency,
       "checksumTestFrequency": checksumTestFrequency,
       "statusCheckFrequency": statusCheckFrequency,
       "discoveryChangeTime": discoveryChangeTime,
       "analyzer": analyzer,
       "analyzerTopFileSavePolicy": analyzerTopFileSavePolicy,
       "analyzerSpecialDurationLimit": analyzerSpecialDurationLimit,
       "analyzerFiles": analyzerFiles,
       "analyzerFilesCountTable": analyzerFilesCountTable,
       "analyzerFileCountEntry": analyzerFileCountEntry,
       "analyzerFileCount": analyzerFileCount,
       "analyzerFilesListTable": analyzerFilesListTable,
       "analyzerFilesListEntry": analyzerFilesListEntry,
       "analyzerFileName": analyzerFileName,
       "analyzerFileSize": analyzerFileSize,
       "analyzerFileCreation": analyzerFileCreation,
       "analyzerFileLastModified": analyzerFileLastModified,
       "analyzerFileIsActive": analyzerFileIsActive,
       "analyzerFileRuntime": analyzerFileRuntime,
       "clients": clients,
       "clientListMaintenanceFrequency": clientListMaintenanceFrequency,
       "clientListRequestExpiration": clientListRequestExpiration,
       "clientListClientExpiration": clientListClientExpiration,
       "trapSetup": trapSetup,
       "discoveryTrapPort": discoveryTrapPort,
       "trapTestFrequency": trapTestFrequency,
       "activePorts": activePorts,
       "standardSNMPRequestPort": standardSNMPRequestPort,
       "esmSNMPRequestPort": esmSNMPRequestPort,
       "celerraTCPPort": celerraTCPPort,
       "xdrTCPPort": xdrTCPPort,
       "agentConfiguration": agentConfiguration,
       "esmVariablePacketSize": esmVariablePacketSize,
       "discoveryFrequency": discoveryFrequency,
       "masterTraceMessagesEnable": masterTraceMessagesEnable,
       "subagentConfiguration": subagentConfiguration,
       "subagentInformation": subagentInformation,
       "subagentInfo": subagentInfo,
       "subagentSymmetrixSerialNumber": subagentSymmetrixSerialNumber,
       "subagentProcessActive": subagentProcessActive,
       "subagentTraceMessagesEnable": subagentTraceMessagesEnable,
       "mainframeVariables": mainframeVariables,
       "mainframeDiskInformation": mainframeDiskInformation,
       "mfDiskInformation": mfDiskInformation,
       "emcSymMvsVolume": emcSymMvsVolume,
       "mainframeDataSetInformation": mainframeDataSetInformation,
       "mfDataSetInformation": mfDataSetInformation,
       "emcSymMvsLUNNumber": emcSymMvsLUNNumber,
       "emcSymMvsDsname": emcSymMvsDsname,
       "emcSymMvsBuildStatus": emcSymMvsBuildStatus,
       "symAPI": symAPI,
       "symAPIList": symAPIList,
       "symList": symList,
       "symListCount": symListCount,
       "symListTable": symListTable,
       "symListEntry": symListEntry,
       "serialNumber": serialNumber,
       "symRemoteList": symRemoteList,
       "symRemoteListCount": symRemoteListCount,
       "symRemoteListTable": symRemoteListTable,
       "symRemoteListEntry": symRemoteListEntry,
       "remoteSerialNumber": remoteSerialNumber,
       "symDevList": symDevList,
       "symDevListCountTable": symDevListCountTable,
       "symDevListCountEntry": symDevListCountEntry,
       "symDevListCount": symDevListCount,
       "symDevListTable": symDevListTable,
       "symDevListEntry": symDevListEntry,
       "symDeviceName": symDeviceName,
       "symPDevList": symPDevList,
       "symPDevListCountTable": symPDevListCountTable,
       "symPDevListCountEntry": symPDevListCountEntry,
       "symPDevListCount": symPDevListCount,
       "symPDevListTable": symPDevListTable,
       "symPDevListEntry": symPDevListEntry,
       "symPDeviceName": symPDeviceName,
       "symPDevNoDgList": symPDevNoDgList,
       "symPDevNoDgListCountTable": symPDevNoDgListCountTable,
       "symPDevNoDgListCountEntry": symPDevNoDgListCountEntry,
       "symPDevNoDgListCount": symPDevNoDgListCount,
       "symPDevNoDgListTable": symPDevNoDgListTable,
       "symPDevNoDgListEntry": symPDevNoDgListEntry,
       "symPDevNoDgDeviceName": symPDevNoDgDeviceName,
       "symDevNoDgList": symDevNoDgList,
       "symDevNoDgListCountTable": symDevNoDgListCountTable,
       "symDevNoDgListCountEntry": symDevNoDgListCountEntry,
       "symDevNoDgListCount": symDevNoDgListCount,
       "symDevNoDgListTable": symDevNoDgListTable,
       "symDevNoDgListEntry": symDevNoDgListEntry,
       "symDevNoDgDeviceName": symDevNoDgDeviceName,
       "symDgList": symDgList,
       "symDgListCount": symDgListCount,
       "symDgListTable": symDgListTable,
       "symDgListEntry": symDgListEntry,
       "symDevGroupName": symDevGroupName,
       "symLDevList": symLDevList,
       "symLDevListCountTable": symLDevListCountTable,
       "symLDevListCountEntry": symLDevListCountEntry,
       "symLDevListCount": symLDevListCount,
       "symLDevListTable": symLDevListTable,
       "symLDevListEntry": symLDevListEntry,
       "lDeviceName": lDeviceName,
       "symGateList": symGateList,
       "symGateListCountTable": symGateListCountTable,
       "symGateListCountEntry": symGateListCountEntry,
       "symGateListCount": symGateListCount,
       "symGateListTable": symGateListTable,
       "symGateListEntry": symGateListEntry,
       "gatekeeperDeviceName": gatekeeperDeviceName,
       "symBcvDevList": symBcvDevList,
       "symBcvDevListCountTable": symBcvDevListCountTable,
       "symBcvDevListCountEntry": symBcvDevListCountEntry,
       "symBcvDevListCount": symBcvDevListCount,
       "symBcvDevListTable": symBcvDevListTable,
       "symBcvDevListEntry": symBcvDevListEntry,
       "bcvDeviceName": bcvDeviceName,
       "symBcvPDevList": symBcvPDevList,
       "symBcvPDevListCountTable": symBcvPDevListCountTable,
       "symBcvPDevListCountEntry": symBcvPDevListCountEntry,
       "symBcvPDevListCount": symBcvPDevListCount,
       "symBcvPDevListTable": symBcvPDevListTable,
       "symBcvPDevListEntry": symBcvPDevListEntry,
       "symBcvPDeviceName": symBcvPDeviceName,
       "symAPIShow": symAPIShow,
       "symShow": symShow,
       "symShowConfiguration": symShowConfiguration,
       "symShowEntry": symShowEntry,
       "symShowSymid": symShowSymid,
       "symShowSymmetrix-ident": symShowSymmetrix_ident,
       "symShowSymmetrix-model": symShowSymmetrix_model,
       "symShowMicrocode-version": symShowMicrocode_version,
       "symShowMicrocode-version-num": symShowMicrocode_version_num,
       "symShowMicrocode-date": symShowMicrocode_date,
       "symShowMicrocode-patch-level": symShowMicrocode_patch_level,
       "symShowMicrocode-patch-date": symShowMicrocode_patch_date,
       "symShowSymmetrix-pwron-time": symShowSymmetrix_pwron_time,
       "symShowSymmetrix-uptime": symShowSymmetrix_uptime,
       "symShowDb-sync-time": symShowDb_sync_time,
       "symShowDb-sync-bcv-time": symShowDb_sync_bcv_time,
       "symShowDb-sync-rdf-time": symShowDb_sync_rdf_time,
       "symShowLast-ipl-time": symShowLast_ipl_time,
       "symShowLast-fast-ipl-time": symShowLast_fast_ipl_time,
       "symShowReserved": symShowReserved,
       "symShowCache-size": symShowCache_size,
       "symShowCache-slot-count": symShowCache_slot_count,
       "symShowMax-wr-pend-slots": symShowMax_wr_pend_slots,
       "symShowMax-da-wr-pend-slots": symShowMax_da_wr_pend_slots,
       "symShowMax-dev-wr-pend-slots": symShowMax_dev_wr_pend_slots,
       "symShowPermacache-slot-count": symShowPermacache_slot_count,
       "symShowNum-disks": symShowNum_disks,
       "symShowNum-symdevs": symShowNum_symdevs,
       "symShowNum-pdevs": symShowNum_pdevs,
       "symShowAPI-version": symShowAPI_version,
       "symShowSDDF-configuration": symShowSDDF_configuration,
       "symShowConfig-checksum": symShowConfig_checksum,
       "symShowNum-powerpath-devs": symShowNum_powerpath_devs,
       "symShowPDevCountTable": symShowPDevCountTable,
       "symShowPDevCountEntry": symShowPDevCountEntry,
       "symShowPDevCount": symShowPDevCount,
       "symShowPDevListTable": symShowPDevListTable,
       "symShowPDevListEntry": symShowPDevListEntry,
       "symShowPDeviceName": symShowPDeviceName,
       "symShowDirectorCountTable": symShowDirectorCountTable,
       "symShowDirectorCountEntry": symShowDirectorCountEntry,
       "symShowDirectorCount": symShowDirectorCount,
       "symShowDirectorConfigurationTable": symShowDirectorConfigurationTable,
       "symShowDirectorConfigurationEntry": symShowDirectorConfigurationEntry,
       "symShowDirector-type": symShowDirector_type,
       "symShowDirector-num": symShowDirector_num,
       "symShowSlot-num": symShowSlot_num,
       "symShowDirector-ident": symShowDirector_ident,
       "symShowDirector-status": symShowDirector_status,
       "symShowScsi-capability": symShowScsi_capability,
       "symShowNum-da-volumes": symShowNum_da_volumes,
       "symShowRemote-symid": symShowRemote_symid,
       "symShowRa-group-num": symShowRa_group_num,
       "symShowRemote-ra-group-num": symShowRemote_ra_group_num,
       "symShowPrevent-auto-link-recovery": symShowPrevent_auto_link_recovery,
       "symShowPrevent-ra-online-upon-pwron": symShowPrevent_ra_online_upon_pwron,
       "symShowNum-ports": symShowNum_ports,
       "symShowPort0-status": symShowPort0_status,
       "symShowPort1-status": symShowPort1_status,
       "symShowPort2-status": symShowPort2_status,
       "symShowPort3-status": symShowPort3_status,
       "symDevShow": symDevShow,
       "devShowConfigurationTable": devShowConfigurationTable,
       "devShowConfigurationEntry": devShowConfigurationEntry,
       "devShowVendor-id": devShowVendor_id,
       "devShowProduct-id": devShowProduct_id,
       "devShowProduct-rev": devShowProduct_rev,
       "devShowSymid": devShowSymid,
       "devShowDevice-serial-id": devShowDevice_serial_id,
       "devShowSym-devname": devShowSym_devname,
       "devShowPdevname": devShowPdevname,
       "devShowDgname": devShowDgname,
       "devShowLdevname": devShowLdevname,
       "devShowDev-config": devShowDev_config,
       "devShowDev-parameters": devShowDev_parameters,
       "devShowDev-status": devShowDev_status,
       "devShowDev-capacity": devShowDev_capacity,
       "devShowTid": devShowTid,
       "devShowLun": devShowLun,
       "devShowDirector-num": devShowDirector_num,
       "devShowDirector-slot-num": devShowDirector_slot_num,
       "devShowDirector-ident": devShowDirector_ident,
       "devShowDirector-port-num": devShowDirector_port_num,
       "devShowMset-M1-type": devShowMset_M1_type,
       "devShowMset-M2-type": devShowMset_M2_type,
       "devShowMset-M3-type": devShowMset_M3_type,
       "devShowMset-M4-type": devShowMset_M4_type,
       "devShowMset-M1-status": devShowMset_M1_status,
       "devShowMset-M2-status": devShowMset_M2_status,
       "devShowMset-M3-status": devShowMset_M3_status,
       "devShowMset-M4-status": devShowMset_M4_status,
       "devShowMset-M1-invalid-tracks": devShowMset_M1_invalid_tracks,
       "devShowMset-M2-invalid-tracks": devShowMset_M2_invalid_tracks,
       "devShowMset-M3-invalid-tracks": devShowMset_M3_invalid_tracks,
       "devShowMset-M4-invalid-tracks": devShowMset_M4_invalid_tracks,
       "devShowDirector-port-status": devShowDirector_port_status,
       "devShowDev-sa-status": devShowDev_sa_status,
       "devShowVbus": devShowVbus,
       "devShowEmulation": devShowEmulation,
       "devShowDev-block-size": devShowDev_block_size,
       "devShowSCSI-negotiation": devShowSCSI_negotiation,
       "devShowSCSI-method": devShowSCSI_method,
       "devShowDev-cylinders": devShowDev_cylinders,
       "devShowAttached-bcv-symdev": devShowAttached_bcv_symdev,
       "devShowRDFInfoTable": devShowRDFInfoTable,
       "devShowRDFInfoEntry": devShowRDFInfoEntry,
       "devShowRemote-symid": devShowRemote_symid,
       "devShowRemote-sym-devname": devShowRemote_sym_devname,
       "devShowRa-group-number": devShowRa_group_number,
       "devShowDev-rdf-type": devShowDev_rdf_type,
       "devShowDev-ra-status": devShowDev_ra_status,
       "devShowDev-link-status": devShowDev_link_status,
       "devShowRdf-mode": devShowRdf_mode,
       "devShowRdf-pair-state": devShowRdf_pair_state,
       "devShowRdf-domino": devShowRdf_domino,
       "devShowAdaptive-copy": devShowAdaptive_copy,
       "devShowAdaptive-copy-skew": devShowAdaptive_copy_skew,
       "devShowNum-r1-invalid-tracks": devShowNum_r1_invalid_tracks,
       "devShowNum-r2-invalid-tracks": devShowNum_r2_invalid_tracks,
       "devShowDev-rdf-state": devShowDev_rdf_state,
       "devShowRemote-dev-rdf-state": devShowRemote_dev_rdf_state,
       "devShowRdf-status": devShowRdf_status,
       "devShowLink-domino": devShowLink_domino,
       "devShowPrevent-auto-link-recovery": devShowPrevent_auto_link_recovery,
       "devShowLink-config": devShowLink_config,
       "devShowSuspend-state": devShowSuspend_state,
       "devShowConsistency-state": devShowConsistency_state,
       "devShowAdaptive-copy-wp-state": devShowAdaptive_copy_wp_state,
       "devShowPrevent-ra-online-upon-pwron": devShowPrevent_ra_online_upon_pwron,
       "devShowBCVInfoTable": devShowBCVInfoTable,
       "devShowBCVInfoEntry": devShowBCVInfoEntry,
       "devShowDev-serial-id": devShowDev_serial_id,
       "devShowDev-sym-devname": devShowDev_sym_devname,
       "devShowDev-dgname": devShowDev_dgname,
       "devShowBcvdev-serial-id": devShowBcvdev_serial_id,
       "devShowBcvdev-sym-devname": devShowBcvdev_sym_devname,
       "devShowBcvdev-dgname": devShowBcvdev_dgname,
       "devShowBcv-pair-state": devShowBcv_pair_state,
       "devShowNum-dev-invalid-tracks": devShowNum_dev_invalid_tracks,
       "devShowNum-bcvdev-invalid-tracks": devShowNum_bcvdev_invalid_tracks,
       "devShowBcvdev-status": devShowBcvdev_status,
       "symAPIStatistics": symAPIStatistics,
       "symStatTable": symStatTable,
       "symStatEntry": symStatEntry,
       "symstatTime-stamp": symstatTime_stamp,
       "symstatNum-rw-reqs": symstatNum_rw_reqs,
       "symstatNum-read-reqs": symstatNum_read_reqs,
       "symstatNum-write-reqs": symstatNum_write_reqs,
       "symstatNum-rw-hits": symstatNum_rw_hits,
       "symstatNum-read-hits": symstatNum_read_hits,
       "symstatNum-write-hits": symstatNum_write_hits,
       "symstatNum-blocks-read": symstatNum_blocks_read,
       "symstatNum-blocks-written": symstatNum_blocks_written,
       "symstatNum-seq-read-reqs": symstatNum_seq_read_reqs,
       "symstatNum-prefetched-tracks": symstatNum_prefetched_tracks,
       "symstatNum-destaged-tracks": symstatNum_destaged_tracks,
       "symstatNum-deferred-writes": symstatNum_deferred_writes,
       "symstatNum-delayed-dfw": symstatNum_delayed_dfw,
       "symstatNum-wr-pend-tracks": symstatNum_wr_pend_tracks,
       "symstatNum-format-pend-tracks": symstatNum_format_pend_tracks,
       "symstatDevice-max-wp-limit": symstatDevice_max_wp_limit,
       "symstatNum-sa-cdb-reqs": symstatNum_sa_cdb_reqs,
       "symstatNum-sa-rw-reqs": symstatNum_sa_rw_reqs,
       "symstatNum-sa-read-reqs": symstatNum_sa_read_reqs,
       "symstatNum-sa-write-reqs": symstatNum_sa_write_reqs,
       "symstatNum-sa-rw-hits": symstatNum_sa_rw_hits,
       "symstatNum-free-permacache-slots": symstatNum_free_permacache_slots,
       "symstatNum-used-permacache-slots": symstatNum_used_permacache_slots,
       "devStatTable": devStatTable,
       "devStatEntry": devStatEntry,
       "devstatTime-stamp": devstatTime_stamp,
       "devstatNum-sym-timeslices": devstatNum_sym_timeslices,
       "devstatNum-rw-reqs": devstatNum_rw_reqs,
       "devstatNum-read-reqs": devstatNum_read_reqs,
       "devstatNum-write-reqs": devstatNum_write_reqs,
       "devstatNum-rw-hits": devstatNum_rw_hits,
       "devstatNum-read-hits": devstatNum_read_hits,
       "devstatNum-write-hits": devstatNum_write_hits,
       "devstatNum-blocks-read": devstatNum_blocks_read,
       "devstatNum-blocks-written": devstatNum_blocks_written,
       "devstatNum-seq-read-reqs": devstatNum_seq_read_reqs,
       "devstatNum-prefetched-tracks": devstatNum_prefetched_tracks,
       "devstatNum-destaged-tracks": devstatNum_destaged_tracks,
       "devstatNum-deferred-writes": devstatNum_deferred_writes,
       "devstatNum-delayed-dfw": devstatNum_delayed_dfw,
       "devstatNum-wp-tracks": devstatNum_wp_tracks,
       "devstatNum-format-pend-tracks": devstatNum_format_pend_tracks,
       "devstatDevice-max-wp-limit": devstatDevice_max_wp_limit,
       "pDevStatTable": pDevStatTable,
       "pDevStatEntry": pDevStatEntry,
       "pdevstatTime-stamp": pdevstatTime_stamp,
       "pdevstatNum-sym-timeslices": pdevstatNum_sym_timeslices,
       "pdevstatNum-rw-reqs": pdevstatNum_rw_reqs,
       "pdevstatNum-read-reqs": pdevstatNum_read_reqs,
       "pdevstatNum-write-reqs": pdevstatNum_write_reqs,
       "pdevstatNum-rw-hits": pdevstatNum_rw_hits,
       "pdevstatNum-read-hits": pdevstatNum_read_hits,
       "pdevstatNum-write-hits": pdevstatNum_write_hits,
       "pdevstatNum-blocks-read": pdevstatNum_blocks_read,
       "pdevstatNum-blocks-written": pdevstatNum_blocks_written,
       "pdevstatNum-seq-read-reqs": pdevstatNum_seq_read_reqs,
       "pdevstatNum-prefetched-tracks": pdevstatNum_prefetched_tracks,
       "pdevstatNum-destaged-tracks": pdevstatNum_destaged_tracks,
       "pdevstatNum-deferred-writes": pdevstatNum_deferred_writes,
       "pdevstatNum-delayed-dfw": pdevstatNum_delayed_dfw,
       "pdevstatNum-wp-tracks": pdevstatNum_wp_tracks,
       "pdevstatNum-format-pend-tracks": pdevstatNum_format_pend_tracks,
       "pdevstatDevice-max-wp-limit": pdevstatDevice_max_wp_limit,
       "lDevStatTable": lDevStatTable,
       "lDevStatEntry": lDevStatEntry,
       "ldevstatTime-stamp": ldevstatTime_stamp,
       "ldevstatNum-sym-timeslices": ldevstatNum_sym_timeslices,
       "ldevstatNum-rw-reqs": ldevstatNum_rw_reqs,
       "ldevstatNum-read-reqs": ldevstatNum_read_reqs,
       "ldevstatNum-write-reqs": ldevstatNum_write_reqs,
       "ldevstatNum-rw-hits": ldevstatNum_rw_hits,
       "ldevstatNum-read-hits": ldevstatNum_read_hits,
       "ldevstatNum-write-hits": ldevstatNum_write_hits,
       "ldevstatNum-blocks-read": ldevstatNum_blocks_read,
       "ldevstatNum-blocks-written": ldevstatNum_blocks_written,
       "ldevstatNum-seq-read-reqs": ldevstatNum_seq_read_reqs,
       "ldevstatNum-prefetched-tracks": ldevstatNum_prefetched_tracks,
       "ldevstatNum-destaged-tracks": ldevstatNum_destaged_tracks,
       "ldevstatNum-deferred-writes": ldevstatNum_deferred_writes,
       "ldevstatNum-delayed-dfw": ldevstatNum_delayed_dfw,
       "ldevstatNum-wp-tracks": ldevstatNum_wp_tracks,
       "ldevstatNum-format-pend-tracks": ldevstatNum_format_pend_tracks,
       "ldevstatDevice-max-wp-limit": ldevstatDevice_max_wp_limit,
       "dgStatTable": dgStatTable,
       "dgStatEntry": dgStatEntry,
       "dgstatTime-stamp": dgstatTime_stamp,
       "dgstatNum-sym-timeslices": dgstatNum_sym_timeslices,
       "dgstatNum-rw-reqs": dgstatNum_rw_reqs,
       "dgstatNum-read-reqs": dgstatNum_read_reqs,
       "dgstatNum-write-reqs": dgstatNum_write_reqs,
       "dgstatNum-rw-hits": dgstatNum_rw_hits,
       "dgstatNum-read-hits": dgstatNum_read_hits,
       "dgstatNum-write-hits": dgstatNum_write_hits,
       "dgstatNum-blocks-read": dgstatNum_blocks_read,
       "dgstatNum-blocks-written": dgstatNum_blocks_written,
       "dgstatNum-seq-read-reqs": dgstatNum_seq_read_reqs,
       "dgstatNum-prefetched-tracks": dgstatNum_prefetched_tracks,
       "dgstatNum-destaged-tracks": dgstatNum_destaged_tracks,
       "dgstatNum-deferred-writes": dgstatNum_deferred_writes,
       "dgstatNum-delayed-dfw": dgstatNum_delayed_dfw,
       "dgstatNum-wp-tracks": dgstatNum_wp_tracks,
       "dgstatNum-format-pend-tracks": dgstatNum_format_pend_tracks,
       "dgstatdevice-max-wp-limit": dgstatdevice_max_wp_limit,
       "directorStatTable": directorStatTable,
       "directorStatEntry": directorStatEntry,
       "dirstatTime-stamp": dirstatTime_stamp,
       "dirstatNum-sym-timeslices": dirstatNum_sym_timeslices,
       "dirstatNum-rw-reqs": dirstatNum_rw_reqs,
       "dirstatNum-read-reqs": dirstatNum_read_reqs,
       "dirstatNum-write-reqs": dirstatNum_write_reqs,
       "dirstatNum-rw-hits": dirstatNum_rw_hits,
       "dirstatNum-permacache-reqs": dirstatNum_permacache_reqs,
       "dirstatNum-ios": dirstatNum_ios,
       "saDirStatTable": saDirStatTable,
       "saDirStatEntry": saDirStatEntry,
       "dirstatSANum-read-misses": dirstatSANum_read_misses,
       "dirstatSANum-slot-collisions": dirstatSANum_slot_collisions,
       "dirstatSANum-system-wp-disconnects": dirstatSANum_system_wp_disconnects,
       "dirstatSANum-device-wp-disconnects": dirstatSANum_device_wp_disconnects,
       "daDirStatTable": daDirStatTable,
       "daDirStatEntry": daDirStatEntry,
       "dirstatDANum-pf-tracks": dirstatDANum_pf_tracks,
       "dirstatDANum-pf-tracks-used": dirstatDANum_pf_tracks_used,
       "dirstatDANum-pf-tracks-unused": dirstatDANum_pf_tracks_unused,
       "dirstatDANum-pf-short-misses": dirstatDANum_pf_short_misses,
       "dirstatDANum-pf-long-misses": dirstatDANum_pf_long_misses,
       "dirstatDANum-pf-restarts": dirstatDANum_pf_restarts,
       "dirstatDANum-pf-mismatches": dirstatDANum_pf_mismatches,
       "raDirStatTable": raDirStatTable,
       "raDirStatEntry": raDirStatEntry,
       "dirstatRANum-read-misses": dirstatRANum_read_misses,
       "dirstatRANum-slot-collisions": dirstatRANum_slot_collisions,
       "dirstatRANum-system-wp-disconnects": dirstatRANum_system_wp_disconnects,
       "dirstatRANum-device-wp-disconnects": dirstatRANum_device_wp_disconnects,
       "dirPortStatistics": dirPortStatistics,
       "dirStatPortCountTable": dirStatPortCountTable,
       "dirStatPortCountEntry": dirStatPortCountEntry,
       "dirPortStatPortCount": dirPortStatPortCount,
       "dirPortStatTable": dirPortStatTable,
       "dirPortStatEntry": dirPortStatEntry,
       "portstatTime-stamp": portstatTime_stamp,
       "portstatNum-sym-timeslices": portstatNum_sym_timeslices,
       "portstatNum-rw-reqs": portstatNum_rw_reqs,
       "portstatNum-blocks-read-and-written": portstatNum_blocks_read_and_written,
       "symmEvent": symmEvent,
       "symmEventMaxEvents": symmEventMaxEvents,
       "symmEventTable": symmEventTable,
       "symmEventEntry": symmEventEntry,
       "symmEventIndex": symmEventIndex,
       "symmEventTime": symmEventTime,
       "symmEventSeverity": symmEventSeverity,
       "symmEventDescr": symmEventDescr}
)
