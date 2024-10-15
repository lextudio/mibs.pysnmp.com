# SNMP MIB module (APTIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APTIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:03 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aptisRootModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Boolean(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Aptis_ObjectIdentity = ObjectIdentity
aptis = _Aptis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637)
)
if mibBuilder.loadTexts:
    aptis.setStatus("current")
_Aptis_reg_ObjectIdentity = ObjectIdentity
aptis_reg = _Aptis_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1)
)
if mibBuilder.loadTexts:
    aptis_reg.setStatus("current")
_Aptis_generic_ObjectIdentity = ObjectIdentity
aptis_generic = _Aptis_generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2)
)
if mibBuilder.loadTexts:
    aptis_generic.setStatus("current")
_Aptis_config_ObjectIdentity = ObjectIdentity
aptis_config = _Aptis_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 1)
)
if mibBuilder.loadTexts:
    aptis_config.setStatus("current")
_Aptis_monitoring_ObjectIdentity = ObjectIdentity
aptis_monitoring = _Aptis_monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 2)
)
if mibBuilder.loadTexts:
    aptis_monitoring.setStatus("current")
_Aptis_actions_ObjectIdentity = ObjectIdentity
aptis_actions = _Aptis_actions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3)
)
if mibBuilder.loadTexts:
    aptis_actions.setStatus("current")
_Aptis_exp_ObjectIdentity = ObjectIdentity
aptis_exp = _Aptis_exp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 4)
)
if mibBuilder.loadTexts:
    aptis_exp.setStatus("current")
_Config_sync_ObjectIdentity = ObjectIdentity
config_sync = _Config_sync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 4, 2)
)
if mibBuilder.loadTexts:
    config_sync.setStatus("current")


class _PrevGenNum_Type(Integer32):
    """Custom type prevGenNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrevGenNum_Type.__name__ = "Integer32"
_PrevGenNum_Object = MibScalar
prevGenNum = _PrevGenNum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 4, 2, 1),
    _PrevGenNum_Type()
)
prevGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prevGenNum.setStatus("current")


class _DeltaCount_Type(Integer32):
    """Custom type deltaCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DeltaCount_Type.__name__ = "Integer32"
_DeltaCount_Object = MibScalar
deltaCount = _DeltaCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 4, 2, 2),
    _DeltaCount_Type()
)
deltaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deltaCount.setStatus("current")


class _CurrentGenNum_Type(Integer32):
    """Custom type currentGenNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CurrentGenNum_Type.__name__ = "Integer32"
_CurrentGenNum_Object = MibScalar
currentGenNum = _CurrentGenNum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 4, 2, 3),
    _CurrentGenNum_Type()
)
currentGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGenNum.setStatus("current")
_Aptis_traps_ObjectIdentity = ObjectIdentity
aptis_traps = _Aptis_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5)
)
if mibBuilder.loadTexts:
    aptis_traps.setStatus("current")
_Aptis_products_ObjectIdentity = ObjectIdentity
aptis_products = _Aptis_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 3)
)
if mibBuilder.loadTexts:
    aptis_products.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APTIS-MIB",
    **{"Boolean": Boolean,
       "aptis": aptis,
       "aptis-reg": aptis_reg,
       "aptisRootModule": aptisRootModule,
       "aptis-generic": aptis_generic,
       "aptis-config": aptis_config,
       "aptis-monitoring": aptis_monitoring,
       "aptis-actions": aptis_actions,
       "aptis-exp": aptis_exp,
       "config-sync": config_sync,
       "prevGenNum": prevGenNum,
       "deltaCount": deltaCount,
       "currentGenNum": currentGenNum,
       "aptis-traps": aptis_traps,
       "aptis-products": aptis_products}
)
