# SNMP MIB module (HH3C-STORM-CONSTRAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-STORM-CONSTRAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:02 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cStormConstrain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cStormConstrainUnit(Integer32, TextualConvention):
    status = "current"
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
        *(("bytesPerSecond", 4),
          ("kbitsPerSecond", 5),
          ("none", 1),
          ("packetsPerSecond", 2),
          ("ratio", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cStormScalarGroup_ObjectIdentity = ObjectIdentity
hh3cStormScalarGroup = _Hh3cStormScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 1)
)


class _Hh3cStormTrapType_Type(Integer32):
    """Custom type hh3cStormTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_Hh3cStormTrapType_Type.__name__ = "Integer32"
_Hh3cStormTrapType_Object = MibScalar
hh3cStormTrapType = _Hh3cStormTrapType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 1, 1),
    _Hh3cStormTrapType_Type()
)
hh3cStormTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cStormTrapType.setStatus("current")
_Hh3cStormTrapThreshold_Type = Integer32
_Hh3cStormTrapThreshold_Object = MibScalar
hh3cStormTrapThreshold = _Hh3cStormTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 1, 2),
    _Hh3cStormTrapThreshold_Type()
)
hh3cStormTrapThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cStormTrapThreshold.setStatus("current")
_Hh3cStormTableGroup_ObjectIdentity = ObjectIdentity
hh3cStormTableGroup = _Hh3cStormTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2)
)
_Hh3cStormCtrlTable_Object = MibTable
hh3cStormCtrlTable = _Hh3cStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cStormCtrlTable.setStatus("current")
_Hh3cStormCtrlEntry_Object = MibTableRow
hh3cStormCtrlEntry = _Hh3cStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1)
)
hh3cStormCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cStormCtrlEntry.setStatus("current")


class _Hh3cStormCtrlPortStatus_Type(Integer32):
    """Custom type hh3cStormCtrlPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlled", 1),
          ("normal", 2))
    )


_Hh3cStormCtrlPortStatus_Type.__name__ = "Integer32"
_Hh3cStormCtrlPortStatus_Object = MibTableColumn
hh3cStormCtrlPortStatus = _Hh3cStormCtrlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 1),
    _Hh3cStormCtrlPortStatus_Type()
)
hh3cStormCtrlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStormCtrlPortStatus.setStatus("current")
_Hh3cStormCtrlBroadcastUnit_Type = Hh3cStormConstrainUnit
_Hh3cStormCtrlBroadcastUnit_Object = MibTableColumn
hh3cStormCtrlBroadcastUnit = _Hh3cStormCtrlBroadcastUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 2),
    _Hh3cStormCtrlBroadcastUnit_Type()
)
hh3cStormCtrlBroadcastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlBroadcastUnit.setStatus("current")
_Hh3cStormCtrlBroadcastUpper_Type = Integer32
_Hh3cStormCtrlBroadcastUpper_Object = MibTableColumn
hh3cStormCtrlBroadcastUpper = _Hh3cStormCtrlBroadcastUpper_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 3),
    _Hh3cStormCtrlBroadcastUpper_Type()
)
hh3cStormCtrlBroadcastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlBroadcastUpper.setStatus("current")
_Hh3cStormCtrlBroadcastLower_Type = Integer32
_Hh3cStormCtrlBroadcastLower_Object = MibTableColumn
hh3cStormCtrlBroadcastLower = _Hh3cStormCtrlBroadcastLower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 4),
    _Hh3cStormCtrlBroadcastLower_Type()
)
hh3cStormCtrlBroadcastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlBroadcastLower.setStatus("current")
_Hh3cStormCtrlMulticastUnit_Type = Hh3cStormConstrainUnit
_Hh3cStormCtrlMulticastUnit_Object = MibTableColumn
hh3cStormCtrlMulticastUnit = _Hh3cStormCtrlMulticastUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 5),
    _Hh3cStormCtrlMulticastUnit_Type()
)
hh3cStormCtrlMulticastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlMulticastUnit.setStatus("current")
_Hh3cStormCtrlMulticastUpper_Type = Integer32
_Hh3cStormCtrlMulticastUpper_Object = MibTableColumn
hh3cStormCtrlMulticastUpper = _Hh3cStormCtrlMulticastUpper_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 6),
    _Hh3cStormCtrlMulticastUpper_Type()
)
hh3cStormCtrlMulticastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlMulticastUpper.setStatus("current")
_Hh3cStormCtrlMulticastLower_Type = Integer32
_Hh3cStormCtrlMulticastLower_Object = MibTableColumn
hh3cStormCtrlMulticastLower = _Hh3cStormCtrlMulticastLower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 7),
    _Hh3cStormCtrlMulticastLower_Type()
)
hh3cStormCtrlMulticastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlMulticastLower.setStatus("current")
_Hh3cStormCtrlUnicastUnit_Type = Hh3cStormConstrainUnit
_Hh3cStormCtrlUnicastUnit_Object = MibTableColumn
hh3cStormCtrlUnicastUnit = _Hh3cStormCtrlUnicastUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 8),
    _Hh3cStormCtrlUnicastUnit_Type()
)
hh3cStormCtrlUnicastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlUnicastUnit.setStatus("current")
_Hh3cStormCtrlUnicastUpper_Type = Integer32
_Hh3cStormCtrlUnicastUpper_Object = MibTableColumn
hh3cStormCtrlUnicastUpper = _Hh3cStormCtrlUnicastUpper_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 9),
    _Hh3cStormCtrlUnicastUpper_Type()
)
hh3cStormCtrlUnicastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlUnicastUpper.setStatus("current")
_Hh3cStormCtrlUnicastLower_Type = Integer32
_Hh3cStormCtrlUnicastLower_Object = MibTableColumn
hh3cStormCtrlUnicastLower = _Hh3cStormCtrlUnicastLower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 10),
    _Hh3cStormCtrlUnicastLower_Type()
)
hh3cStormCtrlUnicastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlUnicastLower.setStatus("current")
_Hh3cStormCtrlRowStatus_Type = RowStatus
_Hh3cStormCtrlRowStatus_Object = MibTableColumn
hh3cStormCtrlRowStatus = _Hh3cStormCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 11),
    _Hh3cStormCtrlRowStatus_Type()
)
hh3cStormCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlRowStatus.setStatus("current")


class _Hh3cStormCtrlPortMode_Type(Integer32):
    """Custom type hh3cStormCtrlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("none", 1),
          ("shutdown", 3))
    )


_Hh3cStormCtrlPortMode_Type.__name__ = "Integer32"
_Hh3cStormCtrlPortMode_Object = MibTableColumn
hh3cStormCtrlPortMode = _Hh3cStormCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 2, 1, 1, 12),
    _Hh3cStormCtrlPortMode_Type()
)
hh3cStormCtrlPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStormCtrlPortMode.setStatus("current")
_Hh3cStormNotifications_ObjectIdentity = ObjectIdentity
hh3cStormNotifications = _Hh3cStormNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 3)
)

# Managed Objects groups


# Notification objects

hh3cStormRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 3, 1)
)
hh3cStormRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-STORM-CONSTRAIN-MIB", "hh3cStormTrapType"),
        ("HH3C-STORM-CONSTRAIN-MIB", "hh3cStormTrapThreshold"),
        ("HH3C-STORM-CONSTRAIN-MIB", "hh3cStormCtrlPortStatus"))
)
if mibBuilder.loadTexts:
    hh3cStormRising.setStatus(
        "current"
    )

hh3cStormFalling = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66, 3, 2)
)
hh3cStormFalling.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-STORM-CONSTRAIN-MIB", "hh3cStormTrapType"),
        ("HH3C-STORM-CONSTRAIN-MIB", "hh3cStormTrapThreshold"),
        ("HH3C-STORM-CONSTRAIN-MIB", "hh3cStormCtrlPortStatus"))
)
if mibBuilder.loadTexts:
    hh3cStormFalling.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-STORM-CONSTRAIN-MIB",
    **{"Hh3cStormConstrainUnit": Hh3cStormConstrainUnit,
       "hh3cStormConstrain": hh3cStormConstrain,
       "hh3cStormScalarGroup": hh3cStormScalarGroup,
       "hh3cStormTrapType": hh3cStormTrapType,
       "hh3cStormTrapThreshold": hh3cStormTrapThreshold,
       "hh3cStormTableGroup": hh3cStormTableGroup,
       "hh3cStormCtrlTable": hh3cStormCtrlTable,
       "hh3cStormCtrlEntry": hh3cStormCtrlEntry,
       "hh3cStormCtrlPortStatus": hh3cStormCtrlPortStatus,
       "hh3cStormCtrlBroadcastUnit": hh3cStormCtrlBroadcastUnit,
       "hh3cStormCtrlBroadcastUpper": hh3cStormCtrlBroadcastUpper,
       "hh3cStormCtrlBroadcastLower": hh3cStormCtrlBroadcastLower,
       "hh3cStormCtrlMulticastUnit": hh3cStormCtrlMulticastUnit,
       "hh3cStormCtrlMulticastUpper": hh3cStormCtrlMulticastUpper,
       "hh3cStormCtrlMulticastLower": hh3cStormCtrlMulticastLower,
       "hh3cStormCtrlUnicastUnit": hh3cStormCtrlUnicastUnit,
       "hh3cStormCtrlUnicastUpper": hh3cStormCtrlUnicastUpper,
       "hh3cStormCtrlUnicastLower": hh3cStormCtrlUnicastLower,
       "hh3cStormCtrlRowStatus": hh3cStormCtrlRowStatus,
       "hh3cStormCtrlPortMode": hh3cStormCtrlPortMode,
       "hh3cStormNotifications": hh3cStormNotifications,
       "hh3cStormRising": hh3cStormRising,
       "hh3cStormFalling": hh3cStormFalling}
)
