# SNMP MIB module (ELTEX-BRIDGE-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-BRIDGE-ERPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:03 2024
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

(eltexBridgeExtMIBObjects,) = mibBuilder.importSymbols(
    "ELTEX-BRIDGE-EXT-MIB",
    "eltexBridgeExtMIBObjects")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltexErpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexErpsEnabledState(Integer32, TextualConvention):
    status = "current"
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



class EltexErpsMgmtRAPSPortState(Integer32, TextualConvention):
    status = "current"
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
        *(("blocking", 2),
          ("forced-switch", 5),
          ("fowarding", 1),
          ("manual-switch", 4),
          ("signal-fail", 3))
    )



class EltexErpsMgmtRAPSPortId(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_EltexErpsCtrl_ObjectIdentity = ObjectIdentity
eltexErpsCtrl = _EltexErpsCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 1)
)


class _EltexErpsAdminState_Type(EltexErpsEnabledState):
    """Custom type eltexErpsAdminState based on EltexErpsEnabledState"""


_EltexErpsAdminState_Object = MibScalar
eltexErpsAdminState = _EltexErpsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 1, 1),
    _EltexErpsAdminState_Type()
)
eltexErpsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsAdminState.setStatus("current")


class _EltexErpsLogState_Type(EltexErpsEnabledState):
    """Custom type eltexErpsLogState based on EltexErpsEnabledState"""


_EltexErpsLogState_Object = MibScalar
eltexErpsLogState = _EltexErpsLogState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 1, 2),
    _EltexErpsLogState_Type()
)
eltexErpsLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsLogState.setStatus("current")


class _EltexErpsTrapState_Type(EltexErpsEnabledState):
    """Custom type eltexErpsTrapState based on EltexErpsEnabledState"""


_EltexErpsTrapState_Object = MibScalar
eltexErpsTrapState = _EltexErpsTrapState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 1, 3),
    _EltexErpsTrapState_Type()
)
eltexErpsTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsTrapState.setStatus("current")


class _EltexErpsPendingAction_Type(Integer32):
    """Custom type eltexErpsPendingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyActivePending", 2),
          ("copyPendingActive", 1))
    )


_EltexErpsPendingAction_Type.__name__ = "Integer32"
_EltexErpsPendingAction_Object = MibScalar
eltexErpsPendingAction = _EltexErpsPendingAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 1, 5),
    _EltexErpsPendingAction_Type()
)
eltexErpsPendingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsPendingAction.setStatus("current")
_EltexErpsPendingActionVlan_Type = Integer32
_EltexErpsPendingActionVlan_Object = MibScalar
eltexErpsPendingActionVlan = _EltexErpsPendingActionVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 1, 6),
    _EltexErpsPendingActionVlan_Type()
)
eltexErpsPendingActionVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsPendingActionVlan.setStatus("current")


class _EltexErpsGetConfigId_Type(Integer32):
    """Custom type eltexErpsGetConfigId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("pending", 2))
    )


_EltexErpsGetConfigId_Type.__name__ = "Integer32"
_EltexErpsGetConfigId_Object = MibScalar
eltexErpsGetConfigId = _EltexErpsGetConfigId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 1, 7),
    _EltexErpsGetConfigId_Type()
)
eltexErpsGetConfigId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsGetConfigId.setStatus("current")
_EltexErpsInfo_ObjectIdentity = ObjectIdentity
eltexErpsInfo = _EltexErpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 2)
)
_EltexErpsMgmt_ObjectIdentity = ObjectIdentity
eltexErpsMgmt = _EltexErpsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3)
)
_EltexErpsMgmtRAPSVlanTable_Object = MibTable
eltexErpsMgmtRAPSVlanTable = _EltexErpsMgmtRAPSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSVlanTable.setStatus("current")
_EltexErpsMgmtRAPSVlanEntry_Object = MibTableRow
eltexErpsMgmtRAPSVlanEntry = _EltexErpsMgmtRAPSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1)
)
eltexErpsMgmtRAPSVlanEntry.setIndexNames(
    (0, "ELTEX-BRIDGE-ERPS-MIB", "eltexErpsMgmtRAPSVlanId"),
)
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSVlanEntry.setStatus("current")
_EltexErpsMgmtRAPSVlanId_Type = Integer32
_EltexErpsMgmtRAPSVlanId_Object = MibTableColumn
eltexErpsMgmtRAPSVlanId = _EltexErpsMgmtRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 1),
    _EltexErpsMgmtRAPSVlanId_Type()
)
eltexErpsMgmtRAPSVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSVlanId.setStatus("current")


class _EltexErpsMgmtRAPSWestPort_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSWestPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EltexErpsMgmtRAPSWestPort_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSWestPort_Object = MibTableColumn
eltexErpsMgmtRAPSWestPort = _EltexErpsMgmtRAPSWestPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 2),
    _EltexErpsMgmtRAPSWestPort_Type()
)
eltexErpsMgmtRAPSWestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSWestPort.setStatus("current")
_EltexErpsMgmtRAPSWestPortState_Type = EltexErpsMgmtRAPSPortState
_EltexErpsMgmtRAPSWestPortState_Object = MibTableColumn
eltexErpsMgmtRAPSWestPortState = _EltexErpsMgmtRAPSWestPortState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 3),
    _EltexErpsMgmtRAPSWestPortState_Type()
)
eltexErpsMgmtRAPSWestPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSWestPortState.setStatus("current")


class _EltexErpsMgmtRAPSEastPort_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSEastPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EltexErpsMgmtRAPSEastPort_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSEastPort_Object = MibTableColumn
eltexErpsMgmtRAPSEastPort = _EltexErpsMgmtRAPSEastPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 4),
    _EltexErpsMgmtRAPSEastPort_Type()
)
eltexErpsMgmtRAPSEastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSEastPort.setStatus("current")
_EltexErpsMgmtRAPSEastPortState_Type = EltexErpsMgmtRAPSPortState
_EltexErpsMgmtRAPSEastPortState_Object = MibTableColumn
eltexErpsMgmtRAPSEastPortState = _EltexErpsMgmtRAPSEastPortState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 5),
    _EltexErpsMgmtRAPSEastPortState_Type()
)
eltexErpsMgmtRAPSEastPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSEastPortState.setStatus("current")


class _EltexErpsMgmtRAPSRPLPort_Type(EltexErpsMgmtRAPSPortId):
    """Custom type eltexErpsMgmtRAPSRPLPort based on EltexErpsMgmtRAPSPortId"""


_EltexErpsMgmtRAPSRPLPort_Object = MibTableColumn
eltexErpsMgmtRAPSRPLPort = _EltexErpsMgmtRAPSRPLPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 6),
    _EltexErpsMgmtRAPSRPLPort_Type()
)
eltexErpsMgmtRAPSRPLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSRPLPort.setStatus("current")


class _EltexErpsMgmtRAPSRPLOwnerAdminState_Type(EltexErpsEnabledState):
    """Custom type eltexErpsMgmtRAPSRPLOwnerAdminState based on EltexErpsEnabledState"""


_EltexErpsMgmtRAPSRPLOwnerAdminState_Object = MibTableColumn
eltexErpsMgmtRAPSRPLOwnerAdminState = _EltexErpsMgmtRAPSRPLOwnerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 7),
    _EltexErpsMgmtRAPSRPLOwnerAdminState_Type()
)
eltexErpsMgmtRAPSRPLOwnerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSRPLOwnerAdminState.setStatus("current")


class _EltexErpsMgmtRAPSRingMEL_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSRingMEL based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EltexErpsMgmtRAPSRingMEL_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSRingMEL_Object = MibTableColumn
eltexErpsMgmtRAPSRingMEL = _EltexErpsMgmtRAPSRingMEL_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 8),
    _EltexErpsMgmtRAPSRingMEL_Type()
)
eltexErpsMgmtRAPSRingMEL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSRingMEL.setStatus("current")


class _EltexErpsMgmtRAPSHoldOffTime_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSHoldOffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EltexErpsMgmtRAPSHoldOffTime_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSHoldOffTime_Object = MibTableColumn
eltexErpsMgmtRAPSHoldOffTime = _EltexErpsMgmtRAPSHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 9),
    _EltexErpsMgmtRAPSHoldOffTime_Type()
)
eltexErpsMgmtRAPSHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSHoldOffTime.setStatus("current")


class _EltexErpsMgmtRAPSGuardTime_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSGuardTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_EltexErpsMgmtRAPSGuardTime_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSGuardTime_Object = MibTableColumn
eltexErpsMgmtRAPSGuardTime = _EltexErpsMgmtRAPSGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 10),
    _EltexErpsMgmtRAPSGuardTime_Type()
)
eltexErpsMgmtRAPSGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSGuardTime.setStatus("current")


class _EltexErpsMgmtRAPSWTRTime_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSWTRTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EltexErpsMgmtRAPSWTRTime_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSWTRTime_Object = MibTableColumn
eltexErpsMgmtRAPSWTRTime = _EltexErpsMgmtRAPSWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 11),
    _EltexErpsMgmtRAPSWTRTime_Type()
)
eltexErpsMgmtRAPSWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSWTRTime.setStatus("current")


class _EltexErpsMgmtRAPSRingState_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("forced-switch", 5),
          ("idle", 2),
          ("init", 1),
          ("manual-switch", 4),
          ("pending", 6),
          ("protection", 3))
    )


_EltexErpsMgmtRAPSRingState_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSRingState_Object = MibTableColumn
eltexErpsMgmtRAPSRingState = _EltexErpsMgmtRAPSRingState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 12),
    _EltexErpsMgmtRAPSRingState_Type()
)
eltexErpsMgmtRAPSRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSRingState.setStatus("current")


class _EltexErpsMgmtRAPSRingAdminState_Type(EltexErpsEnabledState):
    """Custom type eltexErpsMgmtRAPSRingAdminState based on EltexErpsEnabledState"""


_EltexErpsMgmtRAPSRingAdminState_Object = MibTableColumn
eltexErpsMgmtRAPSRingAdminState = _EltexErpsMgmtRAPSRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 13),
    _EltexErpsMgmtRAPSRingAdminState_Type()
)
eltexErpsMgmtRAPSRingAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSRingAdminState.setStatus("current")


class _EltexErpsMgmtRAPSRPLOwnerOperStatus_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSRPLOwnerOperStatus based on Integer32"""
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


_EltexErpsMgmtRAPSRPLOwnerOperStatus_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSRPLOwnerOperStatus_Object = MibTableColumn
eltexErpsMgmtRAPSRPLOwnerOperStatus = _EltexErpsMgmtRAPSRPLOwnerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 14),
    _EltexErpsMgmtRAPSRPLOwnerOperStatus_Type()
)
eltexErpsMgmtRAPSRPLOwnerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSRPLOwnerOperStatus.setStatus("current")


class _EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Type(OctetString):
    """Custom type eltexErpsMgmtRAPSProtectionVlanRangeList1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Type.__name__ = "OctetString"
_EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Object = MibTableColumn
eltexErpsMgmtRAPSProtectionVlanRangeList1to1024 = _EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 15),
    _EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Type()
)
eltexErpsMgmtRAPSProtectionVlanRangeList1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSProtectionVlanRangeList1to1024.setStatus("current")


class _EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type(OctetString):
    """Custom type eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type.__name__ = "OctetString"
_EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Object = MibTableColumn
eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048 = _EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 16),
    _EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type()
)
eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048.setStatus("current")


class _EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type(OctetString):
    """Custom type eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type.__name__ = "OctetString"
_EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Object = MibTableColumn
eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072 = _EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 17),
    _EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type()
)
eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072.setStatus("current")


class _EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type(OctetString):
    """Custom type eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type.__name__ = "OctetString"
_EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Object = MibTableColumn
eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094 = _EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 18),
    _EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type()
)
eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094.setStatus("current")


class _EltexErpsMgmtRAPSRevertive_Type(TruthValue):
    """Custom type eltexErpsMgmtRAPSRevertive based on TruthValue"""


_EltexErpsMgmtRAPSRevertive_Object = MibTableColumn
eltexErpsMgmtRAPSRevertive = _EltexErpsMgmtRAPSRevertive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 19),
    _EltexErpsMgmtRAPSRevertive_Type()
)
eltexErpsMgmtRAPSRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSRevertive.setStatus("current")


class _EltexErpsMgmtRAPSProtocolVersion_Type(Integer32):
    """Custom type eltexErpsMgmtRAPSProtocolVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_EltexErpsMgmtRAPSProtocolVersion_Type.__name__ = "Integer32"
_EltexErpsMgmtRAPSProtocolVersion_Object = MibTableColumn
eltexErpsMgmtRAPSProtocolVersion = _EltexErpsMgmtRAPSProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 20),
    _EltexErpsMgmtRAPSProtocolVersion_Type()
)
eltexErpsMgmtRAPSProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSProtocolVersion.setStatus("current")


class _EltexErpsMgmtRAPSPortForcedSwitch_Type(EltexErpsMgmtRAPSPortId):
    """Custom type eltexErpsMgmtRAPSPortForcedSwitch based on EltexErpsMgmtRAPSPortId"""


_EltexErpsMgmtRAPSPortForcedSwitch_Object = MibTableColumn
eltexErpsMgmtRAPSPortForcedSwitch = _EltexErpsMgmtRAPSPortForcedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 21),
    _EltexErpsMgmtRAPSPortForcedSwitch_Type()
)
eltexErpsMgmtRAPSPortForcedSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSPortForcedSwitch.setStatus("current")


class _EltexErpsMgmtRAPSPortManualSwitch_Type(EltexErpsMgmtRAPSPortId):
    """Custom type eltexErpsMgmtRAPSPortManualSwitch based on EltexErpsMgmtRAPSPortId"""


_EltexErpsMgmtRAPSPortManualSwitch_Object = MibTableColumn
eltexErpsMgmtRAPSPortManualSwitch = _EltexErpsMgmtRAPSPortManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 22),
    _EltexErpsMgmtRAPSPortManualSwitch_Type()
)
eltexErpsMgmtRAPSPortManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSPortManualSwitch.setStatus("current")
_EltexErpsMgmtRAPSRowStatus_Type = RowStatus
_EltexErpsMgmtRAPSRowStatus_Object = MibTableColumn
eltexErpsMgmtRAPSRowStatus = _EltexErpsMgmtRAPSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 1, 1, 23),
    _EltexErpsMgmtRAPSRowStatus_Type()
)
eltexErpsMgmtRAPSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexErpsMgmtRAPSRowStatus.setStatus("current")
_EltexErpsMgmtSubRingCtrlTable_Object = MibTable
eltexErpsMgmtSubRingCtrlTable = _EltexErpsMgmtSubRingCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltexErpsMgmtSubRingCtrlTable.setStatus("current")
_EltexErpsMgmtSubRingCtrlEntry_Object = MibTableRow
eltexErpsMgmtSubRingCtrlEntry = _EltexErpsMgmtSubRingCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 2, 1)
)
eltexErpsMgmtSubRingCtrlEntry.setIndexNames(
    (0, "ELTEX-BRIDGE-ERPS-MIB", "eltexErpsMgmtSubRingCtrlRAPSVlanId"),
    (0, "ELTEX-BRIDGE-ERPS-MIB", "eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId"),
)
if mibBuilder.loadTexts:
    eltexErpsMgmtSubRingCtrlEntry.setStatus("current")
_EltexErpsMgmtSubRingCtrlRAPSVlanId_Type = Integer32
_EltexErpsMgmtSubRingCtrlRAPSVlanId_Object = MibTableColumn
eltexErpsMgmtSubRingCtrlRAPSVlanId = _EltexErpsMgmtSubRingCtrlRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 2, 1, 1),
    _EltexErpsMgmtSubRingCtrlRAPSVlanId_Type()
)
eltexErpsMgmtSubRingCtrlRAPSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexErpsMgmtSubRingCtrlRAPSVlanId.setStatus("current")
_EltexErpsMgmtSubRingCtrlSubRingRAPSVlanId_Type = Integer32
_EltexErpsMgmtSubRingCtrlSubRingRAPSVlanId_Object = MibTableColumn
eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId = _EltexErpsMgmtSubRingCtrlSubRingRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 2, 1, 2),
    _EltexErpsMgmtSubRingCtrlSubRingRAPSVlanId_Type()
)
eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId.setStatus("current")


class _EltexErpsMgmtSubRingCtrlTCPropagationState_Type(EltexErpsEnabledState):
    """Custom type eltexErpsMgmtSubRingCtrlTCPropagationState based on EltexErpsEnabledState"""


_EltexErpsMgmtSubRingCtrlTCPropagationState_Object = MibTableColumn
eltexErpsMgmtSubRingCtrlTCPropagationState = _EltexErpsMgmtSubRingCtrlTCPropagationState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 2, 1, 3),
    _EltexErpsMgmtSubRingCtrlTCPropagationState_Type()
)
eltexErpsMgmtSubRingCtrlTCPropagationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexErpsMgmtSubRingCtrlTCPropagationState.setStatus("current")
_EltexErpsMgmtSubRingCtrlRowStatus_Type = RowStatus
_EltexErpsMgmtSubRingCtrlRowStatus_Object = MibTableColumn
eltexErpsMgmtSubRingCtrlRowStatus = _EltexErpsMgmtSubRingCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 3, 2, 1, 4),
    _EltexErpsMgmtSubRingCtrlRowStatus_Type()
)
eltexErpsMgmtSubRingCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexErpsMgmtSubRingCtrlRowStatus.setStatus("current")
_EltexErpsNotify_ObjectIdentity = ObjectIdentity
eltexErpsNotify = _EltexErpsNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 4)
)
_EltexErpsNotifyPrefix_ObjectIdentity = ObjectIdentity
eltexErpsNotifyPrefix = _EltexErpsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 4, 0)
)
_EltexErpsNotificationBindings_ObjectIdentity = ObjectIdentity
eltexErpsNotificationBindings = _EltexErpsNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 4, 2)
)
_EltexErpsNodeId_Type = MacAddress
_EltexErpsNodeId_Object = MibScalar
eltexErpsNodeId = _EltexErpsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 4, 2, 1),
    _EltexErpsNodeId_Type()
)
eltexErpsNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eltexErpsNodeId.setStatus("current")

# Managed Objects groups


# Notification objects

eltexErpsSFDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 4, 0, 1)
)
eltexErpsSFDetectedTrap.setObjects(
    ("ELTEX-BRIDGE-ERPS-MIB", "eltexErpsNodeId")
)
if mibBuilder.loadTexts:
    eltexErpsSFDetectedTrap.setStatus(
        "current"
    )

eltexErpsSFClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 4, 0, 2)
)
eltexErpsSFClearedTrap.setObjects(
    ("ELTEX-BRIDGE-ERPS-MIB", "eltexErpsNodeId")
)
if mibBuilder.loadTexts:
    eltexErpsSFClearedTrap.setStatus(
        "current"
    )

eltexErpsRPLOwnerConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 35, 1, 1, 4, 0, 3)
)
eltexErpsRPLOwnerConflictTrap.setObjects(
    ("ELTEX-BRIDGE-ERPS-MIB", "eltexErpsNodeId")
)
if mibBuilder.loadTexts:
    eltexErpsRPLOwnerConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-BRIDGE-ERPS-MIB",
    **{"EltexErpsEnabledState": EltexErpsEnabledState,
       "EltexErpsMgmtRAPSPortState": EltexErpsMgmtRAPSPortState,
       "EltexErpsMgmtRAPSPortId": EltexErpsMgmtRAPSPortId,
       "eltexErpsMIB": eltexErpsMIB,
       "eltexErpsCtrl": eltexErpsCtrl,
       "eltexErpsAdminState": eltexErpsAdminState,
       "eltexErpsLogState": eltexErpsLogState,
       "eltexErpsTrapState": eltexErpsTrapState,
       "eltexErpsPendingAction": eltexErpsPendingAction,
       "eltexErpsPendingActionVlan": eltexErpsPendingActionVlan,
       "eltexErpsGetConfigId": eltexErpsGetConfigId,
       "eltexErpsInfo": eltexErpsInfo,
       "eltexErpsMgmt": eltexErpsMgmt,
       "eltexErpsMgmtRAPSVlanTable": eltexErpsMgmtRAPSVlanTable,
       "eltexErpsMgmtRAPSVlanEntry": eltexErpsMgmtRAPSVlanEntry,
       "eltexErpsMgmtRAPSVlanId": eltexErpsMgmtRAPSVlanId,
       "eltexErpsMgmtRAPSWestPort": eltexErpsMgmtRAPSWestPort,
       "eltexErpsMgmtRAPSWestPortState": eltexErpsMgmtRAPSWestPortState,
       "eltexErpsMgmtRAPSEastPort": eltexErpsMgmtRAPSEastPort,
       "eltexErpsMgmtRAPSEastPortState": eltexErpsMgmtRAPSEastPortState,
       "eltexErpsMgmtRAPSRPLPort": eltexErpsMgmtRAPSRPLPort,
       "eltexErpsMgmtRAPSRPLOwnerAdminState": eltexErpsMgmtRAPSRPLOwnerAdminState,
       "eltexErpsMgmtRAPSRingMEL": eltexErpsMgmtRAPSRingMEL,
       "eltexErpsMgmtRAPSHoldOffTime": eltexErpsMgmtRAPSHoldOffTime,
       "eltexErpsMgmtRAPSGuardTime": eltexErpsMgmtRAPSGuardTime,
       "eltexErpsMgmtRAPSWTRTime": eltexErpsMgmtRAPSWTRTime,
       "eltexErpsMgmtRAPSRingState": eltexErpsMgmtRAPSRingState,
       "eltexErpsMgmtRAPSRingAdminState": eltexErpsMgmtRAPSRingAdminState,
       "eltexErpsMgmtRAPSRPLOwnerOperStatus": eltexErpsMgmtRAPSRPLOwnerOperStatus,
       "eltexErpsMgmtRAPSProtectionVlanRangeList1to1024": eltexErpsMgmtRAPSProtectionVlanRangeList1to1024,
       "eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048": eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048,
       "eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072": eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072,
       "eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094": eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094,
       "eltexErpsMgmtRAPSRevertive": eltexErpsMgmtRAPSRevertive,
       "eltexErpsMgmtRAPSProtocolVersion": eltexErpsMgmtRAPSProtocolVersion,
       "eltexErpsMgmtRAPSPortForcedSwitch": eltexErpsMgmtRAPSPortForcedSwitch,
       "eltexErpsMgmtRAPSPortManualSwitch": eltexErpsMgmtRAPSPortManualSwitch,
       "eltexErpsMgmtRAPSRowStatus": eltexErpsMgmtRAPSRowStatus,
       "eltexErpsMgmtSubRingCtrlTable": eltexErpsMgmtSubRingCtrlTable,
       "eltexErpsMgmtSubRingCtrlEntry": eltexErpsMgmtSubRingCtrlEntry,
       "eltexErpsMgmtSubRingCtrlRAPSVlanId": eltexErpsMgmtSubRingCtrlRAPSVlanId,
       "eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId": eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId,
       "eltexErpsMgmtSubRingCtrlTCPropagationState": eltexErpsMgmtSubRingCtrlTCPropagationState,
       "eltexErpsMgmtSubRingCtrlRowStatus": eltexErpsMgmtSubRingCtrlRowStatus,
       "eltexErpsNotify": eltexErpsNotify,
       "eltexErpsNotifyPrefix": eltexErpsNotifyPrefix,
       "eltexErpsSFDetectedTrap": eltexErpsSFDetectedTrap,
       "eltexErpsSFClearedTrap": eltexErpsSFClearedTrap,
       "eltexErpsRPLOwnerConflictTrap": eltexErpsRPLOwnerConflictTrap,
       "eltexErpsNotificationBindings": eltexErpsNotificationBindings,
       "eltexErpsNodeId": eltexErpsNodeId}
)
