# SNMP MIB module (AT-EPSRv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-EPSRv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:07 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atEpsrv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536)
)
atEpsrv2.setRevisions(
        ("2011-07-07 00:00",
         "2010-09-07 00:00",
         "2010-06-14 04:55",
         "2010-05-24 01:19",
         "2010-01-15 00:39",
         "2008-12-23 01:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtEpsrv2NodeState(Integer32, TextualConvention):
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
        *(("complete", 1),
          ("failed", 2),
          ("idle", 0),
          ("linksDown", 4),
          ("linksUp", 3),
          ("preForward", 5),
          ("unknown", 6))
    )



class AtEpsrv2InterfaceState(Integer32, TextualConvention):
    status = "current"
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
        *(("blocked", 3),
          ("down", 2),
          ("forward", 4),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AtEpsrv2Notifications_ObjectIdentity = ObjectIdentity
atEpsrv2Notifications = _AtEpsrv2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 0)
)
_AtEpsrv2Events_ObjectIdentity = ObjectIdentity
atEpsrv2Events = _AtEpsrv2Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 1)
)
_AtEpsrv2VariablesTable_Object = MibTable
atEpsrv2VariablesTable = _AtEpsrv2VariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2)
)
if mibBuilder.loadTexts:
    atEpsrv2VariablesTable.setStatus("current")
_AtEpsrv2VariablesEntry_Object = MibTableRow
atEpsrv2VariablesEntry = _AtEpsrv2VariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1)
)
atEpsrv2VariablesEntry.setIndexNames(
    (0, "AT-EPSRv2-MIB", "atEpsrv2DomainID"),
)
if mibBuilder.loadTexts:
    atEpsrv2VariablesEntry.setStatus("current")


class _AtEpsrv2NodeType_Type(Integer32):
    """Custom type atEpsrv2NodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterNode", 1),
          ("transitNode", 2))
    )


_AtEpsrv2NodeType_Type.__name__ = "Integer32"
_AtEpsrv2NodeType_Object = MibTableColumn
atEpsrv2NodeType = _AtEpsrv2NodeType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 1),
    _AtEpsrv2NodeType_Type()
)
atEpsrv2NodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2NodeType.setStatus("current")


class _AtEpsrv2DomainName_Type(DisplayStringUnsized):
    """Custom type atEpsrv2DomainName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AtEpsrv2DomainName_Type.__name__ = "DisplayStringUnsized"
_AtEpsrv2DomainName_Object = MibTableColumn
atEpsrv2DomainName = _AtEpsrv2DomainName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 2),
    _AtEpsrv2DomainName_Type()
)
atEpsrv2DomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2DomainName.setStatus("current")


class _AtEpsrv2DomainID_Type(Integer32):
    """Custom type atEpsrv2DomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtEpsrv2DomainID_Type.__name__ = "Integer32"
_AtEpsrv2DomainID_Object = MibTableColumn
atEpsrv2DomainID = _AtEpsrv2DomainID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 3),
    _AtEpsrv2DomainID_Type()
)
atEpsrv2DomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2DomainID.setStatus("current")
_AtEpsrv2FromState_Type = AtEpsrv2NodeState
_AtEpsrv2FromState_Object = MibTableColumn
atEpsrv2FromState = _AtEpsrv2FromState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 4),
    _AtEpsrv2FromState_Type()
)
atEpsrv2FromState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2FromState.setStatus("current")
_AtEpsrv2CurrentState_Type = AtEpsrv2NodeState
_AtEpsrv2CurrentState_Object = MibTableColumn
atEpsrv2CurrentState = _AtEpsrv2CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 5),
    _AtEpsrv2CurrentState_Type()
)
atEpsrv2CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2CurrentState.setStatus("current")
_AtEpsrv2ControlVlanId_Type = Integer32
_AtEpsrv2ControlVlanId_Object = MibTableColumn
atEpsrv2ControlVlanId = _AtEpsrv2ControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 6),
    _AtEpsrv2ControlVlanId_Type()
)
atEpsrv2ControlVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2ControlVlanId.setStatus("current")
_AtEpsrv2PrimaryIfIndex_Type = InterfaceIndex
_AtEpsrv2PrimaryIfIndex_Object = MibTableColumn
atEpsrv2PrimaryIfIndex = _AtEpsrv2PrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 7),
    _AtEpsrv2PrimaryIfIndex_Type()
)
atEpsrv2PrimaryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2PrimaryIfIndex.setStatus("current")
_AtEpsrv2PrimaryIfState_Type = AtEpsrv2InterfaceState
_AtEpsrv2PrimaryIfState_Object = MibTableColumn
atEpsrv2PrimaryIfState = _AtEpsrv2PrimaryIfState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 8),
    _AtEpsrv2PrimaryIfState_Type()
)
atEpsrv2PrimaryIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2PrimaryIfState.setStatus("current")
_AtEpsrv2SecondaryIfIndex_Type = InterfaceIndex
_AtEpsrv2SecondaryIfIndex_Object = MibTableColumn
atEpsrv2SecondaryIfIndex = _AtEpsrv2SecondaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 9),
    _AtEpsrv2SecondaryIfIndex_Type()
)
atEpsrv2SecondaryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2SecondaryIfIndex.setStatus("current")
_AtEpsrv2SecondaryIfState_Type = AtEpsrv2InterfaceState
_AtEpsrv2SecondaryIfState_Object = MibTableColumn
atEpsrv2SecondaryIfState = _AtEpsrv2SecondaryIfState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 10),
    _AtEpsrv2SecondaryIfState_Type()
)
atEpsrv2SecondaryIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2SecondaryIfState.setStatus("current")
_AtEpsrv2DomainPriority_Type = Integer32
_AtEpsrv2DomainPriority_Object = MibTableColumn
atEpsrv2DomainPriority = _AtEpsrv2DomainPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 11),
    _AtEpsrv2DomainPriority_Type()
)
atEpsrv2DomainPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2DomainPriority.setStatus("current")
_AtEpsrv2PrimaryIfIsOnCommonSeg_Type = TruthValue
_AtEpsrv2PrimaryIfIsOnCommonSeg_Object = MibTableColumn
atEpsrv2PrimaryIfIsOnCommonSeg = _AtEpsrv2PrimaryIfIsOnCommonSeg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 12),
    _AtEpsrv2PrimaryIfIsOnCommonSeg_Type()
)
atEpsrv2PrimaryIfIsOnCommonSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2PrimaryIfIsOnCommonSeg.setStatus("current")
_AtEpsrv2SecondaryIfIsOnCommonSeg_Type = TruthValue
_AtEpsrv2SecondaryIfIsOnCommonSeg_Object = MibTableColumn
atEpsrv2SecondaryIfIsOnCommonSeg = _AtEpsrv2SecondaryIfIsOnCommonSeg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 13),
    _AtEpsrv2SecondaryIfIsOnCommonSeg_Type()
)
atEpsrv2SecondaryIfIsOnCommonSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2SecondaryIfIsOnCommonSeg.setStatus("current")
_AtEpsrv2HasControlOfPrimaryIf_Type = TruthValue
_AtEpsrv2HasControlOfPrimaryIf_Object = MibTableColumn
atEpsrv2HasControlOfPrimaryIf = _AtEpsrv2HasControlOfPrimaryIf_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 14),
    _AtEpsrv2HasControlOfPrimaryIf_Type()
)
atEpsrv2HasControlOfPrimaryIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2HasControlOfPrimaryIf.setStatus("current")
_AtEpsrv2HasControlOfSecondaryIf_Type = TruthValue
_AtEpsrv2HasControlOfSecondaryIf_Object = MibTableColumn
atEpsrv2HasControlOfSecondaryIf = _AtEpsrv2HasControlOfSecondaryIf_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 15),
    _AtEpsrv2HasControlOfSecondaryIf_Type()
)
atEpsrv2HasControlOfSecondaryIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEpsrv2HasControlOfSecondaryIf.setStatus("current")

# Managed Objects groups


# Notification objects

atEpsrv2Notify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 0, 1)
)
atEpsrv2Notify.setObjects(
      *(("AT-EPSRv2-MIB", "atEpsrv2NodeType"),
        ("AT-EPSRv2-MIB", "atEpsrv2DomainName"),
        ("AT-EPSRv2-MIB", "atEpsrv2DomainID"),
        ("AT-EPSRv2-MIB", "atEpsrv2FromState"),
        ("AT-EPSRv2-MIB", "atEpsrv2CurrentState"),
        ("AT-EPSRv2-MIB", "atEpsrv2ControlVlanId"),
        ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfIndex"),
        ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfState"),
        ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfIndex"),
        ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfState"),
        ("AT-EPSRv2-MIB", "atEpsrv2DomainPriority"),
        ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfIsOnCommonSeg"),
        ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfIsOnCommonSeg"),
        ("AT-EPSRv2-MIB", "atEpsrv2HasControlOfPrimaryIf"),
        ("AT-EPSRv2-MIB", "atEpsrv2HasControlOfSecondaryIf"))
)
if mibBuilder.loadTexts:
    atEpsrv2Notify.setStatus(
        "current"
    )

atEpsrv2NodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 1, 1)
)
atEpsrv2NodeTrap.setObjects(
      *(("AT-EPSRv2-MIB", "atEpsrv2NodeType"),
        ("AT-EPSRv2-MIB", "atEpsrv2DomainName"),
        ("AT-EPSRv2-MIB", "atEpsrv2DomainID"),
        ("AT-EPSRv2-MIB", "atEpsrv2FromState"),
        ("AT-EPSRv2-MIB", "atEpsrv2CurrentState"),
        ("AT-EPSRv2-MIB", "atEpsrv2ControlVlanId"),
        ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfIndex"),
        ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfState"),
        ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfIndex"),
        ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfState"))
)
if mibBuilder.loadTexts:
    atEpsrv2NodeTrap.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-EPSRv2-MIB",
    **{"AtEpsrv2NodeState": AtEpsrv2NodeState,
       "AtEpsrv2InterfaceState": AtEpsrv2InterfaceState,
       "atEpsrv2": atEpsrv2,
       "atEpsrv2Notifications": atEpsrv2Notifications,
       "atEpsrv2Notify": atEpsrv2Notify,
       "atEpsrv2Events": atEpsrv2Events,
       "atEpsrv2NodeTrap": atEpsrv2NodeTrap,
       "atEpsrv2VariablesTable": atEpsrv2VariablesTable,
       "atEpsrv2VariablesEntry": atEpsrv2VariablesEntry,
       "atEpsrv2NodeType": atEpsrv2NodeType,
       "atEpsrv2DomainName": atEpsrv2DomainName,
       "atEpsrv2DomainID": atEpsrv2DomainID,
       "atEpsrv2FromState": atEpsrv2FromState,
       "atEpsrv2CurrentState": atEpsrv2CurrentState,
       "atEpsrv2ControlVlanId": atEpsrv2ControlVlanId,
       "atEpsrv2PrimaryIfIndex": atEpsrv2PrimaryIfIndex,
       "atEpsrv2PrimaryIfState": atEpsrv2PrimaryIfState,
       "atEpsrv2SecondaryIfIndex": atEpsrv2SecondaryIfIndex,
       "atEpsrv2SecondaryIfState": atEpsrv2SecondaryIfState,
       "atEpsrv2DomainPriority": atEpsrv2DomainPriority,
       "atEpsrv2PrimaryIfIsOnCommonSeg": atEpsrv2PrimaryIfIsOnCommonSeg,
       "atEpsrv2SecondaryIfIsOnCommonSeg": atEpsrv2SecondaryIfIsOnCommonSeg,
       "atEpsrv2HasControlOfPrimaryIf": atEpsrv2HasControlOfPrimaryIf,
       "atEpsrv2HasControlOfSecondaryIf": atEpsrv2HasControlOfSecondaryIf}
)
