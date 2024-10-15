# SNMP MIB module (CTRON-RATE-POLICING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-RATE-POLICING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:11 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ctPriorityExt,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctPriorityExt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ctRatePolicing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7)
)
ctRatePolicing.setRevisions(
        ("2003-04-10 15:18",
         "2003-03-11 15:53",
         "2000-11-28 15:51",
         "1999-06-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CtPriList(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CtRatePolActionList(Integer32, TextualConvention):
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
        *(("dropPacket", 1),
          ("dropPacketOrFlowCtrlAndDrop", 3),
          ("flowCtrlPacketAndDrop", 2),
          ("none", 0))
    )



class CtRatePolDirectionList(Integer32, TextualConvention):
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
        *(("inbound", 1),
          ("inboundAndOutbound", 3),
          ("none", 0),
          ("outbound", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CtRatePolicingObjects_ObjectIdentity = ObjectIdentity
ctRatePolicingObjects = _CtRatePolicingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1)
)


class _CtRatePolicingAdminStatus_Type(Integer32):
    """Custom type ctRatePolicingAdminStatus based on Integer32"""
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


_CtRatePolicingAdminStatus_Type.__name__ = "Integer32"
_CtRatePolicingAdminStatus_Object = MibScalar
ctRatePolicingAdminStatus = _CtRatePolicingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 1),
    _CtRatePolicingAdminStatus_Type()
)
ctRatePolicingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRatePolicingAdminStatus.setStatus("current")
_CtRatePolicingConfigLastChange_Type = TimeTicks
_CtRatePolicingConfigLastChange_Object = MibScalar
ctRatePolicingConfigLastChange = _CtRatePolicingConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 2),
    _CtRatePolicingConfigLastChange_Type()
)
ctRatePolicingConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRatePolicingConfigLastChange.setStatus("current")
_CtRatePolicingConfigTable_Object = MibTable
ctRatePolicingConfigTable = _CtRatePolicingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3)
)
if mibBuilder.loadTexts:
    ctRatePolicingConfigTable.setStatus("current")
_CtRatePolicingConfigEntry_Object = MibTableRow
ctRatePolicingConfigEntry = _CtRatePolicingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1)
)
ctRatePolicingConfigEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "CTRON-RATE-POLICING-MIB", "ctRatePolicingResourceIndex"),
)
if mibBuilder.loadTexts:
    ctRatePolicingConfigEntry.setStatus("current")


class _CtRatePolicingResourceIndex_Type(Integer32):
    """Custom type ctRatePolicingResourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtRatePolicingResourceIndex_Type.__name__ = "Integer32"
_CtRatePolicingResourceIndex_Object = MibTableColumn
ctRatePolicingResourceIndex = _CtRatePolicingResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 1),
    _CtRatePolicingResourceIndex_Type()
)
ctRatePolicingResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctRatePolicingResourceIndex.setStatus("current")
_CtRatePolicingActionsAllowed_Type = CtRatePolActionList
_CtRatePolicingActionsAllowed_Object = MibTableColumn
ctRatePolicingActionsAllowed = _CtRatePolicingActionsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 2),
    _CtRatePolicingActionsAllowed_Type()
)
ctRatePolicingActionsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRatePolicingActionsAllowed.setStatus("current")
_CtRatePolicingAction_Type = CtRatePolActionList
_CtRatePolicingAction_Object = MibTableColumn
ctRatePolicingAction = _CtRatePolicingAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 3),
    _CtRatePolicingAction_Type()
)
ctRatePolicingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRatePolicingAction.setStatus("current")


class _CtRatePolicingThreshHoldMin_Type(Integer32):
    """Custom type ctRatePolicingThreshHoldMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtRatePolicingThreshHoldMin_Type.__name__ = "Integer32"
_CtRatePolicingThreshHoldMin_Object = MibTableColumn
ctRatePolicingThreshHoldMin = _CtRatePolicingThreshHoldMin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 4),
    _CtRatePolicingThreshHoldMin_Type()
)
ctRatePolicingThreshHoldMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRatePolicingThreshHoldMin.setStatus("current")
if mibBuilder.loadTexts:
    ctRatePolicingThreshHoldMin.setUnits("kilobytes")


class _CtRatePolicingThreshHold_Type(Integer32):
    """Custom type ctRatePolicingThreshHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtRatePolicingThreshHold_Type.__name__ = "Integer32"
_CtRatePolicingThreshHold_Object = MibTableColumn
ctRatePolicingThreshHold = _CtRatePolicingThreshHold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 5),
    _CtRatePolicingThreshHold_Type()
)
ctRatePolicingThreshHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRatePolicingThreshHold.setStatus("current")
if mibBuilder.loadTexts:
    ctRatePolicingThreshHold.setUnits("kilobytes")
_CtRatePolicingPriorityList_Type = CtPriList
_CtRatePolicingPriorityList_Object = MibTableColumn
ctRatePolicingPriorityList = _CtRatePolicingPriorityList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 6),
    _CtRatePolicingPriorityList_Type()
)
ctRatePolicingPriorityList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRatePolicingPriorityList.setStatus("current")


class _CtRatePolicingRuleStatus_Type(Integer32):
    """Custom type ctRatePolicingRuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 2))
    )


_CtRatePolicingRuleStatus_Type.__name__ = "Integer32"
_CtRatePolicingRuleStatus_Object = MibTableColumn
ctRatePolicingRuleStatus = _CtRatePolicingRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 7),
    _CtRatePolicingRuleStatus_Type()
)
ctRatePolicingRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRatePolicingRuleStatus.setStatus("current")
_CtRatePolicingActionsTaken_Type = Integer32
_CtRatePolicingActionsTaken_Object = MibTableColumn
ctRatePolicingActionsTaken = _CtRatePolicingActionsTaken_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 8),
    _CtRatePolicingActionsTaken_Type()
)
ctRatePolicingActionsTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRatePolicingActionsTaken.setStatus("current")
_CtRatePolicingDirectionsAllowed_Type = CtRatePolDirectionList
_CtRatePolicingDirectionsAllowed_Object = MibTableColumn
ctRatePolicingDirectionsAllowed = _CtRatePolicingDirectionsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 9),
    _CtRatePolicingDirectionsAllowed_Type()
)
ctRatePolicingDirectionsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRatePolicingDirectionsAllowed.setStatus("current")
_CtRatePolicingDirection_Type = CtRatePolDirectionList
_CtRatePolicingDirection_Object = MibTableColumn
ctRatePolicingDirection = _CtRatePolicingDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 10),
    _CtRatePolicingDirection_Type()
)
ctRatePolicingDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRatePolicingDirection.setStatus("current")
_CtRatePolicingConformance_ObjectIdentity = ObjectIdentity
ctRatePolicingConformance = _CtRatePolicingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2)
)
_CtRatePolicingGroups_ObjectIdentity = ObjectIdentity
ctRatePolicingGroups = _CtRatePolicingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 1)
)
_CtRatePolicingCompliances_ObjectIdentity = ObjectIdentity
ctRatePolicingCompliances = _CtRatePolicingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 2)
)

# Managed Objects groups

ctRatePolicingConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 1, 1)
)
ctRatePolicingConfigGroup.setObjects(
      *(("CTRON-RATE-POLICING-MIB", "ctRatePolicingAdminStatus"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingConfigLastChange"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingActionsAllowed"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingAction"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingThreshHold"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingPriorityList"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingRuleStatus"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingActionsTaken"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingDirectionsAllowed"),
        ("CTRON-RATE-POLICING-MIB", "ctRatePolicingDirection"))
)
if mibBuilder.loadTexts:
    ctRatePolicingConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctRatePolicingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ctRatePolicingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-RATE-POLICING-MIB",
    **{"CtPriList": CtPriList,
       "CtRatePolActionList": CtRatePolActionList,
       "CtRatePolDirectionList": CtRatePolDirectionList,
       "ctRatePolicing": ctRatePolicing,
       "ctRatePolicingObjects": ctRatePolicingObjects,
       "ctRatePolicingAdminStatus": ctRatePolicingAdminStatus,
       "ctRatePolicingConfigLastChange": ctRatePolicingConfigLastChange,
       "ctRatePolicingConfigTable": ctRatePolicingConfigTable,
       "ctRatePolicingConfigEntry": ctRatePolicingConfigEntry,
       "ctRatePolicingResourceIndex": ctRatePolicingResourceIndex,
       "ctRatePolicingActionsAllowed": ctRatePolicingActionsAllowed,
       "ctRatePolicingAction": ctRatePolicingAction,
       "ctRatePolicingThreshHoldMin": ctRatePolicingThreshHoldMin,
       "ctRatePolicingThreshHold": ctRatePolicingThreshHold,
       "ctRatePolicingPriorityList": ctRatePolicingPriorityList,
       "ctRatePolicingRuleStatus": ctRatePolicingRuleStatus,
       "ctRatePolicingActionsTaken": ctRatePolicingActionsTaken,
       "ctRatePolicingDirectionsAllowed": ctRatePolicingDirectionsAllowed,
       "ctRatePolicingDirection": ctRatePolicingDirection,
       "ctRatePolicingConformance": ctRatePolicingConformance,
       "ctRatePolicingGroups": ctRatePolicingGroups,
       "ctRatePolicingConfigGroup": ctRatePolicingConfigGroup,
       "ctRatePolicingCompliances": ctRatePolicingCompliances,
       "ctRatePolicingCompliance": ctRatePolicingCompliance}
)
