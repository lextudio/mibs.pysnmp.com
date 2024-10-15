# SNMP MIB module (CHARACTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHARACTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:34 2024
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
 iso,
 mib_2,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "transmission")

(AutonomousType,
 DisplayString,
 InstancePointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "InstancePointer",
    "TextualConvention")


# MODULE-IDENTITY

char = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_CharNumber_Type = Integer32
_CharNumber_Object = MibScalar
charNumber = _CharNumber_Object(
    (1, 3, 6, 1, 2, 1, 19, 1),
    _CharNumber_Type()
)
charNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charNumber.setStatus("current")
_CharPortTable_Object = MibTable
charPortTable = _CharPortTable_Object(
    (1, 3, 6, 1, 2, 1, 19, 2)
)
if mibBuilder.loadTexts:
    charPortTable.setStatus("current")
_CharPortEntry_Object = MibTableRow
charPortEntry = _CharPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1)
)
charPortEntry.setIndexNames(
    (0, "CHARACTER-MIB", "charPortIndex"),
)
if mibBuilder.loadTexts:
    charPortEntry.setStatus("current")
_CharPortIndex_Type = PortIndex
_CharPortIndex_Object = MibTableColumn
charPortIndex = _CharPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 1),
    _CharPortIndex_Type()
)
charPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortIndex.setStatus("current")


class _CharPortName_Type(DisplayString):
    """Custom type charPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CharPortName_Type.__name__ = "DisplayString"
_CharPortName_Object = MibTableColumn
charPortName = _CharPortName_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 2),
    _CharPortName_Type()
)
charPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortName.setStatus("current")


class _CharPortType_Type(Integer32):
    """Custom type charPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("physical", 1),
          ("virtual", 2))
    )


_CharPortType_Type.__name__ = "Integer32"
_CharPortType_Object = MibTableColumn
charPortType = _CharPortType_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 3),
    _CharPortType_Type()
)
charPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortType.setStatus("current")
_CharPortHardware_Type = AutonomousType
_CharPortHardware_Object = MibTableColumn
charPortHardware = _CharPortHardware_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 4),
    _CharPortHardware_Type()
)
charPortHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortHardware.setStatus("current")


class _CharPortReset_Type(Integer32):
    """Custom type charPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_CharPortReset_Type.__name__ = "Integer32"
_CharPortReset_Object = MibTableColumn
charPortReset = _CharPortReset_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 5),
    _CharPortReset_Type()
)
charPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortReset.setStatus("current")


class _CharPortAdminStatus_Type(Integer32):
    """Custom type charPortAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("maintenance", 4),
          ("off", 3))
    )


_CharPortAdminStatus_Type.__name__ = "Integer32"
_CharPortAdminStatus_Object = MibTableColumn
charPortAdminStatus = _CharPortAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 6),
    _CharPortAdminStatus_Type()
)
charPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortAdminStatus.setStatus("current")


class _CharPortOperStatus_Type(Integer32):
    """Custom type charPortOperStatus based on Integer32"""
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
        *(("absent", 4),
          ("active", 5),
          ("down", 2),
          ("maintenance", 3),
          ("up", 1))
    )


_CharPortOperStatus_Type.__name__ = "Integer32"
_CharPortOperStatus_Object = MibTableColumn
charPortOperStatus = _CharPortOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 7),
    _CharPortOperStatus_Type()
)
charPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOperStatus.setStatus("current")
_CharPortLastChange_Type = TimeTicks
_CharPortLastChange_Object = MibTableColumn
charPortLastChange = _CharPortLastChange_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 8),
    _CharPortLastChange_Type()
)
charPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortLastChange.setStatus("current")


class _CharPortInFlowType_Type(Integer32):
    """Custom type charPortInFlowType based on Integer32"""
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
        *(("ctsRts", 4),
          ("dsrDtr", 5),
          ("hardware", 3),
          ("none", 1),
          ("xonXoff", 2))
    )


_CharPortInFlowType_Type.__name__ = "Integer32"
_CharPortInFlowType_Object = MibTableColumn
charPortInFlowType = _CharPortInFlowType_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 9),
    _CharPortInFlowType_Type()
)
charPortInFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortInFlowType.setStatus("deprecated")


class _CharPortOutFlowType_Type(Integer32):
    """Custom type charPortOutFlowType based on Integer32"""
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
        *(("ctsRts", 4),
          ("dsrDtr", 5),
          ("hardware", 3),
          ("none", 1),
          ("xonXoff", 2))
    )


_CharPortOutFlowType_Type.__name__ = "Integer32"
_CharPortOutFlowType_Object = MibTableColumn
charPortOutFlowType = _CharPortOutFlowType_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 10),
    _CharPortOutFlowType_Type()
)
charPortOutFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortOutFlowType.setStatus("deprecated")


class _CharPortInFlowState_Type(Integer32):
    """Custom type charPortInFlowState based on Integer32"""
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
        *(("go", 4),
          ("none", 1),
          ("stop", 3),
          ("unknown", 2))
    )


_CharPortInFlowState_Type.__name__ = "Integer32"
_CharPortInFlowState_Object = MibTableColumn
charPortInFlowState = _CharPortInFlowState_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 11),
    _CharPortInFlowState_Type()
)
charPortInFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortInFlowState.setStatus("current")


class _CharPortOutFlowState_Type(Integer32):
    """Custom type charPortOutFlowState based on Integer32"""
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
        *(("go", 4),
          ("none", 1),
          ("stop", 3),
          ("unknown", 2))
    )


_CharPortOutFlowState_Type.__name__ = "Integer32"
_CharPortOutFlowState_Object = MibTableColumn
charPortOutFlowState = _CharPortOutFlowState_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 12),
    _CharPortOutFlowState_Type()
)
charPortOutFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOutFlowState.setStatus("current")
_CharPortInCharacters_Type = Counter32
_CharPortInCharacters_Object = MibTableColumn
charPortInCharacters = _CharPortInCharacters_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 13),
    _CharPortInCharacters_Type()
)
charPortInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortInCharacters.setStatus("current")
_CharPortOutCharacters_Type = Counter32
_CharPortOutCharacters_Object = MibTableColumn
charPortOutCharacters = _CharPortOutCharacters_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 14),
    _CharPortOutCharacters_Type()
)
charPortOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOutCharacters.setStatus("current")


class _CharPortAdminOrigin_Type(Integer32):
    """Custom type charPortAdminOrigin based on Integer32"""
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
        *(("dynamic", 1),
          ("local", 3),
          ("network", 2),
          ("none", 4))
    )


_CharPortAdminOrigin_Type.__name__ = "Integer32"
_CharPortAdminOrigin_Object = MibTableColumn
charPortAdminOrigin = _CharPortAdminOrigin_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 15),
    _CharPortAdminOrigin_Type()
)
charPortAdminOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortAdminOrigin.setStatus("current")


class _CharPortSessionMaximum_Type(Integer32):
    """Custom type charPortSessionMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CharPortSessionMaximum_Type.__name__ = "Integer32"
_CharPortSessionMaximum_Object = MibTableColumn
charPortSessionMaximum = _CharPortSessionMaximum_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 16),
    _CharPortSessionMaximum_Type()
)
charPortSessionMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortSessionMaximum.setStatus("current")
_CharPortSessionNumber_Type = Gauge32
_CharPortSessionNumber_Object = MibTableColumn
charPortSessionNumber = _CharPortSessionNumber_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 17),
    _CharPortSessionNumber_Type()
)
charPortSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortSessionNumber.setStatus("current")


class _CharPortSessionIndex_Type(Integer32):
    """Custom type charPortSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CharPortSessionIndex_Type.__name__ = "Integer32"
_CharPortSessionIndex_Object = MibTableColumn
charPortSessionIndex = _CharPortSessionIndex_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 18),
    _CharPortSessionIndex_Type()
)
charPortSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortSessionIndex.setStatus("current")


class _CharPortInFlowTypes_Type(OctetString):
    """Custom type charPortInFlowTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CharPortInFlowTypes_Type.__name__ = "OctetString"
_CharPortInFlowTypes_Object = MibTableColumn
charPortInFlowTypes = _CharPortInFlowTypes_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 19),
    _CharPortInFlowTypes_Type()
)
charPortInFlowTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortInFlowTypes.setStatus("current")


class _CharPortOutFlowTypes_Type(OctetString):
    """Custom type charPortOutFlowTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CharPortOutFlowTypes_Type.__name__ = "OctetString"
_CharPortOutFlowTypes_Object = MibTableColumn
charPortOutFlowTypes = _CharPortOutFlowTypes_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 20),
    _CharPortOutFlowTypes_Type()
)
charPortOutFlowTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortOutFlowTypes.setStatus("current")
_CharPortLowerIfIndex_Type = InterfaceIndex
_CharPortLowerIfIndex_Object = MibTableColumn
charPortLowerIfIndex = _CharPortLowerIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 19, 2, 1, 21),
    _CharPortLowerIfIndex_Type()
)
charPortLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortLowerIfIndex.setStatus("current")
_CharSessTable_Object = MibTable
charSessTable = _CharSessTable_Object(
    (1, 3, 6, 1, 2, 1, 19, 3)
)
if mibBuilder.loadTexts:
    charSessTable.setStatus("current")
_CharSessEntry_Object = MibTableRow
charSessEntry = _CharSessEntry_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1)
)
charSessEntry.setIndexNames(
    (0, "CHARACTER-MIB", "charSessPortIndex"),
    (0, "CHARACTER-MIB", "charSessIndex"),
)
if mibBuilder.loadTexts:
    charSessEntry.setStatus("current")
_CharSessPortIndex_Type = PortIndex
_CharSessPortIndex_Object = MibTableColumn
charSessPortIndex = _CharSessPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 1),
    _CharSessPortIndex_Type()
)
charSessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessPortIndex.setStatus("current")


class _CharSessIndex_Type(Integer32):
    """Custom type charSessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CharSessIndex_Type.__name__ = "Integer32"
_CharSessIndex_Object = MibTableColumn
charSessIndex = _CharSessIndex_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 2),
    _CharSessIndex_Type()
)
charSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessIndex.setStatus("current")


class _CharSessKill_Type(Integer32):
    """Custom type charSessKill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_CharSessKill_Type.__name__ = "Integer32"
_CharSessKill_Object = MibTableColumn
charSessKill = _CharSessKill_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 3),
    _CharSessKill_Type()
)
charSessKill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charSessKill.setStatus("current")


class _CharSessState_Type(Integer32):
    """Custom type charSessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connecting", 1),
          ("disconnecting", 3))
    )


_CharSessState_Type.__name__ = "Integer32"
_CharSessState_Object = MibTableColumn
charSessState = _CharSessState_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 4),
    _CharSessState_Type()
)
charSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessState.setStatus("current")
_CharSessProtocol_Type = AutonomousType
_CharSessProtocol_Object = MibTableColumn
charSessProtocol = _CharSessProtocol_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 5),
    _CharSessProtocol_Type()
)
charSessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessProtocol.setStatus("current")


class _CharSessOperOrigin_Type(Integer32):
    """Custom type charSessOperOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("network", 2),
          ("unknown", 1))
    )


_CharSessOperOrigin_Type.__name__ = "Integer32"
_CharSessOperOrigin_Object = MibTableColumn
charSessOperOrigin = _CharSessOperOrigin_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 6),
    _CharSessOperOrigin_Type()
)
charSessOperOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessOperOrigin.setStatus("current")
_CharSessInCharacters_Type = Counter32
_CharSessInCharacters_Object = MibTableColumn
charSessInCharacters = _CharSessInCharacters_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 7),
    _CharSessInCharacters_Type()
)
charSessInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessInCharacters.setStatus("current")
_CharSessOutCharacters_Type = Counter32
_CharSessOutCharacters_Object = MibTableColumn
charSessOutCharacters = _CharSessOutCharacters_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 8),
    _CharSessOutCharacters_Type()
)
charSessOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessOutCharacters.setStatus("current")
_CharSessConnectionId_Type = InstancePointer
_CharSessConnectionId_Object = MibTableColumn
charSessConnectionId = _CharSessConnectionId_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 9),
    _CharSessConnectionId_Type()
)
charSessConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessConnectionId.setStatus("current")
_CharSessStartTime_Type = TimeTicks
_CharSessStartTime_Object = MibTableColumn
charSessStartTime = _CharSessStartTime_Object(
    (1, 3, 6, 1, 2, 1, 19, 3, 1, 10),
    _CharSessStartTime_Type()
)
charSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessStartTime.setStatus("current")
_WellKnownProtocols_ObjectIdentity = ObjectIdentity
wellKnownProtocols = _WellKnownProtocols_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 4)
)
_ProtocolOther_ObjectIdentity = ObjectIdentity
protocolOther = _ProtocolOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 4, 1)
)
_ProtocolTelnet_ObjectIdentity = ObjectIdentity
protocolTelnet = _ProtocolTelnet_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 4, 2)
)
_ProtocolRlogin_ObjectIdentity = ObjectIdentity
protocolRlogin = _ProtocolRlogin_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 4, 3)
)
_ProtocolLat_ObjectIdentity = ObjectIdentity
protocolLat = _ProtocolLat_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 4, 4)
)
_ProtocolX29_ObjectIdentity = ObjectIdentity
protocolX29 = _ProtocolX29_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 4, 5)
)
_ProtocolVtp_ObjectIdentity = ObjectIdentity
protocolVtp = _ProtocolVtp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 4, 6)
)
_CharConformance_ObjectIdentity = ObjectIdentity
charConformance = _CharConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 5)
)
_CharGroups_ObjectIdentity = ObjectIdentity
charGroups = _CharGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 5, 1)
)
_CharCompliances_ObjectIdentity = ObjectIdentity
charCompliances = _CharCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 19, 5, 2)
)

# Managed Objects groups

charGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 19, 5, 1, 1)
)
charGroup.setObjects(
      *(("CHARACTER-MIB", "charNumber"),
        ("CHARACTER-MIB", "charPortIndex"),
        ("CHARACTER-MIB", "charPortName"),
        ("CHARACTER-MIB", "charPortType"),
        ("CHARACTER-MIB", "charPortHardware"),
        ("CHARACTER-MIB", "charPortReset"),
        ("CHARACTER-MIB", "charPortAdminStatus"),
        ("CHARACTER-MIB", "charPortOperStatus"),
        ("CHARACTER-MIB", "charPortLastChange"),
        ("CHARACTER-MIB", "charPortInFlowState"),
        ("CHARACTER-MIB", "charPortOutFlowState"),
        ("CHARACTER-MIB", "charPortAdminOrigin"),
        ("CHARACTER-MIB", "charPortSessionMaximum"),
        ("CHARACTER-MIB", "charPortInFlowTypes"),
        ("CHARACTER-MIB", "charPortOutFlowTypes"),
        ("CHARACTER-MIB", "charPortInCharacters"),
        ("CHARACTER-MIB", "charPortOutCharacters"),
        ("CHARACTER-MIB", "charPortSessionNumber"),
        ("CHARACTER-MIB", "charPortSessionIndex"),
        ("CHARACTER-MIB", "charPortLowerIfIndex"),
        ("CHARACTER-MIB", "charSessPortIndex"),
        ("CHARACTER-MIB", "charSessIndex"),
        ("CHARACTER-MIB", "charSessKill"),
        ("CHARACTER-MIB", "charSessState"),
        ("CHARACTER-MIB", "charSessProtocol"),
        ("CHARACTER-MIB", "charSessOperOrigin"),
        ("CHARACTER-MIB", "charSessInCharacters"),
        ("CHARACTER-MIB", "charSessOutCharacters"),
        ("CHARACTER-MIB", "charSessConnectionId"),
        ("CHARACTER-MIB", "charSessStartTime"))
)
if mibBuilder.loadTexts:
    charGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

charCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 19, 5, 2, 1)
)
if mibBuilder.loadTexts:
    charCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHARACTER-MIB",
    **{"PortIndex": PortIndex,
       "char": char,
       "charNumber": charNumber,
       "charPortTable": charPortTable,
       "charPortEntry": charPortEntry,
       "charPortIndex": charPortIndex,
       "charPortName": charPortName,
       "charPortType": charPortType,
       "charPortHardware": charPortHardware,
       "charPortReset": charPortReset,
       "charPortAdminStatus": charPortAdminStatus,
       "charPortOperStatus": charPortOperStatus,
       "charPortLastChange": charPortLastChange,
       "charPortInFlowType": charPortInFlowType,
       "charPortOutFlowType": charPortOutFlowType,
       "charPortInFlowState": charPortInFlowState,
       "charPortOutFlowState": charPortOutFlowState,
       "charPortInCharacters": charPortInCharacters,
       "charPortOutCharacters": charPortOutCharacters,
       "charPortAdminOrigin": charPortAdminOrigin,
       "charPortSessionMaximum": charPortSessionMaximum,
       "charPortSessionNumber": charPortSessionNumber,
       "charPortSessionIndex": charPortSessionIndex,
       "charPortInFlowTypes": charPortInFlowTypes,
       "charPortOutFlowTypes": charPortOutFlowTypes,
       "charPortLowerIfIndex": charPortLowerIfIndex,
       "charSessTable": charSessTable,
       "charSessEntry": charSessEntry,
       "charSessPortIndex": charSessPortIndex,
       "charSessIndex": charSessIndex,
       "charSessKill": charSessKill,
       "charSessState": charSessState,
       "charSessProtocol": charSessProtocol,
       "charSessOperOrigin": charSessOperOrigin,
       "charSessInCharacters": charSessInCharacters,
       "charSessOutCharacters": charSessOutCharacters,
       "charSessConnectionId": charSessConnectionId,
       "charSessStartTime": charSessStartTime,
       "wellKnownProtocols": wellKnownProtocols,
       "protocolOther": protocolOther,
       "protocolTelnet": protocolTelnet,
       "protocolRlogin": protocolRlogin,
       "protocolLat": protocolLat,
       "protocolX29": protocolX29,
       "protocolVtp": protocolVtp,
       "charConformance": charConformance,
       "charGroups": charGroups,
       "charGroup": charGroup,
       "charCompliances": charCompliances,
       "charCompliance": charCompliance}
)
