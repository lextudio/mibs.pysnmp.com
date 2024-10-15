# SNMP MIB module (SK-GE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SK-GE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:35 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class SkGeMACAddress(OctetString):
    """Custom type SkGeMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sk_ObjectIdentity = ObjectIdentity
sk = _Sk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179)
)
_SkSystems_ObjectIdentity = ObjectIdentity
skSystems = _SkSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 1)
)
_SkMibs_ObjectIdentity = ObjectIdentity
skMibs = _SkMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2)
)
_SkConcMib_ObjectIdentity = ObjectIdentity
skConcMib = _SkConcMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 3)
)
_SkfddiMib_ObjectIdentity = ObjectIdentity
skfddiMib = _SkfddiMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 4)
)
_SkGeMib_ObjectIdentity = ObjectIdentity
skGeMib = _SkGeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 5)
)
_SkGeGeneral_ObjectIdentity = ObjectIdentity
skGeGeneral = _SkGeGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1)
)
_SkGeMibVersion_Type = DisplayString
_SkGeMibVersion_Object = MibScalar
skGeMibVersion = _SkGeMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 1),
    _SkGeMibVersion_Type()
)
skGeMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeMibVersion.setStatus("mandatory")


class _SkGeAction_Type(Integer32):
    """Custom type skGeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("force-trap", 2),
          ("idle", 1),
          ("save-permanent", 3))
    )


_SkGeAction_Type.__name__ = "Integer32"
_SkGeAction_Object = MibScalar
skGeAction = _SkGeAction_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 2),
    _SkGeAction_Type()
)
skGeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeAction.setStatus("mandatory")
_SkGeNumber_Type = Integer32
_SkGeNumber_Object = MibScalar
skGeNumber = _SkGeNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 3),
    _SkGeNumber_Type()
)
skGeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeNumber.setStatus("mandatory")
_SkGeTable_Object = MibTable
skGeTable = _SkGeTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4)
)
if mibBuilder.loadTexts:
    skGeTable.setStatus("mandatory")
_SkGeEntry_Object = MibTableRow
skGeEntry = _SkGeEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1)
)
skGeEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeIndex"),
)
if mibBuilder.loadTexts:
    skGeEntry.setStatus("mandatory")
_SkGeIndex_Type = Integer32
_SkGeIndex_Object = MibTableColumn
skGeIndex = _SkGeIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 1),
    _SkGeIndex_Type()
)
skGeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeIndex.setStatus("mandatory")
_SkGeIfIndex_Type = Integer32
_SkGeIfIndex_Object = MibTableColumn
skGeIfIndex = _SkGeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 2),
    _SkGeIfIndex_Type()
)
skGeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeIfIndex.setStatus("mandatory")
_SkGePortNumber_Type = Integer32
_SkGePortNumber_Object = MibTableColumn
skGePortNumber = _SkGePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 3),
    _SkGePortNumber_Type()
)
skGePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGePortNumber.setStatus("mandatory")
_SkGeDeviceType_Type = ObjectIdentifier
_SkGeDeviceType_Object = MibTableColumn
skGeDeviceType = _SkGeDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 4),
    _SkGeDeviceType_Type()
)
skGeDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeDeviceType.setStatus("mandatory")
_SkGeDriverDescr_Type = DisplayString
_SkGeDriverDescr_Object = MibTableColumn
skGeDriverDescr = _SkGeDriverDescr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 5),
    _SkGeDriverDescr_Type()
)
skGeDriverDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeDriverDescr.setStatus("mandatory")
_SkGeDriverVersion_Type = DisplayString
_SkGeDriverVersion_Object = MibTableColumn
skGeDriverVersion = _SkGeDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 6),
    _SkGeDriverVersion_Type()
)
skGeDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeDriverVersion.setStatus("mandatory")
_SkGeHwDescr_Type = DisplayString
_SkGeHwDescr_Object = MibTableColumn
skGeHwDescr = _SkGeHwDescr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 7),
    _SkGeHwDescr_Type()
)
skGeHwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeHwDescr.setStatus("mandatory")
_SkGeHwVersion_Type = DisplayString
_SkGeHwVersion_Object = MibTableColumn
skGeHwVersion = _SkGeHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 8),
    _SkGeHwVersion_Type()
)
skGeHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeHwVersion.setStatus("mandatory")
_SkGeChipSet_Type = ObjectIdentifier
_SkGeChipSet_Object = MibTableColumn
skGeChipSet = _SkGeChipSet_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 9),
    _SkGeChipSet_Type()
)
skGeChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChipSet.setStatus("mandatory")


class _SkGeDeviceAction_Type(Integer32):
    """Custom type skGeDeviceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("reset", 2),
          ("reset-counters", 4),
          ("self-test", 3))
    )


_SkGeDeviceAction_Type.__name__ = "Integer32"
_SkGeDeviceAction_Object = MibTableColumn
skGeDeviceAction = _SkGeDeviceAction_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 10),
    _SkGeDeviceAction_Type()
)
skGeDeviceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeDeviceAction.setStatus("mandatory")


class _SkGeTestResult_Type(Integer32):
    """Custom type skGeTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SkGeTestResult_Type.__name__ = "Integer32"
_SkGeTestResult_Object = MibTableColumn
skGeTestResult = _SkGeTestResult_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 11),
    _SkGeTestResult_Type()
)
skGeTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeTestResult.setStatus("mandatory")


class _SkGeBusType_Type(Integer32):
    """Custom type skGeBusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("pci", 1)
    )


_SkGeBusType_Type.__name__ = "Integer32"
_SkGeBusType_Object = MibTableColumn
skGeBusType = _SkGeBusType_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 12),
    _SkGeBusType_Type()
)
skGeBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeBusType.setStatus("mandatory")
_SkGeBusSpeed_Type = Integer32
_SkGeBusSpeed_Object = MibTableColumn
skGeBusSpeed = _SkGeBusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 13),
    _SkGeBusSpeed_Type()
)
skGeBusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeBusSpeed.setStatus("mandatory")
_SkGeBusWidth_Type = Integer32
_SkGeBusWidth_Object = MibTableColumn
skGeBusWidth = _SkGeBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 4, 1, 14),
    _SkGeBusWidth_Type()
)
skGeBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeBusWidth.setStatus("mandatory")
_SkGeChecksumEntriesNumber_Type = Integer32
_SkGeChecksumEntriesNumber_Object = MibScalar
skGeChecksumEntriesNumber = _SkGeChecksumEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 5),
    _SkGeChecksumEntriesNumber_Type()
)
skGeChecksumEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChecksumEntriesNumber.setStatus("mandatory")
_SkGeChecksumTable_Object = MibTable
skGeChecksumTable = _SkGeChecksumTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6)
)
if mibBuilder.loadTexts:
    skGeChecksumTable.setStatus("mandatory")
_SkGeChecksumEntry_Object = MibTableRow
skGeChecksumEntry = _SkGeChecksumEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6, 1)
)
skGeChecksumEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeChecksumGeIndex"),
    (0, "SK-GE-MIB", "skGeChecksumIndex"),
)
if mibBuilder.loadTexts:
    skGeChecksumEntry.setStatus("mandatory")
_SkGeChecksumGeIndex_Type = Integer32
_SkGeChecksumGeIndex_Object = MibTableColumn
skGeChecksumGeIndex = _SkGeChecksumGeIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6, 1, 1),
    _SkGeChecksumGeIndex_Type()
)
skGeChecksumGeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChecksumGeIndex.setStatus("mandatory")


class _SkGeChecksumIndex_Type(Integer32):
    """Custom type skGeChecksumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("tcp", 3),
          ("udp", 2))
    )


_SkGeChecksumIndex_Type.__name__ = "Integer32"
_SkGeChecksumIndex_Object = MibTableColumn
skGeChecksumIndex = _SkGeChecksumIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6, 1, 2),
    _SkGeChecksumIndex_Type()
)
skGeChecksumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChecksumIndex.setStatus("mandatory")
_SkGeChecksumRxOkCts_Type = Counter32
_SkGeChecksumRxOkCts_Object = MibTableColumn
skGeChecksumRxOkCts = _SkGeChecksumRxOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6, 1, 3),
    _SkGeChecksumRxOkCts_Type()
)
skGeChecksumRxOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChecksumRxOkCts.setStatus("mandatory")
_SkGeChecksumRxUnableCts_Type = Counter32
_SkGeChecksumRxUnableCts_Object = MibTableColumn
skGeChecksumRxUnableCts = _SkGeChecksumRxUnableCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6, 1, 4),
    _SkGeChecksumRxUnableCts_Type()
)
skGeChecksumRxUnableCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChecksumRxUnableCts.setStatus("mandatory")
_SkGeChecksumRxErrCts_Type = Counter32
_SkGeChecksumRxErrCts_Object = MibTableColumn
skGeChecksumRxErrCts = _SkGeChecksumRxErrCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6, 1, 5),
    _SkGeChecksumRxErrCts_Type()
)
skGeChecksumRxErrCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChecksumRxErrCts.setStatus("mandatory")
_SkGeChecksumTxOkCts_Type = Counter32
_SkGeChecksumTxOkCts_Object = MibTableColumn
skGeChecksumTxOkCts = _SkGeChecksumTxOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6, 1, 6),
    _SkGeChecksumTxOkCts_Type()
)
skGeChecksumTxOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChecksumTxOkCts.setStatus("mandatory")
_SkGeChecksumTxUnableCts_Type = Counter32
_SkGeChecksumTxUnableCts_Object = MibTableColumn
skGeChecksumTxUnableCts = _SkGeChecksumTxUnableCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 6, 1, 7),
    _SkGeChecksumTxUnableCts_Type()
)
skGeChecksumTxUnableCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeChecksumTxUnableCts.setStatus("mandatory")
_SkGeTrapForceType_Type = OctetString
_SkGeTrapForceType_Object = MibScalar
skGeTrapForceType = _SkGeTrapForceType_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 7),
    _SkGeTrapForceType_Type()
)
skGeTrapForceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeTrapForceType.setStatus("mandatory")
_SkGeTrapDestEntriesNumber_Type = Integer32
_SkGeTrapDestEntriesNumber_Object = MibScalar
skGeTrapDestEntriesNumber = _SkGeTrapDestEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 8),
    _SkGeTrapDestEntriesNumber_Type()
)
skGeTrapDestEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeTrapDestEntriesNumber.setStatus("mandatory")
_SkGeTrapDestTable_Object = MibTable
skGeTrapDestTable = _SkGeTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 9)
)
if mibBuilder.loadTexts:
    skGeTrapDestTable.setStatus("mandatory")
_SkGeTrapDestEntry_Object = MibTableRow
skGeTrapDestEntry = _SkGeTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 9, 1)
)
skGeTrapDestEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeTrapDestIndex"),
)
if mibBuilder.loadTexts:
    skGeTrapDestEntry.setStatus("mandatory")
_SkGeTrapDestIndex_Type = Integer32
_SkGeTrapDestIndex_Object = MibTableColumn
skGeTrapDestIndex = _SkGeTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 9, 1, 1),
    _SkGeTrapDestIndex_Type()
)
skGeTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeTrapDestIndex.setStatus("mandatory")
_SkGeTrapDestAddress_Type = IpAddress
_SkGeTrapDestAddress_Object = MibTableColumn
skGeTrapDestAddress = _SkGeTrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 9, 1, 2),
    _SkGeTrapDestAddress_Type()
)
skGeTrapDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeTrapDestAddress.setStatus("mandatory")
_SkGeTrapFilter_Type = Integer32
_SkGeTrapFilter_Object = MibScalar
skGeTrapFilter = _SkGeTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 10),
    _SkGeTrapFilter_Type()
)
skGeTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeTrapFilter.setStatus("mandatory")
_SkGeSensorEntriesNumber_Type = Integer32
_SkGeSensorEntriesNumber_Object = MibScalar
skGeSensorEntriesNumber = _SkGeSensorEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 13),
    _SkGeSensorEntriesNumber_Type()
)
skGeSensorEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorEntriesNumber.setStatus("mandatory")
_SkGeSensorTable_Object = MibTable
skGeSensorTable = _SkGeSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14)
)
if mibBuilder.loadTexts:
    skGeSensorTable.setStatus("mandatory")
_SkGeSensorEntry_Object = MibTableRow
skGeSensorEntry = _SkGeSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1)
)
skGeSensorEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeSensorGeIndex"),
    (0, "SK-GE-MIB", "skGeSensorIndex"),
)
if mibBuilder.loadTexts:
    skGeSensorEntry.setStatus("mandatory")
_SkGeSensorGeIndex_Type = Integer32
_SkGeSensorGeIndex_Object = MibTableColumn
skGeSensorGeIndex = _SkGeSensorGeIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 1),
    _SkGeSensorGeIndex_Type()
)
skGeSensorGeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorGeIndex.setStatus("mandatory")


class _SkGeSensorIndex_Type(Integer32):
    """Custom type skGeSensorIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("speed-fan", 8),
          ("temperature", 1),
          ("voltage-asic", 4),
          ("voltage-pci", 2),
          ("voltage-pci-io", 3),
          ("voltage-phy-2v5", 6),
          ("voltage-phy-b-pll", 7),
          ("voltage-pma-or-phy-a-pll", 5))
    )


_SkGeSensorIndex_Type.__name__ = "Integer32"
_SkGeSensorIndex_Object = MibTableColumn
skGeSensorIndex = _SkGeSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 2),
    _SkGeSensorIndex_Type()
)
skGeSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorIndex.setStatus("mandatory")
_SkGeSensorDescr_Type = DisplayString
_SkGeSensorDescr_Object = MibTableColumn
skGeSensorDescr = _SkGeSensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 3),
    _SkGeSensorDescr_Type()
)
skGeSensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorDescr.setStatus("mandatory")


class _SkGeSensorType_Type(Integer32):
    """Custom type skGeSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rpm", 3),
          ("temperature", 1),
          ("voltage", 2))
    )


_SkGeSensorType_Type.__name__ = "Integer32"
_SkGeSensorType_Object = MibTableColumn
skGeSensorType = _SkGeSensorType_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 4),
    _SkGeSensorType_Type()
)
skGeSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorType.setStatus("mandatory")
_SkGeSensorValue_Type = Integer32
_SkGeSensorValue_Object = MibTableColumn
skGeSensorValue = _SkGeSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 5),
    _SkGeSensorValue_Type()
)
skGeSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorValue.setStatus("mandatory")
_SkGeSensorWarningThresholdLow_Type = Integer32
_SkGeSensorWarningThresholdLow_Object = MibTableColumn
skGeSensorWarningThresholdLow = _SkGeSensorWarningThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 6),
    _SkGeSensorWarningThresholdLow_Type()
)
skGeSensorWarningThresholdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorWarningThresholdLow.setStatus("mandatory")
_SkGeSensorWarningThresholdHigh_Type = Integer32
_SkGeSensorWarningThresholdHigh_Object = MibTableColumn
skGeSensorWarningThresholdHigh = _SkGeSensorWarningThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 7),
    _SkGeSensorWarningThresholdHigh_Type()
)
skGeSensorWarningThresholdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorWarningThresholdHigh.setStatus("mandatory")
_SkGeSensorErrorThresholdLow_Type = Integer32
_SkGeSensorErrorThresholdLow_Object = MibTableColumn
skGeSensorErrorThresholdLow = _SkGeSensorErrorThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 8),
    _SkGeSensorErrorThresholdLow_Type()
)
skGeSensorErrorThresholdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorErrorThresholdLow.setStatus("mandatory")
_SkGeSensorErrorThresholdHigh_Type = Integer32
_SkGeSensorErrorThresholdHigh_Object = MibTableColumn
skGeSensorErrorThresholdHigh = _SkGeSensorErrorThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 9),
    _SkGeSensorErrorThresholdHigh_Type()
)
skGeSensorErrorThresholdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorErrorThresholdHigh.setStatus("mandatory")


class _SkGeSensorStatus_Type(Integer32):
    """Custom type skGeSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("ok", 1),
          ("warning", 2))
    )


_SkGeSensorStatus_Type.__name__ = "Integer32"
_SkGeSensorStatus_Object = MibTableColumn
skGeSensorStatus = _SkGeSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 10),
    _SkGeSensorStatus_Type()
)
skGeSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorStatus.setStatus("mandatory")
_SkGeSensorWarningCts_Type = Counter32
_SkGeSensorWarningCts_Object = MibTableColumn
skGeSensorWarningCts = _SkGeSensorWarningCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 11),
    _SkGeSensorWarningCts_Type()
)
skGeSensorWarningCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorWarningCts.setStatus("mandatory")
_SkGeSensorErrorCts_Type = Counter32
_SkGeSensorErrorCts_Object = MibTableColumn
skGeSensorErrorCts = _SkGeSensorErrorCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 12),
    _SkGeSensorErrorCts_Type()
)
skGeSensorErrorCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorErrorCts.setStatus("mandatory")
_SkGeSensorWarningTimeStamp_Type = TimeTicks
_SkGeSensorWarningTimeStamp_Object = MibTableColumn
skGeSensorWarningTimeStamp = _SkGeSensorWarningTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 13),
    _SkGeSensorWarningTimeStamp_Type()
)
skGeSensorWarningTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorWarningTimeStamp.setStatus("mandatory")
_SkGeSensorErrorTimeStamp_Type = TimeTicks
_SkGeSensorErrorTimeStamp_Object = MibTableColumn
skGeSensorErrorTimeStamp = _SkGeSensorErrorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 14, 1, 14),
    _SkGeSensorErrorTimeStamp_Type()
)
skGeSensorErrorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeSensorErrorTimeStamp.setStatus("mandatory")
_SkGeStatEntriesNumber_Type = Integer32
_SkGeStatEntriesNumber_Object = MibScalar
skGeStatEntriesNumber = _SkGeStatEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 15),
    _SkGeStatEntriesNumber_Type()
)
skGeStatEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatEntriesNumber.setStatus("mandatory")
_SkGeStatTable_Object = MibTable
skGeStatTable = _SkGeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16)
)
if mibBuilder.loadTexts:
    skGeStatTable.setStatus("mandatory")
_SkGeStatEntry_Object = MibTableRow
skGeStatEntry = _SkGeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1)
)
skGeStatEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeStatGeIndex"),
    (0, "SK-GE-MIB", "skGeStatIndex"),
)
if mibBuilder.loadTexts:
    skGeStatEntry.setStatus("mandatory")
_SkGeStatGeIndex_Type = Integer32
_SkGeStatGeIndex_Object = MibTableColumn
skGeStatGeIndex = _SkGeStatGeIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 1),
    _SkGeStatGeIndex_Type()
)
skGeStatGeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatGeIndex.setStatus("mandatory")
_SkGeStatIndex_Type = Integer32
_SkGeStatIndex_Object = MibTableColumn
skGeStatIndex = _SkGeStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 2),
    _SkGeStatIndex_Type()
)
skGeStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatIndex.setStatus("mandatory")
_SkGeStatTxOkCts_Type = Counter32
_SkGeStatTxOkCts_Object = MibTableColumn
skGeStatTxOkCts = _SkGeStatTxOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 3),
    _SkGeStatTxOkCts_Type()
)
skGeStatTxOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOkCts.setStatus("mandatory")
_SkGeStatTxOctetsHighOkCts_Type = Counter32
_SkGeStatTxOctetsHighOkCts_Object = MibTableColumn
skGeStatTxOctetsHighOkCts = _SkGeStatTxOctetsHighOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 4),
    _SkGeStatTxOctetsHighOkCts_Type()
)
skGeStatTxOctetsHighOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOctetsHighOkCts.setStatus("mandatory")
_SkGeStatTxOctetsLowOkCts_Type = Counter32
_SkGeStatTxOctetsLowOkCts_Object = MibTableColumn
skGeStatTxOctetsLowOkCts = _SkGeStatTxOctetsLowOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 5),
    _SkGeStatTxOctetsLowOkCts_Type()
)
skGeStatTxOctetsLowOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOctetsLowOkCts.setStatus("mandatory")
_SkGeStatTxBroadcastOkCts_Type = Counter32
_SkGeStatTxBroadcastOkCts_Object = MibTableColumn
skGeStatTxBroadcastOkCts = _SkGeStatTxBroadcastOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 6),
    _SkGeStatTxBroadcastOkCts_Type()
)
skGeStatTxBroadcastOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxBroadcastOkCts.setStatus("mandatory")
_SkGeStatTxMulticastOkCts_Type = Counter32
_SkGeStatTxMulticastOkCts_Object = MibTableColumn
skGeStatTxMulticastOkCts = _SkGeStatTxMulticastOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 7),
    _SkGeStatTxMulticastOkCts_Type()
)
skGeStatTxMulticastOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxMulticastOkCts.setStatus("mandatory")
_SkGeStatTxUnicastOkCts_Type = Counter32
_SkGeStatTxUnicastOkCts_Object = MibTableColumn
skGeStatTxUnicastOkCts = _SkGeStatTxUnicastOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 8),
    _SkGeStatTxUnicastOkCts_Type()
)
skGeStatTxUnicastOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxUnicastOkCts.setStatus("mandatory")
_SkGeStatTxLongFramesCts_Type = Counter32
_SkGeStatTxLongFramesCts_Object = MibTableColumn
skGeStatTxLongFramesCts = _SkGeStatTxLongFramesCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 9),
    _SkGeStatTxLongFramesCts_Type()
)
skGeStatTxLongFramesCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxLongFramesCts.setStatus("mandatory")
_SkGeStatTxBurstCts_Type = Counter32
_SkGeStatTxBurstCts_Object = MibTableColumn
skGeStatTxBurstCts = _SkGeStatTxBurstCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 10),
    _SkGeStatTxBurstCts_Type()
)
skGeStatTxBurstCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxBurstCts.setStatus("mandatory")
_SkGeStatTxPFlowCtrlCts_Type = Counter32
_SkGeStatTxPFlowCtrlCts_Object = MibTableColumn
skGeStatTxPFlowCtrlCts = _SkGeStatTxPFlowCtrlCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 11),
    _SkGeStatTxPFlowCtrlCts_Type()
)
skGeStatTxPFlowCtrlCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxPFlowCtrlCts.setStatus("mandatory")
_SkGeStatTxFlowCtrlCts_Type = Counter32
_SkGeStatTxFlowCtrlCts_Object = MibTableColumn
skGeStatTxFlowCtrlCts = _SkGeStatTxFlowCtrlCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 12),
    _SkGeStatTxFlowCtrlCts_Type()
)
skGeStatTxFlowCtrlCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxFlowCtrlCts.setStatus("mandatory")
_SkGeStatTxSingleCollisionsCts_Type = Counter32
_SkGeStatTxSingleCollisionsCts_Object = MibTableColumn
skGeStatTxSingleCollisionsCts = _SkGeStatTxSingleCollisionsCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 13),
    _SkGeStatTxSingleCollisionsCts_Type()
)
skGeStatTxSingleCollisionsCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxSingleCollisionsCts.setStatus("mandatory")
_SkGeStatTxMultipleCollisionsCts_Type = Counter32
_SkGeStatTxMultipleCollisionsCts_Object = MibTableColumn
skGeStatTxMultipleCollisionsCts = _SkGeStatTxMultipleCollisionsCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 14),
    _SkGeStatTxMultipleCollisionsCts_Type()
)
skGeStatTxMultipleCollisionsCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxMultipleCollisionsCts.setStatus("mandatory")
_SkGeStatTxExcessiveCollisionsCts_Type = Counter32
_SkGeStatTxExcessiveCollisionsCts_Object = MibTableColumn
skGeStatTxExcessiveCollisionsCts = _SkGeStatTxExcessiveCollisionsCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 15),
    _SkGeStatTxExcessiveCollisionsCts_Type()
)
skGeStatTxExcessiveCollisionsCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxExcessiveCollisionsCts.setStatus("mandatory")
_SkGeStatTxLateCollisionsCts_Type = Counter32
_SkGeStatTxLateCollisionsCts_Object = MibTableColumn
skGeStatTxLateCollisionsCts = _SkGeStatTxLateCollisionsCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 16),
    _SkGeStatTxLateCollisionsCts_Type()
)
skGeStatTxLateCollisionsCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxLateCollisionsCts.setStatus("mandatory")
_SkGeStatTxDeferralCts_Type = Counter32
_SkGeStatTxDeferralCts_Object = MibTableColumn
skGeStatTxDeferralCts = _SkGeStatTxDeferralCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 17),
    _SkGeStatTxDeferralCts_Type()
)
skGeStatTxDeferralCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxDeferralCts.setStatus("mandatory")
_SkGeStatTxExcessiveDeferralCts_Type = Counter32
_SkGeStatTxExcessiveDeferralCts_Object = MibTableColumn
skGeStatTxExcessiveDeferralCts = _SkGeStatTxExcessiveDeferralCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 18),
    _SkGeStatTxExcessiveDeferralCts_Type()
)
skGeStatTxExcessiveDeferralCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxExcessiveDeferralCts.setStatus("mandatory")
_SkGeStatTxFifoUnderrunCts_Type = Counter32
_SkGeStatTxFifoUnderrunCts_Object = MibTableColumn
skGeStatTxFifoUnderrunCts = _SkGeStatTxFifoUnderrunCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 19),
    _SkGeStatTxFifoUnderrunCts_Type()
)
skGeStatTxFifoUnderrunCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxFifoUnderrunCts.setStatus("mandatory")
_SkGeStatTxCarrierSenseCts_Type = Counter32
_SkGeStatTxCarrierSenseCts_Object = MibTableColumn
skGeStatTxCarrierSenseCts = _SkGeStatTxCarrierSenseCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 20),
    _SkGeStatTxCarrierSenseCts_Type()
)
skGeStatTxCarrierSenseCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxCarrierSenseCts.setStatus("mandatory")
_SkGeStatTxOctets64Cts_Type = Counter32
_SkGeStatTxOctets64Cts_Object = MibTableColumn
skGeStatTxOctets64Cts = _SkGeStatTxOctets64Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 22),
    _SkGeStatTxOctets64Cts_Type()
)
skGeStatTxOctets64Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOctets64Cts.setStatus("mandatory")
_SkGeStatTxOctets127Cts_Type = Counter32
_SkGeStatTxOctets127Cts_Object = MibTableColumn
skGeStatTxOctets127Cts = _SkGeStatTxOctets127Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 23),
    _SkGeStatTxOctets127Cts_Type()
)
skGeStatTxOctets127Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOctets127Cts.setStatus("mandatory")
_SkGeStatTxOctets255Cts_Type = Counter32
_SkGeStatTxOctets255Cts_Object = MibTableColumn
skGeStatTxOctets255Cts = _SkGeStatTxOctets255Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 24),
    _SkGeStatTxOctets255Cts_Type()
)
skGeStatTxOctets255Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOctets255Cts.setStatus("mandatory")
_SkGeStatTxOctets511Cts_Type = Counter32
_SkGeStatTxOctets511Cts_Object = MibTableColumn
skGeStatTxOctets511Cts = _SkGeStatTxOctets511Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 25),
    _SkGeStatTxOctets511Cts_Type()
)
skGeStatTxOctets511Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOctets511Cts.setStatus("mandatory")
_SkGeStatTxOctets1023Cts_Type = Counter32
_SkGeStatTxOctets1023Cts_Object = MibTableColumn
skGeStatTxOctets1023Cts = _SkGeStatTxOctets1023Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 26),
    _SkGeStatTxOctets1023Cts_Type()
)
skGeStatTxOctets1023Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOctets1023Cts.setStatus("mandatory")
_SkGeStatTxOctetsMaxCts_Type = Counter32
_SkGeStatTxOctetsMaxCts_Object = MibTableColumn
skGeStatTxOctetsMaxCts = _SkGeStatTxOctetsMaxCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 27),
    _SkGeStatTxOctetsMaxCts_Type()
)
skGeStatTxOctetsMaxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxOctetsMaxCts.setStatus("mandatory")
_SkGeStatTxSyncCts_Type = Counter32
_SkGeStatTxSyncCts_Object = MibTableColumn
skGeStatTxSyncCts = _SkGeStatTxSyncCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 28),
    _SkGeStatTxSyncCts_Type()
)
skGeStatTxSyncCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxSyncCts.setStatus("mandatory")
_SkGeStatTxSyncOctetsHighCts_Type = Counter32
_SkGeStatTxSyncOctetsHighCts_Object = MibTableColumn
skGeStatTxSyncOctetsHighCts = _SkGeStatTxSyncOctetsHighCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 29),
    _SkGeStatTxSyncOctetsHighCts_Type()
)
skGeStatTxSyncOctetsHighCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxSyncOctetsHighCts.setStatus("mandatory")
_SkGeStatTxSyncOctetsLowCts_Type = Counter32
_SkGeStatTxSyncOctetsLowCts_Object = MibTableColumn
skGeStatTxSyncOctetsLowCts = _SkGeStatTxSyncOctetsLowCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 30),
    _SkGeStatTxSyncOctetsLowCts_Type()
)
skGeStatTxSyncOctetsLowCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatTxSyncOctetsLowCts.setStatus("mandatory")
_SkGeStatRxOkCts_Type = Counter32
_SkGeStatRxOkCts_Object = MibTableColumn
skGeStatRxOkCts = _SkGeStatRxOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 31),
    _SkGeStatRxOkCts_Type()
)
skGeStatRxOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOkCts.setStatus("mandatory")
_SkGeStatRxOctetsHighOkCts_Type = Counter32
_SkGeStatRxOctetsHighOkCts_Object = MibTableColumn
skGeStatRxOctetsHighOkCts = _SkGeStatRxOctetsHighOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 32),
    _SkGeStatRxOctetsHighOkCts_Type()
)
skGeStatRxOctetsHighOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOctetsHighOkCts.setStatus("mandatory")
_SkGeStatRxOctetsLowOkCts_Type = Counter32
_SkGeStatRxOctetsLowOkCts_Object = MibTableColumn
skGeStatRxOctetsLowOkCts = _SkGeStatRxOctetsLowOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 33),
    _SkGeStatRxOctetsLowOkCts_Type()
)
skGeStatRxOctetsLowOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOctetsLowOkCts.setStatus("mandatory")
_SkGeStatRxBroadcastOkCts_Type = Counter32
_SkGeStatRxBroadcastOkCts_Object = MibTableColumn
skGeStatRxBroadcastOkCts = _SkGeStatRxBroadcastOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 34),
    _SkGeStatRxBroadcastOkCts_Type()
)
skGeStatRxBroadcastOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxBroadcastOkCts.setStatus("mandatory")
_SkGeStatRxMulticastOkCts_Type = Counter32
_SkGeStatRxMulticastOkCts_Object = MibTableColumn
skGeStatRxMulticastOkCts = _SkGeStatRxMulticastOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 35),
    _SkGeStatRxMulticastOkCts_Type()
)
skGeStatRxMulticastOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxMulticastOkCts.setStatus("mandatory")
_SkGeStatRxUnicastOkCts_Type = Counter32
_SkGeStatRxUnicastOkCts_Object = MibTableColumn
skGeStatRxUnicastOkCts = _SkGeStatRxUnicastOkCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 36),
    _SkGeStatRxUnicastOkCts_Type()
)
skGeStatRxUnicastOkCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxUnicastOkCts.setStatus("mandatory")
_SkGeStatRxPFlowCtrlCts_Type = Counter32
_SkGeStatRxPFlowCtrlCts_Object = MibTableColumn
skGeStatRxPFlowCtrlCts = _SkGeStatRxPFlowCtrlCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 37),
    _SkGeStatRxPFlowCtrlCts_Type()
)
skGeStatRxPFlowCtrlCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxPFlowCtrlCts.setStatus("mandatory")
_SkGeStatRxFlowCtrlCts_Type = Counter32
_SkGeStatRxFlowCtrlCts_Object = MibTableColumn
skGeStatRxFlowCtrlCts = _SkGeStatRxFlowCtrlCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 38),
    _SkGeStatRxFlowCtrlCts_Type()
)
skGeStatRxFlowCtrlCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxFlowCtrlCts.setStatus("mandatory")
_SkGeStatRxPFlowCtrlErrCts_Type = Counter32
_SkGeStatRxPFlowCtrlErrCts_Object = MibTableColumn
skGeStatRxPFlowCtrlErrCts = _SkGeStatRxPFlowCtrlErrCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 39),
    _SkGeStatRxPFlowCtrlErrCts_Type()
)
skGeStatRxPFlowCtrlErrCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxPFlowCtrlErrCts.setStatus("mandatory")
_SkGeStatRxFlowCtrlUnknownCts_Type = Counter32
_SkGeStatRxFlowCtrlUnknownCts_Object = MibTableColumn
skGeStatRxFlowCtrlUnknownCts = _SkGeStatRxFlowCtrlUnknownCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 40),
    _SkGeStatRxFlowCtrlUnknownCts_Type()
)
skGeStatRxFlowCtrlUnknownCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxFlowCtrlUnknownCts.setStatus("mandatory")
_SkGeStatRxBurstCts_Type = Counter32
_SkGeStatRxBurstCts_Object = MibTableColumn
skGeStatRxBurstCts = _SkGeStatRxBurstCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 41),
    _SkGeStatRxBurstCts_Type()
)
skGeStatRxBurstCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxBurstCts.setStatus("mandatory")
_SkGeStatRxMissedCts_Type = Counter32
_SkGeStatRxMissedCts_Object = MibTableColumn
skGeStatRxMissedCts = _SkGeStatRxMissedCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 42),
    _SkGeStatRxMissedCts_Type()
)
skGeStatRxMissedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxMissedCts.setStatus("mandatory")
_SkGeStatRxFramingCts_Type = Counter32
_SkGeStatRxFramingCts_Object = MibTableColumn
skGeStatRxFramingCts = _SkGeStatRxFramingCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 43),
    _SkGeStatRxFramingCts_Type()
)
skGeStatRxFramingCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxFramingCts.setStatus("mandatory")
_SkGeStatRxFifoOverflowCts_Type = Counter32
_SkGeStatRxFifoOverflowCts_Object = MibTableColumn
skGeStatRxFifoOverflowCts = _SkGeStatRxFifoOverflowCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 44),
    _SkGeStatRxFifoOverflowCts_Type()
)
skGeStatRxFifoOverflowCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxFifoOverflowCts.setStatus("mandatory")
_SkGeStatRxJabberCts_Type = Counter32
_SkGeStatRxJabberCts_Object = MibTableColumn
skGeStatRxJabberCts = _SkGeStatRxJabberCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 45),
    _SkGeStatRxJabberCts_Type()
)
skGeStatRxJabberCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxJabberCts.setStatus("mandatory")
_SkGeStatRxCarrierCts_Type = Counter32
_SkGeStatRxCarrierCts_Object = MibTableColumn
skGeStatRxCarrierCts = _SkGeStatRxCarrierCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 46),
    _SkGeStatRxCarrierCts_Type()
)
skGeStatRxCarrierCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxCarrierCts.setStatus("mandatory")
_SkGeStatRxIRLengthCts_Type = Counter32
_SkGeStatRxIRLengthCts_Object = MibTableColumn
skGeStatRxIRLengthCts = _SkGeStatRxIRLengthCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 47),
    _SkGeStatRxIRLengthCts_Type()
)
skGeStatRxIRLengthCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxIRLengthCts.setStatus("mandatory")
_SkGeStatRxSymbolCts_Type = Counter32
_SkGeStatRxSymbolCts_Object = MibTableColumn
skGeStatRxSymbolCts = _SkGeStatRxSymbolCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 48),
    _SkGeStatRxSymbolCts_Type()
)
skGeStatRxSymbolCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxSymbolCts.setStatus("mandatory")
_SkGeStatRxShortsCts_Type = Counter32
_SkGeStatRxShortsCts_Object = MibTableColumn
skGeStatRxShortsCts = _SkGeStatRxShortsCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 49),
    _SkGeStatRxShortsCts_Type()
)
skGeStatRxShortsCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxShortsCts.setStatus("mandatory")
_SkGeStatRxRuntCts_Type = Counter32
_SkGeStatRxRuntCts_Object = MibTableColumn
skGeStatRxRuntCts = _SkGeStatRxRuntCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 50),
    _SkGeStatRxRuntCts_Type()
)
skGeStatRxRuntCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxRuntCts.setStatus("mandatory")
_SkGeStatRxCextCts_Type = Counter32
_SkGeStatRxCextCts_Object = MibTableColumn
skGeStatRxCextCts = _SkGeStatRxCextCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 51),
    _SkGeStatRxCextCts_Type()
)
skGeStatRxCextCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxCextCts.setStatus("mandatory")
_SkGeStatRxTooLongCts_Type = Counter32
_SkGeStatRxTooLongCts_Object = MibTableColumn
skGeStatRxTooLongCts = _SkGeStatRxTooLongCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 52),
    _SkGeStatRxTooLongCts_Type()
)
skGeStatRxTooLongCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxTooLongCts.setStatus("mandatory")
_SkGeStatRxFCSCts_Type = Counter32
_SkGeStatRxFCSCts_Object = MibTableColumn
skGeStatRxFCSCts = _SkGeStatRxFCSCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 53),
    _SkGeStatRxFCSCts_Type()
)
skGeStatRxFCSCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxFCSCts.setStatus("mandatory")
_SkGeStatRxOctets64Cts_Type = Counter32
_SkGeStatRxOctets64Cts_Object = MibTableColumn
skGeStatRxOctets64Cts = _SkGeStatRxOctets64Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 55),
    _SkGeStatRxOctets64Cts_Type()
)
skGeStatRxOctets64Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOctets64Cts.setStatus("mandatory")
_SkGeStatRxOctets127Cts_Type = Counter32
_SkGeStatRxOctets127Cts_Object = MibTableColumn
skGeStatRxOctets127Cts = _SkGeStatRxOctets127Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 56),
    _SkGeStatRxOctets127Cts_Type()
)
skGeStatRxOctets127Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOctets127Cts.setStatus("mandatory")
_SkGeStatRxOctets255Cts_Type = Counter32
_SkGeStatRxOctets255Cts_Object = MibTableColumn
skGeStatRxOctets255Cts = _SkGeStatRxOctets255Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 57),
    _SkGeStatRxOctets255Cts_Type()
)
skGeStatRxOctets255Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOctets255Cts.setStatus("mandatory")
_SkGeStatRxOctets511Cts_Type = Counter32
_SkGeStatRxOctets511Cts_Object = MibTableColumn
skGeStatRxOctets511Cts = _SkGeStatRxOctets511Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 58),
    _SkGeStatRxOctets511Cts_Type()
)
skGeStatRxOctets511Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOctets511Cts.setStatus("mandatory")
_SkGeStatRxOctets1023Cts_Type = Counter32
_SkGeStatRxOctets1023Cts_Object = MibTableColumn
skGeStatRxOctets1023Cts = _SkGeStatRxOctets1023Cts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 59),
    _SkGeStatRxOctets1023Cts_Type()
)
skGeStatRxOctets1023Cts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOctets1023Cts.setStatus("mandatory")
_SkGeStatRxOctetsMaxCts_Type = Counter32
_SkGeStatRxOctetsMaxCts_Object = MibTableColumn
skGeStatRxOctetsMaxCts = _SkGeStatRxOctetsMaxCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 60),
    _SkGeStatRxOctetsMaxCts_Type()
)
skGeStatRxOctetsMaxCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxOctetsMaxCts.setStatus("mandatory")
_SkGeStatRxLongFramesCts_Type = Counter32
_SkGeStatRxLongFramesCts_Object = MibTableColumn
skGeStatRxLongFramesCts = _SkGeStatRxLongFramesCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 16, 1, 61),
    _SkGeStatRxLongFramesCts_Type()
)
skGeStatRxLongFramesCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeStatRxLongFramesCts.setStatus("mandatory")
_SkGeConfEntriesNumber_Type = Integer32
_SkGeConfEntriesNumber_Object = MibScalar
skGeConfEntriesNumber = _SkGeConfEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 17),
    _SkGeConfEntriesNumber_Type()
)
skGeConfEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfEntriesNumber.setStatus("mandatory")
_SkGeConfTable_Object = MibTable
skGeConfTable = _SkGeConfTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18)
)
if mibBuilder.loadTexts:
    skGeConfTable.setStatus("mandatory")
_SkGeConfEntry_Object = MibTableRow
skGeConfEntry = _SkGeConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1)
)
skGeConfEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeConfGeIndex"),
    (0, "SK-GE-MIB", "skGeConfIndex"),
)
if mibBuilder.loadTexts:
    skGeConfEntry.setStatus("mandatory")
_SkGeConfGeIndex_Type = Integer32
_SkGeConfGeIndex_Object = MibTableColumn
skGeConfGeIndex = _SkGeConfGeIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 1),
    _SkGeConfGeIndex_Type()
)
skGeConfGeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfGeIndex.setStatus("mandatory")
_SkGeConfIndex_Type = Integer32
_SkGeConfIndex_Object = MibTableColumn
skGeConfIndex = _SkGeConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 2),
    _SkGeConfIndex_Type()
)
skGeConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfIndex.setStatus("mandatory")
_SkGeConfPhysCurrentAddr_Type = SkGeMACAddress
_SkGeConfPhysCurrentAddr_Object = MibTableColumn
skGeConfPhysCurrentAddr = _SkGeConfPhysCurrentAddr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 3),
    _SkGeConfPhysCurrentAddr_Type()
)
skGeConfPhysCurrentAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfPhysCurrentAddr.setStatus("mandatory")
_SkGeConfPhysFactoryAddr_Type = SkGeMACAddress
_SkGeConfPhysFactoryAddr_Object = MibTableColumn
skGeConfPhysFactoryAddr = _SkGeConfPhysFactoryAddr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 4),
    _SkGeConfPhysFactoryAddr_Type()
)
skGeConfPhysFactoryAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfPhysFactoryAddr.setStatus("mandatory")


class _SkGeConfPMDType_Type(Integer32):
    """Custom type skGeConfPMDType based on Integer32"""
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
        *(("ge1000Base-CX", 4),
          ("ge1000Base-LX", 2),
          ("ge1000Base-SX", 3),
          ("ge1000Base-T", 5),
          ("unknown", 1))
    )


_SkGeConfPMDType_Type.__name__ = "Integer32"
_SkGeConfPMDType_Object = MibTableColumn
skGeConfPMDType = _SkGeConfPMDType_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 5),
    _SkGeConfPMDType_Type()
)
skGeConfPMDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfPMDType.setStatus("mandatory")


class _SkGeConfConnector_Type(Integer32):
    """Custom type skGeConfConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("d-sub", 3),
          ("duplex-sc", 2),
          ("fc-s2", 4),
          ("unknown", 1),
          ("utp", 5),
          ("volition", 6))
    )


_SkGeConfConnector_Type.__name__ = "Integer32"
_SkGeConfConnector_Object = MibTableColumn
skGeConfConnector = _SkGeConfConnector_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 6),
    _SkGeConfConnector_Type()
)
skGeConfConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfConnector.setStatus("mandatory")


class _SkGeConfLinkCap_Type(Integer32):
    """Custom type skGeConfLinkCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SkGeConfLinkCap_Type.__name__ = "Integer32"
_SkGeConfLinkCap_Object = MibTableColumn
skGeConfLinkCap = _SkGeConfLinkCap_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 7),
    _SkGeConfLinkCap_Type()
)
skGeConfLinkCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfLinkCap.setStatus("mandatory")


class _SkGeConfLinkMode_Type(Integer32):
    """Custom type skGeConfLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto-both", 5),
          ("auto-full-duplex", 4),
          ("auto-half-duplex", 3),
          ("full-duplex", 2),
          ("half-duplex", 1),
          ("sense", 6))
    )


_SkGeConfLinkMode_Type.__name__ = "Integer32"
_SkGeConfLinkMode_Object = MibTableColumn
skGeConfLinkMode = _SkGeConfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 8),
    _SkGeConfLinkMode_Type()
)
skGeConfLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeConfLinkMode.setStatus("mandatory")


class _SkGeConfLinkModeStatus_Type(Integer32):
    """Custom type skGeConfLinkModeStatus based on Integer32"""
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
        *(("auto-full-duplex", 5),
          ("auto-half-duplex", 4),
          ("full-duplex", 3),
          ("half-duplex", 2),
          ("unknown", 1))
    )


_SkGeConfLinkModeStatus_Type.__name__ = "Integer32"
_SkGeConfLinkModeStatus_Object = MibTableColumn
skGeConfLinkModeStatus = _SkGeConfLinkModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 9),
    _SkGeConfLinkModeStatus_Type()
)
skGeConfLinkModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfLinkModeStatus.setStatus("mandatory")


class _SkGeConfLinkStatus_Type(Integer32):
    """Custom type skGeConfLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("link-auto-failure", 2),
          ("link-logically-down", 3),
          ("link-logically-up", 4),
          ("link-physically-down", 1))
    )


_SkGeConfLinkStatus_Type.__name__ = "Integer32"
_SkGeConfLinkStatus_Object = MibTableColumn
skGeConfLinkStatus = _SkGeConfLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 10),
    _SkGeConfLinkStatus_Type()
)
skGeConfLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfLinkStatus.setStatus("mandatory")


class _SkGeConfFlowCtrlCap_Type(Integer32):
    """Custom type skGeConfFlowCtrlCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local-send", 2),
          ("none", 1),
          ("symmetric", 3),
          ("symmetric-or-remote-send", 4))
    )


_SkGeConfFlowCtrlCap_Type.__name__ = "Integer32"
_SkGeConfFlowCtrlCap_Object = MibTableColumn
skGeConfFlowCtrlCap = _SkGeConfFlowCtrlCap_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 11),
    _SkGeConfFlowCtrlCap_Type()
)
skGeConfFlowCtrlCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfFlowCtrlCap.setStatus("mandatory")


class _SkGeConfFlowCtrlMode_Type(Integer32):
    """Custom type skGeConfFlowCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local-send", 2),
          ("none", 1),
          ("symmetric", 3),
          ("symmetric-or-remote-send", 4))
    )


_SkGeConfFlowCtrlMode_Type.__name__ = "Integer32"
_SkGeConfFlowCtrlMode_Object = MibTableColumn
skGeConfFlowCtrlMode = _SkGeConfFlowCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 12),
    _SkGeConfFlowCtrlMode_Type()
)
skGeConfFlowCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeConfFlowCtrlMode.setStatus("mandatory")


class _SkGeConfFlowCtrlStatus_Type(Integer32):
    """Custom type skGeConfFlowCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local-send", 3),
          ("none", 1),
          ("remote-send", 2),
          ("symmetric", 4))
    )


_SkGeConfFlowCtrlStatus_Type.__name__ = "Integer32"
_SkGeConfFlowCtrlStatus_Object = MibTableColumn
skGeConfFlowCtrlStatus = _SkGeConfFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 13),
    _SkGeConfFlowCtrlStatus_Type()
)
skGeConfFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfFlowCtrlStatus.setStatus("mandatory")


class _SkGeConfPhyOperationCap_Type(Integer32):
    """Custom type skGeConfPhyOperationCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SkGeConfPhyOperationCap_Type.__name__ = "Integer32"
_SkGeConfPhyOperationCap_Object = MibTableColumn
skGeConfPhyOperationCap = _SkGeConfPhyOperationCap_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 14),
    _SkGeConfPhyOperationCap_Type()
)
skGeConfPhyOperationCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfPhyOperationCap.setStatus("mandatory")


class _SkGeConfPhyOperationMode_Type(Integer32):
    """Custom type skGeConfPhyOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiation", 1),
          ("master", 2),
          ("slave", 3))
    )


_SkGeConfPhyOperationMode_Type.__name__ = "Integer32"
_SkGeConfPhyOperationMode_Object = MibTableColumn
skGeConfPhyOperationMode = _SkGeConfPhyOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 15),
    _SkGeConfPhyOperationMode_Type()
)
skGeConfPhyOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeConfPhyOperationMode.setStatus("mandatory")


class _SkGeConfPhyOperationStatus_Type(Integer32):
    """Custom type skGeConfPhyOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("configuration-fault", 4),
          ("master", 2),
          ("slave", 3),
          ("unset", 1))
    )


_SkGeConfPhyOperationStatus_Type.__name__ = "Integer32"
_SkGeConfPhyOperationStatus_Object = MibTableColumn
skGeConfPhyOperationStatus = _SkGeConfPhyOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 1, 18, 1, 16),
    _SkGeConfPhyOperationStatus_Type()
)
skGeConfPhyOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeConfPhyOperationStatus.setStatus("mandatory")
_SkGeVpd_ObjectIdentity = ObjectIdentity
skGeVpd = _SkGeVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2)
)
_SkGeVpdTable_Object = MibTable
skGeVpdTable = _SkGeVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    skGeVpdTable.setStatus("mandatory")
_SkGeVpdEntry_Object = MibTableRow
skGeVpdEntry = _SkGeVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 1, 1)
)
skGeVpdEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeVpdIndex"),
)
if mibBuilder.loadTexts:
    skGeVpdEntry.setStatus("mandatory")
_SkGeVpdIndex_Type = Integer32
_SkGeVpdIndex_Object = MibTableColumn
skGeVpdIndex = _SkGeVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 1, 1, 1),
    _SkGeVpdIndex_Type()
)
skGeVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeVpdIndex.setStatus("mandatory")
_SkGeVpdFreeBytes_Type = Integer32
_SkGeVpdFreeBytes_Object = MibTableColumn
skGeVpdFreeBytes = _SkGeVpdFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 1, 1, 2),
    _SkGeVpdFreeBytes_Type()
)
skGeVpdFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeVpdFreeBytes.setStatus("mandatory")
_SkGeVpdEntryList_Type = DisplayString
_SkGeVpdEntryList_Object = MibTableColumn
skGeVpdEntryList = _SkGeVpdEntryList_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 1, 1, 3),
    _SkGeVpdEntryList_Type()
)
skGeVpdEntryList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeVpdEntryList.setStatus("mandatory")
_SkGeVpdValueTable_Object = MibTable
skGeVpdValueTable = _SkGeVpdValueTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    skGeVpdValueTable.setStatus("mandatory")
_SkGeVpdValueEntry_Object = MibTableRow
skGeVpdValueEntry = _SkGeVpdValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 2, 1)
)
skGeVpdValueEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeVpdValueIndex"),
    (0, "SK-GE-MIB", "skGeVpdKey"),
)
if mibBuilder.loadTexts:
    skGeVpdValueEntry.setStatus("mandatory")
_SkGeVpdValueIndex_Type = Integer32
_SkGeVpdValueIndex_Object = MibTableColumn
skGeVpdValueIndex = _SkGeVpdValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 2, 1, 1),
    _SkGeVpdValueIndex_Type()
)
skGeVpdValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeVpdValueIndex.setStatus("mandatory")


class _SkGeVpdKey_Type(DisplayString):
    """Custom type skGeVpdKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SkGeVpdKey_Type.__name__ = "DisplayString"
_SkGeVpdKey_Object = MibTableColumn
skGeVpdKey = _SkGeVpdKey_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 2, 1, 2),
    _SkGeVpdKey_Type()
)
skGeVpdKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeVpdKey.setStatus("mandatory")
_SkGeVpdValue_Type = OctetString
_SkGeVpdValue_Object = MibTableColumn
skGeVpdValue = _SkGeVpdValue_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 2, 1, 3),
    _SkGeVpdValue_Type()
)
skGeVpdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeVpdValue.setStatus("mandatory")


class _SkGeVpdAccess_Type(Integer32):
    """Custom type skGeVpdAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_SkGeVpdAccess_Type.__name__ = "Integer32"
_SkGeVpdAccess_Object = MibTableColumn
skGeVpdAccess = _SkGeVpdAccess_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 2, 1, 4),
    _SkGeVpdAccess_Type()
)
skGeVpdAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeVpdAccess.setStatus("mandatory")


class _SkGeVpdValid_Type(Integer32):
    """Custom type skGeVpdValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SkGeVpdValid_Type.__name__ = "Integer32"
_SkGeVpdValid_Object = MibTableColumn
skGeVpdValid = _SkGeVpdValid_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 2, 2, 1, 5),
    _SkGeVpdValid_Type()
)
skGeVpdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeVpdValid.setStatus("mandatory")
_SkGeRlmt_ObjectIdentity = ObjectIdentity
skGeRlmt = _SkGeRlmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3)
)
_SkGeRlmtEntriesNumber_Type = Integer32
_SkGeRlmtEntriesNumber_Object = MibScalar
skGeRlmtEntriesNumber = _SkGeRlmtEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 1),
    _SkGeRlmtEntriesNumber_Type()
)
skGeRlmtEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtEntriesNumber.setStatus("mandatory")
_SkGeRlmtTable_Object = MibTable
skGeRlmtTable = _SkGeRlmtTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    skGeRlmtTable.setStatus("mandatory")
_SkGeRlmtEntry_Object = MibTableRow
skGeRlmtEntry = _SkGeRlmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1)
)
skGeRlmtEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeRlmtIndex"),
)
if mibBuilder.loadTexts:
    skGeRlmtEntry.setStatus("mandatory")
_SkGeRlmtIndex_Type = Integer32
_SkGeRlmtIndex_Object = MibTableColumn
skGeRlmtIndex = _SkGeRlmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 1),
    _SkGeRlmtIndex_Type()
)
skGeRlmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtIndex.setStatus("mandatory")


class _SkGeRlmtMode_Type(Integer32):
    """Custom type skGeRlmtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SkGeRlmtMode_Type.__name__ = "Integer32"
_SkGeRlmtMode_Object = MibTableColumn
skGeRlmtMode = _SkGeRlmtMode_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 2),
    _SkGeRlmtMode_Type()
)
skGeRlmtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeRlmtMode.setStatus("mandatory")
_SkGeRlmtPortActive_Type = Integer32
_SkGeRlmtPortActive_Object = MibTableColumn
skGeRlmtPortActive = _SkGeRlmtPortActive_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 3),
    _SkGeRlmtPortActive_Type()
)
skGeRlmtPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtPortActive.setStatus("mandatory")
_SkGeRlmtPortPreferred_Type = Integer32
_SkGeRlmtPortPreferred_Object = MibTableColumn
skGeRlmtPortPreferred = _SkGeRlmtPortPreferred_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 4),
    _SkGeRlmtPortPreferred_Type()
)
skGeRlmtPortPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeRlmtPortPreferred.setStatus("mandatory")
_SkGeRlmtChangeCts_Type = Counter32
_SkGeRlmtChangeCts_Object = MibTableColumn
skGeRlmtChangeCts = _SkGeRlmtChangeCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 5),
    _SkGeRlmtChangeCts_Type()
)
skGeRlmtChangeCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtChangeCts.setStatus("mandatory")
_SkGeRlmtChangeTimeStamp_Type = TimeTicks
_SkGeRlmtChangeTimeStamp_Object = MibTableColumn
skGeRlmtChangeTimeStamp = _SkGeRlmtChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 6),
    _SkGeRlmtChangeTimeStamp_Type()
)
skGeRlmtChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtChangeTimeStamp.setStatus("mandatory")
_SkGeRlmtChangeEstimate_Type = Integer32
_SkGeRlmtChangeEstimate_Object = MibTableColumn
skGeRlmtChangeEstimate = _SkGeRlmtChangeEstimate_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 7),
    _SkGeRlmtChangeEstimate_Type()
)
skGeRlmtChangeEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtChangeEstimate.setStatus("mandatory")
_SkGeRlmtChangeThreshold_Type = Integer32
_SkGeRlmtChangeThreshold_Object = MibTableColumn
skGeRlmtChangeThreshold = _SkGeRlmtChangeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 8),
    _SkGeRlmtChangeThreshold_Type()
)
skGeRlmtChangeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeRlmtChangeThreshold.setStatus("mandatory")
_SkGeRlmtPortNumber_Type = Integer32
_SkGeRlmtPortNumber_Object = MibTableColumn
skGeRlmtPortNumber = _SkGeRlmtPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 2, 1, 9),
    _SkGeRlmtPortNumber_Type()
)
skGeRlmtPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtPortNumber.setStatus("mandatory")
_SkGeRlmtStatEntriesNumber_Type = Integer32
_SkGeRlmtStatEntriesNumber_Object = MibScalar
skGeRlmtStatEntriesNumber = _SkGeRlmtStatEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 3),
    _SkGeRlmtStatEntriesNumber_Type()
)
skGeRlmtStatEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtStatEntriesNumber.setStatus("mandatory")
_SkGeRlmtStatTable_Object = MibTable
skGeRlmtStatTable = _SkGeRlmtStatTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4)
)
if mibBuilder.loadTexts:
    skGeRlmtStatTable.setStatus("mandatory")
_SkGeRlmtStatEntry_Object = MibTableRow
skGeRlmtStatEntry = _SkGeRlmtStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4, 1)
)
skGeRlmtStatEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeRlmtStatGeIndex"),
    (0, "SK-GE-MIB", "skGeRlmtStatIndex"),
)
if mibBuilder.loadTexts:
    skGeRlmtStatEntry.setStatus("mandatory")
_SkGeRlmtStatGeIndex_Type = Integer32
_SkGeRlmtStatGeIndex_Object = MibTableColumn
skGeRlmtStatGeIndex = _SkGeRlmtStatGeIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4, 1, 1),
    _SkGeRlmtStatGeIndex_Type()
)
skGeRlmtStatGeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtStatGeIndex.setStatus("mandatory")
_SkGeRlmtStatIndex_Type = Integer32
_SkGeRlmtStatIndex_Object = MibTableColumn
skGeRlmtStatIndex = _SkGeRlmtStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4, 1, 2),
    _SkGeRlmtStatIndex_Type()
)
skGeRlmtStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtStatIndex.setStatus("mandatory")


class _SkGeRlmtStatStatus_Type(Integer32):
    """Custom type skGeRlmtStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("error", 3),
          ("standby", 1))
    )


_SkGeRlmtStatStatus_Type.__name__ = "Integer32"
_SkGeRlmtStatStatus_Object = MibTableColumn
skGeRlmtStatStatus = _SkGeRlmtStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4, 1, 3),
    _SkGeRlmtStatStatus_Type()
)
skGeRlmtStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtStatStatus.setStatus("mandatory")
_SkGeRlmtStatTxHelloCts_Type = Counter32
_SkGeRlmtStatTxHelloCts_Object = MibTableColumn
skGeRlmtStatTxHelloCts = _SkGeRlmtStatTxHelloCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4, 1, 4),
    _SkGeRlmtStatTxHelloCts_Type()
)
skGeRlmtStatTxHelloCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtStatTxHelloCts.setStatus("mandatory")
_SkGeRlmtStatRxHelloCts_Type = Counter32
_SkGeRlmtStatRxHelloCts_Object = MibTableColumn
skGeRlmtStatRxHelloCts = _SkGeRlmtStatRxHelloCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4, 1, 5),
    _SkGeRlmtStatRxHelloCts_Type()
)
skGeRlmtStatRxHelloCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtStatRxHelloCts.setStatus("mandatory")
_SkGeRlmtStatTxSpHelloReqCts_Type = Counter32
_SkGeRlmtStatTxSpHelloReqCts_Object = MibTableColumn
skGeRlmtStatTxSpHelloReqCts = _SkGeRlmtStatTxSpHelloReqCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4, 1, 6),
    _SkGeRlmtStatTxSpHelloReqCts_Type()
)
skGeRlmtStatTxSpHelloReqCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtStatTxSpHelloReqCts.setStatus("mandatory")
_SkGeRlmtStatRxSpHelloCts_Type = Counter32
_SkGeRlmtStatRxSpHelloCts_Object = MibTableColumn
skGeRlmtStatRxSpHelloCts = _SkGeRlmtStatRxSpHelloCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 4, 1, 7),
    _SkGeRlmtStatRxSpHelloCts_Type()
)
skGeRlmtStatRxSpHelloCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtStatRxSpHelloCts.setStatus("mandatory")
_SkGeRlmtMonitorEntriesNumber_Type = Integer32
_SkGeRlmtMonitorEntriesNumber_Object = MibScalar
skGeRlmtMonitorEntriesNumber = _SkGeRlmtMonitorEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 5),
    _SkGeRlmtMonitorEntriesNumber_Type()
)
skGeRlmtMonitorEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtMonitorEntriesNumber.setStatus("mandatory")
_SkGeRlmtMonitorTable_Object = MibTable
skGeRlmtMonitorTable = _SkGeRlmtMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 6)
)
if mibBuilder.loadTexts:
    skGeRlmtMonitorTable.setStatus("mandatory")
_SkGeRlmtMonitorEntry_Object = MibTableRow
skGeRlmtMonitorEntry = _SkGeRlmtMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 6, 1)
)
skGeRlmtMonitorEntry.setIndexNames(
    (0, "SK-GE-MIB", "skGeRlmtMonitorGeIndex"),
    (0, "SK-GE-MIB", "skGeRlmtMonitorIndex"),
)
if mibBuilder.loadTexts:
    skGeRlmtMonitorEntry.setStatus("mandatory")
_SkGeRlmtMonitorGeIndex_Type = Integer32
_SkGeRlmtMonitorGeIndex_Object = MibTableColumn
skGeRlmtMonitorGeIndex = _SkGeRlmtMonitorGeIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 6, 1, 1),
    _SkGeRlmtMonitorGeIndex_Type()
)
skGeRlmtMonitorGeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtMonitorGeIndex.setStatus("mandatory")
_SkGeRlmtMonitorIndex_Type = Integer32
_SkGeRlmtMonitorIndex_Object = MibTableColumn
skGeRlmtMonitorIndex = _SkGeRlmtMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 6, 1, 2),
    _SkGeRlmtMonitorIndex_Type()
)
skGeRlmtMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtMonitorIndex.setStatus("mandatory")
_SkGeRlmtMonitorAddr_Type = SkGeMACAddress
_SkGeRlmtMonitorAddr_Object = MibTableColumn
skGeRlmtMonitorAddr = _SkGeRlmtMonitorAddr_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 6, 1, 3),
    _SkGeRlmtMonitorAddr_Type()
)
skGeRlmtMonitorAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeRlmtMonitorAddr.setStatus("mandatory")
_SkGeRlmtMonitorErrCts_Type = Counter32
_SkGeRlmtMonitorErrCts_Object = MibTableColumn
skGeRlmtMonitorErrCts = _SkGeRlmtMonitorErrCts_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 6, 1, 4),
    _SkGeRlmtMonitorErrCts_Type()
)
skGeRlmtMonitorErrCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtMonitorErrCts.setStatus("mandatory")
_SkGeRlmtMonitorErrTimeStamp_Type = TimeTicks
_SkGeRlmtMonitorErrTimeStamp_Object = MibScalar
skGeRlmtMonitorErrTimeStamp = _SkGeRlmtMonitorErrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 6, 1, 5),
    _SkGeRlmtMonitorErrTimeStamp_Type()
)
skGeRlmtMonitorErrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skGeRlmtMonitorErrTimeStamp.setStatus("mandatory")


class _SkGeRlmtMonitorAdmin_Type(Integer32):
    """Custom type skGeRlmtMonitorAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SkGeRlmtMonitorAdmin_Type.__name__ = "Integer32"
_SkGeRlmtMonitorAdmin_Object = MibTableColumn
skGeRlmtMonitorAdmin = _SkGeRlmtMonitorAdmin_Object(
    (1, 3, 6, 1, 4, 1, 179, 2, 5, 3, 6, 1, 6),
    _SkGeRlmtMonitorAdmin_Type()
)
skGeRlmtMonitorAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skGeRlmtMonitorAdmin.setStatus("mandatory")
_SkNICs_ObjectIdentity = ObjectIdentity
skNICs = _SkNICs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3)
)
_SkFddiNICs_ObjectIdentity = ObjectIdentity
skFddiNICs = _SkFddiNICs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 1)
)
_SkGeNICs_ObjectIdentity = ObjectIdentity
skGeNICs = _SkGeNICs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2)
)
_SkGeSxSingleLink_ObjectIdentity = ObjectIdentity
skGeSxSingleLink = _SkGeSxSingleLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2, 1)
)
_SkGeSxDualLink_ObjectIdentity = ObjectIdentity
skGeSxDualLink = _SkGeSxDualLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2, 2)
)
_SkGeLxSingleLink_ObjectIdentity = ObjectIdentity
skGeLxSingleLink = _SkGeLxSingleLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2, 3)
)
_SkGeLxDualLink_ObjectIdentity = ObjectIdentity
skGeLxDualLink = _SkGeLxDualLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2, 4)
)
_SkGeCxSingleLink_ObjectIdentity = ObjectIdentity
skGeCxSingleLink = _SkGeCxSingleLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2, 5)
)
_SkGeCxDualLink_ObjectIdentity = ObjectIdentity
skGeCxDualLink = _SkGeCxDualLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2, 6)
)
_SkGeTxSingleLink_ObjectIdentity = ObjectIdentity
skGeTxSingleLink = _SkGeTxSingleLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2, 7)
)
_SkGeTxDualLink_ObjectIdentity = ObjectIdentity
skGeTxDualLink = _SkGeTxDualLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 3, 2, 8)
)
_SkChipSets_ObjectIdentity = ObjectIdentity
skChipSets = _SkChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 4)
)
_SkGeXMAC11800FP_ObjectIdentity = ObjectIdentity
skGeXMAC11800FP = _SkGeXMAC11800FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 179, 4, 1)
)

# Managed Objects groups


# Notification objects

skGeSensorWarningLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 500)
)
skGeSensorWarningLower.setObjects(
      *(("SK-GE-MIB", "skGeSensorGeIndex"),
        ("SK-GE-MIB", "skGeSensorIndex"),
        ("SK-GE-MIB", "skGeSensorDescr"),
        ("SK-GE-MIB", "skGeSensorType"),
        ("SK-GE-MIB", "skGeSensorValue"))
)
if mibBuilder.loadTexts:
    skGeSensorWarningLower.setStatus(
        ""
    )

skGeSensorWarningUpper = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 501)
)
skGeSensorWarningUpper.setObjects(
      *(("SK-GE-MIB", "skGeSensorGeIndex"),
        ("SK-GE-MIB", "skGeSensorIndex"),
        ("SK-GE-MIB", "skGeSensorDescr"),
        ("SK-GE-MIB", "skGeSensorType"),
        ("SK-GE-MIB", "skGeSensorValue"))
)
if mibBuilder.loadTexts:
    skGeSensorWarningUpper.setStatus(
        ""
    )

skGeSensorErrorLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 502)
)
skGeSensorErrorLower.setObjects(
      *(("SK-GE-MIB", "skGeSensorGeIndex"),
        ("SK-GE-MIB", "skGeSensorIndex"),
        ("SK-GE-MIB", "skGeSensorDescr"),
        ("SK-GE-MIB", "skGeSensorType"),
        ("SK-GE-MIB", "skGeSensorValue"))
)
if mibBuilder.loadTexts:
    skGeSensorErrorLower.setStatus(
        ""
    )

skGeSensorErrorUpper = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 503)
)
skGeSensorErrorUpper.setObjects(
      *(("SK-GE-MIB", "skGeSensorGeIndex"),
        ("SK-GE-MIB", "skGeSensorIndex"),
        ("SK-GE-MIB", "skGeSensorDescr"),
        ("SK-GE-MIB", "skGeSensorType"),
        ("SK-GE-MIB", "skGeSensorValue"))
)
if mibBuilder.loadTexts:
    skGeSensorErrorUpper.setStatus(
        ""
    )

skGeRlmtChangeThresholdCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 520)
)
skGeRlmtChangeThresholdCondition.setObjects(
    ("SK-GE-MIB", "skGeRlmtIndex")
)
if mibBuilder.loadTexts:
    skGeRlmtChangeThresholdCondition.setStatus(
        ""
    )

skGeRlmtChangeCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 521)
)
skGeRlmtChangeCondition.setObjects(
      *(("SK-GE-MIB", "skGeRlmtIndex"),
        ("SK-GE-MIB", "skGeRlmtPortActive"))
)
if mibBuilder.loadTexts:
    skGeRlmtChangeCondition.setStatus(
        ""
    )

skGeRlmtPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 522)
)
skGeRlmtPortDown.setObjects(
      *(("SK-GE-MIB", "skGeRlmtStatGeIndex"),
        ("SK-GE-MIB", "skGeRlmtStatIndex"))
)
if mibBuilder.loadTexts:
    skGeRlmtPortDown.setStatus(
        ""
    )

skGeRlmtPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 523)
)
skGeRlmtPortUp.setObjects(
      *(("SK-GE-MIB", "skGeRlmtStatGeIndex"),
        ("SK-GE-MIB", "skGeRlmtStatIndex"))
)
if mibBuilder.loadTexts:
    skGeRlmtPortUp.setStatus(
        ""
    )

skGeRlmtSegmentation = NotificationType(
    (1, 3, 6, 1, 4, 1, 179, 0, 524)
)
skGeRlmtSegmentation.setObjects(
    ("SK-GE-MIB", "skGeRlmtIndex")
)
if mibBuilder.loadTexts:
    skGeRlmtSegmentation.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SK-GE-MIB",
    **{"SkGeMACAddress": SkGeMACAddress,
       "sk": sk,
       "skGeSensorWarningLower": skGeSensorWarningLower,
       "skGeSensorWarningUpper": skGeSensorWarningUpper,
       "skGeSensorErrorLower": skGeSensorErrorLower,
       "skGeSensorErrorUpper": skGeSensorErrorUpper,
       "skGeRlmtChangeThresholdCondition": skGeRlmtChangeThresholdCondition,
       "skGeRlmtChangeCondition": skGeRlmtChangeCondition,
       "skGeRlmtPortDown": skGeRlmtPortDown,
       "skGeRlmtPortUp": skGeRlmtPortUp,
       "skGeRlmtSegmentation": skGeRlmtSegmentation,
       "skSystems": skSystems,
       "skMibs": skMibs,
       "skConcMib": skConcMib,
       "skfddiMib": skfddiMib,
       "skGeMib": skGeMib,
       "skGeGeneral": skGeGeneral,
       "skGeMibVersion": skGeMibVersion,
       "skGeAction": skGeAction,
       "skGeNumber": skGeNumber,
       "skGeTable": skGeTable,
       "skGeEntry": skGeEntry,
       "skGeIndex": skGeIndex,
       "skGeIfIndex": skGeIfIndex,
       "skGePortNumber": skGePortNumber,
       "skGeDeviceType": skGeDeviceType,
       "skGeDriverDescr": skGeDriverDescr,
       "skGeDriverVersion": skGeDriverVersion,
       "skGeHwDescr": skGeHwDescr,
       "skGeHwVersion": skGeHwVersion,
       "skGeChipSet": skGeChipSet,
       "skGeDeviceAction": skGeDeviceAction,
       "skGeTestResult": skGeTestResult,
       "skGeBusType": skGeBusType,
       "skGeBusSpeed": skGeBusSpeed,
       "skGeBusWidth": skGeBusWidth,
       "skGeChecksumEntriesNumber": skGeChecksumEntriesNumber,
       "skGeChecksumTable": skGeChecksumTable,
       "skGeChecksumEntry": skGeChecksumEntry,
       "skGeChecksumGeIndex": skGeChecksumGeIndex,
       "skGeChecksumIndex": skGeChecksumIndex,
       "skGeChecksumRxOkCts": skGeChecksumRxOkCts,
       "skGeChecksumRxUnableCts": skGeChecksumRxUnableCts,
       "skGeChecksumRxErrCts": skGeChecksumRxErrCts,
       "skGeChecksumTxOkCts": skGeChecksumTxOkCts,
       "skGeChecksumTxUnableCts": skGeChecksumTxUnableCts,
       "skGeTrapForceType": skGeTrapForceType,
       "skGeTrapDestEntriesNumber": skGeTrapDestEntriesNumber,
       "skGeTrapDestTable": skGeTrapDestTable,
       "skGeTrapDestEntry": skGeTrapDestEntry,
       "skGeTrapDestIndex": skGeTrapDestIndex,
       "skGeTrapDestAddress": skGeTrapDestAddress,
       "skGeTrapFilter": skGeTrapFilter,
       "skGeSensorEntriesNumber": skGeSensorEntriesNumber,
       "skGeSensorTable": skGeSensorTable,
       "skGeSensorEntry": skGeSensorEntry,
       "skGeSensorGeIndex": skGeSensorGeIndex,
       "skGeSensorIndex": skGeSensorIndex,
       "skGeSensorDescr": skGeSensorDescr,
       "skGeSensorType": skGeSensorType,
       "skGeSensorValue": skGeSensorValue,
       "skGeSensorWarningThresholdLow": skGeSensorWarningThresholdLow,
       "skGeSensorWarningThresholdHigh": skGeSensorWarningThresholdHigh,
       "skGeSensorErrorThresholdLow": skGeSensorErrorThresholdLow,
       "skGeSensorErrorThresholdHigh": skGeSensorErrorThresholdHigh,
       "skGeSensorStatus": skGeSensorStatus,
       "skGeSensorWarningCts": skGeSensorWarningCts,
       "skGeSensorErrorCts": skGeSensorErrorCts,
       "skGeSensorWarningTimeStamp": skGeSensorWarningTimeStamp,
       "skGeSensorErrorTimeStamp": skGeSensorErrorTimeStamp,
       "skGeStatEntriesNumber": skGeStatEntriesNumber,
       "skGeStatTable": skGeStatTable,
       "skGeStatEntry": skGeStatEntry,
       "skGeStatGeIndex": skGeStatGeIndex,
       "skGeStatIndex": skGeStatIndex,
       "skGeStatTxOkCts": skGeStatTxOkCts,
       "skGeStatTxOctetsHighOkCts": skGeStatTxOctetsHighOkCts,
       "skGeStatTxOctetsLowOkCts": skGeStatTxOctetsLowOkCts,
       "skGeStatTxBroadcastOkCts": skGeStatTxBroadcastOkCts,
       "skGeStatTxMulticastOkCts": skGeStatTxMulticastOkCts,
       "skGeStatTxUnicastOkCts": skGeStatTxUnicastOkCts,
       "skGeStatTxLongFramesCts": skGeStatTxLongFramesCts,
       "skGeStatTxBurstCts": skGeStatTxBurstCts,
       "skGeStatTxPFlowCtrlCts": skGeStatTxPFlowCtrlCts,
       "skGeStatTxFlowCtrlCts": skGeStatTxFlowCtrlCts,
       "skGeStatTxSingleCollisionsCts": skGeStatTxSingleCollisionsCts,
       "skGeStatTxMultipleCollisionsCts": skGeStatTxMultipleCollisionsCts,
       "skGeStatTxExcessiveCollisionsCts": skGeStatTxExcessiveCollisionsCts,
       "skGeStatTxLateCollisionsCts": skGeStatTxLateCollisionsCts,
       "skGeStatTxDeferralCts": skGeStatTxDeferralCts,
       "skGeStatTxExcessiveDeferralCts": skGeStatTxExcessiveDeferralCts,
       "skGeStatTxFifoUnderrunCts": skGeStatTxFifoUnderrunCts,
       "skGeStatTxCarrierSenseCts": skGeStatTxCarrierSenseCts,
       "skGeStatTxOctets64Cts": skGeStatTxOctets64Cts,
       "skGeStatTxOctets127Cts": skGeStatTxOctets127Cts,
       "skGeStatTxOctets255Cts": skGeStatTxOctets255Cts,
       "skGeStatTxOctets511Cts": skGeStatTxOctets511Cts,
       "skGeStatTxOctets1023Cts": skGeStatTxOctets1023Cts,
       "skGeStatTxOctetsMaxCts": skGeStatTxOctetsMaxCts,
       "skGeStatTxSyncCts": skGeStatTxSyncCts,
       "skGeStatTxSyncOctetsHighCts": skGeStatTxSyncOctetsHighCts,
       "skGeStatTxSyncOctetsLowCts": skGeStatTxSyncOctetsLowCts,
       "skGeStatRxOkCts": skGeStatRxOkCts,
       "skGeStatRxOctetsHighOkCts": skGeStatRxOctetsHighOkCts,
       "skGeStatRxOctetsLowOkCts": skGeStatRxOctetsLowOkCts,
       "skGeStatRxBroadcastOkCts": skGeStatRxBroadcastOkCts,
       "skGeStatRxMulticastOkCts": skGeStatRxMulticastOkCts,
       "skGeStatRxUnicastOkCts": skGeStatRxUnicastOkCts,
       "skGeStatRxPFlowCtrlCts": skGeStatRxPFlowCtrlCts,
       "skGeStatRxFlowCtrlCts": skGeStatRxFlowCtrlCts,
       "skGeStatRxPFlowCtrlErrCts": skGeStatRxPFlowCtrlErrCts,
       "skGeStatRxFlowCtrlUnknownCts": skGeStatRxFlowCtrlUnknownCts,
       "skGeStatRxBurstCts": skGeStatRxBurstCts,
       "skGeStatRxMissedCts": skGeStatRxMissedCts,
       "skGeStatRxFramingCts": skGeStatRxFramingCts,
       "skGeStatRxFifoOverflowCts": skGeStatRxFifoOverflowCts,
       "skGeStatRxJabberCts": skGeStatRxJabberCts,
       "skGeStatRxCarrierCts": skGeStatRxCarrierCts,
       "skGeStatRxIRLengthCts": skGeStatRxIRLengthCts,
       "skGeStatRxSymbolCts": skGeStatRxSymbolCts,
       "skGeStatRxShortsCts": skGeStatRxShortsCts,
       "skGeStatRxRuntCts": skGeStatRxRuntCts,
       "skGeStatRxCextCts": skGeStatRxCextCts,
       "skGeStatRxTooLongCts": skGeStatRxTooLongCts,
       "skGeStatRxFCSCts": skGeStatRxFCSCts,
       "skGeStatRxOctets64Cts": skGeStatRxOctets64Cts,
       "skGeStatRxOctets127Cts": skGeStatRxOctets127Cts,
       "skGeStatRxOctets255Cts": skGeStatRxOctets255Cts,
       "skGeStatRxOctets511Cts": skGeStatRxOctets511Cts,
       "skGeStatRxOctets1023Cts": skGeStatRxOctets1023Cts,
       "skGeStatRxOctetsMaxCts": skGeStatRxOctetsMaxCts,
       "skGeStatRxLongFramesCts": skGeStatRxLongFramesCts,
       "skGeConfEntriesNumber": skGeConfEntriesNumber,
       "skGeConfTable": skGeConfTable,
       "skGeConfEntry": skGeConfEntry,
       "skGeConfGeIndex": skGeConfGeIndex,
       "skGeConfIndex": skGeConfIndex,
       "skGeConfPhysCurrentAddr": skGeConfPhysCurrentAddr,
       "skGeConfPhysFactoryAddr": skGeConfPhysFactoryAddr,
       "skGeConfPMDType": skGeConfPMDType,
       "skGeConfConnector": skGeConfConnector,
       "skGeConfLinkCap": skGeConfLinkCap,
       "skGeConfLinkMode": skGeConfLinkMode,
       "skGeConfLinkModeStatus": skGeConfLinkModeStatus,
       "skGeConfLinkStatus": skGeConfLinkStatus,
       "skGeConfFlowCtrlCap": skGeConfFlowCtrlCap,
       "skGeConfFlowCtrlMode": skGeConfFlowCtrlMode,
       "skGeConfFlowCtrlStatus": skGeConfFlowCtrlStatus,
       "skGeConfPhyOperationCap": skGeConfPhyOperationCap,
       "skGeConfPhyOperationMode": skGeConfPhyOperationMode,
       "skGeConfPhyOperationStatus": skGeConfPhyOperationStatus,
       "skGeVpd": skGeVpd,
       "skGeVpdTable": skGeVpdTable,
       "skGeVpdEntry": skGeVpdEntry,
       "skGeVpdIndex": skGeVpdIndex,
       "skGeVpdFreeBytes": skGeVpdFreeBytes,
       "skGeVpdEntryList": skGeVpdEntryList,
       "skGeVpdValueTable": skGeVpdValueTable,
       "skGeVpdValueEntry": skGeVpdValueEntry,
       "skGeVpdValueIndex": skGeVpdValueIndex,
       "skGeVpdKey": skGeVpdKey,
       "skGeVpdValue": skGeVpdValue,
       "skGeVpdAccess": skGeVpdAccess,
       "skGeVpdValid": skGeVpdValid,
       "skGeRlmt": skGeRlmt,
       "skGeRlmtEntriesNumber": skGeRlmtEntriesNumber,
       "skGeRlmtTable": skGeRlmtTable,
       "skGeRlmtEntry": skGeRlmtEntry,
       "skGeRlmtIndex": skGeRlmtIndex,
       "skGeRlmtMode": skGeRlmtMode,
       "skGeRlmtPortActive": skGeRlmtPortActive,
       "skGeRlmtPortPreferred": skGeRlmtPortPreferred,
       "skGeRlmtChangeCts": skGeRlmtChangeCts,
       "skGeRlmtChangeTimeStamp": skGeRlmtChangeTimeStamp,
       "skGeRlmtChangeEstimate": skGeRlmtChangeEstimate,
       "skGeRlmtChangeThreshold": skGeRlmtChangeThreshold,
       "skGeRlmtPortNumber": skGeRlmtPortNumber,
       "skGeRlmtStatEntriesNumber": skGeRlmtStatEntriesNumber,
       "skGeRlmtStatTable": skGeRlmtStatTable,
       "skGeRlmtStatEntry": skGeRlmtStatEntry,
       "skGeRlmtStatGeIndex": skGeRlmtStatGeIndex,
       "skGeRlmtStatIndex": skGeRlmtStatIndex,
       "skGeRlmtStatStatus": skGeRlmtStatStatus,
       "skGeRlmtStatTxHelloCts": skGeRlmtStatTxHelloCts,
       "skGeRlmtStatRxHelloCts": skGeRlmtStatRxHelloCts,
       "skGeRlmtStatTxSpHelloReqCts": skGeRlmtStatTxSpHelloReqCts,
       "skGeRlmtStatRxSpHelloCts": skGeRlmtStatRxSpHelloCts,
       "skGeRlmtMonitorEntriesNumber": skGeRlmtMonitorEntriesNumber,
       "skGeRlmtMonitorTable": skGeRlmtMonitorTable,
       "skGeRlmtMonitorEntry": skGeRlmtMonitorEntry,
       "skGeRlmtMonitorGeIndex": skGeRlmtMonitorGeIndex,
       "skGeRlmtMonitorIndex": skGeRlmtMonitorIndex,
       "skGeRlmtMonitorAddr": skGeRlmtMonitorAddr,
       "skGeRlmtMonitorErrCts": skGeRlmtMonitorErrCts,
       "skGeRlmtMonitorErrTimeStamp": skGeRlmtMonitorErrTimeStamp,
       "skGeRlmtMonitorAdmin": skGeRlmtMonitorAdmin,
       "skNICs": skNICs,
       "skFddiNICs": skFddiNICs,
       "skGeNICs": skGeNICs,
       "skGeSxSingleLink": skGeSxSingleLink,
       "skGeSxDualLink": skGeSxDualLink,
       "skGeLxSingleLink": skGeLxSingleLink,
       "skGeLxDualLink": skGeLxDualLink,
       "skGeCxSingleLink": skGeCxSingleLink,
       "skGeCxDualLink": skGeCxDualLink,
       "skGeTxSingleLink": skGeTxSingleLink,
       "skGeTxDualLink": skGeTxDualLink,
       "skChipSets": skChipSets,
       "skGeXMAC11800FP": skGeXMAC11800FP}
)
