# SNMP MIB module (TERAWAVE-terasystem-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-terasystem-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:24 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraSystem_ObjectIdentity = ObjectIdentity
teraSystem = _TeraSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5)
)
_TeraSystemTime_Type = Integer32
_TeraSystemTime_Object = MibScalar
teraSystemTime = _TeraSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 1),
    _TeraSystemTime_Type()
)
teraSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemTime.setStatus("mandatory")
_TeraSystemCurrTime_Type = Integer32
_TeraSystemCurrTime_Object = MibScalar
teraSystemCurrTime = _TeraSystemCurrTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 2),
    _TeraSystemCurrTime_Type()
)
teraSystemCurrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSystemCurrTime.setStatus("mandatory")
_TeraSlotInstTablePar_ObjectIdentity = ObjectIdentity
teraSlotInstTablePar = _TeraSlotInstTablePar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3)
)
_TeraSlotInstallTable_Object = MibTable
teraSlotInstallTable = _TeraSlotInstallTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1)
)
if mibBuilder.loadTexts:
    teraSlotInstallTable.setStatus("mandatory")
_TeraSlotInstallTableEntry_Object = MibTableRow
teraSlotInstallTableEntry = _TeraSlotInstallTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1)
)
teraSlotInstallTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraInstallSlotNumber"),
)
if mibBuilder.loadTexts:
    teraSlotInstallTableEntry.setStatus("mandatory")


class _TeraInstallSlotNumber_Type(Integer32):
    """Custom type teraInstallSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraInstallSlotNumber_Type.__name__ = "Integer32"
_TeraInstallSlotNumber_Object = MibTableColumn
teraInstallSlotNumber = _TeraInstallSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 1),
    _TeraInstallSlotNumber_Type()
)
teraInstallSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraInstallSlotNumber.setStatus("mandatory")


class _TeraInstallUnitType_Type(Integer32):
    """Custom type teraInstallUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5000),
    )


_TeraInstallUnitType_Type.__name__ = "Integer32"
_TeraInstallUnitType_Object = MibTableColumn
teraInstallUnitType = _TeraInstallUnitType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 2),
    _TeraInstallUnitType_Type()
)
teraInstallUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraInstallUnitType.setStatus("mandatory")
_TeraInstallEquippedUnitType_Type = Integer32
_TeraInstallEquippedUnitType_Object = MibTableColumn
teraInstallEquippedUnitType = _TeraInstallEquippedUnitType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 3),
    _TeraInstallEquippedUnitType_Type()
)
teraInstallEquippedUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraInstallEquippedUnitType.setStatus("mandatory")


class _TeraInstallUnitAdminStatus_Type(Integer32):
    """Custom type teraInstallUnitAdminStatus based on Integer32"""
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
        *(("is", 3),
          ("moos", 4),
          ("moos-trunk", 7),
          ("none", 2),
          ("provision", 1),
          ("reset", 5),
          ("trunk", 6))
    )


_TeraInstallUnitAdminStatus_Type.__name__ = "Integer32"
_TeraInstallUnitAdminStatus_Object = MibTableColumn
teraInstallUnitAdminStatus = _TeraInstallUnitAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 4),
    _TeraInstallUnitAdminStatus_Type()
)
teraInstallUnitAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraInstallUnitAdminStatus.setStatus("mandatory")


class _TeraInstallUnitOperStatus_Type(Integer32):
    """Custom type teraInstallUnitOperStatus based on Integer32"""
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
        *(("empty", 1),
          ("init", 8),
          ("is", 2),
          ("mismatch", 6),
          ("moos", 3),
          ("oos", 7),
          ("removed", 4),
          ("unprovisioned", 5))
    )


_TeraInstallUnitOperStatus_Type.__name__ = "Integer32"
_TeraInstallUnitOperStatus_Object = MibTableColumn
teraInstallUnitOperStatus = _TeraInstallUnitOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 5),
    _TeraInstallUnitOperStatus_Type()
)
teraInstallUnitOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraInstallUnitOperStatus.setStatus("mandatory")
_TeraInstallUnitName_Type = OctetString
_TeraInstallUnitName_Object = MibTableColumn
teraInstallUnitName = _TeraInstallUnitName_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 6),
    _TeraInstallUnitName_Type()
)
teraInstallUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraInstallUnitName.setStatus("mandatory")
_TeraInstallUnitRevision_Type = OctetString
_TeraInstallUnitRevision_Object = MibTableColumn
teraInstallUnitRevision = _TeraInstallUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 7),
    _TeraInstallUnitRevision_Type()
)
teraInstallUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraInstallUnitRevision.setStatus("mandatory")
_TeraInstallUnitSerial_Type = Integer32
_TeraInstallUnitSerial_Object = MibTableColumn
teraInstallUnitSerial = _TeraInstallUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 8),
    _TeraInstallUnitSerial_Type()
)
teraInstallUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraInstallUnitSerial.setStatus("mandatory")
_TeraInstallUnitSWVersion_Type = Integer32
_TeraInstallUnitSWVersion_Object = MibTableColumn
teraInstallUnitSWVersion = _TeraInstallUnitSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 9),
    _TeraInstallUnitSWVersion_Type()
)
teraInstallUnitSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraInstallUnitSWVersion.setStatus("mandatory")
_TeraInstallUnitMfgData_Type = OctetString
_TeraInstallUnitMfgData_Object = MibTableColumn
teraInstallUnitMfgData = _TeraInstallUnitMfgData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 1, 1, 10),
    _TeraInstallUnitMfgData_Type()
)
teraInstallUnitMfgData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraInstallUnitMfgData.setStatus("mandatory")
_TeraSystemInstallTable_Object = MibTable
teraSystemInstallTable = _TeraSystemInstallTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2)
)
if mibBuilder.loadTexts:
    teraSystemInstallTable.setStatus("mandatory")
_TeraSystemInstallTableEntry_Object = MibTableRow
teraSystemInstallTableEntry = _TeraSystemInstallTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1)
)
teraSystemInstallTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-terasystem-MIB", "teraPonIndex"),
)
if mibBuilder.loadTexts:
    teraSystemInstallTableEntry.setStatus("mandatory")


class _TeraSystemNEProvisionAdminStatus_Type(Integer32):
    """Custom type teraSystemNEProvisionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("provision", 1))
    )


_TeraSystemNEProvisionAdminStatus_Type.__name__ = "Integer32"
_TeraSystemNEProvisionAdminStatus_Object = MibTableColumn
teraSystemNEProvisionAdminStatus = _TeraSystemNEProvisionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 1),
    _TeraSystemNEProvisionAdminStatus_Type()
)
teraSystemNEProvisionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNEProvisionAdminStatus.setStatus("mandatory")
_TeraSystemNEName_Type = OctetString
_TeraSystemNEName_Object = MibTableColumn
teraSystemNEName = _TeraSystemNEName_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 2),
    _TeraSystemNEName_Type()
)
teraSystemNEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSystemNEName.setStatus("mandatory")
_TeraSystemNERangingCode_Type = OctetString
_TeraSystemNERangingCode_Object = MibTableColumn
teraSystemNERangingCode = _TeraSystemNERangingCode_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 3),
    _TeraSystemNERangingCode_Type()
)
teraSystemNERangingCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNERangingCode.setStatus("mandatory")


class _TeraSystemNEType_Type(Integer32):
    """Custom type teraSystemNEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("oat", 7),
          ("tw100", 4),
          ("tw150RT", 5),
          ("tw1600", 3),
          ("tw300", 1),
          ("tw600", 2),
          ("unknown", 0))
    )


_TeraSystemNEType_Type.__name__ = "Integer32"
_TeraSystemNEType_Object = MibTableColumn
teraSystemNEType = _TeraSystemNEType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 4),
    _TeraSystemNEType_Type()
)
teraSystemNEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSystemNEType.setStatus("mandatory")


class _TeraSystemNEMaxLatency_Type(Integer32):
    """Custom type teraSystemNEMaxLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 60),
    )


_TeraSystemNEMaxLatency_Type.__name__ = "Integer32"
_TeraSystemNEMaxLatency_Object = MibTableColumn
teraSystemNEMaxLatency = _TeraSystemNEMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 5),
    _TeraSystemNEMaxLatency_Type()
)
teraSystemNEMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNEMaxLatency.setStatus("mandatory")


class _TeraSystemNEAponMaxLength_Type(Integer32):
    """Custom type teraSystemNEAponMaxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TeraSystemNEAponMaxLength_Type.__name__ = "Integer32"
_TeraSystemNEAponMaxLength_Object = MibTableColumn
teraSystemNEAponMaxLength = _TeraSystemNEAponMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 6),
    _TeraSystemNEAponMaxLength_Type()
)
teraSystemNEAponMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNEAponMaxLength.setStatus("mandatory")


class _TeraSystemNEOperStatus_Type(Integer32):
    """Custom type teraSystemNEOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("linkDown", 3),
          ("provisioned", 2))
    )


_TeraSystemNEOperStatus_Type.__name__ = "Integer32"
_TeraSystemNEOperStatus_Object = MibTableColumn
teraSystemNEOperStatus = _TeraSystemNEOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 7),
    _TeraSystemNEOperStatus_Type()
)
teraSystemNEOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSystemNEOperStatus.setStatus("mandatory")


class _TeraSystemNEEocMinBandWidth_Type(Integer32):
    """Custom type teraSystemNEEocMinBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1536),
    )


_TeraSystemNEEocMinBandWidth_Type.__name__ = "Integer32"
_TeraSystemNEEocMinBandWidth_Object = MibTableColumn
teraSystemNEEocMinBandWidth = _TeraSystemNEEocMinBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 8),
    _TeraSystemNEEocMinBandWidth_Type()
)
teraSystemNEEocMinBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNEEocMinBandWidth.setStatus("mandatory")


class _TeraSystemNEEocMaxBandWidth_Type(Integer32):
    """Custom type teraSystemNEEocMaxBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1536),
    )


_TeraSystemNEEocMaxBandWidth_Type.__name__ = "Integer32"
_TeraSystemNEEocMaxBandWidth_Object = MibTableColumn
teraSystemNEEocMaxBandWidth = _TeraSystemNEEocMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 9),
    _TeraSystemNEEocMaxBandWidth_Type()
)
teraSystemNEEocMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNEEocMaxBandWidth.setStatus("mandatory")


class _TeraSystemNEInventoryOverride_Type(Integer32):
    """Custom type teraSystemNEInventoryOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("olt2ont", 1),
          ("ont2olt", 2))
    )


_TeraSystemNEInventoryOverride_Type.__name__ = "Integer32"
_TeraSystemNEInventoryOverride_Object = MibTableColumn
teraSystemNEInventoryOverride = _TeraSystemNEInventoryOverride_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 10),
    _TeraSystemNEInventoryOverride_Type()
)
teraSystemNEInventoryOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNEInventoryOverride.setStatus("mandatory")


class _TeraSystemNERanging_Type(Integer32):
    """Custom type teraSystemNERanging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_TeraSystemNERanging_Type.__name__ = "Integer32"
_TeraSystemNERanging_Object = MibTableColumn
teraSystemNERanging = _TeraSystemNERanging_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 11),
    _TeraSystemNERanging_Type()
)
teraSystemNERanging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNERanging.setStatus("mandatory")


class _TeraSystemNECurrentDistance_Type(Integer32):
    """Custom type teraSystemNECurrentDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TeraSystemNECurrentDistance_Type.__name__ = "Integer32"
_TeraSystemNECurrentDistance_Object = MibTableColumn
teraSystemNECurrentDistance = _TeraSystemNECurrentDistance_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 2, 1, 12),
    _TeraSystemNECurrentDistance_Type()
)
teraSystemNECurrentDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSystemNECurrentDistance.setStatus("mandatory")
_TeraNEInfoTableGroup_ObjectIdentity = ObjectIdentity
teraNEInfoTableGroup = _TeraNEInfoTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 3)
)
_TeraNEInfoTable_ObjectIdentity = ObjectIdentity
teraNEInfoTable = _TeraNEInfoTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 3, 1)
)
_TeraNERangingCode_Type = OctetString
_TeraNERangingCode_Object = MibScalar
teraNERangingCode = _TeraNERangingCode_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 3, 1, 1),
    _TeraNERangingCode_Type()
)
teraNERangingCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraNERangingCode.setStatus("mandatory")


class _TeraNEType_Type(Integer32):
    """Custom type teraNEType based on Integer32"""
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
        *(("oat", 7),
          ("tw100", 4),
          ("tw150RT-ATM", 5),
          ("tw150RT-TDM", 6),
          ("tw1600", 3),
          ("tw300", 1),
          ("tw600", 2),
          ("unknown", 0))
    )


_TeraNEType_Type.__name__ = "Integer32"
_TeraNEType_Object = MibScalar
teraNEType = _TeraNEType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 3, 1, 2),
    _TeraNEType_Type()
)
teraNEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraNEType.setStatus("mandatory")
_TeraNEModel_Type = OctetString
_TeraNEModel_Object = MibScalar
teraNEModel = _TeraNEModel_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 3, 1, 3),
    _TeraNEModel_Type()
)
teraNEModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraNEModel.setStatus("mandatory")
_TeraNESWVersion_Type = OctetString
_TeraNESWVersion_Object = MibScalar
teraNESWVersion = _TeraNESWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 3, 1, 4),
    _TeraNESWVersion_Type()
)
teraNESWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraNESWVersion.setStatus("mandatory")
_TeraNESWRevision_Type = OctetString
_TeraNESWRevision_Object = MibScalar
teraNESWRevision = _TeraNESWRevision_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 3, 3, 1, 5),
    _TeraNESWRevision_Type()
)
teraNESWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraNESWRevision.setStatus("mandatory")
_TeraClockSyncTable_ObjectIdentity = ObjectIdentity
teraClockSyncTable = _TeraClockSyncTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4)
)


class _TeraClockSyncPrimarySource_Type(Integer32):
    """Custom type teraClockSyncPrimarySource based on Integer32"""
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
        *(("bits-A", 1),
          ("freerun", 3),
          ("holdover", 4),
          ("nim", 2))
    )


_TeraClockSyncPrimarySource_Type.__name__ = "Integer32"
_TeraClockSyncPrimarySource_Object = MibScalar
teraClockSyncPrimarySource = _TeraClockSyncPrimarySource_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 1),
    _TeraClockSyncPrimarySource_Type()
)
teraClockSyncPrimarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncPrimarySource.setStatus("mandatory")


class _TeraClockSyncPrimaryNIMSlot_Type(Integer32):
    """Custom type teraClockSyncPrimaryNIMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TeraClockSyncPrimaryNIMSlot_Type.__name__ = "Integer32"
_TeraClockSyncPrimaryNIMSlot_Object = MibScalar
teraClockSyncPrimaryNIMSlot = _TeraClockSyncPrimaryNIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 2),
    _TeraClockSyncPrimaryNIMSlot_Type()
)
teraClockSyncPrimaryNIMSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncPrimaryNIMSlot.setStatus("mandatory")
_TeraClockSyncPrimaryNIMIfIndex_Type = Integer32
_TeraClockSyncPrimaryNIMIfIndex_Object = MibScalar
teraClockSyncPrimaryNIMIfIndex = _TeraClockSyncPrimaryNIMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 3),
    _TeraClockSyncPrimaryNIMIfIndex_Type()
)
teraClockSyncPrimaryNIMIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncPrimaryNIMIfIndex.setStatus("mandatory")


class _TeraClockSyncSecondarySource_Type(Integer32):
    """Custom type teraClockSyncSecondarySource based on Integer32"""
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
        *(("bits-B", 1),
          ("freerun", 3),
          ("holdover", 4),
          ("nim", 2))
    )


_TeraClockSyncSecondarySource_Type.__name__ = "Integer32"
_TeraClockSyncSecondarySource_Object = MibScalar
teraClockSyncSecondarySource = _TeraClockSyncSecondarySource_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 4),
    _TeraClockSyncSecondarySource_Type()
)
teraClockSyncSecondarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncSecondarySource.setStatus("mandatory")


class _TeraClockSyncSecondaryNIMSlot_Type(Integer32):
    """Custom type teraClockSyncSecondaryNIMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TeraClockSyncSecondaryNIMSlot_Type.__name__ = "Integer32"
_TeraClockSyncSecondaryNIMSlot_Object = MibScalar
teraClockSyncSecondaryNIMSlot = _TeraClockSyncSecondaryNIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 5),
    _TeraClockSyncSecondaryNIMSlot_Type()
)
teraClockSyncSecondaryNIMSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncSecondaryNIMSlot.setStatus("mandatory")
_TeraClockSyncSecondaryNIMIfIndex_Type = Integer32
_TeraClockSyncSecondaryNIMIfIndex_Object = MibScalar
teraClockSyncSecondaryNIMIfIndex = _TeraClockSyncSecondaryNIMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 6),
    _TeraClockSyncSecondaryNIMIfIndex_Type()
)
teraClockSyncSecondaryNIMIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncSecondaryNIMIfIndex.setStatus("mandatory")


class _TeraClockSyncLastSource_Type(Integer32):
    """Custom type teraClockSyncLastSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 1),
          ("holdover", 2))
    )


_TeraClockSyncLastSource_Type.__name__ = "Integer32"
_TeraClockSyncLastSource_Object = MibScalar
teraClockSyncLastSource = _TeraClockSyncLastSource_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 7),
    _TeraClockSyncLastSource_Type()
)
teraClockSyncLastSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncLastSource.setStatus("mandatory")


class _TeraClockSyncRevertive_Type(Integer32):
    """Custom type teraClockSyncRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_TeraClockSyncRevertive_Type.__name__ = "Integer32"
_TeraClockSyncRevertive_Object = MibScalar
teraClockSyncRevertive = _TeraClockSyncRevertive_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 8),
    _TeraClockSyncRevertive_Type()
)
teraClockSyncRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncRevertive.setStatus("mandatory")


class _TeraClockSyncActiveSource_Type(Integer32):
    """Custom type teraClockSyncActiveSource based on Integer32"""
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
        *(("bits-A", 1),
          ("bits-B", 2),
          ("freerun", 4),
          ("holdover", 5),
          ("nim", 3))
    )


_TeraClockSyncActiveSource_Type.__name__ = "Integer32"
_TeraClockSyncActiveSource_Object = MibScalar
teraClockSyncActiveSource = _TeraClockSyncActiveSource_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 9),
    _TeraClockSyncActiveSource_Type()
)
teraClockSyncActiveSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraClockSyncActiveSource.setStatus("mandatory")


class _TeraClockSyncActiveNIMSlot_Type(Integer32):
    """Custom type teraClockSyncActiveNIMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TeraClockSyncActiveNIMSlot_Type.__name__ = "Integer32"
_TeraClockSyncActiveNIMSlot_Object = MibScalar
teraClockSyncActiveNIMSlot = _TeraClockSyncActiveNIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 10),
    _TeraClockSyncActiveNIMSlot_Type()
)
teraClockSyncActiveNIMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraClockSyncActiveNIMSlot.setStatus("mandatory")
_TeraClockSyncActiveNIMIfIndex_Type = Integer32
_TeraClockSyncActiveNIMIfIndex_Object = MibScalar
teraClockSyncActiveNIMIfIndex = _TeraClockSyncActiveNIMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 11),
    _TeraClockSyncActiveNIMIfIndex_Type()
)
teraClockSyncActiveNIMIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraClockSyncActiveNIMIfIndex.setStatus("mandatory")


class _TeraClockSyncActiveStatus_Type(Integer32):
    """Custom type teraClockSyncActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_TeraClockSyncActiveStatus_Type.__name__ = "Integer32"
_TeraClockSyncActiveStatus_Object = MibScalar
teraClockSyncActiveStatus = _TeraClockSyncActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 12),
    _TeraClockSyncActiveStatus_Type()
)
teraClockSyncActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraClockSyncActiveStatus.setStatus("mandatory")


class _TeraClockSyncPrimaryStatus_Type(Integer32):
    """Custom type teraClockSyncPrimaryStatus based on Integer32"""
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
        *(("active", 1),
          ("fail", 3),
          ("idle", 2),
          ("oos", 4))
    )


_TeraClockSyncPrimaryStatus_Type.__name__ = "Integer32"
_TeraClockSyncPrimaryStatus_Object = MibScalar
teraClockSyncPrimaryStatus = _TeraClockSyncPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 13),
    _TeraClockSyncPrimaryStatus_Type()
)
teraClockSyncPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraClockSyncPrimaryStatus.setStatus("mandatory")


class _TeraClockSyncSecondaryStatus_Type(Integer32):
    """Custom type teraClockSyncSecondaryStatus based on Integer32"""
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
        *(("active", 1),
          ("fail", 3),
          ("idle", 2),
          ("oos", 4))
    )


_TeraClockSyncSecondaryStatus_Type.__name__ = "Integer32"
_TeraClockSyncSecondaryStatus_Object = MibScalar
teraClockSyncSecondaryStatus = _TeraClockSyncSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 14),
    _TeraClockSyncSecondaryStatus_Type()
)
teraClockSyncSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraClockSyncSecondaryStatus.setStatus("mandatory")


class _TeraClockSyncOperStatus_Type(Integer32):
    """Custom type teraClockSyncOperStatus based on Integer32"""
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
        *(("configure", 1),
          ("switchToFreerun", 5),
          ("switchToHoldover", 4),
          ("switchToPrimary", 2),
          ("switchToSecondary", 3))
    )


_TeraClockSyncOperStatus_Type.__name__ = "Integer32"
_TeraClockSyncOperStatus_Object = MibScalar
teraClockSyncOperStatus = _TeraClockSyncOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 4, 15),
    _TeraClockSyncOperStatus_Type()
)
teraClockSyncOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraClockSyncOperStatus.setStatus("mandatory")
_TeraCommunityGroupTable_ObjectIdentity = ObjectIdentity
teraCommunityGroupTable = _TeraCommunityGroupTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 5)
)
_TeraPublicCommunity_Type = OctetString
_TeraPublicCommunity_Object = MibScalar
teraPublicCommunity = _TeraPublicCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 5, 1),
    _TeraPublicCommunity_Type()
)
teraPublicCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraPublicCommunity.setStatus("mandatory")
_TeraSETCommunity_Type = OctetString
_TeraSETCommunity_Object = MibScalar
teraSETCommunity = _TeraSETCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 5, 2),
    _TeraSETCommunity_Type()
)
teraSETCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSETCommunity.setStatus("mandatory")
_TeraGETCommunity_Type = OctetString
_TeraGETCommunity_Object = MibScalar
teraGETCommunity = _TeraGETCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 5, 3),
    _TeraGETCommunity_Type()
)
teraGETCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraGETCommunity.setStatus("mandatory")
_TeraAdminCommunity_Type = OctetString
_TeraAdminCommunity_Object = MibScalar
teraAdminCommunity = _TeraAdminCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 5, 4),
    _TeraAdminCommunity_Type()
)
teraAdminCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAdminCommunity.setStatus("mandatory")
_TeraTestCommunity_Type = OctetString
_TeraTestCommunity_Object = MibScalar
teraTestCommunity = _TeraTestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 5, 5),
    _TeraTestCommunity_Type()
)
teraTestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraTestCommunity.setStatus("mandatory")
_TeraMasterSlaveTable_ObjectIdentity = ObjectIdentity
teraMasterSlaveTable = _TeraMasterSlaveTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 6)
)


class _TeraMasterSlotNumber_Type(Integer32):
    """Custom type teraMasterSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraMasterSlotNumber_Type.__name__ = "Integer32"
_TeraMasterSlotNumber_Object = MibScalar
teraMasterSlotNumber = _TeraMasterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 6, 1),
    _TeraMasterSlotNumber_Type()
)
teraMasterSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraMasterSlotNumber.setStatus("mandatory")


class _TeraSlaveSlotNumber_Type(Integer32):
    """Custom type teraSlaveSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraSlaveSlotNumber_Type.__name__ = "Integer32"
_TeraSlaveSlotNumber_Object = MibScalar
teraSlaveSlotNumber = _TeraSlaveSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 6, 2),
    _TeraSlaveSlotNumber_Type()
)
teraSlaveSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSlaveSlotNumber.setStatus("mandatory")
_TeraSystemIPGroupTable_ObjectIdentity = ObjectIdentity
teraSystemIPGroupTable = _TeraSystemIPGroupTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 7)
)
_TeraSystemIPAddress_Type = IpAddress
_TeraSystemIPAddress_Object = MibScalar
teraSystemIPAddress = _TeraSystemIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 7, 1),
    _TeraSystemIPAddress_Type()
)
teraSystemIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemIPAddress.setStatus("mandatory")
_TeraSystemIPNetMask_Type = IpAddress
_TeraSystemIPNetMask_Object = MibScalar
teraSystemIPNetMask = _TeraSystemIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 7, 2),
    _TeraSystemIPNetMask_Type()
)
teraSystemIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemIPNetMask.setStatus("mandatory")
_TeraSystemIPGateway_Type = IpAddress
_TeraSystemIPGateway_Object = MibScalar
teraSystemIPGateway = _TeraSystemIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 7, 3),
    _TeraSystemIPGateway_Type()
)
teraSystemIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemIPGateway.setStatus("mandatory")
_TeraLogGroup_ObjectIdentity = ObjectIdentity
teraLogGroup = _TeraLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8)
)
_TeraLogNumberTable_Object = MibTable
teraLogNumberTable = _TeraLogNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 1)
)
if mibBuilder.loadTexts:
    teraLogNumberTable.setStatus("mandatory")
_TeraLogNumberTableEntry_Object = MibTableRow
teraLogNumberTableEntry = _TeraLogNumberTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 1, 1)
)
teraLogNumberTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraLogNumber"),
)
if mibBuilder.loadTexts:
    teraLogNumberTableEntry.setStatus("mandatory")
_TeraLogNumber_Type = Integer32
_TeraLogNumber_Object = MibTableColumn
teraLogNumber = _TeraLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 1, 1, 1),
    _TeraLogNumber_Type()
)
teraLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLogNumber.setStatus("mandatory")
_TeraLogNumberDescr_Type = OctetString
_TeraLogNumberDescr_Object = MibTableColumn
teraLogNumberDescr = _TeraLogNumberDescr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 1, 1, 2),
    _TeraLogNumberDescr_Type()
)
teraLogNumberDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLogNumberDescr.setStatus("mandatory")


class _TeraLogNumberStatus_Type(Integer32):
    """Custom type teraLogNumberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraLogNumberStatus_Type.__name__ = "Integer32"
_TeraLogNumberStatus_Object = MibTableColumn
teraLogNumberStatus = _TeraLogNumberStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 1, 1, 3),
    _TeraLogNumberStatus_Type()
)
teraLogNumberStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLogNumberStatus.setStatus("mandatory")


class _TeraLogClear_Type(Integer32):
    """Custom type teraLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraLogClear_Type.__name__ = "Integer32"
_TeraLogClear_Object = MibScalar
teraLogClear = _TeraLogClear_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 2),
    _TeraLogClear_Type()
)
teraLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLogClear.setStatus("mandatory")
_TeraLogTable_Object = MibTable
teraLogTable = _TeraLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3)
)
if mibBuilder.loadTexts:
    teraLogTable.setStatus("mandatory")
_TeraLogTableEntry_Object = MibTableRow
teraLogTableEntry = _TeraLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 4)
)
teraLogTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-terasystem-MIB", "teraLogNumber"),
    (0, "TERAWAVE-terasystem-MIB", "teraLogMsgIndex"),
)
if mibBuilder.loadTexts:
    teraLogTableEntry.setStatus("mandatory")
_TeraLogMsgIndex_Type = Integer32
_TeraLogMsgIndex_Object = MibTableColumn
teraLogMsgIndex = _TeraLogMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 4, 1),
    _TeraLogMsgIndex_Type()
)
teraLogMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLogMsgIndex.setStatus("mandatory")
_TeraLogMsgNumber_Type = Integer32
_TeraLogMsgNumber_Object = MibTableColumn
teraLogMsgNumber = _TeraLogMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 4, 2),
    _TeraLogMsgNumber_Type()
)
teraLogMsgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLogMsgNumber.setStatus("mandatory")
_TeraLogNumberOfParams_Type = Integer32
_TeraLogNumberOfParams_Object = MibTableColumn
teraLogNumberOfParams = _TeraLogNumberOfParams_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 4, 3),
    _TeraLogNumberOfParams_Type()
)
teraLogNumberOfParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLogNumberOfParams.setStatus("mandatory")
_TeraLogParams_Type = OctetString
_TeraLogParams_Object = MibTableColumn
teraLogParams = _TeraLogParams_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 4, 4),
    _TeraLogParams_Type()
)
teraLogParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLogParams.setStatus("mandatory")


class _TeraLogStatus_Type(Integer32):
    """Custom type teraLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraLogStatus_Type.__name__ = "Integer32"
_TeraLogStatus_Object = MibTableColumn
teraLogStatus = _TeraLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 4, 5),
    _TeraLogStatus_Type()
)
teraLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLogStatus.setStatus("mandatory")
_TeraAllLogsFilterGroup_Object = MibTable
teraAllLogsFilterGroup = _TeraAllLogsFilterGroup_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 5)
)
if mibBuilder.loadTexts:
    teraAllLogsFilterGroup.setStatus("mandatory")
_TeraAllLogsFilterGroupEntry_Object = MibTableRow
teraAllLogsFilterGroupEntry = _TeraAllLogsFilterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 5, 1)
)
teraAllLogsFilterGroupEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraLogNumber"),
)
if mibBuilder.loadTexts:
    teraAllLogsFilterGroupEntry.setStatus("mandatory")
_TeraLogFilterByNumber_Type = Integer32
_TeraLogFilterByNumber_Object = MibTableColumn
teraLogFilterByNumber = _TeraLogFilterByNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 5, 1, 1),
    _TeraLogFilterByNumber_Type()
)
teraLogFilterByNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLogFilterByNumber.setStatus("mandatory")


class _TeraLogFilterBySize_Type(Integer32):
    """Custom type teraLogFilterBySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("last20", 2))
    )


_TeraLogFilterBySize_Type.__name__ = "Integer32"
_TeraLogFilterBySize_Object = MibTableColumn
teraLogFilterBySize = _TeraLogFilterBySize_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 5, 1, 2),
    _TeraLogFilterBySize_Type()
)
teraLogFilterBySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLogFilterBySize.setStatus("mandatory")


class _TeraLogFilterBySeverity_Type(Integer32):
    """Custom type teraLogFilterBySeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("major", 3),
          ("minor", 2),
          ("nominal", 1))
    )


_TeraLogFilterBySeverity_Type.__name__ = "Integer32"
_TeraLogFilterBySeverity_Object = MibTableColumn
teraLogFilterBySeverity = _TeraLogFilterBySeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 5, 1, 3),
    _TeraLogFilterBySeverity_Type()
)
teraLogFilterBySeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLogFilterBySeverity.setStatus("mandatory")
_TeraLogFilterByTask_Type = OctetString
_TeraLogFilterByTask_Object = MibTableColumn
teraLogFilterByTask = _TeraLogFilterByTask_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 8, 3, 5, 1, 4),
    _TeraLogFilterByTask_Type()
)
teraLogFilterByTask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLogFilterByTask.setStatus("mandatory")
_TeraNESlotTable_Object = MibTable
teraNESlotTable = _TeraNESlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 9)
)
if mibBuilder.loadTexts:
    teraNESlotTable.setStatus("mandatory")
_TeraNESlotTableEntry_Object = MibTableRow
teraNESlotTableEntry = _TeraNESlotTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 9, 1)
)
teraNESlotTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-terasystem-MIB", "teraPonIndex"),
    (0, "TERAWAVE-terasystem-MIB", "teraEventSlot"),
)
if mibBuilder.loadTexts:
    teraNESlotTableEntry.setStatus("mandatory")


class _TeraNESlotUnitType_Type(Integer32):
    """Custom type teraNESlotUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_TeraNESlotUnitType_Type.__name__ = "Integer32"
_TeraNESlotUnitType_Object = MibTableColumn
teraNESlotUnitType = _TeraNESlotUnitType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 9, 1, 1),
    _TeraNESlotUnitType_Type()
)
teraNESlotUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraNESlotUnitType.setStatus("mandatory")


class _TeraNESlotUnitAdminStatus_Type(Integer32):
    """Custom type teraNESlotUnitAdminStatus based on Integer32"""
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
        *(("is", 3),
          ("moos", 4),
          ("none", 2),
          ("provision", 1),
          ("reset", 5),
          ("trunk", 6))
    )


_TeraNESlotUnitAdminStatus_Type.__name__ = "Integer32"
_TeraNESlotUnitAdminStatus_Object = MibTableColumn
teraNESlotUnitAdminStatus = _TeraNESlotUnitAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 9, 1, 2),
    _TeraNESlotUnitAdminStatus_Type()
)
teraNESlotUnitAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraNESlotUnitAdminStatus.setStatus("mandatory")
_TeraWLinkIPTable_Object = MibTable
teraWLinkIPTable = _TeraWLinkIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 10)
)
if mibBuilder.loadTexts:
    teraWLinkIPTable.setStatus("mandatory")
_TeraWLinkIPTableEntry_Object = MibTableRow
teraWLinkIPTableEntry = _TeraWLinkIPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 10, 1)
)
teraWLinkIPTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-terasystem-MIB", "teraPonIndex"),
)
if mibBuilder.loadTexts:
    teraWLinkIPTableEntry.setStatus("mandatory")
_TeraWLinkIPAddress_Type = IpAddress
_TeraWLinkIPAddress_Object = MibTableColumn
teraWLinkIPAddress = _TeraWLinkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 10, 1, 1),
    _TeraWLinkIPAddress_Type()
)
teraWLinkIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraWLinkIPAddress.setStatus("mandatory")
_TeraWLinkIPNetMask_Type = IpAddress
_TeraWLinkIPNetMask_Object = MibTableColumn
teraWLinkIPNetMask = _TeraWLinkIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 10, 1, 2),
    _TeraWLinkIPNetMask_Type()
)
teraWLinkIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraWLinkIPNetMask.setStatus("mandatory")
_TeraWLinkIPGateway_Type = IpAddress
_TeraWLinkIPGateway_Object = MibTableColumn
teraWLinkIPGateway = _TeraWLinkIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 10, 1, 3),
    _TeraWLinkIPGateway_Type()
)
teraWLinkIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraWLinkIPGateway.setStatus("mandatory")


class _TeraWLinkIPStatus_Type(Integer32):
    """Custom type teraWLinkIPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("set", 1))
    )


_TeraWLinkIPStatus_Type.__name__ = "Integer32"
_TeraWLinkIPStatus_Object = MibTableColumn
teraWLinkIPStatus = _TeraWLinkIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 10, 1, 4),
    _TeraWLinkIPStatus_Type()
)
teraWLinkIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraWLinkIPStatus.setStatus("mandatory")
_TeraNEMiscTableGroup_ObjectIdentity = ObjectIdentity
teraNEMiscTableGroup = _TeraNEMiscTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 11)
)
_TeraNEMiscTable_ObjectIdentity = ObjectIdentity
teraNEMiscTable = _TeraNEMiscTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 11, 1)
)


class _TeraNELevel2Slot_Type(Integer32):
    """Custom type teraNELevel2Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TeraNELevel2Slot_Type.__name__ = "Integer32"
_TeraNELevel2Slot_Object = MibScalar
teraNELevel2Slot = _TeraNELevel2Slot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 11, 1, 1),
    _TeraNELevel2Slot_Type()
)
teraNELevel2Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraNELevel2Slot.setStatus("mandatory")


class _TeraNEZipSystem_Type(Integer32):
    """Custom type teraNEZipSystem based on Integer32"""
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
        *(("no", 1),
          ("zip-active", 2),
          ("zip-all", 4),
          ("zip-stby", 3))
    )


_TeraNEZipSystem_Type.__name__ = "Integer32"
_TeraNEZipSystem_Object = MibScalar
teraNEZipSystem = _TeraNEZipSystem_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 11, 1, 2),
    _TeraNEZipSystem_Type()
)
teraNEZipSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraNEZipSystem.setStatus("mandatory")


class _TeraNEReset_Type(Integer32):
    """Custom type teraNEReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("reset", 2))
    )


_TeraNEReset_Type.__name__ = "Integer32"
_TeraNEReset_Object = MibScalar
teraNEReset = _TeraNEReset_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 11, 1, 3),
    _TeraNEReset_Type()
)
teraNEReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraNEReset.setStatus("mandatory")
_TeraNETimeZone_Type = OctetString
_TeraNETimeZone_Object = MibScalar
teraNETimeZone = _TeraNETimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 11, 1, 4),
    _TeraNETimeZone_Type()
)
teraNETimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraNETimeZone.setStatus("mandatory")


class _TeraNEInventoryOverride_Type(Integer32):
    """Custom type teraNEInventoryOverride based on Integer32"""
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


_TeraNEInventoryOverride_Type.__name__ = "Integer32"
_TeraNEInventoryOverride_Object = MibScalar
teraNEInventoryOverride = _TeraNEInventoryOverride_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 11, 1, 5),
    _TeraNEInventoryOverride_Type()
)
teraNEInventoryOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraNEInventoryOverride.setStatus("mandatory")


class _TeraNESerialPortType_Type(Integer32):
    """Custom type teraNESerialPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dbshell", 2),
          ("ppp", 1))
    )


_TeraNESerialPortType_Type.__name__ = "Integer32"
_TeraNESerialPortType_Object = MibScalar
teraNESerialPortType = _TeraNESerialPortType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 11, 1, 6),
    _TeraNESerialPortType_Type()
)
teraNESerialPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraNESerialPortType.setStatus("mandatory")
_TeraSysObjectIdTable_ObjectIdentity = ObjectIdentity
teraSysObjectIdTable = _TeraSysObjectIdTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 12)
)
_TeraTW300_Type = ObjectIdentifier
_TeraTW300_Object = MibScalar
teraTW300 = _TeraTW300_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 12, 1),
    _TeraTW300_Type()
)
teraTW300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTW300.setStatus("mandatory")
_TeraTW600_Type = ObjectIdentifier
_TeraTW600_Object = MibScalar
teraTW600 = _TeraTW600_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 12, 2),
    _TeraTW600_Type()
)
teraTW600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTW600.setStatus("mandatory")
_TeraTW1600_Type = ObjectIdentifier
_TeraTW1600_Object = MibScalar
teraTW1600 = _TeraTW1600_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 12, 3),
    _TeraTW1600_Type()
)
teraTW1600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTW1600.setStatus("mandatory")
_TeraTW100_Type = ObjectIdentifier
_TeraTW100_Object = MibScalar
teraTW100 = _TeraTW100_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 12, 4),
    _TeraTW100_Type()
)
teraTW100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTW100.setStatus("mandatory")
_TeraTW150RTATM_Type = ObjectIdentifier
_TeraTW150RTATM_Object = MibScalar
teraTW150RTATM = _TeraTW150RTATM_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 12, 5),
    _TeraTW150RTATM_Type()
)
teraTW150RTATM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTW150RTATM.setStatus("mandatory")
_TeraTW150RTTDM_Type = ObjectIdentifier
_TeraTW150RTTDM_Object = MibScalar
teraTW150RTTDM = _TeraTW150RTTDM_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 12, 6),
    _TeraTW150RTTDM_Type()
)
teraTW150RTTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraTW150RTTDM.setStatus("mandatory")
_TeraOAT_Type = ObjectIdentifier
_TeraOAT_Object = MibScalar
teraOAT = _TeraOAT_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 12, 7),
    _TeraOAT_Type()
)
teraOAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOAT.setStatus("mandatory")
_TeraNEIDxTable_Object = MibTable
teraNEIDxTable = _TeraNEIDxTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 13)
)
if mibBuilder.loadTexts:
    teraNEIDxTable.setStatus("mandatory")
_TeraNEIDxTableEntry_Object = MibTableRow
teraNEIDxTableEntry = _TeraNEIDxTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 13, 1)
)
teraNEIDxTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraNEIDxTableEntry.setStatus("mandatory")


class _TeraNEIDxSlotLevel1_Type(Integer32):
    """Custom type teraNEIDxSlotLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TeraNEIDxSlotLevel1_Type.__name__ = "Integer32"
_TeraNEIDxSlotLevel1_Object = MibTableColumn
teraNEIDxSlotLevel1 = _TeraNEIDxSlotLevel1_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 13, 1, 1),
    _TeraNEIDxSlotLevel1_Type()
)
teraNEIDxSlotLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraNEIDxSlotLevel1.setStatus("mandatory")


class _TeraNEIDxPonID_Type(Integer32):
    """Custom type teraNEIDxPonID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TeraNEIDxPonID_Type.__name__ = "Integer32"
_TeraNEIDxPonID_Object = MibTableColumn
teraNEIDxPonID = _TeraNEIDxPonID_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 13, 1, 2),
    _TeraNEIDxPonID_Type()
)
teraNEIDxPonID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraNEIDxPonID.setStatus("mandatory")
_TeraWLinkIPRangeTable_Object = MibTable
teraWLinkIPRangeTable = _TeraWLinkIPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 14)
)
if mibBuilder.loadTexts:
    teraWLinkIPRangeTable.setStatus("mandatory")
_TeraWLinkIPRangeTableEntry_Object = MibTableRow
teraWLinkIPRangeTableEntry = _TeraWLinkIPRangeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 14, 1)
)
teraWLinkIPRangeTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraWLinkIPRangeTableEntry.setStatus("mandatory")
_TeraWLinkIPRangeStart_Type = IpAddress
_TeraWLinkIPRangeStart_Object = MibTableColumn
teraWLinkIPRangeStart = _TeraWLinkIPRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 14, 1, 1),
    _TeraWLinkIPRangeStart_Type()
)
teraWLinkIPRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraWLinkIPRangeStart.setStatus("mandatory")
_TeraWLinkIPRangeEnd_Type = IpAddress
_TeraWLinkIPRangeEnd_Object = MibTableColumn
teraWLinkIPRangeEnd = _TeraWLinkIPRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 14, 1, 2),
    _TeraWLinkIPRangeEnd_Type()
)
teraWLinkIPRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraWLinkIPRangeEnd.setStatus("mandatory")


class _TeraWLinkIPRangeRowStatus_Type(Integer32):
    """Custom type teraWLinkIPRangeRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_TeraWLinkIPRangeRowStatus_Type.__name__ = "Integer32"
_TeraWLinkIPRangeRowStatus_Object = MibTableColumn
teraWLinkIPRangeRowStatus = _TeraWLinkIPRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 14, 1, 3),
    _TeraWLinkIPRangeRowStatus_Type()
)
teraWLinkIPRangeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraWLinkIPRangeRowStatus.setStatus("mandatory")
_TeraSecondaryMasterSlaveTable_ObjectIdentity = ObjectIdentity
teraSecondaryMasterSlaveTable = _TeraSecondaryMasterSlaveTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 16)
)


class _TeraSecondaryMasterSlotNumber_Type(Integer32):
    """Custom type teraSecondaryMasterSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraSecondaryMasterSlotNumber_Type.__name__ = "Integer32"
_TeraSecondaryMasterSlotNumber_Object = MibScalar
teraSecondaryMasterSlotNumber = _TeraSecondaryMasterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 16, 1),
    _TeraSecondaryMasterSlotNumber_Type()
)
teraSecondaryMasterSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSecondaryMasterSlotNumber.setStatus("mandatory")


class _TeraSecondarySlaveSlotNumber_Type(Integer32):
    """Custom type teraSecondarySlaveSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraSecondarySlaveSlotNumber_Type.__name__ = "Integer32"
_TeraSecondarySlaveSlotNumber_Object = MibScalar
teraSecondarySlaveSlotNumber = _TeraSecondarySlaveSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 16, 2),
    _TeraSecondarySlaveSlotNumber_Type()
)
teraSecondarySlaveSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSecondarySlaveSlotNumber.setStatus("mandatory")
_TeraMasterSlaveStateTable_Object = MibTable
teraMasterSlaveStateTable = _TeraMasterSlaveStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 17)
)
if mibBuilder.loadTexts:
    teraMasterSlaveStateTable.setStatus("mandatory")
_TeraMasterSlaveStateTableEntry_Object = MibTableRow
teraMasterSlaveStateTableEntry = _TeraMasterSlaveStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 17, 1)
)
teraMasterSlaveStateTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraMasterSlaveStateIndex"),
)
if mibBuilder.loadTexts:
    teraMasterSlaveStateTableEntry.setStatus("mandatory")


class _TeraMasterSlaveStateIndex_Type(Integer32):
    """Custom type teraMasterSlaveStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TeraMasterSlaveStateIndex_Type.__name__ = "Integer32"
_TeraMasterSlaveStateIndex_Object = MibTableColumn
teraMasterSlaveStateIndex = _TeraMasterSlaveStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 17, 1, 1),
    _TeraMasterSlaveStateIndex_Type()
)
teraMasterSlaveStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraMasterSlaveStateIndex.setStatus("mandatory")


class _TeraMasterState_Type(Integer32):
    """Custom type teraMasterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("nobody", 1),
          ("unknown", 0))
    )


_TeraMasterState_Type.__name__ = "Integer32"
_TeraMasterState_Object = MibTableColumn
teraMasterState = _TeraMasterState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 17, 1, 2),
    _TeraMasterState_Type()
)
teraMasterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraMasterState.setStatus("mandatory")


class _TeraSlaveState_Type(Integer32):
    """Custom type teraSlaveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("nobody", 1),
          ("slave", 3),
          ("slaveActive", 4),
          ("slaveFail", 5),
          ("unknown", 0))
    )


_TeraSlaveState_Type.__name__ = "Integer32"
_TeraSlaveState_Object = MibTableColumn
teraSlaveState = _TeraSlaveState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 17, 1, 3),
    _TeraSlaveState_Type()
)
teraSlaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSlaveState.setStatus("mandatory")
_TeraPPPBaudRateTbl_ObjectIdentity = ObjectIdentity
teraPPPBaudRateTbl = _TeraPPPBaudRateTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 20)
)
_TeraPPPBaudRateTable_ObjectIdentity = ObjectIdentity
teraPPPBaudRateTable = _TeraPPPBaudRateTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 20, 1)
)


class _TeraPPPAdminBaudRate_Type(Integer32):
    """Custom type teraPPPAdminBaudRate based on Integer32"""
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
        *(("baud115200", 6),
          ("baud19200", 3),
          ("baud230400", 7),
          ("baud2400", 0),
          ("baud38400", 4),
          ("baud4800", 1),
          ("baud57600", 5),
          ("baud9600", 2))
    )


_TeraPPPAdminBaudRate_Type.__name__ = "Integer32"
_TeraPPPAdminBaudRate_Object = MibScalar
teraPPPAdminBaudRate = _TeraPPPAdminBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 20, 1, 1),
    _TeraPPPAdminBaudRate_Type()
)
teraPPPAdminBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraPPPAdminBaudRate.setStatus("mandatory")


class _TeraPPPOperBaudRate_Type(Integer32):
    """Custom type teraPPPOperBaudRate based on Integer32"""
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
        *(("baud115200", 6),
          ("baud19200", 3),
          ("baud230400", 7),
          ("baud2400", 0),
          ("baud38400", 4),
          ("baud4800", 1),
          ("baud57600", 5),
          ("baud9600", 2))
    )


_TeraPPPOperBaudRate_Type.__name__ = "Integer32"
_TeraPPPOperBaudRate_Object = MibScalar
teraPPPOperBaudRate = _TeraPPPOperBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 20, 1, 2),
    _TeraPPPOperBaudRate_Type()
)
teraPPPOperBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraPPPOperBaudRate.setStatus("mandatory")


class _TeraPPPAdminFlowControl_Type(Integer32):
    """Custom type teraPPPAdminFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rTS-CTS", 2),
          ("xon-Xoff", 1))
    )


_TeraPPPAdminFlowControl_Type.__name__ = "Integer32"
_TeraPPPAdminFlowControl_Object = MibScalar
teraPPPAdminFlowControl = _TeraPPPAdminFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 20, 1, 3),
    _TeraPPPAdminFlowControl_Type()
)
teraPPPAdminFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraPPPAdminFlowControl.setStatus("mandatory")


class _TeraPPPOperFlowControl_Type(Integer32):
    """Custom type teraPPPOperFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rTS-CTS", 2),
          ("xon-Xoff", 1))
    )


_TeraPPPOperFlowControl_Type.__name__ = "Integer32"
_TeraPPPOperFlowControl_Object = MibScalar
teraPPPOperFlowControl = _TeraPPPOperFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 20, 1, 4),
    _TeraPPPOperFlowControl_Type()
)
teraPPPOperFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraPPPOperFlowControl.setStatus("mandatory")
_TeraSystemNATGroupTable_ObjectIdentity = ObjectIdentity
teraSystemNATGroupTable = _TeraSystemNATGroupTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 24)
)
_TeraSystemNATSubnetAddress_Type = IpAddress
_TeraSystemNATSubnetAddress_Object = MibScalar
teraSystemNATSubnetAddress = _TeraSystemNATSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 24, 1),
    _TeraSystemNATSubnetAddress_Type()
)
teraSystemNATSubnetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNATSubnetAddress.setStatus("mandatory")
_TeraSystemNATSubnetMask_Type = IpAddress
_TeraSystemNATSubnetMask_Object = MibScalar
teraSystemNATSubnetMask = _TeraSystemNATSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 24, 2),
    _TeraSystemNATSubnetMask_Type()
)
teraSystemNATSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNATSubnetMask.setStatus("mandatory")
_TeraSystemPCUNumTable_ObjectIdentity = ObjectIdentity
teraSystemPCUNumTable = _TeraSystemPCUNumTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 25)
)


class _TeraSystemNumOfPCU_Type(Integer32):
    """Custom type teraSystemNumOfPCU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pCU4", 0),
          ("pCU5", 1))
    )


_TeraSystemNumOfPCU_Type.__name__ = "Integer32"
_TeraSystemNumOfPCU_Object = MibScalar
teraSystemNumOfPCU = _TeraSystemNumOfPCU_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 25, 1),
    _TeraSystemNumOfPCU_Type()
)
teraSystemNumOfPCU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSystemNumOfPCU.setStatus("mandatory")
_TeraInstalledSystemInfoTable_Object = MibTable
teraInstalledSystemInfoTable = _TeraInstalledSystemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 26)
)
if mibBuilder.loadTexts:
    teraInstalledSystemInfoTable.setStatus("mandatory")
_TeraInstalledSystemInfoTableEntry_Object = MibTableRow
teraInstalledSystemInfoTableEntry = _TeraInstalledSystemInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 26, 1)
)
teraInstalledSystemInfoTableEntry.setIndexNames(
    (0, "TERAWAVE-terasystem-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-terasystem-MIB", "teraPonIndex"),
)
if mibBuilder.loadTexts:
    teraInstalledSystemInfoTableEntry.setStatus("mandatory")
_TeraInstalledSystemName_Type = OctetString
_TeraInstalledSystemName_Object = MibTableColumn
teraInstalledSystemName = _TeraInstalledSystemName_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 26, 1, 1),
    _TeraInstalledSystemName_Type()
)
teraInstalledSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraInstalledSystemName.setStatus("mandatory")
_TeraInstalledSystemLocation_Type = OctetString
_TeraInstalledSystemLocation_Object = MibTableColumn
teraInstalledSystemLocation = _TeraInstalledSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 26, 1, 2),
    _TeraInstalledSystemLocation_Type()
)
teraInstalledSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraInstalledSystemLocation.setStatus("mandatory")


class _TeraInstalledNEType_Type(Integer32):
    """Custom type teraInstalledNEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("oat", 7),
          ("tw100", 4),
          ("tw150RT", 5),
          ("tw1600", 3),
          ("tw300", 1),
          ("tw600", 2),
          ("unknown", 0))
    )


_TeraInstalledNEType_Type.__name__ = "Integer32"
_TeraInstalledNEType_Object = MibTableColumn
teraInstalledNEType = _TeraInstalledNEType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 26, 1, 3),
    _TeraInstalledNEType_Type()
)
teraInstalledNEType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraInstalledNEType.setStatus("mandatory")
_TeraCraftInterfaceGroup_ObjectIdentity = ObjectIdentity
teraCraftInterfaceGroup = _TeraCraftInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 28)
)
_TeraCraftInterfaceTable_ObjectIdentity = ObjectIdentity
teraCraftInterfaceTable = _TeraCraftInterfaceTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 5, 28, 1)
)


class _TeraCraftPortStat_Type(Integer32):
    """Custom type teraCraftPortStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TeraCraftPortStat_Type.__name__ = "Integer32"
_TeraCraftPortStat_Object = MibScalar
teraCraftPortStat = _TeraCraftPortStat_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 28, 1, 1),
    _TeraCraftPortStat_Type()
)
teraCraftPortStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCraftPortStat.setStatus("mandatory")


class _TeraCraftDefaultAddrStat_Type(Integer32):
    """Custom type teraCraftDefaultAddrStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TeraCraftDefaultAddrStat_Type.__name__ = "Integer32"
_TeraCraftDefaultAddrStat_Object = MibScalar
teraCraftDefaultAddrStat = _TeraCraftDefaultAddrStat_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 28, 1, 2),
    _TeraCraftDefaultAddrStat_Type()
)
teraCraftDefaultAddrStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCraftDefaultAddrStat.setStatus("mandatory")


class _TeraSNMPState_Type(Integer32):
    """Custom type teraSNMPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 2),
          ("ready", 1))
    )


_TeraSNMPState_Type.__name__ = "Integer32"
_TeraSNMPState_Object = MibScalar
teraSNMPState = _TeraSNMPState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 5, 28, 1, 3),
    _TeraSNMPState_Type()
)
teraSNMPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSNMPState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-terasystem-MIB",
    **{"terawave": terawave,
       "teraSystem": teraSystem,
       "teraSystemTime": teraSystemTime,
       "teraSystemCurrTime": teraSystemCurrTime,
       "teraSlotInstTablePar": teraSlotInstTablePar,
       "teraSlotInstallTable": teraSlotInstallTable,
       "teraSlotInstallTableEntry": teraSlotInstallTableEntry,
       "teraInstallSlotNumber": teraInstallSlotNumber,
       "teraInstallUnitType": teraInstallUnitType,
       "teraInstallEquippedUnitType": teraInstallEquippedUnitType,
       "teraInstallUnitAdminStatus": teraInstallUnitAdminStatus,
       "teraInstallUnitOperStatus": teraInstallUnitOperStatus,
       "teraInstallUnitName": teraInstallUnitName,
       "teraInstallUnitRevision": teraInstallUnitRevision,
       "teraInstallUnitSerial": teraInstallUnitSerial,
       "teraInstallUnitSWVersion": teraInstallUnitSWVersion,
       "teraInstallUnitMfgData": teraInstallUnitMfgData,
       "teraSystemInstallTable": teraSystemInstallTable,
       "teraSystemInstallTableEntry": teraSystemInstallTableEntry,
       "teraSystemNEProvisionAdminStatus": teraSystemNEProvisionAdminStatus,
       "teraSystemNEName": teraSystemNEName,
       "teraSystemNERangingCode": teraSystemNERangingCode,
       "teraSystemNEType": teraSystemNEType,
       "teraSystemNEMaxLatency": teraSystemNEMaxLatency,
       "teraSystemNEAponMaxLength": teraSystemNEAponMaxLength,
       "teraSystemNEOperStatus": teraSystemNEOperStatus,
       "teraSystemNEEocMinBandWidth": teraSystemNEEocMinBandWidth,
       "teraSystemNEEocMaxBandWidth": teraSystemNEEocMaxBandWidth,
       "teraSystemNEInventoryOverride": teraSystemNEInventoryOverride,
       "teraSystemNERanging": teraSystemNERanging,
       "teraSystemNECurrentDistance": teraSystemNECurrentDistance,
       "teraNEInfoTableGroup": teraNEInfoTableGroup,
       "teraNEInfoTable": teraNEInfoTable,
       "teraNERangingCode": teraNERangingCode,
       "teraNEType": teraNEType,
       "teraNEModel": teraNEModel,
       "teraNESWVersion": teraNESWVersion,
       "teraNESWRevision": teraNESWRevision,
       "teraClockSyncTable": teraClockSyncTable,
       "teraClockSyncPrimarySource": teraClockSyncPrimarySource,
       "teraClockSyncPrimaryNIMSlot": teraClockSyncPrimaryNIMSlot,
       "teraClockSyncPrimaryNIMIfIndex": teraClockSyncPrimaryNIMIfIndex,
       "teraClockSyncSecondarySource": teraClockSyncSecondarySource,
       "teraClockSyncSecondaryNIMSlot": teraClockSyncSecondaryNIMSlot,
       "teraClockSyncSecondaryNIMIfIndex": teraClockSyncSecondaryNIMIfIndex,
       "teraClockSyncLastSource": teraClockSyncLastSource,
       "teraClockSyncRevertive": teraClockSyncRevertive,
       "teraClockSyncActiveSource": teraClockSyncActiveSource,
       "teraClockSyncActiveNIMSlot": teraClockSyncActiveNIMSlot,
       "teraClockSyncActiveNIMIfIndex": teraClockSyncActiveNIMIfIndex,
       "teraClockSyncActiveStatus": teraClockSyncActiveStatus,
       "teraClockSyncPrimaryStatus": teraClockSyncPrimaryStatus,
       "teraClockSyncSecondaryStatus": teraClockSyncSecondaryStatus,
       "teraClockSyncOperStatus": teraClockSyncOperStatus,
       "teraCommunityGroupTable": teraCommunityGroupTable,
       "teraPublicCommunity": teraPublicCommunity,
       "teraSETCommunity": teraSETCommunity,
       "teraGETCommunity": teraGETCommunity,
       "teraAdminCommunity": teraAdminCommunity,
       "teraTestCommunity": teraTestCommunity,
       "teraMasterSlaveTable": teraMasterSlaveTable,
       "teraMasterSlotNumber": teraMasterSlotNumber,
       "teraSlaveSlotNumber": teraSlaveSlotNumber,
       "teraSystemIPGroupTable": teraSystemIPGroupTable,
       "teraSystemIPAddress": teraSystemIPAddress,
       "teraSystemIPNetMask": teraSystemIPNetMask,
       "teraSystemIPGateway": teraSystemIPGateway,
       "teraLogGroup": teraLogGroup,
       "teraLogNumberTable": teraLogNumberTable,
       "teraLogNumberTableEntry": teraLogNumberTableEntry,
       "teraLogNumber": teraLogNumber,
       "teraLogNumberDescr": teraLogNumberDescr,
       "teraLogNumberStatus": teraLogNumberStatus,
       "teraLogClear": teraLogClear,
       "teraLogTable": teraLogTable,
       "teraLogTableEntry": teraLogTableEntry,
       "teraLogMsgIndex": teraLogMsgIndex,
       "teraLogMsgNumber": teraLogMsgNumber,
       "teraLogNumberOfParams": teraLogNumberOfParams,
       "teraLogParams": teraLogParams,
       "teraLogStatus": teraLogStatus,
       "teraAllLogsFilterGroup": teraAllLogsFilterGroup,
       "teraAllLogsFilterGroupEntry": teraAllLogsFilterGroupEntry,
       "teraLogFilterByNumber": teraLogFilterByNumber,
       "teraLogFilterBySize": teraLogFilterBySize,
       "teraLogFilterBySeverity": teraLogFilterBySeverity,
       "teraLogFilterByTask": teraLogFilterByTask,
       "teraNESlotTable": teraNESlotTable,
       "teraNESlotTableEntry": teraNESlotTableEntry,
       "teraNESlotUnitType": teraNESlotUnitType,
       "teraNESlotUnitAdminStatus": teraNESlotUnitAdminStatus,
       "teraWLinkIPTable": teraWLinkIPTable,
       "teraWLinkIPTableEntry": teraWLinkIPTableEntry,
       "teraWLinkIPAddress": teraWLinkIPAddress,
       "teraWLinkIPNetMask": teraWLinkIPNetMask,
       "teraWLinkIPGateway": teraWLinkIPGateway,
       "teraWLinkIPStatus": teraWLinkIPStatus,
       "teraNEMiscTableGroup": teraNEMiscTableGroup,
       "teraNEMiscTable": teraNEMiscTable,
       "teraNELevel2Slot": teraNELevel2Slot,
       "teraNEZipSystem": teraNEZipSystem,
       "teraNEReset": teraNEReset,
       "teraNETimeZone": teraNETimeZone,
       "teraNEInventoryOverride": teraNEInventoryOverride,
       "teraNESerialPortType": teraNESerialPortType,
       "teraSysObjectIdTable": teraSysObjectIdTable,
       "teraTW300": teraTW300,
       "teraTW600": teraTW600,
       "teraTW1600": teraTW1600,
       "teraTW100": teraTW100,
       "teraTW150RTATM": teraTW150RTATM,
       "teraTW150RTTDM": teraTW150RTTDM,
       "teraOAT": teraOAT,
       "teraNEIDxTable": teraNEIDxTable,
       "teraNEIDxTableEntry": teraNEIDxTableEntry,
       "teraNEIDxSlotLevel1": teraNEIDxSlotLevel1,
       "teraNEIDxPonID": teraNEIDxPonID,
       "teraWLinkIPRangeTable": teraWLinkIPRangeTable,
       "teraWLinkIPRangeTableEntry": teraWLinkIPRangeTableEntry,
       "teraWLinkIPRangeStart": teraWLinkIPRangeStart,
       "teraWLinkIPRangeEnd": teraWLinkIPRangeEnd,
       "teraWLinkIPRangeRowStatus": teraWLinkIPRangeRowStatus,
       "teraSecondaryMasterSlaveTable": teraSecondaryMasterSlaveTable,
       "teraSecondaryMasterSlotNumber": teraSecondaryMasterSlotNumber,
       "teraSecondarySlaveSlotNumber": teraSecondarySlaveSlotNumber,
       "teraMasterSlaveStateTable": teraMasterSlaveStateTable,
       "teraMasterSlaveStateTableEntry": teraMasterSlaveStateTableEntry,
       "teraMasterSlaveStateIndex": teraMasterSlaveStateIndex,
       "teraMasterState": teraMasterState,
       "teraSlaveState": teraSlaveState,
       "teraPPPBaudRateTbl": teraPPPBaudRateTbl,
       "teraPPPBaudRateTable": teraPPPBaudRateTable,
       "teraPPPAdminBaudRate": teraPPPAdminBaudRate,
       "teraPPPOperBaudRate": teraPPPOperBaudRate,
       "teraPPPAdminFlowControl": teraPPPAdminFlowControl,
       "teraPPPOperFlowControl": teraPPPOperFlowControl,
       "teraSystemNATGroupTable": teraSystemNATGroupTable,
       "teraSystemNATSubnetAddress": teraSystemNATSubnetAddress,
       "teraSystemNATSubnetMask": teraSystemNATSubnetMask,
       "teraSystemPCUNumTable": teraSystemPCUNumTable,
       "teraSystemNumOfPCU": teraSystemNumOfPCU,
       "teraInstalledSystemInfoTable": teraInstalledSystemInfoTable,
       "teraInstalledSystemInfoTableEntry": teraInstalledSystemInfoTableEntry,
       "teraInstalledSystemName": teraInstalledSystemName,
       "teraInstalledSystemLocation": teraInstalledSystemLocation,
       "teraInstalledNEType": teraInstalledNEType,
       "teraCraftInterfaceGroup": teraCraftInterfaceGroup,
       "teraCraftInterfaceTable": teraCraftInterfaceTable,
       "teraCraftPortStat": teraCraftPortStat,
       "teraCraftDefaultAddrStat": teraCraftDefaultAddrStat,
       "teraSNMPState": teraSNMPState}
)
