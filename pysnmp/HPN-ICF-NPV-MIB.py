# SNMP MIB module (HPN-ICF-NPV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-NPV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:19 2024
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

(HpnicfFcVsanIndex,) = mibBuilder.importSymbols(
    "HPN-ICF-FC-TC-MIB",
    "HpnicfFcVsanIndex")

(hpnicfSan,
 hpnicfVsanIndex) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan",
    "hpnicfVsanIndex")

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

hpnicfNpv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6)
)
hpnicfNpv.setRevisions(
        ("2013-04-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfNpvIfIndexList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfNpvMibObjects_ObjectIdentity = ObjectIdentity
hpnicfNpvMibObjects = _HpnicfNpvMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1)
)
_HpnicfNpvConfiguration_ObjectIdentity = ObjectIdentity
hpnicfNpvConfiguration = _HpnicfNpvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1)
)
_HpnicfNpvGlobalObjects_ObjectIdentity = ObjectIdentity
hpnicfNpvGlobalObjects = _HpnicfNpvGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 1)
)
_HpnicfNpvLoadbalanceVsan_Type = HpnicfFcVsanIndex
_HpnicfNpvLoadbalanceVsan_Object = MibScalar
hpnicfNpvLoadbalanceVsan = _HpnicfNpvLoadbalanceVsan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 1, 1),
    _HpnicfNpvLoadbalanceVsan_Type()
)
hpnicfNpvLoadbalanceVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNpvLoadbalanceVsan.setStatus("current")
_HpnicfNpvTrafficMapConfigTable_Object = MibTable
hpnicfNpvTrafficMapConfigTable = _HpnicfNpvTrafficMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfNpvTrafficMapConfigTable.setStatus("current")
_HpnicfNpvTrafficMapConfigEntry_Object = MibTableRow
hpnicfNpvTrafficMapConfigEntry = _HpnicfNpvTrafficMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1)
)
hpnicfNpvTrafficMapConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNpvTrafficMapConfigEntry.setStatus("current")
_HpnicfNpvTrafficMapExternalIfIndexList_Type = HpnicfNpvIfIndexList
_HpnicfNpvTrafficMapExternalIfIndexList_Object = MibTableColumn
hpnicfNpvTrafficMapExternalIfIndexList = _HpnicfNpvTrafficMapExternalIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 1),
    _HpnicfNpvTrafficMapExternalIfIndexList_Type()
)
hpnicfNpvTrafficMapExternalIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNpvTrafficMapExternalIfIndexList.setStatus("current")
_HpnicfNpvTrafficMapLastChange_Type = TimeStamp
_HpnicfNpvTrafficMapLastChange_Object = MibTableColumn
hpnicfNpvTrafficMapLastChange = _HpnicfNpvTrafficMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 2),
    _HpnicfNpvTrafficMapLastChange_Type()
)
hpnicfNpvTrafficMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNpvTrafficMapLastChange.setStatus("current")
_HpnicfNpvTrafficMapRowStatus_Type = RowStatus
_HpnicfNpvTrafficMapRowStatus_Object = MibTableColumn
hpnicfNpvTrafficMapRowStatus = _HpnicfNpvTrafficMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 3),
    _HpnicfNpvTrafficMapRowStatus_Type()
)
hpnicfNpvTrafficMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNpvTrafficMapRowStatus.setStatus("current")
_HpnicfNpvServerIfTable_Object = MibTable
hpnicfNpvServerIfTable = _HpnicfNpvServerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfNpvServerIfTable.setStatus("current")
_HpnicfNpvServerIfEntry_Object = MibTableRow
hpnicfNpvServerIfEntry = _HpnicfNpvServerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3, 1)
)
hpnicfNpvServerIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNpvServerIfEntry.setStatus("current")
_HpnicfNpvExternalIfIndex_Type = InterfaceIndex
_HpnicfNpvExternalIfIndex_Object = MibTableColumn
hpnicfNpvExternalIfIndex = _HpnicfNpvExternalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3, 1, 1),
    _HpnicfNpvExternalIfIndex_Type()
)
hpnicfNpvExternalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNpvExternalIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-NPV-MIB",
    **{"HpnicfNpvIfIndexList": HpnicfNpvIfIndexList,
       "hpnicfNpv": hpnicfNpv,
       "hpnicfNpvMibObjects": hpnicfNpvMibObjects,
       "hpnicfNpvConfiguration": hpnicfNpvConfiguration,
       "hpnicfNpvGlobalObjects": hpnicfNpvGlobalObjects,
       "hpnicfNpvLoadbalanceVsan": hpnicfNpvLoadbalanceVsan,
       "hpnicfNpvTrafficMapConfigTable": hpnicfNpvTrafficMapConfigTable,
       "hpnicfNpvTrafficMapConfigEntry": hpnicfNpvTrafficMapConfigEntry,
       "hpnicfNpvTrafficMapExternalIfIndexList": hpnicfNpvTrafficMapExternalIfIndexList,
       "hpnicfNpvTrafficMapLastChange": hpnicfNpvTrafficMapLastChange,
       "hpnicfNpvTrafficMapRowStatus": hpnicfNpvTrafficMapRowStatus,
       "hpnicfNpvServerIfTable": hpnicfNpvServerIfTable,
       "hpnicfNpvServerIfEntry": hpnicfNpvServerIfEntry,
       "hpnicfNpvExternalIfIndex": hpnicfNpvExternalIfIndex}
)
