# SNMP MIB module (NETSCREEN-ZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-ZONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:11 2024
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

(netscreenZone,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenZone")

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

netscreenZoneMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 8, 0)
)
netscreenZoneMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2000-05-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsZoneCfg_ObjectIdentity = ObjectIdentity
nsZoneCfg = _NsZoneCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 8, 1)
)
_NsZoneCfgTable_Object = MibTable
nsZoneCfgTable = _NsZoneCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 8, 1, 1)
)
if mibBuilder.loadTexts:
    nsZoneCfgTable.setStatus("current")
_NsZoneCfgEntry_Object = MibTableRow
nsZoneCfgEntry = _NsZoneCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1)
)
nsZoneCfgEntry.setIndexNames(
    (0, "NETSCREEN-ZONE-MIB", "nsZoneCfgId"),
)
if mibBuilder.loadTexts:
    nsZoneCfgEntry.setStatus("current")


class _NsZoneCfgId_Type(Integer32):
    """Custom type nsZoneCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsZoneCfgId_Type.__name__ = "Integer32"
_NsZoneCfgId_Object = MibTableColumn
nsZoneCfgId = _NsZoneCfgId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 1),
    _NsZoneCfgId_Type()
)
nsZoneCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsZoneCfgId.setStatus("current")


class _NsZoneCfgName_Type(DisplayString):
    """Custom type nsZoneCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsZoneCfgName_Type.__name__ = "DisplayString"
_NsZoneCfgName_Object = MibTableColumn
nsZoneCfgName = _NsZoneCfgName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 2),
    _NsZoneCfgName_Type()
)
nsZoneCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsZoneCfgName.setStatus("current")


class _NsZoneCfgType_Type(Integer32):
    """Custom type nsZoneCfgType based on Integer32"""
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
        *(("func", 4),
          ("layer2", 1),
          ("null", 3),
          ("regular", 0),
          ("tunnel", 2))
    )


_NsZoneCfgType_Type.__name__ = "Integer32"
_NsZoneCfgType_Object = MibTableColumn
nsZoneCfgType = _NsZoneCfgType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 3),
    _NsZoneCfgType_Type()
)
nsZoneCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsZoneCfgType.setStatus("current")
_NsZoneCfgVsys_Type = Integer32
_NsZoneCfgVsys_Object = MibTableColumn
nsZoneCfgVsys = _NsZoneCfgVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 4),
    _NsZoneCfgVsys_Type()
)
nsZoneCfgVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsZoneCfgVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-ZONE-MIB",
    **{"netscreenZoneMibModule": netscreenZoneMibModule,
       "nsZoneCfg": nsZoneCfg,
       "nsZoneCfgTable": nsZoneCfgTable,
       "nsZoneCfgEntry": nsZoneCfgEntry,
       "nsZoneCfgId": nsZoneCfgId,
       "nsZoneCfgName": nsZoneCfgName,
       "nsZoneCfgType": nsZoneCfgType,
       "nsZoneCfgVsys": nsZoneCfgVsys}
)
