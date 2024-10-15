# SNMP MIB module (AT-EPSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-EPSR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:06 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

epsr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136)
)
epsr.setRevisions(
        ("2006-11-22 12:12",
         "2006-02-16 16:19")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EpsrNodeState(Integer32, TextualConvention):
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



class EpsrInterfaceState(Integer32, TextualConvention):
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
        *(("blocked", 1),
          ("forward", 2),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_EpsrEvents_ObjectIdentity = ObjectIdentity
epsrEvents = _EpsrEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 1)
)
_EpsrEventVariablesTable_Object = MibTable
epsrEventVariablesTable = _EpsrEventVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2)
)
if mibBuilder.loadTexts:
    epsrEventVariablesTable.setStatus("current")
_EpsrEventVariablesEntry_Object = MibTableRow
epsrEventVariablesEntry = _EpsrEventVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1)
)
epsrEventVariablesEntry.setIndexNames(
    (0, "AT-EPSR-MIB", "epsrDomainName"),
)
if mibBuilder.loadTexts:
    epsrEventVariablesEntry.setStatus("current")


class _EpsrNodeTrapType_Type(Integer32):
    """Custom type epsrNodeTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterNodeTrap", 1),
          ("transitNodeTrap", 2),
          ("unknown", 0))
    )


_EpsrNodeTrapType_Type.__name__ = "Integer32"
_EpsrNodeTrapType_Object = MibTableColumn
epsrNodeTrapType = _EpsrNodeTrapType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 1),
    _EpsrNodeTrapType_Type()
)
epsrNodeTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrNodeTrapType.setStatus("current")


class _EpsrDomainName_Type(DisplayStringUnsized):
    """Custom type epsrDomainName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_EpsrDomainName_Type.__name__ = "DisplayStringUnsized"
_EpsrDomainName_Object = MibTableColumn
epsrDomainName = _EpsrDomainName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 2),
    _EpsrDomainName_Type()
)
epsrDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrDomainName.setStatus("current")
_EpsrFromState_Type = EpsrNodeState
_EpsrFromState_Object = MibTableColumn
epsrFromState = _EpsrFromState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 3),
    _EpsrFromState_Type()
)
epsrFromState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrFromState.setStatus("current")
_EpsrToState_Type = EpsrNodeState
_EpsrToState_Object = MibTableColumn
epsrToState = _EpsrToState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 4),
    _EpsrToState_Type()
)
epsrToState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrToState.setStatus("current")
_EpsrControlVlanId_Type = Integer32
_EpsrControlVlanId_Object = MibTableColumn
epsrControlVlanId = _EpsrControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 5),
    _EpsrControlVlanId_Type()
)
epsrControlVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrControlVlanId.setStatus("current")
_EpsrPrimaryIfIndex_Type = InterfaceIndex
_EpsrPrimaryIfIndex_Object = MibTableColumn
epsrPrimaryIfIndex = _EpsrPrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 6),
    _EpsrPrimaryIfIndex_Type()
)
epsrPrimaryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrPrimaryIfIndex.setStatus("current")
_EpsrPrimaryIfState_Type = EpsrInterfaceState
_EpsrPrimaryIfState_Object = MibTableColumn
epsrPrimaryIfState = _EpsrPrimaryIfState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 7),
    _EpsrPrimaryIfState_Type()
)
epsrPrimaryIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrPrimaryIfState.setStatus("current")
_EpsrSecondaryIfIndex_Type = InterfaceIndex
_EpsrSecondaryIfIndex_Object = MibTableColumn
epsrSecondaryIfIndex = _EpsrSecondaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 8),
    _EpsrSecondaryIfIndex_Type()
)
epsrSecondaryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrSecondaryIfIndex.setStatus("current")
_EpsrSecondaryIfState_Type = EpsrInterfaceState
_EpsrSecondaryIfState_Object = MibTableColumn
epsrSecondaryIfState = _EpsrSecondaryIfState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 9),
    _EpsrSecondaryIfState_Type()
)
epsrSecondaryIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsrSecondaryIfState.setStatus("current")

# Managed Objects groups


# Notification objects

epsrNodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 1, 1)
)
epsrNodeTrap.setObjects(
      *(("AT-EPSR-MIB", "epsrNodeTrapType"),
        ("AT-EPSR-MIB", "epsrDomainName"),
        ("AT-EPSR-MIB", "epsrFromState"),
        ("AT-EPSR-MIB", "epsrToState"),
        ("AT-EPSR-MIB", "epsrControlVlanId"),
        ("AT-EPSR-MIB", "epsrPrimaryIfIndex"),
        ("AT-EPSR-MIB", "epsrPrimaryIfState"),
        ("AT-EPSR-MIB", "epsrSecondaryIfIndex"),
        ("AT-EPSR-MIB", "epsrSecondaryIfState"))
)
if mibBuilder.loadTexts:
    epsrNodeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-EPSR-MIB",
    **{"EpsrNodeState": EpsrNodeState,
       "EpsrInterfaceState": EpsrInterfaceState,
       "epsr": epsr,
       "epsrEvents": epsrEvents,
       "epsrNodeTrap": epsrNodeTrap,
       "epsrEventVariablesTable": epsrEventVariablesTable,
       "epsrEventVariablesEntry": epsrEventVariablesEntry,
       "epsrNodeTrapType": epsrNodeTrapType,
       "epsrDomainName": epsrDomainName,
       "epsrFromState": epsrFromState,
       "epsrToState": epsrToState,
       "epsrControlVlanId": epsrControlVlanId,
       "epsrPrimaryIfIndex": epsrPrimaryIfIndex,
       "epsrPrimaryIfState": epsrPrimaryIfState,
       "epsrSecondaryIfIndex": epsrSecondaryIfIndex,
       "epsrSecondaryIfState": epsrSecondaryIfState}
)
