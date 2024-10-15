# SNMP MIB module (TPLINK-LLDPCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-LLDPCONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:17 2024
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

(tplinkLldpMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-LLDP-MIB",
    "tplinkLldpMIBObjects")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpConfig_ObjectIdentity = ObjectIdentity
lldpConfig = _LldpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1)
)
_LldpGlobalConfig_ObjectIdentity = ObjectIdentity
lldpGlobalConfig = _LldpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1)
)


class _LldpGlobalConfigEnable_Type(Integer32):
    """Custom type lldpGlobalConfigEnable based on Integer32"""
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


_LldpGlobalConfigEnable_Type.__name__ = "Integer32"
_LldpGlobalConfigEnable_Object = MibScalar
lldpGlobalConfigEnable = _LldpGlobalConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 1),
    _LldpGlobalConfigEnable_Type()
)
lldpGlobalConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpGlobalConfigEnable.setStatus("current")


class _LldpGlobalConfigTxInterval_Type(Integer32):
    """Custom type lldpGlobalConfigTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_LldpGlobalConfigTxInterval_Type.__name__ = "Integer32"
_LldpGlobalConfigTxInterval_Object = MibScalar
lldpGlobalConfigTxInterval = _LldpGlobalConfigTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 2),
    _LldpGlobalConfigTxInterval_Type()
)
lldpGlobalConfigTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpGlobalConfigTxInterval.setStatus("current")


class _LldpGlobalConfigTtl_Type(Integer32):
    """Custom type lldpGlobalConfigTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_LldpGlobalConfigTtl_Type.__name__ = "Integer32"
_LldpGlobalConfigTtl_Object = MibScalar
lldpGlobalConfigTtl = _LldpGlobalConfigTtl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 3),
    _LldpGlobalConfigTtl_Type()
)
lldpGlobalConfigTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpGlobalConfigTtl.setStatus("current")


class _LldpGlobalConfigTxDelay_Type(Integer32):
    """Custom type lldpGlobalConfigTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_LldpGlobalConfigTxDelay_Type.__name__ = "Integer32"
_LldpGlobalConfigTxDelay_Object = MibScalar
lldpGlobalConfigTxDelay = _LldpGlobalConfigTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 4),
    _LldpGlobalConfigTxDelay_Type()
)
lldpGlobalConfigTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpGlobalConfigTxDelay.setStatus("current")


class _LldpGlobalConfigInitDelay_Type(Integer32):
    """Custom type lldpGlobalConfigInitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpGlobalConfigInitDelay_Type.__name__ = "Integer32"
_LldpGlobalConfigInitDelay_Object = MibScalar
lldpGlobalConfigInitDelay = _LldpGlobalConfigInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 5),
    _LldpGlobalConfigInitDelay_Type()
)
lldpGlobalConfigInitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpGlobalConfigInitDelay.setStatus("current")


class _LldpGlobalConfigTrap_Type(Integer32):
    """Custom type lldpGlobalConfigTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_LldpGlobalConfigTrap_Type.__name__ = "Integer32"
_LldpGlobalConfigTrap_Object = MibScalar
lldpGlobalConfigTrap = _LldpGlobalConfigTrap_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 6),
    _LldpGlobalConfigTrap_Type()
)
lldpGlobalConfigTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpGlobalConfigTrap.setStatus("current")


class _LldpGlobalConfigFastCount_Type(Integer32):
    """Custom type lldpGlobalConfigFastCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpGlobalConfigFastCount_Type.__name__ = "Integer32"
_LldpGlobalConfigFastCount_Object = MibScalar
lldpGlobalConfigFastCount = _LldpGlobalConfigFastCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 7),
    _LldpGlobalConfigFastCount_Type()
)
lldpGlobalConfigFastCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpGlobalConfigFastCount.setStatus("current")
_LldpPortConfigTable_Object = MibTable
lldpPortConfigTable = _LldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpPortConfigTable.setStatus("current")
_LldpPortConfigEntry_Object = MibTableRow
lldpPortConfigEntry = _LldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1)
)
lldpPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lldpPortConfigEntry.setStatus("current")


class _LldpConfigPortId_Type(OctetString):
    """Custom type lldpConfigPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpConfigPortId_Type.__name__ = "OctetString"
_LldpConfigPortId_Object = MibTableColumn
lldpConfigPortId = _LldpConfigPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 1),
    _LldpConfigPortId_Type()
)
lldpConfigPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpConfigPortId.setStatus("current")


class _LldpConfigPortStatus_Type(Integer32):
    """Custom type lldpConfigPortStatus based on Integer32"""
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
        *(("disable", 0),
          ("enableRx", 2),
          ("enableRxTx", 3),
          ("enableTx", 1))
    )


_LldpConfigPortStatus_Type.__name__ = "Integer32"
_LldpConfigPortStatus_Object = MibTableColumn
lldpConfigPortStatus = _LldpConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 2),
    _LldpConfigPortStatus_Type()
)
lldpConfigPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortStatus.setStatus("current")


class _LldpConfigPortSnmpNotifyEnable_Type(Integer32):
    """Custom type lldpConfigPortSnmpNotifyEnable based on Integer32"""
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


_LldpConfigPortSnmpNotifyEnable_Type.__name__ = "Integer32"
_LldpConfigPortSnmpNotifyEnable_Object = MibTableColumn
lldpConfigPortSnmpNotifyEnable = _LldpConfigPortSnmpNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 3),
    _LldpConfigPortSnmpNotifyEnable_Type()
)
lldpConfigPortSnmpNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortSnmpNotifyEnable.setStatus("current")


class _LldpConfigPortTlvDescr_Type(Integer32):
    """Custom type lldpConfigPortTlvDescr based on Integer32"""
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


_LldpConfigPortTlvDescr_Type.__name__ = "Integer32"
_LldpConfigPortTlvDescr_Object = MibTableColumn
lldpConfigPortTlvDescr = _LldpConfigPortTlvDescr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 4),
    _LldpConfigPortTlvDescr_Type()
)
lldpConfigPortTlvDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvDescr.setStatus("current")


class _LldpConfigPortTlvSysCap_Type(Integer32):
    """Custom type lldpConfigPortTlvSysCap based on Integer32"""
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


_LldpConfigPortTlvSysCap_Type.__name__ = "Integer32"
_LldpConfigPortTlvSysCap_Object = MibTableColumn
lldpConfigPortTlvSysCap = _LldpConfigPortTlvSysCap_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 5),
    _LldpConfigPortTlvSysCap_Type()
)
lldpConfigPortTlvSysCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvSysCap.setStatus("current")


class _LldpConfigPortTlvSysDescr_Type(Integer32):
    """Custom type lldpConfigPortTlvSysDescr based on Integer32"""
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


_LldpConfigPortTlvSysDescr_Type.__name__ = "Integer32"
_LldpConfigPortTlvSysDescr_Object = MibTableColumn
lldpConfigPortTlvSysDescr = _LldpConfigPortTlvSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 6),
    _LldpConfigPortTlvSysDescr_Type()
)
lldpConfigPortTlvSysDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvSysDescr.setStatus("current")


class _LldpConfigPortTlvSysName_Type(Integer32):
    """Custom type lldpConfigPortTlvSysName based on Integer32"""
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


_LldpConfigPortTlvSysName_Type.__name__ = "Integer32"
_LldpConfigPortTlvSysName_Object = MibTableColumn
lldpConfigPortTlvSysName = _LldpConfigPortTlvSysName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 7),
    _LldpConfigPortTlvSysName_Type()
)
lldpConfigPortTlvSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvSysName.setStatus("current")


class _LldpConfigPortTlvManageAddr_Type(Integer32):
    """Custom type lldpConfigPortTlvManageAddr based on Integer32"""
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


_LldpConfigPortTlvManageAddr_Type.__name__ = "Integer32"
_LldpConfigPortTlvManageAddr_Object = MibTableColumn
lldpConfigPortTlvManageAddr = _LldpConfigPortTlvManageAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 8),
    _LldpConfigPortTlvManageAddr_Type()
)
lldpConfigPortTlvManageAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvManageAddr.setStatus("current")


class _LldpConfigPortTlvPortVlanId_Type(Integer32):
    """Custom type lldpConfigPortTlvPortVlanId based on Integer32"""
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


_LldpConfigPortTlvPortVlanId_Type.__name__ = "Integer32"
_LldpConfigPortTlvPortVlanId_Object = MibTableColumn
lldpConfigPortTlvPortVlanId = _LldpConfigPortTlvPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 9),
    _LldpConfigPortTlvPortVlanId_Type()
)
lldpConfigPortTlvPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvPortVlanId.setStatus("current")


class _LldpConfigPortTlvProtoVlanId_Type(Integer32):
    """Custom type lldpConfigPortTlvProtoVlanId based on Integer32"""
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


_LldpConfigPortTlvProtoVlanId_Type.__name__ = "Integer32"
_LldpConfigPortTlvProtoVlanId_Object = MibTableColumn
lldpConfigPortTlvProtoVlanId = _LldpConfigPortTlvProtoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 10),
    _LldpConfigPortTlvProtoVlanId_Type()
)
lldpConfigPortTlvProtoVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvProtoVlanId.setStatus("current")


class _LldpConfigPortTlvVlanName_Type(Integer32):
    """Custom type lldpConfigPortTlvVlanName based on Integer32"""
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


_LldpConfigPortTlvVlanName_Type.__name__ = "Integer32"
_LldpConfigPortTlvVlanName_Object = MibTableColumn
lldpConfigPortTlvVlanName = _LldpConfigPortTlvVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 11),
    _LldpConfigPortTlvVlanName_Type()
)
lldpConfigPortTlvVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvVlanName.setStatus("current")


class _LldpConfigPortTlvLinkAggre_Type(Integer32):
    """Custom type lldpConfigPortTlvLinkAggre based on Integer32"""
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


_LldpConfigPortTlvLinkAggre_Type.__name__ = "Integer32"
_LldpConfigPortTlvLinkAggre_Object = MibTableColumn
lldpConfigPortTlvLinkAggre = _LldpConfigPortTlvLinkAggre_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 12),
    _LldpConfigPortTlvLinkAggre_Type()
)
lldpConfigPortTlvLinkAggre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvLinkAggre.setStatus("current")


class _LldpConfigPortTlvPortStatus_Type(Integer32):
    """Custom type lldpConfigPortTlvPortStatus based on Integer32"""
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


_LldpConfigPortTlvPortStatus_Type.__name__ = "Integer32"
_LldpConfigPortTlvPortStatus_Object = MibTableColumn
lldpConfigPortTlvPortStatus = _LldpConfigPortTlvPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 13),
    _LldpConfigPortTlvPortStatus_Type()
)
lldpConfigPortTlvPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvPortStatus.setStatus("current")


class _LldpConfigPortTlvMaxFrame_Type(Integer32):
    """Custom type lldpConfigPortTlvMaxFrame based on Integer32"""
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


_LldpConfigPortTlvMaxFrame_Type.__name__ = "Integer32"
_LldpConfigPortTlvMaxFrame_Object = MibTableColumn
lldpConfigPortTlvMaxFrame = _LldpConfigPortTlvMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 14),
    _LldpConfigPortTlvMaxFrame_Type()
)
lldpConfigPortTlvMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvMaxFrame.setStatus("current")


class _LldpConfigPortTlvPower_Type(Integer32):
    """Custom type lldpConfigPortTlvPower based on Integer32"""
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


_LldpConfigPortTlvPower_Type.__name__ = "Integer32"
_LldpConfigPortTlvPower_Object = MibTableColumn
lldpConfigPortTlvPower = _LldpConfigPortTlvPower_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 15),
    _LldpConfigPortTlvPower_Type()
)
lldpConfigPortTlvPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigPortTlvPower.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-LLDPCONFIG-MIB",
    **{"MacAddress": MacAddress,
       "lldpConfig": lldpConfig,
       "lldpGlobalConfig": lldpGlobalConfig,
       "lldpGlobalConfigEnable": lldpGlobalConfigEnable,
       "lldpGlobalConfigTxInterval": lldpGlobalConfigTxInterval,
       "lldpGlobalConfigTtl": lldpGlobalConfigTtl,
       "lldpGlobalConfigTxDelay": lldpGlobalConfigTxDelay,
       "lldpGlobalConfigInitDelay": lldpGlobalConfigInitDelay,
       "lldpGlobalConfigTrap": lldpGlobalConfigTrap,
       "lldpGlobalConfigFastCount": lldpGlobalConfigFastCount,
       "lldpPortConfigTable": lldpPortConfigTable,
       "lldpPortConfigEntry": lldpPortConfigEntry,
       "lldpConfigPortId": lldpConfigPortId,
       "lldpConfigPortStatus": lldpConfigPortStatus,
       "lldpConfigPortSnmpNotifyEnable": lldpConfigPortSnmpNotifyEnable,
       "lldpConfigPortTlvDescr": lldpConfigPortTlvDescr,
       "lldpConfigPortTlvSysCap": lldpConfigPortTlvSysCap,
       "lldpConfigPortTlvSysDescr": lldpConfigPortTlvSysDescr,
       "lldpConfigPortTlvSysName": lldpConfigPortTlvSysName,
       "lldpConfigPortTlvManageAddr": lldpConfigPortTlvManageAddr,
       "lldpConfigPortTlvPortVlanId": lldpConfigPortTlvPortVlanId,
       "lldpConfigPortTlvProtoVlanId": lldpConfigPortTlvProtoVlanId,
       "lldpConfigPortTlvVlanName": lldpConfigPortTlvVlanName,
       "lldpConfigPortTlvLinkAggre": lldpConfigPortTlvLinkAggre,
       "lldpConfigPortTlvPortStatus": lldpConfigPortTlvPortStatus,
       "lldpConfigPortTlvMaxFrame": lldpConfigPortTlvMaxFrame,
       "lldpConfigPortTlvPower": lldpConfigPortTlvPower}
)
