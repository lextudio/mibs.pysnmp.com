# SNMP MIB module (OGTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OGTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:54 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Opengear_ObjectIdentity = ObjectIdentity
opengear = _Opengear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049)
)
_OgLegacyMgmt_ObjectIdentity = ObjectIdentity
ogLegacyMgmt = _OgLegacyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2)
)
_OgConnectMib_ObjectIdentity = ObjectIdentity
ogConnectMib = _OgConnectMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10)
)
_OgConnectMibObjects_ObjectIdentity = ObjectIdentity
ogConnectMibObjects = _OgConnectMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10, 10)
)
_OgconnEvent_ObjectIdentity = ObjectIdentity
ogconnEvent = _OgconnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1)
)
_OgconnEventTable_ObjectIdentity = ObjectIdentity
ogconnEventTable = _OgconnEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1)
)
_OgconnEventEntry_ObjectIdentity = ObjectIdentity
ogconnEventEntry = _OgconnEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1)
)
_OgconnEventUsername_Type = OctetString
_OgconnEventUsername_Object = MibScalar
ogconnEventUsername = _OgconnEventUsername_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 10),
    _OgconnEventUsername_Type()
)
ogconnEventUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogconnEventUsername.setStatus("mandatory")
_OgconnEventType_Type = OctetString
_OgconnEventType_Object = MibScalar
ogconnEventType = _OgconnEventType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 11),
    _OgconnEventType_Type()
)
ogconnEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogconnEventType.setStatus("mandatory")
_OgconnEventPortNumber_Type = Integer32
_OgconnEventPortNumber_Object = MibScalar
ogconnEventPortNumber = _OgconnEventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 12),
    _OgconnEventPortNumber_Type()
)
ogconnEventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogconnEventPortNumber.setStatus("mandatory")
_OgconnEventPortLabel_Type = OctetString
_OgconnEventPortLabel_Object = MibScalar
ogconnEventPortLabel = _OgconnEventPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 10, 10, 1, 1, 1, 13),
    _OgconnEventPortLabel_Type()
)
ogconnEventPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogconnEventPortLabel.setStatus("mandatory")
_OgSignalMib_ObjectIdentity = ObjectIdentity
ogSignalMib = _OgSignalMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11)
)
_OgSignalMibObjects_ObjectIdentity = ObjectIdentity
ogSignalMibObjects = _OgSignalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11, 10)
)
_OgsgnlEvent_ObjectIdentity = ObjectIdentity
ogsgnlEvent = _OgsgnlEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1)
)
_OgsgnlEventTable_ObjectIdentity = ObjectIdentity
ogsgnlEventTable = _OgsgnlEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1)
)
_OgsgnlEventEntry_ObjectIdentity = ObjectIdentity
ogsgnlEventEntry = _OgsgnlEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1)
)
_OgsgnlEventType_Type = OctetString
_OgsgnlEventType_Object = MibScalar
ogsgnlEventType = _OgsgnlEventType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 10),
    _OgsgnlEventType_Type()
)
ogsgnlEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsgnlEventType.setStatus("mandatory")
_OgsgnlEventState_Type = OctetString
_OgsgnlEventState_Object = MibScalar
ogsgnlEventState = _OgsgnlEventState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 11),
    _OgsgnlEventState_Type()
)
ogsgnlEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsgnlEventState.setStatus("mandatory")
_OgsgnlEventPortNumber_Type = Integer32
_OgsgnlEventPortNumber_Object = MibScalar
ogsgnlEventPortNumber = _OgsgnlEventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 12),
    _OgsgnlEventPortNumber_Type()
)
ogsgnlEventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsgnlEventPortNumber.setStatus("mandatory")
_OgsgnlEventPortLabel_Type = OctetString
_OgsgnlEventPortLabel_Object = MibScalar
ogsgnlEventPortLabel = _OgsgnlEventPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 11, 10, 1, 1, 1, 13),
    _OgsgnlEventPortLabel_Type()
)
ogsgnlEventPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsgnlEventPortLabel.setStatus("mandatory")
_OgPatternMib_ObjectIdentity = ObjectIdentity
ogPatternMib = _OgPatternMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12)
)
_OgPatternMibObjects_ObjectIdentity = ObjectIdentity
ogPatternMibObjects = _OgPatternMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12, 10)
)
_OgpatnEvent_ObjectIdentity = ObjectIdentity
ogpatnEvent = _OgpatnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1)
)
_OgpatnEventTable_ObjectIdentity = ObjectIdentity
ogpatnEventTable = _OgpatnEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1)
)
_OgpatnEventEntry_ObjectIdentity = ObjectIdentity
ogpatnEventEntry = _OgpatnEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1)
)
_OgpatnEventDescription_Type = OctetString
_OgpatnEventDescription_Object = MibScalar
ogpatnEventDescription = _OgpatnEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 10),
    _OgpatnEventDescription_Type()
)
ogpatnEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogpatnEventDescription.setStatus("mandatory")
_OgpatnEventText_Type = OctetString
_OgpatnEventText_Object = MibScalar
ogpatnEventText = _OgpatnEventText_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 11),
    _OgpatnEventText_Type()
)
ogpatnEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogpatnEventText.setStatus("mandatory")
_OgpatnEventPortNumber_Type = Integer32
_OgpatnEventPortNumber_Object = MibScalar
ogpatnEventPortNumber = _OgpatnEventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 12),
    _OgpatnEventPortNumber_Type()
)
ogpatnEventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogpatnEventPortNumber.setStatus("mandatory")
_OgpatnEventPortLabel_Type = OctetString
_OgpatnEventPortLabel_Object = MibScalar
ogpatnEventPortLabel = _OgpatnEventPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 12, 10, 1, 1, 1, 13),
    _OgpatnEventPortLabel_Type()
)
ogpatnEventPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogpatnEventPortLabel.setStatus("mandatory")
_OgSensorMib_ObjectIdentity = ObjectIdentity
ogSensorMib = _OgSensorMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13)
)
_OgSensorMibObjects_ObjectIdentity = ObjectIdentity
ogSensorMibObjects = _OgSensorMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13, 10)
)
_OgsensStatus_ObjectIdentity = ObjectIdentity
ogsensStatus = _OgsensStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1)
)
_OgsensStatusTable_ObjectIdentity = ObjectIdentity
ogsensStatusTable = _OgsensStatusTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1)
)
_OgsensStatusEntry_ObjectIdentity = ObjectIdentity
ogsensStatusEntry = _OgsensStatusEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1)
)
_OgsensStatusName_Type = OctetString
_OgsensStatusName_Object = MibScalar
ogsensStatusName = _OgsensStatusName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 10),
    _OgsensStatusName_Type()
)
ogsensStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsensStatusName.setStatus("mandatory")
_OgsensStatusDevType_Type = OctetString
_OgsensStatusDevType_Object = MibScalar
ogsensStatusDevType = _OgsensStatusDevType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 11),
    _OgsensStatusDevType_Type()
)
ogsensStatusDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsensStatusDevType.setStatus("mandatory")
_OgsensStatusType_Type = OctetString
_OgsensStatusType_Object = MibScalar
ogsensStatusType = _OgsensStatusType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 12),
    _OgsensStatusType_Type()
)
ogsensStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsensStatusType.setStatus("mandatory")
_OgsensStatusValue_Type = Integer32
_OgsensStatusValue_Object = MibScalar
ogsensStatusValue = _OgsensStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 13, 10, 1, 1, 1, 13),
    _OgsensStatusValue_Type()
)
ogsensStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsensStatusValue.setStatus("mandatory")
_OgHostMib_ObjectIdentity = ObjectIdentity
ogHostMib = _OgHostMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14)
)
_OgHostMibObjects_ObjectIdentity = ObjectIdentity
ogHostMibObjects = _OgHostMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10)
)
_OghostEvent_ObjectIdentity = ObjectIdentity
oghostEvent = _OghostEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1)
)
_OghostEventTable_ObjectIdentity = ObjectIdentity
oghostEventTable = _OghostEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1)
)
_OghostEventEntry_ObjectIdentity = ObjectIdentity
oghostEventEntry = _OghostEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1)
)
_OghostEventUsername_Type = OctetString
_OghostEventUsername_Object = MibScalar
oghostEventUsername = _OghostEventUsername_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 10),
    _OghostEventUsername_Type()
)
oghostEventUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventUsername.setStatus("mandatory")
_OghostEventType_Type = OctetString
_OghostEventType_Object = MibScalar
oghostEventType = _OghostEventType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 11),
    _OghostEventType_Type()
)
oghostEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventType.setStatus("mandatory")
_OghostEventAddress_Type = OctetString
_OghostEventAddress_Object = MibScalar
oghostEventAddress = _OghostEventAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 12),
    _OghostEventAddress_Type()
)
oghostEventAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventAddress.setStatus("mandatory")
_OghostEventDescription_Type = OctetString
_OghostEventDescription_Object = MibScalar
oghostEventDescription = _OghostEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 13),
    _OghostEventDescription_Type()
)
oghostEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventDescription.setStatus("mandatory")
_OghostEventProtocol_Type = OctetString
_OghostEventProtocol_Object = MibScalar
oghostEventProtocol = _OghostEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 14),
    _OghostEventProtocol_Type()
)
oghostEventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventProtocol.setStatus("mandatory")
_OghostEventPort_Type = Integer32
_OghostEventPort_Object = MibScalar
oghostEventPort = _OghostEventPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 14, 10, 1, 1, 1, 15),
    _OghostEventPort_Type()
)
oghostEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventPort.setStatus("mandatory")
_OgFailoverMib_ObjectIdentity = ObjectIdentity
ogFailoverMib = _OgFailoverMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 15)
)
_OgFailoverMibObjects_ObjectIdentity = ObjectIdentity
ogFailoverMibObjects = _OgFailoverMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 15, 10)
)
_OgfovrEvent_ObjectIdentity = ObjectIdentity
ogfovrEvent = _OgfovrEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1)
)
_OgfovrEventTable_ObjectIdentity = ObjectIdentity
ogfovrEventTable = _OgfovrEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1)
)
_OgfovrEventEntry_ObjectIdentity = ObjectIdentity
ogfovrEventEntry = _OgfovrEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1)
)
_OgfovrEventPrimary_Type = OctetString
_OgfovrEventPrimary_Object = MibScalar
ogfovrEventPrimary = _OgfovrEventPrimary_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1, 10),
    _OgfovrEventPrimary_Type()
)
ogfovrEventPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogfovrEventPrimary.setStatus("mandatory")
_OgfovrEventSecondary_Type = OctetString
_OgfovrEventSecondary_Object = MibScalar
ogfovrEventSecondary = _OgfovrEventSecondary_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 15, 10, 1, 1, 1, 11),
    _OgfovrEventSecondary_Type()
)
ogfovrEventSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogfovrEventSecondary.setStatus("mandatory")
_OgNetUpsMib_ObjectIdentity = ObjectIdentity
ogNetUpsMib = _OgNetUpsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 16)
)
_OgNetUpsMibObjects_ObjectIdentity = ObjectIdentity
ogNetUpsMibObjects = _OgNetUpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 16, 10)
)
_OgnupsEvent_ObjectIdentity = ObjectIdentity
ognupsEvent = _OgnupsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1)
)
_OgnupsEventTable_ObjectIdentity = ObjectIdentity
ognupsEventTable = _OgnupsEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1)
)
_OgnupsEventEntry_ObjectIdentity = ObjectIdentity
ognupsEventEntry = _OgnupsEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1)
)
_OgnupsEventName_Type = OctetString
_OgnupsEventName_Object = MibScalar
ognupsEventName = _OgnupsEventName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1, 10),
    _OgnupsEventName_Type()
)
ognupsEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ognupsEventName.setStatus("mandatory")
_OgnupsEventType_Type = OctetString
_OgnupsEventType_Object = MibScalar
ognupsEventType = _OgnupsEventType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 16, 10, 1, 1, 1, 11),
    _OgnupsEventType_Type()
)
ognupsEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ognupsEventType.setStatus("mandatory")
_OgDataMib_ObjectIdentity = ObjectIdentity
ogDataMib = _OgDataMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17)
)
_OgDataMibObjects_ObjectIdentity = ObjectIdentity
ogDataMibObjects = _OgDataMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17, 10)
)
_OgdataEvent_ObjectIdentity = ObjectIdentity
ogdataEvent = _OgdataEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1)
)
_OgdataEventTable_ObjectIdentity = ObjectIdentity
ogdataEventTable = _OgdataEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1)
)
_OgdataEventEntry_ObjectIdentity = ObjectIdentity
ogdataEventEntry = _OgdataEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1)
)
_OgdataEventBytes_Type = Integer32
_OgdataEventBytes_Object = MibScalar
ogdataEventBytes = _OgdataEventBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 10),
    _OgdataEventBytes_Type()
)
ogdataEventBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogdataEventBytes.setStatus("mandatory")
_OgdataEventSeconds_Type = Integer32
_OgdataEventSeconds_Object = MibScalar
ogdataEventSeconds = _OgdataEventSeconds_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 11),
    _OgdataEventSeconds_Type()
)
ogdataEventSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogdataEventSeconds.setStatus("mandatory")
_OgdataEventDevice_Type = OctetString
_OgdataEventDevice_Object = MibScalar
ogdataEventDevice = _OgdataEventDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 12),
    _OgdataEventDevice_Type()
)
ogdataEventDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogdataEventDevice.setStatus("mandatory")
_OgdataEventState_Type = Integer32
_OgdataEventState_Object = MibScalar
ogdataEventState = _OgdataEventState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 17, 10, 1, 1, 1, 13),
    _OgdataEventState_Type()
)
ogdataEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogdataEventState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ogconnEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 1001)
)
ogconnEventOccurred.setObjects(
      *(("OGTRAP-MIB", "ogconnEventUsername"),
        ("OGTRAP-MIB", "ogconnEventType"),
        ("OGTRAP-MIB", "ogconnEventPortNumber"),
        ("OGTRAP-MIB", "ogconnEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogconnEventOccurred.setStatus(
        ""
    )

ogsgnlEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 1002)
)
ogsgnlEventOccurred.setObjects(
      *(("OGTRAP-MIB", "ogsgnlEventType"),
        ("OGTRAP-MIB", "ogsgnlEventState"),
        ("OGTRAP-MIB", "ogsgnlEventPortNumber"),
        ("OGTRAP-MIB", "ogsgnlEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogsgnlEventOccurred.setStatus(
        ""
    )

ogpatnEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 1003)
)
ogpatnEventOccurred.setObjects(
      *(("OGTRAP-MIB", "ogpatnEventDescription"),
        ("OGTRAP-MIB", "ogpatnEventText"),
        ("OGTRAP-MIB", "ogpatnEventPortNumber"),
        ("OGTRAP-MIB", "ogpatnEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogpatnEventOccurred.setStatus(
        ""
    )

ogsensStatusOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 1004)
)
ogsensStatusOccurred.setObjects(
      *(("OGTRAP-MIB", "ogsensStatusName"),
        ("OGTRAP-MIB", "ogsensStatusDevType"),
        ("OGTRAP-MIB", "ogsensStatusType"),
        ("OGTRAP-MIB", "ogsensStatusValue"))
)
if mibBuilder.loadTexts:
    ogsensStatusOccurred.setStatus(
        ""
    )

oghostEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 2001)
)
oghostEventOccurred.setObjects(
      *(("OGTRAP-MIB", "oghostEventUsername"),
        ("OGTRAP-MIB", "oghostEventType"),
        ("OGTRAP-MIB", "oghostEventAddress"),
        ("OGTRAP-MIB", "oghostEventDescription"),
        ("OGTRAP-MIB", "oghostEventProtocol"),
        ("OGTRAP-MIB", "oghostEventPort"))
)
if mibBuilder.loadTexts:
    oghostEventOccurred.setStatus(
        ""
    )

ogfovrEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 2002)
)
ogfovrEventOccurred.setObjects(
      *(("OGTRAP-MIB", "ogfovrEventPrimary"),
        ("OGTRAP-MIB", "ogfovrEventSecondary"))
)
if mibBuilder.loadTexts:
    ogfovrEventOccurred.setStatus(
        ""
    )

ognupsEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 2003)
)
ognupsEventOccurred.setObjects(
      *(("OGTRAP-MIB", "ognupsEventName"),
        ("OGTRAP-MIB", "ognupsEventType"))
)
if mibBuilder.loadTexts:
    ognupsEventOccurred.setStatus(
        ""
    )

ogdataEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 2004)
)
ogdataEventOccurred.setObjects(
      *(("OGTRAP-MIB", "ogdataEventBytes"),
        ("OGTRAP-MIB", "ogdataEventSeconds"),
        ("OGTRAP-MIB", "ogdataEventDevice"),
        ("OGTRAP-MIB", "ogdataEventState"))
)
if mibBuilder.loadTexts:
    ogdataEventOccurred.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OGTRAP-MIB",
    **{"opengear": opengear,
       "ogconnEventOccurred": ogconnEventOccurred,
       "ogsgnlEventOccurred": ogsgnlEventOccurred,
       "ogpatnEventOccurred": ogpatnEventOccurred,
       "ogsensStatusOccurred": ogsensStatusOccurred,
       "oghostEventOccurred": oghostEventOccurred,
       "ogfovrEventOccurred": ogfovrEventOccurred,
       "ognupsEventOccurred": ognupsEventOccurred,
       "ogdataEventOccurred": ogdataEventOccurred,
       "ogLegacyMgmt": ogLegacyMgmt,
       "ogConnectMib": ogConnectMib,
       "ogConnectMibObjects": ogConnectMibObjects,
       "ogconnEvent": ogconnEvent,
       "ogconnEventTable": ogconnEventTable,
       "ogconnEventEntry": ogconnEventEntry,
       "ogconnEventUsername": ogconnEventUsername,
       "ogconnEventType": ogconnEventType,
       "ogconnEventPortNumber": ogconnEventPortNumber,
       "ogconnEventPortLabel": ogconnEventPortLabel,
       "ogSignalMib": ogSignalMib,
       "ogSignalMibObjects": ogSignalMibObjects,
       "ogsgnlEvent": ogsgnlEvent,
       "ogsgnlEventTable": ogsgnlEventTable,
       "ogsgnlEventEntry": ogsgnlEventEntry,
       "ogsgnlEventType": ogsgnlEventType,
       "ogsgnlEventState": ogsgnlEventState,
       "ogsgnlEventPortNumber": ogsgnlEventPortNumber,
       "ogsgnlEventPortLabel": ogsgnlEventPortLabel,
       "ogPatternMib": ogPatternMib,
       "ogPatternMibObjects": ogPatternMibObjects,
       "ogpatnEvent": ogpatnEvent,
       "ogpatnEventTable": ogpatnEventTable,
       "ogpatnEventEntry": ogpatnEventEntry,
       "ogpatnEventDescription": ogpatnEventDescription,
       "ogpatnEventText": ogpatnEventText,
       "ogpatnEventPortNumber": ogpatnEventPortNumber,
       "ogpatnEventPortLabel": ogpatnEventPortLabel,
       "ogSensorMib": ogSensorMib,
       "ogSensorMibObjects": ogSensorMibObjects,
       "ogsensStatus": ogsensStatus,
       "ogsensStatusTable": ogsensStatusTable,
       "ogsensStatusEntry": ogsensStatusEntry,
       "ogsensStatusName": ogsensStatusName,
       "ogsensStatusDevType": ogsensStatusDevType,
       "ogsensStatusType": ogsensStatusType,
       "ogsensStatusValue": ogsensStatusValue,
       "ogHostMib": ogHostMib,
       "ogHostMibObjects": ogHostMibObjects,
       "oghostEvent": oghostEvent,
       "oghostEventTable": oghostEventTable,
       "oghostEventEntry": oghostEventEntry,
       "oghostEventUsername": oghostEventUsername,
       "oghostEventType": oghostEventType,
       "oghostEventAddress": oghostEventAddress,
       "oghostEventDescription": oghostEventDescription,
       "oghostEventProtocol": oghostEventProtocol,
       "oghostEventPort": oghostEventPort,
       "ogFailoverMib": ogFailoverMib,
       "ogFailoverMibObjects": ogFailoverMibObjects,
       "ogfovrEvent": ogfovrEvent,
       "ogfovrEventTable": ogfovrEventTable,
       "ogfovrEventEntry": ogfovrEventEntry,
       "ogfovrEventPrimary": ogfovrEventPrimary,
       "ogfovrEventSecondary": ogfovrEventSecondary,
       "ogNetUpsMib": ogNetUpsMib,
       "ogNetUpsMibObjects": ogNetUpsMibObjects,
       "ognupsEvent": ognupsEvent,
       "ognupsEventTable": ognupsEventTable,
       "ognupsEventEntry": ognupsEventEntry,
       "ognupsEventName": ognupsEventName,
       "ognupsEventType": ognupsEventType,
       "ogDataMib": ogDataMib,
       "ogDataMibObjects": ogDataMibObjects,
       "ogdataEvent": ogdataEvent,
       "ogdataEventTable": ogdataEventTable,
       "ogdataEventEntry": ogdataEventEntry,
       "ogdataEventBytes": ogdataEventBytes,
       "ogdataEventSeconds": ogdataEventSeconds,
       "ogdataEventDevice": ogdataEventDevice,
       "ogdataEventState": ogdataEventState}
)
