# SNMP MIB module (AC-ModularGW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-ModularGW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:30 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acModularGateway = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcBoardMibs_ObjectIdentity = ObjectIdentity
acBoardMibs = _AcBoardMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10)
)
_AcModularGatewayConfiguration_ObjectIdentity = ObjectIdentity
acModularGatewayConfiguration = _AcModularGatewayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 1)
)
_AcModularGatewayStatus_ObjectIdentity = ObjectIdentity
acModularGatewayStatus = _AcModularGatewayStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2)
)
_AcModularGWModules_ObjectIdentity = ObjectIdentity
acModularGWModules = _AcModularGWModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1)
)
_AcModularGWModuleTable_Object = MibTable
acModularGWModuleTable = _AcModularGWModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20)
)
if mibBuilder.loadTexts:
    acModularGWModuleTable.setStatus("current")
_AcModularGWModuleEntry_Object = MibTableRow
acModularGWModuleEntry = _AcModularGWModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1)
)
acModularGWModuleEntry.setIndexNames(
    (0, "AC-ModularGW-MIB", "acModularGWModuleIndex"),
)
if mibBuilder.loadTexts:
    acModularGWModuleEntry.setStatus("current")


class _AcModularGWModuleIndex_Type(Integer32):
    """Custom type acModularGWModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcModularGWModuleIndex_Type.__name__ = "Integer32"
_AcModularGWModuleIndex_Object = MibTableColumn
acModularGWModuleIndex = _AcModularGWModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 1),
    _AcModularGWModuleIndex_Type()
)
acModularGWModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acModularGWModuleIndex.setStatus("deprecated")


class _AcModularGWModuleType_Type(Integer32):
    """Custom type acModularGWModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e1-t1-FALC56", 4),
          ("e1-t1-QUAD", 0),
          ("fxo", 2),
          ("fxs", 1))
    )


_AcModularGWModuleType_Type.__name__ = "Integer32"
_AcModularGWModuleType_Object = MibTableColumn
acModularGWModuleType = _AcModularGWModuleType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 2),
    _AcModularGWModuleType_Type()
)
acModularGWModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModularGWModuleType.setStatus("deprecated")


class _AcModularGWModuleNumOfPorts_Type(Integer32):
    """Custom type acModularGWModuleNumOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcModularGWModuleNumOfPorts_Type.__name__ = "Integer32"
_AcModularGWModuleNumOfPorts_Object = MibTableColumn
acModularGWModuleNumOfPorts = _AcModularGWModuleNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 3),
    _AcModularGWModuleNumOfPorts_Type()
)
acModularGWModuleNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModularGWModuleNumOfPorts.setStatus("deprecated")


class _AcModularGWModuleFirstPortNum_Type(Integer32):
    """Custom type acModularGWModuleFirstPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_AcModularGWModuleFirstPortNum_Type.__name__ = "Integer32"
_AcModularGWModuleFirstPortNum_Object = MibTableColumn
acModularGWModuleFirstPortNum = _AcModularGWModuleFirstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 4),
    _AcModularGWModuleFirstPortNum_Type()
)
acModularGWModuleFirstPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModularGWModuleFirstPortNum.setStatus("deprecated")
_AcModularGWCrossReference_ObjectIdentity = ObjectIdentity
acModularGWCrossReference = _AcModularGWCrossReference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2)
)
_AcModularGWTrunkTable_Object = MibTable
acModularGWTrunkTable = _AcModularGWTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20)
)
if mibBuilder.loadTexts:
    acModularGWTrunkTable.setStatus("current")
_AcModularGWTrunkEntry_Object = MibTableRow
acModularGWTrunkEntry = _AcModularGWTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1)
)
acModularGWTrunkEntry.setIndexNames(
    (0, "AC-ModularGW-MIB", "acModularGWTrunkIndex"),
)
if mibBuilder.loadTexts:
    acModularGWTrunkEntry.setStatus("current")


class _AcModularGWTrunkIndex_Type(Integer32):
    """Custom type acModularGWTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AcModularGWTrunkIndex_Type.__name__ = "Integer32"
_AcModularGWTrunkIndex_Object = MibTableColumn
acModularGWTrunkIndex = _AcModularGWTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 1),
    _AcModularGWTrunkIndex_Type()
)
acModularGWTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acModularGWTrunkIndex.setStatus("deprecated")


class _AcModularGWTrunkOnModuleNum_Type(Integer32):
    """Custom type acModularGWTrunkOnModuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcModularGWTrunkOnModuleNum_Type.__name__ = "Integer32"
_AcModularGWTrunkOnModuleNum_Object = MibTableColumn
acModularGWTrunkOnModuleNum = _AcModularGWTrunkOnModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 2),
    _AcModularGWTrunkOnModuleNum_Type()
)
acModularGWTrunkOnModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModularGWTrunkOnModuleNum.setStatus("deprecated")


class _AcModularGWTrunkOnPortNum_Type(Integer32):
    """Custom type acModularGWTrunkOnPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcModularGWTrunkOnPortNum_Type.__name__ = "Integer32"
_AcModularGWTrunkOnPortNum_Object = MibTableColumn
acModularGWTrunkOnPortNum = _AcModularGWTrunkOnPortNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 3),
    _AcModularGWTrunkOnPortNum_Type()
)
acModularGWTrunkOnPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModularGWTrunkOnPortNum.setStatus("deprecated")
_AcModularGWAnalogPortTable_Object = MibTable
acModularGWAnalogPortTable = _AcModularGWAnalogPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21)
)
if mibBuilder.loadTexts:
    acModularGWAnalogPortTable.setStatus("current")
_AcModularGWAnalogPortEntry_Object = MibTableRow
acModularGWAnalogPortEntry = _AcModularGWAnalogPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1)
)
acModularGWAnalogPortEntry.setIndexNames(
    (0, "AC-ModularGW-MIB", "acModularGWAnalogPortIndex"),
)
if mibBuilder.loadTexts:
    acModularGWAnalogPortEntry.setStatus("current")


class _AcModularGWAnalogPortIndex_Type(Integer32):
    """Custom type acModularGWAnalogPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AcModularGWAnalogPortIndex_Type.__name__ = "Integer32"
_AcModularGWAnalogPortIndex_Object = MibTableColumn
acModularGWAnalogPortIndex = _AcModularGWAnalogPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 1),
    _AcModularGWAnalogPortIndex_Type()
)
acModularGWAnalogPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acModularGWAnalogPortIndex.setStatus("deprecated")


class _AcModularGWAnalogPortOnModuleNum_Type(Integer32):
    """Custom type acModularGWAnalogPortOnModuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcModularGWAnalogPortOnModuleNum_Type.__name__ = "Integer32"
_AcModularGWAnalogPortOnModuleNum_Object = MibTableColumn
acModularGWAnalogPortOnModuleNum = _AcModularGWAnalogPortOnModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 2),
    _AcModularGWAnalogPortOnModuleNum_Type()
)
acModularGWAnalogPortOnModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModularGWAnalogPortOnModuleNum.setStatus("deprecated")


class _AcModularGWAnalogPortOnPortNum_Type(Integer32):
    """Custom type acModularGWAnalogPortOnPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcModularGWAnalogPortOnPortNum_Type.__name__ = "Integer32"
_AcModularGWAnalogPortOnPortNum_Object = MibTableColumn
acModularGWAnalogPortOnPortNum = _AcModularGWAnalogPortOnPortNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 3),
    _AcModularGWAnalogPortOnPortNum_Type()
)
acModularGWAnalogPortOnPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acModularGWAnalogPortOnPortNum.setStatus("deprecated")
_AcModularGatewayAction_ObjectIdentity = ObjectIdentity
acModularGatewayAction = _AcModularGatewayAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-ModularGW-MIB",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acProducts": acProducts,
       "acBoardMibs": acBoardMibs,
       "acModularGateway": acModularGateway,
       "acModularGatewayConfiguration": acModularGatewayConfiguration,
       "acModularGatewayStatus": acModularGatewayStatus,
       "acModularGWModules": acModularGWModules,
       "acModularGWModuleTable": acModularGWModuleTable,
       "acModularGWModuleEntry": acModularGWModuleEntry,
       "acModularGWModuleIndex": acModularGWModuleIndex,
       "acModularGWModuleType": acModularGWModuleType,
       "acModularGWModuleNumOfPorts": acModularGWModuleNumOfPorts,
       "acModularGWModuleFirstPortNum": acModularGWModuleFirstPortNum,
       "acModularGWCrossReference": acModularGWCrossReference,
       "acModularGWTrunkTable": acModularGWTrunkTable,
       "acModularGWTrunkEntry": acModularGWTrunkEntry,
       "acModularGWTrunkIndex": acModularGWTrunkIndex,
       "acModularGWTrunkOnModuleNum": acModularGWTrunkOnModuleNum,
       "acModularGWTrunkOnPortNum": acModularGWTrunkOnPortNum,
       "acModularGWAnalogPortTable": acModularGWAnalogPortTable,
       "acModularGWAnalogPortEntry": acModularGWAnalogPortEntry,
       "acModularGWAnalogPortIndex": acModularGWAnalogPortIndex,
       "acModularGWAnalogPortOnModuleNum": acModularGWAnalogPortOnModuleNum,
       "acModularGWAnalogPortOnPortNum": acModularGWAnalogPortOnPortNum,
       "acModularGatewayAction": acModularGatewayAction}
)
