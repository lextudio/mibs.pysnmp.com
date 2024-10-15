# SNMP MIB module (FASTPATH-DOT1X-ADVANCED-FEATURES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-DOT1X-ADVANCED-FEATURES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:49 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "BROADCOM-REF-MIB",
    "fastPath")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathdot1xAdvanced = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36)
)
fastPathdot1xAdvanced.setRevisions(
        ("2007-05-23 00:00",)
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

_AgentDot1xEnhancementConfigGroup_ObjectIdentity = ObjectIdentity
agentDot1xEnhancementConfigGroup = _AgentDot1xEnhancementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 1)
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 1, 1),
    _AgentDot1xRadiusVlanAssignment_Type()
)
agentDot1xRadiusVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xRadiusVlanAssignment.setStatus("current")
_AgentDot1xPortConfigGroup_ObjectIdentity = ObjectIdentity
agentDot1xPortConfigGroup = _AgentDot1xPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2)
)
_AgentDot1xPortConfigTable_Object = MibTable
agentDot1xPortConfigTable = _AgentDot1xPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1)
)
if mibBuilder.loadTexts:
    agentDot1xPortConfigTable.setStatus("current")
_AgentDot1xPortConfigEntry_Object = MibTableRow
agentDot1xPortConfigEntry = _AgentDot1xPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1)
)
agentDot1xPortConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    agentDot1xPortConfigEntry.setStatus("current")


class _AgentDot1xPortControlMode_Type(Dot1xPortControlMode):
    """Custom type agentDot1xPortControlMode based on Dot1xPortControlMode"""


_AgentDot1xPortControlMode_Object = MibTableColumn
agentDot1xPortControlMode = _AgentDot1xPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 1),
    _AgentDot1xPortControlMode_Type()
)
agentDot1xPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xPortControlMode.setStatus("current")


class _AgentDot1xGuestVlanId_Type(Unsigned32):
    """Custom type agentDot1xGuestVlanId based on Unsigned32"""
    defaultValue = 0


_AgentDot1xGuestVlanId_Object = MibTableColumn
agentDot1xGuestVlanId = _AgentDot1xGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 3),
    _AgentDot1xGuestVlanPeriod_Type()
)
agentDot1xGuestVlanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xGuestVlanPeriod.setStatus("current")


class _AgentDot1xUnauthenticatedVlan_Type(Unsigned32):
    """Custom type agentDot1xUnauthenticatedVlan based on Unsigned32"""
    defaultValue = 0


_AgentDot1xUnauthenticatedVlan_Object = MibTableColumn
agentDot1xUnauthenticatedVlan = _AgentDot1xUnauthenticatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 4),
    _AgentDot1xUnauthenticatedVlan_Type()
)
agentDot1xUnauthenticatedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xUnauthenticatedVlan.setStatus("current")
_AgentDot1xMaxUsers_Type = Unsigned32
_AgentDot1xMaxUsers_Object = MibTableColumn
agentDot1xMaxUsers = _AgentDot1xMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 5),
    _AgentDot1xMaxUsers_Type()
)
agentDot1xMaxUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xMaxUsers.setStatus("current")


class _AgentDot1xPortVlanAssigned_Type(Unsigned32):
    """Custom type agentDot1xPortVlanAssigned based on Unsigned32"""
    defaultValue = 0


_AgentDot1xPortVlanAssigned_Object = MibTableColumn
agentDot1xPortVlanAssigned = _AgentDot1xPortVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 6),
    _AgentDot1xPortVlanAssigned_Type()
)
agentDot1xPortVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xPortVlanAssigned.setStatus("current")


class _AgentDot1xPortVlanAssignedReason_Type(Integer32):
    """Custom type agentDot1xPortVlanAssignedReason based on Integer32"""
    defaultValue = 5

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
        *(("default", 1),
          ("guestVlan", 4),
          ("notAssigned", 5),
          ("radius", 2),
          ("unauthenticatedVlan", 3))
    )


_AgentDot1xPortVlanAssignedReason_Type.__name__ = "Integer32"
_AgentDot1xPortVlanAssignedReason_Object = MibTableColumn
agentDot1xPortVlanAssignedReason = _AgentDot1xPortVlanAssignedReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 7),
    _AgentDot1xPortVlanAssignedReason_Type()
)
agentDot1xPortVlanAssignedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xPortVlanAssignedReason.setStatus("current")
_AgentDot1xPortSessionTimeout_Type = Unsigned32
_AgentDot1xPortSessionTimeout_Object = MibTableColumn
agentDot1xPortSessionTimeout = _AgentDot1xPortSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 8),
    _AgentDot1xPortSessionTimeout_Type()
)
agentDot1xPortSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xPortSessionTimeout.setStatus("current")


class _AgentDot1xPortTerminationAction_Type(Dot1xSessionTerminationAction):
    """Custom type agentDot1xPortTerminationAction based on Dot1xSessionTerminationAction"""
    defaultValue = 1


_AgentDot1xPortTerminationAction_Object = MibTableColumn
agentDot1xPortTerminationAction = _AgentDot1xPortTerminationAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 9),
    _AgentDot1xPortTerminationAction_Type()
)
agentDot1xPortTerminationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xPortTerminationAction.setStatus("current")


class _AgentDot1xPortMABenabled_Type(Integer32):
    """Custom type agentDot1xPortMABenabled based on Integer32"""
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


_AgentDot1xPortMABenabled_Type.__name__ = "Integer32"
_AgentDot1xPortMABenabled_Object = MibTableColumn
agentDot1xPortMABenabled = _AgentDot1xPortMABenabled_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 10),
    _AgentDot1xPortMABenabled_Type()
)
agentDot1xPortMABenabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xPortMABenabled.setStatus("current")


class _AgentDot1xPortMABenabledOperational_Type(Integer32):
    """Custom type agentDot1xPortMABenabledOperational based on Integer32"""
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


_AgentDot1xPortMABenabledOperational_Type.__name__ = "Integer32"
_AgentDot1xPortMABenabledOperational_Object = MibTableColumn
agentDot1xPortMABenabledOperational = _AgentDot1xPortMABenabledOperational_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 11),
    _AgentDot1xPortMABenabledOperational_Type()
)
agentDot1xPortMABenabledOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xPortMABenabledOperational.setStatus("current")
_AgentDot1xClientConfigGroup_ObjectIdentity = ObjectIdentity
agentDot1xClientConfigGroup = _AgentDot1xClientConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3)
)
_AgentDot1xClientConfigTable_Object = MibTable
agentDot1xClientConfigTable = _AgentDot1xClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1)
)
if mibBuilder.loadTexts:
    agentDot1xClientConfigTable.setStatus("current")
_AgentDot1xClientConfigEntry_Object = MibTableRow
agentDot1xClientConfigEntry = _AgentDot1xClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1)
)
agentDot1xClientConfigEntry.setIndexNames(
    (0, "FASTPATH-DOT1X-ADVANCED-FEATURES-MIB", "agentDot1xClientMacAddress"),
)
if mibBuilder.loadTexts:
    agentDot1xClientConfigEntry.setStatus("current")
_AgentDot1xClientMacAddress_Type = MacAddress
_AgentDot1xClientMacAddress_Object = MibTableColumn
agentDot1xClientMacAddress = _AgentDot1xClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 1),
    _AgentDot1xClientMacAddress_Type()
)
agentDot1xClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientMacAddress.setStatus("current")
_AgentDot1xLogicalPort_Type = Unsigned32
_AgentDot1xLogicalPort_Object = MibTableColumn
agentDot1xLogicalPort = _AgentDot1xLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 2),
    _AgentDot1xLogicalPort_Type()
)
agentDot1xLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xLogicalPort.setStatus("current")
_AgentDot1xInterface_Type = Unsigned32
_AgentDot1xInterface_Object = MibTableColumn
agentDot1xInterface = _AgentDot1xInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 3),
    _AgentDot1xInterface_Type()
)
agentDot1xInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xInterface.setStatus("current")


class _AgentDot1xClientAuthPAEstate_Type(Integer32):
    """Custom type agentDot1xClientAuthPAEstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("initialize", 1))
    )


_AgentDot1xClientAuthPAEstate_Type.__name__ = "Integer32"
_AgentDot1xClientAuthPAEstate_Object = MibTableColumn
agentDot1xClientAuthPAEstate = _AgentDot1xClientAuthPAEstate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 4),
    _AgentDot1xClientAuthPAEstate_Type()
)
agentDot1xClientAuthPAEstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientAuthPAEstate.setStatus("current")


class _AgentDot1xClientBackendState_Type(Integer32):
    """Custom type agentDot1xClientBackendState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fail", 4),
          ("idle", 6),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_AgentDot1xClientBackendState_Type.__name__ = "Integer32"
_AgentDot1xClientBackendState_Object = MibTableColumn
agentDot1xClientBackendState = _AgentDot1xClientBackendState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 5),
    _AgentDot1xClientBackendState_Type()
)
agentDot1xClientBackendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientBackendState.setStatus("current")
_AgentDot1xClientUserName_Type = DisplayString
_AgentDot1xClientUserName_Object = MibTableColumn
agentDot1xClientUserName = _AgentDot1xClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 6),
    _AgentDot1xClientUserName_Type()
)
agentDot1xClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientUserName.setStatus("current")
_AgentDot1xClientSessionTime_Type = Unsigned32
_AgentDot1xClientSessionTime_Object = MibTableColumn
agentDot1xClientSessionTime = _AgentDot1xClientSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 7),
    _AgentDot1xClientSessionTime_Type()
)
agentDot1xClientSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientSessionTime.setStatus("current")
_AgentDot1xClientFilterID_Type = DisplayString
_AgentDot1xClientFilterID_Object = MibTableColumn
agentDot1xClientFilterID = _AgentDot1xClientFilterID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 8),
    _AgentDot1xClientFilterID_Type()
)
agentDot1xClientFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientFilterID.setStatus("current")
_AgentDot1xClientVlanAssigned_Type = Unsigned32
_AgentDot1xClientVlanAssigned_Object = MibTableColumn
agentDot1xClientVlanAssigned = _AgentDot1xClientVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 9),
    _AgentDot1xClientVlanAssigned_Type()
)
agentDot1xClientVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientVlanAssigned.setStatus("current")


class _AgentDot1xClientVlanAssignedReason_Type(Integer32):
    """Custom type agentDot1xClientVlanAssignedReason based on Integer32"""
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
        *(("default", 1),
          ("invalid", 4),
          ("radius", 2),
          ("unauthenticatedVlan", 3))
    )


_AgentDot1xClientVlanAssignedReason_Type.__name__ = "Integer32"
_AgentDot1xClientVlanAssignedReason_Object = MibTableColumn
agentDot1xClientVlanAssignedReason = _AgentDot1xClientVlanAssignedReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 10),
    _AgentDot1xClientVlanAssignedReason_Type()
)
agentDot1xClientVlanAssignedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientVlanAssignedReason.setStatus("current")
_AgentDot1xClientSessionTimeout_Type = Unsigned32
_AgentDot1xClientSessionTimeout_Object = MibTableColumn
agentDot1xClientSessionTimeout = _AgentDot1xClientSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 11),
    _AgentDot1xClientSessionTimeout_Type()
)
agentDot1xClientSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientSessionTimeout.setStatus("current")
_AgentDot1xClientTerminationAction_Type = Dot1xSessionTerminationAction
_AgentDot1xClientTerminationAction_Object = MibTableColumn
agentDot1xClientTerminationAction = _AgentDot1xClientTerminationAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 12),
    _AgentDot1xClientTerminationAction_Type()
)
agentDot1xClientTerminationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1xClientTerminationAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-DOT1X-ADVANCED-FEATURES-MIB",
    **{"Dot1xPortControlMode": Dot1xPortControlMode,
       "Dot1xSessionTerminationAction": Dot1xSessionTerminationAction,
       "fastPathdot1xAdvanced": fastPathdot1xAdvanced,
       "agentDot1xEnhancementConfigGroup": agentDot1xEnhancementConfigGroup,
       "agentDot1xRadiusVlanAssignment": agentDot1xRadiusVlanAssignment,
       "agentDot1xPortConfigGroup": agentDot1xPortConfigGroup,
       "agentDot1xPortConfigTable": agentDot1xPortConfigTable,
       "agentDot1xPortConfigEntry": agentDot1xPortConfigEntry,
       "agentDot1xPortControlMode": agentDot1xPortControlMode,
       "agentDot1xGuestVlanId": agentDot1xGuestVlanId,
       "agentDot1xGuestVlanPeriod": agentDot1xGuestVlanPeriod,
       "agentDot1xUnauthenticatedVlan": agentDot1xUnauthenticatedVlan,
       "agentDot1xMaxUsers": agentDot1xMaxUsers,
       "agentDot1xPortVlanAssigned": agentDot1xPortVlanAssigned,
       "agentDot1xPortVlanAssignedReason": agentDot1xPortVlanAssignedReason,
       "agentDot1xPortSessionTimeout": agentDot1xPortSessionTimeout,
       "agentDot1xPortTerminationAction": agentDot1xPortTerminationAction,
       "agentDot1xPortMABenabled": agentDot1xPortMABenabled,
       "agentDot1xPortMABenabledOperational": agentDot1xPortMABenabledOperational,
       "agentDot1xClientConfigGroup": agentDot1xClientConfigGroup,
       "agentDot1xClientConfigTable": agentDot1xClientConfigTable,
       "agentDot1xClientConfigEntry": agentDot1xClientConfigEntry,
       "agentDot1xClientMacAddress": agentDot1xClientMacAddress,
       "agentDot1xLogicalPort": agentDot1xLogicalPort,
       "agentDot1xInterface": agentDot1xInterface,
       "agentDot1xClientAuthPAEstate": agentDot1xClientAuthPAEstate,
       "agentDot1xClientBackendState": agentDot1xClientBackendState,
       "agentDot1xClientUserName": agentDot1xClientUserName,
       "agentDot1xClientSessionTime": agentDot1xClientSessionTime,
       "agentDot1xClientFilterID": agentDot1xClientFilterID,
       "agentDot1xClientVlanAssigned": agentDot1xClientVlanAssigned,
       "agentDot1xClientVlanAssignedReason": agentDot1xClientVlanAssignedReason,
       "agentDot1xClientSessionTimeout": agentDot1xClientSessionTimeout,
       "agentDot1xClientTerminationAction": agentDot1xClientTerminationAction}
)
