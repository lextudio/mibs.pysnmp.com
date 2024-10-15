# SNMP MIB module (CISCOSB-EVENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-EVENTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:19 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(RlSmartPortsMacroNameOrZero,) = mibBuilder.importSymbols(
    "CISCOSB-SMARTPORTS-MIB",
    "RlSmartPortsMacroNameOrZero")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlEventsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150)
)
rlEventsMib.setRevisions(
        ("2010-09-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SmartPortType(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ap", 13),
          ("default", 2),
          ("desktop", 4),
          ("guest", 5),
          ("host", 7),
          ("ip-camera", 8),
          ("ip-phone", 9),
          ("ip-phone-desktop", 10),
          ("printer", 3),
          ("router", 12),
          ("server", 6),
          ("switch", 11),
          ("unknown", 1))
    )



class SmartPortMacroParameterName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class SmartPortMacroParameterValue(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class SmartPortMacroType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("built-in", 1),
          ("user-defined", 2))
    )



class SmartPortMacroParameterOrder(Integer32, TextualConvention):
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
        *(("first", 2),
          ("last", 4),
          ("middle", 3),
          ("single", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlPortEvents_ObjectIdentity = ObjectIdentity
rlPortEvents = _RlPortEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1)
)


class _RlAutoSmartPortAdminStatus_Type(Integer32):
    """Custom type rlAutoSmartPortAdminStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlled", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_RlAutoSmartPortAdminStatus_Type.__name__ = "Integer32"
_RlAutoSmartPortAdminStatus_Object = MibScalar
rlAutoSmartPortAdminStatus = _RlAutoSmartPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 1),
    _RlAutoSmartPortAdminStatus_Type()
)
rlAutoSmartPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortAdminStatus.setStatus("current")


class _RlAutoSmartPortOperStatus_Type(Integer32):
    """Custom type rlAutoSmartPortOperStatus based on Integer32"""
    defaultValue = 2

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


_RlAutoSmartPortOperStatus_Type.__name__ = "Integer32"
_RlAutoSmartPortOperStatus_Object = MibScalar
rlAutoSmartPortOperStatus = _RlAutoSmartPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 2),
    _RlAutoSmartPortOperStatus_Type()
)
rlAutoSmartPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAutoSmartPortOperStatus.setStatus("current")


class _RlAutoSmartPortLastVoiceVlanStatus_Type(Integer32):
    """Custom type rlAutoSmartPortLastVoiceVlanStatus based on Integer32"""
    defaultValue = 2

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


_RlAutoSmartPortLastVoiceVlanStatus_Type.__name__ = "Integer32"
_RlAutoSmartPortLastVoiceVlanStatus_Object = MibScalar
rlAutoSmartPortLastVoiceVlanStatus = _RlAutoSmartPortLastVoiceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 3),
    _RlAutoSmartPortLastVoiceVlanStatus_Type()
)
rlAutoSmartPortLastVoiceVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAutoSmartPortLastVoiceVlanStatus.setStatus("current")
_RlAutoSmartPortLastVoiceVlanId_Type = Integer32
_RlAutoSmartPortLastVoiceVlanId_Object = MibScalar
rlAutoSmartPortLastVoiceVlanId = _RlAutoSmartPortLastVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 4),
    _RlAutoSmartPortLastVoiceVlanId_Type()
)
rlAutoSmartPortLastVoiceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAutoSmartPortLastVoiceVlanId.setStatus("current")


class _RlAutoSmartPortLearningProtocols_Type(Bits):
    """Custom type rlAutoSmartPortLearningProtocols based on Bits"""
    namedValues = NamedValues(
        *(("cdp", 0),
          ("lldp", 1))
    )

_RlAutoSmartPortLearningProtocols_Type.__name__ = "Bits"
_RlAutoSmartPortLearningProtocols_Object = MibScalar
rlAutoSmartPortLearningProtocols = _RlAutoSmartPortLearningProtocols_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 5),
    _RlAutoSmartPortLearningProtocols_Type()
)
rlAutoSmartPortLearningProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortLearningProtocols.setStatus("current")
_RlAutoSmartPortTypesTable_Object = MibTable
rlAutoSmartPortTypesTable = _RlAutoSmartPortTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 6)
)
if mibBuilder.loadTexts:
    rlAutoSmartPortTypesTable.setStatus("current")
_RlAutoSmartPortTypesEntry_Object = MibTableRow
rlAutoSmartPortTypesEntry = _RlAutoSmartPortTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 6, 1)
)
rlAutoSmartPortTypesEntry.setIndexNames(
    (0, "CISCOSB-EVENTS-MIB", "rlAutoSmartPortTypesType"),
)
if mibBuilder.loadTexts:
    rlAutoSmartPortTypesEntry.setStatus("current")
_RlAutoSmartPortTypesType_Type = SmartPortType
_RlAutoSmartPortTypesType_Object = MibTableColumn
rlAutoSmartPortTypesType = _RlAutoSmartPortTypesType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 6, 1, 1),
    _RlAutoSmartPortTypesType_Type()
)
rlAutoSmartPortTypesType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartPortTypesType.setStatus("current")


class _RlAutoSmartPortTypeStatus_Type(Integer32):
    """Custom type rlAutoSmartPortTypeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_RlAutoSmartPortTypeStatus_Type.__name__ = "Integer32"
_RlAutoSmartPortTypeStatus_Object = MibTableColumn
rlAutoSmartPortTypeStatus = _RlAutoSmartPortTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 6, 1, 2),
    _RlAutoSmartPortTypeStatus_Type()
)
rlAutoSmartPortTypeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortTypeStatus.setStatus("current")
_RlAutoSmartPortMacro_Type = RlSmartPortsMacroNameOrZero
_RlAutoSmartPortMacro_Object = MibTableColumn
rlAutoSmartPortMacro = _RlAutoSmartPortMacro_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 6, 1, 3),
    _RlAutoSmartPortMacro_Type()
)
rlAutoSmartPortMacro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortMacro.setStatus("current")
_RlAutoSmartPortTypesRevertToDefaultMacro_Type = TruthValue
_RlAutoSmartPortTypesRevertToDefaultMacro_Object = MibTableColumn
rlAutoSmartPortTypesRevertToDefaultMacro = _RlAutoSmartPortTypesRevertToDefaultMacro_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 6, 1, 4),
    _RlAutoSmartPortTypesRevertToDefaultMacro_Type()
)
rlAutoSmartPortTypesRevertToDefaultMacro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortTypesRevertToDefaultMacro.setStatus("current")
_RlAutoSmartPortTypesRevertToDefaultParams_Type = TruthValue
_RlAutoSmartPortTypesRevertToDefaultParams_Object = MibTableColumn
rlAutoSmartPortTypesRevertToDefaultParams = _RlAutoSmartPortTypesRevertToDefaultParams_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 6, 1, 5),
    _RlAutoSmartPortTypesRevertToDefaultParams_Type()
)
rlAutoSmartPortTypesRevertToDefaultParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortTypesRevertToDefaultParams.setStatus("current")
_RlAutoSmartPortTypesBuiltinMacro_Type = SmartPortMacroType
_RlAutoSmartPortTypesBuiltinMacro_Object = MibTableColumn
rlAutoSmartPortTypesBuiltinMacro = _RlAutoSmartPortTypesBuiltinMacro_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 6, 1, 6),
    _RlAutoSmartPortTypesBuiltinMacro_Type()
)
rlAutoSmartPortTypesBuiltinMacro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAutoSmartPortTypesBuiltinMacro.setStatus("current")
_RlAutoSmartPortMacrosParamTable_Object = MibTable
rlAutoSmartPortMacrosParamTable = _RlAutoSmartPortMacrosParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 7)
)
if mibBuilder.loadTexts:
    rlAutoSmartPortMacrosParamTable.setStatus("current")
_RlAutoSmartPortMacrosParamEntry_Object = MibTableRow
rlAutoSmartPortMacrosParamEntry = _RlAutoSmartPortMacrosParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 7, 1)
)
rlAutoSmartPortMacrosParamEntry.setIndexNames(
    (0, "CISCOSB-EVENTS-MIB", "rlAutoSmartPortTypesType"),
    (0, "CISCOSB-EVENTS-MIB", "rlAutoSmartPortMacroType"),
    (1, "CISCOSB-EVENTS-MIB", "rlAutoSmartPortMacrosParamName"),
)
if mibBuilder.loadTexts:
    rlAutoSmartPortMacrosParamEntry.setStatus("current")
_RlAutoSmartPortMacroType_Type = SmartPortMacroType
_RlAutoSmartPortMacroType_Object = MibTableColumn
rlAutoSmartPortMacroType = _RlAutoSmartPortMacroType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 7, 1, 1),
    _RlAutoSmartPortMacroType_Type()
)
rlAutoSmartPortMacroType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartPortMacroType.setStatus("current")
_RlAutoSmartPortMacrosParamName_Type = SmartPortMacroParameterName
_RlAutoSmartPortMacrosParamName_Object = MibTableColumn
rlAutoSmartPortMacrosParamName = _RlAutoSmartPortMacrosParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 7, 1, 2),
    _RlAutoSmartPortMacrosParamName_Type()
)
rlAutoSmartPortMacrosParamName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartPortMacrosParamName.setStatus("current")
_RlAutoSmartPortMacrosParamOrder_Type = SmartPortMacroParameterOrder
_RlAutoSmartPortMacrosParamOrder_Object = MibTableColumn
rlAutoSmartPortMacrosParamOrder = _RlAutoSmartPortMacrosParamOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 7, 1, 3),
    _RlAutoSmartPortMacrosParamOrder_Type()
)
rlAutoSmartPortMacrosParamOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortMacrosParamOrder.setStatus("current")
_RlAutoSmartPortMacrosParamValue_Type = SmartPortMacroParameterValue
_RlAutoSmartPortMacrosParamValue_Object = MibTableColumn
rlAutoSmartPortMacrosParamValue = _RlAutoSmartPortMacrosParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 7, 1, 4),
    _RlAutoSmartPortMacrosParamValue_Type()
)
rlAutoSmartPortMacrosParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortMacrosParamValue.setStatus("current")
_RlAutoSmartPortPortsTable_Object = MibTable
rlAutoSmartPortPortsTable = _RlAutoSmartPortPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8)
)
if mibBuilder.loadTexts:
    rlAutoSmartPortPortsTable.setStatus("current")
_RlAutoSmartPortPortsEntry_Object = MibTableRow
rlAutoSmartPortPortsEntry = _RlAutoSmartPortPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1)
)
rlAutoSmartPortPortsEntry.setIndexNames(
    (0, "CISCOSB-EVENTS-MIB", "rlAutoSmartPortPort"),
)
if mibBuilder.loadTexts:
    rlAutoSmartPortPortsEntry.setStatus("current")
_RlAutoSmartPortPort_Type = InterfaceIndex
_RlAutoSmartPortPort_Object = MibTableColumn
rlAutoSmartPortPort = _RlAutoSmartPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 1),
    _RlAutoSmartPortPort_Type()
)
rlAutoSmartPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartPortPort.setStatus("current")


class _RlAutoSmartPortPortStatus_Type(Integer32):
    """Custom type rlAutoSmartPortPortStatus based on Integer32"""
    defaultValue = 1

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


_RlAutoSmartPortPortStatus_Type.__name__ = "Integer32"
_RlAutoSmartPortPortStatus_Object = MibTableColumn
rlAutoSmartPortPortStatus = _RlAutoSmartPortPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 2),
    _RlAutoSmartPortPortStatus_Type()
)
rlAutoSmartPortPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortPortStatus.setStatus("current")


class _RlAutoSmartPortPortType_Type(SmartPortType):
    """Custom type rlAutoSmartPortPortType based on SmartPortType"""


_RlAutoSmartPortPortType_Object = MibTableColumn
rlAutoSmartPortPortType = _RlAutoSmartPortPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 3),
    _RlAutoSmartPortPortType_Type()
)
rlAutoSmartPortPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortPortType.setStatus("current")


class _RlAutoSmartPortPersistency_Type(Integer32):
    """Custom type rlAutoSmartPortPersistency based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-persistent", 2),
          ("persistent", 1))
    )


_RlAutoSmartPortPersistency_Type.__name__ = "Integer32"
_RlAutoSmartPortPersistency_Object = MibTableColumn
rlAutoSmartPortPersistency = _RlAutoSmartPortPersistency_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 4),
    _RlAutoSmartPortPersistency_Type()
)
rlAutoSmartPortPersistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortPersistency.setStatus("current")


class _RlAutoSmartPortLearntPortType_Type(SmartPortType):
    """Custom type rlAutoSmartPortLearntPortType based on SmartPortType"""


_RlAutoSmartPortLearntPortType_Object = MibTableColumn
rlAutoSmartPortLearntPortType = _RlAutoSmartPortLearntPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 5),
    _RlAutoSmartPortLearntPortType_Type()
)
rlAutoSmartPortLearntPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAutoSmartPortLearntPortType.setStatus("current")


class _RlAutoSmartPortPortAcquiringType_Type(Integer32):
    """Custom type rlAutoSmartPortPortAcquiringType based on Integer32"""
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
        *(("configuration", 2),
          ("default", 1),
          ("learning", 4),
          ("persistency", 3))
    )


_RlAutoSmartPortPortAcquiringType_Type.__name__ = "Integer32"
_RlAutoSmartPortPortAcquiringType_Object = MibTableColumn
rlAutoSmartPortPortAcquiringType = _RlAutoSmartPortPortAcquiringType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 6),
    _RlAutoSmartPortPortAcquiringType_Type()
)
rlAutoSmartPortPortAcquiringType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortPortAcquiringType.setStatus("current")
_RlAutoSmartPortLastActivatedMacro_Type = RlSmartPortsMacroNameOrZero
_RlAutoSmartPortLastActivatedMacro_Object = MibTableColumn
rlAutoSmartPortLastActivatedMacro = _RlAutoSmartPortLastActivatedMacro_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 7),
    _RlAutoSmartPortLastActivatedMacro_Type()
)
rlAutoSmartPortLastActivatedMacro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAutoSmartPortLastActivatedMacro.setStatus("current")
_RlAutoSmartPortFailedCommandNumber_Type = Integer32
_RlAutoSmartPortFailedCommandNumber_Object = MibTableColumn
rlAutoSmartPortFailedCommandNumber = _RlAutoSmartPortFailedCommandNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 8),
    _RlAutoSmartPortFailedCommandNumber_Type()
)
rlAutoSmartPortFailedCommandNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAutoSmartPortFailedCommandNumber.setStatus("current")
_RlAutoSmartPortSetLearntPortType_Type = TruthValue
_RlAutoSmartPortSetLearntPortType_Object = MibTableColumn
rlAutoSmartPortSetLearntPortType = _RlAutoSmartPortSetLearntPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 8, 1, 9),
    _RlAutoSmartPortSetLearntPortType_Type()
)
rlAutoSmartPortSetLearntPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortSetLearntPortType.setStatus("current")
_RlAutoSmartPortParamsTable_Object = MibTable
rlAutoSmartPortParamsTable = _RlAutoSmartPortParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 9)
)
if mibBuilder.loadTexts:
    rlAutoSmartPortParamsTable.setStatus("current")
_RlAutoSmartPortParamsEntry_Object = MibTableRow
rlAutoSmartPortParamsEntry = _RlAutoSmartPortParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 9, 1)
)
rlAutoSmartPortParamsEntry.setIndexNames(
    (0, "CISCOSB-EVENTS-MIB", "rlAutoSmartPortIfIndex"),
    (1, "CISCOSB-EVENTS-MIB", "rlAutoSmartPortParamName"),
)
if mibBuilder.loadTexts:
    rlAutoSmartPortParamsEntry.setStatus("current")
_RlAutoSmartPortIfIndex_Type = InterfaceIndex
_RlAutoSmartPortIfIndex_Object = MibTableColumn
rlAutoSmartPortIfIndex = _RlAutoSmartPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 9, 1, 1),
    _RlAutoSmartPortIfIndex_Type()
)
rlAutoSmartPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartPortIfIndex.setStatus("current")
_RlAutoSmartPortParamName_Type = SmartPortMacroParameterName
_RlAutoSmartPortParamName_Object = MibTableColumn
rlAutoSmartPortParamName = _RlAutoSmartPortParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 9, 1, 2),
    _RlAutoSmartPortParamName_Type()
)
rlAutoSmartPortParamName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartPortParamName.setStatus("current")
_RlAutoSmartPortParamOrder_Type = SmartPortMacroParameterOrder
_RlAutoSmartPortParamOrder_Object = MibTableColumn
rlAutoSmartPortParamOrder = _RlAutoSmartPortParamOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 9, 1, 3),
    _RlAutoSmartPortParamOrder_Type()
)
rlAutoSmartPortParamOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoSmartPortParamOrder.setStatus("current")
_RlAutoSmartPortParamValue_Type = SmartPortMacroParameterValue
_RlAutoSmartPortParamValue_Object = MibTableColumn
rlAutoSmartPortParamValue = _RlAutoSmartPortParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 9, 1, 4),
    _RlAutoSmartPortParamValue_Type()
)
rlAutoSmartPortParamValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartPortParamValue.setStatus("current")
_RlAutoSmartTrunkRefreshTable_Object = MibTable
rlAutoSmartTrunkRefreshTable = _RlAutoSmartTrunkRefreshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 10)
)
if mibBuilder.loadTexts:
    rlAutoSmartTrunkRefreshTable.setStatus("current")
_RlAutoSmartTrunkRefreshEntry_Object = MibTableRow
rlAutoSmartTrunkRefreshEntry = _RlAutoSmartTrunkRefreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 10, 1)
)
rlAutoSmartTrunkRefreshEntry.setIndexNames(
    (0, "CISCOSB-EVENTS-MIB", "rlAutoSmartTrunkRefreshSmartPortType"),
    (0, "CISCOSB-EVENTS-MIB", "rlAutoSmartTrunkRefreshIfIndex"),
)
if mibBuilder.loadTexts:
    rlAutoSmartTrunkRefreshEntry.setStatus("current")


class _RlAutoSmartTrunkRefreshSmartPortType_Type(Integer32):
    """Custom type rlAutoSmartTrunkRefreshSmartPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ap", 13),
          ("default", 1),
          ("router", 12),
          ("switch", 11))
    )


_RlAutoSmartTrunkRefreshSmartPortType_Type.__name__ = "Integer32"
_RlAutoSmartTrunkRefreshSmartPortType_Object = MibTableColumn
rlAutoSmartTrunkRefreshSmartPortType = _RlAutoSmartTrunkRefreshSmartPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 10, 1, 1),
    _RlAutoSmartTrunkRefreshSmartPortType_Type()
)
rlAutoSmartTrunkRefreshSmartPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartTrunkRefreshSmartPortType.setStatus("current")
_RlAutoSmartTrunkRefreshIfIndex_Type = InterfaceIndexOrZero
_RlAutoSmartTrunkRefreshIfIndex_Object = MibTableColumn
rlAutoSmartTrunkRefreshIfIndex = _RlAutoSmartTrunkRefreshIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 10, 1, 2),
    _RlAutoSmartTrunkRefreshIfIndex_Type()
)
rlAutoSmartTrunkRefreshIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAutoSmartTrunkRefreshIfIndex.setStatus("current")
_RlAutoSmartTrunkRefreshRowStatus_Type = RowStatus
_RlAutoSmartTrunkRefreshRowStatus_Object = MibTableColumn
rlAutoSmartTrunkRefreshRowStatus = _RlAutoSmartTrunkRefreshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 10, 1, 3),
    _RlAutoSmartTrunkRefreshRowStatus_Type()
)
rlAutoSmartTrunkRefreshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlAutoSmartTrunkRefreshRowStatus.setStatus("current")
_RlAutoSmartBusy_Type = TruthValue
_RlAutoSmartBusy_Object = MibScalar
rlAutoSmartBusy = _RlAutoSmartBusy_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150, 1, 11),
    _RlAutoSmartBusy_Type()
)
rlAutoSmartBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAutoSmartBusy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-EVENTS-MIB",
    **{"SmartPortType": SmartPortType,
       "SmartPortMacroParameterName": SmartPortMacroParameterName,
       "SmartPortMacroParameterValue": SmartPortMacroParameterValue,
       "SmartPortMacroType": SmartPortMacroType,
       "SmartPortMacroParameterOrder": SmartPortMacroParameterOrder,
       "rlEventsMib": rlEventsMib,
       "rlPortEvents": rlPortEvents,
       "rlAutoSmartPortAdminStatus": rlAutoSmartPortAdminStatus,
       "rlAutoSmartPortOperStatus": rlAutoSmartPortOperStatus,
       "rlAutoSmartPortLastVoiceVlanStatus": rlAutoSmartPortLastVoiceVlanStatus,
       "rlAutoSmartPortLastVoiceVlanId": rlAutoSmartPortLastVoiceVlanId,
       "rlAutoSmartPortLearningProtocols": rlAutoSmartPortLearningProtocols,
       "rlAutoSmartPortTypesTable": rlAutoSmartPortTypesTable,
       "rlAutoSmartPortTypesEntry": rlAutoSmartPortTypesEntry,
       "rlAutoSmartPortTypesType": rlAutoSmartPortTypesType,
       "rlAutoSmartPortTypeStatus": rlAutoSmartPortTypeStatus,
       "rlAutoSmartPortMacro": rlAutoSmartPortMacro,
       "rlAutoSmartPortTypesRevertToDefaultMacro": rlAutoSmartPortTypesRevertToDefaultMacro,
       "rlAutoSmartPortTypesRevertToDefaultParams": rlAutoSmartPortTypesRevertToDefaultParams,
       "rlAutoSmartPortTypesBuiltinMacro": rlAutoSmartPortTypesBuiltinMacro,
       "rlAutoSmartPortMacrosParamTable": rlAutoSmartPortMacrosParamTable,
       "rlAutoSmartPortMacrosParamEntry": rlAutoSmartPortMacrosParamEntry,
       "rlAutoSmartPortMacroType": rlAutoSmartPortMacroType,
       "rlAutoSmartPortMacrosParamName": rlAutoSmartPortMacrosParamName,
       "rlAutoSmartPortMacrosParamOrder": rlAutoSmartPortMacrosParamOrder,
       "rlAutoSmartPortMacrosParamValue": rlAutoSmartPortMacrosParamValue,
       "rlAutoSmartPortPortsTable": rlAutoSmartPortPortsTable,
       "rlAutoSmartPortPortsEntry": rlAutoSmartPortPortsEntry,
       "rlAutoSmartPortPort": rlAutoSmartPortPort,
       "rlAutoSmartPortPortStatus": rlAutoSmartPortPortStatus,
       "rlAutoSmartPortPortType": rlAutoSmartPortPortType,
       "rlAutoSmartPortPersistency": rlAutoSmartPortPersistency,
       "rlAutoSmartPortLearntPortType": rlAutoSmartPortLearntPortType,
       "rlAutoSmartPortPortAcquiringType": rlAutoSmartPortPortAcquiringType,
       "rlAutoSmartPortLastActivatedMacro": rlAutoSmartPortLastActivatedMacro,
       "rlAutoSmartPortFailedCommandNumber": rlAutoSmartPortFailedCommandNumber,
       "rlAutoSmartPortSetLearntPortType": rlAutoSmartPortSetLearntPortType,
       "rlAutoSmartPortParamsTable": rlAutoSmartPortParamsTable,
       "rlAutoSmartPortParamsEntry": rlAutoSmartPortParamsEntry,
       "rlAutoSmartPortIfIndex": rlAutoSmartPortIfIndex,
       "rlAutoSmartPortParamName": rlAutoSmartPortParamName,
       "rlAutoSmartPortParamOrder": rlAutoSmartPortParamOrder,
       "rlAutoSmartPortParamValue": rlAutoSmartPortParamValue,
       "rlAutoSmartTrunkRefreshTable": rlAutoSmartTrunkRefreshTable,
       "rlAutoSmartTrunkRefreshEntry": rlAutoSmartTrunkRefreshEntry,
       "rlAutoSmartTrunkRefreshSmartPortType": rlAutoSmartTrunkRefreshSmartPortType,
       "rlAutoSmartTrunkRefreshIfIndex": rlAutoSmartTrunkRefreshIfIndex,
       "rlAutoSmartTrunkRefreshRowStatus": rlAutoSmartTrunkRefreshRowStatus,
       "rlAutoSmartBusy": rlAutoSmartBusy}
)
