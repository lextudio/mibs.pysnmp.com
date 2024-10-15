# SNMP MIB module (BTI7800-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BTI7800-INVENTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:56 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bTI7800_INVENTORY_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2)
)
bTI7800_INVENTORY_MIB.setRevisions(
        ("2014-12-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class InetAddressIP(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class BicIndexT(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class FanIndexT(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )



class PemIndexT(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class CmmIndexT(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class PortIndexT(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )



class ModuleIndexT(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )



class ChassisIndexT(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



# MIB Managed Objects in the order of their OIDs

_Inventory_chassisTable_Object = MibTable
inventory_chassisTable = _Inventory_chassisTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    inventory_chassisTable.setStatus("current")
_Inventory_chassisEntry_Object = MibTableRow
inventory_chassisEntry = _Inventory_chassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1)
)
inventory_chassisEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-chassisChassisNum"),
)
if mibBuilder.loadTexts:
    inventory_chassisEntry.setStatus("current")
_Inventory_chassisChassisNum_Type = ChassisIndexT
_Inventory_chassisChassisNum_Object = MibScalar
inventory_chassisChassisNum = _Inventory_chassisChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 1),
    _Inventory_chassisChassisNum_Type()
)
inventory_chassisChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_chassisChassisNum.setStatus("current")
_Inventory_chassisName_Type = String
_Inventory_chassisName_Object = MibScalar
inventory_chassisName = _Inventory_chassisName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 2),
    _Inventory_chassisName_Type()
)
inventory_chassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_chassisName.setStatus("current")
_Inventory_chassisPEC_Type = String
_Inventory_chassisPEC_Object = MibScalar
inventory_chassisPEC = _Inventory_chassisPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 3),
    _Inventory_chassisPEC_Type()
)
inventory_chassisPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_chassisPEC.setStatus("current")
_Inventory_chassisRevision_Type = UnsignedShort
_Inventory_chassisRevision_Object = MibScalar
inventory_chassisRevision = _Inventory_chassisRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 4),
    _Inventory_chassisRevision_Type()
)
inventory_chassisRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_chassisRevision.setStatus("current")
_Inventory_chassisSerialNumber_Type = String
_Inventory_chassisSerialNumber_Object = MibScalar
inventory_chassisSerialNumber = _Inventory_chassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 5),
    _Inventory_chassisSerialNumber_Type()
)
inventory_chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_chassisSerialNumber.setStatus("current")
_Inventory_chassisManufactureDate_Type = DateAndTime
_Inventory_chassisManufactureDate_Object = MibScalar
inventory_chassisManufactureDate = _Inventory_chassisManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 6),
    _Inventory_chassisManufactureDate_Type()
)
inventory_chassisManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_chassisManufactureDate.setStatus("current")
_Inventory_chassisVendor_Type = String
_Inventory_chassisVendor_Object = MibScalar
inventory_chassisVendor = _Inventory_chassisVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 7),
    _Inventory_chassisVendor_Type()
)
inventory_chassisVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_chassisVendor.setStatus("current")
_Inventory_fanTable_Object = MibTable
inventory_fanTable = _Inventory_fanTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2)
)
if mibBuilder.loadTexts:
    inventory_fanTable.setStatus("current")
_Inventory_fanEntry_Object = MibTableRow
inventory_fanEntry = _Inventory_fanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1)
)
inventory_fanEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-fanChassisNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-fanSlotNum"),
)
if mibBuilder.loadTexts:
    inventory_fanEntry.setStatus("current")
_Inventory_fanChassisNum_Type = ChassisIndexT
_Inventory_fanChassisNum_Object = MibScalar
inventory_fanChassisNum = _Inventory_fanChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 1),
    _Inventory_fanChassisNum_Type()
)
inventory_fanChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_fanChassisNum.setStatus("current")
_Inventory_fanSlotNum_Type = FanIndexT
_Inventory_fanSlotNum_Object = MibScalar
inventory_fanSlotNum = _Inventory_fanSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 2),
    _Inventory_fanSlotNum_Type()
)
inventory_fanSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_fanSlotNum.setStatus("current")
_Inventory_fanName_Type = String
_Inventory_fanName_Object = MibScalar
inventory_fanName = _Inventory_fanName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 3),
    _Inventory_fanName_Type()
)
inventory_fanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_fanName.setStatus("current")
_Inventory_fanPEC_Type = String
_Inventory_fanPEC_Object = MibScalar
inventory_fanPEC = _Inventory_fanPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 4),
    _Inventory_fanPEC_Type()
)
inventory_fanPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_fanPEC.setStatus("current")
_Inventory_fanRevision_Type = UnsignedShort
_Inventory_fanRevision_Object = MibScalar
inventory_fanRevision = _Inventory_fanRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 5),
    _Inventory_fanRevision_Type()
)
inventory_fanRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_fanRevision.setStatus("current")
_Inventory_fanSerialNumber_Type = String
_Inventory_fanSerialNumber_Object = MibScalar
inventory_fanSerialNumber = _Inventory_fanSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 6),
    _Inventory_fanSerialNumber_Type()
)
inventory_fanSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_fanSerialNumber.setStatus("current")
_Inventory_fanManufactureDate_Type = DateAndTime
_Inventory_fanManufactureDate_Object = MibScalar
inventory_fanManufactureDate = _Inventory_fanManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 7),
    _Inventory_fanManufactureDate_Type()
)
inventory_fanManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_fanManufactureDate.setStatus("current")
_Inventory_fanVendor_Type = String
_Inventory_fanVendor_Object = MibScalar
inventory_fanVendor = _Inventory_fanVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 8),
    _Inventory_fanVendor_Type()
)
inventory_fanVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_fanVendor.setStatus("current")
_Inventory_pemTable_Object = MibTable
inventory_pemTable = _Inventory_pemTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3)
)
if mibBuilder.loadTexts:
    inventory_pemTable.setStatus("current")
_Inventory_pemEntry_Object = MibTableRow
inventory_pemEntry = _Inventory_pemEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1)
)
inventory_pemEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-pemChassisNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-pemSlotNum"),
)
if mibBuilder.loadTexts:
    inventory_pemEntry.setStatus("current")
_Inventory_pemChassisNum_Type = ChassisIndexT
_Inventory_pemChassisNum_Object = MibScalar
inventory_pemChassisNum = _Inventory_pemChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 1),
    _Inventory_pemChassisNum_Type()
)
inventory_pemChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_pemChassisNum.setStatus("current")
_Inventory_pemSlotNum_Type = PemIndexT
_Inventory_pemSlotNum_Object = MibScalar
inventory_pemSlotNum = _Inventory_pemSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 2),
    _Inventory_pemSlotNum_Type()
)
inventory_pemSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_pemSlotNum.setStatus("current")
_Inventory_pemName_Type = String
_Inventory_pemName_Object = MibScalar
inventory_pemName = _Inventory_pemName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 3),
    _Inventory_pemName_Type()
)
inventory_pemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_pemName.setStatus("current")
_Inventory_pemPEC_Type = String
_Inventory_pemPEC_Object = MibScalar
inventory_pemPEC = _Inventory_pemPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 4),
    _Inventory_pemPEC_Type()
)
inventory_pemPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_pemPEC.setStatus("current")
_Inventory_pemRevision_Type = UnsignedShort
_Inventory_pemRevision_Object = MibScalar
inventory_pemRevision = _Inventory_pemRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 5),
    _Inventory_pemRevision_Type()
)
inventory_pemRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_pemRevision.setStatus("current")
_Inventory_pemSerialNumber_Type = String
_Inventory_pemSerialNumber_Object = MibScalar
inventory_pemSerialNumber = _Inventory_pemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 6),
    _Inventory_pemSerialNumber_Type()
)
inventory_pemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_pemSerialNumber.setStatus("current")
_Inventory_pemManufactureDate_Type = DateAndTime
_Inventory_pemManufactureDate_Object = MibScalar
inventory_pemManufactureDate = _Inventory_pemManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 7),
    _Inventory_pemManufactureDate_Type()
)
inventory_pemManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_pemManufactureDate.setStatus("current")
_Inventory_pemVendor_Type = String
_Inventory_pemVendor_Object = MibScalar
inventory_pemVendor = _Inventory_pemVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 8),
    _Inventory_pemVendor_Type()
)
inventory_pemVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_pemVendor.setStatus("current")
_Inventory_cmmTable_Object = MibTable
inventory_cmmTable = _Inventory_cmmTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4)
)
if mibBuilder.loadTexts:
    inventory_cmmTable.setStatus("current")
_Inventory_cmmEntry_Object = MibTableRow
inventory_cmmEntry = _Inventory_cmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1)
)
inventory_cmmEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-cmmChassisNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-cmmSlotNum"),
)
if mibBuilder.loadTexts:
    inventory_cmmEntry.setStatus("current")
_Inventory_cmmChassisNum_Type = ChassisIndexT
_Inventory_cmmChassisNum_Object = MibScalar
inventory_cmmChassisNum = _Inventory_cmmChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 1),
    _Inventory_cmmChassisNum_Type()
)
inventory_cmmChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_cmmChassisNum.setStatus("current")
_Inventory_cmmSlotNum_Type = CmmIndexT
_Inventory_cmmSlotNum_Object = MibScalar
inventory_cmmSlotNum = _Inventory_cmmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 2),
    _Inventory_cmmSlotNum_Type()
)
inventory_cmmSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_cmmSlotNum.setStatus("current")
_Inventory_cmmName_Type = String
_Inventory_cmmName_Object = MibScalar
inventory_cmmName = _Inventory_cmmName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 3),
    _Inventory_cmmName_Type()
)
inventory_cmmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_cmmName.setStatus("current")
_Inventory_cmmPEC_Type = String
_Inventory_cmmPEC_Object = MibScalar
inventory_cmmPEC = _Inventory_cmmPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 4),
    _Inventory_cmmPEC_Type()
)
inventory_cmmPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_cmmPEC.setStatus("current")
_Inventory_cmmRevision_Type = UnsignedShort
_Inventory_cmmRevision_Object = MibScalar
inventory_cmmRevision = _Inventory_cmmRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 5),
    _Inventory_cmmRevision_Type()
)
inventory_cmmRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_cmmRevision.setStatus("current")
_Inventory_cmmSerialNumber_Type = String
_Inventory_cmmSerialNumber_Object = MibScalar
inventory_cmmSerialNumber = _Inventory_cmmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 6),
    _Inventory_cmmSerialNumber_Type()
)
inventory_cmmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_cmmSerialNumber.setStatus("current")
_Inventory_cmmManufactureDate_Type = DateAndTime
_Inventory_cmmManufactureDate_Object = MibScalar
inventory_cmmManufactureDate = _Inventory_cmmManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 7),
    _Inventory_cmmManufactureDate_Type()
)
inventory_cmmManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_cmmManufactureDate.setStatus("current")
_Inventory_cmmVendor_Type = String
_Inventory_cmmVendor_Object = MibScalar
inventory_cmmVendor = _Inventory_cmmVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 8),
    _Inventory_cmmVendor_Type()
)
inventory_cmmVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_cmmVendor.setStatus("current")
_Inventory_moduleTable_Object = MibTable
inventory_moduleTable = _Inventory_moduleTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5)
)
if mibBuilder.loadTexts:
    inventory_moduleTable.setStatus("current")
_Inventory_moduleEntry_Object = MibTableRow
inventory_moduleEntry = _Inventory_moduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1)
)
inventory_moduleEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-moduleChassisNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-moduleSlotNum"),
)
if mibBuilder.loadTexts:
    inventory_moduleEntry.setStatus("current")
_Inventory_moduleChassisNum_Type = ChassisIndexT
_Inventory_moduleChassisNum_Object = MibScalar
inventory_moduleChassisNum = _Inventory_moduleChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 1),
    _Inventory_moduleChassisNum_Type()
)
inventory_moduleChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_moduleChassisNum.setStatus("current")
_Inventory_moduleSlotNum_Type = ModuleIndexT
_Inventory_moduleSlotNum_Object = MibScalar
inventory_moduleSlotNum = _Inventory_moduleSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 2),
    _Inventory_moduleSlotNum_Type()
)
inventory_moduleSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_moduleSlotNum.setStatus("current")
_Inventory_moduleName_Type = String
_Inventory_moduleName_Object = MibScalar
inventory_moduleName = _Inventory_moduleName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 3),
    _Inventory_moduleName_Type()
)
inventory_moduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_moduleName.setStatus("current")
_Inventory_modulePEC_Type = String
_Inventory_modulePEC_Object = MibScalar
inventory_modulePEC = _Inventory_modulePEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 4),
    _Inventory_modulePEC_Type()
)
inventory_modulePEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_modulePEC.setStatus("current")
_Inventory_moduleRevision_Type = UnsignedShort
_Inventory_moduleRevision_Object = MibScalar
inventory_moduleRevision = _Inventory_moduleRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 5),
    _Inventory_moduleRevision_Type()
)
inventory_moduleRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_moduleRevision.setStatus("current")
_Inventory_moduleSerialNumber_Type = String
_Inventory_moduleSerialNumber_Object = MibScalar
inventory_moduleSerialNumber = _Inventory_moduleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 6),
    _Inventory_moduleSerialNumber_Type()
)
inventory_moduleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_moduleSerialNumber.setStatus("current")
_Inventory_moduleManufactureDate_Type = DateAndTime
_Inventory_moduleManufactureDate_Object = MibScalar
inventory_moduleManufactureDate = _Inventory_moduleManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 7),
    _Inventory_moduleManufactureDate_Type()
)
inventory_moduleManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_moduleManufactureDate.setStatus("current")
_Inventory_moduleVendor_Type = String
_Inventory_moduleVendor_Object = MibScalar
inventory_moduleVendor = _Inventory_moduleVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 8),
    _Inventory_moduleVendor_Type()
)
inventory_moduleVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_moduleVendor.setStatus("current")
_Inventory_bicTable_Object = MibTable
inventory_bicTable = _Inventory_bicTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6)
)
if mibBuilder.loadTexts:
    inventory_bicTable.setStatus("current")
_Inventory_bicEntry_Object = MibTableRow
inventory_bicEntry = _Inventory_bicEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1)
)
inventory_bicEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-bicChassisNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-bicSlotNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-bicSubslotNum"),
)
if mibBuilder.loadTexts:
    inventory_bicEntry.setStatus("current")
_Inventory_bicChassisNum_Type = ChassisIndexT
_Inventory_bicChassisNum_Object = MibScalar
inventory_bicChassisNum = _Inventory_bicChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 1),
    _Inventory_bicChassisNum_Type()
)
inventory_bicChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_bicChassisNum.setStatus("current")
_Inventory_bicSlotNum_Type = ModuleIndexT
_Inventory_bicSlotNum_Object = MibScalar
inventory_bicSlotNum = _Inventory_bicSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 2),
    _Inventory_bicSlotNum_Type()
)
inventory_bicSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_bicSlotNum.setStatus("current")
_Inventory_bicSubslotNum_Type = BicIndexT
_Inventory_bicSubslotNum_Object = MibScalar
inventory_bicSubslotNum = _Inventory_bicSubslotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 3),
    _Inventory_bicSubslotNum_Type()
)
inventory_bicSubslotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_bicSubslotNum.setStatus("current")
_Inventory_bicName_Type = String
_Inventory_bicName_Object = MibScalar
inventory_bicName = _Inventory_bicName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 4),
    _Inventory_bicName_Type()
)
inventory_bicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_bicName.setStatus("current")
_Inventory_bicPEC_Type = String
_Inventory_bicPEC_Object = MibScalar
inventory_bicPEC = _Inventory_bicPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 5),
    _Inventory_bicPEC_Type()
)
inventory_bicPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_bicPEC.setStatus("current")
_Inventory_bicRevision_Type = UnsignedShort
_Inventory_bicRevision_Object = MibScalar
inventory_bicRevision = _Inventory_bicRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 6),
    _Inventory_bicRevision_Type()
)
inventory_bicRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_bicRevision.setStatus("current")
_Inventory_bicSerialNumber_Type = String
_Inventory_bicSerialNumber_Object = MibScalar
inventory_bicSerialNumber = _Inventory_bicSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 7),
    _Inventory_bicSerialNumber_Type()
)
inventory_bicSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_bicSerialNumber.setStatus("current")
_Inventory_bicManufactureDate_Type = DateAndTime
_Inventory_bicManufactureDate_Object = MibScalar
inventory_bicManufactureDate = _Inventory_bicManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 8),
    _Inventory_bicManufactureDate_Type()
)
inventory_bicManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_bicManufactureDate.setStatus("current")
_Inventory_bicVendor_Type = String
_Inventory_bicVendor_Object = MibScalar
inventory_bicVendor = _Inventory_bicVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 9),
    _Inventory_bicVendor_Type()
)
inventory_bicVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_bicVendor.setStatus("current")
_Inventory_xcvrTable_Object = MibTable
inventory_xcvrTable = _Inventory_xcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7)
)
if mibBuilder.loadTexts:
    inventory_xcvrTable.setStatus("current")
_Inventory_xcvrEntry_Object = MibTableRow
inventory_xcvrEntry = _Inventory_xcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1)
)
inventory_xcvrEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-xcvrChassisNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-xcvrSlotNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-xcvrSubslotNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-xcvrPortNum"),
)
if mibBuilder.loadTexts:
    inventory_xcvrEntry.setStatus("current")
_Inventory_xcvrChassisNum_Type = ChassisIndexT
_Inventory_xcvrChassisNum_Object = MibScalar
inventory_xcvrChassisNum = _Inventory_xcvrChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 1),
    _Inventory_xcvrChassisNum_Type()
)
inventory_xcvrChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_xcvrChassisNum.setStatus("current")
_Inventory_xcvrSlotNum_Type = ModuleIndexT
_Inventory_xcvrSlotNum_Object = MibScalar
inventory_xcvrSlotNum = _Inventory_xcvrSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 2),
    _Inventory_xcvrSlotNum_Type()
)
inventory_xcvrSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_xcvrSlotNum.setStatus("current")
_Inventory_xcvrSubslotNum_Type = BicIndexT
_Inventory_xcvrSubslotNum_Object = MibScalar
inventory_xcvrSubslotNum = _Inventory_xcvrSubslotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 3),
    _Inventory_xcvrSubslotNum_Type()
)
inventory_xcvrSubslotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_xcvrSubslotNum.setStatus("current")
_Inventory_xcvrPortNum_Type = PortIndexT
_Inventory_xcvrPortNum_Object = MibScalar
inventory_xcvrPortNum = _Inventory_xcvrPortNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 4),
    _Inventory_xcvrPortNum_Type()
)
inventory_xcvrPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_xcvrPortNum.setStatus("current")
_Inventory_xcvrName_Type = String
_Inventory_xcvrName_Object = MibScalar
inventory_xcvrName = _Inventory_xcvrName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 5),
    _Inventory_xcvrName_Type()
)
inventory_xcvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_xcvrName.setStatus("current")
_Inventory_xcvrPEC_Type = String
_Inventory_xcvrPEC_Object = MibScalar
inventory_xcvrPEC = _Inventory_xcvrPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 6),
    _Inventory_xcvrPEC_Type()
)
inventory_xcvrPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_xcvrPEC.setStatus("current")
_Inventory_xcvrRevision_Type = UnsignedShort
_Inventory_xcvrRevision_Object = MibScalar
inventory_xcvrRevision = _Inventory_xcvrRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 7),
    _Inventory_xcvrRevision_Type()
)
inventory_xcvrRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_xcvrRevision.setStatus("current")
_Inventory_xcvrSerialNumber_Type = String
_Inventory_xcvrSerialNumber_Object = MibScalar
inventory_xcvrSerialNumber = _Inventory_xcvrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 8),
    _Inventory_xcvrSerialNumber_Type()
)
inventory_xcvrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_xcvrSerialNumber.setStatus("current")
_Inventory_xcvrManufactureDate_Type = DateAndTime
_Inventory_xcvrManufactureDate_Object = MibScalar
inventory_xcvrManufactureDate = _Inventory_xcvrManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 9),
    _Inventory_xcvrManufactureDate_Type()
)
inventory_xcvrManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_xcvrManufactureDate.setStatus("current")
_Inventory_xcvrVendor_Type = String
_Inventory_xcvrVendor_Object = MibScalar
inventory_xcvrVendor = _Inventory_xcvrVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 10),
    _Inventory_xcvrVendor_Type()
)
inventory_xcvrVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_xcvrVendor.setStatus("current")
_Inventory_xcvrVendorPartNum_Type = String
_Inventory_xcvrVendorPartNum_Object = MibScalar
inventory_xcvrVendorPartNum = _Inventory_xcvrVendorPartNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 11),
    _Inventory_xcvrVendorPartNum_Type()
)
inventory_xcvrVendorPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_xcvrVendorPartNum.setStatus("current")


class _Inventory_xcvrType_Type(Integer32):
    """Custom type inventory_xcvrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cfp", 3),
          ("msa", 4),
          ("msa400", 7),
          ("qsfp", 5),
          ("qsfp28", 6),
          ("sfp", 1),
          ("sfpPlus", 2),
          ("unknown", 0))
    )


_Inventory_xcvrType_Type.__name__ = "Integer32"
_Inventory_xcvrType_Object = MibScalar
inventory_xcvrType = _Inventory_xcvrType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 12),
    _Inventory_xcvrType_Type()
)
inventory_xcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_xcvrType.setStatus("current")
_Inventory_preampTable_Object = MibTable
inventory_preampTable = _Inventory_preampTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8)
)
if mibBuilder.loadTexts:
    inventory_preampTable.setStatus("current")
_Inventory_preampEntry_Object = MibTableRow
inventory_preampEntry = _Inventory_preampEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1)
)
inventory_preampEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-preampChassisNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-preampSlotNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-preampSubslotNum"),
)
if mibBuilder.loadTexts:
    inventory_preampEntry.setStatus("current")
_Inventory_preampChassisNum_Type = ChassisIndexT
_Inventory_preampChassisNum_Object = MibScalar
inventory_preampChassisNum = _Inventory_preampChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 1),
    _Inventory_preampChassisNum_Type()
)
inventory_preampChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_preampChassisNum.setStatus("current")
_Inventory_preampSlotNum_Type = ModuleIndexT
_Inventory_preampSlotNum_Object = MibScalar
inventory_preampSlotNum = _Inventory_preampSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 2),
    _Inventory_preampSlotNum_Type()
)
inventory_preampSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_preampSlotNum.setStatus("current")
_Inventory_preampSubslotNum_Type = BicIndexT
_Inventory_preampSubslotNum_Object = MibScalar
inventory_preampSubslotNum = _Inventory_preampSubslotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 3),
    _Inventory_preampSubslotNum_Type()
)
inventory_preampSubslotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_preampSubslotNum.setStatus("current")
_Inventory_preampName_Type = String
_Inventory_preampName_Object = MibScalar
inventory_preampName = _Inventory_preampName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 4),
    _Inventory_preampName_Type()
)
inventory_preampName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_preampName.setStatus("current")
_Inventory_preampPEC_Type = String
_Inventory_preampPEC_Object = MibScalar
inventory_preampPEC = _Inventory_preampPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 5),
    _Inventory_preampPEC_Type()
)
inventory_preampPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_preampPEC.setStatus("current")
_Inventory_preampRevision_Type = UnsignedShort
_Inventory_preampRevision_Object = MibScalar
inventory_preampRevision = _Inventory_preampRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 6),
    _Inventory_preampRevision_Type()
)
inventory_preampRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_preampRevision.setStatus("current")
_Inventory_preampSerialNumber_Type = String
_Inventory_preampSerialNumber_Object = MibScalar
inventory_preampSerialNumber = _Inventory_preampSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 7),
    _Inventory_preampSerialNumber_Type()
)
inventory_preampSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_preampSerialNumber.setStatus("current")
_Inventory_preampManufactureDate_Type = DateAndTime
_Inventory_preampManufactureDate_Object = MibScalar
inventory_preampManufactureDate = _Inventory_preampManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 8),
    _Inventory_preampManufactureDate_Type()
)
inventory_preampManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_preampManufactureDate.setStatus("current")
_Inventory_preampVendor_Type = String
_Inventory_preampVendor_Object = MibScalar
inventory_preampVendor = _Inventory_preampVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 9),
    _Inventory_preampVendor_Type()
)
inventory_preampVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_preampVendor.setStatus("current")
_Inventory_eslTable_Object = MibTable
inventory_eslTable = _Inventory_eslTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9)
)
if mibBuilder.loadTexts:
    inventory_eslTable.setStatus("current")
_Inventory_eslEntry_Object = MibTableRow
inventory_eslEntry = _Inventory_eslEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1)
)
inventory_eslEntry.setIndexNames(
    (0, "BTI7800-INVENTORY-MIB", "inventory-eslChassisNum"),
    (0, "BTI7800-INVENTORY-MIB", "inventory-eslSlotNum"),
)
if mibBuilder.loadTexts:
    inventory_eslEntry.setStatus("current")
_Inventory_eslChassisNum_Type = ChassisIndexT
_Inventory_eslChassisNum_Object = MibScalar
inventory_eslChassisNum = _Inventory_eslChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 1),
    _Inventory_eslChassisNum_Type()
)
inventory_eslChassisNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_eslChassisNum.setStatus("current")
_Inventory_eslSlotNum_Type = UnsignedByte
_Inventory_eslSlotNum_Object = MibScalar
inventory_eslSlotNum = _Inventory_eslSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 2),
    _Inventory_eslSlotNum_Type()
)
inventory_eslSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventory_eslSlotNum.setStatus("current")
_Inventory_eslName_Type = String
_Inventory_eslName_Object = MibScalar
inventory_eslName = _Inventory_eslName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 3),
    _Inventory_eslName_Type()
)
inventory_eslName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_eslName.setStatus("current")
_Inventory_eslPEC_Type = String
_Inventory_eslPEC_Object = MibScalar
inventory_eslPEC = _Inventory_eslPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 4),
    _Inventory_eslPEC_Type()
)
inventory_eslPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_eslPEC.setStatus("current")
_Inventory_eslRevision_Type = UnsignedShort
_Inventory_eslRevision_Object = MibScalar
inventory_eslRevision = _Inventory_eslRevision_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 5),
    _Inventory_eslRevision_Type()
)
inventory_eslRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_eslRevision.setStatus("current")
_Inventory_eslSerialNumber_Type = String
_Inventory_eslSerialNumber_Object = MibScalar
inventory_eslSerialNumber = _Inventory_eslSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 6),
    _Inventory_eslSerialNumber_Type()
)
inventory_eslSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_eslSerialNumber.setStatus("current")
_Inventory_eslManufactureDate_Type = DateAndTime
_Inventory_eslManufactureDate_Object = MibScalar
inventory_eslManufactureDate = _Inventory_eslManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 7),
    _Inventory_eslManufactureDate_Type()
)
inventory_eslManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_eslManufactureDate.setStatus("current")
_Inventory_eslVendor_Type = String
_Inventory_eslVendor_Object = MibScalar
inventory_eslVendor = _Inventory_eslVendor_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 8),
    _Inventory_eslVendor_Type()
)
inventory_eslVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventory_eslVendor.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI7800-INVENTORY-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "BicIndexT": BicIndexT,
       "FanIndexT": FanIndexT,
       "PemIndexT": PemIndexT,
       "CmmIndexT": CmmIndexT,
       "PortIndexT": PortIndexT,
       "ModuleIndexT": ModuleIndexT,
       "ChassisIndexT": ChassisIndexT,
       "bTI7800-INVENTORY-MIB": bTI7800_INVENTORY_MIB,
       "inventory-chassisTable": inventory_chassisTable,
       "inventory-chassisEntry": inventory_chassisEntry,
       "inventory-chassisChassisNum": inventory_chassisChassisNum,
       "inventory-chassisName": inventory_chassisName,
       "inventory-chassisPEC": inventory_chassisPEC,
       "inventory-chassisRevision": inventory_chassisRevision,
       "inventory-chassisSerialNumber": inventory_chassisSerialNumber,
       "inventory-chassisManufactureDate": inventory_chassisManufactureDate,
       "inventory-chassisVendor": inventory_chassisVendor,
       "inventory-fanTable": inventory_fanTable,
       "inventory-fanEntry": inventory_fanEntry,
       "inventory-fanChassisNum": inventory_fanChassisNum,
       "inventory-fanSlotNum": inventory_fanSlotNum,
       "inventory-fanName": inventory_fanName,
       "inventory-fanPEC": inventory_fanPEC,
       "inventory-fanRevision": inventory_fanRevision,
       "inventory-fanSerialNumber": inventory_fanSerialNumber,
       "inventory-fanManufactureDate": inventory_fanManufactureDate,
       "inventory-fanVendor": inventory_fanVendor,
       "inventory-pemTable": inventory_pemTable,
       "inventory-pemEntry": inventory_pemEntry,
       "inventory-pemChassisNum": inventory_pemChassisNum,
       "inventory-pemSlotNum": inventory_pemSlotNum,
       "inventory-pemName": inventory_pemName,
       "inventory-pemPEC": inventory_pemPEC,
       "inventory-pemRevision": inventory_pemRevision,
       "inventory-pemSerialNumber": inventory_pemSerialNumber,
       "inventory-pemManufactureDate": inventory_pemManufactureDate,
       "inventory-pemVendor": inventory_pemVendor,
       "inventory-cmmTable": inventory_cmmTable,
       "inventory-cmmEntry": inventory_cmmEntry,
       "inventory-cmmChassisNum": inventory_cmmChassisNum,
       "inventory-cmmSlotNum": inventory_cmmSlotNum,
       "inventory-cmmName": inventory_cmmName,
       "inventory-cmmPEC": inventory_cmmPEC,
       "inventory-cmmRevision": inventory_cmmRevision,
       "inventory-cmmSerialNumber": inventory_cmmSerialNumber,
       "inventory-cmmManufactureDate": inventory_cmmManufactureDate,
       "inventory-cmmVendor": inventory_cmmVendor,
       "inventory-moduleTable": inventory_moduleTable,
       "inventory-moduleEntry": inventory_moduleEntry,
       "inventory-moduleChassisNum": inventory_moduleChassisNum,
       "inventory-moduleSlotNum": inventory_moduleSlotNum,
       "inventory-moduleName": inventory_moduleName,
       "inventory-modulePEC": inventory_modulePEC,
       "inventory-moduleRevision": inventory_moduleRevision,
       "inventory-moduleSerialNumber": inventory_moduleSerialNumber,
       "inventory-moduleManufactureDate": inventory_moduleManufactureDate,
       "inventory-moduleVendor": inventory_moduleVendor,
       "inventory-bicTable": inventory_bicTable,
       "inventory-bicEntry": inventory_bicEntry,
       "inventory-bicChassisNum": inventory_bicChassisNum,
       "inventory-bicSlotNum": inventory_bicSlotNum,
       "inventory-bicSubslotNum": inventory_bicSubslotNum,
       "inventory-bicName": inventory_bicName,
       "inventory-bicPEC": inventory_bicPEC,
       "inventory-bicRevision": inventory_bicRevision,
       "inventory-bicSerialNumber": inventory_bicSerialNumber,
       "inventory-bicManufactureDate": inventory_bicManufactureDate,
       "inventory-bicVendor": inventory_bicVendor,
       "inventory-xcvrTable": inventory_xcvrTable,
       "inventory-xcvrEntry": inventory_xcvrEntry,
       "inventory-xcvrChassisNum": inventory_xcvrChassisNum,
       "inventory-xcvrSlotNum": inventory_xcvrSlotNum,
       "inventory-xcvrSubslotNum": inventory_xcvrSubslotNum,
       "inventory-xcvrPortNum": inventory_xcvrPortNum,
       "inventory-xcvrName": inventory_xcvrName,
       "inventory-xcvrPEC": inventory_xcvrPEC,
       "inventory-xcvrRevision": inventory_xcvrRevision,
       "inventory-xcvrSerialNumber": inventory_xcvrSerialNumber,
       "inventory-xcvrManufactureDate": inventory_xcvrManufactureDate,
       "inventory-xcvrVendor": inventory_xcvrVendor,
       "inventory-xcvrVendorPartNum": inventory_xcvrVendorPartNum,
       "inventory-xcvrType": inventory_xcvrType,
       "inventory-preampTable": inventory_preampTable,
       "inventory-preampEntry": inventory_preampEntry,
       "inventory-preampChassisNum": inventory_preampChassisNum,
       "inventory-preampSlotNum": inventory_preampSlotNum,
       "inventory-preampSubslotNum": inventory_preampSubslotNum,
       "inventory-preampName": inventory_preampName,
       "inventory-preampPEC": inventory_preampPEC,
       "inventory-preampRevision": inventory_preampRevision,
       "inventory-preampSerialNumber": inventory_preampSerialNumber,
       "inventory-preampManufactureDate": inventory_preampManufactureDate,
       "inventory-preampVendor": inventory_preampVendor,
       "inventory-eslTable": inventory_eslTable,
       "inventory-eslEntry": inventory_eslEntry,
       "inventory-eslChassisNum": inventory_eslChassisNum,
       "inventory-eslSlotNum": inventory_eslSlotNum,
       "inventory-eslName": inventory_eslName,
       "inventory-eslPEC": inventory_eslPEC,
       "inventory-eslRevision": inventory_eslRevision,
       "inventory-eslSerialNumber": inventory_eslSerialNumber,
       "inventory-eslManufactureDate": inventory_eslManufactureDate,
       "inventory-eslVendor": inventory_eslVendor}
)
