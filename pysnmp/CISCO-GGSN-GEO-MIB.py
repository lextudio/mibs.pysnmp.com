# SNMP MIB module (CISCO-GGSN-GEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GGSN-GEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:49 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cggsnGeoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 724)
)
cggsnGeoMIB.setRevisions(
        ("2010-02-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CggsnGeoPassiveTable_Object = MibTable
cggsnGeoPassiveTable = _CggsnGeoPassiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 1)
)
if mibBuilder.loadTexts:
    cggsnGeoPassiveTable.setStatus("current")
_CggsnGeoPassiveEntry_Object = MibTableRow
cggsnGeoPassiveEntry = _CggsnGeoPassiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1)
)
cggsnGeoPassiveEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-GGSN-GEO-MIB", "cggsnGeoProcessNumber"),
)
if mibBuilder.loadTexts:
    cggsnGeoPassiveEntry.setStatus("current")


class _CggsnGeoProcessNumber_Type(Unsigned32):
    """Custom type cggsnGeoProcessNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CggsnGeoProcessNumber_Type.__name__ = "Unsigned32"
_CggsnGeoProcessNumber_Object = MibTableColumn
cggsnGeoProcessNumber = _CggsnGeoProcessNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 1),
    _CggsnGeoProcessNumber_Type()
)
cggsnGeoProcessNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnGeoProcessNumber.setStatus("current")


class _CggsnGeoPassiveStdbyIfName_Type(SnmpAdminString):
    """Custom type cggsnGeoPassiveStdbyIfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CggsnGeoPassiveStdbyIfName_Type.__name__ = "SnmpAdminString"
_CggsnGeoPassiveStdbyIfName_Object = MibTableColumn
cggsnGeoPassiveStdbyIfName = _CggsnGeoPassiveStdbyIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 2),
    _CggsnGeoPassiveStdbyIfName_Type()
)
cggsnGeoPassiveStdbyIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnGeoPassiveStdbyIfName.setStatus("current")
_CggsnGeoPassiveIfOnStdby_Type = TruthValue
_CggsnGeoPassiveIfOnStdby_Object = MibTableColumn
cggsnGeoPassiveIfOnStdby = _CggsnGeoPassiveIfOnStdby_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 3),
    _CggsnGeoPassiveIfOnStdby_Type()
)
cggsnGeoPassiveIfOnStdby.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnGeoPassiveIfOnStdby.setStatus("current")
_CggsnGeoVRFEnabled_Type = TruthValue
_CggsnGeoVRFEnabled_Object = MibTableColumn
cggsnGeoVRFEnabled = _CggsnGeoVRFEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 4),
    _CggsnGeoVRFEnabled_Type()
)
cggsnGeoVRFEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cggsnGeoVRFEnabled.setStatus("current")
_CggsnGeoRowStatus_Type = RowStatus
_CggsnGeoRowStatus_Object = MibTableColumn
cggsnGeoRowStatus = _CggsnGeoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 5),
    _CggsnGeoRowStatus_Type()
)
cggsnGeoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnGeoRowStatus.setStatus("current")
_CggsnGeoConformance_ObjectIdentity = ObjectIdentity
cggsnGeoConformance = _CggsnGeoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 2)
)
_CggsnGeogroups_ObjectIdentity = ObjectIdentity
cggsnGeogroups = _CggsnGeogroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1)
)
_CggsnGeoCompliances_ObjectIdentity = ObjectIdentity
cggsnGeoCompliances = _CggsnGeoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2)
)

# Managed Objects groups

cggsnGeoPassiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1, 1)
)
cggsnGeoPassiveGroup.setObjects(
      *(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveStdbyIfName"),
        ("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveIfOnStdby"),
        ("CISCO-GGSN-GEO-MIB", "cggsnGeoVRFEnabled"),
        ("CISCO-GGSN-GEO-MIB", "cggsnGeoRowStatus"))
)
if mibBuilder.loadTexts:
    cggsnGeoPassiveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cggsnGeoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cggsnGeoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GGSN-GEO-MIB",
    **{"cggsnGeoMIB": cggsnGeoMIB,
       "cggsnGeoPassiveTable": cggsnGeoPassiveTable,
       "cggsnGeoPassiveEntry": cggsnGeoPassiveEntry,
       "cggsnGeoProcessNumber": cggsnGeoProcessNumber,
       "cggsnGeoPassiveStdbyIfName": cggsnGeoPassiveStdbyIfName,
       "cggsnGeoPassiveIfOnStdby": cggsnGeoPassiveIfOnStdby,
       "cggsnGeoVRFEnabled": cggsnGeoVRFEnabled,
       "cggsnGeoRowStatus": cggsnGeoRowStatus,
       "cggsnGeoConformance": cggsnGeoConformance,
       "cggsnGeogroups": cggsnGeogroups,
       "cggsnGeoPassiveGroup": cggsnGeoPassiveGroup,
       "cggsnGeoCompliances": cggsnGeoCompliances,
       "cggsnGeoCompliance": cggsnGeoCompliance}
)
