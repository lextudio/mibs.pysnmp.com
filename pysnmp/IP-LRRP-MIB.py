# SNMP MIB module (IP-LRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IP-LRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:34 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cjnLrrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnLrrpGlobalGroup_ObjectIdentity = ObjectIdentity
cjnLrrpGlobalGroup = _CjnLrrpGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 1)
)


class _CjnLrrpEnabled_Type(Integer32):
    """Custom type cjnLrrpEnabled based on Integer32"""
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


_CjnLrrpEnabled_Type.__name__ = "Integer32"
_CjnLrrpEnabled_Object = MibScalar
cjnLrrpEnabled = _CjnLrrpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 1, 1),
    _CjnLrrpEnabled_Type()
)
cjnLrrpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpEnabled.setStatus("current")


class _CjnLrrpGlobalStatsReset_Type(Integer32):
    """Custom type cjnLrrpGlobalStatsReset based on Integer32"""
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


_CjnLrrpGlobalStatsReset_Type.__name__ = "Integer32"
_CjnLrrpGlobalStatsReset_Object = MibScalar
cjnLrrpGlobalStatsReset = _CjnLrrpGlobalStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 1, 2),
    _CjnLrrpGlobalStatsReset_Type()
)
cjnLrrpGlobalStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpGlobalStatsReset.setStatus("current")
_CjnLrrpGblStatsGroup_ObjectIdentity = ObjectIdentity
cjnLrrpGblStatsGroup = _CjnLrrpGblStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 2)
)
_CjnLrrpRouterChecksumErrors_Type = Integer32
_CjnLrrpRouterChecksumErrors_Object = MibScalar
cjnLrrpRouterChecksumErrors = _CjnLrrpRouterChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 2, 1),
    _CjnLrrpRouterChecksumErrors_Type()
)
cjnLrrpRouterChecksumErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpRouterChecksumErrors.setStatus("current")
_CjnLrrpRouterVersionErrors_Type = Integer32
_CjnLrrpRouterVersionErrors_Object = MibScalar
cjnLrrpRouterVersionErrors = _CjnLrrpRouterVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 2, 2),
    _CjnLrrpRouterVersionErrors_Type()
)
cjnLrrpRouterVersionErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpRouterVersionErrors.setStatus("current")
_CjnLrrpRouterVrIdErrors_Type = Integer32
_CjnLrrpRouterVrIdErrors_Object = MibScalar
cjnLrrpRouterVrIdErrors = _CjnLrrpRouterVrIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 2, 3),
    _CjnLrrpRouterVrIdErrors_Type()
)
cjnLrrpRouterVrIdErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpRouterVrIdErrors.setStatus("current")
_CjnLrrpRtrStatsGroup_ObjectIdentity = ObjectIdentity
cjnLrrpRtrStatsGroup = _CjnLrrpRtrStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3)
)
_CjnLrrpRouterStatsTable_Object = MibTable
cjnLrrpRouterStatsTable = _CjnLrrpRouterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1)
)
if mibBuilder.loadTexts:
    cjnLrrpRouterStatsTable.setStatus("current")
_CjnLrrpRouterStatsEntry_Object = MibTableRow
cjnLrrpRouterStatsEntry = _CjnLrrpRouterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cjnLrrpRouterStatsEntry.setStatus("current")
_CjnLrrpStatsBecomeMaster_Type = Integer32
_CjnLrrpStatsBecomeMaster_Object = MibTableColumn
cjnLrrpStatsBecomeMaster = _CjnLrrpStatsBecomeMaster_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 1),
    _CjnLrrpStatsBecomeMaster_Type()
)
cjnLrrpStatsBecomeMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsBecomeMaster.setStatus("current")
_CjnLrrpStatsAdvertiseRcvd_Type = Integer32
_CjnLrrpStatsAdvertiseRcvd_Object = MibTableColumn
cjnLrrpStatsAdvertiseRcvd = _CjnLrrpStatsAdvertiseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 2),
    _CjnLrrpStatsAdvertiseRcvd_Type()
)
cjnLrrpStatsAdvertiseRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsAdvertiseRcvd.setStatus("current")
_CjnLrrpStatsAdvertiseIntervalErrors_Type = Integer32
_CjnLrrpStatsAdvertiseIntervalErrors_Object = MibTableColumn
cjnLrrpStatsAdvertiseIntervalErrors = _CjnLrrpStatsAdvertiseIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 6),
    _CjnLrrpStatsAdvertiseIntervalErrors_Type()
)
cjnLrrpStatsAdvertiseIntervalErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsAdvertiseIntervalErrors.setStatus("current")
_CjnLrrpStatsAuthFailures_Type = Integer32
_CjnLrrpStatsAuthFailures_Object = MibTableColumn
cjnLrrpStatsAuthFailures = _CjnLrrpStatsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 7),
    _CjnLrrpStatsAuthFailures_Type()
)
cjnLrrpStatsAuthFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsAuthFailures.setStatus("current")
_CjnLrrpStatsIpTtlErrors_Type = Integer32
_CjnLrrpStatsIpTtlErrors_Object = MibTableColumn
cjnLrrpStatsIpTtlErrors = _CjnLrrpStatsIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 8),
    _CjnLrrpStatsIpTtlErrors_Type()
)
cjnLrrpStatsIpTtlErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsIpTtlErrors.setStatus("current")
_CjnLrrpStatsPriorityZeroPktsRcvd_Type = Integer32
_CjnLrrpStatsPriorityZeroPktsRcvd_Object = MibTableColumn
cjnLrrpStatsPriorityZeroPktsRcvd = _CjnLrrpStatsPriorityZeroPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 9),
    _CjnLrrpStatsPriorityZeroPktsRcvd_Type()
)
cjnLrrpStatsPriorityZeroPktsRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsPriorityZeroPktsRcvd.setStatus("current")
_CjnLrrpStatsPriorityZeroPktsSent_Type = Integer32
_CjnLrrpStatsPriorityZeroPktsSent_Object = MibTableColumn
cjnLrrpStatsPriorityZeroPktsSent = _CjnLrrpStatsPriorityZeroPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 10),
    _CjnLrrpStatsPriorityZeroPktsSent_Type()
)
cjnLrrpStatsPriorityZeroPktsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsPriorityZeroPktsSent.setStatus("current")
_CjnLrrpStatsInvalidTypePktsRcvd_Type = Integer32
_CjnLrrpStatsInvalidTypePktsRcvd_Object = MibTableColumn
cjnLrrpStatsInvalidTypePktsRcvd = _CjnLrrpStatsInvalidTypePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 11),
    _CjnLrrpStatsInvalidTypePktsRcvd_Type()
)
cjnLrrpStatsInvalidTypePktsRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsInvalidTypePktsRcvd.setStatus("current")
_CjnLrrpStatsAddressListErrors_Type = Integer32
_CjnLrrpStatsAddressListErrors_Object = MibTableColumn
cjnLrrpStatsAddressListErrors = _CjnLrrpStatsAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 12),
    _CjnLrrpStatsAddressListErrors_Type()
)
cjnLrrpStatsAddressListErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsAddressListErrors.setStatus("current")
_CjnLrrpStatsInvalidAuthType_Type = Integer32
_CjnLrrpStatsInvalidAuthType_Object = MibTableColumn
cjnLrrpStatsInvalidAuthType = _CjnLrrpStatsInvalidAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 13),
    _CjnLrrpStatsInvalidAuthType_Type()
)
cjnLrrpStatsInvalidAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsInvalidAuthType.setStatus("current")
_CjnLrrpStatsAuthTypeMismatch_Type = Integer32
_CjnLrrpStatsAuthTypeMismatch_Object = MibTableColumn
cjnLrrpStatsAuthTypeMismatch = _CjnLrrpStatsAuthTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 14),
    _CjnLrrpStatsAuthTypeMismatch_Type()
)
cjnLrrpStatsAuthTypeMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsAuthTypeMismatch.setStatus("current")
_CjnLrrpStatsPacketLengthErrors_Type = Integer32
_CjnLrrpStatsPacketLengthErrors_Object = MibTableColumn
cjnLrrpStatsPacketLengthErrors = _CjnLrrpStatsPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 3, 1, 1, 15),
    _CjnLrrpStatsPacketLengthErrors_Type()
)
cjnLrrpStatsPacketLengthErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpStatsPacketLengthErrors.setStatus("current")
_CjnLrrpRtrGroup_ObjectIdentity = ObjectIdentity
cjnLrrpRtrGroup = _CjnLrrpRtrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4)
)
_CjnLrrpOperTable_Object = MibTable
cjnLrrpOperTable = _CjnLrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1)
)
if mibBuilder.loadTexts:
    cjnLrrpOperTable.setStatus("current")
_CjnLrrpOperEntry_Object = MibTableRow
cjnLrrpOperEntry = _CjnLrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1)
)
cjnLrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IP-LRRP-MIB", "cjnLrrpOperVrId"),
)
if mibBuilder.loadTexts:
    cjnLrrpOperEntry.setStatus("current")


class _CjnLrrpOperVrId_Type(Integer32):
    """Custom type cjnLrrpOperVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CjnLrrpOperVrId_Type.__name__ = "Integer32"
_CjnLrrpOperVrId_Object = MibTableColumn
cjnLrrpOperVrId = _CjnLrrpOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 1),
    _CjnLrrpOperVrId_Type()
)
cjnLrrpOperVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnLrrpOperVrId.setStatus("current")
_CjnLrrpOperVirtualMacAddr_Type = MacAddress
_CjnLrrpOperVirtualMacAddr_Object = MibTableColumn
cjnLrrpOperVirtualMacAddr = _CjnLrrpOperVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 2),
    _CjnLrrpOperVirtualMacAddr_Type()
)
cjnLrrpOperVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnLrrpOperVirtualMacAddr.setStatus("current")


class _CjnLrrpOperState_Type(Integer32):
    """Custom type cjnLrrpOperState based on Integer32"""
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


_CjnLrrpOperState_Type.__name__ = "Integer32"
_CjnLrrpOperState_Object = MibTableColumn
cjnLrrpOperState = _CjnLrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 3),
    _CjnLrrpOperState_Type()
)
cjnLrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnLrrpOperState.setStatus("current")


class _CjnLrrpOperAdminState_Type(Integer32):
    """Custom type cjnLrrpOperAdminState based on Integer32"""
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


_CjnLrrpOperAdminState_Type.__name__ = "Integer32"
_CjnLrrpOperAdminState_Object = MibTableColumn
cjnLrrpOperAdminState = _CjnLrrpOperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 4),
    _CjnLrrpOperAdminState_Type()
)
cjnLrrpOperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperAdminState.setStatus("current")


class _CjnLrrpOperPriority_Type(Integer32):
    """Custom type cjnLrrpOperPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CjnLrrpOperPriority_Type.__name__ = "Integer32"
_CjnLrrpOperPriority_Object = MibTableColumn
cjnLrrpOperPriority = _CjnLrrpOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 5),
    _CjnLrrpOperPriority_Type()
)
cjnLrrpOperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperPriority.setStatus("current")


class _CjnLrrpOperIpAddrCount_Type(Integer32):
    """Custom type cjnLrrpOperIpAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CjnLrrpOperIpAddrCount_Type.__name__ = "Integer32"
_CjnLrrpOperIpAddrCount_Object = MibTableColumn
cjnLrrpOperIpAddrCount = _CjnLrrpOperIpAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 6),
    _CjnLrrpOperIpAddrCount_Type()
)
cjnLrrpOperIpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnLrrpOperIpAddrCount.setStatus("current")
_CjnLrrpOperMasterIpAddr_Type = IpAddress
_CjnLrrpOperMasterIpAddr_Object = MibTableColumn
cjnLrrpOperMasterIpAddr = _CjnLrrpOperMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 7),
    _CjnLrrpOperMasterIpAddr_Type()
)
cjnLrrpOperMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnLrrpOperMasterIpAddr.setStatus("current")


class _CjnLrrpOperPrimaryIpAddr_Type(IpAddress):
    """Custom type cjnLrrpOperPrimaryIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CjnLrrpOperPrimaryIpAddr_Object = MibTableColumn
cjnLrrpOperPrimaryIpAddr = _CjnLrrpOperPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 8),
    _CjnLrrpOperPrimaryIpAddr_Type()
)
cjnLrrpOperPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperPrimaryIpAddr.setStatus("current")


class _CjnLrrpOperAuthType_Type(Integer32):
    """Custom type cjnLrrpOperAuthType based on Integer32"""
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


_CjnLrrpOperAuthType_Type.__name__ = "Integer32"
_CjnLrrpOperAuthType_Object = MibTableColumn
cjnLrrpOperAuthType = _CjnLrrpOperAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 9),
    _CjnLrrpOperAuthType_Type()
)
cjnLrrpOperAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperAuthType.setStatus("current")


class _CjnLrrpOperAuthKey_Type(OctetString):
    """Custom type cjnLrrpOperAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CjnLrrpOperAuthKey_Type.__name__ = "OctetString"
_CjnLrrpOperAuthKey_Object = MibTableColumn
cjnLrrpOperAuthKey = _CjnLrrpOperAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 10),
    _CjnLrrpOperAuthKey_Type()
)
cjnLrrpOperAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperAuthKey.setStatus("current")


class _CjnLrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type cjnLrrpOperAdvertisementInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CjnLrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_CjnLrrpOperAdvertisementInterval_Object = MibTableColumn
cjnLrrpOperAdvertisementInterval = _CjnLrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 11),
    _CjnLrrpOperAdvertisementInterval_Type()
)
cjnLrrpOperAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperAdvertisementInterval.setStatus("current")


class _CjnLrrpOperPreemptMode_Type(TruthValue):
    """Custom type cjnLrrpOperPreemptMode based on TruthValue"""


_CjnLrrpOperPreemptMode_Object = MibTableColumn
cjnLrrpOperPreemptMode = _CjnLrrpOperPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 12),
    _CjnLrrpOperPreemptMode_Type()
)
cjnLrrpOperPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperPreemptMode.setStatus("current")
_CjnLrrpOperVirtualRouterUpTime_Type = TimeStamp
_CjnLrrpOperVirtualRouterUpTime_Object = MibTableColumn
cjnLrrpOperVirtualRouterUpTime = _CjnLrrpOperVirtualRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 13),
    _CjnLrrpOperVirtualRouterUpTime_Type()
)
cjnLrrpOperVirtualRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnLrrpOperVirtualRouterUpTime.setStatus("current")


class _CjnLrrpOperProtocol_Type(Integer32):
    """Custom type cjnLrrpOperProtocol based on Integer32"""
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


_CjnLrrpOperProtocol_Type.__name__ = "Integer32"
_CjnLrrpOperProtocol_Object = MibTableColumn
cjnLrrpOperProtocol = _CjnLrrpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 14),
    _CjnLrrpOperProtocol_Type()
)
cjnLrrpOperProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperProtocol.setStatus("current")


class _CjnLrrpOperOverrideAddressOwner_Type(Integer32):
    """Custom type cjnLrrpOperOverrideAddressOwner based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CjnLrrpOperOverrideAddressOwner_Type.__name__ = "Integer32"
_CjnLrrpOperOverrideAddressOwner_Object = MibTableColumn
cjnLrrpOperOverrideAddressOwner = _CjnLrrpOperOverrideAddressOwner_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 15),
    _CjnLrrpOperOverrideAddressOwner_Type()
)
cjnLrrpOperOverrideAddressOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLrrpOperOverrideAddressOwner.setStatus("current")
_CjnLrrpOperRowStatus_Type = RowStatus
_CjnLrrpOperRowStatus_Object = MibTableColumn
cjnLrrpOperRowStatus = _CjnLrrpOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 4, 1, 1, 16),
    _CjnLrrpOperRowStatus_Type()
)
cjnLrrpOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpOperRowStatus.setStatus("current")
_CjnLrrpAssoIpAddrGroup_ObjectIdentity = ObjectIdentity
cjnLrrpAssoIpAddrGroup = _CjnLrrpAssoIpAddrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 5)
)
_CjnLrrpAssoIpAddrTable_Object = MibTable
cjnLrrpAssoIpAddrTable = _CjnLrrpAssoIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 5, 1)
)
if mibBuilder.loadTexts:
    cjnLrrpAssoIpAddrTable.setStatus("current")
_CjnLrrpAssoIpAddrEntry_Object = MibTableRow
cjnLrrpAssoIpAddrEntry = _CjnLrrpAssoIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 5, 1, 1)
)
cjnLrrpAssoIpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IP-LRRP-MIB", "cjnLrrpOperVrId"),
    (0, "IP-LRRP-MIB", "cjnLrrpAssoIpAddr"),
)
if mibBuilder.loadTexts:
    cjnLrrpAssoIpAddrEntry.setStatus("current")
_CjnLrrpAssoIpAddr_Type = IpAddress
_CjnLrrpAssoIpAddr_Object = MibTableColumn
cjnLrrpAssoIpAddr = _CjnLrrpAssoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 5, 1, 1, 1),
    _CjnLrrpAssoIpAddr_Type()
)
cjnLrrpAssoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnLrrpAssoIpAddr.setStatus("current")
_CjnLrrpAssoIpAddrRowStatus_Type = RowStatus
_CjnLrrpAssoIpAddrRowStatus_Object = MibTableColumn
cjnLrrpAssoIpAddrRowStatus = _CjnLrrpAssoIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19, 5, 1, 1, 2),
    _CjnLrrpAssoIpAddrRowStatus_Type()
)
cjnLrrpAssoIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnLrrpAssoIpAddrRowStatus.setStatus("current")
cjnLrrpOperEntry.registerAugmentions(
    ("IP-LRRP-MIB",
     "cjnLrrpRouterStatsEntry")
)
cjnLrrpRouterStatsEntry.setIndexNames(*cjnLrrpOperEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-LRRP-MIB",
    **{"cjnLrrp": cjnLrrp,
       "cjnLrrpGlobalGroup": cjnLrrpGlobalGroup,
       "cjnLrrpEnabled": cjnLrrpEnabled,
       "cjnLrrpGlobalStatsReset": cjnLrrpGlobalStatsReset,
       "cjnLrrpGblStatsGroup": cjnLrrpGblStatsGroup,
       "cjnLrrpRouterChecksumErrors": cjnLrrpRouterChecksumErrors,
       "cjnLrrpRouterVersionErrors": cjnLrrpRouterVersionErrors,
       "cjnLrrpRouterVrIdErrors": cjnLrrpRouterVrIdErrors,
       "cjnLrrpRtrStatsGroup": cjnLrrpRtrStatsGroup,
       "cjnLrrpRouterStatsTable": cjnLrrpRouterStatsTable,
       "cjnLrrpRouterStatsEntry": cjnLrrpRouterStatsEntry,
       "cjnLrrpStatsBecomeMaster": cjnLrrpStatsBecomeMaster,
       "cjnLrrpStatsAdvertiseRcvd": cjnLrrpStatsAdvertiseRcvd,
       "cjnLrrpStatsAdvertiseIntervalErrors": cjnLrrpStatsAdvertiseIntervalErrors,
       "cjnLrrpStatsAuthFailures": cjnLrrpStatsAuthFailures,
       "cjnLrrpStatsIpTtlErrors": cjnLrrpStatsIpTtlErrors,
       "cjnLrrpStatsPriorityZeroPktsRcvd": cjnLrrpStatsPriorityZeroPktsRcvd,
       "cjnLrrpStatsPriorityZeroPktsSent": cjnLrrpStatsPriorityZeroPktsSent,
       "cjnLrrpStatsInvalidTypePktsRcvd": cjnLrrpStatsInvalidTypePktsRcvd,
       "cjnLrrpStatsAddressListErrors": cjnLrrpStatsAddressListErrors,
       "cjnLrrpStatsInvalidAuthType": cjnLrrpStatsInvalidAuthType,
       "cjnLrrpStatsAuthTypeMismatch": cjnLrrpStatsAuthTypeMismatch,
       "cjnLrrpStatsPacketLengthErrors": cjnLrrpStatsPacketLengthErrors,
       "cjnLrrpRtrGroup": cjnLrrpRtrGroup,
       "cjnLrrpOperTable": cjnLrrpOperTable,
       "cjnLrrpOperEntry": cjnLrrpOperEntry,
       "cjnLrrpOperVrId": cjnLrrpOperVrId,
       "cjnLrrpOperVirtualMacAddr": cjnLrrpOperVirtualMacAddr,
       "cjnLrrpOperState": cjnLrrpOperState,
       "cjnLrrpOperAdminState": cjnLrrpOperAdminState,
       "cjnLrrpOperPriority": cjnLrrpOperPriority,
       "cjnLrrpOperIpAddrCount": cjnLrrpOperIpAddrCount,
       "cjnLrrpOperMasterIpAddr": cjnLrrpOperMasterIpAddr,
       "cjnLrrpOperPrimaryIpAddr": cjnLrrpOperPrimaryIpAddr,
       "cjnLrrpOperAuthType": cjnLrrpOperAuthType,
       "cjnLrrpOperAuthKey": cjnLrrpOperAuthKey,
       "cjnLrrpOperAdvertisementInterval": cjnLrrpOperAdvertisementInterval,
       "cjnLrrpOperPreemptMode": cjnLrrpOperPreemptMode,
       "cjnLrrpOperVirtualRouterUpTime": cjnLrrpOperVirtualRouterUpTime,
       "cjnLrrpOperProtocol": cjnLrrpOperProtocol,
       "cjnLrrpOperOverrideAddressOwner": cjnLrrpOperOverrideAddressOwner,
       "cjnLrrpOperRowStatus": cjnLrrpOperRowStatus,
       "cjnLrrpAssoIpAddrGroup": cjnLrrpAssoIpAddrGroup,
       "cjnLrrpAssoIpAddrTable": cjnLrrpAssoIpAddrTable,
       "cjnLrrpAssoIpAddrEntry": cjnLrrpAssoIpAddrEntry,
       "cjnLrrpAssoIpAddr": cjnLrrpAssoIpAddr,
       "cjnLrrpAssoIpAddrRowStatus": cjnLrrpAssoIpAddrRowStatus}
)
