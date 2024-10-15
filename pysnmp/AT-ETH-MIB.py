# SNMP MIB module (AT-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-ETH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:08 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ethernet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23)
)
ethernet.setRevisions(
        ("2006-06-28 12:22",
         "2013-02-07 13:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthernetTraps_ObjectIdentity = ObjectIdentity
ethernetTraps = _EthernetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 0)
)
_EthIntTable_Object = MibTable
ethIntTable = _EthIntTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1)
)
if mibBuilder.loadTexts:
    ethIntTable.setStatus("current")
_EthIntEntry_Object = MibTableRow
ethIntEntry = _EthIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1)
)
ethIntEntry.setIndexNames(
    (0, "AT-ETH-MIB", "ethIntIndex"),
)
if mibBuilder.loadTexts:
    ethIntEntry.setStatus("current")
_EthIntIndex_Type = Integer32
_EthIntIndex_Object = MibTableColumn
ethIntIndex = _EthIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 1),
    _EthIntIndex_Type()
)
ethIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntIndex.setStatus("current")
_EthIntBoardIndex_Type = Integer32
_EthIntBoardIndex_Object = MibTableColumn
ethIntBoardIndex = _EthIntBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 2),
    _EthIntBoardIndex_Type()
)
ethIntBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntBoardIndex.setStatus("current")
_EthIntBoardPosition_Type = Integer32
_EthIntBoardPosition_Object = MibTableColumn
ethIntBoardPosition = _EthIntBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 3),
    _EthIntBoardPosition_Type()
)
ethIntBoardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntBoardPosition.setStatus("current")


class _EthIntDuplexMode_Type(Integer32):
    """Custom type ethIntDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("unknown", 3))
    )


_EthIntDuplexMode_Type.__name__ = "Integer32"
_EthIntDuplexMode_Object = MibTableColumn
ethIntDuplexMode = _EthIntDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 4),
    _EthIntDuplexMode_Type()
)
ethIntDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntDuplexMode.setStatus("current")


class _EthBandwidth_Type(Integer32):
    """Custom type ethBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_EthBandwidth_Type.__name__ = "Integer32"
_EthBandwidth_Object = MibTableColumn
ethBandwidth = _EthBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 1, 1, 5),
    _EthBandwidth_Type()
)
ethBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ethBandwidth.setUnits("kbps")
_EthernetTrapMessage_Type = DisplayString
_EthernetTrapMessage_Object = MibScalar
ethernetTrapMessage = _EthernetTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 2),
    _EthernetTrapMessage_Type()
)
ethernetTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetTrapMessage.setStatus("current")

# Managed Objects groups


# Notification objects

ethernetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 23, 0, 1)
)
ethernetTrap.setObjects(
    ("AT-ETH-MIB", "ethernetTrapMessage")
)
if mibBuilder.loadTexts:
    ethernetTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-ETH-MIB",
    **{"ethernet": ethernet,
       "ethernetTraps": ethernetTraps,
       "ethernetTrap": ethernetTrap,
       "ethIntTable": ethIntTable,
       "ethIntEntry": ethIntEntry,
       "ethIntIndex": ethIntIndex,
       "ethIntBoardIndex": ethIntBoardIndex,
       "ethIntBoardPosition": ethIntBoardPosition,
       "ethIntDuplexMode": ethIntDuplexMode,
       "ethBandwidth": ethBandwidth,
       "ethernetTrapMessage": ethernetTrapMessage}
)
