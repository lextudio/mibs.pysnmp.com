# SNMP MIB module (TPLINK-IPV6-SOURCE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-IPV6-SOURCE-GUARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:12 2024
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

tplinkIpv6SourceGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94)
)
tplinkIpv6SourceGuardMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIpv6SourceGuardMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpv6SourceGuardMIBObjects = _TplinkIpv6SourceGuardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94, 1)
)
_TpIpv6SourceGuardConfig_ObjectIdentity = ObjectIdentity
tpIpv6SourceGuardConfig = _TpIpv6SourceGuardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1)
)
_TpIpv6SourceGuardConfigTable_Object = MibTable
tpIpv6SourceGuardConfigTable = _TpIpv6SourceGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpIpv6SourceGuardConfigTable.setStatus("current")
_TpIpv6SourceGuardConfigEntry_Object = MibTableRow
tpIpv6SourceGuardConfigEntry = _TpIpv6SourceGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1)
)
tpIpv6SourceGuardConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIpv6SourceGuardConfigEntry.setStatus("current")


class _TpIpv6SourceGuardConfigPort_Type(OctetString):
    """Custom type tpIpv6SourceGuardConfigPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpIpv6SourceGuardConfigPort_Type.__name__ = "OctetString"
_TpIpv6SourceGuardConfigPort_Object = MibTableColumn
tpIpv6SourceGuardConfigPort = _TpIpv6SourceGuardConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 1),
    _TpIpv6SourceGuardConfigPort_Type()
)
tpIpv6SourceGuardConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpv6SourceGuardConfigPort.setStatus("current")


class _TpIpv6SourceGuardConfigType_Type(Integer32):
    """Custom type tpIpv6SourceGuardConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("sipv6-mac", 2))
    )


_TpIpv6SourceGuardConfigType_Type.__name__ = "Integer32"
_TpIpv6SourceGuardConfigType_Object = MibTableColumn
tpIpv6SourceGuardConfigType = _TpIpv6SourceGuardConfigType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 2),
    _TpIpv6SourceGuardConfigType_Type()
)
tpIpv6SourceGuardConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpv6SourceGuardConfigType.setStatus("current")


class _TpIpv6SourceGuardConfigPortLag_Type(OctetString):
    """Custom type tpIpv6SourceGuardConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpIpv6SourceGuardConfigPortLag_Type.__name__ = "OctetString"
_TpIpv6SourceGuardConfigPortLag_Object = MibTableColumn
tpIpv6SourceGuardConfigPortLag = _TpIpv6SourceGuardConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 3),
    _TpIpv6SourceGuardConfigPortLag_Type()
)
tpIpv6SourceGuardConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpv6SourceGuardConfigPortLag.setStatus("current")
_TplinkIpv6SourceGuardNotifications_ObjectIdentity = ObjectIdentity
tplinkIpv6SourceGuardNotifications = _TplinkIpv6SourceGuardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 94, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IPV6-SOURCE-GUARD-MIB",
    **{"tplinkIpv6SourceGuardMIB": tplinkIpv6SourceGuardMIB,
       "tplinkIpv6SourceGuardMIBObjects": tplinkIpv6SourceGuardMIBObjects,
       "tpIpv6SourceGuardConfig": tpIpv6SourceGuardConfig,
       "tpIpv6SourceGuardConfigTable": tpIpv6SourceGuardConfigTable,
       "tpIpv6SourceGuardConfigEntry": tpIpv6SourceGuardConfigEntry,
       "tpIpv6SourceGuardConfigPort": tpIpv6SourceGuardConfigPort,
       "tpIpv6SourceGuardConfigType": tpIpv6SourceGuardConfigType,
       "tpIpv6SourceGuardConfigPortLag": tpIpv6SourceGuardConfigPortLag,
       "tplinkIpv6SourceGuardNotifications": tplinkIpv6SourceGuardNotifications}
)
