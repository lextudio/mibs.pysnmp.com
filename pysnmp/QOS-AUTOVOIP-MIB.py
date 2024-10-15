# SNMP MIB module (QOS-AUTOVOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QOS-AUTOVOIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:56 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(qos,) = mibBuilder.importSymbols(
    "QOS-MIB",
    "qos")

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

qosAUTOVOIP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PercentByFives(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(35, 35),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(55, 55),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(65, 65),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(85, 85),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(95, 95),
        ValueRangeConstraint(100, 100),
    )



class Sixteenths(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_AgentAutoVoIPCfgGroup_ObjectIdentity = ObjectIdentity
agentAutoVoIPCfgGroup = _AgentAutoVoIPCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 4, 1)
)
_AgentAutoVoIPTable_Object = MibTable
agentAutoVoIPTable = _AgentAutoVoIPTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    agentAutoVoIPTable.setStatus("current")
_AgentAutoVoIPEntry_Object = MibTableRow
agentAutoVoIPEntry = _AgentAutoVoIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 4, 1, 1, 1)
)
agentAutoVoIPEntry.setIndexNames(
    (0, "QOS-AUTOVOIP-MIB", "agentAutoVoIPIntfIndex"),
)
if mibBuilder.loadTexts:
    agentAutoVoIPEntry.setStatus("current")
_AgentAutoVoIPIntfIndex_Type = InterfaceIndexOrZero
_AgentAutoVoIPIntfIndex_Object = MibTableColumn
agentAutoVoIPIntfIndex = _AgentAutoVoIPIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 4, 1, 1, 1, 1),
    _AgentAutoVoIPIntfIndex_Type()
)
agentAutoVoIPIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAutoVoIPIntfIndex.setStatus("current")


class _AgentAutoVoIPMode_Type(Integer32):
    """Custom type agentAutoVoIPMode based on Integer32"""
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


_AgentAutoVoIPMode_Type.__name__ = "Integer32"
_AgentAutoVoIPMode_Object = MibTableColumn
agentAutoVoIPMode = _AgentAutoVoIPMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 4, 1, 1, 1, 2),
    _AgentAutoVoIPMode_Type()
)
agentAutoVoIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPMode.setStatus("current")


class _AgentAutoVoIPCosQueue_Type(Unsigned32):
    """Custom type agentAutoVoIPCosQueue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentAutoVoIPCosQueue_Type.__name__ = "Unsigned32"
_AgentAutoVoIPCosQueue_Object = MibTableColumn
agentAutoVoIPCosQueue = _AgentAutoVoIPCosQueue_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 3, 4, 1, 1, 1, 3),
    _AgentAutoVoIPCosQueue_Type()
)
agentAutoVoIPCosQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPCosQueue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QOS-AUTOVOIP-MIB",
    **{"PercentByFives": PercentByFives,
       "Sixteenths": Sixteenths,
       "qosAUTOVOIP": qosAUTOVOIP,
       "agentAutoVoIPCfgGroup": agentAutoVoIPCfgGroup,
       "agentAutoVoIPTable": agentAutoVoIPTable,
       "agentAutoVoIPEntry": agentAutoVoIPEntry,
       "agentAutoVoIPIntfIndex": agentAutoVoIPIntfIndex,
       "agentAutoVoIPMode": agentAutoVoIPMode,
       "agentAutoVoIPCosQueue": agentAutoVoIPCosQueue}
)
