# SNMP MIB module (A3COM-HUAWEI-STORM-CONSTRAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-STORM-CONSTRAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:07 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cStormConstrain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cStormConstrainUnit(Integer32, TextualConvention):
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

_H3cStormScalarGroup_ObjectIdentity = ObjectIdentity
h3cStormScalarGroup = _H3cStormScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 1)
)


class _H3cStormTrapType_Type(Integer32):
    """Custom type h3cStormTrapType based on Integer32"""
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


_H3cStormTrapType_Type.__name__ = "Integer32"
_H3cStormTrapType_Object = MibScalar
h3cStormTrapType = _H3cStormTrapType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 1, 1),
    _H3cStormTrapType_Type()
)
h3cStormTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cStormTrapType.setStatus("current")
_H3cStormTrapThreshold_Type = Integer32
_H3cStormTrapThreshold_Object = MibScalar
h3cStormTrapThreshold = _H3cStormTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 1, 2),
    _H3cStormTrapThreshold_Type()
)
h3cStormTrapThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cStormTrapThreshold.setStatus("current")
_H3cStormTableGroup_ObjectIdentity = ObjectIdentity
h3cStormTableGroup = _H3cStormTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2)
)
_H3cStormCtrlTable_Object = MibTable
h3cStormCtrlTable = _H3cStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1)
)
if mibBuilder.loadTexts:
    h3cStormCtrlTable.setStatus("current")
_H3cStormCtrlEntry_Object = MibTableRow
h3cStormCtrlEntry = _H3cStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1)
)
h3cStormCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cStormCtrlEntry.setStatus("current")


class _H3cStormCtrlPortStatus_Type(Integer32):
    """Custom type h3cStormCtrlPortStatus based on Integer32"""
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


_H3cStormCtrlPortStatus_Type.__name__ = "Integer32"
_H3cStormCtrlPortStatus_Object = MibTableColumn
h3cStormCtrlPortStatus = _H3cStormCtrlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 1),
    _H3cStormCtrlPortStatus_Type()
)
h3cStormCtrlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cStormCtrlPortStatus.setStatus("current")
_H3cStormCtrlBroadcastUnit_Type = H3cStormConstrainUnit
_H3cStormCtrlBroadcastUnit_Object = MibTableColumn
h3cStormCtrlBroadcastUnit = _H3cStormCtrlBroadcastUnit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 2),
    _H3cStormCtrlBroadcastUnit_Type()
)
h3cStormCtrlBroadcastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlBroadcastUnit.setStatus("current")
_H3cStormCtrlBroadcastUpper_Type = Integer32
_H3cStormCtrlBroadcastUpper_Object = MibTableColumn
h3cStormCtrlBroadcastUpper = _H3cStormCtrlBroadcastUpper_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 3),
    _H3cStormCtrlBroadcastUpper_Type()
)
h3cStormCtrlBroadcastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlBroadcastUpper.setStatus("current")
_H3cStormCtrlBroadcastLower_Type = Integer32
_H3cStormCtrlBroadcastLower_Object = MibTableColumn
h3cStormCtrlBroadcastLower = _H3cStormCtrlBroadcastLower_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 4),
    _H3cStormCtrlBroadcastLower_Type()
)
h3cStormCtrlBroadcastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlBroadcastLower.setStatus("current")
_H3cStormCtrlMulticastUnit_Type = H3cStormConstrainUnit
_H3cStormCtrlMulticastUnit_Object = MibTableColumn
h3cStormCtrlMulticastUnit = _H3cStormCtrlMulticastUnit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 5),
    _H3cStormCtrlMulticastUnit_Type()
)
h3cStormCtrlMulticastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlMulticastUnit.setStatus("current")
_H3cStormCtrlMulticastUpper_Type = Integer32
_H3cStormCtrlMulticastUpper_Object = MibTableColumn
h3cStormCtrlMulticastUpper = _H3cStormCtrlMulticastUpper_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 6),
    _H3cStormCtrlMulticastUpper_Type()
)
h3cStormCtrlMulticastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlMulticastUpper.setStatus("current")
_H3cStormCtrlMulticastLower_Type = Integer32
_H3cStormCtrlMulticastLower_Object = MibTableColumn
h3cStormCtrlMulticastLower = _H3cStormCtrlMulticastLower_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 7),
    _H3cStormCtrlMulticastLower_Type()
)
h3cStormCtrlMulticastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlMulticastLower.setStatus("current")
_H3cStormCtrlUnicastUnit_Type = H3cStormConstrainUnit
_H3cStormCtrlUnicastUnit_Object = MibTableColumn
h3cStormCtrlUnicastUnit = _H3cStormCtrlUnicastUnit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 8),
    _H3cStormCtrlUnicastUnit_Type()
)
h3cStormCtrlUnicastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlUnicastUnit.setStatus("current")
_H3cStormCtrlUnicastUpper_Type = Integer32
_H3cStormCtrlUnicastUpper_Object = MibTableColumn
h3cStormCtrlUnicastUpper = _H3cStormCtrlUnicastUpper_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 9),
    _H3cStormCtrlUnicastUpper_Type()
)
h3cStormCtrlUnicastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlUnicastUpper.setStatus("current")
_H3cStormCtrlUnicastLower_Type = Integer32
_H3cStormCtrlUnicastLower_Object = MibTableColumn
h3cStormCtrlUnicastLower = _H3cStormCtrlUnicastLower_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 10),
    _H3cStormCtrlUnicastLower_Type()
)
h3cStormCtrlUnicastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlUnicastLower.setStatus("current")
_H3cStormCtrlRowStatus_Type = RowStatus
_H3cStormCtrlRowStatus_Object = MibTableColumn
h3cStormCtrlRowStatus = _H3cStormCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 11),
    _H3cStormCtrlRowStatus_Type()
)
h3cStormCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlRowStatus.setStatus("current")


class _H3cStormCtrlPortMode_Type(Integer32):
    """Custom type h3cStormCtrlPortMode based on Integer32"""
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


_H3cStormCtrlPortMode_Type.__name__ = "Integer32"
_H3cStormCtrlPortMode_Object = MibTableColumn
h3cStormCtrlPortMode = _H3cStormCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 2, 1, 1, 12),
    _H3cStormCtrlPortMode_Type()
)
h3cStormCtrlPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cStormCtrlPortMode.setStatus("current")
_H3cStormNotifications_ObjectIdentity = ObjectIdentity
h3cStormNotifications = _H3cStormNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 3)
)

# Managed Objects groups


# Notification objects

h3cStormRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 3, 1)
)
h3cStormRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("A3COM-HUAWEI-STORM-CONSTRAIN-MIB", "h3cStormTrapType"),
        ("A3COM-HUAWEI-STORM-CONSTRAIN-MIB", "h3cStormTrapThreshold"),
        ("A3COM-HUAWEI-STORM-CONSTRAIN-MIB", "h3cStormCtrlPortStatus"))
)
if mibBuilder.loadTexts:
    h3cStormRising.setStatus(
        "current"
    )

h3cStormFalling = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 66, 3, 2)
)
h3cStormFalling.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("A3COM-HUAWEI-STORM-CONSTRAIN-MIB", "h3cStormTrapType"),
        ("A3COM-HUAWEI-STORM-CONSTRAIN-MIB", "h3cStormTrapThreshold"),
        ("A3COM-HUAWEI-STORM-CONSTRAIN-MIB", "h3cStormCtrlPortStatus"))
)
if mibBuilder.loadTexts:
    h3cStormFalling.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-STORM-CONSTRAIN-MIB",
    **{"H3cStormConstrainUnit": H3cStormConstrainUnit,
       "h3cStormConstrain": h3cStormConstrain,
       "h3cStormScalarGroup": h3cStormScalarGroup,
       "h3cStormTrapType": h3cStormTrapType,
       "h3cStormTrapThreshold": h3cStormTrapThreshold,
       "h3cStormTableGroup": h3cStormTableGroup,
       "h3cStormCtrlTable": h3cStormCtrlTable,
       "h3cStormCtrlEntry": h3cStormCtrlEntry,
       "h3cStormCtrlPortStatus": h3cStormCtrlPortStatus,
       "h3cStormCtrlBroadcastUnit": h3cStormCtrlBroadcastUnit,
       "h3cStormCtrlBroadcastUpper": h3cStormCtrlBroadcastUpper,
       "h3cStormCtrlBroadcastLower": h3cStormCtrlBroadcastLower,
       "h3cStormCtrlMulticastUnit": h3cStormCtrlMulticastUnit,
       "h3cStormCtrlMulticastUpper": h3cStormCtrlMulticastUpper,
       "h3cStormCtrlMulticastLower": h3cStormCtrlMulticastLower,
       "h3cStormCtrlUnicastUnit": h3cStormCtrlUnicastUnit,
       "h3cStormCtrlUnicastUpper": h3cStormCtrlUnicastUpper,
       "h3cStormCtrlUnicastLower": h3cStormCtrlUnicastLower,
       "h3cStormCtrlRowStatus": h3cStormCtrlRowStatus,
       "h3cStormCtrlPortMode": h3cStormCtrlPortMode,
       "h3cStormNotifications": h3cStormNotifications,
       "h3cStormRising": h3cStormRising,
       "h3cStormFalling": h3cStormFalling}
)
