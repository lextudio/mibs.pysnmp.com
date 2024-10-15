# SNMP MIB module (TPLINK-PORTCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-PORTCONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:28 2024
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

tplinkPortConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8)
)
tplinkPortConfigMIB.setRevisions(
        ("2012-11-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPortConfigMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPortConfigMIBObjects = _TplinkPortConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1)
)
_TpPortConfigTable_Object = MibTable
tpPortConfigTable = _TpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tpPortConfigTable.setStatus("current")
_TpPortConfigEntry_Object = MibTableRow
tpPortConfigEntry = _TpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1)
)
tpPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpPortConfigEntry.setStatus("current")
_TpPortConfigDescription_Type = DisplayString
_TpPortConfigDescription_Object = MibTableColumn
tpPortConfigDescription = _TpPortConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 2),
    _TpPortConfigDescription_Type()
)
tpPortConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigDescription.setStatus("current")


class _TpPortConfigStatus_Type(Integer32):
    """Custom type tpPortConfigStatus based on Integer32"""
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


_TpPortConfigStatus_Type.__name__ = "Integer32"
_TpPortConfigStatus_Object = MibTableColumn
tpPortConfigStatus = _TpPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 3),
    _TpPortConfigStatus_Type()
)
tpPortConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigStatus.setStatus("current")


class _TpPortConfigSpeed_Type(Integer32):
    """Custom type tpPortConfigSpeed based on Integer32"""
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
        *(("auto", 4),
          ("speed-100Mbps", 1),
          ("speed-10Gigabps", 3),
          ("speed-10Mbps", 0),
          ("speed-1Gigabps", 2))
    )


_TpPortConfigSpeed_Type.__name__ = "Integer32"
_TpPortConfigSpeed_Object = MibTableColumn
tpPortConfigSpeed = _TpPortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 4),
    _TpPortConfigSpeed_Type()
)
tpPortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigSpeed.setStatus("current")


class _TpPortConfigDuplex_Type(Integer32):
    """Custom type tpPortConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("full", 1),
          ("half", 0))
    )


_TpPortConfigDuplex_Type.__name__ = "Integer32"
_TpPortConfigDuplex_Object = MibTableColumn
tpPortConfigDuplex = _TpPortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 5),
    _TpPortConfigDuplex_Type()
)
tpPortConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigDuplex.setStatus("current")


class _TpPortConfigFlowCtrl_Type(Integer32):
    """Custom type tpPortConfigFlowCtrl based on Integer32"""
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


_TpPortConfigFlowCtrl_Type.__name__ = "Integer32"
_TpPortConfigFlowCtrl_Object = MibTableColumn
tpPortConfigFlowCtrl = _TpPortConfigFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 6),
    _TpPortConfigFlowCtrl_Type()
)
tpPortConfigFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigFlowCtrl.setStatus("current")


class _TpPortConfigJumbo_Type(Integer32):
    """Custom type tpPortConfigJumbo based on Integer32"""
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


_TpPortConfigJumbo_Type.__name__ = "Integer32"
_TpPortConfigJumbo_Object = MibTableColumn
tpPortConfigJumbo = _TpPortConfigJumbo_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 7),
    _TpPortConfigJumbo_Type()
)
tpPortConfigJumbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigJumbo.setStatus("current")
_TpPortConfigLAG_Type = DisplayString
_TpPortConfigLAG_Object = MibTableColumn
tpPortConfigLAG = _TpPortConfigLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 8),
    _TpPortConfigLAG_Type()
)
tpPortConfigLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortConfigLAG.setStatus("current")
_TplinkPortConfigNotifications_ObjectIdentity = ObjectIdentity
tplinkPortConfigNotifications = _TplinkPortConfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PORTCONFIG-MIB",
    **{"tplinkPortConfigMIB": tplinkPortConfigMIB,
       "tplinkPortConfigMIBObjects": tplinkPortConfigMIBObjects,
       "tpPortConfigTable": tpPortConfigTable,
       "tpPortConfigEntry": tpPortConfigEntry,
       "tpPortConfigDescription": tpPortConfigDescription,
       "tpPortConfigStatus": tpPortConfigStatus,
       "tpPortConfigSpeed": tpPortConfigSpeed,
       "tpPortConfigDuplex": tpPortConfigDuplex,
       "tpPortConfigFlowCtrl": tpPortConfigFlowCtrl,
       "tpPortConfigJumbo": tpPortConfigJumbo,
       "tpPortConfigLAG": tpPortConfigLAG,
       "tplinkPortConfigNotifications": tplinkPortConfigNotifications}
)
