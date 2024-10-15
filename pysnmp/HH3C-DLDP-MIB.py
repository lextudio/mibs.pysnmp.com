# SNMP MIB module (HH3C-DLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:46 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43)
)
hh3cDldp.setRevisions(
        ("2004-12-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
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



class DLDPStatus(Integer32, TextualConvention):
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
        *(("active", 3),
          ("advertisement", 4),
          ("disable", 6),
          ("inactive", 2),
          ("initial", 1),
          ("probe", 5))
    )



class DLDPNeighborStatus(Integer32, TextualConvention):
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
        *(("bidirection", 2),
          ("unidirection", 1),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDLDPMibObject_ObjectIdentity = ObjectIdentity
hh3cDLDPMibObject = _Hh3cDLDPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1)
)
_Hh3cDLDPConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDLDPConfigGroup = _Hh3cDLDPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1)
)


class _Hh3cDLDPWorkMode_Type(Integer32):
    """Custom type hh3cDLDPWorkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enhance", 2),
          ("normal", 1))
    )


_Hh3cDLDPWorkMode_Type.__name__ = "Integer32"
_Hh3cDLDPWorkMode_Object = MibScalar
hh3cDLDPWorkMode = _Hh3cDLDPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 1),
    _Hh3cDLDPWorkMode_Type()
)
hh3cDLDPWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPWorkMode.setStatus("current")
_Hh3cDLDPSystemEnable_Type = TruthValue
_Hh3cDLDPSystemEnable_Object = MibScalar
hh3cDLDPSystemEnable = _Hh3cDLDPSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 2),
    _Hh3cDLDPSystemEnable_Type()
)
hh3cDLDPSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPSystemEnable.setStatus("current")
_Hh3cDLDPSystemReset_Type = TruthValue
_Hh3cDLDPSystemReset_Object = MibScalar
hh3cDLDPSystemReset = _Hh3cDLDPSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 3),
    _Hh3cDLDPSystemReset_Type()
)
hh3cDLDPSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPSystemReset.setStatus("current")


class _Hh3cDLDPInterval_Type(Integer32):
    """Custom type hh3cDLDPInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cDLDPInterval_Type.__name__ = "Integer32"
_Hh3cDLDPInterval_Object = MibScalar
hh3cDLDPInterval = _Hh3cDLDPInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 4),
    _Hh3cDLDPInterval_Type()
)
hh3cDLDPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPInterval.setStatus("current")


class _Hh3cDLDPAuthenticationMode_Type(Integer32):
    """Custom type hh3cDLDPAuthenticationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("simple", 2))
    )


_Hh3cDLDPAuthenticationMode_Type.__name__ = "Integer32"
_Hh3cDLDPAuthenticationMode_Object = MibScalar
hh3cDLDPAuthenticationMode = _Hh3cDLDPAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 5),
    _Hh3cDLDPAuthenticationMode_Type()
)
hh3cDLDPAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPAuthenticationMode.setStatus("current")


class _Hh3cDLDPAuthenticationPassword_Type(OctetString):
    """Custom type hh3cDLDPAuthenticationPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Hh3cDLDPAuthenticationPassword_Type.__name__ = "OctetString"
_Hh3cDLDPAuthenticationPassword_Object = MibScalar
hh3cDLDPAuthenticationPassword = _Hh3cDLDPAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 6),
    _Hh3cDLDPAuthenticationPassword_Type()
)
hh3cDLDPAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPAuthenticationPassword.setStatus("current")


class _Hh3cDLDPUnidirectionalShutdown_Type(Integer32):
    """Custom type hh3cDLDPUnidirectionalShutdown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Hh3cDLDPUnidirectionalShutdown_Type.__name__ = "Integer32"
_Hh3cDLDPUnidirectionalShutdown_Object = MibScalar
hh3cDLDPUnidirectionalShutdown = _Hh3cDLDPUnidirectionalShutdown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 1, 7),
    _Hh3cDLDPUnidirectionalShutdown_Type()
)
hh3cDLDPUnidirectionalShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPUnidirectionalShutdown.setStatus("current")
_Hh3cDLDPPortStateTable_Object = MibTable
hh3cDLDPPortStateTable = _Hh3cDLDPPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDLDPPortStateTable.setStatus("current")
_Hh3cDLDPPortStateEntry_Object = MibTableRow
hh3cDLDPPortStateEntry = _Hh3cDLDPPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 2, 1)
)
hh3cDLDPPortStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDLDPPortStateEntry.setStatus("current")


class _Hh3cDLDPPortState_Type(EnabledStatus):
    """Custom type hh3cDLDPPortState based on EnabledStatus"""


_Hh3cDLDPPortState_Object = MibTableColumn
hh3cDLDPPortState = _Hh3cDLDPPortState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 2, 1, 1),
    _Hh3cDLDPPortState_Type()
)
hh3cDLDPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPPortState.setStatus("current")
_Hh3cDLDPPortDLDPTable_Object = MibTable
hh3cDLDPPortDLDPTable = _Hh3cDLDPPortDLDPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDLDPPortDLDPTable.setStatus("current")
_Hh3cDLDPPortDLDPEntry_Object = MibTableRow
hh3cDLDPPortDLDPEntry = _Hh3cDLDPPortDLDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3, 1)
)
hh3cDLDPPortDLDPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDLDPPortDLDPEntry.setStatus("current")
_Hh3cDLDPPortDLDPState_Type = DLDPStatus
_Hh3cDLDPPortDLDPState_Object = MibTableColumn
hh3cDLDPPortDLDPState = _Hh3cDLDPPortDLDPState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3, 1, 1),
    _Hh3cDLDPPortDLDPState_Type()
)
hh3cDLDPPortDLDPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDLDPPortDLDPState.setStatus("current")


class _Hh3cDLDPLinkState_Type(Integer32):
    """Custom type hh3cDLDPLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("unknown", 3),
          ("up", 2))
    )


_Hh3cDLDPLinkState_Type.__name__ = "Integer32"
_Hh3cDLDPLinkState_Object = MibTableColumn
hh3cDLDPLinkState = _Hh3cDLDPLinkState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3, 1, 2),
    _Hh3cDLDPLinkState_Type()
)
hh3cDLDPLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDLDPLinkState.setStatus("current")
_Hh3cDLDPPortDLDPReset_Type = TruthValue
_Hh3cDLDPPortDLDPReset_Object = MibTableColumn
hh3cDLDPPortDLDPReset = _Hh3cDLDPPortDLDPReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 3, 1, 3),
    _Hh3cDLDPPortDLDPReset_Type()
)
hh3cDLDPPortDLDPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDLDPPortDLDPReset.setStatus("current")
_Hh3cDLDPNeighborTable_Object = MibTable
hh3cDLDPNeighborTable = _Hh3cDLDPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDLDPNeighborTable.setStatus("current")
_Hh3cDLDPNeighborEntry_Object = MibTableRow
hh3cDLDPNeighborEntry = _Hh3cDLDPNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1)
)
hh3cDLDPNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-DLDP-MIB", "hh3cDLDPNeighborBridgeMac"),
    (0, "HH3C-DLDP-MIB", "hh3cDLDPNeighborPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cDLDPNeighborEntry.setStatus("current")
_Hh3cDLDPNeighborBridgeMac_Type = MacAddress
_Hh3cDLDPNeighborBridgeMac_Object = MibTableColumn
hh3cDLDPNeighborBridgeMac = _Hh3cDLDPNeighborBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1, 1),
    _Hh3cDLDPNeighborBridgeMac_Type()
)
hh3cDLDPNeighborBridgeMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDLDPNeighborBridgeMac.setStatus("current")
_Hh3cDLDPNeighborPortIndex_Type = Integer32
_Hh3cDLDPNeighborPortIndex_Object = MibTableColumn
hh3cDLDPNeighborPortIndex = _Hh3cDLDPNeighborPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1, 2),
    _Hh3cDLDPNeighborPortIndex_Type()
)
hh3cDLDPNeighborPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDLDPNeighborPortIndex.setStatus("current")
_Hh3cDLDPNeighborState_Type = DLDPNeighborStatus
_Hh3cDLDPNeighborState_Object = MibTableColumn
hh3cDLDPNeighborState = _Hh3cDLDPNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1, 3),
    _Hh3cDLDPNeighborState_Type()
)
hh3cDLDPNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDLDPNeighborState.setStatus("current")
_Hh3cDLDPNeighborAgingTime_Type = Integer32
_Hh3cDLDPNeighborAgingTime_Object = MibTableColumn
hh3cDLDPNeighborAgingTime = _Hh3cDLDPNeighborAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 1, 4, 1, 4),
    _Hh3cDLDPNeighborAgingTime_Type()
)
hh3cDLDPNeighborAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDLDPNeighborAgingTime.setStatus("current")
_Hh3cDLDPTrapObject_ObjectIdentity = ObjectIdentity
hh3cDLDPTrapObject = _Hh3cDLDPTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 2)
)
_Hh3cDLDPNotification_ObjectIdentity = ObjectIdentity
hh3cDLDPNotification = _Hh3cDLDPNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 2, 1)
)

# Managed Objects groups


# Notification objects

hh3cDLDPUnidirectionalPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43, 2, 1, 1)
)
hh3cDLDPUnidirectionalPort.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hh3cDLDPUnidirectionalPort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DLDP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "DLDPStatus": DLDPStatus,
       "DLDPNeighborStatus": DLDPNeighborStatus,
       "hh3cDldp": hh3cDldp,
       "hh3cDLDPMibObject": hh3cDLDPMibObject,
       "hh3cDLDPConfigGroup": hh3cDLDPConfigGroup,
       "hh3cDLDPWorkMode": hh3cDLDPWorkMode,
       "hh3cDLDPSystemEnable": hh3cDLDPSystemEnable,
       "hh3cDLDPSystemReset": hh3cDLDPSystemReset,
       "hh3cDLDPInterval": hh3cDLDPInterval,
       "hh3cDLDPAuthenticationMode": hh3cDLDPAuthenticationMode,
       "hh3cDLDPAuthenticationPassword": hh3cDLDPAuthenticationPassword,
       "hh3cDLDPUnidirectionalShutdown": hh3cDLDPUnidirectionalShutdown,
       "hh3cDLDPPortStateTable": hh3cDLDPPortStateTable,
       "hh3cDLDPPortStateEntry": hh3cDLDPPortStateEntry,
       "hh3cDLDPPortState": hh3cDLDPPortState,
       "hh3cDLDPPortDLDPTable": hh3cDLDPPortDLDPTable,
       "hh3cDLDPPortDLDPEntry": hh3cDLDPPortDLDPEntry,
       "hh3cDLDPPortDLDPState": hh3cDLDPPortDLDPState,
       "hh3cDLDPLinkState": hh3cDLDPLinkState,
       "hh3cDLDPPortDLDPReset": hh3cDLDPPortDLDPReset,
       "hh3cDLDPNeighborTable": hh3cDLDPNeighborTable,
       "hh3cDLDPNeighborEntry": hh3cDLDPNeighborEntry,
       "hh3cDLDPNeighborBridgeMac": hh3cDLDPNeighborBridgeMac,
       "hh3cDLDPNeighborPortIndex": hh3cDLDPNeighborPortIndex,
       "hh3cDLDPNeighborState": hh3cDLDPNeighborState,
       "hh3cDLDPNeighborAgingTime": hh3cDLDPNeighborAgingTime,
       "hh3cDLDPTrapObject": hh3cDLDPTrapObject,
       "hh3cDLDPNotification": hh3cDLDPNotification,
       "hh3cDLDPUnidirectionalPort": hh3cDLDPUnidirectionalPort}
)
