# SNMP MIB module (FSM7326-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSM7326-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:36 2024
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

(fsm7326,) = mibBuilder.importSymbols(
    "FSM7326-REF-MIB",
    "fsm7326")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsm7326Radius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8)
)
fsm7326Radius.setRevisions(
        ("2003-11-10 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentRadiusConfigGroup_ObjectIdentity = ObjectIdentity
agentRadiusConfigGroup = _AgentRadiusConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1)
)


class _AgentRadiusMaxTransmit_Type(Unsigned32):
    """Custom type agentRadiusMaxTransmit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AgentRadiusMaxTransmit_Type.__name__ = "Unsigned32"
_AgentRadiusMaxTransmit_Object = MibScalar
agentRadiusMaxTransmit = _AgentRadiusMaxTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 1),
    _AgentRadiusMaxTransmit_Type()
)
agentRadiusMaxTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusMaxTransmit.setStatus("current")


class _AgentRadiusTimeout_Type(Unsigned32):
    """Custom type agentRadiusTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentRadiusTimeout_Type.__name__ = "Unsigned32"
_AgentRadiusTimeout_Object = MibScalar
agentRadiusTimeout = _AgentRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 2),
    _AgentRadiusTimeout_Type()
)
agentRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusTimeout.setStatus("current")


class _AgentRadiusAccountingMode_Type(Integer32):
    """Custom type agentRadiusAccountingMode based on Integer32"""
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


_AgentRadiusAccountingMode_Type.__name__ = "Integer32"
_AgentRadiusAccountingMode_Object = MibScalar
agentRadiusAccountingMode = _AgentRadiusAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 3),
    _AgentRadiusAccountingMode_Type()
)
agentRadiusAccountingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingMode.setStatus("current")


class _AgentRadiusStatsClear_Type(Integer32):
    """Custom type agentRadiusStatsClear based on Integer32"""
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


_AgentRadiusStatsClear_Type.__name__ = "Integer32"
_AgentRadiusStatsClear_Object = MibScalar
agentRadiusStatsClear = _AgentRadiusStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 4),
    _AgentRadiusStatsClear_Type()
)
agentRadiusStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusStatsClear.setStatus("current")


class _AgentRadiusAccountingIndexNextValid_Type(Integer32):
    """Custom type agentRadiusAccountingIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentRadiusAccountingIndexNextValid_Type.__name__ = "Integer32"
_AgentRadiusAccountingIndexNextValid_Object = MibScalar
agentRadiusAccountingIndexNextValid = _AgentRadiusAccountingIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 5),
    _AgentRadiusAccountingIndexNextValid_Type()
)
agentRadiusAccountingIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAccountingIndexNextValid.setStatus("current")
_AgentRadiusAccountingConfigTable_Object = MibTable
agentRadiusAccountingConfigTable = _AgentRadiusAccountingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 6)
)
if mibBuilder.loadTexts:
    agentRadiusAccountingConfigTable.setStatus("current")
_AgentRadiusAccountingConfigEntry_Object = MibTableRow
agentRadiusAccountingConfigEntry = _AgentRadiusAccountingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 6, 1)
)
agentRadiusAccountingConfigEntry.setIndexNames(
    (0, "FSM7326-RADIUS-MIB", "agentRadiusAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    agentRadiusAccountingConfigEntry.setStatus("current")


class _AgentRadiusAccountingServerIndex_Type(Integer32):
    """Custom type agentRadiusAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusAccountingServerIndex_Type.__name__ = "Integer32"
_AgentRadiusAccountingServerIndex_Object = MibTableColumn
agentRadiusAccountingServerIndex = _AgentRadiusAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 6, 1, 1),
    _AgentRadiusAccountingServerIndex_Type()
)
agentRadiusAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerIndex.setStatus("current")
_AgentRadiusAccountingServerAddress_Type = IpAddress
_AgentRadiusAccountingServerAddress_Object = MibTableColumn
agentRadiusAccountingServerAddress = _AgentRadiusAccountingServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 6, 1, 2),
    _AgentRadiusAccountingServerAddress_Type()
)
agentRadiusAccountingServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerAddress.setStatus("current")


class _AgentRadiusAccountingPort_Type(Unsigned32):
    """Custom type agentRadiusAccountingPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentRadiusAccountingPort_Type.__name__ = "Unsigned32"
_AgentRadiusAccountingPort_Object = MibTableColumn
agentRadiusAccountingPort = _AgentRadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 6, 1, 3),
    _AgentRadiusAccountingPort_Type()
)
agentRadiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingPort.setStatus("current")


class _AgentRadiusAccountingSecret_Type(DisplayString):
    """Custom type agentRadiusAccountingSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AgentRadiusAccountingSecret_Type.__name__ = "DisplayString"
_AgentRadiusAccountingSecret_Object = MibTableColumn
agentRadiusAccountingSecret = _AgentRadiusAccountingSecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 6, 1, 4),
    _AgentRadiusAccountingSecret_Type()
)
agentRadiusAccountingSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingSecret.setStatus("current")
_AgentRadiusAccountingStatus_Type = RowStatus
_AgentRadiusAccountingStatus_Object = MibTableColumn
agentRadiusAccountingStatus = _AgentRadiusAccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 6, 1, 5),
    _AgentRadiusAccountingStatus_Type()
)
agentRadiusAccountingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingStatus.setStatus("current")


class _AgentRadiusServerIndexNextValid_Type(Integer32):
    """Custom type agentRadiusServerIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentRadiusServerIndexNextValid_Type.__name__ = "Integer32"
_AgentRadiusServerIndexNextValid_Object = MibScalar
agentRadiusServerIndexNextValid = _AgentRadiusServerIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 7),
    _AgentRadiusServerIndexNextValid_Type()
)
agentRadiusServerIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerIndexNextValid.setStatus("current")
_AgentRadiusServerConfigTable_Object = MibTable
agentRadiusServerConfigTable = _AgentRadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8)
)
if mibBuilder.loadTexts:
    agentRadiusServerConfigTable.setStatus("current")
_AgentRadiusServerConfigEntry_Object = MibTableRow
agentRadiusServerConfigEntry = _AgentRadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1)
)
agentRadiusServerConfigEntry.setIndexNames(
    (0, "FSM7326-RADIUS-MIB", "agentRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    agentRadiusServerConfigEntry.setStatus("current")


class _AgentRadiusServerIndex_Type(Integer32):
    """Custom type agentRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusServerIndex_Type.__name__ = "Integer32"
_AgentRadiusServerIndex_Object = MibTableColumn
agentRadiusServerIndex = _AgentRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1, 1),
    _AgentRadiusServerIndex_Type()
)
agentRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRadiusServerIndex.setStatus("current")
_AgentRadiusServerAddress_Type = IpAddress
_AgentRadiusServerAddress_Object = MibTableColumn
agentRadiusServerAddress = _AgentRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1, 2),
    _AgentRadiusServerAddress_Type()
)
agentRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerAddress.setStatus("current")


class _AgentRadiusServerPort_Type(Unsigned32):
    """Custom type agentRadiusServerPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentRadiusServerPort_Type.__name__ = "Unsigned32"
_AgentRadiusServerPort_Object = MibTableColumn
agentRadiusServerPort = _AgentRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1, 3),
    _AgentRadiusServerPort_Type()
)
agentRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerPort.setStatus("current")


class _AgentRadiusServerSecret_Type(DisplayString):
    """Custom type agentRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AgentRadiusServerSecret_Type.__name__ = "DisplayString"
_AgentRadiusServerSecret_Object = MibTableColumn
agentRadiusServerSecret = _AgentRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1, 4),
    _AgentRadiusServerSecret_Type()
)
agentRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerSecret.setStatus("current")


class _AgentRadiusServerPrimaryMode_Type(Integer32):
    """Custom type agentRadiusServerPrimaryMode based on Integer32"""
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


_AgentRadiusServerPrimaryMode_Type.__name__ = "Integer32"
_AgentRadiusServerPrimaryMode_Object = MibTableColumn
agentRadiusServerPrimaryMode = _AgentRadiusServerPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1, 5),
    _AgentRadiusServerPrimaryMode_Type()
)
agentRadiusServerPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerPrimaryMode.setStatus("current")


class _AgentRadiusServerCurrentMode_Type(Integer32):
    """Custom type agentRadiusServerCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AgentRadiusServerCurrentMode_Type.__name__ = "Integer32"
_AgentRadiusServerCurrentMode_Object = MibTableColumn
agentRadiusServerCurrentMode = _AgentRadiusServerCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1, 6),
    _AgentRadiusServerCurrentMode_Type()
)
agentRadiusServerCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerCurrentMode.setStatus("current")


class _AgentRadiusServerMsgAuth_Type(Integer32):
    """Custom type agentRadiusServerMsgAuth based on Integer32"""
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


_AgentRadiusServerMsgAuth_Type.__name__ = "Integer32"
_AgentRadiusServerMsgAuth_Object = MibTableColumn
agentRadiusServerMsgAuth = _AgentRadiusServerMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1, 7),
    _AgentRadiusServerMsgAuth_Type()
)
agentRadiusServerMsgAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerMsgAuth.setStatus("current")
_AgentRadiusServerStatus_Type = RowStatus
_AgentRadiusServerStatus_Object = MibTableColumn
agentRadiusServerStatus = _AgentRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 8, 1, 8, 1, 8),
    _AgentRadiusServerStatus_Type()
)
agentRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSM7326-RADIUS-MIB",
    **{"fsm7326Radius": fsm7326Radius,
       "agentRadiusConfigGroup": agentRadiusConfigGroup,
       "agentRadiusMaxTransmit": agentRadiusMaxTransmit,
       "agentRadiusTimeout": agentRadiusTimeout,
       "agentRadiusAccountingMode": agentRadiusAccountingMode,
       "agentRadiusStatsClear": agentRadiusStatsClear,
       "agentRadiusAccountingIndexNextValid": agentRadiusAccountingIndexNextValid,
       "agentRadiusAccountingConfigTable": agentRadiusAccountingConfigTable,
       "agentRadiusAccountingConfigEntry": agentRadiusAccountingConfigEntry,
       "agentRadiusAccountingServerIndex": agentRadiusAccountingServerIndex,
       "agentRadiusAccountingServerAddress": agentRadiusAccountingServerAddress,
       "agentRadiusAccountingPort": agentRadiusAccountingPort,
       "agentRadiusAccountingSecret": agentRadiusAccountingSecret,
       "agentRadiusAccountingStatus": agentRadiusAccountingStatus,
       "agentRadiusServerIndexNextValid": agentRadiusServerIndexNextValid,
       "agentRadiusServerConfigTable": agentRadiusServerConfigTable,
       "agentRadiusServerConfigEntry": agentRadiusServerConfigEntry,
       "agentRadiusServerIndex": agentRadiusServerIndex,
       "agentRadiusServerAddress": agentRadiusServerAddress,
       "agentRadiusServerPort": agentRadiusServerPort,
       "agentRadiusServerSecret": agentRadiusServerSecret,
       "agentRadiusServerPrimaryMode": agentRadiusServerPrimaryMode,
       "agentRadiusServerCurrentMode": agentRadiusServerCurrentMode,
       "agentRadiusServerMsgAuth": agentRadiusServerMsgAuth,
       "agentRadiusServerStatus": agentRadiusServerStatus}
)
