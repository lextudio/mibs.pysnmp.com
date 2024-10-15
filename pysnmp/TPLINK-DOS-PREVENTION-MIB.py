# SNMP MIB module (TPLINK-DOS-PREVENTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-DOS-PREVENTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:58 2024
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


# MODULE-IDENTITY

tplinkDosPreventionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30)
)
tplinkDosPreventionMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDosPreventionMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDosPreventionMIBObjects = _TplinkDosPreventionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1)
)
_TpDosDefendGlobalConfig_ObjectIdentity = ObjectIdentity
tpDosDefendGlobalConfig = _TpDosDefendGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1, 1)
)


class _TpDosDefendGlobalEnable_Type(Integer32):
    """Custom type tpDosDefendGlobalEnable based on Integer32"""
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


_TpDosDefendGlobalEnable_Type.__name__ = "Integer32"
_TpDosDefendGlobalEnable_Object = MibScalar
tpDosDefendGlobalEnable = _TpDosDefendGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1, 1, 1),
    _TpDosDefendGlobalEnable_Type()
)
tpDosDefendGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDosDefendGlobalEnable.setStatus("current")
_TpDosDefendList_ObjectIdentity = ObjectIdentity
tpDosDefendList = _TpDosDefendList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1, 2)
)
_TpDosDefendListTable_Object = MibTable
tpDosDefendListTable = _TpDosDefendListTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpDosDefendListTable.setStatus("current")
_TpDosDefendListEntry_Object = MibTableRow
tpDosDefendListEntry = _TpDosDefendListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1, 2, 1, 1)
)
tpDosDefendListEntry.setIndexNames(
    (0, "TPLINK-DOS-PREVENTION-MIB", "tpDosDefendListIndex"),
)
if mibBuilder.loadTexts:
    tpDosDefendListEntry.setStatus("current")
_TpDosDefendListIndex_Type = Integer32
_TpDosDefendListIndex_Object = MibTableColumn
tpDosDefendListIndex = _TpDosDefendListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1, 2, 1, 1, 1),
    _TpDosDefendListIndex_Type()
)
tpDosDefendListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDosDefendListIndex.setStatus("current")
_TpDosDefendListType_Type = OctetString
_TpDosDefendListType_Object = MibTableColumn
tpDosDefendListType = _TpDosDefendListType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1, 2, 1, 1, 2),
    _TpDosDefendListType_Type()
)
tpDosDefendListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDosDefendListType.setStatus("current")


class _TpDosDefendListEntryEnable_Type(Integer32):
    """Custom type tpDosDefendListEntryEnable based on Integer32"""
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


_TpDosDefendListEntryEnable_Type.__name__ = "Integer32"
_TpDosDefendListEntryEnable_Object = MibTableColumn
tpDosDefendListEntryEnable = _TpDosDefendListEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 1, 2, 1, 1, 3),
    _TpDosDefendListEntryEnable_Type()
)
tpDosDefendListEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDosDefendListEntryEnable.setStatus("current")
_TplinkDosPreventionNotifications_ObjectIdentity = ObjectIdentity
tplinkDosPreventionNotifications = _TplinkDosPreventionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 30, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DOS-PREVENTION-MIB",
    **{"tplinkDosPreventionMIB": tplinkDosPreventionMIB,
       "tplinkDosPreventionMIBObjects": tplinkDosPreventionMIBObjects,
       "tpDosDefendGlobalConfig": tpDosDefendGlobalConfig,
       "tpDosDefendGlobalEnable": tpDosDefendGlobalEnable,
       "tpDosDefendList": tpDosDefendList,
       "tpDosDefendListTable": tpDosDefendListTable,
       "tpDosDefendListEntry": tpDosDefendListEntry,
       "tpDosDefendListIndex": tpDosDefendListIndex,
       "tpDosDefendListType": tpDosDefendListType,
       "tpDosDefendListEntryEnable": tpDosDefendListEntryEnable,
       "tplinkDosPreventionNotifications": tplinkDosPreventionNotifications}
)
