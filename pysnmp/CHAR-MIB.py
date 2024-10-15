# SNMP MIB module (CHAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:33 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class AutonomousType(ObjectIdentifier):
    """Custom type AutonomousType based on ObjectIdentifier"""




class InstancePointer(ObjectIdentifier):
    """Custom type InstancePointer based on ObjectIdentifier"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Char_ObjectIdentity = ObjectIdentity
char = _Char_ObjectIdentity(
    (1, 3, 6, 1, 3, 19)
)
_CharNumber_Type = Integer32
_CharNumber_Object = MibScalar
charNumber = _CharNumber_Object(
    (1, 3, 6, 1, 3, 19, 1),
    _CharNumber_Type()
)
charNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charNumber.setStatus("mandatory")
_CharPortTable_Object = MibTable
charPortTable = _CharPortTable_Object(
    (1, 3, 6, 1, 3, 19, 2)
)
if mibBuilder.loadTexts:
    charPortTable.setStatus("mandatory")
_CharPortEntry_Object = MibTableRow
charPortEntry = _CharPortEntry_Object(
    (1, 3, 6, 1, 3, 19, 2, 1)
)
charPortEntry.setIndexNames(
    (0, "CHAR-MIB", "charPortIndex"),
)
if mibBuilder.loadTexts:
    charPortEntry.setStatus("mandatory")
_CharPortIndex_Type = Integer32
_CharPortIndex_Object = MibTableColumn
charPortIndex = _CharPortIndex_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 1),
    _CharPortIndex_Type()
)
charPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortIndex.setStatus("mandatory")


class _CharPortName_Type(DisplayString):
    """Custom type charPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CharPortName_Type.__name__ = "DisplayString"
_CharPortName_Object = MibTableColumn
charPortName = _CharPortName_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 2),
    _CharPortName_Type()
)
charPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortName.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 3),
    _CharPortType_Type()
)
charPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortType.setStatus("mandatory")
_CharPortHardware_Type = AutonomousType
_CharPortHardware_Object = MibTableColumn
charPortHardware = _CharPortHardware_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 4),
    _CharPortHardware_Type()
)
charPortHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortHardware.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 5),
    _CharPortReset_Type()
)
charPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortReset.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 6),
    _CharPortAdminStatus_Type()
)
charPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortAdminStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 7),
    _CharPortOperStatus_Type()
)
charPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOperStatus.setStatus("mandatory")
_CharPortLastChange_Type = TimeTicks
_CharPortLastChange_Object = MibTableColumn
charPortLastChange = _CharPortLastChange_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 8),
    _CharPortLastChange_Type()
)
charPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortLastChange.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 9),
    _CharPortInFlowType_Type()
)
charPortInFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortInFlowType.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 10),
    _CharPortOutFlowType_Type()
)
charPortOutFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortOutFlowType.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 11),
    _CharPortInFlowState_Type()
)
charPortInFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortInFlowState.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 12),
    _CharPortOutFlowState_Type()
)
charPortOutFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOutFlowState.setStatus("mandatory")
_CharPortInCharacters_Type = Counter32
_CharPortInCharacters_Object = MibTableColumn
charPortInCharacters = _CharPortInCharacters_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 13),
    _CharPortInCharacters_Type()
)
charPortInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortInCharacters.setStatus("mandatory")
_CharPortOutCharacters_Type = Counter32
_CharPortOutCharacters_Object = MibTableColumn
charPortOutCharacters = _CharPortOutCharacters_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 14),
    _CharPortOutCharacters_Type()
)
charPortOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOutCharacters.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 2, 1, 15),
    _CharPortAdminOrigin_Type()
)
charPortAdminOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortAdminOrigin.setStatus("mandatory")
_CharPortSessionMaximum_Type = Integer32
_CharPortSessionMaximum_Object = MibTableColumn
charPortSessionMaximum = _CharPortSessionMaximum_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 16),
    _CharPortSessionMaximum_Type()
)
charPortSessionMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortSessionMaximum.setStatus("mandatory")
_CharPortSessionNumber_Type = Gauge32
_CharPortSessionNumber_Object = MibTableColumn
charPortSessionNumber = _CharPortSessionNumber_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 17),
    _CharPortSessionNumber_Type()
)
charPortSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortSessionNumber.setStatus("mandatory")
_CharPortSessionIndex_Type = Integer32
_CharPortSessionIndex_Object = MibTableColumn
charPortSessionIndex = _CharPortSessionIndex_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 18),
    _CharPortSessionIndex_Type()
)
charPortSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortSessionIndex.setStatus("mandatory")
_CharSessTable_Object = MibTable
charSessTable = _CharSessTable_Object(
    (1, 3, 6, 1, 3, 19, 3)
)
if mibBuilder.loadTexts:
    charSessTable.setStatus("mandatory")
_CharSessEntry_Object = MibTableRow
charSessEntry = _CharSessEntry_Object(
    (1, 3, 6, 1, 3, 19, 3, 1)
)
charSessEntry.setIndexNames(
    (0, "CHAR-MIB", "charSessPortIndex"),
    (0, "CHAR-MIB", "charSessIndex"),
)
if mibBuilder.loadTexts:
    charSessEntry.setStatus("mandatory")
_CharSessPortIndex_Type = Integer32
_CharSessPortIndex_Object = MibTableColumn
charSessPortIndex = _CharSessPortIndex_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 1),
    _CharSessPortIndex_Type()
)
charSessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessPortIndex.setStatus("mandatory")
_CharSessIndex_Type = Integer32
_CharSessIndex_Object = MibTableColumn
charSessIndex = _CharSessIndex_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 2),
    _CharSessIndex_Type()
)
charSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 3, 1, 3),
    _CharSessKill_Type()
)
charSessKill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charSessKill.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 3, 1, 4),
    _CharSessState_Type()
)
charSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessState.setStatus("mandatory")
_CharSessProtocol_Type = AutonomousType
_CharSessProtocol_Object = MibTableColumn
charSessProtocol = _CharSessProtocol_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 5),
    _CharSessProtocol_Type()
)
charSessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessProtocol.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 19, 3, 1, 6),
    _CharSessOperOrigin_Type()
)
charSessOperOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessOperOrigin.setStatus("mandatory")
_CharSessInCharacters_Type = Counter32
_CharSessInCharacters_Object = MibTableColumn
charSessInCharacters = _CharSessInCharacters_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 7),
    _CharSessInCharacters_Type()
)
charSessInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessInCharacters.setStatus("mandatory")
_CharSessOutCharacters_Type = Counter32
_CharSessOutCharacters_Object = MibTableColumn
charSessOutCharacters = _CharSessOutCharacters_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 8),
    _CharSessOutCharacters_Type()
)
charSessOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessOutCharacters.setStatus("mandatory")
_CharSessConnectionId_Type = InstancePointer
_CharSessConnectionId_Object = MibTableColumn
charSessConnectionId = _CharSessConnectionId_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 9),
    _CharSessConnectionId_Type()
)
charSessConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessConnectionId.setStatus("mandatory")
_CharSessStartTime_Type = TimeTicks
_CharSessStartTime_Object = MibTableColumn
charSessStartTime = _CharSessStartTime_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 10),
    _CharSessStartTime_Type()
)
charSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessStartTime.setStatus("mandatory")
_WellKnownProtocols_ObjectIdentity = ObjectIdentity
wellKnownProtocols = _WellKnownProtocols_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4)
)
_ProtocolOther_ObjectIdentity = ObjectIdentity
protocolOther = _ProtocolOther_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 1)
)
_ProtocolTelnet_ObjectIdentity = ObjectIdentity
protocolTelnet = _ProtocolTelnet_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 2)
)
_ProtocolRlogin_ObjectIdentity = ObjectIdentity
protocolRlogin = _ProtocolRlogin_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 3)
)
_ProtocolLat_ObjectIdentity = ObjectIdentity
protocolLat = _ProtocolLat_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 4)
)
_ProtocolX29_ObjectIdentity = ObjectIdentity
protocolX29 = _ProtocolX29_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 5)
)
_ProtocolVtp_ObjectIdentity = ObjectIdentity
protocolVtp = _ProtocolVtp_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHAR-MIB",
    **{"AutonomousType": AutonomousType,
       "InstancePointer": InstancePointer,
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
       "protocolVtp": protocolVtp}
)
