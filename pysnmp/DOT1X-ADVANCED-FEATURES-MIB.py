# SNMP MIB module (DOT1X-ADVANCED-FEATURES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOT1X-ADVANCED-FEATURES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:13 2024
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

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

(switch,) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "switch")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dot1xAdvanced = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot1xPortControlMode(Integer32, TextualConvention):
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
        *(("auto", 2),
          ("forceAuthorized", 3),
          ("forceUnauthorized", 1),
          ("macBased", 4))
    )



class Dot1xSessionTerminationAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reauthenticate", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AgentGuestVlanConfigGroup_ObjectIdentity = ObjectIdentity
agentGuestVlanConfigGroup = _AgentGuestVlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 1)
)


class _AgentGuestVlanSupplMode_Type(Integer32):
    """Custom type agentGuestVlanSupplMode based on Integer32"""
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


_AgentGuestVlanSupplMode_Type.__name__ = "Integer32"
_AgentGuestVlanSupplMode_Object = MibScalar
agentGuestVlanSupplMode = _AgentGuestVlanSupplMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 1),
    _AgentGuestVlanSupplMode_Type()
)
agentGuestVlanSupplMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGuestVlanSupplMode.setStatus("current")
_AgentDot1xGuestVlanPortConfigTable_Object = MibTable
agentDot1xGuestVlanPortConfigTable = _AgentDot1xGuestVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    agentDot1xGuestVlanPortConfigTable.setStatus("current")
_AgentDot1xGuestVlanPortConfigEntry_Object = MibTableRow
agentDot1xGuestVlanPortConfigEntry = _AgentDot1xGuestVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 2, 1)
)
agentDot1xGuestVlanPortConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    agentDot1xGuestVlanPortConfigEntry.setStatus("current")


class _AgentDot1xGuestVlanId_Type(Unsigned32):
    """Custom type agentDot1xGuestVlanId based on Unsigned32"""
    defaultValue = 0


_AgentDot1xGuestVlanId_Object = MibTableColumn
agentDot1xGuestVlanId = _AgentDot1xGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 2, 1, 1),
    _AgentDot1xGuestVlanId_Type()
)
agentDot1xGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xGuestVlanId.setStatus("current")


class _AgentDot1xGuestVlanPeriod_Type(Unsigned32):
    """Custom type agentDot1xGuestVlanPeriod based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentDot1xGuestVlanPeriod_Type.__name__ = "Unsigned32"
_AgentDot1xGuestVlanPeriod_Object = MibTableColumn
agentDot1xGuestVlanPeriod = _AgentDot1xGuestVlanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 2, 1, 2),
    _AgentDot1xGuestVlanPeriod_Type()
)
agentDot1xGuestVlanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xGuestVlanPeriod.setStatus("current")
_AgentDot1xEnhancementConfigGroup_ObjectIdentity = ObjectIdentity
agentDot1xEnhancementConfigGroup = _AgentDot1xEnhancementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 2)
)


class _AgentDot1xRadiusVlanAssignment_Type(Integer32):
    """Custom type agentDot1xRadiusVlanAssignment based on Integer32"""
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


_AgentDot1xRadiusVlanAssignment_Type.__name__ = "Integer32"
_AgentDot1xRadiusVlanAssignment_Object = MibScalar
agentDot1xRadiusVlanAssignment = _AgentDot1xRadiusVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 2, 1),
    _AgentDot1xRadiusVlanAssignment_Type()
)
agentDot1xRadiusVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xRadiusVlanAssignment.setStatus("current")


class _AgentDot1xDynamicVlanCreationMode_Type(Integer32):
    """Custom type agentDot1xDynamicVlanCreationMode based on Integer32"""
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


_AgentDot1xDynamicVlanCreationMode_Type.__name__ = "Integer32"
_AgentDot1xDynamicVlanCreationMode_Object = MibScalar
agentDot1xDynamicVlanCreationMode = _AgentDot1xDynamicVlanCreationMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 2, 2),
    _AgentDot1xDynamicVlanCreationMode_Type()
)
agentDot1xDynamicVlanCreationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xDynamicVlanCreationMode.setStatus("current")
_AgentDot1xClientGroup_ObjectIdentity = ObjectIdentity
agentDot1xClientGroup = _AgentDot1xClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3)
)
_AgentDot1xClientTable_Object = MibTable
agentDot1xClientTable = _AgentDot1xClientTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1)
)
if mibBuilder.loadTexts:
    agentDot1xClientTable.setStatus("current")
_AgentDot1xClientEntry_Object = MibTableRow
agentDot1xClientEntry = _AgentDot1xClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1)
)
agentDot1xClientEntry.setIndexNames(
    (0, "DOT1X-ADVANCED-FEATURES-MIB", "agentDot1xClientLogicalInterface"),
)
if mibBuilder.loadTexts:
    agentDot1xClientEntry.setStatus("current")
_AgentDot1xClientLogicalInterface_Type = Unsigned32
_AgentDot1xClientLogicalInterface_Object = MibTableColumn
agentDot1xClientLogicalInterface = _AgentDot1xClientLogicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 1),
    _AgentDot1xClientLogicalInterface_Type()
)
agentDot1xClientLogicalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientLogicalInterface.setStatus("current")
_AgentDot1xClientInterface_Type = DisplayString
_AgentDot1xClientInterface_Object = MibTableColumn
agentDot1xClientInterface = _AgentDot1xClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 2),
    _AgentDot1xClientInterface_Type()
)
agentDot1xClientInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientInterface.setStatus("current")
_AgentDot1xClientUsername_Type = DisplayString
_AgentDot1xClientUsername_Object = MibTableColumn
agentDot1xClientUsername = _AgentDot1xClientUsername_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 3),
    _AgentDot1xClientUsername_Type()
)
agentDot1xClientUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientUsername.setStatus("current")
_AgentDot1xClientMacAddress_Type = PhysAddress
_AgentDot1xClientMacAddress_Object = MibTableColumn
agentDot1xClientMacAddress = _AgentDot1xClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 4),
    _AgentDot1xClientMacAddress_Type()
)
agentDot1xClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientMacAddress.setStatus("current")
_AgentDot1xClientSessionTime_Type = Unsigned32
_AgentDot1xClientSessionTime_Object = MibTableColumn
agentDot1xClientSessionTime = _AgentDot1xClientSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 5),
    _AgentDot1xClientSessionTime_Type()
)
agentDot1xClientSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientSessionTime.setStatus("current")
_AgentDot1xClientVlanId_Type = Unsigned32
_AgentDot1xClientVlanId_Object = MibTableColumn
agentDot1xClientVlanId = _AgentDot1xClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 6),
    _AgentDot1xClientVlanId_Type()
)
agentDot1xClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientVlanId.setStatus("current")


class _AgentDot1xClientVlanAssigned_Type(Integer32):
    """Custom type agentDot1xClientVlanAssigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("radius", 2),
          ("unauthenticated", 3))
    )


_AgentDot1xClientVlanAssigned_Type.__name__ = "Integer32"
_AgentDot1xClientVlanAssigned_Object = MibTableColumn
agentDot1xClientVlanAssigned = _AgentDot1xClientVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 7),
    _AgentDot1xClientVlanAssigned_Type()
)
agentDot1xClientVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientVlanAssigned.setStatus("current")
_AgentDot1xClientSessionTimeout_Type = Unsigned32
_AgentDot1xClientSessionTimeout_Object = MibTableColumn
agentDot1xClientSessionTimeout = _AgentDot1xClientSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 8),
    _AgentDot1xClientSessionTimeout_Type()
)
agentDot1xClientSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientSessionTimeout.setStatus("current")


class _AgentDot1xClientSessionTerminationAction_Type(Integer32):
    """Custom type agentDot1xClientSessionTerminationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("radius", 2))
    )


_AgentDot1xClientSessionTerminationAction_Type.__name__ = "Integer32"
_AgentDot1xClientSessionTerminationAction_Object = MibTableColumn
agentDot1xClientSessionTerminationAction = _AgentDot1xClientSessionTerminationAction_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 9),
    _AgentDot1xClientSessionTerminationAction_Type()
)
agentDot1xClientSessionTerminationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientSessionTerminationAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOT1X-ADVANCED-FEATURES-MIB",
    **{"Dot1xPortControlMode": Dot1xPortControlMode,
       "Dot1xSessionTerminationAction": Dot1xSessionTerminationAction,
       "dot1xAdvanced": dot1xAdvanced,
       "agentGuestVlanConfigGroup": agentGuestVlanConfigGroup,
       "agentGuestVlanSupplMode": agentGuestVlanSupplMode,
       "agentDot1xGuestVlanPortConfigTable": agentDot1xGuestVlanPortConfigTable,
       "agentDot1xGuestVlanPortConfigEntry": agentDot1xGuestVlanPortConfigEntry,
       "agentDot1xGuestVlanId": agentDot1xGuestVlanId,
       "agentDot1xGuestVlanPeriod": agentDot1xGuestVlanPeriod,
       "agentDot1xEnhancementConfigGroup": agentDot1xEnhancementConfigGroup,
       "agentDot1xRadiusVlanAssignment": agentDot1xRadiusVlanAssignment,
       "agentDot1xDynamicVlanCreationMode": agentDot1xDynamicVlanCreationMode,
       "agentDot1xClientGroup": agentDot1xClientGroup,
       "agentDot1xClientTable": agentDot1xClientTable,
       "agentDot1xClientEntry": agentDot1xClientEntry,
       "agentDot1xClientLogicalInterface": agentDot1xClientLogicalInterface,
       "agentDot1xClientInterface": agentDot1xClientInterface,
       "agentDot1xClientUsername": agentDot1xClientUsername,
       "agentDot1xClientMacAddress": agentDot1xClientMacAddress,
       "agentDot1xClientSessionTime": agentDot1xClientSessionTime,
       "agentDot1xClientVlanId": agentDot1xClientVlanId,
       "agentDot1xClientVlanAssigned": agentDot1xClientVlanAssigned,
       "agentDot1xClientSessionTimeout": agentDot1xClientSessionTimeout,
       "agentDot1xClientSessionTerminationAction": agentDot1xClientSessionTerminationAction}
)
