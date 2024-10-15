# SNMP MIB module (TPLINK-pppoeConfig-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-pppoeConfig-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:51 2024
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

tplinkPPPoEConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57)
)
tplinkPPPoEConfigMIB.setRevisions(
        ("2012-12-17 10:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPPPoEConfigMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPPPoEConfigMIBObjects = _TplinkPPPoEConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1)
)
_TpPppoeIdInsertionGlobalConfig_ObjectIdentity = ObjectIdentity
tpPppoeIdInsertionGlobalConfig = _TpPppoeIdInsertionGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 1)
)


class _TpPppoeIdInsertionGlobalEnable_Type(Integer32):
    """Custom type tpPppoeIdInsertionGlobalEnable based on Integer32"""
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


_TpPppoeIdInsertionGlobalEnable_Type.__name__ = "Integer32"
_TpPppoeIdInsertionGlobalEnable_Object = MibScalar
tpPppoeIdInsertionGlobalEnable = _TpPppoeIdInsertionGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 1, 1),
    _TpPppoeIdInsertionGlobalEnable_Type()
)
tpPppoeIdInsertionGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPppoeIdInsertionGlobalEnable.setStatus("current")
_TpPppoeIdInsertionPortConfig_ObjectIdentity = ObjectIdentity
tpPppoeIdInsertionPortConfig = _TpPppoeIdInsertionPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2)
)
_TpPppoeIdInsertionPortConfigTable_Object = MibTable
tpPppoeIdInsertionPortConfigTable = _TpPppoeIdInsertionPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpPppoeIdInsertionPortConfigTable.setStatus("current")
_TpPppoeIdInsertionPortConfigEntry_Object = MibTableRow
tpPppoeIdInsertionPortConfigEntry = _TpPppoeIdInsertionPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2, 1, 1)
)
tpPppoeIdInsertionPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpPppoeIdInsertionPortConfigEntry.setStatus("current")


class _TpPppoeIdInsertionPortIndex_Type(DisplayString):
    """Custom type tpPppoeIdInsertionPortIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpPppoeIdInsertionPortIndex_Type.__name__ = "DisplayString"
_TpPppoeIdInsertionPortIndex_Object = MibTableColumn
tpPppoeIdInsertionPortIndex = _TpPppoeIdInsertionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2, 1, 1, 1),
    _TpPppoeIdInsertionPortIndex_Type()
)
tpPppoeIdInsertionPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPppoeIdInsertionPortIndex.setStatus("current")


class _TpPppoeCircuitIdPortConfigEnable_Type(Integer32):
    """Custom type tpPppoeCircuitIdPortConfigEnable based on Integer32"""
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


_TpPppoeCircuitIdPortConfigEnable_Type.__name__ = "Integer32"
_TpPppoeCircuitIdPortConfigEnable_Object = MibTableColumn
tpPppoeCircuitIdPortConfigEnable = _TpPppoeCircuitIdPortConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2, 1, 1, 2),
    _TpPppoeCircuitIdPortConfigEnable_Type()
)
tpPppoeCircuitIdPortConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPppoeCircuitIdPortConfigEnable.setStatus("current")


class _TpPppoeCircuitIdPortConfigIdType_Type(Integer32):
    """Custom type tpPppoeCircuitIdPortConfigIdType based on Integer32"""
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
        *(("switchIp", 0),
          ("switchMac", 1),
          ("switchUdf", 2),
          ("switchUdfOnly", 3))
    )


_TpPppoeCircuitIdPortConfigIdType_Type.__name__ = "Integer32"
_TpPppoeCircuitIdPortConfigIdType_Object = MibTableColumn
tpPppoeCircuitIdPortConfigIdType = _TpPppoeCircuitIdPortConfigIdType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2, 1, 1, 3),
    _TpPppoeCircuitIdPortConfigIdType_Type()
)
tpPppoeCircuitIdPortConfigIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPppoeCircuitIdPortConfigIdType.setStatus("current")


class _TpPppoeCircuitIdPortConfigUdfValue_Type(OctetString):
    """Custom type tpPppoeCircuitIdPortConfigUdfValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TpPppoeCircuitIdPortConfigUdfValue_Type.__name__ = "OctetString"
_TpPppoeCircuitIdPortConfigUdfValue_Object = MibTableColumn
tpPppoeCircuitIdPortConfigUdfValue = _TpPppoeCircuitIdPortConfigUdfValue_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2, 1, 1, 4),
    _TpPppoeCircuitIdPortConfigUdfValue_Type()
)
tpPppoeCircuitIdPortConfigUdfValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPppoeCircuitIdPortConfigUdfValue.setStatus("current")


class _TpPppoeRemoteIdPortConfigEnable_Type(Integer32):
    """Custom type tpPppoeRemoteIdPortConfigEnable based on Integer32"""
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


_TpPppoeRemoteIdPortConfigEnable_Type.__name__ = "Integer32"
_TpPppoeRemoteIdPortConfigEnable_Object = MibTableColumn
tpPppoeRemoteIdPortConfigEnable = _TpPppoeRemoteIdPortConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2, 1, 1, 5),
    _TpPppoeRemoteIdPortConfigEnable_Type()
)
tpPppoeRemoteIdPortConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPppoeRemoteIdPortConfigEnable.setStatus("current")


class _TpPppoeRemoteIdPortConfigValue_Type(OctetString):
    """Custom type tpPppoeRemoteIdPortConfigValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TpPppoeRemoteIdPortConfigValue_Type.__name__ = "OctetString"
_TpPppoeRemoteIdPortConfigValue_Object = MibTableColumn
tpPppoeRemoteIdPortConfigValue = _TpPppoeRemoteIdPortConfigValue_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 1, 2, 1, 1, 6),
    _TpPppoeRemoteIdPortConfigValue_Type()
)
tpPppoeRemoteIdPortConfigValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPppoeRemoteIdPortConfigValue.setStatus("current")
_TplinkPPPoEConfigNotifications_ObjectIdentity = ObjectIdentity
tplinkPPPoEConfigNotifications = _TplinkPPPoEConfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 57, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-pppoeConfig-MIB",
    **{"tplinkPPPoEConfigMIB": tplinkPPPoEConfigMIB,
       "tplinkPPPoEConfigMIBObjects": tplinkPPPoEConfigMIBObjects,
       "tpPppoeIdInsertionGlobalConfig": tpPppoeIdInsertionGlobalConfig,
       "tpPppoeIdInsertionGlobalEnable": tpPppoeIdInsertionGlobalEnable,
       "tpPppoeIdInsertionPortConfig": tpPppoeIdInsertionPortConfig,
       "tpPppoeIdInsertionPortConfigTable": tpPppoeIdInsertionPortConfigTable,
       "tpPppoeIdInsertionPortConfigEntry": tpPppoeIdInsertionPortConfigEntry,
       "tpPppoeIdInsertionPortIndex": tpPppoeIdInsertionPortIndex,
       "tpPppoeCircuitIdPortConfigEnable": tpPppoeCircuitIdPortConfigEnable,
       "tpPppoeCircuitIdPortConfigIdType": tpPppoeCircuitIdPortConfigIdType,
       "tpPppoeCircuitIdPortConfigUdfValue": tpPppoeCircuitIdPortConfigUdfValue,
       "tpPppoeRemoteIdPortConfigEnable": tpPppoeRemoteIdPortConfigEnable,
       "tpPppoeRemoteIdPortConfigValue": tpPppoeRemoteIdPortConfigValue,
       "tplinkPPPoEConfigNotifications": tplinkPPPoEConfigNotifications}
)
