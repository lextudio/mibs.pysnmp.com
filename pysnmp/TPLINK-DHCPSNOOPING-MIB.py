# SNMP MIB module (TPLINK-DHCPSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-DHCPSNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:57 2024
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

tplinkDhcpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27)
)
tplinkDhcpSnoopingMIB.setRevisions(
        ("2012-12-17 10:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcpSnoopingMIBObjects = _TplinkDhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1)
)
_DhcpSnoopingGlobalConfig_ObjectIdentity = ObjectIdentity
dhcpSnoopingGlobalConfig = _DhcpSnoopingGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1)
)


class _DhcpSnoopingEnable_Type(Integer32):
    """Custom type dhcpSnoopingEnable based on Integer32"""
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


_DhcpSnoopingEnable_Type.__name__ = "Integer32"
_DhcpSnoopingEnable_Object = MibScalar
dhcpSnoopingEnable = _DhcpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 1),
    _DhcpSnoopingEnable_Type()
)
dhcpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingEnable.setStatus("current")
_DhcpSnoopingVlanConfigTable_Object = MibTable
dhcpSnoopingVlanConfigTable = _DhcpSnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dhcpSnoopingVlanConfigTable.setStatus("current")
_DhcpSnoopingVlanConfigEntry_Object = MibTableRow
dhcpSnoopingVlanConfigEntry = _DhcpSnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 2, 1)
)
dhcpSnoopingVlanConfigEntry.setIndexNames(
    (0, "TPLINK-DHCPSNOOPING-MIB", "dhcpSnoopingVlanId"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingVlanConfigEntry.setStatus("current")


class _DhcpSnoopingVlanId_Type(Integer32):
    """Custom type dhcpSnoopingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnoopingVlanId_Type.__name__ = "Integer32"
_DhcpSnoopingVlanId_Object = MibTableColumn
dhcpSnoopingVlanId = _DhcpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 2, 1, 1),
    _DhcpSnoopingVlanId_Type()
)
dhcpSnoopingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanId.setStatus("current")


class _DhcpSnoopingVlanStatus_Type(Integer32):
    """Custom type dhcpSnoopingVlanStatus based on Integer32"""
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


_DhcpSnoopingVlanStatus_Type.__name__ = "Integer32"
_DhcpSnoopingVlanStatus_Object = MibTableColumn
dhcpSnoopingVlanStatus = _DhcpSnoopingVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 2, 1, 2),
    _DhcpSnoopingVlanStatus_Type()
)
dhcpSnoopingVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanStatus.setStatus("current")
_DhcpSnoopingOption82Config_ObjectIdentity = ObjectIdentity
dhcpSnoopingOption82Config = _DhcpSnoopingOption82Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2)
)
_DhcpSnoopingOption82ConfigTable_Object = MibTable
dhcpSnoopingOption82ConfigTable = _DhcpSnoopingOption82ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigTable.setStatus("current")
_DhcpSnoopingOption82ConfigEntry_Object = MibTableRow
dhcpSnoopingOption82ConfigEntry = _DhcpSnoopingOption82ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1)
)
dhcpSnoopingOption82ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigEntry.setStatus("current")


class _DhcpSnoopingOption82ConfigPort_Type(OctetString):
    """Custom type dhcpSnoopingOption82ConfigPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnoopingOption82ConfigPort_Type.__name__ = "OctetString"
_DhcpSnoopingOption82ConfigPort_Object = MibTableColumn
dhcpSnoopingOption82ConfigPort = _DhcpSnoopingOption82ConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1, 1),
    _DhcpSnoopingOption82ConfigPort_Type()
)
dhcpSnoopingOption82ConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigPort.setStatus("current")


class _DhcpSnoopingOption82ConfigSupportStatus_Type(Integer32):
    """Custom type dhcpSnoopingOption82ConfigSupportStatus based on Integer32"""
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


_DhcpSnoopingOption82ConfigSupportStatus_Type.__name__ = "Integer32"
_DhcpSnoopingOption82ConfigSupportStatus_Object = MibTableColumn
dhcpSnoopingOption82ConfigSupportStatus = _DhcpSnoopingOption82ConfigSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1, 2),
    _DhcpSnoopingOption82ConfigSupportStatus_Type()
)
dhcpSnoopingOption82ConfigSupportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigSupportStatus.setStatus("current")


class _DhcpSnoopingOption82ConfigOperationStrategy_Type(Integer32):
    """Custom type dhcpSnoopingOption82ConfigOperationStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 0),
          ("replace", 1))
    )


_DhcpSnoopingOption82ConfigOperationStrategy_Type.__name__ = "Integer32"
_DhcpSnoopingOption82ConfigOperationStrategy_Object = MibTableColumn
dhcpSnoopingOption82ConfigOperationStrategy = _DhcpSnoopingOption82ConfigOperationStrategy_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1, 3),
    _DhcpSnoopingOption82ConfigOperationStrategy_Type()
)
dhcpSnoopingOption82ConfigOperationStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigOperationStrategy.setStatus("current")


class _DhcpSnoopingOption82ConfigCircuitCustomization_Type(Integer32):
    """Custom type dhcpSnoopingOption82ConfigCircuitCustomization based on Integer32"""
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


_DhcpSnoopingOption82ConfigCircuitCustomization_Type.__name__ = "Integer32"
_DhcpSnoopingOption82ConfigCircuitCustomization_Object = MibTableColumn
dhcpSnoopingOption82ConfigCircuitCustomization = _DhcpSnoopingOption82ConfigCircuitCustomization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1, 4),
    _DhcpSnoopingOption82ConfigCircuitCustomization_Type()
)
dhcpSnoopingOption82ConfigCircuitCustomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigCircuitCustomization.setStatus("current")


class _DhcpSnoopingOption82ConfigCircuitID_Type(OctetString):
    """Custom type dhcpSnoopingOption82ConfigCircuitID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DhcpSnoopingOption82ConfigCircuitID_Type.__name__ = "OctetString"
_DhcpSnoopingOption82ConfigCircuitID_Object = MibTableColumn
dhcpSnoopingOption82ConfigCircuitID = _DhcpSnoopingOption82ConfigCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1, 5),
    _DhcpSnoopingOption82ConfigCircuitID_Type()
)
dhcpSnoopingOption82ConfigCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigCircuitID.setStatus("current")


class _DhcpSnoopingOption82ConfigRemoteCustomization_Type(Integer32):
    """Custom type dhcpSnoopingOption82ConfigRemoteCustomization based on Integer32"""
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


_DhcpSnoopingOption82ConfigRemoteCustomization_Type.__name__ = "Integer32"
_DhcpSnoopingOption82ConfigRemoteCustomization_Object = MibTableColumn
dhcpSnoopingOption82ConfigRemoteCustomization = _DhcpSnoopingOption82ConfigRemoteCustomization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1, 6),
    _DhcpSnoopingOption82ConfigRemoteCustomization_Type()
)
dhcpSnoopingOption82ConfigRemoteCustomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigRemoteCustomization.setStatus("current")


class _DhcpSnoopingOption82ConfigRemoteID_Type(OctetString):
    """Custom type dhcpSnoopingOption82ConfigRemoteID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DhcpSnoopingOption82ConfigRemoteID_Type.__name__ = "OctetString"
_DhcpSnoopingOption82ConfigRemoteID_Object = MibTableColumn
dhcpSnoopingOption82ConfigRemoteID = _DhcpSnoopingOption82ConfigRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1, 7),
    _DhcpSnoopingOption82ConfigRemoteID_Type()
)
dhcpSnoopingOption82ConfigRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigRemoteID.setStatus("current")


class _DhcpSnoopingOption82ConfigLag_Type(OctetString):
    """Custom type dhcpSnoopingOption82ConfigLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DhcpSnoopingOption82ConfigLag_Type.__name__ = "OctetString"
_DhcpSnoopingOption82ConfigLag_Object = MibTableColumn
dhcpSnoopingOption82ConfigLag = _DhcpSnoopingOption82ConfigLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 2, 1, 1, 8),
    _DhcpSnoopingOption82ConfigLag_Type()
)
dhcpSnoopingOption82ConfigLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82ConfigLag.setStatus("current")
_DhcpSnoopingPortConfig_ObjectIdentity = ObjectIdentity
dhcpSnoopingPortConfig = _DhcpSnoopingPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3)
)
_DhcpSnoopingPortConfigTable_Object = MibTable
dhcpSnoopingPortConfigTable = _DhcpSnoopingPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigTable.setStatus("current")
_DhcpSnoopingPortConfigEntry_Object = MibTableRow
dhcpSnoopingPortConfigEntry = _DhcpSnoopingPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1)
)
dhcpSnoopingPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigEntry.setStatus("current")


class _DhcpSnoopingPort_Type(OctetString):
    """Custom type dhcpSnoopingPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnoopingPort_Type.__name__ = "OctetString"
_DhcpSnoopingPort_Object = MibTableColumn
dhcpSnoopingPort = _DhcpSnoopingPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 1),
    _DhcpSnoopingPort_Type()
)
dhcpSnoopingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPort.setStatus("current")


class _DhcpSnoopingPortConfigTrustedPort_Type(Integer32):
    """Custom type dhcpSnoopingPortConfigTrustedPort based on Integer32"""
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


_DhcpSnoopingPortConfigTrustedPort_Type.__name__ = "Integer32"
_DhcpSnoopingPortConfigTrustedPort_Object = MibTableColumn
dhcpSnoopingPortConfigTrustedPort = _DhcpSnoopingPortConfigTrustedPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 2),
    _DhcpSnoopingPortConfigTrustedPort_Type()
)
dhcpSnoopingPortConfigTrustedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigTrustedPort.setStatus("current")


class _DhcpSnoopingPortConfigMacVerify_Type(Integer32):
    """Custom type dhcpSnoopingPortConfigMacVerify based on Integer32"""
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


_DhcpSnoopingPortConfigMacVerify_Type.__name__ = "Integer32"
_DhcpSnoopingPortConfigMacVerify_Object = MibTableColumn
dhcpSnoopingPortConfigMacVerify = _DhcpSnoopingPortConfigMacVerify_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 3),
    _DhcpSnoopingPortConfigMacVerify_Type()
)
dhcpSnoopingPortConfigMacVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigMacVerify.setStatus("current")


class _DhcpSnoopingPortConfigRateLimit_Type(Integer32):
    """Custom type dhcpSnoopingPortConfigRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              20,
              25,
              30)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("value10pps", 10),
          ("value15pps", 15),
          ("value20pps", 20),
          ("value25pps", 25),
          ("value30pps", 30),
          ("value5pps", 5))
    )


_DhcpSnoopingPortConfigRateLimit_Type.__name__ = "Integer32"
_DhcpSnoopingPortConfigRateLimit_Object = MibTableColumn
dhcpSnoopingPortConfigRateLimit = _DhcpSnoopingPortConfigRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 4),
    _DhcpSnoopingPortConfigRateLimit_Type()
)
dhcpSnoopingPortConfigRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigRateLimit.setStatus("current")


class _DhcpSnoopingPortConfigDeclineRateLimit_Type(Integer32):
    """Custom type dhcpSnoopingPortConfigDeclineRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              20,
              25,
              30)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("value10pps", 10),
          ("value15pps", 15),
          ("value20pps", 20),
          ("value25pps", 25),
          ("value30pps", 30),
          ("value5pps", 5))
    )


_DhcpSnoopingPortConfigDeclineRateLimit_Type.__name__ = "Integer32"
_DhcpSnoopingPortConfigDeclineRateLimit_Object = MibTableColumn
dhcpSnoopingPortConfigDeclineRateLimit = _DhcpSnoopingPortConfigDeclineRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 5),
    _DhcpSnoopingPortConfigDeclineRateLimit_Type()
)
dhcpSnoopingPortConfigDeclineRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigDeclineRateLimit.setStatus("current")


class _DhcpSnoopingPortConfigPortLag_Type(OctetString):
    """Custom type dhcpSnoopingPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DhcpSnoopingPortConfigPortLag_Type.__name__ = "OctetString"
_DhcpSnoopingPortConfigPortLag_Object = MibTableColumn
dhcpSnoopingPortConfigPortLag = _DhcpSnoopingPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 6),
    _DhcpSnoopingPortConfigPortLag_Type()
)
dhcpSnoopingPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigPortLag.setStatus("current")
_TplinkDhcpSnoopingNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcpSnoopingNotifications = _TplinkDhcpSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCPSNOOPING-MIB",
    **{"tplinkDhcpSnoopingMIB": tplinkDhcpSnoopingMIB,
       "tplinkDhcpSnoopingMIBObjects": tplinkDhcpSnoopingMIBObjects,
       "dhcpSnoopingGlobalConfig": dhcpSnoopingGlobalConfig,
       "dhcpSnoopingEnable": dhcpSnoopingEnable,
       "dhcpSnoopingVlanConfigTable": dhcpSnoopingVlanConfigTable,
       "dhcpSnoopingVlanConfigEntry": dhcpSnoopingVlanConfigEntry,
       "dhcpSnoopingVlanId": dhcpSnoopingVlanId,
       "dhcpSnoopingVlanStatus": dhcpSnoopingVlanStatus,
       "dhcpSnoopingOption82Config": dhcpSnoopingOption82Config,
       "dhcpSnoopingOption82ConfigTable": dhcpSnoopingOption82ConfigTable,
       "dhcpSnoopingOption82ConfigEntry": dhcpSnoopingOption82ConfigEntry,
       "dhcpSnoopingOption82ConfigPort": dhcpSnoopingOption82ConfigPort,
       "dhcpSnoopingOption82ConfigSupportStatus": dhcpSnoopingOption82ConfigSupportStatus,
       "dhcpSnoopingOption82ConfigOperationStrategy": dhcpSnoopingOption82ConfigOperationStrategy,
       "dhcpSnoopingOption82ConfigCircuitCustomization": dhcpSnoopingOption82ConfigCircuitCustomization,
       "dhcpSnoopingOption82ConfigCircuitID": dhcpSnoopingOption82ConfigCircuitID,
       "dhcpSnoopingOption82ConfigRemoteCustomization": dhcpSnoopingOption82ConfigRemoteCustomization,
       "dhcpSnoopingOption82ConfigRemoteID": dhcpSnoopingOption82ConfigRemoteID,
       "dhcpSnoopingOption82ConfigLag": dhcpSnoopingOption82ConfigLag,
       "dhcpSnoopingPortConfig": dhcpSnoopingPortConfig,
       "dhcpSnoopingPortConfigTable": dhcpSnoopingPortConfigTable,
       "dhcpSnoopingPortConfigEntry": dhcpSnoopingPortConfigEntry,
       "dhcpSnoopingPort": dhcpSnoopingPort,
       "dhcpSnoopingPortConfigTrustedPort": dhcpSnoopingPortConfigTrustedPort,
       "dhcpSnoopingPortConfigMacVerify": dhcpSnoopingPortConfigMacVerify,
       "dhcpSnoopingPortConfigRateLimit": dhcpSnoopingPortConfigRateLimit,
       "dhcpSnoopingPortConfigDeclineRateLimit": dhcpSnoopingPortConfigDeclineRateLimit,
       "dhcpSnoopingPortConfigPortLag": dhcpSnoopingPortConfigPortLag,
       "tplinkDhcpSnoopingNotifications": tplinkDhcpSnoopingNotifications}
)
