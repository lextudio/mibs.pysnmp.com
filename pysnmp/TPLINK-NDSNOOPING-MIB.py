# SNMP MIB module (TPLINK-NDSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-NDSNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:25 2024
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

tplinkNdSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92)
)
tplinkNdSnoopingMIB.setRevisions(
        ("2012-12-17 10:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkNdSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkNdSnoopingMIBObjects = _TplinkNdSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1)
)
_NdSnoopingGlobalConfig_ObjectIdentity = ObjectIdentity
ndSnoopingGlobalConfig = _NdSnoopingGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1)
)


class _NdSnoopingEnable_Type(Integer32):
    """Custom type ndSnoopingEnable based on Integer32"""
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


_NdSnoopingEnable_Type.__name__ = "Integer32"
_NdSnoopingEnable_Object = MibScalar
ndSnoopingEnable = _NdSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 1),
    _NdSnoopingEnable_Type()
)
ndSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndSnoopingEnable.setStatus("current")
_NdSnoopingVlanConfigTable_Object = MibTable
ndSnoopingVlanConfigTable = _NdSnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ndSnoopingVlanConfigTable.setStatus("current")
_NdSnoopingVlanConfigEntry_Object = MibTableRow
ndSnoopingVlanConfigEntry = _NdSnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1)
)
ndSnoopingVlanConfigEntry.setIndexNames(
    (0, "TPLINK-NDSNOOPING-MIB", "ndSnoopingVlanId"),
)
if mibBuilder.loadTexts:
    ndSnoopingVlanConfigEntry.setStatus("current")


class _NdSnoopingVlanId_Type(Integer32):
    """Custom type ndSnoopingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NdSnoopingVlanId_Type.__name__ = "Integer32"
_NdSnoopingVlanId_Object = MibTableColumn
ndSnoopingVlanId = _NdSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1, 1),
    _NdSnoopingVlanId_Type()
)
ndSnoopingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ndSnoopingVlanId.setStatus("current")


class _NdSnoopingVlanStatus_Type(Integer32):
    """Custom type ndSnoopingVlanStatus based on Integer32"""
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


_NdSnoopingVlanStatus_Type.__name__ = "Integer32"
_NdSnoopingVlanStatus_Object = MibTableColumn
ndSnoopingVlanStatus = _NdSnoopingVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1, 2),
    _NdSnoopingVlanStatus_Type()
)
ndSnoopingVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ndSnoopingVlanStatus.setStatus("current")
_NdSnoopingPortConfig_ObjectIdentity = ObjectIdentity
ndSnoopingPortConfig = _NdSnoopingPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3)
)
_NdSnoopingPortConfigTable_Object = MibTable
ndSnoopingPortConfigTable = _NdSnoopingPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ndSnoopingPortConfigTable.setStatus("current")
_NdSnoopingPortConfigEntry_Object = MibTableRow
ndSnoopingPortConfigEntry = _NdSnoopingPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1)
)
ndSnoopingPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ndSnoopingPortConfigEntry.setStatus("current")


class _NdSnoopingPort_Type(OctetString):
    """Custom type ndSnoopingPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NdSnoopingPort_Type.__name__ = "OctetString"
_NdSnoopingPort_Object = MibTableColumn
ndSnoopingPort = _NdSnoopingPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 1),
    _NdSnoopingPort_Type()
)
ndSnoopingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndSnoopingPort.setStatus("current")


class _NdSnoopingPortConfigMaxEntry_Type(Integer32):
    """Custom type ndSnoopingPortConfigMaxEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1024),
    )


_NdSnoopingPortConfigMaxEntry_Type.__name__ = "Integer32"
_NdSnoopingPortConfigMaxEntry_Object = MibTableColumn
ndSnoopingPortConfigMaxEntry = _NdSnoopingPortConfigMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 2),
    _NdSnoopingPortConfigMaxEntry_Type()
)
ndSnoopingPortConfigMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndSnoopingPortConfigMaxEntry.setStatus("current")


class _NdSnoopingPortConfigPortLag_Type(OctetString):
    """Custom type ndSnoopingPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NdSnoopingPortConfigPortLag_Type.__name__ = "OctetString"
_NdSnoopingPortConfigPortLag_Object = MibTableColumn
ndSnoopingPortConfigPortLag = _NdSnoopingPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 3),
    _NdSnoopingPortConfigPortLag_Type()
)
ndSnoopingPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndSnoopingPortConfigPortLag.setStatus("current")
_TplinkNdSnoopingNotifications_ObjectIdentity = ObjectIdentity
tplinkNdSnoopingNotifications = _TplinkNdSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 92, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-NDSNOOPING-MIB",
    **{"tplinkNdSnoopingMIB": tplinkNdSnoopingMIB,
       "tplinkNdSnoopingMIBObjects": tplinkNdSnoopingMIBObjects,
       "ndSnoopingGlobalConfig": ndSnoopingGlobalConfig,
       "ndSnoopingEnable": ndSnoopingEnable,
       "ndSnoopingVlanConfigTable": ndSnoopingVlanConfigTable,
       "ndSnoopingVlanConfigEntry": ndSnoopingVlanConfigEntry,
       "ndSnoopingVlanId": ndSnoopingVlanId,
       "ndSnoopingVlanStatus": ndSnoopingVlanStatus,
       "ndSnoopingPortConfig": ndSnoopingPortConfig,
       "ndSnoopingPortConfigTable": ndSnoopingPortConfigTable,
       "ndSnoopingPortConfigEntry": ndSnoopingPortConfigEntry,
       "ndSnoopingPort": ndSnoopingPort,
       "ndSnoopingPortConfigMaxEntry": ndSnoopingPortConfigMaxEntry,
       "ndSnoopingPortConfigPortLag": ndSnoopingPortConfigPortLag,
       "tplinkNdSnoopingNotifications": tplinkNdSnoopingNotifications}
)
