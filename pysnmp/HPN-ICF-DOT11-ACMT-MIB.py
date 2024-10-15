# SNMP MIB module (HPN-ICF-DOT11-ACMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-ACMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:48 2024
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

(HpnicfDot11MACModeType,
 HpnicfDot11ObjectIDType,
 HpnicfDot11TunnelSecSchemType,
 hpnicfDot11) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11MACModeType",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11TunnelSecSchemType",
    "hpnicfDot11")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfDot11ACMT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1)
)
hpnicfDot11ACMT.setRevisions(
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

_HpnicfDot11ACObjectGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11ACObjectGroup = _HpnicfDot11ACObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1)
)
_HpnicfDot11ACObject_ObjectIdentity = ObjectIdentity
hpnicfDot11ACObject = _HpnicfDot11ACObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 1)
)


class _HpnicfDot11CurrentACMACMode_Type(HpnicfDot11MACModeType):
    """Custom type hpnicfDot11CurrentACMACMode based on HpnicfDot11MACModeType"""


_HpnicfDot11CurrentACMACMode_Object = MibScalar
hpnicfDot11CurrentACMACMode = _HpnicfDot11CurrentACMACMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 1, 1),
    _HpnicfDot11CurrentACMACMode_Type()
)
hpnicfDot11CurrentACMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrentACMACMode.setStatus("current")
_HpnicfDot11MaxAPNumPermitted_Type = Integer32
_HpnicfDot11MaxAPNumPermitted_Object = MibScalar
hpnicfDot11MaxAPNumPermitted = _HpnicfDot11MaxAPNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 1, 2),
    _HpnicfDot11MaxAPNumPermitted_Type()
)
hpnicfDot11MaxAPNumPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MaxAPNumPermitted.setStatus("current")
_HpnicfDot11MaxStationNumPermitted_Type = Integer32
_HpnicfDot11MaxStationNumPermitted_Object = MibScalar
hpnicfDot11MaxStationNumPermitted = _HpnicfDot11MaxStationNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 1, 3),
    _HpnicfDot11MaxStationNumPermitted_Type()
)
hpnicfDot11MaxStationNumPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MaxStationNumPermitted.setStatus("current")


class _HpnicfDot11RunAPNumThreshold_Type(Integer32):
    """Custom type hpnicfDot11RunAPNumThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_HpnicfDot11RunAPNumThreshold_Type.__name__ = "Integer32"
_HpnicfDot11RunAPNumThreshold_Object = MibScalar
hpnicfDot11RunAPNumThreshold = _HpnicfDot11RunAPNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 1, 4),
    _HpnicfDot11RunAPNumThreshold_Type()
)
hpnicfDot11RunAPNumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RunAPNumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RunAPNumThreshold.setUnits("percent")
_HpnicfDot11ACLoadInfo_ObjectIdentity = ObjectIdentity
hpnicfDot11ACLoadInfo = _HpnicfDot11ACLoadInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2)
)
_HpnicfDot11APConnectCount_Type = Integer32
_HpnicfDot11APConnectCount_Object = MibScalar
hpnicfDot11APConnectCount = _HpnicfDot11APConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 1),
    _HpnicfDot11APConnectCount_Type()
)
hpnicfDot11APConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APConnectCount.setStatus("current")
_HpnicfDot11StationConnectCount_Type = Integer32
_HpnicfDot11StationConnectCount_Object = MibScalar
hpnicfDot11StationConnectCount = _HpnicfDot11StationConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 2),
    _HpnicfDot11StationConnectCount_Type()
)
hpnicfDot11StationConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationConnectCount.setStatus("current")
_HpnicfDot11ACIFLoadInfoTable_Object = MibTable
hpnicfDot11ACIFLoadInfoTable = _HpnicfDot11ACIFLoadInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11ACIFLoadInfoTable.setStatus("current")
_HpnicfDot11ACIFLoadInfoEntry_Object = MibTableRow
hpnicfDot11ACIFLoadInfoEntry = _HpnicfDot11ACIFLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 3, 1)
)
hpnicfDot11ACIFLoadInfoEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11ACIFLoadInfoEntry.setStatus("current")
_HpnicfDot11ACIfIndex_Type = Integer32
_HpnicfDot11ACIfIndex_Object = MibTableColumn
hpnicfDot11ACIfIndex = _HpnicfDot11ACIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 3, 1, 1),
    _HpnicfDot11ACIfIndex_Type()
)
hpnicfDot11ACIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACIfIndex.setStatus("current")
_HpnicfDot11ACIfApNum_Type = Integer32
_HpnicfDot11ACIfApNum_Object = MibTableColumn
hpnicfDot11ACIfApNum = _HpnicfDot11ACIfApNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 3, 1, 2),
    _HpnicfDot11ACIfApNum_Type()
)
hpnicfDot11ACIfApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACIfApNum.setStatus("current")
_HpnicfDot11ACIfStaNum_Type = Integer32
_HpnicfDot11ACIfStaNum_Object = MibTableColumn
hpnicfDot11ACIfStaNum = _HpnicfDot11ACIfStaNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 3, 1, 3),
    _HpnicfDot11ACIfStaNum_Type()
)
hpnicfDot11ACIfStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACIfStaNum.setStatus("current")
_HpnicfDot11ACIfName_Type = OctetString
_HpnicfDot11ACIfName_Object = MibTableColumn
hpnicfDot11ACIfName = _HpnicfDot11ACIfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 3, 1, 4),
    _HpnicfDot11ACIfName_Type()
)
hpnicfDot11ACIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACIfName.setStatus("current")
_HpnicfDot11MasterAPCount_Type = Integer32
_HpnicfDot11MasterAPCount_Object = MibScalar
hpnicfDot11MasterAPCount = _HpnicfDot11MasterAPCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 4),
    _HpnicfDot11MasterAPCount_Type()
)
hpnicfDot11MasterAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MasterAPCount.setStatus("current")
_HpnicfDot11SlaveAPCount_Type = Integer32
_HpnicfDot11SlaveAPCount_Object = MibScalar
hpnicfDot11SlaveAPCount = _HpnicfDot11SlaveAPCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 5),
    _HpnicfDot11SlaveAPCount_Type()
)
hpnicfDot11SlaveAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SlaveAPCount.setStatus("current")
_HpnicfDot11ConnectAutoAPCount_Type = Integer32
_HpnicfDot11ConnectAutoAPCount_Object = MibScalar
hpnicfDot11ConnectAutoAPCount = _HpnicfDot11ConnectAutoAPCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 6),
    _HpnicfDot11ConnectAutoAPCount_Type()
)
hpnicfDot11ConnectAutoAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ConnectAutoAPCount.setStatus("current")
_HpnicfDot11PersistentAPCount_Type = Integer32
_HpnicfDot11PersistentAPCount_Object = MibScalar
hpnicfDot11PersistentAPCount = _HpnicfDot11PersistentAPCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 7),
    _HpnicfDot11PersistentAPCount_Type()
)
hpnicfDot11PersistentAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11PersistentAPCount.setStatus("current")
_HpnicfDot11AcUploadFrameCnt_Type = Counter64
_HpnicfDot11AcUploadFrameCnt_Object = MibScalar
hpnicfDot11AcUploadFrameCnt = _HpnicfDot11AcUploadFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 8),
    _HpnicfDot11AcUploadFrameCnt_Type()
)
hpnicfDot11AcUploadFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AcUploadFrameCnt.setStatus("current")
_HpnicfDot11AcDownloadFrameCnt_Type = Counter64
_HpnicfDot11AcDownloadFrameCnt_Object = MibScalar
hpnicfDot11AcDownloadFrameCnt = _HpnicfDot11AcDownloadFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 9),
    _HpnicfDot11AcDownloadFrameCnt_Type()
)
hpnicfDot11AcDownloadFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AcDownloadFrameCnt.setStatus("current")
_HpnicfDot11AcUploadFrameBytes_Type = Counter64
_HpnicfDot11AcUploadFrameBytes_Object = MibScalar
hpnicfDot11AcUploadFrameBytes = _HpnicfDot11AcUploadFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 10),
    _HpnicfDot11AcUploadFrameBytes_Type()
)
hpnicfDot11AcUploadFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AcUploadFrameBytes.setStatus("current")
_HpnicfDot11AcDownloadFrameBytes_Type = Counter64
_HpnicfDot11AcDownloadFrameBytes_Object = MibScalar
hpnicfDot11AcDownloadFrameBytes = _HpnicfDot11AcDownloadFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 11),
    _HpnicfDot11AcDownloadFrameBytes_Type()
)
hpnicfDot11AcDownloadFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AcDownloadFrameBytes.setStatus("current")


class _HpnicfDot11BackupACRole_Type(Integer32):
    """Custom type hpnicfDot11BackupACRole based on Integer32"""
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


_HpnicfDot11BackupACRole_Type.__name__ = "Integer32"
_HpnicfDot11BackupACRole_Object = MibScalar
hpnicfDot11BackupACRole = _HpnicfDot11BackupACRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 12),
    _HpnicfDot11BackupACRole_Type()
)
hpnicfDot11BackupACRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BackupACRole.setStatus("current")
_HpnicfDot11BackupACNMSIP_Type = IpAddress
_HpnicfDot11BackupACNMSIP_Object = MibScalar
hpnicfDot11BackupACNMSIP = _HpnicfDot11BackupACNMSIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 13),
    _HpnicfDot11BackupACNMSIP_Type()
)
hpnicfDot11BackupACNMSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BackupACNMSIP.setStatus("current")


class _HpnicfDot11ACBackupMode_Type(Integer32):
    """Custom type hpnicfDot11ACBackupMode based on Integer32"""
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


_HpnicfDot11ACBackupMode_Type.__name__ = "Integer32"
_HpnicfDot11ACBackupMode_Object = MibScalar
hpnicfDot11ACBackupMode = _HpnicfDot11ACBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 14),
    _HpnicfDot11ACBackupMode_Type()
)
hpnicfDot11ACBackupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACBackupMode.setStatus("current")


class _HpnicfDot11ACBackupStatus_Type(Integer32):
    """Custom type hpnicfDot11ACBackupStatus based on Integer32"""
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


_HpnicfDot11ACBackupStatus_Type.__name__ = "Integer32"
_HpnicfDot11ACBackupStatus_Object = MibScalar
hpnicfDot11ACBackupStatus = _HpnicfDot11ACBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 15),
    _HpnicfDot11ACBackupStatus_Type()
)
hpnicfDot11ACBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACBackupStatus.setStatus("current")
_HpnicfDot11ACSwitchCnt_Type = Integer32
_HpnicfDot11ACSwitchCnt_Object = MibScalar
hpnicfDot11ACSwitchCnt = _HpnicfDot11ACSwitchCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 16),
    _HpnicfDot11ACSwitchCnt_Type()
)
hpnicfDot11ACSwitchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACSwitchCnt.setStatus("current")
_HpnicfDot11ACSouthifPacketOutputCount_Type = Counter64
_HpnicfDot11ACSouthifPacketOutputCount_Object = MibScalar
hpnicfDot11ACSouthifPacketOutputCount = _HpnicfDot11ACSouthifPacketOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 17),
    _HpnicfDot11ACSouthifPacketOutputCount_Type()
)
hpnicfDot11ACSouthifPacketOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACSouthifPacketOutputCount.setStatus("current")
_HpnicfDot11ACSouthifPacketOutputBytes_Type = Counter64
_HpnicfDot11ACSouthifPacketOutputBytes_Object = MibScalar
hpnicfDot11ACSouthifPacketOutputBytes = _HpnicfDot11ACSouthifPacketOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 18),
    _HpnicfDot11ACSouthifPacketOutputBytes_Type()
)
hpnicfDot11ACSouthifPacketOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACSouthifPacketOutputBytes.setStatus("current")
_HpnicfDot11ACSouthifPacketInputCount_Type = Counter64
_HpnicfDot11ACSouthifPacketInputCount_Object = MibScalar
hpnicfDot11ACSouthifPacketInputCount = _HpnicfDot11ACSouthifPacketInputCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 19),
    _HpnicfDot11ACSouthifPacketInputCount_Type()
)
hpnicfDot11ACSouthifPacketInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACSouthifPacketInputCount.setStatus("current")
_HpnicfDot11ACSouthifPacketInputBytes_Type = Counter64
_HpnicfDot11ACSouthifPacketInputBytes_Object = MibScalar
hpnicfDot11ACSouthifPacketInputBytes = _HpnicfDot11ACSouthifPacketInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 20),
    _HpnicfDot11ACSouthifPacketInputBytes_Type()
)
hpnicfDot11ACSouthifPacketInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACSouthifPacketInputBytes.setStatus("current")
_HpnicfDot11TotalAPconnected_Type = Integer32
_HpnicfDot11TotalAPconnected_Object = MibScalar
hpnicfDot11TotalAPconnected = _HpnicfDot11TotalAPconnected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 21),
    _HpnicfDot11TotalAPconnected_Type()
)
hpnicfDot11TotalAPconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TotalAPconnected.setStatus("current")
_HpnicfDot11RemainingAPcapacity_Type = Integer32
_HpnicfDot11RemainingAPcapacity_Object = MibScalar
hpnicfDot11RemainingAPcapacity = _HpnicfDot11RemainingAPcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 2, 22),
    _HpnicfDot11RemainingAPcapacity_Type()
)
hpnicfDot11RemainingAPcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RemainingAPcapacity.setStatus("current")
_HpnicfDot11WLANAssocStatisInfo_ObjectIdentity = ObjectIdentity
hpnicfDot11WLANAssocStatisInfo = _HpnicfDot11WLANAssocStatisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3)
)
_HpnicfDot11StationAssocSum_Type = Counter32
_HpnicfDot11StationAssocSum_Object = MibScalar
hpnicfDot11StationAssocSum = _HpnicfDot11StationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 1),
    _HpnicfDot11StationAssocSum_Type()
)
hpnicfDot11StationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAssocSum.setStatus("current")
_HpnicfDot11StationAssocFailSum_Type = Counter32
_HpnicfDot11StationAssocFailSum_Object = MibScalar
hpnicfDot11StationAssocFailSum = _HpnicfDot11StationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 2),
    _HpnicfDot11StationAssocFailSum_Type()
)
hpnicfDot11StationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAssocFailSum.setStatus("current")
_HpnicfDot11StationReassocSum_Type = Counter32
_HpnicfDot11StationReassocSum_Object = MibScalar
hpnicfDot11StationReassocSum = _HpnicfDot11StationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 3),
    _HpnicfDot11StationReassocSum_Type()
)
hpnicfDot11StationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationReassocSum.setStatus("current")
_HpnicfDot11StationAssocRejectedSum_Type = Counter32
_HpnicfDot11StationAssocRejectedSum_Object = MibScalar
hpnicfDot11StationAssocRejectedSum = _HpnicfDot11StationAssocRejectedSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 4),
    _HpnicfDot11StationAssocRejectedSum_Type()
)
hpnicfDot11StationAssocRejectedSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAssocRejectedSum.setStatus("current")
_HpnicfDot11StationExDeAuthenSum_Type = Counter32
_HpnicfDot11StationExDeAuthenSum_Object = MibScalar
hpnicfDot11StationExDeAuthenSum = _HpnicfDot11StationExDeAuthenSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 5),
    _HpnicfDot11StationExDeAuthenSum_Type()
)
hpnicfDot11StationExDeAuthenSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationExDeAuthenSum.setStatus("current")
_HpnicfDot11StationCurAssocSum_Type = Integer32
_HpnicfDot11StationCurAssocSum_Object = MibScalar
hpnicfDot11StationCurAssocSum = _HpnicfDot11StationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 6),
    _HpnicfDot11StationCurAssocSum_Type()
)
hpnicfDot11StationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationCurAssocSum.setStatus("current")
_HpnicfDot11StationAssocReqSum_Type = Counter32
_HpnicfDot11StationAssocReqSum_Object = MibScalar
hpnicfDot11StationAssocReqSum = _HpnicfDot11StationAssocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 7),
    _HpnicfDot11StationAssocReqSum_Type()
)
hpnicfDot11StationAssocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAssocReqSum.setStatus("current")
_HpnicfDot11StationReassocReqSum_Type = Counter32
_HpnicfDot11StationReassocReqSum_Object = MibScalar
hpnicfDot11StationReassocReqSum = _HpnicfDot11StationReassocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 8),
    _HpnicfDot11StationReassocReqSum_Type()
)
hpnicfDot11StationReassocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationReassocReqSum.setStatus("current")
_HpnicfDot11StationReassocFailSum_Type = Counter32
_HpnicfDot11StationReassocFailSum_Object = MibScalar
hpnicfDot11StationReassocFailSum = _HpnicfDot11StationReassocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 3, 9),
    _HpnicfDot11StationReassocFailSum_Type()
)
hpnicfDot11StationReassocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationReassocFailSum.setStatus("current")
_HpnicfDot11ACBASInfo_ObjectIdentity = ObjectIdentity
hpnicfDot11ACBASInfo = _HpnicfDot11ACBASInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 4)
)
_HpnicfDot11ACBASSysObjects_ObjectIdentity = ObjectIdentity
hpnicfDot11ACBASSysObjects = _HpnicfDot11ACBASSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 4, 1)
)
_HpnicfDot11ACBASTableObjects_ObjectIdentity = ObjectIdentity
hpnicfDot11ACBASTableObjects = _HpnicfDot11ACBASTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 4, 2)
)
_HpnicfDot11ACBASIfTable_Object = MibTable
hpnicfDot11ACBASIfTable = _HpnicfDot11ACBASIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11ACBASIfTable.setStatus("current")
_HpnicfDot11ACBASIfEntry_Object = MibTableRow
hpnicfDot11ACBASIfEntry = _HpnicfDot11ACBASIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 4, 2, 3, 1)
)
hpnicfDot11ACBASIfEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACBASIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11ACBASIfEntry.setStatus("current")
_HpnicfDot11ACBASIfIndex_Type = Integer32
_HpnicfDot11ACBASIfIndex_Object = MibTableColumn
hpnicfDot11ACBASIfIndex = _HpnicfDot11ACBASIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 4, 2, 3, 1, 1),
    _HpnicfDot11ACBASIfIndex_Type()
)
hpnicfDot11ACBASIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11ACBASIfIndex.setStatus("current")


class _HpnicfDot11ACBASIfDescr_Type(OctetString):
    """Custom type hpnicfDot11ACBASIfDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11ACBASIfDescr_Type.__name__ = "OctetString"
_HpnicfDot11ACBASIfDescr_Object = MibTableColumn
hpnicfDot11ACBASIfDescr = _HpnicfDot11ACBASIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 4, 2, 3, 1, 2),
    _HpnicfDot11ACBASIfDescr_Type()
)
hpnicfDot11ACBASIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACBASIfDescr.setStatus("current")
_HpnicfDot11ACBASIfType_Type = IANAifType
_HpnicfDot11ACBASIfType_Object = MibTableColumn
hpnicfDot11ACBASIfType = _HpnicfDot11ACBASIfType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 4, 2, 3, 1, 3),
    _HpnicfDot11ACBASIfType_Type()
)
hpnicfDot11ACBASIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACBASIfType.setStatus("current")
_HpnicfDot11ACStaUserSecAuthStatis_ObjectIdentity = ObjectIdentity
hpnicfDot11ACStaUserSecAuthStatis = _HpnicfDot11ACStaUserSecAuthStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 5)
)
_HpnicfDot11ACStaUserAuthCurNumber_Type = Integer32
_HpnicfDot11ACStaUserAuthCurNumber_Object = MibScalar
hpnicfDot11ACStaUserAuthCurNumber = _HpnicfDot11ACStaUserAuthCurNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 5, 1),
    _HpnicfDot11ACStaUserAuthCurNumber_Type()
)
hpnicfDot11ACStaUserAuthCurNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAuthCurNumber.setStatus("current")
_HpnicfDot11ACStaUserConnFailCnt_Type = Counter32
_HpnicfDot11ACStaUserConnFailCnt_Object = MibScalar
hpnicfDot11ACStaUserConnFailCnt = _HpnicfDot11ACStaUserConnFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 5, 2),
    _HpnicfDot11ACStaUserConnFailCnt_Type()
)
hpnicfDot11ACStaUserConnFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserConnFailCnt.setStatus("current")
_HpnicfDot11ACStaUserAuthReqCnt_Type = Counter32
_HpnicfDot11ACStaUserAuthReqCnt_Object = MibScalar
hpnicfDot11ACStaUserAuthReqCnt = _HpnicfDot11ACStaUserAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 5, 3),
    _HpnicfDot11ACStaUserAuthReqCnt_Type()
)
hpnicfDot11ACStaUserAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAuthReqCnt.setStatus("current")
_HpnicfDot11ACStaUserAuthSuccCnt_Type = Counter32
_HpnicfDot11ACStaUserAuthSuccCnt_Object = MibScalar
hpnicfDot11ACStaUserAuthSuccCnt = _HpnicfDot11ACStaUserAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 5, 4),
    _HpnicfDot11ACStaUserAuthSuccCnt_Type()
)
hpnicfDot11ACStaUserAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAuthSuccCnt.setStatus("current")
_HpnicfDot11ACStaUserAuthFailCnt_Type = Counter32
_HpnicfDot11ACStaUserAuthFailCnt_Object = MibScalar
hpnicfDot11ACStaUserAuthFailCnt = _HpnicfDot11ACStaUserAuthFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 5, 5),
    _HpnicfDot11ACStaUserAuthFailCnt_Type()
)
hpnicfDot11ACStaUserAuthFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAuthFailCnt.setStatus("current")
_HpnicfDot11ACStaUserAllAuthCntCM_Type = Counter32
_HpnicfDot11ACStaUserAllAuthCntCM_Object = MibScalar
hpnicfDot11ACStaUserAllAuthCntCM = _HpnicfDot11ACStaUserAllAuthCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 5, 6),
    _HpnicfDot11ACStaUserAllAuthCntCM_Type()
)
hpnicfDot11ACStaUserAllAuthCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAllAuthCntCM.setStatus("current")
_HpnicfDot11ACStaSecAuthTypeStatis_ObjectIdentity = ObjectIdentity
hpnicfDot11ACStaSecAuthTypeStatis = _HpnicfDot11ACStaSecAuthTypeStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6)
)
_HpnicfDot11ACStaUserPortalOnlineNum_Type = Integer32
_HpnicfDot11ACStaUserPortalOnlineNum_Object = MibScalar
hpnicfDot11ACStaUserPortalOnlineNum = _HpnicfDot11ACStaUserPortalOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 1),
    _HpnicfDot11ACStaUserPortalOnlineNum_Type()
)
hpnicfDot11ACStaUserPortalOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserPortalOnlineNum.setStatus("current")
_HpnicfDot11ACStaUserFreeAuthOnlineNum_Type = Integer32
_HpnicfDot11ACStaUserFreeAuthOnlineNum_Object = MibScalar
hpnicfDot11ACStaUserFreeAuthOnlineNum = _HpnicfDot11ACStaUserFreeAuthOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 2),
    _HpnicfDot11ACStaUserFreeAuthOnlineNum_Type()
)
hpnicfDot11ACStaUserFreeAuthOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserFreeAuthOnlineNum.setStatus("current")
_HpnicfDot11ACStaUserAssociateAuthOnlineNum_Type = Integer32
_HpnicfDot11ACStaUserAssociateAuthOnlineNum_Object = MibScalar
hpnicfDot11ACStaUserAssociateAuthOnlineNum = _HpnicfDot11ACStaUserAssociateAuthOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 3),
    _HpnicfDot11ACStaUserAssociateAuthOnlineNum_Type()
)
hpnicfDot11ACStaUserAssociateAuthOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAssociateAuthOnlineNum.setStatus("current")
_HpnicfDot11ACStaUserMacAuthOnlineNum_Type = Integer32
_HpnicfDot11ACStaUserMacAuthOnlineNum_Object = MibScalar
hpnicfDot11ACStaUserMacAuthOnlineNum = _HpnicfDot11ACStaUserMacAuthOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 4),
    _HpnicfDot11ACStaUserMacAuthOnlineNum_Type()
)
hpnicfDot11ACStaUserMacAuthOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserMacAuthOnlineNum.setStatus("current")
_HpnicfDot11ACStaUserPortalLostConnectionCnt_Type = Counter32
_HpnicfDot11ACStaUserPortalLostConnectionCnt_Object = MibScalar
hpnicfDot11ACStaUserPortalLostConnectionCnt = _HpnicfDot11ACStaUserPortalLostConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 5),
    _HpnicfDot11ACStaUserPortalLostConnectionCnt_Type()
)
hpnicfDot11ACStaUserPortalLostConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserPortalLostConnectionCnt.setStatus("current")
_HpnicfDot11ACStaUserFreeAuthLostConnectionCnt_Type = Counter32
_HpnicfDot11ACStaUserFreeAuthLostConnectionCnt_Object = MibScalar
hpnicfDot11ACStaUserFreeAuthLostConnectionCnt = _HpnicfDot11ACStaUserFreeAuthLostConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 6),
    _HpnicfDot11ACStaUserFreeAuthLostConnectionCnt_Type()
)
hpnicfDot11ACStaUserFreeAuthLostConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserFreeAuthLostConnectionCnt.setStatus("current")
_HpnicfDot11ACStaUserAssociateAuthLostConnectionCnt_Type = Counter32
_HpnicfDot11ACStaUserAssociateAuthLostConnectionCnt_Object = MibScalar
hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt = _HpnicfDot11ACStaUserAssociateAuthLostConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 7),
    _HpnicfDot11ACStaUserAssociateAuthLostConnectionCnt_Type()
)
hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt.setStatus("current")
_HpnicfDot11ACStaUserMacAuthLostConnectionCnt_Type = Counter32
_HpnicfDot11ACStaUserMacAuthLostConnectionCnt_Object = MibScalar
hpnicfDot11ACStaUserMacAuthLostConnectionCnt = _HpnicfDot11ACStaUserMacAuthLostConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 8),
    _HpnicfDot11ACStaUserMacAuthLostConnectionCnt_Type()
)
hpnicfDot11ACStaUserMacAuthLostConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserMacAuthLostConnectionCnt.setStatus("current")
_HpnicfDot11ACStaPortalAuthReqCnt_Type = Counter32
_HpnicfDot11ACStaPortalAuthReqCnt_Object = MibScalar
hpnicfDot11ACStaPortalAuthReqCnt = _HpnicfDot11ACStaPortalAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 9),
    _HpnicfDot11ACStaPortalAuthReqCnt_Type()
)
hpnicfDot11ACStaPortalAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaPortalAuthReqCnt.setStatus("current")
_HpnicfDot11ACStaAssociateAuthReqCnt_Type = Counter32
_HpnicfDot11ACStaAssociateAuthReqCnt_Object = MibScalar
hpnicfDot11ACStaAssociateAuthReqCnt = _HpnicfDot11ACStaAssociateAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 10),
    _HpnicfDot11ACStaAssociateAuthReqCnt_Type()
)
hpnicfDot11ACStaAssociateAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaAssociateAuthReqCnt.setStatus("current")
_HpnicfDot11ACStaMacAuthReqCnt_Type = Counter32
_HpnicfDot11ACStaMacAuthReqCnt_Object = MibScalar
hpnicfDot11ACStaMacAuthReqCnt = _HpnicfDot11ACStaMacAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 11),
    _HpnicfDot11ACStaMacAuthReqCnt_Type()
)
hpnicfDot11ACStaMacAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaMacAuthReqCnt.setStatus("current")
_HpnicfDot11ACStaPortalAuthSuccCnt_Type = Counter32
_HpnicfDot11ACStaPortalAuthSuccCnt_Object = MibScalar
hpnicfDot11ACStaPortalAuthSuccCnt = _HpnicfDot11ACStaPortalAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 12),
    _HpnicfDot11ACStaPortalAuthSuccCnt_Type()
)
hpnicfDot11ACStaPortalAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaPortalAuthSuccCnt.setStatus("current")
_HpnicfDot11ACStaAssociateAuthSuccCnt_Type = Counter32
_HpnicfDot11ACStaAssociateAuthSuccCnt_Object = MibScalar
hpnicfDot11ACStaAssociateAuthSuccCnt = _HpnicfDot11ACStaAssociateAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 13),
    _HpnicfDot11ACStaAssociateAuthSuccCnt_Type()
)
hpnicfDot11ACStaAssociateAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaAssociateAuthSuccCnt.setStatus("current")
_HpnicfDot11ACStaMacAuthSuccCnt_Type = Counter32
_HpnicfDot11ACStaMacAuthSuccCnt_Object = MibScalar
hpnicfDot11ACStaMacAuthSuccCnt = _HpnicfDot11ACStaMacAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 14),
    _HpnicfDot11ACStaMacAuthSuccCnt_Type()
)
hpnicfDot11ACStaMacAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaMacAuthSuccCnt.setStatus("current")
_HpnicfDot11ACStaPortalAuthReqFailCnt_Type = Counter32
_HpnicfDot11ACStaPortalAuthReqFailCnt_Object = MibScalar
hpnicfDot11ACStaPortalAuthReqFailCnt = _HpnicfDot11ACStaPortalAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 15),
    _HpnicfDot11ACStaPortalAuthReqFailCnt_Type()
)
hpnicfDot11ACStaPortalAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaPortalAuthReqFailCnt.setStatus("current")
_HpnicfDot11ACStaAssociateAuthReqFailCnt_Type = Counter32
_HpnicfDot11ACStaAssociateAuthReqFailCnt_Object = MibScalar
hpnicfDot11ACStaAssociateAuthReqFailCnt = _HpnicfDot11ACStaAssociateAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 16),
    _HpnicfDot11ACStaAssociateAuthReqFailCnt_Type()
)
hpnicfDot11ACStaAssociateAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaAssociateAuthReqFailCnt.setStatus("current")
_HpnicfDot11ACStaMacAuthReqFailCnt_Type = Counter32
_HpnicfDot11ACStaMacAuthReqFailCnt_Object = MibScalar
hpnicfDot11ACStaMacAuthReqFailCnt = _HpnicfDot11ACStaMacAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 17),
    _HpnicfDot11ACStaMacAuthReqFailCnt_Type()
)
hpnicfDot11ACStaMacAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaMacAuthReqFailCnt.setStatus("current")
_HpnicfDot11ACStaUserAutoAuthOnlineNumCM_Type = Integer32
_HpnicfDot11ACStaUserAutoAuthOnlineNumCM_Object = MibScalar
hpnicfDot11ACStaUserAutoAuthOnlineNumCM = _HpnicfDot11ACStaUserAutoAuthOnlineNumCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 18),
    _HpnicfDot11ACStaUserAutoAuthOnlineNumCM_Type()
)
hpnicfDot11ACStaUserAutoAuthOnlineNumCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAutoAuthOnlineNumCM.setStatus("current")
_HpnicfDot11ACStaUserAutoAuthLostConnectionCntCM_Type = Counter32
_HpnicfDot11ACStaUserAutoAuthLostConnectionCntCM_Object = MibScalar
hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM = _HpnicfDot11ACStaUserAutoAuthLostConnectionCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 19),
    _HpnicfDot11ACStaUserAutoAuthLostConnectionCntCM_Type()
)
hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM.setStatus("current")
_HpnicfDot11ACStaAutoAuthReqCntCM_Type = Counter32
_HpnicfDot11ACStaAutoAuthReqCntCM_Object = MibScalar
hpnicfDot11ACStaAutoAuthReqCntCM = _HpnicfDot11ACStaAutoAuthReqCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 20),
    _HpnicfDot11ACStaAutoAuthReqCntCM_Type()
)
hpnicfDot11ACStaAutoAuthReqCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaAutoAuthReqCntCM.setStatus("current")
_HpnicfDot11ACStaAutoAuthSuccCntCM_Type = Counter32
_HpnicfDot11ACStaAutoAuthSuccCntCM_Object = MibScalar
hpnicfDot11ACStaAutoAuthSuccCntCM = _HpnicfDot11ACStaAutoAuthSuccCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 21),
    _HpnicfDot11ACStaAutoAuthSuccCntCM_Type()
)
hpnicfDot11ACStaAutoAuthSuccCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaAutoAuthSuccCntCM.setStatus("current")
_HpnicfDot11ACStaAutoAuthReqFailCntCM_Type = Counter32
_HpnicfDot11ACStaAutoAuthReqFailCntCM_Object = MibScalar
hpnicfDot11ACStaAutoAuthReqFailCntCM = _HpnicfDot11ACStaAutoAuthReqFailCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 6, 22),
    _HpnicfDot11ACStaAutoAuthReqFailCntCM_Type()
)
hpnicfDot11ACStaAutoAuthReqFailCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACStaAutoAuthReqFailCntCM.setStatus("current")
_HpnicfDot11ACPortalStatisticCMTable_Object = MibTable
hpnicfDot11ACPortalStatisticCMTable = _HpnicfDot11ACPortalStatisticCMTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfDot11ACPortalStatisticCMTable.setStatus("current")
_HpnicfDot11ACPortalStatisticCMEntry_Object = MibTableRow
hpnicfDot11ACPortalStatisticCMEntry = _HpnicfDot11ACPortalStatisticCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 7, 1)
)
hpnicfDot11ACPortalStatisticCMEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACPortalStatisticSSIDCM"),
)
if mibBuilder.loadTexts:
    hpnicfDot11ACPortalStatisticCMEntry.setStatus("current")


class _HpnicfDot11ACPortalStatisticSSIDCM_Type(OctetString):
    """Custom type hpnicfDot11ACPortalStatisticSSIDCM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfDot11ACPortalStatisticSSIDCM_Type.__name__ = "OctetString"
_HpnicfDot11ACPortalStatisticSSIDCM_Object = MibTableColumn
hpnicfDot11ACPortalStatisticSSIDCM = _HpnicfDot11ACPortalStatisticSSIDCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 7, 1, 1),
    _HpnicfDot11ACPortalStatisticSSIDCM_Type()
)
hpnicfDot11ACPortalStatisticSSIDCM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11ACPortalStatisticSSIDCM.setStatus("current")
_HpnicfDot11ACPortalStatAuthReqCM_Type = Counter32
_HpnicfDot11ACPortalStatAuthReqCM_Object = MibTableColumn
hpnicfDot11ACPortalStatAuthReqCM = _HpnicfDot11ACPortalStatAuthReqCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 7, 1, 2),
    _HpnicfDot11ACPortalStatAuthReqCM_Type()
)
hpnicfDot11ACPortalStatAuthReqCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACPortalStatAuthReqCM.setStatus("current")
_HpnicfDot11ACPortalStatAuthRespCM_Type = Counter32
_HpnicfDot11ACPortalStatAuthRespCM_Object = MibTableColumn
hpnicfDot11ACPortalStatAuthRespCM = _HpnicfDot11ACPortalStatAuthRespCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 1, 7, 1, 3),
    _HpnicfDot11ACPortalStatAuthRespCM_Type()
)
hpnicfDot11ACPortalStatAuthRespCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ACPortalStatAuthRespCM.setStatus("current")
_HpnicfDot11CAPWAPTunnelGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11CAPWAPTunnelGroup = _HpnicfDot11CAPWAPTunnelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2)
)
_HpnicfDot11CAPWAPTunnelTable_Object = MibTable
hpnicfDot11CAPWAPTunnelTable = _HpnicfDot11CAPWAPTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11CAPWAPTunnelTable.setStatus("current")
_HpnicfDot11CAPWAPTunnelEntry_Object = MibTableRow
hpnicfDot11CAPWAPTunnelEntry = _HpnicfDot11CAPWAPTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2, 1, 1)
)
hpnicfDot11CAPWAPTunnelEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11CurrTunnelAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11CAPWAPTunnelEntry.setStatus("current")
_HpnicfDot11CurrTunnelAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11CurrTunnelAPID_Object = MibTableColumn
hpnicfDot11CurrTunnelAPID = _HpnicfDot11CurrTunnelAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2, 1, 1, 1),
    _HpnicfDot11CurrTunnelAPID_Type()
)
hpnicfDot11CurrTunnelAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11CurrTunnelAPID.setStatus("current")


class _HpnicfDot11CtrlTunnelCurrSec_Type(HpnicfDot11TunnelSecSchemType):
    """Custom type hpnicfDot11CtrlTunnelCurrSec based on HpnicfDot11TunnelSecSchemType"""


_HpnicfDot11CtrlTunnelCurrSec_Object = MibTableColumn
hpnicfDot11CtrlTunnelCurrSec = _HpnicfDot11CtrlTunnelCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2, 1, 1, 2),
    _HpnicfDot11CtrlTunnelCurrSec_Type()
)
hpnicfDot11CtrlTunnelCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CtrlTunnelCurrSec.setStatus("current")
_HpnicfDot11CtrlTunnelUpTime_Type = Integer32
_HpnicfDot11CtrlTunnelUpTime_Object = MibTableColumn
hpnicfDot11CtrlTunnelUpTime = _HpnicfDot11CtrlTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2, 1, 1, 3),
    _HpnicfDot11CtrlTunnelUpTime_Type()
)
hpnicfDot11CtrlTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CtrlTunnelUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11CtrlTunnelUpTime.setUnits("second")


class _HpnicfDot11DataTunnelCurrSec_Type(HpnicfDot11TunnelSecSchemType):
    """Custom type hpnicfDot11DataTunnelCurrSec based on HpnicfDot11TunnelSecSchemType"""


_HpnicfDot11DataTunnelCurrSec_Object = MibTableColumn
hpnicfDot11DataTunnelCurrSec = _HpnicfDot11DataTunnelCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2, 1, 1, 4),
    _HpnicfDot11DataTunnelCurrSec_Type()
)
hpnicfDot11DataTunnelCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DataTunnelCurrSec.setStatus("current")
_HpnicfDot11DataTunnelUpTime_Type = Integer32
_HpnicfDot11DataTunnelUpTime_Object = MibTableColumn
hpnicfDot11DataTunnelUpTime = _HpnicfDot11DataTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2, 1, 1, 5),
    _HpnicfDot11DataTunnelUpTime_Type()
)
hpnicfDot11DataTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DataTunnelUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11DataTunnelUpTime.setUnits("second")
_HpnicfDot11CtrlTunnelUpTimeTicks_Type = TimeTicks
_HpnicfDot11CtrlTunnelUpTimeTicks_Object = MibTableColumn
hpnicfDot11CtrlTunnelUpTimeTicks = _HpnicfDot11CtrlTunnelUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 2, 1, 1, 6),
    _HpnicfDot11CtrlTunnelUpTimeTicks_Type()
)
hpnicfDot11CtrlTunnelUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CtrlTunnelUpTimeTicks.setStatus("current")
_HpnicfDot11ACMtNotifyGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11ACMtNotifyGroup = _HpnicfDot11ACMtNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3)
)
_HpnicfDot11ACMtTraps_ObjectIdentity = ObjectIdentity
hpnicfDot11ACMtTraps = _HpnicfDot11ACMtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0)
)
_HpnicfDot11ACMtTrapVarObjects_ObjectIdentity = ObjectIdentity
hpnicfDot11ACMtTrapVarObjects = _HpnicfDot11ACMtTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1)
)


class _HpnicfDot11ACMtTrapTunlDwnInfo_Type(Integer32):
    """Custom type hpnicfDot11ACMtTrapTunlDwnInfo based on Integer32"""
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


_HpnicfDot11ACMtTrapTunlDwnInfo_Type.__name__ = "Integer32"
_HpnicfDot11ACMtTrapTunlDwnInfo_Object = MibScalar
hpnicfDot11ACMtTrapTunlDwnInfo = _HpnicfDot11ACMtTrapTunlDwnInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 1),
    _HpnicfDot11ACMtTrapTunlDwnInfo_Type()
)
hpnicfDot11ACMtTrapTunlDwnInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapTunlDwnInfo.setStatus("current")


class _HpnicfDot11ACMtTrapTunlUpInfo_Type(Integer32):
    """Custom type hpnicfDot11ACMtTrapTunlUpInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("up", 1)
    )


_HpnicfDot11ACMtTrapTunlUpInfo_Type.__name__ = "Integer32"
_HpnicfDot11ACMtTrapTunlUpInfo_Object = MibScalar
hpnicfDot11ACMtTrapTunlUpInfo = _HpnicfDot11ACMtTrapTunlUpInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 2),
    _HpnicfDot11ACMtTrapTunlUpInfo_Type()
)
hpnicfDot11ACMtTrapTunlUpInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapTunlUpInfo.setStatus("current")


class _HpnicfDot11ACMtTrapBackupSwitchInfo_Type(Integer32):
    """Custom type hpnicfDot11ACMtTrapBackupSwitchInfo based on Integer32"""
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


_HpnicfDot11ACMtTrapBackupSwitchInfo_Type.__name__ = "Integer32"
_HpnicfDot11ACMtTrapBackupSwitchInfo_Object = MibScalar
hpnicfDot11ACMtTrapBackupSwitchInfo = _HpnicfDot11ACMtTrapBackupSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 3),
    _HpnicfDot11ACMtTrapBackupSwitchInfo_Type()
)
hpnicfDot11ACMtTrapBackupSwitchInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapBackupSwitchInfo.setStatus("current")
_HpnicfDot11ACMtTrapTnlAPName_Type = OctetString
_HpnicfDot11ACMtTrapTnlAPName_Object = MibScalar
hpnicfDot11ACMtTrapTnlAPName = _HpnicfDot11ACMtTrapTnlAPName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 4),
    _HpnicfDot11ACMtTrapTnlAPName_Type()
)
hpnicfDot11ACMtTrapTnlAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapTnlAPName.setStatus("current")
_HpnicfDot11ACMtTrapTnlAPIPAddr_Type = IpAddress
_HpnicfDot11ACMtTrapTnlAPIPAddr_Object = MibScalar
hpnicfDot11ACMtTrapTnlAPIPAddr = _HpnicfDot11ACMtTrapTnlAPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 5),
    _HpnicfDot11ACMtTrapTnlAPIPAddr_Type()
)
hpnicfDot11ACMtTrapTnlAPIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapTnlAPIPAddr.setStatus("current")


class _HpnicfDot11LoadBalanceType_Type(Integer32):
    """Custom type hpnicfDot11LoadBalanceType based on Integer32"""
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


_HpnicfDot11LoadBalanceType_Type.__name__ = "Integer32"
_HpnicfDot11LoadBalanceType_Object = MibScalar
hpnicfDot11LoadBalanceType = _HpnicfDot11LoadBalanceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 6),
    _HpnicfDot11LoadBalanceType_Type()
)
hpnicfDot11LoadBalanceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11LoadBalanceType.setStatus("current")
_HpnicfDot11LoadBalanceThreshold_Type = Integer32
_HpnicfDot11LoadBalanceThreshold_Object = MibScalar
hpnicfDot11LoadBalanceThreshold = _HpnicfDot11LoadBalanceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 7),
    _HpnicfDot11LoadBalanceThreshold_Type()
)
hpnicfDot11LoadBalanceThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11LoadBalanceThreshold.setStatus("current")
_HpnicfDot11ACMtTrapAPIPv6Addr_Type = OctetString
_HpnicfDot11ACMtTrapAPIPv6Addr_Object = MibScalar
hpnicfDot11ACMtTrapAPIPv6Addr = _HpnicfDot11ACMtTrapAPIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 8),
    _HpnicfDot11ACMtTrapAPIPv6Addr_Type()
)
hpnicfDot11ACMtTrapAPIPv6Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapAPIPv6Addr.setStatus("current")
_HpnicfDot11ACMtTrapTunlDwnCount_Type = Integer32
_HpnicfDot11ACMtTrapTunlDwnCount_Object = MibScalar
hpnicfDot11ACMtTrapTunlDwnCount = _HpnicfDot11ACMtTrapTunlDwnCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 9),
    _HpnicfDot11ACMtTrapTunlDwnCount_Type()
)
hpnicfDot11ACMtTrapTunlDwnCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapTunlDwnCount.setStatus("current")
_HpnicfDot11ACMaxStaNum_Type = Integer32
_HpnicfDot11ACMaxStaNum_Object = MibScalar
hpnicfDot11ACMaxStaNum = _HpnicfDot11ACMaxStaNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 10),
    _HpnicfDot11ACMaxStaNum_Type()
)
hpnicfDot11ACMaxStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMaxStaNum.setStatus("current")
_HpnicfDot11ACMtTrapTnlAPSysName_Type = OctetString
_HpnicfDot11ACMtTrapTnlAPSysName_Object = MibScalar
hpnicfDot11ACMtTrapTnlAPSysName = _HpnicfDot11ACMtTrapTnlAPSysName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 11),
    _HpnicfDot11ACMtTrapTnlAPSysName_Type()
)
hpnicfDot11ACMtTrapTnlAPSysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapTnlAPSysName.setStatus("current")
_HpnicfDot11ACMtFirstTrapTime_Type = TimeTicks
_HpnicfDot11ACMtFirstTrapTime_Object = MibScalar
hpnicfDot11ACMtFirstTrapTime = _HpnicfDot11ACMtFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 12),
    _HpnicfDot11ACMtFirstTrapTime_Type()
)
hpnicfDot11ACMtFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtFirstTrapTime.setStatus("current")


class _HpnicfDot11ACStatusSwitchInfo_Type(Integer32):
    """Custom type hpnicfDot11ACStatusSwitchInfo based on Integer32"""
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


_HpnicfDot11ACStatusSwitchInfo_Type.__name__ = "Integer32"
_HpnicfDot11ACStatusSwitchInfo_Object = MibScalar
hpnicfDot11ACStatusSwitchInfo = _HpnicfDot11ACStatusSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 13),
    _HpnicfDot11ACStatusSwitchInfo_Type()
)
hpnicfDot11ACStatusSwitchInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACStatusSwitchInfo.setStatus("current")
_HpnicfDot11SourceACNmsIP_Type = IpAddress
_HpnicfDot11SourceACNmsIP_Object = MibScalar
hpnicfDot11SourceACNmsIP = _HpnicfDot11SourceACNmsIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 14),
    _HpnicfDot11SourceACNmsIP_Type()
)
hpnicfDot11SourceACNmsIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11SourceACNmsIP.setStatus("current")
_HpnicfDot11ACMtTrapAPMacAddress_Type = MacAddress
_HpnicfDot11ACMtTrapAPMacAddress_Object = MibScalar
hpnicfDot11ACMtTrapAPMacAddress = _HpnicfDot11ACMtTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 1, 15),
    _HpnicfDot11ACMtTrapAPMacAddress_Type()
)
hpnicfDot11ACMtTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTrapAPMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDot11ACMtTunnelSetupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0, 1)
)
hpnicfDot11ACMtTunnelSetupTrap.setObjects(
      *(("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11CurrTunnelAPID"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapTunlUpInfo"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapTnlAPName"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapTnlAPIPAddr"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapAPIPv6Addr"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtFirstTrapTime"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTunnelSetupTrap.setStatus(
        "current"
    )

hpnicfDot11ACMtTunnelDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0, 2)
)
hpnicfDot11ACMtTunnelDownTrap.setObjects(
      *(("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11CurrTunnelAPID"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapTunlDwnInfo"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapTnlAPName"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapTnlAPIPAddr"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapAPIPv6Addr"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapTunlDwnCount"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapTnlAPSysName"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtFirstTrapTime"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11ACMtTunnelDownTrap.setStatus(
        "current"
    )

hpnicfDot11ACMtBackupSwtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0, 3)
)
hpnicfDot11ACMtBackupSwtTrap.setObjects(
      *(("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtTrapBackupSwitchInfo"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11ACMtBackupSwtTrap.setStatus(
        "current"
    )

hpnicfDot11ACLoadBalanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0, 4)
)
hpnicfDot11ACLoadBalanceTrap.setObjects(
      *(("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11LoadBalanceType"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11LoadBalanceThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfDot11ACLoadBalanceTrap.setStatus(
        "current"
    )

hpnicfDot11ACStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0, 5)
)
hpnicfDot11ACStaFullTrap.setObjects(
    ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACMaxStaNum")
)
if mibBuilder.loadTexts:
    hpnicfDot11ACStaFullTrap.setStatus(
        "current"
    )

hpnicfDot11ACStatusSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0, 6)
)
hpnicfDot11ACStatusSwitchTrap.setObjects(
      *(("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11ACStatusSwitchInfo"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11SourceACNmsIP"))
)
if mibBuilder.loadTexts:
    hpnicfDot11ACStatusSwitchTrap.setStatus(
        "current"
    )

hpnicfDot11RunAPNumOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0, 7)
)
hpnicfDot11RunAPNumOverload.setObjects(
      *(("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11MaxAPNumPermitted"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11APConnectCount"))
)
if mibBuilder.loadTexts:
    hpnicfDot11RunAPNumOverload.setStatus(
        "current"
    )

hpnicfDot11RunAPNumOverloadRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 1, 3, 0, 8)
)
hpnicfDot11RunAPNumOverloadRecover.setObjects(
      *(("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11MaxAPNumPermitted"),
        ("HPN-ICF-DOT11-ACMT-MIB", "hpnicfDot11APConnectCount"))
)
if mibBuilder.loadTexts:
    hpnicfDot11RunAPNumOverloadRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-ACMT-MIB",
    **{"hpnicfDot11ACMT": hpnicfDot11ACMT,
       "hpnicfDot11ACObjectGroup": hpnicfDot11ACObjectGroup,
       "hpnicfDot11ACObject": hpnicfDot11ACObject,
       "hpnicfDot11CurrentACMACMode": hpnicfDot11CurrentACMACMode,
       "hpnicfDot11MaxAPNumPermitted": hpnicfDot11MaxAPNumPermitted,
       "hpnicfDot11MaxStationNumPermitted": hpnicfDot11MaxStationNumPermitted,
       "hpnicfDot11RunAPNumThreshold": hpnicfDot11RunAPNumThreshold,
       "hpnicfDot11ACLoadInfo": hpnicfDot11ACLoadInfo,
       "hpnicfDot11APConnectCount": hpnicfDot11APConnectCount,
       "hpnicfDot11StationConnectCount": hpnicfDot11StationConnectCount,
       "hpnicfDot11ACIFLoadInfoTable": hpnicfDot11ACIFLoadInfoTable,
       "hpnicfDot11ACIFLoadInfoEntry": hpnicfDot11ACIFLoadInfoEntry,
       "hpnicfDot11ACIfIndex": hpnicfDot11ACIfIndex,
       "hpnicfDot11ACIfApNum": hpnicfDot11ACIfApNum,
       "hpnicfDot11ACIfStaNum": hpnicfDot11ACIfStaNum,
       "hpnicfDot11ACIfName": hpnicfDot11ACIfName,
       "hpnicfDot11MasterAPCount": hpnicfDot11MasterAPCount,
       "hpnicfDot11SlaveAPCount": hpnicfDot11SlaveAPCount,
       "hpnicfDot11ConnectAutoAPCount": hpnicfDot11ConnectAutoAPCount,
       "hpnicfDot11PersistentAPCount": hpnicfDot11PersistentAPCount,
       "hpnicfDot11AcUploadFrameCnt": hpnicfDot11AcUploadFrameCnt,
       "hpnicfDot11AcDownloadFrameCnt": hpnicfDot11AcDownloadFrameCnt,
       "hpnicfDot11AcUploadFrameBytes": hpnicfDot11AcUploadFrameBytes,
       "hpnicfDot11AcDownloadFrameBytes": hpnicfDot11AcDownloadFrameBytes,
       "hpnicfDot11BackupACRole": hpnicfDot11BackupACRole,
       "hpnicfDot11BackupACNMSIP": hpnicfDot11BackupACNMSIP,
       "hpnicfDot11ACBackupMode": hpnicfDot11ACBackupMode,
       "hpnicfDot11ACBackupStatus": hpnicfDot11ACBackupStatus,
       "hpnicfDot11ACSwitchCnt": hpnicfDot11ACSwitchCnt,
       "hpnicfDot11ACSouthifPacketOutputCount": hpnicfDot11ACSouthifPacketOutputCount,
       "hpnicfDot11ACSouthifPacketOutputBytes": hpnicfDot11ACSouthifPacketOutputBytes,
       "hpnicfDot11ACSouthifPacketInputCount": hpnicfDot11ACSouthifPacketInputCount,
       "hpnicfDot11ACSouthifPacketInputBytes": hpnicfDot11ACSouthifPacketInputBytes,
       "hpnicfDot11TotalAPconnected": hpnicfDot11TotalAPconnected,
       "hpnicfDot11RemainingAPcapacity": hpnicfDot11RemainingAPcapacity,
       "hpnicfDot11WLANAssocStatisInfo": hpnicfDot11WLANAssocStatisInfo,
       "hpnicfDot11StationAssocSum": hpnicfDot11StationAssocSum,
       "hpnicfDot11StationAssocFailSum": hpnicfDot11StationAssocFailSum,
       "hpnicfDot11StationReassocSum": hpnicfDot11StationReassocSum,
       "hpnicfDot11StationAssocRejectedSum": hpnicfDot11StationAssocRejectedSum,
       "hpnicfDot11StationExDeAuthenSum": hpnicfDot11StationExDeAuthenSum,
       "hpnicfDot11StationCurAssocSum": hpnicfDot11StationCurAssocSum,
       "hpnicfDot11StationAssocReqSum": hpnicfDot11StationAssocReqSum,
       "hpnicfDot11StationReassocReqSum": hpnicfDot11StationReassocReqSum,
       "hpnicfDot11StationReassocFailSum": hpnicfDot11StationReassocFailSum,
       "hpnicfDot11ACBASInfo": hpnicfDot11ACBASInfo,
       "hpnicfDot11ACBASSysObjects": hpnicfDot11ACBASSysObjects,
       "hpnicfDot11ACBASTableObjects": hpnicfDot11ACBASTableObjects,
       "hpnicfDot11ACBASIfTable": hpnicfDot11ACBASIfTable,
       "hpnicfDot11ACBASIfEntry": hpnicfDot11ACBASIfEntry,
       "hpnicfDot11ACBASIfIndex": hpnicfDot11ACBASIfIndex,
       "hpnicfDot11ACBASIfDescr": hpnicfDot11ACBASIfDescr,
       "hpnicfDot11ACBASIfType": hpnicfDot11ACBASIfType,
       "hpnicfDot11ACStaUserSecAuthStatis": hpnicfDot11ACStaUserSecAuthStatis,
       "hpnicfDot11ACStaUserAuthCurNumber": hpnicfDot11ACStaUserAuthCurNumber,
       "hpnicfDot11ACStaUserConnFailCnt": hpnicfDot11ACStaUserConnFailCnt,
       "hpnicfDot11ACStaUserAuthReqCnt": hpnicfDot11ACStaUserAuthReqCnt,
       "hpnicfDot11ACStaUserAuthSuccCnt": hpnicfDot11ACStaUserAuthSuccCnt,
       "hpnicfDot11ACStaUserAuthFailCnt": hpnicfDot11ACStaUserAuthFailCnt,
       "hpnicfDot11ACStaUserAllAuthCntCM": hpnicfDot11ACStaUserAllAuthCntCM,
       "hpnicfDot11ACStaSecAuthTypeStatis": hpnicfDot11ACStaSecAuthTypeStatis,
       "hpnicfDot11ACStaUserPortalOnlineNum": hpnicfDot11ACStaUserPortalOnlineNum,
       "hpnicfDot11ACStaUserFreeAuthOnlineNum": hpnicfDot11ACStaUserFreeAuthOnlineNum,
       "hpnicfDot11ACStaUserAssociateAuthOnlineNum": hpnicfDot11ACStaUserAssociateAuthOnlineNum,
       "hpnicfDot11ACStaUserMacAuthOnlineNum": hpnicfDot11ACStaUserMacAuthOnlineNum,
       "hpnicfDot11ACStaUserPortalLostConnectionCnt": hpnicfDot11ACStaUserPortalLostConnectionCnt,
       "hpnicfDot11ACStaUserFreeAuthLostConnectionCnt": hpnicfDot11ACStaUserFreeAuthLostConnectionCnt,
       "hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt": hpnicfDot11ACStaUserAssociateAuthLostConnectionCnt,
       "hpnicfDot11ACStaUserMacAuthLostConnectionCnt": hpnicfDot11ACStaUserMacAuthLostConnectionCnt,
       "hpnicfDot11ACStaPortalAuthReqCnt": hpnicfDot11ACStaPortalAuthReqCnt,
       "hpnicfDot11ACStaAssociateAuthReqCnt": hpnicfDot11ACStaAssociateAuthReqCnt,
       "hpnicfDot11ACStaMacAuthReqCnt": hpnicfDot11ACStaMacAuthReqCnt,
       "hpnicfDot11ACStaPortalAuthSuccCnt": hpnicfDot11ACStaPortalAuthSuccCnt,
       "hpnicfDot11ACStaAssociateAuthSuccCnt": hpnicfDot11ACStaAssociateAuthSuccCnt,
       "hpnicfDot11ACStaMacAuthSuccCnt": hpnicfDot11ACStaMacAuthSuccCnt,
       "hpnicfDot11ACStaPortalAuthReqFailCnt": hpnicfDot11ACStaPortalAuthReqFailCnt,
       "hpnicfDot11ACStaAssociateAuthReqFailCnt": hpnicfDot11ACStaAssociateAuthReqFailCnt,
       "hpnicfDot11ACStaMacAuthReqFailCnt": hpnicfDot11ACStaMacAuthReqFailCnt,
       "hpnicfDot11ACStaUserAutoAuthOnlineNumCM": hpnicfDot11ACStaUserAutoAuthOnlineNumCM,
       "hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM": hpnicfDot11ACStaUserAutoAuthLostConnectionCntCM,
       "hpnicfDot11ACStaAutoAuthReqCntCM": hpnicfDot11ACStaAutoAuthReqCntCM,
       "hpnicfDot11ACStaAutoAuthSuccCntCM": hpnicfDot11ACStaAutoAuthSuccCntCM,
       "hpnicfDot11ACStaAutoAuthReqFailCntCM": hpnicfDot11ACStaAutoAuthReqFailCntCM,
       "hpnicfDot11ACPortalStatisticCMTable": hpnicfDot11ACPortalStatisticCMTable,
       "hpnicfDot11ACPortalStatisticCMEntry": hpnicfDot11ACPortalStatisticCMEntry,
       "hpnicfDot11ACPortalStatisticSSIDCM": hpnicfDot11ACPortalStatisticSSIDCM,
       "hpnicfDot11ACPortalStatAuthReqCM": hpnicfDot11ACPortalStatAuthReqCM,
       "hpnicfDot11ACPortalStatAuthRespCM": hpnicfDot11ACPortalStatAuthRespCM,
       "hpnicfDot11CAPWAPTunnelGroup": hpnicfDot11CAPWAPTunnelGroup,
       "hpnicfDot11CAPWAPTunnelTable": hpnicfDot11CAPWAPTunnelTable,
       "hpnicfDot11CAPWAPTunnelEntry": hpnicfDot11CAPWAPTunnelEntry,
       "hpnicfDot11CurrTunnelAPID": hpnicfDot11CurrTunnelAPID,
       "hpnicfDot11CtrlTunnelCurrSec": hpnicfDot11CtrlTunnelCurrSec,
       "hpnicfDot11CtrlTunnelUpTime": hpnicfDot11CtrlTunnelUpTime,
       "hpnicfDot11DataTunnelCurrSec": hpnicfDot11DataTunnelCurrSec,
       "hpnicfDot11DataTunnelUpTime": hpnicfDot11DataTunnelUpTime,
       "hpnicfDot11CtrlTunnelUpTimeTicks": hpnicfDot11CtrlTunnelUpTimeTicks,
       "hpnicfDot11ACMtNotifyGroup": hpnicfDot11ACMtNotifyGroup,
       "hpnicfDot11ACMtTraps": hpnicfDot11ACMtTraps,
       "hpnicfDot11ACMtTunnelSetupTrap": hpnicfDot11ACMtTunnelSetupTrap,
       "hpnicfDot11ACMtTunnelDownTrap": hpnicfDot11ACMtTunnelDownTrap,
       "hpnicfDot11ACMtBackupSwtTrap": hpnicfDot11ACMtBackupSwtTrap,
       "hpnicfDot11ACLoadBalanceTrap": hpnicfDot11ACLoadBalanceTrap,
       "hpnicfDot11ACStaFullTrap": hpnicfDot11ACStaFullTrap,
       "hpnicfDot11ACStatusSwitchTrap": hpnicfDot11ACStatusSwitchTrap,
       "hpnicfDot11RunAPNumOverload": hpnicfDot11RunAPNumOverload,
       "hpnicfDot11RunAPNumOverloadRecover": hpnicfDot11RunAPNumOverloadRecover,
       "hpnicfDot11ACMtTrapVarObjects": hpnicfDot11ACMtTrapVarObjects,
       "hpnicfDot11ACMtTrapTunlDwnInfo": hpnicfDot11ACMtTrapTunlDwnInfo,
       "hpnicfDot11ACMtTrapTunlUpInfo": hpnicfDot11ACMtTrapTunlUpInfo,
       "hpnicfDot11ACMtTrapBackupSwitchInfo": hpnicfDot11ACMtTrapBackupSwitchInfo,
       "hpnicfDot11ACMtTrapTnlAPName": hpnicfDot11ACMtTrapTnlAPName,
       "hpnicfDot11ACMtTrapTnlAPIPAddr": hpnicfDot11ACMtTrapTnlAPIPAddr,
       "hpnicfDot11LoadBalanceType": hpnicfDot11LoadBalanceType,
       "hpnicfDot11LoadBalanceThreshold": hpnicfDot11LoadBalanceThreshold,
       "hpnicfDot11ACMtTrapAPIPv6Addr": hpnicfDot11ACMtTrapAPIPv6Addr,
       "hpnicfDot11ACMtTrapTunlDwnCount": hpnicfDot11ACMtTrapTunlDwnCount,
       "hpnicfDot11ACMaxStaNum": hpnicfDot11ACMaxStaNum,
       "hpnicfDot11ACMtTrapTnlAPSysName": hpnicfDot11ACMtTrapTnlAPSysName,
       "hpnicfDot11ACMtFirstTrapTime": hpnicfDot11ACMtFirstTrapTime,
       "hpnicfDot11ACStatusSwitchInfo": hpnicfDot11ACStatusSwitchInfo,
       "hpnicfDot11SourceACNmsIP": hpnicfDot11SourceACNmsIP,
       "hpnicfDot11ACMtTrapAPMacAddress": hpnicfDot11ACMtTrapAPMacAddress}
)
