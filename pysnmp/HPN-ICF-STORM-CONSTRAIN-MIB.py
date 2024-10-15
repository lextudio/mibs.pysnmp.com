# SNMP MIB module (HPN-ICF-STORM-CONSTRAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-STORM-CONSTRAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:55 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfStormConstrain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfStormConstrainUnit(Integer32, TextualConvention):
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

_HpnicfStormScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfStormScalarGroup = _HpnicfStormScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 1)
)


class _HpnicfStormTrapType_Type(Integer32):
    """Custom type hpnicfStormTrapType based on Integer32"""
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


_HpnicfStormTrapType_Type.__name__ = "Integer32"
_HpnicfStormTrapType_Object = MibScalar
hpnicfStormTrapType = _HpnicfStormTrapType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 1, 1),
    _HpnicfStormTrapType_Type()
)
hpnicfStormTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfStormTrapType.setStatus("current")
_HpnicfStormTrapThreshold_Type = Integer32
_HpnicfStormTrapThreshold_Object = MibScalar
hpnicfStormTrapThreshold = _HpnicfStormTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 1, 2),
    _HpnicfStormTrapThreshold_Type()
)
hpnicfStormTrapThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfStormTrapThreshold.setStatus("current")
_HpnicfStormTableGroup_ObjectIdentity = ObjectIdentity
hpnicfStormTableGroup = _HpnicfStormTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2)
)
_HpnicfStormCtrlTable_Object = MibTable
hpnicfStormCtrlTable = _HpnicfStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfStormCtrlTable.setStatus("current")
_HpnicfStormCtrlEntry_Object = MibTableRow
hpnicfStormCtrlEntry = _HpnicfStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1)
)
hpnicfStormCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfStormCtrlEntry.setStatus("current")


class _HpnicfStormCtrlPortStatus_Type(Integer32):
    """Custom type hpnicfStormCtrlPortStatus based on Integer32"""
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


_HpnicfStormCtrlPortStatus_Type.__name__ = "Integer32"
_HpnicfStormCtrlPortStatus_Object = MibTableColumn
hpnicfStormCtrlPortStatus = _HpnicfStormCtrlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 1),
    _HpnicfStormCtrlPortStatus_Type()
)
hpnicfStormCtrlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStormCtrlPortStatus.setStatus("current")
_HpnicfStormCtrlBroadcastUnit_Type = HpnicfStormConstrainUnit
_HpnicfStormCtrlBroadcastUnit_Object = MibTableColumn
hpnicfStormCtrlBroadcastUnit = _HpnicfStormCtrlBroadcastUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 2),
    _HpnicfStormCtrlBroadcastUnit_Type()
)
hpnicfStormCtrlBroadcastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlBroadcastUnit.setStatus("current")
_HpnicfStormCtrlBroadcastUpper_Type = Integer32
_HpnicfStormCtrlBroadcastUpper_Object = MibTableColumn
hpnicfStormCtrlBroadcastUpper = _HpnicfStormCtrlBroadcastUpper_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 3),
    _HpnicfStormCtrlBroadcastUpper_Type()
)
hpnicfStormCtrlBroadcastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlBroadcastUpper.setStatus("current")
_HpnicfStormCtrlBroadcastLower_Type = Integer32
_HpnicfStormCtrlBroadcastLower_Object = MibTableColumn
hpnicfStormCtrlBroadcastLower = _HpnicfStormCtrlBroadcastLower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 4),
    _HpnicfStormCtrlBroadcastLower_Type()
)
hpnicfStormCtrlBroadcastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlBroadcastLower.setStatus("current")
_HpnicfStormCtrlMulticastUnit_Type = HpnicfStormConstrainUnit
_HpnicfStormCtrlMulticastUnit_Object = MibTableColumn
hpnicfStormCtrlMulticastUnit = _HpnicfStormCtrlMulticastUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 5),
    _HpnicfStormCtrlMulticastUnit_Type()
)
hpnicfStormCtrlMulticastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlMulticastUnit.setStatus("current")
_HpnicfStormCtrlMulticastUpper_Type = Integer32
_HpnicfStormCtrlMulticastUpper_Object = MibTableColumn
hpnicfStormCtrlMulticastUpper = _HpnicfStormCtrlMulticastUpper_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 6),
    _HpnicfStormCtrlMulticastUpper_Type()
)
hpnicfStormCtrlMulticastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlMulticastUpper.setStatus("current")
_HpnicfStormCtrlMulticastLower_Type = Integer32
_HpnicfStormCtrlMulticastLower_Object = MibTableColumn
hpnicfStormCtrlMulticastLower = _HpnicfStormCtrlMulticastLower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 7),
    _HpnicfStormCtrlMulticastLower_Type()
)
hpnicfStormCtrlMulticastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlMulticastLower.setStatus("current")
_HpnicfStormCtrlUnicastUnit_Type = HpnicfStormConstrainUnit
_HpnicfStormCtrlUnicastUnit_Object = MibTableColumn
hpnicfStormCtrlUnicastUnit = _HpnicfStormCtrlUnicastUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 8),
    _HpnicfStormCtrlUnicastUnit_Type()
)
hpnicfStormCtrlUnicastUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlUnicastUnit.setStatus("current")
_HpnicfStormCtrlUnicastUpper_Type = Integer32
_HpnicfStormCtrlUnicastUpper_Object = MibTableColumn
hpnicfStormCtrlUnicastUpper = _HpnicfStormCtrlUnicastUpper_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 9),
    _HpnicfStormCtrlUnicastUpper_Type()
)
hpnicfStormCtrlUnicastUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlUnicastUpper.setStatus("current")
_HpnicfStormCtrlUnicastLower_Type = Integer32
_HpnicfStormCtrlUnicastLower_Object = MibTableColumn
hpnicfStormCtrlUnicastLower = _HpnicfStormCtrlUnicastLower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 10),
    _HpnicfStormCtrlUnicastLower_Type()
)
hpnicfStormCtrlUnicastLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlUnicastLower.setStatus("current")
_HpnicfStormCtrlRowStatus_Type = RowStatus
_HpnicfStormCtrlRowStatus_Object = MibTableColumn
hpnicfStormCtrlRowStatus = _HpnicfStormCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 11),
    _HpnicfStormCtrlRowStatus_Type()
)
hpnicfStormCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlRowStatus.setStatus("current")


class _HpnicfStormCtrlPortMode_Type(Integer32):
    """Custom type hpnicfStormCtrlPortMode based on Integer32"""
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


_HpnicfStormCtrlPortMode_Type.__name__ = "Integer32"
_HpnicfStormCtrlPortMode_Object = MibTableColumn
hpnicfStormCtrlPortMode = _HpnicfStormCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 2, 1, 1, 12),
    _HpnicfStormCtrlPortMode_Type()
)
hpnicfStormCtrlPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStormCtrlPortMode.setStatus("current")
_HpnicfStormNotifications_ObjectIdentity = ObjectIdentity
hpnicfStormNotifications = _HpnicfStormNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 3)
)

# Managed Objects groups


# Notification objects

hpnicfStormRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 3, 1)
)
hpnicfStormRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-STORM-CONSTRAIN-MIB", "hpnicfStormTrapType"),
        ("HPN-ICF-STORM-CONSTRAIN-MIB", "hpnicfStormTrapThreshold"),
        ("HPN-ICF-STORM-CONSTRAIN-MIB", "hpnicfStormCtrlPortStatus"))
)
if mibBuilder.loadTexts:
    hpnicfStormRising.setStatus(
        "current"
    )

hpnicfStormFalling = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66, 3, 2)
)
hpnicfStormFalling.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-STORM-CONSTRAIN-MIB", "hpnicfStormTrapType"),
        ("HPN-ICF-STORM-CONSTRAIN-MIB", "hpnicfStormTrapThreshold"),
        ("HPN-ICF-STORM-CONSTRAIN-MIB", "hpnicfStormCtrlPortStatus"))
)
if mibBuilder.loadTexts:
    hpnicfStormFalling.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-STORM-CONSTRAIN-MIB",
    **{"HpnicfStormConstrainUnit": HpnicfStormConstrainUnit,
       "hpnicfStormConstrain": hpnicfStormConstrain,
       "hpnicfStormScalarGroup": hpnicfStormScalarGroup,
       "hpnicfStormTrapType": hpnicfStormTrapType,
       "hpnicfStormTrapThreshold": hpnicfStormTrapThreshold,
       "hpnicfStormTableGroup": hpnicfStormTableGroup,
       "hpnicfStormCtrlTable": hpnicfStormCtrlTable,
       "hpnicfStormCtrlEntry": hpnicfStormCtrlEntry,
       "hpnicfStormCtrlPortStatus": hpnicfStormCtrlPortStatus,
       "hpnicfStormCtrlBroadcastUnit": hpnicfStormCtrlBroadcastUnit,
       "hpnicfStormCtrlBroadcastUpper": hpnicfStormCtrlBroadcastUpper,
       "hpnicfStormCtrlBroadcastLower": hpnicfStormCtrlBroadcastLower,
       "hpnicfStormCtrlMulticastUnit": hpnicfStormCtrlMulticastUnit,
       "hpnicfStormCtrlMulticastUpper": hpnicfStormCtrlMulticastUpper,
       "hpnicfStormCtrlMulticastLower": hpnicfStormCtrlMulticastLower,
       "hpnicfStormCtrlUnicastUnit": hpnicfStormCtrlUnicastUnit,
       "hpnicfStormCtrlUnicastUpper": hpnicfStormCtrlUnicastUpper,
       "hpnicfStormCtrlUnicastLower": hpnicfStormCtrlUnicastLower,
       "hpnicfStormCtrlRowStatus": hpnicfStormCtrlRowStatus,
       "hpnicfStormCtrlPortMode": hpnicfStormCtrlPortMode,
       "hpnicfStormNotifications": hpnicfStormNotifications,
       "hpnicfStormRising": hpnicfStormRising,
       "hpnicfStormFalling": hpnicfStormFalling}
)
