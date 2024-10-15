# SNMP MIB module (BAS-ALIAS-CMTS-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-ALIAS-CMTS-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:16 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAliasCmtsCfg) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasCmtsCfg")

(docsIfCmtsModulationEntry,
 docsIfDownstreamChannelEntry,
 docsIfUpstreamChannelEntry) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsModulationEntry",
    "docsIfDownstreamChannelEntry",
    "docsIfUpstreamChannelEntry")

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

basAliasCmtsCfgMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BasCmtsInt8(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )



class BasCmtsUInt8(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class BasCmtsByte(BasCmtsUInt8, TextualConvention):
    status = "current"
    displayHint = "d"


class BasCmtsInt16(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class BasCmtsUInt16(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BasCmtsInt32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class BasCmtsUInt32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class BasCmtsRowAction(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basCmtsRowActionApply", 2),
          ("basCmtsRowActionNone", 1))
    )



class BasCmtsHeadEndMapMode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(99, 99),
    )



class BasCmtsHeadEndMacAddr(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class BasCmtsHeadEndAuthString(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class BasCmtsUpChannelPreamblePattern(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class BasCmtsModulationWsPattern(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



# MIB Managed Objects in the order of their OIDs

_BasCmtsCfgObjects_ObjectIdentity = ObjectIdentity
basCmtsCfgObjects = _BasCmtsCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1)
)
_BasCmtsPLLTable_Object = MibTable
basCmtsPLLTable = _BasCmtsPLLTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basCmtsPLLTable.setStatus("current")
_BasCmtsPLLEntry_Object = MibTableRow
basCmtsPLLEntry = _BasCmtsPLLEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1)
)
basCmtsPLLEntry.setIndexNames(
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLChassis"),
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLSlot"),
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLIf"),
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basCmtsPLLLPort"),
)
if mibBuilder.loadTexts:
    basCmtsPLLEntry.setStatus("current")
_BasCmtsPLLChassis_Type = BasChassisId
_BasCmtsPLLChassis_Object = MibTableColumn
basCmtsPLLChassis = _BasCmtsPLLChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 1),
    _BasCmtsPLLChassis_Type()
)
basCmtsPLLChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCmtsPLLChassis.setStatus("current")
_BasCmtsPLLSlot_Type = BasSlotId
_BasCmtsPLLSlot_Object = MibTableColumn
basCmtsPLLSlot = _BasCmtsPLLSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 2),
    _BasCmtsPLLSlot_Type()
)
basCmtsPLLSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCmtsPLLSlot.setStatus("current")
_BasCmtsPLLIf_Type = BasInterfaceId
_BasCmtsPLLIf_Object = MibTableColumn
basCmtsPLLIf = _BasCmtsPLLIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 3),
    _BasCmtsPLLIf_Type()
)
basCmtsPLLIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCmtsPLLIf.setStatus("current")
_BasCmtsPLLLPort_Type = BasLogicalPortId
_BasCmtsPLLLPort_Object = MibTableColumn
basCmtsPLLLPort = _BasCmtsPLLLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 4),
    _BasCmtsPLLLPort_Type()
)
basCmtsPLLLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCmtsPLLLPort.setStatus("current")


class _BasCmtsPLLState_Type(Integer32):
    """Custom type basCmtsPLLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("pllSet", 2))
    )


_BasCmtsPLLState_Type.__name__ = "Integer32"
_BasCmtsPLLState_Object = MibTableColumn
basCmtsPLLState = _BasCmtsPLLState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 5),
    _BasCmtsPLLState_Type()
)
basCmtsPLLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsPLLState.setStatus("current")
_BasCmtsPLLValue_Type = BasCmtsInt32
_BasCmtsPLLValue_Object = MibTableColumn
basCmtsPLLValue = _BasCmtsPLLValue_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 1, 2, 1, 6),
    _BasCmtsPLLValue_Type()
)
basCmtsPLLValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCmtsPLLValue.setStatus("current")
_BasAlsCmtsMacToSidObjects_ObjectIdentity = ObjectIdentity
basAlsCmtsMacToSidObjects = _BasAlsCmtsMacToSidObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2)
)
_BasAlsCmtsMacToSidTable_Object = MibTable
basAlsCmtsMacToSidTable = _BasAlsCmtsMacToSidTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidTable.setStatus("current")
_BasAlsCmtsMacToSidEntry_Object = MibTableRow
basAlsCmtsMacToSidEntry = _BasAlsCmtsMacToSidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1)
)
basAlsCmtsMacToSidEntry.setIndexNames(
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidChassis"),
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidSlot"),
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidIf"),
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidLPort"),
    (0, "BAS-ALIAS-CMTS-CONFIG-MIB", "basAlsCmtsMacToSidMacAddr"),
)
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidEntry.setStatus("current")
_BasAlsCmtsMacToSidMacAddr_Type = MacAddress
_BasAlsCmtsMacToSidMacAddr_Object = MibTableColumn
basAlsCmtsMacToSidMacAddr = _BasAlsCmtsMacToSidMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 1),
    _BasAlsCmtsMacToSidMacAddr_Type()
)
basAlsCmtsMacToSidMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidMacAddr.setStatus("current")
_BasAlsCmtsMacToSidServiceId_Type = Integer32
_BasAlsCmtsMacToSidServiceId_Object = MibTableColumn
basAlsCmtsMacToSidServiceId = _BasAlsCmtsMacToSidServiceId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 2),
    _BasAlsCmtsMacToSidServiceId_Type()
)
basAlsCmtsMacToSidServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidServiceId.setStatus("current")


class _BasAlsCmtsMacToSidType_Type(Integer32):
    """Custom type basAlsCmtsMacToSidType based on Integer32"""
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
        *(("cableModem", 2),
          ("host", 3),
          ("none", 1))
    )


_BasAlsCmtsMacToSidType_Type.__name__ = "Integer32"
_BasAlsCmtsMacToSidType_Object = MibTableColumn
basAlsCmtsMacToSidType = _BasAlsCmtsMacToSidType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 3),
    _BasAlsCmtsMacToSidType_Type()
)
basAlsCmtsMacToSidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidType.setStatus("current")
_BasAlsCmtsMacToSidChassis_Type = BasChassisId
_BasAlsCmtsMacToSidChassis_Object = MibTableColumn
basAlsCmtsMacToSidChassis = _BasAlsCmtsMacToSidChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 4),
    _BasAlsCmtsMacToSidChassis_Type()
)
basAlsCmtsMacToSidChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidChassis.setStatus("current")
_BasAlsCmtsMacToSidSlot_Type = BasSlotId
_BasAlsCmtsMacToSidSlot_Object = MibTableColumn
basAlsCmtsMacToSidSlot = _BasAlsCmtsMacToSidSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 5),
    _BasAlsCmtsMacToSidSlot_Type()
)
basAlsCmtsMacToSidSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidSlot.setStatus("current")
_BasAlsCmtsMacToSidIf_Type = BasInterfaceId
_BasAlsCmtsMacToSidIf_Object = MibTableColumn
basAlsCmtsMacToSidIf = _BasAlsCmtsMacToSidIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 6),
    _BasAlsCmtsMacToSidIf_Type()
)
basAlsCmtsMacToSidIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidIf.setStatus("current")
_BasAlsCmtsMacToSidLPort_Type = BasLogicalPortId
_BasAlsCmtsMacToSidLPort_Object = MibTableColumn
basAlsCmtsMacToSidLPort = _BasAlsCmtsMacToSidLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10, 1, 2, 1, 1, 7),
    _BasAlsCmtsMacToSidLPort_Type()
)
basAlsCmtsMacToSidLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAlsCmtsMacToSidLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-ALIAS-CMTS-CONFIG-MIB",
    **{"BasCmtsInt8": BasCmtsInt8,
       "BasCmtsUInt8": BasCmtsUInt8,
       "BasCmtsByte": BasCmtsByte,
       "BasCmtsInt16": BasCmtsInt16,
       "BasCmtsUInt16": BasCmtsUInt16,
       "BasCmtsInt32": BasCmtsInt32,
       "BasCmtsUInt32": BasCmtsUInt32,
       "BasCmtsRowAction": BasCmtsRowAction,
       "BasCmtsHeadEndMapMode": BasCmtsHeadEndMapMode,
       "BasCmtsHeadEndMacAddr": BasCmtsHeadEndMacAddr,
       "BasCmtsHeadEndAuthString": BasCmtsHeadEndAuthString,
       "BasCmtsUpChannelPreamblePattern": BasCmtsUpChannelPreamblePattern,
       "BasCmtsModulationWsPattern": BasCmtsModulationWsPattern,
       "basAliasCmtsCfgMib": basAliasCmtsCfgMib,
       "basCmtsCfgObjects": basCmtsCfgObjects,
       "basCmtsPLLTable": basCmtsPLLTable,
       "basCmtsPLLEntry": basCmtsPLLEntry,
       "basCmtsPLLChassis": basCmtsPLLChassis,
       "basCmtsPLLSlot": basCmtsPLLSlot,
       "basCmtsPLLIf": basCmtsPLLIf,
       "basCmtsPLLLPort": basCmtsPLLLPort,
       "basCmtsPLLState": basCmtsPLLState,
       "basCmtsPLLValue": basCmtsPLLValue,
       "basAlsCmtsMacToSidObjects": basAlsCmtsMacToSidObjects,
       "basAlsCmtsMacToSidTable": basAlsCmtsMacToSidTable,
       "basAlsCmtsMacToSidEntry": basAlsCmtsMacToSidEntry,
       "basAlsCmtsMacToSidMacAddr": basAlsCmtsMacToSidMacAddr,
       "basAlsCmtsMacToSidServiceId": basAlsCmtsMacToSidServiceId,
       "basAlsCmtsMacToSidType": basAlsCmtsMacToSidType,
       "basAlsCmtsMacToSidChassis": basAlsCmtsMacToSidChassis,
       "basAlsCmtsMacToSidSlot": basAlsCmtsMacToSidSlot,
       "basAlsCmtsMacToSidIf": basAlsCmtsMacToSidIf,
       "basAlsCmtsMacToSidLPort": basAlsCmtsMacToSidLPort}
)
