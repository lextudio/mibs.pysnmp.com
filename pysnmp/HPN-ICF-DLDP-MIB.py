# SNMP MIB module (HPN-ICF-DLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:45 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfDldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43)
)
hpnicfDldp.setRevisions(
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

_HpnicfDLDPMibObject_ObjectIdentity = ObjectIdentity
hpnicfDLDPMibObject = _HpnicfDLDPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1)
)
_HpnicfDLDPConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDLDPConfigGroup = _HpnicfDLDPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 1)
)


class _HpnicfDLDPWorkMode_Type(Integer32):
    """Custom type hpnicfDLDPWorkMode based on Integer32"""
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


_HpnicfDLDPWorkMode_Type.__name__ = "Integer32"
_HpnicfDLDPWorkMode_Object = MibScalar
hpnicfDLDPWorkMode = _HpnicfDLDPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 1, 1),
    _HpnicfDLDPWorkMode_Type()
)
hpnicfDLDPWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPWorkMode.setStatus("current")
_HpnicfDLDPSystemEnable_Type = TruthValue
_HpnicfDLDPSystemEnable_Object = MibScalar
hpnicfDLDPSystemEnable = _HpnicfDLDPSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 1, 2),
    _HpnicfDLDPSystemEnable_Type()
)
hpnicfDLDPSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPSystemEnable.setStatus("current")
_HpnicfDLDPSystemReset_Type = TruthValue
_HpnicfDLDPSystemReset_Object = MibScalar
hpnicfDLDPSystemReset = _HpnicfDLDPSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 1, 3),
    _HpnicfDLDPSystemReset_Type()
)
hpnicfDLDPSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPSystemReset.setStatus("current")


class _HpnicfDLDPInterval_Type(Integer32):
    """Custom type hpnicfDLDPInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfDLDPInterval_Type.__name__ = "Integer32"
_HpnicfDLDPInterval_Object = MibScalar
hpnicfDLDPInterval = _HpnicfDLDPInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 1, 4),
    _HpnicfDLDPInterval_Type()
)
hpnicfDLDPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPInterval.setStatus("current")


class _HpnicfDLDPAuthenticationMode_Type(Integer32):
    """Custom type hpnicfDLDPAuthenticationMode based on Integer32"""
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


_HpnicfDLDPAuthenticationMode_Type.__name__ = "Integer32"
_HpnicfDLDPAuthenticationMode_Object = MibScalar
hpnicfDLDPAuthenticationMode = _HpnicfDLDPAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 1, 5),
    _HpnicfDLDPAuthenticationMode_Type()
)
hpnicfDLDPAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPAuthenticationMode.setStatus("current")


class _HpnicfDLDPAuthenticationPassword_Type(OctetString):
    """Custom type hpnicfDLDPAuthenticationPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 53),
    )


_HpnicfDLDPAuthenticationPassword_Type.__name__ = "OctetString"
_HpnicfDLDPAuthenticationPassword_Object = MibScalar
hpnicfDLDPAuthenticationPassword = _HpnicfDLDPAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 1, 6),
    _HpnicfDLDPAuthenticationPassword_Type()
)
hpnicfDLDPAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPAuthenticationPassword.setStatus("current")


class _HpnicfDLDPUnidirectionalShutdown_Type(Integer32):
    """Custom type hpnicfDLDPUnidirectionalShutdown based on Integer32"""
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


_HpnicfDLDPUnidirectionalShutdown_Type.__name__ = "Integer32"
_HpnicfDLDPUnidirectionalShutdown_Object = MibScalar
hpnicfDLDPUnidirectionalShutdown = _HpnicfDLDPUnidirectionalShutdown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 1, 7),
    _HpnicfDLDPUnidirectionalShutdown_Type()
)
hpnicfDLDPUnidirectionalShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPUnidirectionalShutdown.setStatus("current")
_HpnicfDLDPPortStateTable_Object = MibTable
hpnicfDLDPPortStateTable = _HpnicfDLDPPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDLDPPortStateTable.setStatus("current")
_HpnicfDLDPPortStateEntry_Object = MibTableRow
hpnicfDLDPPortStateEntry = _HpnicfDLDPPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 2, 1)
)
hpnicfDLDPPortStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDLDPPortStateEntry.setStatus("current")


class _HpnicfDLDPPortState_Type(EnabledStatus):
    """Custom type hpnicfDLDPPortState based on EnabledStatus"""


_HpnicfDLDPPortState_Object = MibTableColumn
hpnicfDLDPPortState = _HpnicfDLDPPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 2, 1, 1),
    _HpnicfDLDPPortState_Type()
)
hpnicfDLDPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPPortState.setStatus("current")
_HpnicfDLDPPortDLDPTable_Object = MibTable
hpnicfDLDPPortDLDPTable = _HpnicfDLDPPortDLDPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDLDPPortDLDPTable.setStatus("current")
_HpnicfDLDPPortDLDPEntry_Object = MibTableRow
hpnicfDLDPPortDLDPEntry = _HpnicfDLDPPortDLDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 3, 1)
)
hpnicfDLDPPortDLDPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDLDPPortDLDPEntry.setStatus("current")
_HpnicfDLDPPortDLDPState_Type = DLDPStatus
_HpnicfDLDPPortDLDPState_Object = MibTableColumn
hpnicfDLDPPortDLDPState = _HpnicfDLDPPortDLDPState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 3, 1, 1),
    _HpnicfDLDPPortDLDPState_Type()
)
hpnicfDLDPPortDLDPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDLDPPortDLDPState.setStatus("current")


class _HpnicfDLDPLinkState_Type(Integer32):
    """Custom type hpnicfDLDPLinkState based on Integer32"""
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


_HpnicfDLDPLinkState_Type.__name__ = "Integer32"
_HpnicfDLDPLinkState_Object = MibTableColumn
hpnicfDLDPLinkState = _HpnicfDLDPLinkState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 3, 1, 2),
    _HpnicfDLDPLinkState_Type()
)
hpnicfDLDPLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDLDPLinkState.setStatus("current")
_HpnicfDLDPPortDLDPReset_Type = TruthValue
_HpnicfDLDPPortDLDPReset_Object = MibTableColumn
hpnicfDLDPPortDLDPReset = _HpnicfDLDPPortDLDPReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 3, 1, 3),
    _HpnicfDLDPPortDLDPReset_Type()
)
hpnicfDLDPPortDLDPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDLDPPortDLDPReset.setStatus("current")
_HpnicfDLDPNeighborTable_Object = MibTable
hpnicfDLDPNeighborTable = _HpnicfDLDPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDLDPNeighborTable.setStatus("current")
_HpnicfDLDPNeighborEntry_Object = MibTableRow
hpnicfDLDPNeighborEntry = _HpnicfDLDPNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 4, 1)
)
hpnicfDLDPNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DLDP-MIB", "hpnicfDLDPNeighborBridgeMac"),
    (0, "HPN-ICF-DLDP-MIB", "hpnicfDLDPNeighborPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDLDPNeighborEntry.setStatus("current")
_HpnicfDLDPNeighborBridgeMac_Type = MacAddress
_HpnicfDLDPNeighborBridgeMac_Object = MibTableColumn
hpnicfDLDPNeighborBridgeMac = _HpnicfDLDPNeighborBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 4, 1, 1),
    _HpnicfDLDPNeighborBridgeMac_Type()
)
hpnicfDLDPNeighborBridgeMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDLDPNeighborBridgeMac.setStatus("current")
_HpnicfDLDPNeighborPortIndex_Type = Integer32
_HpnicfDLDPNeighborPortIndex_Object = MibTableColumn
hpnicfDLDPNeighborPortIndex = _HpnicfDLDPNeighborPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 4, 1, 2),
    _HpnicfDLDPNeighborPortIndex_Type()
)
hpnicfDLDPNeighborPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDLDPNeighborPortIndex.setStatus("current")
_HpnicfDLDPNeighborState_Type = DLDPNeighborStatus
_HpnicfDLDPNeighborState_Object = MibTableColumn
hpnicfDLDPNeighborState = _HpnicfDLDPNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 4, 1, 3),
    _HpnicfDLDPNeighborState_Type()
)
hpnicfDLDPNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDLDPNeighborState.setStatus("current")
_HpnicfDLDPNeighborAgingTime_Type = Integer32
_HpnicfDLDPNeighborAgingTime_Object = MibTableColumn
hpnicfDLDPNeighborAgingTime = _HpnicfDLDPNeighborAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 1, 4, 1, 4),
    _HpnicfDLDPNeighborAgingTime_Type()
)
hpnicfDLDPNeighborAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDLDPNeighborAgingTime.setStatus("current")
_HpnicfDLDPTrapObject_ObjectIdentity = ObjectIdentity
hpnicfDLDPTrapObject = _HpnicfDLDPTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 2)
)
_HpnicfDLDPNotification_ObjectIdentity = ObjectIdentity
hpnicfDLDPNotification = _HpnicfDLDPNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 2, 1)
)

# Managed Objects groups


# Notification objects

hpnicfDLDPUnidirectionalPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43, 2, 1, 1)
)
hpnicfDLDPUnidirectionalPort.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpnicfDLDPUnidirectionalPort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DLDP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "DLDPStatus": DLDPStatus,
       "DLDPNeighborStatus": DLDPNeighborStatus,
       "hpnicfDldp": hpnicfDldp,
       "hpnicfDLDPMibObject": hpnicfDLDPMibObject,
       "hpnicfDLDPConfigGroup": hpnicfDLDPConfigGroup,
       "hpnicfDLDPWorkMode": hpnicfDLDPWorkMode,
       "hpnicfDLDPSystemEnable": hpnicfDLDPSystemEnable,
       "hpnicfDLDPSystemReset": hpnicfDLDPSystemReset,
       "hpnicfDLDPInterval": hpnicfDLDPInterval,
       "hpnicfDLDPAuthenticationMode": hpnicfDLDPAuthenticationMode,
       "hpnicfDLDPAuthenticationPassword": hpnicfDLDPAuthenticationPassword,
       "hpnicfDLDPUnidirectionalShutdown": hpnicfDLDPUnidirectionalShutdown,
       "hpnicfDLDPPortStateTable": hpnicfDLDPPortStateTable,
       "hpnicfDLDPPortStateEntry": hpnicfDLDPPortStateEntry,
       "hpnicfDLDPPortState": hpnicfDLDPPortState,
       "hpnicfDLDPPortDLDPTable": hpnicfDLDPPortDLDPTable,
       "hpnicfDLDPPortDLDPEntry": hpnicfDLDPPortDLDPEntry,
       "hpnicfDLDPPortDLDPState": hpnicfDLDPPortDLDPState,
       "hpnicfDLDPLinkState": hpnicfDLDPLinkState,
       "hpnicfDLDPPortDLDPReset": hpnicfDLDPPortDLDPReset,
       "hpnicfDLDPNeighborTable": hpnicfDLDPNeighborTable,
       "hpnicfDLDPNeighborEntry": hpnicfDLDPNeighborEntry,
       "hpnicfDLDPNeighborBridgeMac": hpnicfDLDPNeighborBridgeMac,
       "hpnicfDLDPNeighborPortIndex": hpnicfDLDPNeighborPortIndex,
       "hpnicfDLDPNeighborState": hpnicfDLDPNeighborState,
       "hpnicfDLDPNeighborAgingTime": hpnicfDLDPNeighborAgingTime,
       "hpnicfDLDPTrapObject": hpnicfDLDPTrapObject,
       "hpnicfDLDPNotification": hpnicfDLDPNotification,
       "hpnicfDLDPUnidirectionalPort": hpnicfDLDPUnidirectionalPort}
)
