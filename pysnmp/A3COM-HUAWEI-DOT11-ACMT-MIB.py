# SNMP MIB module (A3COM-HUAWEI-DOT11-ACMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOT11-ACMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:35 2024
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

(H3cDot11MACModeType,
 H3cDot11ObjectIDType,
 H3cDot11TunnelSecSchemType,
 h3cDot11) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-DOT11-REF-MIB",
    "H3cDot11MACModeType",
    "H3cDot11ObjectIDType",
    "H3cDot11TunnelSecSchemType",
    "h3cDot11")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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

h3cDot11ACMT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1)
)
h3cDot11ACMT.setRevisions(
        ("2010-08-04 18:00",
         "2009-08-07 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2008-07-09 18:00",
         "2007-12-21 18:00",
         "2007-06-19 18:00",
         "2007-04-27 20:00",
         "2006-05-10 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDot11ACObjectGroup_ObjectIdentity = ObjectIdentity
h3cDot11ACObjectGroup = _H3cDot11ACObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1)
)
_H3cDot11ACObject_ObjectIdentity = ObjectIdentity
h3cDot11ACObject = _H3cDot11ACObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 1)
)


class _H3cDot11CurrentACMACMode_Type(H3cDot11MACModeType):
    """Custom type h3cDot11CurrentACMACMode based on H3cDot11MACModeType"""


_H3cDot11CurrentACMACMode_Object = MibScalar
h3cDot11CurrentACMACMode = _H3cDot11CurrentACMACMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 1, 1),
    _H3cDot11CurrentACMACMode_Type()
)
h3cDot11CurrentACMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrentACMACMode.setStatus("current")
_H3cDot11MaxAPNumPermitted_Type = Integer32
_H3cDot11MaxAPNumPermitted_Object = MibScalar
h3cDot11MaxAPNumPermitted = _H3cDot11MaxAPNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 1, 2),
    _H3cDot11MaxAPNumPermitted_Type()
)
h3cDot11MaxAPNumPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MaxAPNumPermitted.setStatus("current")
_H3cDot11MaxStationNumPermitted_Type = Integer32
_H3cDot11MaxStationNumPermitted_Object = MibScalar
h3cDot11MaxStationNumPermitted = _H3cDot11MaxStationNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 1, 3),
    _H3cDot11MaxStationNumPermitted_Type()
)
h3cDot11MaxStationNumPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MaxStationNumPermitted.setStatus("current")
_H3cDot11ACLoadInfo_ObjectIdentity = ObjectIdentity
h3cDot11ACLoadInfo = _H3cDot11ACLoadInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2)
)
_H3cDot11APConnectCount_Type = Integer32
_H3cDot11APConnectCount_Object = MibScalar
h3cDot11APConnectCount = _H3cDot11APConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 1),
    _H3cDot11APConnectCount_Type()
)
h3cDot11APConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APConnectCount.setStatus("current")
_H3cDot11StationConnectCount_Type = Integer32
_H3cDot11StationConnectCount_Object = MibScalar
h3cDot11StationConnectCount = _H3cDot11StationConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 2),
    _H3cDot11StationConnectCount_Type()
)
h3cDot11StationConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationConnectCount.setStatus("current")
_H3cDot11ACIFLoadInfoTable_Object = MibTable
h3cDot11ACIFLoadInfoTable = _H3cDot11ACIFLoadInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDot11ACIFLoadInfoTable.setStatus("current")
_H3cDot11ACIFLoadInfoEntry_Object = MibTableRow
h3cDot11ACIFLoadInfoEntry = _H3cDot11ACIFLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 3, 1)
)
h3cDot11ACIFLoadInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACIfIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11ACIFLoadInfoEntry.setStatus("current")
_H3cDot11ACIfIndex_Type = Integer32
_H3cDot11ACIfIndex_Object = MibTableColumn
h3cDot11ACIfIndex = _H3cDot11ACIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 3, 1, 1),
    _H3cDot11ACIfIndex_Type()
)
h3cDot11ACIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACIfIndex.setStatus("current")
_H3cDot11ACIfApNum_Type = Integer32
_H3cDot11ACIfApNum_Object = MibTableColumn
h3cDot11ACIfApNum = _H3cDot11ACIfApNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 3, 1, 2),
    _H3cDot11ACIfApNum_Type()
)
h3cDot11ACIfApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACIfApNum.setStatus("current")
_H3cDot11ACIfStaNum_Type = Integer32
_H3cDot11ACIfStaNum_Object = MibTableColumn
h3cDot11ACIfStaNum = _H3cDot11ACIfStaNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 3, 1, 3),
    _H3cDot11ACIfStaNum_Type()
)
h3cDot11ACIfStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACIfStaNum.setStatus("current")
_H3cDot11ACIfName_Type = OctetString
_H3cDot11ACIfName_Object = MibTableColumn
h3cDot11ACIfName = _H3cDot11ACIfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 3, 1, 4),
    _H3cDot11ACIfName_Type()
)
h3cDot11ACIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACIfName.setStatus("current")
_H3cDot11MasterAPCount_Type = Integer32
_H3cDot11MasterAPCount_Object = MibScalar
h3cDot11MasterAPCount = _H3cDot11MasterAPCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 4),
    _H3cDot11MasterAPCount_Type()
)
h3cDot11MasterAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MasterAPCount.setStatus("current")
_H3cDot11SlaveAPCount_Type = Integer32
_H3cDot11SlaveAPCount_Object = MibScalar
h3cDot11SlaveAPCount = _H3cDot11SlaveAPCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 5),
    _H3cDot11SlaveAPCount_Type()
)
h3cDot11SlaveAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SlaveAPCount.setStatus("current")
_H3cDot11ConnectAutoAPCount_Type = Integer32
_H3cDot11ConnectAutoAPCount_Object = MibScalar
h3cDot11ConnectAutoAPCount = _H3cDot11ConnectAutoAPCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 6),
    _H3cDot11ConnectAutoAPCount_Type()
)
h3cDot11ConnectAutoAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ConnectAutoAPCount.setStatus("current")
_H3cDot11PersistentAPCount_Type = Integer32
_H3cDot11PersistentAPCount_Object = MibScalar
h3cDot11PersistentAPCount = _H3cDot11PersistentAPCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 7),
    _H3cDot11PersistentAPCount_Type()
)
h3cDot11PersistentAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PersistentAPCount.setStatus("current")
_H3cDot11AcUploadFrameCnt_Type = Counter64
_H3cDot11AcUploadFrameCnt_Object = MibScalar
h3cDot11AcUploadFrameCnt = _H3cDot11AcUploadFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 8),
    _H3cDot11AcUploadFrameCnt_Type()
)
h3cDot11AcUploadFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AcUploadFrameCnt.setStatus("current")
_H3cDot11AcDownloadFrameCnt_Type = Counter64
_H3cDot11AcDownloadFrameCnt_Object = MibScalar
h3cDot11AcDownloadFrameCnt = _H3cDot11AcDownloadFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 9),
    _H3cDot11AcDownloadFrameCnt_Type()
)
h3cDot11AcDownloadFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AcDownloadFrameCnt.setStatus("current")
_H3cDot11AcUploadFrameBytes_Type = Counter64
_H3cDot11AcUploadFrameBytes_Object = MibScalar
h3cDot11AcUploadFrameBytes = _H3cDot11AcUploadFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 10),
    _H3cDot11AcUploadFrameBytes_Type()
)
h3cDot11AcUploadFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AcUploadFrameBytes.setStatus("current")
_H3cDot11AcDownloadFrameBytes_Type = Counter64
_H3cDot11AcDownloadFrameBytes_Object = MibScalar
h3cDot11AcDownloadFrameBytes = _H3cDot11AcDownloadFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 11),
    _H3cDot11AcDownloadFrameBytes_Type()
)
h3cDot11AcDownloadFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AcDownloadFrameBytes.setStatus("current")


class _H3cDot11BackupACRole_Type(Integer32):
    """Custom type h3cDot11BackupACRole based on Integer32"""
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
        *(("master", 2),
          ("null", 1),
          ("slave", 3))
    )


_H3cDot11BackupACRole_Type.__name__ = "Integer32"
_H3cDot11BackupACRole_Object = MibScalar
h3cDot11BackupACRole = _H3cDot11BackupACRole_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 12),
    _H3cDot11BackupACRole_Type()
)
h3cDot11BackupACRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BackupACRole.setStatus("current")
_H3cDot11BackupACNMSIP_Type = IpAddress
_H3cDot11BackupACNMSIP_Object = MibScalar
h3cDot11BackupACNMSIP = _H3cDot11BackupACNMSIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 13),
    _H3cDot11BackupACNMSIP_Type()
)
h3cDot11BackupACNMSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BackupACNMSIP.setStatus("current")


class _H3cDot11ACBackupMode_Type(Integer32):
    """Custom type h3cDot11ACBackupMode based on Integer32"""
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
        *(("coldBackup", 3),
          ("hotBackup", 2),
          ("null", 1))
    )


_H3cDot11ACBackupMode_Type.__name__ = "Integer32"
_H3cDot11ACBackupMode_Object = MibScalar
h3cDot11ACBackupMode = _H3cDot11ACBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 14),
    _H3cDot11ACBackupMode_Type()
)
h3cDot11ACBackupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACBackupMode.setStatus("current")


class _H3cDot11ACBackupStatus_Type(Integer32):
    """Custom type h3cDot11ACBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_H3cDot11ACBackupStatus_Type.__name__ = "Integer32"
_H3cDot11ACBackupStatus_Object = MibScalar
h3cDot11ACBackupStatus = _H3cDot11ACBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 15),
    _H3cDot11ACBackupStatus_Type()
)
h3cDot11ACBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACBackupStatus.setStatus("current")
_H3cDot11ACSwitchCnt_Type = Integer32
_H3cDot11ACSwitchCnt_Object = MibScalar
h3cDot11ACSwitchCnt = _H3cDot11ACSwitchCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 2, 16),
    _H3cDot11ACSwitchCnt_Type()
)
h3cDot11ACSwitchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACSwitchCnt.setStatus("current")
_H3cDot11WLANAssocStatisInfo_ObjectIdentity = ObjectIdentity
h3cDot11WLANAssocStatisInfo = _H3cDot11WLANAssocStatisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 3)
)
_H3cDot11StationAssocSum_Type = Counter32
_H3cDot11StationAssocSum_Object = MibScalar
h3cDot11StationAssocSum = _H3cDot11StationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 3, 1),
    _H3cDot11StationAssocSum_Type()
)
h3cDot11StationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAssocSum.setStatus("current")
_H3cDot11StationAssocFailSum_Type = Counter32
_H3cDot11StationAssocFailSum_Object = MibScalar
h3cDot11StationAssocFailSum = _H3cDot11StationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 3, 2),
    _H3cDot11StationAssocFailSum_Type()
)
h3cDot11StationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAssocFailSum.setStatus("current")
_H3cDot11StationReassocSum_Type = Counter32
_H3cDot11StationReassocSum_Object = MibScalar
h3cDot11StationReassocSum = _H3cDot11StationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 3, 3),
    _H3cDot11StationReassocSum_Type()
)
h3cDot11StationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationReassocSum.setStatus("current")
_H3cDot11StationAssocRejectedSum_Type = Counter32
_H3cDot11StationAssocRejectedSum_Object = MibScalar
h3cDot11StationAssocRejectedSum = _H3cDot11StationAssocRejectedSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 3, 4),
    _H3cDot11StationAssocRejectedSum_Type()
)
h3cDot11StationAssocRejectedSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAssocRejectedSum.setStatus("current")
_H3cDot11StationExDeAuthenSum_Type = Counter32
_H3cDot11StationExDeAuthenSum_Object = MibScalar
h3cDot11StationExDeAuthenSum = _H3cDot11StationExDeAuthenSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 3, 5),
    _H3cDot11StationExDeAuthenSum_Type()
)
h3cDot11StationExDeAuthenSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationExDeAuthenSum.setStatus("current")
_H3cDot11StationCurAssocSum_Type = Integer32
_H3cDot11StationCurAssocSum_Object = MibScalar
h3cDot11StationCurAssocSum = _H3cDot11StationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 3, 6),
    _H3cDot11StationCurAssocSum_Type()
)
h3cDot11StationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationCurAssocSum.setStatus("current")
_H3cDot11ACBASInfo_ObjectIdentity = ObjectIdentity
h3cDot11ACBASInfo = _H3cDot11ACBASInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 4)
)
_H3cDot11ACBASSysObjects_ObjectIdentity = ObjectIdentity
h3cDot11ACBASSysObjects = _H3cDot11ACBASSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 4, 1)
)
_H3cDot11ACBASTableObjects_ObjectIdentity = ObjectIdentity
h3cDot11ACBASTableObjects = _H3cDot11ACBASTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 4, 2)
)
_H3cDot11ACBASIfTable_Object = MibTable
h3cDot11ACBASIfTable = _H3cDot11ACBASIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDot11ACBASIfTable.setStatus("current")
_H3cDot11ACBASIfEntry_Object = MibTableRow
h3cDot11ACBASIfEntry = _H3cDot11ACBASIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 4, 2, 3, 1)
)
h3cDot11ACBASIfEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACBASIfIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11ACBASIfEntry.setStatus("current")
_H3cDot11ACBASIfIndex_Type = Integer32
_H3cDot11ACBASIfIndex_Object = MibTableColumn
h3cDot11ACBASIfIndex = _H3cDot11ACBASIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 4, 2, 3, 1, 1),
    _H3cDot11ACBASIfIndex_Type()
)
h3cDot11ACBASIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11ACBASIfIndex.setStatus("current")


class _H3cDot11ACBASIfDescr_Type(OctetString):
    """Custom type h3cDot11ACBASIfDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11ACBASIfDescr_Type.__name__ = "OctetString"
_H3cDot11ACBASIfDescr_Object = MibTableColumn
h3cDot11ACBASIfDescr = _H3cDot11ACBASIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 4, 2, 3, 1, 2),
    _H3cDot11ACBASIfDescr_Type()
)
h3cDot11ACBASIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACBASIfDescr.setStatus("current")
_H3cDot11ACBASIfType_Type = IANAifType
_H3cDot11ACBASIfType_Object = MibTableColumn
h3cDot11ACBASIfType = _H3cDot11ACBASIfType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 4, 2, 3, 1, 3),
    _H3cDot11ACBASIfType_Type()
)
h3cDot11ACBASIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACBASIfType.setStatus("current")
_H3cDot11ACStaUserSecAuthStatis_ObjectIdentity = ObjectIdentity
h3cDot11ACStaUserSecAuthStatis = _H3cDot11ACStaUserSecAuthStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 5)
)
_H3cDot11ACStaUserAuthCurNumber_Type = Integer32
_H3cDot11ACStaUserAuthCurNumber_Object = MibScalar
h3cDot11ACStaUserAuthCurNumber = _H3cDot11ACStaUserAuthCurNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 5, 1),
    _H3cDot11ACStaUserAuthCurNumber_Type()
)
h3cDot11ACStaUserAuthCurNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACStaUserAuthCurNumber.setStatus("current")
_H3cDot11ACStaUserConnFailCnt_Type = Counter32
_H3cDot11ACStaUserConnFailCnt_Object = MibScalar
h3cDot11ACStaUserConnFailCnt = _H3cDot11ACStaUserConnFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 5, 2),
    _H3cDot11ACStaUserConnFailCnt_Type()
)
h3cDot11ACStaUserConnFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACStaUserConnFailCnt.setStatus("current")
_H3cDot11ACStaUserAuthReqCnt_Type = Counter32
_H3cDot11ACStaUserAuthReqCnt_Object = MibScalar
h3cDot11ACStaUserAuthReqCnt = _H3cDot11ACStaUserAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 5, 3),
    _H3cDot11ACStaUserAuthReqCnt_Type()
)
h3cDot11ACStaUserAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACStaUserAuthReqCnt.setStatus("current")
_H3cDot11ACStaUserAuthSuccCnt_Type = Counter32
_H3cDot11ACStaUserAuthSuccCnt_Object = MibScalar
h3cDot11ACStaUserAuthSuccCnt = _H3cDot11ACStaUserAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 5, 4),
    _H3cDot11ACStaUserAuthSuccCnt_Type()
)
h3cDot11ACStaUserAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACStaUserAuthSuccCnt.setStatus("current")
_H3cDot11ACStaUserAuthFailCnt_Type = Counter32
_H3cDot11ACStaUserAuthFailCnt_Object = MibScalar
h3cDot11ACStaUserAuthFailCnt = _H3cDot11ACStaUserAuthFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 1, 5, 5),
    _H3cDot11ACStaUserAuthFailCnt_Type()
)
h3cDot11ACStaUserAuthFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ACStaUserAuthFailCnt.setStatus("current")
_H3cDot11CAPWAPTunnelGroup_ObjectIdentity = ObjectIdentity
h3cDot11CAPWAPTunnelGroup = _H3cDot11CAPWAPTunnelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2)
)
_H3cDot11CAPWAPTunnelTable_Object = MibTable
h3cDot11CAPWAPTunnelTable = _H3cDot11CAPWAPTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11CAPWAPTunnelTable.setStatus("current")
_H3cDot11CAPWAPTunnelEntry_Object = MibTableRow
h3cDot11CAPWAPTunnelEntry = _H3cDot11CAPWAPTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2, 1, 1)
)
h3cDot11CAPWAPTunnelEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11CurrTunnelAPID"),
)
if mibBuilder.loadTexts:
    h3cDot11CAPWAPTunnelEntry.setStatus("current")
_H3cDot11CurrTunnelAPID_Type = H3cDot11ObjectIDType
_H3cDot11CurrTunnelAPID_Object = MibTableColumn
h3cDot11CurrTunnelAPID = _H3cDot11CurrTunnelAPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2, 1, 1, 1),
    _H3cDot11CurrTunnelAPID_Type()
)
h3cDot11CurrTunnelAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11CurrTunnelAPID.setStatus("current")


class _H3cDot11CtrlTunnelCurrSec_Type(H3cDot11TunnelSecSchemType):
    """Custom type h3cDot11CtrlTunnelCurrSec based on H3cDot11TunnelSecSchemType"""


_H3cDot11CtrlTunnelCurrSec_Object = MibTableColumn
h3cDot11CtrlTunnelCurrSec = _H3cDot11CtrlTunnelCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2, 1, 1, 2),
    _H3cDot11CtrlTunnelCurrSec_Type()
)
h3cDot11CtrlTunnelCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CtrlTunnelCurrSec.setStatus("current")
_H3cDot11CtrlTunnelUpTime_Type = Integer32
_H3cDot11CtrlTunnelUpTime_Object = MibTableColumn
h3cDot11CtrlTunnelUpTime = _H3cDot11CtrlTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2, 1, 1, 3),
    _H3cDot11CtrlTunnelUpTime_Type()
)
h3cDot11CtrlTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CtrlTunnelUpTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11CtrlTunnelUpTime.setUnits("second")


class _H3cDot11DataTunnelCurrSec_Type(H3cDot11TunnelSecSchemType):
    """Custom type h3cDot11DataTunnelCurrSec based on H3cDot11TunnelSecSchemType"""


_H3cDot11DataTunnelCurrSec_Object = MibTableColumn
h3cDot11DataTunnelCurrSec = _H3cDot11DataTunnelCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2, 1, 1, 4),
    _H3cDot11DataTunnelCurrSec_Type()
)
h3cDot11DataTunnelCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11DataTunnelCurrSec.setStatus("current")
_H3cDot11DataTunnelUpTime_Type = Integer32
_H3cDot11DataTunnelUpTime_Object = MibTableColumn
h3cDot11DataTunnelUpTime = _H3cDot11DataTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2, 1, 1, 5),
    _H3cDot11DataTunnelUpTime_Type()
)
h3cDot11DataTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11DataTunnelUpTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11DataTunnelUpTime.setUnits("second")
_H3cDot11CtrlTunnelUpTimeTicks_Type = TimeTicks
_H3cDot11CtrlTunnelUpTimeTicks_Object = MibTableColumn
h3cDot11CtrlTunnelUpTimeTicks = _H3cDot11CtrlTunnelUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 2, 1, 1, 6),
    _H3cDot11CtrlTunnelUpTimeTicks_Type()
)
h3cDot11CtrlTunnelUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CtrlTunnelUpTimeTicks.setStatus("current")
_H3cDot11ACMtNotifyGroup_ObjectIdentity = ObjectIdentity
h3cDot11ACMtNotifyGroup = _H3cDot11ACMtNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3)
)
_H3cDot11ACMtTraps_ObjectIdentity = ObjectIdentity
h3cDot11ACMtTraps = _H3cDot11ACMtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 0)
)
_H3cDot11ACMtTrapVarObjects_ObjectIdentity = ObjectIdentity
h3cDot11ACMtTrapVarObjects = _H3cDot11ACMtTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1)
)


class _H3cDot11ACMtTrapTunlDwnInfo_Type(Integer32):
    """Custom type h3cDot11ACMtTrapTunlDwnInfo based on Integer32"""
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
        *(("apCfgChange", 6),
          ("apCrash", 4),
          ("apDeleted", 5),
          ("apReset", 3),
          ("keyUpdateFailure", 2),
          ("tunnelTimeout", 1))
    )


_H3cDot11ACMtTrapTunlDwnInfo_Type.__name__ = "Integer32"
_H3cDot11ACMtTrapTunlDwnInfo_Object = MibScalar
h3cDot11ACMtTrapTunlDwnInfo = _H3cDot11ACMtTrapTunlDwnInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 1),
    _H3cDot11ACMtTrapTunlDwnInfo_Type()
)
h3cDot11ACMtTrapTunlDwnInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtTrapTunlDwnInfo.setStatus("current")


class _H3cDot11ACMtTrapTunlUpInfo_Type(Integer32):
    """Custom type h3cDot11ACMtTrapTunlUpInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("up", 1)
    )


_H3cDot11ACMtTrapTunlUpInfo_Type.__name__ = "Integer32"
_H3cDot11ACMtTrapTunlUpInfo_Object = MibScalar
h3cDot11ACMtTrapTunlUpInfo = _H3cDot11ACMtTrapTunlUpInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 2),
    _H3cDot11ACMtTrapTunlUpInfo_Type()
)
h3cDot11ACMtTrapTunlUpInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtTrapTunlUpInfo.setStatus("current")


class _H3cDot11ACMtTrapBackupSwitchInfo_Type(Integer32):
    """Custom type h3cDot11ACMtTrapBackupSwitchInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterToSlave", 1),
          ("slaveToMaster", 2))
    )


_H3cDot11ACMtTrapBackupSwitchInfo_Type.__name__ = "Integer32"
_H3cDot11ACMtTrapBackupSwitchInfo_Object = MibScalar
h3cDot11ACMtTrapBackupSwitchInfo = _H3cDot11ACMtTrapBackupSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 3),
    _H3cDot11ACMtTrapBackupSwitchInfo_Type()
)
h3cDot11ACMtTrapBackupSwitchInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtTrapBackupSwitchInfo.setStatus("current")
_H3cDot11ACMtTrapTnlAPName_Type = OctetString
_H3cDot11ACMtTrapTnlAPName_Object = MibScalar
h3cDot11ACMtTrapTnlAPName = _H3cDot11ACMtTrapTnlAPName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 4),
    _H3cDot11ACMtTrapTnlAPName_Type()
)
h3cDot11ACMtTrapTnlAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtTrapTnlAPName.setStatus("current")
_H3cDot11ACMtTrapTnlAPIPAddr_Type = IpAddress
_H3cDot11ACMtTrapTnlAPIPAddr_Object = MibScalar
h3cDot11ACMtTrapTnlAPIPAddr = _H3cDot11ACMtTrapTnlAPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 5),
    _H3cDot11ACMtTrapTnlAPIPAddr_Type()
)
h3cDot11ACMtTrapTnlAPIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtTrapTnlAPIPAddr.setStatus("current")


class _H3cDot11LoadBalanceType_Type(Integer32):
    """Custom type h3cDot11LoadBalanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("session", 2),
          ("traffic", 1))
    )


_H3cDot11LoadBalanceType_Type.__name__ = "Integer32"
_H3cDot11LoadBalanceType_Object = MibScalar
h3cDot11LoadBalanceType = _H3cDot11LoadBalanceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 6),
    _H3cDot11LoadBalanceType_Type()
)
h3cDot11LoadBalanceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11LoadBalanceType.setStatus("current")
_H3cDot11LoadBalanceThreshold_Type = Integer32
_H3cDot11LoadBalanceThreshold_Object = MibScalar
h3cDot11LoadBalanceThreshold = _H3cDot11LoadBalanceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 7),
    _H3cDot11LoadBalanceThreshold_Type()
)
h3cDot11LoadBalanceThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11LoadBalanceThreshold.setStatus("current")
_H3cDot11ACMtTrapAPIPv6Addr_Type = OctetString
_H3cDot11ACMtTrapAPIPv6Addr_Object = MibScalar
h3cDot11ACMtTrapAPIPv6Addr = _H3cDot11ACMtTrapAPIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 8),
    _H3cDot11ACMtTrapAPIPv6Addr_Type()
)
h3cDot11ACMtTrapAPIPv6Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtTrapAPIPv6Addr.setStatus("current")
_H3cDot11ACMtTrapTunlDwnCount_Type = Integer32
_H3cDot11ACMtTrapTunlDwnCount_Object = MibScalar
h3cDot11ACMtTrapTunlDwnCount = _H3cDot11ACMtTrapTunlDwnCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 9),
    _H3cDot11ACMtTrapTunlDwnCount_Type()
)
h3cDot11ACMtTrapTunlDwnCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtTrapTunlDwnCount.setStatus("current")
_H3cDot11ACMaxStaNum_Type = Integer32
_H3cDot11ACMaxStaNum_Object = MibScalar
h3cDot11ACMaxStaNum = _H3cDot11ACMaxStaNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 10),
    _H3cDot11ACMaxStaNum_Type()
)
h3cDot11ACMaxStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMaxStaNum.setStatus("current")
_H3cDot11ACMtTrapTnlAPSysName_Type = OctetString
_H3cDot11ACMtTrapTnlAPSysName_Object = MibScalar
h3cDot11ACMtTrapTnlAPSysName = _H3cDot11ACMtTrapTnlAPSysName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 11),
    _H3cDot11ACMtTrapTnlAPSysName_Type()
)
h3cDot11ACMtTrapTnlAPSysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtTrapTnlAPSysName.setStatus("current")
_H3cDot11ACMtFirstTrapTime_Type = TimeTicks
_H3cDot11ACMtFirstTrapTime_Object = MibScalar
h3cDot11ACMtFirstTrapTime = _H3cDot11ACMtFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 12),
    _H3cDot11ACMtFirstTrapTime_Type()
)
h3cDot11ACMtFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACMtFirstTrapTime.setStatus("current")


class _H3cDot11ACStatusSwitchInfo_Type(Integer32):
    """Custom type h3cDot11ACStatusSwitchInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeToStandby", 1),
          ("standbyToActive", 2))
    )


_H3cDot11ACStatusSwitchInfo_Type.__name__ = "Integer32"
_H3cDot11ACStatusSwitchInfo_Object = MibScalar
h3cDot11ACStatusSwitchInfo = _H3cDot11ACStatusSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 13),
    _H3cDot11ACStatusSwitchInfo_Type()
)
h3cDot11ACStatusSwitchInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ACStatusSwitchInfo.setStatus("current")
_H3cDot11SourceACNmsIP_Type = IpAddress
_H3cDot11SourceACNmsIP_Object = MibScalar
h3cDot11SourceACNmsIP = _H3cDot11SourceACNmsIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 1, 14),
    _H3cDot11SourceACNmsIP_Type()
)
h3cDot11SourceACNmsIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11SourceACNmsIP.setStatus("current")

# Managed Objects groups


# Notification objects

h3cDot11ACMtTunnelSetupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 0, 1)
)
h3cDot11ACMtTunnelSetupTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11CurrTunnelAPID"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapTunlUpInfo"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapTnlAPName"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapTnlAPIPAddr"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapAPIPv6Addr"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11ACMtTunnelSetupTrap.setStatus(
        "current"
    )

h3cDot11ACMtTunnelDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 0, 2)
)
h3cDot11ACMtTunnelDownTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11CurrTunnelAPID"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapTunlDwnInfo"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapTnlAPName"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapTnlAPIPAddr"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapAPIPv6Addr"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapTunlDwnCount"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapTnlAPSysName"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11ACMtTunnelDownTrap.setStatus(
        "current"
    )

h3cDot11ACMtBackupSwtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 0, 3)
)
h3cDot11ACMtBackupSwtTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtTrapBackupSwitchInfo"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11ACMtBackupSwtTrap.setStatus(
        "current"
    )

h3cDot11ACLoadBalanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 0, 4)
)
h3cDot11ACLoadBalanceTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11LoadBalanceType"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11LoadBalanceThreshold"))
)
if mibBuilder.loadTexts:
    h3cDot11ACLoadBalanceTrap.setStatus(
        "current"
    )

h3cDot11ACStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 0, 5)
)
h3cDot11ACStaFullTrap.setObjects(
    ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACMaxStaNum")
)
if mibBuilder.loadTexts:
    h3cDot11ACStaFullTrap.setStatus(
        "current"
    )

h3cDot11ACStatusSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 1, 3, 0, 6)
)
h3cDot11ACStatusSwitchTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11ACStatusSwitchInfo"),
        ("A3COM-HUAWEI-DOT11-ACMT-MIB", "h3cDot11SourceACNmsIP"))
)
if mibBuilder.loadTexts:
    h3cDot11ACStatusSwitchTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOT11-ACMT-MIB",
    **{"h3cDot11ACMT": h3cDot11ACMT,
       "h3cDot11ACObjectGroup": h3cDot11ACObjectGroup,
       "h3cDot11ACObject": h3cDot11ACObject,
       "h3cDot11CurrentACMACMode": h3cDot11CurrentACMACMode,
       "h3cDot11MaxAPNumPermitted": h3cDot11MaxAPNumPermitted,
       "h3cDot11MaxStationNumPermitted": h3cDot11MaxStationNumPermitted,
       "h3cDot11ACLoadInfo": h3cDot11ACLoadInfo,
       "h3cDot11APConnectCount": h3cDot11APConnectCount,
       "h3cDot11StationConnectCount": h3cDot11StationConnectCount,
       "h3cDot11ACIFLoadInfoTable": h3cDot11ACIFLoadInfoTable,
       "h3cDot11ACIFLoadInfoEntry": h3cDot11ACIFLoadInfoEntry,
       "h3cDot11ACIfIndex": h3cDot11ACIfIndex,
       "h3cDot11ACIfApNum": h3cDot11ACIfApNum,
       "h3cDot11ACIfStaNum": h3cDot11ACIfStaNum,
       "h3cDot11ACIfName": h3cDot11ACIfName,
       "h3cDot11MasterAPCount": h3cDot11MasterAPCount,
       "h3cDot11SlaveAPCount": h3cDot11SlaveAPCount,
       "h3cDot11ConnectAutoAPCount": h3cDot11ConnectAutoAPCount,
       "h3cDot11PersistentAPCount": h3cDot11PersistentAPCount,
       "h3cDot11AcUploadFrameCnt": h3cDot11AcUploadFrameCnt,
       "h3cDot11AcDownloadFrameCnt": h3cDot11AcDownloadFrameCnt,
       "h3cDot11AcUploadFrameBytes": h3cDot11AcUploadFrameBytes,
       "h3cDot11AcDownloadFrameBytes": h3cDot11AcDownloadFrameBytes,
       "h3cDot11BackupACRole": h3cDot11BackupACRole,
       "h3cDot11BackupACNMSIP": h3cDot11BackupACNMSIP,
       "h3cDot11ACBackupMode": h3cDot11ACBackupMode,
       "h3cDot11ACBackupStatus": h3cDot11ACBackupStatus,
       "h3cDot11ACSwitchCnt": h3cDot11ACSwitchCnt,
       "h3cDot11WLANAssocStatisInfo": h3cDot11WLANAssocStatisInfo,
       "h3cDot11StationAssocSum": h3cDot11StationAssocSum,
       "h3cDot11StationAssocFailSum": h3cDot11StationAssocFailSum,
       "h3cDot11StationReassocSum": h3cDot11StationReassocSum,
       "h3cDot11StationAssocRejectedSum": h3cDot11StationAssocRejectedSum,
       "h3cDot11StationExDeAuthenSum": h3cDot11StationExDeAuthenSum,
       "h3cDot11StationCurAssocSum": h3cDot11StationCurAssocSum,
       "h3cDot11ACBASInfo": h3cDot11ACBASInfo,
       "h3cDot11ACBASSysObjects": h3cDot11ACBASSysObjects,
       "h3cDot11ACBASTableObjects": h3cDot11ACBASTableObjects,
       "h3cDot11ACBASIfTable": h3cDot11ACBASIfTable,
       "h3cDot11ACBASIfEntry": h3cDot11ACBASIfEntry,
       "h3cDot11ACBASIfIndex": h3cDot11ACBASIfIndex,
       "h3cDot11ACBASIfDescr": h3cDot11ACBASIfDescr,
       "h3cDot11ACBASIfType": h3cDot11ACBASIfType,
       "h3cDot11ACStaUserSecAuthStatis": h3cDot11ACStaUserSecAuthStatis,
       "h3cDot11ACStaUserAuthCurNumber": h3cDot11ACStaUserAuthCurNumber,
       "h3cDot11ACStaUserConnFailCnt": h3cDot11ACStaUserConnFailCnt,
       "h3cDot11ACStaUserAuthReqCnt": h3cDot11ACStaUserAuthReqCnt,
       "h3cDot11ACStaUserAuthSuccCnt": h3cDot11ACStaUserAuthSuccCnt,
       "h3cDot11ACStaUserAuthFailCnt": h3cDot11ACStaUserAuthFailCnt,
       "h3cDot11CAPWAPTunnelGroup": h3cDot11CAPWAPTunnelGroup,
       "h3cDot11CAPWAPTunnelTable": h3cDot11CAPWAPTunnelTable,
       "h3cDot11CAPWAPTunnelEntry": h3cDot11CAPWAPTunnelEntry,
       "h3cDot11CurrTunnelAPID": h3cDot11CurrTunnelAPID,
       "h3cDot11CtrlTunnelCurrSec": h3cDot11CtrlTunnelCurrSec,
       "h3cDot11CtrlTunnelUpTime": h3cDot11CtrlTunnelUpTime,
       "h3cDot11DataTunnelCurrSec": h3cDot11DataTunnelCurrSec,
       "h3cDot11DataTunnelUpTime": h3cDot11DataTunnelUpTime,
       "h3cDot11CtrlTunnelUpTimeTicks": h3cDot11CtrlTunnelUpTimeTicks,
       "h3cDot11ACMtNotifyGroup": h3cDot11ACMtNotifyGroup,
       "h3cDot11ACMtTraps": h3cDot11ACMtTraps,
       "h3cDot11ACMtTunnelSetupTrap": h3cDot11ACMtTunnelSetupTrap,
       "h3cDot11ACMtTunnelDownTrap": h3cDot11ACMtTunnelDownTrap,
       "h3cDot11ACMtBackupSwtTrap": h3cDot11ACMtBackupSwtTrap,
       "h3cDot11ACLoadBalanceTrap": h3cDot11ACLoadBalanceTrap,
       "h3cDot11ACStaFullTrap": h3cDot11ACStaFullTrap,
       "h3cDot11ACStatusSwitchTrap": h3cDot11ACStatusSwitchTrap,
       "h3cDot11ACMtTrapVarObjects": h3cDot11ACMtTrapVarObjects,
       "h3cDot11ACMtTrapTunlDwnInfo": h3cDot11ACMtTrapTunlDwnInfo,
       "h3cDot11ACMtTrapTunlUpInfo": h3cDot11ACMtTrapTunlUpInfo,
       "h3cDot11ACMtTrapBackupSwitchInfo": h3cDot11ACMtTrapBackupSwitchInfo,
       "h3cDot11ACMtTrapTnlAPName": h3cDot11ACMtTrapTnlAPName,
       "h3cDot11ACMtTrapTnlAPIPAddr": h3cDot11ACMtTrapTnlAPIPAddr,
       "h3cDot11LoadBalanceType": h3cDot11LoadBalanceType,
       "h3cDot11LoadBalanceThreshold": h3cDot11LoadBalanceThreshold,
       "h3cDot11ACMtTrapAPIPv6Addr": h3cDot11ACMtTrapAPIPv6Addr,
       "h3cDot11ACMtTrapTunlDwnCount": h3cDot11ACMtTrapTunlDwnCount,
       "h3cDot11ACMaxStaNum": h3cDot11ACMaxStaNum,
       "h3cDot11ACMtTrapTnlAPSysName": h3cDot11ACMtTrapTnlAPSysName,
       "h3cDot11ACMtFirstTrapTime": h3cDot11ACMtFirstTrapTime,
       "h3cDot11ACStatusSwitchInfo": h3cDot11ACStatusSwitchInfo,
       "h3cDot11SourceACNmsIP": h3cDot11SourceACNmsIP}
)
