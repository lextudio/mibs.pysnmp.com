# SNMP MIB module (RADLAN-RADIUSSRV) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-RADIUSSRV
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:09 2024
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

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(rlAAAEap,
 rlRadius,
 rnd) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rlAAAEap",
    "rlRadius",
    "rnd")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rlRadiusServ = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 226)
)
rlRadiusServ.setRevisions(
        ("2015-06-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlRadiusServUserType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("login", 2),
          ("none", 0),
          ("x", 1))
    )



class RlRadiusServRejectedEventType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dateTimeChanged", 3),
          ("invalid", 0),
          ("reboot", 2),
          ("rejected", 4))
    )



class RlRadiusServRejectedReasonType(Integer32, TextualConvention):
    status = "current"
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
        *(("illegalPassword", 2),
          ("noError", 0),
          ("notAllowedTime", 3),
          ("unknownUser", 1))
    )



class RlRadiusServAcctLogUserAuthType(Integer32, TextualConvention):
    status = "current"
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
        *(("local", 2),
          ("none", 0),
          ("radius", 1),
          ("remote", 3))
    )



class RlRadiusServAcctLogEventType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dateTimeChanged", 3),
          ("invalid", 0),
          ("reboot", 2),
          ("start", 4),
          ("stop", 5))
    )



class RlRadiusServAcctLogTerminationReasonType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("adminReboot", 7),
          ("adminReset", 6),
          ("callback", 16),
          ("hostRequest", 18),
          ("idleTimeout", 4),
          ("lostCarrier", 2),
          ("lostService", 3),
          ("nasError", 9),
          ("nasReboot", 11),
          ("nasRequest", 10),
          ("noError", 0),
          ("portError", 8),
          ("portPreempted", 13),
          ("portSuspended", 14),
          ("portUnneeded", 12),
          ("serviceUnavailable", 15),
          ("sessionTimeout", 5),
          ("userError", 17),
          ("userRequest", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlRadiusServEnable_Type = TruthValue
_RlRadiusServEnable_Object = MibScalar
rlRadiusServEnable = _RlRadiusServEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 1),
    _RlRadiusServEnable_Type()
)
rlRadiusServEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServEnable.setStatus("current")


class _RlRadiusServAcctPort_Type(Integer32):
    """Custom type rlRadiusServAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlRadiusServAcctPort_Type.__name__ = "Integer32"
_RlRadiusServAcctPort_Object = MibScalar
rlRadiusServAcctPort = _RlRadiusServAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 2),
    _RlRadiusServAcctPort_Type()
)
rlRadiusServAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServAcctPort.setStatus("current")


class _RlRadiusServAuthPort_Type(Integer32):
    """Custom type rlRadiusServAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlRadiusServAuthPort_Type.__name__ = "Integer32"
_RlRadiusServAuthPort_Object = MibScalar
rlRadiusServAuthPort = _RlRadiusServAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 3),
    _RlRadiusServAuthPort_Type()
)
rlRadiusServAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServAuthPort.setStatus("current")


class _RlRadiusServDefaultKey_Type(DisplayString):
    """Custom type rlRadiusServDefaultKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRadiusServDefaultKey_Type.__name__ = "DisplayString"
_RlRadiusServDefaultKey_Object = MibScalar
rlRadiusServDefaultKey = _RlRadiusServDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 4),
    _RlRadiusServDefaultKey_Type()
)
rlRadiusServDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServDefaultKey.setStatus("current")
_RlRadiusServDefaultKeyMD5_Type = DisplayString
_RlRadiusServDefaultKeyMD5_Object = MibScalar
rlRadiusServDefaultKeyMD5 = _RlRadiusServDefaultKeyMD5_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 5),
    _RlRadiusServDefaultKeyMD5_Type()
)
rlRadiusServDefaultKeyMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServDefaultKeyMD5.setStatus("current")
_RlRadiusServTrapAcct_Type = TruthValue
_RlRadiusServTrapAcct_Object = MibScalar
rlRadiusServTrapAcct = _RlRadiusServTrapAcct_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 6),
    _RlRadiusServTrapAcct_Type()
)
rlRadiusServTrapAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServTrapAcct.setStatus("current")
_RlRadiusServTrapAuthFailure_Type = TruthValue
_RlRadiusServTrapAuthFailure_Object = MibScalar
rlRadiusServTrapAuthFailure = _RlRadiusServTrapAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 7),
    _RlRadiusServTrapAuthFailure_Type()
)
rlRadiusServTrapAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServTrapAuthFailure.setStatus("current")
_RlRadiusServTrapAuthSuccess_Type = TruthValue
_RlRadiusServTrapAuthSuccess_Object = MibScalar
rlRadiusServTrapAuthSuccess = _RlRadiusServTrapAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 8),
    _RlRadiusServTrapAuthSuccess_Type()
)
rlRadiusServTrapAuthSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServTrapAuthSuccess.setStatus("current")
_RlRadiusServGroupTable_Object = MibTable
rlRadiusServGroupTable = _RlRadiusServGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9)
)
if mibBuilder.loadTexts:
    rlRadiusServGroupTable.setStatus("current")
_RlRadiusServGroupEntry_Object = MibTableRow
rlRadiusServGroupEntry = _RlRadiusServGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1)
)
rlRadiusServGroupEntry.setIndexNames(
    (0, "RADLAN-RADIUSSRV", "rlRadiusServGroupName"),
)
if mibBuilder.loadTexts:
    rlRadiusServGroupEntry.setStatus("current")


class _RlRadiusServGroupName_Type(DisplayString):
    """Custom type rlRadiusServGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRadiusServGroupName_Type.__name__ = "DisplayString"
_RlRadiusServGroupName_Object = MibTableColumn
rlRadiusServGroupName = _RlRadiusServGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 1),
    _RlRadiusServGroupName_Type()
)
rlRadiusServGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServGroupName.setStatus("current")


class _RlRadiusServGroupVLAN_Type(Integer32):
    """Custom type rlRadiusServGroupVLAN based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_RlRadiusServGroupVLAN_Type.__name__ = "Integer32"
_RlRadiusServGroupVLAN_Object = MibTableColumn
rlRadiusServGroupVLAN = _RlRadiusServGroupVLAN_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 2),
    _RlRadiusServGroupVLAN_Type()
)
rlRadiusServGroupVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServGroupVLAN.setStatus("current")


class _RlRadiusServGroupVLANName_Type(DisplayString):
    """Custom type rlRadiusServGroupVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRadiusServGroupVLANName_Type.__name__ = "DisplayString"
_RlRadiusServGroupVLANName_Object = MibTableColumn
rlRadiusServGroupVLANName = _RlRadiusServGroupVLANName_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 3),
    _RlRadiusServGroupVLANName_Type()
)
rlRadiusServGroupVLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServGroupVLANName.setStatus("current")


class _RlRadiusServGroupACL1_Type(DisplayString):
    """Custom type rlRadiusServGroupACL1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRadiusServGroupACL1_Type.__name__ = "DisplayString"
_RlRadiusServGroupACL1_Object = MibTableColumn
rlRadiusServGroupACL1 = _RlRadiusServGroupACL1_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 4),
    _RlRadiusServGroupACL1_Type()
)
rlRadiusServGroupACL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServGroupACL1.setStatus("current")


class _RlRadiusServGroupACL2_Type(DisplayString):
    """Custom type rlRadiusServGroupACL2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRadiusServGroupACL2_Type.__name__ = "DisplayString"
_RlRadiusServGroupACL2_Object = MibTableColumn
rlRadiusServGroupACL2 = _RlRadiusServGroupACL2_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 5),
    _RlRadiusServGroupACL2_Type()
)
rlRadiusServGroupACL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServGroupACL2.setStatus("current")


class _RlRadiusServGroupPrvLevel_Type(Integer32):
    """Custom type rlRadiusServGroupPrvLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlRadiusServGroupPrvLevel_Type.__name__ = "Integer32"
_RlRadiusServGroupPrvLevel_Object = MibTableColumn
rlRadiusServGroupPrvLevel = _RlRadiusServGroupPrvLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 6),
    _RlRadiusServGroupPrvLevel_Type()
)
rlRadiusServGroupPrvLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServGroupPrvLevel.setStatus("current")


class _RlRadiusServGroupTimeRangeName_Type(DisplayString):
    """Custom type rlRadiusServGroupTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRadiusServGroupTimeRangeName_Type.__name__ = "DisplayString"
_RlRadiusServGroupTimeRangeName_Object = MibTableColumn
rlRadiusServGroupTimeRangeName = _RlRadiusServGroupTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 7),
    _RlRadiusServGroupTimeRangeName_Type()
)
rlRadiusServGroupTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServGroupTimeRangeName.setStatus("current")
_RlRadiusServGroupStatus_Type = RowStatus
_RlRadiusServGroupStatus_Object = MibTableColumn
rlRadiusServGroupStatus = _RlRadiusServGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 8),
    _RlRadiusServGroupStatus_Type()
)
rlRadiusServGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServGroupStatus.setStatus("current")
_RlRadiusServUserTable_Object = MibTable
rlRadiusServUserTable = _RlRadiusServUserTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 10)
)
if mibBuilder.loadTexts:
    rlRadiusServUserTable.setStatus("current")
_RlRadiusServUserEntry_Object = MibTableRow
rlRadiusServUserEntry = _RlRadiusServUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 10, 1)
)
rlRadiusServUserEntry.setIndexNames(
    (0, "RADLAN-RADIUSSRV", "rlRadiusServUserName"),
)
if mibBuilder.loadTexts:
    rlRadiusServUserEntry.setStatus("current")


class _RlRadiusServUserName_Type(DisplayString):
    """Custom type rlRadiusServUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRadiusServUserName_Type.__name__ = "DisplayString"
_RlRadiusServUserName_Object = MibTableColumn
rlRadiusServUserName = _RlRadiusServUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 1),
    _RlRadiusServUserName_Type()
)
rlRadiusServUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServUserName.setStatus("current")


class _RlRadiusServUserPassword_Type(DisplayString):
    """Custom type rlRadiusServUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlRadiusServUserPassword_Type.__name__ = "DisplayString"
_RlRadiusServUserPassword_Object = MibTableColumn
rlRadiusServUserPassword = _RlRadiusServUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 2),
    _RlRadiusServUserPassword_Type()
)
rlRadiusServUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServUserPassword.setStatus("current")
_RlRadiusServUserPasswordMD5_Type = DisplayString
_RlRadiusServUserPasswordMD5_Object = MibTableColumn
rlRadiusServUserPasswordMD5 = _RlRadiusServUserPasswordMD5_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 3),
    _RlRadiusServUserPasswordMD5_Type()
)
rlRadiusServUserPasswordMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServUserPasswordMD5.setStatus("current")


class _RlRadiusServUserGroupName_Type(DisplayString):
    """Custom type rlRadiusServUserGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRadiusServUserGroupName_Type.__name__ = "DisplayString"
_RlRadiusServUserGroupName_Object = MibTableColumn
rlRadiusServUserGroupName = _RlRadiusServUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 4),
    _RlRadiusServUserGroupName_Type()
)
rlRadiusServUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServUserGroupName.setStatus("current")
_RlRadiusServUserStatus_Type = RowStatus
_RlRadiusServUserStatus_Object = MibTableColumn
rlRadiusServUserStatus = _RlRadiusServUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 5),
    _RlRadiusServUserStatus_Type()
)
rlRadiusServUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServUserStatus.setStatus("current")
_RlRadiusServClientInetTable_Object = MibTable
rlRadiusServClientInetTable = _RlRadiusServClientInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 11)
)
if mibBuilder.loadTexts:
    rlRadiusServClientInetTable.setStatus("current")
_RlRadiusServClientInetEntry_Object = MibTableRow
rlRadiusServClientInetEntry = _RlRadiusServClientInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 11, 1)
)
rlRadiusServClientInetEntry.setIndexNames(
    (0, "RADLAN-RADIUSSRV", "rlRadiusServClientInetAddressType"),
    (0, "RADLAN-RADIUSSRV", "rlRadiusServClientInetAddress"),
)
if mibBuilder.loadTexts:
    rlRadiusServClientInetEntry.setStatus("current")
_RlRadiusServClientInetAddressType_Type = InetAddressType
_RlRadiusServClientInetAddressType_Object = MibTableColumn
rlRadiusServClientInetAddressType = _RlRadiusServClientInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 1),
    _RlRadiusServClientInetAddressType_Type()
)
rlRadiusServClientInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClientInetAddressType.setStatus("current")
_RlRadiusServClientInetAddress_Type = InetAddress
_RlRadiusServClientInetAddress_Object = MibTableColumn
rlRadiusServClientInetAddress = _RlRadiusServClientInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 2),
    _RlRadiusServClientInetAddress_Type()
)
rlRadiusServClientInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClientInetAddress.setStatus("current")


class _RlRadiusServClientInetKey_Type(DisplayString):
    """Custom type rlRadiusServClientInetKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRadiusServClientInetKey_Type.__name__ = "DisplayString"
_RlRadiusServClientInetKey_Object = MibTableColumn
rlRadiusServClientInetKey = _RlRadiusServClientInetKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 3),
    _RlRadiusServClientInetKey_Type()
)
rlRadiusServClientInetKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClientInetKey.setStatus("current")
_RlRadiusServClientInetKeyMD5_Type = DisplayString
_RlRadiusServClientInetKeyMD5_Object = MibTableColumn
rlRadiusServClientInetKeyMD5 = _RlRadiusServClientInetKeyMD5_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 4),
    _RlRadiusServClientInetKeyMD5_Type()
)
rlRadiusServClientInetKeyMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServClientInetKeyMD5.setStatus("current")
_RlRadiusServClientInetStatus_Type = RowStatus
_RlRadiusServClientInetStatus_Object = MibTableColumn
rlRadiusServClientInetStatus = _RlRadiusServClientInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 5),
    _RlRadiusServClientInetStatus_Type()
)
rlRadiusServClientInetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClientInetStatus.setStatus("current")
_RlRadiusServClearAccounting_Type = TruthValue
_RlRadiusServClearAccounting_Object = MibScalar
rlRadiusServClearAccounting = _RlRadiusServClearAccounting_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 12),
    _RlRadiusServClearAccounting_Type()
)
rlRadiusServClearAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClearAccounting.setStatus("current")
_RlRadiusServClearRejectedUsers_Type = TruthValue
_RlRadiusServClearRejectedUsers_Object = MibScalar
rlRadiusServClearRejectedUsers = _RlRadiusServClearRejectedUsers_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 13),
    _RlRadiusServClearRejectedUsers_Type()
)
rlRadiusServClearRejectedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClearRejectedUsers.setStatus("current")
_RlRadiusServClearStatistics_Type = TruthValue
_RlRadiusServClearStatistics_Object = MibScalar
rlRadiusServClearStatistics = _RlRadiusServClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 14),
    _RlRadiusServClearStatistics_Type()
)
rlRadiusServClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClearStatistics.setStatus("current")


class _RlRadiusServClearUsersOfGivenGroup_Type(DisplayString):
    """Custom type rlRadiusServClearUsersOfGivenGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRadiusServClearUsersOfGivenGroup_Type.__name__ = "DisplayString"
_RlRadiusServClearUsersOfGivenGroup_Object = MibScalar
rlRadiusServClearUsersOfGivenGroup = _RlRadiusServClearUsersOfGivenGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 15),
    _RlRadiusServClearUsersOfGivenGroup_Type()
)
rlRadiusServClearUsersOfGivenGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClearUsersOfGivenGroup.setStatus("current")
_RlRadiusServClearClientStatisticsTable_Object = MibTable
rlRadiusServClearClientStatisticsTable = _RlRadiusServClearClientStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 16)
)
if mibBuilder.loadTexts:
    rlRadiusServClearClientStatisticsTable.setStatus("current")
_RlRadiusServClearClientStatisticsEntry_Object = MibTableRow
rlRadiusServClearClientStatisticsEntry = _RlRadiusServClearClientStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 16, 1)
)
rlRadiusServClearClientStatisticsEntry.setIndexNames(
    (0, "RADLAN-RADIUSSRV", "rlRadiusServClearClientStatisticsIndex"),
)
if mibBuilder.loadTexts:
    rlRadiusServClearClientStatisticsEntry.setStatus("current")
_RlRadiusServClearClientStatisticsIndex_Type = Integer32
_RlRadiusServClearClientStatisticsIndex_Object = MibTableColumn
rlRadiusServClearClientStatisticsIndex = _RlRadiusServClearClientStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 16, 1, 1),
    _RlRadiusServClearClientStatisticsIndex_Type()
)
rlRadiusServClearClientStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServClearClientStatisticsIndex.setStatus("current")
_RlRadiusServClearClientStatisticsInetAddressType_Type = InetAddressType
_RlRadiusServClearClientStatisticsInetAddressType_Object = MibTableColumn
rlRadiusServClearClientStatisticsInetAddressType = _RlRadiusServClearClientStatisticsInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 16, 1, 2),
    _RlRadiusServClearClientStatisticsInetAddressType_Type()
)
rlRadiusServClearClientStatisticsInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClearClientStatisticsInetAddressType.setStatus("current")
_RlRadiusServClearClientStatisticsInetAddress_Type = InetAddress
_RlRadiusServClearClientStatisticsInetAddress_Object = MibTableColumn
rlRadiusServClearClientStatisticsInetAddress = _RlRadiusServClearClientStatisticsInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 16, 1, 3),
    _RlRadiusServClearClientStatisticsInetAddress_Type()
)
rlRadiusServClearClientStatisticsInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServClearClientStatisticsInetAddress.setStatus("current")
_RlRadiusServRejectedTable_Object = MibTable
rlRadiusServRejectedTable = _RlRadiusServRejectedTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17)
)
if mibBuilder.loadTexts:
    rlRadiusServRejectedTable.setStatus("current")
_RlRadiusServRejectedEntry_Object = MibTableRow
rlRadiusServRejectedEntry = _RlRadiusServRejectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1)
)
rlRadiusServRejectedEntry.setIndexNames(
    (0, "RADLAN-RADIUSSRV", "rlRadiusServRejectedIndex"),
)
if mibBuilder.loadTexts:
    rlRadiusServRejectedEntry.setStatus("current")


class _RlRadiusServRejectedIndex_Type(Unsigned32):
    """Custom type rlRadiusServRejectedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlRadiusServRejectedIndex_Type.__name__ = "Unsigned32"
_RlRadiusServRejectedIndex_Object = MibTableColumn
rlRadiusServRejectedIndex = _RlRadiusServRejectedIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 1),
    _RlRadiusServRejectedIndex_Type()
)
rlRadiusServRejectedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRadiusServRejectedIndex.setStatus("current")


class _RlRadiusServRejectedUserName_Type(DisplayString):
    """Custom type rlRadiusServRejectedUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRadiusServRejectedUserName_Type.__name__ = "DisplayString"
_RlRadiusServRejectedUserName_Object = MibTableColumn
rlRadiusServRejectedUserName = _RlRadiusServRejectedUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 2),
    _RlRadiusServRejectedUserName_Type()
)
rlRadiusServRejectedUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedUserName.setStatus("current")
_RlRadiusServRejectedUserType_Type = RlRadiusServUserType
_RlRadiusServRejectedUserType_Object = MibTableColumn
rlRadiusServRejectedUserType = _RlRadiusServRejectedUserType_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 3),
    _RlRadiusServRejectedUserType_Type()
)
rlRadiusServRejectedUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedUserType.setStatus("current")
_RlRadiusServRejectedEvent_Type = RlRadiusServRejectedEventType
_RlRadiusServRejectedEvent_Object = MibTableColumn
rlRadiusServRejectedEvent = _RlRadiusServRejectedEvent_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 4),
    _RlRadiusServRejectedEvent_Type()
)
rlRadiusServRejectedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedEvent.setStatus("current")
_RlRadiusServRejectedDateTime_Type = DisplayString
_RlRadiusServRejectedDateTime_Object = MibTableColumn
rlRadiusServRejectedDateTime = _RlRadiusServRejectedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 5),
    _RlRadiusServRejectedDateTime_Type()
)
rlRadiusServRejectedDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedDateTime.setStatus("current")
_RlRadiusServRejectedUpdatedDateTime_Type = DisplayString
_RlRadiusServRejectedUpdatedDateTime_Object = MibTableColumn
rlRadiusServRejectedUpdatedDateTime = _RlRadiusServRejectedUpdatedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 6),
    _RlRadiusServRejectedUpdatedDateTime_Type()
)
rlRadiusServRejectedUpdatedDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedUpdatedDateTime.setStatus("current")
_RlRadiusServRejectedNASInetAddressType_Type = InetAddressType
_RlRadiusServRejectedNASInetAddressType_Object = MibTableColumn
rlRadiusServRejectedNASInetAddressType = _RlRadiusServRejectedNASInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 7),
    _RlRadiusServRejectedNASInetAddressType_Type()
)
rlRadiusServRejectedNASInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedNASInetAddressType.setStatus("current")
_RlRadiusServRejectedNASInetAddress_Type = InetAddress
_RlRadiusServRejectedNASInetAddress_Object = MibTableColumn
rlRadiusServRejectedNASInetAddress = _RlRadiusServRejectedNASInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 8),
    _RlRadiusServRejectedNASInetAddress_Type()
)
rlRadiusServRejectedNASInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedNASInetAddress.setStatus("current")
_RlRadiusServRejectedNASPort_Type = Integer32
_RlRadiusServRejectedNASPort_Object = MibTableColumn
rlRadiusServRejectedNASPort = _RlRadiusServRejectedNASPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 9),
    _RlRadiusServRejectedNASPort_Type()
)
rlRadiusServRejectedNASPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedNASPort.setStatus("current")
_RlRadiusServRejectedUserAddress_Type = DisplayString
_RlRadiusServRejectedUserAddress_Object = MibTableColumn
rlRadiusServRejectedUserAddress = _RlRadiusServRejectedUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 10),
    _RlRadiusServRejectedUserAddress_Type()
)
rlRadiusServRejectedUserAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedUserAddress.setStatus("current")
_RlRadiusServRejectedReason_Type = RlRadiusServRejectedReasonType
_RlRadiusServRejectedReason_Object = MibTableColumn
rlRadiusServRejectedReason = _RlRadiusServRejectedReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 11),
    _RlRadiusServRejectedReason_Type()
)
rlRadiusServRejectedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServRejectedReason.setStatus("current")
_RlRadiusServAcctLogTable_Object = MibTable
rlRadiusServAcctLogTable = _RlRadiusServAcctLogTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18)
)
if mibBuilder.loadTexts:
    rlRadiusServAcctLogTable.setStatus("current")
_RlRadiusServAcctLogEntry_Object = MibTableRow
rlRadiusServAcctLogEntry = _RlRadiusServAcctLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1)
)
rlRadiusServAcctLogEntry.setIndexNames(
    (0, "RADLAN-RADIUSSRV", "rlRadiusServAcctLogIndex"),
)
if mibBuilder.loadTexts:
    rlRadiusServAcctLogEntry.setStatus("current")


class _RlRadiusServAcctLogIndex_Type(Unsigned32):
    """Custom type rlRadiusServAcctLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlRadiusServAcctLogIndex_Type.__name__ = "Unsigned32"
_RlRadiusServAcctLogIndex_Object = MibTableColumn
rlRadiusServAcctLogIndex = _RlRadiusServAcctLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 1),
    _RlRadiusServAcctLogIndex_Type()
)
rlRadiusServAcctLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogIndex.setStatus("current")


class _RlRadiusServAcctLogUserName_Type(DisplayString):
    """Custom type rlRadiusServAcctLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRadiusServAcctLogUserName_Type.__name__ = "DisplayString"
_RlRadiusServAcctLogUserName_Object = MibTableColumn
rlRadiusServAcctLogUserName = _RlRadiusServAcctLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 2),
    _RlRadiusServAcctLogUserName_Type()
)
rlRadiusServAcctLogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogUserName.setStatus("current")
_RlRadiusServAcctLogUserAuth_Type = RlRadiusServAcctLogUserAuthType
_RlRadiusServAcctLogUserAuth_Object = MibTableColumn
rlRadiusServAcctLogUserAuth = _RlRadiusServAcctLogUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 3),
    _RlRadiusServAcctLogUserAuth_Type()
)
rlRadiusServAcctLogUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogUserAuth.setStatus("current")
_RlRadiusServAcctLogEvent_Type = RlRadiusServAcctLogEventType
_RlRadiusServAcctLogEvent_Object = MibTableColumn
rlRadiusServAcctLogEvent = _RlRadiusServAcctLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 4),
    _RlRadiusServAcctLogEvent_Type()
)
rlRadiusServAcctLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogEvent.setStatus("current")
_RlRadiusServAcctLogDateTime_Type = DisplayString
_RlRadiusServAcctLogDateTime_Object = MibTableColumn
rlRadiusServAcctLogDateTime = _RlRadiusServAcctLogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 5),
    _RlRadiusServAcctLogDateTime_Type()
)
rlRadiusServAcctLogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogDateTime.setStatus("current")
_RlRadiusServAcctLogUpdatedDateTime_Type = DisplayString
_RlRadiusServAcctLogUpdatedDateTime_Object = MibTableColumn
rlRadiusServAcctLogUpdatedDateTime = _RlRadiusServAcctLogUpdatedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 6),
    _RlRadiusServAcctLogUpdatedDateTime_Type()
)
rlRadiusServAcctLogUpdatedDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogUpdatedDateTime.setStatus("current")
_RlRadiusServAcctLogSessionDuration_Type = Unsigned32
_RlRadiusServAcctLogSessionDuration_Object = MibTableColumn
rlRadiusServAcctLogSessionDuration = _RlRadiusServAcctLogSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 7),
    _RlRadiusServAcctLogSessionDuration_Type()
)
rlRadiusServAcctLogSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogSessionDuration.setStatus("current")
_RlRadiusServAcctLogNASInetAddressType_Type = InetAddressType
_RlRadiusServAcctLogNASInetAddressType_Object = MibTableColumn
rlRadiusServAcctLogNASInetAddressType = _RlRadiusServAcctLogNASInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 8),
    _RlRadiusServAcctLogNASInetAddressType_Type()
)
rlRadiusServAcctLogNASInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogNASInetAddressType.setStatus("current")
_RlRadiusServAcctLogNASInetAddress_Type = InetAddress
_RlRadiusServAcctLogNASInetAddress_Object = MibTableColumn
rlRadiusServAcctLogNASInetAddress = _RlRadiusServAcctLogNASInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 9),
    _RlRadiusServAcctLogNASInetAddress_Type()
)
rlRadiusServAcctLogNASInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogNASInetAddress.setStatus("current")
_RlRadiusServAcctLogNASPort_Type = Integer32
_RlRadiusServAcctLogNASPort_Object = MibTableColumn
rlRadiusServAcctLogNASPort = _RlRadiusServAcctLogNASPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 10),
    _RlRadiusServAcctLogNASPort_Type()
)
rlRadiusServAcctLogNASPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogNASPort.setStatus("current")
_RlRadiusServAcctLogUserAddress_Type = DisplayString
_RlRadiusServAcctLogUserAddress_Object = MibTableColumn
rlRadiusServAcctLogUserAddress = _RlRadiusServAcctLogUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 11),
    _RlRadiusServAcctLogUserAddress_Type()
)
rlRadiusServAcctLogUserAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogUserAddress.setStatus("current")
_RlRadiusServAcctLogTerminationReason_Type = RlRadiusServAcctLogTerminationReasonType
_RlRadiusServAcctLogTerminationReason_Object = MibTableColumn
rlRadiusServAcctLogTerminationReason = _RlRadiusServAcctLogTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 12),
    _RlRadiusServAcctLogTerminationReason_Type()
)
rlRadiusServAcctLogTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServAcctLogTerminationReason.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-RADIUSSRV",
    **{"RlRadiusServUserType": RlRadiusServUserType,
       "RlRadiusServRejectedEventType": RlRadiusServRejectedEventType,
       "RlRadiusServRejectedReasonType": RlRadiusServRejectedReasonType,
       "RlRadiusServAcctLogUserAuthType": RlRadiusServAcctLogUserAuthType,
       "RlRadiusServAcctLogEventType": RlRadiusServAcctLogEventType,
       "RlRadiusServAcctLogTerminationReasonType": RlRadiusServAcctLogTerminationReasonType,
       "rlRadiusServ": rlRadiusServ,
       "rlRadiusServEnable": rlRadiusServEnable,
       "rlRadiusServAcctPort": rlRadiusServAcctPort,
       "rlRadiusServAuthPort": rlRadiusServAuthPort,
       "rlRadiusServDefaultKey": rlRadiusServDefaultKey,
       "rlRadiusServDefaultKeyMD5": rlRadiusServDefaultKeyMD5,
       "rlRadiusServTrapAcct": rlRadiusServTrapAcct,
       "rlRadiusServTrapAuthFailure": rlRadiusServTrapAuthFailure,
       "rlRadiusServTrapAuthSuccess": rlRadiusServTrapAuthSuccess,
       "rlRadiusServGroupTable": rlRadiusServGroupTable,
       "rlRadiusServGroupEntry": rlRadiusServGroupEntry,
       "rlRadiusServGroupName": rlRadiusServGroupName,
       "rlRadiusServGroupVLAN": rlRadiusServGroupVLAN,
       "rlRadiusServGroupVLANName": rlRadiusServGroupVLANName,
       "rlRadiusServGroupACL1": rlRadiusServGroupACL1,
       "rlRadiusServGroupACL2": rlRadiusServGroupACL2,
       "rlRadiusServGroupPrvLevel": rlRadiusServGroupPrvLevel,
       "rlRadiusServGroupTimeRangeName": rlRadiusServGroupTimeRangeName,
       "rlRadiusServGroupStatus": rlRadiusServGroupStatus,
       "rlRadiusServUserTable": rlRadiusServUserTable,
       "rlRadiusServUserEntry": rlRadiusServUserEntry,
       "rlRadiusServUserName": rlRadiusServUserName,
       "rlRadiusServUserPassword": rlRadiusServUserPassword,
       "rlRadiusServUserPasswordMD5": rlRadiusServUserPasswordMD5,
       "rlRadiusServUserGroupName": rlRadiusServUserGroupName,
       "rlRadiusServUserStatus": rlRadiusServUserStatus,
       "rlRadiusServClientInetTable": rlRadiusServClientInetTable,
       "rlRadiusServClientInetEntry": rlRadiusServClientInetEntry,
       "rlRadiusServClientInetAddressType": rlRadiusServClientInetAddressType,
       "rlRadiusServClientInetAddress": rlRadiusServClientInetAddress,
       "rlRadiusServClientInetKey": rlRadiusServClientInetKey,
       "rlRadiusServClientInetKeyMD5": rlRadiusServClientInetKeyMD5,
       "rlRadiusServClientInetStatus": rlRadiusServClientInetStatus,
       "rlRadiusServClearAccounting": rlRadiusServClearAccounting,
       "rlRadiusServClearRejectedUsers": rlRadiusServClearRejectedUsers,
       "rlRadiusServClearStatistics": rlRadiusServClearStatistics,
       "rlRadiusServClearUsersOfGivenGroup": rlRadiusServClearUsersOfGivenGroup,
       "rlRadiusServClearClientStatisticsTable": rlRadiusServClearClientStatisticsTable,
       "rlRadiusServClearClientStatisticsEntry": rlRadiusServClearClientStatisticsEntry,
       "rlRadiusServClearClientStatisticsIndex": rlRadiusServClearClientStatisticsIndex,
       "rlRadiusServClearClientStatisticsInetAddressType": rlRadiusServClearClientStatisticsInetAddressType,
       "rlRadiusServClearClientStatisticsInetAddress": rlRadiusServClearClientStatisticsInetAddress,
       "rlRadiusServRejectedTable": rlRadiusServRejectedTable,
       "rlRadiusServRejectedEntry": rlRadiusServRejectedEntry,
       "rlRadiusServRejectedIndex": rlRadiusServRejectedIndex,
       "rlRadiusServRejectedUserName": rlRadiusServRejectedUserName,
       "rlRadiusServRejectedUserType": rlRadiusServRejectedUserType,
       "rlRadiusServRejectedEvent": rlRadiusServRejectedEvent,
       "rlRadiusServRejectedDateTime": rlRadiusServRejectedDateTime,
       "rlRadiusServRejectedUpdatedDateTime": rlRadiusServRejectedUpdatedDateTime,
       "rlRadiusServRejectedNASInetAddressType": rlRadiusServRejectedNASInetAddressType,
       "rlRadiusServRejectedNASInetAddress": rlRadiusServRejectedNASInetAddress,
       "rlRadiusServRejectedNASPort": rlRadiusServRejectedNASPort,
       "rlRadiusServRejectedUserAddress": rlRadiusServRejectedUserAddress,
       "rlRadiusServRejectedReason": rlRadiusServRejectedReason,
       "rlRadiusServAcctLogTable": rlRadiusServAcctLogTable,
       "rlRadiusServAcctLogEntry": rlRadiusServAcctLogEntry,
       "rlRadiusServAcctLogIndex": rlRadiusServAcctLogIndex,
       "rlRadiusServAcctLogUserName": rlRadiusServAcctLogUserName,
       "rlRadiusServAcctLogUserAuth": rlRadiusServAcctLogUserAuth,
       "rlRadiusServAcctLogEvent": rlRadiusServAcctLogEvent,
       "rlRadiusServAcctLogDateTime": rlRadiusServAcctLogDateTime,
       "rlRadiusServAcctLogUpdatedDateTime": rlRadiusServAcctLogUpdatedDateTime,
       "rlRadiusServAcctLogSessionDuration": rlRadiusServAcctLogSessionDuration,
       "rlRadiusServAcctLogNASInetAddressType": rlRadiusServAcctLogNASInetAddressType,
       "rlRadiusServAcctLogNASInetAddress": rlRadiusServAcctLogNASInetAddress,
       "rlRadiusServAcctLogNASPort": rlRadiusServAcctLogNASPort,
       "rlRadiusServAcctLogUserAddress": rlRadiusServAcctLogUserAddress,
       "rlRadiusServAcctLogTerminationReason": rlRadiusServAcctLogTerminationReason}
)
