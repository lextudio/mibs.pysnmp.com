# SNMP MIB module (ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:37 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swERPSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 78)
)


# Types definitions



class VidList(OctetString):
    """Custom type VidList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwERPSCtrl_ObjectIdentity = ObjectIdentity
swERPSCtrl = _SwERPSCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 1)
)


class _SwERPSAdminState_Type(Integer32):
    """Custom type swERPSAdminState based on Integer32"""
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


_SwERPSAdminState_Type.__name__ = "Integer32"
_SwERPSAdminState_Object = MibScalar
swERPSAdminState = _SwERPSAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 1, 1),
    _SwERPSAdminState_Type()
)
swERPSAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSAdminState.setStatus("current")


class _SwERPSLogState_Type(Integer32):
    """Custom type swERPSLogState based on Integer32"""
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


_SwERPSLogState_Type.__name__ = "Integer32"
_SwERPSLogState_Object = MibScalar
swERPSLogState = _SwERPSLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 1, 2),
    _SwERPSLogState_Type()
)
swERPSLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSLogState.setStatus("current")


class _SwERPSTrapState_Type(Integer32):
    """Custom type swERPSTrapState based on Integer32"""
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


_SwERPSTrapState_Type.__name__ = "Integer32"
_SwERPSTrapState_Object = MibScalar
swERPSTrapState = _SwERPSTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 1, 3),
    _SwERPSTrapState_Type()
)
swERPSTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSTrapState.setStatus("current")
_SwERPSInfo_ObjectIdentity = ObjectIdentity
swERPSInfo = _SwERPSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 2)
)
_SwERPSMgmt_ObjectIdentity = ObjectIdentity
swERPSMgmt = _SwERPSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3)
)
_SwERPSMgmtRAPSVlanTable_Object = MibTable
swERPSMgmtRAPSVlanTable = _SwERPSMgmtRAPSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1)
)
if mibBuilder.loadTexts:
    swERPSMgmtRAPSVlanTable.setStatus("current")
_SwERPSMgmtRAPSVlanEntry_Object = MibTableRow
swERPSMgmtRAPSVlanEntry = _SwERPSMgmtRAPSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1)
)
swERPSMgmtRAPSVlanEntry.setIndexNames(
    (0, "ERPS-MIB", "swERPSMgmtRAPSVlanId"),
)
if mibBuilder.loadTexts:
    swERPSMgmtRAPSVlanEntry.setStatus("current")
_SwERPSMgmtRAPSVlanId_Type = Integer32
_SwERPSMgmtRAPSVlanId_Object = MibTableColumn
swERPSMgmtRAPSVlanId = _SwERPSMgmtRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 1),
    _SwERPSMgmtRAPSVlanId_Type()
)
swERPSMgmtRAPSVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSVlanId.setStatus("current")


class _SwERPSMgmtRAPSWestPort_Type(Integer32):
    """Custom type swERPSMgmtRAPSWestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_SwERPSMgmtRAPSWestPort_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSWestPort_Object = MibTableColumn
swERPSMgmtRAPSWestPort = _SwERPSMgmtRAPSWestPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 2),
    _SwERPSMgmtRAPSWestPort_Type()
)
swERPSMgmtRAPSWestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSWestPort.setStatus("current")


class _SwERPSMgmtRAPSWestPortState_Type(Integer32):
    """Custom type swERPSMgmtRAPSWestPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("fowarding", 1),
          ("signal-fail", 3))
    )


_SwERPSMgmtRAPSWestPortState_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSWestPortState_Object = MibTableColumn
swERPSMgmtRAPSWestPortState = _SwERPSMgmtRAPSWestPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 3),
    _SwERPSMgmtRAPSWestPortState_Type()
)
swERPSMgmtRAPSWestPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSWestPortState.setStatus("current")


class _SwERPSMgmtRAPSEastPort_Type(Integer32):
    """Custom type swERPSMgmtRAPSEastPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_SwERPSMgmtRAPSEastPort_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSEastPort_Object = MibTableColumn
swERPSMgmtRAPSEastPort = _SwERPSMgmtRAPSEastPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 4),
    _SwERPSMgmtRAPSEastPort_Type()
)
swERPSMgmtRAPSEastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSEastPort.setStatus("current")


class _SwERPSMgmtRAPSEastPortState_Type(Integer32):
    """Custom type swERPSMgmtRAPSEastPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("fowarding", 1),
          ("signal-fail", 3))
    )


_SwERPSMgmtRAPSEastPortState_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSEastPortState_Object = MibTableColumn
swERPSMgmtRAPSEastPortState = _SwERPSMgmtRAPSEastPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 5),
    _SwERPSMgmtRAPSEastPortState_Type()
)
swERPSMgmtRAPSEastPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSEastPortState.setStatus("current")


class _SwERPSMgmtRAPSRPLPort_Type(Integer32):
    """Custom type swERPSMgmtRAPSRPLPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 3),
          ("none", 1),
          ("west", 2))
    )


_SwERPSMgmtRAPSRPLPort_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSRPLPort_Object = MibTableColumn
swERPSMgmtRAPSRPLPort = _SwERPSMgmtRAPSRPLPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 6),
    _SwERPSMgmtRAPSRPLPort_Type()
)
swERPSMgmtRAPSRPLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRPLPort.setStatus("current")


class _SwERPSMgmtRAPSRPLOwnerAdminState_Type(Integer32):
    """Custom type swERPSMgmtRAPSRPLOwnerAdminState based on Integer32"""
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


_SwERPSMgmtRAPSRPLOwnerAdminState_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSRPLOwnerAdminState_Object = MibTableColumn
swERPSMgmtRAPSRPLOwnerAdminState = _SwERPSMgmtRAPSRPLOwnerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 7),
    _SwERPSMgmtRAPSRPLOwnerAdminState_Type()
)
swERPSMgmtRAPSRPLOwnerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRPLOwnerAdminState.setStatus("current")
_SwERPSMgmtRAPSProtectionVlan_Type = VidList
_SwERPSMgmtRAPSProtectionVlan_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlan = _SwERPSMgmtRAPSProtectionVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 8),
    _SwERPSMgmtRAPSProtectionVlan_Type()
)
swERPSMgmtRAPSProtectionVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlan.setStatus("current")


class _SwERPSMgmtRAPSRingMEL_Type(Integer32):
    """Custom type swERPSMgmtRAPSRingMEL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwERPSMgmtRAPSRingMEL_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSRingMEL_Object = MibTableColumn
swERPSMgmtRAPSRingMEL = _SwERPSMgmtRAPSRingMEL_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 9),
    _SwERPSMgmtRAPSRingMEL_Type()
)
swERPSMgmtRAPSRingMEL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRingMEL.setStatus("current")


class _SwERPSMgmtRAPSHoldOffTime_Type(Integer32):
    """Custom type swERPSMgmtRAPSHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SwERPSMgmtRAPSHoldOffTime_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSHoldOffTime_Object = MibTableColumn
swERPSMgmtRAPSHoldOffTime = _SwERPSMgmtRAPSHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 10),
    _SwERPSMgmtRAPSHoldOffTime_Type()
)
swERPSMgmtRAPSHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSHoldOffTime.setStatus("current")


class _SwERPSMgmtRAPSGuardTime_Type(Integer32):
    """Custom type swERPSMgmtRAPSGuardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_SwERPSMgmtRAPSGuardTime_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSGuardTime_Object = MibTableColumn
swERPSMgmtRAPSGuardTime = _SwERPSMgmtRAPSGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 11),
    _SwERPSMgmtRAPSGuardTime_Type()
)
swERPSMgmtRAPSGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSGuardTime.setStatus("current")


class _SwERPSMgmtRAPSWTRTime_Type(Integer32):
    """Custom type swERPSMgmtRAPSWTRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_SwERPSMgmtRAPSWTRTime_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSWTRTime_Object = MibTableColumn
swERPSMgmtRAPSWTRTime = _SwERPSMgmtRAPSWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 12),
    _SwERPSMgmtRAPSWTRTime_Type()
)
swERPSMgmtRAPSWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSWTRTime.setStatus("current")


class _SwERPSMgmtRAPSRingState_Type(Integer32):
    """Custom type swERPSMgmtRAPSRingState based on Integer32"""
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
        *(("begin", 1),
          ("idle", 3),
          ("init", 2),
          ("protection", 4))
    )


_SwERPSMgmtRAPSRingState_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSRingState_Object = MibTableColumn
swERPSMgmtRAPSRingState = _SwERPSMgmtRAPSRingState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 13),
    _SwERPSMgmtRAPSRingState_Type()
)
swERPSMgmtRAPSRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRingState.setStatus("current")


class _SwERPSMgmtRAPSRingAdminState_Type(Integer32):
    """Custom type swERPSMgmtRAPSRingAdminState based on Integer32"""
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


_SwERPSMgmtRAPSRingAdminState_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSRingAdminState_Object = MibTableColumn
swERPSMgmtRAPSRingAdminState = _SwERPSMgmtRAPSRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 14),
    _SwERPSMgmtRAPSRingAdminState_Type()
)
swERPSMgmtRAPSRingAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRingAdminState.setStatus("current")


class _SwERPSMgmtRAPSRPLOwnerOperStatus_Type(Integer32):
    """Custom type swERPSMgmtRAPSRPLOwnerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 3),
          ("inactive", 2))
    )


_SwERPSMgmtRAPSRPLOwnerOperStatus_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSRPLOwnerOperStatus_Object = MibTableColumn
swERPSMgmtRAPSRPLOwnerOperStatus = _SwERPSMgmtRAPSRPLOwnerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 15),
    _SwERPSMgmtRAPSRPLOwnerOperStatus_Type()
)
swERPSMgmtRAPSRPLOwnerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRPLOwnerOperStatus.setStatus("current")


class _SwERPSMgmtRAPSProtectionVlanRangeList1to64_Type(OctetString):
    """Custom type swERPSMgmtRAPSProtectionVlanRangeList1to64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwERPSMgmtRAPSProtectionVlanRangeList1to64_Type.__name__ = "OctetString"
_SwERPSMgmtRAPSProtectionVlanRangeList1to64_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlanRangeList1to64 = _SwERPSMgmtRAPSProtectionVlanRangeList1to64_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 16),
    _SwERPSMgmtRAPSProtectionVlanRangeList1to64_Type()
)
swERPSMgmtRAPSProtectionVlanRangeList1to64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlanRangeList1to64.setStatus("current")


class _SwERPSMgmtRAPSProtectionVlanRangeList65to128_Type(OctetString):
    """Custom type swERPSMgmtRAPSProtectionVlanRangeList65to128 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwERPSMgmtRAPSProtectionVlanRangeList65to128_Type.__name__ = "OctetString"
_SwERPSMgmtRAPSProtectionVlanRangeList65to128_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlanRangeList65to128 = _SwERPSMgmtRAPSProtectionVlanRangeList65to128_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 17),
    _SwERPSMgmtRAPSProtectionVlanRangeList65to128_Type()
)
swERPSMgmtRAPSProtectionVlanRangeList65to128.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlanRangeList65to128.setStatus("current")


class _SwERPSMgmtRAPSProtectionVlanRangeList129to192_Type(OctetString):
    """Custom type swERPSMgmtRAPSProtectionVlanRangeList129to192 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwERPSMgmtRAPSProtectionVlanRangeList129to192_Type.__name__ = "OctetString"
_SwERPSMgmtRAPSProtectionVlanRangeList129to192_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlanRangeList129to192 = _SwERPSMgmtRAPSProtectionVlanRangeList129to192_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 18),
    _SwERPSMgmtRAPSProtectionVlanRangeList129to192_Type()
)
swERPSMgmtRAPSProtectionVlanRangeList129to192.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlanRangeList129to192.setStatus("current")


class _SwERPSMgmtRAPSProtectionVlanRangeList193to256_Type(OctetString):
    """Custom type swERPSMgmtRAPSProtectionVlanRangeList193to256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwERPSMgmtRAPSProtectionVlanRangeList193to256_Type.__name__ = "OctetString"
_SwERPSMgmtRAPSProtectionVlanRangeList193to256_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlanRangeList193to256 = _SwERPSMgmtRAPSProtectionVlanRangeList193to256_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 19),
    _SwERPSMgmtRAPSProtectionVlanRangeList193to256_Type()
)
swERPSMgmtRAPSProtectionVlanRangeList193to256.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlanRangeList193to256.setStatus("current")


class _SwERPSMgmtRAPSProtectionVlanRangeList257to320_Type(OctetString):
    """Custom type swERPSMgmtRAPSProtectionVlanRangeList257to320 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwERPSMgmtRAPSProtectionVlanRangeList257to320_Type.__name__ = "OctetString"
_SwERPSMgmtRAPSProtectionVlanRangeList257to320_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlanRangeList257to320 = _SwERPSMgmtRAPSProtectionVlanRangeList257to320_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 20),
    _SwERPSMgmtRAPSProtectionVlanRangeList257to320_Type()
)
swERPSMgmtRAPSProtectionVlanRangeList257to320.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlanRangeList257to320.setStatus("current")


class _SwERPSMgmtRAPSProtectionVlanRangeList321to384_Type(OctetString):
    """Custom type swERPSMgmtRAPSProtectionVlanRangeList321to384 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwERPSMgmtRAPSProtectionVlanRangeList321to384_Type.__name__ = "OctetString"
_SwERPSMgmtRAPSProtectionVlanRangeList321to384_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlanRangeList321to384 = _SwERPSMgmtRAPSProtectionVlanRangeList321to384_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 21),
    _SwERPSMgmtRAPSProtectionVlanRangeList321to384_Type()
)
swERPSMgmtRAPSProtectionVlanRangeList321to384.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlanRangeList321to384.setStatus("current")


class _SwERPSMgmtRAPSProtectionVlanRangeList385to448_Type(OctetString):
    """Custom type swERPSMgmtRAPSProtectionVlanRangeList385to448 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwERPSMgmtRAPSProtectionVlanRangeList385to448_Type.__name__ = "OctetString"
_SwERPSMgmtRAPSProtectionVlanRangeList385to448_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlanRangeList385to448 = _SwERPSMgmtRAPSProtectionVlanRangeList385to448_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 22),
    _SwERPSMgmtRAPSProtectionVlanRangeList385to448_Type()
)
swERPSMgmtRAPSProtectionVlanRangeList385to448.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlanRangeList385to448.setStatus("current")


class _SwERPSMgmtRAPSProtectionVlanRangeList449to512_Type(OctetString):
    """Custom type swERPSMgmtRAPSProtectionVlanRangeList449to512 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwERPSMgmtRAPSProtectionVlanRangeList449to512_Type.__name__ = "OctetString"
_SwERPSMgmtRAPSProtectionVlanRangeList449to512_Object = MibTableColumn
swERPSMgmtRAPSProtectionVlanRangeList449to512 = _SwERPSMgmtRAPSProtectionVlanRangeList449to512_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 23),
    _SwERPSMgmtRAPSProtectionVlanRangeList449to512_Type()
)
swERPSMgmtRAPSProtectionVlanRangeList449to512.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSProtectionVlanRangeList449to512.setStatus("current")


class _SwERPSMgmtRAPSRevertive_Type(Integer32):
    """Custom type swERPSMgmtRAPSRevertive based on Integer32"""
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


_SwERPSMgmtRAPSRevertive_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSRevertive_Object = MibTableColumn
swERPSMgmtRAPSRevertive = _SwERPSMgmtRAPSRevertive_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 24),
    _SwERPSMgmtRAPSRevertive_Type()
)
swERPSMgmtRAPSRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRevertive.setStatus("current")


class _SwERPSMgmtRAPSOperWestPort_Type(Integer32):
    """Custom type swERPSMgmtRAPSOperWestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_SwERPSMgmtRAPSOperWestPort_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSOperWestPort_Object = MibTableColumn
swERPSMgmtRAPSOperWestPort = _SwERPSMgmtRAPSOperWestPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 25),
    _SwERPSMgmtRAPSOperWestPort_Type()
)
swERPSMgmtRAPSOperWestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSOperWestPort.setStatus("current")


class _SwERPSMgmtRAPSOperEastPort_Type(Integer32):
    """Custom type swERPSMgmtRAPSOperEastPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_SwERPSMgmtRAPSOperEastPort_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSOperEastPort_Object = MibTableColumn
swERPSMgmtRAPSOperEastPort = _SwERPSMgmtRAPSOperEastPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 26),
    _SwERPSMgmtRAPSOperEastPort_Type()
)
swERPSMgmtRAPSOperEastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSOperEastPort.setStatus("current")


class _SwERPSMgmtRAPSOperRPLPort_Type(Integer32):
    """Custom type swERPSMgmtRAPSOperRPLPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 3),
          ("none", 1),
          ("west", 2))
    )


_SwERPSMgmtRAPSOperRPLPort_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSOperRPLPort_Object = MibTableColumn
swERPSMgmtRAPSOperRPLPort = _SwERPSMgmtRAPSOperRPLPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 27),
    _SwERPSMgmtRAPSOperRPLPort_Type()
)
swERPSMgmtRAPSOperRPLPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSOperRPLPort.setStatus("current")


class _SwERPSMgmtRAPSRPLOwnerOperState_Type(Integer32):
    """Custom type swERPSMgmtRAPSRPLOwnerOperState based on Integer32"""
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


_SwERPSMgmtRAPSRPLOwnerOperState_Type.__name__ = "Integer32"
_SwERPSMgmtRAPSRPLOwnerOperState_Object = MibTableColumn
swERPSMgmtRAPSRPLOwnerOperState = _SwERPSMgmtRAPSRPLOwnerOperState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 28),
    _SwERPSMgmtRAPSRPLOwnerOperState_Type()
)
swERPSMgmtRAPSRPLOwnerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRPLOwnerOperState.setStatus("current")
_SwERPSMgmtRAPSRowStatus_Type = RowStatus
_SwERPSMgmtRAPSRowStatus_Object = MibTableColumn
swERPSMgmtRAPSRowStatus = _SwERPSMgmtRAPSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 100),
    _SwERPSMgmtRAPSRowStatus_Type()
)
swERPSMgmtRAPSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swERPSMgmtRAPSRowStatus.setStatus("current")
_SwERPSMgmtSubRingCtrlTable_Object = MibTable
swERPSMgmtSubRingCtrlTable = _SwERPSMgmtSubRingCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2)
)
if mibBuilder.loadTexts:
    swERPSMgmtSubRingCtrlTable.setStatus("current")
_SwERPSMgmtSubRingCtrlEntry_Object = MibTableRow
swERPSMgmtSubRingCtrlEntry = _SwERPSMgmtSubRingCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1)
)
swERPSMgmtSubRingCtrlEntry.setIndexNames(
    (0, "ERPS-MIB", "swERPSMgmtSubRingCtrlRAPSVlanId"),
    (0, "ERPS-MIB", "swERPSMgmtSubRingCtrlSubRingRAPSVlanId"),
)
if mibBuilder.loadTexts:
    swERPSMgmtSubRingCtrlEntry.setStatus("current")
_SwERPSMgmtSubRingCtrlRAPSVlanId_Type = Integer32
_SwERPSMgmtSubRingCtrlRAPSVlanId_Object = MibTableColumn
swERPSMgmtSubRingCtrlRAPSVlanId = _SwERPSMgmtSubRingCtrlRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1, 1),
    _SwERPSMgmtSubRingCtrlRAPSVlanId_Type()
)
swERPSMgmtSubRingCtrlRAPSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swERPSMgmtSubRingCtrlRAPSVlanId.setStatus("current")
_SwERPSMgmtSubRingCtrlSubRingRAPSVlanId_Type = Integer32
_SwERPSMgmtSubRingCtrlSubRingRAPSVlanId_Object = MibTableColumn
swERPSMgmtSubRingCtrlSubRingRAPSVlanId = _SwERPSMgmtSubRingCtrlSubRingRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1, 2),
    _SwERPSMgmtSubRingCtrlSubRingRAPSVlanId_Type()
)
swERPSMgmtSubRingCtrlSubRingRAPSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swERPSMgmtSubRingCtrlSubRingRAPSVlanId.setStatus("current")


class _SwERPSMgmtSubRingCtrlTCPropagationState_Type(Integer32):
    """Custom type swERPSMgmtSubRingCtrlTCPropagationState based on Integer32"""
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


_SwERPSMgmtSubRingCtrlTCPropagationState_Type.__name__ = "Integer32"
_SwERPSMgmtSubRingCtrlTCPropagationState_Object = MibTableColumn
swERPSMgmtSubRingCtrlTCPropagationState = _SwERPSMgmtSubRingCtrlTCPropagationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1, 3),
    _SwERPSMgmtSubRingCtrlTCPropagationState_Type()
)
swERPSMgmtSubRingCtrlTCPropagationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swERPSMgmtSubRingCtrlTCPropagationState.setStatus("current")
_SwERPSMgmtSubRingCtrlRowStatus_Type = RowStatus
_SwERPSMgmtSubRingCtrlRowStatus_Object = MibTableColumn
swERPSMgmtSubRingCtrlRowStatus = _SwERPSMgmtSubRingCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1, 4),
    _SwERPSMgmtSubRingCtrlRowStatus_Type()
)
swERPSMgmtSubRingCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swERPSMgmtSubRingCtrlRowStatus.setStatus("current")
_SwERPSNotify_ObjectIdentity = ObjectIdentity
swERPSNotify = _SwERPSNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 4)
)
_SwERPSNotifyPrefix_ObjectIdentity = ObjectIdentity
swERPSNotifyPrefix = _SwERPSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 0)
)
_SwERPSNotificationBindings_ObjectIdentity = ObjectIdentity
swERPSNotificationBindings = _SwERPSNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 2)
)
_SwERPSNodeId_Type = MacAddress
_SwERPSNodeId_Object = MibScalar
swERPSNodeId = _SwERPSNodeId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 2, 1),
    _SwERPSNodeId_Type()
)
swERPSNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swERPSNodeId.setStatus("current")

# Managed Objects groups


# Notification objects

swERPSSFDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 0, 1)
)
swERPSSFDetectedTrap.setObjects(
    ("ERPS-MIB", "swERPSNodeId")
)
if mibBuilder.loadTexts:
    swERPSSFDetectedTrap.setStatus(
        "current"
    )

swERPSSFClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 0, 2)
)
swERPSSFClearedTrap.setObjects(
    ("ERPS-MIB", "swERPSNodeId")
)
if mibBuilder.loadTexts:
    swERPSSFClearedTrap.setStatus(
        "current"
    )

swERPSRPLOwnerConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 0, 3)
)
swERPSRPLOwnerConflictTrap.setObjects(
    ("ERPS-MIB", "swERPSNodeId")
)
if mibBuilder.loadTexts:
    swERPSRPLOwnerConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERPS-MIB",
    **{"VidList": VidList,
       "swERPSMIB": swERPSMIB,
       "swERPSCtrl": swERPSCtrl,
       "swERPSAdminState": swERPSAdminState,
       "swERPSLogState": swERPSLogState,
       "swERPSTrapState": swERPSTrapState,
       "swERPSInfo": swERPSInfo,
       "swERPSMgmt": swERPSMgmt,
       "swERPSMgmtRAPSVlanTable": swERPSMgmtRAPSVlanTable,
       "swERPSMgmtRAPSVlanEntry": swERPSMgmtRAPSVlanEntry,
       "swERPSMgmtRAPSVlanId": swERPSMgmtRAPSVlanId,
       "swERPSMgmtRAPSWestPort": swERPSMgmtRAPSWestPort,
       "swERPSMgmtRAPSWestPortState": swERPSMgmtRAPSWestPortState,
       "swERPSMgmtRAPSEastPort": swERPSMgmtRAPSEastPort,
       "swERPSMgmtRAPSEastPortState": swERPSMgmtRAPSEastPortState,
       "swERPSMgmtRAPSRPLPort": swERPSMgmtRAPSRPLPort,
       "swERPSMgmtRAPSRPLOwnerAdminState": swERPSMgmtRAPSRPLOwnerAdminState,
       "swERPSMgmtRAPSProtectionVlan": swERPSMgmtRAPSProtectionVlan,
       "swERPSMgmtRAPSRingMEL": swERPSMgmtRAPSRingMEL,
       "swERPSMgmtRAPSHoldOffTime": swERPSMgmtRAPSHoldOffTime,
       "swERPSMgmtRAPSGuardTime": swERPSMgmtRAPSGuardTime,
       "swERPSMgmtRAPSWTRTime": swERPSMgmtRAPSWTRTime,
       "swERPSMgmtRAPSRingState": swERPSMgmtRAPSRingState,
       "swERPSMgmtRAPSRingAdminState": swERPSMgmtRAPSRingAdminState,
       "swERPSMgmtRAPSRPLOwnerOperStatus": swERPSMgmtRAPSRPLOwnerOperStatus,
       "swERPSMgmtRAPSProtectionVlanRangeList1to64": swERPSMgmtRAPSProtectionVlanRangeList1to64,
       "swERPSMgmtRAPSProtectionVlanRangeList65to128": swERPSMgmtRAPSProtectionVlanRangeList65to128,
       "swERPSMgmtRAPSProtectionVlanRangeList129to192": swERPSMgmtRAPSProtectionVlanRangeList129to192,
       "swERPSMgmtRAPSProtectionVlanRangeList193to256": swERPSMgmtRAPSProtectionVlanRangeList193to256,
       "swERPSMgmtRAPSProtectionVlanRangeList257to320": swERPSMgmtRAPSProtectionVlanRangeList257to320,
       "swERPSMgmtRAPSProtectionVlanRangeList321to384": swERPSMgmtRAPSProtectionVlanRangeList321to384,
       "swERPSMgmtRAPSProtectionVlanRangeList385to448": swERPSMgmtRAPSProtectionVlanRangeList385to448,
       "swERPSMgmtRAPSProtectionVlanRangeList449to512": swERPSMgmtRAPSProtectionVlanRangeList449to512,
       "swERPSMgmtRAPSRevertive": swERPSMgmtRAPSRevertive,
       "swERPSMgmtRAPSOperWestPort": swERPSMgmtRAPSOperWestPort,
       "swERPSMgmtRAPSOperEastPort": swERPSMgmtRAPSOperEastPort,
       "swERPSMgmtRAPSOperRPLPort": swERPSMgmtRAPSOperRPLPort,
       "swERPSMgmtRAPSRPLOwnerOperState": swERPSMgmtRAPSRPLOwnerOperState,
       "swERPSMgmtRAPSRowStatus": swERPSMgmtRAPSRowStatus,
       "swERPSMgmtSubRingCtrlTable": swERPSMgmtSubRingCtrlTable,
       "swERPSMgmtSubRingCtrlEntry": swERPSMgmtSubRingCtrlEntry,
       "swERPSMgmtSubRingCtrlRAPSVlanId": swERPSMgmtSubRingCtrlRAPSVlanId,
       "swERPSMgmtSubRingCtrlSubRingRAPSVlanId": swERPSMgmtSubRingCtrlSubRingRAPSVlanId,
       "swERPSMgmtSubRingCtrlTCPropagationState": swERPSMgmtSubRingCtrlTCPropagationState,
       "swERPSMgmtSubRingCtrlRowStatus": swERPSMgmtSubRingCtrlRowStatus,
       "swERPSNotify": swERPSNotify,
       "swERPSNotifyPrefix": swERPSNotifyPrefix,
       "swERPSSFDetectedTrap": swERPSSFDetectedTrap,
       "swERPSSFClearedTrap": swERPSSFClearedTrap,
       "swERPSRPLOwnerConflictTrap": swERPSRPLOwnerConflictTrap,
       "swERPSNotificationBindings": swERPSNotificationBindings,
       "swERPSNodeId": swERPSNodeId}
)
