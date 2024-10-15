# SNMP MIB module (HP-ICF-XRRP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-XRRP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:31 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(LastCreateTime,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "LastCreateTime")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hpicfXrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18)
)
hpicfXrrpMIB.setRevisions(
        ("2005-08-05 00:00",
         "2004-10-20 00:00",
         "2002-08-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XrrpRouterId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_HpicfXrrpNotifications_ObjectIdentity = ObjectIdentity
hpicfXrrpNotifications = _HpicfXrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 1)
)
_HpicfXrrpNotificationsPrefix_ObjectIdentity = ObjectIdentity
hpicfXrrpNotificationsPrefix = _HpicfXrrpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 1, 0)
)
_HpicfXrrpNotificationsObjects_ObjectIdentity = ObjectIdentity
hpicfXrrpNotificationsObjects = _HpicfXrrpNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 1, 1)
)


class _HpicfXrrpTrapAuthErrorType_Type(Integer32):
    """Custom type hpicfXrrpTrapAuthErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authFailure", 3),
          ("authTypeMismatch", 2),
          ("invalidAuthType", 1))
    )


_HpicfXrrpTrapAuthErrorType_Type.__name__ = "Integer32"
_HpicfXrrpTrapAuthErrorType_Object = MibScalar
hpicfXrrpTrapAuthErrorType = _HpicfXrrpTrapAuthErrorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 1, 1, 1),
    _HpicfXrrpTrapAuthErrorType_Type()
)
hpicfXrrpTrapAuthErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfXrrpTrapAuthErrorType.setStatus("current")
_HpicfXrrpOperations_ObjectIdentity = ObjectIdentity
hpicfXrrpOperations = _HpicfXrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2)
)
_HpicfXrrpVersion_Type = Integer32
_HpicfXrrpVersion_Object = MibScalar
hpicfXrrpVersion = _HpicfXrrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 1),
    _HpicfXrrpVersion_Type()
)
hpicfXrrpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpVersion.setStatus("current")


class _HpicfXrrpAdminState_Type(Integer32):
    """Custom type hpicfXrrpAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfXrrpAdminState_Type.__name__ = "Integer32"
_HpicfXrrpAdminState_Object = MibScalar
hpicfXrrpAdminState = _HpicfXrrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 2),
    _HpicfXrrpAdminState_Type()
)
hpicfXrrpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXrrpAdminState.setStatus("current")


class _HpicfXrrpDomain_Type(Integer32):
    """Custom type hpicfXrrpDomain based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfXrrpDomain_Type.__name__ = "Integer32"
_HpicfXrrpDomain_Object = MibScalar
hpicfXrrpDomain = _HpicfXrrpDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 3),
    _HpicfXrrpDomain_Type()
)
hpicfXrrpDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXrrpDomain.setStatus("current")


class _HpicfXrrpRouterId_Type(XrrpRouterId):
    """Custom type hpicfXrrpRouterId based on XrrpRouterId"""
    defaultValue = 1


_HpicfXrrpRouterId_Object = MibScalar
hpicfXrrpRouterId = _HpicfXrrpRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 4),
    _HpicfXrrpRouterId_Type()
)
hpicfXrrpRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXrrpRouterId.setStatus("current")


class _HpicfXrrpFailback_Type(Integer32):
    """Custom type hpicfXrrpFailback based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999),
    )


_HpicfXrrpFailback_Type.__name__ = "Integer32"
_HpicfXrrpFailback_Object = MibScalar
hpicfXrrpFailback = _HpicfXrrpFailback_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 5),
    _HpicfXrrpFailback_Type()
)
hpicfXrrpFailback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXrrpFailback.setStatus("current")


class _HpicfXrrpTrapCntl_Type(Bits):
    """Custom type hpicfXrrpTrapCntl based on Bits"""
    namedValues = NamedValues(
        *(("authFailure", 2),
          ("masterState", 1),
          ("stateChange", 0))
    )

_HpicfXrrpTrapCntl_Type.__name__ = "Bits"
_HpicfXrrpTrapCntl_Object = MibScalar
hpicfXrrpTrapCntl = _HpicfXrrpTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 6),
    _HpicfXrrpTrapCntl_Type()
)
hpicfXrrpTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXrrpTrapCntl.setStatus("current")
_HpicfXrrpInstancesTable_Object = MibTable
hpicfXrrpInstancesTable = _HpicfXrrpInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfXrrpInstancesTable.setStatus("current")
_HpicfXrrpInstanceEntry_Object = MibTableRow
hpicfXrrpInstanceEntry = _HpicfXrrpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1)
)
hpicfXrrpInstanceEntry.setIndexNames(
    (0, "HP-ICF-XRRP", "hpicfXrrpInstanceRouterId"),
    (0, "HP-ICF-XRRP", "hpicfXrrpInstanceVlanId"),
)
if mibBuilder.loadTexts:
    hpicfXrrpInstanceEntry.setStatus("current")
_HpicfXrrpInstanceRouterId_Type = XrrpRouterId
_HpicfXrrpInstanceRouterId_Object = MibTableColumn
hpicfXrrpInstanceRouterId = _HpicfXrrpInstanceRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1, 1),
    _HpicfXrrpInstanceRouterId_Type()
)
hpicfXrrpInstanceRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfXrrpInstanceRouterId.setStatus("current")
_HpicfXrrpInstanceVlanId_Type = VlanId
_HpicfXrrpInstanceVlanId_Object = MibTableColumn
hpicfXrrpInstanceVlanId = _HpicfXrrpInstanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1, 2),
    _HpicfXrrpInstanceVlanId_Type()
)
hpicfXrrpInstanceVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfXrrpInstanceVlanId.setStatus("current")


class _HpicfXrrpInstanceOperState_Type(Integer32):
    """Custom type hpicfXrrpInstanceOperState based on Integer32"""
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
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3),
          ("vlandown", 4))
    )


_HpicfXrrpInstanceOperState_Type.__name__ = "Integer32"
_HpicfXrrpInstanceOperState_Object = MibTableColumn
hpicfXrrpInstanceOperState = _HpicfXrrpInstanceOperState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1, 3),
    _HpicfXrrpInstanceOperState_Type()
)
hpicfXrrpInstanceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpInstanceOperState.setStatus("current")


class _HpicfXrrpInstanceAuthType_Type(Integer32):
    """Custom type hpicfXrrpInstanceAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", 1),
          ("simpleTextPassword", 2))
    )


_HpicfXrrpInstanceAuthType_Type.__name__ = "Integer32"
_HpicfXrrpInstanceAuthType_Object = MibTableColumn
hpicfXrrpInstanceAuthType = _HpicfXrrpInstanceAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1, 4),
    _HpicfXrrpInstanceAuthType_Type()
)
hpicfXrrpInstanceAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfXrrpInstanceAuthType.setStatus("current")


class _HpicfXrrpInstanceAuthKey_Type(OctetString):
    """Custom type hpicfXrrpInstanceAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpicfXrrpInstanceAuthKey_Type.__name__ = "OctetString"
_HpicfXrrpInstanceAuthKey_Object = MibTableColumn
hpicfXrrpInstanceAuthKey = _HpicfXrrpInstanceAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1, 5),
    _HpicfXrrpInstanceAuthKey_Type()
)
hpicfXrrpInstanceAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfXrrpInstanceAuthKey.setStatus("current")


class _HpicfXrrpInstanceAdvertiseInterval_Type(Integer32):
    """Custom type hpicfXrrpInstanceAdvertiseInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HpicfXrrpInstanceAdvertiseInterval_Type.__name__ = "Integer32"
_HpicfXrrpInstanceAdvertiseInterval_Object = MibTableColumn
hpicfXrrpInstanceAdvertiseInterval = _HpicfXrrpInstanceAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1, 6),
    _HpicfXrrpInstanceAdvertiseInterval_Type()
)
hpicfXrrpInstanceAdvertiseInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfXrrpInstanceAdvertiseInterval.setStatus("current")
_HpicfXrrpInstanceUpTime_Type = TimeStamp
_HpicfXrrpInstanceUpTime_Object = MibTableColumn
hpicfXrrpInstanceUpTime = _HpicfXrrpInstanceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1, 7),
    _HpicfXrrpInstanceUpTime_Type()
)
hpicfXrrpInstanceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpInstanceUpTime.setStatus("current")
_HpicfXrrpInstanceRowStatus_Type = RowStatus
_HpicfXrrpInstanceRowStatus_Object = MibTableColumn
hpicfXrrpInstanceRowStatus = _HpicfXrrpInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 7, 1, 8),
    _HpicfXrrpInstanceRowStatus_Type()
)
hpicfXrrpInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfXrrpInstanceRowStatus.setStatus("current")
_HpicfXrrpInstanceAssoIpAddrTable_Object = MibTable
hpicfXrrpInstanceAssoIpAddrTable = _HpicfXrrpInstanceAssoIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 8)
)
if mibBuilder.loadTexts:
    hpicfXrrpInstanceAssoIpAddrTable.setStatus("current")
_HpicfXrrpInstanceAssoIpAddrEntry_Object = MibTableRow
hpicfXrrpInstanceAssoIpAddrEntry = _HpicfXrrpInstanceAssoIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 8, 1)
)
hpicfXrrpInstanceAssoIpAddrEntry.setIndexNames(
    (0, "HP-ICF-XRRP", "hpicfXrrpInstanceRouterId"),
    (0, "HP-ICF-XRRP", "hpicfXrrpInstanceVlanId"),
    (0, "HP-ICF-XRRP", "hpicfXrrpAssoIpAddr"),
)
if mibBuilder.loadTexts:
    hpicfXrrpInstanceAssoIpAddrEntry.setStatus("current")
_HpicfXrrpAssoIpAddr_Type = IpAddress
_HpicfXrrpAssoIpAddr_Object = MibTableColumn
hpicfXrrpAssoIpAddr = _HpicfXrrpAssoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 8, 1, 1),
    _HpicfXrrpAssoIpAddr_Type()
)
hpicfXrrpAssoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfXrrpAssoIpAddr.setStatus("current")
_HpicfXrrpAssoIpMask_Type = IpAddress
_HpicfXrrpAssoIpMask_Object = MibTableColumn
hpicfXrrpAssoIpMask = _HpicfXrrpAssoIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 8, 1, 2),
    _HpicfXrrpAssoIpMask_Type()
)
hpicfXrrpAssoIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfXrrpAssoIpMask.setStatus("current")
_HpicfXrrpAssoRowStatus_Type = RowStatus
_HpicfXrrpAssoRowStatus_Object = MibTableColumn
hpicfXrrpAssoRowStatus = _HpicfXrrpAssoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 8, 1, 3),
    _HpicfXrrpAssoRowStatus_Type()
)
hpicfXrrpAssoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfXrrpAssoRowStatus.setStatus("current")


class _HpicfXrrpTransferControl_Type(Integer32):
    """Custom type hpicfXrrpTransferControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notransferCtrl", 2),
          ("transferCtrl", 1))
    )


_HpicfXrrpTransferControl_Type.__name__ = "Integer32"
_HpicfXrrpTransferControl_Object = MibScalar
hpicfXrrpTransferControl = _HpicfXrrpTransferControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 9),
    _HpicfXrrpTransferControl_Type()
)
hpicfXrrpTransferControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXrrpTransferControl.setStatus("current")


class _HpicfXrrpInfiniteFailback_Type(Integer32):
    """Custom type hpicfXrrpInfiniteFailback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfXrrpInfiniteFailback_Type.__name__ = "Integer32"
_HpicfXrrpInfiniteFailback_Object = MibScalar
hpicfXrrpInfiniteFailback = _HpicfXrrpInfiniteFailback_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 2, 10),
    _HpicfXrrpInfiniteFailback_Type()
)
hpicfXrrpInfiniteFailback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXrrpInfiniteFailback.setStatus("current")
_HpicfXrrpStatistics_ObjectIdentity = ObjectIdentity
hpicfXrrpStatistics = _HpicfXrrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3)
)
_HpicfXrrpStatsXrrpMacAddress_Type = MacAddress
_HpicfXrrpStatsXrrpMacAddress_Object = MibScalar
hpicfXrrpStatsXrrpMacAddress = _HpicfXrrpStatsXrrpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 1),
    _HpicfXrrpStatsXrrpMacAddress_Type()
)
hpicfXrrpStatsXrrpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsXrrpMacAddress.setStatus("current")
_HpicfXrrpStatsMacAndMask_Type = MacAddress
_HpicfXrrpStatsMacAndMask_Object = MibScalar
hpicfXrrpStatsMacAndMask = _HpicfXrrpStatsMacAndMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 2),
    _HpicfXrrpStatsMacAndMask_Type()
)
hpicfXrrpStatsMacAndMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsMacAndMask.setStatus("current")
_HpicfXrrpStatsPktsRcvd_Type = Counter32
_HpicfXrrpStatsPktsRcvd_Object = MibScalar
hpicfXrrpStatsPktsRcvd = _HpicfXrrpStatsPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 3),
    _HpicfXrrpStatsPktsRcvd_Type()
)
hpicfXrrpStatsPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsPktsRcvd.setStatus("current")
_HpicfXrrpStatsNotDomainPktsReject_Type = Counter32
_HpicfXrrpStatsNotDomainPktsReject_Object = MibScalar
hpicfXrrpStatsNotDomainPktsReject = _HpicfXrrpStatsNotDomainPktsReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 4),
    _HpicfXrrpStatsNotDomainPktsReject_Type()
)
hpicfXrrpStatsNotDomainPktsReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsNotDomainPktsReject.setStatus("current")
_HpicfXrrpStatsCheckSumPktsReject_Type = Counter32
_HpicfXrrpStatsCheckSumPktsReject_Object = MibScalar
hpicfXrrpStatsCheckSumPktsReject = _HpicfXrrpStatsCheckSumPktsReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 5),
    _HpicfXrrpStatsCheckSumPktsReject_Type()
)
hpicfXrrpStatsCheckSumPktsReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsCheckSumPktsReject.setStatus("current")
_HpicfXrrpStatsBadValuePktsReject_Type = Counter32
_HpicfXrrpStatsBadValuePktsReject_Object = MibScalar
hpicfXrrpStatsBadValuePktsReject = _HpicfXrrpStatsBadValuePktsReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 6),
    _HpicfXrrpStatsBadValuePktsReject_Type()
)
hpicfXrrpStatsBadValuePktsReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsBadValuePktsReject.setStatus("current")
_HpicfXrrpStatsCorruptedPktsReject_Type = Counter32
_HpicfXrrpStatsCorruptedPktsReject_Object = MibScalar
hpicfXrrpStatsCorruptedPktsReject = _HpicfXrrpStatsCorruptedPktsReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 7),
    _HpicfXrrpStatsCorruptedPktsReject_Type()
)
hpicfXrrpStatsCorruptedPktsReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsCorruptedPktsReject.setStatus("current")
_HpicfXrrpStatsVersionErrorPktsReject_Type = Counter32
_HpicfXrrpStatsVersionErrorPktsReject_Object = MibScalar
hpicfXrrpStatsVersionErrorPktsReject = _HpicfXrrpStatsVersionErrorPktsReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 8),
    _HpicfXrrpStatsVersionErrorPktsReject_Type()
)
hpicfXrrpStatsVersionErrorPktsReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsVersionErrorPktsReject.setStatus("current")
_HpicfXrrpStatsBcastArpsXmtd_Type = Counter32
_HpicfXrrpStatsBcastArpsXmtd_Object = MibScalar
hpicfXrrpStatsBcastArpsXmtd = _HpicfXrrpStatsBcastArpsXmtd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 9),
    _HpicfXrrpStatsBcastArpsXmtd_Type()
)
hpicfXrrpStatsBcastArpsXmtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsBcastArpsXmtd.setStatus("current")
_HpicfXrrpStatsUpTime_Type = TimeStamp
_HpicfXrrpStatsUpTime_Object = MibScalar
hpicfXrrpStatsUpTime = _HpicfXrrpStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 10),
    _HpicfXrrpStatsUpTime_Type()
)
hpicfXrrpStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsUpTime.setStatus("current")
_HpicfXrrpStatsProtocolCreateTime_Type = LastCreateTime
_HpicfXrrpStatsProtocolCreateTime_Object = MibScalar
hpicfXrrpStatsProtocolCreateTime = _HpicfXrrpStatsProtocolCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 11),
    _HpicfXrrpStatsProtocolCreateTime_Type()
)
hpicfXrrpStatsProtocolCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsProtocolCreateTime.setStatus("current")
_HpicfXrrpStatsInstancesTable_Object = MibTable
hpicfXrrpStatsInstancesTable = _HpicfXrrpStatsInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12)
)
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstancesTable.setStatus("current")
_HpicfXrrpStatsInstanceEntry_Object = MibTableRow
hpicfXrrpStatsInstanceEntry = _HpicfXrrpStatsInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1)
)
hpicfXrrpStatsInstanceEntry.setIndexNames(
    (0, "HP-ICF-XRRP", "hpicfXrrpInstanceRouterId"),
    (0, "HP-ICF-XRRP", "hpicfXrrpInstanceVlanId"),
)
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstanceEntry.setStatus("current")
_HpicfXrrpStatsInstancePktsRcvd_Type = Counter32
_HpicfXrrpStatsInstancePktsRcvd_Object = MibTableColumn
hpicfXrrpStatsInstancePktsRcvd = _HpicfXrrpStatsInstancePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 1),
    _HpicfXrrpStatsInstancePktsRcvd_Type()
)
hpicfXrrpStatsInstancePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstancePktsRcvd.setStatus("current")
_HpicfXrrpStatsInstancePktsXmtd_Type = Counter32
_HpicfXrrpStatsInstancePktsXmtd_Object = MibTableColumn
hpicfXrrpStatsInstancePktsXmtd = _HpicfXrrpStatsInstancePktsXmtd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 2),
    _HpicfXrrpStatsInstancePktsXmtd_Type()
)
hpicfXrrpStatsInstancePktsXmtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstancePktsXmtd.setStatus("current")
_HpicfXrrpStatsInstanceVersionErrPkts_Type = Counter32
_HpicfXrrpStatsInstanceVersionErrPkts_Object = MibTableColumn
hpicfXrrpStatsInstanceVersionErrPkts = _HpicfXrrpStatsInstanceVersionErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 3),
    _HpicfXrrpStatsInstanceVersionErrPkts_Type()
)
hpicfXrrpStatsInstanceVersionErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstanceVersionErrPkts.setStatus("current")
_HpicfXrrpStatsInstancePriorityZeroPktsRcvd_Type = Counter32
_HpicfXrrpStatsInstancePriorityZeroPktsRcvd_Object = MibTableColumn
hpicfXrrpStatsInstancePriorityZeroPktsRcvd = _HpicfXrrpStatsInstancePriorityZeroPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 4),
    _HpicfXrrpStatsInstancePriorityZeroPktsRcvd_Type()
)
hpicfXrrpStatsInstancePriorityZeroPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstancePriorityZeroPktsRcvd.setStatus("current")
_HpicfXrrpStatsInstancePriorityZeroPktsXmtd_Type = Counter32
_HpicfXrrpStatsInstancePriorityZeroPktsXmtd_Object = MibTableColumn
hpicfXrrpStatsInstancePriorityZeroPktsXmtd = _HpicfXrrpStatsInstancePriorityZeroPktsXmtd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 5),
    _HpicfXrrpStatsInstancePriorityZeroPktsXmtd_Type()
)
hpicfXrrpStatsInstancePriorityZeroPktsXmtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstancePriorityZeroPktsXmtd.setStatus("current")
_HpicfXrrpStatsInstanceMismatchedIpPkts_Type = Counter32
_HpicfXrrpStatsInstanceMismatchedIpPkts_Object = MibTableColumn
hpicfXrrpStatsInstanceMismatchedIpPkts = _HpicfXrrpStatsInstanceMismatchedIpPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 6),
    _HpicfXrrpStatsInstanceMismatchedIpPkts_Type()
)
hpicfXrrpStatsInstanceMismatchedIpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstanceMismatchedIpPkts.setStatus("current")
_HpicfXrrpStatsInstanceAuthFailPktsReject_Type = Counter32
_HpicfXrrpStatsInstanceAuthFailPktsReject_Object = MibTableColumn
hpicfXrrpStatsInstanceAuthFailPktsReject = _HpicfXrrpStatsInstanceAuthFailPktsReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 7),
    _HpicfXrrpStatsInstanceAuthFailPktsReject_Type()
)
hpicfXrrpStatsInstanceAuthFailPktsReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstanceAuthFailPktsReject.setStatus("current")
_HpicfXrrpStatsInstanceIntervalMismatchPkts_Type = Counter32
_HpicfXrrpStatsInstanceIntervalMismatchPkts_Object = MibTableColumn
hpicfXrrpStatsInstanceIntervalMismatchPkts = _HpicfXrrpStatsInstanceIntervalMismatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 8),
    _HpicfXrrpStatsInstanceIntervalMismatchPkts_Type()
)
hpicfXrrpStatsInstanceIntervalMismatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstanceIntervalMismatchPkts.setStatus("current")
_HpicfXrrpStatsInstanceCreateTime_Type = LastCreateTime
_HpicfXrrpStatsInstanceCreateTime_Object = MibTableColumn
hpicfXrrpStatsInstanceCreateTime = _HpicfXrrpStatsInstanceCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 12, 1, 9),
    _HpicfXrrpStatsInstanceCreateTime_Type()
)
hpicfXrrpStatsInstanceCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsInstanceCreateTime.setStatus("current")
_HpicfXrrpStatsRcTable_Object = MibTable
hpicfXrrpStatsRcTable = _HpicfXrrpStatsRcTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13)
)
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcTable.setStatus("current")
_HpicfXrrpStatsRcEntry_Object = MibTableRow
hpicfXrrpStatsRcEntry = _HpicfXrrpStatsRcEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1)
)
hpicfXrrpStatsRcEntry.setIndexNames(
    (0, "HP-ICF-XRRP", "hpicfXrrpStatsRcRouterId"),
)
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcEntry.setStatus("current")
_HpicfXrrpStatsRcRouterId_Type = XrrpRouterId
_HpicfXrrpStatsRcRouterId_Object = MibTableColumn
hpicfXrrpStatsRcRouterId = _HpicfXrrpStatsRcRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 1),
    _HpicfXrrpStatsRcRouterId_Type()
)
hpicfXrrpStatsRcRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcRouterId.setStatus("current")


class _HpicfXrrpStatsRcOperState_Type(Integer32):
    """Custom type hpicfXrrpStatsRcOperState based on Integer32"""
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
        *(("backup", 2),
          ("failback", 4),
          ("initialize", 1),
          ("master", 3))
    )


_HpicfXrrpStatsRcOperState_Type.__name__ = "Integer32"
_HpicfXrrpStatsRcOperState_Object = MibTableColumn
hpicfXrrpStatsRcOperState = _HpicfXrrpStatsRcOperState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 2),
    _HpicfXrrpStatsRcOperState_Type()
)
hpicfXrrpStatsRcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcOperState.setStatus("current")
_HpicfXrrpStatsRcType1PktsRcvd_Type = Counter32
_HpicfXrrpStatsRcType1PktsRcvd_Object = MibTableColumn
hpicfXrrpStatsRcType1PktsRcvd = _HpicfXrrpStatsRcType1PktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 3),
    _HpicfXrrpStatsRcType1PktsRcvd_Type()
)
hpicfXrrpStatsRcType1PktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcType1PktsRcvd.setStatus("current")
_HpicfXrrpStatsRcType1PktsXmtd_Type = Counter32
_HpicfXrrpStatsRcType1PktsXmtd_Object = MibTableColumn
hpicfXrrpStatsRcType1PktsXmtd = _HpicfXrrpStatsRcType1PktsXmtd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 4),
    _HpicfXrrpStatsRcType1PktsXmtd_Type()
)
hpicfXrrpStatsRcType1PktsXmtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcType1PktsXmtd.setStatus("current")
_HpicfXrrpStatsRcType2PktsRcvd_Type = Counter32
_HpicfXrrpStatsRcType2PktsRcvd_Object = MibTableColumn
hpicfXrrpStatsRcType2PktsRcvd = _HpicfXrrpStatsRcType2PktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 5),
    _HpicfXrrpStatsRcType2PktsRcvd_Type()
)
hpicfXrrpStatsRcType2PktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcType2PktsRcvd.setStatus("current")
_HpicfXrrpStatsRcType2PktsXmtd_Type = Counter32
_HpicfXrrpStatsRcType2PktsXmtd_Object = MibTableColumn
hpicfXrrpStatsRcType2PktsXmtd = _HpicfXrrpStatsRcType2PktsXmtd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 6),
    _HpicfXrrpStatsRcType2PktsXmtd_Type()
)
hpicfXrrpStatsRcType2PktsXmtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcType2PktsXmtd.setStatus("current")
_HpicfXrrpStatsRcBecomeMaster_Type = Counter32
_HpicfXrrpStatsRcBecomeMaster_Object = MibTableColumn
hpicfXrrpStatsRcBecomeMaster = _HpicfXrrpStatsRcBecomeMaster_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 7),
    _HpicfXrrpStatsRcBecomeMaster_Type()
)
hpicfXrrpStatsRcBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcBecomeMaster.setStatus("current")
_HpicfXrrpStatsRcMasterTime_Type = TimeStamp
_HpicfXrrpStatsRcMasterTime_Object = MibTableColumn
hpicfXrrpStatsRcMasterTime = _HpicfXrrpStatsRcMasterTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 8),
    _HpicfXrrpStatsRcMasterTime_Type()
)
hpicfXrrpStatsRcMasterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcMasterTime.setStatus("current")
_HpicfXrrpStatsRcUnknownVlanId_Type = Counter32
_HpicfXrrpStatsRcUnknownVlanId_Object = MibTableColumn
hpicfXrrpStatsRcUnknownVlanId = _HpicfXrrpStatsRcUnknownVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 9),
    _HpicfXrrpStatsRcUnknownVlanId_Type()
)
hpicfXrrpStatsRcUnknownVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcUnknownVlanId.setStatus("current")
_HpicfXrrpStatsRcCreateTime_Type = LastCreateTime
_HpicfXrrpStatsRcCreateTime_Object = MibTableColumn
hpicfXrrpStatsRcCreateTime = _HpicfXrrpStatsRcCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 3, 13, 1, 10),
    _HpicfXrrpStatsRcCreateTime_Type()
)
hpicfXrrpStatsRcCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXrrpStatsRcCreateTime.setStatus("current")
_HpicfXrrpConformance_ObjectIdentity = ObjectIdentity
hpicfXrrpConformance = _HpicfXrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4)
)
_HpicfXrrpMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfXrrpMIBCompliances = _HpicfXrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 1)
)
_HpicfXrrpMIBGroups_ObjectIdentity = ObjectIdentity
hpicfXrrpMIBGroups = _HpicfXrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 2)
)

# Managed Objects groups

hpicfXrrpOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 2, 1)
)
hpicfXrrpOperGroup.setObjects(
      *(("HP-ICF-XRRP", "hpicfXrrpVersion"),
        ("HP-ICF-XRRP", "hpicfXrrpAdminState"),
        ("HP-ICF-XRRP", "hpicfXrrpDomain"),
        ("HP-ICF-XRRP", "hpicfXrrpRouterId"),
        ("HP-ICF-XRRP", "hpicfXrrpTrapCntl"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceOperState"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAuthType"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAuthKey"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAdvertiseInterval"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceUpTime"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceRowStatus"),
        ("HP-ICF-XRRP", "hpicfXrrpAssoIpMask"),
        ("HP-ICF-XRRP", "hpicfXrrpAssoRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfXrrpOperGroup.setStatus("deprecated")

hpicfXrrpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 2, 2)
)
hpicfXrrpStatsGroup.setObjects(
      *(("HP-ICF-XRRP", "hpicfXrrpStatsXrrpMacAddress"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsMacAndMask"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsPktsRcvd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsNotDomainPktsReject"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsCheckSumPktsReject"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsBadValuePktsReject"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsCorruptedPktsReject"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsVersionErrorPktsReject"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsBcastArpsXmtd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsUpTime"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsProtocolCreateTime"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstancePktsRcvd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstancePktsXmtd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstanceVersionErrPkts"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstancePriorityZeroPktsRcvd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstancePriorityZeroPktsXmtd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstanceMismatchedIpPkts"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstanceAuthFailPktsReject"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstanceIntervalMismatchPkts"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsInstanceCreateTime"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcOperState"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcType1PktsRcvd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcType1PktsXmtd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcType2PktsRcvd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcType2PktsXmtd"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcBecomeMaster"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcMasterTime"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcUnknownVlanId"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcCreateTime"))
)
if mibBuilder.loadTexts:
    hpicfXrrpStatsGroup.setStatus("current")

hpicfXrrpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 2, 3)
)
hpicfXrrpTrapGroup.setObjects(
    ("HP-ICF-XRRP", "hpicfXrrpTrapAuthErrorType")
)
if mibBuilder.loadTexts:
    hpicfXrrpTrapGroup.setStatus("current")

hpicfXrrpOperGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 2, 5)
)
hpicfXrrpOperGroup1.setObjects(
      *(("HP-ICF-XRRP", "hpicfXrrpVersion"),
        ("HP-ICF-XRRP", "hpicfXrrpAdminState"),
        ("HP-ICF-XRRP", "hpicfXrrpDomain"),
        ("HP-ICF-XRRP", "hpicfXrrpRouterId"),
        ("HP-ICF-XRRP", "hpicfXrrpTrapCntl"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceOperState"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAuthType"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAuthKey"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAdvertiseInterval"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceUpTime"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceRowStatus"),
        ("HP-ICF-XRRP", "hpicfXrrpAssoIpMask"),
        ("HP-ICF-XRRP", "hpicfXrrpAssoRowStatus"),
        ("HP-ICF-XRRP", "hpicfXrrpTransferControl"),
        ("HP-ICF-XRRP", "hpicfXrrpInfiniteFailback"))
)
if mibBuilder.loadTexts:
    hpicfXrrpOperGroup1.setStatus("current")

hpicfXrrpOperGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 2, 6)
)
hpicfXrrpOperGroup2.setObjects(
      *(("HP-ICF-XRRP", "hpicfXrrpVersion"),
        ("HP-ICF-XRRP", "hpicfXrrpAdminState"),
        ("HP-ICF-XRRP", "hpicfXrrpDomain"),
        ("HP-ICF-XRRP", "hpicfXrrpRouterId"),
        ("HP-ICF-XRRP", "hpicfXrrpFailback"),
        ("HP-ICF-XRRP", "hpicfXrrpTrapCntl"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceOperState"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAuthType"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAuthKey"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceAdvertiseInterval"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceUpTime"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceRowStatus"),
        ("HP-ICF-XRRP", "hpicfXrrpAssoIpMask"),
        ("HP-ICF-XRRP", "hpicfXrrpAssoRowStatus"),
        ("HP-ICF-XRRP", "hpicfXrrpTransferControl"),
        ("HP-ICF-XRRP", "hpicfXrrpInfiniteFailback"))
)
if mibBuilder.loadTexts:
    hpicfXrrpOperGroup2.setStatus("current")


# Notification objects

hpicfXrrpTrapStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 1, 0, 1)
)
hpicfXrrpTrapStateChange.setObjects(
      *(("HP-ICF-XRRP", "hpicfXrrpDomain"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcRouterId"),
        ("HP-ICF-XRRP", "hpicfXrrpStatsRcOperState"))
)
if mibBuilder.loadTexts:
    hpicfXrrpTrapStateChange.setStatus(
        "current"
    )

hpicfXrrpTrapAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 1, 0, 2)
)
hpicfXrrpTrapAuthFailure.setObjects(
      *(("HP-ICF-XRRP", "hpicfXrrpDomain"),
        ("HP-ICF-XRRP", "hpicfXrrpRouterId"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceRouterId"),
        ("HP-ICF-XRRP", "hpicfXrrpInstanceVlanId"),
        ("HP-ICF-XRRP", "hpicfXrrpTrapAuthErrorType"))
)
if mibBuilder.loadTexts:
    hpicfXrrpTrapAuthFailure.setStatus(
        "current"
    )


# Notifications groups

hpicfXrrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 2, 4)
)
hpicfXrrpNotificationGroup.setObjects(
      *(("HP-ICF-XRRP", "hpicfXrrpTrapStateChange"),
        ("HP-ICF-XRRP", "hpicfXrrpTrapAuthFailure"))
)
if mibBuilder.loadTexts:
    hpicfXrrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfXrrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfXrrpMIBCompliance.setStatus(
        "deprecated"
    )

hpicfXrrpMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfXrrpMIBCompliance1.setStatus(
        "current"
    )

hpicfXrrpMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfXrrpMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-XRRP",
    **{"XrrpRouterId": XrrpRouterId,
       "hpicfXrrpMIB": hpicfXrrpMIB,
       "hpicfXrrpNotifications": hpicfXrrpNotifications,
       "hpicfXrrpNotificationsPrefix": hpicfXrrpNotificationsPrefix,
       "hpicfXrrpTrapStateChange": hpicfXrrpTrapStateChange,
       "hpicfXrrpTrapAuthFailure": hpicfXrrpTrapAuthFailure,
       "hpicfXrrpNotificationsObjects": hpicfXrrpNotificationsObjects,
       "hpicfXrrpTrapAuthErrorType": hpicfXrrpTrapAuthErrorType,
       "hpicfXrrpOperations": hpicfXrrpOperations,
       "hpicfXrrpVersion": hpicfXrrpVersion,
       "hpicfXrrpAdminState": hpicfXrrpAdminState,
       "hpicfXrrpDomain": hpicfXrrpDomain,
       "hpicfXrrpRouterId": hpicfXrrpRouterId,
       "hpicfXrrpFailback": hpicfXrrpFailback,
       "hpicfXrrpTrapCntl": hpicfXrrpTrapCntl,
       "hpicfXrrpInstancesTable": hpicfXrrpInstancesTable,
       "hpicfXrrpInstanceEntry": hpicfXrrpInstanceEntry,
       "hpicfXrrpInstanceRouterId": hpicfXrrpInstanceRouterId,
       "hpicfXrrpInstanceVlanId": hpicfXrrpInstanceVlanId,
       "hpicfXrrpInstanceOperState": hpicfXrrpInstanceOperState,
       "hpicfXrrpInstanceAuthType": hpicfXrrpInstanceAuthType,
       "hpicfXrrpInstanceAuthKey": hpicfXrrpInstanceAuthKey,
       "hpicfXrrpInstanceAdvertiseInterval": hpicfXrrpInstanceAdvertiseInterval,
       "hpicfXrrpInstanceUpTime": hpicfXrrpInstanceUpTime,
       "hpicfXrrpInstanceRowStatus": hpicfXrrpInstanceRowStatus,
       "hpicfXrrpInstanceAssoIpAddrTable": hpicfXrrpInstanceAssoIpAddrTable,
       "hpicfXrrpInstanceAssoIpAddrEntry": hpicfXrrpInstanceAssoIpAddrEntry,
       "hpicfXrrpAssoIpAddr": hpicfXrrpAssoIpAddr,
       "hpicfXrrpAssoIpMask": hpicfXrrpAssoIpMask,
       "hpicfXrrpAssoRowStatus": hpicfXrrpAssoRowStatus,
       "hpicfXrrpTransferControl": hpicfXrrpTransferControl,
       "hpicfXrrpInfiniteFailback": hpicfXrrpInfiniteFailback,
       "hpicfXrrpStatistics": hpicfXrrpStatistics,
       "hpicfXrrpStatsXrrpMacAddress": hpicfXrrpStatsXrrpMacAddress,
       "hpicfXrrpStatsMacAndMask": hpicfXrrpStatsMacAndMask,
       "hpicfXrrpStatsPktsRcvd": hpicfXrrpStatsPktsRcvd,
       "hpicfXrrpStatsNotDomainPktsReject": hpicfXrrpStatsNotDomainPktsReject,
       "hpicfXrrpStatsCheckSumPktsReject": hpicfXrrpStatsCheckSumPktsReject,
       "hpicfXrrpStatsBadValuePktsReject": hpicfXrrpStatsBadValuePktsReject,
       "hpicfXrrpStatsCorruptedPktsReject": hpicfXrrpStatsCorruptedPktsReject,
       "hpicfXrrpStatsVersionErrorPktsReject": hpicfXrrpStatsVersionErrorPktsReject,
       "hpicfXrrpStatsBcastArpsXmtd": hpicfXrrpStatsBcastArpsXmtd,
       "hpicfXrrpStatsUpTime": hpicfXrrpStatsUpTime,
       "hpicfXrrpStatsProtocolCreateTime": hpicfXrrpStatsProtocolCreateTime,
       "hpicfXrrpStatsInstancesTable": hpicfXrrpStatsInstancesTable,
       "hpicfXrrpStatsInstanceEntry": hpicfXrrpStatsInstanceEntry,
       "hpicfXrrpStatsInstancePktsRcvd": hpicfXrrpStatsInstancePktsRcvd,
       "hpicfXrrpStatsInstancePktsXmtd": hpicfXrrpStatsInstancePktsXmtd,
       "hpicfXrrpStatsInstanceVersionErrPkts": hpicfXrrpStatsInstanceVersionErrPkts,
       "hpicfXrrpStatsInstancePriorityZeroPktsRcvd": hpicfXrrpStatsInstancePriorityZeroPktsRcvd,
       "hpicfXrrpStatsInstancePriorityZeroPktsXmtd": hpicfXrrpStatsInstancePriorityZeroPktsXmtd,
       "hpicfXrrpStatsInstanceMismatchedIpPkts": hpicfXrrpStatsInstanceMismatchedIpPkts,
       "hpicfXrrpStatsInstanceAuthFailPktsReject": hpicfXrrpStatsInstanceAuthFailPktsReject,
       "hpicfXrrpStatsInstanceIntervalMismatchPkts": hpicfXrrpStatsInstanceIntervalMismatchPkts,
       "hpicfXrrpStatsInstanceCreateTime": hpicfXrrpStatsInstanceCreateTime,
       "hpicfXrrpStatsRcTable": hpicfXrrpStatsRcTable,
       "hpicfXrrpStatsRcEntry": hpicfXrrpStatsRcEntry,
       "hpicfXrrpStatsRcRouterId": hpicfXrrpStatsRcRouterId,
       "hpicfXrrpStatsRcOperState": hpicfXrrpStatsRcOperState,
       "hpicfXrrpStatsRcType1PktsRcvd": hpicfXrrpStatsRcType1PktsRcvd,
       "hpicfXrrpStatsRcType1PktsXmtd": hpicfXrrpStatsRcType1PktsXmtd,
       "hpicfXrrpStatsRcType2PktsRcvd": hpicfXrrpStatsRcType2PktsRcvd,
       "hpicfXrrpStatsRcType2PktsXmtd": hpicfXrrpStatsRcType2PktsXmtd,
       "hpicfXrrpStatsRcBecomeMaster": hpicfXrrpStatsRcBecomeMaster,
       "hpicfXrrpStatsRcMasterTime": hpicfXrrpStatsRcMasterTime,
       "hpicfXrrpStatsRcUnknownVlanId": hpicfXrrpStatsRcUnknownVlanId,
       "hpicfXrrpStatsRcCreateTime": hpicfXrrpStatsRcCreateTime,
       "hpicfXrrpConformance": hpicfXrrpConformance,
       "hpicfXrrpMIBCompliances": hpicfXrrpMIBCompliances,
       "hpicfXrrpMIBCompliance": hpicfXrrpMIBCompliance,
       "hpicfXrrpMIBCompliance1": hpicfXrrpMIBCompliance1,
       "hpicfXrrpMIBCompliance2": hpicfXrrpMIBCompliance2,
       "hpicfXrrpMIBGroups": hpicfXrrpMIBGroups,
       "hpicfXrrpOperGroup": hpicfXrrpOperGroup,
       "hpicfXrrpStatsGroup": hpicfXrrpStatsGroup,
       "hpicfXrrpTrapGroup": hpicfXrrpTrapGroup,
       "hpicfXrrpNotificationGroup": hpicfXrrpNotificationGroup,
       "hpicfXrrpOperGroup1": hpicfXrrpOperGroup1,
       "hpicfXrrpOperGroup2": hpicfXrrpOperGroup2}
)
