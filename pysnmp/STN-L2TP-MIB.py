# SNMP MIB module (STN-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:08 2024
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

(l2tp,) = mibBuilder.importSymbols(
    "L2TP-MIB",
    "l2tp")

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

(StnDomainMapType,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-TC",
    "StnDomainMapType")


# MODULE-IDENTITY

stnL2tp = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnL2tpObjects_ObjectIdentity = ObjectIdentity
stnL2tpObjects = _StnL2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 1)
)
_StnL2tpDomainMapTable_Object = MibTable
stnL2tpDomainMapTable = _StnL2tpDomainMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 1, 10)
)
if mibBuilder.loadTexts:
    stnL2tpDomainMapTable.setStatus("current")
_StnL2tpDomainMapTableEntry_Object = MibTableRow
stnL2tpDomainMapTableEntry = _StnL2tpDomainMapTableEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 1, 10, 1)
)
stnL2tpDomainMapTableEntry.setIndexNames(
    (0, "STN-L2TP-MIB", "stnL2tpDomainMapIdentifier"),
)
if mibBuilder.loadTexts:
    stnL2tpDomainMapTableEntry.setStatus("current")
_StnL2tpDomainMapIdentifier_Type = DisplayString
_StnL2tpDomainMapIdentifier_Object = MibTableColumn
stnL2tpDomainMapIdentifier = _StnL2tpDomainMapIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 1, 10, 1, 1),
    _StnL2tpDomainMapIdentifier_Type()
)
stnL2tpDomainMapIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnL2tpDomainMapIdentifier.setStatus("current")
_StnL2tpDomainMapHostName_Type = DisplayString
_StnL2tpDomainMapHostName_Object = MibTableColumn
stnL2tpDomainMapHostName = _StnL2tpDomainMapHostName_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 1, 10, 1, 2),
    _StnL2tpDomainMapHostName_Type()
)
stnL2tpDomainMapHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnL2tpDomainMapHostName.setStatus("current")
_StnL2tpDomainMapType_Type = StnDomainMapType
_StnL2tpDomainMapType_Object = MibTableColumn
stnL2tpDomainMapType = _StnL2tpDomainMapType_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 1, 10, 1, 3),
    _StnL2tpDomainMapType_Type()
)
stnL2tpDomainMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnL2tpDomainMapType.setStatus("current")
_StnL2tpDomainMapTypeInfo_Type = DisplayString
_StnL2tpDomainMapTypeInfo_Object = MibTableColumn
stnL2tpDomainMapTypeInfo = _StnL2tpDomainMapTypeInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 1, 10, 1, 4),
    _StnL2tpDomainMapTypeInfo_Type()
)
stnL2tpDomainMapTypeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnL2tpDomainMapTypeInfo.setStatus("current")
_StnL2tpMibConformance_ObjectIdentity = ObjectIdentity
stnL2tpMibConformance = _StnL2tpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 2)
)
_StnL2tpTraps_ObjectIdentity = ObjectIdentity
stnL2tpTraps = _StnL2tpTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 10, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-L2TP-MIB",
    **{"stnL2tp": stnL2tp,
       "stnL2tpObjects": stnL2tpObjects,
       "stnL2tpDomainMapTable": stnL2tpDomainMapTable,
       "stnL2tpDomainMapTableEntry": stnL2tpDomainMapTableEntry,
       "stnL2tpDomainMapIdentifier": stnL2tpDomainMapIdentifier,
       "stnL2tpDomainMapHostName": stnL2tpDomainMapHostName,
       "stnL2tpDomainMapType": stnL2tpDomainMapType,
       "stnL2tpDomainMapTypeInfo": stnL2tpDomainMapTypeInfo,
       "stnL2tpMibConformance": stnL2tpMibConformance,
       "stnL2tpTraps": stnL2tpTraps}
)
