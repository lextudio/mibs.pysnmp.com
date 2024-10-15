# SNMP MIB module (HPN-ICF-DOT11-ROAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-ROAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:53 2024
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

(hpnicfDot11,) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "hpnicfDot11")

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

hpnicfDot11ROAM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10)
)
hpnicfDot11ROAM.setRevisions(
        ("2010-08-04 18:00",
         "2009-05-07 20:00",
         "2008-07-23 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfDot11RoamMobileTunnelType(Integer32, TextualConvention):
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



class HpnicfDot11RoamAuthMode(Integer32, TextualConvention):
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



class HpnicfDot11RoamIACTPStatus(Integer32, TextualConvention):
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

_HpnicfDot11RoamCfgGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RoamCfgGroup = _HpnicfDot11RoamCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1)
)
_HpnicfDot11MobGrpTable_Object = MibTable
hpnicfDot11MobGrpTable = _HpnicfDot11MobGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpTable.setStatus("current")
_HpnicfDot11MobGrpEntry_Object = MibTableRow
hpnicfDot11MobGrpEntry = _HpnicfDot11MobGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1, 1)
)
hpnicfDot11MobGrpEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ROAM-MIB", "hpnicfDot11MobGrpName"),
)
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpEntry.setStatus("current")


class _HpnicfDot11MobGrpName_Type(OctetString):
    """Custom type hpnicfDot11MobGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HpnicfDot11MobGrpName_Type.__name__ = "OctetString"
_HpnicfDot11MobGrpName_Object = MibTableColumn
hpnicfDot11MobGrpName = _HpnicfDot11MobGrpName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1, 1, 1),
    _HpnicfDot11MobGrpName_Type()
)
hpnicfDot11MobGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpName.setStatus("current")


class _Hpnicfdot11MobGrpTunnelType_Type(HpnicfDot11RoamMobileTunnelType):
    """Custom type hpnicfdot11MobGrpTunnelType based on HpnicfDot11RoamMobileTunnelType"""


_Hpnicfdot11MobGrpTunnelType_Object = MibTableColumn
hpnicfdot11MobGrpTunnelType = _Hpnicfdot11MobGrpTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1, 1, 2),
    _Hpnicfdot11MobGrpTunnelType_Type()
)
hpnicfdot11MobGrpTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdot11MobGrpTunnelType.setStatus("current")
_HpnicfDot11MobGrpSrcIPAddr_Type = InetAddress
_HpnicfDot11MobGrpSrcIPAddr_Object = MibTableColumn
hpnicfDot11MobGrpSrcIPAddr = _HpnicfDot11MobGrpSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1, 1, 3),
    _HpnicfDot11MobGrpSrcIPAddr_Type()
)
hpnicfDot11MobGrpSrcIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpSrcIPAddr.setStatus("current")


class _HpnicfDot11MobGrpAuthMode_Type(HpnicfDot11RoamAuthMode):
    """Custom type hpnicfDot11MobGrpAuthMode based on HpnicfDot11RoamAuthMode"""


_HpnicfDot11MobGrpAuthMode_Object = MibTableColumn
hpnicfDot11MobGrpAuthMode = _HpnicfDot11MobGrpAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1, 1, 4),
    _HpnicfDot11MobGrpAuthMode_Type()
)
hpnicfDot11MobGrpAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpAuthMode.setStatus("current")


class _HpnicfDot11MobGrpAuthKey_Type(OctetString):
    """Custom type hpnicfDot11MobGrpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpnicfDot11MobGrpAuthKey_Type.__name__ = "OctetString"
_HpnicfDot11MobGrpAuthKey_Object = MibTableColumn
hpnicfDot11MobGrpAuthKey = _HpnicfDot11MobGrpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1, 1, 5),
    _HpnicfDot11MobGrpAuthKey_Type()
)
hpnicfDot11MobGrpAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpAuthKey.setStatus("current")


class _HpnicfDot11MobGrpEnable_Type(TruthValue):
    """Custom type hpnicfDot11MobGrpEnable based on TruthValue"""


_HpnicfDot11MobGrpEnable_Object = MibTableColumn
hpnicfDot11MobGrpEnable = _HpnicfDot11MobGrpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1, 1, 6),
    _HpnicfDot11MobGrpEnable_Type()
)
hpnicfDot11MobGrpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpEnable.setStatus("current")
_HpnicfDot11MobGrpRowStatus_Type = RowStatus
_HpnicfDot11MobGrpRowStatus_Object = MibTableColumn
hpnicfDot11MobGrpRowStatus = _HpnicfDot11MobGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 1, 1, 7),
    _HpnicfDot11MobGrpRowStatus_Type()
)
hpnicfDot11MobGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpRowStatus.setStatus("current")
_HpnicfDot11MobGrpMemberTable_Object = MibTable
hpnicfDot11MobGrpMemberTable = _HpnicfDot11MobGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpMemberTable.setStatus("current")
_HpnicfDot11MobGrpMemberEntry_Object = MibTableRow
hpnicfDot11MobGrpMemberEntry = _HpnicfDot11MobGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 2, 1)
)
hpnicfDot11MobGrpMemberEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ROAM-MIB", "hpnicfDot11MobGrpName"),
    (0, "HPN-ICF-DOT11-ROAM-MIB", "hpnicfDot11MobGrpMemberIpAddr"),
)
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpMemberEntry.setStatus("current")
_HpnicfDot11MobGrpMemberIpAddr_Type = InetAddress
_HpnicfDot11MobGrpMemberIpAddr_Object = MibTableColumn
hpnicfDot11MobGrpMemberIpAddr = _HpnicfDot11MobGrpMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 2, 1, 1),
    _HpnicfDot11MobGrpMemberIpAddr_Type()
)
hpnicfDot11MobGrpMemberIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpMemberIpAddr.setStatus("current")
_HpnicfDot11MobGrpMemberStatus_Type = HpnicfDot11RoamIACTPStatus
_HpnicfDot11MobGrpMemberStatus_Object = MibTableColumn
hpnicfDot11MobGrpMemberStatus = _HpnicfDot11MobGrpMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 2, 1, 2),
    _HpnicfDot11MobGrpMemberStatus_Type()
)
hpnicfDot11MobGrpMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpMemberStatus.setStatus("current")
_HpnicfDot11MobGrpMemberIf_Type = OctetString
_HpnicfDot11MobGrpMemberIf_Object = MibTableColumn
hpnicfDot11MobGrpMemberIf = _HpnicfDot11MobGrpMemberIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 2, 1, 3),
    _HpnicfDot11MobGrpMemberIf_Type()
)
hpnicfDot11MobGrpMemberIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpMemberIf.setStatus("current")
_HpnicfDot11MobGrpMemberUpTime_Type = Integer32
_HpnicfDot11MobGrpMemberUpTime_Object = MibTableColumn
hpnicfDot11MobGrpMemberUpTime = _HpnicfDot11MobGrpMemberUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 2, 1, 4),
    _HpnicfDot11MobGrpMemberUpTime_Type()
)
hpnicfDot11MobGrpMemberUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpMemberUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpMemberUpTime.setUnits("second")
_HpnicfDot11MobGrpMemberRowStatus_Type = RowStatus
_HpnicfDot11MobGrpMemberRowStatus_Object = MibTableColumn
hpnicfDot11MobGrpMemberRowStatus = _HpnicfDot11MobGrpMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 1, 2, 1, 5),
    _HpnicfDot11MobGrpMemberRowStatus_Type()
)
hpnicfDot11MobGrpMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11MobGrpMemberRowStatus.setStatus("current")
_HpnicfDot11RoamStatusGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RoamStatusGroup = _HpnicfDot11RoamStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2)
)
_HpnicfDot11RoamInInfoTable_Object = MibTable
hpnicfDot11RoamInInfoTable = _HpnicfDot11RoamInInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11RoamInInfoTable.setStatus("current")
_HpnicfDot11RoamInInfoEntry_Object = MibTableRow
hpnicfDot11RoamInInfoEntry = _HpnicfDot11RoamInInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 1, 1)
)
hpnicfDot11RoamInInfoEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ROAM-MIB", "hpnicfDot11RoamClientMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RoamInInfoEntry.setStatus("current")
_HpnicfDot11RoamClientMAC_Type = MacAddress
_HpnicfDot11RoamClientMAC_Object = MibTableColumn
hpnicfDot11RoamClientMAC = _HpnicfDot11RoamClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 1, 1, 1),
    _HpnicfDot11RoamClientMAC_Type()
)
hpnicfDot11RoamClientMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RoamClientMAC.setStatus("current")
_HpnicfDot11RoamInClientBSSID_Type = MacAddress
_HpnicfDot11RoamInClientBSSID_Object = MibTableColumn
hpnicfDot11RoamInClientBSSID = _HpnicfDot11RoamInClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 1, 1, 2),
    _HpnicfDot11RoamInClientBSSID_Type()
)
hpnicfDot11RoamInClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamInClientBSSID.setStatus("current")
_HpnicfDot11RoamInClientVlanID_Type = Integer32
_HpnicfDot11RoamInClientVlanID_Object = MibTableColumn
hpnicfDot11RoamInClientVlanID = _HpnicfDot11RoamInClientVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 1, 1, 3),
    _HpnicfDot11RoamInClientVlanID_Type()
)
hpnicfDot11RoamInClientVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamInClientVlanID.setStatus("current")
_HpnicfDot11RoamInHomeACIPType_Type = InetAddressType
_HpnicfDot11RoamInHomeACIPType_Object = MibTableColumn
hpnicfDot11RoamInHomeACIPType = _HpnicfDot11RoamInHomeACIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 1, 1, 4),
    _HpnicfDot11RoamInHomeACIPType_Type()
)
hpnicfDot11RoamInHomeACIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamInHomeACIPType.setStatus("current")
_HpnicfDot11RoamInHomeACIPAddr_Type = InetAddress
_HpnicfDot11RoamInHomeACIPAddr_Object = MibTableColumn
hpnicfDot11RoamInHomeACIPAddr = _HpnicfDot11RoamInHomeACIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 1, 1, 5),
    _HpnicfDot11RoamInHomeACIPAddr_Type()
)
hpnicfDot11RoamInHomeACIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamInHomeACIPAddr.setStatus("current")
_HpnicfDot11RoamOutInfoTable_Object = MibTable
hpnicfDot11RoamOutInfoTable = _HpnicfDot11RoamOutInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11RoamOutInfoTable.setStatus("current")
_HpnicfDot11RoamOutInfoEntry_Object = MibTableRow
hpnicfDot11RoamOutInfoEntry = _HpnicfDot11RoamOutInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 2, 1)
)
hpnicfDot11RoamOutInfoEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ROAM-MIB", "hpnicfDot11RoamClientMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RoamOutInfoEntry.setStatus("current")
_HpnicfDot11RoamOutClientBSSID_Type = MacAddress
_HpnicfDot11RoamOutClientBSSID_Object = MibTableColumn
hpnicfDot11RoamOutClientBSSID = _HpnicfDot11RoamOutClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 2, 1, 1),
    _HpnicfDot11RoamOutClientBSSID_Type()
)
hpnicfDot11RoamOutClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamOutClientBSSID.setStatus("current")
_HpnicfDot11RoamOutClientVlanID_Type = Integer32
_HpnicfDot11RoamOutClientVlanID_Object = MibTableColumn
hpnicfDot11RoamOutClientVlanID = _HpnicfDot11RoamOutClientVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 2, 1, 2),
    _HpnicfDot11RoamOutClientVlanID_Type()
)
hpnicfDot11RoamOutClientVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamOutClientVlanID.setStatus("current")
_HpnicfDot11RoamOutForeignACIPType_Type = InetAddressType
_HpnicfDot11RoamOutForeignACIPType_Object = MibTableColumn
hpnicfDot11RoamOutForeignACIPType = _HpnicfDot11RoamOutForeignACIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 2, 1, 3),
    _HpnicfDot11RoamOutForeignACIPType_Type()
)
hpnicfDot11RoamOutForeignACIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamOutForeignACIPType.setStatus("current")
_HpnicfDot11RoamOutForeignACIPAddr_Type = InetAddress
_HpnicfDot11RoamOutForeignACIPAddr_Object = MibTableColumn
hpnicfDot11RoamOutForeignACIPAddr = _HpnicfDot11RoamOutForeignACIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 2, 1, 4),
    _HpnicfDot11RoamOutForeignACIPAddr_Type()
)
hpnicfDot11RoamOutForeignACIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamOutForeignACIPAddr.setStatus("current")
_HpnicfDot11RoamOutClientUpTime_Type = Integer32
_HpnicfDot11RoamOutClientUpTime_Object = MibTableColumn
hpnicfDot11RoamOutClientUpTime = _HpnicfDot11RoamOutClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 2, 1, 5),
    _HpnicfDot11RoamOutClientUpTime_Type()
)
hpnicfDot11RoamOutClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamOutClientUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RoamOutClientUpTime.setUnits("second")
_HpnicfDot11RoamTrackTable_Object = MibTable
hpnicfDot11RoamTrackTable = _HpnicfDot11RoamTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackTable.setStatus("current")
_HpnicfDot11RoamTrackEntry_Object = MibTableRow
hpnicfDot11RoamTrackEntry = _HpnicfDot11RoamTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 3, 1)
)
hpnicfDot11RoamTrackEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-ROAM-MIB", "hpnicfDot11RoamTrackIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackEntry.setStatus("current")
_HpnicfDot11RoamTrackIndex_Type = Integer32
_HpnicfDot11RoamTrackIndex_Object = MibTableColumn
hpnicfDot11RoamTrackIndex = _HpnicfDot11RoamTrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 3, 1, 1),
    _HpnicfDot11RoamTrackIndex_Type()
)
hpnicfDot11RoamTrackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackIndex.setStatus("current")
_HpnicfDot11RoamTrackClientMAC_Type = MacAddress
_HpnicfDot11RoamTrackClientMAC_Object = MibTableColumn
hpnicfDot11RoamTrackClientMAC = _HpnicfDot11RoamTrackClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 3, 1, 2),
    _HpnicfDot11RoamTrackClientMAC_Type()
)
hpnicfDot11RoamTrackClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackClientMAC.setStatus("current")
_HpnicfDot11RoamTrackBSSID_Type = MacAddress
_HpnicfDot11RoamTrackBSSID_Object = MibTableColumn
hpnicfDot11RoamTrackBSSID = _HpnicfDot11RoamTrackBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 3, 1, 3),
    _HpnicfDot11RoamTrackBSSID_Type()
)
hpnicfDot11RoamTrackBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackBSSID.setStatus("current")
_HpnicfDot11RoamTrackUpTime_Type = Integer32
_HpnicfDot11RoamTrackUpTime_Object = MibTableColumn
hpnicfDot11RoamTrackUpTime = _HpnicfDot11RoamTrackUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 3, 1, 4),
    _HpnicfDot11RoamTrackUpTime_Type()
)
hpnicfDot11RoamTrackUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackUpTime.setUnits("second")
_HpnicfDot11RoamTrackACIPType_Type = InetAddressType
_HpnicfDot11RoamTrackACIPType_Object = MibTableColumn
hpnicfDot11RoamTrackACIPType = _HpnicfDot11RoamTrackACIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 3, 1, 5),
    _HpnicfDot11RoamTrackACIPType_Type()
)
hpnicfDot11RoamTrackACIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackACIPType.setStatus("current")
_HpnicfDot11RoamTrackACIPAddr_Type = InetAddress
_HpnicfDot11RoamTrackACIPAddr_Object = MibTableColumn
hpnicfDot11RoamTrackACIPAddr = _HpnicfDot11RoamTrackACIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 2, 3, 1, 6),
    _HpnicfDot11RoamTrackACIPAddr_Type()
)
hpnicfDot11RoamTrackACIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RoamTrackACIPAddr.setStatus("current")
_HpnicfDot11RoamStatisGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RoamStatisGroup = _HpnicfDot11RoamStatisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 3)
)
_HpnicfDot11IntraACRoamingSuccCnt_Type = Integer32
_HpnicfDot11IntraACRoamingSuccCnt_Object = MibScalar
hpnicfDot11IntraACRoamingSuccCnt = _HpnicfDot11IntraACRoamingSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 3, 1),
    _HpnicfDot11IntraACRoamingSuccCnt_Type()
)
hpnicfDot11IntraACRoamingSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11IntraACRoamingSuccCnt.setStatus("current")
_HpnicfDot11InterACRoamingSuccCnt_Type = Integer32
_HpnicfDot11InterACRoamingSuccCnt_Object = MibScalar
hpnicfDot11InterACRoamingSuccCnt = _HpnicfDot11InterACRoamingSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 3, 2),
    _HpnicfDot11InterACRoamingSuccCnt_Type()
)
hpnicfDot11InterACRoamingSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11InterACRoamingSuccCnt.setStatus("current")
_HpnicfDot11InterACRoamOutSuccCnt_Type = Integer32
_HpnicfDot11InterACRoamOutSuccCnt_Object = MibScalar
hpnicfDot11InterACRoamOutSuccCnt = _HpnicfDot11InterACRoamOutSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 3, 3),
    _HpnicfDot11InterACRoamOutSuccCnt_Type()
)
hpnicfDot11InterACRoamOutSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11InterACRoamOutSuccCnt.setStatus("current")
_HpnicfDot11RoamStatis2Group_ObjectIdentity = ObjectIdentity
hpnicfDot11RoamStatis2Group = _HpnicfDot11RoamStatis2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 4)
)
_HpnicfDot11IntraACRoamingSuccCnt2_Type = Counter32
_HpnicfDot11IntraACRoamingSuccCnt2_Object = MibScalar
hpnicfDot11IntraACRoamingSuccCnt2 = _HpnicfDot11IntraACRoamingSuccCnt2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 4, 1),
    _HpnicfDot11IntraACRoamingSuccCnt2_Type()
)
hpnicfDot11IntraACRoamingSuccCnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11IntraACRoamingSuccCnt2.setStatus("current")
_HpnicfDot11InterACRoamingSuccCnt2_Type = Counter32
_HpnicfDot11InterACRoamingSuccCnt2_Object = MibScalar
hpnicfDot11InterACRoamingSuccCnt2 = _HpnicfDot11InterACRoamingSuccCnt2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 4, 2),
    _HpnicfDot11InterACRoamingSuccCnt2_Type()
)
hpnicfDot11InterACRoamingSuccCnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11InterACRoamingSuccCnt2.setStatus("current")
_HpnicfDot11InterACRoamOutSuccCnt2_Type = Counter32
_HpnicfDot11InterACRoamOutSuccCnt2_Object = MibScalar
hpnicfDot11InterACRoamOutSuccCnt2 = _HpnicfDot11InterACRoamOutSuccCnt2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 10, 4, 3),
    _HpnicfDot11InterACRoamOutSuccCnt2_Type()
)
hpnicfDot11InterACRoamOutSuccCnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11InterACRoamOutSuccCnt2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-ROAM-MIB",
    **{"HpnicfDot11RoamMobileTunnelType": HpnicfDot11RoamMobileTunnelType,
       "HpnicfDot11RoamAuthMode": HpnicfDot11RoamAuthMode,
       "HpnicfDot11RoamIACTPStatus": HpnicfDot11RoamIACTPStatus,
       "hpnicfDot11ROAM": hpnicfDot11ROAM,
       "hpnicfDot11RoamCfgGroup": hpnicfDot11RoamCfgGroup,
       "hpnicfDot11MobGrpTable": hpnicfDot11MobGrpTable,
       "hpnicfDot11MobGrpEntry": hpnicfDot11MobGrpEntry,
       "hpnicfDot11MobGrpName": hpnicfDot11MobGrpName,
       "hpnicfdot11MobGrpTunnelType": hpnicfdot11MobGrpTunnelType,
       "hpnicfDot11MobGrpSrcIPAddr": hpnicfDot11MobGrpSrcIPAddr,
       "hpnicfDot11MobGrpAuthMode": hpnicfDot11MobGrpAuthMode,
       "hpnicfDot11MobGrpAuthKey": hpnicfDot11MobGrpAuthKey,
       "hpnicfDot11MobGrpEnable": hpnicfDot11MobGrpEnable,
       "hpnicfDot11MobGrpRowStatus": hpnicfDot11MobGrpRowStatus,
       "hpnicfDot11MobGrpMemberTable": hpnicfDot11MobGrpMemberTable,
       "hpnicfDot11MobGrpMemberEntry": hpnicfDot11MobGrpMemberEntry,
       "hpnicfDot11MobGrpMemberIpAddr": hpnicfDot11MobGrpMemberIpAddr,
       "hpnicfDot11MobGrpMemberStatus": hpnicfDot11MobGrpMemberStatus,
       "hpnicfDot11MobGrpMemberIf": hpnicfDot11MobGrpMemberIf,
       "hpnicfDot11MobGrpMemberUpTime": hpnicfDot11MobGrpMemberUpTime,
       "hpnicfDot11MobGrpMemberRowStatus": hpnicfDot11MobGrpMemberRowStatus,
       "hpnicfDot11RoamStatusGroup": hpnicfDot11RoamStatusGroup,
       "hpnicfDot11RoamInInfoTable": hpnicfDot11RoamInInfoTable,
       "hpnicfDot11RoamInInfoEntry": hpnicfDot11RoamInInfoEntry,
       "hpnicfDot11RoamClientMAC": hpnicfDot11RoamClientMAC,
       "hpnicfDot11RoamInClientBSSID": hpnicfDot11RoamInClientBSSID,
       "hpnicfDot11RoamInClientVlanID": hpnicfDot11RoamInClientVlanID,
       "hpnicfDot11RoamInHomeACIPType": hpnicfDot11RoamInHomeACIPType,
       "hpnicfDot11RoamInHomeACIPAddr": hpnicfDot11RoamInHomeACIPAddr,
       "hpnicfDot11RoamOutInfoTable": hpnicfDot11RoamOutInfoTable,
       "hpnicfDot11RoamOutInfoEntry": hpnicfDot11RoamOutInfoEntry,
       "hpnicfDot11RoamOutClientBSSID": hpnicfDot11RoamOutClientBSSID,
       "hpnicfDot11RoamOutClientVlanID": hpnicfDot11RoamOutClientVlanID,
       "hpnicfDot11RoamOutForeignACIPType": hpnicfDot11RoamOutForeignACIPType,
       "hpnicfDot11RoamOutForeignACIPAddr": hpnicfDot11RoamOutForeignACIPAddr,
       "hpnicfDot11RoamOutClientUpTime": hpnicfDot11RoamOutClientUpTime,
       "hpnicfDot11RoamTrackTable": hpnicfDot11RoamTrackTable,
       "hpnicfDot11RoamTrackEntry": hpnicfDot11RoamTrackEntry,
       "hpnicfDot11RoamTrackIndex": hpnicfDot11RoamTrackIndex,
       "hpnicfDot11RoamTrackClientMAC": hpnicfDot11RoamTrackClientMAC,
       "hpnicfDot11RoamTrackBSSID": hpnicfDot11RoamTrackBSSID,
       "hpnicfDot11RoamTrackUpTime": hpnicfDot11RoamTrackUpTime,
       "hpnicfDot11RoamTrackACIPType": hpnicfDot11RoamTrackACIPType,
       "hpnicfDot11RoamTrackACIPAddr": hpnicfDot11RoamTrackACIPAddr,
       "hpnicfDot11RoamStatisGroup": hpnicfDot11RoamStatisGroup,
       "hpnicfDot11IntraACRoamingSuccCnt": hpnicfDot11IntraACRoamingSuccCnt,
       "hpnicfDot11InterACRoamingSuccCnt": hpnicfDot11InterACRoamingSuccCnt,
       "hpnicfDot11InterACRoamOutSuccCnt": hpnicfDot11InterACRoamOutSuccCnt,
       "hpnicfDot11RoamStatis2Group": hpnicfDot11RoamStatis2Group,
       "hpnicfDot11IntraACRoamingSuccCnt2": hpnicfDot11IntraACRoamingSuccCnt2,
       "hpnicfDot11InterACRoamingSuccCnt2": hpnicfDot11InterACRoamingSuccCnt2,
       "hpnicfDot11InterACRoamOutSuccCnt2": hpnicfDot11InterACRoamOutSuccCnt2}
)
