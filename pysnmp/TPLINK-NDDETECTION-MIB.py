# SNMP MIB module (TPLINK-NDDETECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-NDDETECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:24 2024
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

tplinkNdDetectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93)
)
tplinkNdDetectionMIB.setRevisions(
        ("2012-12-17 10:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkNdDetectionMIBObjects_ObjectIdentity = ObjectIdentity
tplinkNdDetectionMIBObjects = _TplinkNdDetectionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1)
)
_NdDetectionGlobalConfig_ObjectIdentity = ObjectIdentity
ndDetectionGlobalConfig = _NdDetectionGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 1)
)


class _NdDetectionEnable_Type(Integer32):
    """Custom type ndDetectionEnable based on Integer32"""
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


_NdDetectionEnable_Type.__name__ = "Integer32"
_NdDetectionEnable_Object = MibScalar
ndDetectionEnable = _NdDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 1, 1),
    _NdDetectionEnable_Type()
)
ndDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndDetectionEnable.setStatus("current")
_NdDetectionVlanConfigTable_Object = MibTable
ndDetectionVlanConfigTable = _NdDetectionVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ndDetectionVlanConfigTable.setStatus("current")
_NdDetectionVlanConfigEntry_Object = MibTableRow
ndDetectionVlanConfigEntry = _NdDetectionVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 1, 2, 1)
)
ndDetectionVlanConfigEntry.setIndexNames(
    (0, "TPLINK-NDDETECTION-MIB", "ndDetectionVlanId"),
)
if mibBuilder.loadTexts:
    ndDetectionVlanConfigEntry.setStatus("current")


class _NdDetectionVlanId_Type(Integer32):
    """Custom type ndDetectionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NdDetectionVlanId_Type.__name__ = "Integer32"
_NdDetectionVlanId_Object = MibTableColumn
ndDetectionVlanId = _NdDetectionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 1, 2, 1, 1),
    _NdDetectionVlanId_Type()
)
ndDetectionVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ndDetectionVlanId.setStatus("current")


class _NdDetectionVlanStatus_Type(Integer32):
    """Custom type ndDetectionVlanStatus based on Integer32"""
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


_NdDetectionVlanStatus_Type.__name__ = "Integer32"
_NdDetectionVlanStatus_Object = MibTableColumn
ndDetectionVlanStatus = _NdDetectionVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 1, 2, 1, 2),
    _NdDetectionVlanStatus_Type()
)
ndDetectionVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ndDetectionVlanStatus.setStatus("current")
_NdDetectionPortConfig_ObjectIdentity = ObjectIdentity
ndDetectionPortConfig = _NdDetectionPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3)
)
_NdDetectionPortConfigTable_Object = MibTable
ndDetectionPortConfigTable = _NdDetectionPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ndDetectionPortConfigTable.setStatus("current")
_NdDetectionPortConfigEntry_Object = MibTableRow
ndDetectionPortConfigEntry = _NdDetectionPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1, 1)
)
ndDetectionPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ndDetectionPortConfigEntry.setStatus("current")


class _NdDetectionPort_Type(OctetString):
    """Custom type ndDetectionPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NdDetectionPort_Type.__name__ = "OctetString"
_NdDetectionPort_Object = MibTableColumn
ndDetectionPort = _NdDetectionPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1, 1, 1),
    _NdDetectionPort_Type()
)
ndDetectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndDetectionPort.setStatus("current")


class _NdDetectionPortConfigTrustedPort_Type(Integer32):
    """Custom type ndDetectionPortConfigTrustedPort based on Integer32"""
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


_NdDetectionPortConfigTrustedPort_Type.__name__ = "Integer32"
_NdDetectionPortConfigTrustedPort_Object = MibTableColumn
ndDetectionPortConfigTrustedPort = _NdDetectionPortConfigTrustedPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1, 1, 2),
    _NdDetectionPortConfigTrustedPort_Type()
)
ndDetectionPortConfigTrustedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndDetectionPortConfigTrustedPort.setStatus("current")


class _NdDetectionPortConfigPortLag_Type(OctetString):
    """Custom type ndDetectionPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NdDetectionPortConfigPortLag_Type.__name__ = "OctetString"
_NdDetectionPortConfigPortLag_Object = MibTableColumn
ndDetectionPortConfigPortLag = _NdDetectionPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1, 1, 3),
    _NdDetectionPortConfigPortLag_Type()
)
ndDetectionPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndDetectionPortConfigPortLag.setStatus("current")
_TplinkNdDetectionNotifications_ObjectIdentity = ObjectIdentity
tplinkNdDetectionNotifications = _TplinkNdDetectionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-NDDETECTION-MIB",
    **{"tplinkNdDetectionMIB": tplinkNdDetectionMIB,
       "tplinkNdDetectionMIBObjects": tplinkNdDetectionMIBObjects,
       "ndDetectionGlobalConfig": ndDetectionGlobalConfig,
       "ndDetectionEnable": ndDetectionEnable,
       "ndDetectionVlanConfigTable": ndDetectionVlanConfigTable,
       "ndDetectionVlanConfigEntry": ndDetectionVlanConfigEntry,
       "ndDetectionVlanId": ndDetectionVlanId,
       "ndDetectionVlanStatus": ndDetectionVlanStatus,
       "ndDetectionPortConfig": ndDetectionPortConfig,
       "ndDetectionPortConfigTable": ndDetectionPortConfigTable,
       "ndDetectionPortConfigEntry": ndDetectionPortConfigEntry,
       "ndDetectionPort": ndDetectionPort,
       "ndDetectionPortConfigTrustedPort": ndDetectionPortConfigTrustedPort,
       "ndDetectionPortConfigPortLag": ndDetectionPortConfigPortLag,
       "tplinkNdDetectionNotifications": tplinkNdDetectionNotifications}
)
