# SNMP MIB module (HH3C-DOT11-ACMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-ACMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:48 2024
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

(Hh3cDot11MACModeType,
 Hh3cDot11ObjectIDType,
 Hh3cDot11TunnelSecSchemType,
 hh3cDot11) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11MACModeType",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11TunnelSecSchemType",
    "hh3cDot11")

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

hh3cDot11ACMT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1)
)
hh3cDot11ACMT.setRevisions(
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

_Hh3cDot11ACObjectGroup_ObjectIdentity = ObjectIdentity
hh3cDot11ACObjectGroup = _Hh3cDot11ACObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1)
)
_Hh3cDot11ACObject_ObjectIdentity = ObjectIdentity
hh3cDot11ACObject = _Hh3cDot11ACObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1)
)


class _Hh3cDot11CurrentACMACMode_Type(Hh3cDot11MACModeType):
    """Custom type hh3cDot11CurrentACMACMode based on Hh3cDot11MACModeType"""


_Hh3cDot11CurrentACMACMode_Object = MibScalar
hh3cDot11CurrentACMACMode = _Hh3cDot11CurrentACMACMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 1),
    _Hh3cDot11CurrentACMACMode_Type()
)
hh3cDot11CurrentACMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrentACMACMode.setStatus("current")
_Hh3cDot11MaxAPNumPermitted_Type = Integer32
_Hh3cDot11MaxAPNumPermitted_Object = MibScalar
hh3cDot11MaxAPNumPermitted = _Hh3cDot11MaxAPNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 2),
    _Hh3cDot11MaxAPNumPermitted_Type()
)
hh3cDot11MaxAPNumPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MaxAPNumPermitted.setStatus("current")
_Hh3cDot11MaxStationNumPermitted_Type = Integer32
_Hh3cDot11MaxStationNumPermitted_Object = MibScalar
hh3cDot11MaxStationNumPermitted = _Hh3cDot11MaxStationNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 3),
    _Hh3cDot11MaxStationNumPermitted_Type()
)
hh3cDot11MaxStationNumPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MaxStationNumPermitted.setStatus("current")
_Hh3cDot11ACLoadInfo_ObjectIdentity = ObjectIdentity
hh3cDot11ACLoadInfo = _Hh3cDot11ACLoadInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2)
)
_Hh3cDot11APConnectCount_Type = Integer32
_Hh3cDot11APConnectCount_Object = MibScalar
hh3cDot11APConnectCount = _Hh3cDot11APConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 1),
    _Hh3cDot11APConnectCount_Type()
)
hh3cDot11APConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APConnectCount.setStatus("current")
_Hh3cDot11StationConnectCount_Type = Integer32
_Hh3cDot11StationConnectCount_Object = MibScalar
hh3cDot11StationConnectCount = _Hh3cDot11StationConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 2),
    _Hh3cDot11StationConnectCount_Type()
)
hh3cDot11StationConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationConnectCount.setStatus("current")
_Hh3cDot11ACIFLoadInfoTable_Object = MibTable
hh3cDot11ACIFLoadInfoTable = _Hh3cDot11ACIFLoadInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11ACIFLoadInfoTable.setStatus("current")
_Hh3cDot11ACIFLoadInfoEntry_Object = MibTableRow
hh3cDot11ACIFLoadInfoEntry = _Hh3cDot11ACIFLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1)
)
hh3cDot11ACIFLoadInfoEntry.setIndexNames(
    (0, "HH3C-DOT11-ACMT-MIB", "hh3cDot11ACIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11ACIFLoadInfoEntry.setStatus("current")
_Hh3cDot11ACIfIndex_Type = Integer32
_Hh3cDot11ACIfIndex_Object = MibTableColumn
hh3cDot11ACIfIndex = _Hh3cDot11ACIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1, 1),
    _Hh3cDot11ACIfIndex_Type()
)
hh3cDot11ACIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACIfIndex.setStatus("current")
_Hh3cDot11ACIfApNum_Type = Integer32
_Hh3cDot11ACIfApNum_Object = MibTableColumn
hh3cDot11ACIfApNum = _Hh3cDot11ACIfApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1, 2),
    _Hh3cDot11ACIfApNum_Type()
)
hh3cDot11ACIfApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACIfApNum.setStatus("current")
_Hh3cDot11ACIfStaNum_Type = Integer32
_Hh3cDot11ACIfStaNum_Object = MibTableColumn
hh3cDot11ACIfStaNum = _Hh3cDot11ACIfStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1, 3),
    _Hh3cDot11ACIfStaNum_Type()
)
hh3cDot11ACIfStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACIfStaNum.setStatus("current")
_Hh3cDot11ACIfName_Type = OctetString
_Hh3cDot11ACIfName_Object = MibTableColumn
hh3cDot11ACIfName = _Hh3cDot11ACIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1, 4),
    _Hh3cDot11ACIfName_Type()
)
hh3cDot11ACIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACIfName.setStatus("current")
_Hh3cDot11MasterAPCount_Type = Integer32
_Hh3cDot11MasterAPCount_Object = MibScalar
hh3cDot11MasterAPCount = _Hh3cDot11MasterAPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 4),
    _Hh3cDot11MasterAPCount_Type()
)
hh3cDot11MasterAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MasterAPCount.setStatus("current")
_Hh3cDot11SlaveAPCount_Type = Integer32
_Hh3cDot11SlaveAPCount_Object = MibScalar
hh3cDot11SlaveAPCount = _Hh3cDot11SlaveAPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 5),
    _Hh3cDot11SlaveAPCount_Type()
)
hh3cDot11SlaveAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SlaveAPCount.setStatus("current")
_Hh3cDot11ConnectAutoAPCount_Type = Integer32
_Hh3cDot11ConnectAutoAPCount_Object = MibScalar
hh3cDot11ConnectAutoAPCount = _Hh3cDot11ConnectAutoAPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 6),
    _Hh3cDot11ConnectAutoAPCount_Type()
)
hh3cDot11ConnectAutoAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ConnectAutoAPCount.setStatus("current")
_Hh3cDot11PersistentAPCount_Type = Integer32
_Hh3cDot11PersistentAPCount_Object = MibScalar
hh3cDot11PersistentAPCount = _Hh3cDot11PersistentAPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 7),
    _Hh3cDot11PersistentAPCount_Type()
)
hh3cDot11PersistentAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PersistentAPCount.setStatus("current")
_Hh3cDot11AcUploadFrameCnt_Type = Counter64
_Hh3cDot11AcUploadFrameCnt_Object = MibScalar
hh3cDot11AcUploadFrameCnt = _Hh3cDot11AcUploadFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 8),
    _Hh3cDot11AcUploadFrameCnt_Type()
)
hh3cDot11AcUploadFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcUploadFrameCnt.setStatus("current")
_Hh3cDot11AcDownloadFrameCnt_Type = Counter64
_Hh3cDot11AcDownloadFrameCnt_Object = MibScalar
hh3cDot11AcDownloadFrameCnt = _Hh3cDot11AcDownloadFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 9),
    _Hh3cDot11AcDownloadFrameCnt_Type()
)
hh3cDot11AcDownloadFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcDownloadFrameCnt.setStatus("current")
_Hh3cDot11AcUploadFrameBytes_Type = Counter64
_Hh3cDot11AcUploadFrameBytes_Object = MibScalar
hh3cDot11AcUploadFrameBytes = _Hh3cDot11AcUploadFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 10),
    _Hh3cDot11AcUploadFrameBytes_Type()
)
hh3cDot11AcUploadFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcUploadFrameBytes.setStatus("current")
_Hh3cDot11AcDownloadFrameBytes_Type = Counter64
_Hh3cDot11AcDownloadFrameBytes_Object = MibScalar
hh3cDot11AcDownloadFrameBytes = _Hh3cDot11AcDownloadFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 11),
    _Hh3cDot11AcDownloadFrameBytes_Type()
)
hh3cDot11AcDownloadFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcDownloadFrameBytes.setStatus("current")
_Hh3cDot11WLANAssocStatisInfo_ObjectIdentity = ObjectIdentity
hh3cDot11WLANAssocStatisInfo = _Hh3cDot11WLANAssocStatisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3)
)
_Hh3cDot11StationAssocSum_Type = Counter32
_Hh3cDot11StationAssocSum_Object = MibScalar
hh3cDot11StationAssocSum = _Hh3cDot11StationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 1),
    _Hh3cDot11StationAssocSum_Type()
)
hh3cDot11StationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocSum.setStatus("current")
_Hh3cDot11StationAssocFailSum_Type = Counter32
_Hh3cDot11StationAssocFailSum_Object = MibScalar
hh3cDot11StationAssocFailSum = _Hh3cDot11StationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 2),
    _Hh3cDot11StationAssocFailSum_Type()
)
hh3cDot11StationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocFailSum.setStatus("current")
_Hh3cDot11StationReassocSum_Type = Counter32
_Hh3cDot11StationReassocSum_Object = MibScalar
hh3cDot11StationReassocSum = _Hh3cDot11StationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 3),
    _Hh3cDot11StationReassocSum_Type()
)
hh3cDot11StationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationReassocSum.setStatus("current")
_Hh3cDot11StationAssocRejectedSum_Type = Counter32
_Hh3cDot11StationAssocRejectedSum_Object = MibScalar
hh3cDot11StationAssocRejectedSum = _Hh3cDot11StationAssocRejectedSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 4),
    _Hh3cDot11StationAssocRejectedSum_Type()
)
hh3cDot11StationAssocRejectedSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocRejectedSum.setStatus("current")
_Hh3cDot11StationExDeAuthenSum_Type = Counter32
_Hh3cDot11StationExDeAuthenSum_Object = MibScalar
hh3cDot11StationExDeAuthenSum = _Hh3cDot11StationExDeAuthenSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 5),
    _Hh3cDot11StationExDeAuthenSum_Type()
)
hh3cDot11StationExDeAuthenSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationExDeAuthenSum.setStatus("current")
_Hh3cDot11StationCurAssocSum_Type = Integer32
_Hh3cDot11StationCurAssocSum_Object = MibScalar
hh3cDot11StationCurAssocSum = _Hh3cDot11StationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 6),
    _Hh3cDot11StationCurAssocSum_Type()
)
hh3cDot11StationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationCurAssocSum.setStatus("current")
_Hh3cDot11ACBASInfo_ObjectIdentity = ObjectIdentity
hh3cDot11ACBASInfo = _Hh3cDot11ACBASInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4)
)
_Hh3cDot11ACBASSysObjects_ObjectIdentity = ObjectIdentity
hh3cDot11ACBASSysObjects = _Hh3cDot11ACBASSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 1)
)
_Hh3cDot11ACBASTableObjects_ObjectIdentity = ObjectIdentity
hh3cDot11ACBASTableObjects = _Hh3cDot11ACBASTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2)
)
_Hh3cDot11ACBASIfTable_Object = MibTable
hh3cDot11ACBASIfTable = _Hh3cDot11ACBASIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfTable.setStatus("current")
_Hh3cDot11ACBASIfEntry_Object = MibTableRow
hh3cDot11ACBASIfEntry = _Hh3cDot11ACBASIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3, 1)
)
hh3cDot11ACBASIfEntry.setIndexNames(
    (0, "HH3C-DOT11-ACMT-MIB", "hh3cDot11ACBASIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfEntry.setStatus("current")
_Hh3cDot11ACBASIfIndex_Type = Integer32
_Hh3cDot11ACBASIfIndex_Object = MibTableColumn
hh3cDot11ACBASIfIndex = _Hh3cDot11ACBASIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3, 1, 1),
    _Hh3cDot11ACBASIfIndex_Type()
)
hh3cDot11ACBASIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfIndex.setStatus("current")


class _Hh3cDot11ACBASIfDescr_Type(OctetString):
    """Custom type hh3cDot11ACBASIfDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11ACBASIfDescr_Type.__name__ = "OctetString"
_Hh3cDot11ACBASIfDescr_Object = MibTableColumn
hh3cDot11ACBASIfDescr = _Hh3cDot11ACBASIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3, 1, 2),
    _Hh3cDot11ACBASIfDescr_Type()
)
hh3cDot11ACBASIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfDescr.setStatus("current")
_Hh3cDot11ACBASIfType_Type = IANAifType
_Hh3cDot11ACBASIfType_Object = MibTableColumn
hh3cDot11ACBASIfType = _Hh3cDot11ACBASIfType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3, 1, 3),
    _Hh3cDot11ACBASIfType_Type()
)
hh3cDot11ACBASIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfType.setStatus("current")
_Hh3cDot11ACStaUserSecAuthStatis_ObjectIdentity = ObjectIdentity
hh3cDot11ACStaUserSecAuthStatis = _Hh3cDot11ACStaUserSecAuthStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5)
)
_Hh3cDot11ACStaUserAuthCurNumber_Type = Integer32
_Hh3cDot11ACStaUserAuthCurNumber_Object = MibScalar
hh3cDot11ACStaUserAuthCurNumber = _Hh3cDot11ACStaUserAuthCurNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 1),
    _Hh3cDot11ACStaUserAuthCurNumber_Type()
)
hh3cDot11ACStaUserAuthCurNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthCurNumber.setStatus("current")
_Hh3cDot11ACStaUserConnFailCnt_Type = Counter32
_Hh3cDot11ACStaUserConnFailCnt_Object = MibScalar
hh3cDot11ACStaUserConnFailCnt = _Hh3cDot11ACStaUserConnFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 2),
    _Hh3cDot11ACStaUserConnFailCnt_Type()
)
hh3cDot11ACStaUserConnFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserConnFailCnt.setStatus("current")
_Hh3cDot11ACStaUserAuthReqCnt_Type = Counter32
_Hh3cDot11ACStaUserAuthReqCnt_Object = MibScalar
hh3cDot11ACStaUserAuthReqCnt = _Hh3cDot11ACStaUserAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 3),
    _Hh3cDot11ACStaUserAuthReqCnt_Type()
)
hh3cDot11ACStaUserAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthReqCnt.setStatus("current")
_Hh3cDot11ACStaUserAuthSuccCnt_Type = Counter32
_Hh3cDot11ACStaUserAuthSuccCnt_Object = MibScalar
hh3cDot11ACStaUserAuthSuccCnt = _Hh3cDot11ACStaUserAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 4),
    _Hh3cDot11ACStaUserAuthSuccCnt_Type()
)
hh3cDot11ACStaUserAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthSuccCnt.setStatus("current")
_Hh3cDot11ACStaUserAuthFailCnt_Type = Counter32
_Hh3cDot11ACStaUserAuthFailCnt_Object = MibScalar
hh3cDot11ACStaUserAuthFailCnt = _Hh3cDot11ACStaUserAuthFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 5),
    _Hh3cDot11ACStaUserAuthFailCnt_Type()
)
hh3cDot11ACStaUserAuthFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthFailCnt.setStatus("current")
_Hh3cDot11CAPWAPTunnelGroup_ObjectIdentity = ObjectIdentity
hh3cDot11CAPWAPTunnelGroup = _Hh3cDot11CAPWAPTunnelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2)
)
_Hh3cDot11CAPWAPTunnelTable_Object = MibTable
hh3cDot11CAPWAPTunnelTable = _Hh3cDot11CAPWAPTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11CAPWAPTunnelTable.setStatus("current")
_Hh3cDot11CAPWAPTunnelEntry_Object = MibTableRow
hh3cDot11CAPWAPTunnelEntry = _Hh3cDot11CAPWAPTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1)
)
hh3cDot11CAPWAPTunnelEntry.setIndexNames(
    (0, "HH3C-DOT11-ACMT-MIB", "hh3cDot11CurrTunnelAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11CAPWAPTunnelEntry.setStatus("current")
_Hh3cDot11CurrTunnelAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11CurrTunnelAPID_Object = MibTableColumn
hh3cDot11CurrTunnelAPID = _Hh3cDot11CurrTunnelAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 1),
    _Hh3cDot11CurrTunnelAPID_Type()
)
hh3cDot11CurrTunnelAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11CurrTunnelAPID.setStatus("current")


class _Hh3cDot11CtrlTunnelCurrSec_Type(Hh3cDot11TunnelSecSchemType):
    """Custom type hh3cDot11CtrlTunnelCurrSec based on Hh3cDot11TunnelSecSchemType"""


_Hh3cDot11CtrlTunnelCurrSec_Object = MibTableColumn
hh3cDot11CtrlTunnelCurrSec = _Hh3cDot11CtrlTunnelCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 2),
    _Hh3cDot11CtrlTunnelCurrSec_Type()
)
hh3cDot11CtrlTunnelCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CtrlTunnelCurrSec.setStatus("current")
_Hh3cDot11CtrlTunnelUpTime_Type = Integer32
_Hh3cDot11CtrlTunnelUpTime_Object = MibTableColumn
hh3cDot11CtrlTunnelUpTime = _Hh3cDot11CtrlTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 3),
    _Hh3cDot11CtrlTunnelUpTime_Type()
)
hh3cDot11CtrlTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CtrlTunnelUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CtrlTunnelUpTime.setUnits("second")


class _Hh3cDot11DataTunnelCurrSec_Type(Hh3cDot11TunnelSecSchemType):
    """Custom type hh3cDot11DataTunnelCurrSec based on Hh3cDot11TunnelSecSchemType"""


_Hh3cDot11DataTunnelCurrSec_Object = MibTableColumn
hh3cDot11DataTunnelCurrSec = _Hh3cDot11DataTunnelCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 4),
    _Hh3cDot11DataTunnelCurrSec_Type()
)
hh3cDot11DataTunnelCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DataTunnelCurrSec.setStatus("current")
_Hh3cDot11DataTunnelUpTime_Type = Integer32
_Hh3cDot11DataTunnelUpTime_Object = MibTableColumn
hh3cDot11DataTunnelUpTime = _Hh3cDot11DataTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 5),
    _Hh3cDot11DataTunnelUpTime_Type()
)
hh3cDot11DataTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DataTunnelUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11DataTunnelUpTime.setUnits("second")
_Hh3cDot11CtrlTunnelUpTimeTicks_Type = TimeTicks
_Hh3cDot11CtrlTunnelUpTimeTicks_Object = MibTableColumn
hh3cDot11CtrlTunnelUpTimeTicks = _Hh3cDot11CtrlTunnelUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 6),
    _Hh3cDot11CtrlTunnelUpTimeTicks_Type()
)
hh3cDot11CtrlTunnelUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CtrlTunnelUpTimeTicks.setStatus("current")
_Hh3cDot11ACMtNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11ACMtNotifyGroup = _Hh3cDot11ACMtNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3)
)
_Hh3cDot11ACMtTraps_ObjectIdentity = ObjectIdentity
hh3cDot11ACMtTraps = _Hh3cDot11ACMtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0)
)
_Hh3cDot11ACMtTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cDot11ACMtTrapVarObjects = _Hh3cDot11ACMtTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1)
)


class _Hh3cDot11ACMtTrapTunlDwnInfo_Type(Integer32):
    """Custom type hh3cDot11ACMtTrapTunlDwnInfo based on Integer32"""
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


_Hh3cDot11ACMtTrapTunlDwnInfo_Type.__name__ = "Integer32"
_Hh3cDot11ACMtTrapTunlDwnInfo_Object = MibScalar
hh3cDot11ACMtTrapTunlDwnInfo = _Hh3cDot11ACMtTrapTunlDwnInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 1),
    _Hh3cDot11ACMtTrapTunlDwnInfo_Type()
)
hh3cDot11ACMtTrapTunlDwnInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTunlDwnInfo.setStatus("current")


class _Hh3cDot11ACMtTrapTunlUpInfo_Type(Integer32):
    """Custom type hh3cDot11ACMtTrapTunlUpInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("up", 1)
    )


_Hh3cDot11ACMtTrapTunlUpInfo_Type.__name__ = "Integer32"
_Hh3cDot11ACMtTrapTunlUpInfo_Object = MibScalar
hh3cDot11ACMtTrapTunlUpInfo = _Hh3cDot11ACMtTrapTunlUpInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 2),
    _Hh3cDot11ACMtTrapTunlUpInfo_Type()
)
hh3cDot11ACMtTrapTunlUpInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTunlUpInfo.setStatus("current")


class _Hh3cDot11ACMtTrapBackupSwitchInfo_Type(Integer32):
    """Custom type hh3cDot11ACMtTrapBackupSwitchInfo based on Integer32"""
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


_Hh3cDot11ACMtTrapBackupSwitchInfo_Type.__name__ = "Integer32"
_Hh3cDot11ACMtTrapBackupSwitchInfo_Object = MibScalar
hh3cDot11ACMtTrapBackupSwitchInfo = _Hh3cDot11ACMtTrapBackupSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 3),
    _Hh3cDot11ACMtTrapBackupSwitchInfo_Type()
)
hh3cDot11ACMtTrapBackupSwitchInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapBackupSwitchInfo.setStatus("current")
_Hh3cDot11ACMtTrapTnlAPName_Type = OctetString
_Hh3cDot11ACMtTrapTnlAPName_Object = MibScalar
hh3cDot11ACMtTrapTnlAPName = _Hh3cDot11ACMtTrapTnlAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 4),
    _Hh3cDot11ACMtTrapTnlAPName_Type()
)
hh3cDot11ACMtTrapTnlAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTnlAPName.setStatus("current")
_Hh3cDot11ACMtTrapTnlAPIPAddr_Type = IpAddress
_Hh3cDot11ACMtTrapTnlAPIPAddr_Object = MibScalar
hh3cDot11ACMtTrapTnlAPIPAddr = _Hh3cDot11ACMtTrapTnlAPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 5),
    _Hh3cDot11ACMtTrapTnlAPIPAddr_Type()
)
hh3cDot11ACMtTrapTnlAPIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTnlAPIPAddr.setStatus("current")


class _Hh3cDot11LoadBalanceType_Type(Integer32):
    """Custom type hh3cDot11LoadBalanceType based on Integer32"""
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


_Hh3cDot11LoadBalanceType_Type.__name__ = "Integer32"
_Hh3cDot11LoadBalanceType_Object = MibScalar
hh3cDot11LoadBalanceType = _Hh3cDot11LoadBalanceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 6),
    _Hh3cDot11LoadBalanceType_Type()
)
hh3cDot11LoadBalanceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceType.setStatus("current")
_Hh3cDot11LoadBalanceThreshold_Type = Integer32
_Hh3cDot11LoadBalanceThreshold_Object = MibScalar
hh3cDot11LoadBalanceThreshold = _Hh3cDot11LoadBalanceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 7),
    _Hh3cDot11LoadBalanceThreshold_Type()
)
hh3cDot11LoadBalanceThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceThreshold.setStatus("current")
_Hh3cDot11ACMtTrapAPIPv6Addr_Type = OctetString
_Hh3cDot11ACMtTrapAPIPv6Addr_Object = MibScalar
hh3cDot11ACMtTrapAPIPv6Addr = _Hh3cDot11ACMtTrapAPIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 8),
    _Hh3cDot11ACMtTrapAPIPv6Addr_Type()
)
hh3cDot11ACMtTrapAPIPv6Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapAPIPv6Addr.setStatus("current")
_Hh3cDot11ACMtTrapTunlDwnCount_Type = Integer32
_Hh3cDot11ACMtTrapTunlDwnCount_Object = MibScalar
hh3cDot11ACMtTrapTunlDwnCount = _Hh3cDot11ACMtTrapTunlDwnCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 9),
    _Hh3cDot11ACMtTrapTunlDwnCount_Type()
)
hh3cDot11ACMtTrapTunlDwnCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTunlDwnCount.setStatus("current")
_Hh3cDot11ACMaxStaNum_Type = Integer32
_Hh3cDot11ACMaxStaNum_Object = MibScalar
hh3cDot11ACMaxStaNum = _Hh3cDot11ACMaxStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 10),
    _Hh3cDot11ACMaxStaNum_Type()
)
hh3cDot11ACMaxStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMaxStaNum.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11ACMtTunnelSetupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 1)
)
hh3cDot11ACMtTunnelSetupTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11CurrTunnelAPID"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTunlUpInfo"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPName"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPIPAddr"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapAPIPv6Addr"))
)
if mibBuilder.loadTexts:
    hh3cDot11ACMtTunnelSetupTrap.setStatus(
        "current"
    )

hh3cDot11ACMtTunnelDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 2)
)
hh3cDot11ACMtTunnelDownTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11CurrTunnelAPID"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTunlDwnInfo"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPName"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPIPAddr"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapAPIPv6Addr"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTunlDwnCount"))
)
if mibBuilder.loadTexts:
    hh3cDot11ACMtTunnelDownTrap.setStatus(
        "current"
    )

hh3cDot11ACMtBackupSwtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 3)
)
hh3cDot11ACMtBackupSwtTrap.setObjects(
    ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapBackupSwitchInfo")
)
if mibBuilder.loadTexts:
    hh3cDot11ACMtBackupSwtTrap.setStatus(
        "current"
    )

hh3cDot11ACLoadBalanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 4)
)
hh3cDot11ACLoadBalanceTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11LoadBalanceType"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11LoadBalanceThreshold"))
)
if mibBuilder.loadTexts:
    hh3cDot11ACLoadBalanceTrap.setStatus(
        "current"
    )

hh3cDot11ACStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 5)
)
hh3cDot11ACStaFullTrap.setObjects(
    ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMaxStaNum")
)
if mibBuilder.loadTexts:
    hh3cDot11ACStaFullTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-ACMT-MIB",
    **{"hh3cDot11ACMT": hh3cDot11ACMT,
       "hh3cDot11ACObjectGroup": hh3cDot11ACObjectGroup,
       "hh3cDot11ACObject": hh3cDot11ACObject,
       "hh3cDot11CurrentACMACMode": hh3cDot11CurrentACMACMode,
       "hh3cDot11MaxAPNumPermitted": hh3cDot11MaxAPNumPermitted,
       "hh3cDot11MaxStationNumPermitted": hh3cDot11MaxStationNumPermitted,
       "hh3cDot11ACLoadInfo": hh3cDot11ACLoadInfo,
       "hh3cDot11APConnectCount": hh3cDot11APConnectCount,
       "hh3cDot11StationConnectCount": hh3cDot11StationConnectCount,
       "hh3cDot11ACIFLoadInfoTable": hh3cDot11ACIFLoadInfoTable,
       "hh3cDot11ACIFLoadInfoEntry": hh3cDot11ACIFLoadInfoEntry,
       "hh3cDot11ACIfIndex": hh3cDot11ACIfIndex,
       "hh3cDot11ACIfApNum": hh3cDot11ACIfApNum,
       "hh3cDot11ACIfStaNum": hh3cDot11ACIfStaNum,
       "hh3cDot11ACIfName": hh3cDot11ACIfName,
       "hh3cDot11MasterAPCount": hh3cDot11MasterAPCount,
       "hh3cDot11SlaveAPCount": hh3cDot11SlaveAPCount,
       "hh3cDot11ConnectAutoAPCount": hh3cDot11ConnectAutoAPCount,
       "hh3cDot11PersistentAPCount": hh3cDot11PersistentAPCount,
       "hh3cDot11AcUploadFrameCnt": hh3cDot11AcUploadFrameCnt,
       "hh3cDot11AcDownloadFrameCnt": hh3cDot11AcDownloadFrameCnt,
       "hh3cDot11AcUploadFrameBytes": hh3cDot11AcUploadFrameBytes,
       "hh3cDot11AcDownloadFrameBytes": hh3cDot11AcDownloadFrameBytes,
       "hh3cDot11WLANAssocStatisInfo": hh3cDot11WLANAssocStatisInfo,
       "hh3cDot11StationAssocSum": hh3cDot11StationAssocSum,
       "hh3cDot11StationAssocFailSum": hh3cDot11StationAssocFailSum,
       "hh3cDot11StationReassocSum": hh3cDot11StationReassocSum,
       "hh3cDot11StationAssocRejectedSum": hh3cDot11StationAssocRejectedSum,
       "hh3cDot11StationExDeAuthenSum": hh3cDot11StationExDeAuthenSum,
       "hh3cDot11StationCurAssocSum": hh3cDot11StationCurAssocSum,
       "hh3cDot11ACBASInfo": hh3cDot11ACBASInfo,
       "hh3cDot11ACBASSysObjects": hh3cDot11ACBASSysObjects,
       "hh3cDot11ACBASTableObjects": hh3cDot11ACBASTableObjects,
       "hh3cDot11ACBASIfTable": hh3cDot11ACBASIfTable,
       "hh3cDot11ACBASIfEntry": hh3cDot11ACBASIfEntry,
       "hh3cDot11ACBASIfIndex": hh3cDot11ACBASIfIndex,
       "hh3cDot11ACBASIfDescr": hh3cDot11ACBASIfDescr,
       "hh3cDot11ACBASIfType": hh3cDot11ACBASIfType,
       "hh3cDot11ACStaUserSecAuthStatis": hh3cDot11ACStaUserSecAuthStatis,
       "hh3cDot11ACStaUserAuthCurNumber": hh3cDot11ACStaUserAuthCurNumber,
       "hh3cDot11ACStaUserConnFailCnt": hh3cDot11ACStaUserConnFailCnt,
       "hh3cDot11ACStaUserAuthReqCnt": hh3cDot11ACStaUserAuthReqCnt,
       "hh3cDot11ACStaUserAuthSuccCnt": hh3cDot11ACStaUserAuthSuccCnt,
       "hh3cDot11ACStaUserAuthFailCnt": hh3cDot11ACStaUserAuthFailCnt,
       "hh3cDot11CAPWAPTunnelGroup": hh3cDot11CAPWAPTunnelGroup,
       "hh3cDot11CAPWAPTunnelTable": hh3cDot11CAPWAPTunnelTable,
       "hh3cDot11CAPWAPTunnelEntry": hh3cDot11CAPWAPTunnelEntry,
       "hh3cDot11CurrTunnelAPID": hh3cDot11CurrTunnelAPID,
       "hh3cDot11CtrlTunnelCurrSec": hh3cDot11CtrlTunnelCurrSec,
       "hh3cDot11CtrlTunnelUpTime": hh3cDot11CtrlTunnelUpTime,
       "hh3cDot11DataTunnelCurrSec": hh3cDot11DataTunnelCurrSec,
       "hh3cDot11DataTunnelUpTime": hh3cDot11DataTunnelUpTime,
       "hh3cDot11CtrlTunnelUpTimeTicks": hh3cDot11CtrlTunnelUpTimeTicks,
       "hh3cDot11ACMtNotifyGroup": hh3cDot11ACMtNotifyGroup,
       "hh3cDot11ACMtTraps": hh3cDot11ACMtTraps,
       "hh3cDot11ACMtTunnelSetupTrap": hh3cDot11ACMtTunnelSetupTrap,
       "hh3cDot11ACMtTunnelDownTrap": hh3cDot11ACMtTunnelDownTrap,
       "hh3cDot11ACMtBackupSwtTrap": hh3cDot11ACMtBackupSwtTrap,
       "hh3cDot11ACLoadBalanceTrap": hh3cDot11ACLoadBalanceTrap,
       "hh3cDot11ACStaFullTrap": hh3cDot11ACStaFullTrap,
       "hh3cDot11ACMtTrapVarObjects": hh3cDot11ACMtTrapVarObjects,
       "hh3cDot11ACMtTrapTunlDwnInfo": hh3cDot11ACMtTrapTunlDwnInfo,
       "hh3cDot11ACMtTrapTunlUpInfo": hh3cDot11ACMtTrapTunlUpInfo,
       "hh3cDot11ACMtTrapBackupSwitchInfo": hh3cDot11ACMtTrapBackupSwitchInfo,
       "hh3cDot11ACMtTrapTnlAPName": hh3cDot11ACMtTrapTnlAPName,
       "hh3cDot11ACMtTrapTnlAPIPAddr": hh3cDot11ACMtTrapTnlAPIPAddr,
       "hh3cDot11LoadBalanceType": hh3cDot11LoadBalanceType,
       "hh3cDot11LoadBalanceThreshold": hh3cDot11LoadBalanceThreshold,
       "hh3cDot11ACMtTrapAPIPv6Addr": hh3cDot11ACMtTrapAPIPv6Addr,
       "hh3cDot11ACMtTrapTunlDwnCount": hh3cDot11ACMtTrapTunlDwnCount,
       "hh3cDot11ACMaxStaNum": hh3cDot11ACMaxStaNum}
)
