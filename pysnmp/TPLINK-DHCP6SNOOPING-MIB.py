# SNMP MIB module (TPLINK-DHCP6SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-DHCP6SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:53 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkDhcp6SnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91)
)
tplinkDhcp6SnoopingMIB.setRevisions(
        ("2012-12-17 10:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcp6SnoopingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcp6SnoopingMIBObjects = _TplinkDhcp6SnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1)
)
_Dhcp6SnoopingGlobalConfig_ObjectIdentity = ObjectIdentity
dhcp6SnoopingGlobalConfig = _Dhcp6SnoopingGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 1)
)


class _Dhcp6SnoopingEnable_Type(Integer32):
    """Custom type dhcp6SnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Dhcp6SnoopingEnable_Type.__name__ = "Integer32"
_Dhcp6SnoopingEnable_Object = MibScalar
dhcp6SnoopingEnable = _Dhcp6SnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 1, 1),
    _Dhcp6SnoopingEnable_Type()
)
dhcp6SnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6SnoopingEnable.setStatus("current")
_Dhcp6SnoopingVlanConfigTable_Object = MibTable
dhcp6SnoopingVlanConfigTable = _Dhcp6SnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dhcp6SnoopingVlanConfigTable.setStatus("current")
_Dhcp6SnoopingVlanConfigEntry_Object = MibTableRow
dhcp6SnoopingVlanConfigEntry = _Dhcp6SnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 1, 2, 1)
)
dhcp6SnoopingVlanConfigEntry.setIndexNames(
    (0, "TPLINK-DHCP6SNOOPING-MIB", "dhcp6SnoopingVlanId"),
)
if mibBuilder.loadTexts:
    dhcp6SnoopingVlanConfigEntry.setStatus("current")


class _Dhcp6SnoopingVlanId_Type(Integer32):
    """Custom type dhcp6SnoopingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dhcp6SnoopingVlanId_Type.__name__ = "Integer32"
_Dhcp6SnoopingVlanId_Object = MibTableColumn
dhcp6SnoopingVlanId = _Dhcp6SnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 1, 2, 1, 1),
    _Dhcp6SnoopingVlanId_Type()
)
dhcp6SnoopingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcp6SnoopingVlanId.setStatus("current")


class _Dhcp6SnoopingVlanStatus_Type(Integer32):
    """Custom type dhcp6SnoopingVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Dhcp6SnoopingVlanStatus_Type.__name__ = "Integer32"
_Dhcp6SnoopingVlanStatus_Object = MibTableColumn
dhcp6SnoopingVlanStatus = _Dhcp6SnoopingVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 1, 2, 1, 2),
    _Dhcp6SnoopingVlanStatus_Type()
)
dhcp6SnoopingVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcp6SnoopingVlanStatus.setStatus("current")
_Dhcp6SnoopingPortConfig_ObjectIdentity = ObjectIdentity
dhcp6SnoopingPortConfig = _Dhcp6SnoopingPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 3)
)
_Dhcp6SnoopingPortConfigTable_Object = MibTable
dhcp6SnoopingPortConfigTable = _Dhcp6SnoopingPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dhcp6SnoopingPortConfigTable.setStatus("current")
_Dhcp6SnoopingPortConfigEntry_Object = MibTableRow
dhcp6SnoopingPortConfigEntry = _Dhcp6SnoopingPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 3, 1, 1)
)
dhcp6SnoopingPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcp6SnoopingPortConfigEntry.setStatus("current")


class _Dhcp6SnoopingPort_Type(OctetString):
    """Custom type dhcp6SnoopingPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dhcp6SnoopingPort_Type.__name__ = "OctetString"
_Dhcp6SnoopingPort_Object = MibTableColumn
dhcp6SnoopingPort = _Dhcp6SnoopingPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 3, 1, 1, 1),
    _Dhcp6SnoopingPort_Type()
)
dhcp6SnoopingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcp6SnoopingPort.setStatus("current")


class _Dhcp6SnoopingPortConfigTrustedPort_Type(Integer32):
    """Custom type dhcp6SnoopingPortConfigTrustedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Dhcp6SnoopingPortConfigTrustedPort_Type.__name__ = "Integer32"
_Dhcp6SnoopingPortConfigTrustedPort_Object = MibTableColumn
dhcp6SnoopingPortConfigTrustedPort = _Dhcp6SnoopingPortConfigTrustedPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 3, 1, 1, 2),
    _Dhcp6SnoopingPortConfigTrustedPort_Type()
)
dhcp6SnoopingPortConfigTrustedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6SnoopingPortConfigTrustedPort.setStatus("current")


class _Dhcp6SnoopingPortConfigPortLag_Type(OctetString):
    """Custom type dhcp6SnoopingPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Dhcp6SnoopingPortConfigPortLag_Type.__name__ = "OctetString"
_Dhcp6SnoopingPortConfigPortLag_Object = MibTableColumn
dhcp6SnoopingPortConfigPortLag = _Dhcp6SnoopingPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 1, 3, 1, 1, 3),
    _Dhcp6SnoopingPortConfigPortLag_Type()
)
dhcp6SnoopingPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcp6SnoopingPortConfigPortLag.setStatus("current")
_TplinkDhcp6SnoopingNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcp6SnoopingNotifications = _TplinkDhcp6SnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 91, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCP6SNOOPING-MIB",
    **{"tplinkDhcp6SnoopingMIB": tplinkDhcp6SnoopingMIB,
       "tplinkDhcp6SnoopingMIBObjects": tplinkDhcp6SnoopingMIBObjects,
       "dhcp6SnoopingGlobalConfig": dhcp6SnoopingGlobalConfig,
       "dhcp6SnoopingEnable": dhcp6SnoopingEnable,
       "dhcp6SnoopingVlanConfigTable": dhcp6SnoopingVlanConfigTable,
       "dhcp6SnoopingVlanConfigEntry": dhcp6SnoopingVlanConfigEntry,
       "dhcp6SnoopingVlanId": dhcp6SnoopingVlanId,
       "dhcp6SnoopingVlanStatus": dhcp6SnoopingVlanStatus,
       "dhcp6SnoopingPortConfig": dhcp6SnoopingPortConfig,
       "dhcp6SnoopingPortConfigTable": dhcp6SnoopingPortConfigTable,
       "dhcp6SnoopingPortConfigEntry": dhcp6SnoopingPortConfigEntry,
       "dhcp6SnoopingPort": dhcp6SnoopingPort,
       "dhcp6SnoopingPortConfigTrustedPort": dhcp6SnoopingPortConfigTrustedPort,
       "dhcp6SnoopingPortConfigPortLag": dhcp6SnoopingPortConfigPortLag,
       "tplinkDhcp6SnoopingNotifications": tplinkDhcp6SnoopingNotifications}
)
