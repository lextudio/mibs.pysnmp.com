# SNMP MIB module (EMPIRE-APACHEMOD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMPIRE-APACHEMOD
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:27 2024
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

_Empire_ObjectIdentity = ObjectIdentity
empire = _Empire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546)
)
_Applications_ObjectIdentity = ObjectIdentity
applications = _Applications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16)
)
_ApacheSrv_ObjectIdentity = ObjectIdentity
apacheSrv = _ApacheSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 3)
)
_ApacheModVersion_Type = DisplayString
_ApacheModVersion_Object = MibScalar
apacheModVersion = _ApacheModVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 1),
    _ApacheModVersion_Type()
)
apacheModVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheModVersion.setStatus("mandatory")


class _ApacheModMode_Type(Integer32):
    """Custom type apacheModMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullMode", 1),
          ("restrictedMode", 2))
    )


_ApacheModMode_Type.__name__ = "Integer32"
_ApacheModMode_Object = MibScalar
apacheModMode = _ApacheModMode_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 2),
    _ApacheModMode_Type()
)
apacheModMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheModMode.setStatus("mandatory")
_ApacheConfigTable_Object = MibTable
apacheConfigTable = _ApacheConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10)
)
if mibBuilder.loadTexts:
    apacheConfigTable.setStatus("mandatory")
_ApacheConfigEntry_Object = MibTableRow
apacheConfigEntry = _ApacheConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1)
)
apacheConfigEntry.setIndexNames(
    (0, "EMPIRE-APACHEMOD", "apacheConfigPort"),
)
if mibBuilder.loadTexts:
    apacheConfigEntry.setStatus("mandatory")
_ApacheConfigPort_Type = Integer32
_ApacheConfigPort_Object = MibTableColumn
apacheConfigPort = _ApacheConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 1),
    _ApacheConfigPort_Type()
)
apacheConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigPort.setStatus("mandatory")
_ApacheConfigVersion_Type = DisplayString
_ApacheConfigVersion_Object = MibTableColumn
apacheConfigVersion = _ApacheConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 2),
    _ApacheConfigVersion_Type()
)
apacheConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigVersion.setStatus("mandatory")
_ApacheConfigPID_Type = Integer32
_ApacheConfigPID_Object = MibTableColumn
apacheConfigPID = _ApacheConfigPID_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 3),
    _ApacheConfigPID_Type()
)
apacheConfigPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigPID.setStatus("mandatory")
_ApacheConfigRunMode_Type = DisplayString
_ApacheConfigRunMode_Object = MibTableColumn
apacheConfigRunMode = _ApacheConfigRunMode_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 4),
    _ApacheConfigRunMode_Type()
)
apacheConfigRunMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigRunMode.setStatus("mandatory")
_ApacheConfigUser_Type = DisplayString
_ApacheConfigUser_Object = MibTableColumn
apacheConfigUser = _ApacheConfigUser_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 5),
    _ApacheConfigUser_Type()
)
apacheConfigUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigUser.setStatus("mandatory")
_ApacheConfigGroup_Type = DisplayString
_ApacheConfigGroup_Object = MibTableColumn
apacheConfigGroup = _ApacheConfigGroup_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 6),
    _ApacheConfigGroup_Type()
)
apacheConfigGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigGroup.setStatus("mandatory")
_ApacheConfigHostname_Type = DisplayString
_ApacheConfigHostname_Object = MibTableColumn
apacheConfigHostname = _ApacheConfigHostname_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 7),
    _ApacheConfigHostname_Type()
)
apacheConfigHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigHostname.setStatus("mandatory")
_ApacheConfigStartProcs_Type = Integer32
_ApacheConfigStartProcs_Object = MibTableColumn
apacheConfigStartProcs = _ApacheConfigStartProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 8),
    _ApacheConfigStartProcs_Type()
)
apacheConfigStartProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigStartProcs.setStatus("mandatory")
_ApacheConfigMinIdleProcs_Type = Integer32
_ApacheConfigMinIdleProcs_Object = MibTableColumn
apacheConfigMinIdleProcs = _ApacheConfigMinIdleProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 9),
    _ApacheConfigMinIdleProcs_Type()
)
apacheConfigMinIdleProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigMinIdleProcs.setStatus("mandatory")
_ApacheConfigMaxIdleProcs_Type = Integer32
_ApacheConfigMaxIdleProcs_Object = MibTableColumn
apacheConfigMaxIdleProcs = _ApacheConfigMaxIdleProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 10),
    _ApacheConfigMaxIdleProcs_Type()
)
apacheConfigMaxIdleProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigMaxIdleProcs.setStatus("mandatory")
_ApacheConfigMaxProcs_Type = Integer32
_ApacheConfigMaxProcs_Object = MibTableColumn
apacheConfigMaxProcs = _ApacheConfigMaxProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 11),
    _ApacheConfigMaxProcs_Type()
)
apacheConfigMaxProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigMaxProcs.setStatus("mandatory")
_ApacheConfigRequestsMaxPerChild_Type = Integer32
_ApacheConfigRequestsMaxPerChild_Object = MibTableColumn
apacheConfigRequestsMaxPerChild = _ApacheConfigRequestsMaxPerChild_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 12),
    _ApacheConfigRequestsMaxPerChild_Type()
)
apacheConfigRequestsMaxPerChild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigRequestsMaxPerChild.setStatus("mandatory")
_ApacheConfigRequestsKeepAlive_Type = Integer32
_ApacheConfigRequestsKeepAlive_Object = MibTableColumn
apacheConfigRequestsKeepAlive = _ApacheConfigRequestsKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 13),
    _ApacheConfigRequestsKeepAlive_Type()
)
apacheConfigRequestsKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigRequestsKeepAlive.setStatus("mandatory")
_ApacheConfigRequestsMaxPerConn_Type = Integer32
_ApacheConfigRequestsMaxPerConn_Object = MibTableColumn
apacheConfigRequestsMaxPerConn = _ApacheConfigRequestsMaxPerConn_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 14),
    _ApacheConfigRequestsMaxPerConn_Type()
)
apacheConfigRequestsMaxPerConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigRequestsMaxPerConn.setStatus("mandatory")
_ApacheConfigThreadsPerChild_Type = Integer32
_ApacheConfigThreadsPerChild_Object = MibTableColumn
apacheConfigThreadsPerChild = _ApacheConfigThreadsPerChild_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 15),
    _ApacheConfigThreadsPerChild_Type()
)
apacheConfigThreadsPerChild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigThreadsPerChild.setStatus("mandatory")
_ApacheConfigConnectionTimeout_Type = Integer32
_ApacheConfigConnectionTimeout_Object = MibTableColumn
apacheConfigConnectionTimeout = _ApacheConfigConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 16),
    _ApacheConfigConnectionTimeout_Type()
)
apacheConfigConnectionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigConnectionTimeout.setStatus("mandatory")
_ApacheConfigKeepAliveTimeout_Type = Integer32
_ApacheConfigKeepAliveTimeout_Object = MibTableColumn
apacheConfigKeepAliveTimeout = _ApacheConfigKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 17),
    _ApacheConfigKeepAliveTimeout_Type()
)
apacheConfigKeepAliveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigKeepAliveTimeout.setStatus("mandatory")
_ApacheConfigServerRoot_Type = DisplayString
_ApacheConfigServerRoot_Object = MibTableColumn
apacheConfigServerRoot = _ApacheConfigServerRoot_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 18),
    _ApacheConfigServerRoot_Type()
)
apacheConfigServerRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigServerRoot.setStatus("mandatory")
_ApacheConfigConfigFile_Type = DisplayString
_ApacheConfigConfigFile_Object = MibTableColumn
apacheConfigConfigFile = _ApacheConfigConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 19),
    _ApacheConfigConfigFile_Type()
)
apacheConfigConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigConfigFile.setStatus("mandatory")
_ApacheConfigPIDFile_Type = DisplayString
_ApacheConfigPIDFile_Object = MibTableColumn
apacheConfigPIDFile = _ApacheConfigPIDFile_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 20),
    _ApacheConfigPIDFile_Type()
)
apacheConfigPIDFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigPIDFile.setStatus("mandatory")
_ApacheConfigScoreboardFile_Type = DisplayString
_ApacheConfigScoreboardFile_Object = MibTableColumn
apacheConfigScoreboardFile = _ApacheConfigScoreboardFile_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 21),
    _ApacheConfigScoreboardFile_Type()
)
apacheConfigScoreboardFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigScoreboardFile.setStatus("mandatory")
_ApacheConfigDocumentRoot_Type = DisplayString
_ApacheConfigDocumentRoot_Object = MibTableColumn
apacheConfigDocumentRoot = _ApacheConfigDocumentRoot_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 22),
    _ApacheConfigDocumentRoot_Type()
)
apacheConfigDocumentRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigDocumentRoot.setStatus("mandatory")
_ApacheConfigAccessLogFile_Type = DisplayString
_ApacheConfigAccessLogFile_Object = MibTableColumn
apacheConfigAccessLogFile = _ApacheConfigAccessLogFile_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 23),
    _ApacheConfigAccessLogFile_Type()
)
apacheConfigAccessLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigAccessLogFile.setStatus("mandatory")
_ApacheConfigErrorLogFile_Type = DisplayString
_ApacheConfigErrorLogFile_Object = MibTableColumn
apacheConfigErrorLogFile = _ApacheConfigErrorLogFile_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 24),
    _ApacheConfigErrorLogFile_Type()
)
apacheConfigErrorLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigErrorLogFile.setStatus("mandatory")
_ApacheConfigScriptLogFile_Type = DisplayString
_ApacheConfigScriptLogFile_Object = MibTableColumn
apacheConfigScriptLogFile = _ApacheConfigScriptLogFile_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 10, 1, 25),
    _ApacheConfigScriptLogFile_Type()
)
apacheConfigScriptLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheConfigScriptLogFile.setStatus("mandatory")
_ApachePerformance_ObjectIdentity = ObjectIdentity
apachePerformance = _ApachePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11)
)
_ApacheFootprintTable_Object = MibTable
apacheFootprintTable = _ApacheFootprintTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1)
)
if mibBuilder.loadTexts:
    apacheFootprintTable.setStatus("mandatory")
_ApacheFootprintEntry_Object = MibTableRow
apacheFootprintEntry = _ApacheFootprintEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1)
)
apacheFootprintEntry.setIndexNames(
    (0, "EMPIRE-APACHEMOD", "apacheFootprintPort"),
)
if mibBuilder.loadTexts:
    apacheFootprintEntry.setStatus("mandatory")
_ApacheFootprintPort_Type = Integer32
_ApacheFootprintPort_Object = MibTableColumn
apacheFootprintPort = _ApacheFootprintPort_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 1),
    _ApacheFootprintPort_Type()
)
apacheFootprintPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintPort.setStatus("mandatory")
_ApacheFootprintCPUTime_Type = Integer32
_ApacheFootprintCPUTime_Object = MibTableColumn
apacheFootprintCPUTime = _ApacheFootprintCPUTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 2),
    _ApacheFootprintCPUTime_Type()
)
apacheFootprintCPUTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintCPUTime.setStatus("mandatory")


class _ApacheFootprintPercentCPU_Type(Integer32):
    """Custom type apacheFootprintPercentCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApacheFootprintPercentCPU_Type.__name__ = "Integer32"
_ApacheFootprintPercentCPU_Object = MibTableColumn
apacheFootprintPercentCPU = _ApacheFootprintPercentCPU_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 3),
    _ApacheFootprintPercentCPU_Type()
)
apacheFootprintPercentCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintPercentCPU.setStatus("mandatory")
_ApacheFootprintTotalMEMSize_Type = Gauge32
_ApacheFootprintTotalMEMSize_Object = MibTableColumn
apacheFootprintTotalMEMSize = _ApacheFootprintTotalMEMSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 4),
    _ApacheFootprintTotalMEMSize_Type()
)
apacheFootprintTotalMEMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintTotalMEMSize.setStatus("mandatory")
_ApacheFootprintTotalRSS_Type = Gauge32
_ApacheFootprintTotalRSS_Object = MibTableColumn
apacheFootprintTotalRSS = _ApacheFootprintTotalRSS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 5),
    _ApacheFootprintTotalRSS_Type()
)
apacheFootprintTotalRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintTotalRSS.setStatus("mandatory")


class _ApacheFootprintPercentMEM_Type(Integer32):
    """Custom type apacheFootprintPercentMEM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApacheFootprintPercentMEM_Type.__name__ = "Integer32"
_ApacheFootprintPercentMEM_Object = MibTableColumn
apacheFootprintPercentMEM = _ApacheFootprintPercentMEM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 6),
    _ApacheFootprintPercentMEM_Type()
)
apacheFootprintPercentMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintPercentMEM.setStatus("mandatory")
_ApacheFootprintNumThreads_Type = Gauge32
_ApacheFootprintNumThreads_Object = MibTableColumn
apacheFootprintNumThreads = _ApacheFootprintNumThreads_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 7),
    _ApacheFootprintNumThreads_Type()
)
apacheFootprintNumThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintNumThreads.setStatus("mandatory")
_ApacheFootprintInBlks_Type = Counter32
_ApacheFootprintInBlks_Object = MibTableColumn
apacheFootprintInBlks = _ApacheFootprintInBlks_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 8),
    _ApacheFootprintInBlks_Type()
)
apacheFootprintInBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintInBlks.setStatus("mandatory")
_ApacheFootprintOutBlks_Type = Counter32
_ApacheFootprintOutBlks_Object = MibTableColumn
apacheFootprintOutBlks = _ApacheFootprintOutBlks_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 9),
    _ApacheFootprintOutBlks_Type()
)
apacheFootprintOutBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintOutBlks.setStatus("mandatory")
_ApacheFootprintMsgsSent_Type = Counter32
_ApacheFootprintMsgsSent_Object = MibTableColumn
apacheFootprintMsgsSent = _ApacheFootprintMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 10),
    _ApacheFootprintMsgsSent_Type()
)
apacheFootprintMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintMsgsSent.setStatus("mandatory")
_ApacheFootprintMsgsRecv_Type = Counter32
_ApacheFootprintMsgsRecv_Object = MibTableColumn
apacheFootprintMsgsRecv = _ApacheFootprintMsgsRecv_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 11),
    _ApacheFootprintMsgsRecv_Type()
)
apacheFootprintMsgsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintMsgsRecv.setStatus("mandatory")
_ApacheFootprintSysCalls_Type = Counter32
_ApacheFootprintSysCalls_Object = MibTableColumn
apacheFootprintSysCalls = _ApacheFootprintSysCalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 12),
    _ApacheFootprintSysCalls_Type()
)
apacheFootprintSysCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintSysCalls.setStatus("mandatory")
_ApacheFootprintMinorPgFlts_Type = Counter32
_ApacheFootprintMinorPgFlts_Object = MibTableColumn
apacheFootprintMinorPgFlts = _ApacheFootprintMinorPgFlts_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 13),
    _ApacheFootprintMinorPgFlts_Type()
)
apacheFootprintMinorPgFlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintMinorPgFlts.setStatus("mandatory")
_ApacheFootprintMajorPgFlts_Type = Counter32
_ApacheFootprintMajorPgFlts_Object = MibTableColumn
apacheFootprintMajorPgFlts = _ApacheFootprintMajorPgFlts_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 14),
    _ApacheFootprintMajorPgFlts_Type()
)
apacheFootprintMajorPgFlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintMajorPgFlts.setStatus("mandatory")
_ApacheFootprintNumSwaps_Type = Counter32
_ApacheFootprintNumSwaps_Object = MibTableColumn
apacheFootprintNumSwaps = _ApacheFootprintNumSwaps_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 15),
    _ApacheFootprintNumSwaps_Type()
)
apacheFootprintNumSwaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintNumSwaps.setStatus("mandatory")
_ApacheFootprintVolCtx_Type = Counter32
_ApacheFootprintVolCtx_Object = MibTableColumn
apacheFootprintVolCtx = _ApacheFootprintVolCtx_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 16),
    _ApacheFootprintVolCtx_Type()
)
apacheFootprintVolCtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintVolCtx.setStatus("mandatory")
_ApacheFootprintInvolCtx_Type = Counter32
_ApacheFootprintInvolCtx_Object = MibTableColumn
apacheFootprintInvolCtx = _ApacheFootprintInvolCtx_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 17),
    _ApacheFootprintInvolCtx_Type()
)
apacheFootprintInvolCtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintInvolCtx.setStatus("mandatory")
_ApacheFootprintTotalLogSize_Type = Gauge32
_ApacheFootprintTotalLogSize_Object = MibTableColumn
apacheFootprintTotalLogSize = _ApacheFootprintTotalLogSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 18),
    _ApacheFootprintTotalLogSize_Type()
)
apacheFootprintTotalLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintTotalLogSize.setStatus("mandatory")
_ApacheFootprintDocSize_Type = Gauge32
_ApacheFootprintDocSize_Object = MibTableColumn
apacheFootprintDocSize = _ApacheFootprintDocSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 19),
    _ApacheFootprintDocSize_Type()
)
apacheFootprintDocSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintDocSize.setStatus("mandatory")
_ApacheFootprintTotalDiskSize_Type = Gauge32
_ApacheFootprintTotalDiskSize_Object = MibTableColumn
apacheFootprintTotalDiskSize = _ApacheFootprintTotalDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 1, 1, 20),
    _ApacheFootprintTotalDiskSize_Type()
)
apacheFootprintTotalDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheFootprintTotalDiskSize.setStatus("mandatory")
_ApacheServerPerfTable_Object = MibTable
apacheServerPerfTable = _ApacheServerPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2)
)
if mibBuilder.loadTexts:
    apacheServerPerfTable.setStatus("mandatory")
_ApacheServerPerfEntry_Object = MibTableRow
apacheServerPerfEntry = _ApacheServerPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1)
)
apacheServerPerfEntry.setIndexNames(
    (0, "EMPIRE-APACHEMOD", "apacheServerPerfPort"),
)
if mibBuilder.loadTexts:
    apacheServerPerfEntry.setStatus("mandatory")
_ApacheServerPerfPort_Type = Integer32
_ApacheServerPerfPort_Object = MibTableColumn
apacheServerPerfPort = _ApacheServerPerfPort_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 1),
    _ApacheServerPerfPort_Type()
)
apacheServerPerfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfPort.setStatus("mandatory")
_ApacheServerPerfUptime_Type = Counter32
_ApacheServerPerfUptime_Object = MibTableColumn
apacheServerPerfUptime = _ApacheServerPerfUptime_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 2),
    _ApacheServerPerfUptime_Type()
)
apacheServerPerfUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfUptime.setStatus("mandatory")
_ApacheServerPerfTotalAccesses_Type = Counter32
_ApacheServerPerfTotalAccesses_Object = MibTableColumn
apacheServerPerfTotalAccesses = _ApacheServerPerfTotalAccesses_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 3),
    _ApacheServerPerfTotalAccesses_Type()
)
apacheServerPerfTotalAccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfTotalAccesses.setStatus("mandatory")
_ApacheServerPerfTotalTraffic_Type = Counter32
_ApacheServerPerfTotalTraffic_Object = MibTableColumn
apacheServerPerfTotalTraffic = _ApacheServerPerfTotalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 4),
    _ApacheServerPerfTotalTraffic_Type()
)
apacheServerPerfTotalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfTotalTraffic.setStatus("mandatory")
_ApacheServerPerfCurrentUsers_Type = Gauge32
_ApacheServerPerfCurrentUsers_Object = MibTableColumn
apacheServerPerfCurrentUsers = _ApacheServerPerfCurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 5),
    _ApacheServerPerfCurrentUsers_Type()
)
apacheServerPerfCurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentUsers.setStatus("mandatory")
_ApacheServerPerfCurrentIdleProcs_Type = Gauge32
_ApacheServerPerfCurrentIdleProcs_Object = MibTableColumn
apacheServerPerfCurrentIdleProcs = _ApacheServerPerfCurrentIdleProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 6),
    _ApacheServerPerfCurrentIdleProcs_Type()
)
apacheServerPerfCurrentIdleProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentIdleProcs.setStatus("mandatory")
_ApacheServerPerfCurrentStartupProcs_Type = Gauge32
_ApacheServerPerfCurrentStartupProcs_Object = MibTableColumn
apacheServerPerfCurrentStartupProcs = _ApacheServerPerfCurrentStartupProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 7),
    _ApacheServerPerfCurrentStartupProcs_Type()
)
apacheServerPerfCurrentStartupProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentStartupProcs.setStatus("mandatory")
_ApacheServerPerfCurrentReadProcs_Type = Gauge32
_ApacheServerPerfCurrentReadProcs_Object = MibTableColumn
apacheServerPerfCurrentReadProcs = _ApacheServerPerfCurrentReadProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 8),
    _ApacheServerPerfCurrentReadProcs_Type()
)
apacheServerPerfCurrentReadProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentReadProcs.setStatus("mandatory")
_ApacheServerPerfCurrentReplyProcs_Type = Gauge32
_ApacheServerPerfCurrentReplyProcs_Object = MibTableColumn
apacheServerPerfCurrentReplyProcs = _ApacheServerPerfCurrentReplyProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 9),
    _ApacheServerPerfCurrentReplyProcs_Type()
)
apacheServerPerfCurrentReplyProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentReplyProcs.setStatus("mandatory")
_ApacheServerPerfCurrentKeepAliveProcs_Type = Gauge32
_ApacheServerPerfCurrentKeepAliveProcs_Object = MibTableColumn
apacheServerPerfCurrentKeepAliveProcs = _ApacheServerPerfCurrentKeepAliveProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 10),
    _ApacheServerPerfCurrentKeepAliveProcs_Type()
)
apacheServerPerfCurrentKeepAliveProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentKeepAliveProcs.setStatus("mandatory")
_ApacheServerPerfCurrentDNSProcs_Type = Gauge32
_ApacheServerPerfCurrentDNSProcs_Object = MibTableColumn
apacheServerPerfCurrentDNSProcs = _ApacheServerPerfCurrentDNSProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 11),
    _ApacheServerPerfCurrentDNSProcs_Type()
)
apacheServerPerfCurrentDNSProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentDNSProcs.setStatus("mandatory")
_ApacheServerPerfCurrentLoggingProcs_Type = Gauge32
_ApacheServerPerfCurrentLoggingProcs_Object = MibTableColumn
apacheServerPerfCurrentLoggingProcs = _ApacheServerPerfCurrentLoggingProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 12),
    _ApacheServerPerfCurrentLoggingProcs_Type()
)
apacheServerPerfCurrentLoggingProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentLoggingProcs.setStatus("mandatory")
_ApacheServerPerfCurrentFinishingProcs_Type = Gauge32
_ApacheServerPerfCurrentFinishingProcs_Object = MibTableColumn
apacheServerPerfCurrentFinishingProcs = _ApacheServerPerfCurrentFinishingProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 13),
    _ApacheServerPerfCurrentFinishingProcs_Type()
)
apacheServerPerfCurrentFinishingProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentFinishingProcs.setStatus("mandatory")
_ApacheServerPerfCurrentTotalProcs_Type = Gauge32
_ApacheServerPerfCurrentTotalProcs_Object = MibTableColumn
apacheServerPerfCurrentTotalProcs = _ApacheServerPerfCurrentTotalProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 14),
    _ApacheServerPerfCurrentTotalProcs_Type()
)
apacheServerPerfCurrentTotalProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentTotalProcs.setStatus("mandatory")
_ApacheServerPerfCurrentBusyProcs_Type = Gauge32
_ApacheServerPerfCurrentBusyProcs_Object = MibTableColumn
apacheServerPerfCurrentBusyProcs = _ApacheServerPerfCurrentBusyProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 3, 11, 2, 1, 15),
    _ApacheServerPerfCurrentBusyProcs_Type()
)
apacheServerPerfCurrentBusyProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apacheServerPerfCurrentBusyProcs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMPIRE-APACHEMOD",
    **{"empire": empire,
       "applications": applications,
       "apacheSrv": apacheSrv,
       "apacheModVersion": apacheModVersion,
       "apacheModMode": apacheModMode,
       "apacheConfigTable": apacheConfigTable,
       "apacheConfigEntry": apacheConfigEntry,
       "apacheConfigPort": apacheConfigPort,
       "apacheConfigVersion": apacheConfigVersion,
       "apacheConfigPID": apacheConfigPID,
       "apacheConfigRunMode": apacheConfigRunMode,
       "apacheConfigUser": apacheConfigUser,
       "apacheConfigGroup": apacheConfigGroup,
       "apacheConfigHostname": apacheConfigHostname,
       "apacheConfigStartProcs": apacheConfigStartProcs,
       "apacheConfigMinIdleProcs": apacheConfigMinIdleProcs,
       "apacheConfigMaxIdleProcs": apacheConfigMaxIdleProcs,
       "apacheConfigMaxProcs": apacheConfigMaxProcs,
       "apacheConfigRequestsMaxPerChild": apacheConfigRequestsMaxPerChild,
       "apacheConfigRequestsKeepAlive": apacheConfigRequestsKeepAlive,
       "apacheConfigRequestsMaxPerConn": apacheConfigRequestsMaxPerConn,
       "apacheConfigThreadsPerChild": apacheConfigThreadsPerChild,
       "apacheConfigConnectionTimeout": apacheConfigConnectionTimeout,
       "apacheConfigKeepAliveTimeout": apacheConfigKeepAliveTimeout,
       "apacheConfigServerRoot": apacheConfigServerRoot,
       "apacheConfigConfigFile": apacheConfigConfigFile,
       "apacheConfigPIDFile": apacheConfigPIDFile,
       "apacheConfigScoreboardFile": apacheConfigScoreboardFile,
       "apacheConfigDocumentRoot": apacheConfigDocumentRoot,
       "apacheConfigAccessLogFile": apacheConfigAccessLogFile,
       "apacheConfigErrorLogFile": apacheConfigErrorLogFile,
       "apacheConfigScriptLogFile": apacheConfigScriptLogFile,
       "apachePerformance": apachePerformance,
       "apacheFootprintTable": apacheFootprintTable,
       "apacheFootprintEntry": apacheFootprintEntry,
       "apacheFootprintPort": apacheFootprintPort,
       "apacheFootprintCPUTime": apacheFootprintCPUTime,
       "apacheFootprintPercentCPU": apacheFootprintPercentCPU,
       "apacheFootprintTotalMEMSize": apacheFootprintTotalMEMSize,
       "apacheFootprintTotalRSS": apacheFootprintTotalRSS,
       "apacheFootprintPercentMEM": apacheFootprintPercentMEM,
       "apacheFootprintNumThreads": apacheFootprintNumThreads,
       "apacheFootprintInBlks": apacheFootprintInBlks,
       "apacheFootprintOutBlks": apacheFootprintOutBlks,
       "apacheFootprintMsgsSent": apacheFootprintMsgsSent,
       "apacheFootprintMsgsRecv": apacheFootprintMsgsRecv,
       "apacheFootprintSysCalls": apacheFootprintSysCalls,
       "apacheFootprintMinorPgFlts": apacheFootprintMinorPgFlts,
       "apacheFootprintMajorPgFlts": apacheFootprintMajorPgFlts,
       "apacheFootprintNumSwaps": apacheFootprintNumSwaps,
       "apacheFootprintVolCtx": apacheFootprintVolCtx,
       "apacheFootprintInvolCtx": apacheFootprintInvolCtx,
       "apacheFootprintTotalLogSize": apacheFootprintTotalLogSize,
       "apacheFootprintDocSize": apacheFootprintDocSize,
       "apacheFootprintTotalDiskSize": apacheFootprintTotalDiskSize,
       "apacheServerPerfTable": apacheServerPerfTable,
       "apacheServerPerfEntry": apacheServerPerfEntry,
       "apacheServerPerfPort": apacheServerPerfPort,
       "apacheServerPerfUptime": apacheServerPerfUptime,
       "apacheServerPerfTotalAccesses": apacheServerPerfTotalAccesses,
       "apacheServerPerfTotalTraffic": apacheServerPerfTotalTraffic,
       "apacheServerPerfCurrentUsers": apacheServerPerfCurrentUsers,
       "apacheServerPerfCurrentIdleProcs": apacheServerPerfCurrentIdleProcs,
       "apacheServerPerfCurrentStartupProcs": apacheServerPerfCurrentStartupProcs,
       "apacheServerPerfCurrentReadProcs": apacheServerPerfCurrentReadProcs,
       "apacheServerPerfCurrentReplyProcs": apacheServerPerfCurrentReplyProcs,
       "apacheServerPerfCurrentKeepAliveProcs": apacheServerPerfCurrentKeepAliveProcs,
       "apacheServerPerfCurrentDNSProcs": apacheServerPerfCurrentDNSProcs,
       "apacheServerPerfCurrentLoggingProcs": apacheServerPerfCurrentLoggingProcs,
       "apacheServerPerfCurrentFinishingProcs": apacheServerPerfCurrentFinishingProcs,
       "apacheServerPerfCurrentTotalProcs": apacheServerPerfCurrentTotalProcs,
       "apacheServerPerfCurrentBusyProcs": apacheServerPerfCurrentBusyProcs}
)
