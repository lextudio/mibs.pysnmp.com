# SNMP MIB module (CISCOSB-RLINVENTORYENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-RLINVENTORYENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:44 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class UnitIfindexType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ifindex", 1),
          ("unit", 0))
    )



# MIB Managed Objects in the order of their OIDs

_RlInventoryEntTable_Object = MibTable
rlInventoryEntTable = _RlInventoryEntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217)
)
if mibBuilder.loadTexts:
    rlInventoryEntTable.setStatus("current")
_RlInventoryEntEntry_Object = MibTableRow
rlInventoryEntEntry = _RlInventoryEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1)
)
rlInventoryEntEntry.setIndexNames(
    (0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitOrIfindex"),
    (0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitIfindexID"),
)
if mibBuilder.loadTexts:
    rlInventoryEntEntry.setStatus("current")
_RlInventoryEntUnitOrIfindex_Type = UnitIfindexType
_RlInventoryEntUnitOrIfindex_Object = MibTableColumn
rlInventoryEntUnitOrIfindex = _RlInventoryEntUnitOrIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 1),
    _RlInventoryEntUnitOrIfindex_Type()
)
rlInventoryEntUnitOrIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntUnitOrIfindex.setStatus("current")
_RlInventoryEntUnitIfindexID_Type = Unsigned32
_RlInventoryEntUnitIfindexID_Object = MibTableColumn
rlInventoryEntUnitIfindexID = _RlInventoryEntUnitIfindexID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 2),
    _RlInventoryEntUnitIfindexID_Type()
)
rlInventoryEntUnitIfindexID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntUnitIfindexID.setStatus("current")
_RlInventoryEntVendorID_Type = DisplayString
_RlInventoryEntVendorID_Object = MibTableColumn
rlInventoryEntVendorID = _RlInventoryEntVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 3),
    _RlInventoryEntVendorID_Type()
)
rlInventoryEntVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntVendorID.setStatus("current")
_RlInventoryEntPID_Type = DisplayString
_RlInventoryEntPID_Object = MibTableColumn
rlInventoryEntPID = _RlInventoryEntPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 4),
    _RlInventoryEntPID_Type()
)
rlInventoryEntPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntPID.setStatus("current")
_RlInventoryEntName_Type = DisplayString
_RlInventoryEntName_Object = MibTableColumn
rlInventoryEntName = _RlInventoryEntName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 5),
    _RlInventoryEntName_Type()
)
rlInventoryEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntName.setStatus("current")
_RlInventoryEntDescription_Type = DisplayString
_RlInventoryEntDescription_Object = MibTableColumn
rlInventoryEntDescription = _RlInventoryEntDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 6),
    _RlInventoryEntDescription_Type()
)
rlInventoryEntDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntDescription.setStatus("current")
_RlInventoryEntSerialNumber_Type = DisplayString
_RlInventoryEntSerialNumber_Object = MibTableColumn
rlInventoryEntSerialNumber = _RlInventoryEntSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 7),
    _RlInventoryEntSerialNumber_Type()
)
rlInventoryEntSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntSerialNumber.setStatus("current")
_RlInventoryEntUnitNum_Type = Unsigned32
_RlInventoryEntUnitNum_Object = MibTableColumn
rlInventoryEntUnitNum = _RlInventoryEntUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 8),
    _RlInventoryEntUnitNum_Type()
)
rlInventoryEntUnitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntUnitNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-RLINVENTORYENT-MIB",
    **{"UnitIfindexType": UnitIfindexType,
       "rlInventoryEntTable": rlInventoryEntTable,
       "rlInventoryEntEntry": rlInventoryEntEntry,
       "rlInventoryEntUnitOrIfindex": rlInventoryEntUnitOrIfindex,
       "rlInventoryEntUnitIfindexID": rlInventoryEntUnitIfindexID,
       "rlInventoryEntVendorID": rlInventoryEntVendorID,
       "rlInventoryEntPID": rlInventoryEntPID,
       "rlInventoryEntName": rlInventoryEntName,
       "rlInventoryEntDescription": rlInventoryEntDescription,
       "rlInventoryEntSerialNumber": rlInventoryEntSerialNumber,
       "rlInventoryEntUnitNum": rlInventoryEntUnitNum}
)
