# SNMP MIB module (ZYXEL-MAC-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MAC-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:17 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMacFilter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMacFilterSetup_ObjectIdentity = ObjectIdentity
zyxelMacFilterSetup = _ZyxelMacFilterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1)
)
_ZyMacFilterMaxNumberOfRules_Type = Integer32
_ZyMacFilterMaxNumberOfRules_Object = MibScalar
zyMacFilterMaxNumberOfRules = _ZyMacFilterMaxNumberOfRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 1),
    _ZyMacFilterMaxNumberOfRules_Type()
)
zyMacFilterMaxNumberOfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMacFilterMaxNumberOfRules.setStatus("current")
_ZyxelMacFilterTable_Object = MibTable
zyxelMacFilterTable = _ZyxelMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelMacFilterTable.setStatus("current")
_ZyxelMacFilterEntry_Object = MibTableRow
zyxelMacFilterEntry = _ZyxelMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1)
)
zyxelMacFilterEntry.setIndexNames(
    (0, "ZYXEL-MAC-FILTER-MIB", "zyMacFilterMacAddress"),
    (0, "ZYXEL-MAC-FILTER-MIB", "zyMacFilterVid"),
)
if mibBuilder.loadTexts:
    zyxelMacFilterEntry.setStatus("current")
_ZyMacFilterMacAddress_Type = MacAddress
_ZyMacFilterMacAddress_Object = MibTableColumn
zyMacFilterMacAddress = _ZyMacFilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 1),
    _ZyMacFilterMacAddress_Type()
)
zyMacFilterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMacFilterMacAddress.setStatus("current")
_ZyMacFilterVid_Type = Integer32
_ZyMacFilterVid_Object = MibTableColumn
zyMacFilterVid = _ZyMacFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 2),
    _ZyMacFilterVid_Type()
)
zyMacFilterVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMacFilterVid.setStatus("current")
_ZyMacFilterName_Type = DisplayString
_ZyMacFilterName_Object = MibTableColumn
zyMacFilterName = _ZyMacFilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 3),
    _ZyMacFilterName_Type()
)
zyMacFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacFilterName.setStatus("current")


class _ZyMacFilterAction_Type(Integer32):
    """Custom type zyMacFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("discardDestination", 2),
          ("discardSource", 1))
    )


_ZyMacFilterAction_Type.__name__ = "Integer32"
_ZyMacFilterAction_Object = MibTableColumn
zyMacFilterAction = _ZyMacFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 4),
    _ZyMacFilterAction_Type()
)
zyMacFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacFilterAction.setStatus("current")
_ZyMacFilterRowStatus_Type = RowStatus
_ZyMacFilterRowStatus_Object = MibTableColumn
zyMacFilterRowStatus = _ZyMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 5),
    _ZyMacFilterRowStatus_Type()
)
zyMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyMacFilterRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MAC-FILTER-MIB",
    **{"zyxelMacFilter": zyxelMacFilter,
       "zyxelMacFilterSetup": zyxelMacFilterSetup,
       "zyMacFilterMaxNumberOfRules": zyMacFilterMaxNumberOfRules,
       "zyxelMacFilterTable": zyxelMacFilterTable,
       "zyxelMacFilterEntry": zyxelMacFilterEntry,
       "zyMacFilterMacAddress": zyMacFilterMacAddress,
       "zyMacFilterVid": zyMacFilterVid,
       "zyMacFilterName": zyMacFilterName,
       "zyMacFilterAction": zyMacFilterAction,
       "zyMacFilterRowStatus": zyMacFilterRowStatus}
)
