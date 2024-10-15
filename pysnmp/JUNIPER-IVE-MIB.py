# SNMP MIB module (JUNIPER-IVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:12 2024
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

juniper_ive = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12532)
)
juniper_ive.setRevisions(
        ("2010-02-22 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LogFullPercent_Type = Gauge32
_LogFullPercent_Object = MibScalar
logFullPercent = _LogFullPercent_Object(
    (1, 3, 6, 1, 4, 1, 12532, 1),
    _LogFullPercent_Type()
)
logFullPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFullPercent.setStatus("current")
_SignedInWebUsers_Type = Gauge32
_SignedInWebUsers_Object = MibScalar
signedInWebUsers = _SignedInWebUsers_Object(
    (1, 3, 6, 1, 4, 1, 12532, 2),
    _SignedInWebUsers_Type()
)
signedInWebUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signedInWebUsers.setStatus("current")
_SignedInMailUsers_Type = Gauge32
_SignedInMailUsers_Object = MibScalar
signedInMailUsers = _SignedInMailUsers_Object(
    (1, 3, 6, 1, 4, 1, 12532, 3),
    _SignedInMailUsers_Type()
)
signedInMailUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signedInMailUsers.setStatus("current")
_BlockedIP_Type = IpAddress
_BlockedIP_Object = MibScalar
blockedIP = _BlockedIP_Object(
    (1, 3, 6, 1, 4, 1, 12532, 4),
    _BlockedIP_Type()
)
blockedIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    blockedIP.setStatus("current")
_AuthServerName_Type = OctetString
_AuthServerName_Object = MibScalar
authServerName = _AuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 5),
    _AuthServerName_Type()
)
authServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authServerName.setStatus("current")
_ProductName_Type = OctetString
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 6),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_ProductVersion_Type = OctetString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 12532, 7),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_FileName_Type = OctetString
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 8),
    _FileName_Type()
)
fileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fileName.setStatus("current")
_MeetingUserCount_Type = Gauge32
_MeetingUserCount_Object = MibScalar
meetingUserCount = _MeetingUserCount_Object(
    (1, 3, 6, 1, 4, 1, 12532, 9),
    _MeetingUserCount_Type()
)
meetingUserCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    meetingUserCount.setStatus("current")
_IveCpuUtil_Type = Gauge32
_IveCpuUtil_Object = MibScalar
iveCpuUtil = _IveCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 12532, 10),
    _IveCpuUtil_Type()
)
iveCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveCpuUtil.setStatus("current")
_IveMemoryUtil_Type = Gauge32
_IveMemoryUtil_Object = MibScalar
iveMemoryUtil = _IveMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 12532, 11),
    _IveMemoryUtil_Type()
)
iveMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveMemoryUtil.setStatus("current")
_IveConcurrentUsers_Type = Gauge32
_IveConcurrentUsers_Object = MibScalar
iveConcurrentUsers = _IveConcurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 12532, 12),
    _IveConcurrentUsers_Type()
)
iveConcurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveConcurrentUsers.setStatus("current")
_ClusterConcurrentUsers_Type = Gauge32
_ClusterConcurrentUsers_Object = MibScalar
clusterConcurrentUsers = _ClusterConcurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 12532, 13),
    _ClusterConcurrentUsers_Type()
)
clusterConcurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterConcurrentUsers.setStatus("current")
_IveTotalHits_Type = Counter64
_IveTotalHits_Object = MibScalar
iveTotalHits = _IveTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 14),
    _IveTotalHits_Type()
)
iveTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveTotalHits.setStatus("current")
_IveFileHits_Type = Counter64
_IveFileHits_Object = MibScalar
iveFileHits = _IveFileHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 15),
    _IveFileHits_Type()
)
iveFileHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveFileHits.setStatus("current")
_IveWebHits_Type = Counter64
_IveWebHits_Object = MibScalar
iveWebHits = _IveWebHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 16),
    _IveWebHits_Type()
)
iveWebHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveWebHits.setStatus("current")
_IveAppletHits_Type = Counter64
_IveAppletHits_Object = MibScalar
iveAppletHits = _IveAppletHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 17),
    _IveAppletHits_Type()
)
iveAppletHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveAppletHits.setStatus("current")
_IvetermHits_Type = Counter64
_IvetermHits_Object = MibScalar
ivetermHits = _IvetermHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 18),
    _IvetermHits_Type()
)
ivetermHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivetermHits.setStatus("current")
_IveSAMHits_Type = Counter64
_IveSAMHits_Object = MibScalar
iveSAMHits = _IveSAMHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 19),
    _IveSAMHits_Type()
)
iveSAMHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveSAMHits.setStatus("current")
_IveNCHits_Type = Counter64
_IveNCHits_Object = MibScalar
iveNCHits = _IveNCHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 20),
    _IveNCHits_Type()
)
iveNCHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveNCHits.setStatus("current")
_MeetingHits_Type = Counter64
_MeetingHits_Object = MibScalar
meetingHits = _MeetingHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 21),
    _MeetingHits_Type()
)
meetingHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meetingHits.setStatus("current")
_MeetingCount_Type = Gauge32
_MeetingCount_Object = MibScalar
meetingCount = _MeetingCount_Object(
    (1, 3, 6, 1, 4, 1, 12532, 22),
    _MeetingCount_Type()
)
meetingCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    meetingCount.setStatus("current")
_LogName_Type = OctetString
_LogName_Object = MibScalar
logName = _LogName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 23),
    _LogName_Type()
)
logName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    logName.setStatus("current")
_IveSwapUtil_Type = Gauge32
_IveSwapUtil_Object = MibScalar
iveSwapUtil = _IveSwapUtil_Object(
    (1, 3, 6, 1, 4, 1, 12532, 24),
    _IveSwapUtil_Type()
)
iveSwapUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveSwapUtil.setStatus("current")
_DiskFullPercent_Type = Gauge32
_DiskFullPercent_Object = MibScalar
diskFullPercent = _DiskFullPercent_Object(
    (1, 3, 6, 1, 4, 1, 12532, 25),
    _DiskFullPercent_Type()
)
diskFullPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFullPercent.setStatus("current")
_BlockedIPList_Object = MibTable
blockedIPList = _BlockedIPList_Object(
    (1, 3, 6, 1, 4, 1, 12532, 26)
)
if mibBuilder.loadTexts:
    blockedIPList.setStatus("current")
_IpEntry_Object = MibTableRow
ipEntry = _IpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12532, 26, 1)
)
ipEntry.setIndexNames(
    (0, "JUNIPER-IVE-MIB", "ipIndex"),
)
if mibBuilder.loadTexts:
    ipEntry.setStatus("current")
_IpIndex_Type = Integer32
_IpIndex_Object = MibTableColumn
ipIndex = _IpIndex_Object(
    (1, 3, 6, 1, 4, 1, 12532, 26, 1, 1),
    _IpIndex_Type()
)
ipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIndex.setStatus("current")
_IpValue_Type = IpAddress
_IpValue_Object = MibTableColumn
ipValue = _IpValue_Object(
    (1, 3, 6, 1, 4, 1, 12532, 26, 1, 2),
    _IpValue_Type()
)
ipValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipValue.setStatus("current")
_LogID_Type = OctetString
_LogID_Object = MibScalar
logID = _LogID_Object(
    (1, 3, 6, 1, 4, 1, 12532, 27),
    _LogID_Type()
)
logID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    logID.setStatus("current")
_LogType_Type = OctetString
_LogType_Object = MibScalar
logType = _LogType_Object(
    (1, 3, 6, 1, 4, 1, 12532, 28),
    _LogType_Type()
)
logType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    logType.setStatus("current")
_LogDescription_Type = OctetString
_LogDescription_Object = MibScalar
logDescription = _LogDescription_Object(
    (1, 3, 6, 1, 4, 1, 12532, 29),
    _LogDescription_Type()
)
logDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    logDescription.setStatus("current")
_IvsName_Type = OctetString
_IvsName_Object = MibScalar
ivsName = _IvsName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 30),
    _IvsName_Type()
)
ivsName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ivsName.setStatus("current")
_OcspResponderURL_Type = OctetString
_OcspResponderURL_Object = MibScalar
ocspResponderURL = _OcspResponderURL_Object(
    (1, 3, 6, 1, 4, 1, 12532, 31),
    _OcspResponderURL_Type()
)
ocspResponderURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ocspResponderURL.setStatus("current")
_FanDescription_Type = OctetString
_FanDescription_Object = MibScalar
fanDescription = _FanDescription_Object(
    (1, 3, 6, 1, 4, 1, 12532, 32),
    _FanDescription_Type()
)
fanDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fanDescription.setStatus("current")
_PsDescription_Type = OctetString
_PsDescription_Object = MibScalar
psDescription = _PsDescription_Object(
    (1, 3, 6, 1, 4, 1, 12532, 33),
    _PsDescription_Type()
)
psDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psDescription.setStatus("current")
_RaidDescription_Type = OctetString
_RaidDescription_Object = MibScalar
raidDescription = _RaidDescription_Object(
    (1, 3, 6, 1, 4, 1, 12532, 34),
    _RaidDescription_Type()
)
raidDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raidDescription.setStatus("current")
_ClusterName_Type = OctetString
_ClusterName_Object = MibScalar
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 35),
    _ClusterName_Type()
)
clusterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clusterName.setStatus("current")
_NodeList_Type = OctetString
_NodeList_Object = MibScalar
nodeList = _NodeList_Object(
    (1, 3, 6, 1, 4, 1, 12532, 36),
    _NodeList_Type()
)
nodeList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nodeList.setStatus("current")
_VipType_Type = OctetString
_VipType_Object = MibScalar
vipType = _VipType_Object(
    (1, 3, 6, 1, 4, 1, 12532, 37),
    _VipType_Type()
)
vipType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vipType.setStatus("current")
_CurrentVIP_Type = OctetString
_CurrentVIP_Object = MibScalar
currentVIP = _CurrentVIP_Object(
    (1, 3, 6, 1, 4, 1, 12532, 38),
    _CurrentVIP_Type()
)
currentVIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentVIP.setStatus("current")
_NewVIP_Type = OctetString
_NewVIP_Object = MibScalar
newVIP = _NewVIP_Object(
    (1, 3, 6, 1, 4, 1, 12532, 39),
    _NewVIP_Type()
)
newVIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    newVIP.setStatus("current")
_NicEvent_Type = OctetString
_NicEvent_Object = MibScalar
nicEvent = _NicEvent_Object(
    (1, 3, 6, 1, 4, 1, 12532, 40),
    _NicEvent_Type()
)
nicEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nicEvent.setStatus("current")
_NodeName_Type = OctetString
_NodeName_Object = MibScalar
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 41),
    _NodeName_Type()
)
nodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nodeName.setStatus("current")
_IveTemperature_Type = Gauge32
_IveTemperature_Object = MibScalar
iveTemperature = _IveTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12532, 42),
    _IveTemperature_Type()
)
iveTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveTemperature.setStatus("current")
_IveTraps_ObjectIdentity = ObjectIdentity
iveTraps = _IveTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 251)
)
_IveSAProduct_ObjectIdentity = ObjectIdentity
iveSAProduct = _IveSAProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252)
)
_IveProductSA700_ObjectIdentity = ObjectIdentity
iveProductSA700 = _IveProductSA700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 1)
)
_IveSA700_ObjectIdentity = ObjectIdentity
iveSA700 = _IveSA700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 1, 1)
)
_IveProductSA2000_ObjectIdentity = ObjectIdentity
iveProductSA2000 = _IveProductSA2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 2)
)
_IveSA2000_ObjectIdentity = ObjectIdentity
iveSA2000 = _IveSA2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 2, 1)
)
_IveProductSA2500_ObjectIdentity = ObjectIdentity
iveProductSA2500 = _IveProductSA2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 3)
)
_IveSA2500_ObjectIdentity = ObjectIdentity
iveSA2500 = _IveSA2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 3, 1)
)
_IveProductSA4000_ObjectIdentity = ObjectIdentity
iveProductSA4000 = _IveProductSA4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 4)
)
_IveSA4000_ObjectIdentity = ObjectIdentity
iveSA4000 = _IveSA4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 4, 1)
)
_IveSA4000FIPS_ObjectIdentity = ObjectIdentity
iveSA4000FIPS = _IveSA4000FIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 4, 2)
)
_IveProductSA4500_ObjectIdentity = ObjectIdentity
iveProductSA4500 = _IveProductSA4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 5)
)
_IveSA4500_ObjectIdentity = ObjectIdentity
iveSA4500 = _IveSA4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 5, 1)
)
_IveSA4500FIPS_ObjectIdentity = ObjectIdentity
iveSA4500FIPS = _IveSA4500FIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 5, 2)
)
_IveProductSA6000_ObjectIdentity = ObjectIdentity
iveProductSA6000 = _IveProductSA6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 6)
)
_IveSA6000_ObjectIdentity = ObjectIdentity
iveSA6000 = _IveSA6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 6, 1)
)
_IveSA6000FIPS_ObjectIdentity = ObjectIdentity
iveSA6000FIPS = _IveSA6000FIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 6, 2)
)
_IveProductSA6500_ObjectIdentity = ObjectIdentity
iveProductSA6500 = _IveProductSA6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 7)
)
_IveSA6500_ObjectIdentity = ObjectIdentity
iveSA6500 = _IveSA6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 7, 1)
)
_IveSA6500FIPS_ObjectIdentity = ObjectIdentity
iveSA6500FIPS = _IveSA6500FIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 252, 7, 2)
)
_IveICProduct_ObjectIdentity = ObjectIdentity
iveICProduct = _IveICProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253)
)
_IveProductIC4000_ObjectIdentity = ObjectIdentity
iveProductIC4000 = _IveProductIC4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 1)
)
_IveIC4000_ObjectIdentity = ObjectIdentity
iveIC4000 = _IveIC4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 1, 1)
)
_IveProductIC4500_ObjectIdentity = ObjectIdentity
iveProductIC4500 = _IveProductIC4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 2)
)
_IveIC4500_ObjectIdentity = ObjectIdentity
iveIC4500 = _IveIC4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 2, 1)
)
_IveProductIC6000_ObjectIdentity = ObjectIdentity
iveProductIC6000 = _IveProductIC6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 3)
)
_IveIC6000_ObjectIdentity = ObjectIdentity
iveIC6000 = _IveIC6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 3, 1)
)
_IveIC6000FIPS_ObjectIdentity = ObjectIdentity
iveIC6000FIPS = _IveIC6000FIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 3, 2)
)
_IveProductIC6500_ObjectIdentity = ObjectIdentity
iveProductIC6500 = _IveProductIC6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 4)
)
_IveIC6500_ObjectIdentity = ObjectIdentity
iveIC6500 = _IveIC6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 253, 4, 1)
)
_IveMAGProduct_ObjectIdentity = ObjectIdentity
iveMAGProduct = _IveMAGProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254)
)
_IveProductMAG2600_ObjectIdentity = ObjectIdentity
iveProductMAG2600 = _IveProductMAG2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254, 1)
)
_IveMAG2600_ObjectIdentity = ObjectIdentity
iveMAG2600 = _IveMAG2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254, 1, 1)
)
_IveProductMAG4610_ObjectIdentity = ObjectIdentity
iveProductMAG4610 = _IveProductMAG4610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254, 2)
)
_IveMAG4610_ObjectIdentity = ObjectIdentity
iveMAG4610 = _IveMAG4610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254, 2, 1)
)
_IveProductSM160_ObjectIdentity = ObjectIdentity
iveProductSM160 = _IveProductSM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254, 3)
)
_IveMAGSM160_ObjectIdentity = ObjectIdentity
iveMAGSM160 = _IveMAGSM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254, 3, 1)
)
_IveProductSM360_ObjectIdentity = ObjectIdentity
iveProductSM360 = _IveProductSM360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254, 4)
)
_IveMAGSM360_ObjectIdentity = ObjectIdentity
iveMAGSM360 = _IveMAGSM360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 254, 4, 1)
)

# Managed Objects groups


# Notification objects

iveLogNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 4)
)
iveLogNearlyFull.setObjects(
      *(("JUNIPER-IVE-MIB", "logFullPercent"),
        ("JUNIPER-IVE-MIB", "logName"))
)
if mibBuilder.loadTexts:
    iveLogNearlyFull.setStatus(
        "current"
    )

iveLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 5)
)
iveLogFull.setObjects(
    ("JUNIPER-IVE-MIB", "logName")
)
if mibBuilder.loadTexts:
    iveLogFull.setStatus(
        "current"
    )

iveMaxConcurrentUsersSignedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 6)
)
if mibBuilder.loadTexts:
    iveMaxConcurrentUsersSignedIn.setStatus(
        "current"
    )

iveTooManyFailedLoginAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 7)
)
iveTooManyFailedLoginAttempts.setObjects(
    ("JUNIPER-IVE-MIB", "blockedIP")
)
if mibBuilder.loadTexts:
    iveTooManyFailedLoginAttempts.setStatus(
        "current"
    )

externalAuthServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 8)
)
externalAuthServerUnreachable.setObjects(
    ("JUNIPER-IVE-MIB", "authServerName")
)
if mibBuilder.loadTexts:
    externalAuthServerUnreachable.setStatus(
        "current"
    )

iveStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 9)
)
if mibBuilder.loadTexts:
    iveStart.setStatus(
        "current"
    )

iveShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 10)
)
if mibBuilder.loadTexts:
    iveShutdown.setStatus(
        "current"
    )

iveReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 11)
)
if mibBuilder.loadTexts:
    iveReboot.setStatus(
        "current"
    )

archiveServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 12)
)
if mibBuilder.loadTexts:
    archiveServerUnreachable.setStatus(
        "current"
    )

archiveServerLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 13)
)
if mibBuilder.loadTexts:
    archiveServerLoginFailed.setStatus(
        "current"
    )

archiveFileTransferFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 14)
)
archiveFileTransferFailed.setObjects(
    ("JUNIPER-IVE-MIB", "fileName")
)
if mibBuilder.loadTexts:
    archiveFileTransferFailed.setStatus(
        "current"
    )

meetingUserLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 15)
)
meetingUserLimit.setObjects(
    ("JUNIPER-IVE-MIB", "meetingUserCount")
)
if mibBuilder.loadTexts:
    meetingUserLimit.setStatus(
        "current"
    )

iveRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 16)
)
if mibBuilder.loadTexts:
    iveRestart.setStatus(
        "current"
    )

meetingLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 17)
)
meetingLimit.setObjects(
    ("JUNIPER-IVE-MIB", "meetingCount")
)
if mibBuilder.loadTexts:
    meetingLimit.setStatus(
        "current"
    )

iveDiskNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 18)
)
iveDiskNearlyFull.setObjects(
    ("JUNIPER-IVE-MIB", "diskFullPercent")
)
if mibBuilder.loadTexts:
    iveDiskNearlyFull.setStatus(
        "current"
    )

iveDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 19)
)
if mibBuilder.loadTexts:
    iveDiskFull.setStatus(
        "current"
    )

logMessageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 20)
)
logMessageTrap.setObjects(
      *(("JUNIPER-IVE-MIB", "logID"),
        ("JUNIPER-IVE-MIB", "logType"),
        ("JUNIPER-IVE-MIB", "logDescription"))
)
if mibBuilder.loadTexts:
    logMessageTrap.setStatus(
        "current"
    )

memUtilNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 21)
)
memUtilNotify.setObjects(
    ("JUNIPER-IVE-MIB", "iveMemoryUtil")
)
if mibBuilder.loadTexts:
    memUtilNotify.setStatus(
        "current"
    )

cpuUtilNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 22)
)
cpuUtilNotify.setObjects(
    ("JUNIPER-IVE-MIB", "iveCpuUtil")
)
if mibBuilder.loadTexts:
    cpuUtilNotify.setStatus(
        "current"
    )

swapUtilNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 23)
)
swapUtilNotify.setObjects(
    ("JUNIPER-IVE-MIB", "iveSwapUtil")
)
if mibBuilder.loadTexts:
    swapUtilNotify.setStatus(
        "current"
    )

iveMaxConcurrentUsersVirtualSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 24)
)
iveMaxConcurrentUsersVirtualSystem.setObjects(
    ("JUNIPER-IVE-MIB", "ivsName")
)
if mibBuilder.loadTexts:
    iveMaxConcurrentUsersVirtualSystem.setStatus(
        "current"
    )

ocspResponderConnectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 25)
)
ocspResponderConnectionFailed.setObjects(
    ("JUNIPER-IVE-MIB", "ocspResponderURL")
)
if mibBuilder.loadTexts:
    ocspResponderConnectionFailed.setStatus(
        "current"
    )

iveFanNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 26)
)
iveFanNotify.setObjects(
    ("JUNIPER-IVE-MIB", "fanDescription")
)
if mibBuilder.loadTexts:
    iveFanNotify.setStatus(
        "current"
    )

ivePowerSupplyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 27)
)
ivePowerSupplyNotify.setObjects(
    ("JUNIPER-IVE-MIB", "psDescription")
)
if mibBuilder.loadTexts:
    ivePowerSupplyNotify.setStatus(
        "current"
    )

iveRaidNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 28)
)
iveRaidNotify.setObjects(
    ("JUNIPER-IVE-MIB", "raidDescription")
)
if mibBuilder.loadTexts:
    iveRaidNotify.setStatus(
        "current"
    )

iveClusterDisableNodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 29)
)
iveClusterDisableNodeTrap.setObjects(
      *(("JUNIPER-IVE-MIB", "clusterName"),
        ("JUNIPER-IVE-MIB", "nodeList"))
)
if mibBuilder.loadTexts:
    iveClusterDisableNodeTrap.setStatus(
        "current"
    )

iveClusterChangedVIPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 30)
)
iveClusterChangedVIPTrap.setObjects(
      *(("JUNIPER-IVE-MIB", "vipType"),
        ("JUNIPER-IVE-MIB", "currentVIP"),
        ("JUNIPER-IVE-MIB", "newVIP"))
)
if mibBuilder.loadTexts:
    iveClusterChangedVIPTrap.setStatus(
        "current"
    )

iveNetExternalInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 31)
)
iveNetExternalInterfaceDownTrap.setObjects(
    ("JUNIPER-IVE-MIB", "nicEvent")
)
if mibBuilder.loadTexts:
    iveNetExternalInterfaceDownTrap.setStatus(
        "current"
    )

iveClusterDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 32)
)
iveClusterDeleteTrap.setObjects(
    ("JUNIPER-IVE-MIB", "nodeName")
)
if mibBuilder.loadTexts:
    iveClusterDeleteTrap.setStatus(
        "current"
    )

iveNetInternalInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 33)
)
iveNetInternalInterfaceDownTrap.setObjects(
    ("JUNIPER-IVE-MIB", "nicEvent")
)
if mibBuilder.loadTexts:
    iveNetInternalInterfaceDownTrap.setStatus(
        "current"
    )

iveNetManagementInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 34)
)
iveNetManagementInterfaceDownTrap.setObjects(
    ("JUNIPER-IVE-MIB", "nicEvent")
)
if mibBuilder.loadTexts:
    iveNetManagementInterfaceDownTrap.setStatus(
        "current"
    )

iveTemperatureNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 35)
)
iveTemperatureNotify.setObjects(
    ("JUNIPER-IVE-MIB", "iveTemperature")
)
if mibBuilder.loadTexts:
    iveTemperatureNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IVE-MIB",
    **{"juniper-ive": juniper_ive,
       "logFullPercent": logFullPercent,
       "signedInWebUsers": signedInWebUsers,
       "signedInMailUsers": signedInMailUsers,
       "blockedIP": blockedIP,
       "authServerName": authServerName,
       "productName": productName,
       "productVersion": productVersion,
       "fileName": fileName,
       "meetingUserCount": meetingUserCount,
       "iveCpuUtil": iveCpuUtil,
       "iveMemoryUtil": iveMemoryUtil,
       "iveConcurrentUsers": iveConcurrentUsers,
       "clusterConcurrentUsers": clusterConcurrentUsers,
       "iveTotalHits": iveTotalHits,
       "iveFileHits": iveFileHits,
       "iveWebHits": iveWebHits,
       "iveAppletHits": iveAppletHits,
       "ivetermHits": ivetermHits,
       "iveSAMHits": iveSAMHits,
       "iveNCHits": iveNCHits,
       "meetingHits": meetingHits,
       "meetingCount": meetingCount,
       "logName": logName,
       "iveSwapUtil": iveSwapUtil,
       "diskFullPercent": diskFullPercent,
       "blockedIPList": blockedIPList,
       "ipEntry": ipEntry,
       "ipIndex": ipIndex,
       "ipValue": ipValue,
       "logID": logID,
       "logType": logType,
       "logDescription": logDescription,
       "ivsName": ivsName,
       "ocspResponderURL": ocspResponderURL,
       "fanDescription": fanDescription,
       "psDescription": psDescription,
       "raidDescription": raidDescription,
       "clusterName": clusterName,
       "nodeList": nodeList,
       "vipType": vipType,
       "currentVIP": currentVIP,
       "newVIP": newVIP,
       "nicEvent": nicEvent,
       "nodeName": nodeName,
       "iveTemperature": iveTemperature,
       "iveTraps": iveTraps,
       "iveLogNearlyFull": iveLogNearlyFull,
       "iveLogFull": iveLogFull,
       "iveMaxConcurrentUsersSignedIn": iveMaxConcurrentUsersSignedIn,
       "iveTooManyFailedLoginAttempts": iveTooManyFailedLoginAttempts,
       "externalAuthServerUnreachable": externalAuthServerUnreachable,
       "iveStart": iveStart,
       "iveShutdown": iveShutdown,
       "iveReboot": iveReboot,
       "archiveServerUnreachable": archiveServerUnreachable,
       "archiveServerLoginFailed": archiveServerLoginFailed,
       "archiveFileTransferFailed": archiveFileTransferFailed,
       "meetingUserLimit": meetingUserLimit,
       "iveRestart": iveRestart,
       "meetingLimit": meetingLimit,
       "iveDiskNearlyFull": iveDiskNearlyFull,
       "iveDiskFull": iveDiskFull,
       "logMessageTrap": logMessageTrap,
       "memUtilNotify": memUtilNotify,
       "cpuUtilNotify": cpuUtilNotify,
       "swapUtilNotify": swapUtilNotify,
       "iveMaxConcurrentUsersVirtualSystem": iveMaxConcurrentUsersVirtualSystem,
       "ocspResponderConnectionFailed": ocspResponderConnectionFailed,
       "iveFanNotify": iveFanNotify,
       "ivePowerSupplyNotify": ivePowerSupplyNotify,
       "iveRaidNotify": iveRaidNotify,
       "iveClusterDisableNodeTrap": iveClusterDisableNodeTrap,
       "iveClusterChangedVIPTrap": iveClusterChangedVIPTrap,
       "iveNetExternalInterfaceDownTrap": iveNetExternalInterfaceDownTrap,
       "iveClusterDeleteTrap": iveClusterDeleteTrap,
       "iveNetInternalInterfaceDownTrap": iveNetInternalInterfaceDownTrap,
       "iveNetManagementInterfaceDownTrap": iveNetManagementInterfaceDownTrap,
       "iveTemperatureNotify": iveTemperatureNotify,
       "iveSAProduct": iveSAProduct,
       "iveProductSA700": iveProductSA700,
       "iveSA700": iveSA700,
       "iveProductSA2000": iveProductSA2000,
       "iveSA2000": iveSA2000,
       "iveProductSA2500": iveProductSA2500,
       "iveSA2500": iveSA2500,
       "iveProductSA4000": iveProductSA4000,
       "iveSA4000": iveSA4000,
       "iveSA4000FIPS": iveSA4000FIPS,
       "iveProductSA4500": iveProductSA4500,
       "iveSA4500": iveSA4500,
       "iveSA4500FIPS": iveSA4500FIPS,
       "iveProductSA6000": iveProductSA6000,
       "iveSA6000": iveSA6000,
       "iveSA6000FIPS": iveSA6000FIPS,
       "iveProductSA6500": iveProductSA6500,
       "iveSA6500": iveSA6500,
       "iveSA6500FIPS": iveSA6500FIPS,
       "iveICProduct": iveICProduct,
       "iveProductIC4000": iveProductIC4000,
       "iveIC4000": iveIC4000,
       "iveProductIC4500": iveProductIC4500,
       "iveIC4500": iveIC4500,
       "iveProductIC6000": iveProductIC6000,
       "iveIC6000": iveIC6000,
       "iveIC6000FIPS": iveIC6000FIPS,
       "iveProductIC6500": iveProductIC6500,
       "iveIC6500": iveIC6500,
       "iveMAGProduct": iveMAGProduct,
       "iveProductMAG2600": iveProductMAG2600,
       "iveMAG2600": iveMAG2600,
       "iveProductMAG4610": iveProductMAG4610,
       "iveMAG4610": iveMAG4610,
       "iveProductSM160": iveProductSM160,
       "iveMAGSM160": iveMAGSM160,
       "iveProductSM360": iveProductSM360,
       "iveMAGSM360": iveMAGSM360}
)
