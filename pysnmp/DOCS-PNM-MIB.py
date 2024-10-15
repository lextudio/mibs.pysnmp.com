# SNMP MIB module (DOCS-PNM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-PNM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:58 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(TenthdB,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB")

(docsIf3CmSpectrumAnalysisCtrlCmd,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "docsIf3CmSpectrumAnalysisCtrlCmd")

(DsOfdmModulationType,) = mibBuilder.importSymbols(
    "DOCS-IF31-MIB",
    "DsOfdmModulationType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

docsPnmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27)
)
docsPnmMIB.setRevisions(
        ("2017-04-13 00:00",
         "2016-12-15 00:00",
         "2016-09-01 00:00",
         "2016-05-05 00:00",
         "2015-11-04 00:00",
         "2015-05-20 00:00",
         "2015-04-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MeasStatusType(Integer32, TextualConvention):
    status = "current"
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
        *(("busy", 3),
          ("error", 5),
          ("inactive", 2),
          ("other", 1),
          ("resourceUnavailable", 6),
          ("sampleReady", 4),
          ("sampleTruncated", 7))
    )



class ThousandthdB(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-3"


class UsOfdmaWindowingSizeType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(224, 224),
    )



# MIB Managed Objects in the order of their OIDs



class _DocsIf3CmSpectrumAnalysisCtrlCmdFileEnable_Type(TruthValue):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdFileEnable based on TruthValue"""


_DocsIf3CmSpectrumAnalysisCtrlCmdFileEnable_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdFileEnable = _DocsIf3CmSpectrumAnalysisCtrlCmdFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 10),
    _DocsIf3CmSpectrumAnalysisCtrlCmdFileEnable_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdFileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdFileEnable.setStatus("current")
_DocsIf3CmSpectrumAnalysisCtrlCmdMeasStatus_Type = MeasStatusType
_DocsIf3CmSpectrumAnalysisCtrlCmdMeasStatus_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdMeasStatus = _DocsIf3CmSpectrumAnalysisCtrlCmdMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 11),
    _DocsIf3CmSpectrumAnalysisCtrlCmdMeasStatus_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdMeasStatus.setStatus("current")
_DocsIf3CmSpectrumAnalysisCtrlCmdFileName_Type = SnmpAdminString
_DocsIf3CmSpectrumAnalysisCtrlCmdFileName_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdFileName = _DocsIf3CmSpectrumAnalysisCtrlCmdFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 12),
    _DocsIf3CmSpectrumAnalysisCtrlCmdFileName_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdFileName.setStatus("current")
_DocsPnmNotifications_ObjectIdentity = ObjectIdentity
docsPnmNotifications = _DocsPnmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 0)
)
_DocsPnmMibObjects_ObjectIdentity = ObjectIdentity
docsPnmMibObjects = _DocsPnmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1)
)
_DocsPnmBulkData_ObjectIdentity = ObjectIdentity
docsPnmBulkData = _DocsPnmBulkData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1)
)
_DocsPnmBulkCtl_ObjectIdentity = ObjectIdentity
docsPnmBulkCtl = _DocsPnmBulkCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 1)
)


class _DocsPnmBulkDestIpAddrType_Type(InetAddressType):
    """Custom type docsPnmBulkDestIpAddrType based on InetAddressType"""


_DocsPnmBulkDestIpAddrType_Object = MibScalar
docsPnmBulkDestIpAddrType = _DocsPnmBulkDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 1, 1),
    _DocsPnmBulkDestIpAddrType_Type()
)
docsPnmBulkDestIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmBulkDestIpAddrType.setStatus("current")
_DocsPnmBulkDestIpAddr_Type = InetAddress
_DocsPnmBulkDestIpAddr_Object = MibScalar
docsPnmBulkDestIpAddr = _DocsPnmBulkDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 1, 2),
    _DocsPnmBulkDestIpAddr_Type()
)
docsPnmBulkDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmBulkDestIpAddr.setStatus("current")
_DocsPnmBulkDestPath_Type = SnmpAdminString
_DocsPnmBulkDestPath_Object = MibScalar
docsPnmBulkDestPath = _DocsPnmBulkDestPath_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 1, 3),
    _DocsPnmBulkDestPath_Type()
)
docsPnmBulkDestPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmBulkDestPath.setStatus("current")


class _DocsPnmBulkUploadControl_Type(Integer32):
    """Custom type docsPnmBulkUploadControl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoUpload", 3),
          ("noAutoUpload", 2),
          ("other", 1))
    )


_DocsPnmBulkUploadControl_Type.__name__ = "Integer32"
_DocsPnmBulkUploadControl_Object = MibScalar
docsPnmBulkUploadControl = _DocsPnmBulkUploadControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 1, 4),
    _DocsPnmBulkUploadControl_Type()
)
docsPnmBulkUploadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmBulkUploadControl.setStatus("current")
_DocsPnmBulkFileTable_Object = MibTable
docsPnmBulkFileTable = _DocsPnmBulkFileTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsPnmBulkFileTable.setStatus("current")
_DocsPnmBulkFileEntry_Object = MibTableRow
docsPnmBulkFileEntry = _DocsPnmBulkFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 2, 1)
)
docsPnmBulkFileEntry.setIndexNames(
    (0, "DOCS-PNM-MIB", "docsPnmBulkFileIndex"),
)
if mibBuilder.loadTexts:
    docsPnmBulkFileEntry.setStatus("current")


class _DocsPnmBulkFileIndex_Type(Unsigned32):
    """Custom type docsPnmBulkFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsPnmBulkFileIndex_Type.__name__ = "Unsigned32"
_DocsPnmBulkFileIndex_Object = MibTableColumn
docsPnmBulkFileIndex = _DocsPnmBulkFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 2, 1, 1),
    _DocsPnmBulkFileIndex_Type()
)
docsPnmBulkFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsPnmBulkFileIndex.setStatus("current")
_DocsPnmBulkFileName_Type = SnmpAdminString
_DocsPnmBulkFileName_Object = MibTableColumn
docsPnmBulkFileName = _DocsPnmBulkFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 2, 1, 2),
    _DocsPnmBulkFileName_Type()
)
docsPnmBulkFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmBulkFileName.setStatus("current")


class _DocsPnmBulkFileControl_Type(Integer32):
    """Custom type docsPnmBulkFileControl based on Integer32"""
    defaultValue = 1

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
        *(("cancelUpload", 3),
          ("deleteFile", 4),
          ("other", 1),
          ("tftpUpload", 2))
    )


_DocsPnmBulkFileControl_Type.__name__ = "Integer32"
_DocsPnmBulkFileControl_Object = MibTableColumn
docsPnmBulkFileControl = _DocsPnmBulkFileControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 2, 1, 3),
    _DocsPnmBulkFileControl_Type()
)
docsPnmBulkFileControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmBulkFileControl.setStatus("current")


class _DocsPnmBulkFileUploadStatus_Type(Integer32):
    """Custom type docsPnmBulkFileUploadStatus based on Integer32"""
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
        *(("availableForUpload", 2),
          ("error", 7),
          ("other", 1),
          ("uploadCancelled", 6),
          ("uploadCompleted", 4),
          ("uploadInProgress", 3),
          ("uploadPending", 5))
    )


_DocsPnmBulkFileUploadStatus_Type.__name__ = "Integer32"
_DocsPnmBulkFileUploadStatus_Object = MibTableColumn
docsPnmBulkFileUploadStatus = _DocsPnmBulkFileUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 1, 2, 1, 4),
    _DocsPnmBulkFileUploadStatus_Type()
)
docsPnmBulkFileUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmBulkFileUploadStatus.setStatus("current")
_DocsPnmCmObjects_ObjectIdentity = ObjectIdentity
docsPnmCmObjects = _DocsPnmCmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2)
)
_DocsPnmCmControlObjects_ObjectIdentity = ObjectIdentity
docsPnmCmControlObjects = _DocsPnmCmControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 1)
)


class _DocsPnmCmCtlTest_Type(Integer32):
    """Custom type docsPnmCmCtlTest based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dsConstellationDisp", 5),
          ("dsHistogram", 8),
          ("dsOfdmChanEstCoef", 4),
          ("dsOfdmCodewordErrorRate", 7),
          ("dsOfdmRxMERPerSubCar", 6),
          ("dsOfdmSymbolCapture", 3),
          ("dsSpectrumAnalyzer", 2),
          ("other", 1),
          ("usPreEqualizerCoef", 9))
    )


_DocsPnmCmCtlTest_Type.__name__ = "Integer32"
_DocsPnmCmCtlTest_Object = MibScalar
docsPnmCmCtlTest = _DocsPnmCmCtlTest_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 1, 1),
    _DocsPnmCmCtlTest_Type()
)
docsPnmCmCtlTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmCtlTest.setStatus("current")
_DocsPnmCmCtlTestDuration_Type = Unsigned32
_DocsPnmCmCtlTestDuration_Object = MibScalar
docsPnmCmCtlTestDuration = _DocsPnmCmCtlTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 1, 2),
    _DocsPnmCmCtlTestDuration_Type()
)
docsPnmCmCtlTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmCtlTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmCtlTestDuration.setUnits("seconds")


class _DocsPnmCmCtlStatus_Type(Integer32):
    """Custom type docsPnmCmCtlStatus based on Integer32"""
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
        *(("other", 1),
          ("ready", 2),
          ("tempReject", 4),
          ("testInProgress", 3))
    )


_DocsPnmCmCtlStatus_Type.__name__ = "Integer32"
_DocsPnmCmCtlStatus_Object = MibScalar
docsPnmCmCtlStatus = _DocsPnmCmCtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 1, 3),
    _DocsPnmCmCtlStatus_Type()
)
docsPnmCmCtlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmCtlStatus.setStatus("current")
_DocsPnmCmDsOfdmSymCapTable_Object = MibTable
docsPnmCmDsOfdmSymCapTable = _DocsPnmCmDsOfdmSymCapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2)
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymCapTable.setStatus("current")
_DocsPnmCmDsOfdmSymCapEntry_Object = MibTableRow
docsPnmCmDsOfdmSymCapEntry = _DocsPnmCmDsOfdmSymCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1)
)
docsPnmCmDsOfdmSymCapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymCapEntry.setStatus("current")


class _DocsPnmCmDsOfdmSymTrigEnable_Type(TruthValue):
    """Custom type docsPnmCmDsOfdmSymTrigEnable based on TruthValue"""


_DocsPnmCmDsOfdmSymTrigEnable_Object = MibTableColumn
docsPnmCmDsOfdmSymTrigEnable = _DocsPnmCmDsOfdmSymTrigEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 1),
    _DocsPnmCmDsOfdmSymTrigEnable_Type()
)
docsPnmCmDsOfdmSymTrigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymTrigEnable.setStatus("current")


class _DocsPnmCmDsOfdmSymTrigEnableTimeout_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmSymTrigEnableTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DocsPnmCmDsOfdmSymTrigEnableTimeout_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmSymTrigEnableTimeout_Object = MibTableColumn
docsPnmCmDsOfdmSymTrigEnableTimeout = _DocsPnmCmDsOfdmSymTrigEnableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 2),
    _DocsPnmCmDsOfdmSymTrigEnableTimeout_Type()
)
docsPnmCmDsOfdmSymTrigEnableTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymTrigEnableTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymTrigEnableTimeout.setUnits("seconds")


class _DocsPnmCmDsOfdmSymTrigGroupId_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmSymTrigGroupId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmDsOfdmSymTrigGroupId_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmSymTrigGroupId_Object = MibTableColumn
docsPnmCmDsOfdmSymTrigGroupId = _DocsPnmCmDsOfdmSymTrigGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 3),
    _DocsPnmCmDsOfdmSymTrigGroupId_Type()
)
docsPnmCmDsOfdmSymTrigGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymTrigGroupId.setStatus("current")
_DocsPnmCmDsOfdmSymRxWindowing_Type = TruthValue
_DocsPnmCmDsOfdmSymRxWindowing_Object = MibTableColumn
docsPnmCmDsOfdmSymRxWindowing = _DocsPnmCmDsOfdmSymRxWindowing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 4),
    _DocsPnmCmDsOfdmSymRxWindowing_Type()
)
docsPnmCmDsOfdmSymRxWindowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymRxWindowing.setStatus("current")


class _DocsPnmCmDsOfdmSymTransactionId_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmSymTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmDsOfdmSymTransactionId_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmSymTransactionId_Object = MibTableColumn
docsPnmCmDsOfdmSymTransactionId = _DocsPnmCmDsOfdmSymTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 5),
    _DocsPnmCmDsOfdmSymTransactionId_Type()
)
docsPnmCmDsOfdmSymTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymTransactionId.setStatus("current")
_DocsPnmCmDsOfdmSymSampleRate_Type = Unsigned32
_DocsPnmCmDsOfdmSymSampleRate_Object = MibTableColumn
docsPnmCmDsOfdmSymSampleRate = _DocsPnmCmDsOfdmSymSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 6),
    _DocsPnmCmDsOfdmSymSampleRate_Type()
)
docsPnmCmDsOfdmSymSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymSampleRate.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymSampleRate.setUnits("Hz")


class _DocsPnmCmDsOfdmSymFftLength_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmSymFftLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
        ValueRangeConstraint(8192, 8192),
    )


_DocsPnmCmDsOfdmSymFftLength_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmSymFftLength_Object = MibTableColumn
docsPnmCmDsOfdmSymFftLength = _DocsPnmCmDsOfdmSymFftLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 7),
    _DocsPnmCmDsOfdmSymFftLength_Type()
)
docsPnmCmDsOfdmSymFftLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymFftLength.setStatus("current")
_DocsPnmCmDsOfdmSymMeasStatus_Type = MeasStatusType
_DocsPnmCmDsOfdmSymMeasStatus_Object = MibTableColumn
docsPnmCmDsOfdmSymMeasStatus = _DocsPnmCmDsOfdmSymMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 8),
    _DocsPnmCmDsOfdmSymMeasStatus_Type()
)
docsPnmCmDsOfdmSymMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymMeasStatus.setStatus("current")
_DocsPnmCmDsOfdmSymCaptFileName_Type = SnmpAdminString
_DocsPnmCmDsOfdmSymCaptFileName_Object = MibTableColumn
docsPnmCmDsOfdmSymCaptFileName = _DocsPnmCmDsOfdmSymCaptFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 2, 1, 9),
    _DocsPnmCmDsOfdmSymCaptFileName_Type()
)
docsPnmCmDsOfdmSymCaptFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmSymCaptFileName.setStatus("current")
_DocsPnmCmOfdmChanEstCoefTable_Object = MibTable
docsPnmCmOfdmChanEstCoefTable = _DocsPnmCmOfdmChanEstCoefTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3)
)
if mibBuilder.loadTexts:
    docsPnmCmOfdmChanEstCoefTable.setStatus("current")
_DocsPnmCmOfdmChanEstCoefEntry_Object = MibTableRow
docsPnmCmOfdmChanEstCoefEntry = _DocsPnmCmOfdmChanEstCoefEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1)
)
docsPnmCmOfdmChanEstCoefEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmOfdmChanEstCoefEntry.setStatus("current")


class _DocsPnmCmOfdmChEstCoefTrigEnable_Type(TruthValue):
    """Custom type docsPnmCmOfdmChEstCoefTrigEnable based on TruthValue"""


_DocsPnmCmOfdmChEstCoefTrigEnable_Object = MibTableColumn
docsPnmCmOfdmChEstCoefTrigEnable = _DocsPnmCmOfdmChEstCoefTrigEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 1),
    _DocsPnmCmOfdmChEstCoefTrigEnable_Type()
)
docsPnmCmOfdmChEstCoefTrigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefTrigEnable.setStatus("current")
_DocsPnmCmOfdmChEstCoefAmpRipplePkToPk_Type = ThousandthdB
_DocsPnmCmOfdmChEstCoefAmpRipplePkToPk_Object = MibTableColumn
docsPnmCmOfdmChEstCoefAmpRipplePkToPk = _DocsPnmCmOfdmChEstCoefAmpRipplePkToPk_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 2),
    _DocsPnmCmOfdmChEstCoefAmpRipplePkToPk_Type()
)
docsPnmCmOfdmChEstCoefAmpRipplePkToPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefAmpRipplePkToPk.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefAmpRipplePkToPk.setUnits("ThousandthdB")
_DocsPnmCmOfdmChEstCoefAmpRippleRms_Type = ThousandthdB
_DocsPnmCmOfdmChEstCoefAmpRippleRms_Object = MibTableColumn
docsPnmCmOfdmChEstCoefAmpRippleRms = _DocsPnmCmOfdmChEstCoefAmpRippleRms_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 3),
    _DocsPnmCmOfdmChEstCoefAmpRippleRms_Type()
)
docsPnmCmOfdmChEstCoefAmpRippleRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefAmpRippleRms.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefAmpRippleRms.setUnits("ThousandthdB")
_DocsPnmCmOfdmChEstCoefAmpSlope_Type = Integer32
_DocsPnmCmOfdmChEstCoefAmpSlope_Object = MibTableColumn
docsPnmCmOfdmChEstCoefAmpSlope = _DocsPnmCmOfdmChEstCoefAmpSlope_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 4),
    _DocsPnmCmOfdmChEstCoefAmpSlope_Type()
)
docsPnmCmOfdmChEstCoefAmpSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefAmpSlope.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefAmpSlope.setUnits("ThousandthdB/MHz")
_DocsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk_Type = Unsigned32
_DocsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk_Object = MibTableColumn
docsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk = _DocsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 5),
    _DocsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk_Type()
)
docsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk.setUnits("ThousandthNsec")
_DocsPnmCmOfdmChEstCoefGrpDelayRippleRms_Type = Unsigned32
_DocsPnmCmOfdmChEstCoefGrpDelayRippleRms_Object = MibTableColumn
docsPnmCmOfdmChEstCoefGrpDelayRippleRms = _DocsPnmCmOfdmChEstCoefGrpDelayRippleRms_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 6),
    _DocsPnmCmOfdmChEstCoefGrpDelayRippleRms_Type()
)
docsPnmCmOfdmChEstCoefGrpDelayRippleRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefGrpDelayRippleRms.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefGrpDelayRippleRms.setUnits("ThousandthNsec")
_DocsPnmCmOfdmChEstCoefMeasStatus_Type = MeasStatusType
_DocsPnmCmOfdmChEstCoefMeasStatus_Object = MibTableColumn
docsPnmCmOfdmChEstCoefMeasStatus = _DocsPnmCmOfdmChEstCoefMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 7),
    _DocsPnmCmOfdmChEstCoefMeasStatus_Type()
)
docsPnmCmOfdmChEstCoefMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefMeasStatus.setStatus("current")
_DocsPnmCmOfdmChEstCoefFileName_Type = SnmpAdminString
_DocsPnmCmOfdmChEstCoefFileName_Object = MibTableColumn
docsPnmCmOfdmChEstCoefFileName = _DocsPnmCmOfdmChEstCoefFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 8),
    _DocsPnmCmOfdmChEstCoefFileName_Type()
)
docsPnmCmOfdmChEstCoefFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefFileName.setStatus("current")
_DocsPnmCmOfdmChEstCoefAmpMean_Type = ThousandthdB
_DocsPnmCmOfdmChEstCoefAmpMean_Object = MibTableColumn
docsPnmCmOfdmChEstCoefAmpMean = _DocsPnmCmOfdmChEstCoefAmpMean_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 9),
    _DocsPnmCmOfdmChEstCoefAmpMean_Type()
)
docsPnmCmOfdmChEstCoefAmpMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefAmpMean.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefAmpMean.setUnits("ThousandthdB")
_DocsPnmCmOfdmChEstCoefGrpDelaySlope_Type = Integer32
_DocsPnmCmOfdmChEstCoefGrpDelaySlope_Object = MibTableColumn
docsPnmCmOfdmChEstCoefGrpDelaySlope = _DocsPnmCmOfdmChEstCoefGrpDelaySlope_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 10),
    _DocsPnmCmOfdmChEstCoefGrpDelaySlope_Type()
)
docsPnmCmOfdmChEstCoefGrpDelaySlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefGrpDelaySlope.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefGrpDelaySlope.setUnits("ThousandthNsec/MHz")
_DocsPnmCmOfdmChEstCoefGrpDelayMean_Type = Integer32
_DocsPnmCmOfdmChEstCoefGrpDelayMean_Object = MibTableColumn
docsPnmCmOfdmChEstCoefGrpDelayMean = _DocsPnmCmOfdmChEstCoefGrpDelayMean_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 3, 1, 11),
    _DocsPnmCmOfdmChEstCoefGrpDelayMean_Type()
)
docsPnmCmOfdmChEstCoefGrpDelayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefGrpDelayMean.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmOfdmChEstCoefGrpDelayMean.setUnits("ThousandthNsec")
_DocsPnmCmDsConstDispMeasTable_Object = MibTable
docsPnmCmDsConstDispMeasTable = _DocsPnmCmDsConstDispMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 4)
)
if mibBuilder.loadTexts:
    docsPnmCmDsConstDispMeasTable.setStatus("current")
_DocsPnmCmDsConstDispMeasEntry_Object = MibTableRow
docsPnmCmDsConstDispMeasEntry = _DocsPnmCmDsConstDispMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 4, 1)
)
docsPnmCmDsConstDispMeasEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmDsConstDispMeasEntry.setStatus("current")


class _DocsPnmCmDsConstDispTrigEnable_Type(TruthValue):
    """Custom type docsPnmCmDsConstDispTrigEnable based on TruthValue"""


_DocsPnmCmDsConstDispTrigEnable_Object = MibTableColumn
docsPnmCmDsConstDispTrigEnable = _DocsPnmCmDsConstDispTrigEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 4, 1, 1),
    _DocsPnmCmDsConstDispTrigEnable_Type()
)
docsPnmCmDsConstDispTrigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsConstDispTrigEnable.setStatus("current")


class _DocsPnmCmDsConstDispModOrderOffset_Type(Unsigned32):
    """Custom type docsPnmCmDsConstDispModOrderOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DocsPnmCmDsConstDispModOrderOffset_Type.__name__ = "Unsigned32"
_DocsPnmCmDsConstDispModOrderOffset_Object = MibTableColumn
docsPnmCmDsConstDispModOrderOffset = _DocsPnmCmDsConstDispModOrderOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 4, 1, 2),
    _DocsPnmCmDsConstDispModOrderOffset_Type()
)
docsPnmCmDsConstDispModOrderOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsConstDispModOrderOffset.setStatus("current")


class _DocsPnmCmDsConstDispNumSampleSymb_Type(Unsigned32):
    """Custom type docsPnmCmDsConstDispNumSampleSymb based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmDsConstDispNumSampleSymb_Type.__name__ = "Unsigned32"
_DocsPnmCmDsConstDispNumSampleSymb_Object = MibTableColumn
docsPnmCmDsConstDispNumSampleSymb = _DocsPnmCmDsConstDispNumSampleSymb_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 4, 1, 3),
    _DocsPnmCmDsConstDispNumSampleSymb_Type()
)
docsPnmCmDsConstDispNumSampleSymb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsConstDispNumSampleSymb.setStatus("current")
_DocsPnmCmDsConstDispSelModOrder_Type = DsOfdmModulationType
_DocsPnmCmDsConstDispSelModOrder_Object = MibTableColumn
docsPnmCmDsConstDispSelModOrder = _DocsPnmCmDsConstDispSelModOrder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 4, 1, 4),
    _DocsPnmCmDsConstDispSelModOrder_Type()
)
docsPnmCmDsConstDispSelModOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsConstDispSelModOrder.setStatus("current")
_DocsPnmCmDsConstDispMeasStatus_Type = MeasStatusType
_DocsPnmCmDsConstDispMeasStatus_Object = MibTableColumn
docsPnmCmDsConstDispMeasStatus = _DocsPnmCmDsConstDispMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 4, 1, 5),
    _DocsPnmCmDsConstDispMeasStatus_Type()
)
docsPnmCmDsConstDispMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsConstDispMeasStatus.setStatus("current")
_DocsPnmCmDsConstDispFileName_Type = SnmpAdminString
_DocsPnmCmDsConstDispFileName_Object = MibTableColumn
docsPnmCmDsConstDispFileName = _DocsPnmCmDsConstDispFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 4, 1, 6),
    _DocsPnmCmDsConstDispFileName_Type()
)
docsPnmCmDsConstDispFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsConstDispFileName.setStatus("current")
_DocsPnmCmDsOfdmRxMerTable_Object = MibTable
docsPnmCmDsOfdmRxMerTable = _DocsPnmCmDsOfdmRxMerTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5)
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerTable.setStatus("current")
_DocsPnmCmDsOfdmRxMerEntry_Object = MibTableRow
docsPnmCmDsOfdmRxMerEntry = _DocsPnmCmDsOfdmRxMerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1)
)
docsPnmCmDsOfdmRxMerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerEntry.setStatus("current")


class _DocsPnmCmDsOfdmRxMerFileEnable_Type(TruthValue):
    """Custom type docsPnmCmDsOfdmRxMerFileEnable based on TruthValue"""


_DocsPnmCmDsOfdmRxMerFileEnable_Object = MibTableColumn
docsPnmCmDsOfdmRxMerFileEnable = _DocsPnmCmDsOfdmRxMerFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1, 1),
    _DocsPnmCmDsOfdmRxMerFileEnable_Type()
)
docsPnmCmDsOfdmRxMerFileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerFileEnable.setStatus("current")


class _DocsPnmCmDsOfdmRxMerPercentile_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmRxMerPercentile based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmDsOfdmRxMerPercentile_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmRxMerPercentile_Object = MibTableColumn
docsPnmCmDsOfdmRxMerPercentile = _DocsPnmCmDsOfdmRxMerPercentile_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1, 2),
    _DocsPnmCmDsOfdmRxMerPercentile_Type()
)
docsPnmCmDsOfdmRxMerPercentile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerPercentile.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerPercentile.setUnits("percent")


class _DocsPnmCmDsOfdmRxMerMean_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmRxMerMean based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmDsOfdmRxMerMean_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmRxMerMean_Object = MibTableColumn
docsPnmCmDsOfdmRxMerMean = _DocsPnmCmDsOfdmRxMerMean_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1, 3),
    _DocsPnmCmDsOfdmRxMerMean_Type()
)
docsPnmCmDsOfdmRxMerMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerMean.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerMean.setUnits("hundredthDb")


class _DocsPnmCmDsOfdmRxMerStdDev_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmRxMerStdDev based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmDsOfdmRxMerStdDev_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmRxMerStdDev_Object = MibTableColumn
docsPnmCmDsOfdmRxMerStdDev = _DocsPnmCmDsOfdmRxMerStdDev_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1, 4),
    _DocsPnmCmDsOfdmRxMerStdDev_Type()
)
docsPnmCmDsOfdmRxMerStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerStdDev.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerStdDev.setUnits("hundredthDb")


class _DocsPnmCmDsOfdmRxMerThrVal_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmRxMerThrVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmDsOfdmRxMerThrVal_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmRxMerThrVal_Object = MibTableColumn
docsPnmCmDsOfdmRxMerThrVal = _DocsPnmCmDsOfdmRxMerThrVal_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1, 5),
    _DocsPnmCmDsOfdmRxMerThrVal_Type()
)
docsPnmCmDsOfdmRxMerThrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerThrVal.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerThrVal.setUnits("quarterDb")
_DocsPnmCmDsOfdmRxMerThrHighestFreq_Type = Unsigned32
_DocsPnmCmDsOfdmRxMerThrHighestFreq_Object = MibTableColumn
docsPnmCmDsOfdmRxMerThrHighestFreq = _DocsPnmCmDsOfdmRxMerThrHighestFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1, 6),
    _DocsPnmCmDsOfdmRxMerThrHighestFreq_Type()
)
docsPnmCmDsOfdmRxMerThrHighestFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerThrHighestFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerThrHighestFreq.setUnits("Hz")
_DocsPnmCmDsOfdmRxMerMeasStatus_Type = MeasStatusType
_DocsPnmCmDsOfdmRxMerMeasStatus_Object = MibTableColumn
docsPnmCmDsOfdmRxMerMeasStatus = _DocsPnmCmDsOfdmRxMerMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1, 7),
    _DocsPnmCmDsOfdmRxMerMeasStatus_Type()
)
docsPnmCmDsOfdmRxMerMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerMeasStatus.setStatus("current")
_DocsPnmCmDsOfdmRxMerFileName_Type = SnmpAdminString
_DocsPnmCmDsOfdmRxMerFileName_Object = MibTableColumn
docsPnmCmDsOfdmRxMerFileName = _DocsPnmCmDsOfdmRxMerFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 5, 1, 8),
    _DocsPnmCmDsOfdmRxMerFileName_Type()
)
docsPnmCmDsOfdmRxMerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmRxMerFileName.setStatus("current")
_DocsPnmCmDsOfdmMerMarTable_Object = MibTable
docsPnmCmDsOfdmMerMarTable = _DocsPnmCmDsOfdmMerMarTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6)
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarTable.setStatus("current")
_DocsPnmCmDsOfdmMerMarEntry_Object = MibTableRow
docsPnmCmDsOfdmMerMarEntry = _DocsPnmCmDsOfdmMerMarEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1)
)
docsPnmCmDsOfdmMerMarEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarEntry.setStatus("current")


class _DocsPnmCmDsOfdmMerMarProfileId_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmMerMarProfileId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsPnmCmDsOfdmMerMarProfileId_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmMerMarProfileId_Object = MibTableColumn
docsPnmCmDsOfdmMerMarProfileId = _DocsPnmCmDsOfdmMerMarProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 1),
    _DocsPnmCmDsOfdmMerMarProfileId_Type()
)
docsPnmCmDsOfdmMerMarProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarProfileId.setStatus("current")


class _DocsPnmCmDsOfdmMerMarThrshldOffset_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmMerMarThrshldOffset based on Unsigned32"""
    defaultValue = 0


_DocsPnmCmDsOfdmMerMarThrshldOffset_Object = MibTableColumn
docsPnmCmDsOfdmMerMarThrshldOffset = _DocsPnmCmDsOfdmMerMarThrshldOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 2),
    _DocsPnmCmDsOfdmMerMarThrshldOffset_Type()
)
docsPnmCmDsOfdmMerMarThrshldOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarThrshldOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarThrshldOffset.setUnits("quarterDb")


class _DocsPnmCmDsOfdmMerMarMeasEnable_Type(TruthValue):
    """Custom type docsPnmCmDsOfdmMerMarMeasEnable based on TruthValue"""


_DocsPnmCmDsOfdmMerMarMeasEnable_Object = MibTableColumn
docsPnmCmDsOfdmMerMarMeasEnable = _DocsPnmCmDsOfdmMerMarMeasEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 3),
    _DocsPnmCmDsOfdmMerMarMeasEnable_Type()
)
docsPnmCmDsOfdmMerMarMeasEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarMeasEnable.setStatus("current")


class _DocsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg_Object = MibTableColumn
docsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg = _DocsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 4),
    _DocsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg_Type()
)
docsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg.setStatus("current")


class _DocsPnmCmDsOfdmMerMarReqAvgMer_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmMerMarReqAvgMer based on Unsigned32"""
    defaultValue = 0


_DocsPnmCmDsOfdmMerMarReqAvgMer_Object = MibTableColumn
docsPnmCmDsOfdmMerMarReqAvgMer = _DocsPnmCmDsOfdmMerMarReqAvgMer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 5),
    _DocsPnmCmDsOfdmMerMarReqAvgMer_Type()
)
docsPnmCmDsOfdmMerMarReqAvgMer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarReqAvgMer.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarReqAvgMer.setUnits("quarterDb")


class _DocsPnmCmDsOfdmMerMarNumSubCarBelowThrshld_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmMerMarNumSubCarBelowThrshld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmDsOfdmMerMarNumSubCarBelowThrshld_Type.__name__ = "Unsigned32"
_DocsPnmCmDsOfdmMerMarNumSubCarBelowThrshld_Object = MibTableColumn
docsPnmCmDsOfdmMerMarNumSubCarBelowThrshld = _DocsPnmCmDsOfdmMerMarNumSubCarBelowThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 6),
    _DocsPnmCmDsOfdmMerMarNumSubCarBelowThrshld_Type()
)
docsPnmCmDsOfdmMerMarNumSubCarBelowThrshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarNumSubCarBelowThrshld.setStatus("current")
_DocsPnmCmDsOfdmMerMarMeasuredAvgMer_Type = Unsigned32
_DocsPnmCmDsOfdmMerMarMeasuredAvgMer_Object = MibTableColumn
docsPnmCmDsOfdmMerMarMeasuredAvgMer = _DocsPnmCmDsOfdmMerMarMeasuredAvgMer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 7),
    _DocsPnmCmDsOfdmMerMarMeasuredAvgMer_Type()
)
docsPnmCmDsOfdmMerMarMeasuredAvgMer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarMeasuredAvgMer.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarMeasuredAvgMer.setUnits("hundrethdB")
_DocsPnmCmDsOfdmMerMarAvgMerMargin_Type = Unsigned32
_DocsPnmCmDsOfdmMerMarAvgMerMargin_Object = MibTableColumn
docsPnmCmDsOfdmMerMarAvgMerMargin = _DocsPnmCmDsOfdmMerMarAvgMerMargin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 8),
    _DocsPnmCmDsOfdmMerMarAvgMerMargin_Type()
)
docsPnmCmDsOfdmMerMarAvgMerMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarAvgMerMargin.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarAvgMerMargin.setUnits("hundrethdB")
_DocsPnmCmDsOfdmMerMarMeasStatus_Type = MeasStatusType
_DocsPnmCmDsOfdmMerMarMeasStatus_Object = MibTableColumn
docsPnmCmDsOfdmMerMarMeasStatus = _DocsPnmCmDsOfdmMerMarMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 6, 1, 9),
    _DocsPnmCmDsOfdmMerMarMeasStatus_Type()
)
docsPnmCmDsOfdmMerMarMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmMerMarMeasStatus.setStatus("current")
_DocsPnmCmDsOfdmFecTable_Object = MibTable
docsPnmCmDsOfdmFecTable = _DocsPnmCmDsOfdmFecTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 7)
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmFecTable.setStatus("current")
_DocsPnmCmDsOfdmFecEntry_Object = MibTableRow
docsPnmCmDsOfdmFecEntry = _DocsPnmCmDsOfdmFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 7, 1)
)
docsPnmCmDsOfdmFecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmFecEntry.setStatus("current")


class _DocsPnmCmDsOfdmFecSumType_Type(Integer32):
    """Custom type docsPnmCmDsOfdmFecSumType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interval10min", 2),
          ("interval24hr", 3),
          ("other", 1))
    )


_DocsPnmCmDsOfdmFecSumType_Type.__name__ = "Integer32"
_DocsPnmCmDsOfdmFecSumType_Object = MibTableColumn
docsPnmCmDsOfdmFecSumType = _DocsPnmCmDsOfdmFecSumType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 7, 1, 1),
    _DocsPnmCmDsOfdmFecSumType_Type()
)
docsPnmCmDsOfdmFecSumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmFecSumType.setStatus("current")


class _DocsPnmCmDsOfdmFecFileEnable_Type(TruthValue):
    """Custom type docsPnmCmDsOfdmFecFileEnable based on TruthValue"""


_DocsPnmCmDsOfdmFecFileEnable_Object = MibTableColumn
docsPnmCmDsOfdmFecFileEnable = _DocsPnmCmDsOfdmFecFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 7, 1, 2),
    _DocsPnmCmDsOfdmFecFileEnable_Type()
)
docsPnmCmDsOfdmFecFileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmFecFileEnable.setStatus("current")
_DocsPnmCmDsOfdmFecMeasStatus_Type = MeasStatusType
_DocsPnmCmDsOfdmFecMeasStatus_Object = MibTableColumn
docsPnmCmDsOfdmFecMeasStatus = _DocsPnmCmDsOfdmFecMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 7, 1, 3),
    _DocsPnmCmDsOfdmFecMeasStatus_Type()
)
docsPnmCmDsOfdmFecMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmFecMeasStatus.setStatus("current")
_DocsPnmCmDsOfdmFecFileName_Type = SnmpAdminString
_DocsPnmCmDsOfdmFecFileName_Object = MibTableColumn
docsPnmCmDsOfdmFecFileName = _DocsPnmCmDsOfdmFecFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 7, 1, 4),
    _DocsPnmCmDsOfdmFecFileName_Type()
)
docsPnmCmDsOfdmFecFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmFecFileName.setStatus("current")
_DocsPnmCmDsOfdmReqMERObjects_ObjectIdentity = ObjectIdentity
docsPnmCmDsOfdmReqMERObjects = _DocsPnmCmDsOfdmReqMERObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8)
)


class _DocsPnmCmDsOfdmReqMerQam16_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam16 based on Unsigned32"""
    defaultValue = 60


_DocsPnmCmDsOfdmReqMerQam16_Object = MibScalar
docsPnmCmDsOfdmReqMerQam16 = _DocsPnmCmDsOfdmReqMerQam16_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 1),
    _DocsPnmCmDsOfdmReqMerQam16_Type()
)
docsPnmCmDsOfdmReqMerQam16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam16.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam16.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam64_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam64 based on Unsigned32"""
    defaultValue = 84


_DocsPnmCmDsOfdmReqMerQam64_Object = MibScalar
docsPnmCmDsOfdmReqMerQam64 = _DocsPnmCmDsOfdmReqMerQam64_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 2),
    _DocsPnmCmDsOfdmReqMerQam64_Type()
)
docsPnmCmDsOfdmReqMerQam64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam64.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam64.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam128_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam128 based on Unsigned32"""
    defaultValue = 96


_DocsPnmCmDsOfdmReqMerQam128_Object = MibScalar
docsPnmCmDsOfdmReqMerQam128 = _DocsPnmCmDsOfdmReqMerQam128_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 3),
    _DocsPnmCmDsOfdmReqMerQam128_Type()
)
docsPnmCmDsOfdmReqMerQam128.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam128.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam128.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam256_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam256 based on Unsigned32"""
    defaultValue = 108


_DocsPnmCmDsOfdmReqMerQam256_Object = MibScalar
docsPnmCmDsOfdmReqMerQam256 = _DocsPnmCmDsOfdmReqMerQam256_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 4),
    _DocsPnmCmDsOfdmReqMerQam256_Type()
)
docsPnmCmDsOfdmReqMerQam256.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam256.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam256.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam512_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam512 based on Unsigned32"""
    defaultValue = 122


_DocsPnmCmDsOfdmReqMerQam512_Object = MibScalar
docsPnmCmDsOfdmReqMerQam512 = _DocsPnmCmDsOfdmReqMerQam512_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 5),
    _DocsPnmCmDsOfdmReqMerQam512_Type()
)
docsPnmCmDsOfdmReqMerQam512.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam512.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam512.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam1024_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam1024 based on Unsigned32"""
    defaultValue = 136


_DocsPnmCmDsOfdmReqMerQam1024_Object = MibScalar
docsPnmCmDsOfdmReqMerQam1024 = _DocsPnmCmDsOfdmReqMerQam1024_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 6),
    _DocsPnmCmDsOfdmReqMerQam1024_Type()
)
docsPnmCmDsOfdmReqMerQam1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam1024.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam1024.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam2048_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam2048 based on Unsigned32"""
    defaultValue = 148


_DocsPnmCmDsOfdmReqMerQam2048_Object = MibScalar
docsPnmCmDsOfdmReqMerQam2048 = _DocsPnmCmDsOfdmReqMerQam2048_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 7),
    _DocsPnmCmDsOfdmReqMerQam2048_Type()
)
docsPnmCmDsOfdmReqMerQam2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam2048.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam2048.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam4096_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam4096 based on Unsigned32"""
    defaultValue = 164


_DocsPnmCmDsOfdmReqMerQam4096_Object = MibScalar
docsPnmCmDsOfdmReqMerQam4096 = _DocsPnmCmDsOfdmReqMerQam4096_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 8),
    _DocsPnmCmDsOfdmReqMerQam4096_Type()
)
docsPnmCmDsOfdmReqMerQam4096.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam4096.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam4096.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam8192_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam8192 based on Unsigned32"""
    defaultValue = 184


_DocsPnmCmDsOfdmReqMerQam8192_Object = MibScalar
docsPnmCmDsOfdmReqMerQam8192 = _DocsPnmCmDsOfdmReqMerQam8192_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 9),
    _DocsPnmCmDsOfdmReqMerQam8192_Type()
)
docsPnmCmDsOfdmReqMerQam8192.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam8192.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam8192.setUnits("quarterdB")


class _DocsPnmCmDsOfdmReqMerQam16384_Type(Unsigned32):
    """Custom type docsPnmCmDsOfdmReqMerQam16384 based on Unsigned32"""
    defaultValue = 208


_DocsPnmCmDsOfdmReqMerQam16384_Object = MibScalar
docsPnmCmDsOfdmReqMerQam16384 = _DocsPnmCmDsOfdmReqMerQam16384_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 8, 10),
    _DocsPnmCmDsOfdmReqMerQam16384_Type()
)
docsPnmCmDsOfdmReqMerQam16384.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam16384.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmReqMerQam16384.setUnits("quarterdB")
_DocsPnmCmDsHistTable_Object = MibTable
docsPnmCmDsHistTable = _DocsPnmCmDsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 9)
)
if mibBuilder.loadTexts:
    docsPnmCmDsHistTable.setStatus("current")
_DocsPnmCmDsHistEntry_Object = MibTableRow
docsPnmCmDsHistEntry = _DocsPnmCmDsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 9, 1)
)
docsPnmCmDsHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmDsHistEntry.setStatus("current")


class _DocsPnmCmDsHistEnable_Type(TruthValue):
    """Custom type docsPnmCmDsHistEnable based on TruthValue"""


_DocsPnmCmDsHistEnable_Object = MibTableColumn
docsPnmCmDsHistEnable = _DocsPnmCmDsHistEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 9, 1, 1),
    _DocsPnmCmDsHistEnable_Type()
)
docsPnmCmDsHistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsHistEnable.setStatus("current")


class _DocsPnmCmDsHistTimeOut_Type(Unsigned32):
    """Custom type docsPnmCmDsHistTimeOut based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmDsHistTimeOut_Type.__name__ = "Unsigned32"
_DocsPnmCmDsHistTimeOut_Object = MibTableColumn
docsPnmCmDsHistTimeOut = _DocsPnmCmDsHistTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 9, 1, 2),
    _DocsPnmCmDsHistTimeOut_Type()
)
docsPnmCmDsHistTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsHistTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmDsHistTimeOut.setUnits("seconds")
_DocsPnmCmDsHistMeasStatus_Type = MeasStatusType
_DocsPnmCmDsHistMeasStatus_Object = MibTableColumn
docsPnmCmDsHistMeasStatus = _DocsPnmCmDsHistMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 9, 1, 3),
    _DocsPnmCmDsHistMeasStatus_Type()
)
docsPnmCmDsHistMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsHistMeasStatus.setStatus("current")
_DocsPnmCmDsHistFileName_Type = SnmpAdminString
_DocsPnmCmDsHistFileName_Object = MibTableColumn
docsPnmCmDsHistFileName = _DocsPnmCmDsHistFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 9, 1, 4),
    _DocsPnmCmDsHistFileName_Type()
)
docsPnmCmDsHistFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsHistFileName.setStatus("current")
_DocsPnmCmUsPreEqTable_Object = MibTable
docsPnmCmUsPreEqTable = _DocsPnmCmUsPreEqTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10)
)
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqTable.setStatus("current")
_DocsPnmCmUsPreEqEntry_Object = MibTableRow
docsPnmCmUsPreEqEntry = _DocsPnmCmUsPreEqEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1)
)
docsPnmCmUsPreEqEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqEntry.setStatus("current")


class _DocsPnmCmUsPreEqFileEnable_Type(TruthValue):
    """Custom type docsPnmCmUsPreEqFileEnable based on TruthValue"""


_DocsPnmCmUsPreEqFileEnable_Object = MibTableColumn
docsPnmCmUsPreEqFileEnable = _DocsPnmCmUsPreEqFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 1),
    _DocsPnmCmUsPreEqFileEnable_Type()
)
docsPnmCmUsPreEqFileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqFileEnable.setStatus("current")
_DocsPnmCmUsPreEqAmpRipplePkToPk_Type = ThousandthdB
_DocsPnmCmUsPreEqAmpRipplePkToPk_Object = MibTableColumn
docsPnmCmUsPreEqAmpRipplePkToPk = _DocsPnmCmUsPreEqAmpRipplePkToPk_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 2),
    _DocsPnmCmUsPreEqAmpRipplePkToPk_Type()
)
docsPnmCmUsPreEqAmpRipplePkToPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqAmpRipplePkToPk.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqAmpRipplePkToPk.setUnits("ThousandthdB")
_DocsPnmCmUsPreEqAmpRippleRms_Type = ThousandthdB
_DocsPnmCmUsPreEqAmpRippleRms_Object = MibTableColumn
docsPnmCmUsPreEqAmpRippleRms = _DocsPnmCmUsPreEqAmpRippleRms_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 3),
    _DocsPnmCmUsPreEqAmpRippleRms_Type()
)
docsPnmCmUsPreEqAmpRippleRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqAmpRippleRms.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqAmpRippleRms.setUnits("ThousandthdB")
_DocsPnmCmUsPreEqAmpSlope_Type = Integer32
_DocsPnmCmUsPreEqAmpSlope_Object = MibTableColumn
docsPnmCmUsPreEqAmpSlope = _DocsPnmCmUsPreEqAmpSlope_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 4),
    _DocsPnmCmUsPreEqAmpSlope_Type()
)
docsPnmCmUsPreEqAmpSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqAmpSlope.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqAmpSlope.setUnits("ThousandthdB/MHz")
_DocsPnmCmUsPreEqGrpDelayRipplePkToPk_Type = Unsigned32
_DocsPnmCmUsPreEqGrpDelayRipplePkToPk_Object = MibTableColumn
docsPnmCmUsPreEqGrpDelayRipplePkToPk = _DocsPnmCmUsPreEqGrpDelayRipplePkToPk_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 5),
    _DocsPnmCmUsPreEqGrpDelayRipplePkToPk_Type()
)
docsPnmCmUsPreEqGrpDelayRipplePkToPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqGrpDelayRipplePkToPk.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqGrpDelayRipplePkToPk.setUnits("nsec")
_DocsPnmCmUsPreEqGrpDelayRippleRms_Type = Unsigned32
_DocsPnmCmUsPreEqGrpDelayRippleRms_Object = MibTableColumn
docsPnmCmUsPreEqGrpDelayRippleRms = _DocsPnmCmUsPreEqGrpDelayRippleRms_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 6),
    _DocsPnmCmUsPreEqGrpDelayRippleRms_Type()
)
docsPnmCmUsPreEqGrpDelayRippleRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqGrpDelayRippleRms.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqGrpDelayRippleRms.setUnits("nsec")


class _DocsPnmCmUsPreEqPreEqCoAdjStatus_Type(Integer32):
    """Custom type docsPnmCmUsPreEqPreEqCoAdjStatus based on Integer32"""
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
        *(("clipped", 3),
          ("other", 1),
          ("rejected", 4),
          ("success", 2))
    )


_DocsPnmCmUsPreEqPreEqCoAdjStatus_Type.__name__ = "Integer32"
_DocsPnmCmUsPreEqPreEqCoAdjStatus_Object = MibTableColumn
docsPnmCmUsPreEqPreEqCoAdjStatus = _DocsPnmCmUsPreEqPreEqCoAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 7),
    _DocsPnmCmUsPreEqPreEqCoAdjStatus_Type()
)
docsPnmCmUsPreEqPreEqCoAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqPreEqCoAdjStatus.setStatus("current")
_DocsPnmCmUsPreEqMeasStatus_Type = MeasStatusType
_DocsPnmCmUsPreEqMeasStatus_Object = MibTableColumn
docsPnmCmUsPreEqMeasStatus = _DocsPnmCmUsPreEqMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 8),
    _DocsPnmCmUsPreEqMeasStatus_Type()
)
docsPnmCmUsPreEqMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqMeasStatus.setStatus("current")
_DocsPnmCmUsPreEqLastUpdateFileName_Type = SnmpAdminString
_DocsPnmCmUsPreEqLastUpdateFileName_Object = MibTableColumn
docsPnmCmUsPreEqLastUpdateFileName = _DocsPnmCmUsPreEqLastUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 9),
    _DocsPnmCmUsPreEqLastUpdateFileName_Type()
)
docsPnmCmUsPreEqLastUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqLastUpdateFileName.setStatus("current")
_DocsPnmCmUsPreEqFileName_Type = SnmpAdminString
_DocsPnmCmUsPreEqFileName_Object = MibTableColumn
docsPnmCmUsPreEqFileName = _DocsPnmCmUsPreEqFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 10),
    _DocsPnmCmUsPreEqFileName_Type()
)
docsPnmCmUsPreEqFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqFileName.setStatus("current")
_DocsPnmCmUsPreEqAmpMean_Type = ThousandthdB
_DocsPnmCmUsPreEqAmpMean_Object = MibTableColumn
docsPnmCmUsPreEqAmpMean = _DocsPnmCmUsPreEqAmpMean_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 11),
    _DocsPnmCmUsPreEqAmpMean_Type()
)
docsPnmCmUsPreEqAmpMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqAmpMean.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqAmpMean.setUnits("ThousandthdB")
_DocsPnmCmUsPreEqGrpDelaySlope_Type = Integer32
_DocsPnmCmUsPreEqGrpDelaySlope_Object = MibTableColumn
docsPnmCmUsPreEqGrpDelaySlope = _DocsPnmCmUsPreEqGrpDelaySlope_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 12),
    _DocsPnmCmUsPreEqGrpDelaySlope_Type()
)
docsPnmCmUsPreEqGrpDelaySlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqGrpDelaySlope.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqGrpDelaySlope.setUnits("ThousandthNsec/MHz")
_DocsPnmCmUsPreEqGrpDelayMean_Type = Integer32
_DocsPnmCmUsPreEqGrpDelayMean_Object = MibTableColumn
docsPnmCmUsPreEqGrpDelayMean = _DocsPnmCmUsPreEqGrpDelayMean_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 10, 1, 13),
    _DocsPnmCmUsPreEqGrpDelayMean_Type()
)
docsPnmCmUsPreEqGrpDelayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqGrpDelayMean.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmUsPreEqGrpDelayMean.setUnits("ThousandthNsec")
_DocsPnmCmDsOfdmModProfTable_Object = MibTable
docsPnmCmDsOfdmModProfTable = _DocsPnmCmDsOfdmModProfTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 11)
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmModProfTable.setStatus("current")
_DocsPnmCmDsOfdmModProfEntry_Object = MibTableRow
docsPnmCmDsOfdmModProfEntry = _DocsPnmCmDsOfdmModProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 11, 1)
)
docsPnmCmDsOfdmModProfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmModProfEntry.setStatus("current")


class _DocsPnmCmDsOfdmModProfFileEnable_Type(TruthValue):
    """Custom type docsPnmCmDsOfdmModProfFileEnable based on TruthValue"""


_DocsPnmCmDsOfdmModProfFileEnable_Object = MibTableColumn
docsPnmCmDsOfdmModProfFileEnable = _DocsPnmCmDsOfdmModProfFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 11, 1, 1),
    _DocsPnmCmDsOfdmModProfFileEnable_Type()
)
docsPnmCmDsOfdmModProfFileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmModProfFileEnable.setStatus("current")
_DocsPnmCmDsOfdmModProfMeasStatus_Type = MeasStatusType
_DocsPnmCmDsOfdmModProfMeasStatus_Object = MibTableColumn
docsPnmCmDsOfdmModProfMeasStatus = _DocsPnmCmDsOfdmModProfMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 11, 1, 2),
    _DocsPnmCmDsOfdmModProfMeasStatus_Type()
)
docsPnmCmDsOfdmModProfMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmModProfMeasStatus.setStatus("current")
_DocsPnmCmDsOfdmModProfFileName_Type = SnmpAdminString
_DocsPnmCmDsOfdmModProfFileName_Object = MibTableColumn
docsPnmCmDsOfdmModProfFileName = _DocsPnmCmDsOfdmModProfFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 2, 11, 1, 3),
    _DocsPnmCmDsOfdmModProfFileName_Type()
)
docsPnmCmDsOfdmModProfFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmDsOfdmModProfFileName.setStatus("current")
_DocsPnmCmtsObjects_ObjectIdentity = ObjectIdentity
docsPnmCmtsObjects = _DocsPnmCmtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3)
)
_DocsPnmCmtsDsOfdmSymCapTable_Object = MibTable
docsPnmCmtsDsOfdmSymCapTable = _DocsPnmCmtsDsOfdmSymCapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1)
)
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymCapTable.setStatus("current")
_DocsPnmCmtsDsOfdmSymCapEntry_Object = MibTableRow
docsPnmCmtsDsOfdmSymCapEntry = _DocsPnmCmtsDsOfdmSymCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1)
)
docsPnmCmtsDsOfdmSymCapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymCapEntry.setStatus("current")


class _DocsPnmCmtsDsOfdmSymTrigEnable_Type(TruthValue):
    """Custom type docsPnmCmtsDsOfdmSymTrigEnable based on TruthValue"""


_DocsPnmCmtsDsOfdmSymTrigEnable_Object = MibTableColumn
docsPnmCmtsDsOfdmSymTrigEnable = _DocsPnmCmtsDsOfdmSymTrigEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 1),
    _DocsPnmCmtsDsOfdmSymTrigEnable_Type()
)
docsPnmCmtsDsOfdmSymTrigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymTrigEnable.setStatus("current")


class _DocsPnmCmtsDsOfdmSymTrigGroupId_Type(Unsigned32):
    """Custom type docsPnmCmtsDsOfdmSymTrigGroupId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsDsOfdmSymTrigGroupId_Type.__name__ = "Unsigned32"
_DocsPnmCmtsDsOfdmSymTrigGroupId_Object = MibTableColumn
docsPnmCmtsDsOfdmSymTrigGroupId = _DocsPnmCmtsDsOfdmSymTrigGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 2),
    _DocsPnmCmtsDsOfdmSymTrigGroupId_Type()
)
docsPnmCmtsDsOfdmSymTrigGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymTrigGroupId.setStatus("current")


class _DocsPnmCmtsDsOfdmSymFirstActSubCarIdx_Type(Unsigned32):
    """Custom type docsPnmCmtsDsOfdmSymFirstActSubCarIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsDsOfdmSymFirstActSubCarIdx_Type.__name__ = "Unsigned32"
_DocsPnmCmtsDsOfdmSymFirstActSubCarIdx_Object = MibTableColumn
docsPnmCmtsDsOfdmSymFirstActSubCarIdx = _DocsPnmCmtsDsOfdmSymFirstActSubCarIdx_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 3),
    _DocsPnmCmtsDsOfdmSymFirstActSubCarIdx_Type()
)
docsPnmCmtsDsOfdmSymFirstActSubCarIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymFirstActSubCarIdx.setStatus("current")


class _DocsPnmCmtsDsOfdmSymLastActSubCarIdx_Type(Unsigned32):
    """Custom type docsPnmCmtsDsOfdmSymLastActSubCarIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsDsOfdmSymLastActSubCarIdx_Type.__name__ = "Unsigned32"
_DocsPnmCmtsDsOfdmSymLastActSubCarIdx_Object = MibTableColumn
docsPnmCmtsDsOfdmSymLastActSubCarIdx = _DocsPnmCmtsDsOfdmSymLastActSubCarIdx_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 4),
    _DocsPnmCmtsDsOfdmSymLastActSubCarIdx_Type()
)
docsPnmCmtsDsOfdmSymLastActSubCarIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymLastActSubCarIdx.setStatus("current")
_DocsPnmCmtsDsOfdmSymRxWindowing_Type = TruthValue
_DocsPnmCmtsDsOfdmSymRxWindowing_Object = MibTableColumn
docsPnmCmtsDsOfdmSymRxWindowing = _DocsPnmCmtsDsOfdmSymRxWindowing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 5),
    _DocsPnmCmtsDsOfdmSymRxWindowing_Type()
)
docsPnmCmtsDsOfdmSymRxWindowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymRxWindowing.setStatus("current")


class _DocsPnmCmtsDsOfdmSymTransactionId_Type(Unsigned32):
    """Custom type docsPnmCmtsDsOfdmSymTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmtsDsOfdmSymTransactionId_Type.__name__ = "Unsigned32"
_DocsPnmCmtsDsOfdmSymTransactionId_Object = MibTableColumn
docsPnmCmtsDsOfdmSymTransactionId = _DocsPnmCmtsDsOfdmSymTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 6),
    _DocsPnmCmtsDsOfdmSymTransactionId_Type()
)
docsPnmCmtsDsOfdmSymTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymTransactionId.setStatus("current")
_DocsPnmCmtsDsOfdmSymSampleRate_Type = Unsigned32
_DocsPnmCmtsDsOfdmSymSampleRate_Object = MibTableColumn
docsPnmCmtsDsOfdmSymSampleRate = _DocsPnmCmtsDsOfdmSymSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 7),
    _DocsPnmCmtsDsOfdmSymSampleRate_Type()
)
docsPnmCmtsDsOfdmSymSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymSampleRate.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymSampleRate.setUnits("Hz")


class _DocsPnmCmtsDsOfdmSymFftLength_Type(Unsigned32):
    """Custom type docsPnmCmtsDsOfdmSymFftLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
        ValueRangeConstraint(8192, 8192),
    )


_DocsPnmCmtsDsOfdmSymFftLength_Type.__name__ = "Unsigned32"
_DocsPnmCmtsDsOfdmSymFftLength_Object = MibTableColumn
docsPnmCmtsDsOfdmSymFftLength = _DocsPnmCmtsDsOfdmSymFftLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 8),
    _DocsPnmCmtsDsOfdmSymFftLength_Type()
)
docsPnmCmtsDsOfdmSymFftLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymFftLength.setStatus("current")
_DocsPnmCmtsDsOfdmSymMeasStatus_Type = MeasStatusType
_DocsPnmCmtsDsOfdmSymMeasStatus_Object = MibTableColumn
docsPnmCmtsDsOfdmSymMeasStatus = _DocsPnmCmtsDsOfdmSymMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 9),
    _DocsPnmCmtsDsOfdmSymMeasStatus_Type()
)
docsPnmCmtsDsOfdmSymMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymMeasStatus.setStatus("current")
_DocsPnmCmtsDsOfdmSymCaptFileName_Type = SnmpAdminString
_DocsPnmCmtsDsOfdmSymCaptFileName_Object = MibTableColumn
docsPnmCmtsDsOfdmSymCaptFileName = _DocsPnmCmtsDsOfdmSymCaptFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 1, 1, 10),
    _DocsPnmCmtsDsOfdmSymCaptFileName_Type()
)
docsPnmCmtsDsOfdmSymCaptFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmSymCaptFileName.setStatus("current")
_DocsPnmCmtsDsOfdmNoisePwrRatioTable_Object = MibTable
docsPnmCmtsDsOfdmNoisePwrRatioTable = _DocsPnmCmtsDsOfdmNoisePwrRatioTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 2)
)
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmNoisePwrRatioTable.setStatus("current")
_DocsPnmCmtsDsOfdmNoisePwrRatioEntry_Object = MibTableRow
docsPnmCmtsDsOfdmNoisePwrRatioEntry = _DocsPnmCmtsDsOfdmNoisePwrRatioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 2, 1)
)
docsPnmCmtsDsOfdmNoisePwrRatioEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmNoisePwrRatioEntry.setStatus("current")


class _DocsPnmCmtsDsOfdmNprStartSubcar_Type(Unsigned32):
    """Custom type docsPnmCmtsDsOfdmNprStartSubcar based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_DocsPnmCmtsDsOfdmNprStartSubcar_Type.__name__ = "Unsigned32"
_DocsPnmCmtsDsOfdmNprStartSubcar_Object = MibTableColumn
docsPnmCmtsDsOfdmNprStartSubcar = _DocsPnmCmtsDsOfdmNprStartSubcar_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 2, 1, 1),
    _DocsPnmCmtsDsOfdmNprStartSubcar_Type()
)
docsPnmCmtsDsOfdmNprStartSubcar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmNprStartSubcar.setStatus("current")


class _DocsPnmCmtsDsOfdmNprStopSubcar_Type(Unsigned32):
    """Custom type docsPnmCmtsDsOfdmNprStopSubcar based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_DocsPnmCmtsDsOfdmNprStopSubcar_Type.__name__ = "Unsigned32"
_DocsPnmCmtsDsOfdmNprStopSubcar_Object = MibTableColumn
docsPnmCmtsDsOfdmNprStopSubcar = _DocsPnmCmtsDsOfdmNprStopSubcar_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 2, 1, 2),
    _DocsPnmCmtsDsOfdmNprStopSubcar_Type()
)
docsPnmCmtsDsOfdmNprStopSubcar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmNprStopSubcar.setStatus("current")


class _DocsPnmCmtsDsOfdmNprEnable_Type(TruthValue):
    """Custom type docsPnmCmtsDsOfdmNprEnable based on TruthValue"""


_DocsPnmCmtsDsOfdmNprEnable_Object = MibTableColumn
docsPnmCmtsDsOfdmNprEnable = _DocsPnmCmtsDsOfdmNprEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 2, 1, 3),
    _DocsPnmCmtsDsOfdmNprEnable_Type()
)
docsPnmCmtsDsOfdmNprEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmNprEnable.setStatus("current")


class _DocsPnmCmtsDsOfdmNprDuration_Type(Unsigned32):
    """Custom type docsPnmCmtsDsOfdmNprDuration based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsDsOfdmNprDuration_Type.__name__ = "Unsigned32"
_DocsPnmCmtsDsOfdmNprDuration_Object = MibTableColumn
docsPnmCmtsDsOfdmNprDuration = _DocsPnmCmtsDsOfdmNprDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 2, 1, 4),
    _DocsPnmCmtsDsOfdmNprDuration_Type()
)
docsPnmCmtsDsOfdmNprDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmNprDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsDsOfdmNprDuration.setUnits("seconds")
_DocsPnmCmtsUsOfdmaAQProbeTable_Object = MibTable
docsPnmCmtsUsOfdmaAQProbeTable = _DocsPnmCmtsUsOfdmaAQProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeTable.setStatus("current")
_DocsPnmCmtsUsOfdmaAQProbeEntry_Object = MibTableRow
docsPnmCmtsUsOfdmaAQProbeEntry = _DocsPnmCmtsUsOfdmaAQProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1)
)
docsPnmCmtsUsOfdmaAQProbeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeEntry.setStatus("current")


class _DocsPnmCmtsUsOfdmaAQProbeCmMacAddr_Type(MacAddress):
    """Custom type docsPnmCmtsUsOfdmaAQProbeCmMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsPnmCmtsUsOfdmaAQProbeCmMacAddr_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeCmMacAddr = _DocsPnmCmtsUsOfdmaAQProbeCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 1),
    _DocsPnmCmtsUsOfdmaAQProbeCmMacAddr_Type()
)
docsPnmCmtsUsOfdmaAQProbeCmMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeCmMacAddr.setStatus("current")


class _DocsPnmCmtsUsOfdmaAQProbeUseIdleSid_Type(TruthValue):
    """Custom type docsPnmCmtsUsOfdmaAQProbeUseIdleSid based on TruthValue"""


_DocsPnmCmtsUsOfdmaAQProbeUseIdleSid_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeUseIdleSid = _DocsPnmCmtsUsOfdmaAQProbeUseIdleSid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 2),
    _DocsPnmCmtsUsOfdmaAQProbeUseIdleSid_Type()
)
docsPnmCmtsUsOfdmaAQProbeUseIdleSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeUseIdleSid.setStatus("current")


class _DocsPnmCmtsUsOfdmaAQProbePreEqOn_Type(TruthValue):
    """Custom type docsPnmCmtsUsOfdmaAQProbePreEqOn based on TruthValue"""


_DocsPnmCmtsUsOfdmaAQProbePreEqOn_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbePreEqOn = _DocsPnmCmtsUsOfdmaAQProbePreEqOn_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 3),
    _DocsPnmCmtsUsOfdmaAQProbePreEqOn_Type()
)
docsPnmCmtsUsOfdmaAQProbePreEqOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbePreEqOn.setStatus("current")


class _DocsPnmCmtsUsOfdmaAQProbeEnable_Type(TruthValue):
    """Custom type docsPnmCmtsUsOfdmaAQProbeEnable based on TruthValue"""


_DocsPnmCmtsUsOfdmaAQProbeEnable_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeEnable = _DocsPnmCmtsUsOfdmaAQProbeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 4),
    _DocsPnmCmtsUsOfdmaAQProbeEnable_Type()
)
docsPnmCmtsUsOfdmaAQProbeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeEnable.setStatus("current")


class _DocsPnmCmtsUsOfdmaAQProbeTimeout_Type(Unsigned32):
    """Custom type docsPnmCmtsUsOfdmaAQProbeTimeout based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsOfdmaAQProbeTimeout_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsOfdmaAQProbeTimeout_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeTimeout = _DocsPnmCmtsUsOfdmaAQProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 5),
    _DocsPnmCmtsUsOfdmaAQProbeTimeout_Type()
)
docsPnmCmtsUsOfdmaAQProbeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeTimeout.setUnits("seconds")


class _DocsPnmCmtsUsOfdmaAQProbeNumSymToCapt_Type(Unsigned32):
    """Custom type docsPnmCmtsUsOfdmaAQProbeNumSymToCapt based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsOfdmaAQProbeNumSymToCapt_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsOfdmaAQProbeNumSymToCapt_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeNumSymToCapt = _DocsPnmCmtsUsOfdmaAQProbeNumSymToCapt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 6),
    _DocsPnmCmtsUsOfdmaAQProbeNumSymToCapt_Type()
)
docsPnmCmtsUsOfdmaAQProbeNumSymToCapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeNumSymToCapt.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeNumSymToCapt.setUnits("symbols")


class _DocsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols_Type(Unsigned32):
    """Custom type docsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols = _DocsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 7),
    _DocsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols_Type()
)
docsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols.setStatus("current")


class _DocsPnmCmtsUsOfdmaAQProbeNumSamples_Type(Unsigned32):
    """Custom type docsPnmCmtsUsOfdmaAQProbeNumSamples based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsOfdmaAQProbeNumSamples_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsOfdmaAQProbeNumSamples_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeNumSamples = _DocsPnmCmtsUsOfdmaAQProbeNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 8),
    _DocsPnmCmtsUsOfdmaAQProbeNumSamples_Type()
)
docsPnmCmtsUsOfdmaAQProbeNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeNumSamples.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeNumSamples.setUnits("samples")


class _DocsPnmCmtsUsOfdmaAQProbeTimeStamp_Type(OctetString):
    """Custom type docsPnmCmtsUsOfdmaAQProbeTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DocsPnmCmtsUsOfdmaAQProbeTimeStamp_Type.__name__ = "OctetString"
_DocsPnmCmtsUsOfdmaAQProbeTimeStamp_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeTimeStamp = _DocsPnmCmtsUsOfdmaAQProbeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 9),
    _DocsPnmCmtsUsOfdmaAQProbeTimeStamp_Type()
)
docsPnmCmtsUsOfdmaAQProbeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeTimeStamp.setStatus("current")
_DocsPnmCmtsUsOfdmaAQProbeMeasStatus_Type = MeasStatusType
_DocsPnmCmtsUsOfdmaAQProbeMeasStatus_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeMeasStatus = _DocsPnmCmtsUsOfdmaAQProbeMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 10),
    _DocsPnmCmtsUsOfdmaAQProbeMeasStatus_Type()
)
docsPnmCmtsUsOfdmaAQProbeMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeMeasStatus.setStatus("current")
_DocsPnmCmtsUsOfdmaAQProbeFileName_Type = SnmpAdminString
_DocsPnmCmtsUsOfdmaAQProbeFileName_Object = MibTableColumn
docsPnmCmtsUsOfdmaAQProbeFileName = _DocsPnmCmtsUsOfdmaAQProbeFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 3, 1, 11),
    _DocsPnmCmtsUsOfdmaAQProbeFileName_Type()
)
docsPnmCmtsUsOfdmaAQProbeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaAQProbeFileName.setStatus("current")
_DocsPnmCmtsUsImpNoiseTable_Object = MibTable
docsPnmCmtsUsImpNoiseTable = _DocsPnmCmtsUsImpNoiseTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseTable.setStatus("current")
_DocsPnmCmtsUsImpNoiseEntry_Object = MibTableRow
docsPnmCmtsUsImpNoiseEntry = _DocsPnmCmtsUsImpNoiseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1)
)
docsPnmCmtsUsImpNoiseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseEntry.setStatus("current")


class _DocsPnmCmtsUsImpNoiseEnable_Type(TruthValue):
    """Custom type docsPnmCmtsUsImpNoiseEnable based on TruthValue"""


_DocsPnmCmtsUsImpNoiseEnable_Object = MibTableColumn
docsPnmCmtsUsImpNoiseEnable = _DocsPnmCmtsUsImpNoiseEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 1),
    _DocsPnmCmtsUsImpNoiseEnable_Type()
)
docsPnmCmtsUsImpNoiseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseEnable.setStatus("current")


class _DocsPnmCmtsUsImpNoiseFreeRunDuration_Type(Unsigned32):
    """Custom type docsPnmCmtsUsImpNoiseFreeRunDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_DocsPnmCmtsUsImpNoiseFreeRunDuration_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsImpNoiseFreeRunDuration_Object = MibTableColumn
docsPnmCmtsUsImpNoiseFreeRunDuration = _DocsPnmCmtsUsImpNoiseFreeRunDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 2),
    _DocsPnmCmtsUsImpNoiseFreeRunDuration_Type()
)
docsPnmCmtsUsImpNoiseFreeRunDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseFreeRunDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseFreeRunDuration.setUnits("seconds")


class _DocsPnmCmtsUsImpNoiseStTrigLvl_Type(Unsigned32):
    """Custom type docsPnmCmtsUsImpNoiseStTrigLvl based on Unsigned32"""
    defaultValue = 300


_DocsPnmCmtsUsImpNoiseStTrigLvl_Object = MibTableColumn
docsPnmCmtsUsImpNoiseStTrigLvl = _DocsPnmCmtsUsImpNoiseStTrigLvl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 3),
    _DocsPnmCmtsUsImpNoiseStTrigLvl_Type()
)
docsPnmCmtsUsImpNoiseStTrigLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseStTrigLvl.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseStTrigLvl.setUnits("microvolts")


class _DocsPnmCmtsUsImpNoiseEndTrigLvl_Type(Unsigned32):
    """Custom type docsPnmCmtsUsImpNoiseEndTrigLvl based on Unsigned32"""
    defaultValue = 150


_DocsPnmCmtsUsImpNoiseEndTrigLvl_Object = MibTableColumn
docsPnmCmtsUsImpNoiseEndTrigLvl = _DocsPnmCmtsUsImpNoiseEndTrigLvl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 4),
    _DocsPnmCmtsUsImpNoiseEndTrigLvl_Type()
)
docsPnmCmtsUsImpNoiseEndTrigLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseEndTrigLvl.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseEndTrigLvl.setUnits("microvolts")


class _DocsPnmCmtsUsImpNoiseCenterFrq_Type(Unsigned32):
    """Custom type docsPnmCmtsUsImpNoiseCenterFrq based on Unsigned32"""
    defaultValue = 7000000


_DocsPnmCmtsUsImpNoiseCenterFrq_Object = MibTableColumn
docsPnmCmtsUsImpNoiseCenterFrq = _DocsPnmCmtsUsImpNoiseCenterFrq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 5),
    _DocsPnmCmtsUsImpNoiseCenterFrq_Type()
)
docsPnmCmtsUsImpNoiseCenterFrq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseCenterFrq.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseCenterFrq.setUnits("Hz")


class _DocsPnmCmtsUsImpNoiseMeasBw_Type(Unsigned32):
    """Custom type docsPnmCmtsUsImpNoiseMeasBw based on Unsigned32"""
    defaultValue = 2560

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(320, 320),
        ValueRangeConstraint(640, 640),
        ValueRangeConstraint(1280, 1280),
        ValueRangeConstraint(2560, 2560),
        ValueRangeConstraint(5120, 5120),
    )


_DocsPnmCmtsUsImpNoiseMeasBw_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsImpNoiseMeasBw_Object = MibTableColumn
docsPnmCmtsUsImpNoiseMeasBw = _DocsPnmCmtsUsImpNoiseMeasBw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 6),
    _DocsPnmCmtsUsImpNoiseMeasBw_Type()
)
docsPnmCmtsUsImpNoiseMeasBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseMeasBw.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseMeasBw.setUnits("kHz")


class _DocsPnmCmtsUsImpNoiseNumEvtsCnted_Type(Unsigned32):
    """Custom type docsPnmCmtsUsImpNoiseNumEvtsCnted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsImpNoiseNumEvtsCnted_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsImpNoiseNumEvtsCnted_Object = MibTableColumn
docsPnmCmtsUsImpNoiseNumEvtsCnted = _DocsPnmCmtsUsImpNoiseNumEvtsCnted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 7),
    _DocsPnmCmtsUsImpNoiseNumEvtsCnted_Type()
)
docsPnmCmtsUsImpNoiseNumEvtsCnted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseNumEvtsCnted.setStatus("current")


class _DocsPnmCmtsUsImpNoiseLastEvtTimeStamp_Type(OctetString):
    """Custom type docsPnmCmtsUsImpNoiseLastEvtTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DocsPnmCmtsUsImpNoiseLastEvtTimeStamp_Type.__name__ = "OctetString"
_DocsPnmCmtsUsImpNoiseLastEvtTimeStamp_Object = MibTableColumn
docsPnmCmtsUsImpNoiseLastEvtTimeStamp = _DocsPnmCmtsUsImpNoiseLastEvtTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 8),
    _DocsPnmCmtsUsImpNoiseLastEvtTimeStamp_Type()
)
docsPnmCmtsUsImpNoiseLastEvtTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseLastEvtTimeStamp.setStatus("current")
_DocsPnmCmtsUsImpNoiseLastEvtDuration_Type = Unsigned32
_DocsPnmCmtsUsImpNoiseLastEvtDuration_Object = MibTableColumn
docsPnmCmtsUsImpNoiseLastEvtDuration = _DocsPnmCmtsUsImpNoiseLastEvtDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 9),
    _DocsPnmCmtsUsImpNoiseLastEvtDuration_Type()
)
docsPnmCmtsUsImpNoiseLastEvtDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseLastEvtDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseLastEvtDuration.setUnits("nanoseconds")
_DocsPnmCmtsUsImpNoiseLastEvtAvgPwr_Type = Integer32
_DocsPnmCmtsUsImpNoiseLastEvtAvgPwr_Object = MibTableColumn
docsPnmCmtsUsImpNoiseLastEvtAvgPwr = _DocsPnmCmtsUsImpNoiseLastEvtAvgPwr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 10),
    _DocsPnmCmtsUsImpNoiseLastEvtAvgPwr_Type()
)
docsPnmCmtsUsImpNoiseLastEvtAvgPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseLastEvtAvgPwr.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseLastEvtAvgPwr.setUnits("dBmV")
_DocsPnmCmtsUsImpNoiseMeasStatus_Type = MeasStatusType
_DocsPnmCmtsUsImpNoiseMeasStatus_Object = MibTableColumn
docsPnmCmtsUsImpNoiseMeasStatus = _DocsPnmCmtsUsImpNoiseMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 11),
    _DocsPnmCmtsUsImpNoiseMeasStatus_Type()
)
docsPnmCmtsUsImpNoiseMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseMeasStatus.setStatus("current")
_DocsPnmCmtsUsImpNoiseFileName_Type = SnmpAdminString
_DocsPnmCmtsUsImpNoiseFileName_Object = MibTableColumn
docsPnmCmtsUsImpNoiseFileName = _DocsPnmCmtsUsImpNoiseFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 4, 1, 12),
    _DocsPnmCmtsUsImpNoiseFileName_Type()
)
docsPnmCmtsUsImpNoiseFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsImpNoiseFileName.setStatus("current")
_DocsPnmCmtsUsHistTable_Object = MibTable
docsPnmCmtsUsHistTable = _DocsPnmCmtsUsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 5)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsHistTable.setStatus("current")
_DocsPnmCmtsUsHistEntry_Object = MibTableRow
docsPnmCmtsUsHistEntry = _DocsPnmCmtsUsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 5, 1)
)
docsPnmCmtsUsHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsHistEntry.setStatus("current")


class _DocsPnmCmtsUsHistEnable_Type(TruthValue):
    """Custom type docsPnmCmtsUsHistEnable based on TruthValue"""


_DocsPnmCmtsUsHistEnable_Object = MibTableColumn
docsPnmCmtsUsHistEnable = _DocsPnmCmtsUsHistEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 5, 1, 1),
    _DocsPnmCmtsUsHistEnable_Type()
)
docsPnmCmtsUsHistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsHistEnable.setStatus("current")


class _DocsPnmCmtsUsHistTimeOut_Type(Unsigned32):
    """Custom type docsPnmCmtsUsHistTimeOut based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsHistTimeOut_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsHistTimeOut_Object = MibTableColumn
docsPnmCmtsUsHistTimeOut = _DocsPnmCmtsUsHistTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 5, 1, 2),
    _DocsPnmCmtsUsHistTimeOut_Type()
)
docsPnmCmtsUsHistTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsHistTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsUsHistTimeOut.setUnits("seconds")
_DocsPnmCmtsUsHistMeasStatus_Type = MeasStatusType
_DocsPnmCmtsUsHistMeasStatus_Object = MibTableColumn
docsPnmCmtsUsHistMeasStatus = _DocsPnmCmtsUsHistMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 5, 1, 3),
    _DocsPnmCmtsUsHistMeasStatus_Type()
)
docsPnmCmtsUsHistMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsHistMeasStatus.setStatus("current")
_DocsPnmCmtsUsHistFileName_Type = SnmpAdminString
_DocsPnmCmtsUsHistFileName_Object = MibTableColumn
docsPnmCmtsUsHistFileName = _DocsPnmCmtsUsHistFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 5, 1, 4),
    _DocsPnmCmtsUsHistFileName_Type()
)
docsPnmCmtsUsHistFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsHistFileName.setStatus("current")
_DocsPnmCmtsUsOfdmaRxPwrTable_Object = MibTable
docsPnmCmtsUsOfdmaRxPwrTable = _DocsPnmCmtsUsOfdmaRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 6)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxPwrTable.setStatus("current")
_DocsPnmCmtsUsOfdmaRxPwrEntry_Object = MibTableRow
docsPnmCmtsUsOfdmaRxPwrEntry = _DocsPnmCmtsUsOfdmaRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 6, 1)
)
docsPnmCmtsUsOfdmaRxPwrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxPwrCmMac"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxPwrEntry.setStatus("current")


class _DocsPnmCmtsUsOfdmaRxPwrEnable_Type(TruthValue):
    """Custom type docsPnmCmtsUsOfdmaRxPwrEnable based on TruthValue"""


_DocsPnmCmtsUsOfdmaRxPwrEnable_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxPwrEnable = _DocsPnmCmtsUsOfdmaRxPwrEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 6, 1, 1),
    _DocsPnmCmtsUsOfdmaRxPwrEnable_Type()
)
docsPnmCmtsUsOfdmaRxPwrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxPwrEnable.setStatus("current")
_DocsPnmCmtsUsOfdmaRxPwrCmMac_Type = MacAddress
_DocsPnmCmtsUsOfdmaRxPwrCmMac_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxPwrCmMac = _DocsPnmCmtsUsOfdmaRxPwrCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 6, 1, 2),
    _DocsPnmCmtsUsOfdmaRxPwrCmMac_Type()
)
docsPnmCmtsUsOfdmaRxPwrCmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxPwrCmMac.setStatus("current")


class _DocsPnmCmtsUsOfdmaRxPwrPreEq_Type(TruthValue):
    """Custom type docsPnmCmtsUsOfdmaRxPwrPreEq based on TruthValue"""


_DocsPnmCmtsUsOfdmaRxPwrPreEq_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxPwrPreEq = _DocsPnmCmtsUsOfdmaRxPwrPreEq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 6, 1, 3),
    _DocsPnmCmtsUsOfdmaRxPwrPreEq_Type()
)
docsPnmCmtsUsOfdmaRxPwrPreEq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxPwrPreEq.setStatus("current")


class _DocsPnmCmtsUsOfdmaRxPwrNumAvgs_Type(Unsigned32):
    """Custom type docsPnmCmtsUsOfdmaRxPwrNumAvgs based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmtsUsOfdmaRxPwrNumAvgs_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsOfdmaRxPwrNumAvgs_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxPwrNumAvgs = _DocsPnmCmtsUsOfdmaRxPwrNumAvgs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 6, 1, 4),
    _DocsPnmCmtsUsOfdmaRxPwrNumAvgs_Type()
)
docsPnmCmtsUsOfdmaRxPwrNumAvgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxPwrNumAvgs.setStatus("current")
_DocsPnmCmtsUsOfdmaRxPwrOnePtSixPsd_Type = TenthdB
_DocsPnmCmtsUsOfdmaRxPwrOnePtSixPsd_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxPwrOnePtSixPsd = _DocsPnmCmtsUsOfdmaRxPwrOnePtSixPsd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 6, 1, 5),
    _DocsPnmCmtsUsOfdmaRxPwrOnePtSixPsd_Type()
)
docsPnmCmtsUsOfdmaRxPwrOnePtSixPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxPwrOnePtSixPsd.setStatus("current")
_DocsPnmCmtsUsOfdmaRxPwrMeasStatus_Type = MeasStatusType
_DocsPnmCmtsUsOfdmaRxPwrMeasStatus_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxPwrMeasStatus = _DocsPnmCmtsUsOfdmaRxPwrMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 6, 1, 6),
    _DocsPnmCmtsUsOfdmaRxPwrMeasStatus_Type()
)
docsPnmCmtsUsOfdmaRxPwrMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxPwrMeasStatus.setStatus("current")
_DocsPnmCmtsUsOfdmaRxMerTable_Object = MibTable
docsPnmCmtsUsOfdmaRxMerTable = _DocsPnmCmtsUsOfdmaRxMerTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 7)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxMerTable.setStatus("current")
_DocsPnmCmtsUsOfdmaRxMerEntry_Object = MibTableRow
docsPnmCmtsUsOfdmaRxMerEntry = _DocsPnmCmtsUsOfdmaRxMerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 7, 1)
)
docsPnmCmtsUsOfdmaRxMerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxMerEntry.setStatus("current")


class _DocsPnmCmtsUsOfdmaRxMerEnable_Type(TruthValue):
    """Custom type docsPnmCmtsUsOfdmaRxMerEnable based on TruthValue"""


_DocsPnmCmtsUsOfdmaRxMerEnable_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxMerEnable = _DocsPnmCmtsUsOfdmaRxMerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 7, 1, 1),
    _DocsPnmCmtsUsOfdmaRxMerEnable_Type()
)
docsPnmCmtsUsOfdmaRxMerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxMerEnable.setStatus("current")


class _DocsPnmCmtsUsOfdmaRxMerCmMac_Type(MacAddress):
    """Custom type docsPnmCmtsUsOfdmaRxMerCmMac based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsPnmCmtsUsOfdmaRxMerCmMac_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxMerCmMac = _DocsPnmCmtsUsOfdmaRxMerCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 7, 1, 2),
    _DocsPnmCmtsUsOfdmaRxMerCmMac_Type()
)
docsPnmCmtsUsOfdmaRxMerCmMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxMerCmMac.setStatus("current")


class _DocsPnmCmtsUsOfdmaRxMerPreEq_Type(TruthValue):
    """Custom type docsPnmCmtsUsOfdmaRxMerPreEq based on TruthValue"""


_DocsPnmCmtsUsOfdmaRxMerPreEq_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxMerPreEq = _DocsPnmCmtsUsOfdmaRxMerPreEq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 7, 1, 3),
    _DocsPnmCmtsUsOfdmaRxMerPreEq_Type()
)
docsPnmCmtsUsOfdmaRxMerPreEq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxMerPreEq.setStatus("current")


class _DocsPnmCmtsUsOfdmaRxMerNumAvgs_Type(Unsigned32):
    """Custom type docsPnmCmtsUsOfdmaRxMerNumAvgs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmtsUsOfdmaRxMerNumAvgs_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsOfdmaRxMerNumAvgs_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxMerNumAvgs = _DocsPnmCmtsUsOfdmaRxMerNumAvgs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 7, 1, 4),
    _DocsPnmCmtsUsOfdmaRxMerNumAvgs_Type()
)
docsPnmCmtsUsOfdmaRxMerNumAvgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxMerNumAvgs.setStatus("current")
_DocsPnmCmtsUsOfdmaRxMerMeasStatus_Type = MeasStatusType
_DocsPnmCmtsUsOfdmaRxMerMeasStatus_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxMerMeasStatus = _DocsPnmCmtsUsOfdmaRxMerMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 7, 1, 5),
    _DocsPnmCmtsUsOfdmaRxMerMeasStatus_Type()
)
docsPnmCmtsUsOfdmaRxMerMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxMerMeasStatus.setStatus("current")
_DocsPnmCmtsUsOfdmaRxMerFileName_Type = SnmpAdminString
_DocsPnmCmtsUsOfdmaRxMerFileName_Object = MibTableColumn
docsPnmCmtsUsOfdmaRxMerFileName = _DocsPnmCmtsUsOfdmaRxMerFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 7, 1, 6),
    _DocsPnmCmtsUsOfdmaRxMerFileName_Type()
)
docsPnmCmtsUsOfdmaRxMerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsOfdmaRxMerFileName.setStatus("current")
_DocsPnmCmtsUsSpecAnTable_Object = MibTable
docsPnmCmtsUsSpecAnTable = _DocsPnmCmtsUsSpecAnTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnTable.setStatus("deprecated")
_DocsPnmCmtsUsSpecAnEntry_Object = MibTableRow
docsPnmCmtsUsSpecAnEntry = _DocsPnmCmtsUsSpecAnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1)
)
docsPnmCmtsUsSpecAnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnEntry.setStatus("deprecated")


class _DocsPnmCmtsUsSpecAnEnable_Type(TruthValue):
    """Custom type docsPnmCmtsUsSpecAnEnable based on TruthValue"""


_DocsPnmCmtsUsSpecAnEnable_Object = MibTableColumn
docsPnmCmtsUsSpecAnEnable = _DocsPnmCmtsUsSpecAnEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 1),
    _DocsPnmCmtsUsSpecAnEnable_Type()
)
docsPnmCmtsUsSpecAnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnEnable.setStatus("deprecated")


class _DocsPnmCmtsUsSpecAnTrigMode_Type(Integer32):
    """Custom type docsPnmCmtsUsSpecAnTrigMode based on Integer32"""
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
        *(("cmMac", 7),
          ("freeRunning", 2),
          ("idleSid", 5),
          ("miniSlotCount", 3),
          ("minislotNumber", 6),
          ("other", 1),
          ("quietProbeSymbol", 8),
          ("sid", 4))
    )


_DocsPnmCmtsUsSpecAnTrigMode_Type.__name__ = "Integer32"
_DocsPnmCmtsUsSpecAnTrigMode_Object = MibTableColumn
docsPnmCmtsUsSpecAnTrigMode = _DocsPnmCmtsUsSpecAnTrigMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 2),
    _DocsPnmCmtsUsSpecAnTrigMode_Type()
)
docsPnmCmtsUsSpecAnTrigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnTrigMode.setStatus("deprecated")


class _DocsPnmCmtsUsSpecAnMiniSlotCnt_Type(Unsigned32):
    """Custom type docsPnmCmtsUsSpecAnMiniSlotCnt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsSpecAnMiniSlotCnt_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsSpecAnMiniSlotCnt_Object = MibTableColumn
docsPnmCmtsUsSpecAnMiniSlotCnt = _DocsPnmCmtsUsSpecAnMiniSlotCnt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 3),
    _DocsPnmCmtsUsSpecAnMiniSlotCnt_Type()
)
docsPnmCmtsUsSpecAnMiniSlotCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnMiniSlotCnt.setStatus("deprecated")


class _DocsPnmCmtsUsSpecAnSid_Type(Unsigned32):
    """Custom type docsPnmCmtsUsSpecAnSid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsSpecAnSid_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsSpecAnSid_Object = MibTableColumn
docsPnmCmtsUsSpecAnSid = _DocsPnmCmtsUsSpecAnSid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 4),
    _DocsPnmCmtsUsSpecAnSid_Type()
)
docsPnmCmtsUsSpecAnSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnSid.setStatus("deprecated")


class _DocsPnmCmtsUsSpecAnMiniSlotNum_Type(Unsigned32):
    """Custom type docsPnmCmtsUsSpecAnMiniSlotNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsSpecAnMiniSlotNum_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsSpecAnMiniSlotNum_Object = MibTableColumn
docsPnmCmtsUsSpecAnMiniSlotNum = _DocsPnmCmtsUsSpecAnMiniSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 5),
    _DocsPnmCmtsUsSpecAnMiniSlotNum_Type()
)
docsPnmCmtsUsSpecAnMiniSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnMiniSlotNum.setStatus("deprecated")


class _DocsPnmCmtsUsSpecAnCmMac_Type(MacAddress):
    """Custom type docsPnmCmtsUsSpecAnCmMac based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsPnmCmtsUsSpecAnCmMac_Object = MibTableColumn
docsPnmCmtsUsSpecAnCmMac = _DocsPnmCmtsUsSpecAnCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 6),
    _DocsPnmCmtsUsSpecAnCmMac_Type()
)
docsPnmCmtsUsSpecAnCmMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnCmMac.setStatus("deprecated")


class _DocsPnmCmtsUsSpecAnCenterFreq_Type(Unsigned32):
    """Custom type docsPnmCmtsUsSpecAnCenterFreq based on Unsigned32"""
    defaultValue = 0


_DocsPnmCmtsUsSpecAnCenterFreq_Object = MibTableColumn
docsPnmCmtsUsSpecAnCenterFreq = _DocsPnmCmtsUsSpecAnCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 7),
    _DocsPnmCmtsUsSpecAnCenterFreq_Type()
)
docsPnmCmtsUsSpecAnCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnCenterFreq.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnCenterFreq.setUnits("Hz")


class _DocsPnmCmtsUsSpecAnSpan_Type(Unsigned32):
    """Custom type docsPnmCmtsUsSpecAnSpan based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsSpecAnSpan_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsSpecAnSpan_Object = MibTableColumn
docsPnmCmtsUsSpecAnSpan = _DocsPnmCmtsUsSpecAnSpan_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 8),
    _DocsPnmCmtsUsSpecAnSpan_Type()
)
docsPnmCmtsUsSpecAnSpan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnSpan.setStatus("deprecated")


class _DocsPnmCmtsUsSpecAnNumberOfBins_Type(Unsigned32):
    """Custom type docsPnmCmtsUsSpecAnNumberOfBins based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUsSpecAnNumberOfBins_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUsSpecAnNumberOfBins_Object = MibTableColumn
docsPnmCmtsUsSpecAnNumberOfBins = _DocsPnmCmtsUsSpecAnNumberOfBins_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 9),
    _DocsPnmCmtsUsSpecAnNumberOfBins_Type()
)
docsPnmCmtsUsSpecAnNumberOfBins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnNumberOfBins.setStatus("deprecated")
_DocsPnmCmtsUsSpecAnMeasStatus_Type = MeasStatusType
_DocsPnmCmtsUsSpecAnMeasStatus_Object = MibTableColumn
docsPnmCmtsUsSpecAnMeasStatus = _DocsPnmCmtsUsSpecAnMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 10),
    _DocsPnmCmtsUsSpecAnMeasStatus_Type()
)
docsPnmCmtsUsSpecAnMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnMeasStatus.setStatus("deprecated")
_DocsPnmCmtsUsSpecAnFileName_Type = SnmpAdminString
_DocsPnmCmtsUsSpecAnFileName_Object = MibTableColumn
docsPnmCmtsUsSpecAnFileName = _DocsPnmCmtsUsSpecAnFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 8, 1, 11),
    _DocsPnmCmtsUsSpecAnFileName_Type()
)
docsPnmCmtsUsSpecAnFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUsSpecAnFileName.setStatus("deprecated")
_DocsPnmCmtsOptObjects_ObjectIdentity = ObjectIdentity
docsPnmCmtsOptObjects = _DocsPnmCmtsOptObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9)
)
_DocsPnmCmtsOptReqTable_Object = MibTable
docsPnmCmtsOptReqTable = _DocsPnmCmtsOptReqTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1)
)
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqTable.setStatus("current")
_DocsPnmCmtsOptReqEntry_Object = MibTableRow
docsPnmCmtsOptReqEntry = _DocsPnmCmtsOptReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1)
)
docsPnmCmtsOptReqEntry.setIndexNames(
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqCmMacAddr"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqDsOfdmChanCfgIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqDsOfdmProfCfgId"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqEntry.setStatus("current")
_DocsPnmCmtsOptReqCmMacAddr_Type = MacAddress
_DocsPnmCmtsOptReqCmMacAddr_Object = MibTableColumn
docsPnmCmtsOptReqCmMacAddr = _DocsPnmCmtsOptReqCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 1),
    _DocsPnmCmtsOptReqCmMacAddr_Type()
)
docsPnmCmtsOptReqCmMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqCmMacAddr.setStatus("current")


class _DocsPnmCmtsOptReqDsOfdmChanCfgIndex_Type(Unsigned32):
    """Custom type docsPnmCmtsOptReqDsOfdmChanCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmtsOptReqDsOfdmChanCfgIndex_Type.__name__ = "Unsigned32"
_DocsPnmCmtsOptReqDsOfdmChanCfgIndex_Object = MibTableColumn
docsPnmCmtsOptReqDsOfdmChanCfgIndex = _DocsPnmCmtsOptReqDsOfdmChanCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 2),
    _DocsPnmCmtsOptReqDsOfdmChanCfgIndex_Type()
)
docsPnmCmtsOptReqDsOfdmChanCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqDsOfdmChanCfgIndex.setStatus("current")


class _DocsPnmCmtsOptReqDsOfdmProfCfgId_Type(Unsigned32):
    """Custom type docsPnmCmtsOptReqDsOfdmProfCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_DocsPnmCmtsOptReqDsOfdmProfCfgId_Type.__name__ = "Unsigned32"
_DocsPnmCmtsOptReqDsOfdmProfCfgId_Object = MibTableColumn
docsPnmCmtsOptReqDsOfdmProfCfgId = _DocsPnmCmtsOptReqDsOfdmProfCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 3),
    _DocsPnmCmtsOptReqDsOfdmProfCfgId_Type()
)
docsPnmCmtsOptReqDsOfdmProfCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqDsOfdmProfCfgId.setStatus("current")


class _DocsPnmCmtsOptReqOpCode_Type(Integer32):
    """Custom type docsPnmCmtsOptReqOpCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abort", 3),
          ("other", 1),
          ("start", 2))
    )


_DocsPnmCmtsOptReqOpCode_Type.__name__ = "Integer32"
_DocsPnmCmtsOptReqOpCode_Object = MibTableColumn
docsPnmCmtsOptReqOpCode = _DocsPnmCmtsOptReqOpCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 4),
    _DocsPnmCmtsOptReqOpCode_Type()
)
docsPnmCmtsOptReqOpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqOpCode.setStatus("current")


class _DocsPnmCmtsOptReqProfileTest_Type(Bits):
    """Custom type docsPnmCmtsOptReqProfileTest based on Bits"""
    namedValues = NamedValues(
        *(("codewordStats", 3),
          ("codewordThreshComp", 4),
          ("ncpCrcThreshComp", 6),
          ("ncpFieldStats", 5),
          ("other", 8),
          ("reserved", 7),
          ("rxMerSubCarrierStats", 0),
          ("rxMerSubCarrierThreshComp", 1),
          ("snrMarginCandidateProfile", 2))
    )

_DocsPnmCmtsOptReqProfileTest_Type.__name__ = "Bits"
_DocsPnmCmtsOptReqProfileTest_Object = MibTableColumn
docsPnmCmtsOptReqProfileTest = _DocsPnmCmtsOptReqProfileTest_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 5),
    _DocsPnmCmtsOptReqProfileTest_Type()
)
docsPnmCmtsOptReqProfileTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqProfileTest.setStatus("current")
_DocsPnmCmtsOptReqMaxDuration_Type = Unsigned32
_DocsPnmCmtsOptReqMaxDuration_Object = MibTableColumn
docsPnmCmtsOptReqMaxDuration = _DocsPnmCmtsOptReqMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 6),
    _DocsPnmCmtsOptReqMaxDuration_Type()
)
docsPnmCmtsOptReqMaxDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqMaxDuration.setUnits("milliseconds")
_DocsPnmCmtsOptReqMaxCodewords_Type = Unsigned32
_DocsPnmCmtsOptReqMaxCodewords_Object = MibTableColumn
docsPnmCmtsOptReqMaxCodewords = _DocsPnmCmtsOptReqMaxCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 7),
    _DocsPnmCmtsOptReqMaxCodewords_Type()
)
docsPnmCmtsOptReqMaxCodewords.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqMaxCodewords.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqMaxCodewords.setUnits("Number of Codewords")
_DocsPnmCmtsOptReqMaxUncorrectableCws_Type = Unsigned32
_DocsPnmCmtsOptReqMaxUncorrectableCws_Object = MibTableColumn
docsPnmCmtsOptReqMaxUncorrectableCws = _DocsPnmCmtsOptReqMaxUncorrectableCws_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 8),
    _DocsPnmCmtsOptReqMaxUncorrectableCws_Type()
)
docsPnmCmtsOptReqMaxUncorrectableCws.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqMaxUncorrectableCws.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqMaxUncorrectableCws.setUnits("Number of Codewords")


class _DocsPnmCmtsOptReqCwTaggingEnabled_Type(TruthValue):
    """Custom type docsPnmCmtsOptReqCwTaggingEnabled based on TruthValue"""


_DocsPnmCmtsOptReqCwTaggingEnabled_Object = MibTableColumn
docsPnmCmtsOptReqCwTaggingEnabled = _DocsPnmCmtsOptReqCwTaggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 9),
    _DocsPnmCmtsOptReqCwTaggingEnabled_Type()
)
docsPnmCmtsOptReqCwTaggingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqCwTaggingEnabled.setStatus("current")
_DocsPnmCmtsOptReqNcpFields_Type = Unsigned32
_DocsPnmCmtsOptReqNcpFields_Object = MibTableColumn
docsPnmCmtsOptReqNcpFields = _DocsPnmCmtsOptReqNcpFields_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 10),
    _DocsPnmCmtsOptReqNcpFields_Type()
)
docsPnmCmtsOptReqNcpFields.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqNcpFields.setStatus("current")
_DocsPnmCmtsOptReqMaxNcpCrcFails_Type = Unsigned32
_DocsPnmCmtsOptReqMaxNcpCrcFails_Object = MibTableColumn
docsPnmCmtsOptReqMaxNcpCrcFails = _DocsPnmCmtsOptReqMaxNcpCrcFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 11),
    _DocsPnmCmtsOptReqMaxNcpCrcFails_Type()
)
docsPnmCmtsOptReqMaxNcpCrcFails.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqMaxNcpCrcFails.setStatus("current")
_DocsPnmCmtsOptReqStatus_Type = RowStatus
_DocsPnmCmtsOptReqStatus_Object = MibTableColumn
docsPnmCmtsOptReqStatus = _DocsPnmCmtsOptReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 1, 1, 12),
    _DocsPnmCmtsOptReqStatus_Type()
)
docsPnmCmtsOptReqStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptReqStatus.setStatus("current")
_DocsPnmCmtsOptMerThreshCfgTable_Object = MibTable
docsPnmCmtsOptMerThreshCfgTable = _DocsPnmCmtsOptMerThreshCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    docsPnmCmtsOptMerThreshCfgTable.setStatus("current")
_DocsPnmCmtsOptMerThreshCfgEntry_Object = MibTableRow
docsPnmCmtsOptMerThreshCfgEntry = _DocsPnmCmtsOptMerThreshCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 2, 1)
)
docsPnmCmtsOptMerThreshCfgEntry.setIndexNames(
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqDsOfdmChanCfgIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqDsOfdmProfCfgId"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptMerThreshCfgModOrder"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsOptMerThreshCfgEntry.setStatus("current")
_DocsPnmCmtsOptMerThreshCfgModOrder_Type = DsOfdmModulationType
_DocsPnmCmtsOptMerThreshCfgModOrder_Object = MibTableColumn
docsPnmCmtsOptMerThreshCfgModOrder = _DocsPnmCmtsOptMerThreshCfgModOrder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 2, 1, 1),
    _DocsPnmCmtsOptMerThreshCfgModOrder_Type()
)
docsPnmCmtsOptMerThreshCfgModOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsPnmCmtsOptMerThreshCfgModOrder.setStatus("current")


class _DocsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget_Type(Unsigned32):
    """Custom type docsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget_Type.__name__ = "Unsigned32"
_DocsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget_Object = MibTableColumn
docsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget = _DocsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 2, 1, 2),
    _DocsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget_Type()
)
docsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget.setUnits("QuarterdB")
_DocsPnmCmtsOptMerThreshCfgRxMerMargin_Type = Unsigned32
_DocsPnmCmtsOptMerThreshCfgRxMerMargin_Object = MibTableColumn
docsPnmCmtsOptMerThreshCfgRxMerMargin = _DocsPnmCmtsOptMerThreshCfgRxMerMargin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 2, 1, 3),
    _DocsPnmCmtsOptMerThreshCfgRxMerMargin_Type()
)
docsPnmCmtsOptMerThreshCfgRxMerMargin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptMerThreshCfgRxMerMargin.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsOptMerThreshCfgRxMerMargin.setUnits("dB")
_DocsPnmCmtsOptMerThreshCfgStatus_Type = RowStatus
_DocsPnmCmtsOptMerThreshCfgStatus_Object = MibTableColumn
docsPnmCmtsOptMerThreshCfgStatus = _DocsPnmCmtsOptMerThreshCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 2, 1, 4),
    _DocsPnmCmtsOptMerThreshCfgStatus_Type()
)
docsPnmCmtsOptMerThreshCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptMerThreshCfgStatus.setStatus("current")
_DocsPnmCmtsOptProfChgCfgTable_Object = MibTable
docsPnmCmtsOptProfChgCfgTable = _DocsPnmCmtsOptProfChgCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 3)
)
if mibBuilder.loadTexts:
    docsPnmCmtsOptProfChgCfgTable.setStatus("current")
_DocsPnmCmtsOptProfChgCfgEntry_Object = MibTableRow
docsPnmCmtsOptProfChgCfgEntry = _DocsPnmCmtsOptProfChgCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 3, 1)
)
docsPnmCmtsOptProfChgCfgEntry.setIndexNames(
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqCmMacAddr"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptProfChgCfgIfIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsOptProfChgCfgEntry.setStatus("current")
_DocsPnmCmtsOptProfChgCfgIfIndex_Type = InterfaceIndex
_DocsPnmCmtsOptProfChgCfgIfIndex_Object = MibTableColumn
docsPnmCmtsOptProfChgCfgIfIndex = _DocsPnmCmtsOptProfChgCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 3, 1, 1),
    _DocsPnmCmtsOptProfChgCfgIfIndex_Type()
)
docsPnmCmtsOptProfChgCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsPnmCmtsOptProfChgCfgIfIndex.setStatus("current")


class _DocsPnmCmtsOptProfChgCfgDsProfList_Type(OctetString):
    """Custom type docsPnmCmtsOptProfChgCfgDsProfList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DocsPnmCmtsOptProfChgCfgDsProfList_Type.__name__ = "OctetString"
_DocsPnmCmtsOptProfChgCfgDsProfList_Object = MibTableColumn
docsPnmCmtsOptProfChgCfgDsProfList = _DocsPnmCmtsOptProfChgCfgDsProfList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 3, 1, 2),
    _DocsPnmCmtsOptProfChgCfgDsProfList_Type()
)
docsPnmCmtsOptProfChgCfgDsProfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptProfChgCfgDsProfList.setStatus("current")
_DocsPnmCmtsOptProfChgCfgStatus_Type = RowStatus
_DocsPnmCmtsOptProfChgCfgStatus_Object = MibTableColumn
docsPnmCmtsOptProfChgCfgStatus = _DocsPnmCmtsOptProfChgCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 3, 1, 3),
    _DocsPnmCmtsOptProfChgCfgStatus_Type()
)
docsPnmCmtsOptProfChgCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsPnmCmtsOptProfChgCfgStatus.setStatus("current")
_DocsPnmCmtsOptRespTable_Object = MibTable
docsPnmCmtsOptRespTable = _DocsPnmCmtsOptRespTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4)
)
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespTable.setStatus("current")
_DocsPnmCmtsOptRespEntry_Object = MibTableRow
docsPnmCmtsOptRespEntry = _DocsPnmCmtsOptRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1)
)
docsPnmCmtsOptRespEntry.setIndexNames(
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqCmMacAddr"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqDsOfdmChanCfgIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsOptReqDsOfdmProfCfgId"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespEntry.setStatus("current")


class _DocsPnmCmtsOptRespStatus_Type(Integer32):
    """Custom type docsPnmCmtsOptRespStatus based on Integer32"""
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
        *(("aborted", 5),
          ("complete", 6),
          ("maxDurationExpired", 4),
          ("profileAlreadyAssigned", 7),
          ("profileAlreadyUnderTest", 2),
          ("testing", 1),
          ("unavailableResources", 3))
    )


_DocsPnmCmtsOptRespStatus_Type.__name__ = "Integer32"
_DocsPnmCmtsOptRespStatus_Object = MibTableColumn
docsPnmCmtsOptRespStatus = _DocsPnmCmtsOptRespStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 1),
    _DocsPnmCmtsOptRespStatus_Type()
)
docsPnmCmtsOptRespStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespStatus.setStatus("current")


class _DocsPnmCmtsOptRespFirstActiveSubcarrierNum_Type(Unsigned32):
    """Custom type docsPnmCmtsOptRespFirstActiveSubcarrierNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(148, 7895),
    )


_DocsPnmCmtsOptRespFirstActiveSubcarrierNum_Type.__name__ = "Unsigned32"
_DocsPnmCmtsOptRespFirstActiveSubcarrierNum_Object = MibTableColumn
docsPnmCmtsOptRespFirstActiveSubcarrierNum = _DocsPnmCmtsOptRespFirstActiveSubcarrierNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 2),
    _DocsPnmCmtsOptRespFirstActiveSubcarrierNum_Type()
)
docsPnmCmtsOptRespFirstActiveSubcarrierNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespFirstActiveSubcarrierNum.setStatus("current")


class _DocsPnmCmtsOptRespMerData_Type(OctetString):
    """Custom type docsPnmCmtsOptRespMerData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7680),
    )


_DocsPnmCmtsOptRespMerData_Type.__name__ = "OctetString"
_DocsPnmCmtsOptRespMerData_Object = MibTableColumn
docsPnmCmtsOptRespMerData = _DocsPnmCmtsOptRespMerData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 3),
    _DocsPnmCmtsOptRespMerData_Type()
)
docsPnmCmtsOptRespMerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespMerData.setStatus("current")


class _DocsPnmCmtsOptRespMerPassFailData_Type(OctetString):
    """Custom type docsPnmCmtsOptRespMerPassFailData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7680),
    )


_DocsPnmCmtsOptRespMerPassFailData_Type.__name__ = "OctetString"
_DocsPnmCmtsOptRespMerPassFailData_Object = MibTableColumn
docsPnmCmtsOptRespMerPassFailData = _DocsPnmCmtsOptRespMerPassFailData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 4),
    _DocsPnmCmtsOptRespMerPassFailData_Type()
)
docsPnmCmtsOptRespMerPassFailData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespMerPassFailData.setStatus("current")
_DocsPnmCmtsOptRespNumSubcarriersBelowThresh_Type = Unsigned32
_DocsPnmCmtsOptRespNumSubcarriersBelowThresh_Object = MibTableColumn
docsPnmCmtsOptRespNumSubcarriersBelowThresh = _DocsPnmCmtsOptRespNumSubcarriersBelowThresh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 5),
    _DocsPnmCmtsOptRespNumSubcarriersBelowThresh_Type()
)
docsPnmCmtsOptRespNumSubcarriersBelowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespNumSubcarriersBelowThresh.setStatus("current")
_DocsPnmCmtsOptRespSnrMarginData_Type = Unsigned32
_DocsPnmCmtsOptRespSnrMarginData_Object = MibTableColumn
docsPnmCmtsOptRespSnrMarginData = _DocsPnmCmtsOptRespSnrMarginData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 6),
    _DocsPnmCmtsOptRespSnrMarginData_Type()
)
docsPnmCmtsOptRespSnrMarginData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespSnrMarginData.setStatus("current")
_DocsPnmCmtsOptRespCodewordCt_Type = Counter64
_DocsPnmCmtsOptRespCodewordCt_Object = MibTableColumn
docsPnmCmtsOptRespCodewordCt = _DocsPnmCmtsOptRespCodewordCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 7),
    _DocsPnmCmtsOptRespCodewordCt_Type()
)
docsPnmCmtsOptRespCodewordCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespCodewordCt.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespCodewordCt.setUnits("Number of Codewords")
_DocsPnmCmtsOptRespCorrectedCodewordCt_Type = Counter64
_DocsPnmCmtsOptRespCorrectedCodewordCt_Object = MibTableColumn
docsPnmCmtsOptRespCorrectedCodewordCt = _DocsPnmCmtsOptRespCorrectedCodewordCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 8),
    _DocsPnmCmtsOptRespCorrectedCodewordCt_Type()
)
docsPnmCmtsOptRespCorrectedCodewordCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespCorrectedCodewordCt.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespCorrectedCodewordCt.setUnits("Number of Codewords")
_DocsPnmCmtsOptRespUncorrectableCodewordCt_Type = Counter64
_DocsPnmCmtsOptRespUncorrectableCodewordCt_Object = MibTableColumn
docsPnmCmtsOptRespUncorrectableCodewordCt = _DocsPnmCmtsOptRespUncorrectableCodewordCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 9),
    _DocsPnmCmtsOptRespUncorrectableCodewordCt_Type()
)
docsPnmCmtsOptRespUncorrectableCodewordCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespUncorrectableCodewordCt.setStatus("current")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespUncorrectableCodewordCt.setUnits("Number of Codewords")
_DocsPnmCmtsOptRespNcpFieldCt_Type = Counter64
_DocsPnmCmtsOptRespNcpFieldCt_Object = MibTableColumn
docsPnmCmtsOptRespNcpFieldCt = _DocsPnmCmtsOptRespNcpFieldCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 10),
    _DocsPnmCmtsOptRespNcpFieldCt_Type()
)
docsPnmCmtsOptRespNcpFieldCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespNcpFieldCt.setStatus("current")
_DocsPnmCmtsOptRespNcpCrcFailCt_Type = Counter64
_DocsPnmCmtsOptRespNcpCrcFailCt_Object = MibTableColumn
docsPnmCmtsOptRespNcpCrcFailCt = _DocsPnmCmtsOptRespNcpCrcFailCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 9, 4, 1, 11),
    _DocsPnmCmtsOptRespNcpCrcFailCt_Type()
)
docsPnmCmtsOptRespNcpCrcFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsOptRespNcpCrcFailCt.setStatus("current")
_DocsPnmCmtsUtscObjects_ObjectIdentity = ObjectIdentity
docsPnmCmtsUtscObjects = _DocsPnmCmtsUtscObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10)
)
_DocsPnmCmtsUtscCapabTable_Object = MibTable
docsPnmCmtsUtscCapabTable = _DocsPnmCmtsUtscCapabTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCapabTable.setStatus("current")
_DocsPnmCmtsUtscCapabEntry_Object = MibTableRow
docsPnmCmtsUtscCapabEntry = _DocsPnmCmtsUtscCapabEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 1, 1)
)
docsPnmCmtsUtscCapabEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCapabEntry.setStatus("current")


class _DocsPnmCmtsUtscCapabTriggerMode_Type(Bits):
    """Custom type docsPnmCmtsUtscCapabTriggerMode based on Bits"""
    namedValues = NamedValues(
        *(("burstIuc", 7),
          ("cmMac", 5),
          ("freeRunning", 1),
          ("idleSid", 4),
          ("miniSlotCount", 2),
          ("other", 0),
          ("quietProbeSymbol", 6),
          ("sid", 3),
          ("timestamp", 8))
    )

_DocsPnmCmtsUtscCapabTriggerMode_Type.__name__ = "Bits"
_DocsPnmCmtsUtscCapabTriggerMode_Object = MibTableColumn
docsPnmCmtsUtscCapabTriggerMode = _DocsPnmCmtsUtscCapabTriggerMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 1, 1, 1),
    _DocsPnmCmtsUtscCapabTriggerMode_Type()
)
docsPnmCmtsUtscCapabTriggerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCapabTriggerMode.setStatus("current")


class _DocsPnmCmtsUtscCapabOutputFormat_Type(Bits):
    """Custom type docsPnmCmtsUtscCapabOutputFormat based on Bits"""
    namedValues = NamedValues(
        *(("fftAmplitude", 5),
          ("fftDb", 6),
          ("fftIQ", 4),
          ("fftPower", 2),
          ("other", 0),
          ("rawAdc", 3),
          ("timeIQ", 1))
    )

_DocsPnmCmtsUtscCapabOutputFormat_Type.__name__ = "Bits"
_DocsPnmCmtsUtscCapabOutputFormat_Object = MibTableColumn
docsPnmCmtsUtscCapabOutputFormat = _DocsPnmCmtsUtscCapabOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 1, 1, 2),
    _DocsPnmCmtsUtscCapabOutputFormat_Type()
)
docsPnmCmtsUtscCapabOutputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCapabOutputFormat.setStatus("current")


class _DocsPnmCmtsUtscCapabWindow_Type(Bits):
    """Custom type docsPnmCmtsUtscCapabWindow based on Bits"""
    namedValues = NamedValues(
        *(("blackmanHarris", 3),
          ("chebyshev", 7),
          ("flatTop", 5),
          ("gaussian", 6),
          ("hamming", 4),
          ("hann", 2),
          ("other", 0),
          ("rectangular", 1))
    )

_DocsPnmCmtsUtscCapabWindow_Type.__name__ = "Bits"
_DocsPnmCmtsUtscCapabWindow_Object = MibTableColumn
docsPnmCmtsUtscCapabWindow = _DocsPnmCmtsUtscCapabWindow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 1, 1, 3),
    _DocsPnmCmtsUtscCapabWindow_Type()
)
docsPnmCmtsUtscCapabWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCapabWindow.setStatus("current")
_DocsPnmCmtsUtscCapabDescription_Type = SnmpAdminString
_DocsPnmCmtsUtscCapabDescription_Object = MibTableColumn
docsPnmCmtsUtscCapabDescription = _DocsPnmCmtsUtscCapabDescription_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 1, 1, 4),
    _DocsPnmCmtsUtscCapabDescription_Type()
)
docsPnmCmtsUtscCapabDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCapabDescription.setStatus("current")
_DocsPnmCmtsUtscCfgTable_Object = MibTable
docsPnmCmtsUtscCfgTable = _DocsPnmCmtsUtscCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgTable.setStatus("current")
_DocsPnmCmtsUtscCfgEntry_Object = MibTableRow
docsPnmCmtsUtscCfgEntry = _DocsPnmCmtsUtscCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1)
)
docsPnmCmtsUtscCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsUtscCfgIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgEntry.setStatus("current")


class _DocsPnmCmtsUtscCfgIndex_Type(Unsigned32):
    """Custom type docsPnmCmtsUtscCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsPnmCmtsUtscCfgIndex_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUtscCfgIndex_Object = MibTableColumn
docsPnmCmtsUtscCfgIndex = _DocsPnmCmtsUtscCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 1),
    _DocsPnmCmtsUtscCfgIndex_Type()
)
docsPnmCmtsUtscCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgIndex.setStatus("current")
_DocsPnmCmtsUtscCfgLogicalChIfIndex_Type = InterfaceIndexOrZero
_DocsPnmCmtsUtscCfgLogicalChIfIndex_Object = MibTableColumn
docsPnmCmtsUtscCfgLogicalChIfIndex = _DocsPnmCmtsUtscCfgLogicalChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 2),
    _DocsPnmCmtsUtscCfgLogicalChIfIndex_Type()
)
docsPnmCmtsUtscCfgLogicalChIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgLogicalChIfIndex.setStatus("current")


class _DocsPnmCmtsUtscCfgTriggerMode_Type(Integer32):
    """Custom type docsPnmCmtsUtscCfgTriggerMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("burstIuc", 8),
          ("cmMac", 6),
          ("freeRunning", 2),
          ("idleSid", 5),
          ("miniSlotCount", 3),
          ("other", 1),
          ("quietProbeSymbol", 7),
          ("sid", 4),
          ("timestamp", 9))
    )


_DocsPnmCmtsUtscCfgTriggerMode_Type.__name__ = "Integer32"
_DocsPnmCmtsUtscCfgTriggerMode_Object = MibTableColumn
docsPnmCmtsUtscCfgTriggerMode = _DocsPnmCmtsUtscCfgTriggerMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 3),
    _DocsPnmCmtsUtscCfgTriggerMode_Type()
)
docsPnmCmtsUtscCfgTriggerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgTriggerMode.setStatus("current")
_DocsPnmCmtsUtscCfgMinislotCount_Type = Unsigned32
_DocsPnmCmtsUtscCfgMinislotCount_Object = MibTableColumn
docsPnmCmtsUtscCfgMinislotCount = _DocsPnmCmtsUtscCfgMinislotCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 4),
    _DocsPnmCmtsUtscCfgMinislotCount_Type()
)
docsPnmCmtsUtscCfgMinislotCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgMinislotCount.setStatus("current")
_DocsPnmCmtsUtscCfgSid_Type = Unsigned32
_DocsPnmCmtsUtscCfgSid_Object = MibTableColumn
docsPnmCmtsUtscCfgSid = _DocsPnmCmtsUtscCfgSid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 5),
    _DocsPnmCmtsUtscCfgSid_Type()
)
docsPnmCmtsUtscCfgSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgSid.setStatus("current")
_DocsPnmCmtsUtscCfgCmMacAddr_Type = MacAddress
_DocsPnmCmtsUtscCfgCmMacAddr_Object = MibTableColumn
docsPnmCmtsUtscCfgCmMacAddr = _DocsPnmCmtsUtscCfgCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 6),
    _DocsPnmCmtsUtscCfgCmMacAddr_Type()
)
docsPnmCmtsUtscCfgCmMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgCmMacAddr.setStatus("current")
_DocsPnmCmtsUtscCfgTimestamp_Type = TimeStamp
_DocsPnmCmtsUtscCfgTimestamp_Object = MibTableColumn
docsPnmCmtsUtscCfgTimestamp = _DocsPnmCmtsUtscCfgTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 7),
    _DocsPnmCmtsUtscCfgTimestamp_Type()
)
docsPnmCmtsUtscCfgTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgTimestamp.setStatus("current")
_DocsPnmCmtsUtscCfgCenterFreq_Type = Unsigned32
_DocsPnmCmtsUtscCfgCenterFreq_Object = MibTableColumn
docsPnmCmtsUtscCfgCenterFreq = _DocsPnmCmtsUtscCfgCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 8),
    _DocsPnmCmtsUtscCfgCenterFreq_Type()
)
docsPnmCmtsUtscCfgCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgCenterFreq.setStatus("current")
_DocsPnmCmtsUtscCfgSpan_Type = Unsigned32
_DocsPnmCmtsUtscCfgSpan_Object = MibTableColumn
docsPnmCmtsUtscCfgSpan = _DocsPnmCmtsUtscCfgSpan_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 9),
    _DocsPnmCmtsUtscCfgSpan_Type()
)
docsPnmCmtsUtscCfgSpan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgSpan.setStatus("current")


class _DocsPnmCmtsUtscCfgNumBins_Type(Unsigned32):
    """Custom type docsPnmCmtsUtscCfgNumBins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsPnmCmtsUtscCfgNumBins_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUtscCfgNumBins_Object = MibTableColumn
docsPnmCmtsUtscCfgNumBins = _DocsPnmCmtsUtscCfgNumBins_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 10),
    _DocsPnmCmtsUtscCfgNumBins_Type()
)
docsPnmCmtsUtscCfgNumBins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgNumBins.setStatus("current")


class _DocsPnmCmtsUtscCfgAveraging_Type(Unsigned32):
    """Custom type docsPnmCmtsUtscCfgAveraging based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsPnmCmtsUtscCfgAveraging_Type.__name__ = "Unsigned32"
_DocsPnmCmtsUtscCfgAveraging_Object = MibTableColumn
docsPnmCmtsUtscCfgAveraging = _DocsPnmCmtsUtscCfgAveraging_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 11),
    _DocsPnmCmtsUtscCfgAveraging_Type()
)
docsPnmCmtsUtscCfgAveraging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgAveraging.setStatus("current")
_DocsPnmCmtsUtscCfgFilename_Type = SnmpAdminString
_DocsPnmCmtsUtscCfgFilename_Object = MibTableColumn
docsPnmCmtsUtscCfgFilename = _DocsPnmCmtsUtscCfgFilename_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 12),
    _DocsPnmCmtsUtscCfgFilename_Type()
)
docsPnmCmtsUtscCfgFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgFilename.setStatus("current")
_DocsPnmCmtsUtscCfgQualifyCenterFreq_Type = Unsigned32
_DocsPnmCmtsUtscCfgQualifyCenterFreq_Object = MibTableColumn
docsPnmCmtsUtscCfgQualifyCenterFreq = _DocsPnmCmtsUtscCfgQualifyCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 13),
    _DocsPnmCmtsUtscCfgQualifyCenterFreq_Type()
)
docsPnmCmtsUtscCfgQualifyCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgQualifyCenterFreq.setStatus("current")
_DocsPnmCmtsUtscCfgQualifyBw_Type = Unsigned32
_DocsPnmCmtsUtscCfgQualifyBw_Object = MibTableColumn
docsPnmCmtsUtscCfgQualifyBw = _DocsPnmCmtsUtscCfgQualifyBw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 14),
    _DocsPnmCmtsUtscCfgQualifyBw_Type()
)
docsPnmCmtsUtscCfgQualifyBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgQualifyBw.setStatus("current")
_DocsPnmCmtsUtscCfgQualifyThrshld_Type = Integer32
_DocsPnmCmtsUtscCfgQualifyThrshld_Object = MibTableColumn
docsPnmCmtsUtscCfgQualifyThrshld = _DocsPnmCmtsUtscCfgQualifyThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 15),
    _DocsPnmCmtsUtscCfgQualifyThrshld_Type()
)
docsPnmCmtsUtscCfgQualifyThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgQualifyThrshld.setStatus("current")


class _DocsPnmCmtsUtscCfgWindow_Type(Integer32):
    """Custom type docsPnmCmtsUtscCfgWindow based on Integer32"""
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
        *(("blackmanHarris", 4),
          ("chebyshev", 8),
          ("flatTop", 6),
          ("gaussian", 7),
          ("hamming", 5),
          ("hann", 3),
          ("other", 1),
          ("rectangular", 2))
    )


_DocsPnmCmtsUtscCfgWindow_Type.__name__ = "Integer32"
_DocsPnmCmtsUtscCfgWindow_Object = MibTableColumn
docsPnmCmtsUtscCfgWindow = _DocsPnmCmtsUtscCfgWindow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 16),
    _DocsPnmCmtsUtscCfgWindow_Type()
)
docsPnmCmtsUtscCfgWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgWindow.setStatus("current")


class _DocsPnmCmtsUtscCfgOutputFormat_Type(Integer32):
    """Custom type docsPnmCmtsUtscCfgOutputFormat based on Integer32"""
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
        *(("fftAmplitude", 5),
          ("fftDb", 6),
          ("fftIQ", 4),
          ("fftPower", 2),
          ("rawAdc", 3),
          ("timeIQ", 1))
    )


_DocsPnmCmtsUtscCfgOutputFormat_Type.__name__ = "Integer32"
_DocsPnmCmtsUtscCfgOutputFormat_Object = MibTableColumn
docsPnmCmtsUtscCfgOutputFormat = _DocsPnmCmtsUtscCfgOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 17),
    _DocsPnmCmtsUtscCfgOutputFormat_Type()
)
docsPnmCmtsUtscCfgOutputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgOutputFormat.setStatus("current")
_DocsPnmCmtsUtscCfgRepeatPeriod_Type = Unsigned32
_DocsPnmCmtsUtscCfgRepeatPeriod_Object = MibTableColumn
docsPnmCmtsUtscCfgRepeatPeriod = _DocsPnmCmtsUtscCfgRepeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 18),
    _DocsPnmCmtsUtscCfgRepeatPeriod_Type()
)
docsPnmCmtsUtscCfgRepeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgRepeatPeriod.setStatus("current")
_DocsPnmCmtsUtscCfgFreeRunDuration_Type = Unsigned32
_DocsPnmCmtsUtscCfgFreeRunDuration_Object = MibTableColumn
docsPnmCmtsUtscCfgFreeRunDuration = _DocsPnmCmtsUtscCfgFreeRunDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 19),
    _DocsPnmCmtsUtscCfgFreeRunDuration_Type()
)
docsPnmCmtsUtscCfgFreeRunDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgFreeRunDuration.setStatus("current")
_DocsPnmCmtsUtscCfgTriggerCount_Type = Unsigned32
_DocsPnmCmtsUtscCfgTriggerCount_Object = MibTableColumn
docsPnmCmtsUtscCfgTriggerCount = _DocsPnmCmtsUtscCfgTriggerCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 20),
    _DocsPnmCmtsUtscCfgTriggerCount_Type()
)
docsPnmCmtsUtscCfgTriggerCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgTriggerCount.setStatus("current")
_DocsPnmCmtsUtscCfgStatus_Type = RowStatus
_DocsPnmCmtsUtscCfgStatus_Object = MibTableColumn
docsPnmCmtsUtscCfgStatus = _DocsPnmCmtsUtscCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 2, 1, 21),
    _DocsPnmCmtsUtscCfgStatus_Type()
)
docsPnmCmtsUtscCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCfgStatus.setStatus("current")
_DocsPnmCmtsUtscCtrlTable_Object = MibTable
docsPnmCmtsUtscCtrlTable = _DocsPnmCmtsUtscCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 3)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCtrlTable.setStatus("current")
_DocsPnmCmtsUtscCtrlEntry_Object = MibTableRow
docsPnmCmtsUtscCtrlEntry = _DocsPnmCmtsUtscCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 3, 1)
)
docsPnmCmtsUtscCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsUtscCfgIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCtrlEntry.setStatus("current")
_DocsPnmCmtsUtscCtrlInitiateTest_Type = TruthValue
_DocsPnmCmtsUtscCtrlInitiateTest_Object = MibTableColumn
docsPnmCmtsUtscCtrlInitiateTest = _DocsPnmCmtsUtscCtrlInitiateTest_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 3, 1, 1),
    _DocsPnmCmtsUtscCtrlInitiateTest_Type()
)
docsPnmCmtsUtscCtrlInitiateTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscCtrlInitiateTest.setStatus("current")
_DocsPnmCmtsUtscStatusTable_Object = MibTable
docsPnmCmtsUtscStatusTable = _DocsPnmCmtsUtscStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 4)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscStatusTable.setStatus("current")
_DocsPnmCmtsUtscStatusEntry_Object = MibTableRow
docsPnmCmtsUtscStatusEntry = _DocsPnmCmtsUtscStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 4, 1)
)
docsPnmCmtsUtscStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsUtscCfgIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscStatusEntry.setStatus("current")
_DocsPnmCmtsUtscStatusMeasStatus_Type = MeasStatusType
_DocsPnmCmtsUtscStatusMeasStatus_Object = MibTableColumn
docsPnmCmtsUtscStatusMeasStatus = _DocsPnmCmtsUtscStatusMeasStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 4, 1, 1),
    _DocsPnmCmtsUtscStatusMeasStatus_Type()
)
docsPnmCmtsUtscStatusMeasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscStatusMeasStatus.setStatus("current")
_DocsPnmCmtsUtscResultTable_Object = MibTable
docsPnmCmtsUtscResultTable = _DocsPnmCmtsUtscResultTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 5)
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscResultTable.setStatus("current")
_DocsPnmCmtsUtscResultEntry_Object = MibTableRow
docsPnmCmtsUtscResultEntry = _DocsPnmCmtsUtscResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 5, 1)
)
docsPnmCmtsUtscResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsUtscCfgIndex"),
)
if mibBuilder.loadTexts:
    docsPnmCmtsUtscResultEntry.setStatus("current")
_DocsPnmCmtsUtscResultSampleRate_Type = Unsigned32
_DocsPnmCmtsUtscResultSampleRate_Object = MibTableColumn
docsPnmCmtsUtscResultSampleRate = _DocsPnmCmtsUtscResultSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 5, 1, 1),
    _DocsPnmCmtsUtscResultSampleRate_Type()
)
docsPnmCmtsUtscResultSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscResultSampleRate.setStatus("current")
_DocsPnmCmtsUtscResultUsSampleSize_Type = Unsigned32
_DocsPnmCmtsUtscResultUsSampleSize_Object = MibTableColumn
docsPnmCmtsUtscResultUsSampleSize = _DocsPnmCmtsUtscResultUsSampleSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 5, 1, 2),
    _DocsPnmCmtsUtscResultUsSampleSize_Type()
)
docsPnmCmtsUtscResultUsSampleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscResultUsSampleSize.setStatus("current")
_DocsPnmCmtsUtscResultSampleTimestamp_Type = TimeStamp
_DocsPnmCmtsUtscResultSampleTimestamp_Object = MibTableColumn
docsPnmCmtsUtscResultSampleTimestamp = _DocsPnmCmtsUtscResultSampleTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 5, 1, 3),
    _DocsPnmCmtsUtscResultSampleTimestamp_Type()
)
docsPnmCmtsUtscResultSampleTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscResultSampleTimestamp.setStatus("current")
_DocsPnmCmtsUtscResultResolutionBw_Type = Unsigned32
_DocsPnmCmtsUtscResultResolutionBw_Object = MibTableColumn
docsPnmCmtsUtscResultResolutionBw = _DocsPnmCmtsUtscResultResolutionBw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 5, 1, 4),
    _DocsPnmCmtsUtscResultResolutionBw_Type()
)
docsPnmCmtsUtscResultResolutionBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscResultResolutionBw.setStatus("current")
_DocsPnmCmtsUtscResultOutput_Type = OctetString
_DocsPnmCmtsUtscResultOutput_Object = MibTableColumn
docsPnmCmtsUtscResultOutput = _DocsPnmCmtsUtscResultOutput_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 1, 3, 10, 5, 1, 5),
    _DocsPnmCmtsUtscResultOutput_Type()
)
docsPnmCmtsUtscResultOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsPnmCmtsUtscResultOutput.setStatus("current")
_DocsPnmMibConformance_ObjectIdentity = ObjectIdentity
docsPnmMibConformance = _DocsPnmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2)
)
_DocsPnmMibCompliances_ObjectIdentity = ObjectIdentity
docsPnmMibCompliances = _DocsPnmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 1)
)
_DocsPnmMibGroups_ObjectIdentity = ObjectIdentity
docsPnmMibGroups = _DocsPnmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 2)
)

# Managed Objects groups

docsPnmBulkDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 2, 1)
)
docsPnmBulkDataGroup.setObjects(
      *(("DOCS-PNM-MIB", "docsPnmBulkDestIpAddrType"),
        ("DOCS-PNM-MIB", "docsPnmBulkDestIpAddr"),
        ("DOCS-PNM-MIB", "docsPnmBulkDestPath"),
        ("DOCS-PNM-MIB", "docsPnmBulkUploadControl"),
        ("DOCS-PNM-MIB", "docsPnmBulkFileName"),
        ("DOCS-PNM-MIB", "docsPnmBulkFileControl"),
        ("DOCS-PNM-MIB", "docsPnmBulkFileUploadStatus"))
)
if mibBuilder.loadTexts:
    docsPnmBulkDataGroup.setStatus("current")

docsPnmCmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 2, 2)
)
docsPnmCmtsGroup.setObjects(
      *(("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymTrigEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymTrigGroupId"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymFirstActSubCarIdx"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymLastActSubCarIdx"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymRxWindowing"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymTransactionId"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymSampleRate"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymFftLength"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmSymCaptFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmNprStartSubcar"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmNprStopSubcar"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmNprEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmtsDsOfdmNprDuration"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeCmMacAddr"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeUseIdleSid"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbePreEqOn"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeTimeout"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeNumSymToCapt"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeNumSamples"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeTimeStamp"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaAQProbeFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseFreeRunDuration"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseStTrigLvl"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseEndTrigLvl"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseCenterFrq"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseMeasBw"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseNumEvtsCnted"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseLastEvtTimeStamp"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseLastEvtDuration"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseLastEvtAvgPwr"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsImpNoiseFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsHistEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsHistTimeOut"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsHistMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsHistFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxPwrEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxPwrPreEq"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxPwrNumAvgs"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxPwrOnePtSixPsd"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxPwrMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxMerEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxMerCmMac"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxMerPreEq"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxMerNumAvgs"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxMerMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsOfdmaRxMerFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqOpCode"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqProfileTest"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqMaxDuration"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqMaxCodewords"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqMaxUncorrectableCws"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqCwTaggingEnabled"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqNcpFields"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqMaxNcpCrcFails"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptReqStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptMerThreshCfgRxMerMargin"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptMerThreshCfgStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptProfChgCfgDsProfList"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptProfChgCfgStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespFirstActiveSubcarrierNum"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespMerData"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespMerPassFailData"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespNumSubcarriersBelowThresh"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespSnrMarginData"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespCodewordCt"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespCorrectedCodewordCt"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespUncorrectableCodewordCt"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespNcpFieldCt"),
        ("DOCS-PNM-MIB", "docsPnmCmtsOptRespNcpCrcFailCt"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCapabTriggerMode"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCapabOutputFormat"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCapabWindow"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCapabDescription"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgLogicalChIfIndex"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgTriggerMode"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgMinislotCount"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgSid"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgCmMacAddr"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgTimestamp"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgCenterFreq"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgSpan"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgNumBins"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgAveraging"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgFilename"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgQualifyCenterFreq"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgQualifyBw"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgQualifyThrshld"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgWindow"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgOutputFormat"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgRepeatPeriod"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgFreeRunDuration"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgTriggerCount"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCfgStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscCtrlInitiateTest"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscStatusMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscResultSampleRate"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscResultUsSampleSize"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscResultSampleTimestamp"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscResultResolutionBw"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUtscResultOutput"))
)
if mibBuilder.loadTexts:
    docsPnmCmtsGroup.setStatus("current")

docsPnmCmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 2, 3)
)
docsPnmCmGroup.setObjects(
      *(("DOCS-PNM-MIB", "docsPnmCmCtlTest"),
        ("DOCS-PNM-MIB", "docsPnmCmCtlTestDuration"),
        ("DOCS-PNM-MIB", "docsPnmCmCtlStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymTrigEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymTrigEnableTimeout"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymTrigGroupId"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymRxWindowing"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymTransactionId"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymSampleRate"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymFftLength"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmSymCaptFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefTrigEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefAmpRipplePkToPk"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefAmpRippleRms"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefAmpSlope"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefGrpDelayRippleRms"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefAmpMean"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefGrpDelaySlope"),
        ("DOCS-PNM-MIB", "docsPnmCmOfdmChEstCoefGrpDelayMean"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmModProfFileEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmModProfMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmModProfFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmDsConstDispTrigEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmDsConstDispModOrderOffset"),
        ("DOCS-PNM-MIB", "docsPnmCmDsConstDispNumSampleSymb"),
        ("DOCS-PNM-MIB", "docsPnmCmDsConstDispSelModOrder"),
        ("DOCS-PNM-MIB", "docsPnmCmDsConstDispMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmDsConstDispFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmRxMerFileEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmRxMerPercentile"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmRxMerMean"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmRxMerStdDev"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmRxMerThrVal"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmRxMerThrHighestFreq"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmRxMerMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmRxMerFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarProfileId"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarThrshldOffset"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarMeasEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarReqAvgMer"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarNumSubCarBelowThrshld"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarMeasuredAvgMer"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmMerMarAvgMerMargin"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmFecSumType"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmFecFileEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmFecMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmFecFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam16"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam64"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam128"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam256"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam512"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam1024"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam2048"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam4096"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam8192"),
        ("DOCS-PNM-MIB", "docsPnmCmDsOfdmReqMerQam16384"),
        ("DOCS-PNM-MIB", "docsPnmCmDsHistEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmDsHistTimeOut"),
        ("DOCS-PNM-MIB", "docsPnmCmDsHistMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmDsHistFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqFileEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqAmpRipplePkToPk"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqAmpRippleRms"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqAmpSlope"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqGrpDelayRipplePkToPk"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqGrpDelayRippleRms"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqPreEqCoAdjStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqLastUpdateFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqFileName"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqAmpMean"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqGrpDelaySlope"),
        ("DOCS-PNM-MIB", "docsPnmCmUsPreEqGrpDelayMean"),
        ("DOCS-PNM-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdFileEnable"),
        ("DOCS-PNM-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdMeasStatus"),
        ("DOCS-PNM-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdFileName"))
)
if mibBuilder.loadTexts:
    docsPnmCmGroup.setStatus("current")

docsPnmCmtsDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 2, 4)
)
docsPnmCmtsDeprecatedGroup.setObjects(
      *(("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnEnable"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnTrigMode"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnMiniSlotCnt"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnSid"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnMiniSlotNum"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnCmMac"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnCenterFreq"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnSpan"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnNumberOfBins"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnMeasStatus"),
        ("DOCS-PNM-MIB", "docsPnmCmtsUsSpecAnFileName"))
)
if mibBuilder.loadTexts:
    docsPnmCmtsDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsPnmCmtsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsPnmCmtsCompliance.setStatus(
        "current"
    )

docsPnmCmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 1, 2)
)
if mibBuilder.loadTexts:
    docsPnmCmCompliance.setStatus(
        "current"
    )

docsPnmCmtsDeprecatedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 27, 2, 1, 3)
)
if mibBuilder.loadTexts:
    docsPnmCmtsDeprecatedCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-PNM-MIB",
    **{"MeasStatusType": MeasStatusType,
       "ThousandthdB": ThousandthdB,
       "UsOfdmaWindowingSizeType": UsOfdmaWindowingSizeType,
       "docsIf3CmSpectrumAnalysisCtrlCmdFileEnable": docsIf3CmSpectrumAnalysisCtrlCmdFileEnable,
       "docsIf3CmSpectrumAnalysisCtrlCmdMeasStatus": docsIf3CmSpectrumAnalysisCtrlCmdMeasStatus,
       "docsIf3CmSpectrumAnalysisCtrlCmdFileName": docsIf3CmSpectrumAnalysisCtrlCmdFileName,
       "docsPnmMIB": docsPnmMIB,
       "docsPnmNotifications": docsPnmNotifications,
       "docsPnmMibObjects": docsPnmMibObjects,
       "docsPnmBulkData": docsPnmBulkData,
       "docsPnmBulkCtl": docsPnmBulkCtl,
       "docsPnmBulkDestIpAddrType": docsPnmBulkDestIpAddrType,
       "docsPnmBulkDestIpAddr": docsPnmBulkDestIpAddr,
       "docsPnmBulkDestPath": docsPnmBulkDestPath,
       "docsPnmBulkUploadControl": docsPnmBulkUploadControl,
       "docsPnmBulkFileTable": docsPnmBulkFileTable,
       "docsPnmBulkFileEntry": docsPnmBulkFileEntry,
       "docsPnmBulkFileIndex": docsPnmBulkFileIndex,
       "docsPnmBulkFileName": docsPnmBulkFileName,
       "docsPnmBulkFileControl": docsPnmBulkFileControl,
       "docsPnmBulkFileUploadStatus": docsPnmBulkFileUploadStatus,
       "docsPnmCmObjects": docsPnmCmObjects,
       "docsPnmCmControlObjects": docsPnmCmControlObjects,
       "docsPnmCmCtlTest": docsPnmCmCtlTest,
       "docsPnmCmCtlTestDuration": docsPnmCmCtlTestDuration,
       "docsPnmCmCtlStatus": docsPnmCmCtlStatus,
       "docsPnmCmDsOfdmSymCapTable": docsPnmCmDsOfdmSymCapTable,
       "docsPnmCmDsOfdmSymCapEntry": docsPnmCmDsOfdmSymCapEntry,
       "docsPnmCmDsOfdmSymTrigEnable": docsPnmCmDsOfdmSymTrigEnable,
       "docsPnmCmDsOfdmSymTrigEnableTimeout": docsPnmCmDsOfdmSymTrigEnableTimeout,
       "docsPnmCmDsOfdmSymTrigGroupId": docsPnmCmDsOfdmSymTrigGroupId,
       "docsPnmCmDsOfdmSymRxWindowing": docsPnmCmDsOfdmSymRxWindowing,
       "docsPnmCmDsOfdmSymTransactionId": docsPnmCmDsOfdmSymTransactionId,
       "docsPnmCmDsOfdmSymSampleRate": docsPnmCmDsOfdmSymSampleRate,
       "docsPnmCmDsOfdmSymFftLength": docsPnmCmDsOfdmSymFftLength,
       "docsPnmCmDsOfdmSymMeasStatus": docsPnmCmDsOfdmSymMeasStatus,
       "docsPnmCmDsOfdmSymCaptFileName": docsPnmCmDsOfdmSymCaptFileName,
       "docsPnmCmOfdmChanEstCoefTable": docsPnmCmOfdmChanEstCoefTable,
       "docsPnmCmOfdmChanEstCoefEntry": docsPnmCmOfdmChanEstCoefEntry,
       "docsPnmCmOfdmChEstCoefTrigEnable": docsPnmCmOfdmChEstCoefTrigEnable,
       "docsPnmCmOfdmChEstCoefAmpRipplePkToPk": docsPnmCmOfdmChEstCoefAmpRipplePkToPk,
       "docsPnmCmOfdmChEstCoefAmpRippleRms": docsPnmCmOfdmChEstCoefAmpRippleRms,
       "docsPnmCmOfdmChEstCoefAmpSlope": docsPnmCmOfdmChEstCoefAmpSlope,
       "docsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk": docsPnmCmOfdmChEstCoefGrpDelayRipplePkToPk,
       "docsPnmCmOfdmChEstCoefGrpDelayRippleRms": docsPnmCmOfdmChEstCoefGrpDelayRippleRms,
       "docsPnmCmOfdmChEstCoefMeasStatus": docsPnmCmOfdmChEstCoefMeasStatus,
       "docsPnmCmOfdmChEstCoefFileName": docsPnmCmOfdmChEstCoefFileName,
       "docsPnmCmOfdmChEstCoefAmpMean": docsPnmCmOfdmChEstCoefAmpMean,
       "docsPnmCmOfdmChEstCoefGrpDelaySlope": docsPnmCmOfdmChEstCoefGrpDelaySlope,
       "docsPnmCmOfdmChEstCoefGrpDelayMean": docsPnmCmOfdmChEstCoefGrpDelayMean,
       "docsPnmCmDsConstDispMeasTable": docsPnmCmDsConstDispMeasTable,
       "docsPnmCmDsConstDispMeasEntry": docsPnmCmDsConstDispMeasEntry,
       "docsPnmCmDsConstDispTrigEnable": docsPnmCmDsConstDispTrigEnable,
       "docsPnmCmDsConstDispModOrderOffset": docsPnmCmDsConstDispModOrderOffset,
       "docsPnmCmDsConstDispNumSampleSymb": docsPnmCmDsConstDispNumSampleSymb,
       "docsPnmCmDsConstDispSelModOrder": docsPnmCmDsConstDispSelModOrder,
       "docsPnmCmDsConstDispMeasStatus": docsPnmCmDsConstDispMeasStatus,
       "docsPnmCmDsConstDispFileName": docsPnmCmDsConstDispFileName,
       "docsPnmCmDsOfdmRxMerTable": docsPnmCmDsOfdmRxMerTable,
       "docsPnmCmDsOfdmRxMerEntry": docsPnmCmDsOfdmRxMerEntry,
       "docsPnmCmDsOfdmRxMerFileEnable": docsPnmCmDsOfdmRxMerFileEnable,
       "docsPnmCmDsOfdmRxMerPercentile": docsPnmCmDsOfdmRxMerPercentile,
       "docsPnmCmDsOfdmRxMerMean": docsPnmCmDsOfdmRxMerMean,
       "docsPnmCmDsOfdmRxMerStdDev": docsPnmCmDsOfdmRxMerStdDev,
       "docsPnmCmDsOfdmRxMerThrVal": docsPnmCmDsOfdmRxMerThrVal,
       "docsPnmCmDsOfdmRxMerThrHighestFreq": docsPnmCmDsOfdmRxMerThrHighestFreq,
       "docsPnmCmDsOfdmRxMerMeasStatus": docsPnmCmDsOfdmRxMerMeasStatus,
       "docsPnmCmDsOfdmRxMerFileName": docsPnmCmDsOfdmRxMerFileName,
       "docsPnmCmDsOfdmMerMarTable": docsPnmCmDsOfdmMerMarTable,
       "docsPnmCmDsOfdmMerMarEntry": docsPnmCmDsOfdmMerMarEntry,
       "docsPnmCmDsOfdmMerMarProfileId": docsPnmCmDsOfdmMerMarProfileId,
       "docsPnmCmDsOfdmMerMarThrshldOffset": docsPnmCmDsOfdmMerMarThrshldOffset,
       "docsPnmCmDsOfdmMerMarMeasEnable": docsPnmCmDsOfdmMerMarMeasEnable,
       "docsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg": docsPnmCmDsOfdmMerMarNumSymPerSubCarToAvg,
       "docsPnmCmDsOfdmMerMarReqAvgMer": docsPnmCmDsOfdmMerMarReqAvgMer,
       "docsPnmCmDsOfdmMerMarNumSubCarBelowThrshld": docsPnmCmDsOfdmMerMarNumSubCarBelowThrshld,
       "docsPnmCmDsOfdmMerMarMeasuredAvgMer": docsPnmCmDsOfdmMerMarMeasuredAvgMer,
       "docsPnmCmDsOfdmMerMarAvgMerMargin": docsPnmCmDsOfdmMerMarAvgMerMargin,
       "docsPnmCmDsOfdmMerMarMeasStatus": docsPnmCmDsOfdmMerMarMeasStatus,
       "docsPnmCmDsOfdmFecTable": docsPnmCmDsOfdmFecTable,
       "docsPnmCmDsOfdmFecEntry": docsPnmCmDsOfdmFecEntry,
       "docsPnmCmDsOfdmFecSumType": docsPnmCmDsOfdmFecSumType,
       "docsPnmCmDsOfdmFecFileEnable": docsPnmCmDsOfdmFecFileEnable,
       "docsPnmCmDsOfdmFecMeasStatus": docsPnmCmDsOfdmFecMeasStatus,
       "docsPnmCmDsOfdmFecFileName": docsPnmCmDsOfdmFecFileName,
       "docsPnmCmDsOfdmReqMERObjects": docsPnmCmDsOfdmReqMERObjects,
       "docsPnmCmDsOfdmReqMerQam16": docsPnmCmDsOfdmReqMerQam16,
       "docsPnmCmDsOfdmReqMerQam64": docsPnmCmDsOfdmReqMerQam64,
       "docsPnmCmDsOfdmReqMerQam128": docsPnmCmDsOfdmReqMerQam128,
       "docsPnmCmDsOfdmReqMerQam256": docsPnmCmDsOfdmReqMerQam256,
       "docsPnmCmDsOfdmReqMerQam512": docsPnmCmDsOfdmReqMerQam512,
       "docsPnmCmDsOfdmReqMerQam1024": docsPnmCmDsOfdmReqMerQam1024,
       "docsPnmCmDsOfdmReqMerQam2048": docsPnmCmDsOfdmReqMerQam2048,
       "docsPnmCmDsOfdmReqMerQam4096": docsPnmCmDsOfdmReqMerQam4096,
       "docsPnmCmDsOfdmReqMerQam8192": docsPnmCmDsOfdmReqMerQam8192,
       "docsPnmCmDsOfdmReqMerQam16384": docsPnmCmDsOfdmReqMerQam16384,
       "docsPnmCmDsHistTable": docsPnmCmDsHistTable,
       "docsPnmCmDsHistEntry": docsPnmCmDsHistEntry,
       "docsPnmCmDsHistEnable": docsPnmCmDsHistEnable,
       "docsPnmCmDsHistTimeOut": docsPnmCmDsHistTimeOut,
       "docsPnmCmDsHistMeasStatus": docsPnmCmDsHistMeasStatus,
       "docsPnmCmDsHistFileName": docsPnmCmDsHistFileName,
       "docsPnmCmUsPreEqTable": docsPnmCmUsPreEqTable,
       "docsPnmCmUsPreEqEntry": docsPnmCmUsPreEqEntry,
       "docsPnmCmUsPreEqFileEnable": docsPnmCmUsPreEqFileEnable,
       "docsPnmCmUsPreEqAmpRipplePkToPk": docsPnmCmUsPreEqAmpRipplePkToPk,
       "docsPnmCmUsPreEqAmpRippleRms": docsPnmCmUsPreEqAmpRippleRms,
       "docsPnmCmUsPreEqAmpSlope": docsPnmCmUsPreEqAmpSlope,
       "docsPnmCmUsPreEqGrpDelayRipplePkToPk": docsPnmCmUsPreEqGrpDelayRipplePkToPk,
       "docsPnmCmUsPreEqGrpDelayRippleRms": docsPnmCmUsPreEqGrpDelayRippleRms,
       "docsPnmCmUsPreEqPreEqCoAdjStatus": docsPnmCmUsPreEqPreEqCoAdjStatus,
       "docsPnmCmUsPreEqMeasStatus": docsPnmCmUsPreEqMeasStatus,
       "docsPnmCmUsPreEqLastUpdateFileName": docsPnmCmUsPreEqLastUpdateFileName,
       "docsPnmCmUsPreEqFileName": docsPnmCmUsPreEqFileName,
       "docsPnmCmUsPreEqAmpMean": docsPnmCmUsPreEqAmpMean,
       "docsPnmCmUsPreEqGrpDelaySlope": docsPnmCmUsPreEqGrpDelaySlope,
       "docsPnmCmUsPreEqGrpDelayMean": docsPnmCmUsPreEqGrpDelayMean,
       "docsPnmCmDsOfdmModProfTable": docsPnmCmDsOfdmModProfTable,
       "docsPnmCmDsOfdmModProfEntry": docsPnmCmDsOfdmModProfEntry,
       "docsPnmCmDsOfdmModProfFileEnable": docsPnmCmDsOfdmModProfFileEnable,
       "docsPnmCmDsOfdmModProfMeasStatus": docsPnmCmDsOfdmModProfMeasStatus,
       "docsPnmCmDsOfdmModProfFileName": docsPnmCmDsOfdmModProfFileName,
       "docsPnmCmtsObjects": docsPnmCmtsObjects,
       "docsPnmCmtsDsOfdmSymCapTable": docsPnmCmtsDsOfdmSymCapTable,
       "docsPnmCmtsDsOfdmSymCapEntry": docsPnmCmtsDsOfdmSymCapEntry,
       "docsPnmCmtsDsOfdmSymTrigEnable": docsPnmCmtsDsOfdmSymTrigEnable,
       "docsPnmCmtsDsOfdmSymTrigGroupId": docsPnmCmtsDsOfdmSymTrigGroupId,
       "docsPnmCmtsDsOfdmSymFirstActSubCarIdx": docsPnmCmtsDsOfdmSymFirstActSubCarIdx,
       "docsPnmCmtsDsOfdmSymLastActSubCarIdx": docsPnmCmtsDsOfdmSymLastActSubCarIdx,
       "docsPnmCmtsDsOfdmSymRxWindowing": docsPnmCmtsDsOfdmSymRxWindowing,
       "docsPnmCmtsDsOfdmSymTransactionId": docsPnmCmtsDsOfdmSymTransactionId,
       "docsPnmCmtsDsOfdmSymSampleRate": docsPnmCmtsDsOfdmSymSampleRate,
       "docsPnmCmtsDsOfdmSymFftLength": docsPnmCmtsDsOfdmSymFftLength,
       "docsPnmCmtsDsOfdmSymMeasStatus": docsPnmCmtsDsOfdmSymMeasStatus,
       "docsPnmCmtsDsOfdmSymCaptFileName": docsPnmCmtsDsOfdmSymCaptFileName,
       "docsPnmCmtsDsOfdmNoisePwrRatioTable": docsPnmCmtsDsOfdmNoisePwrRatioTable,
       "docsPnmCmtsDsOfdmNoisePwrRatioEntry": docsPnmCmtsDsOfdmNoisePwrRatioEntry,
       "docsPnmCmtsDsOfdmNprStartSubcar": docsPnmCmtsDsOfdmNprStartSubcar,
       "docsPnmCmtsDsOfdmNprStopSubcar": docsPnmCmtsDsOfdmNprStopSubcar,
       "docsPnmCmtsDsOfdmNprEnable": docsPnmCmtsDsOfdmNprEnable,
       "docsPnmCmtsDsOfdmNprDuration": docsPnmCmtsDsOfdmNprDuration,
       "docsPnmCmtsUsOfdmaAQProbeTable": docsPnmCmtsUsOfdmaAQProbeTable,
       "docsPnmCmtsUsOfdmaAQProbeEntry": docsPnmCmtsUsOfdmaAQProbeEntry,
       "docsPnmCmtsUsOfdmaAQProbeCmMacAddr": docsPnmCmtsUsOfdmaAQProbeCmMacAddr,
       "docsPnmCmtsUsOfdmaAQProbeUseIdleSid": docsPnmCmtsUsOfdmaAQProbeUseIdleSid,
       "docsPnmCmtsUsOfdmaAQProbePreEqOn": docsPnmCmtsUsOfdmaAQProbePreEqOn,
       "docsPnmCmtsUsOfdmaAQProbeEnable": docsPnmCmtsUsOfdmaAQProbeEnable,
       "docsPnmCmtsUsOfdmaAQProbeTimeout": docsPnmCmtsUsOfdmaAQProbeTimeout,
       "docsPnmCmtsUsOfdmaAQProbeNumSymToCapt": docsPnmCmtsUsOfdmaAQProbeNumSymToCapt,
       "docsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols": docsPnmCmtsUsOfdmaAQProbeMaxCaptSymbols,
       "docsPnmCmtsUsOfdmaAQProbeNumSamples": docsPnmCmtsUsOfdmaAQProbeNumSamples,
       "docsPnmCmtsUsOfdmaAQProbeTimeStamp": docsPnmCmtsUsOfdmaAQProbeTimeStamp,
       "docsPnmCmtsUsOfdmaAQProbeMeasStatus": docsPnmCmtsUsOfdmaAQProbeMeasStatus,
       "docsPnmCmtsUsOfdmaAQProbeFileName": docsPnmCmtsUsOfdmaAQProbeFileName,
       "docsPnmCmtsUsImpNoiseTable": docsPnmCmtsUsImpNoiseTable,
       "docsPnmCmtsUsImpNoiseEntry": docsPnmCmtsUsImpNoiseEntry,
       "docsPnmCmtsUsImpNoiseEnable": docsPnmCmtsUsImpNoiseEnable,
       "docsPnmCmtsUsImpNoiseFreeRunDuration": docsPnmCmtsUsImpNoiseFreeRunDuration,
       "docsPnmCmtsUsImpNoiseStTrigLvl": docsPnmCmtsUsImpNoiseStTrigLvl,
       "docsPnmCmtsUsImpNoiseEndTrigLvl": docsPnmCmtsUsImpNoiseEndTrigLvl,
       "docsPnmCmtsUsImpNoiseCenterFrq": docsPnmCmtsUsImpNoiseCenterFrq,
       "docsPnmCmtsUsImpNoiseMeasBw": docsPnmCmtsUsImpNoiseMeasBw,
       "docsPnmCmtsUsImpNoiseNumEvtsCnted": docsPnmCmtsUsImpNoiseNumEvtsCnted,
       "docsPnmCmtsUsImpNoiseLastEvtTimeStamp": docsPnmCmtsUsImpNoiseLastEvtTimeStamp,
       "docsPnmCmtsUsImpNoiseLastEvtDuration": docsPnmCmtsUsImpNoiseLastEvtDuration,
       "docsPnmCmtsUsImpNoiseLastEvtAvgPwr": docsPnmCmtsUsImpNoiseLastEvtAvgPwr,
       "docsPnmCmtsUsImpNoiseMeasStatus": docsPnmCmtsUsImpNoiseMeasStatus,
       "docsPnmCmtsUsImpNoiseFileName": docsPnmCmtsUsImpNoiseFileName,
       "docsPnmCmtsUsHistTable": docsPnmCmtsUsHistTable,
       "docsPnmCmtsUsHistEntry": docsPnmCmtsUsHistEntry,
       "docsPnmCmtsUsHistEnable": docsPnmCmtsUsHistEnable,
       "docsPnmCmtsUsHistTimeOut": docsPnmCmtsUsHistTimeOut,
       "docsPnmCmtsUsHistMeasStatus": docsPnmCmtsUsHistMeasStatus,
       "docsPnmCmtsUsHistFileName": docsPnmCmtsUsHistFileName,
       "docsPnmCmtsUsOfdmaRxPwrTable": docsPnmCmtsUsOfdmaRxPwrTable,
       "docsPnmCmtsUsOfdmaRxPwrEntry": docsPnmCmtsUsOfdmaRxPwrEntry,
       "docsPnmCmtsUsOfdmaRxPwrEnable": docsPnmCmtsUsOfdmaRxPwrEnable,
       "docsPnmCmtsUsOfdmaRxPwrCmMac": docsPnmCmtsUsOfdmaRxPwrCmMac,
       "docsPnmCmtsUsOfdmaRxPwrPreEq": docsPnmCmtsUsOfdmaRxPwrPreEq,
       "docsPnmCmtsUsOfdmaRxPwrNumAvgs": docsPnmCmtsUsOfdmaRxPwrNumAvgs,
       "docsPnmCmtsUsOfdmaRxPwrOnePtSixPsd": docsPnmCmtsUsOfdmaRxPwrOnePtSixPsd,
       "docsPnmCmtsUsOfdmaRxPwrMeasStatus": docsPnmCmtsUsOfdmaRxPwrMeasStatus,
       "docsPnmCmtsUsOfdmaRxMerTable": docsPnmCmtsUsOfdmaRxMerTable,
       "docsPnmCmtsUsOfdmaRxMerEntry": docsPnmCmtsUsOfdmaRxMerEntry,
       "docsPnmCmtsUsOfdmaRxMerEnable": docsPnmCmtsUsOfdmaRxMerEnable,
       "docsPnmCmtsUsOfdmaRxMerCmMac": docsPnmCmtsUsOfdmaRxMerCmMac,
       "docsPnmCmtsUsOfdmaRxMerPreEq": docsPnmCmtsUsOfdmaRxMerPreEq,
       "docsPnmCmtsUsOfdmaRxMerNumAvgs": docsPnmCmtsUsOfdmaRxMerNumAvgs,
       "docsPnmCmtsUsOfdmaRxMerMeasStatus": docsPnmCmtsUsOfdmaRxMerMeasStatus,
       "docsPnmCmtsUsOfdmaRxMerFileName": docsPnmCmtsUsOfdmaRxMerFileName,
       "docsPnmCmtsUsSpecAnTable": docsPnmCmtsUsSpecAnTable,
       "docsPnmCmtsUsSpecAnEntry": docsPnmCmtsUsSpecAnEntry,
       "docsPnmCmtsUsSpecAnEnable": docsPnmCmtsUsSpecAnEnable,
       "docsPnmCmtsUsSpecAnTrigMode": docsPnmCmtsUsSpecAnTrigMode,
       "docsPnmCmtsUsSpecAnMiniSlotCnt": docsPnmCmtsUsSpecAnMiniSlotCnt,
       "docsPnmCmtsUsSpecAnSid": docsPnmCmtsUsSpecAnSid,
       "docsPnmCmtsUsSpecAnMiniSlotNum": docsPnmCmtsUsSpecAnMiniSlotNum,
       "docsPnmCmtsUsSpecAnCmMac": docsPnmCmtsUsSpecAnCmMac,
       "docsPnmCmtsUsSpecAnCenterFreq": docsPnmCmtsUsSpecAnCenterFreq,
       "docsPnmCmtsUsSpecAnSpan": docsPnmCmtsUsSpecAnSpan,
       "docsPnmCmtsUsSpecAnNumberOfBins": docsPnmCmtsUsSpecAnNumberOfBins,
       "docsPnmCmtsUsSpecAnMeasStatus": docsPnmCmtsUsSpecAnMeasStatus,
       "docsPnmCmtsUsSpecAnFileName": docsPnmCmtsUsSpecAnFileName,
       "docsPnmCmtsOptObjects": docsPnmCmtsOptObjects,
       "docsPnmCmtsOptReqTable": docsPnmCmtsOptReqTable,
       "docsPnmCmtsOptReqEntry": docsPnmCmtsOptReqEntry,
       "docsPnmCmtsOptReqCmMacAddr": docsPnmCmtsOptReqCmMacAddr,
       "docsPnmCmtsOptReqDsOfdmChanCfgIndex": docsPnmCmtsOptReqDsOfdmChanCfgIndex,
       "docsPnmCmtsOptReqDsOfdmProfCfgId": docsPnmCmtsOptReqDsOfdmProfCfgId,
       "docsPnmCmtsOptReqOpCode": docsPnmCmtsOptReqOpCode,
       "docsPnmCmtsOptReqProfileTest": docsPnmCmtsOptReqProfileTest,
       "docsPnmCmtsOptReqMaxDuration": docsPnmCmtsOptReqMaxDuration,
       "docsPnmCmtsOptReqMaxCodewords": docsPnmCmtsOptReqMaxCodewords,
       "docsPnmCmtsOptReqMaxUncorrectableCws": docsPnmCmtsOptReqMaxUncorrectableCws,
       "docsPnmCmtsOptReqCwTaggingEnabled": docsPnmCmtsOptReqCwTaggingEnabled,
       "docsPnmCmtsOptReqNcpFields": docsPnmCmtsOptReqNcpFields,
       "docsPnmCmtsOptReqMaxNcpCrcFails": docsPnmCmtsOptReqMaxNcpCrcFails,
       "docsPnmCmtsOptReqStatus": docsPnmCmtsOptReqStatus,
       "docsPnmCmtsOptMerThreshCfgTable": docsPnmCmtsOptMerThreshCfgTable,
       "docsPnmCmtsOptMerThreshCfgEntry": docsPnmCmtsOptMerThreshCfgEntry,
       "docsPnmCmtsOptMerThreshCfgModOrder": docsPnmCmtsOptMerThreshCfgModOrder,
       "docsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget": docsPnmCmtsOptMerThreshCfgRxMerVsBitloadingTarget,
       "docsPnmCmtsOptMerThreshCfgRxMerMargin": docsPnmCmtsOptMerThreshCfgRxMerMargin,
       "docsPnmCmtsOptMerThreshCfgStatus": docsPnmCmtsOptMerThreshCfgStatus,
       "docsPnmCmtsOptProfChgCfgTable": docsPnmCmtsOptProfChgCfgTable,
       "docsPnmCmtsOptProfChgCfgEntry": docsPnmCmtsOptProfChgCfgEntry,
       "docsPnmCmtsOptProfChgCfgIfIndex": docsPnmCmtsOptProfChgCfgIfIndex,
       "docsPnmCmtsOptProfChgCfgDsProfList": docsPnmCmtsOptProfChgCfgDsProfList,
       "docsPnmCmtsOptProfChgCfgStatus": docsPnmCmtsOptProfChgCfgStatus,
       "docsPnmCmtsOptRespTable": docsPnmCmtsOptRespTable,
       "docsPnmCmtsOptRespEntry": docsPnmCmtsOptRespEntry,
       "docsPnmCmtsOptRespStatus": docsPnmCmtsOptRespStatus,
       "docsPnmCmtsOptRespFirstActiveSubcarrierNum": docsPnmCmtsOptRespFirstActiveSubcarrierNum,
       "docsPnmCmtsOptRespMerData": docsPnmCmtsOptRespMerData,
       "docsPnmCmtsOptRespMerPassFailData": docsPnmCmtsOptRespMerPassFailData,
       "docsPnmCmtsOptRespNumSubcarriersBelowThresh": docsPnmCmtsOptRespNumSubcarriersBelowThresh,
       "docsPnmCmtsOptRespSnrMarginData": docsPnmCmtsOptRespSnrMarginData,
       "docsPnmCmtsOptRespCodewordCt": docsPnmCmtsOptRespCodewordCt,
       "docsPnmCmtsOptRespCorrectedCodewordCt": docsPnmCmtsOptRespCorrectedCodewordCt,
       "docsPnmCmtsOptRespUncorrectableCodewordCt": docsPnmCmtsOptRespUncorrectableCodewordCt,
       "docsPnmCmtsOptRespNcpFieldCt": docsPnmCmtsOptRespNcpFieldCt,
       "docsPnmCmtsOptRespNcpCrcFailCt": docsPnmCmtsOptRespNcpCrcFailCt,
       "docsPnmCmtsUtscObjects": docsPnmCmtsUtscObjects,
       "docsPnmCmtsUtscCapabTable": docsPnmCmtsUtscCapabTable,
       "docsPnmCmtsUtscCapabEntry": docsPnmCmtsUtscCapabEntry,
       "docsPnmCmtsUtscCapabTriggerMode": docsPnmCmtsUtscCapabTriggerMode,
       "docsPnmCmtsUtscCapabOutputFormat": docsPnmCmtsUtscCapabOutputFormat,
       "docsPnmCmtsUtscCapabWindow": docsPnmCmtsUtscCapabWindow,
       "docsPnmCmtsUtscCapabDescription": docsPnmCmtsUtscCapabDescription,
       "docsPnmCmtsUtscCfgTable": docsPnmCmtsUtscCfgTable,
       "docsPnmCmtsUtscCfgEntry": docsPnmCmtsUtscCfgEntry,
       "docsPnmCmtsUtscCfgIndex": docsPnmCmtsUtscCfgIndex,
       "docsPnmCmtsUtscCfgLogicalChIfIndex": docsPnmCmtsUtscCfgLogicalChIfIndex,
       "docsPnmCmtsUtscCfgTriggerMode": docsPnmCmtsUtscCfgTriggerMode,
       "docsPnmCmtsUtscCfgMinislotCount": docsPnmCmtsUtscCfgMinislotCount,
       "docsPnmCmtsUtscCfgSid": docsPnmCmtsUtscCfgSid,
       "docsPnmCmtsUtscCfgCmMacAddr": docsPnmCmtsUtscCfgCmMacAddr,
       "docsPnmCmtsUtscCfgTimestamp": docsPnmCmtsUtscCfgTimestamp,
       "docsPnmCmtsUtscCfgCenterFreq": docsPnmCmtsUtscCfgCenterFreq,
       "docsPnmCmtsUtscCfgSpan": docsPnmCmtsUtscCfgSpan,
       "docsPnmCmtsUtscCfgNumBins": docsPnmCmtsUtscCfgNumBins,
       "docsPnmCmtsUtscCfgAveraging": docsPnmCmtsUtscCfgAveraging,
       "docsPnmCmtsUtscCfgFilename": docsPnmCmtsUtscCfgFilename,
       "docsPnmCmtsUtscCfgQualifyCenterFreq": docsPnmCmtsUtscCfgQualifyCenterFreq,
       "docsPnmCmtsUtscCfgQualifyBw": docsPnmCmtsUtscCfgQualifyBw,
       "docsPnmCmtsUtscCfgQualifyThrshld": docsPnmCmtsUtscCfgQualifyThrshld,
       "docsPnmCmtsUtscCfgWindow": docsPnmCmtsUtscCfgWindow,
       "docsPnmCmtsUtscCfgOutputFormat": docsPnmCmtsUtscCfgOutputFormat,
       "docsPnmCmtsUtscCfgRepeatPeriod": docsPnmCmtsUtscCfgRepeatPeriod,
       "docsPnmCmtsUtscCfgFreeRunDuration": docsPnmCmtsUtscCfgFreeRunDuration,
       "docsPnmCmtsUtscCfgTriggerCount": docsPnmCmtsUtscCfgTriggerCount,
       "docsPnmCmtsUtscCfgStatus": docsPnmCmtsUtscCfgStatus,
       "docsPnmCmtsUtscCtrlTable": docsPnmCmtsUtscCtrlTable,
       "docsPnmCmtsUtscCtrlEntry": docsPnmCmtsUtscCtrlEntry,
       "docsPnmCmtsUtscCtrlInitiateTest": docsPnmCmtsUtscCtrlInitiateTest,
       "docsPnmCmtsUtscStatusTable": docsPnmCmtsUtscStatusTable,
       "docsPnmCmtsUtscStatusEntry": docsPnmCmtsUtscStatusEntry,
       "docsPnmCmtsUtscStatusMeasStatus": docsPnmCmtsUtscStatusMeasStatus,
       "docsPnmCmtsUtscResultTable": docsPnmCmtsUtscResultTable,
       "docsPnmCmtsUtscResultEntry": docsPnmCmtsUtscResultEntry,
       "docsPnmCmtsUtscResultSampleRate": docsPnmCmtsUtscResultSampleRate,
       "docsPnmCmtsUtscResultUsSampleSize": docsPnmCmtsUtscResultUsSampleSize,
       "docsPnmCmtsUtscResultSampleTimestamp": docsPnmCmtsUtscResultSampleTimestamp,
       "docsPnmCmtsUtscResultResolutionBw": docsPnmCmtsUtscResultResolutionBw,
       "docsPnmCmtsUtscResultOutput": docsPnmCmtsUtscResultOutput,
       "docsPnmMibConformance": docsPnmMibConformance,
       "docsPnmMibCompliances": docsPnmMibCompliances,
       "docsPnmCmtsCompliance": docsPnmCmtsCompliance,
       "docsPnmCmCompliance": docsPnmCmCompliance,
       "docsPnmCmtsDeprecatedCompliance": docsPnmCmtsDeprecatedCompliance,
       "docsPnmMibGroups": docsPnmMibGroups,
       "docsPnmBulkDataGroup": docsPnmBulkDataGroup,
       "docsPnmCmtsGroup": docsPnmCmtsGroup,
       "docsPnmCmGroup": docsPnmCmGroup,
       "docsPnmCmtsDeprecatedGroup": docsPnmCmtsDeprecatedGroup}
)
