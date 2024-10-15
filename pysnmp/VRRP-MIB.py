# SNMP MIB module (VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:29 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

vrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 68)
)
vrrpMIB.setRevisions(
        ("2006-12-13 00:00",
         "2000-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VrId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_VrrpNotifications_ObjectIdentity = ObjectIdentity
vrrpNotifications = _VrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 0)
)
_VrrpOperations_ObjectIdentity = ObjectIdentity
vrrpOperations = _VrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 1)
)
_VrrpNodeVersion_Type = Integer32
_VrrpNodeVersion_Object = MibScalar
vrrpNodeVersion = _VrrpNodeVersion_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 1),
    _VrrpNodeVersion_Type()
)
vrrpNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNodeVersion.setStatus("deprecated")


class _VrrpNotificationCntl_Type(Integer32):
    """Custom type vrrpNotificationCntl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VrrpNotificationCntl_Type.__name__ = "Integer32"
_VrrpNotificationCntl_Object = MibScalar
vrrpNotificationCntl = _VrrpNotificationCntl_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 2),
    _VrrpNotificationCntl_Type()
)
vrrpNotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNotificationCntl.setStatus("current")
_VrrpOperTable_Object = MibTable
vrrpOperTable = _VrrpOperTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3)
)
if mibBuilder.loadTexts:
    vrrpOperTable.setStatus("deprecated")
_VrrpOperEntry_Object = MibTableRow
vrrpOperEntry = _VrrpOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1)
)
vrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    vrrpOperEntry.setStatus("deprecated")
_VrrpOperVrId_Type = VrId
_VrrpOperVrId_Object = MibTableColumn
vrrpOperVrId = _VrrpOperVrId_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 1),
    _VrrpOperVrId_Type()
)
vrrpOperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpOperVrId.setStatus("deprecated")
_VrrpOperVirtualMacAddr_Type = MacAddress
_VrrpOperVirtualMacAddr_Object = MibTableColumn
vrrpOperVirtualMacAddr = _VrrpOperVirtualMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 2),
    _VrrpOperVirtualMacAddr_Type()
)
vrrpOperVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperVirtualMacAddr.setStatus("deprecated")


class _VrrpOperState_Type(Integer32):
    """Custom type vrrpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )


_VrrpOperState_Type.__name__ = "Integer32"
_VrrpOperState_Object = MibTableColumn
vrrpOperState = _VrrpOperState_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 3),
    _VrrpOperState_Type()
)
vrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperState.setStatus("deprecated")


class _VrrpOperAdminState_Type(Integer32):
    """Custom type vrrpOperAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VrrpOperAdminState_Type.__name__ = "Integer32"
_VrrpOperAdminState_Object = MibTableColumn
vrrpOperAdminState = _VrrpOperAdminState_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 4),
    _VrrpOperAdminState_Type()
)
vrrpOperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperAdminState.setStatus("deprecated")


class _VrrpOperPriority_Type(Integer32):
    """Custom type vrrpOperPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpOperPriority_Type.__name__ = "Integer32"
_VrrpOperPriority_Object = MibTableColumn
vrrpOperPriority = _VrrpOperPriority_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 5),
    _VrrpOperPriority_Type()
)
vrrpOperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperPriority.setStatus("deprecated")


class _VrrpOperIpAddrCount_Type(Integer32):
    """Custom type vrrpOperIpAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpOperIpAddrCount_Type.__name__ = "Integer32"
_VrrpOperIpAddrCount_Object = MibTableColumn
vrrpOperIpAddrCount = _VrrpOperIpAddrCount_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 6),
    _VrrpOperIpAddrCount_Type()
)
vrrpOperIpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperIpAddrCount.setStatus("deprecated")
_VrrpOperMasterIpAddr_Type = IpAddress
_VrrpOperMasterIpAddr_Object = MibTableColumn
vrrpOperMasterIpAddr = _VrrpOperMasterIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 7),
    _VrrpOperMasterIpAddr_Type()
)
vrrpOperMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperMasterIpAddr.setStatus("deprecated")


class _VrrpOperPrimaryIpAddr_Type(IpAddress):
    """Custom type vrrpOperPrimaryIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_VrrpOperPrimaryIpAddr_Object = MibTableColumn
vrrpOperPrimaryIpAddr = _VrrpOperPrimaryIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 8),
    _VrrpOperPrimaryIpAddr_Type()
)
vrrpOperPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperPrimaryIpAddr.setStatus("deprecated")


class _VrrpOperAuthType_Type(Integer32):
    """Custom type vrrpOperAuthType based on Integer32"""
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
        *(("ipAuthenticationHeader", 3),
          ("noAuthentication", 1),
          ("simpleTextPassword", 2))
    )


_VrrpOperAuthType_Type.__name__ = "Integer32"
_VrrpOperAuthType_Object = MibTableColumn
vrrpOperAuthType = _VrrpOperAuthType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 9),
    _VrrpOperAuthType_Type()
)
vrrpOperAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperAuthType.setStatus("deprecated")


class _VrrpOperAuthKey_Type(OctetString):
    """Custom type vrrpOperAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VrrpOperAuthKey_Type.__name__ = "OctetString"
_VrrpOperAuthKey_Object = MibTableColumn
vrrpOperAuthKey = _VrrpOperAuthKey_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 10),
    _VrrpOperAuthKey_Type()
)
vrrpOperAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperAuthKey.setStatus("deprecated")


class _VrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type vrrpOperAdvertisementInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_VrrpOperAdvertisementInterval_Object = MibTableColumn
vrrpOperAdvertisementInterval = _VrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 11),
    _VrrpOperAdvertisementInterval_Type()
)
vrrpOperAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperAdvertisementInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    vrrpOperAdvertisementInterval.setUnits("seconds")


class _VrrpOperPreemptMode_Type(TruthValue):
    """Custom type vrrpOperPreemptMode based on TruthValue"""


_VrrpOperPreemptMode_Object = MibTableColumn
vrrpOperPreemptMode = _VrrpOperPreemptMode_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 12),
    _VrrpOperPreemptMode_Type()
)
vrrpOperPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperPreemptMode.setStatus("deprecated")
_VrrpOperVirtualRouterUpTime_Type = TimeStamp
_VrrpOperVirtualRouterUpTime_Object = MibTableColumn
vrrpOperVirtualRouterUpTime = _VrrpOperVirtualRouterUpTime_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 13),
    _VrrpOperVirtualRouterUpTime_Type()
)
vrrpOperVirtualRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperVirtualRouterUpTime.setStatus("deprecated")


class _VrrpOperProtocol_Type(Integer32):
    """Custom type vrrpOperProtocol based on Integer32"""
    defaultValue = 1

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
        *(("bridge", 2),
          ("decnet", 3),
          ("ip", 1),
          ("other", 4))
    )


_VrrpOperProtocol_Type.__name__ = "Integer32"
_VrrpOperProtocol_Object = MibTableColumn
vrrpOperProtocol = _VrrpOperProtocol_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 14),
    _VrrpOperProtocol_Type()
)
vrrpOperProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperProtocol.setStatus("deprecated")
_VrrpOperRowStatus_Type = RowStatus
_VrrpOperRowStatus_Object = MibTableColumn
vrrpOperRowStatus = _VrrpOperRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 15),
    _VrrpOperRowStatus_Type()
)
vrrpOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperRowStatus.setStatus("deprecated")
_VrrpAssoIpAddrTable_Object = MibTable
vrrpAssoIpAddrTable = _VrrpAssoIpAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 4)
)
if mibBuilder.loadTexts:
    vrrpAssoIpAddrTable.setStatus("deprecated")
_VrrpAssoIpAddrEntry_Object = MibTableRow
vrrpAssoIpAddrEntry = _VrrpAssoIpAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 4, 1)
)
vrrpAssoIpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "VRRP-MIB", "vrrpAssoIpAddr"),
)
if mibBuilder.loadTexts:
    vrrpAssoIpAddrEntry.setStatus("deprecated")
_VrrpAssoIpAddr_Type = IpAddress
_VrrpAssoIpAddr_Object = MibTableColumn
vrrpAssoIpAddr = _VrrpAssoIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 1),
    _VrrpAssoIpAddr_Type()
)
vrrpAssoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpAssoIpAddr.setStatus("deprecated")
_VrrpAssoIpAddrRowStatus_Type = RowStatus
_VrrpAssoIpAddrRowStatus_Object = MibTableColumn
vrrpAssoIpAddrRowStatus = _VrrpAssoIpAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 2),
    _VrrpAssoIpAddrRowStatus_Type()
)
vrrpAssoIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpAssoIpAddrRowStatus.setStatus("deprecated")
_VrrpTrapPacketSrc_Type = IpAddress
_VrrpTrapPacketSrc_Object = MibScalar
vrrpTrapPacketSrc = _VrrpTrapPacketSrc_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 5),
    _VrrpTrapPacketSrc_Type()
)
vrrpTrapPacketSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vrrpTrapPacketSrc.setStatus("deprecated")


class _VrrpTrapAuthErrorType_Type(Integer32):
    """Custom type vrrpTrapAuthErrorType based on Integer32"""
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


_VrrpTrapAuthErrorType_Type.__name__ = "Integer32"
_VrrpTrapAuthErrorType_Object = MibScalar
vrrpTrapAuthErrorType = _VrrpTrapAuthErrorType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 6),
    _VrrpTrapAuthErrorType_Type()
)
vrrpTrapAuthErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vrrpTrapAuthErrorType.setStatus("deprecated")
_VrrpOperationsTable_Object = MibTable
vrrpOperationsTable = _VrrpOperationsTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7)
)
if mibBuilder.loadTexts:
    vrrpOperationsTable.setStatus("current")
_VrrpOperationsEntry_Object = MibTableRow
vrrpOperationsEntry = _VrrpOperationsEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1)
)
vrrpOperationsEntry.setIndexNames(
    (0, "VRRP-MIB", "vrrpOperationsInetAddrType"),
    (0, "VRRP-MIB", "vrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vrrpOperationsEntry.setStatus("current")
_VrrpOperationsInetAddrType_Type = InetAddressType
_VrrpOperationsInetAddrType_Object = MibTableColumn
vrrpOperationsInetAddrType = _VrrpOperationsInetAddrType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 1),
    _VrrpOperationsInetAddrType_Type()
)
vrrpOperationsInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpOperationsInetAddrType.setStatus("current")
_VrrpOperationsVrId_Type = VrId
_VrrpOperationsVrId_Object = MibTableColumn
vrrpOperationsVrId = _VrrpOperationsVrId_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 2),
    _VrrpOperationsVrId_Type()
)
vrrpOperationsVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpOperationsVrId.setStatus("current")
_VrrpOperationsVirtualMacAddr_Type = MacAddress
_VrrpOperationsVirtualMacAddr_Object = MibTableColumn
vrrpOperationsVirtualMacAddr = _VrrpOperationsVirtualMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 3),
    _VrrpOperationsVirtualMacAddr_Type()
)
vrrpOperationsVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsVirtualMacAddr.setStatus("current")


class _VrrpOperationsState_Type(Integer32):
    """Custom type vrrpOperationsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )


_VrrpOperationsState_Type.__name__ = "Integer32"
_VrrpOperationsState_Object = MibTableColumn
vrrpOperationsState = _VrrpOperationsState_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 4),
    _VrrpOperationsState_Type()
)
vrrpOperationsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsState.setStatus("current")


class _VrrpOperationsPriority_Type(Unsigned32):
    """Custom type vrrpOperationsPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpOperationsPriority_Type.__name__ = "Unsigned32"
_VrrpOperationsPriority_Object = MibTableColumn
vrrpOperationsPriority = _VrrpOperationsPriority_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 5),
    _VrrpOperationsPriority_Type()
)
vrrpOperationsPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsPriority.setStatus("current")


class _VrrpOperationsAddrCount_Type(Integer32):
    """Custom type vrrpOperationsAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpOperationsAddrCount_Type.__name__ = "Integer32"
_VrrpOperationsAddrCount_Object = MibTableColumn
vrrpOperationsAddrCount = _VrrpOperationsAddrCount_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 6),
    _VrrpOperationsAddrCount_Type()
)
vrrpOperationsAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsAddrCount.setStatus("current")
_VrrpOperationsMasterIpAddr_Type = InetAddress
_VrrpOperationsMasterIpAddr_Object = MibTableColumn
vrrpOperationsMasterIpAddr = _VrrpOperationsMasterIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 7),
    _VrrpOperationsMasterIpAddr_Type()
)
vrrpOperationsMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsMasterIpAddr.setStatus("current")
_VrrpOperationsPrimaryIpAddr_Type = InetAddress
_VrrpOperationsPrimaryIpAddr_Object = MibTableColumn
vrrpOperationsPrimaryIpAddr = _VrrpOperationsPrimaryIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 8),
    _VrrpOperationsPrimaryIpAddr_Type()
)
vrrpOperationsPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsPrimaryIpAddr.setStatus("current")


class _VrrpOperationsAdvInterval_Type(TimeInterval):
    """Custom type vrrpOperationsAdvInterval based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VrrpOperationsAdvInterval_Type.__name__ = "TimeInterval"
_VrrpOperationsAdvInterval_Object = MibTableColumn
vrrpOperationsAdvInterval = _VrrpOperationsAdvInterval_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 9),
    _VrrpOperationsAdvInterval_Type()
)
vrrpOperationsAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    vrrpOperationsAdvInterval.setUnits("centiseconds")


class _VrrpOperationsPreemptMode_Type(TruthValue):
    """Custom type vrrpOperationsPreemptMode based on TruthValue"""


_VrrpOperationsPreemptMode_Object = MibTableColumn
vrrpOperationsPreemptMode = _VrrpOperationsPreemptMode_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 10),
    _VrrpOperationsPreemptMode_Type()
)
vrrpOperationsPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsPreemptMode.setStatus("current")


class _VrrpOperationsAcceptMode_Type(TruthValue):
    """Custom type vrrpOperationsAcceptMode based on TruthValue"""


_VrrpOperationsAcceptMode_Object = MibTableColumn
vrrpOperationsAcceptMode = _VrrpOperationsAcceptMode_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 11),
    _VrrpOperationsAcceptMode_Type()
)
vrrpOperationsAcceptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsAcceptMode.setStatus("current")
_VrrpOperationsUpTime_Type = TimeStamp
_VrrpOperationsUpTime_Object = MibTableColumn
vrrpOperationsUpTime = _VrrpOperationsUpTime_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 12),
    _VrrpOperationsUpTime_Type()
)
vrrpOperationsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsUpTime.setStatus("current")


class _VrrpOperationsStorageType_Type(StorageType):
    """Custom type vrrpOperationsStorageType based on StorageType"""


_VrrpOperationsStorageType_Object = MibTableColumn
vrrpOperationsStorageType = _VrrpOperationsStorageType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 13),
    _VrrpOperationsStorageType_Type()
)
vrrpOperationsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsStorageType.setStatus("current")
_VrrpOperationsRowStatus_Type = RowStatus
_VrrpOperationsRowStatus_Object = MibTableColumn
vrrpOperationsRowStatus = _VrrpOperationsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 14),
    _VrrpOperationsRowStatus_Type()
)
vrrpOperationsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsRowStatus.setStatus("current")
_VrrpAssociatedIpAddrTable_Object = MibTable
vrrpAssociatedIpAddrTable = _VrrpAssociatedIpAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8)
)
if mibBuilder.loadTexts:
    vrrpAssociatedIpAddrTable.setStatus("current")
_VrrpAssociatedIpAddrEntry_Object = MibTableRow
vrrpAssociatedIpAddrEntry = _VrrpAssociatedIpAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8, 1)
)
vrrpAssociatedIpAddrEntry.setIndexNames(
    (0, "VRRP-MIB", "vrrpOperationsInetAddrType"),
    (0, "VRRP-MIB", "vrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpAssociatedIpAddr"),
)
if mibBuilder.loadTexts:
    vrrpAssociatedIpAddrEntry.setStatus("current")


class _VrrpAssociatedIpAddr_Type(InetAddress):
    """Custom type vrrpAssociatedIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VrrpAssociatedIpAddr_Type.__name__ = "InetAddress"
_VrrpAssociatedIpAddr_Object = MibTableColumn
vrrpAssociatedIpAddr = _VrrpAssociatedIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 1),
    _VrrpAssociatedIpAddr_Type()
)
vrrpAssociatedIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpAssociatedIpAddr.setStatus("current")


class _VrrpAssociatedStorageType_Type(StorageType):
    """Custom type vrrpAssociatedStorageType based on StorageType"""


_VrrpAssociatedStorageType_Object = MibTableColumn
vrrpAssociatedStorageType = _VrrpAssociatedStorageType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 2),
    _VrrpAssociatedStorageType_Type()
)
vrrpAssociatedStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpAssociatedStorageType.setStatus("current")
_VrrpAssociatedIpAddrRowStatus_Type = RowStatus
_VrrpAssociatedIpAddrRowStatus_Object = MibTableColumn
vrrpAssociatedIpAddrRowStatus = _VrrpAssociatedIpAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 3),
    _VrrpAssociatedIpAddrRowStatus_Type()
)
vrrpAssociatedIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpAssociatedIpAddrRowStatus.setStatus("current")


class _VrrpNewMasterReason_Type(Integer32):
    """Custom type vrrpNewMasterReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("masterNoResponse", 3),
          ("notmaster", 0),
          ("preempted", 2),
          ("priority", 1))
    )


_VrrpNewMasterReason_Type.__name__ = "Integer32"
_VrrpNewMasterReason_Object = MibScalar
vrrpNewMasterReason = _VrrpNewMasterReason_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 9),
    _VrrpNewMasterReason_Type()
)
vrrpNewMasterReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewMasterReason.setStatus("current")


class _VrrpTrapProtoErrReason_Type(Integer32):
    """Custom type vrrpTrapProtoErrReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checksumError", 2),
          ("hopLimitError", 0),
          ("versionError", 1),
          ("vridError", 3))
    )


_VrrpTrapProtoErrReason_Type.__name__ = "Integer32"
_VrrpTrapProtoErrReason_Object = MibScalar
vrrpTrapProtoErrReason = _VrrpTrapProtoErrReason_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 10),
    _VrrpTrapProtoErrReason_Type()
)
vrrpTrapProtoErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vrrpTrapProtoErrReason.setStatus("current")
_VrrpStatistics_ObjectIdentity = ObjectIdentity
vrrpStatistics = _VrrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 2)
)
_VrrpRouterChecksumErrors_Type = Counter32
_VrrpRouterChecksumErrors_Object = MibScalar
vrrpRouterChecksumErrors = _VrrpRouterChecksumErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 1),
    _VrrpRouterChecksumErrors_Type()
)
vrrpRouterChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouterChecksumErrors.setStatus("current")
_VrrpRouterVersionErrors_Type = Counter32
_VrrpRouterVersionErrors_Object = MibScalar
vrrpRouterVersionErrors = _VrrpRouterVersionErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 2),
    _VrrpRouterVersionErrors_Type()
)
vrrpRouterVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouterVersionErrors.setStatus("current")
_VrrpRouterVrIdErrors_Type = Counter32
_VrrpRouterVrIdErrors_Object = MibScalar
vrrpRouterVrIdErrors = _VrrpRouterVrIdErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 3),
    _VrrpRouterVrIdErrors_Type()
)
vrrpRouterVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouterVrIdErrors.setStatus("current")
_VrrpRouterStatsTable_Object = MibTable
vrrpRouterStatsTable = _VrrpRouterStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4)
)
if mibBuilder.loadTexts:
    vrrpRouterStatsTable.setStatus("deprecated")
_VrrpRouterStatsEntry_Object = MibTableRow
vrrpRouterStatsEntry = _VrrpRouterStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vrrpRouterStatsEntry.setStatus("deprecated")
_VrrpStatsBecomeMaster_Type = Counter32
_VrrpStatsBecomeMaster_Object = MibTableColumn
vrrpStatsBecomeMaster = _VrrpStatsBecomeMaster_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 1),
    _VrrpStatsBecomeMaster_Type()
)
vrrpStatsBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsBecomeMaster.setStatus("deprecated")
_VrrpStatsAdvertiseRcvd_Type = Counter32
_VrrpStatsAdvertiseRcvd_Object = MibTableColumn
vrrpStatsAdvertiseRcvd = _VrrpStatsAdvertiseRcvd_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 2),
    _VrrpStatsAdvertiseRcvd_Type()
)
vrrpStatsAdvertiseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAdvertiseRcvd.setStatus("deprecated")
_VrrpStatsAdvertiseIntervalErrors_Type = Counter32
_VrrpStatsAdvertiseIntervalErrors_Object = MibTableColumn
vrrpStatsAdvertiseIntervalErrors = _VrrpStatsAdvertiseIntervalErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 3),
    _VrrpStatsAdvertiseIntervalErrors_Type()
)
vrrpStatsAdvertiseIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAdvertiseIntervalErrors.setStatus("deprecated")
_VrrpStatsAuthFailures_Type = Counter32
_VrrpStatsAuthFailures_Object = MibTableColumn
vrrpStatsAuthFailures = _VrrpStatsAuthFailures_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 4),
    _VrrpStatsAuthFailures_Type()
)
vrrpStatsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAuthFailures.setStatus("deprecated")
_VrrpStatsIpTtlErrors_Type = Counter32
_VrrpStatsIpTtlErrors_Object = MibTableColumn
vrrpStatsIpTtlErrors = _VrrpStatsIpTtlErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 5),
    _VrrpStatsIpTtlErrors_Type()
)
vrrpStatsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsIpTtlErrors.setStatus("deprecated")
_VrrpStatsPriorityZeroPktsRcvd_Type = Counter32
_VrrpStatsPriorityZeroPktsRcvd_Object = MibTableColumn
vrrpStatsPriorityZeroPktsRcvd = _VrrpStatsPriorityZeroPktsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 6),
    _VrrpStatsPriorityZeroPktsRcvd_Type()
)
vrrpStatsPriorityZeroPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsPriorityZeroPktsRcvd.setStatus("deprecated")
_VrrpStatsPriorityZeroPktsSent_Type = Counter32
_VrrpStatsPriorityZeroPktsSent_Object = MibTableColumn
vrrpStatsPriorityZeroPktsSent = _VrrpStatsPriorityZeroPktsSent_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 7),
    _VrrpStatsPriorityZeroPktsSent_Type()
)
vrrpStatsPriorityZeroPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsPriorityZeroPktsSent.setStatus("deprecated")
_VrrpStatsInvalidTypePktsRcvd_Type = Counter32
_VrrpStatsInvalidTypePktsRcvd_Object = MibTableColumn
vrrpStatsInvalidTypePktsRcvd = _VrrpStatsInvalidTypePktsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 8),
    _VrrpStatsInvalidTypePktsRcvd_Type()
)
vrrpStatsInvalidTypePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsInvalidTypePktsRcvd.setStatus("deprecated")
_VrrpStatsAddressListErrors_Type = Counter32
_VrrpStatsAddressListErrors_Object = MibTableColumn
vrrpStatsAddressListErrors = _VrrpStatsAddressListErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 9),
    _VrrpStatsAddressListErrors_Type()
)
vrrpStatsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAddressListErrors.setStatus("deprecated")
_VrrpStatsInvalidAuthType_Type = Counter32
_VrrpStatsInvalidAuthType_Object = MibTableColumn
vrrpStatsInvalidAuthType = _VrrpStatsInvalidAuthType_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 10),
    _VrrpStatsInvalidAuthType_Type()
)
vrrpStatsInvalidAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsInvalidAuthType.setStatus("deprecated")
_VrrpStatsAuthTypeMismatch_Type = Counter32
_VrrpStatsAuthTypeMismatch_Object = MibTableColumn
vrrpStatsAuthTypeMismatch = _VrrpStatsAuthTypeMismatch_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 11),
    _VrrpStatsAuthTypeMismatch_Type()
)
vrrpStatsAuthTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAuthTypeMismatch.setStatus("deprecated")
_VrrpStatsPacketLengthErrors_Type = Counter32
_VrrpStatsPacketLengthErrors_Object = MibTableColumn
vrrpStatsPacketLengthErrors = _VrrpStatsPacketLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 12),
    _VrrpStatsPacketLengthErrors_Type()
)
vrrpStatsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsPacketLengthErrors.setStatus("deprecated")
_VrrpRouterStatisticsTable_Object = MibTable
vrrpRouterStatisticsTable = _VrrpRouterStatisticsTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5)
)
if mibBuilder.loadTexts:
    vrrpRouterStatisticsTable.setStatus("current")
_VrrpRouterStatisticsEntry_Object = MibTableRow
vrrpRouterStatisticsEntry = _VrrpRouterStatisticsEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vrrpRouterStatisticsEntry.setStatus("current")
_VrrpStatisticsMasterTransitions_Type = Counter32
_VrrpStatisticsMasterTransitions_Object = MibTableColumn
vrrpStatisticsMasterTransitions = _VrrpStatisticsMasterTransitions_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 1),
    _VrrpStatisticsMasterTransitions_Type()
)
vrrpStatisticsMasterTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsMasterTransitions.setStatus("current")
_VrrpStatisticsRcvdAdvertisements_Type = Counter32
_VrrpStatisticsRcvdAdvertisements_Object = MibTableColumn
vrrpStatisticsRcvdAdvertisements = _VrrpStatisticsRcvdAdvertisements_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 2),
    _VrrpStatisticsRcvdAdvertisements_Type()
)
vrrpStatisticsRcvdAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRcvdAdvertisements.setStatus("current")
_VrrpStatisticsAdvIntervalErrors_Type = Counter32
_VrrpStatisticsAdvIntervalErrors_Object = MibTableColumn
vrrpStatisticsAdvIntervalErrors = _VrrpStatisticsAdvIntervalErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 3),
    _VrrpStatisticsAdvIntervalErrors_Type()
)
vrrpStatisticsAdvIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsAdvIntervalErrors.setStatus("current")
_VrrpStatisticsIpTtlErrors_Type = Counter32
_VrrpStatisticsIpTtlErrors_Object = MibTableColumn
vrrpStatisticsIpTtlErrors = _VrrpStatisticsIpTtlErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 4),
    _VrrpStatisticsIpTtlErrors_Type()
)
vrrpStatisticsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsIpTtlErrors.setStatus("current")
_VrrpStatisticsRcvdPriZeroPackets_Type = Counter32
_VrrpStatisticsRcvdPriZeroPackets_Object = MibTableColumn
vrrpStatisticsRcvdPriZeroPackets = _VrrpStatisticsRcvdPriZeroPackets_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 5),
    _VrrpStatisticsRcvdPriZeroPackets_Type()
)
vrrpStatisticsRcvdPriZeroPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRcvdPriZeroPackets.setStatus("current")
_VrrpStatisticsSentPriZeroPackets_Type = Counter32
_VrrpStatisticsSentPriZeroPackets_Object = MibTableColumn
vrrpStatisticsSentPriZeroPackets = _VrrpStatisticsSentPriZeroPackets_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 6),
    _VrrpStatisticsSentPriZeroPackets_Type()
)
vrrpStatisticsSentPriZeroPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsSentPriZeroPackets.setStatus("current")
_VrrpStatisticsRcvdInvalidTypePkts_Type = Counter32
_VrrpStatisticsRcvdInvalidTypePkts_Object = MibTableColumn
vrrpStatisticsRcvdInvalidTypePkts = _VrrpStatisticsRcvdInvalidTypePkts_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 7),
    _VrrpStatisticsRcvdInvalidTypePkts_Type()
)
vrrpStatisticsRcvdInvalidTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRcvdInvalidTypePkts.setStatus("current")
_VrrpStatisticsAddressListErrors_Type = Counter32
_VrrpStatisticsAddressListErrors_Object = MibTableColumn
vrrpStatisticsAddressListErrors = _VrrpStatisticsAddressListErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 8),
    _VrrpStatisticsAddressListErrors_Type()
)
vrrpStatisticsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsAddressListErrors.setStatus("current")
_VrrpStatisticsPacketLengthErrors_Type = Counter32
_VrrpStatisticsPacketLengthErrors_Object = MibTableColumn
vrrpStatisticsPacketLengthErrors = _VrrpStatisticsPacketLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 9),
    _VrrpStatisticsPacketLengthErrors_Type()
)
vrrpStatisticsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsPacketLengthErrors.setStatus("current")
_VrrpStatisticsRcvdInvalidAuthentications_Type = Counter32
_VrrpStatisticsRcvdInvalidAuthentications_Object = MibTableColumn
vrrpStatisticsRcvdInvalidAuthentications = _VrrpStatisticsRcvdInvalidAuthentications_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 10),
    _VrrpStatisticsRcvdInvalidAuthentications_Type()
)
vrrpStatisticsRcvdInvalidAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRcvdInvalidAuthentications.setStatus("current")
_VrrpStatisticsDiscontinuityTime_Type = TimeStamp
_VrrpStatisticsDiscontinuityTime_Object = MibTableColumn
vrrpStatisticsDiscontinuityTime = _VrrpStatisticsDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 11),
    _VrrpStatisticsDiscontinuityTime_Type()
)
vrrpStatisticsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsDiscontinuityTime.setStatus("current")
_VrrpStatisticsRefreshRate_Type = Unsigned32
_VrrpStatisticsRefreshRate_Object = MibTableColumn
vrrpStatisticsRefreshRate = _VrrpStatisticsRefreshRate_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 12),
    _VrrpStatisticsRefreshRate_Type()
)
vrrpStatisticsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    vrrpStatisticsRefreshRate.setUnits("milli-seconds")
_VrrpConformance_ObjectIdentity = ObjectIdentity
vrrpConformance = _VrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 3)
)
_VrrpMIBCompliances_ObjectIdentity = ObjectIdentity
vrrpMIBCompliances = _VrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 3, 1)
)
_VrrpMIBGroups_ObjectIdentity = ObjectIdentity
vrrpMIBGroups = _VrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 3, 2)
)
vrrpOperEntry.registerAugmentions(
    ("VRRP-MIB",
     "vrrpRouterStatsEntry")
)
vrrpRouterStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
vrrpOperationsEntry.registerAugmentions(
    ("VRRP-MIB",
     "vrrpRouterStatisticsEntry")
)
vrrpRouterStatisticsEntry.setIndexNames(*vrrpOperationsEntry.getIndexNames())

# Managed Objects groups

vrrpOperGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 1)
)
vrrpOperGroup.setObjects(
      *(("VRRP-MIB", "vrrpNodeVersion"),
        ("VRRP-MIB", "vrrpNotificationCntl"),
        ("VRRP-MIB", "vrrpOperVirtualMacAddr"),
        ("VRRP-MIB", "vrrpOperState"),
        ("VRRP-MIB", "vrrpOperAdminState"),
        ("VRRP-MIB", "vrrpOperPriority"),
        ("VRRP-MIB", "vrrpOperIpAddrCount"),
        ("VRRP-MIB", "vrrpOperMasterIpAddr"),
        ("VRRP-MIB", "vrrpOperPrimaryIpAddr"),
        ("VRRP-MIB", "vrrpOperAuthType"),
        ("VRRP-MIB", "vrrpOperAuthKey"),
        ("VRRP-MIB", "vrrpOperAdvertisementInterval"),
        ("VRRP-MIB", "vrrpOperPreemptMode"),
        ("VRRP-MIB", "vrrpOperVirtualRouterUpTime"),
        ("VRRP-MIB", "vrrpOperProtocol"),
        ("VRRP-MIB", "vrrpOperRowStatus"),
        ("VRRP-MIB", "vrrpAssoIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    vrrpOperGroup.setStatus("deprecated")

vrrpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 2)
)
vrrpStatsGroup.setObjects(
      *(("VRRP-MIB", "vrrpRouterChecksumErrors"),
        ("VRRP-MIB", "vrrpRouterVersionErrors"),
        ("VRRP-MIB", "vrrpRouterVrIdErrors"),
        ("VRRP-MIB", "vrrpStatsBecomeMaster"),
        ("VRRP-MIB", "vrrpStatsAdvertiseRcvd"),
        ("VRRP-MIB", "vrrpStatsAdvertiseIntervalErrors"),
        ("VRRP-MIB", "vrrpStatsAuthFailures"),
        ("VRRP-MIB", "vrrpStatsIpTtlErrors"),
        ("VRRP-MIB", "vrrpStatsPriorityZeroPktsRcvd"),
        ("VRRP-MIB", "vrrpStatsPriorityZeroPktsSent"),
        ("VRRP-MIB", "vrrpStatsInvalidTypePktsRcvd"),
        ("VRRP-MIB", "vrrpStatsAddressListErrors"),
        ("VRRP-MIB", "vrrpStatsInvalidAuthType"),
        ("VRRP-MIB", "vrrpStatsAuthTypeMismatch"),
        ("VRRP-MIB", "vrrpStatsPacketLengthErrors"))
)
if mibBuilder.loadTexts:
    vrrpStatsGroup.setStatus("deprecated")

vrrpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 3)
)
vrrpTrapGroup.setObjects(
      *(("VRRP-MIB", "vrrpTrapPacketSrc"),
        ("VRRP-MIB", "vrrpTrapAuthErrorType"))
)
if mibBuilder.loadTexts:
    vrrpTrapGroup.setStatus("deprecated")

vrrpOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 5)
)
vrrpOperationsGroup.setObjects(
      *(("VRRP-MIB", "vrrpNotificationCntl"),
        ("VRRP-MIB", "vrrpOperationsVirtualMacAddr"),
        ("VRRP-MIB", "vrrpOperationsState"),
        ("VRRP-MIB", "vrrpOperationsPriority"),
        ("VRRP-MIB", "vrrpOperationsMasterIpAddr"),
        ("VRRP-MIB", "vrrpOperationsAdvInterval"),
        ("VRRP-MIB", "vrrpOperationsPreemptMode"),
        ("VRRP-MIB", "vrrpOperationsAcceptMode"),
        ("VRRP-MIB", "vrrpOperationsUpTime"),
        ("VRRP-MIB", "vrrpOperationsStorageType"),
        ("VRRP-MIB", "vrrpOperationsRowStatus"),
        ("VRRP-MIB", "vrrpOperationsAddrCount"),
        ("VRRP-MIB", "vrrpOperationsPrimaryIpAddr"),
        ("VRRP-MIB", "vrrpAssociatedStorageType"),
        ("VRRP-MIB", "vrrpAssociatedIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    vrrpOperationsGroup.setStatus("current")

vrrpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 6)
)
vrrpStatisticsGroup.setObjects(
      *(("VRRP-MIB", "vrrpRouterChecksumErrors"),
        ("VRRP-MIB", "vrrpRouterVersionErrors"),
        ("VRRP-MIB", "vrrpRouterVrIdErrors"),
        ("VRRP-MIB", "vrrpStatisticsMasterTransitions"),
        ("VRRP-MIB", "vrrpStatisticsRcvdAdvertisements"),
        ("VRRP-MIB", "vrrpStatisticsAdvIntervalErrors"),
        ("VRRP-MIB", "vrrpStatisticsRcvdPriZeroPackets"),
        ("VRRP-MIB", "vrrpStatisticsSentPriZeroPackets"),
        ("VRRP-MIB", "vrrpStatisticsRcvdInvalidTypePkts"),
        ("VRRP-MIB", "vrrpStatisticsIpTtlErrors"),
        ("VRRP-MIB", "vrrpStatisticsAddressListErrors"),
        ("VRRP-MIB", "vrrpStatisticsPacketLengthErrors"),
        ("VRRP-MIB", "vrrpStatisticsRcvdInvalidAuthentications"),
        ("VRRP-MIB", "vrrpStatisticsDiscontinuityTime"),
        ("VRRP-MIB", "vrrpStatisticsRefreshRate"))
)
if mibBuilder.loadTexts:
    vrrpStatisticsGroup.setStatus("current")

vrrpTrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 7)
)
vrrpTrapInfoGroup.setObjects(
      *(("VRRP-MIB", "vrrpNewMasterReason"),
        ("VRRP-MIB", "vrrpTrapProtoErrReason"))
)
if mibBuilder.loadTexts:
    vrrpTrapInfoGroup.setStatus("current")


# Notification objects

vrrpTrapNewMaster = NotificationType(
    (1, 3, 6, 1, 2, 1, 68, 0, 1)
)
vrrpTrapNewMaster.setObjects(
      *(("VRRP-MIB", "vrrpOperationsMasterIpAddr"),
        ("VRRP-MIB", "vrrpNewMasterReason"))
)
if mibBuilder.loadTexts:
    vrrpTrapNewMaster.setStatus(
        "current"
    )

vrrpTrapAuthFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 68, 0, 2)
)
vrrpTrapAuthFailure.setObjects(
      *(("VRRP-MIB", "vrrpTrapPacketSrc"),
        ("VRRP-MIB", "vrrpTrapAuthErrorType"))
)
if mibBuilder.loadTexts:
    vrrpTrapAuthFailure.setStatus(
        "deprecated"
    )

vrrpTrapProtoError = NotificationType(
    (1, 3, 6, 1, 2, 1, 68, 0, 3)
)
vrrpTrapProtoError.setObjects(
    ("VRRP-MIB", "vrrpTrapProtoErrReason")
)
if mibBuilder.loadTexts:
    vrrpTrapProtoError.setStatus(
        "current"
    )


# Notifications groups

vrrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 4)
)
vrrpNotificationGroup.setObjects(
      *(("VRRP-MIB", "vrrpTrapNewMaster"),
        ("VRRP-MIB", "vrrpTrapAuthFailure"))
)
if mibBuilder.loadTexts:
    vrrpNotificationGroup.setStatus(
        "deprecated"
    )

vrrpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 8)
)
vrrpNotificationsGroup.setObjects(
      *(("VRRP-MIB", "vrrpTrapNewMaster"),
        ("VRRP-MIB", "vrrpTrapProtoError"))
)
if mibBuilder.loadTexts:
    vrrpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vrrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 68, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vrrpMIBCompliance.setStatus(
        "deprecated"
    )

vrrpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 68, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vrrpModuleFullCompliance.setStatus(
        "current"
    )

vrrpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 68, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vrrpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VRRP-MIB",
    **{"VrId": VrId,
       "vrrpMIB": vrrpMIB,
       "vrrpNotifications": vrrpNotifications,
       "vrrpTrapNewMaster": vrrpTrapNewMaster,
       "vrrpTrapAuthFailure": vrrpTrapAuthFailure,
       "vrrpTrapProtoError": vrrpTrapProtoError,
       "vrrpOperations": vrrpOperations,
       "vrrpNodeVersion": vrrpNodeVersion,
       "vrrpNotificationCntl": vrrpNotificationCntl,
       "vrrpOperTable": vrrpOperTable,
       "vrrpOperEntry": vrrpOperEntry,
       "vrrpOperVrId": vrrpOperVrId,
       "vrrpOperVirtualMacAddr": vrrpOperVirtualMacAddr,
       "vrrpOperState": vrrpOperState,
       "vrrpOperAdminState": vrrpOperAdminState,
       "vrrpOperPriority": vrrpOperPriority,
       "vrrpOperIpAddrCount": vrrpOperIpAddrCount,
       "vrrpOperMasterIpAddr": vrrpOperMasterIpAddr,
       "vrrpOperPrimaryIpAddr": vrrpOperPrimaryIpAddr,
       "vrrpOperAuthType": vrrpOperAuthType,
       "vrrpOperAuthKey": vrrpOperAuthKey,
       "vrrpOperAdvertisementInterval": vrrpOperAdvertisementInterval,
       "vrrpOperPreemptMode": vrrpOperPreemptMode,
       "vrrpOperVirtualRouterUpTime": vrrpOperVirtualRouterUpTime,
       "vrrpOperProtocol": vrrpOperProtocol,
       "vrrpOperRowStatus": vrrpOperRowStatus,
       "vrrpAssoIpAddrTable": vrrpAssoIpAddrTable,
       "vrrpAssoIpAddrEntry": vrrpAssoIpAddrEntry,
       "vrrpAssoIpAddr": vrrpAssoIpAddr,
       "vrrpAssoIpAddrRowStatus": vrrpAssoIpAddrRowStatus,
       "vrrpTrapPacketSrc": vrrpTrapPacketSrc,
       "vrrpTrapAuthErrorType": vrrpTrapAuthErrorType,
       "vrrpOperationsTable": vrrpOperationsTable,
       "vrrpOperationsEntry": vrrpOperationsEntry,
       "vrrpOperationsInetAddrType": vrrpOperationsInetAddrType,
       "vrrpOperationsVrId": vrrpOperationsVrId,
       "vrrpOperationsVirtualMacAddr": vrrpOperationsVirtualMacAddr,
       "vrrpOperationsState": vrrpOperationsState,
       "vrrpOperationsPriority": vrrpOperationsPriority,
       "vrrpOperationsAddrCount": vrrpOperationsAddrCount,
       "vrrpOperationsMasterIpAddr": vrrpOperationsMasterIpAddr,
       "vrrpOperationsPrimaryIpAddr": vrrpOperationsPrimaryIpAddr,
       "vrrpOperationsAdvInterval": vrrpOperationsAdvInterval,
       "vrrpOperationsPreemptMode": vrrpOperationsPreemptMode,
       "vrrpOperationsAcceptMode": vrrpOperationsAcceptMode,
       "vrrpOperationsUpTime": vrrpOperationsUpTime,
       "vrrpOperationsStorageType": vrrpOperationsStorageType,
       "vrrpOperationsRowStatus": vrrpOperationsRowStatus,
       "vrrpAssociatedIpAddrTable": vrrpAssociatedIpAddrTable,
       "vrrpAssociatedIpAddrEntry": vrrpAssociatedIpAddrEntry,
       "vrrpAssociatedIpAddr": vrrpAssociatedIpAddr,
       "vrrpAssociatedStorageType": vrrpAssociatedStorageType,
       "vrrpAssociatedIpAddrRowStatus": vrrpAssociatedIpAddrRowStatus,
       "vrrpNewMasterReason": vrrpNewMasterReason,
       "vrrpTrapProtoErrReason": vrrpTrapProtoErrReason,
       "vrrpStatistics": vrrpStatistics,
       "vrrpRouterChecksumErrors": vrrpRouterChecksumErrors,
       "vrrpRouterVersionErrors": vrrpRouterVersionErrors,
       "vrrpRouterVrIdErrors": vrrpRouterVrIdErrors,
       "vrrpRouterStatsTable": vrrpRouterStatsTable,
       "vrrpRouterStatsEntry": vrrpRouterStatsEntry,
       "vrrpStatsBecomeMaster": vrrpStatsBecomeMaster,
       "vrrpStatsAdvertiseRcvd": vrrpStatsAdvertiseRcvd,
       "vrrpStatsAdvertiseIntervalErrors": vrrpStatsAdvertiseIntervalErrors,
       "vrrpStatsAuthFailures": vrrpStatsAuthFailures,
       "vrrpStatsIpTtlErrors": vrrpStatsIpTtlErrors,
       "vrrpStatsPriorityZeroPktsRcvd": vrrpStatsPriorityZeroPktsRcvd,
       "vrrpStatsPriorityZeroPktsSent": vrrpStatsPriorityZeroPktsSent,
       "vrrpStatsInvalidTypePktsRcvd": vrrpStatsInvalidTypePktsRcvd,
       "vrrpStatsAddressListErrors": vrrpStatsAddressListErrors,
       "vrrpStatsInvalidAuthType": vrrpStatsInvalidAuthType,
       "vrrpStatsAuthTypeMismatch": vrrpStatsAuthTypeMismatch,
       "vrrpStatsPacketLengthErrors": vrrpStatsPacketLengthErrors,
       "vrrpRouterStatisticsTable": vrrpRouterStatisticsTable,
       "vrrpRouterStatisticsEntry": vrrpRouterStatisticsEntry,
       "vrrpStatisticsMasterTransitions": vrrpStatisticsMasterTransitions,
       "vrrpStatisticsRcvdAdvertisements": vrrpStatisticsRcvdAdvertisements,
       "vrrpStatisticsAdvIntervalErrors": vrrpStatisticsAdvIntervalErrors,
       "vrrpStatisticsIpTtlErrors": vrrpStatisticsIpTtlErrors,
       "vrrpStatisticsRcvdPriZeroPackets": vrrpStatisticsRcvdPriZeroPackets,
       "vrrpStatisticsSentPriZeroPackets": vrrpStatisticsSentPriZeroPackets,
       "vrrpStatisticsRcvdInvalidTypePkts": vrrpStatisticsRcvdInvalidTypePkts,
       "vrrpStatisticsAddressListErrors": vrrpStatisticsAddressListErrors,
       "vrrpStatisticsPacketLengthErrors": vrrpStatisticsPacketLengthErrors,
       "vrrpStatisticsRcvdInvalidAuthentications": vrrpStatisticsRcvdInvalidAuthentications,
       "vrrpStatisticsDiscontinuityTime": vrrpStatisticsDiscontinuityTime,
       "vrrpStatisticsRefreshRate": vrrpStatisticsRefreshRate,
       "vrrpConformance": vrrpConformance,
       "vrrpMIBCompliances": vrrpMIBCompliances,
       "vrrpMIBCompliance": vrrpMIBCompliance,
       "vrrpModuleFullCompliance": vrrpModuleFullCompliance,
       "vrrpModuleReadOnlyCompliance": vrrpModuleReadOnlyCompliance,
       "vrrpMIBGroups": vrrpMIBGroups,
       "vrrpOperGroup": vrrpOperGroup,
       "vrrpStatsGroup": vrrpStatsGroup,
       "vrrpTrapGroup": vrrpTrapGroup,
       "vrrpNotificationGroup": vrrpNotificationGroup,
       "vrrpOperationsGroup": vrrpOperationsGroup,
       "vrrpStatisticsGroup": vrrpStatisticsGroup,
       "vrrpTrapInfoGroup": vrrpTrapInfoGroup,
       "vrrpNotificationsGroup": vrrpNotificationsGroup}
)
