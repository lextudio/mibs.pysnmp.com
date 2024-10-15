# SNMP MIB module (ADTRAN-ATLAS-UNIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS-UNIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:22 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(frCircuitDlci,
 frCircuitIfIndex) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "frCircuitDlci",
    "frCircuitIfIndex")

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



class AdTftpConfigXferStatus(Integer32):
    """Custom type AdTftpConfigXferStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("downloadCopyingInternalConfig", 14),
          ("downoadWaitingOnNVRAMsave", 22),
          ("errorNotEnoughMmemory", 4),
          ("idle", 1),
          ("tftpBadConfigFile", 11),
          ("tftpBadFileChecksum", 20),
          ("tftpBadFilesize", 12),
          ("tftpDownloadComplete", 9),
          ("tftpDownloadFailed", 7),
          ("tftpDownloadInProgress", 5),
          ("tftpFileAccessViolation", 19),
          ("tftpFileAlreadyExists", 18),
          ("tftpFileRevisionTooOld", 16),
          ("tftpFilenotFound", 2),
          ("tftpFiletypeNotBinary", 15),
          ("tftpNVRAMcfgCopyFailed", 13),
          ("tftpReadNVRAMparseFailed", 21),
          ("tftpRemoteDiskFull", 17),
          ("tftpServerTimeout", 3),
          ("tftpUploadComplete", 10),
          ("tftpUploadFailed", 8),
          ("tftpUploadInProgress", 6),
          ("uploadWritingInternalConfig", 23))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLASmg_ObjectIdentity = ObjectIdentity
adATLASmg = _AdATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154)
)
_AdGenATLASmg_ObjectIdentity = ObjectIdentity
adGenATLASmg = _AdGenATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1)
)
_AdATLASUnitmg_ObjectIdentity = ObjectIdentity
adATLASUnitmg = _AdATLASUnitmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5)
)
_AdATLASUnitInfo_ObjectIdentity = ObjectIdentity
adATLASUnitInfo = _AdATLASUnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1)
)
_AdATLASUnitIfNumber_Type = Integer32
_AdATLASUnitIfNumber_Object = MibScalar
adATLASUnitIfNumber = _AdATLASUnitIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 1),
    _AdATLASUnitIfNumber_Type()
)
adATLASUnitIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUnitIfNumber.setStatus("mandatory")
_AdATLASUnitPortInfoTable_Object = MibTable
adATLASUnitPortInfoTable = _AdATLASUnitPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    adATLASUnitPortInfoTable.setStatus("mandatory")
_AdATLASUnitPortInfoEntry_Object = MibTableRow
adATLASUnitPortInfoEntry = _AdATLASUnitPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2, 1)
)
adATLASUnitPortInfoEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
    (0, "ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
)
if mibBuilder.loadTexts:
    adATLASUnitPortInfoEntry.setStatus("mandatory")


class _AdATLASUnitPortStatus_Type(Integer32):
    """Custom type adATLASUnitPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("inTest", 3),
          ("up", 1))
    )


_AdATLASUnitPortStatus_Type.__name__ = "Integer32"
_AdATLASUnitPortStatus_Object = MibTableColumn
adATLASUnitPortStatus = _AdATLASUnitPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2, 1, 1),
    _AdATLASUnitPortStatus_Type()
)
adATLASUnitPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUnitPortStatus.setStatus("mandatory")
_AdATLASUnitPortIfIndex_Type = Integer32
_AdATLASUnitPortIfIndex_Object = MibTableColumn
adATLASUnitPortIfIndex = _AdATLASUnitPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2, 1, 2),
    _AdATLASUnitPortIfIndex_Type()
)
adATLASUnitPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUnitPortIfIndex.setStatus("mandatory")
_AdATLASUnitPortDescription_Type = DisplayString
_AdATLASUnitPortDescription_Object = MibTableColumn
adATLASUnitPortDescription = _AdATLASUnitPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2, 1, 4),
    _AdATLASUnitPortDescription_Type()
)
adATLASUnitPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUnitPortDescription.setStatus("mandatory")
_AdATLASUnitPortSlotMapTable_Object = MibTable
adATLASUnitPortSlotMapTable = _AdATLASUnitPortSlotMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    adATLASUnitPortSlotMapTable.setStatus("mandatory")
_AdATLASUnitPortSlotMapEntry_Object = MibTableRow
adATLASUnitPortSlotMapEntry = _AdATLASUnitPortSlotMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 3, 1)
)
adATLASUnitPortSlotMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adATLASUnitPortSlotMapEntry.setStatus("mandatory")
_AdATLASUnitSlotAddress_Type = Integer32
_AdATLASUnitSlotAddress_Object = MibTableColumn
adATLASUnitSlotAddress = _AdATLASUnitSlotAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 3, 1, 1),
    _AdATLASUnitSlotAddress_Type()
)
adATLASUnitSlotAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUnitSlotAddress.setStatus("mandatory")
_AdATLASUnitPortAddress_Type = Integer32
_AdATLASUnitPortAddress_Object = MibTableColumn
adATLASUnitPortAddress = _AdATLASUnitPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 3, 1, 2),
    _AdATLASUnitPortAddress_Type()
)
adATLASUnitPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUnitPortAddress.setStatus("mandatory")
_AdATLASUnitUtil_ObjectIdentity = ObjectIdentity
adATLASUnitUtil = _AdATLASUnitUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3)
)
_AdATLASUpdateFw_ObjectIdentity = ObjectIdentity
adATLASUpdateFw = _AdATLASUpdateFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1)
)
_AdATLASUpdateFwModuleNum_Type = Integer32
_AdATLASUpdateFwModuleNum_Object = MibScalar
adATLASUpdateFwModuleNum = _AdATLASUpdateFwModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 1),
    _AdATLASUpdateFwModuleNum_Type()
)
adATLASUpdateFwModuleNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASUpdateFwModuleNum.setStatus("mandatory")
_AdATLASUpdateFwTFTPSrvAddr_Type = IpAddress
_AdATLASUpdateFwTFTPSrvAddr_Object = MibScalar
adATLASUpdateFwTFTPSrvAddr = _AdATLASUpdateFwTFTPSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 2),
    _AdATLASUpdateFwTFTPSrvAddr_Type()
)
adATLASUpdateFwTFTPSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASUpdateFwTFTPSrvAddr.setStatus("mandatory")
_AdATLASUpdateFwTFTPSrvFileName_Type = DisplayString
_AdATLASUpdateFwTFTPSrvFileName_Object = MibScalar
adATLASUpdateFwTFTPSrvFileName = _AdATLASUpdateFwTFTPSrvFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 3),
    _AdATLASUpdateFwTFTPSrvFileName_Type()
)
adATLASUpdateFwTFTPSrvFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASUpdateFwTFTPSrvFileName.setStatus("mandatory")
_AdATLASUpdateFwCurrStatus_Type = DisplayString
_AdATLASUpdateFwCurrStatus_Object = MibScalar
adATLASUpdateFwCurrStatus = _AdATLASUpdateFwCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 4),
    _AdATLASUpdateFwCurrStatus_Type()
)
adATLASUpdateFwCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUpdateFwCurrStatus.setStatus("mandatory")
_AdATLASUpdateFwPrevStatus_Type = DisplayString
_AdATLASUpdateFwPrevStatus_Object = MibScalar
adATLASUpdateFwPrevStatus = _AdATLASUpdateFwPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 5),
    _AdATLASUpdateFwPrevStatus_Type()
)
adATLASUpdateFwPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUpdateFwPrevStatus.setStatus("mandatory")


class _AdATLASUpdateFwControl_Type(Integer32):
    """Custom type adATLASUpdateFwControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_AdATLASUpdateFwControl_Type.__name__ = "Integer32"
_AdATLASUpdateFwControl_Object = MibScalar
adATLASUpdateFwControl = _AdATLASUpdateFwControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 6),
    _AdATLASUpdateFwControl_Type()
)
adATLASUpdateFwControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASUpdateFwControl.setStatus("mandatory")
_AdATLASConfigXfer_ObjectIdentity = ObjectIdentity
adATLASConfigXfer = _AdATLASConfigXfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2)
)
_AdATLASConfigXferTFTPSrvAddr_Type = IpAddress
_AdATLASConfigXferTFTPSrvAddr_Object = MibScalar
adATLASConfigXferTFTPSrvAddr = _AdATLASConfigXferTFTPSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 1),
    _AdATLASConfigXferTFTPSrvAddr_Type()
)
adATLASConfigXferTFTPSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASConfigXferTFTPSrvAddr.setStatus("mandatory")
_AdATLASConfigXferTFTPSrvFileName_Type = DisplayString
_AdATLASConfigXferTFTPSrvFileName_Object = MibScalar
adATLASConfigXferTFTPSrvFileName = _AdATLASConfigXferTFTPSrvFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 2),
    _AdATLASConfigXferTFTPSrvFileName_Type()
)
adATLASConfigXferTFTPSrvFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASConfigXferTFTPSrvFileName.setStatus("mandatory")
_AdATLASConfigXferCurrStatus_Type = AdTftpConfigXferStatus
_AdATLASConfigXferCurrStatus_Object = MibScalar
adATLASConfigXferCurrStatus = _AdATLASConfigXferCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 3),
    _AdATLASConfigXferCurrStatus_Type()
)
adATLASConfigXferCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASConfigXferCurrStatus.setStatus("mandatory")
_AdATLASConfigXferPrevStatus_Type = AdTftpConfigXferStatus
_AdATLASConfigXferPrevStatus_Object = MibScalar
adATLASConfigXferPrevStatus = _AdATLASConfigXferPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 4),
    _AdATLASConfigXferPrevStatus_Type()
)
adATLASConfigXferPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASConfigXferPrevStatus.setStatus("mandatory")


class _AdATLASConfigXferDwnldControl_Type(Integer32):
    """Custom type adATLASConfigXferDwnldControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loadAndUseCfg", 1)
    )


_AdATLASConfigXferDwnldControl_Type.__name__ = "Integer32"
_AdATLASConfigXferDwnldControl_Object = MibScalar
adATLASConfigXferDwnldControl = _AdATLASConfigXferDwnldControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 5),
    _AdATLASConfigXferDwnldControl_Type()
)
adATLASConfigXferDwnldControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASConfigXferDwnldControl.setStatus("mandatory")


class _AdATLASConfigXferUpldControl_Type(Integer32):
    """Custom type adATLASConfigXferUpldControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("saveCfg", 1)
    )


_AdATLASConfigXferUpldControl_Type.__name__ = "Integer32"
_AdATLASConfigXferUpldControl_Object = MibScalar
adATLASConfigXferUpldControl = _AdATLASConfigXferUpldControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 6),
    _AdATLASConfigXferUpldControl_Type()
)
adATLASConfigXferUpldControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASConfigXferUpldControl.setStatus("mandatory")
_AdATLASUnitStatus_ObjectIdentity = ObjectIdentity
adATLASUnitStatus = _AdATLASUnitStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 4)
)


class _AdATLASUnitFPStatus_Type(Integer32):
    """Custom type adATLASUnitFPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdATLASUnitFPStatus_Type.__name__ = "Integer32"
_AdATLASUnitFPStatus_Object = MibScalar
adATLASUnitFPStatus = _AdATLASUnitFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 4, 1),
    _AdATLASUnitFPStatus_Type()
)
adATLASUnitFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASUnitFPStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

adATLASFrSwToBkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400500)
)
adATLASFrSwToBkup.setObjects(
      *(("RFC1315-MIB", "frCircuitIfIndex"),
        ("RFC1315-MIB", "frCircuitDlci"))
)
if mibBuilder.loadTexts:
    adATLASFrSwToBkup.setStatus(
        ""
    )

adATLASFrSwToPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400501)
)
adATLASFrSwToPrimary.setObjects(
      *(("RFC1315-MIB", "frCircuitIfIndex"),
        ("RFC1315-MIB", "frCircuitDlci"))
)
if mibBuilder.loadTexts:
    adATLASFrSwToPrimary.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS-UNIT-MIB",
    **{"AdTftpConfigXferStatus": AdTftpConfigXferStatus,
       "adtran": adtran,
       "adMgmt": adMgmt,
       "adATLASmg": adATLASmg,
       "adATLASFrSwToBkup": adATLASFrSwToBkup,
       "adATLASFrSwToPrimary": adATLASFrSwToPrimary,
       "adGenATLASmg": adGenATLASmg,
       "adATLASUnitmg": adATLASUnitmg,
       "adATLASUnitInfo": adATLASUnitInfo,
       "adATLASUnitIfNumber": adATLASUnitIfNumber,
       "adATLASUnitPortInfoTable": adATLASUnitPortInfoTable,
       "adATLASUnitPortInfoEntry": adATLASUnitPortInfoEntry,
       "adATLASUnitPortStatus": adATLASUnitPortStatus,
       "adATLASUnitPortIfIndex": adATLASUnitPortIfIndex,
       "adATLASUnitPortDescription": adATLASUnitPortDescription,
       "adATLASUnitPortSlotMapTable": adATLASUnitPortSlotMapTable,
       "adATLASUnitPortSlotMapEntry": adATLASUnitPortSlotMapEntry,
       "adATLASUnitSlotAddress": adATLASUnitSlotAddress,
       "adATLASUnitPortAddress": adATLASUnitPortAddress,
       "adATLASUnitUtil": adATLASUnitUtil,
       "adATLASUpdateFw": adATLASUpdateFw,
       "adATLASUpdateFwModuleNum": adATLASUpdateFwModuleNum,
       "adATLASUpdateFwTFTPSrvAddr": adATLASUpdateFwTFTPSrvAddr,
       "adATLASUpdateFwTFTPSrvFileName": adATLASUpdateFwTFTPSrvFileName,
       "adATLASUpdateFwCurrStatus": adATLASUpdateFwCurrStatus,
       "adATLASUpdateFwPrevStatus": adATLASUpdateFwPrevStatus,
       "adATLASUpdateFwControl": adATLASUpdateFwControl,
       "adATLASConfigXfer": adATLASConfigXfer,
       "adATLASConfigXferTFTPSrvAddr": adATLASConfigXferTFTPSrvAddr,
       "adATLASConfigXferTFTPSrvFileName": adATLASConfigXferTFTPSrvFileName,
       "adATLASConfigXferCurrStatus": adATLASConfigXferCurrStatus,
       "adATLASConfigXferPrevStatus": adATLASConfigXferPrevStatus,
       "adATLASConfigXferDwnldControl": adATLASConfigXferDwnldControl,
       "adATLASConfigXferUpldControl": adATLASConfigXferUpldControl,
       "adATLASUnitStatus": adATLASUnitStatus,
       "adATLASUnitFPStatus": adATLASUnitFPStatus}
)
