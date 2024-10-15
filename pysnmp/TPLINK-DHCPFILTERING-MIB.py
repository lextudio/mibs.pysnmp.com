# SNMP MIB module (TPLINK-DHCPFILTERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-DHCPFILTERING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:54 2024
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

tplinkDhcpFilteringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48)
)
tplinkDhcpFilteringMIB.setRevisions(
        ("2012-12-17 10:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcpFilteringMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcpFilteringMIBObjects = _TplinkDhcpFilteringMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1)
)
_DhcpFilteringGlobalConfig_ObjectIdentity = ObjectIdentity
dhcpFilteringGlobalConfig = _DhcpFilteringGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 1)
)


class _DhcpFilteringEnable_Type(Integer32):
    """Custom type dhcpFilteringEnable based on Integer32"""
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


_DhcpFilteringEnable_Type.__name__ = "Integer32"
_DhcpFilteringEnable_Object = MibScalar
dhcpFilteringEnable = _DhcpFilteringEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 1, 1),
    _DhcpFilteringEnable_Type()
)
dhcpFilteringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFilteringEnable.setStatus("current")
_DhcpFilteringVlanConfigTable_Object = MibTable
dhcpFilteringVlanConfigTable = _DhcpFilteringVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dhcpFilteringVlanConfigTable.setStatus("current")
_DhcpFilteringVlanConfigEntry_Object = MibTableRow
dhcpFilteringVlanConfigEntry = _DhcpFilteringVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 1, 2, 1)
)
dhcpFilteringVlanConfigEntry.setIndexNames(
    (0, "TPLINK-DHCPFILTERING-MIB", "dhcpFilteringVlanId"),
)
if mibBuilder.loadTexts:
    dhcpFilteringVlanConfigEntry.setStatus("current")


class _DhcpFilteringVlanId_Type(Integer32):
    """Custom type dhcpFilteringVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpFilteringVlanId_Type.__name__ = "Integer32"
_DhcpFilteringVlanId_Object = MibTableColumn
dhcpFilteringVlanId = _DhcpFilteringVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 1, 2, 1, 1),
    _DhcpFilteringVlanId_Type()
)
dhcpFilteringVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpFilteringVlanId.setStatus("current")


class _DhcpFilteringVlanStatus_Type(Integer32):
    """Custom type dhcpFilteringVlanStatus based on Integer32"""
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


_DhcpFilteringVlanStatus_Type.__name__ = "Integer32"
_DhcpFilteringVlanStatus_Object = MibTableColumn
dhcpFilteringVlanStatus = _DhcpFilteringVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 1, 2, 1, 2),
    _DhcpFilteringVlanStatus_Type()
)
dhcpFilteringVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpFilteringVlanStatus.setStatus("current")
_DhcpFilteringPortConfig_ObjectIdentity = ObjectIdentity
dhcpFilteringPortConfig = _DhcpFilteringPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3)
)
_DhcpFilteringPortConfigTable_Object = MibTable
dhcpFilteringPortConfigTable = _DhcpFilteringPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpFilteringPortConfigTable.setStatus("current")
_DhcpFilteringPortConfigEntry_Object = MibTableRow
dhcpFilteringPortConfigEntry = _DhcpFilteringPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1)
)
dhcpFilteringPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpFilteringPortConfigEntry.setStatus("current")


class _DhcpFilteringPort_Type(OctetString):
    """Custom type dhcpFilteringPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpFilteringPort_Type.__name__ = "OctetString"
_DhcpFilteringPort_Object = MibTableColumn
dhcpFilteringPort = _DhcpFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1, 1),
    _DhcpFilteringPort_Type()
)
dhcpFilteringPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpFilteringPort.setStatus("current")


class _DhcpFilteringPortConfigTrustedPort_Type(Integer32):
    """Custom type dhcpFilteringPortConfigTrustedPort based on Integer32"""
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


_DhcpFilteringPortConfigTrustedPort_Type.__name__ = "Integer32"
_DhcpFilteringPortConfigTrustedPort_Object = MibTableColumn
dhcpFilteringPortConfigTrustedPort = _DhcpFilteringPortConfigTrustedPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1, 2),
    _DhcpFilteringPortConfigTrustedPort_Type()
)
dhcpFilteringPortConfigTrustedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFilteringPortConfigTrustedPort.setStatus("current")


class _DhcpFilteringPortConfigPortLag_Type(OctetString):
    """Custom type dhcpFilteringPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DhcpFilteringPortConfigPortLag_Type.__name__ = "OctetString"
_DhcpFilteringPortConfigPortLag_Object = MibTableColumn
dhcpFilteringPortConfigPortLag = _DhcpFilteringPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 1, 3, 1, 1, 3),
    _DhcpFilteringPortConfigPortLag_Type()
)
dhcpFilteringPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpFilteringPortConfigPortLag.setStatus("current")
_TplinkDhcpFilteringNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcpFilteringNotifications = _TplinkDhcpFilteringNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 48, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCPFILTERING-MIB",
    **{"tplinkDhcpFilteringMIB": tplinkDhcpFilteringMIB,
       "tplinkDhcpFilteringMIBObjects": tplinkDhcpFilteringMIBObjects,
       "dhcpFilteringGlobalConfig": dhcpFilteringGlobalConfig,
       "dhcpFilteringEnable": dhcpFilteringEnable,
       "dhcpFilteringVlanConfigTable": dhcpFilteringVlanConfigTable,
       "dhcpFilteringVlanConfigEntry": dhcpFilteringVlanConfigEntry,
       "dhcpFilteringVlanId": dhcpFilteringVlanId,
       "dhcpFilteringVlanStatus": dhcpFilteringVlanStatus,
       "dhcpFilteringPortConfig": dhcpFilteringPortConfig,
       "dhcpFilteringPortConfigTable": dhcpFilteringPortConfigTable,
       "dhcpFilteringPortConfigEntry": dhcpFilteringPortConfigEntry,
       "dhcpFilteringPort": dhcpFilteringPort,
       "dhcpFilteringPortConfigTrustedPort": dhcpFilteringPortConfigTrustedPort,
       "dhcpFilteringPortConfigPortLag": dhcpFilteringPortConfigPortLag,
       "tplinkDhcpFilteringNotifications": tplinkDhcpFilteringNotifications}
)
