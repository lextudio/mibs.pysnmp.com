# SNMP MIB module (HH3C-NPV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-NPV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:21 2024
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

(Hh3cFcVsanIndex,) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcVsanIndex")

(hh3cSan,
 hh3cVsanIndex) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan",
    "hh3cVsanIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hh3cNpv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6)
)
hh3cNpv.setRevisions(
        ("2013-04-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cNpvIfIndexList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cNpvMibObjects_ObjectIdentity = ObjectIdentity
hh3cNpvMibObjects = _Hh3cNpvMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1)
)
_Hh3cNpvConfiguration_ObjectIdentity = ObjectIdentity
hh3cNpvConfiguration = _Hh3cNpvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1)
)
_Hh3cNpvGlobalObjects_ObjectIdentity = ObjectIdentity
hh3cNpvGlobalObjects = _Hh3cNpvGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 1)
)
_Hh3cNpvLoadbalanceVsan_Type = Hh3cFcVsanIndex
_Hh3cNpvLoadbalanceVsan_Object = MibScalar
hh3cNpvLoadbalanceVsan = _Hh3cNpvLoadbalanceVsan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 1, 1),
    _Hh3cNpvLoadbalanceVsan_Type()
)
hh3cNpvLoadbalanceVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNpvLoadbalanceVsan.setStatus("current")
_Hh3cNpvTrafficMapConfigTable_Object = MibTable
hh3cNpvTrafficMapConfigTable = _Hh3cNpvTrafficMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapConfigTable.setStatus("current")
_Hh3cNpvTrafficMapConfigEntry_Object = MibTableRow
hh3cNpvTrafficMapConfigEntry = _Hh3cNpvTrafficMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2, 1)
)
hh3cNpvTrafficMapConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapConfigEntry.setStatus("current")
_Hh3cNpvTrafficMapExternalIfIndexList_Type = Hh3cNpvIfIndexList
_Hh3cNpvTrafficMapExternalIfIndexList_Object = MibTableColumn
hh3cNpvTrafficMapExternalIfIndexList = _Hh3cNpvTrafficMapExternalIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2, 1, 1),
    _Hh3cNpvTrafficMapExternalIfIndexList_Type()
)
hh3cNpvTrafficMapExternalIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapExternalIfIndexList.setStatus("current")
_Hh3cNpvTrafficMapLastChange_Type = TimeStamp
_Hh3cNpvTrafficMapLastChange_Object = MibTableColumn
hh3cNpvTrafficMapLastChange = _Hh3cNpvTrafficMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2, 1, 2),
    _Hh3cNpvTrafficMapLastChange_Type()
)
hh3cNpvTrafficMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapLastChange.setStatus("current")
_Hh3cNpvTrafficMapRowStatus_Type = RowStatus
_Hh3cNpvTrafficMapRowStatus_Object = MibTableColumn
hh3cNpvTrafficMapRowStatus = _Hh3cNpvTrafficMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2, 1, 3),
    _Hh3cNpvTrafficMapRowStatus_Type()
)
hh3cNpvTrafficMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapRowStatus.setStatus("current")
_Hh3cNpvServerIfTable_Object = MibTable
hh3cNpvServerIfTable = _Hh3cNpvServerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cNpvServerIfTable.setStatus("current")
_Hh3cNpvServerIfEntry_Object = MibTableRow
hh3cNpvServerIfEntry = _Hh3cNpvServerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 3, 1)
)
hh3cNpvServerIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cNpvServerIfEntry.setStatus("current")
_Hh3cNpvExternalIfIndex_Type = InterfaceIndex
_Hh3cNpvExternalIfIndex_Object = MibTableColumn
hh3cNpvExternalIfIndex = _Hh3cNpvExternalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 3, 1, 1),
    _Hh3cNpvExternalIfIndex_Type()
)
hh3cNpvExternalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNpvExternalIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NPV-MIB",
    **{"Hh3cNpvIfIndexList": Hh3cNpvIfIndexList,
       "hh3cNpv": hh3cNpv,
       "hh3cNpvMibObjects": hh3cNpvMibObjects,
       "hh3cNpvConfiguration": hh3cNpvConfiguration,
       "hh3cNpvGlobalObjects": hh3cNpvGlobalObjects,
       "hh3cNpvLoadbalanceVsan": hh3cNpvLoadbalanceVsan,
       "hh3cNpvTrafficMapConfigTable": hh3cNpvTrafficMapConfigTable,
       "hh3cNpvTrafficMapConfigEntry": hh3cNpvTrafficMapConfigEntry,
       "hh3cNpvTrafficMapExternalIfIndexList": hh3cNpvTrafficMapExternalIfIndexList,
       "hh3cNpvTrafficMapLastChange": hh3cNpvTrafficMapLastChange,
       "hh3cNpvTrafficMapRowStatus": hh3cNpvTrafficMapRowStatus,
       "hh3cNpvServerIfTable": hh3cNpvServerIfTable,
       "hh3cNpvServerIfEntry": hh3cNpvServerIfEntry,
       "hh3cNpvExternalIfIndex": hh3cNpvExternalIfIndex}
)
