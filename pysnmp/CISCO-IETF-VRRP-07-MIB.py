# SNMP MIB module (CISCO-IETF-VRRP-07-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-VRRP-07-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:07 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

ciscoVrrp07MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 143)
)
ciscoVrrp07MIB.setRevisions(
        ("2010-02-23 00:00",
         "2009-03-10 00:00",
         "2000-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class C07VrId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_C07vrrpNotifications_ObjectIdentity = ObjectIdentity
c07vrrpNotifications = _C07vrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 0)
)
_C07vrrpOperations_ObjectIdentity = ObjectIdentity
c07vrrpOperations = _C07vrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1)
)
_C07vrrpNodeVersion_Type = Integer32
_C07vrrpNodeVersion_Object = MibScalar
c07vrrpNodeVersion = _C07vrrpNodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 1),
    _C07vrrpNodeVersion_Type()
)
c07vrrpNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpNodeVersion.setStatus("deprecated")


class _C07vrrpNotificationCntl_Type(Integer32):
    """Custom type c07vrrpNotificationCntl based on Integer32"""
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


_C07vrrpNotificationCntl_Type.__name__ = "Integer32"
_C07vrrpNotificationCntl_Object = MibScalar
c07vrrpNotificationCntl = _C07vrrpNotificationCntl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 2),
    _C07vrrpNotificationCntl_Type()
)
c07vrrpNotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c07vrrpNotificationCntl.setStatus("deprecated")
_C07vrrpOperTable_Object = MibTable
c07vrrpOperTable = _C07vrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3)
)
if mibBuilder.loadTexts:
    c07vrrpOperTable.setStatus("deprecated")
_C07vrrpOperEntry_Object = MibTableRow
c07vrrpOperEntry = _C07vrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1)
)
c07vrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-VRRP-07-MIB", "c07vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    c07vrrpOperEntry.setStatus("deprecated")
_C07vrrpOperVrId_Type = C07VrId
_C07vrrpOperVrId_Object = MibTableColumn
c07vrrpOperVrId = _C07vrrpOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 1),
    _C07vrrpOperVrId_Type()
)
c07vrrpOperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c07vrrpOperVrId.setStatus("deprecated")
_C07vrrpOperVirtualMacAddr_Type = MacAddress
_C07vrrpOperVirtualMacAddr_Object = MibTableColumn
c07vrrpOperVirtualMacAddr = _C07vrrpOperVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 2),
    _C07vrrpOperVirtualMacAddr_Type()
)
c07vrrpOperVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperVirtualMacAddr.setStatus("deprecated")


class _C07vrrpOperState_Type(Integer32):
    """Custom type c07vrrpOperState based on Integer32"""
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


_C07vrrpOperState_Type.__name__ = "Integer32"
_C07vrrpOperState_Object = MibTableColumn
c07vrrpOperState = _C07vrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 3),
    _C07vrrpOperState_Type()
)
c07vrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperState.setStatus("deprecated")


class _C07vrrpOperAdminState_Type(Integer32):
    """Custom type c07vrrpOperAdminState based on Integer32"""
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


_C07vrrpOperAdminState_Type.__name__ = "Integer32"
_C07vrrpOperAdminState_Object = MibTableColumn
c07vrrpOperAdminState = _C07vrrpOperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 4),
    _C07vrrpOperAdminState_Type()
)
c07vrrpOperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperAdminState.setStatus("deprecated")


class _C07vrrpOperPriority_Type(Integer32):
    """Custom type c07vrrpOperPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_C07vrrpOperPriority_Type.__name__ = "Integer32"
_C07vrrpOperPriority_Object = MibTableColumn
c07vrrpOperPriority = _C07vrrpOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 5),
    _C07vrrpOperPriority_Type()
)
c07vrrpOperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperPriority.setStatus("deprecated")


class _C07vrrpOperIpAddrCount_Type(Integer32):
    """Custom type c07vrrpOperIpAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_C07vrrpOperIpAddrCount_Type.__name__ = "Integer32"
_C07vrrpOperIpAddrCount_Object = MibTableColumn
c07vrrpOperIpAddrCount = _C07vrrpOperIpAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 6),
    _C07vrrpOperIpAddrCount_Type()
)
c07vrrpOperIpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperIpAddrCount.setStatus("deprecated")
_C07vrrpOperMasterIpAddr_Type = IpAddress
_C07vrrpOperMasterIpAddr_Object = MibTableColumn
c07vrrpOperMasterIpAddr = _C07vrrpOperMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 7),
    _C07vrrpOperMasterIpAddr_Type()
)
c07vrrpOperMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperMasterIpAddr.setStatus("deprecated")


class _C07vrrpOperPrimaryIpAddr_Type(IpAddress):
    """Custom type c07vrrpOperPrimaryIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_C07vrrpOperPrimaryIpAddr_Object = MibTableColumn
c07vrrpOperPrimaryIpAddr = _C07vrrpOperPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 8),
    _C07vrrpOperPrimaryIpAddr_Type()
)
c07vrrpOperPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperPrimaryIpAddr.setStatus("deprecated")


class _C07vrrpOperAuthType_Type(Integer32):
    """Custom type c07vrrpOperAuthType based on Integer32"""
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


_C07vrrpOperAuthType_Type.__name__ = "Integer32"
_C07vrrpOperAuthType_Object = MibTableColumn
c07vrrpOperAuthType = _C07vrrpOperAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 9),
    _C07vrrpOperAuthType_Type()
)
c07vrrpOperAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperAuthType.setStatus("deprecated")


class _C07vrrpOperAuthKey_Type(OctetString):
    """Custom type c07vrrpOperAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_C07vrrpOperAuthKey_Type.__name__ = "OctetString"
_C07vrrpOperAuthKey_Object = MibTableColumn
c07vrrpOperAuthKey = _C07vrrpOperAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 10),
    _C07vrrpOperAuthKey_Type()
)
c07vrrpOperAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperAuthKey.setStatus("deprecated")


class _C07vrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type c07vrrpOperAdvertisementInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_C07vrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_C07vrrpOperAdvertisementInterval_Object = MibTableColumn
c07vrrpOperAdvertisementInterval = _C07vrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 11),
    _C07vrrpOperAdvertisementInterval_Type()
)
c07vrrpOperAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperAdvertisementInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    c07vrrpOperAdvertisementInterval.setUnits("seconds")


class _C07vrrpOperPreemptMode_Type(TruthValue):
    """Custom type c07vrrpOperPreemptMode based on TruthValue"""


_C07vrrpOperPreemptMode_Object = MibTableColumn
c07vrrpOperPreemptMode = _C07vrrpOperPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 12),
    _C07vrrpOperPreemptMode_Type()
)
c07vrrpOperPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperPreemptMode.setStatus("deprecated")
_C07vrrpOperVirtualRouterUpTime_Type = TimeStamp
_C07vrrpOperVirtualRouterUpTime_Object = MibTableColumn
c07vrrpOperVirtualRouterUpTime = _C07vrrpOperVirtualRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 13),
    _C07vrrpOperVirtualRouterUpTime_Type()
)
c07vrrpOperVirtualRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperVirtualRouterUpTime.setStatus("deprecated")


class _C07vrrpOperProtocol_Type(Integer32):
    """Custom type c07vrrpOperProtocol based on Integer32"""
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


_C07vrrpOperProtocol_Type.__name__ = "Integer32"
_C07vrrpOperProtocol_Object = MibTableColumn
c07vrrpOperProtocol = _C07vrrpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 14),
    _C07vrrpOperProtocol_Type()
)
c07vrrpOperProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperProtocol.setStatus("deprecated")
_C07vrrpOperRowStatus_Type = RowStatus
_C07vrrpOperRowStatus_Object = MibTableColumn
c07vrrpOperRowStatus = _C07vrrpOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 3, 1, 15),
    _C07vrrpOperRowStatus_Type()
)
c07vrrpOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperRowStatus.setStatus("deprecated")
_C07vrrpAssoIpAddrTable_Object = MibTable
c07vrrpAssoIpAddrTable = _C07vrrpAssoIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 4)
)
if mibBuilder.loadTexts:
    c07vrrpAssoIpAddrTable.setStatus("deprecated")
_C07vrrpAssoIpAddrEntry_Object = MibTableRow
c07vrrpAssoIpAddrEntry = _C07vrrpAssoIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 4, 1)
)
c07vrrpAssoIpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-VRRP-07-MIB", "c07vrrpOperVrId"),
    (0, "CISCO-IETF-VRRP-07-MIB", "c07vrrpAssoIpAddr"),
)
if mibBuilder.loadTexts:
    c07vrrpAssoIpAddrEntry.setStatus("deprecated")
_C07vrrpAssoIpAddr_Type = IpAddress
_C07vrrpAssoIpAddr_Object = MibTableColumn
c07vrrpAssoIpAddr = _C07vrrpAssoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 4, 1, 1),
    _C07vrrpAssoIpAddr_Type()
)
c07vrrpAssoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c07vrrpAssoIpAddr.setStatus("deprecated")
_C07vrrpAssoIpAddrRowStatus_Type = RowStatus
_C07vrrpAssoIpAddrRowStatus_Object = MibTableColumn
c07vrrpAssoIpAddrRowStatus = _C07vrrpAssoIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 4, 1, 2),
    _C07vrrpAssoIpAddrRowStatus_Type()
)
c07vrrpAssoIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpAssoIpAddrRowStatus.setStatus("deprecated")
_C07vrrpTrapPacketSrc_Type = IpAddress
_C07vrrpTrapPacketSrc_Object = MibScalar
c07vrrpTrapPacketSrc = _C07vrrpTrapPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 5),
    _C07vrrpTrapPacketSrc_Type()
)
c07vrrpTrapPacketSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    c07vrrpTrapPacketSrc.setStatus("deprecated")


class _C07vrrpTrapAuthErrorType_Type(Integer32):
    """Custom type c07vrrpTrapAuthErrorType based on Integer32"""
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


_C07vrrpTrapAuthErrorType_Type.__name__ = "Integer32"
_C07vrrpTrapAuthErrorType_Object = MibScalar
c07vrrpTrapAuthErrorType = _C07vrrpTrapAuthErrorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 6),
    _C07vrrpTrapAuthErrorType_Type()
)
c07vrrpTrapAuthErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    c07vrrpTrapAuthErrorType.setStatus("deprecated")
_C07vrrpOperationsTable_Object = MibTable
c07vrrpOperationsTable = _C07vrrpOperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7)
)
if mibBuilder.loadTexts:
    c07vrrpOperationsTable.setStatus("current")
_C07vrrpOperationsEntry_Object = MibTableRow
c07vrrpOperationsEntry = _C07vrrpOperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1)
)
c07vrrpOperationsEntry.setIndexNames(
    (0, "CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsInetAddrType"),
    (0, "CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    c07vrrpOperationsEntry.setStatus("current")
_C07vrrpOperationsInetAddrType_Type = InetAddressType
_C07vrrpOperationsInetAddrType_Object = MibTableColumn
c07vrrpOperationsInetAddrType = _C07vrrpOperationsInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 1),
    _C07vrrpOperationsInetAddrType_Type()
)
c07vrrpOperationsInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c07vrrpOperationsInetAddrType.setStatus("current")
_C07vrrpOperationsVrId_Type = C07VrId
_C07vrrpOperationsVrId_Object = MibTableColumn
c07vrrpOperationsVrId = _C07vrrpOperationsVrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 2),
    _C07vrrpOperationsVrId_Type()
)
c07vrrpOperationsVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c07vrrpOperationsVrId.setStatus("current")
_C07vrrpOperationsVirtualMacAddr_Type = MacAddress
_C07vrrpOperationsVirtualMacAddr_Object = MibTableColumn
c07vrrpOperationsVirtualMacAddr = _C07vrrpOperationsVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 3),
    _C07vrrpOperationsVirtualMacAddr_Type()
)
c07vrrpOperationsVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperationsVirtualMacAddr.setStatus("current")


class _C07vrrpOperationsState_Type(Integer32):
    """Custom type c07vrrpOperationsState based on Integer32"""
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


_C07vrrpOperationsState_Type.__name__ = "Integer32"
_C07vrrpOperationsState_Object = MibTableColumn
c07vrrpOperationsState = _C07vrrpOperationsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 4),
    _C07vrrpOperationsState_Type()
)
c07vrrpOperationsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperationsState.setStatus("current")


class _C07vrrpOperationsPriority_Type(Unsigned32):
    """Custom type c07vrrpOperationsPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_C07vrrpOperationsPriority_Type.__name__ = "Unsigned32"
_C07vrrpOperationsPriority_Object = MibTableColumn
c07vrrpOperationsPriority = _C07vrrpOperationsPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 5),
    _C07vrrpOperationsPriority_Type()
)
c07vrrpOperationsPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperationsPriority.setStatus("current")


class _C07vrrpOperationsAddrCount_Type(Integer32):
    """Custom type c07vrrpOperationsAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_C07vrrpOperationsAddrCount_Type.__name__ = "Integer32"
_C07vrrpOperationsAddrCount_Object = MibTableColumn
c07vrrpOperationsAddrCount = _C07vrrpOperationsAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 6),
    _C07vrrpOperationsAddrCount_Type()
)
c07vrrpOperationsAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperationsAddrCount.setStatus("current")
_C07vrrpOperationsMasterIpAddr_Type = InetAddress
_C07vrrpOperationsMasterIpAddr_Object = MibTableColumn
c07vrrpOperationsMasterIpAddr = _C07vrrpOperationsMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 7),
    _C07vrrpOperationsMasterIpAddr_Type()
)
c07vrrpOperationsMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperationsMasterIpAddr.setStatus("current")
_C07vrrpOperationsPrimaryIpAddr_Type = InetAddress
_C07vrrpOperationsPrimaryIpAddr_Object = MibTableColumn
c07vrrpOperationsPrimaryIpAddr = _C07vrrpOperationsPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 8),
    _C07vrrpOperationsPrimaryIpAddr_Type()
)
c07vrrpOperationsPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperationsPrimaryIpAddr.setStatus("current")


class _C07vrrpOperationsAdvInterval_Type(TimeInterval):
    """Custom type c07vrrpOperationsAdvInterval based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_C07vrrpOperationsAdvInterval_Type.__name__ = "TimeInterval"
_C07vrrpOperationsAdvInterval_Object = MibTableColumn
c07vrrpOperationsAdvInterval = _C07vrrpOperationsAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 9),
    _C07vrrpOperationsAdvInterval_Type()
)
c07vrrpOperationsAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperationsAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    c07vrrpOperationsAdvInterval.setUnits("centiseconds")


class _C07vrrpOperationsPreemptMode_Type(TruthValue):
    """Custom type c07vrrpOperationsPreemptMode based on TruthValue"""


_C07vrrpOperationsPreemptMode_Object = MibTableColumn
c07vrrpOperationsPreemptMode = _C07vrrpOperationsPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 10),
    _C07vrrpOperationsPreemptMode_Type()
)
c07vrrpOperationsPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperationsPreemptMode.setStatus("current")


class _C07vrrpOperationsAcceptMode_Type(TruthValue):
    """Custom type c07vrrpOperationsAcceptMode based on TruthValue"""


_C07vrrpOperationsAcceptMode_Object = MibTableColumn
c07vrrpOperationsAcceptMode = _C07vrrpOperationsAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 11),
    _C07vrrpOperationsAcceptMode_Type()
)
c07vrrpOperationsAcceptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperationsAcceptMode.setStatus("current")
_C07vrrpOperationsUpTime_Type = TimeStamp
_C07vrrpOperationsUpTime_Object = MibTableColumn
c07vrrpOperationsUpTime = _C07vrrpOperationsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 12),
    _C07vrrpOperationsUpTime_Type()
)
c07vrrpOperationsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpOperationsUpTime.setStatus("current")


class _C07vrrpOperationsStorageType_Type(StorageType):
    """Custom type c07vrrpOperationsStorageType based on StorageType"""


_C07vrrpOperationsStorageType_Object = MibTableColumn
c07vrrpOperationsStorageType = _C07vrrpOperationsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 13),
    _C07vrrpOperationsStorageType_Type()
)
c07vrrpOperationsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperationsStorageType.setStatus("current")
_C07vrrpOperationsRowStatus_Type = RowStatus
_C07vrrpOperationsRowStatus_Object = MibTableColumn
c07vrrpOperationsRowStatus = _C07vrrpOperationsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 7, 1, 14),
    _C07vrrpOperationsRowStatus_Type()
)
c07vrrpOperationsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpOperationsRowStatus.setStatus("current")
_C07vrrpAssociatedIpAddrTable_Object = MibTable
c07vrrpAssociatedIpAddrTable = _C07vrrpAssociatedIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 8)
)
if mibBuilder.loadTexts:
    c07vrrpAssociatedIpAddrTable.setStatus("current")
_C07vrrpAssociatedIpAddrEntry_Object = MibTableRow
c07vrrpAssociatedIpAddrEntry = _C07vrrpAssociatedIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 8, 1)
)
c07vrrpAssociatedIpAddrEntry.setIndexNames(
    (0, "CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsInetAddrType"),
    (0, "CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-VRRP-07-MIB", "c07vrrpAssociatedIpAddr"),
)
if mibBuilder.loadTexts:
    c07vrrpAssociatedIpAddrEntry.setStatus("current")
_C07vrrpAssociatedIpAddr_Type = InetAddress
_C07vrrpAssociatedIpAddr_Object = MibTableColumn
c07vrrpAssociatedIpAddr = _C07vrrpAssociatedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 8, 1, 1),
    _C07vrrpAssociatedIpAddr_Type()
)
c07vrrpAssociatedIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c07vrrpAssociatedIpAddr.setStatus("current")


class _C07vrrpAssociatedStorageType_Type(StorageType):
    """Custom type c07vrrpAssociatedStorageType based on StorageType"""


_C07vrrpAssociatedStorageType_Object = MibTableColumn
c07vrrpAssociatedStorageType = _C07vrrpAssociatedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 8, 1, 2),
    _C07vrrpAssociatedStorageType_Type()
)
c07vrrpAssociatedStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpAssociatedStorageType.setStatus("current")
_C07vrrpAssociatedIpAddrRowStatus_Type = RowStatus
_C07vrrpAssociatedIpAddrRowStatus_Object = MibTableColumn
c07vrrpAssociatedIpAddrRowStatus = _C07vrrpAssociatedIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 8, 1, 3),
    _C07vrrpAssociatedIpAddrRowStatus_Type()
)
c07vrrpAssociatedIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c07vrrpAssociatedIpAddrRowStatus.setStatus("current")


class _C07vrrpNewMasterReason_Type(Integer32):
    """Custom type c07vrrpNewMasterReason based on Integer32"""
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


_C07vrrpNewMasterReason_Type.__name__ = "Integer32"
_C07vrrpNewMasterReason_Object = MibScalar
c07vrrpNewMasterReason = _C07vrrpNewMasterReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 9),
    _C07vrrpNewMasterReason_Type()
)
c07vrrpNewMasterReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    c07vrrpNewMasterReason.setStatus("current")


class _C07vrrpTrapProtoErrReason_Type(Integer32):
    """Custom type c07vrrpTrapProtoErrReason based on Integer32"""
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
          ("ipTtlError", 0),
          ("versionError", 1),
          ("vridError", 3))
    )


_C07vrrpTrapProtoErrReason_Type.__name__ = "Integer32"
_C07vrrpTrapProtoErrReason_Object = MibScalar
c07vrrpTrapProtoErrReason = _C07vrrpTrapProtoErrReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 10),
    _C07vrrpTrapProtoErrReason_Type()
)
c07vrrpTrapProtoErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    c07vrrpTrapProtoErrReason.setStatus("current")


class _C07vrrpTrapNewMasterCntl_Type(Integer32):
    """Custom type c07vrrpTrapNewMasterCntl based on Integer32"""
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


_C07vrrpTrapNewMasterCntl_Type.__name__ = "Integer32"
_C07vrrpTrapNewMasterCntl_Object = MibScalar
c07vrrpTrapNewMasterCntl = _C07vrrpTrapNewMasterCntl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 11),
    _C07vrrpTrapNewMasterCntl_Type()
)
c07vrrpTrapNewMasterCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c07vrrpTrapNewMasterCntl.setStatus("current")


class _C07vrrpTrapProtoErrorCntl_Type(Integer32):
    """Custom type c07vrrpTrapProtoErrorCntl based on Integer32"""
    defaultValue = 2

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


_C07vrrpTrapProtoErrorCntl_Type.__name__ = "Integer32"
_C07vrrpTrapProtoErrorCntl_Object = MibScalar
c07vrrpTrapProtoErrorCntl = _C07vrrpTrapProtoErrorCntl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 1, 12),
    _C07vrrpTrapProtoErrorCntl_Type()
)
c07vrrpTrapProtoErrorCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c07vrrpTrapProtoErrorCntl.setStatus("current")
_C07vrrpStatistics_ObjectIdentity = ObjectIdentity
c07vrrpStatistics = _C07vrrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2)
)
_C07vrrpRouterChecksumErrors_Type = Counter32
_C07vrrpRouterChecksumErrors_Object = MibScalar
c07vrrpRouterChecksumErrors = _C07vrrpRouterChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 1),
    _C07vrrpRouterChecksumErrors_Type()
)
c07vrrpRouterChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpRouterChecksumErrors.setStatus("current")
_C07vrrpRouterVersionErrors_Type = Counter32
_C07vrrpRouterVersionErrors_Object = MibScalar
c07vrrpRouterVersionErrors = _C07vrrpRouterVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 2),
    _C07vrrpRouterVersionErrors_Type()
)
c07vrrpRouterVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpRouterVersionErrors.setStatus("current")
_C07vrrpRouterVrIdErrors_Type = Counter32
_C07vrrpRouterVrIdErrors_Object = MibScalar
c07vrrpRouterVrIdErrors = _C07vrrpRouterVrIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 3),
    _C07vrrpRouterVrIdErrors_Type()
)
c07vrrpRouterVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpRouterVrIdErrors.setStatus("current")
_C07vrrpRouterStatsTable_Object = MibTable
c07vrrpRouterStatsTable = _C07vrrpRouterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4)
)
if mibBuilder.loadTexts:
    c07vrrpRouterStatsTable.setStatus("deprecated")
_C07vrrpRouterStatsEntry_Object = MibTableRow
c07vrrpRouterStatsEntry = _C07vrrpRouterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1)
)
if mibBuilder.loadTexts:
    c07vrrpRouterStatsEntry.setStatus("deprecated")
_C07vrrpStatsBecomeMaster_Type = Counter32
_C07vrrpStatsBecomeMaster_Object = MibTableColumn
c07vrrpStatsBecomeMaster = _C07vrrpStatsBecomeMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 1),
    _C07vrrpStatsBecomeMaster_Type()
)
c07vrrpStatsBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsBecomeMaster.setStatus("deprecated")
_C07vrrpStatsAdvertiseRcvd_Type = Counter32
_C07vrrpStatsAdvertiseRcvd_Object = MibTableColumn
c07vrrpStatsAdvertiseRcvd = _C07vrrpStatsAdvertiseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 2),
    _C07vrrpStatsAdvertiseRcvd_Type()
)
c07vrrpStatsAdvertiseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsAdvertiseRcvd.setStatus("deprecated")
_C07vrrpStatsAdvertiseIntervalErrors_Type = Counter32
_C07vrrpStatsAdvertiseIntervalErrors_Object = MibTableColumn
c07vrrpStatsAdvertiseIntervalErrors = _C07vrrpStatsAdvertiseIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 3),
    _C07vrrpStatsAdvertiseIntervalErrors_Type()
)
c07vrrpStatsAdvertiseIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsAdvertiseIntervalErrors.setStatus("deprecated")
_C07vrrpStatsAuthFailures_Type = Counter32
_C07vrrpStatsAuthFailures_Object = MibTableColumn
c07vrrpStatsAuthFailures = _C07vrrpStatsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 4),
    _C07vrrpStatsAuthFailures_Type()
)
c07vrrpStatsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsAuthFailures.setStatus("deprecated")
_C07vrrpStatsIpTtlErrors_Type = Counter32
_C07vrrpStatsIpTtlErrors_Object = MibTableColumn
c07vrrpStatsIpTtlErrors = _C07vrrpStatsIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 5),
    _C07vrrpStatsIpTtlErrors_Type()
)
c07vrrpStatsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsIpTtlErrors.setStatus("deprecated")
_C07vrrpStatsPriorityZeroPktsRcvd_Type = Counter32
_C07vrrpStatsPriorityZeroPktsRcvd_Object = MibTableColumn
c07vrrpStatsPriorityZeroPktsRcvd = _C07vrrpStatsPriorityZeroPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 6),
    _C07vrrpStatsPriorityZeroPktsRcvd_Type()
)
c07vrrpStatsPriorityZeroPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsPriorityZeroPktsRcvd.setStatus("deprecated")
_C07vrrpStatsPriorityZeroPktsSent_Type = Counter32
_C07vrrpStatsPriorityZeroPktsSent_Object = MibTableColumn
c07vrrpStatsPriorityZeroPktsSent = _C07vrrpStatsPriorityZeroPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 7),
    _C07vrrpStatsPriorityZeroPktsSent_Type()
)
c07vrrpStatsPriorityZeroPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsPriorityZeroPktsSent.setStatus("deprecated")
_C07vrrpStatsInvalidTypePktsRcvd_Type = Counter32
_C07vrrpStatsInvalidTypePktsRcvd_Object = MibTableColumn
c07vrrpStatsInvalidTypePktsRcvd = _C07vrrpStatsInvalidTypePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 8),
    _C07vrrpStatsInvalidTypePktsRcvd_Type()
)
c07vrrpStatsInvalidTypePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsInvalidTypePktsRcvd.setStatus("deprecated")
_C07vrrpStatsAddressListErrors_Type = Counter32
_C07vrrpStatsAddressListErrors_Object = MibTableColumn
c07vrrpStatsAddressListErrors = _C07vrrpStatsAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 9),
    _C07vrrpStatsAddressListErrors_Type()
)
c07vrrpStatsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsAddressListErrors.setStatus("deprecated")
_C07vrrpStatsInvalidAuthType_Type = Counter32
_C07vrrpStatsInvalidAuthType_Object = MibTableColumn
c07vrrpStatsInvalidAuthType = _C07vrrpStatsInvalidAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 10),
    _C07vrrpStatsInvalidAuthType_Type()
)
c07vrrpStatsInvalidAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsInvalidAuthType.setStatus("deprecated")
_C07vrrpStatsAuthTypeMismatch_Type = Counter32
_C07vrrpStatsAuthTypeMismatch_Object = MibTableColumn
c07vrrpStatsAuthTypeMismatch = _C07vrrpStatsAuthTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 11),
    _C07vrrpStatsAuthTypeMismatch_Type()
)
c07vrrpStatsAuthTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsAuthTypeMismatch.setStatus("deprecated")
_C07vrrpStatsPacketLengthErrors_Type = Counter32
_C07vrrpStatsPacketLengthErrors_Object = MibTableColumn
c07vrrpStatsPacketLengthErrors = _C07vrrpStatsPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 4, 1, 12),
    _C07vrrpStatsPacketLengthErrors_Type()
)
c07vrrpStatsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatsPacketLengthErrors.setStatus("deprecated")
_C07vrrpRouterStatisticsTable_Object = MibTable
c07vrrpRouterStatisticsTable = _C07vrrpRouterStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5)
)
if mibBuilder.loadTexts:
    c07vrrpRouterStatisticsTable.setStatus("current")
_C07vrrpRouterStatisticsEntry_Object = MibTableRow
c07vrrpRouterStatisticsEntry = _C07vrrpRouterStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1)
)
if mibBuilder.loadTexts:
    c07vrrpRouterStatisticsEntry.setStatus("current")
_C07vrrpStatisticsMasterTransitions_Type = Counter32
_C07vrrpStatisticsMasterTransitions_Object = MibTableColumn
c07vrrpStatisticsMasterTransitions = _C07vrrpStatisticsMasterTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 1),
    _C07vrrpStatisticsMasterTransitions_Type()
)
c07vrrpStatisticsMasterTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsMasterTransitions.setStatus("current")
_C07vrrpStatisticsRcvdAdvertisements_Type = Counter32
_C07vrrpStatisticsRcvdAdvertisements_Object = MibTableColumn
c07vrrpStatisticsRcvdAdvertisements = _C07vrrpStatisticsRcvdAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 2),
    _C07vrrpStatisticsRcvdAdvertisements_Type()
)
c07vrrpStatisticsRcvdAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsRcvdAdvertisements.setStatus("current")
_C07vrrpStatisticsAdvIntervalErrors_Type = Counter32
_C07vrrpStatisticsAdvIntervalErrors_Object = MibTableColumn
c07vrrpStatisticsAdvIntervalErrors = _C07vrrpStatisticsAdvIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 3),
    _C07vrrpStatisticsAdvIntervalErrors_Type()
)
c07vrrpStatisticsAdvIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsAdvIntervalErrors.setStatus("current")
_C07vrrpStatisticsIpTtlErrors_Type = Counter32
_C07vrrpStatisticsIpTtlErrors_Object = MibTableColumn
c07vrrpStatisticsIpTtlErrors = _C07vrrpStatisticsIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 4),
    _C07vrrpStatisticsIpTtlErrors_Type()
)
c07vrrpStatisticsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsIpTtlErrors.setStatus("current")
_C07vrrpStatisticsRcvdPriZeroPackets_Type = Counter32
_C07vrrpStatisticsRcvdPriZeroPackets_Object = MibTableColumn
c07vrrpStatisticsRcvdPriZeroPackets = _C07vrrpStatisticsRcvdPriZeroPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 5),
    _C07vrrpStatisticsRcvdPriZeroPackets_Type()
)
c07vrrpStatisticsRcvdPriZeroPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsRcvdPriZeroPackets.setStatus("current")
_C07vrrpStatisticsSentPriZeroPackets_Type = Counter32
_C07vrrpStatisticsSentPriZeroPackets_Object = MibTableColumn
c07vrrpStatisticsSentPriZeroPackets = _C07vrrpStatisticsSentPriZeroPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 6),
    _C07vrrpStatisticsSentPriZeroPackets_Type()
)
c07vrrpStatisticsSentPriZeroPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsSentPriZeroPackets.setStatus("current")
_C07vrrpStatisticsRcvdInvalidTypePkts_Type = Counter32
_C07vrrpStatisticsRcvdInvalidTypePkts_Object = MibTableColumn
c07vrrpStatisticsRcvdInvalidTypePkts = _C07vrrpStatisticsRcvdInvalidTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 7),
    _C07vrrpStatisticsRcvdInvalidTypePkts_Type()
)
c07vrrpStatisticsRcvdInvalidTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsRcvdInvalidTypePkts.setStatus("current")
_C07vrrpStatisticsAddressListErrors_Type = Counter32
_C07vrrpStatisticsAddressListErrors_Object = MibTableColumn
c07vrrpStatisticsAddressListErrors = _C07vrrpStatisticsAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 8),
    _C07vrrpStatisticsAddressListErrors_Type()
)
c07vrrpStatisticsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsAddressListErrors.setStatus("current")
_C07vrrpStatisticsPacketLengthErrors_Type = Counter32
_C07vrrpStatisticsPacketLengthErrors_Object = MibTableColumn
c07vrrpStatisticsPacketLengthErrors = _C07vrrpStatisticsPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 9),
    _C07vrrpStatisticsPacketLengthErrors_Type()
)
c07vrrpStatisticsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsPacketLengthErrors.setStatus("current")
_C07vrrpStatisticsRcvdInvalidAuthentications_Type = Counter32
_C07vrrpStatisticsRcvdInvalidAuthentications_Object = MibTableColumn
c07vrrpStatisticsRcvdInvalidAuthentications = _C07vrrpStatisticsRcvdInvalidAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 10),
    _C07vrrpStatisticsRcvdInvalidAuthentications_Type()
)
c07vrrpStatisticsRcvdInvalidAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsRcvdInvalidAuthentications.setStatus("current")
_C07vrrpStatisticsDiscontinuityTime_Type = TimeStamp
_C07vrrpStatisticsDiscontinuityTime_Object = MibTableColumn
c07vrrpStatisticsDiscontinuityTime = _C07vrrpStatisticsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 11),
    _C07vrrpStatisticsDiscontinuityTime_Type()
)
c07vrrpStatisticsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsDiscontinuityTime.setStatus("current")
_C07vrrpStatisticsRefreshRate_Type = Unsigned32
_C07vrrpStatisticsRefreshRate_Object = MibTableColumn
c07vrrpStatisticsRefreshRate = _C07vrrpStatisticsRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 2, 5, 1, 12),
    _C07vrrpStatisticsRefreshRate_Type()
)
c07vrrpStatisticsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c07vrrpStatisticsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    c07vrrpStatisticsRefreshRate.setUnits("milli-seconds")
_C07vrrpConformance_ObjectIdentity = ObjectIdentity
c07vrrpConformance = _C07vrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3)
)
_C07vrrpMIBCompliances_ObjectIdentity = ObjectIdentity
c07vrrpMIBCompliances = _C07vrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 1)
)
_C07vrrpMIBGroups_ObjectIdentity = ObjectIdentity
c07vrrpMIBGroups = _C07vrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2)
)
c07vrrpOperEntry.registerAugmentions(
    ("CISCO-IETF-VRRP-07-MIB",
     "c07vrrpRouterStatsEntry")
)
c07vrrpRouterStatsEntry.setIndexNames(*c07vrrpOperEntry.getIndexNames())
c07vrrpOperationsEntry.registerAugmentions(
    ("CISCO-IETF-VRRP-07-MIB",
     "c07vrrpRouterStatisticsEntry")
)
c07vrrpRouterStatisticsEntry.setIndexNames(*c07vrrpOperationsEntry.getIndexNames())

# Managed Objects groups

c07vrrpOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2, 1)
)
c07vrrpOperGroup.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpNodeVersion"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpNotificationCntl"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperVirtualMacAddr"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperState"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperAdminState"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperPriority"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperIpAddrCount"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperMasterIpAddr"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperPrimaryIpAddr"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperAuthType"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperAuthKey"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperAdvertisementInterval"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperPreemptMode"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperVirtualRouterUpTime"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperProtocol"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperRowStatus"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpAssoIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    c07vrrpOperGroup.setStatus("deprecated")

c07vrrpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2, 2)
)
c07vrrpStatsGroup.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpRouterChecksumErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpRouterVersionErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpRouterVrIdErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsBecomeMaster"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsAdvertiseRcvd"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsAdvertiseIntervalErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsAuthFailures"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsIpTtlErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsPriorityZeroPktsRcvd"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsPriorityZeroPktsSent"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsInvalidTypePktsRcvd"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsAddressListErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsInvalidAuthType"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsAuthTypeMismatch"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatsPacketLengthErrors"))
)
if mibBuilder.loadTexts:
    c07vrrpStatsGroup.setStatus("deprecated")

c07vrrpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2, 3)
)
c07vrrpTrapGroup.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapPacketSrc"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapAuthErrorType"))
)
if mibBuilder.loadTexts:
    c07vrrpTrapGroup.setStatus("deprecated")

c07vrrpOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2, 5)
)
c07vrrpOperationsGroup.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapNewMasterCntl"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapProtoErrorCntl"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsVirtualMacAddr"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsState"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsPriority"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsMasterIpAddr"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsAdvInterval"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsPreemptMode"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsAcceptMode"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsUpTime"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsStorageType"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsRowStatus"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsAddrCount"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsPrimaryIpAddr"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpAssociatedStorageType"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpAssociatedIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    c07vrrpOperationsGroup.setStatus("current")

c07vrrpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2, 6)
)
c07vrrpStatisticsGroup.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpRouterChecksumErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpRouterVersionErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpRouterVrIdErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsMasterTransitions"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsRcvdAdvertisements"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsAdvIntervalErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsRcvdPriZeroPackets"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsSentPriZeroPackets"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsRcvdInvalidTypePkts"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsIpTtlErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsAddressListErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsPacketLengthErrors"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsRcvdInvalidAuthentications"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsDiscontinuityTime"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpStatisticsRefreshRate"))
)
if mibBuilder.loadTexts:
    c07vrrpStatisticsGroup.setStatus("current")

c07vrrpTrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2, 8)
)
c07vrrpTrapInfoGroup.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapProtoErrReason"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpNewMasterReason"))
)
if mibBuilder.loadTexts:
    c07vrrpTrapInfoGroup.setStatus("current")


# Notification objects

c07vrrpTrapNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 0, 1)
)
c07vrrpTrapNewMaster.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpOperationsMasterIpAddr"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpNewMasterReason"))
)
if mibBuilder.loadTexts:
    c07vrrpTrapNewMaster.setStatus(
        "current"
    )

c07vrrpTrapAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 0, 2)
)
c07vrrpTrapAuthFailure.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapPacketSrc"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapAuthErrorType"))
)
if mibBuilder.loadTexts:
    c07vrrpTrapAuthFailure.setStatus(
        "deprecated"
    )

c07vrrpTrapProtoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 0, 3)
)
c07vrrpTrapProtoError.setObjects(
    ("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapProtoErrReason")
)
if mibBuilder.loadTexts:
    c07vrrpTrapProtoError.setStatus(
        "current"
    )


# Notifications groups

c07vrrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2, 4)
)
c07vrrpNotificationGroup.setObjects(
    ("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapAuthFailure")
)
if mibBuilder.loadTexts:
    c07vrrpNotificationGroup.setStatus(
        "deprecated"
    )

c07vrrpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 2, 9)
)
c07vrrpNotificationsGroup.setObjects(
      *(("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapNewMaster"),
        ("CISCO-IETF-VRRP-07-MIB", "c07vrrpTrapProtoError"))
)
if mibBuilder.loadTexts:
    c07vrrpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

c07vrrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 1, 1)
)
if mibBuilder.loadTexts:
    c07vrrpMIBCompliance.setStatus(
        "deprecated"
    )

c07vrrpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 1, 2)
)
if mibBuilder.loadTexts:
    c07vrrpModuleFullCompliance.setStatus(
        "current"
    )

c07vrrpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 143, 3, 1, 3)
)
if mibBuilder.loadTexts:
    c07vrrpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-VRRP-07-MIB",
    **{"C07VrId": C07VrId,
       "ciscoVrrp07MIB": ciscoVrrp07MIB,
       "c07vrrpNotifications": c07vrrpNotifications,
       "c07vrrpTrapNewMaster": c07vrrpTrapNewMaster,
       "c07vrrpTrapAuthFailure": c07vrrpTrapAuthFailure,
       "c07vrrpTrapProtoError": c07vrrpTrapProtoError,
       "c07vrrpOperations": c07vrrpOperations,
       "c07vrrpNodeVersion": c07vrrpNodeVersion,
       "c07vrrpNotificationCntl": c07vrrpNotificationCntl,
       "c07vrrpOperTable": c07vrrpOperTable,
       "c07vrrpOperEntry": c07vrrpOperEntry,
       "c07vrrpOperVrId": c07vrrpOperVrId,
       "c07vrrpOperVirtualMacAddr": c07vrrpOperVirtualMacAddr,
       "c07vrrpOperState": c07vrrpOperState,
       "c07vrrpOperAdminState": c07vrrpOperAdminState,
       "c07vrrpOperPriority": c07vrrpOperPriority,
       "c07vrrpOperIpAddrCount": c07vrrpOperIpAddrCount,
       "c07vrrpOperMasterIpAddr": c07vrrpOperMasterIpAddr,
       "c07vrrpOperPrimaryIpAddr": c07vrrpOperPrimaryIpAddr,
       "c07vrrpOperAuthType": c07vrrpOperAuthType,
       "c07vrrpOperAuthKey": c07vrrpOperAuthKey,
       "c07vrrpOperAdvertisementInterval": c07vrrpOperAdvertisementInterval,
       "c07vrrpOperPreemptMode": c07vrrpOperPreemptMode,
       "c07vrrpOperVirtualRouterUpTime": c07vrrpOperVirtualRouterUpTime,
       "c07vrrpOperProtocol": c07vrrpOperProtocol,
       "c07vrrpOperRowStatus": c07vrrpOperRowStatus,
       "c07vrrpAssoIpAddrTable": c07vrrpAssoIpAddrTable,
       "c07vrrpAssoIpAddrEntry": c07vrrpAssoIpAddrEntry,
       "c07vrrpAssoIpAddr": c07vrrpAssoIpAddr,
       "c07vrrpAssoIpAddrRowStatus": c07vrrpAssoIpAddrRowStatus,
       "c07vrrpTrapPacketSrc": c07vrrpTrapPacketSrc,
       "c07vrrpTrapAuthErrorType": c07vrrpTrapAuthErrorType,
       "c07vrrpOperationsTable": c07vrrpOperationsTable,
       "c07vrrpOperationsEntry": c07vrrpOperationsEntry,
       "c07vrrpOperationsInetAddrType": c07vrrpOperationsInetAddrType,
       "c07vrrpOperationsVrId": c07vrrpOperationsVrId,
       "c07vrrpOperationsVirtualMacAddr": c07vrrpOperationsVirtualMacAddr,
       "c07vrrpOperationsState": c07vrrpOperationsState,
       "c07vrrpOperationsPriority": c07vrrpOperationsPriority,
       "c07vrrpOperationsAddrCount": c07vrrpOperationsAddrCount,
       "c07vrrpOperationsMasterIpAddr": c07vrrpOperationsMasterIpAddr,
       "c07vrrpOperationsPrimaryIpAddr": c07vrrpOperationsPrimaryIpAddr,
       "c07vrrpOperationsAdvInterval": c07vrrpOperationsAdvInterval,
       "c07vrrpOperationsPreemptMode": c07vrrpOperationsPreemptMode,
       "c07vrrpOperationsAcceptMode": c07vrrpOperationsAcceptMode,
       "c07vrrpOperationsUpTime": c07vrrpOperationsUpTime,
       "c07vrrpOperationsStorageType": c07vrrpOperationsStorageType,
       "c07vrrpOperationsRowStatus": c07vrrpOperationsRowStatus,
       "c07vrrpAssociatedIpAddrTable": c07vrrpAssociatedIpAddrTable,
       "c07vrrpAssociatedIpAddrEntry": c07vrrpAssociatedIpAddrEntry,
       "c07vrrpAssociatedIpAddr": c07vrrpAssociatedIpAddr,
       "c07vrrpAssociatedStorageType": c07vrrpAssociatedStorageType,
       "c07vrrpAssociatedIpAddrRowStatus": c07vrrpAssociatedIpAddrRowStatus,
       "c07vrrpNewMasterReason": c07vrrpNewMasterReason,
       "c07vrrpTrapProtoErrReason": c07vrrpTrapProtoErrReason,
       "c07vrrpTrapNewMasterCntl": c07vrrpTrapNewMasterCntl,
       "c07vrrpTrapProtoErrorCntl": c07vrrpTrapProtoErrorCntl,
       "c07vrrpStatistics": c07vrrpStatistics,
       "c07vrrpRouterChecksumErrors": c07vrrpRouterChecksumErrors,
       "c07vrrpRouterVersionErrors": c07vrrpRouterVersionErrors,
       "c07vrrpRouterVrIdErrors": c07vrrpRouterVrIdErrors,
       "c07vrrpRouterStatsTable": c07vrrpRouterStatsTable,
       "c07vrrpRouterStatsEntry": c07vrrpRouterStatsEntry,
       "c07vrrpStatsBecomeMaster": c07vrrpStatsBecomeMaster,
       "c07vrrpStatsAdvertiseRcvd": c07vrrpStatsAdvertiseRcvd,
       "c07vrrpStatsAdvertiseIntervalErrors": c07vrrpStatsAdvertiseIntervalErrors,
       "c07vrrpStatsAuthFailures": c07vrrpStatsAuthFailures,
       "c07vrrpStatsIpTtlErrors": c07vrrpStatsIpTtlErrors,
       "c07vrrpStatsPriorityZeroPktsRcvd": c07vrrpStatsPriorityZeroPktsRcvd,
       "c07vrrpStatsPriorityZeroPktsSent": c07vrrpStatsPriorityZeroPktsSent,
       "c07vrrpStatsInvalidTypePktsRcvd": c07vrrpStatsInvalidTypePktsRcvd,
       "c07vrrpStatsAddressListErrors": c07vrrpStatsAddressListErrors,
       "c07vrrpStatsInvalidAuthType": c07vrrpStatsInvalidAuthType,
       "c07vrrpStatsAuthTypeMismatch": c07vrrpStatsAuthTypeMismatch,
       "c07vrrpStatsPacketLengthErrors": c07vrrpStatsPacketLengthErrors,
       "c07vrrpRouterStatisticsTable": c07vrrpRouterStatisticsTable,
       "c07vrrpRouterStatisticsEntry": c07vrrpRouterStatisticsEntry,
       "c07vrrpStatisticsMasterTransitions": c07vrrpStatisticsMasterTransitions,
       "c07vrrpStatisticsRcvdAdvertisements": c07vrrpStatisticsRcvdAdvertisements,
       "c07vrrpStatisticsAdvIntervalErrors": c07vrrpStatisticsAdvIntervalErrors,
       "c07vrrpStatisticsIpTtlErrors": c07vrrpStatisticsIpTtlErrors,
       "c07vrrpStatisticsRcvdPriZeroPackets": c07vrrpStatisticsRcvdPriZeroPackets,
       "c07vrrpStatisticsSentPriZeroPackets": c07vrrpStatisticsSentPriZeroPackets,
       "c07vrrpStatisticsRcvdInvalidTypePkts": c07vrrpStatisticsRcvdInvalidTypePkts,
       "c07vrrpStatisticsAddressListErrors": c07vrrpStatisticsAddressListErrors,
       "c07vrrpStatisticsPacketLengthErrors": c07vrrpStatisticsPacketLengthErrors,
       "c07vrrpStatisticsRcvdInvalidAuthentications": c07vrrpStatisticsRcvdInvalidAuthentications,
       "c07vrrpStatisticsDiscontinuityTime": c07vrrpStatisticsDiscontinuityTime,
       "c07vrrpStatisticsRefreshRate": c07vrrpStatisticsRefreshRate,
       "c07vrrpConformance": c07vrrpConformance,
       "c07vrrpMIBCompliances": c07vrrpMIBCompliances,
       "c07vrrpMIBCompliance": c07vrrpMIBCompliance,
       "c07vrrpModuleFullCompliance": c07vrrpModuleFullCompliance,
       "c07vrrpModuleReadOnlyCompliance": c07vrrpModuleReadOnlyCompliance,
       "c07vrrpMIBGroups": c07vrrpMIBGroups,
       "c07vrrpOperGroup": c07vrrpOperGroup,
       "c07vrrpStatsGroup": c07vrrpStatsGroup,
       "c07vrrpTrapGroup": c07vrrpTrapGroup,
       "c07vrrpNotificationGroup": c07vrrpNotificationGroup,
       "c07vrrpOperationsGroup": c07vrrpOperationsGroup,
       "c07vrrpStatisticsGroup": c07vrrpStatisticsGroup,
       "c07vrrpTrapInfoGroup": c07vrrpTrapInfoGroup,
       "c07vrrpNotificationsGroup": c07vrrpNotificationsGroup}
)
