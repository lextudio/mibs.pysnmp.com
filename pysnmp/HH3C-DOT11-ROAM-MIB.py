# SNMP MIB module (HH3C-DOT11-ROAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-ROAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:54 2024
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

(hh3cDot11,) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "hh3cDot11")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDot11ROAM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10)
)
hh3cDot11ROAM.setRevisions(
        ("2010-08-04 18:00",
         "2009-05-07 20:00",
         "2008-07-23 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDot11RoamMobileTunnelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )



class Hh3cDot11RoamAuthMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1))
    )



class Hh3cDot11RoamIACTPStatus(Integer32, TextualConvention):
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
        *(("idle", 2),
          ("init", 1),
          ("joinConfirmWait", 5),
          ("joinError", 6),
          ("joinRequestWait", 3),
          ("joinResponseWait", 4),
          ("run", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11RoamCfgGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RoamCfgGroup = _Hh3cDot11RoamCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1)
)
_Hh3cDot11MobGrpTable_Object = MibTable
hh3cDot11MobGrpTable = _Hh3cDot11MobGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11MobGrpTable.setStatus("current")
_Hh3cDot11MobGrpEntry_Object = MibTableRow
hh3cDot11MobGrpEntry = _Hh3cDot11MobGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1, 1)
)
hh3cDot11MobGrpEntry.setIndexNames(
    (0, "HH3C-DOT11-ROAM-MIB", "hh3cDot11MobGrpName"),
)
if mibBuilder.loadTexts:
    hh3cDot11MobGrpEntry.setStatus("current")


class _Hh3cDot11MobGrpName_Type(OctetString):
    """Custom type hh3cDot11MobGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cDot11MobGrpName_Type.__name__ = "OctetString"
_Hh3cDot11MobGrpName_Object = MibTableColumn
hh3cDot11MobGrpName = _Hh3cDot11MobGrpName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1, 1, 1),
    _Hh3cDot11MobGrpName_Type()
)
hh3cDot11MobGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpName.setStatus("current")


class _Hh3cdot11MobGrpTunnelType_Type(Hh3cDot11RoamMobileTunnelType):
    """Custom type hh3cdot11MobGrpTunnelType based on Hh3cDot11RoamMobileTunnelType"""


_Hh3cdot11MobGrpTunnelType_Object = MibTableColumn
hh3cdot11MobGrpTunnelType = _Hh3cdot11MobGrpTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1, 1, 2),
    _Hh3cdot11MobGrpTunnelType_Type()
)
hh3cdot11MobGrpTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdot11MobGrpTunnelType.setStatus("current")
_Hh3cDot11MobGrpSrcIPAddr_Type = InetAddress
_Hh3cDot11MobGrpSrcIPAddr_Object = MibTableColumn
hh3cDot11MobGrpSrcIPAddr = _Hh3cDot11MobGrpSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1, 1, 3),
    _Hh3cDot11MobGrpSrcIPAddr_Type()
)
hh3cDot11MobGrpSrcIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpSrcIPAddr.setStatus("current")


class _Hh3cDot11MobGrpAuthMode_Type(Hh3cDot11RoamAuthMode):
    """Custom type hh3cDot11MobGrpAuthMode based on Hh3cDot11RoamAuthMode"""


_Hh3cDot11MobGrpAuthMode_Object = MibTableColumn
hh3cDot11MobGrpAuthMode = _Hh3cDot11MobGrpAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1, 1, 4),
    _Hh3cDot11MobGrpAuthMode_Type()
)
hh3cDot11MobGrpAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpAuthMode.setStatus("current")


class _Hh3cDot11MobGrpAuthKey_Type(OctetString):
    """Custom type hh3cDot11MobGrpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hh3cDot11MobGrpAuthKey_Type.__name__ = "OctetString"
_Hh3cDot11MobGrpAuthKey_Object = MibTableColumn
hh3cDot11MobGrpAuthKey = _Hh3cDot11MobGrpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1, 1, 5),
    _Hh3cDot11MobGrpAuthKey_Type()
)
hh3cDot11MobGrpAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpAuthKey.setStatus("current")


class _Hh3cDot11MobGrpEnable_Type(TruthValue):
    """Custom type hh3cDot11MobGrpEnable based on TruthValue"""


_Hh3cDot11MobGrpEnable_Object = MibTableColumn
hh3cDot11MobGrpEnable = _Hh3cDot11MobGrpEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1, 1, 6),
    _Hh3cDot11MobGrpEnable_Type()
)
hh3cDot11MobGrpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpEnable.setStatus("current")
_Hh3cDot11MobGrpRowStatus_Type = RowStatus
_Hh3cDot11MobGrpRowStatus_Object = MibTableColumn
hh3cDot11MobGrpRowStatus = _Hh3cDot11MobGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 1, 1, 7),
    _Hh3cDot11MobGrpRowStatus_Type()
)
hh3cDot11MobGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpRowStatus.setStatus("current")
_Hh3cDot11MobGrpMemberTable_Object = MibTable
hh3cDot11MobGrpMemberTable = _Hh3cDot11MobGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11MobGrpMemberTable.setStatus("current")
_Hh3cDot11MobGrpMemberEntry_Object = MibTableRow
hh3cDot11MobGrpMemberEntry = _Hh3cDot11MobGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 2, 1)
)
hh3cDot11MobGrpMemberEntry.setIndexNames(
    (0, "HH3C-DOT11-ROAM-MIB", "hh3cDot11MobGrpName"),
    (0, "HH3C-DOT11-ROAM-MIB", "hh3cDot11MobGrpMemberIpAddr"),
)
if mibBuilder.loadTexts:
    hh3cDot11MobGrpMemberEntry.setStatus("current")
_Hh3cDot11MobGrpMemberIpAddr_Type = InetAddress
_Hh3cDot11MobGrpMemberIpAddr_Object = MibTableColumn
hh3cDot11MobGrpMemberIpAddr = _Hh3cDot11MobGrpMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 2, 1, 1),
    _Hh3cDot11MobGrpMemberIpAddr_Type()
)
hh3cDot11MobGrpMemberIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpMemberIpAddr.setStatus("current")
_Hh3cDot11MobGrpMemberStatus_Type = Hh3cDot11RoamIACTPStatus
_Hh3cDot11MobGrpMemberStatus_Object = MibTableColumn
hh3cDot11MobGrpMemberStatus = _Hh3cDot11MobGrpMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 2, 1, 2),
    _Hh3cDot11MobGrpMemberStatus_Type()
)
hh3cDot11MobGrpMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpMemberStatus.setStatus("current")
_Hh3cDot11MobGrpMemberIf_Type = OctetString
_Hh3cDot11MobGrpMemberIf_Object = MibTableColumn
hh3cDot11MobGrpMemberIf = _Hh3cDot11MobGrpMemberIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 2, 1, 3),
    _Hh3cDot11MobGrpMemberIf_Type()
)
hh3cDot11MobGrpMemberIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpMemberIf.setStatus("current")
_Hh3cDot11MobGrpMemberUpTime_Type = Integer32
_Hh3cDot11MobGrpMemberUpTime_Object = MibTableColumn
hh3cDot11MobGrpMemberUpTime = _Hh3cDot11MobGrpMemberUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 2, 1, 4),
    _Hh3cDot11MobGrpMemberUpTime_Type()
)
hh3cDot11MobGrpMemberUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpMemberUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpMemberUpTime.setUnits("second")
_Hh3cDot11MobGrpMemberRowStatus_Type = RowStatus
_Hh3cDot11MobGrpMemberRowStatus_Object = MibTableColumn
hh3cDot11MobGrpMemberRowStatus = _Hh3cDot11MobGrpMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 1, 2, 1, 5),
    _Hh3cDot11MobGrpMemberRowStatus_Type()
)
hh3cDot11MobGrpMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11MobGrpMemberRowStatus.setStatus("current")
_Hh3cDot11RoamStatusGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RoamStatusGroup = _Hh3cDot11RoamStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2)
)
_Hh3cDot11RoamInInfoTable_Object = MibTable
hh3cDot11RoamInInfoTable = _Hh3cDot11RoamInInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RoamInInfoTable.setStatus("current")
_Hh3cDot11RoamInInfoEntry_Object = MibTableRow
hh3cDot11RoamInInfoEntry = _Hh3cDot11RoamInInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 1, 1)
)
hh3cDot11RoamInInfoEntry.setIndexNames(
    (0, "HH3C-DOT11-ROAM-MIB", "hh3cDot11RoamClientMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11RoamInInfoEntry.setStatus("current")
_Hh3cDot11RoamClientMAC_Type = MacAddress
_Hh3cDot11RoamClientMAC_Object = MibTableColumn
hh3cDot11RoamClientMAC = _Hh3cDot11RoamClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 1, 1, 1),
    _Hh3cDot11RoamClientMAC_Type()
)
hh3cDot11RoamClientMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RoamClientMAC.setStatus("current")
_Hh3cDot11RoamInClientBSSID_Type = MacAddress
_Hh3cDot11RoamInClientBSSID_Object = MibTableColumn
hh3cDot11RoamInClientBSSID = _Hh3cDot11RoamInClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 1, 1, 2),
    _Hh3cDot11RoamInClientBSSID_Type()
)
hh3cDot11RoamInClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamInClientBSSID.setStatus("current")
_Hh3cDot11RoamInClientVlanID_Type = Integer32
_Hh3cDot11RoamInClientVlanID_Object = MibTableColumn
hh3cDot11RoamInClientVlanID = _Hh3cDot11RoamInClientVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 1, 1, 3),
    _Hh3cDot11RoamInClientVlanID_Type()
)
hh3cDot11RoamInClientVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamInClientVlanID.setStatus("current")
_Hh3cDot11RoamInHomeACIPType_Type = InetAddressType
_Hh3cDot11RoamInHomeACIPType_Object = MibTableColumn
hh3cDot11RoamInHomeACIPType = _Hh3cDot11RoamInHomeACIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 1, 1, 4),
    _Hh3cDot11RoamInHomeACIPType_Type()
)
hh3cDot11RoamInHomeACIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamInHomeACIPType.setStatus("current")
_Hh3cDot11RoamInHomeACIPAddr_Type = InetAddress
_Hh3cDot11RoamInHomeACIPAddr_Object = MibTableColumn
hh3cDot11RoamInHomeACIPAddr = _Hh3cDot11RoamInHomeACIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 1, 1, 5),
    _Hh3cDot11RoamInHomeACIPAddr_Type()
)
hh3cDot11RoamInHomeACIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamInHomeACIPAddr.setStatus("current")
_Hh3cDot11RoamOutInfoTable_Object = MibTable
hh3cDot11RoamOutInfoTable = _Hh3cDot11RoamOutInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RoamOutInfoTable.setStatus("current")
_Hh3cDot11RoamOutInfoEntry_Object = MibTableRow
hh3cDot11RoamOutInfoEntry = _Hh3cDot11RoamOutInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 2, 1)
)
hh3cDot11RoamOutInfoEntry.setIndexNames(
    (0, "HH3C-DOT11-ROAM-MIB", "hh3cDot11RoamClientMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11RoamOutInfoEntry.setStatus("current")
_Hh3cDot11RoamOutClientBSSID_Type = MacAddress
_Hh3cDot11RoamOutClientBSSID_Object = MibTableColumn
hh3cDot11RoamOutClientBSSID = _Hh3cDot11RoamOutClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 2, 1, 1),
    _Hh3cDot11RoamOutClientBSSID_Type()
)
hh3cDot11RoamOutClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamOutClientBSSID.setStatus("current")
_Hh3cDot11RoamOutClientVlanID_Type = Integer32
_Hh3cDot11RoamOutClientVlanID_Object = MibTableColumn
hh3cDot11RoamOutClientVlanID = _Hh3cDot11RoamOutClientVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 2, 1, 2),
    _Hh3cDot11RoamOutClientVlanID_Type()
)
hh3cDot11RoamOutClientVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamOutClientVlanID.setStatus("current")
_Hh3cDot11RoamOutForeignACIPType_Type = InetAddressType
_Hh3cDot11RoamOutForeignACIPType_Object = MibTableColumn
hh3cDot11RoamOutForeignACIPType = _Hh3cDot11RoamOutForeignACIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 2, 1, 3),
    _Hh3cDot11RoamOutForeignACIPType_Type()
)
hh3cDot11RoamOutForeignACIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamOutForeignACIPType.setStatus("current")
_Hh3cDot11RoamOutForeignACIPAddr_Type = InetAddress
_Hh3cDot11RoamOutForeignACIPAddr_Object = MibTableColumn
hh3cDot11RoamOutForeignACIPAddr = _Hh3cDot11RoamOutForeignACIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 2, 1, 4),
    _Hh3cDot11RoamOutForeignACIPAddr_Type()
)
hh3cDot11RoamOutForeignACIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamOutForeignACIPAddr.setStatus("current")
_Hh3cDot11RoamOutClientUpTime_Type = Integer32
_Hh3cDot11RoamOutClientUpTime_Object = MibTableColumn
hh3cDot11RoamOutClientUpTime = _Hh3cDot11RoamOutClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 2, 1, 5),
    _Hh3cDot11RoamOutClientUpTime_Type()
)
hh3cDot11RoamOutClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamOutClientUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RoamOutClientUpTime.setUnits("second")
_Hh3cDot11RoamTrackTable_Object = MibTable
hh3cDot11RoamTrackTable = _Hh3cDot11RoamTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackTable.setStatus("current")
_Hh3cDot11RoamTrackEntry_Object = MibTableRow
hh3cDot11RoamTrackEntry = _Hh3cDot11RoamTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 3, 1)
)
hh3cDot11RoamTrackEntry.setIndexNames(
    (0, "HH3C-DOT11-ROAM-MIB", "hh3cDot11RoamTrackIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackEntry.setStatus("current")
_Hh3cDot11RoamTrackIndex_Type = Integer32
_Hh3cDot11RoamTrackIndex_Object = MibTableColumn
hh3cDot11RoamTrackIndex = _Hh3cDot11RoamTrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 3, 1, 1),
    _Hh3cDot11RoamTrackIndex_Type()
)
hh3cDot11RoamTrackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackIndex.setStatus("current")
_Hh3cDot11RoamTrackClientMAC_Type = MacAddress
_Hh3cDot11RoamTrackClientMAC_Object = MibTableColumn
hh3cDot11RoamTrackClientMAC = _Hh3cDot11RoamTrackClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 3, 1, 2),
    _Hh3cDot11RoamTrackClientMAC_Type()
)
hh3cDot11RoamTrackClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackClientMAC.setStatus("current")
_Hh3cDot11RoamTrackBSSID_Type = MacAddress
_Hh3cDot11RoamTrackBSSID_Object = MibTableColumn
hh3cDot11RoamTrackBSSID = _Hh3cDot11RoamTrackBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 3, 1, 3),
    _Hh3cDot11RoamTrackBSSID_Type()
)
hh3cDot11RoamTrackBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackBSSID.setStatus("current")
_Hh3cDot11RoamTrackUpTime_Type = Integer32
_Hh3cDot11RoamTrackUpTime_Object = MibTableColumn
hh3cDot11RoamTrackUpTime = _Hh3cDot11RoamTrackUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 3, 1, 4),
    _Hh3cDot11RoamTrackUpTime_Type()
)
hh3cDot11RoamTrackUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackUpTime.setUnits("second")
_Hh3cDot11RoamTrackACIPType_Type = InetAddressType
_Hh3cDot11RoamTrackACIPType_Object = MibTableColumn
hh3cDot11RoamTrackACIPType = _Hh3cDot11RoamTrackACIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 3, 1, 5),
    _Hh3cDot11RoamTrackACIPType_Type()
)
hh3cDot11RoamTrackACIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackACIPType.setStatus("current")
_Hh3cDot11RoamTrackACIPAddr_Type = InetAddress
_Hh3cDot11RoamTrackACIPAddr_Object = MibTableColumn
hh3cDot11RoamTrackACIPAddr = _Hh3cDot11RoamTrackACIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 2, 3, 1, 6),
    _Hh3cDot11RoamTrackACIPAddr_Type()
)
hh3cDot11RoamTrackACIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RoamTrackACIPAddr.setStatus("current")
_Hh3cDot11RoamStatisGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RoamStatisGroup = _Hh3cDot11RoamStatisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 3)
)
_Hh3cDot11IntraACRoamingSuccCnt_Type = Integer32
_Hh3cDot11IntraACRoamingSuccCnt_Object = MibScalar
hh3cDot11IntraACRoamingSuccCnt = _Hh3cDot11IntraACRoamingSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 3, 1),
    _Hh3cDot11IntraACRoamingSuccCnt_Type()
)
hh3cDot11IntraACRoamingSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IntraACRoamingSuccCnt.setStatus("current")
_Hh3cDot11InterACRoamingSuccCnt_Type = Integer32
_Hh3cDot11InterACRoamingSuccCnt_Object = MibScalar
hh3cDot11InterACRoamingSuccCnt = _Hh3cDot11InterACRoamingSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 3, 2),
    _Hh3cDot11InterACRoamingSuccCnt_Type()
)
hh3cDot11InterACRoamingSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11InterACRoamingSuccCnt.setStatus("current")
_Hh3cDot11InterACRoamOutSuccCnt_Type = Integer32
_Hh3cDot11InterACRoamOutSuccCnt_Object = MibScalar
hh3cDot11InterACRoamOutSuccCnt = _Hh3cDot11InterACRoamOutSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 3, 3),
    _Hh3cDot11InterACRoamOutSuccCnt_Type()
)
hh3cDot11InterACRoamOutSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11InterACRoamOutSuccCnt.setStatus("current")
_Hh3cDot11RoamStatis2Group_ObjectIdentity = ObjectIdentity
hh3cDot11RoamStatis2Group = _Hh3cDot11RoamStatis2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 4)
)
_Hh3cDot11IntraACRoamingSuccCnt2_Type = Counter32
_Hh3cDot11IntraACRoamingSuccCnt2_Object = MibScalar
hh3cDot11IntraACRoamingSuccCnt2 = _Hh3cDot11IntraACRoamingSuccCnt2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 4, 1),
    _Hh3cDot11IntraACRoamingSuccCnt2_Type()
)
hh3cDot11IntraACRoamingSuccCnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IntraACRoamingSuccCnt2.setStatus("current")
_Hh3cDot11InterACRoamingSuccCnt2_Type = Counter32
_Hh3cDot11InterACRoamingSuccCnt2_Object = MibScalar
hh3cDot11InterACRoamingSuccCnt2 = _Hh3cDot11InterACRoamingSuccCnt2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 4, 2),
    _Hh3cDot11InterACRoamingSuccCnt2_Type()
)
hh3cDot11InterACRoamingSuccCnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11InterACRoamingSuccCnt2.setStatus("current")
_Hh3cDot11InterACRoamOutSuccCnt2_Type = Counter32
_Hh3cDot11InterACRoamOutSuccCnt2_Object = MibScalar
hh3cDot11InterACRoamOutSuccCnt2 = _Hh3cDot11InterACRoamOutSuccCnt2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 10, 4, 3),
    _Hh3cDot11InterACRoamOutSuccCnt2_Type()
)
hh3cDot11InterACRoamOutSuccCnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11InterACRoamOutSuccCnt2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-ROAM-MIB",
    **{"Hh3cDot11RoamMobileTunnelType": Hh3cDot11RoamMobileTunnelType,
       "Hh3cDot11RoamAuthMode": Hh3cDot11RoamAuthMode,
       "Hh3cDot11RoamIACTPStatus": Hh3cDot11RoamIACTPStatus,
       "hh3cDot11ROAM": hh3cDot11ROAM,
       "hh3cDot11RoamCfgGroup": hh3cDot11RoamCfgGroup,
       "hh3cDot11MobGrpTable": hh3cDot11MobGrpTable,
       "hh3cDot11MobGrpEntry": hh3cDot11MobGrpEntry,
       "hh3cDot11MobGrpName": hh3cDot11MobGrpName,
       "hh3cdot11MobGrpTunnelType": hh3cdot11MobGrpTunnelType,
       "hh3cDot11MobGrpSrcIPAddr": hh3cDot11MobGrpSrcIPAddr,
       "hh3cDot11MobGrpAuthMode": hh3cDot11MobGrpAuthMode,
       "hh3cDot11MobGrpAuthKey": hh3cDot11MobGrpAuthKey,
       "hh3cDot11MobGrpEnable": hh3cDot11MobGrpEnable,
       "hh3cDot11MobGrpRowStatus": hh3cDot11MobGrpRowStatus,
       "hh3cDot11MobGrpMemberTable": hh3cDot11MobGrpMemberTable,
       "hh3cDot11MobGrpMemberEntry": hh3cDot11MobGrpMemberEntry,
       "hh3cDot11MobGrpMemberIpAddr": hh3cDot11MobGrpMemberIpAddr,
       "hh3cDot11MobGrpMemberStatus": hh3cDot11MobGrpMemberStatus,
       "hh3cDot11MobGrpMemberIf": hh3cDot11MobGrpMemberIf,
       "hh3cDot11MobGrpMemberUpTime": hh3cDot11MobGrpMemberUpTime,
       "hh3cDot11MobGrpMemberRowStatus": hh3cDot11MobGrpMemberRowStatus,
       "hh3cDot11RoamStatusGroup": hh3cDot11RoamStatusGroup,
       "hh3cDot11RoamInInfoTable": hh3cDot11RoamInInfoTable,
       "hh3cDot11RoamInInfoEntry": hh3cDot11RoamInInfoEntry,
       "hh3cDot11RoamClientMAC": hh3cDot11RoamClientMAC,
       "hh3cDot11RoamInClientBSSID": hh3cDot11RoamInClientBSSID,
       "hh3cDot11RoamInClientVlanID": hh3cDot11RoamInClientVlanID,
       "hh3cDot11RoamInHomeACIPType": hh3cDot11RoamInHomeACIPType,
       "hh3cDot11RoamInHomeACIPAddr": hh3cDot11RoamInHomeACIPAddr,
       "hh3cDot11RoamOutInfoTable": hh3cDot11RoamOutInfoTable,
       "hh3cDot11RoamOutInfoEntry": hh3cDot11RoamOutInfoEntry,
       "hh3cDot11RoamOutClientBSSID": hh3cDot11RoamOutClientBSSID,
       "hh3cDot11RoamOutClientVlanID": hh3cDot11RoamOutClientVlanID,
       "hh3cDot11RoamOutForeignACIPType": hh3cDot11RoamOutForeignACIPType,
       "hh3cDot11RoamOutForeignACIPAddr": hh3cDot11RoamOutForeignACIPAddr,
       "hh3cDot11RoamOutClientUpTime": hh3cDot11RoamOutClientUpTime,
       "hh3cDot11RoamTrackTable": hh3cDot11RoamTrackTable,
       "hh3cDot11RoamTrackEntry": hh3cDot11RoamTrackEntry,
       "hh3cDot11RoamTrackIndex": hh3cDot11RoamTrackIndex,
       "hh3cDot11RoamTrackClientMAC": hh3cDot11RoamTrackClientMAC,
       "hh3cDot11RoamTrackBSSID": hh3cDot11RoamTrackBSSID,
       "hh3cDot11RoamTrackUpTime": hh3cDot11RoamTrackUpTime,
       "hh3cDot11RoamTrackACIPType": hh3cDot11RoamTrackACIPType,
       "hh3cDot11RoamTrackACIPAddr": hh3cDot11RoamTrackACIPAddr,
       "hh3cDot11RoamStatisGroup": hh3cDot11RoamStatisGroup,
       "hh3cDot11IntraACRoamingSuccCnt": hh3cDot11IntraACRoamingSuccCnt,
       "hh3cDot11InterACRoamingSuccCnt": hh3cDot11InterACRoamingSuccCnt,
       "hh3cDot11InterACRoamOutSuccCnt": hh3cDot11InterACRoamOutSuccCnt,
       "hh3cDot11RoamStatis2Group": hh3cDot11RoamStatis2Group,
       "hh3cDot11IntraACRoamingSuccCnt2": hh3cDot11IntraACRoamingSuccCnt2,
       "hh3cDot11InterACRoamingSuccCnt2": hh3cDot11InterACRoamingSuccCnt2,
       "hh3cDot11InterACRoamOutSuccCnt2": hh3cDot11InterACRoamOutSuccCnt2}
)
