# SNMP MIB module (TPLINK-STATICARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-STATICARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:43 2024
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

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkStaticARPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54)
)
tplinkStaticARPMIB.setRevisions(
        ("2014-11-24 14:42",)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkStaticARPMIBObjects_ObjectIdentity = ObjectIdentity
tplinkStaticARPMIBObjects = _TplinkStaticARPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1)
)
_TpStaticARPConfig_ObjectIdentity = ObjectIdentity
tpStaticARPConfig = _TpStaticARPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1)
)
_TpStaticARPConfigTable_Object = MibTable
tpStaticARPConfigTable = _TpStaticARPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpStaticARPConfigTable.setStatus("current")
_TpStaticARPConfigEntry_Object = MibTableRow
tpStaticARPConfigEntry = _TpStaticARPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1)
)
tpStaticARPConfigEntry.setIndexNames(
    (0, "TPLINK-STATICARP-MIB", "tpStaticARPItemIp"),
)
if mibBuilder.loadTexts:
    tpStaticARPConfigEntry.setStatus("current")
_TpStaticARPItemIp_Type = IpAddress
_TpStaticARPItemIp_Object = MibTableColumn
tpStaticARPItemIp = _TpStaticARPItemIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 1),
    _TpStaticARPItemIp_Type()
)
tpStaticARPItemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticARPItemIp.setStatus("current")


class _TpStaticARPItemMac_Type(OctetString):
    """Custom type tpStaticARPItemMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TpStaticARPItemMac_Type.__name__ = "OctetString"
_TpStaticARPItemMac_Object = MibTableColumn
tpStaticARPItemMac = _TpStaticARPItemMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 2),
    _TpStaticARPItemMac_Type()
)
tpStaticARPItemMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticARPItemMac.setStatus("current")


class _TpStaticArpItemInterfaceName_Type(OctetString):
    """Custom type tpStaticArpItemInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStaticArpItemInterfaceName_Type.__name__ = "OctetString"
_TpStaticArpItemInterfaceName_Object = MibTableColumn
tpStaticArpItemInterfaceName = _TpStaticArpItemInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 3),
    _TpStaticArpItemInterfaceName_Type()
)
tpStaticArpItemInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticArpItemInterfaceName.setStatus("current")
_TpStaticARPItemStatus_Type = TPRowStatus
_TpStaticARPItemStatus_Object = MibTableColumn
tpStaticARPItemStatus = _TpStaticARPItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 4),
    _TpStaticARPItemStatus_Type()
)
tpStaticARPItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticARPItemStatus.setStatus("current")
_TplinkStaticARPNotifications_ObjectIdentity = ObjectIdentity
tplinkStaticARPNotifications = _TplinkStaticARPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-STATICARP-MIB",
    **{"MacAddress": MacAddress,
       "tplinkStaticARPMIB": tplinkStaticARPMIB,
       "tplinkStaticARPMIBObjects": tplinkStaticARPMIBObjects,
       "tpStaticARPConfig": tpStaticARPConfig,
       "tpStaticARPConfigTable": tpStaticARPConfigTable,
       "tpStaticARPConfigEntry": tpStaticARPConfigEntry,
       "tpStaticARPItemIp": tpStaticARPItemIp,
       "tpStaticARPItemMac": tpStaticARPItemMac,
       "tpStaticArpItemInterfaceName": tpStaticArpItemInterfaceName,
       "tpStaticARPItemStatus": tpStaticARPItemStatus,
       "tplinkStaticARPNotifications": tplinkStaticARPNotifications}
)
