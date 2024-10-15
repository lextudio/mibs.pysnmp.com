# SNMP MIB module (HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:59 2024
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

(fibrechannel,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "fibrechannel")

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

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

(swID,
 swSsn) = mibBuilder.importSymbols(
    "SW-MIB",
    "swID",
    "swSsn")


# MODULE-IDENTITY

haMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2)
)
haMIB.setRevisions(
        ("2002-08-16 00:00",
         "2004-02-25 15:30",
         "2009-02-09 00:00",
         "2009-04-06 00:00",
         "2009-06-25 12:00",
         "2010-07-22 10:00",
         "2012-09-25 10:00",
         "2013-05-07 17:57")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FruClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("applicationblade", 11),
          ("chassis", 3),
          ("coreblade", 10),
          ("cp", 4),
          ("fan", 9),
          ("other", 1),
          ("other-CP", 5),
          ("powerSupply", 8),
          ("switchblade", 6),
          ("unknown", 2),
          ("wwn", 7))
    )



# MIB Managed Objects in the order of their OIDs

_HighAvailability_ObjectIdentity = ObjectIdentity
highAvailability = _HighAvailability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1)
)


class _HaStatus_Type(Integer32):
    """Custom type haStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonredundant", 1),
          ("redundant", 0))
    )


_HaStatus_Type.__name__ = "Integer32"
_HaStatus_Object = MibScalar
haStatus = _HaStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 1),
    _HaStatus_Type()
)
haStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStatus.setStatus("current")
_FruTable_Object = MibTable
fruTable = _FruTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    fruTable.setStatus("current")
_FRUEntry_Object = MibTableRow
fRUEntry = _FRUEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1)
)
fRUEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fRUEntry.setStatus("current")
_FruClass_Type = FruClass
_FruClass_Object = MibTableColumn
fruClass = _FruClass_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 1),
    _FruClass_Type()
)
fruClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruClass.setStatus("current")


class _FruStatus_Type(Integer32):
    """Custom type fruStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 5),
          ("initialized", 7),
          ("off", 4),
          ("on", 3),
          ("other", 1),
          ("poweredon", 6),
          ("unknown", 2))
    )


_FruStatus_Type.__name__ = "Integer32"
_FruStatus_Object = MibTableColumn
fruStatus = _FruStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 2),
    _FruStatus_Type()
)
fruStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruStatus.setStatus("current")
_FruObjectNum_Type = Integer32
_FruObjectNum_Object = MibTableColumn
fruObjectNum = _FruObjectNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 3),
    _FruObjectNum_Type()
)
fruObjectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruObjectNum.setStatus("current")
_FruSupplierId_Type = DisplayString
_FruSupplierId_Object = MibTableColumn
fruSupplierId = _FruSupplierId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 4),
    _FruSupplierId_Type()
)
fruSupplierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruSupplierId.setStatus("current")
_FruSupplierPartNum_Type = DisplayString
_FruSupplierPartNum_Object = MibTableColumn
fruSupplierPartNum = _FruSupplierPartNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 5),
    _FruSupplierPartNum_Type()
)
fruSupplierPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruSupplierPartNum.setStatus("current")


class _FruSupplierSerialNum_Type(DisplayString):
    """Custom type fruSupplierSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FruSupplierSerialNum_Type.__name__ = "DisplayString"
_FruSupplierSerialNum_Object = MibTableColumn
fruSupplierSerialNum = _FruSupplierSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 6),
    _FruSupplierSerialNum_Type()
)
fruSupplierSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruSupplierSerialNum.setStatus("current")
_FruSupplierRevCode_Type = DisplayString
_FruSupplierRevCode_Object = MibTableColumn
fruSupplierRevCode = _FruSupplierRevCode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 7),
    _FruSupplierRevCode_Type()
)
fruSupplierRevCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruSupplierRevCode.setStatus("current")
_FruPowerConsumption_Type = DisplayString
_FruPowerConsumption_Object = MibTableColumn
fruPowerConsumption = _FruPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 8),
    _FruPowerConsumption_Type()
)
fruPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerConsumption.setStatus("current")
if mibBuilder.loadTexts:
    fruPowerConsumption.setUnits("watt")
_FruHistoryTable_Object = MibTable
fruHistoryTable = _FruHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    fruHistoryTable.setStatus("current")
_FruHistoryEntry_Object = MibTableRow
fruHistoryEntry = _FruHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1)
)
fruHistoryEntry.setIndexNames(
    (0, "HA-MIB", "fruHistoryIndex"),
)
if mibBuilder.loadTexts:
    fruHistoryEntry.setStatus("current")
_FruHistoryIndex_Type = Integer32
_FruHistoryIndex_Object = MibTableColumn
fruHistoryIndex = _FruHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 1),
    _FruHistoryIndex_Type()
)
fruHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruHistoryIndex.setStatus("current")
_FruHistoryClass_Type = FruClass
_FruHistoryClass_Object = MibTableColumn
fruHistoryClass = _FruHistoryClass_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 2),
    _FruHistoryClass_Type()
)
fruHistoryClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruHistoryClass.setStatus("current")
_FruHistoryObjectNum_Type = Integer32
_FruHistoryObjectNum_Object = MibTableColumn
fruHistoryObjectNum = _FruHistoryObjectNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 3),
    _FruHistoryObjectNum_Type()
)
fruHistoryObjectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruHistoryObjectNum.setStatus("current")


class _FruHistoryEvent_Type(Integer32):
    """Custom type fruHistoryEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("added", 1),
          ("invalid", 3),
          ("removed", 2))
    )


_FruHistoryEvent_Type.__name__ = "Integer32"
_FruHistoryEvent_Object = MibTableColumn
fruHistoryEvent = _FruHistoryEvent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 4),
    _FruHistoryEvent_Type()
)
fruHistoryEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruHistoryEvent.setStatus("current")
_FruHistoryTime_Type = DisplayString
_FruHistoryTime_Object = MibTableColumn
fruHistoryTime = _FruHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 5),
    _FruHistoryTime_Type()
)
fruHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruHistoryTime.setStatus("current")
_FruHistoryFactoryPartNum_Type = DisplayString
_FruHistoryFactoryPartNum_Object = MibTableColumn
fruHistoryFactoryPartNum = _FruHistoryFactoryPartNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 6),
    _FruHistoryFactoryPartNum_Type()
)
fruHistoryFactoryPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruHistoryFactoryPartNum.setStatus("current")
_FruHistoryFactorySerialNum_Type = DisplayString
_FruHistoryFactorySerialNum_Object = MibTableColumn
fruHistoryFactorySerialNum = _FruHistoryFactorySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 7),
    _FruHistoryFactorySerialNum_Type()
)
fruHistoryFactorySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruHistoryFactorySerialNum.setStatus("current")
_CpTable_Object = MibTable
cpTable = _CpTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cpTable.setStatus("current")
_CpEntry_Object = MibTableRow
cpEntry = _CpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1)
)
cpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cpEntry.setStatus("current")


class _CpStatus_Type(Integer32):
    """Custom type cpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("failed", 5),
          ("other", 1),
          ("standby", 4),
          ("unknown", 2))
    )


_CpStatus_Type.__name__ = "Integer32"
_CpStatus_Object = MibTableColumn
cpStatus = _CpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 1),
    _CpStatus_Type()
)
cpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpStatus.setStatus("current")
_CpIpAddress_Type = IpAddress
_CpIpAddress_Object = MibTableColumn
cpIpAddress = _CpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 2),
    _CpIpAddress_Type()
)
cpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIpAddress.setStatus("current")
_CpIpMask_Type = IpAddress
_CpIpMask_Object = MibTableColumn
cpIpMask = _CpIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 3),
    _CpIpMask_Type()
)
cpIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIpMask.setStatus("current")
_CpIpGateway_Type = IpAddress
_CpIpGateway_Object = MibTableColumn
cpIpGateway = _CpIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 4),
    _CpIpGateway_Type()
)
cpIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIpGateway.setStatus("current")


class _CpLastEvent_Type(Integer32):
    """Custom type cpLastEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("configChange", 8),
          ("cpActive", 7),
          ("cpFaulty", 5),
          ("cpHealthy", 6),
          ("failOverDone", 10),
          ("failOverStart", 9),
          ("firmwareCommit", 11),
          ("firmwareUpgrade", 12),
          ("haOutSync", 4),
          ("haSync", 3),
          ("other", 1),
          ("unknown", 2))
    )


_CpLastEvent_Type.__name__ = "Integer32"
_CpLastEvent_Object = MibTableColumn
cpLastEvent = _CpLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 5),
    _CpLastEvent_Type()
)
cpLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpLastEvent.setStatus("current")
_BpTable_Object = MibTable
bpTable = _BpTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    bpTable.setStatus("current")
_BpEntry_Object = MibTableRow
bpEntry = _BpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1)
)
bpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    bpEntry.setStatus("current")


class _BpStatus_Type(Integer32):
    """Custom type bpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 3),
          ("off", 2),
          ("on", 1),
          ("others", 5),
          ("unknow", 4))
    )


_BpStatus_Type.__name__ = "Integer32"
_BpStatus_Object = MibTableColumn
bpStatus = _BpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 1),
    _BpStatus_Type()
)
bpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatus.setStatus("current")
_Bpeth0IpAddress_Type = IpAddress
_Bpeth0IpAddress_Object = MibTableColumn
bpeth0IpAddress = _Bpeth0IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 2),
    _Bpeth0IpAddress_Type()
)
bpeth0IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpeth0IpAddress.setStatus("current")
_Bpeth1IpAddress_Type = IpAddress
_Bpeth1IpAddress_Object = MibTableColumn
bpeth1IpAddress = _Bpeth1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 3),
    _Bpeth1IpAddress_Type()
)
bpeth1IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpeth1IpAddress.setStatus("current")
_BpsubNetMaskIpaddress_Type = IpAddress
_BpsubNetMaskIpaddress_Object = MibTableColumn
bpsubNetMaskIpaddress = _BpsubNetMaskIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 4),
    _BpsubNetMaskIpaddress_Type()
)
bpsubNetMaskIpaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpsubNetMaskIpaddress.setStatus("current")
_BpIpGateway_Type = IpAddress
_BpIpGateway_Object = MibTableColumn
bpIpGateway = _BpIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 5),
    _BpIpGateway_Type()
)
bpIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIpGateway.setStatus("current")


class _BpSasPriVersion_Type(DisplayString):
    """Custom type bpSasPriVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_BpSasPriVersion_Type.__name__ = "DisplayString"
_BpSasPriVersion_Object = MibTableColumn
bpSasPriVersion = _BpSasPriVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 6),
    _BpSasPriVersion_Type()
)
bpSasPriVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpSasPriVersion.setStatus("current")


class _BpSasSecVersion_Type(DisplayString):
    """Custom type bpSasSecVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_BpSasSecVersion_Type.__name__ = "DisplayString"
_BpSasSecVersion_Object = MibTableColumn
bpSasSecVersion = _BpSasSecVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 7),
    _BpSasSecVersion_Type()
)
bpSasSecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpSasSecVersion.setStatus("current")
_HaMIBTraps_ObjectIdentity = ObjectIdentity
haMIBTraps = _HaMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2)
)
_HaMIBTrapPrefix_ObjectIdentity = ObjectIdentity
haMIBTrapPrefix = _HaMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

fruStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2, 0, 1)
)
fruStatusChanged.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HA-MIB", "fruStatus"),
        ("HA-MIB", "fruClass"),
        ("HA-MIB", "fruObjectNum"))
)
if mibBuilder.loadTexts:
    fruStatusChanged.setStatus(
        "current"
    )

cpStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2, 0, 2)
)
cpStatusChanged.setObjects(
      *(("HA-MIB", "cpStatus"),
        ("HA-MIB", "cpLastEvent"),
        ("SW-MIB", "swID"),
        ("SW-MIB", "swSsn"))
)
if mibBuilder.loadTexts:
    cpStatusChanged.setStatus(
        "current"
    )

fruHistoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2, 0, 3)
)
fruHistoryTrap.setObjects(
      *(("HA-MIB", "fruHistoryClass"),
        ("HA-MIB", "fruHistoryObjectNum"),
        ("HA-MIB", "fruHistoryEvent"),
        ("HA-MIB", "fruHistoryTime"),
        ("HA-MIB", "fruHistoryFactoryPartNum"),
        ("HA-MIB", "fruHistoryFactorySerialNum"))
)
if mibBuilder.loadTexts:
    fruHistoryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HA-MIB",
    **{"FruClass": FruClass,
       "haMIB": haMIB,
       "highAvailability": highAvailability,
       "haStatus": haStatus,
       "fruTable": fruTable,
       "fRUEntry": fRUEntry,
       "fruClass": fruClass,
       "fruStatus": fruStatus,
       "fruObjectNum": fruObjectNum,
       "fruSupplierId": fruSupplierId,
       "fruSupplierPartNum": fruSupplierPartNum,
       "fruSupplierSerialNum": fruSupplierSerialNum,
       "fruSupplierRevCode": fruSupplierRevCode,
       "fruPowerConsumption": fruPowerConsumption,
       "fruHistoryTable": fruHistoryTable,
       "fruHistoryEntry": fruHistoryEntry,
       "fruHistoryIndex": fruHistoryIndex,
       "fruHistoryClass": fruHistoryClass,
       "fruHistoryObjectNum": fruHistoryObjectNum,
       "fruHistoryEvent": fruHistoryEvent,
       "fruHistoryTime": fruHistoryTime,
       "fruHistoryFactoryPartNum": fruHistoryFactoryPartNum,
       "fruHistoryFactorySerialNum": fruHistoryFactorySerialNum,
       "cpTable": cpTable,
       "cpEntry": cpEntry,
       "cpStatus": cpStatus,
       "cpIpAddress": cpIpAddress,
       "cpIpMask": cpIpMask,
       "cpIpGateway": cpIpGateway,
       "cpLastEvent": cpLastEvent,
       "bpTable": bpTable,
       "bpEntry": bpEntry,
       "bpStatus": bpStatus,
       "bpeth0IpAddress": bpeth0IpAddress,
       "bpeth1IpAddress": bpeth1IpAddress,
       "bpsubNetMaskIpaddress": bpsubNetMaskIpaddress,
       "bpIpGateway": bpIpGateway,
       "bpSasPriVersion": bpSasPriVersion,
       "bpSasSecVersion": bpSasSecVersion,
       "haMIBTraps": haMIBTraps,
       "haMIBTrapPrefix": haMIBTrapPrefix,
       "fruStatusChanged": fruStatusChanged,
       "cpStatusChanged": cpStatusChanged,
       "fruHistoryTrap": fruHistoryTrap}
)
