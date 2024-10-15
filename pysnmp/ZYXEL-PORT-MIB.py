# SNMP MIB module (ZYXEL-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:35 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPortSetup_ObjectIdentity = ObjectIdentity
zyxelPortSetup = _ZyxelPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1)
)
_ZyxelPortTable_Object = MibTable
zyxelPortTable = _ZyxelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelPortTable.setStatus("current")
_ZyxelPortEntry_Object = MibTableRow
zyxelPortEntry = _ZyxelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1)
)
zyxelPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPortEntry.setStatus("current")


class _ZyPortSpeedDuplex_Type(Integer32):
    """Custom type zyPortSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed10000Full", 6),
          ("speed1000Auto", 9),
          ("speed1000Full", 5),
          ("speed100Full", 4),
          ("speed100Half", 3),
          ("speed10Full", 2),
          ("speed10Half", 1),
          ("speed12000Full", 7),
          ("speed40000Full", 8),
          ("speedAuto1000", 10),
          ("speedAuto10000", 11))
    )


_ZyPortSpeedDuplex_Type.__name__ = "Integer32"
_ZyPortSpeedDuplex_Object = MibTableColumn
zyPortSpeedDuplex = _ZyPortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 1),
    _ZyPortSpeedDuplex_Type()
)
zyPortSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortSpeedDuplex.setStatus("current")
_ZyPortFlowControlState_Type = EnabledStatus
_ZyPortFlowControlState_Object = MibTableColumn
zyPortFlowControlState = _ZyPortFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 2),
    _ZyPortFlowControlState_Type()
)
zyPortFlowControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortFlowControlState.setStatus("current")
_ZyPortName_Type = DisplayString
_ZyPortName_Object = MibTableColumn
zyPortName = _ZyPortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 3),
    _ZyPortName_Type()
)
zyPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortName.setStatus("current")
_ZyPortIntrusionLockState_Type = EnabledStatus
_ZyPortIntrusionLockState_Object = MibTableColumn
zyPortIntrusionLockState = _ZyPortIntrusionLockState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 4),
    _ZyPortIntrusionLockState_Type()
)
zyPortIntrusionLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortIntrusionLockState.setStatus("current")


class _ZyPortCX4CableLength_Type(Integer32):
    """Custom type zyPortCX4CableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMeters", 5),
          ("fiveMeters", 3),
          ("halfMeters", 0),
          ("oneMeters", 1),
          ("tenMeters", 4),
          ("threeMeters", 2))
    )


_ZyPortCX4CableLength_Type.__name__ = "Integer32"
_ZyPortCX4CableLength_Object = MibTableColumn
zyPortCX4CableLength = _ZyPortCX4CableLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 5),
    _ZyPortCX4CableLength_Type()
)
zyPortCX4CableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortCX4CableLength.setStatus("current")


class _ZyPort10GMediaType_Type(Integer32):
    """Custom type zyPort10GMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dac10g", 1),
          ("sfpPlus", 0))
    )


_ZyPort10GMediaType_Type.__name__ = "Integer32"
_ZyPort10GMediaType_Object = MibTableColumn
zyPort10GMediaType = _ZyPort10GMediaType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 1, 1, 1, 6),
    _ZyPort10GMediaType_Type()
)
zyPort10GMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPort10GMediaType.setStatus("current")
_ZyxelPortStatus_ObjectIdentity = ObjectIdentity
zyxelPortStatus = _ZyxelPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2)
)
_ZyxelPortInfoTable_Object = MibTable
zyxelPortInfoTable = _ZyxelPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelPortInfoTable.setStatus("current")
_ZyxelPortInfoEntry_Object = MibTableRow
zyxelPortInfoEntry = _ZyxelPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1)
)
zyxelPortInfoEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPortInfoEntry.setStatus("current")


class _ZyPortModuleType_Type(Integer32):
    """Custom type zyPortModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fastEthernet", 0),
          ("gigabitEthernet", 1),
          ("x1Ethernet40000", 3),
          ("xgEthernet10000", 2))
    )


_ZyPortModuleType_Type.__name__ = "Integer32"
_ZyPortModuleType_Object = MibTableColumn
zyPortModuleType = _ZyPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1, 1),
    _ZyPortModuleType_Type()
)
zyPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPortModuleType.setStatus("current")


class _ZyPortLinkUpType_Type(Integer32):
    """Custom type zyPortLinkUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("cx4", 4),
          ("down", 0),
          ("fiber", 2),
          ("xfp", 3))
    )


_ZyPortLinkUpType_Type.__name__ = "Integer32"
_ZyPortLinkUpType_Object = MibTableColumn
zyPortLinkUpType = _ZyPortLinkUpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1, 2),
    _ZyPortLinkUpType_Type()
)
zyPortLinkUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPortLinkUpType.setStatus("current")


class _ZyPortTestStatus_Type(Integer32):
    """Custom type zyPortTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("none", 0),
          ("success", 2),
          ("underTesting", 1))
    )


_ZyPortTestStatus_Type.__name__ = "Integer32"
_ZyPortTestStatus_Object = MibTableColumn
zyPortTestStatus = _ZyPortTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1, 3),
    _ZyPortTestStatus_Type()
)
zyPortTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPortTestStatus.setStatus("current")
_ZyPortCounterReset_Type = EnabledStatus
_ZyPortCounterReset_Object = MibTableColumn
zyPortCounterReset = _ZyPortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 2, 1, 1, 4),
    _ZyPortCounterReset_Type()
)
zyPortCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortCounterReset.setStatus("current")
_ZyxelPortNotifications_ObjectIdentity = ObjectIdentity
zyxelPortNotifications = _ZyxelPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 3)
)

# Managed Objects groups


# Notification objects

zyPortAutonegotiationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 3, 1)
)
zyPortAutonegotiationFailed.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPortAutonegotiationFailed.setStatus(
        "current"
    )

zyPortIntrusionLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 3, 2)
)
zyPortIntrusionLock.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPortIntrusionLock.setStatus(
        "current"
    )

zyPortAutonegotiationFailedRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 61, 3, 3)
)
zyPortAutonegotiationFailedRecovered.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPortAutonegotiationFailedRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PORT-MIB",
    **{"zyxelPort": zyxelPort,
       "zyxelPortSetup": zyxelPortSetup,
       "zyxelPortTable": zyxelPortTable,
       "zyxelPortEntry": zyxelPortEntry,
       "zyPortSpeedDuplex": zyPortSpeedDuplex,
       "zyPortFlowControlState": zyPortFlowControlState,
       "zyPortName": zyPortName,
       "zyPortIntrusionLockState": zyPortIntrusionLockState,
       "zyPortCX4CableLength": zyPortCX4CableLength,
       "zyPort10GMediaType": zyPort10GMediaType,
       "zyxelPortStatus": zyxelPortStatus,
       "zyxelPortInfoTable": zyxelPortInfoTable,
       "zyxelPortInfoEntry": zyxelPortInfoEntry,
       "zyPortModuleType": zyPortModuleType,
       "zyPortLinkUpType": zyPortLinkUpType,
       "zyPortTestStatus": zyPortTestStatus,
       "zyPortCounterReset": zyPortCounterReset,
       "zyxelPortNotifications": zyxelPortNotifications,
       "zyPortAutonegotiationFailed": zyPortAutonegotiationFailed,
       "zyPortIntrusionLock": zyPortIntrusionLock,
       "zyPortAutonegotiationFailedRecovered": zyPortAutonegotiationFailedRecovered}
)
