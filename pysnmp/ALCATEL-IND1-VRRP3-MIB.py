# SNMP MIB module (ALCATEL-IND1-VRRP3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-VRRP3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:36 2024
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

(softentIND1Vrrp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Vrrp")

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

(VrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "VrId")


# MODULE-IDENTITY

alcatelIND1VRRP3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2)
)
alcatelIND1VRRP3MIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaVrrp3Notifications_ObjectIdentity = ObjectIdentity
alaVrrp3Notifications = _AlaVrrp3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 0)
)
_AlaVrrp3Operations_ObjectIdentity = ObjectIdentity
alaVrrp3Operations = _AlaVrrp3Operations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1)
)


class _AlaVrrp3NotificationCntl_Type(Integer32):
    """Custom type alaVrrp3NotificationCntl based on Integer32"""
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


_AlaVrrp3NotificationCntl_Type.__name__ = "Integer32"
_AlaVrrp3NotificationCntl_Object = MibScalar
alaVrrp3NotificationCntl = _AlaVrrp3NotificationCntl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 1),
    _AlaVrrp3NotificationCntl_Type()
)
alaVrrp3NotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrrp3NotificationCntl.setStatus("current")
_AlaVrrp3OperTable_Object = MibTable
alaVrrp3OperTable = _AlaVrrp3OperTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alaVrrp3OperTable.setStatus("current")
_AlaVrrp3OperEntry_Object = MibTableRow
alaVrrp3OperEntry = _AlaVrrp3OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1)
)
alaVrrp3OperEntry.setIndexNames(
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpVersion"),
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVrId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alaVrrp3OperEntry.setStatus("current")


class _AlaVrrp3OperIpVersion_Type(Integer32):
    """Custom type alaVrrp3OperIpVersion based on Integer32"""
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


_AlaVrrp3OperIpVersion_Type.__name__ = "Integer32"
_AlaVrrp3OperIpVersion_Object = MibTableColumn
alaVrrp3OperIpVersion = _AlaVrrp3OperIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 1),
    _AlaVrrp3OperIpVersion_Type()
)
alaVrrp3OperIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrrp3OperIpVersion.setStatus("current")
_AlaVrrp3OperVrId_Type = VrId
_AlaVrrp3OperVrId_Object = MibTableColumn
alaVrrp3OperVrId = _AlaVrrp3OperVrId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 2),
    _AlaVrrp3OperVrId_Type()
)
alaVrrp3OperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrrp3OperVrId.setStatus("current")
_AlaVrrp3OperVirtualMacAddr_Type = MacAddress
_AlaVrrp3OperVirtualMacAddr_Object = MibTableColumn
alaVrrp3OperVirtualMacAddr = _AlaVrrp3OperVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 3),
    _AlaVrrp3OperVirtualMacAddr_Type()
)
alaVrrp3OperVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperVirtualMacAddr.setStatus("current")


class _AlaVrrp3OperState_Type(Integer32):
    """Custom type alaVrrp3OperState based on Integer32"""
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


_AlaVrrp3OperState_Type.__name__ = "Integer32"
_AlaVrrp3OperState_Object = MibTableColumn
alaVrrp3OperState = _AlaVrrp3OperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 4),
    _AlaVrrp3OperState_Type()
)
alaVrrp3OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperState.setStatus("current")


class _AlaVrrp3OperAdminState_Type(Integer32):
    """Custom type alaVrrp3OperAdminState based on Integer32"""
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


_AlaVrrp3OperAdminState_Type.__name__ = "Integer32"
_AlaVrrp3OperAdminState_Object = MibTableColumn
alaVrrp3OperAdminState = _AlaVrrp3OperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 5),
    _AlaVrrp3OperAdminState_Type()
)
alaVrrp3OperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrp3OperAdminState.setStatus("current")


class _AlaVrrp3OperPriority_Type(Integer32):
    """Custom type alaVrrp3OperPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaVrrp3OperPriority_Type.__name__ = "Integer32"
_AlaVrrp3OperPriority_Object = MibTableColumn
alaVrrp3OperPriority = _AlaVrrp3OperPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 6),
    _AlaVrrp3OperPriority_Type()
)
alaVrrp3OperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrp3OperPriority.setStatus("current")


class _AlaVrrp3OperVersion_Type(Integer32):
    """Custom type alaVrrp3OperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vrrpv2", 1),
          ("vrrpv3", 2))
    )


_AlaVrrp3OperVersion_Type.__name__ = "Integer32"
_AlaVrrp3OperVersion_Object = MibTableColumn
alaVrrp3OperVersion = _AlaVrrp3OperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 7),
    _AlaVrrp3OperVersion_Type()
)
alaVrrp3OperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperVersion.setStatus("current")


class _AlaVrrp3OperIpAddrCount_Type(Integer32):
    """Custom type alaVrrp3OperIpAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaVrrp3OperIpAddrCount_Type.__name__ = "Integer32"
_AlaVrrp3OperIpAddrCount_Object = MibTableColumn
alaVrrp3OperIpAddrCount = _AlaVrrp3OperIpAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 8),
    _AlaVrrp3OperIpAddrCount_Type()
)
alaVrrp3OperIpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperIpAddrCount.setStatus("current")
_AlaVrrp3OperMasterIpAddrType_Type = InetAddressType
_AlaVrrp3OperMasterIpAddrType_Object = MibTableColumn
alaVrrp3OperMasterIpAddrType = _AlaVrrp3OperMasterIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 9),
    _AlaVrrp3OperMasterIpAddrType_Type()
)
alaVrrp3OperMasterIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperMasterIpAddrType.setStatus("current")
_AlaVrrp3OperMasterIpAddr_Type = InetAddress
_AlaVrrp3OperMasterIpAddr_Object = MibTableColumn
alaVrrp3OperMasterIpAddr = _AlaVrrp3OperMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 10),
    _AlaVrrp3OperMasterIpAddr_Type()
)
alaVrrp3OperMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperMasterIpAddr.setStatus("current")
_AlaVrrp3OperPrimaryIpAddrType_Type = InetAddressType
_AlaVrrp3OperPrimaryIpAddrType_Object = MibTableColumn
alaVrrp3OperPrimaryIpAddrType = _AlaVrrp3OperPrimaryIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 11),
    _AlaVrrp3OperPrimaryIpAddrType_Type()
)
alaVrrp3OperPrimaryIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperPrimaryIpAddrType.setStatus("current")


class _AlaVrrp3OperPrimaryIpAddr_Type(InetAddress):
    """Custom type alaVrrp3OperPrimaryIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_AlaVrrp3OperPrimaryIpAddr_Object = MibTableColumn
alaVrrp3OperPrimaryIpAddr = _AlaVrrp3OperPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 12),
    _AlaVrrp3OperPrimaryIpAddr_Type()
)
alaVrrp3OperPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperPrimaryIpAddr.setStatus("current")


class _AlaVrrp3OperAdvInterval_Type(Integer32):
    """Custom type alaVrrp3OperAdvInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AlaVrrp3OperAdvInterval_Type.__name__ = "Integer32"
_AlaVrrp3OperAdvInterval_Object = MibTableColumn
alaVrrp3OperAdvInterval = _AlaVrrp3OperAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 13),
    _AlaVrrp3OperAdvInterval_Type()
)
alaVrrp3OperAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrp3OperAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaVrrp3OperAdvInterval.setUnits("centiseconds")


class _AlaVrrp3OperPreemptMode_Type(TruthValue):
    """Custom type alaVrrp3OperPreemptMode based on TruthValue"""


_AlaVrrp3OperPreemptMode_Object = MibTableColumn
alaVrrp3OperPreemptMode = _AlaVrrp3OperPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 14),
    _AlaVrrp3OperPreemptMode_Type()
)
alaVrrp3OperPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrp3OperPreemptMode.setStatus("current")


class _AlaVrrp3OperAcceptMode_Type(TruthValue):
    """Custom type alaVrrp3OperAcceptMode based on TruthValue"""


_AlaVrrp3OperAcceptMode_Object = MibTableColumn
alaVrrp3OperAcceptMode = _AlaVrrp3OperAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 15),
    _AlaVrrp3OperAcceptMode_Type()
)
alaVrrp3OperAcceptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrp3OperAcceptMode.setStatus("current")
_AlaVrrp3OperUpTime_Type = TimeStamp
_AlaVrrp3OperUpTime_Object = MibTableColumn
alaVrrp3OperUpTime = _AlaVrrp3OperUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 16),
    _AlaVrrp3OperUpTime_Type()
)
alaVrrp3OperUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3OperUpTime.setStatus("current")
_AlaVrrp3OperRowStatus_Type = RowStatus
_AlaVrrp3OperRowStatus_Object = MibTableColumn
alaVrrp3OperRowStatus = _AlaVrrp3OperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 17),
    _AlaVrrp3OperRowStatus_Type()
)
alaVrrp3OperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrp3OperRowStatus.setStatus("current")
_AlaVrrp3AssoIpAddrTable_Object = MibTable
alaVrrp3AssoIpAddrTable = _AlaVrrp3AssoIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3)
)
if mibBuilder.loadTexts:
    alaVrrp3AssoIpAddrTable.setStatus("current")
_AlaVrrp3AssoIpAddrEntry_Object = MibTableRow
alaVrrp3AssoIpAddrEntry = _AlaVrrp3AssoIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3, 1)
)
alaVrrp3AssoIpAddrEntry.setIndexNames(
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpVersion"),
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVrId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3AssoIpAddrType"),
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3AssoIpAddr"),
)
if mibBuilder.loadTexts:
    alaVrrp3AssoIpAddrEntry.setStatus("current")
_AlaVrrp3AssoIpAddrType_Type = InetAddressType
_AlaVrrp3AssoIpAddrType_Object = MibTableColumn
alaVrrp3AssoIpAddrType = _AlaVrrp3AssoIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3, 1, 1),
    _AlaVrrp3AssoIpAddrType_Type()
)
alaVrrp3AssoIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrrp3AssoIpAddrType.setStatus("current")


class _AlaVrrp3AssoIpAddr_Type(InetAddress):
    """Custom type alaVrrp3AssoIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaVrrp3AssoIpAddr_Type.__name__ = "InetAddress"
_AlaVrrp3AssoIpAddr_Object = MibTableColumn
alaVrrp3AssoIpAddr = _AlaVrrp3AssoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3, 1, 2),
    _AlaVrrp3AssoIpAddr_Type()
)
alaVrrp3AssoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrrp3AssoIpAddr.setStatus("current")
_AlaVrrp3AssoIpAddrRowStatus_Type = RowStatus
_AlaVrrp3AssoIpAddrRowStatus_Object = MibTableColumn
alaVrrp3AssoIpAddrRowStatus = _AlaVrrp3AssoIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3, 1, 3),
    _AlaVrrp3AssoIpAddrRowStatus_Type()
)
alaVrrp3AssoIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrp3AssoIpAddrRowStatus.setStatus("current")


class _AlaVrrp3TrapNewMasterReason_Type(Integer32):
    """Custom type alaVrrp3TrapNewMasterReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterNoResponse", 2),
          ("preempted", 1),
          ("priority", 0))
    )


_AlaVrrp3TrapNewMasterReason_Type.__name__ = "Integer32"
_AlaVrrp3TrapNewMasterReason_Object = MibScalar
alaVrrp3TrapNewMasterReason = _AlaVrrp3TrapNewMasterReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 4),
    _AlaVrrp3TrapNewMasterReason_Type()
)
alaVrrp3TrapNewMasterReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVrrp3TrapNewMasterReason.setStatus("current")


class _AlaVrrp3TrapProtoErrReason_Type(Integer32):
    """Custom type alaVrrp3TrapProtoErrReason based on Integer32"""
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


_AlaVrrp3TrapProtoErrReason_Type.__name__ = "Integer32"
_AlaVrrp3TrapProtoErrReason_Object = MibScalar
alaVrrp3TrapProtoErrReason = _AlaVrrp3TrapProtoErrReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 5),
    _AlaVrrp3TrapProtoErrReason_Type()
)
alaVrrp3TrapProtoErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVrrp3TrapProtoErrReason.setStatus("current")
_AlaVrrp3Statistics_ObjectIdentity = ObjectIdentity
alaVrrp3Statistics = _AlaVrrp3Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2)
)
_AlaVrrp3RouterChecksumErrors_Type = Counter32
_AlaVrrp3RouterChecksumErrors_Object = MibScalar
alaVrrp3RouterChecksumErrors = _AlaVrrp3RouterChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 1),
    _AlaVrrp3RouterChecksumErrors_Type()
)
alaVrrp3RouterChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3RouterChecksumErrors.setStatus("current")
_AlaVrrp3RouterVersionErrors_Type = Counter32
_AlaVrrp3RouterVersionErrors_Object = MibScalar
alaVrrp3RouterVersionErrors = _AlaVrrp3RouterVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 2),
    _AlaVrrp3RouterVersionErrors_Type()
)
alaVrrp3RouterVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3RouterVersionErrors.setStatus("current")
_AlaVrrp3RouterVrIdErrors_Type = Counter32
_AlaVrrp3RouterVrIdErrors_Object = MibScalar
alaVrrp3RouterVrIdErrors = _AlaVrrp3RouterVrIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 3),
    _AlaVrrp3RouterVrIdErrors_Type()
)
alaVrrp3RouterVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3RouterVrIdErrors.setStatus("current")
_AlaVrrp3RouterStatsTable_Object = MibTable
alaVrrp3RouterStatsTable = _AlaVrrp3RouterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4)
)
if mibBuilder.loadTexts:
    alaVrrp3RouterStatsTable.setStatus("current")
_AlaVrrp3RouterStatsEntry_Object = MibTableRow
alaVrrp3RouterStatsEntry = _AlaVrrp3RouterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1)
)
alaVrrp3RouterStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpVersion"),
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVrId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alaVrrp3RouterStatsEntry.setStatus("current")
_AlaVrrp3StatsBecomeMaster_Type = Counter32
_AlaVrrp3StatsBecomeMaster_Object = MibTableColumn
alaVrrp3StatsBecomeMaster = _AlaVrrp3StatsBecomeMaster_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 1),
    _AlaVrrp3StatsBecomeMaster_Type()
)
alaVrrp3StatsBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsBecomeMaster.setStatus("current")
_AlaVrrp3StatsAdvertiseRcvd_Type = Counter32
_AlaVrrp3StatsAdvertiseRcvd_Object = MibTableColumn
alaVrrp3StatsAdvertiseRcvd = _AlaVrrp3StatsAdvertiseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 2),
    _AlaVrrp3StatsAdvertiseRcvd_Type()
)
alaVrrp3StatsAdvertiseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsAdvertiseRcvd.setStatus("current")
_AlaVrrp3StatsAdvIntervalErrors_Type = Counter32
_AlaVrrp3StatsAdvIntervalErrors_Object = MibTableColumn
alaVrrp3StatsAdvIntervalErrors = _AlaVrrp3StatsAdvIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 3),
    _AlaVrrp3StatsAdvIntervalErrors_Type()
)
alaVrrp3StatsAdvIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsAdvIntervalErrors.setStatus("current")
_AlaVrrp3StatsIpTtlErrors_Type = Counter32
_AlaVrrp3StatsIpTtlErrors_Object = MibTableColumn
alaVrrp3StatsIpTtlErrors = _AlaVrrp3StatsIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 4),
    _AlaVrrp3StatsIpTtlErrors_Type()
)
alaVrrp3StatsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsIpTtlErrors.setStatus("current")
_AlaVrrp3StatsPriZeroPktsRcvd_Type = Counter32
_AlaVrrp3StatsPriZeroPktsRcvd_Object = MibTableColumn
alaVrrp3StatsPriZeroPktsRcvd = _AlaVrrp3StatsPriZeroPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 5),
    _AlaVrrp3StatsPriZeroPktsRcvd_Type()
)
alaVrrp3StatsPriZeroPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsPriZeroPktsRcvd.setStatus("current")
_AlaVrrp3StatsPriZeroPktsSent_Type = Counter32
_AlaVrrp3StatsPriZeroPktsSent_Object = MibTableColumn
alaVrrp3StatsPriZeroPktsSent = _AlaVrrp3StatsPriZeroPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 6),
    _AlaVrrp3StatsPriZeroPktsSent_Type()
)
alaVrrp3StatsPriZeroPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsPriZeroPktsSent.setStatus("current")
_AlaVrrp3StatsInvldTypePktsRcvd_Type = Counter32
_AlaVrrp3StatsInvldTypePktsRcvd_Object = MibTableColumn
alaVrrp3StatsInvldTypePktsRcvd = _AlaVrrp3StatsInvldTypePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 7),
    _AlaVrrp3StatsInvldTypePktsRcvd_Type()
)
alaVrrp3StatsInvldTypePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsInvldTypePktsRcvd.setStatus("current")
_AlaVrrp3StatsAddressListErrors_Type = Counter32
_AlaVrrp3StatsAddressListErrors_Object = MibTableColumn
alaVrrp3StatsAddressListErrors = _AlaVrrp3StatsAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 8),
    _AlaVrrp3StatsAddressListErrors_Type()
)
alaVrrp3StatsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsAddressListErrors.setStatus("current")
_AlaVrrp3StatsInvldAuthType_Type = Counter32
_AlaVrrp3StatsInvldAuthType_Object = MibTableColumn
alaVrrp3StatsInvldAuthType = _AlaVrrp3StatsInvldAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 9),
    _AlaVrrp3StatsInvldAuthType_Type()
)
alaVrrp3StatsInvldAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsInvldAuthType.setStatus("current")
_AlaVrrp3StatsPacketLengthErrors_Type = Counter32
_AlaVrrp3StatsPacketLengthErrors_Object = MibTableColumn
alaVrrp3StatsPacketLengthErrors = _AlaVrrp3StatsPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 10),
    _AlaVrrp3StatsPacketLengthErrors_Type()
)
alaVrrp3StatsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3StatsPacketLengthErrors.setStatus("current")
_AlaVrrp3Conformance_ObjectIdentity = ObjectIdentity
alaVrrp3Conformance = _AlaVrrp3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3)
)
_AlaVrrp3MIBCompliances_ObjectIdentity = ObjectIdentity
alaVrrp3MIBCompliances = _AlaVrrp3MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 1)
)
_AlaVrrp3MIBGroups_ObjectIdentity = ObjectIdentity
alaVrrp3MIBGroups = _AlaVrrp3MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2)
)

# Managed Objects groups

alaVrrp3OperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2, 1)
)
alaVrrp3OperGroup.setObjects(
      *(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3NotificationCntl"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVirtualMacAddr"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperState"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperAdminState"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperPriority"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVersion"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpAddrCount"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperMasterIpAddrType"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperMasterIpAddr"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperPrimaryIpAddrType"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperPrimaryIpAddr"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperAdvInterval"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperPreemptMode"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperAcceptMode"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperUpTime"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperRowStatus"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3AssoIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    alaVrrp3OperGroup.setStatus("current")

alaVrrp3StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2, 2)
)
alaVrrp3StatsGroup.setObjects(
      *(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3RouterChecksumErrors"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3RouterVersionErrors"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3RouterVrIdErrors"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsBecomeMaster"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsAdvertiseRcvd"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsAdvIntervalErrors"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsPriZeroPktsRcvd"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsPriZeroPktsSent"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsInvldTypePktsRcvd"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsInvldAuthType"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsIpTtlErrors"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsAddressListErrors"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsPacketLengthErrors"))
)
if mibBuilder.loadTexts:
    alaVrrp3StatsGroup.setStatus("current")

alaVrrp3TrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2, 3)
)
alaVrrp3TrapInfoGroup.setObjects(
      *(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapNewMasterReason"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapProtoErrReason"))
)
if mibBuilder.loadTexts:
    alaVrrp3TrapInfoGroup.setStatus("current")


# Notification objects

alaVrrp3TrapNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 0, 1)
)
alaVrrp3TrapNewMaster.setObjects(
      *(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperMasterIpAddrType"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperMasterIpAddr"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapNewMasterReason"))
)
if mibBuilder.loadTexts:
    alaVrrp3TrapNewMaster.setStatus(
        "current"
    )

alaVrrp3TrapProtoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 0, 2)
)
alaVrrp3TrapProtoError.setObjects(
    ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapProtoErrReason")
)
if mibBuilder.loadTexts:
    alaVrrp3TrapProtoError.setStatus(
        "current"
    )


# Notifications groups

alaVrrp3NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2, 4)
)
alaVrrp3NotificationsGroup.setObjects(
      *(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapNewMaster"),
        ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapProtoError"))
)
if mibBuilder.loadTexts:
    alaVrrp3NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaVrrp3MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alaVrrp3MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VRRP3-MIB",
    **{"alcatelIND1VRRP3MIB": alcatelIND1VRRP3MIB,
       "alaVrrp3Notifications": alaVrrp3Notifications,
       "alaVrrp3TrapNewMaster": alaVrrp3TrapNewMaster,
       "alaVrrp3TrapProtoError": alaVrrp3TrapProtoError,
       "alaVrrp3Operations": alaVrrp3Operations,
       "alaVrrp3NotificationCntl": alaVrrp3NotificationCntl,
       "alaVrrp3OperTable": alaVrrp3OperTable,
       "alaVrrp3OperEntry": alaVrrp3OperEntry,
       "alaVrrp3OperIpVersion": alaVrrp3OperIpVersion,
       "alaVrrp3OperVrId": alaVrrp3OperVrId,
       "alaVrrp3OperVirtualMacAddr": alaVrrp3OperVirtualMacAddr,
       "alaVrrp3OperState": alaVrrp3OperState,
       "alaVrrp3OperAdminState": alaVrrp3OperAdminState,
       "alaVrrp3OperPriority": alaVrrp3OperPriority,
       "alaVrrp3OperVersion": alaVrrp3OperVersion,
       "alaVrrp3OperIpAddrCount": alaVrrp3OperIpAddrCount,
       "alaVrrp3OperMasterIpAddrType": alaVrrp3OperMasterIpAddrType,
       "alaVrrp3OperMasterIpAddr": alaVrrp3OperMasterIpAddr,
       "alaVrrp3OperPrimaryIpAddrType": alaVrrp3OperPrimaryIpAddrType,
       "alaVrrp3OperPrimaryIpAddr": alaVrrp3OperPrimaryIpAddr,
       "alaVrrp3OperAdvInterval": alaVrrp3OperAdvInterval,
       "alaVrrp3OperPreemptMode": alaVrrp3OperPreemptMode,
       "alaVrrp3OperAcceptMode": alaVrrp3OperAcceptMode,
       "alaVrrp3OperUpTime": alaVrrp3OperUpTime,
       "alaVrrp3OperRowStatus": alaVrrp3OperRowStatus,
       "alaVrrp3AssoIpAddrTable": alaVrrp3AssoIpAddrTable,
       "alaVrrp3AssoIpAddrEntry": alaVrrp3AssoIpAddrEntry,
       "alaVrrp3AssoIpAddrType": alaVrrp3AssoIpAddrType,
       "alaVrrp3AssoIpAddr": alaVrrp3AssoIpAddr,
       "alaVrrp3AssoIpAddrRowStatus": alaVrrp3AssoIpAddrRowStatus,
       "alaVrrp3TrapNewMasterReason": alaVrrp3TrapNewMasterReason,
       "alaVrrp3TrapProtoErrReason": alaVrrp3TrapProtoErrReason,
       "alaVrrp3Statistics": alaVrrp3Statistics,
       "alaVrrp3RouterChecksumErrors": alaVrrp3RouterChecksumErrors,
       "alaVrrp3RouterVersionErrors": alaVrrp3RouterVersionErrors,
       "alaVrrp3RouterVrIdErrors": alaVrrp3RouterVrIdErrors,
       "alaVrrp3RouterStatsTable": alaVrrp3RouterStatsTable,
       "alaVrrp3RouterStatsEntry": alaVrrp3RouterStatsEntry,
       "alaVrrp3StatsBecomeMaster": alaVrrp3StatsBecomeMaster,
       "alaVrrp3StatsAdvertiseRcvd": alaVrrp3StatsAdvertiseRcvd,
       "alaVrrp3StatsAdvIntervalErrors": alaVrrp3StatsAdvIntervalErrors,
       "alaVrrp3StatsIpTtlErrors": alaVrrp3StatsIpTtlErrors,
       "alaVrrp3StatsPriZeroPktsRcvd": alaVrrp3StatsPriZeroPktsRcvd,
       "alaVrrp3StatsPriZeroPktsSent": alaVrrp3StatsPriZeroPktsSent,
       "alaVrrp3StatsInvldTypePktsRcvd": alaVrrp3StatsInvldTypePktsRcvd,
       "alaVrrp3StatsAddressListErrors": alaVrrp3StatsAddressListErrors,
       "alaVrrp3StatsInvldAuthType": alaVrrp3StatsInvldAuthType,
       "alaVrrp3StatsPacketLengthErrors": alaVrrp3StatsPacketLengthErrors,
       "alaVrrp3Conformance": alaVrrp3Conformance,
       "alaVrrp3MIBCompliances": alaVrrp3MIBCompliances,
       "alaVrrp3MIBCompliance": alaVrrp3MIBCompliance,
       "alaVrrp3MIBGroups": alaVrrp3MIBGroups,
       "alaVrrp3OperGroup": alaVrrp3OperGroup,
       "alaVrrp3StatsGroup": alaVrrp3StatsGroup,
       "alaVrrp3TrapInfoGroup": alaVrrp3TrapInfoGroup,
       "alaVrrp3NotificationsGroup": alaVrrp3NotificationsGroup}
)
