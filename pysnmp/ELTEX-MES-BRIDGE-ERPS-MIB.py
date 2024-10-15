# SNMP MIB module (ELTEX-MES-BRIDGE-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-BRIDGE-ERPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:25 2024
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

(eltMesBridgeExtMIBObjects,) = mibBuilder.importSymbols(
    "ELTEX-MES-BRIDGE-EXT-MIB",
    "eltMesBridgeExtMIBObjects")

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

eltMesErpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1)
)
eltMesErpsMIB.setRevisions(
        ("2015-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltErpsEnabledState(Integer32, TextualConvention):
    status = "deprecated"
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



class EltErpsMgmtRAPSPortState(Integer32, TextualConvention):
    status = "deprecated"
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



class EltErpsMgmtRAPSPortId(Integer32, TextualConvention):
    status = "deprecated"
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

_EltMesErpsCtrl_ObjectIdentity = ObjectIdentity
eltMesErpsCtrl = _EltMesErpsCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1)
)


class _EltErpsAdminState_Type(EltErpsEnabledState):
    """Custom type eltErpsAdminState based on EltErpsEnabledState"""


_EltErpsAdminState_Object = MibScalar
eltErpsAdminState = _EltErpsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 1),
    _EltErpsAdminState_Type()
)
eltErpsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsAdminState.setStatus("deprecated")


class _EltErpsLogState_Type(EltErpsEnabledState):
    """Custom type eltErpsLogState based on EltErpsEnabledState"""


_EltErpsLogState_Object = MibScalar
eltErpsLogState = _EltErpsLogState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 2),
    _EltErpsLogState_Type()
)
eltErpsLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsLogState.setStatus("deprecated")


class _EltErpsTrapState_Type(EltErpsEnabledState):
    """Custom type eltErpsTrapState based on EltErpsEnabledState"""


_EltErpsTrapState_Object = MibScalar
eltErpsTrapState = _EltErpsTrapState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 3),
    _EltErpsTrapState_Type()
)
eltErpsTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsTrapState.setStatus("deprecated")


class _EltErpsPendingAction_Type(Integer32):
    """Custom type eltErpsPendingAction based on Integer32"""
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


_EltErpsPendingAction_Type.__name__ = "Integer32"
_EltErpsPendingAction_Object = MibScalar
eltErpsPendingAction = _EltErpsPendingAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 5),
    _EltErpsPendingAction_Type()
)
eltErpsPendingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsPendingAction.setStatus("deprecated")
_EltErpsPendingActionVlan_Type = Integer32
_EltErpsPendingActionVlan_Object = MibScalar
eltErpsPendingActionVlan = _EltErpsPendingActionVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 6),
    _EltErpsPendingActionVlan_Type()
)
eltErpsPendingActionVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsPendingActionVlan.setStatus("deprecated")


class _EltErpsGetConfigId_Type(Integer32):
    """Custom type eltErpsGetConfigId based on Integer32"""
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


_EltErpsGetConfigId_Type.__name__ = "Integer32"
_EltErpsGetConfigId_Object = MibScalar
eltErpsGetConfigId = _EltErpsGetConfigId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 1, 7),
    _EltErpsGetConfigId_Type()
)
eltErpsGetConfigId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsGetConfigId.setStatus("deprecated")
_EltMesErpsInfo_ObjectIdentity = ObjectIdentity
eltMesErpsInfo = _EltMesErpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 2)
)
_EltMesErpsMgmt_ObjectIdentity = ObjectIdentity
eltMesErpsMgmt = _EltMesErpsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3)
)
_EltErpsMgmtRAPSVlanTable_Object = MibTable
eltErpsMgmtRAPSVlanTable = _EltErpsMgmtRAPSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSVlanTable.setStatus("deprecated")
_EltErpsMgmtRAPSVlanEntry_Object = MibTableRow
eltErpsMgmtRAPSVlanEntry = _EltErpsMgmtRAPSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1)
)
eltErpsMgmtRAPSVlanEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsMgmtRAPSVlanId"),
)
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSVlanEntry.setStatus("deprecated")
_EltErpsMgmtRAPSVlanId_Type = Integer32
_EltErpsMgmtRAPSVlanId_Object = MibTableColumn
eltErpsMgmtRAPSVlanId = _EltErpsMgmtRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 1),
    _EltErpsMgmtRAPSVlanId_Type()
)
eltErpsMgmtRAPSVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSVlanId.setStatus("deprecated")


class _EltErpsMgmtRAPSWestPort_Type(Integer32):
    """Custom type eltErpsMgmtRAPSWestPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EltErpsMgmtRAPSWestPort_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSWestPort_Object = MibTableColumn
eltErpsMgmtRAPSWestPort = _EltErpsMgmtRAPSWestPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 2),
    _EltErpsMgmtRAPSWestPort_Type()
)
eltErpsMgmtRAPSWestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSWestPort.setStatus("deprecated")
_EltErpsMgmtRAPSWestPortState_Type = EltErpsMgmtRAPSPortState
_EltErpsMgmtRAPSWestPortState_Object = MibTableColumn
eltErpsMgmtRAPSWestPortState = _EltErpsMgmtRAPSWestPortState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 3),
    _EltErpsMgmtRAPSWestPortState_Type()
)
eltErpsMgmtRAPSWestPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSWestPortState.setStatus("deprecated")


class _EltErpsMgmtRAPSEastPort_Type(Integer32):
    """Custom type eltErpsMgmtRAPSEastPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EltErpsMgmtRAPSEastPort_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSEastPort_Object = MibTableColumn
eltErpsMgmtRAPSEastPort = _EltErpsMgmtRAPSEastPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 4),
    _EltErpsMgmtRAPSEastPort_Type()
)
eltErpsMgmtRAPSEastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSEastPort.setStatus("deprecated")
_EltErpsMgmtRAPSEastPortState_Type = EltErpsMgmtRAPSPortState
_EltErpsMgmtRAPSEastPortState_Object = MibTableColumn
eltErpsMgmtRAPSEastPortState = _EltErpsMgmtRAPSEastPortState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 5),
    _EltErpsMgmtRAPSEastPortState_Type()
)
eltErpsMgmtRAPSEastPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSEastPortState.setStatus("deprecated")


class _EltErpsMgmtRAPSRPLPort_Type(EltErpsMgmtRAPSPortId):
    """Custom type eltErpsMgmtRAPSRPLPort based on EltErpsMgmtRAPSPortId"""


_EltErpsMgmtRAPSRPLPort_Object = MibTableColumn
eltErpsMgmtRAPSRPLPort = _EltErpsMgmtRAPSRPLPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 6),
    _EltErpsMgmtRAPSRPLPort_Type()
)
eltErpsMgmtRAPSRPLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSRPLPort.setStatus("deprecated")


class _EltErpsMgmtRAPSRPLOwnerAdminState_Type(EltErpsEnabledState):
    """Custom type eltErpsMgmtRAPSRPLOwnerAdminState based on EltErpsEnabledState"""


_EltErpsMgmtRAPSRPLOwnerAdminState_Object = MibTableColumn
eltErpsMgmtRAPSRPLOwnerAdminState = _EltErpsMgmtRAPSRPLOwnerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 7),
    _EltErpsMgmtRAPSRPLOwnerAdminState_Type()
)
eltErpsMgmtRAPSRPLOwnerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSRPLOwnerAdminState.setStatus("deprecated")


class _EltErpsMgmtRAPSRingMEL_Type(Integer32):
    """Custom type eltErpsMgmtRAPSRingMEL based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EltErpsMgmtRAPSRingMEL_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSRingMEL_Object = MibTableColumn
eltErpsMgmtRAPSRingMEL = _EltErpsMgmtRAPSRingMEL_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 8),
    _EltErpsMgmtRAPSRingMEL_Type()
)
eltErpsMgmtRAPSRingMEL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSRingMEL.setStatus("deprecated")


class _EltErpsMgmtRAPSHoldOffTime_Type(Integer32):
    """Custom type eltErpsMgmtRAPSHoldOffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EltErpsMgmtRAPSHoldOffTime_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSHoldOffTime_Object = MibTableColumn
eltErpsMgmtRAPSHoldOffTime = _EltErpsMgmtRAPSHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 9),
    _EltErpsMgmtRAPSHoldOffTime_Type()
)
eltErpsMgmtRAPSHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSHoldOffTime.setStatus("deprecated")


class _EltErpsMgmtRAPSGuardTime_Type(Integer32):
    """Custom type eltErpsMgmtRAPSGuardTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_EltErpsMgmtRAPSGuardTime_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSGuardTime_Object = MibTableColumn
eltErpsMgmtRAPSGuardTime = _EltErpsMgmtRAPSGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 10),
    _EltErpsMgmtRAPSGuardTime_Type()
)
eltErpsMgmtRAPSGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSGuardTime.setStatus("deprecated")


class _EltErpsMgmtRAPSWTRTime_Type(Integer32):
    """Custom type eltErpsMgmtRAPSWTRTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EltErpsMgmtRAPSWTRTime_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSWTRTime_Object = MibTableColumn
eltErpsMgmtRAPSWTRTime = _EltErpsMgmtRAPSWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 11),
    _EltErpsMgmtRAPSWTRTime_Type()
)
eltErpsMgmtRAPSWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSWTRTime.setStatus("deprecated")


class _EltErpsMgmtRAPSRingState_Type(Integer32):
    """Custom type eltErpsMgmtRAPSRingState based on Integer32"""
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


_EltErpsMgmtRAPSRingState_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSRingState_Object = MibTableColumn
eltErpsMgmtRAPSRingState = _EltErpsMgmtRAPSRingState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 12),
    _EltErpsMgmtRAPSRingState_Type()
)
eltErpsMgmtRAPSRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSRingState.setStatus("deprecated")


class _EltErpsMgmtRAPSRingAdminState_Type(EltErpsEnabledState):
    """Custom type eltErpsMgmtRAPSRingAdminState based on EltErpsEnabledState"""


_EltErpsMgmtRAPSRingAdminState_Object = MibTableColumn
eltErpsMgmtRAPSRingAdminState = _EltErpsMgmtRAPSRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 13),
    _EltErpsMgmtRAPSRingAdminState_Type()
)
eltErpsMgmtRAPSRingAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSRingAdminState.setStatus("deprecated")


class _EltErpsMgmtRAPSRPLOwnerOperStatus_Type(Integer32):
    """Custom type eltErpsMgmtRAPSRPLOwnerOperStatus based on Integer32"""
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


_EltErpsMgmtRAPSRPLOwnerOperStatus_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSRPLOwnerOperStatus_Object = MibTableColumn
eltErpsMgmtRAPSRPLOwnerOperStatus = _EltErpsMgmtRAPSRPLOwnerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 14),
    _EltErpsMgmtRAPSRPLOwnerOperStatus_Type()
)
eltErpsMgmtRAPSRPLOwnerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSRPLOwnerOperStatus.setStatus("deprecated")


class _EltErpsMgmtRAPSProtectionVlanRangeList1to1024_Type(OctetString):
    """Custom type eltErpsMgmtRAPSProtectionVlanRangeList1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltErpsMgmtRAPSProtectionVlanRangeList1to1024_Type.__name__ = "OctetString"
_EltErpsMgmtRAPSProtectionVlanRangeList1to1024_Object = MibTableColumn
eltErpsMgmtRAPSProtectionVlanRangeList1to1024 = _EltErpsMgmtRAPSProtectionVlanRangeList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 15),
    _EltErpsMgmtRAPSProtectionVlanRangeList1to1024_Type()
)
eltErpsMgmtRAPSProtectionVlanRangeList1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSProtectionVlanRangeList1to1024.setStatus("deprecated")


class _EltErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type(OctetString):
    """Custom type eltErpsMgmtRAPSProtectionVlanRangeList1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type.__name__ = "OctetString"
_EltErpsMgmtRAPSProtectionVlanRangeList1025to2048_Object = MibTableColumn
eltErpsMgmtRAPSProtectionVlanRangeList1025to2048 = _EltErpsMgmtRAPSProtectionVlanRangeList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 16),
    _EltErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type()
)
eltErpsMgmtRAPSProtectionVlanRangeList1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSProtectionVlanRangeList1025to2048.setStatus("deprecated")


class _EltErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type(OctetString):
    """Custom type eltErpsMgmtRAPSProtectionVlanRangeList2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type.__name__ = "OctetString"
_EltErpsMgmtRAPSProtectionVlanRangeList2049to3072_Object = MibTableColumn
eltErpsMgmtRAPSProtectionVlanRangeList2049to3072 = _EltErpsMgmtRAPSProtectionVlanRangeList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 17),
    _EltErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type()
)
eltErpsMgmtRAPSProtectionVlanRangeList2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSProtectionVlanRangeList2049to3072.setStatus("deprecated")


class _EltErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type(OctetString):
    """Custom type eltErpsMgmtRAPSProtectionVlanRangeList3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type.__name__ = "OctetString"
_EltErpsMgmtRAPSProtectionVlanRangeList3073to4094_Object = MibTableColumn
eltErpsMgmtRAPSProtectionVlanRangeList3073to4094 = _EltErpsMgmtRAPSProtectionVlanRangeList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 18),
    _EltErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type()
)
eltErpsMgmtRAPSProtectionVlanRangeList3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSProtectionVlanRangeList3073to4094.setStatus("deprecated")


class _EltErpsMgmtRAPSRevertive_Type(TruthValue):
    """Custom type eltErpsMgmtRAPSRevertive based on TruthValue"""


_EltErpsMgmtRAPSRevertive_Object = MibTableColumn
eltErpsMgmtRAPSRevertive = _EltErpsMgmtRAPSRevertive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 19),
    _EltErpsMgmtRAPSRevertive_Type()
)
eltErpsMgmtRAPSRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSRevertive.setStatus("deprecated")


class _EltErpsMgmtRAPSProtocolVersion_Type(Integer32):
    """Custom type eltErpsMgmtRAPSProtocolVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_EltErpsMgmtRAPSProtocolVersion_Type.__name__ = "Integer32"
_EltErpsMgmtRAPSProtocolVersion_Object = MibTableColumn
eltErpsMgmtRAPSProtocolVersion = _EltErpsMgmtRAPSProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 20),
    _EltErpsMgmtRAPSProtocolVersion_Type()
)
eltErpsMgmtRAPSProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSProtocolVersion.setStatus("deprecated")


class _EltErpsMgmtRAPSPortForcedSwitch_Type(EltErpsMgmtRAPSPortId):
    """Custom type eltErpsMgmtRAPSPortForcedSwitch based on EltErpsMgmtRAPSPortId"""


_EltErpsMgmtRAPSPortForcedSwitch_Object = MibTableColumn
eltErpsMgmtRAPSPortForcedSwitch = _EltErpsMgmtRAPSPortForcedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 21),
    _EltErpsMgmtRAPSPortForcedSwitch_Type()
)
eltErpsMgmtRAPSPortForcedSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSPortForcedSwitch.setStatus("deprecated")


class _EltErpsMgmtRAPSPortManualSwitch_Type(EltErpsMgmtRAPSPortId):
    """Custom type eltErpsMgmtRAPSPortManualSwitch based on EltErpsMgmtRAPSPortId"""


_EltErpsMgmtRAPSPortManualSwitch_Object = MibTableColumn
eltErpsMgmtRAPSPortManualSwitch = _EltErpsMgmtRAPSPortManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 22),
    _EltErpsMgmtRAPSPortManualSwitch_Type()
)
eltErpsMgmtRAPSPortManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSPortManualSwitch.setStatus("deprecated")
_EltErpsMgmtRAPSRowStatus_Type = RowStatus
_EltErpsMgmtRAPSRowStatus_Object = MibTableColumn
eltErpsMgmtRAPSRowStatus = _EltErpsMgmtRAPSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 1, 1, 23),
    _EltErpsMgmtRAPSRowStatus_Type()
)
eltErpsMgmtRAPSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltErpsMgmtRAPSRowStatus.setStatus("deprecated")
_EltErpsMgmtSubRingCtrlTable_Object = MibTable
eltErpsMgmtSubRingCtrlTable = _EltErpsMgmtSubRingCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltErpsMgmtSubRingCtrlTable.setStatus("deprecated")
_EltErpsMgmtSubRingCtrlEntry_Object = MibTableRow
eltErpsMgmtSubRingCtrlEntry = _EltErpsMgmtSubRingCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1)
)
eltErpsMgmtSubRingCtrlEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsMgmtSubRingCtrlRAPSVlanId"),
    (0, "ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsMgmtSubRingCtrlSubRingRAPSVlanId"),
)
if mibBuilder.loadTexts:
    eltErpsMgmtSubRingCtrlEntry.setStatus("deprecated")
_EltErpsMgmtSubRingCtrlRAPSVlanId_Type = Integer32
_EltErpsMgmtSubRingCtrlRAPSVlanId_Object = MibTableColumn
eltErpsMgmtSubRingCtrlRAPSVlanId = _EltErpsMgmtSubRingCtrlRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1, 1),
    _EltErpsMgmtSubRingCtrlRAPSVlanId_Type()
)
eltErpsMgmtSubRingCtrlRAPSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltErpsMgmtSubRingCtrlRAPSVlanId.setStatus("deprecated")
_EltErpsMgmtSubRingCtrlSubRingRAPSVlanId_Type = Integer32
_EltErpsMgmtSubRingCtrlSubRingRAPSVlanId_Object = MibTableColumn
eltErpsMgmtSubRingCtrlSubRingRAPSVlanId = _EltErpsMgmtSubRingCtrlSubRingRAPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1, 2),
    _EltErpsMgmtSubRingCtrlSubRingRAPSVlanId_Type()
)
eltErpsMgmtSubRingCtrlSubRingRAPSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltErpsMgmtSubRingCtrlSubRingRAPSVlanId.setStatus("deprecated")


class _EltErpsMgmtSubRingCtrlTCPropagationState_Type(EltErpsEnabledState):
    """Custom type eltErpsMgmtSubRingCtrlTCPropagationState based on EltErpsEnabledState"""


_EltErpsMgmtSubRingCtrlTCPropagationState_Object = MibTableColumn
eltErpsMgmtSubRingCtrlTCPropagationState = _EltErpsMgmtSubRingCtrlTCPropagationState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1, 3),
    _EltErpsMgmtSubRingCtrlTCPropagationState_Type()
)
eltErpsMgmtSubRingCtrlTCPropagationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltErpsMgmtSubRingCtrlTCPropagationState.setStatus("deprecated")
_EltErpsMgmtSubRingCtrlRowStatus_Type = RowStatus
_EltErpsMgmtSubRingCtrlRowStatus_Object = MibTableColumn
eltErpsMgmtSubRingCtrlRowStatus = _EltErpsMgmtSubRingCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 3, 2, 1, 4),
    _EltErpsMgmtSubRingCtrlRowStatus_Type()
)
eltErpsMgmtSubRingCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltErpsMgmtSubRingCtrlRowStatus.setStatus("deprecated")
_EltMesErpsNotify_ObjectIdentity = ObjectIdentity
eltMesErpsNotify = _EltMesErpsNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4)
)
_EltMesErpsNotifyPrefix_ObjectIdentity = ObjectIdentity
eltMesErpsNotifyPrefix = _EltMesErpsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 0)
)
_EltMesErpsNotificationBindings_ObjectIdentity = ObjectIdentity
eltMesErpsNotificationBindings = _EltMesErpsNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 2)
)
_EltErpsNodeId_Type = MacAddress
_EltErpsNodeId_Object = MibScalar
eltErpsNodeId = _EltErpsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 2, 1),
    _EltErpsNodeId_Type()
)
eltErpsNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eltErpsNodeId.setStatus("deprecated")

# Managed Objects groups


# Notification objects

eltErpsSFDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 0, 1)
)
eltErpsSFDetectedTrap.setObjects(
    ("ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsNodeId")
)
if mibBuilder.loadTexts:
    eltErpsSFDetectedTrap.setStatus(
        "deprecated"
    )

eltErpsSFClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 0, 2)
)
eltErpsSFClearedTrap.setObjects(
    ("ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsNodeId")
)
if mibBuilder.loadTexts:
    eltErpsSFClearedTrap.setStatus(
        "deprecated"
    )

eltErpsRPLOwnerConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 1, 4, 0, 3)
)
eltErpsRPLOwnerConflictTrap.setObjects(
    ("ELTEX-MES-BRIDGE-ERPS-MIB", "eltErpsNodeId")
)
if mibBuilder.loadTexts:
    eltErpsRPLOwnerConflictTrap.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-BRIDGE-ERPS-MIB",
    **{"EltErpsEnabledState": EltErpsEnabledState,
       "EltErpsMgmtRAPSPortState": EltErpsMgmtRAPSPortState,
       "EltErpsMgmtRAPSPortId": EltErpsMgmtRAPSPortId,
       "eltMesErpsMIB": eltMesErpsMIB,
       "eltMesErpsCtrl": eltMesErpsCtrl,
       "eltErpsAdminState": eltErpsAdminState,
       "eltErpsLogState": eltErpsLogState,
       "eltErpsTrapState": eltErpsTrapState,
       "eltErpsPendingAction": eltErpsPendingAction,
       "eltErpsPendingActionVlan": eltErpsPendingActionVlan,
       "eltErpsGetConfigId": eltErpsGetConfigId,
       "eltMesErpsInfo": eltMesErpsInfo,
       "eltMesErpsMgmt": eltMesErpsMgmt,
       "eltErpsMgmtRAPSVlanTable": eltErpsMgmtRAPSVlanTable,
       "eltErpsMgmtRAPSVlanEntry": eltErpsMgmtRAPSVlanEntry,
       "eltErpsMgmtRAPSVlanId": eltErpsMgmtRAPSVlanId,
       "eltErpsMgmtRAPSWestPort": eltErpsMgmtRAPSWestPort,
       "eltErpsMgmtRAPSWestPortState": eltErpsMgmtRAPSWestPortState,
       "eltErpsMgmtRAPSEastPort": eltErpsMgmtRAPSEastPort,
       "eltErpsMgmtRAPSEastPortState": eltErpsMgmtRAPSEastPortState,
       "eltErpsMgmtRAPSRPLPort": eltErpsMgmtRAPSRPLPort,
       "eltErpsMgmtRAPSRPLOwnerAdminState": eltErpsMgmtRAPSRPLOwnerAdminState,
       "eltErpsMgmtRAPSRingMEL": eltErpsMgmtRAPSRingMEL,
       "eltErpsMgmtRAPSHoldOffTime": eltErpsMgmtRAPSHoldOffTime,
       "eltErpsMgmtRAPSGuardTime": eltErpsMgmtRAPSGuardTime,
       "eltErpsMgmtRAPSWTRTime": eltErpsMgmtRAPSWTRTime,
       "eltErpsMgmtRAPSRingState": eltErpsMgmtRAPSRingState,
       "eltErpsMgmtRAPSRingAdminState": eltErpsMgmtRAPSRingAdminState,
       "eltErpsMgmtRAPSRPLOwnerOperStatus": eltErpsMgmtRAPSRPLOwnerOperStatus,
       "eltErpsMgmtRAPSProtectionVlanRangeList1to1024": eltErpsMgmtRAPSProtectionVlanRangeList1to1024,
       "eltErpsMgmtRAPSProtectionVlanRangeList1025to2048": eltErpsMgmtRAPSProtectionVlanRangeList1025to2048,
       "eltErpsMgmtRAPSProtectionVlanRangeList2049to3072": eltErpsMgmtRAPSProtectionVlanRangeList2049to3072,
       "eltErpsMgmtRAPSProtectionVlanRangeList3073to4094": eltErpsMgmtRAPSProtectionVlanRangeList3073to4094,
       "eltErpsMgmtRAPSRevertive": eltErpsMgmtRAPSRevertive,
       "eltErpsMgmtRAPSProtocolVersion": eltErpsMgmtRAPSProtocolVersion,
       "eltErpsMgmtRAPSPortForcedSwitch": eltErpsMgmtRAPSPortForcedSwitch,
       "eltErpsMgmtRAPSPortManualSwitch": eltErpsMgmtRAPSPortManualSwitch,
       "eltErpsMgmtRAPSRowStatus": eltErpsMgmtRAPSRowStatus,
       "eltErpsMgmtSubRingCtrlTable": eltErpsMgmtSubRingCtrlTable,
       "eltErpsMgmtSubRingCtrlEntry": eltErpsMgmtSubRingCtrlEntry,
       "eltErpsMgmtSubRingCtrlRAPSVlanId": eltErpsMgmtSubRingCtrlRAPSVlanId,
       "eltErpsMgmtSubRingCtrlSubRingRAPSVlanId": eltErpsMgmtSubRingCtrlSubRingRAPSVlanId,
       "eltErpsMgmtSubRingCtrlTCPropagationState": eltErpsMgmtSubRingCtrlTCPropagationState,
       "eltErpsMgmtSubRingCtrlRowStatus": eltErpsMgmtSubRingCtrlRowStatus,
       "eltMesErpsNotify": eltMesErpsNotify,
       "eltMesErpsNotifyPrefix": eltMesErpsNotifyPrefix,
       "eltErpsSFDetectedTrap": eltErpsSFDetectedTrap,
       "eltErpsSFClearedTrap": eltErpsSFClearedTrap,
       "eltErpsRPLOwnerConflictTrap": eltErpsRPLOwnerConflictTrap,
       "eltMesErpsNotificationBindings": eltMesErpsNotificationBindings,
       "eltErpsNodeId": eltErpsNodeId}
)
