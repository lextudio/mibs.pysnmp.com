# SNMP MIB module (MERU-CONFIG-STATICSTATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-STATICSTATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:09 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigStaticStation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwStaticStationTable_Object = MibTable
mwStaticStationTable = _MwStaticStationTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1)
)
if mibBuilder.loadTexts:
    mwStaticStationTable.setStatus("current")
_MwStaticStationEntry_Object = MibTableRow
mwStaticStationEntry = _MwStaticStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1)
)
mwStaticStationEntry.setIndexNames(
    (0, "MERU-CONFIG-STATICSTATION-MIB", "mwStaticStationTableIndex"),
)
if mibBuilder.loadTexts:
    mwStaticStationEntry.setStatus("current")
_MwStaticStationTableIndex_Type = Integer32
_MwStaticStationTableIndex_Object = MibTableColumn
mwStaticStationTableIndex = _MwStaticStationTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1, 1),
    _MwStaticStationTableIndex_Type()
)
mwStaticStationTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwStaticStationTableIndex.setStatus("current")
_MwStaticStationIpAddress_Type = IpAddress
_MwStaticStationIpAddress_Object = MibTableColumn
mwStaticStationIpAddress = _MwStaticStationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1, 2),
    _MwStaticStationIpAddress_Type()
)
mwStaticStationIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStaticStationIpAddress.setStatus("current")
_MwStaticStationMacAddress_Type = MacAddress
_MwStaticStationMacAddress_Object = MibTableColumn
mwStaticStationMacAddress = _MwStaticStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1, 3),
    _MwStaticStationMacAddress_Type()
)
mwStaticStationMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStaticStationMacAddress.setStatus("current")
_MwStaticStationRowStatus_Type = RowStatus
_MwStaticStationRowStatus_Object = MibTableColumn
mwStaticStationRowStatus = _MwStaticStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1, 4),
    _MwStaticStationRowStatus_Type()
)
mwStaticStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStaticStationRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-STATICSTATION-MIB",
    **{"mwConfigStaticStation": mwConfigStaticStation,
       "mwStaticStationTable": mwStaticStationTable,
       "mwStaticStationEntry": mwStaticStationEntry,
       "mwStaticStationTableIndex": mwStaticStationTableIndex,
       "mwStaticStationIpAddress": mwStaticStationIpAddress,
       "mwStaticStationMacAddress": mwStaticStationMacAddress,
       "mwStaticStationRowStatus": mwStaticStationRowStatus}
)
