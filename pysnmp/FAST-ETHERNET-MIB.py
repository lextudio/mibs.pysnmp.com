# SNMP MIB module (FAST-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FAST-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:42 2024
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

(ctFastEthernet,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFastEthernet")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtFastEthernetCtl_ObjectIdentity = ObjectIdentity
ctFastEthernetCtl = _CtFastEthernetCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1)
)
_CtFastEthernetCtlTable_Object = MibTable
ctFastEthernetCtlTable = _CtFastEthernetCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    ctFastEthernetCtlTable.setStatus("mandatory")
_CtFastEthernetCtlEntry_Object = MibTableRow
ctFastEthernetCtlEntry = _CtFastEthernetCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1)
)
ctFastEthernetCtlEntry.setIndexNames(
    (0, "FAST-ETHERNET-MIB", "ctFastEthernetCtlInterface"),
    (0, "FAST-ETHERNET-MIB", "ctFastEthernetCtlPortGroup"),
    (0, "FAST-ETHERNET-MIB", "ctFastEthernetCtlPort"),
)
if mibBuilder.loadTexts:
    ctFastEthernetCtlEntry.setStatus("mandatory")
_CtFastEthernetCtlInterface_Type = Integer32
_CtFastEthernetCtlInterface_Object = MibTableColumn
ctFastEthernetCtlInterface = _CtFastEthernetCtlInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 1),
    _CtFastEthernetCtlInterface_Type()
)
ctFastEthernetCtlInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFastEthernetCtlInterface.setStatus("mandatory")
_CtFastEthernetCtlPortGroup_Type = Integer32
_CtFastEthernetCtlPortGroup_Object = MibTableColumn
ctFastEthernetCtlPortGroup = _CtFastEthernetCtlPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 2),
    _CtFastEthernetCtlPortGroup_Type()
)
ctFastEthernetCtlPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFastEthernetCtlPortGroup.setStatus("mandatory")
_CtFastEthernetCtlPort_Type = Integer32
_CtFastEthernetCtlPort_Object = MibTableColumn
ctFastEthernetCtlPort = _CtFastEthernetCtlPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 3),
    _CtFastEthernetCtlPort_Type()
)
ctFastEthernetCtlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFastEthernetCtlPort.setStatus("mandatory")


class _CtFastEthernetLocalTechnologyAbility_Type(Integer32):
    """Custom type ctFastEthernetLocalTechnologyAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CtFastEthernetLocalTechnologyAbility_Type.__name__ = "Integer32"
_CtFastEthernetLocalTechnologyAbility_Object = MibTableColumn
ctFastEthernetLocalTechnologyAbility = _CtFastEthernetLocalTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 4),
    _CtFastEthernetLocalTechnologyAbility_Type()
)
ctFastEthernetLocalTechnologyAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFastEthernetLocalTechnologyAbility.setStatus("mandatory")


class _CtFastEthernetCurrentOperationalMode_Type(Integer32):
    """Custom type ctFastEthernetCurrentOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CtFastEthernetCurrentOperationalMode_Type.__name__ = "Integer32"
_CtFastEthernetCurrentOperationalMode_Object = MibTableColumn
ctFastEthernetCurrentOperationalMode = _CtFastEthernetCurrentOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 5),
    _CtFastEthernetCurrentOperationalMode_Type()
)
ctFastEthernetCurrentOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFastEthernetCurrentOperationalMode.setStatus("mandatory")


class _CtFastEthernetAdvertisedTechnologyAbility_Type(Integer32):
    """Custom type ctFastEthernetAdvertisedTechnologyAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CtFastEthernetAdvertisedTechnologyAbility_Type.__name__ = "Integer32"
_CtFastEthernetAdvertisedTechnologyAbility_Object = MibTableColumn
ctFastEthernetAdvertisedTechnologyAbility = _CtFastEthernetAdvertisedTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 6),
    _CtFastEthernetAdvertisedTechnologyAbility_Type()
)
ctFastEthernetAdvertisedTechnologyAbility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFastEthernetAdvertisedTechnologyAbility.setStatus("mandatory")


class _CtFastEthernetReceivedTechnologyAbility_Type(Integer32):
    """Custom type ctFastEthernetReceivedTechnologyAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CtFastEthernetReceivedTechnologyAbility_Type.__name__ = "Integer32"
_CtFastEthernetReceivedTechnologyAbility_Object = MibTableColumn
ctFastEthernetReceivedTechnologyAbility = _CtFastEthernetReceivedTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 7),
    _CtFastEthernetReceivedTechnologyAbility_Type()
)
ctFastEthernetReceivedTechnologyAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFastEthernetReceivedTechnologyAbility.setStatus("mandatory")
_CtFastEthernetCtlTableNumEntries_Type = Integer32
_CtFastEthernetCtlTableNumEntries_Object = MibScalar
ctFastEthernetCtlTableNumEntries = _CtFastEthernetCtlTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 2),
    _CtFastEthernetCtlTableNumEntries_Type()
)
ctFastEthernetCtlTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFastEthernetCtlTableNumEntries.setStatus("mandatory")
_CtMMACFENBCfg_ObjectIdentity = ObjectIdentity
ctMMACFENBCfg = _CtMMACFENBCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2)
)
_CtMMACFENBCfgTable_Object = MibTable
ctMMACFENBCfgTable = _CtMMACFENBCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    ctMMACFENBCfgTable.setStatus("mandatory")
_CtMMACFENBCfgEntry_Object = MibTableRow
ctMMACFENBCfgEntry = _CtMMACFENBCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1)
)
ctMMACFENBCfgEntry.setIndexNames(
    (0, "FAST-ETHERNET-MIB", "ctMMACFENBCfgInterface"),
    (0, "FAST-ETHERNET-MIB", "ctMMACFENBCfgPortGroup"),
    (0, "FAST-ETHERNET-MIB", "ctMMACFENBCfgPort"),
)
if mibBuilder.loadTexts:
    ctMMACFENBCfgEntry.setStatus("mandatory")
_CtMMACFENBCfgInterface_Type = Integer32
_CtMMACFENBCfgInterface_Object = MibTableColumn
ctMMACFENBCfgInterface = _CtMMACFENBCfgInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 1),
    _CtMMACFENBCfgInterface_Type()
)
ctMMACFENBCfgInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctMMACFENBCfgInterface.setStatus("mandatory")
_CtMMACFENBCfgPortGroup_Type = Integer32
_CtMMACFENBCfgPortGroup_Object = MibTableColumn
ctMMACFENBCfgPortGroup = _CtMMACFENBCfgPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 2),
    _CtMMACFENBCfgPortGroup_Type()
)
ctMMACFENBCfgPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctMMACFENBCfgPortGroup.setStatus("mandatory")
_CtMMACFENBCfgPort_Type = Integer32
_CtMMACFENBCfgPort_Object = MibTableColumn
ctMMACFENBCfgPort = _CtMMACFENBCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 3),
    _CtMMACFENBCfgPort_Type()
)
ctMMACFENBCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctMMACFENBCfgPort.setStatus("mandatory")


class _CtMMACFENBOperCapabilities_Type(Integer32):
    """Custom type ctMMACFENBOperCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_CtMMACFENBOperCapabilities_Type.__name__ = "Integer32"
_CtMMACFENBOperCapabilities_Object = MibTableColumn
ctMMACFENBOperCapabilities = _CtMMACFENBOperCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 4),
    _CtMMACFENBOperCapabilities_Type()
)
ctMMACFENBOperCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctMMACFENBOperCapabilities.setStatus("mandatory")


class _CtMMACFENBAdminCapabilities_Type(Integer32):
    """Custom type ctMMACFENBAdminCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_CtMMACFENBAdminCapabilities_Type.__name__ = "Integer32"
_CtMMACFENBAdminCapabilities_Object = MibTableColumn
ctMMACFENBAdminCapabilities = _CtMMACFENBAdminCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 5),
    _CtMMACFENBAdminCapabilities_Type()
)
ctMMACFENBAdminCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctMMACFENBAdminCapabilities.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FAST-ETHERNET-MIB",
    **{"ctFastEthernetCtl": ctFastEthernetCtl,
       "ctFastEthernetCtlTable": ctFastEthernetCtlTable,
       "ctFastEthernetCtlEntry": ctFastEthernetCtlEntry,
       "ctFastEthernetCtlInterface": ctFastEthernetCtlInterface,
       "ctFastEthernetCtlPortGroup": ctFastEthernetCtlPortGroup,
       "ctFastEthernetCtlPort": ctFastEthernetCtlPort,
       "ctFastEthernetLocalTechnologyAbility": ctFastEthernetLocalTechnologyAbility,
       "ctFastEthernetCurrentOperationalMode": ctFastEthernetCurrentOperationalMode,
       "ctFastEthernetAdvertisedTechnologyAbility": ctFastEthernetAdvertisedTechnologyAbility,
       "ctFastEthernetReceivedTechnologyAbility": ctFastEthernetReceivedTechnologyAbility,
       "ctFastEthernetCtlTableNumEntries": ctFastEthernetCtlTableNumEntries,
       "ctMMACFENBCfg": ctMMACFENBCfg,
       "ctMMACFENBCfgTable": ctMMACFENBCfgTable,
       "ctMMACFENBCfgEntry": ctMMACFENBCfgEntry,
       "ctMMACFENBCfgInterface": ctMMACFENBCfgInterface,
       "ctMMACFENBCfgPortGroup": ctMMACFENBCfgPortGroup,
       "ctMMACFENBCfgPort": ctMMACFENBCfgPort,
       "ctMMACFENBOperCapabilities": ctMMACFENBOperCapabilities,
       "ctMMACFENBAdminCapabilities": ctMMACFENBAdminCapabilities}
)
