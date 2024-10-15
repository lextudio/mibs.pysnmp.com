# SNMP MIB module (CISCO-IPSLA-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSLA-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:59 2024
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

(rttMonCtrlAdminIndex,) = mibBuilder.importSymbols(
    "CISCO-RTTMON-MIB",
    "rttMonCtrlAdminIndex")

(RttMonCtrlIndex,
 RttMonIdLst,
 RttMonReactVar,
 RttMonRttType,
 RttResponseSense) = mibBuilder.importSymbols(
    "CISCO-RTTMON-TC-MIB",
    "RttMonCtrlIndex",
    "RttMonIdLst",
    "RttMonReactVar",
    "RttMonRttType",
    "RttResponseSense")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Layer2Cos,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Layer2Cos")

(Dot1agCfmMaintDomainName,
 Dot1agCfmMaintDomainNameType) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMaintDomainName",
    "Dot1agCfmMaintDomainNameType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoIpSlaEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585)
)
ciscoIpSlaEthernetMIB.setRevisions(
        ("2012-05-15 00:00",
         "2008-01-02 00:00",
         "2006-02-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpSlaEthernetMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpSlaEthernetMIBNotifs = _CiscoIpSlaEthernetMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 0)
)
_CiscoIpSlaEthernetMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpSlaEthernetMIBObjects = _CiscoIpSlaEthernetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1)
)
_IpslaEthernetGrpCtrl_ObjectIdentity = ObjectIdentity
ipslaEthernetGrpCtrl = _IpslaEthernetGrpCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1)
)
_IpslaEthernetGrpCtrlTable_Object = MibTable
ipslaEthernetGrpCtrlTable = _IpslaEthernetGrpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlTable.setStatus("current")
_IpslaEthernetGrpCtrlEntry_Object = MibTableRow
ipslaEthernetGrpCtrlEntry = _IpslaEthernetGrpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1)
)
ipslaEthernetGrpCtrlEntry.setIndexNames(
    (0, "CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlIndex"),
)
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlEntry.setStatus("current")
_IpslaEthernetGrpCtrlIndex_Type = RttMonCtrlIndex
_IpslaEthernetGrpCtrlIndex_Object = MibTableColumn
ipslaEthernetGrpCtrlIndex = _IpslaEthernetGrpCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 1),
    _IpslaEthernetGrpCtrlIndex_Type()
)
ipslaEthernetGrpCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlIndex.setStatus("current")
_IpslaEthernetGrpCtrlStatus_Type = RowStatus
_IpslaEthernetGrpCtrlStatus_Object = MibTableColumn
ipslaEthernetGrpCtrlStatus = _IpslaEthernetGrpCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 2),
    _IpslaEthernetGrpCtrlStatus_Type()
)
ipslaEthernetGrpCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlStatus.setStatus("current")


class _IpslaEthernetGrpCtrlStorageType_Type(StorageType):
    """Custom type ipslaEthernetGrpCtrlStorageType based on StorageType"""


_IpslaEthernetGrpCtrlStorageType_Object = MibTableColumn
ipslaEthernetGrpCtrlStorageType = _IpslaEthernetGrpCtrlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 3),
    _IpslaEthernetGrpCtrlStorageType_Type()
)
ipslaEthernetGrpCtrlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlStorageType.setStatus("current")
_IpslaEthernetGrpCtrlRttType_Type = RttMonRttType
_IpslaEthernetGrpCtrlRttType_Object = MibTableColumn
ipslaEthernetGrpCtrlRttType = _IpslaEthernetGrpCtrlRttType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 4),
    _IpslaEthernetGrpCtrlRttType_Type()
)
ipslaEthernetGrpCtrlRttType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlRttType.setStatus("current")


class _IpslaEthernetGrpCtrlOwner_Type(SnmpAdminString):
    """Custom type ipslaEthernetGrpCtrlOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpslaEthernetGrpCtrlOwner_Type.__name__ = "SnmpAdminString"
_IpslaEthernetGrpCtrlOwner_Object = MibTableColumn
ipslaEthernetGrpCtrlOwner = _IpslaEthernetGrpCtrlOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 5),
    _IpslaEthernetGrpCtrlOwner_Type()
)
ipslaEthernetGrpCtrlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlOwner.setStatus("current")


class _IpslaEthernetGrpCtrlTag_Type(SnmpAdminString):
    """Custom type ipslaEthernetGrpCtrlTag based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpslaEthernetGrpCtrlTag_Type.__name__ = "SnmpAdminString"
_IpslaEthernetGrpCtrlTag_Object = MibTableColumn
ipslaEthernetGrpCtrlTag = _IpslaEthernetGrpCtrlTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 6),
    _IpslaEthernetGrpCtrlTag_Type()
)
ipslaEthernetGrpCtrlTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlTag.setStatus("current")


class _IpslaEthernetGrpCtrlThreshold_Type(Unsigned32):
    """Custom type ipslaEthernetGrpCtrlThreshold based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpslaEthernetGrpCtrlThreshold_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpCtrlThreshold_Object = MibTableColumn
ipslaEthernetGrpCtrlThreshold = _IpslaEthernetGrpCtrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 7),
    _IpslaEthernetGrpCtrlThreshold_Type()
)
ipslaEthernetGrpCtrlThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlThreshold.setUnits("milliseconds")


class _IpslaEthernetGrpCtrlTimeout_Type(Unsigned32):
    """Custom type ipslaEthernetGrpCtrlTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_IpslaEthernetGrpCtrlTimeout_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpCtrlTimeout_Object = MibTableColumn
ipslaEthernetGrpCtrlTimeout = _IpslaEthernetGrpCtrlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 8),
    _IpslaEthernetGrpCtrlTimeout_Type()
)
ipslaEthernetGrpCtrlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlTimeout.setUnits("milliseconds")
_IpslaEthernetGrpCtrlProbeList_Type = RttMonIdLst
_IpslaEthernetGrpCtrlProbeList_Object = MibTableColumn
ipslaEthernetGrpCtrlProbeList = _IpslaEthernetGrpCtrlProbeList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 9),
    _IpslaEthernetGrpCtrlProbeList_Type()
)
ipslaEthernetGrpCtrlProbeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlProbeList.setStatus("current")
_IpslaEthernetGrpCtrlVLAN_Type = VlanId
_IpslaEthernetGrpCtrlVLAN_Object = MibTableColumn
ipslaEthernetGrpCtrlVLAN = _IpslaEthernetGrpCtrlVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 10),
    _IpslaEthernetGrpCtrlVLAN_Type()
)
ipslaEthernetGrpCtrlVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlVLAN.setStatus("current")


class _IpslaEthernetGrpCtrlDomainNameType_Type(Dot1agCfmMaintDomainNameType):
    """Custom type ipslaEthernetGrpCtrlDomainNameType based on Dot1agCfmMaintDomainNameType"""


_IpslaEthernetGrpCtrlDomainNameType_Object = MibTableColumn
ipslaEthernetGrpCtrlDomainNameType = _IpslaEthernetGrpCtrlDomainNameType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 11),
    _IpslaEthernetGrpCtrlDomainNameType_Type()
)
ipslaEthernetGrpCtrlDomainNameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlDomainNameType.setStatus("current")
_IpslaEthernetGrpCtrlDomainName_Type = Dot1agCfmMaintDomainName
_IpslaEthernetGrpCtrlDomainName_Object = MibTableColumn
ipslaEthernetGrpCtrlDomainName = _IpslaEthernetGrpCtrlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 12),
    _IpslaEthernetGrpCtrlDomainName_Type()
)
ipslaEthernetGrpCtrlDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlDomainName.setStatus("current")


class _IpslaEthernetGrpCtrlReqDataSize_Type(Unsigned32):
    """Custom type ipslaEthernetGrpCtrlReqDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_IpslaEthernetGrpCtrlReqDataSize_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpCtrlReqDataSize_Object = MibTableColumn
ipslaEthernetGrpCtrlReqDataSize = _IpslaEthernetGrpCtrlReqDataSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 13),
    _IpslaEthernetGrpCtrlReqDataSize_Type()
)
ipslaEthernetGrpCtrlReqDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlReqDataSize.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlReqDataSize.setUnits("octets")
_IpslaEthernetGrpCtrlMPIDExLst_Type = RttMonIdLst
_IpslaEthernetGrpCtrlMPIDExLst_Object = MibTableColumn
ipslaEthernetGrpCtrlMPIDExLst = _IpslaEthernetGrpCtrlMPIDExLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 14),
    _IpslaEthernetGrpCtrlMPIDExLst_Type()
)
ipslaEthernetGrpCtrlMPIDExLst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlMPIDExLst.setStatus("current")


class _IpslaEthernetGrpCtrlCOS_Type(Layer2Cos):
    """Custom type ipslaEthernetGrpCtrlCOS based on Layer2Cos"""
    defaultValue = 0


_IpslaEthernetGrpCtrlCOS_Object = MibTableColumn
ipslaEthernetGrpCtrlCOS = _IpslaEthernetGrpCtrlCOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 15),
    _IpslaEthernetGrpCtrlCOS_Type()
)
ipslaEthernetGrpCtrlCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlCOS.setStatus("current")


class _IpslaEthernetGrpCtrlInterval_Type(Unsigned32):
    """Custom type ipslaEthernetGrpCtrlInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_IpslaEthernetGrpCtrlInterval_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpCtrlInterval_Object = MibTableColumn
ipslaEthernetGrpCtrlInterval = _IpslaEthernetGrpCtrlInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 16),
    _IpslaEthernetGrpCtrlInterval_Type()
)
ipslaEthernetGrpCtrlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlInterval.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlInterval.setUnits("milliseconds")


class _IpslaEthernetGrpCtrlNumFrames_Type(Unsigned32):
    """Custom type ipslaEthernetGrpCtrlNumFrames based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_IpslaEthernetGrpCtrlNumFrames_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpCtrlNumFrames_Object = MibTableColumn
ipslaEthernetGrpCtrlNumFrames = _IpslaEthernetGrpCtrlNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 17),
    _IpslaEthernetGrpCtrlNumFrames_Type()
)
ipslaEthernetGrpCtrlNumFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlNumFrames.setStatus("current")


class _IpslaEthernetGrpScheduleRttStartTime_Type(TimeTicks):
    """Custom type ipslaEthernetGrpScheduleRttStartTime based on TimeTicks"""
    defaultValue = 0


_IpslaEthernetGrpScheduleRttStartTime_Object = MibTableColumn
ipslaEthernetGrpScheduleRttStartTime = _IpslaEthernetGrpScheduleRttStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 18),
    _IpslaEthernetGrpScheduleRttStartTime_Type()
)
ipslaEthernetGrpScheduleRttStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpScheduleRttStartTime.setStatus("current")


class _IpslaEthernetGrpSchedulePeriod_Type(Unsigned32):
    """Custom type ipslaEthernetGrpSchedulePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_IpslaEthernetGrpSchedulePeriod_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpSchedulePeriod_Object = MibTableColumn
ipslaEthernetGrpSchedulePeriod = _IpslaEthernetGrpSchedulePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 19),
    _IpslaEthernetGrpSchedulePeriod_Type()
)
ipslaEthernetGrpSchedulePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpSchedulePeriod.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEthernetGrpSchedulePeriod.setUnits("seconds")


class _IpslaEthernetGrpScheduleFrequency_Type(Unsigned32):
    """Custom type ipslaEthernetGrpScheduleFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_IpslaEthernetGrpScheduleFrequency_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpScheduleFrequency_Object = MibTableColumn
ipslaEthernetGrpScheduleFrequency = _IpslaEthernetGrpScheduleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 20),
    _IpslaEthernetGrpScheduleFrequency_Type()
)
ipslaEthernetGrpScheduleFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpScheduleFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEthernetGrpScheduleFrequency.setUnits("seconds")


class _IpslaEthernetGrpCtrlEVC_Type(SnmpAdminString):
    """Custom type ipslaEthernetGrpCtrlEVC based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_IpslaEthernetGrpCtrlEVC_Type.__name__ = "SnmpAdminString"
_IpslaEthernetGrpCtrlEVC_Object = MibTableColumn
ipslaEthernetGrpCtrlEVC = _IpslaEthernetGrpCtrlEVC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 21),
    _IpslaEthernetGrpCtrlEVC_Type()
)
ipslaEthernetGrpCtrlEVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlEVC.setStatus("current")


class _IpslaEthernetGrpCtrlServiceInsType_Type(Integer32):
    """Custom type ipslaEthernetGrpCtrlServiceInsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("evc", 2),
          ("vlan", 1))
    )


_IpslaEthernetGrpCtrlServiceInsType_Type.__name__ = "Integer32"
_IpslaEthernetGrpCtrlServiceInsType_Object = MibTableColumn
ipslaEthernetGrpCtrlServiceInsType = _IpslaEthernetGrpCtrlServiceInsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 1, 1, 22),
    _IpslaEthernetGrpCtrlServiceInsType_Type()
)
ipslaEthernetGrpCtrlServiceInsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpCtrlServiceInsType.setStatus("current")
_IpslaEthernetGrpReactTable_Object = MibTable
ipslaEthernetGrpReactTable = _IpslaEthernetGrpReactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactTable.setStatus("current")
_IpslaEthernetGrpReactEntry_Object = MibTableRow
ipslaEthernetGrpReactEntry = _IpslaEthernetGrpReactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1)
)
ipslaEthernetGrpReactEntry.setIndexNames(
    (0, "CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlIndex"),
    (0, "CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactConfigIndex"),
)
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactEntry.setStatus("current")
_IpslaEthernetGrpReactConfigIndex_Type = RttMonCtrlIndex
_IpslaEthernetGrpReactConfigIndex_Object = MibTableColumn
ipslaEthernetGrpReactConfigIndex = _IpslaEthernetGrpReactConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 1),
    _IpslaEthernetGrpReactConfigIndex_Type()
)
ipslaEthernetGrpReactConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactConfigIndex.setStatus("current")
_IpslaEthernetGrpReactStatus_Type = RowStatus
_IpslaEthernetGrpReactStatus_Object = MibTableColumn
ipslaEthernetGrpReactStatus = _IpslaEthernetGrpReactStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 2),
    _IpslaEthernetGrpReactStatus_Type()
)
ipslaEthernetGrpReactStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactStatus.setStatus("current")


class _IpslaEthernetGrpReactStorageType_Type(StorageType):
    """Custom type ipslaEthernetGrpReactStorageType based on StorageType"""


_IpslaEthernetGrpReactStorageType_Object = MibTableColumn
ipslaEthernetGrpReactStorageType = _IpslaEthernetGrpReactStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 3),
    _IpslaEthernetGrpReactStorageType_Type()
)
ipslaEthernetGrpReactStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactStorageType.setStatus("current")
_IpslaEthernetGrpReactVar_Type = RttMonReactVar
_IpslaEthernetGrpReactVar_Object = MibTableColumn
ipslaEthernetGrpReactVar = _IpslaEthernetGrpReactVar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 4),
    _IpslaEthernetGrpReactVar_Type()
)
ipslaEthernetGrpReactVar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactVar.setStatus("current")


class _IpslaEthernetGrpReactThresholdType_Type(Integer32):
    """Custom type ipslaEthernetGrpReactThresholdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("average", 5),
          ("consecutive", 3),
          ("immediate", 2),
          ("never", 1),
          ("xOfy", 4))
    )


_IpslaEthernetGrpReactThresholdType_Type.__name__ = "Integer32"
_IpslaEthernetGrpReactThresholdType_Object = MibTableColumn
ipslaEthernetGrpReactThresholdType = _IpslaEthernetGrpReactThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 5),
    _IpslaEthernetGrpReactThresholdType_Type()
)
ipslaEthernetGrpReactThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactThresholdType.setStatus("current")


class _IpslaEthernetGrpReactThresholdRising_Type(Unsigned32):
    """Custom type ipslaEthernetGrpReactThresholdRising based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpslaEthernetGrpReactThresholdRising_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpReactThresholdRising_Object = MibTableColumn
ipslaEthernetGrpReactThresholdRising = _IpslaEthernetGrpReactThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 6),
    _IpslaEthernetGrpReactThresholdRising_Type()
)
ipslaEthernetGrpReactThresholdRising.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactThresholdRising.setStatus("current")


class _IpslaEthernetGrpReactThresholdFalling_Type(Unsigned32):
    """Custom type ipslaEthernetGrpReactThresholdFalling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpslaEthernetGrpReactThresholdFalling_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpReactThresholdFalling_Object = MibTableColumn
ipslaEthernetGrpReactThresholdFalling = _IpslaEthernetGrpReactThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 7),
    _IpslaEthernetGrpReactThresholdFalling_Type()
)
ipslaEthernetGrpReactThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactThresholdFalling.setStatus("current")


class _IpslaEthernetGrpReactThresholdCountX_Type(Unsigned32):
    """Custom type ipslaEthernetGrpReactThresholdCountX based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IpslaEthernetGrpReactThresholdCountX_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpReactThresholdCountX_Object = MibTableColumn
ipslaEthernetGrpReactThresholdCountX = _IpslaEthernetGrpReactThresholdCountX_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 8),
    _IpslaEthernetGrpReactThresholdCountX_Type()
)
ipslaEthernetGrpReactThresholdCountX.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactThresholdCountX.setStatus("current")


class _IpslaEthernetGrpReactThresholdCountY_Type(Unsigned32):
    """Custom type ipslaEthernetGrpReactThresholdCountY based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IpslaEthernetGrpReactThresholdCountY_Type.__name__ = "Unsigned32"
_IpslaEthernetGrpReactThresholdCountY_Object = MibTableColumn
ipslaEthernetGrpReactThresholdCountY = _IpslaEthernetGrpReactThresholdCountY_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 9),
    _IpslaEthernetGrpReactThresholdCountY_Type()
)
ipslaEthernetGrpReactThresholdCountY.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactThresholdCountY.setStatus("current")


class _IpslaEthernetGrpReactActionType_Type(Integer32):
    """Custom type ipslaEthernetGrpReactActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("notification", 2))
    )


_IpslaEthernetGrpReactActionType_Type.__name__ = "Integer32"
_IpslaEthernetGrpReactActionType_Object = MibTableColumn
ipslaEthernetGrpReactActionType = _IpslaEthernetGrpReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 1, 2, 1, 10),
    _IpslaEthernetGrpReactActionType_Type()
)
ipslaEthernetGrpReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipslaEthernetGrpReactActionType.setStatus("current")
_IpslaEthernetStats_ObjectIdentity = ObjectIdentity
ipslaEthernetStats = _IpslaEthernetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2)
)
_IpslaEtherJitterAggStatsTable_Object = MibTable
ipslaEtherJitterAggStatsTable = _IpslaEtherJitterAggStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipslaEtherJitterAggStatsTable.setStatus("current")
_IpslaEtherJitterAggStatsEntry_Object = MibTableRow
ipslaEtherJitterAggStatsEntry = _IpslaEtherJitterAggStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1)
)
ipslaEtherJitterAggStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggStatsStartTimeId"),
)
if mibBuilder.loadTexts:
    ipslaEtherJitterAggStatsEntry.setStatus("current")
_IpslaEtherJAggStatsStartTimeId_Type = TimeStamp
_IpslaEtherJAggStatsStartTimeId_Object = MibTableColumn
ipslaEtherJAggStatsStartTimeId = _IpslaEtherJAggStatsStartTimeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 1),
    _IpslaEtherJAggStatsStartTimeId_Type()
)
ipslaEtherJAggStatsStartTimeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipslaEtherJAggStatsStartTimeId.setStatus("current")
_IpslaEtherJAggMeasuredCmpletions_Type = Counter32
_IpslaEtherJAggMeasuredCmpletions_Object = MibTableColumn
ipslaEtherJAggMeasuredCmpletions = _IpslaEtherJAggMeasuredCmpletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 2),
    _IpslaEtherJAggMeasuredCmpletions_Type()
)
ipslaEtherJAggMeasuredCmpletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCmpletions.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCmpletions.setUnits("completions")
_IpslaEtherJAggMeasuredOvThrshlds_Type = Counter32
_IpslaEtherJAggMeasuredOvThrshlds_Object = MibTableColumn
ipslaEtherJAggMeasuredOvThrshlds = _IpslaEtherJAggMeasuredOvThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 3),
    _IpslaEtherJAggMeasuredOvThrshlds_Type()
)
ipslaEtherJAggMeasuredOvThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOvThrshlds.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOvThrshlds.setUnits("operations")
_IpslaEtherJAggMeasuredNumRTTs_Type = Counter32
_IpslaEtherJAggMeasuredNumRTTs_Object = MibTableColumn
ipslaEtherJAggMeasuredNumRTTs = _IpslaEtherJAggMeasuredNumRTTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 4),
    _IpslaEtherJAggMeasuredNumRTTs_Type()
)
ipslaEtherJAggMeasuredNumRTTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumRTTs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumRTTs.setUnits("frames")
_IpslaEtherJAggMeasuredRTTSums_Type = Counter32
_IpslaEtherJAggMeasuredRTTSums_Object = MibTableColumn
ipslaEtherJAggMeasuredRTTSums = _IpslaEtherJAggMeasuredRTTSums_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 5),
    _IpslaEtherJAggMeasuredRTTSums_Type()
)
ipslaEtherJAggMeasuredRTTSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTSums.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTSums.setUnits("milliseconds")
_IpslaEtherJAggMeasuredRTTSum2Ls_Type = Counter32
_IpslaEtherJAggMeasuredRTTSum2Ls_Object = MibTableColumn
ipslaEtherJAggMeasuredRTTSum2Ls = _IpslaEtherJAggMeasuredRTTSum2Ls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 6),
    _IpslaEtherJAggMeasuredRTTSum2Ls_Type()
)
ipslaEtherJAggMeasuredRTTSum2Ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTSum2Ls.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTSum2Ls.setUnits("milliseconds")
_IpslaEtherJAggMeasuredRTTSum2Hs_Type = Counter32
_IpslaEtherJAggMeasuredRTTSum2Hs_Object = MibTableColumn
ipslaEtherJAggMeasuredRTTSum2Hs = _IpslaEtherJAggMeasuredRTTSum2Hs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 7),
    _IpslaEtherJAggMeasuredRTTSum2Hs_Type()
)
ipslaEtherJAggMeasuredRTTSum2Hs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTSum2Hs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTSum2Hs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredRTTMin_Type = Gauge32
_IpslaEtherJAggMeasuredRTTMin_Object = MibTableColumn
ipslaEtherJAggMeasuredRTTMin = _IpslaEtherJAggMeasuredRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 8),
    _IpslaEtherJAggMeasuredRTTMin_Type()
)
ipslaEtherJAggMeasuredRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTMin.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTMin.setUnits("milliseconds")
_IpslaEtherJAggMeasuredRTTMax_Type = Gauge32
_IpslaEtherJAggMeasuredRTTMax_Object = MibTableColumn
ipslaEtherJAggMeasuredRTTMax = _IpslaEtherJAggMeasuredRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 9),
    _IpslaEtherJAggMeasuredRTTMax_Type()
)
ipslaEtherJAggMeasuredRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTMax.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRTTMax.setUnits("milliseconds")
_IpslaEtherJAggMeasuredMinPosSD_Type = Gauge32
_IpslaEtherJAggMeasuredMinPosSD_Object = MibTableColumn
ipslaEtherJAggMeasuredMinPosSD = _IpslaEtherJAggMeasuredMinPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 10),
    _IpslaEtherJAggMeasuredMinPosSD_Type()
)
ipslaEtherJAggMeasuredMinPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinPosSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinPosSD.setUnits("milliseconds")
_IpslaEtherJAggMeasuredMaxPosSD_Type = Gauge32
_IpslaEtherJAggMeasuredMaxPosSD_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxPosSD = _IpslaEtherJAggMeasuredMaxPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 11),
    _IpslaEtherJAggMeasuredMaxPosSD_Type()
)
ipslaEtherJAggMeasuredMaxPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxPosSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxPosSD.setUnits("milliseconds")
_IpslaEtherJAggMeasuredNumPosSDs_Type = Counter32
_IpslaEtherJAggMeasuredNumPosSDs_Object = MibTableColumn
ipslaEtherJAggMeasuredNumPosSDs = _IpslaEtherJAggMeasuredNumPosSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 12),
    _IpslaEtherJAggMeasuredNumPosSDs_Type()
)
ipslaEtherJAggMeasuredNumPosSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumPosSDs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumPosSDs.setUnits("occurrences")
_IpslaEtherJAggMeasuredSumPosSDs_Type = Counter32
_IpslaEtherJAggMeasuredSumPosSDs_Object = MibTableColumn
ipslaEtherJAggMeasuredSumPosSDs = _IpslaEtherJAggMeasuredSumPosSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 13),
    _IpslaEtherJAggMeasuredSumPosSDs_Type()
)
ipslaEtherJAggMeasuredSumPosSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSumPosSDs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSumPosSDs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredSum2PSDLs_Type = Counter32
_IpslaEtherJAggMeasuredSum2PSDLs_Object = MibTableColumn
ipslaEtherJAggMeasuredSum2PSDLs = _IpslaEtherJAggMeasuredSum2PSDLs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 14),
    _IpslaEtherJAggMeasuredSum2PSDLs_Type()
)
ipslaEtherJAggMeasuredSum2PSDLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2PSDLs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2PSDLs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredSum2PSDHs_Type = Counter32
_IpslaEtherJAggMeasuredSum2PSDHs_Object = MibTableColumn
ipslaEtherJAggMeasuredSum2PSDHs = _IpslaEtherJAggMeasuredSum2PSDHs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 15),
    _IpslaEtherJAggMeasuredSum2PSDHs_Type()
)
ipslaEtherJAggMeasuredSum2PSDHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2PSDHs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2PSDHs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredMinNegSD_Type = Gauge32
_IpslaEtherJAggMeasuredMinNegSD_Object = MibTableColumn
ipslaEtherJAggMeasuredMinNegSD = _IpslaEtherJAggMeasuredMinNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 16),
    _IpslaEtherJAggMeasuredMinNegSD_Type()
)
ipslaEtherJAggMeasuredMinNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinNegSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinNegSD.setUnits("milliseconds")
_IpslaEtherJAggMeasuredMaxNegSD_Type = Gauge32
_IpslaEtherJAggMeasuredMaxNegSD_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxNegSD = _IpslaEtherJAggMeasuredMaxNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 17),
    _IpslaEtherJAggMeasuredMaxNegSD_Type()
)
ipslaEtherJAggMeasuredMaxNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxNegSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxNegSD.setUnits("milliseconds")
_IpslaEtherJAggMeasuredNumNegSDs_Type = Counter32
_IpslaEtherJAggMeasuredNumNegSDs_Object = MibTableColumn
ipslaEtherJAggMeasuredNumNegSDs = _IpslaEtherJAggMeasuredNumNegSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 18),
    _IpslaEtherJAggMeasuredNumNegSDs_Type()
)
ipslaEtherJAggMeasuredNumNegSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumNegSDs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumNegSDs.setUnits("occurrences")
_IpslaEtherJAggMeasuredSumNegSDs_Type = Counter32
_IpslaEtherJAggMeasuredSumNegSDs_Object = MibTableColumn
ipslaEtherJAggMeasuredSumNegSDs = _IpslaEtherJAggMeasuredSumNegSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 19),
    _IpslaEtherJAggMeasuredSumNegSDs_Type()
)
ipslaEtherJAggMeasuredSumNegSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSumNegSDs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSumNegSDs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredSum2NSDLs_Type = Counter32
_IpslaEtherJAggMeasuredSum2NSDLs_Object = MibTableColumn
ipslaEtherJAggMeasuredSum2NSDLs = _IpslaEtherJAggMeasuredSum2NSDLs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 20),
    _IpslaEtherJAggMeasuredSum2NSDLs_Type()
)
ipslaEtherJAggMeasuredSum2NSDLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2NSDLs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2NSDLs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredSum2NSDHs_Type = Counter32
_IpslaEtherJAggMeasuredSum2NSDHs_Object = MibTableColumn
ipslaEtherJAggMeasuredSum2NSDHs = _IpslaEtherJAggMeasuredSum2NSDHs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 21),
    _IpslaEtherJAggMeasuredSum2NSDHs_Type()
)
ipslaEtherJAggMeasuredSum2NSDHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2NSDHs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2NSDHs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredMinPosDS_Type = Gauge32
_IpslaEtherJAggMeasuredMinPosDS_Object = MibTableColumn
ipslaEtherJAggMeasuredMinPosDS = _IpslaEtherJAggMeasuredMinPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 22),
    _IpslaEtherJAggMeasuredMinPosDS_Type()
)
ipslaEtherJAggMeasuredMinPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinPosDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinPosDS.setUnits("milliseconds")
_IpslaEtherJAggMeasuredMaxPosDS_Type = Gauge32
_IpslaEtherJAggMeasuredMaxPosDS_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxPosDS = _IpslaEtherJAggMeasuredMaxPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 23),
    _IpslaEtherJAggMeasuredMaxPosDS_Type()
)
ipslaEtherJAggMeasuredMaxPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxPosDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxPosDS.setUnits("milliseconds")
_IpslaEtherJAggMeasuredNumPosDSes_Type = Counter32
_IpslaEtherJAggMeasuredNumPosDSes_Object = MibTableColumn
ipslaEtherJAggMeasuredNumPosDSes = _IpslaEtherJAggMeasuredNumPosDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 24),
    _IpslaEtherJAggMeasuredNumPosDSes_Type()
)
ipslaEtherJAggMeasuredNumPosDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumPosDSes.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumPosDSes.setUnits("occurrences")
_IpslaEtherJAggMeasuredSumPosDSes_Type = Counter32
_IpslaEtherJAggMeasuredSumPosDSes_Object = MibTableColumn
ipslaEtherJAggMeasuredSumPosDSes = _IpslaEtherJAggMeasuredSumPosDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 25),
    _IpslaEtherJAggMeasuredSumPosDSes_Type()
)
ipslaEtherJAggMeasuredSumPosDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSumPosDSes.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSumPosDSes.setUnits("milliseconds")
_IpslaEtherJAggMeasuredSum2PDSLs_Type = Counter32
_IpslaEtherJAggMeasuredSum2PDSLs_Object = MibTableColumn
ipslaEtherJAggMeasuredSum2PDSLs = _IpslaEtherJAggMeasuredSum2PDSLs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 26),
    _IpslaEtherJAggMeasuredSum2PDSLs_Type()
)
ipslaEtherJAggMeasuredSum2PDSLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2PDSLs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2PDSLs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredSum2PDSHs_Type = Counter32
_IpslaEtherJAggMeasuredSum2PDSHs_Object = MibTableColumn
ipslaEtherJAggMeasuredSum2PDSHs = _IpslaEtherJAggMeasuredSum2PDSHs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 27),
    _IpslaEtherJAggMeasuredSum2PDSHs_Type()
)
ipslaEtherJAggMeasuredSum2PDSHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2PDSHs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2PDSHs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredMinNegDS_Type = Gauge32
_IpslaEtherJAggMeasuredMinNegDS_Object = MibTableColumn
ipslaEtherJAggMeasuredMinNegDS = _IpslaEtherJAggMeasuredMinNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 28),
    _IpslaEtherJAggMeasuredMinNegDS_Type()
)
ipslaEtherJAggMeasuredMinNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinNegDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinNegDS.setUnits("milliseconds")
_IpslaEtherJAggMeasuredMaxNegDS_Type = Gauge32
_IpslaEtherJAggMeasuredMaxNegDS_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxNegDS = _IpslaEtherJAggMeasuredMaxNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 29),
    _IpslaEtherJAggMeasuredMaxNegDS_Type()
)
ipslaEtherJAggMeasuredMaxNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxNegDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxNegDS.setUnits("milliseconds")
_IpslaEtherJAggMeasuredNumNegDSes_Type = Counter32
_IpslaEtherJAggMeasuredNumNegDSes_Object = MibTableColumn
ipslaEtherJAggMeasuredNumNegDSes = _IpslaEtherJAggMeasuredNumNegDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 30),
    _IpslaEtherJAggMeasuredNumNegDSes_Type()
)
ipslaEtherJAggMeasuredNumNegDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumNegDSes.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumNegDSes.setUnits("occurrences")
_IpslaEtherJAggMeasuredSumNegDSes_Type = Counter32
_IpslaEtherJAggMeasuredSumNegDSes_Object = MibTableColumn
ipslaEtherJAggMeasuredSumNegDSes = _IpslaEtherJAggMeasuredSumNegDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 31),
    _IpslaEtherJAggMeasuredSumNegDSes_Type()
)
ipslaEtherJAggMeasuredSumNegDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSumNegDSes.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSumNegDSes.setUnits("milliseconds")
_IpslaEtherJAggMeasuredSum2NDSLs_Type = Counter32
_IpslaEtherJAggMeasuredSum2NDSLs_Object = MibTableColumn
ipslaEtherJAggMeasuredSum2NDSLs = _IpslaEtherJAggMeasuredSum2NDSLs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 32),
    _IpslaEtherJAggMeasuredSum2NDSLs_Type()
)
ipslaEtherJAggMeasuredSum2NDSLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2NDSLs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2NDSLs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredSum2NDSHs_Type = Counter32
_IpslaEtherJAggMeasuredSum2NDSHs_Object = MibTableColumn
ipslaEtherJAggMeasuredSum2NDSHs = _IpslaEtherJAggMeasuredSum2NDSHs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 33),
    _IpslaEtherJAggMeasuredSum2NDSHs_Type()
)
ipslaEtherJAggMeasuredSum2NDSHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2NDSHs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredSum2NDSHs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredFrmLossSDs_Type = Counter32
_IpslaEtherJAggMeasuredFrmLossSDs_Object = MibTableColumn
ipslaEtherJAggMeasuredFrmLossSDs = _IpslaEtherJAggMeasuredFrmLossSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 34),
    _IpslaEtherJAggMeasuredFrmLossSDs_Type()
)
ipslaEtherJAggMeasuredFrmLossSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmLossSDs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmLossSDs.setUnits("frames")
_IpslaEtherJAggMeasuredFrmLssDSes_Type = Counter32
_IpslaEtherJAggMeasuredFrmLssDSes_Object = MibTableColumn
ipslaEtherJAggMeasuredFrmLssDSes = _IpslaEtherJAggMeasuredFrmLssDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 35),
    _IpslaEtherJAggMeasuredFrmLssDSes_Type()
)
ipslaEtherJAggMeasuredFrmLssDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmLssDSes.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmLssDSes.setUnits("frames")
_IpslaEtherJAggMeasuredFrmOutSeqs_Type = Counter32
_IpslaEtherJAggMeasuredFrmOutSeqs_Object = MibTableColumn
ipslaEtherJAggMeasuredFrmOutSeqs = _IpslaEtherJAggMeasuredFrmOutSeqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 36),
    _IpslaEtherJAggMeasuredFrmOutSeqs_Type()
)
ipslaEtherJAggMeasuredFrmOutSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmOutSeqs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmOutSeqs.setUnits("frames")
_IpslaEtherJAggMeasuredFrmMIAes_Type = Counter32
_IpslaEtherJAggMeasuredFrmMIAes_Object = MibTableColumn
ipslaEtherJAggMeasuredFrmMIAes = _IpslaEtherJAggMeasuredFrmMIAes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 37),
    _IpslaEtherJAggMeasuredFrmMIAes_Type()
)
ipslaEtherJAggMeasuredFrmMIAes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmMIAes.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmMIAes.setUnits("frames")
_IpslaEtherJAggMeasuredFrmSkippds_Type = Counter32
_IpslaEtherJAggMeasuredFrmSkippds_Object = MibTableColumn
ipslaEtherJAggMeasuredFrmSkippds = _IpslaEtherJAggMeasuredFrmSkippds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 38),
    _IpslaEtherJAggMeasuredFrmSkippds_Type()
)
ipslaEtherJAggMeasuredFrmSkippds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmSkippds.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmSkippds.setUnits("frames")
_IpslaEtherJAggMeasuredErrors_Type = Counter32
_IpslaEtherJAggMeasuredErrors_Object = MibTableColumn
ipslaEtherJAggMeasuredErrors = _IpslaEtherJAggMeasuredErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 39),
    _IpslaEtherJAggMeasuredErrors_Type()
)
ipslaEtherJAggMeasuredErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredErrors.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredErrors.setUnits("errors")
_IpslaEtherJAggMeasuredBusies_Type = Counter32
_IpslaEtherJAggMeasuredBusies_Object = MibTableColumn
ipslaEtherJAggMeasuredBusies = _IpslaEtherJAggMeasuredBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 40),
    _IpslaEtherJAggMeasuredBusies_Type()
)
ipslaEtherJAggMeasuredBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredBusies.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredBusies.setUnits("busies")
_IpslaEtherJAggMeasuredOWSumSDs_Type = Counter32
_IpslaEtherJAggMeasuredOWSumSDs_Object = MibTableColumn
ipslaEtherJAggMeasuredOWSumSDs = _IpslaEtherJAggMeasuredOWSumSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 41),
    _IpslaEtherJAggMeasuredOWSumSDs_Type()
)
ipslaEtherJAggMeasuredOWSumSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSumSDs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSumSDs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWSum2SDLs_Type = Counter32
_IpslaEtherJAggMeasuredOWSum2SDLs_Object = MibTableColumn
ipslaEtherJAggMeasuredOWSum2SDLs = _IpslaEtherJAggMeasuredOWSum2SDLs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 42),
    _IpslaEtherJAggMeasuredOWSum2SDLs_Type()
)
ipslaEtherJAggMeasuredOWSum2SDLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSum2SDLs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSum2SDLs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWSum2SDHs_Type = Counter32
_IpslaEtherJAggMeasuredOWSum2SDHs_Object = MibTableColumn
ipslaEtherJAggMeasuredOWSum2SDHs = _IpslaEtherJAggMeasuredOWSum2SDHs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 43),
    _IpslaEtherJAggMeasuredOWSum2SDHs_Type()
)
ipslaEtherJAggMeasuredOWSum2SDHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSum2SDHs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSum2SDHs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWMinSD_Type = Gauge32
_IpslaEtherJAggMeasuredOWMinSD_Object = MibTableColumn
ipslaEtherJAggMeasuredOWMinSD = _IpslaEtherJAggMeasuredOWMinSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 44),
    _IpslaEtherJAggMeasuredOWMinSD_Type()
)
ipslaEtherJAggMeasuredOWMinSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWMinSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWMinSD.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWMaxSD_Type = Gauge32
_IpslaEtherJAggMeasuredOWMaxSD_Object = MibTableColumn
ipslaEtherJAggMeasuredOWMaxSD = _IpslaEtherJAggMeasuredOWMaxSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 45),
    _IpslaEtherJAggMeasuredOWMaxSD_Type()
)
ipslaEtherJAggMeasuredOWMaxSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWMaxSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWMaxSD.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWSumDSes_Type = Counter32
_IpslaEtherJAggMeasuredOWSumDSes_Object = MibTableColumn
ipslaEtherJAggMeasuredOWSumDSes = _IpslaEtherJAggMeasuredOWSumDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 46),
    _IpslaEtherJAggMeasuredOWSumDSes_Type()
)
ipslaEtherJAggMeasuredOWSumDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSumDSes.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSumDSes.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWSum2DSLs_Type = Counter32
_IpslaEtherJAggMeasuredOWSum2DSLs_Object = MibTableColumn
ipslaEtherJAggMeasuredOWSum2DSLs = _IpslaEtherJAggMeasuredOWSum2DSLs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 47),
    _IpslaEtherJAggMeasuredOWSum2DSLs_Type()
)
ipslaEtherJAggMeasuredOWSum2DSLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSum2DSLs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSum2DSLs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWSum2DSHs_Type = Counter32
_IpslaEtherJAggMeasuredOWSum2DSHs_Object = MibTableColumn
ipslaEtherJAggMeasuredOWSum2DSHs = _IpslaEtherJAggMeasuredOWSum2DSHs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 48),
    _IpslaEtherJAggMeasuredOWSum2DSHs_Type()
)
ipslaEtherJAggMeasuredOWSum2DSHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSum2DSHs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWSum2DSHs.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWMinDS_Type = Gauge32
_IpslaEtherJAggMeasuredOWMinDS_Object = MibTableColumn
ipslaEtherJAggMeasuredOWMinDS = _IpslaEtherJAggMeasuredOWMinDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 49),
    _IpslaEtherJAggMeasuredOWMinDS_Type()
)
ipslaEtherJAggMeasuredOWMinDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWMinDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWMinDS.setUnits("milliseconds")
_IpslaEtherJAggMeasuredOWMaxDS_Type = Gauge32
_IpslaEtherJAggMeasuredOWMaxDS_Object = MibTableColumn
ipslaEtherJAggMeasuredOWMaxDS = _IpslaEtherJAggMeasuredOWMaxDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 50),
    _IpslaEtherJAggMeasuredOWMaxDS_Type()
)
ipslaEtherJAggMeasuredOWMaxDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWMaxDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredOWMaxDS.setUnits("milliseconds")
_IpslaEtherJAggMeasuredNumOWs_Type = Counter32
_IpslaEtherJAggMeasuredNumOWs_Object = MibTableColumn
ipslaEtherJAggMeasuredNumOWs = _IpslaEtherJAggMeasuredNumOWs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 51),
    _IpslaEtherJAggMeasuredNumOWs_Type()
)
ipslaEtherJAggMeasuredNumOWs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumOWs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredNumOWs.setUnits("frames")
_IpslaEtherJAggMeasuredAvgJ_Type = Gauge32
_IpslaEtherJAggMeasuredAvgJ_Object = MibTableColumn
ipslaEtherJAggMeasuredAvgJ = _IpslaEtherJAggMeasuredAvgJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 52),
    _IpslaEtherJAggMeasuredAvgJ_Type()
)
ipslaEtherJAggMeasuredAvgJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgJ.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgJ.setUnits("milliseconds")
_IpslaEtherJAggMeasuredAvgJSD_Type = Gauge32
_IpslaEtherJAggMeasuredAvgJSD_Object = MibTableColumn
ipslaEtherJAggMeasuredAvgJSD = _IpslaEtherJAggMeasuredAvgJSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 53),
    _IpslaEtherJAggMeasuredAvgJSD_Type()
)
ipslaEtherJAggMeasuredAvgJSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgJSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgJSD.setUnits("milliseconds")
_IpslaEtherJAggMeasuredAvgJDS_Type = Gauge32
_IpslaEtherJAggMeasuredAvgJDS_Object = MibTableColumn
ipslaEtherJAggMeasuredAvgJDS = _IpslaEtherJAggMeasuredAvgJDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 54),
    _IpslaEtherJAggMeasuredAvgJDS_Type()
)
ipslaEtherJAggMeasuredAvgJDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgJDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgJDS.setUnits("milliseconds")
_IpslaEtherJAggMinSucFrmLoss_Type = Gauge32
_IpslaEtherJAggMinSucFrmLoss_Object = MibTableColumn
ipslaEtherJAggMinSucFrmLoss = _IpslaEtherJAggMinSucFrmLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 55),
    _IpslaEtherJAggMinSucFrmLoss_Type()
)
ipslaEtherJAggMinSucFrmLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMinSucFrmLoss.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMinSucFrmLoss.setUnits("frames")
_IpslaEtherJAggMaxSucFrmLoss_Type = Gauge32
_IpslaEtherJAggMaxSucFrmLoss_Object = MibTableColumn
ipslaEtherJAggMaxSucFrmLoss = _IpslaEtherJAggMaxSucFrmLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 56),
    _IpslaEtherJAggMaxSucFrmLoss_Type()
)
ipslaEtherJAggMaxSucFrmLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMaxSucFrmLoss.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMaxSucFrmLoss.setUnits("frames")
_IpslaEtherJAggMeasuredIAJOut_Type = Gauge32
_IpslaEtherJAggMeasuredIAJOut_Object = MibTableColumn
ipslaEtherJAggMeasuredIAJOut = _IpslaEtherJAggMeasuredIAJOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 57),
    _IpslaEtherJAggMeasuredIAJOut_Type()
)
ipslaEtherJAggMeasuredIAJOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredIAJOut.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredIAJOut.setUnits("milliseconds")
_IpslaEtherJAggMeasuredIAJIn_Type = Gauge32
_IpslaEtherJAggMeasuredIAJIn_Object = MibTableColumn
ipslaEtherJAggMeasuredIAJIn = _IpslaEtherJAggMeasuredIAJIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 58),
    _IpslaEtherJAggMeasuredIAJIn_Type()
)
ipslaEtherJAggMeasuredIAJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredIAJIn.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredIAJIn.setUnits("milliseconds")
_IpslaEtherJAggMeasuredFrmLateAs_Type = Counter32
_IpslaEtherJAggMeasuredFrmLateAs_Object = MibTableColumn
ipslaEtherJAggMeasuredFrmLateAs = _IpslaEtherJAggMeasuredFrmLateAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 59),
    _IpslaEtherJAggMeasuredFrmLateAs_Type()
)
ipslaEtherJAggMeasuredFrmLateAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmLateAs.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmLateAs.setUnits("frames")
_IpslaEtherJAggMeasuredFrmUnPrcds_Type = Counter32
_IpslaEtherJAggMeasuredFrmUnPrcds_Object = MibTableColumn
ipslaEtherJAggMeasuredFrmUnPrcds = _IpslaEtherJAggMeasuredFrmUnPrcds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 60),
    _IpslaEtherJAggMeasuredFrmUnPrcds_Type()
)
ipslaEtherJAggMeasuredFrmUnPrcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmUnPrcds.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredFrmUnPrcds.setUnits("frames")
_IpslaEtherJAggMeasuredMaxPosTW_Type = Gauge32
_IpslaEtherJAggMeasuredMaxPosTW_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxPosTW = _IpslaEtherJAggMeasuredMaxPosTW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 61),
    _IpslaEtherJAggMeasuredMaxPosTW_Type()
)
ipslaEtherJAggMeasuredMaxPosTW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxPosTW.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxPosTW.setUnits("microseconds")
_IpslaEtherJAggMeasuredMaxNegTW_Type = Gauge32
_IpslaEtherJAggMeasuredMaxNegTW_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxNegTW = _IpslaEtherJAggMeasuredMaxNegTW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 62),
    _IpslaEtherJAggMeasuredMaxNegTW_Type()
)
ipslaEtherJAggMeasuredMaxNegTW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxNegTW.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxNegTW.setUnits("microseconds")
_IpslaEtherJAggMeasuredMinPosTW_Type = Gauge32
_IpslaEtherJAggMeasuredMinPosTW_Object = MibTableColumn
ipslaEtherJAggMeasuredMinPosTW = _IpslaEtherJAggMeasuredMinPosTW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 63),
    _IpslaEtherJAggMeasuredMinPosTW_Type()
)
ipslaEtherJAggMeasuredMinPosTW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinPosTW.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinPosTW.setUnits("microseconds")
_IpslaEtherJAggMeasuredMinNegTW_Type = Gauge32
_IpslaEtherJAggMeasuredMinNegTW_Object = MibTableColumn
ipslaEtherJAggMeasuredMinNegTW = _IpslaEtherJAggMeasuredMinNegTW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 64),
    _IpslaEtherJAggMeasuredMinNegTW_Type()
)
ipslaEtherJAggMeasuredMinNegTW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinNegTW.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinNegTW.setUnits("microseconds")
_IpslaEtherJAggMeasuredTxFrmsSD_Type = Counter64
_IpslaEtherJAggMeasuredTxFrmsSD_Object = MibTableColumn
ipslaEtherJAggMeasuredTxFrmsSD = _IpslaEtherJAggMeasuredTxFrmsSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 65),
    _IpslaEtherJAggMeasuredTxFrmsSD_Type()
)
ipslaEtherJAggMeasuredTxFrmsSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredTxFrmsSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredTxFrmsSD.setUnits("frames")
_IpslaEtherJAggMeasuredTxFrmsDS_Type = Counter64
_IpslaEtherJAggMeasuredTxFrmsDS_Object = MibTableColumn
ipslaEtherJAggMeasuredTxFrmsDS = _IpslaEtherJAggMeasuredTxFrmsDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 66),
    _IpslaEtherJAggMeasuredTxFrmsDS_Type()
)
ipslaEtherJAggMeasuredTxFrmsDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredTxFrmsDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredTxFrmsDS.setUnits("frames")
_IpslaEtherJAggMeasuredRxFrmsSD_Type = Counter64
_IpslaEtherJAggMeasuredRxFrmsSD_Object = MibTableColumn
ipslaEtherJAggMeasuredRxFrmsSD = _IpslaEtherJAggMeasuredRxFrmsSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 67),
    _IpslaEtherJAggMeasuredRxFrmsSD_Type()
)
ipslaEtherJAggMeasuredRxFrmsSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRxFrmsSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRxFrmsSD.setUnits("frames")
_IpslaEtherJAggMeasuredRxFrmsDS_Type = Counter64
_IpslaEtherJAggMeasuredRxFrmsDS_Object = MibTableColumn
ipslaEtherJAggMeasuredRxFrmsDS = _IpslaEtherJAggMeasuredRxFrmsDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 68),
    _IpslaEtherJAggMeasuredRxFrmsDS_Type()
)
ipslaEtherJAggMeasuredRxFrmsDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRxFrmsDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredRxFrmsDS.setUnits("frames")
_IpslaEtherJAggMeasuredMinLossNumeratorSD_Type = Gauge32
_IpslaEtherJAggMeasuredMinLossNumeratorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredMinLossNumeratorSD = _IpslaEtherJAggMeasuredMinLossNumeratorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 69),
    _IpslaEtherJAggMeasuredMinLossNumeratorSD_Type()
)
ipslaEtherJAggMeasuredMinLossNumeratorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinLossNumeratorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinLossNumeratorSD.setUnits("frames")
_IpslaEtherJAggMeasuredMinLossDenominatorSD_Type = Gauge32
_IpslaEtherJAggMeasuredMinLossDenominatorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredMinLossDenominatorSD = _IpslaEtherJAggMeasuredMinLossDenominatorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 70),
    _IpslaEtherJAggMeasuredMinLossDenominatorSD_Type()
)
ipslaEtherJAggMeasuredMinLossDenominatorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinLossDenominatorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinLossDenominatorSD.setUnits("frames")
_IpslaEtherJAggMeasuredMaxLossNumeratorSD_Type = Gauge32
_IpslaEtherJAggMeasuredMaxLossNumeratorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxLossNumeratorSD = _IpslaEtherJAggMeasuredMaxLossNumeratorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 71),
    _IpslaEtherJAggMeasuredMaxLossNumeratorSD_Type()
)
ipslaEtherJAggMeasuredMaxLossNumeratorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxLossNumeratorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxLossNumeratorSD.setUnits("frames")
_IpslaEtherJAggMeasuredMaxLossDenominatorSD_Type = Gauge32
_IpslaEtherJAggMeasuredMaxLossDenominatorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxLossDenominatorSD = _IpslaEtherJAggMeasuredMaxLossDenominatorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 72),
    _IpslaEtherJAggMeasuredMaxLossDenominatorSD_Type()
)
ipslaEtherJAggMeasuredMaxLossDenominatorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxLossDenominatorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxLossDenominatorSD.setUnits("frames")
_IpslaEtherJAggMeasuredAvgLossNumeratorSD_Type = Gauge32
_IpslaEtherJAggMeasuredAvgLossNumeratorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredAvgLossNumeratorSD = _IpslaEtherJAggMeasuredAvgLossNumeratorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 73),
    _IpslaEtherJAggMeasuredAvgLossNumeratorSD_Type()
)
ipslaEtherJAggMeasuredAvgLossNumeratorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgLossNumeratorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgLossNumeratorSD.setUnits("frames")
_IpslaEtherJAggMeasuredAvgLossDenominatorSD_Type = Gauge32
_IpslaEtherJAggMeasuredAvgLossDenominatorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredAvgLossDenominatorSD = _IpslaEtherJAggMeasuredAvgLossDenominatorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 74),
    _IpslaEtherJAggMeasuredAvgLossDenominatorSD_Type()
)
ipslaEtherJAggMeasuredAvgLossDenominatorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgLossDenominatorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgLossDenominatorSD.setUnits("frames")
_IpslaEtherJAggMeasuredMinLossNumeratorDS_Type = Gauge32
_IpslaEtherJAggMeasuredMinLossNumeratorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredMinLossNumeratorDS = _IpslaEtherJAggMeasuredMinLossNumeratorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 75),
    _IpslaEtherJAggMeasuredMinLossNumeratorDS_Type()
)
ipslaEtherJAggMeasuredMinLossNumeratorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinLossNumeratorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinLossNumeratorDS.setUnits("frames")
_IpslaEtherJAggMeasuredMinLossDenominatorDS_Type = Gauge32
_IpslaEtherJAggMeasuredMinLossDenominatorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredMinLossDenominatorDS = _IpslaEtherJAggMeasuredMinLossDenominatorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 76),
    _IpslaEtherJAggMeasuredMinLossDenominatorDS_Type()
)
ipslaEtherJAggMeasuredMinLossDenominatorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinLossDenominatorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMinLossDenominatorDS.setUnits("frames")
_IpslaEtherJAggMeasuredMaxLossNumeratorDS_Type = Gauge32
_IpslaEtherJAggMeasuredMaxLossNumeratorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxLossNumeratorDS = _IpslaEtherJAggMeasuredMaxLossNumeratorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 77),
    _IpslaEtherJAggMeasuredMaxLossNumeratorDS_Type()
)
ipslaEtherJAggMeasuredMaxLossNumeratorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxLossNumeratorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxLossNumeratorDS.setUnits("frames")
_IpslaEtherJAggMeasuredMaxLossDenominatorDS_Type = Gauge32
_IpslaEtherJAggMeasuredMaxLossDenominatorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredMaxLossDenominatorDS = _IpslaEtherJAggMeasuredMaxLossDenominatorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 78),
    _IpslaEtherJAggMeasuredMaxLossDenominatorDS_Type()
)
ipslaEtherJAggMeasuredMaxLossDenominatorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxLossDenominatorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredMaxLossDenominatorDS.setUnits("frames")
_IpslaEtherJAggMeasuredAvgLossNumeratorDS_Type = Gauge32
_IpslaEtherJAggMeasuredAvgLossNumeratorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredAvgLossNumeratorDS = _IpslaEtherJAggMeasuredAvgLossNumeratorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 79),
    _IpslaEtherJAggMeasuredAvgLossNumeratorDS_Type()
)
ipslaEtherJAggMeasuredAvgLossNumeratorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgLossNumeratorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgLossNumeratorDS.setUnits("frames")
_IpslaEtherJAggMeasuredAvgLossDenominatorDS_Type = Gauge32
_IpslaEtherJAggMeasuredAvgLossDenominatorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredAvgLossDenominatorDS = _IpslaEtherJAggMeasuredAvgLossDenominatorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 80),
    _IpslaEtherJAggMeasuredAvgLossDenominatorDS_Type()
)
ipslaEtherJAggMeasuredAvgLossDenominatorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgLossDenominatorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredAvgLossDenominatorDS.setUnits("frames")
_IpslaEtherJAggMeasuredCumulativeLossNumeratorSD_Type = Gauge32
_IpslaEtherJAggMeasuredCumulativeLossNumeratorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredCumulativeLossNumeratorSD = _IpslaEtherJAggMeasuredCumulativeLossNumeratorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 81),
    _IpslaEtherJAggMeasuredCumulativeLossNumeratorSD_Type()
)
ipslaEtherJAggMeasuredCumulativeLossNumeratorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeLossNumeratorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeLossNumeratorSD.setUnits("frames")
_IpslaEtherJAggMeasuredCumulativeLossDenominatorSD_Type = Gauge32
_IpslaEtherJAggMeasuredCumulativeLossDenominatorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredCumulativeLossDenominatorSD = _IpslaEtherJAggMeasuredCumulativeLossDenominatorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 82),
    _IpslaEtherJAggMeasuredCumulativeLossDenominatorSD_Type()
)
ipslaEtherJAggMeasuredCumulativeLossDenominatorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeLossDenominatorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeLossDenominatorSD.setUnits("frames")
_IpslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD_Type = Gauge32
_IpslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD = _IpslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 83),
    _IpslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD_Type()
)
ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD.setUnits("frames")
_IpslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD_Type = Gauge32
_IpslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD_Object = MibTableColumn
ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD = _IpslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 84),
    _IpslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD_Type()
)
ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD.setUnits("frames")
_IpslaEtherJAggMeasuredCumulativeLossNumeratorDS_Type = Gauge32
_IpslaEtherJAggMeasuredCumulativeLossNumeratorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredCumulativeLossNumeratorDS = _IpslaEtherJAggMeasuredCumulativeLossNumeratorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 85),
    _IpslaEtherJAggMeasuredCumulativeLossNumeratorDS_Type()
)
ipslaEtherJAggMeasuredCumulativeLossNumeratorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeLossNumeratorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeLossNumeratorDS.setUnits("frames")
_IpslaEtherJAggMeasuredCumulativeLossDenominatorDS_Type = Gauge32
_IpslaEtherJAggMeasuredCumulativeLossDenominatorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredCumulativeLossDenominatorDS = _IpslaEtherJAggMeasuredCumulativeLossDenominatorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 86),
    _IpslaEtherJAggMeasuredCumulativeLossDenominatorDS_Type()
)
ipslaEtherJAggMeasuredCumulativeLossDenominatorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeLossDenominatorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeLossDenominatorDS.setUnits("frames")
_IpslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS_Type = Gauge32
_IpslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS = _IpslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 87),
    _IpslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS_Type()
)
ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS.setUnits("frames")
_IpslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS_Type = Gauge32
_IpslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS_Object = MibTableColumn
ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS = _IpslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 2, 1, 1, 88),
    _IpslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS_Type()
)
ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS.setUnits("frames")
_IpslaEthernetLatestOper_ObjectIdentity = ObjectIdentity
ipslaEthernetLatestOper = _IpslaEthernetLatestOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3)
)
_IpslaEtherJitterLatestStatsTable_Object = MibTable
ipslaEtherJitterLatestStatsTable = _IpslaEtherJitterLatestStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestStatsTable.setStatus("current")
_IpslaEtherJitterLatestStatsEntry_Object = MibTableRow
ipslaEtherJitterLatestStatsEntry = _IpslaEtherJitterLatestStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1)
)
ipslaEtherJitterLatestStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestStatsEntry.setStatus("current")
_IpslaEtherJitterLatestNumRTT_Type = Gauge32
_IpslaEtherJitterLatestNumRTT_Object = MibTableColumn
ipslaEtherJitterLatestNumRTT = _IpslaEtherJitterLatestNumRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 1),
    _IpslaEtherJitterLatestNumRTT_Type()
)
ipslaEtherJitterLatestNumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumRTT.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumRTT.setUnits("packets")
_IpslaEtherJitterLatestRTTSum_Type = Gauge32
_IpslaEtherJitterLatestRTTSum_Object = MibTableColumn
ipslaEtherJitterLatestRTTSum = _IpslaEtherJitterLatestRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 2),
    _IpslaEtherJitterLatestRTTSum_Type()
)
ipslaEtherJitterLatestRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestRTTSum.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestRTTSum.setUnits("milliseconds")
_IpslaEtherJitterLatestRTTSum2_Type = Gauge32
_IpslaEtherJitterLatestRTTSum2_Object = MibTableColumn
ipslaEtherJitterLatestRTTSum2 = _IpslaEtherJitterLatestRTTSum2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 3),
    _IpslaEtherJitterLatestRTTSum2_Type()
)
ipslaEtherJitterLatestRTTSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestRTTSum2.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestRTTSum2.setUnits("milliseconds")
_IpslaEtherJitterLatestRTTMin_Type = Gauge32
_IpslaEtherJitterLatestRTTMin_Object = MibTableColumn
ipslaEtherJitterLatestRTTMin = _IpslaEtherJitterLatestRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 4),
    _IpslaEtherJitterLatestRTTMin_Type()
)
ipslaEtherJitterLatestRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestRTTMin.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestRTTMin.setUnits("milliseconds")
_IpslaEtherJitterLatestRTTMax_Type = Gauge32
_IpslaEtherJitterLatestRTTMax_Object = MibTableColumn
ipslaEtherJitterLatestRTTMax = _IpslaEtherJitterLatestRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 5),
    _IpslaEtherJitterLatestRTTMax_Type()
)
ipslaEtherJitterLatestRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestRTTMax.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestRTTMax.setUnits("milliseconds")
_IpslaEtherJitterLatestMinPosSD_Type = Gauge32
_IpslaEtherJitterLatestMinPosSD_Object = MibTableColumn
ipslaEtherJitterLatestMinPosSD = _IpslaEtherJitterLatestMinPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 6),
    _IpslaEtherJitterLatestMinPosSD_Type()
)
ipslaEtherJitterLatestMinPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinPosSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinPosSD.setUnits("milliseconds")
_IpslaEtherJitterLatestMaxPosSD_Type = Gauge32
_IpslaEtherJitterLatestMaxPosSD_Object = MibTableColumn
ipslaEtherJitterLatestMaxPosSD = _IpslaEtherJitterLatestMaxPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 7),
    _IpslaEtherJitterLatestMaxPosSD_Type()
)
ipslaEtherJitterLatestMaxPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxPosSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxPosSD.setUnits("milliseconds")
_IpslaEtherJitterLatestNumPosSD_Type = Gauge32
_IpslaEtherJitterLatestNumPosSD_Object = MibTableColumn
ipslaEtherJitterLatestNumPosSD = _IpslaEtherJitterLatestNumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 8),
    _IpslaEtherJitterLatestNumPosSD_Type()
)
ipslaEtherJitterLatestNumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumPosSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumPosSD.setUnits("occurrences")
_IpslaEtherJitterLatestSumPosSD_Type = Gauge32
_IpslaEtherJitterLatestSumPosSD_Object = MibTableColumn
ipslaEtherJitterLatestSumPosSD = _IpslaEtherJitterLatestSumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 9),
    _IpslaEtherJitterLatestSumPosSD_Type()
)
ipslaEtherJitterLatestSumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSumPosSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSumPosSD.setUnits("milliseconds")
_IpslaEtherJitterLatestSum2PosSD_Type = Gauge32
_IpslaEtherJitterLatestSum2PosSD_Object = MibTableColumn
ipslaEtherJitterLatestSum2PosSD = _IpslaEtherJitterLatestSum2PosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 10),
    _IpslaEtherJitterLatestSum2PosSD_Type()
)
ipslaEtherJitterLatestSum2PosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSum2PosSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSum2PosSD.setUnits("milliseconds")
_IpslaEtherJitterLatestMinNegSD_Type = Gauge32
_IpslaEtherJitterLatestMinNegSD_Object = MibTableColumn
ipslaEtherJitterLatestMinNegSD = _IpslaEtherJitterLatestMinNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 11),
    _IpslaEtherJitterLatestMinNegSD_Type()
)
ipslaEtherJitterLatestMinNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinNegSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinNegSD.setUnits("milliseconds")
_IpslaEtherJitterLatestMaxNegSD_Type = Gauge32
_IpslaEtherJitterLatestMaxNegSD_Object = MibTableColumn
ipslaEtherJitterLatestMaxNegSD = _IpslaEtherJitterLatestMaxNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 12),
    _IpslaEtherJitterLatestMaxNegSD_Type()
)
ipslaEtherJitterLatestMaxNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxNegSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxNegSD.setUnits("milliseconds")
_IpslaEtherJitterLatestNumNegSD_Type = Gauge32
_IpslaEtherJitterLatestNumNegSD_Object = MibTableColumn
ipslaEtherJitterLatestNumNegSD = _IpslaEtherJitterLatestNumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 13),
    _IpslaEtherJitterLatestNumNegSD_Type()
)
ipslaEtherJitterLatestNumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumNegSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumNegSD.setUnits("occurrences")
_IpslaEtherJitterLatestSumNegSD_Type = Gauge32
_IpslaEtherJitterLatestSumNegSD_Object = MibTableColumn
ipslaEtherJitterLatestSumNegSD = _IpslaEtherJitterLatestSumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 14),
    _IpslaEtherJitterLatestSumNegSD_Type()
)
ipslaEtherJitterLatestSumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSumNegSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSumNegSD.setUnits("milliseconds")
_IpslaEtherJitterLatestSum2NegSD_Type = Gauge32
_IpslaEtherJitterLatestSum2NegSD_Object = MibTableColumn
ipslaEtherJitterLatestSum2NegSD = _IpslaEtherJitterLatestSum2NegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 15),
    _IpslaEtherJitterLatestSum2NegSD_Type()
)
ipslaEtherJitterLatestSum2NegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSum2NegSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSum2NegSD.setUnits("milliseconds")
_IpslaEtherJitterLatestMinPosDS_Type = Gauge32
_IpslaEtherJitterLatestMinPosDS_Object = MibTableColumn
ipslaEtherJitterLatestMinPosDS = _IpslaEtherJitterLatestMinPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 16),
    _IpslaEtherJitterLatestMinPosDS_Type()
)
ipslaEtherJitterLatestMinPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinPosDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinPosDS.setUnits("milliseconds")
_IpslaEtherJitterLatestMaxPosDS_Type = Gauge32
_IpslaEtherJitterLatestMaxPosDS_Object = MibTableColumn
ipslaEtherJitterLatestMaxPosDS = _IpslaEtherJitterLatestMaxPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 17),
    _IpslaEtherJitterLatestMaxPosDS_Type()
)
ipslaEtherJitterLatestMaxPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxPosDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxPosDS.setUnits("milliseconds")
_IpslaEtherJitterLatestNumPosDS_Type = Gauge32
_IpslaEtherJitterLatestNumPosDS_Object = MibTableColumn
ipslaEtherJitterLatestNumPosDS = _IpslaEtherJitterLatestNumPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 18),
    _IpslaEtherJitterLatestNumPosDS_Type()
)
ipslaEtherJitterLatestNumPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumPosDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumPosDS.setUnits("occurrences")
_IpslaEtherJitterLatestSumPosDS_Type = Gauge32
_IpslaEtherJitterLatestSumPosDS_Object = MibTableColumn
ipslaEtherJitterLatestSumPosDS = _IpslaEtherJitterLatestSumPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 19),
    _IpslaEtherJitterLatestSumPosDS_Type()
)
ipslaEtherJitterLatestSumPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSumPosDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSumPosDS.setUnits("milliseconds")
_IpslaEtherJitterLatestSum2PosDS_Type = Gauge32
_IpslaEtherJitterLatestSum2PosDS_Object = MibTableColumn
ipslaEtherJitterLatestSum2PosDS = _IpslaEtherJitterLatestSum2PosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 20),
    _IpslaEtherJitterLatestSum2PosDS_Type()
)
ipslaEtherJitterLatestSum2PosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSum2PosDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSum2PosDS.setUnits("milliseconds")
_IpslaEtherJitterLatestMinNegDS_Type = Gauge32
_IpslaEtherJitterLatestMinNegDS_Object = MibTableColumn
ipslaEtherJitterLatestMinNegDS = _IpslaEtherJitterLatestMinNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 21),
    _IpslaEtherJitterLatestMinNegDS_Type()
)
ipslaEtherJitterLatestMinNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinNegDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinNegDS.setUnits("milliseconds")
_IpslaEtherJitterLatestMaxNegDS_Type = Gauge32
_IpslaEtherJitterLatestMaxNegDS_Object = MibTableColumn
ipslaEtherJitterLatestMaxNegDS = _IpslaEtherJitterLatestMaxNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 22),
    _IpslaEtherJitterLatestMaxNegDS_Type()
)
ipslaEtherJitterLatestMaxNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxNegDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxNegDS.setUnits("milliseconds")
_IpslaEtherJitterLatestNumNegDS_Type = Gauge32
_IpslaEtherJitterLatestNumNegDS_Object = MibTableColumn
ipslaEtherJitterLatestNumNegDS = _IpslaEtherJitterLatestNumNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 23),
    _IpslaEtherJitterLatestNumNegDS_Type()
)
ipslaEtherJitterLatestNumNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumNegDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumNegDS.setUnits("occurrences")
_IpslaEtherJitterLatestSumNegDS_Type = Gauge32
_IpslaEtherJitterLatestSumNegDS_Object = MibTableColumn
ipslaEtherJitterLatestSumNegDS = _IpslaEtherJitterLatestSumNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 24),
    _IpslaEtherJitterLatestSumNegDS_Type()
)
ipslaEtherJitterLatestSumNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSumNegDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSumNegDS.setUnits("milliseconds")
_IpslaEtherJitterLatestSum2NegDS_Type = Gauge32
_IpslaEtherJitterLatestSum2NegDS_Object = MibTableColumn
ipslaEtherJitterLatestSum2NegDS = _IpslaEtherJitterLatestSum2NegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 25),
    _IpslaEtherJitterLatestSum2NegDS_Type()
)
ipslaEtherJitterLatestSum2NegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSum2NegDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSum2NegDS.setUnits("milliseconds")
_IpslaEtherJitterLatestFrmLossSD_Type = Gauge32
_IpslaEtherJitterLatestFrmLossSD_Object = MibTableColumn
ipslaEtherJitterLatestFrmLossSD = _IpslaEtherJitterLatestFrmLossSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 26),
    _IpslaEtherJitterLatestFrmLossSD_Type()
)
ipslaEtherJitterLatestFrmLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmLossSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmLossSD.setUnits("frames")
_IpslaEtherJitterLatestFrmLossDS_Type = Gauge32
_IpslaEtherJitterLatestFrmLossDS_Object = MibTableColumn
ipslaEtherJitterLatestFrmLossDS = _IpslaEtherJitterLatestFrmLossDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 27),
    _IpslaEtherJitterLatestFrmLossDS_Type()
)
ipslaEtherJitterLatestFrmLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmLossDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmLossDS.setUnits("frames")
_IpslaEtherJitterLatestFrmOutSeq_Type = Gauge32
_IpslaEtherJitterLatestFrmOutSeq_Object = MibTableColumn
ipslaEtherJitterLatestFrmOutSeq = _IpslaEtherJitterLatestFrmOutSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 28),
    _IpslaEtherJitterLatestFrmOutSeq_Type()
)
ipslaEtherJitterLatestFrmOutSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmOutSeq.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmOutSeq.setUnits("packets")
_IpslaEtherJitterLatestFrmMIA_Type = Gauge32
_IpslaEtherJitterLatestFrmMIA_Object = MibTableColumn
ipslaEtherJitterLatestFrmMIA = _IpslaEtherJitterLatestFrmMIA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 29),
    _IpslaEtherJitterLatestFrmMIA_Type()
)
ipslaEtherJitterLatestFrmMIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmMIA.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmMIA.setUnits("frames")
_IpslaEtherJitterLatestFrmSkipped_Type = Gauge32
_IpslaEtherJitterLatestFrmSkipped_Object = MibTableColumn
ipslaEtherJitterLatestFrmSkipped = _IpslaEtherJitterLatestFrmSkipped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 30),
    _IpslaEtherJitterLatestFrmSkipped_Type()
)
ipslaEtherJitterLatestFrmSkipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmSkipped.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmSkipped.setUnits("frames")
_IpslaEtherJitterLatestSense_Type = RttResponseSense
_IpslaEtherJitterLatestSense_Object = MibTableColumn
ipslaEtherJitterLatestSense = _IpslaEtherJitterLatestSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 31),
    _IpslaEtherJitterLatestSense_Type()
)
ipslaEtherJitterLatestSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestSense.setStatus("current")
_IpslaEtherJitterLatestFrmLateA_Type = Gauge32
_IpslaEtherJitterLatestFrmLateA_Object = MibTableColumn
ipslaEtherJitterLatestFrmLateA = _IpslaEtherJitterLatestFrmLateA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 32),
    _IpslaEtherJitterLatestFrmLateA_Type()
)
ipslaEtherJitterLatestFrmLateA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmLateA.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestFrmLateA.setUnits("frames")
_IpslaEtherJitterLatestMinSucFrmL_Type = Gauge32
_IpslaEtherJitterLatestMinSucFrmL_Object = MibTableColumn
ipslaEtherJitterLatestMinSucFrmL = _IpslaEtherJitterLatestMinSucFrmL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 33),
    _IpslaEtherJitterLatestMinSucFrmL_Type()
)
ipslaEtherJitterLatestMinSucFrmL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinSucFrmL.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMinSucFrmL.setUnits("frames")
_IpslaEtherJitterLatestMaxSucFrmL_Type = Gauge32
_IpslaEtherJitterLatestMaxSucFrmL_Object = MibTableColumn
ipslaEtherJitterLatestMaxSucFrmL = _IpslaEtherJitterLatestMaxSucFrmL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 34),
    _IpslaEtherJitterLatestMaxSucFrmL_Type()
)
ipslaEtherJitterLatestMaxSucFrmL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxSucFrmL.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestMaxSucFrmL.setUnits("frames")
_IpslaEtherJitterLatestOWSumSD_Type = Gauge32
_IpslaEtherJitterLatestOWSumSD_Object = MibTableColumn
ipslaEtherJitterLatestOWSumSD = _IpslaEtherJitterLatestOWSumSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 35),
    _IpslaEtherJitterLatestOWSumSD_Type()
)
ipslaEtherJitterLatestOWSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWSumSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWSumSD.setUnits("milliseconds")
_IpslaEtherJitterLatestOWSum2SD_Type = Gauge32
_IpslaEtherJitterLatestOWSum2SD_Object = MibTableColumn
ipslaEtherJitterLatestOWSum2SD = _IpslaEtherJitterLatestOWSum2SD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 36),
    _IpslaEtherJitterLatestOWSum2SD_Type()
)
ipslaEtherJitterLatestOWSum2SD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWSum2SD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWSum2SD.setUnits("milliseconds")
_IpslaEtherJitterLatestOWMinSD_Type = Gauge32
_IpslaEtherJitterLatestOWMinSD_Object = MibTableColumn
ipslaEtherJitterLatestOWMinSD = _IpslaEtherJitterLatestOWMinSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 37),
    _IpslaEtherJitterLatestOWMinSD_Type()
)
ipslaEtherJitterLatestOWMinSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWMinSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWMinSD.setUnits("milliseconds")
_IpslaEtherJitterLatestOWMaxSD_Type = Gauge32
_IpslaEtherJitterLatestOWMaxSD_Object = MibTableColumn
ipslaEtherJitterLatestOWMaxSD = _IpslaEtherJitterLatestOWMaxSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 38),
    _IpslaEtherJitterLatestOWMaxSD_Type()
)
ipslaEtherJitterLatestOWMaxSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWMaxSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWMaxSD.setUnits("milliseconds")
_IpslaEtherJitterLatestOWSumDS_Type = Gauge32
_IpslaEtherJitterLatestOWSumDS_Object = MibTableColumn
ipslaEtherJitterLatestOWSumDS = _IpslaEtherJitterLatestOWSumDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 39),
    _IpslaEtherJitterLatestOWSumDS_Type()
)
ipslaEtherJitterLatestOWSumDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWSumDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWSumDS.setUnits("milliseconds")
_IpslaEtherJitterLatestOWSum2DS_Type = Gauge32
_IpslaEtherJitterLatestOWSum2DS_Object = MibTableColumn
ipslaEtherJitterLatestOWSum2DS = _IpslaEtherJitterLatestOWSum2DS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 40),
    _IpslaEtherJitterLatestOWSum2DS_Type()
)
ipslaEtherJitterLatestOWSum2DS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWSum2DS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWSum2DS.setUnits("milliseconds")
_IpslaEtherJitterLatestOWMinDS_Type = Gauge32
_IpslaEtherJitterLatestOWMinDS_Object = MibTableColumn
ipslaEtherJitterLatestOWMinDS = _IpslaEtherJitterLatestOWMinDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 41),
    _IpslaEtherJitterLatestOWMinDS_Type()
)
ipslaEtherJitterLatestOWMinDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWMinDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWMinDS.setUnits("milliseconds")
_IpslaEtherJitterLatestOWMaxDS_Type = Gauge32
_IpslaEtherJitterLatestOWMaxDS_Object = MibTableColumn
ipslaEtherJitterLatestOWMaxDS = _IpslaEtherJitterLatestOWMaxDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 42),
    _IpslaEtherJitterLatestOWMaxDS_Type()
)
ipslaEtherJitterLatestOWMaxDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWMaxDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWMaxDS.setUnits("milliseconds")
_IpslaEtherJitterLatestNumOW_Type = Gauge32
_IpslaEtherJitterLatestNumOW_Object = MibTableColumn
ipslaEtherJitterLatestNumOW = _IpslaEtherJitterLatestNumOW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 43),
    _IpslaEtherJitterLatestNumOW_Type()
)
ipslaEtherJitterLatestNumOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumOW.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestNumOW.setUnits("frames")
_IpslaEtherJitterLatestAvgJitter_Type = Gauge32
_IpslaEtherJitterLatestAvgJitter_Object = MibTableColumn
ipslaEtherJitterLatestAvgJitter = _IpslaEtherJitterLatestAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 44),
    _IpslaEtherJitterLatestAvgJitter_Type()
)
ipslaEtherJitterLatestAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestAvgJitter.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestAvgJitter.setUnits("milliseconds")
_IpslaEtherJitterLatestAvgSDJ_Type = Gauge32
_IpslaEtherJitterLatestAvgSDJ_Object = MibTableColumn
ipslaEtherJitterLatestAvgSDJ = _IpslaEtherJitterLatestAvgSDJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 45),
    _IpslaEtherJitterLatestAvgSDJ_Type()
)
ipslaEtherJitterLatestAvgSDJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestAvgSDJ.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestAvgSDJ.setUnits("milliseconds")
_IpslaEtherJitterLatestAvgDSJ_Type = Gauge32
_IpslaEtherJitterLatestAvgDSJ_Object = MibTableColumn
ipslaEtherJitterLatestAvgDSJ = _IpslaEtherJitterLatestAvgDSJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 46),
    _IpslaEtherJitterLatestAvgDSJ_Type()
)
ipslaEtherJitterLatestAvgDSJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestAvgDSJ.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestAvgDSJ.setUnits("milliseconds")
_IpslaEtherJitterLatestOWAvgSD_Type = Gauge32
_IpslaEtherJitterLatestOWAvgSD_Object = MibTableColumn
ipslaEtherJitterLatestOWAvgSD = _IpslaEtherJitterLatestOWAvgSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 47),
    _IpslaEtherJitterLatestOWAvgSD_Type()
)
ipslaEtherJitterLatestOWAvgSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWAvgSD.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWAvgSD.setUnits("milliseconds")
_IpslaEtherJitterLatestOWAvgDS_Type = Gauge32
_IpslaEtherJitterLatestOWAvgDS_Object = MibTableColumn
ipslaEtherJitterLatestOWAvgDS = _IpslaEtherJitterLatestOWAvgDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 48),
    _IpslaEtherJitterLatestOWAvgDS_Type()
)
ipslaEtherJitterLatestOWAvgDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWAvgDS.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestOWAvgDS.setUnits("milliseconds")
_IpslaEtherJitterLatestIAJOut_Type = Gauge32
_IpslaEtherJitterLatestIAJOut_Object = MibTableColumn
ipslaEtherJitterLatestIAJOut = _IpslaEtherJitterLatestIAJOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 49),
    _IpslaEtherJitterLatestIAJOut_Type()
)
ipslaEtherJitterLatestIAJOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestIAJOut.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestIAJOut.setUnits("milliseconds")
_IpslaEtherJitterLatestIAJIn_Type = Gauge32
_IpslaEtherJitterLatestIAJIn_Object = MibTableColumn
ipslaEtherJitterLatestIAJIn = _IpslaEtherJitterLatestIAJIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 50),
    _IpslaEtherJitterLatestIAJIn_Type()
)
ipslaEtherJitterLatestIAJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestIAJIn.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJitterLatestIAJIn.setUnits("milliseconds")
_IpslaEtherJLatestFrmUnProcessed_Type = Gauge32
_IpslaEtherJLatestFrmUnProcessed_Object = MibTableColumn
ipslaEtherJLatestFrmUnProcessed = _IpslaEtherJLatestFrmUnProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 1, 3, 1, 1, 51),
    _IpslaEtherJLatestFrmUnProcessed_Type()
)
ipslaEtherJLatestFrmUnProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipslaEtherJLatestFrmUnProcessed.setStatus("current")
if mibBuilder.loadTexts:
    ipslaEtherJLatestFrmUnProcessed.setUnits("frames")
_CiscoIpSlaEthernetMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpSlaEthernetMIBConform = _CiscoIpSlaEthernetMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2)
)
_CiscoIpSlaEthernetCompliances_ObjectIdentity = ObjectIdentity
ciscoIpSlaEthernetCompliances = _CiscoIpSlaEthernetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 1)
)
_CiscoIpSlaEthernetMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpSlaEthernetMIBGroups = _CiscoIpSlaEthernetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 2)
)

# Managed Objects groups

ciscoIpSlaEthernetAutoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 2, 1)
)
ciscoIpSlaEthernetAutoGroup.setObjects(
      *(("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlStatus"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlStorageType"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlRttType"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlOwner"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlTag"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlThreshold"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlTimeout"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlProbeList"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlVLAN"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlDomainNameType"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlDomainName"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlReqDataSize"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlMPIDExLst"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlCOS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlInterval"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlNumFrames"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactStatus"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactStorageType"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactVar"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactThresholdType"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactThresholdRising"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactThresholdFalling"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactThresholdCountX"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactThresholdCountY"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpReactActionType"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpScheduleRttStartTime"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpSchedulePeriod"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpScheduleFrequency"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaEthernetAutoGroup.setStatus("current")

ciscoIpSlaEthernetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 2, 2)
)
ciscoIpSlaEthernetStatsGroup.setObjects(
      *(("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestNumRTT"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestRTTSum"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestRTTSum2"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestRTTMin"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestRTTMax"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMinPosSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMaxPosSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestNumPosSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSumPosSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSum2PosSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMinNegSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMaxNegSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestNumNegSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSumNegSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSum2NegSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMinPosDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMaxPosDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestNumPosDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSumPosDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSum2PosDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMinNegDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMaxNegDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestNumNegDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSumNegDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSum2NegDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestFrmLossSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestFrmLossDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestFrmOutSeq"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestFrmMIA"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestFrmSkipped"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestSense"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestFrmLateA"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMinSucFrmL"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestMaxSucFrmL"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWSumSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWSum2SD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWMinSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWMaxSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWSumDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWSum2DS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWMinDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWMaxDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestNumOW"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestAvgJitter"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestAvgSDJ"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestAvgDSJ"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWAvgSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestOWAvgDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestIAJOut"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJitterLatestIAJIn"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJLatestFrmUnProcessed"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCmpletions"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOvThrshlds"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredNumRTTs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredRTTSums"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredRTTSum2Ls"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredRTTSum2Hs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredRTTMin"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredRTTMax"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinPosSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxPosSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredNumPosSDs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSumPosSDs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSum2PSDLs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSum2PSDHs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinNegSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxNegSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredNumNegSDs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSumNegSDs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSum2NSDLs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSum2NSDHs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinPosDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxPosDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredNumPosDSes"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSumPosDSes"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSum2PDSLs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSum2PDSHs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinNegDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxNegDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredNumNegDSes"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSumNegDSes"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSum2NDSLs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredSum2NDSHs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredFrmLossSDs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredFrmLssDSes"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredFrmOutSeqs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredFrmMIAes"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredFrmSkippds"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredErrors"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredBusies"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWSumSDs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWSum2SDLs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWSum2SDHs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWMinSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWMaxSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWSumDSes"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWSum2DSLs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWSum2DSHs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWMinDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredOWMaxDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredNumOWs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredAvgJ"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredAvgJSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredAvgJDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMinSucFrmLoss"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMaxSucFrmLoss"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredIAJOut"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredIAJIn"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredFrmLateAs"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredFrmUnPrcds"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaEthernetStatsGroup.setStatus("current")

ciscoIpSlaEthernetAutoEVCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 2, 3)
)
ciscoIpSlaEthernetAutoEVCGroup.setObjects(
      *(("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlEVC"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEthernetGrpCtrlServiceInsType"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaEthernetAutoEVCGroup.setStatus("current")

ciscoIpSlaEthernetY1731Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 2, 4)
)
ciscoIpSlaEthernetY1731Group.setObjects(
      *(("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxPosTW"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxNegTW"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinPosTW"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinNegTW"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredTxFrmsSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredTxFrmsDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredRxFrmsSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredRxFrmsDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinLossNumeratorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinLossDenominatorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxLossNumeratorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxLossDenominatorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredAvgLossNumeratorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredAvgLossDenominatorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinLossNumeratorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMinLossDenominatorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxLossNumeratorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredMaxLossDenominatorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredAvgLossNumeratorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredAvgLossDenominatorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCumulativeLossNumeratorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCumulativeLossDenominatorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCumulativeLossNumeratorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCumulativeLossDenominatorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS"),
        ("CISCO-IPSLA-ETHERNET-MIB", "ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaEthernetY1731Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpSlaEthernetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpSlaEthernetCompliance.setStatus(
        "deprecated"
    )

ciscoIpSlaEthernetComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIpSlaEthernetComplianceRev2.setStatus(
        "deprecated"
    )

ciscoIpSlaEthernetComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 585, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIpSlaEthernetComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSLA-ETHERNET-MIB",
    **{"ciscoIpSlaEthernetMIB": ciscoIpSlaEthernetMIB,
       "ciscoIpSlaEthernetMIBNotifs": ciscoIpSlaEthernetMIBNotifs,
       "ciscoIpSlaEthernetMIBObjects": ciscoIpSlaEthernetMIBObjects,
       "ipslaEthernetGrpCtrl": ipslaEthernetGrpCtrl,
       "ipslaEthernetGrpCtrlTable": ipslaEthernetGrpCtrlTable,
       "ipslaEthernetGrpCtrlEntry": ipslaEthernetGrpCtrlEntry,
       "ipslaEthernetGrpCtrlIndex": ipslaEthernetGrpCtrlIndex,
       "ipslaEthernetGrpCtrlStatus": ipslaEthernetGrpCtrlStatus,
       "ipslaEthernetGrpCtrlStorageType": ipslaEthernetGrpCtrlStorageType,
       "ipslaEthernetGrpCtrlRttType": ipslaEthernetGrpCtrlRttType,
       "ipslaEthernetGrpCtrlOwner": ipslaEthernetGrpCtrlOwner,
       "ipslaEthernetGrpCtrlTag": ipslaEthernetGrpCtrlTag,
       "ipslaEthernetGrpCtrlThreshold": ipslaEthernetGrpCtrlThreshold,
       "ipslaEthernetGrpCtrlTimeout": ipslaEthernetGrpCtrlTimeout,
       "ipslaEthernetGrpCtrlProbeList": ipslaEthernetGrpCtrlProbeList,
       "ipslaEthernetGrpCtrlVLAN": ipslaEthernetGrpCtrlVLAN,
       "ipslaEthernetGrpCtrlDomainNameType": ipslaEthernetGrpCtrlDomainNameType,
       "ipslaEthernetGrpCtrlDomainName": ipslaEthernetGrpCtrlDomainName,
       "ipslaEthernetGrpCtrlReqDataSize": ipslaEthernetGrpCtrlReqDataSize,
       "ipslaEthernetGrpCtrlMPIDExLst": ipslaEthernetGrpCtrlMPIDExLst,
       "ipslaEthernetGrpCtrlCOS": ipslaEthernetGrpCtrlCOS,
       "ipslaEthernetGrpCtrlInterval": ipslaEthernetGrpCtrlInterval,
       "ipslaEthernetGrpCtrlNumFrames": ipslaEthernetGrpCtrlNumFrames,
       "ipslaEthernetGrpScheduleRttStartTime": ipslaEthernetGrpScheduleRttStartTime,
       "ipslaEthernetGrpSchedulePeriod": ipslaEthernetGrpSchedulePeriod,
       "ipslaEthernetGrpScheduleFrequency": ipslaEthernetGrpScheduleFrequency,
       "ipslaEthernetGrpCtrlEVC": ipslaEthernetGrpCtrlEVC,
       "ipslaEthernetGrpCtrlServiceInsType": ipslaEthernetGrpCtrlServiceInsType,
       "ipslaEthernetGrpReactTable": ipslaEthernetGrpReactTable,
       "ipslaEthernetGrpReactEntry": ipslaEthernetGrpReactEntry,
       "ipslaEthernetGrpReactConfigIndex": ipslaEthernetGrpReactConfigIndex,
       "ipslaEthernetGrpReactStatus": ipslaEthernetGrpReactStatus,
       "ipslaEthernetGrpReactStorageType": ipslaEthernetGrpReactStorageType,
       "ipslaEthernetGrpReactVar": ipslaEthernetGrpReactVar,
       "ipslaEthernetGrpReactThresholdType": ipslaEthernetGrpReactThresholdType,
       "ipslaEthernetGrpReactThresholdRising": ipslaEthernetGrpReactThresholdRising,
       "ipslaEthernetGrpReactThresholdFalling": ipslaEthernetGrpReactThresholdFalling,
       "ipslaEthernetGrpReactThresholdCountX": ipslaEthernetGrpReactThresholdCountX,
       "ipslaEthernetGrpReactThresholdCountY": ipslaEthernetGrpReactThresholdCountY,
       "ipslaEthernetGrpReactActionType": ipslaEthernetGrpReactActionType,
       "ipslaEthernetStats": ipslaEthernetStats,
       "ipslaEtherJitterAggStatsTable": ipslaEtherJitterAggStatsTable,
       "ipslaEtherJitterAggStatsEntry": ipslaEtherJitterAggStatsEntry,
       "ipslaEtherJAggStatsStartTimeId": ipslaEtherJAggStatsStartTimeId,
       "ipslaEtherJAggMeasuredCmpletions": ipslaEtherJAggMeasuredCmpletions,
       "ipslaEtherJAggMeasuredOvThrshlds": ipslaEtherJAggMeasuredOvThrshlds,
       "ipslaEtherJAggMeasuredNumRTTs": ipslaEtherJAggMeasuredNumRTTs,
       "ipslaEtherJAggMeasuredRTTSums": ipslaEtherJAggMeasuredRTTSums,
       "ipslaEtherJAggMeasuredRTTSum2Ls": ipslaEtherJAggMeasuredRTTSum2Ls,
       "ipslaEtherJAggMeasuredRTTSum2Hs": ipslaEtherJAggMeasuredRTTSum2Hs,
       "ipslaEtherJAggMeasuredRTTMin": ipslaEtherJAggMeasuredRTTMin,
       "ipslaEtherJAggMeasuredRTTMax": ipslaEtherJAggMeasuredRTTMax,
       "ipslaEtherJAggMeasuredMinPosSD": ipslaEtherJAggMeasuredMinPosSD,
       "ipslaEtherJAggMeasuredMaxPosSD": ipslaEtherJAggMeasuredMaxPosSD,
       "ipslaEtherJAggMeasuredNumPosSDs": ipslaEtherJAggMeasuredNumPosSDs,
       "ipslaEtherJAggMeasuredSumPosSDs": ipslaEtherJAggMeasuredSumPosSDs,
       "ipslaEtherJAggMeasuredSum2PSDLs": ipslaEtherJAggMeasuredSum2PSDLs,
       "ipslaEtherJAggMeasuredSum2PSDHs": ipslaEtherJAggMeasuredSum2PSDHs,
       "ipslaEtherJAggMeasuredMinNegSD": ipslaEtherJAggMeasuredMinNegSD,
       "ipslaEtherJAggMeasuredMaxNegSD": ipslaEtherJAggMeasuredMaxNegSD,
       "ipslaEtherJAggMeasuredNumNegSDs": ipslaEtherJAggMeasuredNumNegSDs,
       "ipslaEtherJAggMeasuredSumNegSDs": ipslaEtherJAggMeasuredSumNegSDs,
       "ipslaEtherJAggMeasuredSum2NSDLs": ipslaEtherJAggMeasuredSum2NSDLs,
       "ipslaEtherJAggMeasuredSum2NSDHs": ipslaEtherJAggMeasuredSum2NSDHs,
       "ipslaEtherJAggMeasuredMinPosDS": ipslaEtherJAggMeasuredMinPosDS,
       "ipslaEtherJAggMeasuredMaxPosDS": ipslaEtherJAggMeasuredMaxPosDS,
       "ipslaEtherJAggMeasuredNumPosDSes": ipslaEtherJAggMeasuredNumPosDSes,
       "ipslaEtherJAggMeasuredSumPosDSes": ipslaEtherJAggMeasuredSumPosDSes,
       "ipslaEtherJAggMeasuredSum2PDSLs": ipslaEtherJAggMeasuredSum2PDSLs,
       "ipslaEtherJAggMeasuredSum2PDSHs": ipslaEtherJAggMeasuredSum2PDSHs,
       "ipslaEtherJAggMeasuredMinNegDS": ipslaEtherJAggMeasuredMinNegDS,
       "ipslaEtherJAggMeasuredMaxNegDS": ipslaEtherJAggMeasuredMaxNegDS,
       "ipslaEtherJAggMeasuredNumNegDSes": ipslaEtherJAggMeasuredNumNegDSes,
       "ipslaEtherJAggMeasuredSumNegDSes": ipslaEtherJAggMeasuredSumNegDSes,
       "ipslaEtherJAggMeasuredSum2NDSLs": ipslaEtherJAggMeasuredSum2NDSLs,
       "ipslaEtherJAggMeasuredSum2NDSHs": ipslaEtherJAggMeasuredSum2NDSHs,
       "ipslaEtherJAggMeasuredFrmLossSDs": ipslaEtherJAggMeasuredFrmLossSDs,
       "ipslaEtherJAggMeasuredFrmLssDSes": ipslaEtherJAggMeasuredFrmLssDSes,
       "ipslaEtherJAggMeasuredFrmOutSeqs": ipslaEtherJAggMeasuredFrmOutSeqs,
       "ipslaEtherJAggMeasuredFrmMIAes": ipslaEtherJAggMeasuredFrmMIAes,
       "ipslaEtherJAggMeasuredFrmSkippds": ipslaEtherJAggMeasuredFrmSkippds,
       "ipslaEtherJAggMeasuredErrors": ipslaEtherJAggMeasuredErrors,
       "ipslaEtherJAggMeasuredBusies": ipslaEtherJAggMeasuredBusies,
       "ipslaEtherJAggMeasuredOWSumSDs": ipslaEtherJAggMeasuredOWSumSDs,
       "ipslaEtherJAggMeasuredOWSum2SDLs": ipslaEtherJAggMeasuredOWSum2SDLs,
       "ipslaEtherJAggMeasuredOWSum2SDHs": ipslaEtherJAggMeasuredOWSum2SDHs,
       "ipslaEtherJAggMeasuredOWMinSD": ipslaEtherJAggMeasuredOWMinSD,
       "ipslaEtherJAggMeasuredOWMaxSD": ipslaEtherJAggMeasuredOWMaxSD,
       "ipslaEtherJAggMeasuredOWSumDSes": ipslaEtherJAggMeasuredOWSumDSes,
       "ipslaEtherJAggMeasuredOWSum2DSLs": ipslaEtherJAggMeasuredOWSum2DSLs,
       "ipslaEtherJAggMeasuredOWSum2DSHs": ipslaEtherJAggMeasuredOWSum2DSHs,
       "ipslaEtherJAggMeasuredOWMinDS": ipslaEtherJAggMeasuredOWMinDS,
       "ipslaEtherJAggMeasuredOWMaxDS": ipslaEtherJAggMeasuredOWMaxDS,
       "ipslaEtherJAggMeasuredNumOWs": ipslaEtherJAggMeasuredNumOWs,
       "ipslaEtherJAggMeasuredAvgJ": ipslaEtherJAggMeasuredAvgJ,
       "ipslaEtherJAggMeasuredAvgJSD": ipslaEtherJAggMeasuredAvgJSD,
       "ipslaEtherJAggMeasuredAvgJDS": ipslaEtherJAggMeasuredAvgJDS,
       "ipslaEtherJAggMinSucFrmLoss": ipslaEtherJAggMinSucFrmLoss,
       "ipslaEtherJAggMaxSucFrmLoss": ipslaEtherJAggMaxSucFrmLoss,
       "ipslaEtherJAggMeasuredIAJOut": ipslaEtherJAggMeasuredIAJOut,
       "ipslaEtherJAggMeasuredIAJIn": ipslaEtherJAggMeasuredIAJIn,
       "ipslaEtherJAggMeasuredFrmLateAs": ipslaEtherJAggMeasuredFrmLateAs,
       "ipslaEtherJAggMeasuredFrmUnPrcds": ipslaEtherJAggMeasuredFrmUnPrcds,
       "ipslaEtherJAggMeasuredMaxPosTW": ipslaEtherJAggMeasuredMaxPosTW,
       "ipslaEtherJAggMeasuredMaxNegTW": ipslaEtherJAggMeasuredMaxNegTW,
       "ipslaEtherJAggMeasuredMinPosTW": ipslaEtherJAggMeasuredMinPosTW,
       "ipslaEtherJAggMeasuredMinNegTW": ipslaEtherJAggMeasuredMinNegTW,
       "ipslaEtherJAggMeasuredTxFrmsSD": ipslaEtherJAggMeasuredTxFrmsSD,
       "ipslaEtherJAggMeasuredTxFrmsDS": ipslaEtherJAggMeasuredTxFrmsDS,
       "ipslaEtherJAggMeasuredRxFrmsSD": ipslaEtherJAggMeasuredRxFrmsSD,
       "ipslaEtherJAggMeasuredRxFrmsDS": ipslaEtherJAggMeasuredRxFrmsDS,
       "ipslaEtherJAggMeasuredMinLossNumeratorSD": ipslaEtherJAggMeasuredMinLossNumeratorSD,
       "ipslaEtherJAggMeasuredMinLossDenominatorSD": ipslaEtherJAggMeasuredMinLossDenominatorSD,
       "ipslaEtherJAggMeasuredMaxLossNumeratorSD": ipslaEtherJAggMeasuredMaxLossNumeratorSD,
       "ipslaEtherJAggMeasuredMaxLossDenominatorSD": ipslaEtherJAggMeasuredMaxLossDenominatorSD,
       "ipslaEtherJAggMeasuredAvgLossNumeratorSD": ipslaEtherJAggMeasuredAvgLossNumeratorSD,
       "ipslaEtherJAggMeasuredAvgLossDenominatorSD": ipslaEtherJAggMeasuredAvgLossDenominatorSD,
       "ipslaEtherJAggMeasuredMinLossNumeratorDS": ipslaEtherJAggMeasuredMinLossNumeratorDS,
       "ipslaEtherJAggMeasuredMinLossDenominatorDS": ipslaEtherJAggMeasuredMinLossDenominatorDS,
       "ipslaEtherJAggMeasuredMaxLossNumeratorDS": ipslaEtherJAggMeasuredMaxLossNumeratorDS,
       "ipslaEtherJAggMeasuredMaxLossDenominatorDS": ipslaEtherJAggMeasuredMaxLossDenominatorDS,
       "ipslaEtherJAggMeasuredAvgLossNumeratorDS": ipslaEtherJAggMeasuredAvgLossNumeratorDS,
       "ipslaEtherJAggMeasuredAvgLossDenominatorDS": ipslaEtherJAggMeasuredAvgLossDenominatorDS,
       "ipslaEtherJAggMeasuredCumulativeLossNumeratorSD": ipslaEtherJAggMeasuredCumulativeLossNumeratorSD,
       "ipslaEtherJAggMeasuredCumulativeLossDenominatorSD": ipslaEtherJAggMeasuredCumulativeLossDenominatorSD,
       "ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD": ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD,
       "ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD": ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD,
       "ipslaEtherJAggMeasuredCumulativeLossNumeratorDS": ipslaEtherJAggMeasuredCumulativeLossNumeratorDS,
       "ipslaEtherJAggMeasuredCumulativeLossDenominatorDS": ipslaEtherJAggMeasuredCumulativeLossDenominatorDS,
       "ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS": ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS,
       "ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS": ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS,
       "ipslaEthernetLatestOper": ipslaEthernetLatestOper,
       "ipslaEtherJitterLatestStatsTable": ipslaEtherJitterLatestStatsTable,
       "ipslaEtherJitterLatestStatsEntry": ipslaEtherJitterLatestStatsEntry,
       "ipslaEtherJitterLatestNumRTT": ipslaEtherJitterLatestNumRTT,
       "ipslaEtherJitterLatestRTTSum": ipslaEtherJitterLatestRTTSum,
       "ipslaEtherJitterLatestRTTSum2": ipslaEtherJitterLatestRTTSum2,
       "ipslaEtherJitterLatestRTTMin": ipslaEtherJitterLatestRTTMin,
       "ipslaEtherJitterLatestRTTMax": ipslaEtherJitterLatestRTTMax,
       "ipslaEtherJitterLatestMinPosSD": ipslaEtherJitterLatestMinPosSD,
       "ipslaEtherJitterLatestMaxPosSD": ipslaEtherJitterLatestMaxPosSD,
       "ipslaEtherJitterLatestNumPosSD": ipslaEtherJitterLatestNumPosSD,
       "ipslaEtherJitterLatestSumPosSD": ipslaEtherJitterLatestSumPosSD,
       "ipslaEtherJitterLatestSum2PosSD": ipslaEtherJitterLatestSum2PosSD,
       "ipslaEtherJitterLatestMinNegSD": ipslaEtherJitterLatestMinNegSD,
       "ipslaEtherJitterLatestMaxNegSD": ipslaEtherJitterLatestMaxNegSD,
       "ipslaEtherJitterLatestNumNegSD": ipslaEtherJitterLatestNumNegSD,
       "ipslaEtherJitterLatestSumNegSD": ipslaEtherJitterLatestSumNegSD,
       "ipslaEtherJitterLatestSum2NegSD": ipslaEtherJitterLatestSum2NegSD,
       "ipslaEtherJitterLatestMinPosDS": ipslaEtherJitterLatestMinPosDS,
       "ipslaEtherJitterLatestMaxPosDS": ipslaEtherJitterLatestMaxPosDS,
       "ipslaEtherJitterLatestNumPosDS": ipslaEtherJitterLatestNumPosDS,
       "ipslaEtherJitterLatestSumPosDS": ipslaEtherJitterLatestSumPosDS,
       "ipslaEtherJitterLatestSum2PosDS": ipslaEtherJitterLatestSum2PosDS,
       "ipslaEtherJitterLatestMinNegDS": ipslaEtherJitterLatestMinNegDS,
       "ipslaEtherJitterLatestMaxNegDS": ipslaEtherJitterLatestMaxNegDS,
       "ipslaEtherJitterLatestNumNegDS": ipslaEtherJitterLatestNumNegDS,
       "ipslaEtherJitterLatestSumNegDS": ipslaEtherJitterLatestSumNegDS,
       "ipslaEtherJitterLatestSum2NegDS": ipslaEtherJitterLatestSum2NegDS,
       "ipslaEtherJitterLatestFrmLossSD": ipslaEtherJitterLatestFrmLossSD,
       "ipslaEtherJitterLatestFrmLossDS": ipslaEtherJitterLatestFrmLossDS,
       "ipslaEtherJitterLatestFrmOutSeq": ipslaEtherJitterLatestFrmOutSeq,
       "ipslaEtherJitterLatestFrmMIA": ipslaEtherJitterLatestFrmMIA,
       "ipslaEtherJitterLatestFrmSkipped": ipslaEtherJitterLatestFrmSkipped,
       "ipslaEtherJitterLatestSense": ipslaEtherJitterLatestSense,
       "ipslaEtherJitterLatestFrmLateA": ipslaEtherJitterLatestFrmLateA,
       "ipslaEtherJitterLatestMinSucFrmL": ipslaEtherJitterLatestMinSucFrmL,
       "ipslaEtherJitterLatestMaxSucFrmL": ipslaEtherJitterLatestMaxSucFrmL,
       "ipslaEtherJitterLatestOWSumSD": ipslaEtherJitterLatestOWSumSD,
       "ipslaEtherJitterLatestOWSum2SD": ipslaEtherJitterLatestOWSum2SD,
       "ipslaEtherJitterLatestOWMinSD": ipslaEtherJitterLatestOWMinSD,
       "ipslaEtherJitterLatestOWMaxSD": ipslaEtherJitterLatestOWMaxSD,
       "ipslaEtherJitterLatestOWSumDS": ipslaEtherJitterLatestOWSumDS,
       "ipslaEtherJitterLatestOWSum2DS": ipslaEtherJitterLatestOWSum2DS,
       "ipslaEtherJitterLatestOWMinDS": ipslaEtherJitterLatestOWMinDS,
       "ipslaEtherJitterLatestOWMaxDS": ipslaEtherJitterLatestOWMaxDS,
       "ipslaEtherJitterLatestNumOW": ipslaEtherJitterLatestNumOW,
       "ipslaEtherJitterLatestAvgJitter": ipslaEtherJitterLatestAvgJitter,
       "ipslaEtherJitterLatestAvgSDJ": ipslaEtherJitterLatestAvgSDJ,
       "ipslaEtherJitterLatestAvgDSJ": ipslaEtherJitterLatestAvgDSJ,
       "ipslaEtherJitterLatestOWAvgSD": ipslaEtherJitterLatestOWAvgSD,
       "ipslaEtherJitterLatestOWAvgDS": ipslaEtherJitterLatestOWAvgDS,
       "ipslaEtherJitterLatestIAJOut": ipslaEtherJitterLatestIAJOut,
       "ipslaEtherJitterLatestIAJIn": ipslaEtherJitterLatestIAJIn,
       "ipslaEtherJLatestFrmUnProcessed": ipslaEtherJLatestFrmUnProcessed,
       "ciscoIpSlaEthernetMIBConform": ciscoIpSlaEthernetMIBConform,
       "ciscoIpSlaEthernetCompliances": ciscoIpSlaEthernetCompliances,
       "ciscoIpSlaEthernetCompliance": ciscoIpSlaEthernetCompliance,
       "ciscoIpSlaEthernetComplianceRev2": ciscoIpSlaEthernetComplianceRev2,
       "ciscoIpSlaEthernetComplianceRev3": ciscoIpSlaEthernetComplianceRev3,
       "ciscoIpSlaEthernetMIBGroups": ciscoIpSlaEthernetMIBGroups,
       "ciscoIpSlaEthernetAutoGroup": ciscoIpSlaEthernetAutoGroup,
       "ciscoIpSlaEthernetStatsGroup": ciscoIpSlaEthernetStatsGroup,
       "ciscoIpSlaEthernetAutoEVCGroup": ciscoIpSlaEthernetAutoEVCGroup,
       "ciscoIpSlaEthernetY1731Group": ciscoIpSlaEthernetY1731Group}
)
