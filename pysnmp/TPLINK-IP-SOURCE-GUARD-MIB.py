# SNMP MIB module (TPLINK-IP-SOURCE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-IP-SOURCE-GUARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:09 2024
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

tplinkIpSourceGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29)
)
tplinkIpSourceGuardMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIpSourceGuardMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpSourceGuardMIBObjects = _TplinkIpSourceGuardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1)
)
_TpIpSourceGuardConfig_ObjectIdentity = ObjectIdentity
tpIpSourceGuardConfig = _TpIpSourceGuardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1)
)
_TpIpSourceGuardConfigTable_Object = MibTable
tpIpSourceGuardConfigTable = _TpIpSourceGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigTable.setStatus("current")
_TpIpSourceGuardConfigEntry_Object = MibTableRow
tpIpSourceGuardConfigEntry = _TpIpSourceGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1, 1)
)
tpIpSourceGuardConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigEntry.setStatus("current")


class _TpIpSourceGuardConfigPort_Type(OctetString):
    """Custom type tpIpSourceGuardConfigPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpIpSourceGuardConfigPort_Type.__name__ = "OctetString"
_TpIpSourceGuardConfigPort_Object = MibTableColumn
tpIpSourceGuardConfigPort = _TpIpSourceGuardConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1, 1, 1),
    _TpIpSourceGuardConfigPort_Type()
)
tpIpSourceGuardConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigPort.setStatus("current")


class _TpIpSourceGuardConfigType_Type(Integer32):
    """Custom type tpIpSourceGuardConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("sip-mac", 2))
    )


_TpIpSourceGuardConfigType_Type.__name__ = "Integer32"
_TpIpSourceGuardConfigType_Object = MibTableColumn
tpIpSourceGuardConfigType = _TpIpSourceGuardConfigType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1, 1, 2),
    _TpIpSourceGuardConfigType_Type()
)
tpIpSourceGuardConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigType.setStatus("current")


class _TpIpSourceGuardConfigPortLag_Type(OctetString):
    """Custom type tpIpSourceGuardConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpIpSourceGuardConfigPortLag_Type.__name__ = "OctetString"
_TpIpSourceGuardConfigPortLag_Object = MibTableColumn
tpIpSourceGuardConfigPortLag = _TpIpSourceGuardConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1, 1, 3),
    _TpIpSourceGuardConfigPortLag_Type()
)
tpIpSourceGuardConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigPortLag.setStatus("current")
_TplinkIpSourceGuardNotifications_ObjectIdentity = ObjectIdentity
tplinkIpSourceGuardNotifications = _TplinkIpSourceGuardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IP-SOURCE-GUARD-MIB",
    **{"tplinkIpSourceGuardMIB": tplinkIpSourceGuardMIB,
       "tplinkIpSourceGuardMIBObjects": tplinkIpSourceGuardMIBObjects,
       "tpIpSourceGuardConfig": tpIpSourceGuardConfig,
       "tpIpSourceGuardConfigTable": tpIpSourceGuardConfigTable,
       "tpIpSourceGuardConfigEntry": tpIpSourceGuardConfigEntry,
       "tpIpSourceGuardConfigPort": tpIpSourceGuardConfigPort,
       "tpIpSourceGuardConfigType": tpIpSourceGuardConfigType,
       "tpIpSourceGuardConfigPortLag": tpIpSourceGuardConfigPortLag,
       "tplinkIpSourceGuardNotifications": tplinkIpSourceGuardNotifications}
)
