# SNMP MIB module (NTWS-AP-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-AP-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:51 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(NtwsApSerialNum,) = mibBuilder.importSymbols(
    "NTWS-AP-TC",
    "NtwsApSerialNum")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntwsApIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16)
)
ntwsApIfMib.setRevisions(
        ("2008-11-20 00:01",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsApInterfaceIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_NtwsApIfMibObjects_ObjectIdentity = ObjectIdentity
ntwsApIfMibObjects = _NtwsApIfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1)
)
_NtwsApIfTable_Object = MibTable
ntwsApIfTable = _NtwsApIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsApIfTable.setStatus("current")
_NtwsApIfEntry_Object = MibTableRow
ntwsApIfEntry = _NtwsApIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1)
)
ntwsApIfEntry.setIndexNames(
    (0, "NTWS-AP-IF-MIB", "ntwsApIfApSerialNum"),
    (0, "NTWS-AP-IF-MIB", "ntwsApIfIndex"),
)
if mibBuilder.loadTexts:
    ntwsApIfEntry.setStatus("current")
_NtwsApIfApSerialNum_Type = NtwsApSerialNum
_NtwsApIfApSerialNum_Object = MibTableColumn
ntwsApIfApSerialNum = _NtwsApIfApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 1),
    _NtwsApIfApSerialNum_Type()
)
ntwsApIfApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApIfApSerialNum.setStatus("current")
_NtwsApIfIndex_Type = NtwsApInterfaceIndex
_NtwsApIfIndex_Object = MibTableColumn
ntwsApIfIndex = _NtwsApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 2),
    _NtwsApIfIndex_Type()
)
ntwsApIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApIfIndex.setStatus("current")
_NtwsApIfName_Type = DisplayString
_NtwsApIfName_Object = MibTableColumn
ntwsApIfName = _NtwsApIfName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 3),
    _NtwsApIfName_Type()
)
ntwsApIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApIfName.setStatus("current")
_NtwsApIfType_Type = IANAifType
_NtwsApIfType_Object = MibTableColumn
ntwsApIfType = _NtwsApIfType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 4),
    _NtwsApIfType_Type()
)
ntwsApIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApIfType.setStatus("current")
_NtwsApIfMtu_Type = Unsigned32
_NtwsApIfMtu_Object = MibTableColumn
ntwsApIfMtu = _NtwsApIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 5),
    _NtwsApIfMtu_Type()
)
ntwsApIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApIfMtu.setStatus("current")
_NtwsApIfHighSpeed_Type = Gauge32
_NtwsApIfHighSpeed_Object = MibTableColumn
ntwsApIfHighSpeed = _NtwsApIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 6),
    _NtwsApIfHighSpeed_Type()
)
ntwsApIfHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApIfHighSpeed.setStatus("current")
_NtwsApIfMac_Type = MacAddress
_NtwsApIfMac_Object = MibTableColumn
ntwsApIfMac = _NtwsApIfMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 7),
    _NtwsApIfMac_Type()
)
ntwsApIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApIfMac.setStatus("current")
_NtwsApIfConformance_ObjectIdentity = ObjectIdentity
ntwsApIfConformance = _NtwsApIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2)
)
_NtwsApIfCompliances_ObjectIdentity = ObjectIdentity
ntwsApIfCompliances = _NtwsApIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 1)
)
_NtwsApIfGroups_ObjectIdentity = ObjectIdentity
ntwsApIfGroups = _NtwsApIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 2)
)

# Managed Objects groups

ntwsApIfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 2, 1)
)
ntwsApIfBasicGroup.setObjects(
      *(("NTWS-AP-IF-MIB", "ntwsApIfName"),
        ("NTWS-AP-IF-MIB", "ntwsApIfType"),
        ("NTWS-AP-IF-MIB", "ntwsApIfMtu"),
        ("NTWS-AP-IF-MIB", "ntwsApIfHighSpeed"),
        ("NTWS-AP-IF-MIB", "ntwsApIfMac"))
)
if mibBuilder.loadTexts:
    ntwsApIfBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsApIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsApIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-AP-IF-MIB",
    **{"NtwsApInterfaceIndex": NtwsApInterfaceIndex,
       "ntwsApIfMib": ntwsApIfMib,
       "ntwsApIfMibObjects": ntwsApIfMibObjects,
       "ntwsApIfTable": ntwsApIfTable,
       "ntwsApIfEntry": ntwsApIfEntry,
       "ntwsApIfApSerialNum": ntwsApIfApSerialNum,
       "ntwsApIfIndex": ntwsApIfIndex,
       "ntwsApIfName": ntwsApIfName,
       "ntwsApIfType": ntwsApIfType,
       "ntwsApIfMtu": ntwsApIfMtu,
       "ntwsApIfHighSpeed": ntwsApIfHighSpeed,
       "ntwsApIfMac": ntwsApIfMac,
       "ntwsApIfConformance": ntwsApIfConformance,
       "ntwsApIfCompliances": ntwsApIfCompliances,
       "ntwsApIfCompliance": ntwsApIfCompliance,
       "ntwsApIfGroups": ntwsApIfGroups,
       "ntwsApIfBasicGroup": ntwsApIfBasicGroup}
)
