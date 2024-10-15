# SNMP MIB module (MICROCOM-MBR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICROCOM-MBR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:57 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class CompRatio(Integer32):
    """Custom type CompRatio based on Integer32"""




class PortNum(Integer32):
    """Custom type PortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )





class VcNum(Integer32):
    """Custom type VcNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )





class StatsInterval(Integer32):
    """Custom type StatsInterval based on Integer32"""




class LongTermStatsPeriod(Integer32):
    """Custom type LongTermStatsPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )





class StatsRawCount(Integer32):
    """Custom type StatsRawCount based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mnpi_ObjectIdentity = ObjectIdentity
mnpi = _Mnpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102)
)
_Mbr_ObjectIdentity = ObjectIdentity
mbr = _Mbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1)
)
_MbrSystem_ObjectIdentity = ObjectIdentity
mbrSystem = _MbrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1)
)
_MbrSysInfo_ObjectIdentity = ObjectIdentity
mbrSysInfo = _MbrSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1)
)
_MbrSysSwVers_ObjectIdentity = ObjectIdentity
mbrSysSwVers = _MbrSysSwVers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 1)
)
_MbrSWRev_Type = Integer32
_MbrSWRev_Object = MibScalar
mbrSWRev = _MbrSWRev_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 1, 1),
    _MbrSWRev_Type()
)
mbrSWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrSWRev.setStatus("mandatory")
_MbrSWRel_Type = Integer32
_MbrSWRel_Object = MibScalar
mbrSWRel = _MbrSWRel_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 1, 2),
    _MbrSWRel_Type()
)
mbrSWRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrSWRel.setStatus("mandatory")
_MbrSWTstVers_Type = Integer32
_MbrSWTstVers_Object = MibScalar
mbrSWTstVers = _MbrSWTstVers_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 1, 3),
    _MbrSWTstVers_Type()
)
mbrSWTstVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrSWTstVers.setStatus("mandatory")
_MbrSWSpecial_Type = Integer32
_MbrSWSpecial_Object = MibScalar
mbrSWSpecial = _MbrSWSpecial_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 1, 4),
    _MbrSWSpecial_Type()
)
mbrSWSpecial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrSWSpecial.setStatus("mandatory")
_MbrBootDate_Type = Counter32
_MbrBootDate_Object = MibScalar
mbrBootDate = _MbrBootDate_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 2),
    _MbrBootDate_Type()
)
mbrBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrBootDate.setStatus("mandatory")
_MbrBootTime_Type = Counter32
_MbrBootTime_Object = MibScalar
mbrBootTime = _MbrBootTime_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 3),
    _MbrBootTime_Type()
)
mbrBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrBootTime.setStatus("mandatory")
_MbrConfigString_ObjectIdentity = ObjectIdentity
mbrConfigString = _MbrConfigString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 4)
)
_MbrArchCfgStr_Type = OctetString
_MbrArchCfgStr_Object = MibScalar
mbrArchCfgStr = _MbrArchCfgStr_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 4, 1),
    _MbrArchCfgStr_Type()
)
mbrArchCfgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrArchCfgStr.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 4, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_MbrCurCfgStr_Type = OctetString
_MbrCurCfgStr_Object = MibScalar
mbrCurCfgStr = _MbrCurCfgStr_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 4, 2),
    _MbrCurCfgStr_Type()
)
mbrCurCfgStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCurCfgStr.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 4, 2, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_MbrRunCfgStr_Type = OctetString
_MbrRunCfgStr_Object = MibScalar
mbrRunCfgStr = _MbrRunCfgStr_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 4, 3),
    _MbrRunCfgStr_Type()
)
mbrRunCfgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrRunCfgStr.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 4, 3, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_MbrSysAddress_Type = MacAddress
_MbrSysAddress_Object = MibScalar
mbrSysAddress = _MbrSysAddress_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 5),
    _MbrSysAddress_Type()
)
mbrSysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrSysAddress.setStatus("mandatory")
_MbrConfigRec_Type = Counter32
_MbrConfigRec_Object = MibScalar
mbrConfigRec = _MbrConfigRec_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 6),
    _MbrConfigRec_Type()
)
mbrConfigRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrConfigRec.setStatus("mandatory")
_PysmiFakeCol4_Type = Integer32
_PysmiFakeCol4_Object = MibTableColumn
pysmiFakeCol4 = _PysmiFakeCol4_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 1, 6, 4294967295),
    _PysmiFakeCol4_Type()
)
pysmiFakeCol4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol4.setStatus("mandatory")
_MbrSysCfgTbl_ObjectIdentity = ObjectIdentity
mbrSysCfgTbl = _MbrSysCfgTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 2)
)


class _MbrSysType_Type(Integer32):
    """Custom type mbrSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mbr6000", 2),
          ("mbr6500", 4))
    )


_MbrSysType_Type.__name__ = "Integer32"
_MbrSysType_Object = MibScalar
mbrSysType = _MbrSysType_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 2, 1),
    _MbrSysType_Type()
)
mbrSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrSysType.setStatus("mandatory")
_MbrSysName_Type = DisplayString
_MbrSysName_Object = MibScalar
mbrSysName = _MbrSysName_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 2, 2),
    _MbrSysName_Type()
)
mbrSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrSysName.setStatus("mandatory")
_MbrSysPasswd_Type = DisplayString
_MbrSysPasswd_Object = MibScalar
mbrSysPasswd = _MbrSysPasswd_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 2, 3),
    _MbrSysPasswd_Type()
)
mbrSysPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrSysPasswd.setStatus("mandatory")
_MbrSysStats_ObjectIdentity = ObjectIdentity
mbrSysStats = _MbrSysStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 3)
)
_MbrDesigRootAddr_Type = MacAddress
_MbrDesigRootAddr_Object = MibScalar
mbrDesigRootAddr = _MbrDesigRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 3, 1),
    _MbrDesigRootAddr_Type()
)
mbrDesigRootAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrDesigRootAddr.setStatus("mandatory")
_MbrDesigRootPriority_Type = Counter32
_MbrDesigRootPriority_Object = MibScalar
mbrDesigRootPriority = _MbrDesigRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 3, 2),
    _MbrDesigRootPriority_Type()
)
mbrDesigRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrDesigRootPriority.setStatus("mandatory")
_MbrRootPathCost_Type = Counter32
_MbrRootPathCost_Object = MibScalar
mbrRootPathCost = _MbrRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 3, 3),
    _MbrRootPathCost_Type()
)
mbrRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrRootPathCost.setStatus("mandatory")
_MbrRootPort_Type = DisplayString
_MbrRootPort_Object = MibScalar
mbrRootPort = _MbrRootPort_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 3, 4),
    _MbrRootPort_Type()
)
mbrRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrRootPort.setStatus("mandatory")
_MbrSysControl_ObjectIdentity = ObjectIdentity
mbrSysControl = _MbrSysControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4)
)


class _MbrCtrlRequester_Type(OctetString):
    """Custom type mbrCtrlRequester based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MbrCtrlRequester_Type.__name__ = "OctetString"
_MbrCtrlRequester_Object = MibScalar
mbrCtrlRequester = _MbrCtrlRequester_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4, 1),
    _MbrCtrlRequester_Type()
)
mbrCtrlRequester.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCtrlRequester.setStatus("mandatory")
_MbrCtrlPasswd_Type = DisplayString
_MbrCtrlPasswd_Object = MibScalar
mbrCtrlPasswd = _MbrCtrlPasswd_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4, 2),
    _MbrCtrlPasswd_Type()
)
mbrCtrlPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCtrlPasswd.setStatus("mandatory")
_MbrCtrlCmd_Type = Counter32
_MbrCtrlCmd_Object = MibScalar
mbrCtrlCmd = _MbrCtrlCmd_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4, 3),
    _MbrCtrlCmd_Type()
)
mbrCtrlCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCtrlCmd.setStatus("mandatory")
_MbrCtrlPort_Type = Counter32
_MbrCtrlPort_Object = MibScalar
mbrCtrlPort = _MbrCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4, 4),
    _MbrCtrlPort_Type()
)
mbrCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCtrlPort.setStatus("mandatory")
_MbrCtrlAddress_Type = OctetString
_MbrCtrlAddress_Object = MibScalar
mbrCtrlAddress = _MbrCtrlAddress_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4, 5),
    _MbrCtrlAddress_Type()
)
mbrCtrlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCtrlAddress.setStatus("mandatory")
_MbrCtrlPath_Type = OctetString
_MbrCtrlPath_Object = MibScalar
mbrCtrlPath = _MbrCtrlPath_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4, 6),
    _MbrCtrlPath_Type()
)
mbrCtrlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCtrlPath.setStatus("mandatory")
_MbrCtrlParm_Type = Counter32
_MbrCtrlParm_Object = MibScalar
mbrCtrlParm = _MbrCtrlParm_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4, 7),
    _MbrCtrlParm_Type()
)
mbrCtrlParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCtrlParm.setStatus("mandatory")
_MbrCtrlVC_Type = Counter32
_MbrCtrlVC_Object = MibScalar
mbrCtrlVC = _MbrCtrlVC_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 4, 8),
    _MbrCtrlVC_Type()
)
mbrCtrlVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrCtrlVC.setStatus("mandatory")
_MbrSession_ObjectIdentity = ObjectIdentity
mbrSession = _MbrSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 5)
)


class _MbrSessionFlag_Type(Integer32):
    """Custom type mbrSessionFlag based on Integer32"""
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


_MbrSessionFlag_Type.__name__ = "Integer32"
_MbrSessionFlag_Object = MibScalar
mbrSessionFlag = _MbrSessionFlag_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 5, 1),
    _MbrSessionFlag_Type()
)
mbrSessionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrSessionFlag.setStatus("mandatory")


class _MbrSessionPartner_Type(OctetString):
    """Custom type mbrSessionPartner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MbrSessionPartner_Type.__name__ = "OctetString"
_MbrSessionPartner_Object = MibScalar
mbrSessionPartner = _MbrSessionPartner_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 5, 2),
    _MbrSessionPartner_Type()
)
mbrSessionPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrSessionPartner.setStatus("mandatory")
_MbrSessionPath_Type = OctetString
_MbrSessionPath_Object = MibScalar
mbrSessionPath = _MbrSessionPath_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 5, 3),
    _MbrSessionPath_Type()
)
mbrSessionPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrSessionPath.setStatus("mandatory")
_MbrDownload_ObjectIdentity = ObjectIdentity
mbrDownload = _MbrDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6)
)
_MbrDlFileName_Type = DisplayString
_MbrDlFileName_Object = MibScalar
mbrDlFileName = _MbrDlFileName_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6, 1),
    _MbrDlFileName_Type()
)
mbrDlFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrDlFileName.setStatus("mandatory")
_MbrDlDevice_Type = Integer32
_MbrDlDevice_Object = MibScalar
mbrDlDevice = _MbrDlDevice_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6, 2),
    _MbrDlDevice_Type()
)
mbrDlDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrDlDevice.setStatus("mandatory")
_MbrDlStatus_Type = Counter32
_MbrDlStatus_Object = MibScalar
mbrDlStatus = _MbrDlStatus_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6, 3),
    _MbrDlStatus_Type()
)
mbrDlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrDlStatus.setStatus("mandatory")
_MbrDlReadRec_Type = OctetString
_MbrDlReadRec_Object = MibScalar
mbrDlReadRec = _MbrDlReadRec_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6, 4),
    _MbrDlReadRec_Type()
)
mbrDlReadRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrDlReadRec.setStatus("mandatory")
_PysmiFakeCol5_Type = Integer32
_PysmiFakeCol5_Object = MibTableColumn
pysmiFakeCol5 = _PysmiFakeCol5_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6, 4, 4294967295),
    _PysmiFakeCol5_Type()
)
pysmiFakeCol5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol5.setStatus("mandatory")
_MbrDlWriteRec_Type = OctetString
_MbrDlWriteRec_Object = MibScalar
mbrDlWriteRec = _MbrDlWriteRec_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6, 5),
    _MbrDlWriteRec_Type()
)
mbrDlWriteRec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrDlWriteRec.setStatus("mandatory")
_PysmiFakeCol6_Type = Integer32
_PysmiFakeCol6_Object = MibTableColumn
pysmiFakeCol6 = _PysmiFakeCol6_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6, 5, 4294967295),
    _PysmiFakeCol6_Type()
)
pysmiFakeCol6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol6.setStatus("mandatory")
_MbrDlFileSize_Type = Integer32
_MbrDlFileSize_Object = MibScalar
mbrDlFileSize = _MbrDlFileSize_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 6, 6),
    _MbrDlFileSize_Type()
)
mbrDlFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrDlFileSize.setStatus("mandatory")
_MbrAlarms_ObjectIdentity = ObjectIdentity
mbrAlarms = _MbrAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 7)
)
_MbrAlarmTable_Object = MibTable
mbrAlarmTable = _MbrAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mbrAlarmTable.setStatus("mandatory")
_MbrAlarmEntry_Object = MibTableRow
mbrAlarmEntry = _MbrAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 7, 1, 1)
)
mbrAlarmEntry.setIndexNames(
    (0, "MICROCOM-MBR-MIB", "pysmiFakeCol7"),
)
if mibBuilder.loadTexts:
    mbrAlarmEntry.setStatus("mandatory")
_MbrAlarmText_Type = Integer32
_MbrAlarmText_Object = MibTableColumn
mbrAlarmText = _MbrAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 7, 1, 1, 7),
    _MbrAlarmText_Type()
)
mbrAlarmText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbrAlarmText.setStatus("mandatory")
_PysmiFakeCol7_Type = Integer32
_PysmiFakeCol7_Object = MibTableColumn
pysmiFakeCol7 = _PysmiFakeCol7_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 7, 1, 1, 4294967295),
    _PysmiFakeCol7_Type()
)
pysmiFakeCol7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol7.setStatus("mandatory")
_MbrNetReports_ObjectIdentity = ObjectIdentity
mbrNetReports = _MbrNetReports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 8)
)
_MbrNetRptDestIpAddress_Type = IpAddress
_MbrNetRptDestIpAddress_Object = MibScalar
mbrNetRptDestIpAddress = _MbrNetRptDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 8, 4),
    _MbrNetRptDestIpAddress_Type()
)
mbrNetRptDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbrNetRptDestIpAddress.setStatus("mandatory")
_MbrTraps_ObjectIdentity = ObjectIdentity
mbrTraps = _MbrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 10)
)
_MbrTrapCode_Type = Counter32
_MbrTrapCode_Object = MibScalar
mbrTrapCode = _MbrTrapCode_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 10, 1),
    _MbrTrapCode_Type()
)
mbrTrapCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbrTrapCode.setStatus("mandatory")
_MbrTrapPort_Type = Integer32
_MbrTrapPort_Object = MibScalar
mbrTrapPort = _MbrTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 10, 2),
    _MbrTrapPort_Type()
)
mbrTrapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbrTrapPort.setStatus("mandatory")
_MbrTrapInfo_Type = Integer32
_MbrTrapInfo_Object = MibScalar
mbrTrapInfo = _MbrTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 10, 3),
    _MbrTrapInfo_Type()
)
mbrTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbrTrapInfo.setStatus("mandatory")
_PysmiFakeCol8_Type = Integer32
_PysmiFakeCol8_Object = MibTableColumn
pysmiFakeCol8 = _PysmiFakeCol8_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 10, 3, 4294967295),
    _PysmiFakeCol8_Type()
)
pysmiFakeCol8.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol8.setStatus("mandatory")
_MbrRingMgtAlarms_ObjectIdentity = ObjectIdentity
mbrRingMgtAlarms = _MbrRingMgtAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 11)
)
_MbrRmAlarmStatAddr_Type = MacAddress
_MbrRmAlarmStatAddr_Object = MibScalar
mbrRmAlarmStatAddr = _MbrRmAlarmStatAddr_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 11, 1),
    _MbrRmAlarmStatAddr_Type()
)
mbrRmAlarmStatAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbrRmAlarmStatAddr.setStatus("mandatory")
_MbrRmAlarmNaunAddr_Type = MacAddress
_MbrRmAlarmNaunAddr_Object = MibScalar
mbrRmAlarmNaunAddr = _MbrRmAlarmNaunAddr_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 11, 2),
    _MbrRmAlarmNaunAddr_Type()
)
mbrRmAlarmNaunAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbrRmAlarmNaunAddr.setStatus("mandatory")


class _MbrRmAlarmBeaconType_Type(Integer32):
    """Custom type mbrRmAlarmBeaconType based on Integer32"""
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
        *(("recoveryModeSet", 1),
          ("signalLossError", 2),
          ("streamSignalClaimToken", 4),
          ("streamSignalNotClaimToken", 3))
    )


_MbrRmAlarmBeaconType_Type.__name__ = "Integer32"
_MbrRmAlarmBeaconType_Object = MibScalar
mbrRmAlarmBeaconType = _MbrRmAlarmBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 1, 11, 14),
    _MbrRmAlarmBeaconType_Type()
)
mbrRmAlarmBeaconType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbrRmAlarmBeaconType.setStatus("mandatory")
_MbrWanInterfaces_ObjectIdentity = ObjectIdentity
mbrWanInterfaces = _MbrWanInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2)
)
_MbrWifTable_ObjectIdentity = ObjectIdentity
mbrWifTable = _MbrWifTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2)
)
_MbrWifEntry_ObjectIdentity = ObjectIdentity
mbrWifEntry = _MbrWifEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1)
)
_MbrWifInfo_ObjectIdentity = ObjectIdentity
mbrWifInfo = _MbrWifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2)
)


class _MbrWifLinkState_Type(Integer32):
    """Custom type mbrWifLinkState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("blockingInit", 5),
          ("disabled", 0),
          ("down", 7),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2),
          ("up", 6))
    )


_MbrWifLinkState_Type.__name__ = "Integer32"
_MbrWifLinkState_Object = MibScalar
mbrWifLinkState = _MbrWifLinkState_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 1),
    _MbrWifLinkState_Type()
)
mbrWifLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLinkState.setStatus("mandatory")
_MbrWifLinkDelay_ObjectIdentity = ObjectIdentity
mbrWifLinkDelay = _MbrWifLinkDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 2)
)
_MbrWifLinkDelaySeconds_Type = Counter32
_MbrWifLinkDelaySeconds_Object = MibScalar
mbrWifLinkDelaySeconds = _MbrWifLinkDelaySeconds_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 2, 1),
    _MbrWifLinkDelaySeconds_Type()
)
mbrWifLinkDelaySeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLinkDelaySeconds.setStatus("mandatory")
_MbrWifLinkDelayMillis_Type = Counter32
_MbrWifLinkDelayMillis_Object = MibScalar
mbrWifLinkDelayMillis = _MbrWifLinkDelayMillis_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 2, 2),
    _MbrWifLinkDelayMillis_Type()
)
mbrWifLinkDelayMillis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLinkDelayMillis.setStatus("mandatory")
_MbrWifSppActiveCount_Type = Integer32
_MbrWifSppActiveCount_Object = MibScalar
mbrWifSppActiveCount = _MbrWifSppActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 3),
    _MbrWifSppActiveCount_Type()
)
mbrWifSppActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifSppActiveCount.setStatus("mandatory")
_MbrWifLinkSpeed_Type = Integer32
_MbrWifLinkSpeed_Object = MibScalar
mbrWifLinkSpeed = _MbrWifLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 4),
    _MbrWifLinkSpeed_Type()
)
mbrWifLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLinkSpeed.setStatus("mandatory")
_MbrWifLinkChangeTime_Type = Integer32
_MbrWifLinkChangeTime_Object = MibScalar
mbrWifLinkChangeTime = _MbrWifLinkChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 5),
    _MbrWifLinkChangeTime_Type()
)
mbrWifLinkChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLinkChangeTime.setStatus("mandatory")
_MbrWifLinkChangeDate_Type = Integer32
_MbrWifLinkChangeDate_Object = MibScalar
mbrWifLinkChangeDate = _MbrWifLinkChangeDate_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 6),
    _MbrWifLinkChangeDate_Type()
)
mbrWifLinkChangeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLinkChangeDate.setStatus("mandatory")
_MbrWifLongTermStatsInterval_Type = LongTermStatsPeriod
_MbrWifLongTermStatsInterval_Object = MibScalar
mbrWifLongTermStatsInterval = _MbrWifLongTermStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 7),
    _MbrWifLongTermStatsInterval_Type()
)
mbrWifLongTermStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLongTermStatsInterval.setStatus("mandatory")


class _MbrWifCompNeg_Type(Integer32):
    """Custom type mbrWifCompNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compressionOff", 0),
          ("compressionOn", 1))
    )


_MbrWifCompNeg_Type.__name__ = "Integer32"
_MbrWifCompNeg_Object = MibScalar
mbrWifCompNeg = _MbrWifCompNeg_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 8),
    _MbrWifCompNeg_Type()
)
mbrWifCompNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifCompNeg.setStatus("mandatory")
_MbrWifLoadShareSetId_Type = Counter32
_MbrWifLoadShareSetId_Object = MibScalar
mbrWifLoadShareSetId = _MbrWifLoadShareSetId_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 9),
    _MbrWifLoadShareSetId_Type()
)
mbrWifLoadShareSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLoadShareSetId.setStatus("mandatory")
_MbrWifSpecificInfo_ObjectIdentity = ObjectIdentity
mbrWifSpecificInfo = _MbrWifSpecificInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10)
)
_MbrWifX25Info_ObjectIdentity = ObjectIdentity
mbrWifX25Info = _MbrWifX25Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1)
)
_MbrWifVcCount_Type = Integer32
_MbrWifVcCount_Object = MibScalar
mbrWifVcCount = _MbrWifVcCount_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 1),
    _MbrWifVcCount_Type()
)
mbrWifVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcCount.setStatus("mandatory")
_MbrWifVcInfo_ObjectIdentity = ObjectIdentity
mbrWifVcInfo = _MbrWifVcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2)
)


class _MbrWifVcCallState_Type(Integer32):
    """Custom type mbrWifVcCallState based on Integer32"""
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
        *(("available", 6),
          ("calling", 2),
          ("disconnecting", 5),
          ("established", 4),
          ("idle", 1),
          ("listening", 3),
          ("noSwitch", 0))
    )


_MbrWifVcCallState_Type.__name__ = "Integer32"
_MbrWifVcCallState_Object = MibScalar
mbrWifVcCallState = _MbrWifVcCallState_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2, 1),
    _MbrWifVcCallState_Type()
)
mbrWifVcCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcCallState.setStatus("mandatory")
_MbrWifVcDelay_ObjectIdentity = ObjectIdentity
mbrWifVcDelay = _MbrWifVcDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2, 2)
)
_MbrWifVcDelaySeconds_Type = Integer32
_MbrWifVcDelaySeconds_Object = MibScalar
mbrWifVcDelaySeconds = _MbrWifVcDelaySeconds_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2, 2, 1),
    _MbrWifVcDelaySeconds_Type()
)
mbrWifVcDelaySeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcDelaySeconds.setStatus("mandatory")
_MbrWifVcDelayMillis_Type = Integer32
_MbrWifVcDelayMillis_Object = MibScalar
mbrWifVcDelayMillis = _MbrWifVcDelayMillis_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2, 2, 2),
    _MbrWifVcDelayMillis_Type()
)
mbrWifVcDelayMillis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcDelayMillis.setStatus("mandatory")
_MbrWifVcLongTermStatsInterval_Type = LongTermStatsPeriod
_MbrWifVcLongTermStatsInterval_Object = MibScalar
mbrWifVcLongTermStatsInterval = _MbrWifVcLongTermStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2, 3),
    _MbrWifVcLongTermStatsInterval_Type()
)
mbrWifVcLongTermStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcLongTermStatsInterval.setStatus("mandatory")


class _MbrWifVcCompNeg_Type(Integer32):
    """Custom type mbrWifVcCompNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compressionOff", 0),
          ("compressionOn", 1))
    )


_MbrWifVcCompNeg_Type.__name__ = "Integer32"
_MbrWifVcCompNeg_Object = MibScalar
mbrWifVcCompNeg = _MbrWifVcCompNeg_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2, 4),
    _MbrWifVcCompNeg_Type()
)
mbrWifVcCompNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcCompNeg.setStatus("mandatory")
_MbrWifVcLcn_Type = Integer32
_MbrWifVcLcn_Object = MibScalar
mbrWifVcLcn = _MbrWifVcLcn_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2, 5),
    _MbrWifVcLcn_Type()
)
mbrWifVcLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcLcn.setStatus("mandatory")
_MbrWifVcRemoteDte_Type = DisplayString
_MbrWifVcRemoteDte_Object = MibScalar
mbrWifVcRemoteDte = _MbrWifVcRemoteDte_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 2, 10, 1, 2, 6),
    _MbrWifVcRemoteDte_Type()
)
mbrWifVcRemoteDte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcRemoteDte.setStatus("mandatory")
_MbrWifStatTable_Object = MibTable
mbrWifStatTable = _MbrWifStatTable_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    mbrWifStatTable.setStatus("mandatory")
_MbrWifStatEntry_Object = MibTableRow
mbrWifStatEntry = _MbrWifStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1)
)
mbrWifStatEntry.setIndexNames(
    (0, "MICROCOM-MBR-MIB", "StatsInterval"),
    (0, "MICROCOM-MBR-MIB", "PortNum"),
)
if mibBuilder.loadTexts:
    mbrWifStatEntry.setStatus("mandatory")
_MbrWifRcvChars_Type = StatsRawCount
_MbrWifRcvChars_Object = MibScalar
mbrWifRcvChars = _MbrWifRcvChars_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 1),
    _MbrWifRcvChars_Type()
)
mbrWifRcvChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifRcvChars.setStatus("mandatory")
_MbrWifXmtChars_Type = StatsRawCount
_MbrWifXmtChars_Object = MibTableColumn
mbrWifXmtChars = _MbrWifXmtChars_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 2),
    _MbrWifXmtChars_Type()
)
mbrWifXmtChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifXmtChars.setStatus("mandatory")
_MbrWifRcvFrames_Type = StatsRawCount
_MbrWifRcvFrames_Object = MibTableColumn
mbrWifRcvFrames = _MbrWifRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 3),
    _MbrWifRcvFrames_Type()
)
mbrWifRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifRcvFrames.setStatus("mandatory")
_MbrWifXmtFrames_Type = StatsRawCount
_MbrWifXmtFrames_Object = MibTableColumn
mbrWifXmtFrames = _MbrWifXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 4),
    _MbrWifXmtFrames_Type()
)
mbrWifXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifXmtFrames.setStatus("mandatory")
_MbrWifRcvBadFrames_Type = StatsRawCount
_MbrWifRcvBadFrames_Object = MibTableColumn
mbrWifRcvBadFrames = _MbrWifRcvBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 5),
    _MbrWifRcvBadFrames_Type()
)
mbrWifRcvBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifRcvBadFrames.setStatus("mandatory")
_MbrWifXmtRejects_Type = StatsRawCount
_MbrWifXmtRejects_Object = MibTableColumn
mbrWifXmtRejects = _MbrWifXmtRejects_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 6),
    _MbrWifXmtRejects_Type()
)
mbrWifXmtRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifXmtRejects.setStatus("mandatory")
_MbrWifRcvRejects_Type = StatsRawCount
_MbrWifRcvRejects_Object = MibTableColumn
mbrWifRcvRejects = _MbrWifRcvRejects_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 7),
    _MbrWifRcvRejects_Type()
)
mbrWifRcvRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifRcvRejects.setStatus("mandatory")
_MbrWifRexmtTimeouts_Type = StatsRawCount
_MbrWifRexmtTimeouts_Object = MibTableColumn
mbrWifRexmtTimeouts = _MbrWifRexmtTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 8),
    _MbrWifRexmtTimeouts_Type()
)
mbrWifRexmtTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifRexmtTimeouts.setStatus("mandatory")
_MbrWifLanPktsDiscarded_Type = StatsRawCount
_MbrWifLanPktsDiscarded_Object = MibTableColumn
mbrWifLanPktsDiscarded = _MbrWifLanPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 9),
    _MbrWifLanPktsDiscarded_Type()
)
mbrWifLanPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifLanPktsDiscarded.setStatus("mandatory")
_MbrWifMgmtPktsForwarded_Type = StatsRawCount
_MbrWifMgmtPktsForwarded_Object = MibTableColumn
mbrWifMgmtPktsForwarded = _MbrWifMgmtPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 10),
    _MbrWifMgmtPktsForwarded_Type()
)
mbrWifMgmtPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifMgmtPktsForwarded.setStatus("mandatory")
_MbrWifRcvCompRatio_Type = CompRatio
_MbrWifRcvCompRatio_Object = MibScalar
mbrWifRcvCompRatio = _MbrWifRcvCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 11),
    _MbrWifRcvCompRatio_Type()
)
mbrWifRcvCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifRcvCompRatio.setStatus("mandatory")
_MbrWifXmtCompRatio_Type = CompRatio
_MbrWifXmtCompRatio_Object = MibScalar
mbrWifXmtCompRatio = _MbrWifXmtCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 12),
    _MbrWifXmtCompRatio_Type()
)
mbrWifXmtCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifXmtCompRatio.setStatus("mandatory")
_MbrWifRminCompRatio_Type = CompRatio
_MbrWifRminCompRatio_Object = MibScalar
mbrWifRminCompRatio = _MbrWifRminCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 13),
    _MbrWifRminCompRatio_Type()
)
mbrWifRminCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifRminCompRatio.setStatus("mandatory")
_MbrWifXminCompRatio_Type = CompRatio
_MbrWifXminCompRatio_Object = MibScalar
mbrWifXminCompRatio = _MbrWifXminCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 14),
    _MbrWifXminCompRatio_Type()
)
mbrWifXminCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifXminCompRatio.setStatus("mandatory")
_MbrWifRmaxCompRatio_Type = CompRatio
_MbrWifRmaxCompRatio_Object = MibScalar
mbrWifRmaxCompRatio = _MbrWifRmaxCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 15),
    _MbrWifRmaxCompRatio_Type()
)
mbrWifRmaxCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifRmaxCompRatio.setStatus("mandatory")
_MbrWifXmaxCompRatio_Type = CompRatio
_MbrWifXmaxCompRatio_Object = MibScalar
mbrWifXmaxCompRatio = _MbrWifXmaxCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 1, 16),
    _MbrWifXmaxCompRatio_Type()
)
mbrWifXmaxCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifXmaxCompRatio.setStatus("mandatory")
_MbrWifVcStatTable_Object = MibTable
mbrWifVcStatTable = _MbrWifVcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mbrWifVcStatTable.setStatus("mandatory")
_MbrWifVcStatEntry_Object = MibTableRow
mbrWifVcStatEntry = _MbrWifVcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1)
)
mbrWifVcStatEntry.setIndexNames(
    (0, "MICROCOM-MBR-MIB", "StatInterval"),
    (0, "MICROCOM-MBR-MIB", "PortNum"),
    (0, "MICROCOM-MBR-MIB", "VcNum"),
)
if mibBuilder.loadTexts:
    mbrWifVcStatEntry.setStatus("mandatory")
_MbrWifVcRcvChars_Type = StatsRawCount
_MbrWifVcRcvChars_Object = MibTableColumn
mbrWifVcRcvChars = _MbrWifVcRcvChars_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 1),
    _MbrWifVcRcvChars_Type()
)
mbrWifVcRcvChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcRcvChars.setStatus("mandatory")
_MbrWifVcXmtChars_Type = StatsRawCount
_MbrWifVcXmtChars_Object = MibTableColumn
mbrWifVcXmtChars = _MbrWifVcXmtChars_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 2),
    _MbrWifVcXmtChars_Type()
)
mbrWifVcXmtChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcXmtChars.setStatus("mandatory")
_MbrWifVcRcvX25Pkts_Type = StatsRawCount
_MbrWifVcRcvX25Pkts_Object = MibTableColumn
mbrWifVcRcvX25Pkts = _MbrWifVcRcvX25Pkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 3),
    _MbrWifVcRcvX25Pkts_Type()
)
mbrWifVcRcvX25Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcRcvX25Pkts.setStatus("mandatory")
_MbrWifVcXmtX25Pkts_Type = StatsRawCount
_MbrWifVcXmtX25Pkts_Object = MibTableColumn
mbrWifVcXmtX25Pkts = _MbrWifVcXmtX25Pkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 4),
    _MbrWifVcXmtX25Pkts_Type()
)
mbrWifVcXmtX25Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcXmtX25Pkts.setStatus("mandatory")
_MbrWifVcRcvCompRatio_Type = CompRatio
_MbrWifVcRcvCompRatio_Object = MibScalar
mbrWifVcRcvCompRatio = _MbrWifVcRcvCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 5),
    _MbrWifVcRcvCompRatio_Type()
)
mbrWifVcRcvCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcRcvCompRatio.setStatus("mandatory")
_MbrWifVcXmtCompRatio_Type = CompRatio
_MbrWifVcXmtCompRatio_Object = MibScalar
mbrWifVcXmtCompRatio = _MbrWifVcXmtCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 6),
    _MbrWifVcXmtCompRatio_Type()
)
mbrWifVcXmtCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcXmtCompRatio.setStatus("mandatory")
_MbrWifVcRminCompRatio_Type = CompRatio
_MbrWifVcRminCompRatio_Object = MibScalar
mbrWifVcRminCompRatio = _MbrWifVcRminCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 7),
    _MbrWifVcRminCompRatio_Type()
)
mbrWifVcRminCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcRminCompRatio.setStatus("mandatory")
_MbrWifVcXminCompRatio_Type = CompRatio
_MbrWifVcXminCompRatio_Object = MibScalar
mbrWifVcXminCompRatio = _MbrWifVcXminCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 8),
    _MbrWifVcXminCompRatio_Type()
)
mbrWifVcXminCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcXminCompRatio.setStatus("mandatory")
_MbrWifVcRmaxCompRatio_Type = CompRatio
_MbrWifVcRmaxCompRatio_Object = MibScalar
mbrWifVcRmaxCompRatio = _MbrWifVcRmaxCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 9),
    _MbrWifVcRmaxCompRatio_Type()
)
mbrWifVcRmaxCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcRmaxCompRatio.setStatus("mandatory")
_MbrWifVcXmaxCompRatio_Type = CompRatio
_MbrWifVcXmaxCompRatio_Object = MibScalar
mbrWifVcXmaxCompRatio = _MbrWifVcXmaxCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 2, 2, 1, 3, 2, 1, 10),
    _MbrWifVcXmaxCompRatio_Type()
)
mbrWifVcXmaxCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrWifVcXmaxCompRatio.setStatus("mandatory")
_MbrLanInterfaces_ObjectIdentity = ObjectIdentity
mbrLanInterfaces = _MbrLanInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 3)
)
_MbrLifTable_ObjectIdentity = ObjectIdentity
mbrLifTable = _MbrLifTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2)
)
_MbrLifEntry_ObjectIdentity = ObjectIdentity
mbrLifEntry = _MbrLifEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1)
)
_MbrLifInfo_ObjectIdentity = ObjectIdentity
mbrLifInfo = _MbrLifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 2)
)
_MbrLifState_Type = Counter32
_MbrLifState_Object = MibScalar
mbrLifState = _MbrLifState_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 2, 1),
    _MbrLifState_Type()
)
mbrLifState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifState.setStatus("mandatory")
_MbrLifMacAddress_Type = MacAddress
_MbrLifMacAddress_Object = MibScalar
mbrLifMacAddress = _MbrLifMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 2, 2),
    _MbrLifMacAddress_Type()
)
mbrLifMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifMacAddress.setStatus("mandatory")
_MbrLifHardwareRev_Type = Counter32
_MbrLifHardwareRev_Object = MibScalar
mbrLifHardwareRev = _MbrLifHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 2, 3),
    _MbrLifHardwareRev_Type()
)
mbrLifHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifHardwareRev.setStatus("mandatory")
_MbrLifLongTermStatsInterval_Type = LongTermStatsPeriod
_MbrLifLongTermStatsInterval_Object = MibScalar
mbrLifLongTermStatsInterval = _MbrLifLongTermStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 2, 4),
    _MbrLifLongTermStatsInterval_Type()
)
mbrLifLongTermStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifLongTermStatsInterval.setStatus("mandatory")
_MbrLifRingNumber_Type = Integer32
_MbrLifRingNumber_Object = MibScalar
mbrLifRingNumber = _MbrLifRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 2, 5),
    _MbrLifRingNumber_Type()
)
mbrLifRingNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbrLifRingNumber.setStatus("mandatory")
_MbrLifStatistics_ObjectIdentity = ObjectIdentity
mbrLifStatistics = _MbrLifStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3)
)
_MbrLifStatTable_Object = MibTable
mbrLifStatTable = _MbrLifStatTable_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mbrLifStatTable.setStatus("mandatory")
_MbrLifStatEntry_Object = MibTableRow
mbrLifStatEntry = _MbrLifStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1, 1)
)
mbrLifStatEntry.setIndexNames(
    (0, "MICROCOM-MBR-MIB", "StatsInterval"),
    (0, "MICROCOM-MBR-MIB", "PortNum"),
)
if mibBuilder.loadTexts:
    mbrLifStatEntry.setStatus("mandatory")
_MbrLifRcvPkts_Type = StatsRawCount
_MbrLifRcvPkts_Object = MibTableColumn
mbrLifRcvPkts = _MbrLifRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1, 1, 1),
    _MbrLifRcvPkts_Type()
)
mbrLifRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifRcvPkts.setStatus("mandatory")
_MbrLifFwdPkts_Type = StatsRawCount
_MbrLifFwdPkts_Object = MibTableColumn
mbrLifFwdPkts = _MbrLifFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1, 1, 2),
    _MbrLifFwdPkts_Type()
)
mbrLifFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifFwdPkts.setStatus("mandatory")
_MbrLifRcvMcastPkts_Type = StatsRawCount
_MbrLifRcvMcastPkts_Object = MibTableColumn
mbrLifRcvMcastPkts = _MbrLifRcvMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1, 1, 3),
    _MbrLifRcvMcastPkts_Type()
)
mbrLifRcvMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifRcvMcastPkts.setStatus("mandatory")
_MbrLifFwdMcastPkts_Type = StatsRawCount
_MbrLifFwdMcastPkts_Object = MibTableColumn
mbrLifFwdMcastPkts = _MbrLifFwdMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1, 1, 4),
    _MbrLifFwdMcastPkts_Type()
)
mbrLifFwdMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifFwdMcastPkts.setStatus("mandatory")
_MbrLifRcvErrPkts_Type = StatsRawCount
_MbrLifRcvErrPkts_Object = MibTableColumn
mbrLifRcvErrPkts = _MbrLifRcvErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1, 1, 5),
    _MbrLifRcvErrPkts_Type()
)
mbrLifRcvErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifRcvErrPkts.setStatus("mandatory")
_MbrLifNobufDiscPkts_Type = StatsRawCount
_MbrLifNobufDiscPkts_Object = MibTableColumn
mbrLifNobufDiscPkts = _MbrLifNobufDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1, 1, 6),
    _MbrLifNobufDiscPkts_Type()
)
mbrLifNobufDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifNobufDiscPkts.setStatus("mandatory")
_MbrLifXmtPkts_Type = StatsRawCount
_MbrLifXmtPkts_Object = MibTableColumn
mbrLifXmtPkts = _MbrLifXmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 102, 1, 3, 2, 1, 3, 1, 1, 7),
    _MbrLifXmtPkts_Type()
)
mbrLifXmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbrLifXmtPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICROCOM-MBR-MIB",
    **{"MacAddress": MacAddress,
       "CompRatio": CompRatio,
       "PortNum": PortNum,
       "VcNum": VcNum,
       "StatsInterval": StatsInterval,
       "LongTermStatsPeriod": LongTermStatsPeriod,
       "StatsRawCount": StatsRawCount,
       "mnpi": mnpi,
       "mbr": mbr,
       "mbrSystem": mbrSystem,
       "mbrSysInfo": mbrSysInfo,
       "mbrSysSwVers": mbrSysSwVers,
       "mbrSWRev": mbrSWRev,
       "mbrSWRel": mbrSWRel,
       "mbrSWTstVers": mbrSWTstVers,
       "mbrSWSpecial": mbrSWSpecial,
       "mbrBootDate": mbrBootDate,
       "mbrBootTime": mbrBootTime,
       "mbrConfigString": mbrConfigString,
       "mbrArchCfgStr": mbrArchCfgStr,
       "pysmiFakeCol1": pysmiFakeCol1,
       "mbrCurCfgStr": mbrCurCfgStr,
       "pysmiFakeCol2": pysmiFakeCol2,
       "mbrRunCfgStr": mbrRunCfgStr,
       "pysmiFakeCol3": pysmiFakeCol3,
       "mbrSysAddress": mbrSysAddress,
       "mbrConfigRec": mbrConfigRec,
       "pysmiFakeCol4": pysmiFakeCol4,
       "mbrSysCfgTbl": mbrSysCfgTbl,
       "mbrSysType": mbrSysType,
       "mbrSysName": mbrSysName,
       "mbrSysPasswd": mbrSysPasswd,
       "mbrSysStats": mbrSysStats,
       "mbrDesigRootAddr": mbrDesigRootAddr,
       "mbrDesigRootPriority": mbrDesigRootPriority,
       "mbrRootPathCost": mbrRootPathCost,
       "mbrRootPort": mbrRootPort,
       "mbrSysControl": mbrSysControl,
       "mbrCtrlRequester": mbrCtrlRequester,
       "mbrCtrlPasswd": mbrCtrlPasswd,
       "mbrCtrlCmd": mbrCtrlCmd,
       "mbrCtrlPort": mbrCtrlPort,
       "mbrCtrlAddress": mbrCtrlAddress,
       "mbrCtrlPath": mbrCtrlPath,
       "mbrCtrlParm": mbrCtrlParm,
       "mbrCtrlVC": mbrCtrlVC,
       "mbrSession": mbrSession,
       "mbrSessionFlag": mbrSessionFlag,
       "mbrSessionPartner": mbrSessionPartner,
       "mbrSessionPath": mbrSessionPath,
       "mbrDownload": mbrDownload,
       "mbrDlFileName": mbrDlFileName,
       "mbrDlDevice": mbrDlDevice,
       "mbrDlStatus": mbrDlStatus,
       "mbrDlReadRec": mbrDlReadRec,
       "pysmiFakeCol5": pysmiFakeCol5,
       "mbrDlWriteRec": mbrDlWriteRec,
       "pysmiFakeCol6": pysmiFakeCol6,
       "mbrDlFileSize": mbrDlFileSize,
       "mbrAlarms": mbrAlarms,
       "mbrAlarmTable": mbrAlarmTable,
       "mbrAlarmEntry": mbrAlarmEntry,
       "mbrAlarmText": mbrAlarmText,
       "pysmiFakeCol7": pysmiFakeCol7,
       "mbrNetReports": mbrNetReports,
       "mbrNetRptDestIpAddress": mbrNetRptDestIpAddress,
       "mbrTraps": mbrTraps,
       "mbrTrapCode": mbrTrapCode,
       "mbrTrapPort": mbrTrapPort,
       "mbrTrapInfo": mbrTrapInfo,
       "pysmiFakeCol8": pysmiFakeCol8,
       "mbrRingMgtAlarms": mbrRingMgtAlarms,
       "mbrRmAlarmStatAddr": mbrRmAlarmStatAddr,
       "mbrRmAlarmNaunAddr": mbrRmAlarmNaunAddr,
       "mbrRmAlarmBeaconType": mbrRmAlarmBeaconType,
       "mbrWanInterfaces": mbrWanInterfaces,
       "mbrWifTable": mbrWifTable,
       "mbrWifEntry": mbrWifEntry,
       "mbrWifInfo": mbrWifInfo,
       "mbrWifLinkState": mbrWifLinkState,
       "mbrWifLinkDelay": mbrWifLinkDelay,
       "mbrWifLinkDelaySeconds": mbrWifLinkDelaySeconds,
       "mbrWifLinkDelayMillis": mbrWifLinkDelayMillis,
       "mbrWifSppActiveCount": mbrWifSppActiveCount,
       "mbrWifLinkSpeed": mbrWifLinkSpeed,
       "mbrWifLinkChangeTime": mbrWifLinkChangeTime,
       "mbrWifLinkChangeDate": mbrWifLinkChangeDate,
       "mbrWifLongTermStatsInterval": mbrWifLongTermStatsInterval,
       "mbrWifCompNeg": mbrWifCompNeg,
       "mbrWifLoadShareSetId": mbrWifLoadShareSetId,
       "mbrWifSpecificInfo": mbrWifSpecificInfo,
       "mbrWifX25Info": mbrWifX25Info,
       "mbrWifVcCount": mbrWifVcCount,
       "mbrWifVcInfo": mbrWifVcInfo,
       "mbrWifVcCallState": mbrWifVcCallState,
       "mbrWifVcDelay": mbrWifVcDelay,
       "mbrWifVcDelaySeconds": mbrWifVcDelaySeconds,
       "mbrWifVcDelayMillis": mbrWifVcDelayMillis,
       "mbrWifVcLongTermStatsInterval": mbrWifVcLongTermStatsInterval,
       "mbrWifVcCompNeg": mbrWifVcCompNeg,
       "mbrWifVcLcn": mbrWifVcLcn,
       "mbrWifVcRemoteDte": mbrWifVcRemoteDte,
       "mbrWifStatTable": mbrWifStatTable,
       "mbrWifStatEntry": mbrWifStatEntry,
       "mbrWifRcvChars": mbrWifRcvChars,
       "mbrWifXmtChars": mbrWifXmtChars,
       "mbrWifRcvFrames": mbrWifRcvFrames,
       "mbrWifXmtFrames": mbrWifXmtFrames,
       "mbrWifRcvBadFrames": mbrWifRcvBadFrames,
       "mbrWifXmtRejects": mbrWifXmtRejects,
       "mbrWifRcvRejects": mbrWifRcvRejects,
       "mbrWifRexmtTimeouts": mbrWifRexmtTimeouts,
       "mbrWifLanPktsDiscarded": mbrWifLanPktsDiscarded,
       "mbrWifMgmtPktsForwarded": mbrWifMgmtPktsForwarded,
       "mbrWifRcvCompRatio": mbrWifRcvCompRatio,
       "mbrWifXmtCompRatio": mbrWifXmtCompRatio,
       "mbrWifRminCompRatio": mbrWifRminCompRatio,
       "mbrWifXminCompRatio": mbrWifXminCompRatio,
       "mbrWifRmaxCompRatio": mbrWifRmaxCompRatio,
       "mbrWifXmaxCompRatio": mbrWifXmaxCompRatio,
       "mbrWifVcStatTable": mbrWifVcStatTable,
       "mbrWifVcStatEntry": mbrWifVcStatEntry,
       "mbrWifVcRcvChars": mbrWifVcRcvChars,
       "mbrWifVcXmtChars": mbrWifVcXmtChars,
       "mbrWifVcRcvX25Pkts": mbrWifVcRcvX25Pkts,
       "mbrWifVcXmtX25Pkts": mbrWifVcXmtX25Pkts,
       "mbrWifVcRcvCompRatio": mbrWifVcRcvCompRatio,
       "mbrWifVcXmtCompRatio": mbrWifVcXmtCompRatio,
       "mbrWifVcRminCompRatio": mbrWifVcRminCompRatio,
       "mbrWifVcXminCompRatio": mbrWifVcXminCompRatio,
       "mbrWifVcRmaxCompRatio": mbrWifVcRmaxCompRatio,
       "mbrWifVcXmaxCompRatio": mbrWifVcXmaxCompRatio,
       "mbrLanInterfaces": mbrLanInterfaces,
       "mbrLifTable": mbrLifTable,
       "mbrLifEntry": mbrLifEntry,
       "mbrLifInfo": mbrLifInfo,
       "mbrLifState": mbrLifState,
       "mbrLifMacAddress": mbrLifMacAddress,
       "mbrLifHardwareRev": mbrLifHardwareRev,
       "mbrLifLongTermStatsInterval": mbrLifLongTermStatsInterval,
       "mbrLifRingNumber": mbrLifRingNumber,
       "mbrLifStatistics": mbrLifStatistics,
       "mbrLifStatTable": mbrLifStatTable,
       "mbrLifStatEntry": mbrLifStatEntry,
       "mbrLifRcvPkts": mbrLifRcvPkts,
       "mbrLifFwdPkts": mbrLifFwdPkts,
       "mbrLifRcvMcastPkts": mbrLifRcvMcastPkts,
       "mbrLifFwdMcastPkts": mbrLifFwdMcastPkts,
       "mbrLifRcvErrPkts": mbrLifRcvErrPkts,
       "mbrLifNobufDiscPkts": mbrLifNobufDiscPkts,
       "mbrLifXmtPkts": mbrLifXmtPkts}
)
