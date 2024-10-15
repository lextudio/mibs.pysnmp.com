# SNMP MIB module (ALCATEL-IND1-STACK-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-STACK-MANAGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:07 2024
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

(softentIND1StackMgr,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1StackMgr")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1StackMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1)
)
alcatelIND1StackMgrMIB.setRevisions(
        ("2009-02-06 00:00",
         "2007-04-03 00:00",
         "2005-07-15 00:00",
         "2004-07-01 00:00",
         "2004-04-23 00:00",
         "2004-04-08 00:00",
         "2004-04-04 00:00",
         "2004-03-22 00:00",
         "2004-03-08 00:00",
         "2001-08-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaStackMgrLinkNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              51,
              52)
        )
    )
    namedValues = NamedValues(
        *(("linkA", 1),
          ("linkA25", 25),
          ("linkA27", 27),
          ("linkA29", 29),
          ("linkA31", 31),
          ("linkA51", 51),
          ("linkB", 2),
          ("linkB26", 26),
          ("linkB28", 28),
          ("linkB30", 30),
          ("linkB32", 32),
          ("linkB52", 52))
    )



class AlaStackMgrNINumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1008),
    )



class AlaStackMgrLinkStatus(Integer32, TextualConvention):
    status = "current"
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



class AlaStackMgrSlotRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 3),
          ("passthrough", 5),
          ("primary", 1),
          ("secondary", 2),
          ("standalone", 4),
          ("unassigned", 0))
    )



class AlaStackMgrStackStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("noloop", 2))
    )



class AlaStackMgrSlotState(Integer32, TextualConvention):
    status = "current"
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
        *(("badMix", 6),
          ("clearedSlot", 3),
          ("duplicateSlot", 2),
          ("outOfSlots", 4),
          ("outOfTokens", 5),
          ("running", 1))
    )



class AlaStackMgrCommandAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clearSlot", 1),
          ("clearSlotImmediately", 2),
          ("notSignificant", 0),
          ("reloadAny", 3),
          ("reloadPassThru", 4))
    )



class AlaStackMgrCommandStatus(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("clearSlotFailed", 2),
          ("clearSlotInProgress", 1),
          ("clearSlotSuccess", 3),
          ("notSignificant", 0),
          ("setSlotFailed", 5),
          ("setSlotInProgress", 4),
          ("setSlotSuccess", 6))
    )



class AlaStackMgrStackingMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stackable", 1),
          ("standalone", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1StackMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1StackMgrMIBObjects = _AlcatelIND1StackMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1)
)
_AlaStackMgrChassisTable_Object = MibTable
alaStackMgrChassisTable = _AlaStackMgrChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaStackMgrChassisTable.setStatus("current")
_AlaStackMgrChassisEntry_Object = MibTableRow
alaStackMgrChassisEntry = _AlaStackMgrChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1)
)
alaStackMgrChassisEntry.setIndexNames(
    (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"),
)
if mibBuilder.loadTexts:
    alaStackMgrChassisEntry.setStatus("current")
_AlaStackMgrSlotNINumber_Type = AlaStackMgrNINumber
_AlaStackMgrSlotNINumber_Object = MibTableColumn
alaStackMgrSlotNINumber = _AlaStackMgrSlotNINumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 1),
    _AlaStackMgrSlotNINumber_Type()
)
alaStackMgrSlotNINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrSlotNINumber.setStatus("current")


class _AlaStackMgrSlotCMMNumber_Type(Integer32):
    """Custom type alaStackMgrSlotCMMNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 72),
    )


_AlaStackMgrSlotCMMNumber_Type.__name__ = "Integer32"
_AlaStackMgrSlotCMMNumber_Object = MibTableColumn
alaStackMgrSlotCMMNumber = _AlaStackMgrSlotCMMNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 2),
    _AlaStackMgrSlotCMMNumber_Type()
)
alaStackMgrSlotCMMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrSlotCMMNumber.setStatus("current")
_AlaStackMgrChasRole_Type = AlaStackMgrSlotRole
_AlaStackMgrChasRole_Object = MibTableColumn
alaStackMgrChasRole = _AlaStackMgrChasRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 3),
    _AlaStackMgrChasRole_Type()
)
alaStackMgrChasRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrChasRole.setStatus("current")
_AlaStackMgrLocalLinkStateA_Type = AlaStackMgrLinkStatus
_AlaStackMgrLocalLinkStateA_Object = MibTableColumn
alaStackMgrLocalLinkStateA = _AlaStackMgrLocalLinkStateA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 4),
    _AlaStackMgrLocalLinkStateA_Type()
)
alaStackMgrLocalLinkStateA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrLocalLinkStateA.setStatus("current")
_AlaStackMgrRemoteNISlotA_Type = AlaStackMgrNINumber
_AlaStackMgrRemoteNISlotA_Object = MibTableColumn
alaStackMgrRemoteNISlotA = _AlaStackMgrRemoteNISlotA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 5),
    _AlaStackMgrRemoteNISlotA_Type()
)
alaStackMgrRemoteNISlotA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrRemoteNISlotA.setStatus("current")
_AlaStackMgrRemoteLinkA_Type = AlaStackMgrLinkNumber
_AlaStackMgrRemoteLinkA_Object = MibTableColumn
alaStackMgrRemoteLinkA = _AlaStackMgrRemoteLinkA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 6),
    _AlaStackMgrRemoteLinkA_Type()
)
alaStackMgrRemoteLinkA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrRemoteLinkA.setStatus("current")
_AlaStackMgrLocalLinkStateB_Type = AlaStackMgrLinkStatus
_AlaStackMgrLocalLinkStateB_Object = MibTableColumn
alaStackMgrLocalLinkStateB = _AlaStackMgrLocalLinkStateB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 7),
    _AlaStackMgrLocalLinkStateB_Type()
)
alaStackMgrLocalLinkStateB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrLocalLinkStateB.setStatus("current")
_AlaStackMgrRemoteNISlotB_Type = AlaStackMgrNINumber
_AlaStackMgrRemoteNISlotB_Object = MibTableColumn
alaStackMgrRemoteNISlotB = _AlaStackMgrRemoteNISlotB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 8),
    _AlaStackMgrRemoteNISlotB_Type()
)
alaStackMgrRemoteNISlotB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrRemoteNISlotB.setStatus("current")
_AlaStackMgrRemoteLinkB_Type = AlaStackMgrLinkNumber
_AlaStackMgrRemoteLinkB_Object = MibTableColumn
alaStackMgrRemoteLinkB = _AlaStackMgrRemoteLinkB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 9),
    _AlaStackMgrRemoteLinkB_Type()
)
alaStackMgrRemoteLinkB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrRemoteLinkB.setStatus("current")
_AlaStackMgrChasState_Type = AlaStackMgrSlotState
_AlaStackMgrChasState_Object = MibTableColumn
alaStackMgrChasState = _AlaStackMgrChasState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 10),
    _AlaStackMgrChasState_Type()
)
alaStackMgrChasState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrChasState.setStatus("current")
_AlaStackMgrSavedSlotNINumber_Type = AlaStackMgrNINumber
_AlaStackMgrSavedSlotNINumber_Object = MibTableColumn
alaStackMgrSavedSlotNINumber = _AlaStackMgrSavedSlotNINumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 11),
    _AlaStackMgrSavedSlotNINumber_Type()
)
alaStackMgrSavedSlotNINumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaStackMgrSavedSlotNINumber.setStatus("current")
_AlaStackMgrCommandAction_Type = AlaStackMgrCommandAction
_AlaStackMgrCommandAction_Object = MibTableColumn
alaStackMgrCommandAction = _AlaStackMgrCommandAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 12),
    _AlaStackMgrCommandAction_Type()
)
alaStackMgrCommandAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaStackMgrCommandAction.setStatus("current")
_AlaStackMgrCommandStatus_Type = AlaStackMgrCommandStatus
_AlaStackMgrCommandStatus_Object = MibTableColumn
alaStackMgrCommandStatus = _AlaStackMgrCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 13),
    _AlaStackMgrCommandStatus_Type()
)
alaStackMgrCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrCommandStatus.setStatus("current")
_AlaStackMgrOperStackingMode_Type = AlaStackMgrStackingMode
_AlaStackMgrOperStackingMode_Object = MibTableColumn
alaStackMgrOperStackingMode = _AlaStackMgrOperStackingMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 14),
    _AlaStackMgrOperStackingMode_Type()
)
alaStackMgrOperStackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrOperStackingMode.setStatus("current")
_AlaStackMgrAdminStackingMode_Type = AlaStackMgrStackingMode
_AlaStackMgrAdminStackingMode_Object = MibTableColumn
alaStackMgrAdminStackingMode = _AlaStackMgrAdminStackingMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 15),
    _AlaStackMgrAdminStackingMode_Type()
)
alaStackMgrAdminStackingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaStackMgrAdminStackingMode.setStatus("current")
_AlaStackMgrStatsTable_Object = MibTable
alaStackMgrStatsTable = _AlaStackMgrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaStackMgrStatsTable.setStatus("current")
_AlaStackMgrStatsEntry_Object = MibTableRow
alaStackMgrStatsEntry = _AlaStackMgrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1)
)
alaStackMgrStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"),
    (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatLinkNumber"),
)
if mibBuilder.loadTexts:
    alaStackMgrStatsEntry.setStatus("current")
_AlaStackMgrStatLinkNumber_Type = AlaStackMgrLinkNumber
_AlaStackMgrStatLinkNumber_Object = MibTableColumn
alaStackMgrStatLinkNumber = _AlaStackMgrStatLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 1),
    _AlaStackMgrStatLinkNumber_Type()
)
alaStackMgrStatLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrStatLinkNumber.setStatus("current")
_AlaStackMgrStatPktsRx_Type = Counter32
_AlaStackMgrStatPktsRx_Object = MibTableColumn
alaStackMgrStatPktsRx = _AlaStackMgrStatPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 2),
    _AlaStackMgrStatPktsRx_Type()
)
alaStackMgrStatPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrStatPktsRx.setStatus("current")
_AlaStackMgrStatPktsTx_Type = Counter32
_AlaStackMgrStatPktsTx_Object = MibTableColumn
alaStackMgrStatPktsTx = _AlaStackMgrStatPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 3),
    _AlaStackMgrStatPktsTx_Type()
)
alaStackMgrStatPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrStatPktsTx.setStatus("current")
_AlaStackMgrStatErrorsRx_Type = Counter32
_AlaStackMgrStatErrorsRx_Object = MibTableColumn
alaStackMgrStatErrorsRx = _AlaStackMgrStatErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 4),
    _AlaStackMgrStatErrorsRx_Type()
)
alaStackMgrStatErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrStatErrorsRx.setStatus("current")
_AlaStackMgrStatErrorsTx_Type = Counter32
_AlaStackMgrStatErrorsTx_Object = MibTableColumn
alaStackMgrStatErrorsTx = _AlaStackMgrStatErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 5),
    _AlaStackMgrStatErrorsTx_Type()
)
alaStackMgrStatErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrStatErrorsTx.setStatus("current")


class _AlaStackMgrStatDelayFromLastMsg_Type(Integer32):
    """Custom type alaStackMgrStatDelayFromLastMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaStackMgrStatDelayFromLastMsg_Type.__name__ = "Integer32"
_AlaStackMgrStatDelayFromLastMsg_Object = MibTableColumn
alaStackMgrStatDelayFromLastMsg = _AlaStackMgrStatDelayFromLastMsg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 6),
    _AlaStackMgrStatDelayFromLastMsg_Type()
)
alaStackMgrStatDelayFromLastMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrStatDelayFromLastMsg.setStatus("current")
_AlaStackMgrStackStatus_Type = AlaStackMgrStackStatus
_AlaStackMgrStackStatus_Object = MibScalar
alaStackMgrStackStatus = _AlaStackMgrStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 3),
    _AlaStackMgrStackStatus_Type()
)
alaStackMgrStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrStackStatus.setStatus("current")


class _AlaStackMgrTokensUsed_Type(Integer32):
    """Custom type alaStackMgrTokensUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaStackMgrTokensUsed_Type.__name__ = "Integer32"
_AlaStackMgrTokensUsed_Object = MibScalar
alaStackMgrTokensUsed = _AlaStackMgrTokensUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 4),
    _AlaStackMgrTokensUsed_Type()
)
alaStackMgrTokensUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrTokensUsed.setStatus("current")


class _AlaStackMgrTokensAvailable_Type(Integer32):
    """Custom type alaStackMgrTokensAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaStackMgrTokensAvailable_Type.__name__ = "Integer32"
_AlaStackMgrTokensAvailable_Object = MibScalar
alaStackMgrTokensAvailable = _AlaStackMgrTokensAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 5),
    _AlaStackMgrTokensAvailable_Type()
)
alaStackMgrTokensAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrTokensAvailable.setStatus("current")
_AlaStackMgrStaticRouteTable_Object = MibTable
alaStackMgrStaticRouteTable = _AlaStackMgrStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaStackMgrStaticRouteTable.setStatus("current")
_AlaStackMgrStaticRouteEntry_Object = MibTableRow
alaStackMgrStaticRouteEntry = _AlaStackMgrStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1)
)
alaStackMgrStaticRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteSrcStartIf"),
    (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteSrcEndIf"),
    (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteDstStartIf"),
    (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteDstEndIf"),
)
if mibBuilder.loadTexts:
    alaStackMgrStaticRouteEntry.setStatus("current")
_AlaStackMgrStaticRouteSrcStartIf_Type = InterfaceIndex
_AlaStackMgrStaticRouteSrcStartIf_Object = MibTableColumn
alaStackMgrStaticRouteSrcStartIf = _AlaStackMgrStaticRouteSrcStartIf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 1),
    _AlaStackMgrStaticRouteSrcStartIf_Type()
)
alaStackMgrStaticRouteSrcStartIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaStackMgrStaticRouteSrcStartIf.setStatus("current")
_AlaStackMgrStaticRouteSrcEndIf_Type = InterfaceIndex
_AlaStackMgrStaticRouteSrcEndIf_Object = MibTableColumn
alaStackMgrStaticRouteSrcEndIf = _AlaStackMgrStaticRouteSrcEndIf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 2),
    _AlaStackMgrStaticRouteSrcEndIf_Type()
)
alaStackMgrStaticRouteSrcEndIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaStackMgrStaticRouteSrcEndIf.setStatus("current")
_AlaStackMgrStaticRouteDstStartIf_Type = InterfaceIndex
_AlaStackMgrStaticRouteDstStartIf_Object = MibTableColumn
alaStackMgrStaticRouteDstStartIf = _AlaStackMgrStaticRouteDstStartIf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 3),
    _AlaStackMgrStaticRouteDstStartIf_Type()
)
alaStackMgrStaticRouteDstStartIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaStackMgrStaticRouteDstStartIf.setStatus("current")
_AlaStackMgrStaticRouteDstEndIf_Type = InterfaceIndex
_AlaStackMgrStaticRouteDstEndIf_Object = MibTableColumn
alaStackMgrStaticRouteDstEndIf = _AlaStackMgrStaticRouteDstEndIf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 4),
    _AlaStackMgrStaticRouteDstEndIf_Type()
)
alaStackMgrStaticRouteDstEndIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaStackMgrStaticRouteDstEndIf.setStatus("current")


class _AlaStackMgrStaticRoutePort_Type(AlaStackMgrLinkNumber):
    """Custom type alaStackMgrStaticRoutePort based on AlaStackMgrLinkNumber"""
    defaultValue = 1


_AlaStackMgrStaticRoutePort_Object = MibTableColumn
alaStackMgrStaticRoutePort = _AlaStackMgrStaticRoutePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 5),
    _AlaStackMgrStaticRoutePort_Type()
)
alaStackMgrStaticRoutePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaStackMgrStaticRoutePort.setStatus("current")
_AlaStackMgrStaticRoutePortState_Type = AlaStackMgrLinkStatus
_AlaStackMgrStaticRoutePortState_Object = MibTableColumn
alaStackMgrStaticRoutePortState = _AlaStackMgrStaticRoutePortState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 6),
    _AlaStackMgrStaticRoutePortState_Type()
)
alaStackMgrStaticRoutePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaStackMgrStaticRoutePortState.setStatus("current")


class _AlaStackMgrStaticRouteStatus_Type(Integer32):
    """Custom type alaStackMgrStaticRouteStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AlaStackMgrStaticRouteStatus_Type.__name__ = "Integer32"
_AlaStackMgrStaticRouteStatus_Object = MibTableColumn
alaStackMgrStaticRouteStatus = _AlaStackMgrStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 7),
    _AlaStackMgrStaticRouteStatus_Type()
)
alaStackMgrStaticRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaStackMgrStaticRouteStatus.setStatus("current")
_AlaStackMgrStaticRouteRowStatus_Type = RowStatus
_AlaStackMgrStaticRouteRowStatus_Object = MibTableColumn
alaStackMgrStaticRouteRowStatus = _AlaStackMgrStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 8),
    _AlaStackMgrStaticRouteRowStatus_Type()
)
alaStackMgrStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaStackMgrStaticRouteRowStatus.setStatus("current")
_AlcatelIND1StackMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1StackMgrMIBConformance = _AlcatelIND1StackMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2)
)
_AlcatelIND1StackMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1StackMgrMIBGroups = _AlcatelIND1StackMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1)
)
_AlcatelIND1StackMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1StackMgrMIBCompliances = _AlcatelIND1StackMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 2)
)
_AlcatelIND1StackMgrTrapObjects_ObjectIdentity = ObjectIdentity
alcatelIND1StackMgrTrapObjects = _AlcatelIND1StackMgrTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3)
)
_AlaStackMgrTrapLinkNumber_Type = AlaStackMgrLinkNumber
_AlaStackMgrTrapLinkNumber_Object = MibScalar
alaStackMgrTrapLinkNumber = _AlaStackMgrTrapLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 1),
    _AlaStackMgrTrapLinkNumber_Type()
)
alaStackMgrTrapLinkNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaStackMgrTrapLinkNumber.setStatus("current")
_AlaStackMgrPrimary_Type = AlaStackMgrNINumber
_AlaStackMgrPrimary_Object = MibScalar
alaStackMgrPrimary = _AlaStackMgrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 2),
    _AlaStackMgrPrimary_Type()
)
alaStackMgrPrimary.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaStackMgrPrimary.setStatus("current")
_AlaStackMgrSecondary_Type = AlaStackMgrNINumber
_AlaStackMgrSecondary_Object = MibScalar
alaStackMgrSecondary = _AlaStackMgrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 3),
    _AlaStackMgrSecondary_Type()
)
alaStackMgrSecondary.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaStackMgrSecondary.setStatus("current")
_AlaStackMgrTraps_ObjectIdentity = ObjectIdentity
alaStackMgrTraps = _AlaStackMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4)
)

# Managed Objects groups

alaStackMgrCfgMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1, 1)
)
alaStackMgrCfgMgrGroup.setObjects(
      *(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotCMMNumber"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasRole"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrLocalLinkStateA"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteNISlotA"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteLinkA"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrLocalLinkStateB"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteNISlotB"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteLinkB"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasState"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSavedSlotNINumber"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCommandAction"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCommandStatus"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOperStackingMode"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrAdminStackingMode"))
)
if mibBuilder.loadTexts:
    alaStackMgrCfgMgrGroup.setStatus("current")


# Notification objects

alaStackMgrDuplicateSlotTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 1)
)
alaStackMgrDuplicateSlotTrap.setObjects(
    ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber")
)
if mibBuilder.loadTexts:
    alaStackMgrDuplicateSlotTrap.setStatus(
        "current"
    )

alaStackMgrNeighborChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 2)
)
alaStackMgrNeighborChangeTrap.setObjects(
      *(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStackStatus"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrTrapLinkNumber"))
)
if mibBuilder.loadTexts:
    alaStackMgrNeighborChangeTrap.setStatus(
        "current"
    )

alaStackMgrRoleChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 3)
)
alaStackMgrRoleChangeTrap.setObjects(
      *(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrPrimary"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSecondary"))
)
if mibBuilder.loadTexts:
    alaStackMgrRoleChangeTrap.setStatus(
        "current"
    )

alaStackMgrDuplicateRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 4)
)
alaStackMgrDuplicateRoleTrap.setObjects(
      *(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasRole"))
)
if mibBuilder.loadTexts:
    alaStackMgrDuplicateRoleTrap.setStatus(
        "current"
    )

alaStackMgrClearedSlotTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 5)
)
alaStackMgrClearedSlotTrap.setObjects(
    ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber")
)
if mibBuilder.loadTexts:
    alaStackMgrClearedSlotTrap.setStatus(
        "current"
    )

alaStackMgrOutOfSlotsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 6)
)
if mibBuilder.loadTexts:
    alaStackMgrOutOfSlotsTrap.setStatus(
        "current"
    )

alaStackMgrOutOfTokensTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 7)
)
alaStackMgrOutOfTokensTrap.setObjects(
    ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber")
)
if mibBuilder.loadTexts:
    alaStackMgrOutOfTokensTrap.setStatus(
        "current"
    )

alaStackMgrOutOfPassThruSlotsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 8)
)
if mibBuilder.loadTexts:
    alaStackMgrOutOfPassThruSlotsTrap.setStatus(
        "current"
    )

alaStackMgrBadMixTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 9)
)
alaStackMgrBadMixTrap.setObjects(
    ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber")
)
if mibBuilder.loadTexts:
    alaStackMgrBadMixTrap.setStatus(
        "current"
    )


# Notifications groups

alaStackMgrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1, 2)
)
alaStackMgrNotificationGroup.setObjects(
      *(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrDuplicateSlotTrap"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrNeighborChangeTrap"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRoleChangeTrap"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrDuplicateRoleTrap"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrClearedSlotTrap"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfSlotsTrap"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfTokensTrap"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfPassThruSlotsTrap"),
        ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrBadMixTrap"))
)
if mibBuilder.loadTexts:
    alaStackMgrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1StackMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1StackMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-STACK-MANAGER-MIB",
    **{"AlaStackMgrLinkNumber": AlaStackMgrLinkNumber,
       "AlaStackMgrNINumber": AlaStackMgrNINumber,
       "AlaStackMgrLinkStatus": AlaStackMgrLinkStatus,
       "AlaStackMgrSlotRole": AlaStackMgrSlotRole,
       "AlaStackMgrStackStatus": AlaStackMgrStackStatus,
       "AlaStackMgrSlotState": AlaStackMgrSlotState,
       "AlaStackMgrCommandAction": AlaStackMgrCommandAction,
       "AlaStackMgrCommandStatus": AlaStackMgrCommandStatus,
       "AlaStackMgrStackingMode": AlaStackMgrStackingMode,
       "alcatelIND1StackMgrMIB": alcatelIND1StackMgrMIB,
       "alcatelIND1StackMgrMIBObjects": alcatelIND1StackMgrMIBObjects,
       "alaStackMgrChassisTable": alaStackMgrChassisTable,
       "alaStackMgrChassisEntry": alaStackMgrChassisEntry,
       "alaStackMgrSlotNINumber": alaStackMgrSlotNINumber,
       "alaStackMgrSlotCMMNumber": alaStackMgrSlotCMMNumber,
       "alaStackMgrChasRole": alaStackMgrChasRole,
       "alaStackMgrLocalLinkStateA": alaStackMgrLocalLinkStateA,
       "alaStackMgrRemoteNISlotA": alaStackMgrRemoteNISlotA,
       "alaStackMgrRemoteLinkA": alaStackMgrRemoteLinkA,
       "alaStackMgrLocalLinkStateB": alaStackMgrLocalLinkStateB,
       "alaStackMgrRemoteNISlotB": alaStackMgrRemoteNISlotB,
       "alaStackMgrRemoteLinkB": alaStackMgrRemoteLinkB,
       "alaStackMgrChasState": alaStackMgrChasState,
       "alaStackMgrSavedSlotNINumber": alaStackMgrSavedSlotNINumber,
       "alaStackMgrCommandAction": alaStackMgrCommandAction,
       "alaStackMgrCommandStatus": alaStackMgrCommandStatus,
       "alaStackMgrOperStackingMode": alaStackMgrOperStackingMode,
       "alaStackMgrAdminStackingMode": alaStackMgrAdminStackingMode,
       "alaStackMgrStatsTable": alaStackMgrStatsTable,
       "alaStackMgrStatsEntry": alaStackMgrStatsEntry,
       "alaStackMgrStatLinkNumber": alaStackMgrStatLinkNumber,
       "alaStackMgrStatPktsRx": alaStackMgrStatPktsRx,
       "alaStackMgrStatPktsTx": alaStackMgrStatPktsTx,
       "alaStackMgrStatErrorsRx": alaStackMgrStatErrorsRx,
       "alaStackMgrStatErrorsTx": alaStackMgrStatErrorsTx,
       "alaStackMgrStatDelayFromLastMsg": alaStackMgrStatDelayFromLastMsg,
       "alaStackMgrStackStatus": alaStackMgrStackStatus,
       "alaStackMgrTokensUsed": alaStackMgrTokensUsed,
       "alaStackMgrTokensAvailable": alaStackMgrTokensAvailable,
       "alaStackMgrStaticRouteTable": alaStackMgrStaticRouteTable,
       "alaStackMgrStaticRouteEntry": alaStackMgrStaticRouteEntry,
       "alaStackMgrStaticRouteSrcStartIf": alaStackMgrStaticRouteSrcStartIf,
       "alaStackMgrStaticRouteSrcEndIf": alaStackMgrStaticRouteSrcEndIf,
       "alaStackMgrStaticRouteDstStartIf": alaStackMgrStaticRouteDstStartIf,
       "alaStackMgrStaticRouteDstEndIf": alaStackMgrStaticRouteDstEndIf,
       "alaStackMgrStaticRoutePort": alaStackMgrStaticRoutePort,
       "alaStackMgrStaticRoutePortState": alaStackMgrStaticRoutePortState,
       "alaStackMgrStaticRouteStatus": alaStackMgrStaticRouteStatus,
       "alaStackMgrStaticRouteRowStatus": alaStackMgrStaticRouteRowStatus,
       "alcatelIND1StackMgrMIBConformance": alcatelIND1StackMgrMIBConformance,
       "alcatelIND1StackMgrMIBGroups": alcatelIND1StackMgrMIBGroups,
       "alaStackMgrCfgMgrGroup": alaStackMgrCfgMgrGroup,
       "alaStackMgrNotificationGroup": alaStackMgrNotificationGroup,
       "alcatelIND1StackMgrMIBCompliances": alcatelIND1StackMgrMIBCompliances,
       "alcatelIND1StackMgrMIBCompliance": alcatelIND1StackMgrMIBCompliance,
       "alcatelIND1StackMgrTrapObjects": alcatelIND1StackMgrTrapObjects,
       "alaStackMgrTrapLinkNumber": alaStackMgrTrapLinkNumber,
       "alaStackMgrPrimary": alaStackMgrPrimary,
       "alaStackMgrSecondary": alaStackMgrSecondary,
       "alaStackMgrTraps": alaStackMgrTraps,
       "alaStackMgrDuplicateSlotTrap": alaStackMgrDuplicateSlotTrap,
       "alaStackMgrNeighborChangeTrap": alaStackMgrNeighborChangeTrap,
       "alaStackMgrRoleChangeTrap": alaStackMgrRoleChangeTrap,
       "alaStackMgrDuplicateRoleTrap": alaStackMgrDuplicateRoleTrap,
       "alaStackMgrClearedSlotTrap": alaStackMgrClearedSlotTrap,
       "alaStackMgrOutOfSlotsTrap": alaStackMgrOutOfSlotsTrap,
       "alaStackMgrOutOfTokensTrap": alaStackMgrOutOfTokensTrap,
       "alaStackMgrOutOfPassThruSlotsTrap": alaStackMgrOutOfPassThruSlotsTrap,
       "alaStackMgrBadMixTrap": alaStackMgrBadMixTrap}
)
