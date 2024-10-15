# SNMP MIB module (STN-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:06 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,
 stnSystems) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification",
    "stnSystems")


# MODULE-IDENTITY

stnIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class StnInterfaceType(Integer32, TextualConvention):
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
        *(("ds3", 5),
          ("epif", 4),
          ("ethernet", 2),
          ("sonet", 3),
          ("unknown", 1))
    )



class StnIfOperStatus(Integer32, TextualConvention):
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
        *(("down-non-redundant", 4),
          ("down-redundant", 5),
          ("unknown", 1),
          ("up-non-redundant", 2),
          ("up-redundant", 3))
    )



class StnIfDuplexType(Integer32, TextualConvention):
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
        *(("full", 3),
          ("half", 2),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_StnInterfaces_ObjectIdentity = ObjectIdentity
stnInterfaces = _StnInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1)
)
_StnIf_ObjectIdentity = ObjectIdentity
stnIf = _StnIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1)
)
_StnIfTable_Object = MibTable
stnIfTable = _StnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnIfTable.setStatus("current")
_StnIfEntry_Object = MibTableRow
stnIfEntry = _StnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1)
)
stnIfEntry.setIndexNames(
    (0, "STN-IF-MIB", "stnIfIndex"),
)
if mibBuilder.loadTexts:
    stnIfEntry.setStatus("current")
_StnIfIndex_Type = InterfaceIndex
_StnIfIndex_Object = MibTableColumn
stnIfIndex = _StnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 1),
    _StnIfIndex_Type()
)
stnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfIndex.setStatus("current")
_StnIfSlot_Type = Integer32
_StnIfSlot_Object = MibTableColumn
stnIfSlot = _StnIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 2),
    _StnIfSlot_Type()
)
stnIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfSlot.setStatus("current")
_StnIfPort_Type = Integer32
_StnIfPort_Object = MibTableColumn
stnIfPort = _StnIfPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 3),
    _StnIfPort_Type()
)
stnIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfPort.setStatus("current")
_StnIfEngine1_Type = Integer32
_StnIfEngine1_Object = MibTableColumn
stnIfEngine1 = _StnIfEngine1_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 4),
    _StnIfEngine1_Type()
)
stnIfEngine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfEngine1.setStatus("current")
_StnIfEngine2_Type = Integer32
_StnIfEngine2_Object = MibTableColumn
stnIfEngine2 = _StnIfEngine2_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 5),
    _StnIfEngine2_Type()
)
stnIfEngine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfEngine2.setStatus("current")
_StnIfInternalPort_Type = Integer32
_StnIfInternalPort_Object = MibTableColumn
stnIfInternalPort = _StnIfInternalPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 6),
    _StnIfInternalPort_Type()
)
stnIfInternalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfInternalPort.setStatus("current")
_StnIfType_Type = StnInterfaceType
_StnIfType_Object = MibTableColumn
stnIfType = _StnIfType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 7),
    _StnIfType_Type()
)
stnIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfType.setStatus("current")
_StnIfOperStatus_Type = StnIfOperStatus
_StnIfOperStatus_Object = MibTableColumn
stnIfOperStatus = _StnIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 8),
    _StnIfOperStatus_Type()
)
stnIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfOperStatus.setStatus("current")
_StnIfDescr_Type = DisplayString
_StnIfDescr_Object = MibTableColumn
stnIfDescr = _StnIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 9),
    _StnIfDescr_Type()
)
stnIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfDescr.setStatus("current")
_StnIfDuplex_Type = StnIfDuplexType
_StnIfDuplex_Object = MibTableColumn
stnIfDuplex = _StnIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 1, 1, 1, 1, 10),
    _StnIfDuplex_Type()
)
stnIfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIfDuplex.setStatus("current")
_StnIfMibConformance_ObjectIdentity = ObjectIdentity
stnIfMibConformance = _StnIfMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 2)
)
_StnIfMibCompliances_ObjectIdentity = ObjectIdentity
stnIfMibCompliances = _StnIfMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 1)
)
_StnIfMibGroups_ObjectIdentity = ObjectIdentity
stnIfMibGroups = _StnIfMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 2)
)

# Managed Objects groups

stnIfMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 2, 1)
)
stnIfMibGroup.setObjects(
      *(("STN-IF-MIB", "stnIfIndex"),
        ("STN-IF-MIB", "stnIfSlot"),
        ("STN-IF-MIB", "stnIfPort"),
        ("STN-IF-MIB", "stnIfEngine1"),
        ("STN-IF-MIB", "stnIfEngine2"),
        ("STN-IF-MIB", "stnIfInternalPort"),
        ("STN-IF-MIB", "stnIfType"),
        ("STN-IF-MIB", "stnIfOperStatus"),
        ("STN-IF-MIB", "stnIfDescr"),
        ("STN-IF-MIB", "stnIfDuplex"))
)
if mibBuilder.loadTexts:
    stnIfMibGroup.setStatus("current")


# Notification objects

stnInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 13)
)
stnInterfaceUp.setObjects(
      *(("STN-IF-MIB", "stnIfIndex"),
        ("STN-IF-MIB", "stnIfSlot"),
        ("STN-IF-MIB", "stnIfPort"),
        ("STN-IF-MIB", "stnIfEngine1"),
        ("STN-IF-MIB", "stnIfEngine2"),
        ("STN-IF-MIB", "stnIfInternalPort"),
        ("STN-IF-MIB", "stnIfType"),
        ("STN-IF-MIB", "stnIfOperStatus"),
        ("STN-IF-MIB", "stnIfDescr"))
)
if mibBuilder.loadTexts:
    stnInterfaceUp.setStatus(
        "current"
    )

stnInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 14)
)
stnInterfaceDown.setObjects(
      *(("STN-IF-MIB", "stnIfIndex"),
        ("STN-IF-MIB", "stnIfSlot"),
        ("STN-IF-MIB", "stnIfPort"),
        ("STN-IF-MIB", "stnIfEngine1"),
        ("STN-IF-MIB", "stnIfEngine2"),
        ("STN-IF-MIB", "stnIfInternalPort"),
        ("STN-IF-MIB", "stnIfType"),
        ("STN-IF-MIB", "stnIfOperStatus"),
        ("STN-IF-MIB", "stnIfDescr"))
)
if mibBuilder.loadTexts:
    stnInterfaceDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

stnIfMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3551, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    stnIfMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-IF-MIB",
    **{"StnInterfaceType": StnInterfaceType,
       "StnIfOperStatus": StnIfOperStatus,
       "StnIfDuplexType": StnIfDuplexType,
       "stnIfMIB": stnIfMIB,
       "stnInterfaces": stnInterfaces,
       "stnIf": stnIf,
       "stnIfTable": stnIfTable,
       "stnIfEntry": stnIfEntry,
       "stnIfIndex": stnIfIndex,
       "stnIfSlot": stnIfSlot,
       "stnIfPort": stnIfPort,
       "stnIfEngine1": stnIfEngine1,
       "stnIfEngine2": stnIfEngine2,
       "stnIfInternalPort": stnIfInternalPort,
       "stnIfType": stnIfType,
       "stnIfOperStatus": stnIfOperStatus,
       "stnIfDescr": stnIfDescr,
       "stnIfDuplex": stnIfDuplex,
       "stnIfMibConformance": stnIfMibConformance,
       "stnIfMibCompliances": stnIfMibCompliances,
       "stnIfMibComplianceRev1": stnIfMibComplianceRev1,
       "stnIfMibGroups": stnIfMibGroups,
       "stnIfMibGroup": stnIfMibGroup,
       "stnInterfaceUp": stnInterfaceUp,
       "stnInterfaceDown": stnInterfaceDown}
)
